import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import Anthropic from '@anthropic-ai/sdk';
import { createClient } from '@supabase/supabase-js';
import { config } from 'dotenv';

config();

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const isProd = process.env.NODE_ENV === 'production';

const app = express();
app.use(cors());
app.use(express.json({ limit: '200kb' }));

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

/* ── Supabase (service role — bypasses RLS, server-side only) ── */
const supabaseAdmin = createClient(
  process.env.VITE_SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY,
  { auth: { autoRefreshToken: false, persistSession: false } }
);

async function getAuthenticatedUser(req) {
  const authHeader = req.headers.authorization || '';
  const token = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : null;
  if (!token) return null;
  const { data, error } = await supabaseAdmin.auth.getUser(token);
  if (error || !data?.user) return null;
  return data.user;
}

async function markUserPaid(userId) {
  await supabaseAdmin
    .from('profils_utilisateurs')
    .upsert({ user_id: userId, crpe_paid: true, paid_at: new Date().toISOString() }, { onConflict: 'user_id' });
}

/* ── PayPal ── */
const PAYPAL_API_BASE = process.env.PAYPAL_ENV === 'live'
  ? 'https://api-m.paypal.com'
  : 'https://api-m.sandbox.paypal.com';
const CRPE_PRICE = { currency_code: 'EUR', value: '399.00' };

async function getPaypalAccessToken() {
  const auth = Buffer.from(`${process.env.PAYPAL_CLIENT_ID}:${process.env.PAYPAL_CLIENT_SECRET}`).toString('base64');
  const res = await fetch(`${PAYPAL_API_BASE}/v1/oauth2/token`, {
    method: 'POST',
    headers: { Authorization: `Basic ${auth}`, 'Content-Type': 'application/x-www-form-urlencoded' },
    body: 'grant_type=client_credentials',
  });
  if (!res.ok) throw new Error(`PayPal auth failed: ${res.status}`);
  const json = await res.json();
  return json.access_token;
}

app.post('/api/paypal/create-order', async (req, res) => {
  try {
    const user = await getAuthenticatedUser(req);
    if (!user) return res.status(401).json({ error: 'Non authentifié' });

    const accessToken = await getPaypalAccessToken();
    const orderRes = await fetch(`${PAYPAL_API_BASE}/v2/checkout/orders`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        intent: 'CAPTURE',
        purchase_units: [{
          custom_id: user.id,
          description: 'Accès complet PassCRPE',
          amount: CRPE_PRICE,
        }],
      }),
    });
    const order = await orderRes.json();
    if (!orderRes.ok) throw new Error(order.message || 'Erreur PayPal');
    res.json({ id: order.id });
  } catch (err) {
    console.error('[PayPal create-order]', err.message);
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/paypal/capture-order', async (req, res) => {
  try {
    const user = await getAuthenticatedUser(req);
    if (!user) return res.status(401).json({ error: 'Non authentifié' });
    const { orderID } = req.body;
    if (!orderID) return res.status(400).json({ error: 'orderID manquant' });

    const accessToken = await getPaypalAccessToken();
    const captureRes = await fetch(`${PAYPAL_API_BASE}/v2/checkout/orders/${orderID}/capture`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
    });
    const capture = await captureRes.json();
    if (!captureRes.ok) throw new Error(capture.message || 'Erreur de capture PayPal');

    const customId = capture.purchase_units?.[0]?.payments?.captures?.[0]?.custom_id;
    if (capture.status === 'COMPLETED' && customId === user.id) {
      await markUserPaid(user.id);
    }
    res.json({ status: capture.status });
  } catch (err) {
    console.error('[PayPal capture-order]', err.message);
    res.status(500).json({ error: err.message });
  }
});

/* ── PayPal webhook — source de vérité, indépendante du parcours client ── */
app.post('/api/webhook/paypal', async (req, res) => {
  try {
    const accessToken = await getPaypalAccessToken();
    const verifyRes = await fetch(`${PAYPAL_API_BASE}/v1/notifications/verify-webhook-signature`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        transmission_id: req.headers['paypal-transmission-id'],
        transmission_time: req.headers['paypal-transmission-time'],
        cert_url: req.headers['paypal-cert-url'],
        auth_algo: req.headers['paypal-auth-algo'],
        transmission_sig: req.headers['paypal-transmission-sig'],
        webhook_id: process.env.PAYPAL_WEBHOOK_ID,
        webhook_event: req.body,
      }),
    });
    const verification = await verifyRes.json();
    if (verification.verification_status !== 'SUCCESS') {
      console.warn('[PayPal webhook] signature invalide', verification);
      return res.status(400).json({ error: 'Signature invalide' });
    }

    const event = req.body;
    if (event.event_type === 'PAYMENT.CAPTURE.COMPLETED') {
      const customId = event.resource?.custom_id;
      if (customId) await markUserPaid(customId);
    }
    res.status(200).json({ received: true });
  } catch (err) {
    console.error('[PayPal webhook]', err.message);
    res.status(500).json({ error: err.message });
  }
});

/* ── API ── */
async function logConsommation({ meta, model, usage, dureeMs, success }) {
  if (!meta?.user_id) return;
  try {
    await supabaseAdmin.from('consommation_utilisateurs').insert({
      user_id: meta.user_id,
      session_id: meta.session_id || null,
      type_evenement: meta.type_evenement || 'chat',
      matiere: meta.matiere || null,
      thematique: meta.thematique || null,
      client_ref_id: meta.client_ref_id || null,
      id_question_generee: meta.id_question_generee || null,
      model,
      input_tokens: usage?.input_tokens || 0,
      output_tokens: usage?.output_tokens || 0,
      cache_read_input_tokens: usage?.cache_read_input_tokens || 0,
      cache_creation_input_tokens: usage?.cache_creation_input_tokens || 0,
      duree_ms: dureeMs,
      success,
    });
  } catch (e) {
    console.warn('[consommation] insert échouée', e.message);
  }
}

const CHAT_MODEL = 'claude-sonnet-4-6';

app.post('/api/chat', async (req, res) => {
  const { messages, system, meta } = req.body;
  const startedAt = Date.now();

  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  try {
    const stream = client.messages.stream({
      model: CHAT_MODEL,
      max_tokens: 2000,
      system: [{ type: 'text', text: system, cache_control: { type: 'ephemeral' } }],
      messages,
    });

    stream.on('text', (text) => {
      res.write(`data: ${JSON.stringify({ text })}\n\n`);
    });

    const finalMsg = await stream.finalMessage();
    res.write('data: [DONE]\n\n');
    res.end();
    logConsommation({ meta, model: finalMsg.model, usage: finalMsg.usage, dureeMs: Date.now() - startedAt, success: true });
  } catch (err) {
    console.error('[API error]', err.message);
    res.write(`data: ${JSON.stringify({ error: err.message })}\n\n`);
    res.write('data: [DONE]\n\n');
    res.end();
    logConsommation({ meta, model: CHAT_MODEL, usage: null, dureeMs: Date.now() - startedAt, success: false });
  }
});

/* ── Static (dev local uniquement — sur Vercel ces fichiers sont servis directement depuis dist/) ── */
app.use(express.static(path.join(__dirname, 'landing')));

if (isProd) {
  app.use('/app', express.static(path.join(__dirname, 'dist/app')));
  app.get('/app/*', (_, res) =>
    res.sendFile(path.join(__dirname, 'dist/app/index.html'))
  );
}

app.get('/', (_, res) =>
  res.sendFile(path.join(__dirname, 'landing/index.html'))
);

export default app;

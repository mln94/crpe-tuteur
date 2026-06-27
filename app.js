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

/* ── Klaviyo ── */
const KLAVIYO_API_BASE      = 'https://a.klaviyo.com/api';
const KLAVIYO_LIST_NEWSLETTER = 'U97rGQ';
const KLAVIYO_LIST_SIGNUP     = 'SgJQyM';
const KLAVIYO_REVISION      = '2026-04-15';

function klaviyoHeaders() {
  return {
    'Authorization': `Klaviyo-API-Key ${process.env.KLAVIYO_PRIVATE_API_KEY}`,
    'accept': 'application/vnd.api+json',
    'content-type': 'application/vnd.api+json',
    'revision': KLAVIYO_REVISION,
  };
}

async function klaviyoSubscribePipeline(email, prenom, nom, listId, properties = {}) {
  // 1. Créer le profil (ou récupérer l'ID existant en cas de 409)
  const profileRes = await fetch(`${KLAVIYO_API_BASE}/profiles`, {
    method: 'POST',
    headers: klaviyoHeaders(),
    body: JSON.stringify({
      data: {
        type: 'profile',
        attributes: { email, first_name: prenom, last_name: nom, ...(Object.keys(properties).length ? { properties } : {}) },
      },
    }),
  });
  let profileId;
  if (profileRes.status === 409) {
    const dup = await profileRes.json();
    profileId = dup.errors?.[0]?.meta?.duplicate_profile_id;
    if (!profileId) throw new Error('Profil en double sans ID récupérable.');
  } else if (profileRes.ok) {
    profileId = (await profileRes.json()).data?.id;
  } else {
    const err = await profileRes.json();
    throw new Error(err.errors?.[0]?.detail || `Erreur création profil: ${profileRes.status}`);
  }

  // 2. Ajouter le profil à la liste
  const listRes = await fetch(`${KLAVIYO_API_BASE}/lists/${listId}/relationships/profiles`, {
    method: 'POST',
    headers: klaviyoHeaders(),
    body: JSON.stringify({ data: [{ type: 'profile', id: profileId }] }),
  });
  if (!listRes.ok && listRes.status !== 409) {
    const err = await listRes.json();
    throw new Error(err.errors?.[0]?.detail || `Erreur ajout à la liste: ${listRes.status}`);
  }

  // 3. Consentement e-mail marketing
  const consentRes = await fetch(`${KLAVIYO_API_BASE}/profile-subscription-bulk-create-jobs`, {
    method: 'POST',
    headers: klaviyoHeaders(),
    body: JSON.stringify({
      data: {
        type: 'profile-subscription-bulk-create-job',
        attributes: {
          profiles: {
            data: [{
              type: 'profile',
              attributes: {
                email,
                subscriptions: { email: { marketing: { consent: 'SUBSCRIBED' } } },
              },
            }],
          },
          historical_import: false,
        },
        relationships: { list: { data: { type: 'list', id: listId } } },
      },
    }),
  });
  if (!consentRes.ok) {
    const err = await consentRes.json();
    throw new Error(err.errors?.[0]?.detail || `Erreur consentement: ${consentRes.status}`);
  }
}

function klaviyoGuard(res) {
  if (!process.env.KLAVIYO_PRIVATE_API_KEY) {
    console.error('[Klaviyo] KLAVIYO_PRIVATE_API_KEY manquante');
    res.status(500).json({ error: 'Configuration serveur incomplète.' });
    return false;
  }
  return true;
}

app.post('/api/newsletter/subscribe', async (req, res) => {
  if (!klaviyoGuard(res)) return;
  const { prenom, nom, email } = req.body || {};
  if (!prenom || !nom || !email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))
    return res.status(400).json({ error: 'Données invalides.' });
  try {
    await klaviyoSubscribePipeline(email, prenom, nom, KLAVIYO_LIST_NEWSLETTER);
    res.json({ ok: true });
  } catch (err) {
    console.error('[Klaviyo newsletter]', err.message);
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/klaviyo/signup', async (req, res) => {
  if (!klaviyoGuard(res)) return;
  const { prenom, nom, email, user_id } = req.body || {};
  if (!prenom || !nom || !email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))
    return res.status(400).json({ error: 'Données invalides.' });
  try {
    await klaviyoSubscribePipeline(email, prenom, nom, KLAVIYO_LIST_SIGNUP, { email_verified: false, trial: true, paid_user: false, form_trial: false });

    // Créer la ligne profil Supabase avec trial = true
    if (user_id) {
      await supabaseAdmin
        .from('profils_utilisateurs')
        .upsert({ user_id, trial: true }, { onConflict: 'user_id', ignoreDuplicates: true });
    }

    res.json({ ok: true });
  } catch (err) {
    console.error('[Klaviyo signup]', err.message);
    res.status(500).json({ error: err.message });
  }
});

/* ── Klaviyo : passer email_verified à true pour un email donné ── */
async function klaviyoSetEmailVerified(email) {
  const searchRes = await fetch(
    `${KLAVIYO_API_BASE}/profiles/?filter=equals(email,"${encodeURIComponent(email)}")`,
    { headers: klaviyoHeaders() }
  );
  const searchData = await searchRes.json();
  const profileId  = searchData.data?.[0]?.id;
  if (!profileId) {
    console.warn(`[Klaviyo] Profil introuvable pour ${email}`);
    return;
  }
  const patchRes = await fetch(`${KLAVIYO_API_BASE}/profiles/${profileId}`, {
    method: 'PATCH',
    headers: klaviyoHeaders(),
    body: JSON.stringify({
      data: { type: 'profile', id: profileId, attributes: { properties: { email_verified: true } } },
    }),
  });
  if (!patchRes.ok) {
    const err = await patchRes.json();
    throw new Error(err.errors?.[0]?.detail || `Erreur PATCH profil: ${patchRes.status}`);
  }
  console.log(`[Klaviyo] email_verified=true pour ${email}`);
}

/* ── Route : confirmation e-mail depuis le front (access_token dans le hash) ─
   Valide le token côté serveur via Supabase Admin pour ne jamais exposer
   la clé Klaviyo au navigateur.
─────────────────────────────────────────────────────────────────────────── */
app.post('/api/klaviyo/email-verified', async (req, res) => {
  const { access_token } = req.body || {};
  if (!access_token) return res.status(400).json({ error: 'Token manquant.' });
  try {
    const { data, error } = await supabaseAdmin.auth.getUser(access_token);
    if (error || !data?.user) return res.status(401).json({ error: 'Token invalide.' });
    const email = data.user.email;
    if (!email) return res.status(400).json({ error: 'Email introuvable dans le token.' });
    await klaviyoSetEmailVerified(email);
    res.json({ ok: true });
  } catch (err) {
    console.error('[Klaviyo email-verified]', err.message);
    res.status(500).json({ error: err.message });
  }
});

/* ── Route : fin de période d'essai (10 questions atteintes) ── */
app.post('/api/klaviyo/trial-ended', async (req, res) => {
  const authHeader = req.headers.authorization || '';
  const token = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : null;
  if (!token) return res.status(401).json({ error: 'Token manquant.' });
  try {
    const { data, error } = await supabaseAdmin.auth.getUser(token);
    if (error || !data?.user) return res.status(401).json({ error: 'Token invalide.' });
    const { id: userId, email } = data.user;
    if (!email) return res.status(400).json({ error: 'Email introuvable dans le token.' });

    const now = new Date().toISOString();

    // Supabase : trial = false + trial_ended_at
    await supabaseAdmin
      .from('profils_utilisateurs')
      .upsert(
        { user_id: userId, trial: false, trial_ended_at: now },
        { onConflict: 'user_id' }
      );

    // Klaviyo : même mise à jour
    const searchRes = await fetch(
      `${KLAVIYO_API_BASE}/profiles/?filter=equals(email,"${encodeURIComponent(email)}")`,
      { headers: klaviyoHeaders() }
    );
    const searchData = await searchRes.json();
    const profileId  = searchData.data?.[0]?.id;
    if (!profileId) {
      console.warn(`[Klaviyo trial-ended] Profil introuvable pour ${email}`);
      return res.json({ ok: true, skipped: 'profil klaviyo introuvable' });
    }

    const patchRes = await fetch(`${KLAVIYO_API_BASE}/profiles/${profileId}`, {
      method: 'PATCH',
      headers: klaviyoHeaders(),
      body: JSON.stringify({
        data: {
          type: 'profile',
          id: profileId,
          attributes: { properties: { trial: false, date_trial_ended: now } },
        },
      }),
    });
    if (!patchRes.ok) {
      const err = await patchRes.json();
      throw new Error(err.errors?.[0]?.detail || `Erreur PATCH: ${patchRes.status}`);
    }
    console.log(`[trial-ended] trial=false pour ${email}`);
    res.json({ ok: true });
  } catch (err) {
    console.error('[Klaviyo trial-ended]', err.message);
    res.status(500).json({ error: err.message });
  }
});

/* ── Formulaire avis post-essai ── */
app.post('/api/feedback/trial', async (req, res) => {
  const {
    email, telephone, note_globale, peut_aider, pourquoi, plus_apprecie, moins_apprecie,
    exercices_attendus, corrections_utiles, manquait,
    calibrage_questions, frein_souscription, continuer, frein_continuer,
    recommander, autres_outils, lesquels_outils, suggestions,
  } = req.body || {};

  if (note_globale == null || !peut_aider)
    return res.status(400).json({ error: 'Champs obligatoires manquants.' });

  const { error } = await supabaseAdmin.from('avis_trial').insert({
    email:                email || null,
    telephone:            telephone || null,
    note_globale:         Number(note_globale),
    peut_aider,
    pourquoi:             pourquoi || null,
    plus_apprecie:        plus_apprecie || null,
    moins_apprecie:       moins_apprecie || null,
    exercices_attendus:   exercices_attendus || null,
    corrections_utiles:   corrections_utiles || null,
    manquait:             manquait || null,
    calibrage_questions:  calibrage_questions || null,
    frein_souscription:   frein_souscription || null,
    continuer:            continuer || null,
    frein_continuer:      frein_continuer || null,
    recommander:          recommander || null,
    autres_outils:        autres_outils || null,
    lesquels_outils:      lesquels_outils || null,
    suggestions:          suggestions || null,
  });

  if (error) {
    console.error('[feedback/trial]', error.message);
    return res.status(500).json({ error: error.message });
  }

  // Klaviyo : form_trial = true si on a l'email
  if (email) {
    try {
      const searchRes = await fetch(
        `${KLAVIYO_API_BASE}/profiles/?filter=equals(email,"${encodeURIComponent(email)}")`,
        { headers: klaviyoHeaders() }
      );
      const searchData = await searchRes.json();
      const profileId  = searchData.data?.[0]?.id;
      if (profileId) {
        await fetch(`${KLAVIYO_API_BASE}/profiles/${profileId}`, {
          method: 'PATCH',
          headers: klaviyoHeaders(),
          body: JSON.stringify({
            data: { type: 'profile', id: profileId, attributes: { properties: { form_trial: true } } },
          }),
        });
      }
    } catch (e) {
      console.warn('[feedback/trial] Klaviyo patch form_trial:', e.message);
    }
  }

  res.json({ ok: true });
});

/* ── Supabase Auth Webhook → Klaviyo email_verified ──────────────────────────
   Dashboard → Database → Webhooks → New webhook
     Table : auth.users   Events : UPDATE
     URL   : https://www.passcrpe.fr/api/webhook/supabase-auth
───────────────────────────────────────────────────────────────────────────── */
app.post('/api/webhook/supabase-auth', async (req, res) => {
  const { type, record, old_record } = req.body || {};
  if (type !== 'UPDATE') return res.json({ ignored: true });
  const wasVerified = !!old_record?.email_confirmed_at;
  const isVerified  = !!record?.email_confirmed_at;
  if (wasVerified || !isVerified) return res.json({ ignored: true });
  const email = record?.email;
  if (!email) return res.status(400).json({ error: 'Email manquant.' });
  try {
    await klaviyoSetEmailVerified(email);
    res.json({ ok: true });
  } catch (err) {
    console.error('[Klaviyo webhook]', err.message);
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

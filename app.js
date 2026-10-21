import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import Anthropic from '@anthropic-ai/sdk';
import { createClient } from '@supabase/supabase-js';
import { config } from 'dotenv';
import { createHash, randomBytes } from 'crypto';
import { registerEntraineurRoutes } from './entraineur/routes.js';

config();

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const isProd = process.env.NODE_ENV === 'production';

const app = express();
app.use(cors());
app.use(express.json({ limit: '200kb' }));

// Clés lues sans espaces, retours à la ligne ni guillemets copiés par erreur dans Vercel
const cleanKey = v => (v || '').trim().replace(/^["']+|["']+$/g, '').trim();
// Clé de l'application : ANTHROPIC_API_KEY_CRPE_APP (nom actuel dans Vercel), ANTHROPIC_API_KEY en secours
const APP_ANTHROPIC_KEY = cleanKey(process.env.ANTHROPIC_API_KEY_CRPE_APP) || cleanKey(process.env.ANTHROPIC_API_KEY);
if (!APP_ANTHROPIC_KEY) console.error('[config] ANTHROPIC_API_KEY_CRPE_APP manquante');
// Empreinte d'une clé pour les logs (début, fin, longueur) : jamais la clé entière
const keyFingerprint = k => (k ? `${k.slice(0, 14)}…${k.slice(-4)} (${k.length} caractères)` : 'absente');
console.log('[config] clé application :', keyFingerprint(APP_ANTHROPIC_KEY));
const client = new Anthropic({ apiKey: APP_ANTHROPIC_KEY });

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

async function markUserPaid(userId, email, ref) {
  await supabaseAdmin
    .from('profils_utilisateurs')
    .upsert({ user_id: userId, crpe_paid: true, paid_at: new Date().toISOString(), ...(ref ? { paypal_ref_passcrpe: ref } : {}) }, { onConflict: 'user_id' });

  // Klaviyo : paid_user = true — resynchronise même en flux webhook (pas d'email direct dans l'event PayPal)
  try {
    let resolvedEmail = email;
    if (!resolvedEmail) {
      const { data, error } = await supabaseAdmin.auth.admin.getUserById(userId);
      if (error) throw error;
      resolvedEmail = data?.user?.email;
    }
    if (resolvedEmail) await klaviyoSetPaidUser(resolvedEmail);
  } catch (err) {
    console.error('[markUserPaid] Klaviyo sync échouée (accès Supabase débloqué quand même) :', err.message);
  }
}

// Déblocage du Quiz CRPE (profils_utilisateurs.quizcrpe_paye) + Klaviyo quiz_paid ; appelée par la capture et par le webhook
async function markQuizPaid(userId, ref, email) {
  const { data: avant } = await supabaseAdmin.from('profils_utilisateurs').select('quizcrpe_paye, email').eq('user_id', userId).maybeSingle();
  if (avant?.quizcrpe_paye) return; // déjà débloqué (capture puis webhook pour le même paiement)
  const { error } = await supabaseAdmin.from('profils_utilisateurs')
    .upsert({ user_id: userId, quizcrpe_paye: true, quizcrpe_paye_at: new Date().toISOString(), paypal_ref_quizcrpe: ref || null }, { onConflict: 'user_id' });
  if (error) throw new Error(`Déblocage du quiz : ${error.message}`);
  quizOublier(userId);
  try {
    let e = email;
    if (!e) e = avant?.email;
    if (!e) { const { data } = await supabaseAdmin.auth.admin.getUserById(userId); e = data?.user?.email; }
    if (e) await klaviyoSetProperties(e, { quiz_paid: true, quiz_date_paid: new Date().toISOString() });
  } catch (err) {
    console.error('[markQuizPaid] Klaviyo sync échouée (accès débloqué quand même) :', err.message);
  }
}

/* ── PayPal ── */
// Forcé en live (le toggle via PAYPAL_ENV posait problème sur Vercel).
// Pour retester en sandbox : remplacer temporairement par 'https://api-m.sandbox.paypal.com'
// et utiliser les identifiants sandbox (PAYPAL_CLIENT_ID/SECRET) correspondants.
const PAYPAL_API_BASE = 'https://api-m.paypal.com';
const CRPE_PRICE = { currency_code: 'EUR', value: '360.00' }; // 360,00 € TTC (299,00 € HT)

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

    const captureTuteur = capture.purchase_units?.[0]?.payments?.captures?.[0];
    const customId = captureTuteur?.custom_id;
    if (capture.status === 'COMPLETED' && customId === user.id) {
      await markUserPaid(user.id, user.email, captureTuteur.id);
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
      // Paiements du quiz : custom_id « quiz:<id du compte> » ; sinon compte du tuteur IA
      if (customId?.startsWith('quiz:')) await markQuizPaid(customId.slice(5), event.resource?.id);
      else if (customId) await markUserPaid(customId, null, event.resource?.id);
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

// Propriétés Klaviyo « parcours_signup » (page de l'inscription) et « parcours_newsletter » (page de l'abonnement
// à la newsletter) : site PassCRPE ou page du quiz
const PARCOURS = new Set(['passcrpe', 'quizcrpe']);
const parcoursOf = v => (PARCOURS.has(v) ? v : 'passcrpe');

async function klaviyoSubscribePipeline(email, prenom, nom, listId, properties = {}, extraAttrs = {}, subscribeMarketing = true) {
  // 1. Créer le profil (ou récupérer l'ID existant en cas de 409)
  const profileRes = await fetch(`${KLAVIYO_API_BASE}/profiles`, {
    method: 'POST',
    headers: klaviyoHeaders(),
    body: JSON.stringify({
      data: {
        type: 'profile',
        attributes: {
          email, first_name: prenom, last_name: nom,
          ...extraAttrs,
          ...(Object.keys(properties).length ? { properties } : {}),
        },
      },
    }),
  });
  let profileId;
  if (profileRes.status === 409) {
    const dup = await profileRes.json();
    profileId = dup.errors?.[0]?.meta?.duplicate_profile_id;
    if (!profileId) throw new Error('Profil en double sans ID récupérable.');
    // Profil existant : seules les propriétés de parcours sont mises à jour (les autres propriétés ne sont pas écrasées)
    const parcoursProps = Object.fromEntries(['parcours_signup', 'parcours_newsletter'].filter(k => properties[k]).map(k => [k, properties[k]]));
    if (Object.keys(parcoursProps).length) {
      await fetch(`${KLAVIYO_API_BASE}/profiles/${profileId}`, {
        method: 'PATCH',
        headers: klaviyoHeaders(),
        body: JSON.stringify({ data: { type: 'profile', id: profileId, attributes: { properties: parcoursProps } } }),
      });
    }
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

  // 3. Consentement e-mail marketing (seulement si la personne l'a donné)
  if (!subscribeMarketing) return;
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
    await klaviyoSubscribePipeline(email, prenom, nom, KLAVIYO_LIST_NEWSLETTER, { parcours_newsletter: parcoursOf(req.body?.parcours) });
    res.json({ ok: true });
  } catch (err) {
    console.error('[Klaviyo newsletter]', err.message);
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/klaviyo/signup', async (req, res) => {
  if (!klaviyoGuard(res)) return;
  const { prenom, nom, email, user_id, telephone } = req.body || {};
  // Cases facultatives de l'inscription : l'abonnement aux e-mails marketing n'est fait qu'avec le consentement « conseils »
  const consent_conseils = req.body?.consent_conseils === true;
  const consent_partenaires = req.body?.consent_partenaires === true;
  if (!prenom || !nom || !email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))
    return res.status(400).json({ error: 'Données invalides.' });
  try {
    const phoneAttrs = telephone ? { phone_number: telephone } : {};
    await klaviyoSubscribePipeline(email, prenom, nom, KLAVIYO_LIST_SIGNUP,
      { email_verified: false, trial: true, paid_user: false, form_trial: false, consent_conseils, consent_partenaires, parcours_signup: parcoursOf(req.body?.parcours) },
      phoneAttrs, consent_conseils);
    // Newsletter : seuls les inscrits qui ont coché la case rejoignent la liste newsletter, et y sont abonnés
    // (consentement explicite exigé pour la prospection par e-mail)
    if (consent_conseils)
      await klaviyoSubscribePipeline(email, prenom, nom, KLAVIYO_LIST_NEWSLETTER, { parcours_newsletter: parcoursOf(req.body?.parcours) }, phoneAttrs, true);

    // Créer la ligne profil Supabase avec trial = true (un seul compte pour le tuteur IA et le quiz)
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

/* ── Klaviyo : newsletter à la confirmation de l'inscription ──
   Toutes les fenêtres d'inscription du site enregistrent la case « Je souhaite recevoir la newsletter PassCRPE »
   dans les métadonnées Supabase (consent_conseils). À la confirmation de l'e-mail, si la case est cochée,
   la personne est ajoutée à la liste newsletter et abonnée. Une seule fois par compte (newsletter_sync_at),
   pour ne jamais réabonner quelqu'un qui se serait désinscrit ensuite. */
async function klaviyoNewsletterDepuisInscription(user) {
  const meta = user.user_metadata || {};
  if (meta.consent_conseils !== true || meta.newsletter_sync_at) return;
  const prenom = meta.prenom || '', nom = meta.nom || '';
  await klaviyoSubscribePipeline(user.email, prenom, nom, KLAVIYO_LIST_NEWSLETTER, { parcours_signup: parcoursOf(meta.parcours), parcours_newsletter: parcoursOf(meta.parcours) });
  const { error } = await supabaseAdmin.auth.admin.updateUserById(user.id, { user_metadata: { ...meta, newsletter_sync_at: new Date().toISOString() } });
  if (error) console.error('[Klaviyo newsletter inscription] marque non enregistrée :', error.message);
  console.log(`[Klaviyo] newsletter : ${user.email} ajouté à la liste ${KLAVIYO_LIST_NEWSLETTER}`);
}

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

/* ── Klaviyo : mettre à jour des propriétés d'un profil (recherché par e-mail) ── */
async function klaviyoSetProperties(email, properties) {
  const searchRes = await fetch(`${KLAVIYO_API_BASE}/profiles/?filter=equals(email,"${encodeURIComponent(email)}")`, { headers: klaviyoHeaders() });
  const profileId = (await searchRes.json()).data?.[0]?.id;
  if (!profileId) { console.warn(`[Klaviyo] Profil introuvable pour ${email}`); return; }
  const patchRes = await fetch(`${KLAVIYO_API_BASE}/profiles/${profileId}`, {
    method: 'PATCH', headers: klaviyoHeaders(),
    body: JSON.stringify({ data: { type: 'profile', id: profileId, attributes: { properties } } }),
  });
  if (!patchRes.ok) { const err = await patchRes.json(); throw new Error(err.errors?.[0]?.detail || `Erreur PATCH profil: ${patchRes.status}`); }
}

/* ── Klaviyo : passer paid_user à true pour un email donné ── */
async function klaviyoSetPaidUser(email) {
  const searchRes = await fetch(
    `${KLAVIYO_API_BASE}/profiles/?filter=equals(email,"${encodeURIComponent(email)}")`,
    { headers: klaviyoHeaders() }
  );
  const searchData = await searchRes.json();
  const profileId  = searchData.data?.[0]?.id;
  if (!profileId) {
    console.warn(`[Klaviyo] Profil introuvable pour ${email} (paid_user)`);
    return;
  }
  const patchRes = await fetch(`${KLAVIYO_API_BASE}/profiles/${profileId}`, {
    method: 'PATCH',
    headers: klaviyoHeaders(),
    body: JSON.stringify({
      data: { type: 'profile', id: profileId, attributes: { properties: { paid_user: true, date_paid: new Date().toISOString() } } },
    }),
  });
  if (!patchRes.ok) {
    const err = await patchRes.json();
    throw new Error(err.errors?.[0]?.detail || `Erreur PATCH profil: ${patchRes.status}`);
  }
  console.log(`[Klaviyo] paid_user=true pour ${email}`);
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
    await klaviyoNewsletterDepuisInscription(data.user);
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
    email, note_globale, peut_aider, pourquoi, plus_apprecie, moins_apprecie,
    exercices_attendus, corrections_utiles, manquait,
    calibrage_questions, frein_souscription, continuer, frein_continuer,
    recommander, autres_outils, lesquels_outils, suggestions,
  } = req.body || {};

  if (note_globale == null || !peut_aider)
    return res.status(400).json({ error: 'Champs obligatoires manquants.' });

  const { error } = await supabaseAdmin.from('avis_trial').insert({
    email:                email || null,
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

const CHAT_MODEL = 'claude-sonnet-5-5';

/* ── Quiz CRPE ──
   Même projet Supabase et même compte que le tuteur IA (un seul compte, une seule authentification). Parcours : compte → test de positionnement gratuit (obligatoire) → paiement PayPal
   (79 € TTC pour 1 an d'accès, en une seule fois) → accès au quiz. Le blocage est vérifié ici : catalogue et correction réservés aux comptes payés.
   Tables quiz_questions et quiz_comptes, lues et écrites par le serveur (clé service_role). */
const QUIZ_MATIERES = ['francais', 'mathematiques', 'histoire_geographie', 'emc', 'svt', 'physique_chimie', 'technologie', 'arts', 'anglais'];
const QUIZ_LABELS = { francais: 'Français', mathematiques: 'Mathématiques', histoire_geographie: 'Histoire-géographie', emc: 'EMC', svt: 'SVT', physique_chimie: 'Physique-chimie', technologie: 'Technologie', arts: 'Arts', anglais: 'Anglais' };
const QUIZ_PRICE = { currency_code: 'EUR', value: '79.00' }; // 79 € TTC pour 1 an d'accès, en une seule fois, aligné avec la page /quizcrpe
const POSITIONNEMENT_PAR_MATIERE = { facile: 2, intermediaire: 3, difficile: 2 }; // 7 questions × 9 matières = 63 questions
const melanger = a => { const t = [...a]; for (let i = t.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [t[i], t[j]] = [t[j], t[i]]; } return t; };

// Catalogue d'une matière (sans réponses), gardé 10 minutes en mémoire
const quizCatalogues = new Map();
async function quizCatalogue(matiere) {
  const c = quizCatalogues.get(matiere);
  if (c && c.until > Date.now()) return c.data;
  // Supabase renvoie au plus 1 000 lignes par requête : on lit le catalogue par pages
  const data = [];
  for (let from = 0; ; from += 1000) {
    const { data: page, error } = await supabaseAdmin.from('quiz_questions')
      .select('id, notion, niveau, type, question, choix, programme_ref, classe, theme, sous_theme, objectif')
      .eq('matiere', matiere).eq('actif', true).order('ordre').order('id').range(from, from + 999);
    if (error) throw new Error(error.message);
    data.push(...page);
    if (page.length < 1000) break;
  }
  const questions = data.map(q => ({ ...q, notion: q.notion || `q${q.id}`, niveau: q.niveau || 'facile' }));
  // Version du catalogue (empreinte du contenu) : le navigateur garde sa copie tant qu'elle ne change pas
  const version = createHash('sha1').update(JSON.stringify(questions)).digest('hex').slice(0, 16);
  quizCatalogues.set(matiere, { data: questions, version, until: Date.now() + 600000 });
  return questions;
}
const quizVersion = matiere => quizCatalogues.get(matiere)?.version;

// Compte du quiz à partir du jeton, avec son état (positionnement, paiement), gardé 2 minutes
const quizSessions = new Map();
async function quizCompte(req, { frais = false } = {}) {
  const auth = req.headers.authorization || '';
  const token = auth.startsWith('Bearer ') ? auth.slice(7) : null;
  if (!token) return null;
  const c = quizSessions.get(token);
  if (!frais && c && c.until > Date.now()) return c.compte;
  const { data, error } = await supabaseAdmin.auth.getUser(token);
  if (error || !data?.user) return null;
  // Accès payé : profils_utilisateurs.quizcrpe_paye (source de vérité, modifiable à la main dans Supabase)
  const [{ data: ligne, error: e2 }, { data: profil, error: e3 }] = await Promise.all([
    supabaseAdmin.from('quiz_comptes').select('positionnement, essai_reponses').eq('user_id', data.user.id).maybeSingle(),
    supabaseAdmin.from('profils_utilisateurs').select('quizcrpe_paye').eq('user_id', data.user.id).maybeSingle(),
  ]);
  if (e2 || e3) throw new Error((e2 || e3).message);
  const l = ligne || {};
  const compte = { id: data.user.id, email: data.user.email, positionnement: l.positionnement || null, paid: profil?.quizcrpe_paye === true, essaiReponses: l.essai_reponses || {} };
  quizSessions.set(token, { compte, until: Date.now() + 120000 });
  return compte;
}
const quizOublier = userId => { for (const [t, c] of quizSessions) if (c.compte.id === userId) quizSessions.delete(t); };

/* ── Essai gratuit après le test : une série dans chacune des 2 matières les moins réussies, au niveau conseillé ── */
const ESSAI_NB_MATIERES = 2;
const niveauConseille = m => {
  const t = x => (x && x.n ? x.ok / x.n : null);
  if (!m.niveaux) return m.pct >= 80 ? 'difficile' : m.pct >= 40 ? 'intermediaire' : 'facile';
  const f = t(m.niveaux.facile), i = t(m.niveaux.intermediaire);
  if (f !== null && f < 1) return 'facile';
  if (i !== null && i < 1) return 'intermediaire';
  return 'difficile';
};
// Matières offertes (déduites du test, donc stables) et nombre de questions de chaque série d'essai
async function quizEssai(compte) {
  const r = compte.positionnement;
  if (!r || !Array.isArray(r.matieres)) return null;
  const ordre = m => QUIZ_MATIERES.indexOf(m.matiere);
  const choisies = r.matieres.slice().sort((a, b) => a.pct - b.pct || ordre(a) - ordre(b)).slice(0, ESSAI_NB_MATIERES);
  const matieres = await Promise.all(choisies.map(async m => {
    const niveau = niveauConseille(m);
    const notions = new Set((await quizCatalogue(m.matiere)).filter(q => q.niveau === niveau).map(q => q.notion));
    const max = Math.min(20, notions.size), faites = (compte.essaiReponses[m.matiere] || []).length;
    return { matiere: m.matiere, label: QUIZ_LABELS[m.matiere], niveau, max, faites: Math.min(faites, max), termine: faites >= max };
  }));
  return { matieres, termine: matieres.every(m => m.termine) };
}

// Accès au quiz : compte payé, ou essai gratuit dans une matière offerte (matiere = matière demandée)
async function quizAcces(req, res, matiere) {
  try {
    const compte = await quizCompte(req);
    if (!compte) { res.status(401).json({ error: 'Connexion requise.', code: 'connexion' }); return null; }
    if (compte.paid) return compte;
    const essai = compte.positionnement && matiere ? await quizEssai(compte) : null;
    const m = essai?.matieres.find(x => x.matiere === matiere);
    if (m && !m.termine) { compte.essaiMatiere = m; return compte; } // matière offerte dont la série d'essai n'est pas finie
    res.status(402).json({ error: 'Accès réservé aux comptes débloqués.', code: 'paiement' }); return null;
  } catch (err) {
    console.error('[quiz/acces]', err.message);
    res.status(500).json({ error: 'Le quiz n\'a pas pu être chargé.' }); return null;
  }
}

// Matière d'une question, à partir des catalogues gardés en mémoire
async function quizMatiereDe(id) {
  const cats = await Promise.all(QUIZ_MATIERES.map(quizCatalogue));
  for (const [i, cat] of cats.entries()) if (cat.some(q => q.id === id)) return QUIZ_MATIERES[i];
  return null;
}

// Propriétés Klaviyo du test de positionnement
const proprietesTest = (r, lien) => ({ test_positionnement_realise: true, test_positionnement_date: r.date, test_positionnement_score: r.pct,
  quizcrpe_trial: true, ...(lien ? { quiz_rapport_url: lien.url, quiz_rapport_expire: lien.expire } : {}) });
// Lien provisoire du rapport de positionnement : jeton aléatoire, valable 7 jours (effacé ensuite par une tâche planifiée Supabase)
const RAPPORT_JOURS = 7;
const lienRapport = token => `https://www.passcrpe.fr/quizapp?rapport=${token}`;

// Libellé précis d'un thème pour le rapport : le sous-thème du programme, raccourci (« Thème 1 : », détails après « : » ou « ; »)
function libelleTheme(q) {
  let t = (q.sous_theme || q.theme || 'Notions').replace(/^Thème \d+\s*:\s*/, '');
  if (t.length > 60 && t.includes(' : ')) t = t.split(' : ')[0];
  if (t.length > 60 && t.includes(' ; ')) t = t.split(' ; ')[0].length >= 15 ? t.split(' ; ')[0] : (q.theme || t);
  return t;
}

const nombre = v => Number(String(v ?? '').replace(/\s/g, '').replace(',', '.').replace('−', '-'));
const indices = v => String(v ?? '').split(',').map(x => x.trim()).filter(Boolean).map(Number).sort((a, b) => a - b).join(',');
async function quizCorriger(id, reponse) {
  const { data, error } = await supabaseAdmin.from('quiz_questions')
    .select('type, choix, reponse, explication, tolerance').eq('id', id).eq('actif', true).maybeSingle();
  if (error || !data) return null;
  let correct;
  if (data.type === 'numerique') {
    const n = nombre(reponse);
    correct = Number.isFinite(n) && Math.abs(n - nombre(data.reponse)) <= Number(data.tolerance || 0) + 1e-9;
  } else if (data.type === 'cliquer_mot') {
    correct = indices(reponse) === indices(data.reponse);
  } else {
    correct = String(reponse) === data.reponse;
  }
  // Pour les mots à cliquer, on renvoie aussi les mots attendus, lisibles
  const attendu = data.type === 'cliquer_mot' ? data.reponse.split(',').map(i => data.choix[Number(i)]).join(' ')
    : data.type === 'numerique' ? nombre(data.reponse).toLocaleString('fr-FR', { maximumFractionDigits: 6 }).replace('-', '−')
    : data.reponse;
  return { correct, reponse: data.reponse, attendu, explication: data.explication };
}

/* ── Formulaire de contact (/contact) : crée un ticket dans le support (support_tickets), visible dans /admin-support ── */
// Raisons des visiteurs non connectés et des personnes connectées (voir scripts/generate_contact.py)
const CONTACT_RAISONS = ['Problème de paiement', 'Question sur le Quiz CRPE', 'Question sur le Tuteur IA', 'Problème technique',
  'Question sur mon compte', 'Demande de remboursement', "Suggestion d'amélioration", 'Partenariat ou presse', 'Autre',
  "Problème d'inscription ou de connexion", "Je n'ai pas reçu l'e-mail de confirmation", 'Question sur le concours CRPE'];
const KLAVIYO_LIST_CONTACT = 'S2W3Pr'; // personnes ayant écrit via /contact (ajout à la liste, sans abonnement marketing)
const contactEnvois = new Map(); // limite simple : 5 messages par heure et par adresse IP
app.post('/api/contact', async (req, res) => {
  const { prenom = '', nom = '', email = '', raison = '', message = '', site = '' } = req.body || {};
  if (site) return res.json({ ok: true }); // champ piège rempli par les robots : on ignore
  const ip = String(req.headers['x-forwarded-for'] || req.socket?.remoteAddress || '').split(',')[0].trim();
  const now = Date.now(), recents = (contactEnvois.get(ip) || []).filter(t => now - t < 3600000);
  if (recents.length >= 5) return res.status(429).json({ error: 'Trop de messages envoyés. Réessayez dans une heure.' });
  const mail = String(email).trim().toLowerCase(), texte = String(message).trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail)) return res.status(400).json({ error: 'Adresse e-mail invalide.' });
  if (!CONTACT_RAISONS.includes(raison)) return res.status(400).json({ error: 'Choisissez une raison de contact.' });
  if (texte.length < 10 || texte.length > 5000) return res.status(400).json({ error: 'Votre message doit faire entre 10 et 5 000 caractères.' });
  try {
    const user = await getAuthenticatedUser(req); // compte connecté : la réponse apparaîtra aussi dans l'onglet Support de l'app
    const p = String(prenom).trim().slice(0, 80) || user?.user_metadata?.prenom || '';
    const n = String(nom).trim().slice(0, 80) || user?.user_metadata?.nom || '';
    const { error } = await supabaseAdmin.from('support_tickets').insert({
      user_id: user?.id || null, user_email: user?.email || mail,
      user_prenom: `${p} ${n}`.trim() || null, // prénom et nom, affichés dans /admin-support
      category: raison, message: texte,
      produit: raison === 'Question sur le Quiz CRPE' ? 'quiz' : raison === 'Question sur le Tuteur IA' ? 'tuteur' : null,
    });
    if (error) throw new Error(error.message);
    contactEnvois.set(ip, [...recents, now]);
    // Klaviyo : liste « contact » avec prénom, nom et raison (sans consentement marketing). Attendu avant de répondre
    // (sur Vercel, un envoi lancé après la réponse peut être perdu) ; un échec n'empêche pas l'envoi du message
    if (process.env.KLAVIYO_PRIVATE_API_KEY) {
      const proprietes = { contact_raison: raison, contact_date: new Date().toISOString() };
      try {
        await klaviyoSubscribePipeline(user?.email || mail, p, n, KLAVIYO_LIST_CONTACT, proprietes, {}, false);
        // profil déjà existant : le pipeline ne met à jour que les propriétés de parcours, on ajoute donc la raison explicitement
        await klaviyoSetProperties(user?.email || mail, proprietes);
      } catch (e) { console.error('[contact Klaviyo]', e.message); }
    }
    res.json({ ok: true });
  } catch (err) {
    console.error('[contact]', err.message);
    res.status(500).json({ error: "Votre message n'a pas pu être envoyé. Réessayez dans quelques instants." });
  }
});

// « Mes outils » : état du tuteur IA et du quiz pour le compte connecté
app.get('/api/espace', async (req, res) => {
  try {
    const user = await getAuthenticatedUser(req);
    if (!user) return res.status(401).json({ error: 'Connexion requise.' });
    const [{ data: profil }, { data: quiz }] = await Promise.all([
      supabaseAdmin.from('profils_utilisateurs').select('crpe_paid, trial, quizcrpe_paye').eq('user_id', user.id).maybeSingle(),
      supabaseAdmin.from('quiz_comptes').select('positionnement').eq('user_id', user.id).maybeSingle(),
    ]);
    res.json({
      email: user.email, prenom: user.user_metadata?.prenom || '',
      tuteur: { paid: profil?.crpe_paid === true, trial: profil?.trial !== false },
      quiz: { positionnement: !!quiz?.positionnement, score: quiz?.positionnement?.pct ?? null, paid: profil?.quizcrpe_paye === true },
    });
  } catch (err) {
    console.error('[espace]', err.message);
    res.status(500).json({ error: 'Votre espace n\'a pas pu être chargé.' });
  }
});

// État du compte : sert à l'application pour choisir l'écran (test, résultat + paiement, quiz)
app.get('/api/quiz/compte', async (req, res) => {
  try {
    const compte = await quizCompte(req, { frais: true });
    if (!compte) return res.status(401).json({ error: 'Connexion requise.' });
    res.json({ email: compte.email, positionnement: compte.positionnement, paid: compte.paid,
      essai: compte.paid ? null : await quizEssai(compte),
      paypal_client_id: process.env.VITE_PAYPAL_CLIENT_ID || process.env.PAYPAL_CLIENT_ID || null, prix: QUIZ_PRICE.value });
  } catch (err) {
    console.error('[quiz/compte]', err.message);
    res.status(500).json({ error: 'Votre compte n\'a pas pu être chargé.' });
  }
});

// Test de positionnement : 7 questions par matière (2 faciles, 3 intermédiaires, 2 avancées), sur des thèmes variés
app.get('/api/quiz/positionnement', async (req, res) => {
  try {
    const compte = await quizCompte(req);
    if (!compte) return res.status(401).json({ error: 'Connexion requise.' });
    const questions = [];
    // Les 9 matières sont chargées en parallèle (puis gardées 10 minutes en mémoire)
    const catalogues = await Promise.all(QUIZ_MATIERES.map(quizCatalogue));
    for (const [im, matiere] of QUIZ_MATIERES.entries()) {
      const cat = catalogues[im];
      const themesVus = new Set();
      for (const [niveau, n] of Object.entries(POSITIONNEMENT_PAR_MATIERE)) {
        // une question par notion, en privilégiant les thèmes pas encore posés
        const notions = {};
        cat.filter(q => q.niveau === niveau).forEach(q => { (notions[q.notion] ||= []).push(q); });
        const choix = melanger(Object.values(notions)).sort((a, b) => themesVus.has(a[0].theme) - themesVus.has(b[0].theme)).slice(0, n);
        choix.forEach(qs => { const q = qs[Math.floor(Math.random() * qs.length)]; themesVus.add(q.theme); questions.push({ ...q, matiere, choix: q.type === 'qcm' ? melanger(q.choix) : q.choix }); });
      }
    }
    res.json({ questions, deja: compte.positionnement || null });
  } catch (err) {
    console.error('[quiz/positionnement]', err.message);
    res.status(500).json({ error: 'Le test n\'a pas pu être chargé.' });
  }
});

// Correction du test et carte des forces et faiblesses (par matière et par thème)
app.post('/api/quiz/positionnement', async (req, res) => {
  try {
    const compte = await quizCompte(req, { frais: true });
    if (!compte) return res.status(401).json({ error: 'Connexion requise.' });
    if (compte.positionnement) return res.json({ resultat: compte.positionnement });
    const reponses = Array.isArray(req.body?.reponses) ? req.body.reponses.slice(0, 80) : [];
    if (reponses.length < 9) return res.status(400).json({ error: 'Test incomplet.' });
    const index = {};
    (await Promise.all(QUIZ_MATIERES.map(quizCatalogue))).forEach((cat, im) => cat.forEach(q => { index[q.id] = { ...q, matiere: QUIZ_MATIERES[im] }; }));
    const corrections = await Promise.all(reponses.map(r => index[Number(r.id)] ? quizCorriger(Number(r.id), r.reponse ?? '') : null));
    const parMatiere = {};
    reponses.forEach((r, i) => {
      const q = index[Number(r.id)], c = corrections[i]; if (!q || !c) return;
      const m = parMatiere[q.matiere] ||= { matiere: q.matiere, label: QUIZ_LABELS[q.matiere], ok: 0, n: 0, themes: {}, niveaux: {} };
      const lib = libelleTheme(q);
      const t = m.themes[lib] ||= { theme: lib, domaine: q.theme || '', ok: 0, n: 0 };
      const nv = m.niveaux[q.niveau] ||= { ok: 0, n: 0 };
      m.n++; t.n++; nv.n++; if (c.correct) { m.ok++; t.ok++; nv.ok++; }
    });
    const matieres = QUIZ_MATIERES.filter(m => parMatiere[m]).map(m => {
      const x = parMatiere[m];
      return { matiere: m, label: x.label, ok: x.ok, n: x.n, pct: Math.round(x.ok / x.n * 100), themes: Object.values(x.themes), niveaux: x.niveaux };
    });
    const ok = matieres.reduce((s, m) => s + m.ok, 0), n = matieres.reduce((s, m) => s + m.n, 0);
    const resultat = { date: new Date().toISOString(), ok, n, pct: n ? Math.round(ok / n * 100) : 0, matieres };
    // Détail des réponses données, conservé dans quiz_comptes.reponses_positionnement
    const detail = reponses.map((r, i) => {
      const q = index[Number(r.id)], c = corrections[i]; if (!q || !c) return null;
      return { id: q.id, matiere: q.matiere, niveau: q.niveau, theme: libelleTheme(q), question: q.question,
        reponse: r.reponse ?? '', attendu: c.attendu, correct: c.correct };
    }).filter(Boolean);
    // Enregistré une seule fois : un second envoi ne remplace pas le premier résultat
    const { data: existant } = await supabaseAdmin.from('quiz_comptes').select('positionnement').eq('user_id', compte.id).maybeSingle();
    let enregistre = existant?.positionnement, lien = null;
    if (!enregistre) {
      const rapport_token = randomBytes(24).toString('base64url');
      const rapport_expire_at = new Date(Date.parse(resultat.date) + RAPPORT_JOURS * 86400000).toISOString();
      const { error } = await supabaseAdmin.from('quiz_comptes').upsert({ user_id: compte.id, email: compte.email, positionnement: resultat,
        positionnement_at: resultat.date, reponses_positionnement: detail, rapport_token, rapport_expire_at, updated_at: new Date().toISOString() }, { onConflict: 'user_id' });
      lien = { url: lienRapport(rapport_token), expire: rapport_expire_at };
      if (error) throw new Error(error.message);
      enregistre = resultat;
    }
    quizOublier(compte.id);
    // Klaviyo : test réalisé, date et score global (relances vers le paiement). Attendu avant de répondre :
    // sur Vercel, le serveur peut s'arrêter dès la réponse envoyée et un envoi lancé après serait perdu
    if (compte.email && process.env.KLAVIYO_PRIVATE_API_KEY) {
      try { await klaviyoSetProperties(compte.email, proprietesTest(enregistre || resultat, lien)); }
      catch (e) { console.error('[Klaviyo positionnement]', e.message); }
    }
    res.json({ resultat: enregistre || resultat });
  } catch (err) {
    console.error('[quiz/positionnement correction]', err.message);
    res.status(500).json({ error: 'Le test n\'a pas pu être corrigé. Réessayez.' });
  }
});

// Bilan global de l'app : nombre de questions et de notions de chaque matière, comptés en base (gardés 10 minutes)
let quizTotaux = null;
app.get('/api/quiz/totaux', async (req, res) => {
  try {
    const compte = await quizCompte(req);
    if (!compte) return res.status(401).json({ error: 'Connexion requise.' });
    if (!quizTotaux || quizTotaux.until < Date.now()) {
      const { data, error } = await supabaseAdmin.rpc('quiz_totaux');
      if (error) throw new Error(error.message);
      const par = Object.fromEntries((data || []).map(r => [r.matiere, r]));
      const matieres = QUIZ_MATIERES.map(m => ({ matiere: m, label: QUIZ_LABELS[m], questions: Number(par[m]?.questions || 0), notions: Number(par[m]?.notions || 0) }));
      quizTotaux = { until: Date.now() + 600000, data: { matieres, questions: matieres.reduce((t, m) => t + m.questions, 0), notions: matieres.reduce((t, m) => t + m.notions, 0) } };
    }
    res.json(quizTotaux.data);
  } catch (err) { console.error('[quiz/totaux]', err.message); res.status(500).json({ error: 'Le bilan n\'a pas pu être chargé.' }); }
});

// Catalogue d'une matière sans les réponses : la sélection des séries de 20 et la révision espacée se font côté navigateur.
// Le navigateur garde sa copie (IndexedDB) et envoie sa version : si elle est à jour, seule la version est renvoyée.
// Les choix des QCM sont mélangés par le navigateur à chaque série.
app.get('/api/quiz/catalogue', async (req, res) => {
  const matiere = String(req.query.matiere || '');
  if (!QUIZ_MATIERES.includes(matiere)) return res.status(400).json({ error: 'Matière inconnue.' });
  if (!(await quizAcces(req, res, matiere))) return;
  try {
    const data = await quizCatalogue(matiere), version = quizVersion(matiere);
    if (req.query.version && req.query.version === version) return res.json({ version, inchange: true });
    res.json({ version, questions: data });
  } catch (err) { console.error('[quiz/catalogue]', err.message); res.status(500).json({ error: 'Le quiz n\'a pas pu être chargé.' }); }
});

app.post('/api/quiz/reponse', async (req, res) => {
  const id = Number(req.body?.id);
  const reponse = req.body?.reponse ?? req.body?.choix ?? '';
  if (!Number.isInteger(id)) return res.status(400).json({ error: 'Question inconnue.' });
  const matiere = await quizMatiereDe(id);
  if (!matiere) return res.status(404).json({ error: 'Question inconnue.' });
  const compte = await quizAcces(req, res, matiere);
  if (!compte) return;
  if (!compte.paid) {
    // Essai : la question compte dans la série offerte de cette matière, jusqu'à « max » questions différentes
    const deja = compte.essaiReponses[matiere] || [];
    if (!deja.includes(id)) {
      if (deja.length >= compte.essaiMatiere.max) return res.status(402).json({ error: "Votre série d'essai dans cette matière est terminée.", code: 'paiement' });
      const essai = { ...compte.essaiReponses, [matiere]: [...deja, id] };
      const { error } = await supabaseAdmin.from('quiz_comptes').update({ essai_reponses: essai, updated_at: new Date().toISOString() }).eq('user_id', compte.id);
      if (error) { console.error('[quiz/essai]', error.message); return res.status(500).json({ error: 'La correction n\'a pas pu être chargée.' }); }
      compte.essaiReponses = essai;
      // Cette réponse termine la série d'essai de la matière : si les 2 séries sont faites, essai terminé :
      // quizcrpe_trial passe à false (même logique que trial pour PassCRPE : true tant que l'essai est en cours)
      if (deja.length + 1 >= compte.essaiMatiere.max) {
        try {
          const e = await quizEssai(compte);
          if (e?.termine) {
            await supabaseAdmin.from('profils_utilisateurs').update({ quizcrpe_trial: false }).eq('user_id', compte.id);
            if (compte.email && process.env.KLAVIYO_PRIVATE_API_KEY) await klaviyoSetProperties(compte.email, { quizcrpe_trial: false });
          }
        } catch (err) { console.error('[quiz/essai terminé]', err.message); }
      }
    }
  }
  const c = await quizCorriger(id, reponse);
  if (!c) return res.status(404).json({ error: 'Question inconnue.' });
  res.json(c);
});

// Rapport de positionnement par lien provisoire (sans connexion) : valable jusqu'à rapport_expire_at, ensuite introuvable
app.get('/api/quiz/rapport', async (req, res) => {
  const token = String(req.query.token || '');
  if (!/^[A-Za-z0-9_-]{20,80}$/.test(token)) return res.status(404).json({ error: 'Ce lien n\'existe pas ou a expiré.' });
  try {
    const { data, error } = await supabaseAdmin.from('quiz_comptes').select('positionnement, rapport_expire_at, prenom')
      .eq('rapport_token', token).maybeSingle();
    if (error) throw new Error(error.message);
    if (!data?.positionnement || !data.rapport_expire_at || Date.parse(data.rapport_expire_at) < Date.now())
      return res.status(404).json({ error: 'Ce lien n\'existe pas ou a expiré.' });
    res.set('Cache-Control', 'no-store').json({ resultat: data.positionnement, expire: data.rapport_expire_at, prenom: data.prenom || '' });
  } catch (err) { console.error('[quiz/rapport]', err.message); res.status(500).json({ error: 'Le rapport n\'a pas pu être chargé.' }); }
});

// Paiement PayPal du quiz : même fonctionnement que PassCRPE (commande serveur, custom_id = « quiz:<id du compte> »)
app.post('/api/quiz/paypal/create-order', async (req, res) => {
  try {
    const compte = await quizCompte(req, { frais: true });
    if (!compte) return res.status(401).json({ error: 'Non authentifié' });
    if (compte.paid) return res.status(409).json({ error: 'Votre accès est déjà débloqué.' });
    const accessToken = await getPaypalAccessToken();
    const orderRes = await fetch(`${PAYPAL_API_BASE}/v2/checkout/orders`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ intent: 'CAPTURE', purchase_units: [{ custom_id: `quiz:${compte.id}`, description: 'Accès Quiz CRPE', amount: QUIZ_PRICE }] }),
    });
    const order = await orderRes.json();
    if (!orderRes.ok) throw new Error(order.message || 'Erreur PayPal');
    res.json({ id: order.id });
  } catch (err) {
    console.error('[Quiz PayPal create-order]', err.message);
    res.status(500).json({ error: err.message });
  }
});

app.post('/api/quiz/paypal/capture-order', async (req, res) => {
  try {
    const compte = await quizCompte(req, { frais: true });
    if (!compte) return res.status(401).json({ error: 'Non authentifié' });
    const { orderID } = req.body || {};
    if (!orderID) return res.status(400).json({ error: 'orderID manquant' });
    const accessToken = await getPaypalAccessToken();
    const captureRes = await fetch(`${PAYPAL_API_BASE}/v2/checkout/orders/${encodeURIComponent(orderID)}/capture`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
    });
    const capture = await captureRes.json();
    if (!captureRes.ok) throw new Error(capture.message || 'Erreur de capture PayPal');
    const cap = capture.purchase_units?.[0]?.payments?.captures?.[0];
    if (capture.status === 'COMPLETED' && cap?.custom_id === `quiz:${compte.id}`) await markQuizPaid(compte.id, cap.id, compte.email);
    res.json({ status: capture.status });
  } catch (err) {
    console.error('[Quiz PayPal capture-order]', err.message);
    res.status(500).json({ error: err.message });
  }
});


app.post('/api/chat', async (req, res) => {
  // Réservé aux candidats connectés : sans ça, n'importe qui pourrait utiliser la clé Anthropic
  const user = await getAuthenticatedUser(req);
  if (!user) return res.status(401).json({ error: 'Connexion requise.' });

  const { messages, system } = req.body;
  // L'identifiant utilisateur vient du jeton, pas du navigateur
  const meta = { ...(req.body.meta || {}), user_id: user.id };
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

/* ── Entraîneur CRPE (outil gratuit) ── */
// Même modèle que les corrections de l'application (CHAT_MODEL)
// L'Entraîneur utilise uniquement sa propre clé ANTHROPIC_API_KEY_ENTRAINEUR (consommation suivie à part), jamais celle de l'application
const ENTRAINEUR_ANTHROPIC_KEY = cleanKey(process.env.ANTHROPIC_API_KEY_ENTRAINEUR);
if (!ENTRAINEUR_ANTHROPIC_KEY) console.error('[config] ANTHROPIC_API_KEY_ENTRAINEUR manquante : les rapports de l\'Entraîneur échoueront');
console.log('[config] clé Entraîneur :', keyFingerprint(ENTRAINEUR_ANTHROPIC_KEY));
const entraineurClient = new Anthropic({
  apiKey: ENTRAINEUR_ANTHROPIC_KEY,
  // Une clé utilisateur (sk-ant-usr-…) non rattachée à un espace de travail doit préciser lequel facturer
  ...(cleanKey(process.env.ANTHROPIC_WORKSPACE_ID_ENTRAINEUR) ? { defaultHeaders: { 'anthropic-workspace-id': cleanKey(process.env.ANTHROPIC_WORKSPACE_ID_ENTRAINEUR) } } : {}),
});
// Entraîneur : Sonnet pour la synthèse, Haiku (environ 3 fois moins cher) pour corriger chacune des 5 réponses
const ENTRAINEUR_MODEL_CORRECTION = process.env.ENTRAINEUR_MODEL_CORRECTION || 'claude-haiku-5-5';
registerEntraineurRoutes(app, { supabaseAdmin, anthropic: entraineurClient, model: CHAT_MODEL, modelCorrection: ENTRAINEUR_MODEL_CORRECTION, klaviyoHeaders, klaviyoApiBase: KLAVIYO_API_BASE });

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

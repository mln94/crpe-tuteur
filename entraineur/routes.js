// Entraîneur CRPE : API du lead magnet (tirage de questions, quotas, correction IA, révélation du corrigé).
// Toutes les tables entraineur_* sont fermées au navigateur (RLS sans règle) : seul ce serveur y accède.
import crypto from 'crypto';
import { SYSTEM_PROMPT, REPORT_TOOL, buildUserMessage, validateReport } from './prompt.js';

// ── Réglages faciles à modifier ──
export const ANON_QUESTION_LIMIT   = 1;   // questions au total sans inscription
export const WEEKLY_QUESTION_LIMIT = 5;   // questions par semaine avec inscription (recharge le lundi 0 h, heure de Paris)
export const MAX_ATTEMPTS          = 3;   // tentatives par question
export const MAX_ANSWER_LENGTH     = 3000;
export const CORRECTIONS_PER_HOUR  = 10;  // limite de fréquence des corrections par personne
const KLAVIYO_LIST_LEAD_MAGNET     = 'TVBdQK'; // Lead_magnet_ecrire_crpe
const CONSENT_VERSION              = '2026-10-12';

// Catégories proposées (niveau cycle 4) ; une catégorie sans question n'est simplement jamais tirée
export const CATEGORIES = {
  maths: [
    'Nombres et calculs',
    'Espace et géométrie',
    'Proportionnalité, fonctions',
    'Organisation et gestion de données et probabilités',
    'La pensée informatique',
  ],
  francais: [
    'Lecture',
    'Culture littéraire et artistique',
    'Écriture',
    'Vocabulaire et orthographe lexicale',
    'Grammaire et orthographe grammaticale',
  ],
};
const SOURCE = {
  maths:    { table: 'exercices_maths',      cols: 'id, thematique, classe, enonce, question, figure_path, figure_svg' },
  francais: { table: 'exercices_francais_v', cols: 'id, thematique, niveau, texte_support, question' },
};

const ANON_COOKIE = 'pc_anon';
const LEAD_COOKIE = 'pc_lead';
const YEAR_MS = 365 * 24 * 3600 * 1000;

export function registerEntraineurRoutes(app, { supabaseAdmin, anthropic, model, klaviyoHeaders, klaviyoApiBase }) {
  const SECRET = process.env.ENTRAINEUR_SECRET || process.env.SUPABASE_SERVICE_ROLE_KEY || '';
  const hmac = v => crypto.createHmac('sha256', SECRET).update(v).digest('hex');

  // ── Cookies et identité (identifiant anonyme haché, jamais d'adresse IP) ──
  function readCookies(req) {
    const out = {};
    for (const part of (req.headers.cookie || '').split(';')) {
      const i = part.indexOf('=');
      if (i > 0) out[part.slice(0, i).trim()] = decodeURIComponent(part.slice(i + 1).trim());
    }
    return out;
  }
  function setCookie(req, res, name, value) {
    const secure = process.env.NODE_ENV === 'production' || req.headers['x-forwarded-proto'] === 'https';
    const cookie = `${name}=${encodeURIComponent(value)}; Path=/; Max-Age=${YEAR_MS / 1000}; HttpOnly; SameSite=Lax${secure ? '; Secure' : ''}`;
    const prev = res.getHeader('Set-Cookie');
    res.setHeader('Set-Cookie', prev ? [].concat(prev, cookie) : cookie);
  }
  function identify(req, res) {
    const cookies = readCookies(req);
    let anonId = cookies[ANON_COOKIE];
    if (!anonId || !/^[a-f0-9]{48}$/.test(anonId)) {
      anonId = crypto.randomBytes(24).toString('hex');
      setCookie(req, res, ANON_COOKIE, anonId);
    }
    let leadId = null;
    const signed = cookies[LEAD_COOKIE] || '';
    const [id, sig] = signed.split('.');
    if (id && sig && crypto.timingSafeEqual(Buffer.from(hmac(`lead:${id}`)), Buffer.from(sig.padEnd(64, '0').slice(0, 64)))) leadId = id;
    return { anonHash: hmac(`anon:${anonId}`), leadId };
  }

  // ── Semaine : lundi 0 h, heure de Paris ──
  function parisOffsetMs(date) {
    const p = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone: 'Europe/Paris', hourCycle: 'h23',
      year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' })
      .formatToParts(date).map(x => [x.type, x.value]));
    return Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour, +p.minute, +p.second) - Math.floor(date.getTime() / 1000) * 1000;
  }
  function parisWeekStart(now = new Date()) {
    const local = new Date(now.getTime() + parisOffsetMs(now));            // heure de Paris lue comme UTC
    const sinceMonday = (local.getUTCDay() + 6) % 7;
    const mondayLocal = Date.UTC(local.getUTCFullYear(), local.getUTCMonth(), local.getUTCDate() - sinceMonday);
    return new Date(mondayLocal - parisOffsetMs(new Date(mondayLocal)));
  }
  const nextReset = start => parisWeekStart(new Date(start.getTime() + 7.5 * 24 * 3600 * 1000));

  async function loadLead(leadId) {
    if (!leadId) return null;
    const { data } = await supabaseAdmin.from('entraineur_leads').select('id, prenom').eq('id', leadId).maybeSingle();
    return data || null;
  }

  async function quotaFor(ident, lead) {
    if (lead) {
      const start = parisWeekStart();
      const { count } = await supabaseAdmin.from('entraineur_questions_servies')
        .select('id', { count: 'exact', head: true }).eq('lead_id', lead.id).gte('served_at', start.toISOString());
      const used = count || 0;
      return { type: 'lead', limit: WEEKLY_QUESTION_LIMIT, used, remaining: Math.max(0, WEEKLY_QUESTION_LIMIT - used), resetAt: nextReset(start).toISOString() };
    }
    const { count } = await supabaseAdmin.from('entraineur_questions_servies')
      .select('id', { count: 'exact', head: true }).eq('anon_id_hash', ident.anonHash).is('lead_id', null);
    const used = count || 0;
    return { type: 'anon', limit: ANON_QUESTION_LIMIT, used, remaining: Math.max(0, ANON_QUESTION_LIMIT - used), resetAt: null };
  }

  // Liste des questions disponibles (id + catégorie), gardée 10 minutes en mémoire
  const pool = {};
  async function questionPool(matiere) {
    if (pool[matiere] && pool[matiere].at > Date.now() - 600_000) return pool[matiere].rows;
    const { data, error } = await supabaseAdmin.from(SOURCE[matiere].table).select('id, thematique').in('thematique', CATEGORIES[matiere]);
    if (error) throw error;
    pool[matiere] = { at: Date.now(), rows: data || [] };
    return pool[matiere].rows;
  }

  // Question telle qu'envoyée au navigateur : jamais le corrigé
  function publicQuestion(matiere, q) {
    const figure = matiere === 'maths'
      ? (q.figure_path ? { type: 'path', src: q.figure_path } : q.figure_svg ? { type: 'svg', svg: q.figure_svg } : null)
      : null;
    return {
      matiere,
      categorie: q.thematique,
      classe: q.classe || q.niveau || null,
      enonce: q.enonce || null,
      texte_support: q.texte_support || null,
      question: q.question,
      figure,
    };
  }
  async function fetchQuestion(matiere, id, withCorrige = false) {
    const cols = SOURCE[matiere].cols + (withCorrige ? ', reponse_ideale, synthese_cours' : '');
    const { data, error } = await supabaseAdmin.from(SOURCE[matiere].table).select(cols).eq('id', id).single();
    if (error) throw error;
    return data;
  }

  const ownsServie = (s, ident) => s && ((ident.leadId && s.lead_id === ident.leadId) || s.anon_id_hash === ident.anonHash);
  const publicAttempt = t => ({ tentative: t.tentative, reponse: t.reponse, rapport: t.rapport, created_at: t.created_at });

  async function corrigeFor(servie, attempts) {
    const q = await fetchQuestion(servie.matiere, servie.question_id, true);
    const last = attempts.find(a => a.tentative === MAX_ATTEMPTS);
    return { reponse_ideale: q.reponse_ideale, synthese: q.synthese_cours || null, explication: last?.rapport?.explication || null };
  }

  // État d'une question servie (pour reprendre après un rechargement de page)
  async function servieState(servie) {
    const { data: attempts } = await supabaseAdmin.from('entraineur_tentatives')
      .select('tentative, reponse, rapport, created_at').eq('servie_id', servie.id).order('tentative');
    const q = await fetchQuestion(servie.matiere, servie.question_id);
    return {
      servieId: servie.id,
      ...publicQuestion(servie.matiere, q),
      attempts: (attempts || []).map(publicAttempt),
      revealed: !!servie.revealed_at,
      corrige: servie.revealed_at ? await corrigeFor(servie, attempts || []) : null,
    };
  }

  const fail = (res, status, error, extra = {}) => res.status(status).json({ error, ...extra });

  // ── GET /api/entraineur/status : contact, compteur et question en cours ──
  app.get('/api/entraineur/status', async (req, res) => {
    try {
      const ident = identify(req, res);
      const lead = await loadLead(ident.leadId);
      const quota = await quotaFor(ident, lead);
      let q = supabaseAdmin.from('entraineur_questions_servies').select('*').order('served_at', { ascending: false }).limit(1)
        .gte('served_at', new Date(Date.now() - 7 * 24 * 3600 * 1000).toISOString());
      q = lead ? q.or(`lead_id.eq.${lead.id},anon_id_hash.eq.${ident.anonHash}`) : q.eq('anon_id_hash', ident.anonHash);
      const { data: last } = await q;
      res.json({
        lead: lead ? { prenom: lead.prenom } : null,
        quota,
        current: last?.[0] ? await servieState(last[0]) : null,
      });
    } catch (e) {
      console.error('[entraineur/status]', e.message);
      fail(res, 500, 'Le service est momentanément indisponible.');
    }
  });

  // ── POST /api/entraineur/question : tire une nouvelle question (consomme le quota) ──
  app.post('/api/entraineur/question', async (req, res) => {
    try {
      const matiere = req.body?.matiere;
      if (!SOURCE[matiere]) return fail(res, 400, 'Matière invalide.');
      const ident = identify(req, res);
      const lead = await loadLead(ident.leadId);
      const quota = await quotaFor(ident, lead);
      if (quota.remaining <= 0) return fail(res, 403, quota.type === 'anon' ? 'signup_required' : 'weekly_limit', { quota });

      // Évite les questions déjà vues par cette personne (sur ce navigateur et avec son e-mail)
      let seenQ = supabaseAdmin.from('entraineur_questions_servies').select('question_id').eq('matiere', matiere);
      seenQ = lead ? seenQ.or(`lead_id.eq.${lead.id},anon_id_hash.eq.${ident.anonHash}`) : seenQ.eq('anon_id_hash', ident.anonHash);
      const { data: seenRows } = await seenQ;
      const seen = new Set((seenRows || []).map(r => r.question_id));
      const all = await questionPool(matiere);
      if (!all.length) return fail(res, 503, 'Aucune question disponible pour le moment.');
      const fresh = all.filter(r => !seen.has(r.id));
      const pick = (fresh.length ? fresh : all)[crypto.randomInt((fresh.length ? fresh : all).length)];

      const { data: servie, error } = await supabaseAdmin.from('entraineur_questions_servies').insert({
        lead_id: lead?.id || null,
        anon_id_hash: lead ? null : ident.anonHash,
        matiere,
        question_id: pick.id,
        categorie: pick.thematique,
      }).select('*').single();
      if (error) throw error;

      res.json({ question: await servieState(servie), quota: await quotaFor(ident, lead) });
    } catch (e) {
      console.error('[entraineur/question]', e.message);
      fail(res, 500, 'Impossible de tirer une question pour le moment.');
    }
  });

  // ── POST /api/entraineur/lead : formulaire d'accès (prénom, nom, e-mail, téléphone, consentements) ──
  app.post('/api/entraineur/lead', async (req, res) => {
    try {
      const b = req.body || {};
      const prenom = String(b.prenom || '').trim().slice(0, 80);
      const nom = String(b.nom || '').trim().slice(0, 80);
      const email = String(b.email || '').trim().toLowerCase();
      const telephone = String(b.telephone || '').trim();
      if (!prenom || !nom) return fail(res, 400, 'Merci d\'indiquer ton prénom et ton nom.');
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || email.length > 254) return fail(res, 400, 'Adresse e-mail invalide.');
      const digits = telephone.replace(/\D/g, '');
      if (!/^\+?[\d\s.\-()]{6,30}$/.test(telephone) || digits.length < 9 || digits.length > 15) return fail(res, 400, 'Numéro de téléphone invalide.');
      const consent_conseils = b.consent_conseils === true;
      const consent_partenaires = b.consent_partenaires === true;

      const ident = identify(req, res);
      const { data: existing } = await supabaseAdmin.from('entraineur_leads').select('id, consent_conseils, consent_partenaires').eq('email', email).maybeSingle();
      // Un consentement déjà donné n'est jamais retiré en silence (le retrait passe par le lien de désinscription)
      const row = {
        prenom, nom, email, telephone,
        consent_conseils: consent_conseils || !!existing?.consent_conseils,
        consent_partenaires: consent_partenaires || !!existing?.consent_partenaires,
        consent_version: CONSENT_VERSION, updated_at: new Date().toISOString(),
      };
      const { data: lead, error } = existing
        ? await supabaseAdmin.from('entraineur_leads').update(row).eq('id', existing.id).select('id, prenom').single()
        : await supabaseAdmin.from('entraineur_leads').insert(row).select('id, prenom').single();
      if (error) throw error;

      setCookie(req, res, LEAD_COOKIE, `${lead.id}.${hmac(`lead:${lead.id}`)}`);

      // Klaviyo : liste Lead_magnet_ecrire_crpe ; abonnement marketing seulement si la case « conseils » est cochée
      try {
        await klaviyoAddLead({ prenom, nom, email, telephone, consent_conseils, consent_partenaires });
        await supabaseAdmin.from('entraineur_leads').update({ klaviyo_synced_at: new Date().toISOString() }).eq('id', lead.id);
      } catch (e) {
        console.error('[entraineur/klaviyo]', e.message);
      }

      res.json({ lead: { prenom: lead.prenom }, existing: !!existing, quota: await quotaFor(ident, lead) });
    } catch (e) {
      console.error('[entraineur/lead]', e.message);
      fail(res, 500, 'Inscription impossible pour le moment. Réessaie dans quelques instants.');
    }
  });

  function toE164(tel) {
    const t = tel.replace(/[\s.\-()]/g, '');
    if (/^\+\d{8,15}$/.test(t)) return t;
    if (/^00\d{8,15}$/.test(t)) return '+' + t.slice(2);
    if (/^0\d{9}$/.test(t)) return '+33' + t.slice(1);
    return null;
  }

  async function klaviyoAddLead({ prenom, nom, email, telephone, consent_conseils, consent_partenaires }) {
    if (!process.env.KLAVIYO_PRIVATE_API_KEY) throw new Error('KLAVIYO_PRIVATE_API_KEY manquante');
    const phone = toE164(telephone);
    const attributes = {
      email, first_name: prenom, last_name: nom,
      ...(phone ? { phone_number: phone } : {}),
      properties: { lead_magnet: 'entraineur_crpe', telephone_saisi: telephone, consent_conseils, consent_partenaires, consent_version: CONSENT_VERSION },
    };
    let r = await fetch(`${klaviyoApiBase}/profiles`, { method: 'POST', headers: klaviyoHeaders(), body: JSON.stringify({ data: { type: 'profile', attributes } }) });
    if (r.status === 400 && phone) { // numéro refusé par Klaviyo : on garde le profil sans phone_number
      delete attributes.phone_number;
      r = await fetch(`${klaviyoApiBase}/profiles`, { method: 'POST', headers: klaviyoHeaders(), body: JSON.stringify({ data: { type: 'profile', attributes } }) });
    }
    let profileId;
    if (r.status === 409) {
      profileId = (await r.json()).errors?.[0]?.meta?.duplicate_profile_id;
      if (profileId) {
        await fetch(`${klaviyoApiBase}/profiles/${profileId}`, { method: 'PATCH', headers: klaviyoHeaders(),
          body: JSON.stringify({ data: { type: 'profile', id: profileId, attributes: { first_name: prenom, last_name: nom, properties: attributes.properties } } }) });
      }
    } else if (r.ok) {
      profileId = (await r.json()).data?.id;
    } else {
      throw new Error(`profil Klaviyo : ${r.status}`);
    }
    if (!profileId) throw new Error('profil Klaviyo introuvable');
    const l = await fetch(`${klaviyoApiBase}/lists/${KLAVIYO_LIST_LEAD_MAGNET}/relationships/profiles`, {
      method: 'POST', headers: klaviyoHeaders(), body: JSON.stringify({ data: [{ type: 'profile', id: profileId }] }),
    });
    if (!l.ok && l.status !== 409) throw new Error(`liste Klaviyo : ${l.status}`);
    if (consent_conseils) {
      const c = await fetch(`${klaviyoApiBase}/profile-subscription-bulk-create-jobs`, {
        method: 'POST', headers: klaviyoHeaders(),
        body: JSON.stringify({ data: {
          type: 'profile-subscription-bulk-create-job',
          attributes: { profiles: { data: [{ type: 'profile', attributes: { email, subscriptions: { email: { marketing: { consent: 'SUBSCRIBED' } } } } }] }, historical_import: false },
          relationships: { list: { data: { type: 'list', id: KLAVIYO_LIST_LEAD_MAGNET } } },
        } }),
      });
      if (!c.ok) throw new Error(`consentement Klaviyo : ${c.status}`);
    }
  }

  async function loadOwnedServie(req, res) {
    const ident = identify(req, res);
    const servieId = String(req.body?.servieId || '');
    if (!/^[0-9a-f-]{36}$/.test(servieId)) return { ident, servie: null };
    const { data: servie } = await supabaseAdmin.from('entraineur_questions_servies').select('*').eq('id', servieId).maybeSingle();
    return { ident, servie: ownsServie(servie, ident) ? servie : null };
  }

  // Appel au modèle avec sortie forcée dans l'outil rapport_correction ; une nouvelle tentative si le JSON est invalide
  async function correct(payload) {
    let usage = { input_tokens: 0, output_tokens: 0 };
    for (let essai = 0; essai < 2; essai++) {
      const msg = await anthropic.messages.create({
        model,
        max_tokens: 2500,
        system: [{ type: 'text', text: SYSTEM_PROMPT, cache_control: { type: 'ephemeral' } }],
        tools: [REPORT_TOOL],
        tool_choice: { type: 'tool', name: REPORT_TOOL.name },
        messages: [{ role: 'user', content: buildUserMessage(payload) }],
      });
      usage = { input_tokens: usage.input_tokens + (msg.usage?.input_tokens || 0), output_tokens: usage.output_tokens + (msg.usage?.output_tokens || 0) };
      const block = msg.content.find(c => c.type === 'tool_use' && c.name === REPORT_TOOL.name);
      const report = validateReport(block?.input, payload.tentative);
      if (report) return { report, usage, model: msg.model };
    }
    return { report: null, usage };
  }

  // ── POST /api/entraineur/correct : corrige une tentative (ne consomme pas de question) ──
  app.post('/api/entraineur/correct', async (req, res) => {
    try {
      const { ident, servie } = await loadOwnedServie(req, res);
      if (!servie) return fail(res, 404, 'Question introuvable.');
      if (servie.revealed_at) return fail(res, 409, 'La réponse a déjà été révélée pour cette question.');
      const reponse = String(req.body?.reponse || '').trim();
      if (reponse.length < 5) return fail(res, 400, 'Ta réponse est trop courte.');
      if (reponse.length > MAX_ANSWER_LENGTH) return fail(res, 400, `Ta réponse dépasse ${MAX_ANSWER_LENGTH} caractères.`);

      const { data: attempts } = await supabaseAdmin.from('entraineur_tentatives')
        .select('tentative, reponse, rapport, created_at').eq('servie_id', servie.id).order('tentative');
      const tentative = (attempts?.length || 0) + 1;
      if (tentative > MAX_ATTEMPTS) return fail(res, 409, 'Tu as utilisé tes 3 tentatives pour cette question.');

      // Limite de fréquence : corrections de la dernière heure pour cette personne
      const since = new Date(Date.now() - 3600 * 1000).toISOString();
      let rl = supabaseAdmin.from('entraineur_tentatives').select('id, entraineur_questions_servies!inner(lead_id, anon_id_hash)', { count: 'exact', head: true }).gte('created_at', since);
      rl = ident.leadId ? rl.eq('entraineur_questions_servies.lead_id', ident.leadId) : rl.eq('entraineur_questions_servies.anon_id_hash', ident.anonHash);
      const { count } = await rl;
      if ((count || 0) >= CORRECTIONS_PER_HOUR) return fail(res, 429, 'Tu as atteint la limite de corrections pour cette heure. Réessaie un peu plus tard.');

      const q = await fetchQuestion(servie.matiere, servie.question_id, true);
      const pub = publicQuestion(servie.matiere, q);
      const { report, usage, model: usedModel } = await correct({
        matiere: servie.matiere,
        categorie: servie.categorie,
        question: pub,
        corrige: q.reponse_ideale,
        tentative,
        reponse,
        rapportPrecedent: attempts?.length ? attempts[attempts.length - 1].rapport : null,
      });
      if (!report) return fail(res, 502, 'La correction n\'a pas pu être générée. Ta tentative n\'est pas comptée : réessaie.');

      const { data: saved, error } = await supabaseAdmin.from('entraineur_tentatives').insert({
        servie_id: servie.id, tentative, reponse, rapport: report, note: report.note,
        model: usedModel, input_tokens: usage.input_tokens, output_tokens: usage.output_tokens,
      }).select('tentative, reponse, rapport, created_at').single();
      if (error) {
        if (error.code === '23505') return fail(res, 409, 'Cette tentative a déjà été corrigée.');
        throw error;
      }

      // 3e tentative : la réponse attendue est révélée automatiquement
      let corrige = null;
      if (tentative === MAX_ATTEMPTS) {
        await supabaseAdmin.from('entraineur_questions_servies').update({ revealed_at: new Date().toISOString() }).eq('id', servie.id);
        corrige = { reponse_ideale: q.reponse_ideale, synthese: q.synthese_cours || null, explication: report.explication };
      }
      res.json({ attempt: publicAttempt(saved), revealed: !!corrige, corrige });
    } catch (e) {
      console.error('[entraineur/correct]', e.message);
      fail(res, 500, 'La correction a échoué. Ta tentative n\'est pas comptée : réessaie.');
    }
  });

  // ── POST /api/entraineur/reveal : affiche la réponse attendue (après au moins une tentative) ──
  app.post('/api/entraineur/reveal', async (req, res) => {
    try {
      const { servie } = await loadOwnedServie(req, res);
      if (!servie) return fail(res, 404, 'Question introuvable.');
      const { data: attempts } = await supabaseAdmin.from('entraineur_tentatives')
        .select('tentative, rapport').eq('servie_id', servie.id).order('tentative');
      if (!attempts?.length) return fail(res, 409, 'Propose au moins une réponse avant de voir la réponse attendue.');
      if (!servie.revealed_at) {
        await supabaseAdmin.from('entraineur_questions_servies').update({ revealed_at: new Date().toISOString() }).eq('id', servie.id);
      }
      res.json({ revealed: true, corrige: await corrigeFor(servie, attempts) });
    } catch (e) {
      console.error('[entraineur/reveal]', e.message);
      fail(res, 500, 'Impossible d\'afficher la réponse pour le moment.');
    }
  });
}

// Entraîneur CRPE : API du lead magnet.
// Parcours : le candidat répond à 5 questions (sans correction à l'écran), remplit le formulaire, puis reçoit par e-mail
// (flow Klaviyo déclenché par l'événement « Rapport Entraîneur CRPE ») le lien vers son rapport détaillé.
// Toutes les tables entraineur_* sont fermées au navigateur (RLS sans règle) : seul ce serveur y accède.
import crypto from 'crypto';
import { questionPrompt, synthesePrompt, QUESTION_TOOL, SYNTHESE_TOOL, questionMessage, syntheseMessage, validateQuestion, validateSynthese } from './prompt.js';

// ── Réglages faciles à modifier ──
export const QUESTIONS_PER_SET     = 5;   // questions par série
export const WEEKLY_REPORT_LIMIT   = 1;   // rapports par adresse e-mail et par semaine (recharge le lundi 0 h, heure de Paris)
export const MAX_ANSWER_LENGTH     = 3000;
export const REPORT_RETENTION_DAYS = 7;   // rapports personnels supprimés après 7 jours (une copie anonyme est gardée dans entraineur_corpus)
const SET_MAX_AGE_MS               = 48 * 3600 * 1000; // une série de questions reste valable 48 h
const KLAVIYO_LIST_LEAD_MAGNET     = 'RazEb5'; // liste Lead_magnet_entraineur_crpe (simple opt-in)
const KLAVIYO_REPORT_METRIC        = 'Rapport Entraîneur CRPE';
const CONSENT_VERSION              = '2026-10-12';
const SITE                         = 'https://www.passcrpe.fr';
export const REPORT_PATH           = '/outils/entraineur-crpe/rapport/';

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
  maths:    { table: 'exercices_maths',      cols: 'id, thematique, classe, enonce, question, figure_path, figure_svg, figure_masquee, outil_reponse' },
  francais: { table: 'exercices_francais_v', cols: 'id, thematique, niveau, texte_support, question' },
};
const MATIERE_LABEL = { maths: 'Mathématiques', francais: 'Français' };
const NIVEAU_LABEL = { a_retravailler: 'À retravailler', en_bonne_voie: 'En bonne voie', attendu_atteint: 'Attendu du CRPE atteint' };

export function registerEntraineurRoutes(app, { supabaseAdmin, anthropic, model, klaviyoHeaders, klaviyoApiBase }) {
  const SECRET = process.env.ENTRAINEUR_SECRET || process.env.SUPABASE_SERVICE_ROLE_KEY || '';
  const hmac = v => crypto.createHmac('sha256', SECRET).update(v).digest('base64url');
  const fail = (res, status, error, extra = {}) => res.status(status).json({ error, ...extra });

  // ── Série de questions signée : le navigateur la garde et la renvoie avec les réponses (pas de cookie) ──
  const signSet = set => { const p = Buffer.from(JSON.stringify(set)).toString('base64url'); return `${p}.${hmac(`set:${p}`)}`; };
  function readSet(token) {
    const [p, sig] = String(token || '').split('.');
    if (!p || !sig) return null;
    const expected = Buffer.from(hmac(`set:${p}`));
    const given = Buffer.from(sig);
    if (expected.length !== given.length || !crypto.timingSafeEqual(expected, given)) return null;
    try {
      const set = JSON.parse(Buffer.from(p, 'base64url').toString());
      if (!SOURCE[set.m] || !Array.isArray(set.ids) || set.ids.length !== QUESTIONS_PER_SET || Date.now() - set.t > SET_MAX_AGE_MS) return null;
      return set;
    } catch { return null; }
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
    // Figure masquée en base (elle donnait la réponse ou n'apportait rien) : jamais envoyée
    const figure = matiere === 'maths' && !q.figure_masquee
      ? (q.figure_path ? { type: 'path', src: q.figure_path } : q.figure_svg ? { type: 'svg', svg: q.figure_svg } : null)
      : null;
    return {
      id: q.id,
      categorie: q.thematique,
      classe: q.classe || q.niveau || null,
      enonce: q.enonce || null,
      texte_support: q.texte_support || null,
      question: q.question,
      figure,
      // Outils de réponse (droite graduée, repère, tableau) : réglages sans la solution
      outil: Array.isArray(q.outil_reponse) && q.outil_reponse.length ? q.outil_reponse : null,
    };
  }
  async function fetchQuestions(matiere, ids, withCorrige = false) {
    const cols = SOURCE[matiere].cols + (withCorrige ? ', reponse_ideale' : '');
    const { data, error } = await supabaseAdmin.from(SOURCE[matiere].table).select(cols).in('id', ids);
    if (error) throw error;
    const byId = new Map((data || []).map(q => [q.id, q]));
    return ids.map(id => byId.get(id)).filter(Boolean);
  }

  // ── POST /api/entraineur/questions : tire une série de 5 questions au hasard dans la matière ──
  app.post('/api/entraineur/questions', async (req, res) => {
    try {
      const matiere = req.body?.matiere;
      if (!SOURCE[matiere]) return fail(res, 400, 'Matière invalide.');
      const all = await questionPool(matiere);
      if (all.length < QUESTIONS_PER_SET) return fail(res, 503, 'Pas assez de questions disponibles pour le moment.');
      const picked = new Set();
      while (picked.size < QUESTIONS_PER_SET) picked.add(all[crypto.randomInt(all.length)].id);
      const ids = [...picked];
      const questions = await fetchQuestions(matiere, ids);
      res.json({
        matiere,
        token: signSet({ m: matiere, ids, t: Date.now() }),
        questions: questions.map(q => publicQuestion(matiere, q)),
      });
    } catch (e) {
      console.error('[entraineur/questions]', e.message);
      fail(res, 500, 'Impossible de tirer les questions pour le moment.');
    }
  });

  // ── Contact : enregistré dans Supabase et dans Klaviyo (profil ajouté à la liste Lead_magnet_entraineur_crpe) ──
  async function saveLead(b) {
    const prenom = String(b.prenom || '').trim().slice(0, 80);
    const nom = String(b.nom || '').trim().slice(0, 80);
    const email = String(b.email || '').trim().toLowerCase();
    const telephone = String(b.telephone || '').trim();
    const consent_conseils = b.consent_conseils === true;
    const consent_partenaires = b.consent_partenaires === true;
    const consent_contact_sms = b.consent_contact_sms === true;
    if (!prenom || !nom) return { error: 'Merci d\'indiquer ton prénom et ton nom.' };
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || email.length > 254) return { error: 'Adresse e-mail invalide.' };
    const digits = telephone.replace(/\D/g, '');
    if (!/^\+?[\d\s.\-()]{6,30}$/.test(telephone) || digits.length < 9 || digits.length > 15) return { error: 'Numéro de téléphone invalide.' };
    const { data: existing } = await supabaseAdmin.from('entraineur_leads')
      .select('id, telephone, consent_conseils, consent_partenaires, consent_contact_sms').eq('email', email).maybeSingle();
    // Un consentement déjà donné n'est jamais retiré en silence (le retrait passe par le lien de désinscription)
    const row = {
      prenom, nom, email,
      telephone: telephone || existing?.telephone || null,
      consent_conseils: consent_conseils || !!existing?.consent_conseils,
      consent_partenaires: consent_partenaires || !!existing?.consent_partenaires,
      consent_contact_sms: consent_contact_sms || !!existing?.consent_contact_sms,
      consent_version: CONSENT_VERSION, updated_at: new Date().toISOString(),
    };
    const { data: lead, error } = existing
      ? await supabaseAdmin.from('entraineur_leads').update(row).eq('id', existing.id).select('id, prenom, email').single()
      : await supabaseAdmin.from('entraineur_leads').insert(row).select('id, prenom, email').single();
    if (error) throw error;
    return { lead, row };
  }

  function toE164(tel) {
    const t = tel.replace(/[\s.\-()]/g, '');
    if (/^\+\d{8,15}$/.test(t)) return t;
    if (/^00\d{8,15}$/.test(t)) return '+' + t.slice(2);
    if (/^0\d{9}$/.test(t)) return '+33' + t.slice(1);
    return null;
  }

  async function klaviyoAddLead({ prenom, nom, email, telephone, consent_conseils, consent_partenaires, consent_contact_sms }) {
    if (!process.env.KLAVIYO_PRIVATE_API_KEY) throw new Error('KLAVIYO_PRIVATE_API_KEY manquante');
    const phone = telephone ? toE164(telephone) : null;
    const attributes = {
      email, first_name: prenom, last_name: nom,
      ...(phone ? { phone_number: phone } : {}),
      properties: { telephone_saisi: telephone || null, consent_conseils, consent_partenaires, consent_contact_sms, consent_version: CONSENT_VERSION, parcours_signup: 'passcrpe' },
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
    // Ajout à la liste Lead_magnet_entraineur_crpe (chaque personne qui remplit le formulaire)
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
        } }),
      });
      if (!c.ok) throw new Error(`consentement Klaviyo : ${c.status}`);
    }
  }

  // Événement qui déclenche le flow Klaviyo d'envoi du rapport (e-mail transactionnel, envoyé même sans abonnement marketing)
  async function klaviyoReportEvent({ email, prenom, rapportId, matiere, note, synthese, url }) {
    if (!process.env.KLAVIYO_PRIVATE_API_KEY) throw new Error('KLAVIYO_PRIVATE_API_KEY manquante');
    const r = await fetch(`${klaviyoApiBase}/events`, {
      method: 'POST', headers: klaviyoHeaders(),
      body: JSON.stringify({ data: { type: 'event', attributes: {
        properties: {
          report_url: url,
          prenom,
          // Date du rapport déjà rédigée en français, heure de Paris (ex. « 12 octobre 2026 »)
          date_rapport: new Date().toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Europe/Paris' }),
          date_rapport_courte: new Date().toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', year: 'numeric', timeZone: 'Europe/Paris' }),
          // Nom du rapport : prénom_entraineur_crpe_JJ-MM-AAAA (ex. « Marie_entraineur_crpe_12-10-2026 »)
          nom_rapport: `${String(prenom || 'rapport').trim().replace(/\s+/g, '-')}_entraineur_crpe_${new Date().toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', year: 'numeric', timeZone: 'Europe/Paris' }).replace(/\//g, '-')}`,
          // Dernier jour où le lien fonctionne (le rapport est supprimé après 30 jours)
          date_expiration: new Date(Date.now() + (REPORT_RETENTION_DAYS - 1) * 24 * 3600 * 1000).toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Europe/Paris' }),
          matiere: MATIERE_LABEL[matiere],
          note_globale: String(note).replace('.', ','),
          // Même note en nombre, pour filtrer dans Klaviyo (ex. note_globale_nombre < 5)
          note_globale_nombre: Number(note),
          niveau: NIVEAU_LABEL[synthese.niveau],
          appreciation: synthese.appreciation_globale,
          point_cle_1: synthese.points_cles[0] || '',
          point_cle_2: synthese.points_cles[1] || '',
          point_cle_3: synthese.points_cles[2] || '',
        },
        metric: { data: { type: 'metric', attributes: { name: KLAVIYO_REPORT_METRIC } } },
        profile: { data: { type: 'profile', attributes: { email, first_name: prenom } } },
        unique_id: rapportId,
      } } }),
    });
    if (!r.ok) throw new Error(`événement Klaviyo : ${r.status} ${await r.text().catch(() => '')}`);
  }

  // Appel au modèle avec sortie forcée dans un outil ; une nouvelle tentative si le JSON est invalide
  async function callTool(system, tool, content, validate, maxTokens) {
    const usage = { input_tokens: 0, output_tokens: 0 };
    for (let essai = 0; essai < 2; essai++) {
      const msg = await anthropic.messages.create({
        model,
        max_tokens: maxTokens,
        system: [{ type: 'text', text: system, cache_control: { type: 'ephemeral' } }],
        tools: [tool],
        tool_choice: { type: 'tool', name: tool.name },
        messages: [{ role: 'user', content }],
      });
      usage.input_tokens += msg.usage?.input_tokens || 0;
      usage.output_tokens += msg.usage?.output_tokens || 0;
      const out = validate(msg.content.find(c => c.type === 'tool_use' && c.name === tool.name)?.input);
      if (out) return { out, usage };
    }
    return { out: null, usage };
  }

  // ── Copie anonyme pour les contenus pédagogiques : aucune identité, seulement le mois ──
  const escapeRe = t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  function anonymise(text, prenom, nom) {
    let t = String(text || '')
      .replace(/[\w.%+-]+@[\w.-]+\.[a-z]{2,}/gi, '[e-mail]')
      .replace(/(\+33 ?|0033 ?|\b0)[1-9]([ .-]?\d{2}){4}\b/g, '[téléphone]');
    for (const [mot, remplace] of [[prenom, '[prénom]'], [nom, '[nom]']]) {
      if (mot && mot.trim().length >= 2) t = t.replace(new RegExp(`(?<![\\p{L}])${escapeRe(mot.trim())}(?![\\p{L}])`, 'giu'), remplace);
    }
    return t;
  }
  async function saveAnonymousCopy({ items, synthese, matiere, prenom, nom }) {
    const serie_id = crypto.randomUUID();
    const now = new Date();
    const mois = `${now.getUTCFullYear()}-${String(now.getUTCMonth() + 1).padStart(2, '0')}-01`;
    const syntheseAnonyme = JSON.parse(anonymise(JSON.stringify(synthese), prenom, nom));
    const rows = items.map((it, i) => ({
      serie_id, position: i + 1, mois, matiere,
      categorie: it.categorie, classe: it.classe, enonce: it.enonce, texte_support: it.texte_support,
      question: it.question, reponse_attendue: it.reponse_attendue,
      reponse_candidat: anonymise(it.reponse, prenom, nom),
      note: it.evaluation.note, niveau: it.evaluation.niveau,
      evaluation: JSON.parse(anonymise(JSON.stringify(it.evaluation), prenom, nom)),
      synthese_serie: syntheseAnonyme, model, created_at: `${mois}T00:00:00Z`,
    }));
    try {
      const { error } = await supabaseAdmin.from('entraineur_corpus').insert(rows);
      if (error) throw error;
    } catch (e) {
      console.error('[entraineur/corpus]', e.message);
    }
  }

  // Suppression définitive des rapports personnels (et réponses) après le délai, y compris les données de l'ancien parcours
  async function purgeOldReports() {
    const cutoff = new Date(Date.now() - REPORT_RETENTION_DAYS * 24 * 3600 * 1000).toISOString();
    try {
      await supabaseAdmin.from('entraineur_rapports').delete().lt('created_at', cutoff);
      await supabaseAdmin.from('entraineur_questions_servies').delete().lt('served_at', cutoff);
    } catch (e) {
      console.error('[entraineur/purge]', e.message);
    }
  }

  // ── POST /api/entraineur/rapport : formulaire + réponses → rapport détaillé, puis e-mail via Klaviyo ──
  app.post('/api/entraineur/rapport', async (req, res) => {
    try {
      const set = readSet(req.body?.token);
      if (!set) return fail(res, 400, 'Ta série de questions a expiré. Recommence une nouvelle série.');
      const reponses = Array.isArray(req.body?.reponses) ? req.body.reponses.map(r => String(r || '').trim()) : [];
      if (reponses.length !== QUESTIONS_PER_SET) return fail(res, 400, 'Réponses incomplètes.');
      if (reponses.some(r => r.length > MAX_ANSWER_LENGTH)) return fail(res, 400, `Chaque réponse est limitée à ${MAX_ANSWER_LENGTH} caractères.`);
      if (reponses.some(r => r.length === 0)) return fail(res, 400, `Réponds aux ${QUESTIONS_PER_SET} questions avant de demander ton rapport.`);

      const saved = await saveLead(req.body || {});
      if (saved.error) return fail(res, 400, saved.error);
      const { lead, row } = saved;

      // Klaviyo : profil ajouté à la liste (avant le contrôle de limite : le contact est enregistré dans tous les cas)
      try { await klaviyoAddLead(row); await supabaseAdmin.from('entraineur_leads').update({ klaviyo_synced_at: new Date().toISOString() }).eq('id', lead.id); }
      catch (e) { console.error('[entraineur/klaviyo lead]', e.message); }

      // Limite : 1 rapport par adresse e-mail et par semaine
      const start = parisWeekStart();
      const { count } = await supabaseAdmin.from('entraineur_rapports')
        .select('id', { count: 'exact', head: true }).eq('lead_id', lead.id).gte('created_at', start.toISOString());
      if ((count || 0) >= WEEKLY_REPORT_LIMIT) return fail(res, 429, 'weekly_limit', { resetAt: nextReset(start).toISOString() });

      // Correction : les 5 réponses et la synthèse sur la manière de répondre, toutes en parallèle (temps limité sur Vercel)
      const rows = await fetchQuestions(set.m, set.ids, true);
      if (rows.length !== QUESTIONS_PER_SET) return fail(res, 409, 'Une question n\'est plus disponible. Recommence une nouvelle série.');
      const items = rows.map((q, i) => ({ ...publicQuestion(set.m, q), reponse: reponses[i], reponse_attendue: q.reponse_ideale }));
      const vide = { out: { note: 0, niveau: 'a_retravailler', appreciation: 'Pas de réponse.', points_forts: [], points_a_ameliorer: [],
        elements_manquants: ['Une réponse rédigée'], langue: [], explication: 'Consulte la réponse attendue ci-dessous.' }, usage: { input_tokens: 0, output_tokens: 0 } };
      const [synth, ...evals] = await Promise.all([
        callTool(synthesePrompt(set.m), SYNTHESE_TOOL, syntheseMessage({ matiere: set.m, items }), validateSynthese, 3000),
        ...items.map(it => it.reponse
          ? callTool(questionPrompt(set.m), QUESTION_TOOL, questionMessage({ matiere: set.m, q: it, reponse: it.reponse }), validateQuestion, 1800)
          : Promise.resolve(vide)),
      ]);
      if (!synth.out || evals.some(e => !e.out)) return fail(res, 502, 'Le rapport n\'a pas pu être généré. Réessaie dans quelques instants.');
      items.forEach((it, i) => { it.evaluation = evals[i].out; });

      const note = Math.round(items.reduce((n, it) => n + it.evaluation.note, 0) / items.length * 2) / 2;
      const usage = [...evals, synth].reduce((u, e) => ({ input_tokens: u.input_tokens + e.usage.input_tokens, output_tokens: u.output_tokens + e.usage.output_tokens }), { input_tokens: 0, output_tokens: 0 });
      const token = crypto.randomBytes(24).toString('base64url');
      const { data: rapport, error } = await supabaseAdmin.from('entraineur_rapports').insert({
        token, lead_id: lead.id, matiere: set.m, questions: items, synthese: synth.out, note, model, ...usage,
      }).select('id').single();
      if (error) throw error;

      await saveAnonymousCopy({ items, synthese: synth.out, matiere: set.m, prenom: row.prenom, nom: row.nom });
      await purgeOldReports();
      const url = `${SITE}${REPORT_PATH}${token}`;
      let emailed = false;
      try {
        await klaviyoReportEvent({ email: lead.email, prenom: lead.prenom, rapportId: rapport.id, matiere: set.m, note, synthese: synth.out, url });
        await supabaseAdmin.from('entraineur_rapports').update({ klaviyo_event_at: new Date().toISOString() }).eq('id', rapport.id);
        emailed = true;
      } catch (e) {
        console.error('[entraineur/klaviyo event]', e.message);
      }
      // Si l'e-mail n'a pas pu partir, le candidat reçoit directement son lien pour ne pas perdre son rapport
      res.json({ ok: true, emailed, email: lead.email, ...(emailed ? {} : { report_url: `${REPORT_PATH}${token}` }) });
    } catch (e) {
      console.error('[entraineur/rapport]', e.status || '', e.error?.error?.type || '', e.error?.error?.message || e.message);
      fail(res, 500, 'Le rapport n\'a pas pu être généré. Réessaie dans quelques instants.');
    }
  });

  // ── GET /api/entraineur/rapport/:token : contenu du rapport (lien personnel reçu par e-mail) ──
  app.get('/api/entraineur/rapport/:token', async (req, res) => {
    try {
      const token = String(req.params.token || '');
      if (!/^[A-Za-z0-9_-]{32,64}$/.test(token)) return fail(res, 404, 'Rapport introuvable.');
      const { data: r } = await supabaseAdmin.from('entraineur_rapports')
        .select('matiere, questions, synthese, note, created_at, entraineur_leads(prenom)').eq('token', token).maybeSingle();
      if (!r || Date.now() - new Date(r.created_at).getTime() > REPORT_RETENTION_DAYS * 24 * 3600 * 1000) return fail(res, 404, 'Rapport introuvable.');
      res.setHeader('Cache-Control', 'private, no-store');
      res.setHeader('X-Robots-Tag', 'noindex');
      res.json({
        prenom: r.entraineur_leads?.prenom || '',
        matiere: r.matiere,
        note: r.note,
        created_at: r.created_at,
        synthese: r.synthese,
        questions: r.questions.map(({ id, ...q }) => q),
      });
    } catch (e) {
      console.error('[entraineur/rapport get]', e.message);
      fail(res, 500, 'Impossible d\'afficher le rapport pour le moment.');
    }
  });
}

// Intitulés « Je sais… » des notions (écran « Mes notions ») : générés par Claude à partir des questions de chaque notion.
//
//   node scripts/quiz/intitules.mjs                       génère scripts/quiz/intitules-proposes.json (reprend là où il s'est arrêté)
//   node scripts/quiz/intitules.mjs --matiere svt         une seule matière
//   node scripts/quiz/intitules.mjs --appliquer           écrit les intitulés relus dans quiz_notions.intitule (seulement les vides)
//   node scripts/quiz/intitules.mjs --appliquer --remplacer   … en remplaçant aussi ceux déjà écrits
//
// La génération ne touche pas à la base : on relit le fichier JSON (on peut le corriger à la main), puis on applique.
// Lit VITE_SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY et ANTHROPIC_API_KEY_CRPE_APP dans .env.
import fs from 'fs';
import Anthropic from '@anthropic-ai/sdk';
import { createClient } from '@supabase/supabase-js';

const env = Object.fromEntries(fs.readFileSync('.env', 'utf8').split('\n').filter(l => /^\s*[A-Z_]+\s*=/.test(l))
  .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim().replace(/^["']|["']$/g, '')]; }));
const sb = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY);
const SORTIE = 'scripts/quiz/intitules-proposes.json';
const args = process.argv.slice(2);
const option = n => { const i = args.indexOf(n); return i >= 0 ? (args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true) : null; };

// Lecture paginée (Supabase renvoie au plus 1 000 lignes par requête)
async function tout(requete) {
  const lignes = [];
  for (let from = 0; ; from += 1000) {
    const { data, error } = await requete().range(from, from + 999);
    if (error) throw new Error(error.message);
    lignes.push(...data);
    if (data.length < 1000) return lignes;
  }
}

// ── Application des intitulés relus ──
if (option('--appliquer')) {
  const proposes = JSON.parse(fs.readFileSync(SORTIE, 'utf8'));
  const remplacer = !!option('--remplacer');
  const existants = new Map((await tout(() => sb.from('quiz_notions').select('matiere, notion, intitule')))
    .map(n => [n.matiere + '|' + n.notion, n.intitule]));
  let n = 0;
  for (const [cle, intitule] of Object.entries(proposes)) {
    if (!existants.has(cle) || (existants.get(cle) && !remplacer)) continue;
    const [matiere, notion] = cle.split('|');
    const { error } = await sb.from('quiz_notions').update({ intitule }).eq('matiere', matiere).eq('notion', notion);
    if (error) { console.error(cle, error.message); process.exit(1); }
    n++;
  }
  console.log(n, 'intitulés écrits dans quiz_notions');
  process.exit(0);
}

// ── Génération ──
const client = new Anthropic({
  apiKey: env.ANTHROPIC_API_KEY_CRPE_APP,
  ...(env.ANTHROPIC_WORKSPACE_ID_CRPE_APP ? { defaultHeaders: { 'anthropic-workspace-id': env.ANTHROPIC_WORKSPACE_ID_CRPE_APP } } : {}),
});
const MODELE = 'claude-opus-5-5';
const PRIX = { entree: 4 / 1e6, sortie: 20 / 1e6 }; // $ par token (Claude Opus 5.5)

const SYSTEME = `Tu rédiges les intitulés des notions d'un quiz de révision du CRPE (concours de professeur des écoles), programme du cycle 4.
Chaque notion est travaillée par plusieurs questions (fournies avec leur bonne réponse). Pour chaque notion, écris UN intitulé :
- formulé comme une compétence, qui commence exactement par « Je sais » suivi d'un verbe d'action à l'infinitif (reconnaître, calculer, identifier, situer, expliquer, conjuguer, distinguer, citer, dater…) ;
- qui décrit ce que les questions vérifient vraiment, de façon précise et concrète (pas l'intitulé général du programme) ;
- sur une seule ligne, 60 à 100 caractères de préférence, jamais plus de 110 ;
- en français correct, sans point final, sans guillemets autour, sans abréviation obscure ; les mots anglais éventuels (anglais) restent en anglais ;
- deux notions différentes d'un même thème doivent avoir des intitulés différents.
Exemples : « Je sais reconnaître les parallélogrammes particuliers (rectangle, losange, carré) », « Je sais additionner deux fractions de dénominateurs différents », « Je sais situer le couronnement de Charlemagne dans le temps ».
Réponds avec un intitulé pour chaque clé de notion reçue, sans en oublier ni en inventer.`;

const SCHEMA = {
  type: 'object', additionalProperties: false, required: ['intitules'],
  properties: { intitules: { type: 'array', items: {
    type: 'object', additionalProperties: false, required: ['notion', 'intitule'],
    properties: { notion: { type: 'string' }, intitule: { type: 'string' } } } } },
};

const valide = t => typeof t === 'string' && /^Je sais [a-zà-ÿ]/.test(t) && !/\n/.test(t) && t.length <= 110;
// Réponse lisible d'une question (mots à cliquer : indices → mots)
const reponseLisible = q => q.type === 'cliquer_mot' ? String(q.reponse).split(',').map(i => (q.choix || [])[Number(i)]).join(' ') : String(q.reponse);

const notions = await tout(() => sb.from('quiz_notions').select('matiere, notion, theme, sous_theme, classe, niveau').order('matiere').order('ordre'));
const questions = await tout(() => sb.from('quiz_questions').select('matiere, notion, type, question, choix, reponse').eq('actif', true).order('id'));
const parNotion = new Map();
for (const q of questions) { const k = q.matiere + '|' + q.notion; if (!parNotion.has(k)) parNotion.set(k, []); parNotion.get(k).push(q); }

const resultat = fs.existsSync(SORTIE) ? JSON.parse(fs.readFileSync(SORTIE, 'utf8')) : {};
const matiere = option('--matiere');
const aFaire = notions.filter(n => (!matiere || n.matiere === matiere) && !valide(resultat[n.matiere + '|' + n.notion]));
// Un appel par thème (au plus 40 notions par appel)
const lots = [];
for (const n of aFaire) {
  const dernier = lots[lots.length - 1];
  if (dernier && dernier.cle === n.matiere + '|' + n.theme && dernier.notions.length < 40) dernier.notions.push(n);
  else lots.push({ cle: n.matiere + '|' + n.theme, matiere: n.matiere, theme: n.theme, notions: [n] });
}
console.log(aFaire.length, 'notions à traiter en', lots.length, 'appels');

let entree = 0, sortie = 0, faits = 0;
async function traiter(lot, essai = 1) {
  const donnees = lot.notions.map(n => ({
    notion: n.notion, sous_theme: n.sous_theme, classe: n.classe || 'cycle 4', niveau: n.niveau,
    questions: (parNotion.get(n.matiere + '|' + n.notion) || []).map(q => ({ question: q.question, bonne_reponse: reponseLisible(q) })),
  }));
  const reponse = await client.messages.create({
    model: MODELE, max_tokens: 16000, system: SYSTEME,
    messages: [{ role: 'user', content: `Matière : ${lot.matiere}\nThème : ${lot.theme}\n\nNotions :\n${JSON.stringify(donnees, null, 1)}` }],
    output_config: { format: { type: 'json_schema', schema: SCHEMA } },
    fallbacks: 'default',
  }, { headers: { 'anthropic-beta': 'server-side-fallback-2026-07-01' } });
  entree += (reponse.usage?.input_tokens || 0) + (reponse.usage?.cache_read_input_tokens || 0);
  sortie += reponse.usage?.output_tokens || 0;
  if (reponse.stop_reason === 'refusal') throw new Error('refus (' + (reponse.stop_details?.category || '?') + ')');
  if (reponse.stop_reason === 'max_tokens') throw new Error('réponse tronquée');
  const texte = reponse.content.filter(b => b.type === 'text').map(b => b.text).join('');
  const recus = new Map(JSON.parse(texte).intitules.map(x => [x.notion, x.intitule.trim().replace(/\.$/, '')]));
  const manquants = [];
  for (const n of lot.notions) {
    const t = recus.get(n.notion);
    if (valide(t)) resultat[n.matiere + '|' + n.notion] = t; else manquants.push(n);
  }
  faits += lot.notions.length - manquants.length;
  fs.writeFileSync(SORTIE, JSON.stringify(resultat, null, 1));
  if (manquants.length && essai < 3) return traiter({ ...lot, notions: manquants }, essai + 1);
  if (manquants.length) console.warn('  sans intitulé valide :', manquants.map(n => n.notion).join(', '));
}

// 4 appels en parallèle ; un appel en erreur est retenté, puis signalé sans arrêter les autres
const file = [...lots];
await Promise.all(Array.from({ length: 4 }, async () => {
  for (let lot; (lot = file.shift());) {
    for (let essai = 1; ; essai++) {
      try { await traiter(lot); break; }
      catch (e) {
        if (essai >= 3) { console.error('  échec', lot.cle, ':', e.message); break; }
        await new Promise(r => setTimeout(r, 5000 * essai));
      }
    }
    console.log(`${faits} / ${aFaire.length} · ${lot.cle} · ~${(entree * PRIX.entree + sortie * PRIX.sortie).toFixed(2)} $`);
  }
}));
console.log(`Terminé : ${Object.keys(resultat).length} intitulés dans ${SORTIE} · ${entree} tokens en entrée, ${sortie} en sortie · ~${(entree * PRIX.entree + sortie * PRIX.sortie).toFixed(2)} $`);

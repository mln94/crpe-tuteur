// Insère en base les exercices « Intermédiaire » rédigés dans francais/lot*.json et maths/lot*.json.
// Chaque exercice reprend de sa version facile (source_id) : classe, objectif, sous-catégorie, et pour le français le texte
// support ; la synthèse de cours et les définitions sont reprises du facile sauf si le lot en fournit.
// Sans doublon : un objectif n'a qu'une version intermédiaire (déjà présente → ignorée).
//
//   node scripts/exercices_intermediaires/inserer.mjs            (tous les lots)
//   node scripts/exercices_intermediaires/inserer.mjs --essai    (affiche sans insérer)
import fs from 'node:fs';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';

const ICI = path.dirname(new URL(import.meta.url).pathname), RACINE = path.resolve(ICI, '../..');
const env = Object.fromEntries(fs.readFileSync(path.join(RACINE, '.env'), 'utf8').split('\n').filter(l => l.includes('=') && !l.trim().startsWith('#'))
  .map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim().replace(/^["']|["']$/g, '')]));
const sb = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY);
const ESSAI = process.argv.includes('--essai');

const lots = (dossier) => {
  const d = path.join(ICI, dossier);
  if (!fs.existsSync(d)) return [];
  return fs.readdirSync(d).filter(f => /^lot\d+\.json$/.test(f)).sort()
    .flatMap(f => JSON.parse(fs.readFileSync(path.join(d, f), 'utf8')).map(x => ({ ...x, lot: f })));
};
const verifier = (x, champs) => { for (const c of champs) if (!x[c] || !String(x[c]).trim()) throw new Error(`${x.lot} #${x.source_id} : champ « ${c} » vide`); };

// ── Français ──
async function francais() {
  const items = lots('francais');
  if (!items.length) return;
  const { data: src, error } = await sb.from('exercices_français').select('*').in('id', items.map(x => x.source_id));
  if (error) throw new Error(error.message);
  const parId = new Map(src.map(r => [r.id, r]));
  const { data: deja } = await sb.from('exercices_français').select('objectif_id,niveau').eq('niveau_difficulte', 'Intermédiaire');
  const existe = new Set((deja || []).map(r => `${r.objectif_id}|${r.niveau}`));
  const lignes = [];
  for (const x of items) {
    verifier(x, ['question', 'reponse_ideale']);
    const f = parId.get(x.source_id);
    if (!f) throw new Error(`français #${x.source_id} introuvable`);
    if (f.niveau_difficulte !== 'Facile') throw new Error(`français #${x.source_id} n'est pas un exercice facile`);
    if (existe.has(`${f.objectif_id}|${f.niveau}`)) continue;
    lignes.push({
      matiere: f.matiere, niveau: f.niveau, objectif_apprentissage: f.objectif_apprentissage, objectif_id: f.objectif_id,
      texte_support: x.texte_support ?? f.texte_support, question: x.question, reponse_ideale: x.reponse_ideale,
      niveau_difficulte: 'Intermédiaire',
      synthese_cours: x.synthese_cours ?? f.synthese_cours, definition_mots_cles: x.definition_mots_cles ?? f.definition_mots_cles,
      conseil_paragraphe_argumente: x.conseil_paragraphe_argumente ?? f.conseil_paragraphe_argumente,
    });
  }
  console.log(`français : ${items.length} rédigé(s), ${lignes.length} à insérer`);
  if (!ESSAI && lignes.length) { const { error: e } = await sb.from('exercices_français').insert(lignes); if (e) throw new Error(e.message); }
}

// ── Maths ──
async function maths() {
  const items = lots('maths');
  if (!items.length) return;
  const { data: src, error } = await sb.from('exercices_maths').select('*').in('id', items.map(x => x.source_id));
  if (error) throw new Error(error.message);
  const parId = new Map(src.map(r => [r.id, r]));
  const { data: deja } = await sb.from('exercices_maths').select('objectif_id,classe').eq('niveau_difficulte', 'Intermédiaire');
  const existe = new Set((deja || []).map(r => `${r.objectif_id}|${r.classe}`));
  const lignes = [];
  for (const x of items) {
    verifier(x, ['enonce', 'question', 'reponse_ideale']);
    const f = parId.get(x.source_id);
    if (!f) throw new Error(`maths #${x.source_id} introuvable`);
    if (f.niveau_difficulte !== 'Facile') throw new Error(`maths #${x.source_id} n'est pas un exercice facile`);
    if (existe.has(`${f.objectif_id}|${f.classe}`)) continue;
    lignes.push({
      objectif_id: f.objectif_id, objectif_apprentissage: f.objectif_apprentissage, thematique: f.thematique, sous_categorie: f.sous_categorie,
      classe: f.classe, niveau_difficulte: 'Intermédiaire', enonce: x.enonce, question: x.question, reponse_ideale: x.reponse_ideale,
      synthese_cours: x.synthese_cours ?? f.synthese_cours, definition_mots_cles: x.definition_mots_cles ?? f.definition_mots_cles,
      figure_svg: null, figure_path: null, figure_masquee: false, outil_reponse: x.outil_reponse ?? null,
    });
  }
  console.log(`maths : ${items.length} rédigé(s), ${lignes.length} à insérer`);
  if (!ESSAI && lignes.length) { const { error: e } = await sb.from('exercices_maths').insert(lignes); if (e) throw new Error(e.message); }
}

await francais();
await maths();
console.log(ESSAI ? 'Essai : rien n’a été inséré.' : 'Insertion terminée.');

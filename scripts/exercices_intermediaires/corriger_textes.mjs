// Corrige les textes supports français dont la citation est inventée ou mal attribuée.
// Lit corrections/lot*.json : [{ id, texte_support, question?, reponse_ideale?, remplacements? }] (id = exercice « Facile »).
// remplacements : [[ancien, nouveau], …] appliqués à la question et à la correction du facile et des intermédiaires liés.
// Met à jour l'exercice facile, puis les exercices « Intermédiaire » qui partagent encore l'ancien texte.
//
//   node scripts/exercices_intermediaires/corriger_textes.mjs           (applique)
//   node scripts/exercices_intermediaires/corriger_textes.mjs --essai   (affiche sans écrire)
import fs from 'node:fs';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';

const ICI = path.dirname(new URL(import.meta.url).pathname), RACINE = path.resolve(ICI, '../..');
const env = Object.fromEntries(fs.readFileSync(path.join(RACINE, '.env'), 'utf8').split('\n').filter(l => l.includes('=') && !l.trim().startsWith('#'))
  .map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim().replace(/^["']|["']$/g, '')]));
const sb = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY);
const ESSAI = process.argv.includes('--essai');
const T = 'exercices_français';

const d = path.join(ICI, 'corrections');
const items = fs.existsSync(d) ? fs.readdirSync(d).filter(f => /^lot\d+\.json$/.test(f)).sort()
  .flatMap(f => JSON.parse(fs.readFileSync(path.join(d, f), 'utf8')).map(x => ({ ...x, lot: f }))) : [];

let faits = 0, inter = 0, deja = 0;
for (const x of items) {
  if (!x.texte_support?.trim()) throw new Error(`${x.lot} #${x.id} : texte_support vide`);
  const { data: f, error } = await sb.from(T).select('id,texte_support,question,reponse_ideale,niveau_difficulte').eq('id', x.id).single();
  if (error) throw new Error(`#${x.id} : ${error.message}`);
  if (f.niveau_difficulte !== 'Facile') throw new Error(`#${x.id} n'est pas un exercice facile`);
  if (f.texte_support === x.texte_support) { deja++; continue; }
  const remp = (s) => (x.remplacements || []).reduce((acc, [a, b]) => acc.split(a).join(b), s || '');
  const maj = { texte_support: x.texte_support, question: x.question || remp(f.question), reponse_ideale: x.reponse_ideale || remp(f.reponse_ideale) };
  const { data: freres } = await sb.from(T).select('id,question,reponse_ideale').eq('niveau_difficulte', 'Intermédiaire').eq('texte_support', f.texte_support);
  if (ESSAI) { console.log(`#${x.id} (${x.lot}) → ${Object.keys(maj).join(', ')} ; intermédiaires liés : ${(freres || []).map(r => r.id).join(', ') || 'aucun'}`); continue; }
  const { error: e1 } = await sb.from(T).update(maj).eq('id', x.id);
  if (e1) throw new Error(`#${x.id} : ${e1.message}`);
  for (const r of freres || []) {
    const { error: e2 } = await sb.from(T).update({ texte_support: x.texte_support, question: remp(r.question), reponse_ideale: remp(r.reponse_ideale) }).eq('id', r.id);
    if (e2) throw new Error(`#${x.id} intermédiaire #${r.id} : ${e2.message}`);
    inter++;
  }
  faits++;
}
console.log(`${faits} exercice(s) facile(s) corrigé(s), ${inter} intermédiaire(s) mis à jour, ${deja} déjà à jour.`);

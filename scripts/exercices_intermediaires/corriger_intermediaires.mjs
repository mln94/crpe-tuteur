// Applique des remplacements de texte aux exercices « Intermédiaire » français (question et correction),
// en base et dans francais/lot*.json. Lit corrections/inter*.json : [{ source_id, remplacements: [[ancien, nouveau], …] }].
//   node scripts/exercices_intermediaires/corriger_intermediaires.mjs
import fs from 'node:fs';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';

const ICI = path.dirname(new URL(import.meta.url).pathname), RACINE = path.resolve(ICI, '../..');
const env = Object.fromEntries(fs.readFileSync(path.join(RACINE, '.env'), 'utf8').split('\n').filter(l => l.includes('=') && !l.trim().startsWith('#'))
  .map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim().replace(/^["']|["']$/g, '')]));
const sb = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY);
const T = 'exercices_français';
const C = path.join(ICI, 'corrections');
const REP = new Map(fs.readdirSync(C).filter(f => /^inter\d+\.json$/.test(f)).sort()
  .flatMap(f => JSON.parse(fs.readFileSync(path.join(C, f), 'utf8'))).map(x => [x.source_id, x.remplacements]));
const remp = (s, l) => l.reduce((a, [x, y]) => a.split(x).join(y), s || '');

let n = 0;
for (const [id, l] of REP) {
  const { data: f, error } = await sb.from(T).select('texte_support').eq('id', id).single();
  if (error) throw new Error(`#${id} : ${error.message}`);
  const { data: rs } = await sb.from(T).select('id,question,reponse_ideale').eq('niveau_difficulte', 'Intermédiaire').eq('texte_support', f.texte_support);
  for (const r of rs || []) {
    const maj = { question: remp(r.question, l), reponse_ideale: remp(r.reponse_ideale, l) };
    if (maj.question === r.question && maj.reponse_ideale === r.reponse_ideale) continue;
    const { error: e } = await sb.from(T).update(maj).eq('id', r.id);
    if (e) throw new Error(`#${r.id} : ${e.message}`);
    n++;
  }
}
const D = path.join(ICI, 'francais');
for (const fic of fs.readdirSync(D).filter(f => /^lot\d+\.json$/.test(f))) {
  const p = path.join(D, fic), a = JSON.parse(fs.readFileSync(p, 'utf8'));
  let modif = false;
  for (const x of a) if (REP.has(x.source_id)) {
    const q = remp(x.question, REP.get(x.source_id)), r = remp(x.reponse_ideale, REP.get(x.source_id));
    if (q !== x.question || r !== x.reponse_ideale) { x.question = q; x.reponse_ideale = r; modif = true; }
  }
  if (modif) fs.writeFileSync(p, JSON.stringify(a, null, 2) + '\n');
}
console.log(`${n} exercice(s) intermédiaire(s) mis à jour en base.`);

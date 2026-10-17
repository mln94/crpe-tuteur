// Insère les questions d'un fichier JSON (sortie de construire.py) dans quiz_questions.
// Une matière qui a déjà des questions rattachées à des notions est ignorée ; les anciennes questions
// sans notion de la matière sont désactivées (jamais supprimées).
// Usage (depuis la racine du projet) : node scripts/quiz/inserer.mjs lignes.json
import { createClient } from '@supabase/supabase-js';
import fs from 'fs';
const env = Object.fromEntries(fs.readFileSync('.env', 'utf8').split('\n').filter(l => /^\s*[A-Z_]+\s*=/.test(l))
  .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim().replace(/^["']|["']$/g, '')]; }));
const sb = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY);
const rows = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
for (const matiere of [...new Set(rows.map(r => r.matiere))]) {
  const { count } = await sb.from('quiz_questions').select('id', { count: 'exact', head: true }).eq('matiere', matiere).not('notion', 'is', null);
  if (count) { console.log(matiere, ': déjà', count, 'questions, rien inséré'); continue; }
  const lot = rows.filter(r => r.matiere === matiere);
  for (let i = 0; i < lot.length; i += 200) {
    const { error } = await sb.from('quiz_questions').insert(lot.slice(i, i + 200));
    if (error) { console.error(matiere, error); process.exit(1); }
  }
  const { count: n } = await sb.from('quiz_questions').update({ actif: false }, { count: 'exact' }).eq('matiere', matiere).is('notion', null);
  console.log(matiere, ':', lot.length, 'questions insérées ;', n, 'anciennes désactivées');
}

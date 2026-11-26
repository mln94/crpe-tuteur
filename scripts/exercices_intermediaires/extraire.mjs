// Extrait les exercices « Facile » (français et maths) dans sources.json : modèles des versions « Intermédiaire »
import fs from 'node:fs';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';
const ICI = path.dirname(new URL(import.meta.url).pathname), RACINE = path.resolve(ICI, '../..');
const env = Object.fromEntries(fs.readFileSync(path.join(RACINE, '.env'), 'utf8').split('\n').filter(l => l.includes('=') && !l.trim().startsWith('#'))
  .map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim().replace(/^["']|["']$/g, '')]));
const sb = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY);
const { data: fr, error: e1 } = await sb.from('exercices_francais_v').select('id,niveau,thematique,sous_categorie,objectif,texte_support,question,reponse_ideale').eq('niveau_difficulte', 'Facile').order('id');
const { data: ma, error: e2 } = await sb.from('exercices_maths').select('id,classe,thematique,sous_categorie,objectif_apprentissage,enonce,question,reponse_ideale').eq('niveau_difficulte', 'Facile').order('id');
if (e1 || e2) throw new Error((e1 || e2).message);
fs.writeFileSync(path.join(ICI, 'sources.json'), JSON.stringify({ francais: fr, maths: ma }, null, 1));
console.log(`français : ${fr.length} · maths : ${ma.length}`);

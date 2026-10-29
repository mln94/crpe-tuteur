// Klaviyo : essai_fait_quizcrpe (true / false) pour tous les comptes du quiz déjà dans Klaviyo. Source : quiz_comptes.essai_fait.
// Ensuite, le serveur la tient à jour (false au premier test de positionnement, true à la première question de l'essai).
// Usage : node scripts/klaviyo_sync_essai_fait.mjs          (simulation)
//         node scripts/klaviyo_sync_essai_fait.mjs --apply  (écriture dans Klaviyo)
import 'dotenv/config';
import { createClient } from '@supabase/supabase-js';

const APPLY = process.argv.includes('--apply');
const KEY = process.env.KLAVIYO_PRIVATE_API_KEY;
if (!KEY) { console.error('KLAVIYO_PRIVATE_API_KEY manquante (.env)'); process.exit(1); }
const headers = { Authorization: `Klaviyo-API-Key ${KEY}`, revision: '2026-04-15', 'Content-Type': 'application/json', accept: 'application/json' };
const sb = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });

const { data: quiz, error } = await sb.from('quiz_comptes').select('email, essai_fait');
if (error) throw error;

const bilan = { maj: 0, aJour: 0, absent: 0, echec: 0 };
for (const q of quiz) {
  if (!q.email) continue;
  const r = await fetch(`https://a.klaviyo.com/api/profiles/?filter=equals(email,"${encodeURIComponent(q.email)}")`, { headers });
  const p = (await r.json()).data?.[0];
  if (!p) { bilan.absent++; continue; }
  if (p.attributes?.properties?.essai_fait_quizcrpe === q.essai_fait) { bilan.aJour++; continue; }
  console.log(`${q.email.padEnd(45)} essai_fait_quizcrpe = ${q.essai_fait}`);
  bilan.maj++;
  if (APPLY) {
    const m = await fetch(`https://a.klaviyo.com/api/profiles/${p.id}/`, { method: 'PATCH', headers,
      body: JSON.stringify({ data: { type: 'profile', id: p.id, attributes: { properties: { essai_fait_quizcrpe: q.essai_fait } } } }) });
    if (!m.ok) { bilan.echec++; console.error(`  échec ${m.status} : ${await m.text()}`); }
  }
}
console.log(`${quiz.length} comptes du quiz.`, APPLY ? 'Écrit dans Klaviyo :' : 'Simulation (rien écrit) :', bilan);

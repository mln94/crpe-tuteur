// Klaviyo : date_creation_compte (date d'inscription) et date_dernier_essai_quizcrpe (dernière question gratuite du quiz)
// pour tous les comptes déjà dans Klaviyo. Sources : auth.users.created_at, quiz_comptes.essai_derniere_question_at.
// Les comptes absents de Klaviyo sont laissés de côté. Retire aussi date_dernier_signin (propriété abandonnée).
// Ensuite, le serveur tient ces dates à jour (inscription : POST /api/webhook/supabase-auth ; essai : POST /api/quiz/reponse).
// Usage : node scripts/klaviyo_sync_dates_compte.mjs          (simulation)
//         node scripts/klaviyo_sync_dates_compte.mjs --apply  (écriture dans Klaviyo)
import 'dotenv/config';
import { createClient } from '@supabase/supabase-js';

const APPLY = process.argv.includes('--apply');
const KEY = process.env.KLAVIYO_PRIVATE_API_KEY;
if (!KEY) { console.error('KLAVIYO_PRIVATE_API_KEY manquante (.env)'); process.exit(1); }
const headers = { Authorization: `Klaviyo-API-Key ${KEY}`, revision: '2026-04-15', 'Content-Type': 'application/json', accept: 'application/json' };
const sb = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });

const users = [];
for (let page = 1; ; page++) {
  const { data, error } = await sb.auth.admin.listUsers({ page, perPage: 1000 });
  if (error) throw error;
  users.push(...data.users);
  if (data.users.length < 1000) break;
}

const { data: quiz, error: eq } = await sb.from('quiz_comptes').select('user_id, essai_derniere_question_at');
if (eq) throw eq;
const essai = new Map(quiz.filter(q => q.essai_derniere_question_at).map(q => [q.user_id, q.essai_derniere_question_at]));

// Format « 2026-10-27T13:08:26Z » (ISO 8601 sans fractions de seconde), reconnu comme date par Klaviyo
const dateKlaviyo = d => new Date(d).toISOString().slice(0, 19) + 'Z';

const bilan = { maj: 0, aJour: 0, absent: 0, sansEmail: 0, echec: 0 };
for (const u of users) {
  if (!u.email) { bilan.sansEmail++; continue; }
  const dates = { date_creation_compte: dateKlaviyo(u.created_at), ...(essai.has(u.id) ? { date_dernier_essai_quizcrpe: dateKlaviyo(essai.get(u.id)) } : {}) };
  const r = await fetch(`https://a.klaviyo.com/api/profiles/?filter=equals(email,"${encodeURIComponent(u.email)}")`, { headers });
  const p = (await r.json()).data?.[0];
  if (!p) { bilan.absent++; continue; }
  const props = p.attributes?.properties || {};
  if (!('date_dernier_signin' in props) && Object.entries(dates).every(([k, v]) => props[k] === v)) { bilan.aJour++; continue; }
  console.log(`${u.email.padEnd(45)} inscription ${u.created_at.slice(0, 10)}  dernier essai ${(essai.get(u.id) || '—').slice(0, 10)}`);
  bilan.maj++;
  if (APPLY) {
    const m = await fetch(`https://a.klaviyo.com/api/profiles/${p.id}/`, { method: 'PATCH', headers,
      body: JSON.stringify({ data: { type: 'profile', id: p.id, attributes: { properties: dates },
        meta: { patch_properties: { unset: ['date_dernier_signin'] } } } }) });
    if (!m.ok) { bilan.echec++; console.error(`  échec ${m.status} : ${await m.text()}`); }
  }
}
console.log(`${users.length} comptes.`, APPLY ? 'Écrit dans Klaviyo :' : 'Simulation (rien écrit) :', bilan);

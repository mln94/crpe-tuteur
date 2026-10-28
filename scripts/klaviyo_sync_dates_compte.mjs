// Klaviyo : date_creation_compte et date_dernier_signin pour tous les comptes déjà dans Klaviyo.
// Source : auth.users.created_at et last_sign_in_at. Les comptes absents de Klaviyo sont laissés de côté.
// Ensuite, le serveur tient ces dates à jour (POST /api/webhook/supabase-auth : INSERT et SIGNIN).
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

const bilan = { maj: 0, aJour: 0, absent: 0, sansEmail: 0, echec: 0 };
for (const u of users) {
  if (!u.email) { bilan.sansEmail++; continue; }
  const dates = { date_creation_compte: u.created_at, ...(u.last_sign_in_at ? { date_dernier_signin: u.last_sign_in_at } : {}) };
  const r = await fetch(`https://a.klaviyo.com/api/profiles/?filter=equals(email,"${encodeURIComponent(u.email)}")`, { headers });
  const p = (await r.json()).data?.[0];
  if (!p) { bilan.absent++; continue; }
  const props = p.attributes?.properties || {};
  if (Object.entries(dates).every(([k, v]) => props[k] && Date.parse(props[k]) === Date.parse(v))) { bilan.aJour++; continue; }
  console.log(`${u.email.padEnd(45)} création ${u.created_at.slice(0, 10)}  dernière connexion ${(u.last_sign_in_at || '—').slice(0, 10)}`);
  bilan.maj++;
  if (APPLY) {
    const m = await fetch(`https://a.klaviyo.com/api/profiles/${p.id}/`, { method: 'PATCH', headers,
      body: JSON.stringify({ data: { type: 'profile', id: p.id, attributes: { properties: dates } } }) });
    if (!m.ok) { bilan.echec++; console.error(`  échec ${m.status} : ${await m.text()}`); }
  }
}
console.log(`${users.length} comptes.`, APPLY ? 'Écrit dans Klaviyo :' : 'Simulation (rien écrit) :', bilan);

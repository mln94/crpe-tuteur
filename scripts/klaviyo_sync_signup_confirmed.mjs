// Klaviyo : signup_confirmed (et email_verified) = true si l'e-mail du compte est confirmé, false sinon, pour tous les comptes.
// Source : auth.users.email_confirmed_at. Un compte absent de Klaviyo y est créé par le serveur (POST /api/webhook/supabase-auth),
// avec les mêmes listes et consentements qu'à l'inscription.
// Usage : node scripts/klaviyo_sync_signup_confirmed.mjs          (simulation)
//         node scripts/klaviyo_sync_signup_confirmed.mjs --apply  (écriture dans Klaviyo)
//         --sans-creation : les comptes absents de Klaviyo (comptes de test, admin) ne sont pas créés
import 'dotenv/config';
import { createClient } from '@supabase/supabase-js';

const APPLY = process.argv.includes('--apply');
const SANS_CREATION = process.argv.includes('--sans-creation');
const KEY = process.env.KLAVIYO_PRIVATE_API_KEY;
if (!KEY) { console.error('KLAVIYO_PRIVATE_API_KEY manquante (.env)'); process.exit(1); }
const WEBHOOK = 'https://www.passcrpe.fr/api/webhook/supabase-auth';
const headers = { Authorization: `Klaviyo-API-Key ${KEY}`, revision: '2026-04-15', 'Content-Type': 'application/json', accept: 'application/json' };
const sb = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });

const users = [];
for (let page = 1; ; page++) {
  const { data, error } = await sb.auth.admin.listUsers({ page, perPage: 1000 });
  if (error) throw error;
  users.push(...data.users);
  if (data.users.length < 1000) break;
}

const bilan = { true: 0, false: 0, aJour: 0, cree: 0, sansEmail: 0 };
for (const u of users) {
  if (!u.email) { bilan.sansEmail++; continue; }
  const confirmed = !!u.email_confirmed_at;
  const r = await fetch(`https://a.klaviyo.com/api/profiles/?filter=equals(email,"${encodeURIComponent(u.email)}")`, { headers });
  const p = (await r.json()).data?.[0];
  if (!p) {
    console.log(`absent       ${u.email} → ${SANS_CREATION ? 'laissé absent' : `créé (signup_confirmed ${confirmed})`}`);
    bilan.cree++;
    if (APPLY && !SANS_CREATION) {
      const w = await fetch(WEBHOOK, { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type: confirmed ? 'UPDATE' : 'INSERT', record: { id: u.id } }) });
      if (!w.ok) console.error(`  échec ${w.status} : ${await w.text()}`);
    }
    continue;
  }
  const props = p.attributes?.properties || {};
  if (props.signup_confirmed === confirmed && props.email_verified === confirmed) { bilan.aJour++; continue; }
  console.log(`${String(confirmed).padEnd(12)} ${u.email} (avant : ${props.signup_confirmed ?? 'absent'})`);
  bilan[confirmed]++;
  if (APPLY) {
    const m = await fetch(`https://a.klaviyo.com/api/profiles/${p.id}/`, { method: 'PATCH', headers,
      body: JSON.stringify({ data: { type: 'profile', id: p.id, attributes: { properties: { signup_confirmed: confirmed, email_verified: confirmed } } } }) });
    if (!m.ok) console.error(`  échec ${m.status} : ${await m.text()}`);
  }
}
console.log(`${users.length} comptes.`, APPLY ? 'Écrit dans Klaviyo :' : 'Simulation (rien écrit) :', bilan);

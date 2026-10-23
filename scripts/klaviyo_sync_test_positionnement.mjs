// Klaviyo : test_positionnement_realise = false pour les inscrits qui n'ont pas fait le test, true pour ceux qui l'ont fait.
// Source : profils_utilisateurs.test_positionnement_realise. Un profil Klaviyo déjà à true n'est jamais repassé à false.
// Usage : node scripts/klaviyo_sync_test_positionnement.mjs          (simulation)
//         node scripts/klaviyo_sync_test_positionnement.mjs --apply  (écriture dans Klaviyo)
import 'dotenv/config';
import { createClient } from '@supabase/supabase-js';

const APPLY = process.argv.includes('--apply');
const KEY = process.env.KLAVIYO_PRIVATE_API_KEY;
if (!KEY) { console.error('KLAVIYO_PRIVATE_API_KEY manquante (.env)'); process.exit(1); }
const headers = { Authorization: `Klaviyo-API-Key ${KEY}`, revision: '2026-04-15', 'Content-Type': 'application/json', accept: 'application/json' };
const sb = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });

const { data: profils, error } = await sb.from('profils_utilisateurs').select('email, test_positionnement_realise').not('email', 'is', null);
if (error) throw error;

const bilan = { true: 0, false: 0, dejaTrue: 0, introuvable: 0 };
for (const { email, test_positionnement_realise: fait } of profils) {
  const r = await fetch(`https://a.klaviyo.com/api/profiles/?filter=equals(email,"${encodeURIComponent(email)}")`, { headers });
  const p = (await r.json()).data?.[0];
  if (!p) { bilan.introuvable++; console.log(`introuvable  ${email}`); continue; }
  const actuel = p.attributes?.properties?.test_positionnement_realise;
  if (!fait && actuel === true) { bilan.dejaTrue++; console.log(`déjà true    ${email} (laissé à true)`); continue; }
  console.log(`${String(fait).padEnd(12)} ${email} (avant : ${actuel ?? 'absent'})`);
  bilan[fait]++;
  if (APPLY) {
    const u = await fetch(`https://a.klaviyo.com/api/profiles/${p.id}/`, { method: 'PATCH', headers,
      body: JSON.stringify({ data: { type: 'profile', id: p.id, attributes: { properties: { test_positionnement_realise: fait } } } }) });
    if (!u.ok) console.error(`  échec ${u.status} : ${await u.text()}`);
  }
}
console.log(APPLY ? 'Écrit dans Klaviyo :' : 'Simulation (rien écrit) :', bilan);

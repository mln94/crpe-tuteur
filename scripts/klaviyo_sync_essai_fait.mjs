// Klaviyo : essai_fait_quizcrpe (true / false) pour TOUS les profils Klaviyo, quelle que soit leur origine.
// true seulement si quiz_comptes.essai_fait = true pour cet email ; tous les autres profils (aucune question d'essai) : false.
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
const attendre = (ms) => new Promise((r) => setTimeout(r, ms));

const { data: quiz, error } = await sb.from('quiz_comptes').select('email').eq('essai_fait', true);
if (error) throw error;
const essaiFait = new Set(quiz.filter((q) => q.email).map((q) => q.email.trim().toLowerCase()));

// Tous les profils Klaviyo, page par page
const profils = [];
let url = 'https://a.klaviyo.com/api/profiles/?page[size]=100&fields[profile]=email,properties';
while (url) {
  const r = await fetch(url, { headers });
  if (r.status === 429) { await attendre(2000); continue; }
  if (!r.ok) throw new Error(`Klaviyo ${r.status} : ${await r.text()}`);
  const j = await r.json();
  profils.push(...j.data);
  url = j.links?.next || null;
}

const bilan = { versTrue: 0, versFalse: 0, aJour: 0, echec: 0 };
for (const p of profils) {
  const email = (p.attributes?.email || '').trim().toLowerCase();
  const valeur = essaiFait.has(email);
  if (p.attributes?.properties?.essai_fait_quizcrpe === valeur) { bilan.aJour++; continue; }
  console.log(`${(email || p.id).padEnd(45)} essai_fait_quizcrpe = ${valeur}`);
  valeur ? bilan.versTrue++ : bilan.versFalse++;
  if (!APPLY) continue;
  for (let essai = 0; essai < 5; essai++) {
    const m = await fetch(`https://a.klaviyo.com/api/profiles/${p.id}/`, { method: 'PATCH', headers,
      body: JSON.stringify({ data: { type: 'profile', id: p.id, attributes: { properties: { essai_fait_quizcrpe: valeur } } } }) });
    if (m.status === 429) { await attendre(2000); continue; }
    if (!m.ok) { bilan.echec++; console.error(`  échec ${m.status} : ${await m.text()}`); }
    break;
  }
}
console.log(`${profils.length} profils Klaviyo, ${essaiFait.size} comptes avec essai fait.`, APPLY ? 'Écrit dans Klaviyo :' : 'Simulation (rien écrit) :', bilan);

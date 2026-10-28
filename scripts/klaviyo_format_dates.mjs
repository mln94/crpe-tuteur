// Klaviyo : toutes les dates des profils au même format « 2026-10-27T13:08:26Z » (ISO 8601 sans fractions de seconde),
// reconnu comme date par les flows. Parcourt tous les profils Klaviyo (inscrits du site, leads de l'Entraîneur…) et réécrit
// chaque propriété (hors propriétés système « $… ») dont la valeur est une date ISO dans un autre format (« …16.635Z », « …26.126101Z », « +00:00 »…).
// Le serveur envoie déjà ce format (dateKlaviyo, app.js).
// Usage : node scripts/klaviyo_format_dates.mjs          (simulation)
//         node scripts/klaviyo_format_dates.mjs --apply  (écriture dans Klaviyo)
import 'dotenv/config';

const APPLY = process.argv.includes('--apply');
const KEY = process.env.KLAVIYO_PRIVATE_API_KEY;
if (!KEY) { console.error('KLAVIYO_PRIVATE_API_KEY manquante (.env)'); process.exit(1); }
const headers = { Authorization: `Klaviyo-API-Key ${KEY}`, revision: '2026-04-15', 'Content-Type': 'application/json', accept: 'application/json' };

const ISO = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:?\d{2})$/;
const dateKlaviyo = d => new Date(d).toISOString().slice(0, 19) + 'Z';

const bilan = { profils: 0, modifies: 0, proprietes: 0, echec: 0 };
const parPropriete = {};
for (let url = 'https://a.klaviyo.com/api/profiles/?page[size]=100'; url; ) {
  const r = await fetch(url, { headers });
  const j = await r.json();
  if (!r.ok) throw new Error(JSON.stringify(j.errors || j));
  for (const p of j.data) {
    bilan.profils++;
    const props = p.attributes?.properties || {};
    const corrige = {};
    for (const [k, v] of Object.entries(props))
      if (!k.startsWith('$') && typeof v === 'string' && ISO.test(v) && dateKlaviyo(v) !== v) corrige[k] = dateKlaviyo(v); // $… : propriétés système de Klaviyo, laissées telles quelles
    if (!Object.keys(corrige).length) continue;
    bilan.modifies++; bilan.proprietes += Object.keys(corrige).length;
    Object.keys(corrige).forEach(k => { parPropriete[k] = (parPropriete[k] || 0) + 1; });
    console.log(`${(p.attributes.email || p.id).padEnd(45)} ${Object.entries(corrige).map(([k, v]) => `${k}: ${props[k]} → ${v}`).join(' · ')}`);
    if (APPLY) {
      const m = await fetch(`https://a.klaviyo.com/api/profiles/${p.id}/`, { method: 'PATCH', headers,
        body: JSON.stringify({ data: { type: 'profile', id: p.id, attributes: { properties: corrige } } }) });
      if (!m.ok) { bilan.echec++; console.error(`  échec ${m.status} : ${await m.text()}`); }
    }
  }
  url = j.links?.next || null;
}
console.log(APPLY ? 'Écrit dans Klaviyo :' : 'Simulation (rien écrit) :', bilan, parPropriete);

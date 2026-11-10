// Publie une nouveauté du site dans le dashboard /suivi-nouveautes (et la met à jour si elle existe déjà).
// Dossier d'une nouveauté : Ressources/nouveautes/AAAA-MM-JJ-sujet/
//   nouveaute.json   { modifie_le, type, titre, resume, lien, insta_legende, facebook_post,
//                      groupes: { campagne, message },                       // message avec {LIEN} = lien du groupe
//                      email: { nom, objet, preheader } }                  // fonctionnalités / design seulement
//   instagram.png    1080 × 1350           facebook.png   1200 × 630
//   email.html       (si email) ; ses images locales (src="xxx.png") sont envoyées dans le bucket et remplacées par leur URL
// Ce que fait le script :
//   1. images → bucket Supabase public « nouveautes »
//   2. groupes Facebook → campagne meta_campagnes (les liens par groupe sont générés à l'ouverture de /suivi-publications)
//   3. email → template + campagne Klaviyo en BROUILLON pour la liste Signup (rien n'est envoyé), lien Klaviyo enregistré
//   4. ligne site_nouveautes (id gardé dans nouveaute.json → les relances du script mettent à jour au lieu de dupliquer)
// Usage : node scripts/nouveaute.mjs "Ressources/nouveautes/2026-11-10-sujet"
//         node scripts/nouveaute.mjs --demandes        (liste les demandes de changement en attente)
//         node scripts/nouveaute.mjs --faite <id> "ce qui a été changé"   (marque une demande comme faite)
import 'dotenv/config';
import fs from 'node:fs';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';

const sb = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
const KL = { Authorization: `Klaviyo-API-Key ${process.env.KLAVIYO_PRIVATE_API_KEY}`, revision: '2026-04-15', 'Content-Type': 'application/vnd.api+json', accept: 'application/vnd.api+json' };
const LISTE_SIGNUP = 'SgJQyM';
const EXPEDITEUR = { from_email: 'contact@passcrpe.fr', from_label: 'PassCRPE' };
const APP = t => ['feature_passcrpe', 'feature_quizcrpe', 'design'].includes(t);
const ELEMENTS = { insta_texte: 'Légende Instagram', insta_image: 'Image Instagram', facebook_texte: 'Texte Facebook', facebook_image: 'Image Facebook', groupes_message: 'Message des groupes', email: 'Email' };

const arg = process.argv.slice(2);
if (arg[0] === '--demandes') {
  const { data, error } = await sb.from('site_nouveautes_demandes').select('*, site_nouveautes(titre, modifie_le)').eq('statut', 'en_attente').order('created_at');
  if (error) throw error;
  if (!data.length) console.log('Aucune demande en attente.');
  for (const d of data) console.log(`${d.id}  [${ELEMENTS[d.element]}]  « ${d.site_nouveautes.titre} » (${d.site_nouveautes.modifie_le})\n    ${d.demande}\n`);
  process.exit(0);
}
if (arg[0] === '--faite') {
  const { error } = await sb.from('site_nouveautes_demandes').update({ statut: 'faite', reponse: arg[2] || null, traitee_at: new Date().toISOString() }).eq('id', arg[1]);
  if (error) throw error;
  console.log('Demande marquée comme faite.'); process.exit(0);
}

const dossier = arg[0];
if (!dossier || !fs.existsSync(path.join(dossier, 'nouveaute.json'))) { console.error('Usage : node scripts/nouveaute.mjs <dossier contenant nouveaute.json>'); process.exit(1); }
const fichierJson = path.join(dossier, 'nouveaute.json');
const nv = JSON.parse(fs.readFileSync(fichierJson, 'utf8'));
const cle = path.basename(path.resolve(dossier));
const v = Date.now(); // contourne le cache des images remplacées

async function envoyer(fichier, nom) {
  const ext = path.extname(fichier).slice(1).toLowerCase();
  const type = { png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', gif: 'image/gif', webp: 'image/webp' }[ext] || 'application/octet-stream';
  const { error } = await sb.storage.from('nouveautes').upload(`${cle}/${nom}`, fs.readFileSync(fichier), { contentType: type, upsert: true, cacheControl: '60' });
  if (error) throw new Error(`Envoi de ${fichier} : ${error.message}`);
  return `${sb.storage.from('nouveautes').getPublicUrl(`${cle}/${nom}`).data.publicUrl}?v=${v}`;
}
async function klaviyo(methode, url, corps) {
  const r = await fetch(`https://a.klaviyo.com/api/${url}`, { method: methode, headers: KL, body: corps ? JSON.stringify(corps) : undefined });
  const t = await r.text();
  if (!r.ok) throw new Error(`Klaviyo ${methode} ${url} : ${r.status} ${t}`);
  return t ? JSON.parse(t) : null;
}

const ligne = {
  modifie_le: nv.modifie_le, type: nv.type, titre: nv.titre, resume: nv.resume, lien: nv.lien,
  insta_legende: nv.insta_legende || null, facebook_post: nv.facebook_post || null, updated_at: new Date().toISOString(),
};

// 1. Images
for (const [f, champ] of [['instagram.png', 'insta_image_url'], ['facebook.png', 'facebook_image_url']])
  if (fs.existsSync(path.join(dossier, f))) { ligne[champ] = await envoyer(path.join(dossier, f), f); console.log(`image   ${f} → ${ligne[champ]}`); }

// 2. Groupes Facebook
if (nv.groupes?.campagne) {
  const nom = nv.groupes.campagne;
  const { data: exist } = await sb.from('meta_campagnes').select('id').eq('nom', nom).maybeSingle();
  const champs = { message: nv.groupes.message || null, message_maj_at: nv.groupes.message ? new Date().toISOString() : null, base_url: nv.lien };
  if (exist) {
    const { error } = await sb.from('meta_campagnes').update(champs).eq('id', exist.id); if (error) throw error;
    ligne.meta_campagne_id = exist.id; console.log(`groupes campagne « ${nom} » mise à jour (message)`);
  } else {
    const { data, error } = await sb.from('meta_campagnes').insert({ nom, ...champs }).select('id').single(); if (error) throw error;
    ligne.meta_campagne_id = data.id; console.log(`groupes campagne « ${nom} » créée (liens générés à l'ouverture de /suivi-publications)`);
  }
}

// 3. Email Klaviyo (applications seulement)
if (APP(nv.type) && nv.email && fs.existsSync(path.join(dossier, 'email.html'))) {
  let html = fs.readFileSync(path.join(dossier, 'email.html'), 'utf8');
  for (const src of new Set([...html.matchAll(/src="(?!https?:|data:|\{)([^"]+)"/g)].map(m => m[1]))) {
    const url = await envoyer(path.join(dossier, src), 'email-' + path.basename(src));
    html = html.split(`src="${src}"`).join(`src="${url}"`);
  }
  ligne.email_html = html; ligne.email_objet = nv.email.objet;
  const nomCampagne = nv.email.nom; // toujours « PassCRPE - … »
  const tpl = await klaviyo('POST', 'templates/', { data: { type: 'template', attributes: { name: nomCampagne, editor_type: 'CODE', html } } });
  const contenu = { subject: nv.email.objet, preview_text: nv.email.preheader || '', ...EXPEDITEUR };
  let campagneId = nv.klaviyo_campaign_id, messageId;
  if (campagneId) {
    const c = await klaviyo('GET', `campaigns/${campagneId}/?include=campaign-messages`);
    if (c.data.attributes.status !== 'Draft') throw new Error(`La campagne Klaviyo ${campagneId} n'est plus un brouillon (${c.data.attributes.status}) : elle n'est pas modifiée.`);
    messageId = c.included[0].id;
    await klaviyo('PATCH', `campaigns/${campagneId}/`, { data: { type: 'campaign', id: campagneId, attributes: { name: nomCampagne } } });
    await klaviyo('PATCH', `campaign-messages/${messageId}/`, { data: { type: 'campaign-message', id: messageId, attributes: { definition: { channel: 'email', label: nomCampagne, content: contenu } } } });
  } else {
    const c = await klaviyo('POST', 'campaigns/', { data: { type: 'campaign', attributes: {
      name: nomCampagne, audiences: { included: [LISTE_SIGNUP], excluded: [] },
      send_strategy: { method: 'immediate' },
      'campaign-messages': { data: [{ type: 'campaign-message', attributes: { definition: { channel: 'email', label: nomCampagne, content: contenu } } }] },
    } } });
    campagneId = c.data.id; messageId = c.data.relationships['campaign-messages'].data[0].id;
    nv.klaviyo_campaign_id = campagneId;
  }
  await klaviyo('POST', 'campaign-message-assign-template/', { data: { type: 'campaign-message', id: messageId, relationships: { template: { data: { type: 'template', id: tpl.data.id } } } } });
  ligne.klaviyo_campaign_id = campagneId;
  ligne.klaviyo_url = `https://www.klaviyo.com/campaign/${campagneId}/wizard/1`;
  console.log(`email   campagne Klaviyo « ${nomCampagne} » en brouillon → ${ligne.klaviyo_url}`);
}

// 4. Ligne du dashboard
if (nv.id) {
  const { error } = await sb.from('site_nouveautes').update(ligne).eq('id', nv.id); if (error) throw error;
  console.log(`dashboard nouveauté mise à jour : ${nv.id}`);
} else {
  const { data, error } = await sb.from('site_nouveautes').insert(ligne).select('id').single(); if (error) throw error;
  nv.id = data.id; console.log(`dashboard nouveauté ajoutée : ${nv.id}`);
}
fs.writeFileSync(fichierJson, JSON.stringify(nv, null, 2) + '\n');
console.log(`→ https://www.passcrpe.fr/suivi-nouveautes?nouveaute=${nv.id}`);

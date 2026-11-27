// Lien entre les agents IA du Mac et le dashboard /suivi-agents (tables Supabase agents_*).
// Usage :
//   node scripts/agents_suivi.mjs --planifier-veille [AAAA-MM-JJ]      crée un passage « en_attente » (défaut : hier, heure de Paris)
//   node scripts/agents_suivi.mjs --prochaine-veille                   prend le plus ancien passage en attente → affiche « <id> <jour> »
//   node scripts/agents_suivi.mjs --enregistrer-veille <fichier.json> <run_id>
//        fichier : { jour, groupes_lus, groupes_echec: [{groupe, raison}], resume,
//                    messages: [{ post_le, groupe, groupe_slug, lien_groupe, pseudo, message, type_demande, lien_post, reponse }] }
//   node scripts/agents_suivi.mjs --echec-veille <run_id> "<raison>"   marque en erreur un passage resté « en_cours »
//   node scripts/agents_suivi.mjs --etat <clé> "<valeur>"                 enregistre l'état d'un programme du Mac
//   node scripts/agents_suivi.mjs --sync-blog                          envoie l'état des articles de Ressources/articles-auto/
import 'dotenv/config';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createClient } from '@supabase/supabase-js';

const sb = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
const REPO = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const [cmd, a1, a2] = process.argv.slice(2);

const jourParis = (decalage = 0) => {
  const d = new Date(Date.now() + decalage * 86400000);
  return new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Paris' }).format(d);
};
const ok = (r) => { if (r.error) { console.error(r.error.message); process.exit(1); } return r.data; };
const etat = (cle, valeur) => sb.from('agents_etat').upsert({ cle, valeur, updated_at: new Date().toISOString() });

if (cmd === '--planifier-veille') {
  const jour = a1 || jourParis(-1);
  // Un seul passage planifié par jour (même en erreur : on ne réessaie pas en boucle ; relance possible depuis le dashboard)
  const deja = ok(await sb.from('agents_runs').select('id').eq('agent', 'veille_facebook').eq('jour', jour));
  if (deja.length) console.log('déjà fait ou prévu pour', jour);
  else { ok(await sb.from('agents_runs').insert({ agent: 'veille_facebook', jour, origine: 'planifie' })); console.log('prévu', jour); }

} else if (cmd === '--prochaine-veille') {
  await etat('poller_dernier_passage', new Date().toISOString());
  const [r] = ok(await sb.from('agents_runs').select('id, jour').eq('agent', 'veille_facebook').eq('statut', 'en_attente').order('created_at').limit(1));
  if (r) {
    ok(await sb.from('agents_runs').update({ statut: 'en_cours', debut: new Date().toISOString() }).eq('id', r.id).eq('statut', 'en_attente'));
    console.log(r.id, r.jour);
  }

} else if (cmd === '--enregistrer-veille') {
  const d = JSON.parse(fs.readFileSync(a1, 'utf8'));
  const run = a2;
  const msgs = (d.messages || []).filter(m => m.message && m.groupe).map(m => ({
    jour: d.jour, post_le: m.post_le || null, groupe: m.groupe, groupe_slug: m.groupe_slug || null, lien_groupe: m.lien_groupe || null,
    pseudo: m.pseudo || null, message: m.message, type_demande: m.type_demande || null, lien_post: m.lien_post || null,
    reponse: m.reponse || null, run_id: run || null,
  }));
  // Un post déjà enregistré (même lien) garde son statut et sa réponse
  if (msgs.length) ok(await sb.from('agents_veille_messages').upsert(msgs, { onConflict: 'lien_post', ignoreDuplicates: true }));
  const maj = { statut: 'ok', fin: new Date().toISOString(), groupes_lus: d.groupes_lus ?? null, groupes_echec: d.groupes_echec || [],
    messages_retenus: msgs.length, resume: d.resume || null };
  if (run) ok(await sb.from('agents_runs').update(maj).eq('id', run));
  else ok(await sb.from('agents_runs').insert({ agent: 'veille_facebook', jour: d.jour, origine: 'planifie', ...maj }));
  console.log(`enregistré : ${msgs.length} message(s) pour le ${d.jour}`);

} else if (cmd === '--echec-veille') {
  ok(await sb.from('agents_runs').update({ statut: 'erreur', fin: new Date().toISOString(), resume: (a2 || 'Échec').slice(0, 4000) })
    .eq('id', a1).eq('statut', 'en_cours'));

} else if (cmd === '--sync-blog') {
  const dir = path.join(REPO, 'Ressources', 'articles-auto');
  const lignes = [];
  for (const dossier of fs.existsSync(dir) ? fs.readdirSync(dir) : []) {
    const p = path.join(dir, dossier);
    if (!fs.statSync(p).isDirectory()) continue;
    const lire = (f) => { try { return JSON.parse(fs.readFileSync(path.join(p, f), 'utf8')); } catch { return null; } };
    const def = lire('traite.json') || lire('pret.json') || {};
    let res = lire('resultat.json');
    if (!res) {
      // Article publié sans le Publieur (avant sa mise en place) : premier commit qui a ajouté la page
      try {
        const g = execFileSync('git', ['log', '--diff-filter=A', '--format=%h %s%x09%aI', '--', `landing/${def.slug || dossier.slice(11)}.html`], { cwd: REPO, encoding: 'utf8' }).trim().split('\n').pop();
        if (g) { const [commit, date] = g.split('\t'); res = { statut: 'OK', commit, date }; }
      } catch {}
    }
    const slug = def.slug || dossier.replace(/^\d{4}-\d{2}-\d{2}-/, '');
    let titre = null;
    try { titre = (fs.readFileSync(path.join(REPO, 'landing', slug + '.html'), 'utf8').match(/<title>([^<]*)<\/title>/) || [])[1] || null; } catch {}
    if (titre) titre = titre.replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16))).replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(+d))
      .replace(/&quot;/g, '"').replace(/&apos;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
    lignes.push({
      dossier, jour: dossier.slice(0, 10), slug, titre: titre && titre.replace(/\s*\|\s*Blog PassCRPE\s*$/, ''),
      url: `https://www.passcrpe.fr/blog/${slug}`,
      statut: res ? res.statut : (fs.existsSync(path.join(p, 'pret.json')) ? 'en attente de publication' : 'en préparation'),
      commit: res?.commit || null,
      erreur: res && res.statut !== 'OK' ? String(res.details || '').slice(-3000) : null,
      publie_le: res?.date ? new Date(res.date.replace(/([+-]\d{2})(\d{2})$/, '$1:$2')).toISOString() : null,
      updated_at: new Date().toISOString(),
    });
  }
  if (lignes.length) ok(await sb.from('agents_blog_articles').upsert(lignes, { onConflict: 'dossier' }));
  const pl = path.join(process.env.HOME, '.passcrpe', 'publier.log');
  if (fs.existsSync(pl)) await etat('publieur_journal', fs.readFileSync(pl, 'utf8').trim().split('\n').slice(-15).join('\n'));
  console.log(`blog : ${lignes.length} article(s) synchronisé(s)`);

} else if (cmd === '--etat') {
  ok(await etat(a1, a2 ?? ''));

} else {
  console.error('commande inconnue'); process.exit(1);
}

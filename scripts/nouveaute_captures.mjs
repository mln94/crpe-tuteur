// Captures d'écran de l'application (passcrpe.fr), connecté avec le compte administrateur, pour les publications d'une nouveauté.
// Connexion sans mot de passe : lien magique généré par la clé service (aucun email envoyé), session posée dans le navigateur.
// Le nom du compte est remplacé par « Mon compte » sur les captures (visuels publics).
// Navigateur : Chrome installé sur le Mac, piloté par Playwright (paquet trouvé dans le cache npx, ou PLAYWRIGHT_MODULE).
//
// Usage dans un script de capture propre à la nouveauté (Ressources/nouveautes/<dossier>/captures.mjs) :
//   import { ouvrir, capturer } from '../../../scripts/nouveaute_captures.mjs';
//   const { navigateur, page } = await ouvrir();            // téléphone 430 × 932, rendu 2x
//   await page.goto('https://www.passcrpe.fr/quizapp'); …
//   await capturer(page, 'captures/1-accueil.png');
//   await navigateur.close();
// Attention : répondre à une question dans le quiz compte dans les questions gratuites du jour du compte administrateur.
import 'dotenv/config';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';

const EMAIL_ADMIN = 'mohamed.necib94310@gmail.com';
const CLE_SESSION = 'sb-zqwcermgfvcusuwjfviz-auth-token';

async function playwright() {
  if (process.env.PLAYWRIGHT_MODULE) return import(process.env.PLAYWRIGHT_MODULE);
  try { return await import('playwright'); } catch (e) {}
  const npx = path.join(os.homedir(), '.npm/_npx');
  for (const d of fs.existsSync(npx) ? fs.readdirSync(npx) : []) {
    const m = path.join(npx, d, 'node_modules/playwright/index.mjs');
    if (fs.existsSync(m)) return import(m);
  }
  throw new Error('Playwright introuvable : lancez une fois « npx playwright --version » ou définissez PLAYWRIGHT_MODULE.');
}

export async function ouvrir({ largeur = 430, hauteur = 932 } = {}) {
  const admin = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
  const { data: lien, error: e1 } = await admin.auth.admin.generateLink({ type: 'magiclink', email: EMAIL_ADMIN });
  if (e1) throw e1;
  const pub = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY, { auth: { persistSession: false } });
  const { data: s, error: e2 } = await pub.auth.verifyOtp({ token_hash: lien.properties.hashed_token, type: 'magiclink' });
  if (e2) throw e2;
  const { chromium } = await playwright();
  const navigateur = await chromium.launch({ channel: 'chrome' });
  const ctx = await navigateur.newContext({ viewport: { width: largeur, height: hauteur }, deviceScaleFactor: 2 });
  await ctx.addInitScript(([k, v]) => { if (!localStorage.getItem(k)) localStorage.setItem(k, v); }, [CLE_SESSION, JSON.stringify(s.session)]);
  return { navigateur, page: await ctx.newPage() };
}

// Remplace le nom du compte (visible dans l'en-tête) avant la capture
export async function capturer(page, fichier, options = {}) {
  await page.evaluate(() => {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let n; (n = w.nextNode());) if (/Mohamed Necib/.test(n.nodeValue)) n.nodeValue = n.nodeValue.replace(/Mohamed Necib/g, 'Mon compte');
  });
  await page.waitForTimeout(200);
  await page.screenshot({ path: fichier, ...options });
  console.log('capture →', fichier);
}

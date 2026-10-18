#!/usr/bin/env python3
"""Génère src/siteChrome.js : l'en-tête et le pied de page du site pour le tuteur IA (/app).

Même structure que /quizapp et /espace : menu du site, menu du compte (nom du profil, Mes outils, Tuteur IA,
Quiz CRPE, Se déconnecter) et pied de page. Le HTML et les styles sont repris du gabarit des pages du site ;
seules les règles CSS du menu et du pied de page sont gardées, pour ne pas toucher aux styles de l'application.
Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html ; menu du compte : scripts/nav_compte.py
Le tuteur IA utilise APP_NAV_HTML (en-tête d'application, sans menu du site ni pied de page).
Usage   : python3 scripts/generate_app_chrome.py
"""
import json
import os
import re

import nav_compte

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
OUT = os.path.join(ROOT, 'src', 'siteChrome.js')

tpl = open(TEMPLATE, encoding='utf-8').read()
NAV = tpl[tpl.index('<nav class="site-nav">'):tpl.index('</nav>') + len('</nav>')]
NAV = NAV.replace('<li><a href="/blog" class="active">Blog</a></li>', '<li><a href="/blog">Blog</a></li>')
FOOTER = tpl[tpl.index('<footer>'):tpl.index('</footer>') + len('</footer>')]
css_all = tpl[tpl.index('<style>') + 7:tpl.index('</style>')]

GARDER = ('.site-nav', '.nav-', 'footer', '.footer-', ':root')


def garde(selecteurs):
    return all(s.strip().startswith(GARDER) for s in selecteurs.split(','))


def filtrer(css):
    """Garde les règles du menu et du pied de page (y compris dans les @media)."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out, i = [], 0
    while i < len(css):
        j = css.find('{', i)
        if j < 0:
            break
        tete = css[i:j].strip()
        if tete.startswith('@media'):
            prof, k = 1, j + 1
            while prof:
                prof += {'{': 1, '}': -1}.get(css[k], 0)
                k += 1
            dedans = filtrer(css[j + 1:k - 1])
            if dedans.strip():
                out.append(f'{tete} {{\n{dedans}}}\n')
            i = k
        else:
            k = css.index('}', j)
            if garde(tete):
                out.append(f'{tete} {{{css[j + 1:k]}}}\n')
            i = k + 1
    return ''.join(out)


CSS = filtrer(css_all) + nav_compte.CSS + """
    /* Tuteur IA : police du site, pied de page pleine largeur au-dessus de la barre d'onglets */
    .site-nav, .site-footer-wrap { font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    .site-nav { flex-shrink: 0; }
    .site-footer-wrap { margin-top: 32px; }
    .site-footer-wrap footer { padding-bottom: 96px; }
    .site-nav.connecte .nav-actions > .nav-login, .site-nav.connecte .nav-actions > .nav-cta { display: none !important; }
"""

MODULE = f"""// Généré par scripts/generate_app_chrome.py — ne pas modifier à la main.
// En-tête et pied de page du site pour le tuteur IA, identiques à /quizapp et /espace.
export const SITE_NAV_HTML = {json.dumps(NAV, ensure_ascii=False)};
// En-tête de l'application : logo, bouton Support et menu du compte, sans le menu du site
export const APP_NAV_HTML = {json.dumps(nav_compte.nav_application(NAV, '/app?onglet=support'), ensure_ascii=False)};
export const SITE_FOOTER_HTML = {json.dumps(FOOTER, ensure_ascii=False)};
export const SITE_CHROME_CSS = {json.dumps(CSS, ensure_ascii=False)};
"""

open(OUT, 'w', encoding='utf-8').write(MODULE)
print('src/siteChrome.js', len(CSS), 'caractères de CSS')

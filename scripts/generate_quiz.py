#!/usr/bin/env python3
"""Génère la page de l'application « Quiz CRPE » : /quizapp.

Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Sortie  : landing/quizapp.html
Données : table Supabase quiz_questions, servie par /api/quiz/catalogue et /api/quiz/reponse (app.js)
Usage   : python3 scripts/generate_quiz.py

Accès : compte PassCRPE (projet Supabase « crpe », le même que le tuteur IA), créé sur /quiz ou sur l'accueil. Test de positionnement gratuit et obligatoire
(45 questions, carte des forces et faiblesses), puis paiement PayPal (59 € TTC) pour débloquer le quiz. Le serveur
(app.js) vérifie le paiement avant de servir les questions.

Fonctionnement du quiz :
- séries de 20 questions, note sur 20 à la fin ;
- chaque notion est posée sous plusieurs formulations : 3 bonnes réponses (formulations différentes) = notion maîtrisée ;
- révision espacée : après une bonne réponse, la formulation suivante revient 1 jour puis 3 jours plus tard ;
  après une erreur, l'explication est affichée et une question similaire revient le lendemain ;
- progression gardée dans le navigateur (localStorage), par matière et par thème.
"""
import json
import os

import nav_compte

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'

# (clé dans la table, libellé, icône)
MATIERES = [
    ('francais', 'Français', '✍️'),
    ('mathematiques', 'Mathématiques', '🔢'),
    ('histoire_geographie', 'Histoire-géographie', '🌍'),
    ('emc', 'Enseignement moral et civique', '⚖️'),
    ('svt', 'Sciences de la vie et de la Terre', '🌱'),
    ('physique_chimie', 'Physique-chimie', '⚗️'),
    ('technologie', 'Technologie', '⚙️'),
    ('arts', 'Arts', '🎨'),
    ('anglais', 'Anglais', '🇬🇧'),
]
PRIX = '59 €'
TAILLE_SERIE = 20
BONNES_POUR_MAITRISER = 3
INTERVALLES_JOURS = [1, 3]   # après la 1re puis la 2e bonne réponse
APRES_ERREUR_JOURS = 1

# ── Gabarit commun ───────────────────────────────────────────────────────────
tpl = open(TEMPLATE, encoding='utf-8').read()
HEAD_START = tpl[:tpl.index('  <title>')]
css_start = tpl.index('  <link rel="preconnect"')
css_end = tpl.index('  </style>', css_start)
CSS_BASE = tpl[css_start:css_end]
BODY_START = tpl[css_end:tpl.index('<div class="article-wrap">')]
TAIL = tpl[tpl.index('<footer>'):]
NAV_BLOG = '<li><a href="/blog" class="active">Blog</a></li>'
assert BODY_START.count(NAV_BLOG) == 1
BODY_NAV = BODY_START.replace(NAV_BLOG, '<li><a href="/blog">Blog</a></li>')
# Application : en-tête sans le menu du site (logo, Support, menu du compte) et pas de pied de page
_nav = BODY_NAV[BODY_NAV.index('<nav class="site-nav">'):BODY_NAV.index('</nav>') + len('</nav>')]
BODY_NAV = BODY_NAV.replace(_nav, nav_compte.nav_application(_nav, '/app?onglet=support&produit=quiz'))
TAIL = TAIL[:TAIL.index('<footer>')] + TAIL[TAIL.index('</footer>') + len('</footer>'):]
ICONES = {
    'accueil': '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    'support': '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    'profil': '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
}
# Barre d'onglets en bas, comme dans le tuteur IA : Accueil (quiz), Support et Profil (onglets du compte PassCRPE)
TABBAR = '<nav class="quiz-tabbar" aria-label="Navigation du quiz">' + ''.join(
    f'<a href="{href}"{cls}><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONES[k]}</svg>{extra}</span>{lib}</a>'
    for k, lib, href, cls, extra in [
        ('accueil', 'Accueil', '/quizapp', ' class="actif" aria-current="page"', ''),
        ('support', 'Support', '/app?onglet=support&produit=quiz', ' id="tab-support"', '<span class="pastille" hidden></span>'),
        ('profil', 'Profil', '/app?onglet=profile', '', ''),
    ]) + '</nav>\n'

CSS = """
    /* QUIZ */
    .quiz-wrap { max-width: 780px; margin: 0 auto; padding: 32px 20px 72px; color: var(--gray-700); }
    .quiz-wrap h1 { font-size: clamp(28px, 4.5vw, 38px); font-weight: 900; color: var(--gray-900); line-height: 1.15; letter-spacing: -.5px; margin-bottom: 10px; }
    .quiz-lead { font-size: 16px; line-height: 1.6; margin-bottom: 26px; }
    .quiz-filtres { display: grid; gap: 18px; }
    .quiz-filtre label, .quiz-filtre .lbl { display: block; font-size: 13px; font-weight: 800; color: var(--gray-700); margin-bottom: 8px; }
    .quiz-select { width: 100%; padding: 13px 14px; font: inherit; font-size: 16px; font-weight: 600; color: var(--gray-900); border: 1.5px solid var(--gray-200); border-radius: 12px; background: #fff; cursor: pointer; }
    .quiz-select:focus { outline: none; border-color: #fb923c; }
    .quiz-niveaux { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .quiz-niveau { padding: 12px 8px; border-radius: 12px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 15px; font-weight: 700; color: var(--gray-700); cursor: pointer; transition: border-color .15s, background .15s; }
    .quiz-niveau:hover { border-color: #fb923c; }
    .quiz-niveau[aria-pressed="true"] { border-color: #f97316; background: #fff7ed; color: #c2410c; }
    .quiz-resume { font-size: 14px; color: var(--gray-600); background: var(--gray-50); border-radius: 12px; padding: 12px 14px; min-height: 46px; }
    .quiz-resume b { color: var(--gray-900); }
    .quiz-card { background: #fff; border: 1.5px solid var(--gray-200); border-radius: 20px; padding: 28px; box-shadow: 0 8px 30px rgba(0,0,0,.04); }
    .quiz-top { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 10px; font-size: 13px; font-weight: 700; color: var(--gray-500); }
    .quiz-top .mat { color: #c2410c; }
    .quiz-bar { height: 6px; border-radius: 6px; background: var(--gray-100); overflow: hidden; margin-bottom: 16px; }
    .quiz-bar span { display: block; height: 100%; background: linear-gradient(90deg, #f97316, #fb923c); transition: width .3s; }
    .quiz-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
    .chip { font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 100px; background: var(--gray-100); color: var(--gray-600); }
    .chip.facile { background: #dcfce7; color: #166534; }
    .chip.intermediaire { background: #fef3c7; color: #92400e; }
    .chip.difficile { background: #fee2e2; color: #991b1b; }
    .chip.theme { background: #ede9fe; color: #5b21b6; }
    .quiz-objectif { font-size: 12.5px; color: var(--gray-500); line-height: 1.5; margin-bottom: 18px; }
    .quiz-objectif strong { color: var(--gray-600); }
    .quiz-q { font-size: 19px; font-weight: 800; color: var(--gray-900); line-height: 1.45; margin-bottom: 18px; }
    .quiz-choices { display: grid; gap: 10px; }
    .quiz-choice { text-align: left; padding: 14px 16px; border-radius: 12px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 15px; color: var(--gray-800); cursor: pointer; transition: border-color .15s, background .15s; }
    .quiz-choice:hover:not(:disabled) { border-color: #fb923c; background: #fff7ed; }
    .quiz-choice:disabled { cursor: default; }
    .quiz-choice.good, .quiz-choice.bad, .tok.good, .tok.bad { transition: none; }
    .quiz-choice.good { border-color: #16a34a; background: #f0fdf4; color: #14532d; font-weight: 700; }
    .quiz-choice.bad { border-color: #dc2626; background: #fef2f2; color: #7f1d1d; }
    .quiz-num { display: flex; gap: 10px; flex-wrap: wrap; }
    .quiz-num input { flex: 1; min-width: 160px; padding: 13px 14px; font: inherit; font-size: 17px; border: 1.5px solid var(--gray-200); border-radius: 12px; }
    .quiz-num input:focus { outline: none; border-color: #fb923c; }
    .quiz-num input.good { border-color: #16a34a; background: #f0fdf4; }
    .quiz-num input.bad { border-color: #dc2626; background: #fef2f2; }
    .quiz-phrase { font-size: 19px; line-height: 2.3; padding: 14px 16px; border-radius: 14px; background: var(--gray-50); border: 1px solid var(--gray-200); margin-bottom: 14px; }
    .tok { display: inline-block; font: inherit; padding: 0 6px; margin: 0 1px; border-radius: 8px; border: 1.5px solid transparent; background: none; cursor: pointer; color: var(--gray-900); line-height: 1.7; }
    .tok:hover:not(:disabled) { background: #ffedd5; }
    .tok.sel { background: #fed7aa; border-color: #fb923c; }
    .tok.good { background: #dcfce7; border-color: #16a34a; }
    .tok.bad { background: #fee2e2; border-color: #dc2626; }
    .tok:disabled { cursor: default; }
    .punct { color: var(--gray-700); }
    .quiz-hint { font-size: 13px; color: var(--gray-500); margin-bottom: 4px; }
    .quiz-feedback { margin-top: 18px; padding: 16px 18px; border-radius: 14px; font-size: 15px; line-height: 1.6; }
    .quiz-feedback.ok { background: #f0fdf4; border: 1px solid #bbf7d0; }
    .quiz-feedback.ko { background: #fef2f2; border: 1px solid #fecaca; }
    .quiz-feedback strong { display: block; margin-bottom: 4px; color: var(--gray-900); }
    .quiz-feedback .suite { display: block; margin-top: 8px; font-size: 13px; color: var(--gray-600); }
    .quiz-actions { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 20px; }
    .quiz-btn { display: inline-flex; align-items: center; justify-content: center; padding: 12px 22px; border-radius: 10px; border: 0; font: inherit; font-size: 15px; font-weight: 800; cursor: pointer; background: #f97316; color: #fff; text-decoration: none; }
    .quiz-btn:hover { background: #ea580c; }
    .quiz-btn:disabled { background: #fdba74; cursor: not-allowed; }
    .quiz-btn.ghost { background: #fff; color: var(--gray-700); border: 1.5px solid var(--gray-200); }
    .quiz-btn.ghost:hover { background: var(--gray-50); }
    .quiz-score { text-align: center; }
    .quiz-score .big { font-size: 56px; font-weight: 900; color: var(--gray-900); letter-spacing: -1px; line-height: 1; margin: 6px 0 8px; }
    .quiz-score p { font-size: 16px; margin-bottom: 6px; }
    .quiz-score .quiz-actions { justify-content: center; }
    .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 18px 0 4px; }
    .stat { background: var(--gray-50); border-radius: 12px; padding: 12px 8px; text-align: center; }
    .stat b { display: block; font-size: 22px; font-weight: 900; color: var(--gray-900); }
    .stat span { font-size: 12px; color: var(--gray-500); }
    .quiz-recap { text-align: left; margin-top: 22px; display: grid; gap: 8px; }
    .quiz-recap div { font-size: 14px; padding: 10px 12px; border-radius: 10px; background: var(--gray-50); line-height: 1.5; }
    .quiz-recap .r-ok::before { content: "✓ "; color: #16a34a; font-weight: 900; }
    .quiz-recap .r-ko::before { content: "✗ "; color: #dc2626; font-weight: 900; }
    .prog-theme { margin-top: 16px; }
    .prog-theme h3 { font-size: 15px; font-weight: 800; color: var(--gray-900); margin-bottom: 6px; display: flex; justify-content: space-between; gap: 10px; }
    .prog-theme h3 span { font-size: 13px; font-weight: 600; color: var(--gray-500); }
    .prog-bar { height: 10px; border-radius: 10px; background: var(--gray-100); overflow: hidden; display: flex; }
    .prog-bar .m { background: #16a34a; }
    .prog-bar .c { background: #fbbf24; }
    .prog-legend { display: flex; gap: 14px; flex-wrap: wrap; font-size: 12px; color: var(--gray-500); margin-top: 14px; }
    .prog-legend i { display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 5px; vertical-align: -1px; }
    .quiz-msg { padding: 14px 16px; border-radius: 12px; background: #fef2f2; color: #7f1d1d; font-size: 15px; }
    .quiz-link { background: none; border: 0; font: inherit; font-size: 13px; color: var(--gray-500); text-decoration: underline; cursor: pointer; padding: 0; }
    @media (max-width: 600px) { .quiz-card { padding: 20px 16px; } .quiz-q { font-size: 17px; } .quiz-phrase { font-size: 17px; } .stat b { font-size: 19px; } }
    .quiz-compte { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px 16px; font-size: 13px; color: var(--gray-500); margin: 0 0 14px; }
    .quiz-compte .liens { display: flex; gap: 14px; flex-wrap: wrap; }
    .quiz-card h2 { font-size: 22px; font-weight: 900; color: var(--gray-900); line-height: 1.25; margin-bottom: 10px; }
    .quiz-card > p { font-size: 15px; line-height: 1.6; margin-bottom: 10px; }
    .quiz-points { margin: 6px 0 4px 18px; font-size: 15px; line-height: 1.7; }
    .quiz-choice.sel { border-color: #f97316; background: #fff7ed; font-weight: 700; }
    /* Rapport de positionnement : couleurs PassCRPE (indigo, violet) */
    .rp-tete { border-radius: 22px; padding: 28px 24px; margin-bottom: 16px; color: #fff; text-align: center; background: linear-gradient(140deg, #312e81, #4f46e5 60%, #7c3aed); box-shadow: 0 16px 40px rgba(79,70,229,.25); }
    .rp-sur { font-size: 12px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; opacity: .8; }
    .rp-score { font-size: 64px; font-weight: 900; line-height: 1; margin: 10px 0 6px; letter-spacing: -1px; }
    .rp-titre { font-size: 22px; font-weight: 900; }
    .rp-sous { font-size: 14px; opacity: .85; margin-top: 6px; }
    .rp-bloc { margin-bottom: 16px; }
    .rp-bloc p { font-size: 15.5px; line-height: 1.7; color: var(--gray-700); }
    .rp-bloc strong { color: #3730a3; }
    .rp-mat { padding: 12px 0; border-bottom: 1px solid #eef2ff; }
    .rp-mat:last-child { border-bottom: 0; }
    .rp-ligne { display: grid; grid-template-columns: 150px 1fr 48px; gap: 12px; align-items: center; font-size: 15px; font-weight: 800; color: var(--gray-900); }
    .rp-ligne .barre { height: 12px; border-radius: 10px; background: #eef2ff; overflow: hidden; }
    .rp-ligne .barre span { display: block; height: 100%; border-radius: 10px; }
    .rp-ligne .pct { text-align: right; color: #3730a3; }
    .barre .acquis { background: #3730a3; } .barre .engage { background: #6366f1; } .barre .cours { background: #a5b4fc; } .barre .construire { background: #c4b5fd; }
    .rp-info { font-size: 13.5px; line-height: 1.55; color: var(--gray-600); margin-top: 6px; }
    .rp-chip { display: inline-block; font-size: 11.5px; font-weight: 800; padding: 3px 10px; border-radius: 100px; margin-right: 8px; }
    .rp-chip.acquis { background: #3730a3; color: #fff; } .rp-chip.engage { background: #e0e7ff; color: #3730a3; } .rp-chip.cours { background: #eef2ff; color: #4f46e5; } .rp-chip.construire { background: #f5f3ff; color: #6d28d9; border: 1px solid #ddd6fe; }
    .rp-niv { display: block; margin-top: 3px; color: var(--gray-500); }
    .rp-niv strong { color: #4f46e5; }
    .rp-listes { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
    .rp-listes h3 { font-size: 16px; font-weight: 900; color: var(--gray-900); margin-bottom: 8px; }
    .rp-listes ul { list-style: none; display: grid; gap: 8px; }
    .rp-listes li { font-size: 14px; line-height: 1.45; color: var(--gray-700); }
    .rp-listes .mat { display: block; font-size: 11.5px; font-weight: 800; color: #6366f1; text-transform: uppercase; letter-spacing: .03em; }
    .rp-plan { margin: 4px 0 0 20px; display: grid; gap: 8px; font-size: 15px; line-height: 1.6; color: var(--gray-700); }
    .rp-plan .niv { font-size: 12px; font-weight: 800; color: #4f46e5; background: #eef2ff; border-radius: 100px; padding: 2px 8px; }
    .rp-note { font-size: 13px !important; color: var(--gray-500) !important; margin-top: 14px; }
    @media (max-width: 600px) { .rp-ligne { grid-template-columns: 105px 1fr 42px; font-size: 13.5px; } .rp-listes { grid-template-columns: 1fr; } .rp-score { font-size: 52px; } }
    .paywall { margin: 0 0 16px; border: 2px solid #c7d2fe; background: linear-gradient(160deg, #eef2ff, #fff 60%); }
    .pw-grille { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: start; }
    .paywall .paypal-zone { margin-top: 4px; max-width: none; }
    .paywall .garantie { max-width: none; margin-top: 12px; }
    .pw-liens { display: flex; flex-wrap: wrap; gap: 6px 16px; margin-top: 12px; }
    .pw-cta { background: #4f46e5 !important; }
    .pw-cta:hover { background: #4338ca !important; }
    @media (max-width: 720px) { .pw-grille { grid-template-columns: 1fr; gap: 8px; } .paywall .quiz-points { display: none; } .paywall h2 { font-size: 19px; }
      .rp-tete { padding: 18px 16px; } .rp-score { font-size: 46px; margin: 6px 0 4px; } .rp-titre { font-size: 19px; } }
    .paywall .prix { font-size: 40px; font-weight: 900; color: var(--gray-900); letter-spacing: -1px; }
    .paywall .prix span { font-size: 14px; font-weight: 600; color: var(--gray-500); letter-spacing: 0; }
    .garantie { display: flex; gap: 14px; align-items: flex-start; margin: 16px 0 4px; padding: 14px 16px; border-radius: 14px; background: #f0fdf4; border: 2px solid #86efac; max-width: 560px; font-size: 14px; line-height: 1.55; color: #14532d; }
    .garantie .sceau { font-size: 30px; line-height: 1; flex-shrink: 0; }
    .garantie strong { display: block; font-size: 16px; font-weight: 900; color: #14532d; margin-bottom: 2px; }
    .paypal-zone { display: grid; gap: 10px; margin-top: 16px; max-width: 420px; }
    .quiz-wrap { padding-bottom: 110px; }
    .quiz-tabbar { position: fixed; left: 0; right: 0; bottom: 0; top: auto; height: auto; padding: 0; z-index: 90; display: flex; justify-content: center; background: #fff; border-top: 1px solid var(--gray-100); }
    .quiz-tabbar a { flex: 1; max-width: 160px; display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 10px 0 12px; font-size: 12px; font-weight: 600; color: var(--gray-400); text-decoration: none; }
    .quiz-tabbar a:hover { color: var(--gray-600); }
    .quiz-tabbar a.actif { color: var(--indigo-600); }
    .quiz-tabbar .ico { position: relative; }
    .quiz-tabbar svg { width: 20px; height: 20px; display: block; }
    .quiz-tabbar .pastille { position: absolute; top: -2px; right: -3px; width: 8px; height: 8px; border-radius: 50%; background: #ef4444; border: 1.5px solid #fff; }
  .quiz-confirm { background: #dcfce7; color: #166534; font-weight: 600; border-radius: 12px; padding: 12px 16px; margin: 0 0 16px; }
"""

JS = """<script>
(function () {
  var SB = window.passcrpeSB, PRIX = '__PRIX__';
  var compte = null, tst = null, CLE_TEST = 'passcrpe-quiz-test', testPret = null;
  function jeton() { return SB.auth.getSession().then(function (r) { return r.data.session ? r.data.session.access_token : null; }); }
  // Appels à l'API du quiz avec le jeton du compte ; les erreurs gardent leur code (connexion, paiement)
  function api(url, opts) {
    return jeton().then(function (t) {
      var h = { 'Content-Type': 'application/json' }; if (t) h.Authorization = 'Bearer ' + t;
      return fetch(url, Object.assign({}, opts || {}, { headers: h }));
    }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) {
      if (!r.ok) { var e = new Error(d.error || 'Erreur'); e.code = d.code; e.status = r.status; throw e; } return d; }); });
  }
  var MATIERES = __MATIERES__, SERIE = __SERIE__, MAITRISE = __MAITRISE__, INTERVALLES = __INTERVALLES__, APRES_ERREUR = __APRES_ERREUR__;
  var JOUR = 86400000, CLE = 'passcrpe-quiz-v1';
  var NIVEAUX = { facile: 'Facile', intermediaire: 'Intermédiaire', difficile: 'Avancé' };
  var CLE_CHOIX = 'passcrpe-quiz-choix';
  var root = document.getElementById('quiz-app');
  var catalogues = {}, st = null, choix = lireChoix();

  // ── Progression (navigateur uniquement) ──
  function lire() { try { return JSON.parse(localStorage.getItem(CLE)) || {}; } catch (e) { return {}; } }
  function ecrire(p) { try { localStorage.setItem(CLE, JSON.stringify(p)); } catch (e) {} }
  // Dernier choix de matière et de niveau, retrouvé à la prochaine visite
  function lireChoix() { var c = {}; try { c = JSON.parse(localStorage.getItem(CLE_CHOIX)) || {}; } catch (e) {}
    return { mat: MATIERES.some(function (m) { return m[0] === c.mat; }) ? c.mat : MATIERES[0][0], niveau: NIVEAUX[c.niveau] ? c.niveau : 'facile' }; }
  function garderChoix() { try { localStorage.setItem(CLE_CHOIX, JSON.stringify(choix)); } catch (e) {} }
  function prog(mat) { var p = lire(); return (p[mat] && p[mat].notions) ? p[mat] : { notions: {}, series: 0 }; }
  function sauver(mat, pm) { var p = lire(); p[mat] = pm; ecrire(p); }

  function esc(v) { return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function label(k) { for (var i = 0; i < MATIERES.length; i++) if (MATIERES[i][0] === k) return MATIERES[i][1]; return k; }
  function top() { window.scrollTo({ top: root.offsetTop - 90, behavior: 'smooth' }); }
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function jours(n) { return n <= 1 ? 'demain' : 'dans ' + n + ' jours'; }
  function dateFr(ts) { return new Date(ts).toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' }); }

  function grouper(qs) {
    var notions = {}, ordre = [];
    qs.forEach(function (q) { if (!notions[q.notion]) { notions[q.notion] = { cle: q.notion, niveau: q.niveau, theme: q.theme, questions: [] }; ordre.push(q.notion); } notions[q.notion].questions.push(q); });
    return { notions: notions, ordre: ordre };
  }
  function charger(mat) {
    if (catalogues[mat]) return Promise.resolve(catalogues[mat]);
    return api('/api/quiz/catalogue?matiere=' + encodeURIComponent(mat)).then(function (d) {
      if (!d.questions || !d.questions.length) throw new Error(d.error || 'vide');
      catalogues[mat] = grouper(d.questions); return catalogues[mat];
    });
  }

  // ── Composition d'une série du niveau choisi : révisions dues, puis nouvelles notions, puis révisions anticipées ──
  function composer(cat, pm, niveau) {
    var now = Date.now(), dues = [], neuves = [], attente = [], rang = { facile: 0, intermediaire: 1, difficile: 2 };
    cat.ordre.forEach(function (k) {
      if (niveau && cat.notions[k].niveau !== niveau) return;
      var s = pm.notions[k];
      if (!s) neuves.push(k);
      else if (s.maitrise) return;
      else if ((s.due || 0) <= now) dues.push(k);
      else attente.push(k);
    });
    dues.sort(function (a, b) { return (pm.notions[a].due || 0) - (pm.notions[b].due || 0); });
    neuves = melange(neuves).sort(function (a, b) { return rang[cat.notions[a].niveau] - rang[cat.notions[b].niveau]; });
    attente.sort(function (a, b) { return pm.notions[a].due - pm.notions[b].due; });
    var choisies = dues.concat(neuves, attente).slice(0, SERIE);
    return melange(choisies.map(function (k) {
      var s = pm.notions[k] || { ok: [], vus: [] }, qs = cat.notions[k].questions;
      var restantes = qs.filter(function (q) { return s.ok.indexOf(q.id) < 0; });
      if (!restantes.length) restantes = qs;
      var jamais = restantes.filter(function (q) { return s.vus.indexOf(q.id) < 0; });
      var pool = jamais.length ? jamais : restantes;
      return pool[Math.floor(Math.random() * pool.length)];
    }));
  }

  function bilan(mat, cat, niveau) {
    var pm = prog(mat), m = 0, c = 0, n = 0, now = Date.now(), prochaine = null, dues = 0;
    cat.ordre.forEach(function (k) {
      if (niveau && cat.notions[k].niveau !== niveau) return;
      n++;
      var s = pm.notions[k]; if (!s) return;
      if (s.maitrise) m++; else { c++; if ((s.due || 0) <= now) dues++; else if (!prochaine || s.due < prochaine) prochaine = s.due; }
    });
    return { maitrisees: m, encours: c, total: n, dues: dues, prochaine: prochaine };
  }

  // ── Écrans ──
  function intro(v) { var l = document.querySelector('.quiz-lead'), h = document.querySelector('.quiz-wrap > h1'); if (l) l.hidden = !v; if (h) h.hidden = !v; }
  function accueil() {
    st = null; intro(true);
    root.innerHTML = barreCompte() + '<div class="quiz-card quiz-filtres">' +
      '<div class="quiz-filtre"><label for="quiz-mat">Matière</label><select id="quiz-mat" class="quiz-select">' +
      MATIERES.map(function (m) { return '<option value="' + m[0] + '"' + (m[0] === choix.mat ? ' selected' : '') + '>' + esc(m[1]) + '</option>'; }).join('') + '</select></div>' +
      '<div class="quiz-filtre"><span class="lbl" id="quiz-niv-lbl">Niveau</span><div class="quiz-niveaux" role="group" aria-labelledby="quiz-niv-lbl">' +
      Object.keys(NIVEAUX).map(function (n) { return '<button type="button" class="quiz-niveau" data-niv="' + n + '" aria-pressed="' + (n === choix.niveau) + '">' + NIVEAUX[n] + '</button>'; }).join('') + '</div></div>' +
      '<div class="quiz-resume" id="quiz-resume">…</div>' +
      '<div class="quiz-actions" style="margin-top:0"><button type="button" class="quiz-btn" data-act="start">Lancer une série</button><button type="button" class="quiz-btn ghost" data-act="prog-choix">Ma progression</button></div>' +
      '</div>';
    resume();
  }

  // Résumé du choix en cours : notions du niveau, maîtrisées, à réviser
  function resume() {
    var el = document.getElementById('quiz-resume'); if (!el) return;
    var mat = choix.mat, niveau = choix.niveau;
    el.textContent = 'Chargement…';
    charger(mat).then(function (cat) {
      if (!document.getElementById('quiz-resume') || choix.mat !== mat || choix.niveau !== niveau) return;
      var b = bilan(mat, cat, niveau), nq = 0;
      cat.ordre.forEach(function (k) { if (cat.notions[k].niveau === niveau) nq += cat.notions[k].questions.length; });
      // Une série pose une question par notion non maîtrisée, dans la limite de 20
      var serie = Math.min(SERIE, b.total - b.maitrisees);
      el.innerHTML = '<b>' + esc(label(mat)) + ' · ' + NIVEAUX[niveau] + '</b> : ' + nq + ' questions sur ' + b.total + ' notions' +
        (serie ? ', en séries de ' + serie + ' questions' : '') + '. ' +
        b.maitrisees + ' notion' + (b.maitrisees > 1 ? 's' : '') + ' maîtrisée' + (b.maitrisees > 1 ? 's' : '') +
        (b.dues ? ', <b>' + b.dues + ' à réviser aujourd\\'hui</b>' : '') + '.';
    }).catch(function () { el.textContent = 'Le quiz n\\'a pas pu être chargé. Réessaie dans quelques instants.'; });
  }

  // ── Compte : connexion, test de positionnement, paiement ──
  // Lien vers le résultat du test ; l'e-mail, « Mes outils » et la déconnexion sont dans le menu de l'en-tête
  function barreCompte() {
    return compte && compte.positionnement ? '<div class="quiz-compte"><span></span><span class="liens"><button type="button" class="quiz-link" data-act="voir-resultat">Mon test de positionnement</button></span></div>' : '';
  }
  function erreur(msg) {
    root.innerHTML = '<div class="quiz-msg">' + esc(msg) + '</div><div class="quiz-actions"><button type="button" class="quiz-btn ghost" data-act="boot">Réessayer</button></div>';
  }
  // Choix de l'écran selon le compte : connexion → test → résultat et paiement → quiz
  function boot() {
    st = null; tst = null;
    root.innerHTML = '<div class="quiz-card"><p>Chargement…</p></div>';
    jeton().then(function (t) {
      if (!t) return connexion();
      return api('/api/quiz/compte').then(function (c) {
        compte = c;
        if (!c.positionnement) return introTest();
        if (!c.paid) return resultat(c.positionnement);
        accueil();
      });
    }).catch(function (e) { if (e.status === 401) return connexion(); erreur('Votre compte n\\'a pas pu être chargé. Réessayez dans quelques instants.'); });
  }
  function connexion() {
    root.innerHTML = '<div class="quiz-card"><h2>Connectez-vous pour accéder au Quiz CRPE</h2>' +
      '<p>Créez votre compte gratuitement : vous commencez par un <strong>test de positionnement de 15 minutes</strong> qui vous donne la carte de vos forces et faiblesses dans les 9 matières.</p>' +
      '<div class="quiz-actions"><a class="quiz-btn" href="/quiz?auth=register">Créer mon compte gratuitement</a><a class="quiz-btn ghost" href="/quiz?auth=login">J\\'ai déjà un compte PassCRPE</a></div></div>';
  }
  function introTest() {
    var t = lireTest();
    // Le test est préparé en arrière-plan pendant la lecture de l'introduction : « Commencer » est immédiat
    if (!t && !testPret) testPret = api('/api/quiz/positionnement').catch(function (e) { testPret = null; throw e; });
    root.innerHTML = barreCompte() + '<div class="quiz-card"><h2>Votre test de positionnement</h2>' +
      '<p>Avant d\\'accéder au quiz, faites le point sur votre niveau. Le test est <strong>gratuit</strong> et dure environ <strong>15 minutes</strong> :</p>' +
      '<ul class="quiz-points"><li>45 questions, 5 dans chacune des 9 matières ;</li><li>des questions faciles, intermédiaires et avancées ;</li><li>pas de correction pendant le test : à la fin, vous obtenez votre carte des forces et faiblesses, matière par matière.</li></ul>' +
      '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="test-start">' + (t ? 'Reprendre mon test (question ' + (t.i + 1) + ' / ' + t.qs.length + ')' : 'Commencer mon test') + '</button></div></div>';
  }
  function lireTest() { try { var t = JSON.parse(localStorage.getItem(CLE_TEST)); return t && t.qs && t.qs.length && t.user === (compte && compte.email) ? t : null; } catch (e) { return null; } }
  function garderTest() { try { localStorage.setItem(CLE_TEST, JSON.stringify(tst)); } catch (e) {} }
  function testStart() {
    tst = lireTest();
    if (tst) return testQuestion();
    root.innerHTML = '<div class="quiz-card"><p>Préparation de votre test…</p></div>';
    (testPret || api('/api/quiz/positionnement')).then(function (d) {
      testPret = null;
      if (d.deja) { compte.positionnement = d.deja; return resultat(d.deja); }
      tst = { user: compte.email, qs: d.questions, i: 0, rep: [] }; garderTest(); testQuestion(); top();
    }).catch(function () { testPret = null; erreur('Le test n\\'a pas pu être chargé. Réessayez dans quelques instants.'); });
  }
  function testQuestion() {
    var q = tst.qs[tst.i], n = tst.qs.length, corps;
    tst.val = null;
    if (q.type === 'numerique') corps = '<div class="quiz-num"><input type="text" inputmode="decimal" autocomplete="off" placeholder="Votre réponse (nombre)" aria-label="Votre réponse" id="t-num"></div>';
    else if (q.type === 'cliquer_mot') { tst.val = []; corps = '<p class="quiz-hint">Cliquez sur le ou les mots.</p><div class="quiz-phrase">' + q.choix.map(function (t, k) {
        return /[\\wÀ-ÿ]/.test(t) ? '<button type="button" class="tok" data-ttok="' + k + '">' + esc(t) + '</button>' : '<span class="punct">' + esc(t) + '</span>'; }).join(' ') + '</div>'; }
    else corps = '<div class="quiz-choices">' + q.choix.map(function (c, k) { return '<button type="button" class="quiz-choice" data-tk="' + k + '">' + esc(c) + '</button>'; }).join('') + '</div>';
    root.innerHTML = '<div class="quiz-card"><div class="quiz-top"><span class="mat">Test de positionnement · ' + esc(label(q.matiere)) + '</span><span>Question ' + (tst.i + 1) + ' / ' + n + '</span></div>' +
      '<div class="quiz-bar"><span style="width:' + Math.round(tst.i / n * 100) + '%"></span></div>' +
      '<p class="quiz-q">' + esc(q.question) + '</p>' + corps +
      '<p class="quiz-hint" id="t-aide">' + (q.type === 'qcm' ? 'Cliquez sur une réponse pour passer à la question suivante.' : 'Appuyez sur Entrée pour passer à la question suivante.') + '</p>' +
      '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="t-suivant">' + (tst.i === n - 1 ? 'Terminer le test' : 'Question suivante →') + '</button><button type="button" class="quiz-btn ghost" data-act="t-passer">Je ne sais pas</button></div></div>';
    var inp = document.getElementById('t-num'); if (inp) inp.focus();
  }
  function testRepondre(passer) {
    var q = tst.qs[tst.i], v = '';
    if (!passer) {
      if (q.type === 'numerique') v = (document.getElementById('t-num').value || '').trim();
      else if (q.type === 'cliquer_mot') v = tst.val.slice().sort(function (a, b) { return a - b; }).join(',');
      else v = tst.val == null ? '' : q.choix[tst.val];
      if (v === '') { var aide = document.getElementById('t-aide'); if (aide) { aide.textContent = 'Choisissez une réponse, ou cliquez sur « Je ne sais pas ».'; aide.style.color = '#b91c1c'; } return; }
    }
    tst.rep[tst.i] = { id: q.id, reponse: v }; tst.i++; garderTest();
    if (tst.i < tst.qs.length) { testQuestion(); return; }
    root.innerHTML = '<div class="quiz-card"><p>Correction de votre test…</p></div>';
    api('/api/quiz/positionnement', { method: 'POST', body: JSON.stringify({ reponses: tst.rep }) }).then(function (d) {
      try { localStorage.removeItem(CLE_TEST); } catch (e) {}
      compte.positionnement = d.resultat; tst = null; resultat(d.resultat); top();
    }).catch(function () { tst.i--; garderTest(); erreur('Votre test n\\'a pas pu être corrigé. Vos réponses sont gardées : réessayez.'); });
  }
  // ── Rapport de positionnement : diagnostic qualitatif construit par des règles fixes (sans IA) ──
  var CATS = [
    { min: 80, cle: 'acquis', label: 'Acquis', txt: "Des connaissances solides dans cette matière." },
    { min: 60, cle: 'engage', label: 'Bien engagé', txt: "Les bases sont là ; quelques notions restent à fixer." },
    { min: 40, cle: 'cours', label: "En cours d'acquisition", txt: "Des repères existent, mais plusieurs notions sont à revoir." },
    { min: 0, cle: 'construire', label: 'À construire', txt: "C'est ici que vos révisions auront le plus d'effet." }
  ];
  function categorie(p) { for (var i = 0; i < CATS.length; i++) if (p >= CATS[i].min) return CATS[i]; return CATS[CATS.length - 1]; }
  function taux(x) { return x && x.n ? x.ok / x.n : null; }
  // Niveau conseillé pour démarrer une matière, d'après les questions faciles et intermédiaires du test
  function niveauConseille(m) {
    if (!m.niveaux) return m.pct >= 80 ? 'difficile' : m.pct >= 40 ? 'intermediaire' : 'facile';
    var f = taux(m.niveaux.facile), i = taux(m.niveaux.intermediaire);
    if (f !== null && f < 1) return 'facile';
    if (i !== null && i < 1) return 'intermediaire';
    return 'difficile';
  }
  function liste(noms) { return noms.length < 2 ? noms.join('') : noms.slice(0, -1).join(', ') + ' et ' + noms[noms.length - 1]; }
  function profil(r) {
    var p = r.pct, titre = p >= 75 ? 'Un profil solide' : p >= 50 ? 'Un profil en bonne voie' : p >= 30 ? 'Des bases à consolider' : 'Un profil à construire';
    var tri = r.matieres.slice().sort(function (a, b) { return b.pct - a.pct; });
    var appuis = tri.filter(function (m) { return m.pct >= 80; }).map(function (m) { return m.label; });
    if (!appuis.length && tri[0] && tri[0].pct >= 60) appuis = [tri[0].label];
    var priorites = tri.slice().reverse().filter(function (m) { return m.pct < 60; }).slice(0, 3).map(function (m) { return m.label; });
    var phrases = [];
    if (appuis.length) phrases.push('Vos points d’appui : <strong>' + esc(liste(appuis)) + '</strong>.');
    if (priorites.length) phrases.push('Vos priorités : <strong>' + esc(liste(priorites)) + '</strong>.');
    // Lecture par niveau de difficulté, sur l'ensemble du test
    var F = { ok: 0, n: 0 }, A = { ok: 0, n: 0 };
    r.matieres.forEach(function (m) { if (!m.niveaux) return; ['facile'].forEach(function (k) { var x = m.niveaux[k]; if (x) { F.ok += x.ok; F.n += x.n; } }); var a = m.niveaux.difficile; if (a) { A.ok += a.ok; A.n += a.n; } });
    var tf = taux(F), ta = taux(A);
    if (tf !== null) {
      if (tf < .5) phrases.push("Les questions faciles vous ont posé difficulté dans plusieurs matières : priorité aux fondamentaux. C'est aussi là que les progrès sont les plus rapides.");
      else if (ta !== null && ta < .5) phrases.push("Les fondamentaux sont bien là : ce sont les questions avancées qui feront maintenant la différence.");
      else phrases.push("Vous réussissez aussi bien les questions faciles que les plus exigeantes : continuez à monter en difficulté.");
    }
    return { titre: titre, texte: phrases.join(' ') };
  }
  // Plan de révision : les matières les plus fragiles d'abord, deux par semaine, avec le niveau conseillé
  function plan(r) {
    // seules les matières pas encore acquises entrent dans le plan
    var tri = r.matieres.filter(function (m) { return m.pct < 80; }).sort(function (a, b) { return a.pct - b.pct; }), semaines = [];
    for (var i = 0; i < tri.length && semaines.length < 3; i += 2) semaines.push(tri.slice(i, i + 2));
    return semaines.map(function (s, k) {
      return '<li><strong>Semaine ' + (k + 1) + '</strong> : ' + s.map(function (m) { return esc(m.label) + ' <span class="niv">' + NIVEAUX[niveauConseille(m)] + '</span>'; }).join(' · ') + '</li>';
    }).join('') + '<li><strong>Ensuite</strong> : consolidez vos matières fortes au niveau avancé, et laissez les révisions espacées faire revenir chaque notion.</li>';
  }
  function resultat(r) {
    var pf = profil(r), tri = r.matieres.slice().sort(function (a, b) { return b.pct - a.pct; }), forts = [], faibles = [];
    tri.forEach(function (m) { m.themes.forEach(function (t) { if (t.ok === t.n) forts.push([m.label, t.theme]); }); });
    tri.slice().reverse().forEach(function (m) { m.themes.forEach(function (t) { if (t.ok / t.n < .5) faibles.push([m.label, t.theme]); }); });
    var item = function (x) { return '<li><span class="mat">' + esc(x[0]) + '</span>' + esc(x[1]) + '</li>'; };
    var date = r.date ? new Date(r.date).toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' }) : '';
    var html = barreCompte() +
      '<div class="rp-tete"><div class="rp-sur">Rapport de positionnement' + (date ? ' · ' + date : '') + '</div>' +
      '<div class="rp-score">' + r.pct + ' %</div><div class="rp-titre">' + pf.titre + '</div>' +
      '<div class="rp-sous">' + r.ok + ' bonnes réponses sur ' + r.n + ' · 9 matières · 3 niveaux</div></div>' +
      '<!--PAIEMENT-->' +
      '<div class="quiz-card rp-bloc"><h2>Votre profil</h2><p>' + pf.texte + '</p></div>' +
      '<div class="quiz-card rp-bloc"><h2>Matière par matière</h2>' +
      tri.map(function (m) {
        var c = categorie(m.pct), nv = m.niveaux, det = nv ? ['facile', 'intermediaire', 'difficile'].filter(function (k) { return nv[k]; }).map(function (k) { return NIVEAUX[k].toLowerCase() + ' ' + nv[k].ok + '/' + nv[k].n; }).join(' · ') : '';
        return '<div class="rp-mat"><div class="rp-ligne"><span class="nom">' + esc(m.label) + '</span><div class="barre"><span class="' + c.cle + '" style="width:' + Math.max(m.pct, 4) + '%"></span></div><span class="pct">' + m.pct + ' %</span></div>' +
          '<div class="rp-info"><span class="rp-chip ' + c.cle + '">' + c.label + '</span>' + c.txt + ' <span class="rp-niv">Niveau conseillé pour démarrer : <strong>' + NIVEAUX[niveauConseille(m)] + '</strong>' + (det ? ' (' + det + ')' : '') + '</span></div></div>';
      }).join('') + '</div>' +
      '<div class="rp-listes"><div class="quiz-card"><h3>💪 Vos points forts</h3><ul>' + (forts.slice(0, 6).map(item).join('') || '<li>Ils apparaîtront au fil de vos séries.</li>') + '</ul></div>' +
      '<div class="quiz-card"><h3>🎯 À travailler en priorité</h3><ul>' + (faibles.slice(0, 6).map(item).join('') || '<li>Aucune lacune nette : visez la maîtrise complète.</li>') + '</ul></div></div>' +
      '<div class="quiz-card rp-bloc"><h2>Votre plan de révision</h2><ol class="rp-plan">' + plan(r) + '</ol>' +
      '<p class="rp-note">Ce diagnostic repose sur 45 questions (5 par matière) : c’est une première photographie de votre niveau. Vos séries d’entraînement l’affinent jour après jour.</p></div>';
    if (compte && compte.paid) html = html.replace('<!--PAIEMENT-->', '') + '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="home">Aller au quiz</button></div>';
    else {
      // Paiement visible dès l'arrivée sur le rapport, juste sous le score
      var pay = '<div class="quiz-card paywall" id="paiement"><div class="pw-grille"><div>' +
        '<h2>Débloquez le Quiz CRPE pour combler ces lacunes</h2>' +
        '<div class="prix">' + PRIX + ' <span>TTC · paiement unique</span></div>' +
        '<ul class="quiz-points"><li>2 700 questions, 9 matières, 3 niveaux ;</li><li>des séries de 20 notées sur 20, avec l’explication de chaque erreur ;</li><li>des révisions espacées et votre progression par thème.</li></ul>' +
        '</div><div>' +
        '<div class="paypal-zone"><div id="pp-paypal"></div><div id="pp-carte"></div></div>' +
        '<p class="quiz-hint" id="pp-msg">Paiement sécurisé par PayPal, par compte PayPal ou carte bancaire.</p>' +
        '<div class="garantie"><span class="sceau">🛡️</span><div><strong>Satisfait ou remboursé pendant 14 jours</strong>Si le quiz ne vous convient pas, écrivez-nous dans les 14 jours suivant votre achat : remboursement intégral, sans avoir à vous justifier.</div></div>' +
        '<p class="pw-liens"><a class="quiz-link" href="/app?onglet=support&produit=quiz&categorie=paiement">Un problème avec le paiement ? Contactez le support</a><button type="button" class="quiz-link" data-act="boot">J’ai déjà payé : actualiser mon accès</button></p>' +
        '</div></div></div>';
      html = html.replace('<!--PAIEMENT-->', pay) + '<div class="quiz-actions" style="justify-content:center"><a class="quiz-btn pw-cta" href="#paiement">Débloquer le quiz pour ' + PRIX + '</a></div>';
    }
    root.innerHTML = html;
    intro(false); // l'introduction du quiz est masquée sur le rapport : le paiement reste visible sans faire défiler
    if (!(compte && compte.paid)) paypal();
  }
  function chargerPaypal() {
    if (window.paypal && window.paypal.Buttons) return Promise.resolve();
    if (!compte.paypal_client_id) return Promise.reject(new Error('id'));
    return new Promise(function (ok, ko) {
      var s = document.createElement('script');
      s.src = 'https://www.paypal.com/sdk/js?client-id=' + encodeURIComponent(compte.paypal_client_id) + '&components=buttons&intent=capture&currency=EUR&disable-funding=venmo';
      s.onload = ok; s.onerror = ko; document.head.appendChild(s);
    });
  }
  // Même fonctionnement que PassCRPE : commande créée par le serveur (custom_id = compte), capture puis déblocage
  function paypal() {
    var msg = function (t, err) { var el = document.getElementById('pp-msg'); if (el) { el.textContent = t; el.style.color = err ? '#b91c1c' : ''; } };
    chargerPaypal().then(function () {
      var opts = {
        createOrder: function () { msg('Ouverture du paiement…'); return api('/api/quiz/paypal/create-order', { method: 'POST' }).then(function (d) { return d.id; }); },
        onApprove: function (data) {
          msg('Confirmation du paiement…');
          return api('/api/quiz/paypal/capture-order', { method: 'POST', body: JSON.stringify({ orderID: data.orderID }) }).then(function (d) {
            if (d.status !== 'COMPLETED') throw new Error('non confirmé');
            window.dataLayer = window.dataLayer || []; window.dataLayer.push({ event: 'purchase', parcours: 'quizcrpe', value: 59, currency: 'EUR' });
            boot();
          }).catch(function () { msg('Le paiement n\\'a pas pu être confirmé. S\\'il a été débité, cliquez sur « J\\'ai déjà payé » dans quelques instants.', true); });
        },
        onError: function () { msg('Une erreur est survenue avec PayPal. Réessayez.', true); }
      };
      var b1 = window.paypal.Buttons(Object.assign({ fundingSource: window.paypal.FUNDING.PAYPAL, style: { layout: 'horizontal', color: 'blue', shape: 'pill', label: 'pay', height: 45 } }, opts));
      var b2 = window.paypal.Buttons(Object.assign({ fundingSource: window.paypal.FUNDING.CARD, style: { layout: 'horizontal', color: 'black', shape: 'pill', label: 'pay', height: 45 } }, opts));
      if (b1.isEligible()) b1.render('#pp-paypal');
      if (b2.isEligible()) b2.render('#pp-carte');
    }).catch(function () { msg('Le module de paiement PayPal n\\'a pas pu se charger. Rechargez la page.', true); });
  }

  function demarrer(mat, niveau) {
    root.innerHTML = '<div class="quiz-card"><p>Chargement des questions…</p></div>';
    charger(mat).then(function (cat) {
      var serie = composer(cat, prog(mat), niveau);
      if (!serie.length) return progression(mat, 'Toutes les notions de niveau ' + NIVEAUX[niveau].toLowerCase() + ' sont maîtrisées dans cette matière. Bravo ! Essayez un autre niveau.');
      st = { mat: mat, niveau: niveau, cat: cat, serie: serie, i: 0, score: 0, recap: [], sel: [], repondu: false };
      question(); top();
    }).catch(function (e) {
      if (e.status === 401 || e.status === 402) return boot();
      root.innerHTML = '<div class="quiz-msg">Le quiz n\\'a pas pu être chargé. Réessaie dans quelques instants.</div><div class="quiz-actions"><button type="button" class="quiz-btn ghost" data-act="home">Changer de matière ou de niveau</button></div>';
    });
  }

  function entete(q) {
    var n = st.serie.length;
    return '<div class="quiz-top"><span class="mat">' + esc(label(st.mat)) + ' · ' + NIVEAUX[st.niveau] + '</span><span>Question ' + (st.i + 1) + ' / ' + n + '</span></div>' +
      '<div class="quiz-bar"><span style="width:' + Math.round(st.i / n * 100) + '%"></span></div>' +
      '<div class="quiz-meta"><span class="chip ' + q.niveau + '">' + (NIVEAUX[q.niveau] || '') + '</span>' +
      (q.theme ? '<span class="chip theme">' + esc(q.theme) + (q.sous_theme ? ' › ' + esc(q.sous_theme) : '') + '</span>' : '') +
      (q.classe ? '<span class="chip">Programme de ' + esc(q.classe) + '</span>' : '') + '</div>' +
      (q.objectif ? '<p class="quiz-objectif"><strong>Objectif du programme :</strong> ' + esc(q.objectif) + '</p>' : '');
  }

  function question() {
    var q = st.serie[st.i], corps = '';
    st.repondu = false; st.sel = [];
    if (q.type === 'numerique') {
      corps = '<form class="quiz-num" data-form="num"><input type="text" inputmode="decimal" autocomplete="off" placeholder="Votre réponse (nombre)" aria-label="Votre réponse"><button type="submit" class="quiz-btn">Valider</button></form>';
    } else if (q.type === 'cliquer_mot') {
      corps = '<p class="quiz-hint">Cliquez sur le ou les mots, puis validez.</p><div class="quiz-phrase">' + q.choix.map(function (t, k) {
        return /[\\wÀ-ÿ]/.test(t) ? '<button type="button" class="tok" data-tok="' + k + '">' + esc(t) + '</button>' : '<span class="punct">' + esc(t) + '</span>';
      }).join(' ') + '</div><button type="button" class="quiz-btn" data-act="valider" disabled>Valider</button>';
    } else {
      corps = '<div class="quiz-choices">' + q.choix.map(function (c, k) { return '<button type="button" class="quiz-choice" data-k="' + k + '">' + esc(c) + '</button>'; }).join('') + '</div>';
    }
    root.innerHTML = '<div class="quiz-card">' + entete(q) + '<p class="quiz-q">' + esc(q.question) + '</p>' + corps + '<div id="quiz-fb"></div></div>';
    var inp = root.querySelector('.quiz-num input'); if (inp) inp.focus();
  }

  function envoyer(reponse, afficher) {
    if (st.repondu) return; st.repondu = true;
    var q = st.serie[st.i];
    api('/api/quiz/reponse', { method: 'POST', body: JSON.stringify({ id: q.id, reponse: reponse }) })
      .then(function (d) {
        afficher(d);
        var suite = enregistrer(q, d.correct);
        if (d.correct) st.score++;
        st.recap.push({ q: q.question, ok: d.correct, attendu: d.attendu });
        var last = st.i === st.serie.length - 1;
        document.getElementById('quiz-fb').innerHTML =
          '<div class="quiz-feedback ' + (d.correct ? 'ok' : 'ko') + '"><strong>' + (d.correct ? 'Bonne réponse !' : 'Ce n\\'est pas la bonne réponse. Réponse attendue : ' + esc(d.attendu)) + '</strong>' + esc(d.explication) +
          '<span class="suite">' + suite + '</span></div>' +
          '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="next">' + (last ? 'Voir ma note' : 'Question suivante →') + '</button></div>';
      }).catch(function (e) {
        if (e.status === 401 || e.status === 402) return boot();
        st.repondu = false;
        document.getElementById('quiz-fb').innerHTML = '<div class="quiz-msg" style="margin-top:16px">La correction n\\'a pas pu être chargée. Réessaie.</div>';
      });
  }

  // Révision espacée : met à jour la notion et renvoie le message affiché sous l'explication
  function enregistrer(q, correct) {
    var pm = prog(st.mat), s = pm.notions[q.notion] || { ok: [], vus: [], erreurs: 0, due: 0, maitrise: false };
    var now = Date.now(), msg;
    if (s.vus.indexOf(q.id) < 0) s.vus.push(q.id);
    if (correct) {
      if (s.ok.indexOf(q.id) < 0) s.ok.push(q.id);
      if (s.ok.length >= MAITRISE) { s.maitrise = true; msg = '🎉 Notion maîtrisée : ' + MAITRISE + ' bonnes réponses à des questions différentes.'; }
      else { var j = INTERVALLES[Math.min(s.ok.length - 1, INTERVALLES.length - 1)]; s.due = now + j * JOUR; msg = 'Bonne réponse ' + s.ok.length + ' / ' + MAITRISE + ' pour cette notion : une autre formulation vous sera posée ' + jours(j) + '.'; }
    } else {
      s.erreurs = (s.erreurs || 0) + 1; s.due = now + APRES_ERREUR * JOUR;
      msg = 'Une question similaire vous sera reposée ' + jours(APRES_ERREUR) + ', pour ancrer la notion.';
    }
    pm.notions[q.notion] = s; sauver(st.mat, pm);
    return msg;
  }

  function fin() {
    var pm = prog(st.mat); pm.series = (pm.series || 0) + 1; sauver(st.mat, pm);
    var n = st.serie.length, s = st.score, b = bilan(st.mat, st.cat, st.niveau);
    var note = Math.round(s / n * 20 * 2) / 2;
    var msg = note >= 16 ? 'Excellent travail !' : note >= 12 ? 'Bon travail, continuez comme ça.' : note >= 8 ? 'C\\'est un début : les notions ratées reviendront pour être retravaillées.' : 'Ces notions sont à retravailler : elles reviendront dans vos prochaines séries.';
    root.innerHTML = '<div class="quiz-card quiz-score">' +
      '<div class="quiz-top" style="justify-content:center"><span class="mat">' + esc(label(st.mat)) + ' · ' + NIVEAUX[st.niveau] + ' · série ' + pm.series + '</span></div>' +
      '<div class="big">' + String(note).replace('.', ',') + ' / 20</div><p>' + s + ' bonne' + (s > 1 ? 's' : '') + ' réponse' + (s > 1 ? 's' : '') + ' sur ' + n + '. ' + msg + '</p>' +
      '<div class="stats"><div class="stat"><b>' + b.maitrisees + '</b><span>notions maîtrisées</span></div><div class="stat"><b>' + b.encours + '</b><span>en cours</span></div><div class="stat"><b>' + (b.total - b.maitrisees - b.encours) + '</b><span>à découvrir</span></div></div>' +
      (b.prochaine && !b.dues ? '<p style="font-size:13px;color:var(--gray-500)">Prochaines révisions à partir du ' + dateFr(b.prochaine) + '.</p>' : '') +
      '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="again">Nouvelle série de ' + SERIE + '</button><button type="button" class="quiz-btn ghost" data-act="prog">Ma progression</button><button type="button" class="quiz-btn ghost" data-act="home">Changer de matière ou de niveau</button></div>' +
      '<div class="quiz-recap">' + st.recap.map(function (r) {
        return '<div class="' + (r.ok ? 'r-ok' : 'r-ko') + '">' + esc(r.q) + (r.ok ? '' : ' <em>Réponse : ' + esc(r.attendu) + '</em>') + '</div>';
      }).join('') + '</div></div>';
    top();
  }

  function progression(mat, message) {
    charger(mat).then(function (cat) {
      var pm = prog(mat), b = bilan(mat, cat), themes = {}, ordre = [];
      cat.ordre.forEach(function (k) {
        var t = cat.notions[k].theme || 'Notions';
        if (!themes[t]) { themes[t] = { m: 0, c: 0, n: 0 }; ordre.push(t); }
        var s = pm.notions[k]; themes[t].n++;
        if (s && s.maitrise) themes[t].m++; else if (s) themes[t].c++;
      });
      var niveau = (st && st.niveau) || choix.niveau;
      st = { mat: mat, niveau: niveau, cat: cat };
      var parNiveau = Object.keys(NIVEAUX).map(function (n) { var x = bilan(mat, cat, n); return '<div class="stat"><b>' + x.maitrisees + ' / ' + x.total + '</b><span>' + NIVEAUX[n] + '</span></div>'; }).join('');
      root.innerHTML = '<div class="quiz-card">' +
        '<div class="quiz-top"><span class="mat">' + esc(label(mat)) + ' · ma progression</span><span>' + (pm.series || 0) + ' série' + ((pm.series || 0) > 1 ? 's' : '') + '</span></div>' +
        (message ? '<p style="font-weight:700;color:#166534">' + esc(message) + '</p>' : '') +
        '<div class="stats"><div class="stat"><b>' + b.maitrisees + ' / ' + b.total + '</b><span>notions maîtrisées</span></div><div class="stat"><b>' + b.encours + '</b><span>en cours</span></div><div class="stat"><b>' + b.dues + '</b><span>à réviser aujourd\\'hui</span></div></div>' +
        '<p style="font-size:13px;font-weight:800;color:var(--gray-700);margin-top:14px">Notions maîtrisées par niveau</p><div class="stats" style="margin-top:6px">' + parNiveau + '</div>' +
        ordre.map(function (t) {
          var x = themes[t];
          return '<div class="prog-theme"><h3>' + esc(t) + '<span>' + x.m + ' / ' + x.n + ' maîtrisées</span></h3><div class="prog-bar"><span class="m" style="width:' + (x.m / x.n * 100) + '%"></span><span class="c" style="width:' + (x.c / x.n * 100) + '%"></span></div></div>';
        }).join('') +
        '<div class="prog-legend"><span><i style="background:#16a34a"></i>Maîtrisées (' + MAITRISE + ' bonnes réponses)</span><span><i style="background:#fbbf24"></i>En cours</span><span><i style="background:var(--gray-100)"></i>À découvrir</span></div>' +
        '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="again">Lancer une série · ' + NIVEAUX[niveau] + '</button><button type="button" class="quiz-btn ghost" data-act="home">Changer de matière ou de niveau</button></div>' +
        '<p style="margin-top:18px"><button type="button" class="quiz-link" data-act="reset">Réinitialiser ma progression dans cette matière</button></p></div>';
      top();
    }).catch(function () { root.innerHTML = '<div class="quiz-msg">La progression n\\'a pas pu être chargée.</div>'; });
  }

  // ── Interactions ──
  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b || b.type === 'submit') return;
    if (tst && b.dataset.tk !== undefined) {
      if (tst.avance) return;
      tst.val = +b.dataset.tk; root.querySelectorAll('.quiz-choice').forEach(function (x) { x.classList.toggle('sel', x === b); });
      tst.avance = true; setTimeout(function () { tst.avance = false; testRepondre(false); }, 150);
      return;
    }
    if (tst && b.dataset.ttok !== undefined) { var tk = +b.dataset.ttok, ti = tst.val.indexOf(tk); if (ti < 0) tst.val.push(tk); else tst.val.splice(ti, 1); b.classList.toggle('sel'); return; }
    if (b.dataset.niv) { choix.niveau = b.dataset.niv; garderChoix(); root.querySelectorAll('.quiz-niveau').forEach(function (x) { x.setAttribute('aria-pressed', x === b); }); resume(); return; }
    if (b.dataset.k !== undefined && st && !st.repondu) {
      var q = st.serie[st.i], k = +b.dataset.k, btns = root.querySelectorAll('.quiz-choice');
      btns.forEach(function (x) { x.disabled = true; });
      envoyer(q.choix[k], function (d) { btns.forEach(function (x, j) { if (q.choix[j] === d.reponse) x.classList.add('good'); else if (j === k) x.classList.add('bad'); }); });
      return;
    }
    if (b.dataset.tok !== undefined && st && !st.repondu) {
      var t = +b.dataset.tok, i = st.sel.indexOf(t);
      if (i < 0) st.sel.push(t); else st.sel.splice(i, 1);
      b.classList.toggle('sel');
      root.querySelector('[data-act="valider"]').disabled = !st.sel.length;
      return;
    }
    var act = b.dataset.act;
    if (act === 'valider' && st && !st.repondu) {
      var toks = root.querySelectorAll('.tok'); toks.forEach(function (x) { x.disabled = true; }); b.disabled = true;
      envoyer(st.sel.slice().sort(function (x, y) { return x - y; }).join(','), function (d) {
        var att = d.reponse.split(',').map(Number);
        toks.forEach(function (x) { var k = +x.dataset.tok; x.classList.remove('sel'); if (att.indexOf(k) >= 0) x.classList.add('good'); else if (st.sel.indexOf(k) >= 0) x.classList.add('bad'); });
      });
    }
    else if (act === 'next') { if (st.i < st.serie.length - 1) { st.i++; question(); top(); } else fin(); }
    else if (act === 'boot') boot();
    else if (act === 'test-start') testStart();
    else if (act === 't-suivant') testRepondre(false);
    else if (act === 't-passer') testRepondre(true);
    else if (act === 'voir-resultat') { resultat(compte.positionnement); top(); }
    else if (act === 'start') demarrer(choix.mat, choix.niveau);
    else if (act === 'prog-choix') { st = null; progression(choix.mat); }
    else if (act === 'again') demarrer(st.mat, st.niveau);
    else if (act === 'prog') progression(st.mat);
    else if (act === 'home') { accueil(); top(); }
    else if (act === 'reset' && confirm('Effacer votre progression dans cette matière ?')) { var p = lire(); delete p[st.mat]; ecrire(p); progression(st.mat); }
  });
  root.addEventListener('change', function (e) {
    if (e.target.id === 'quiz-mat') { choix.mat = e.target.value; garderChoix(); resume(); }
  });
  document.addEventListener('keydown', function (e) {
    if (!tst || e.key !== 'Enter' || !document.querySelector('[data-act="t-suivant"]')) return;
    if (e.target.closest && e.target.closest('button, a') && e.target.id !== 't-num') return; // laisse Entrée activer le bouton qui a le focus
    e.preventDefault(); testRepondre(false);
  });
  root.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!st || st.repondu) return;
    var inp = root.querySelector('.quiz-num input'), v = inp.value.trim(); if (!v) return;
    inp.disabled = true; root.querySelector('.quiz-num button').disabled = true;
    envoyer(v, function (d) { inp.classList.add(d.correct ? 'good' : 'bad'); });
  });
  boot();
  // Pastille sur l'onglet Support : réponses du support pas encore lues
  SB.auth.getSession().then(function (r) {
    if (!r.data.session) return;
    SB.from('support_tickets').select('id', { count: 'exact', head: true }).eq('user_seen_reply', false).not('admin_reply', 'is', null)
      .then(function (x) { var p = document.querySelector('#tab-support .pastille'); if (p && x.count) p.hidden = false; });
  });
})();
</script>
<script>
  // Arrivée depuis l'e-mail de confirmation :
  // message de bienvenue et mise à jour de email_verified dans Klaviyo
  (function () {
    var h = new URLSearchParams(location.hash.slice(1));
    if (h.get('type') !== 'signup' || !h.get('access_token')) return;
    document.getElementById('quiz-confirm').hidden = false;
    window.dataLayer = window.dataLayer || []; window.dataLayer.push({ event: 'inscription_confirmee', parcours: 'quizcrpe' });
    fetch('/api/klaviyo/email-verified', { method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ access_token: h.get('access_token') }) }).catch(function () {});
    history.replaceState(null, '', location.pathname + location.search);
  })();
</script>
"""


def page():
    title = 'Quiz CRPE : testez vos connaissances'
    desc = "Quiz CRPE : séries de 20 questions en français, mathématiques, histoire-géographie, EMC, sciences, arts et anglais, corrigées, expliquées et rattachées au programme."
    body = f'''<main class="quiz-wrap">
  <h1>Quiz CRPE</h1>
  <p class="quiz-confirm" id="quiz-confirm" hidden>✓ Votre adresse e-mail est confirmée : bienvenue sur le Quiz CRPE !</p>
  <p class="quiz-lead">Lancez des séries de {TAILLE_SERIE} questions rattachées au programme du concours, par matière et par niveau. Chaque notion est posée sous plusieurs formes : avec {BONNES_POUR_MAITRISER} bonnes réponses, elle est maîtrisée. En cas d'erreur, vous voyez l'explication et une question similaire revient plus tard.</p>
  <div id="quiz-app"></div>
</main>
'''
    head = (HEAD_START
            + f'  <title>{title} | PassCRPE</title>\n'
            + f'  <meta name="description" content="{desc}" />\n'
            + '  <meta name="robots" content="noindex, nofollow" />\n'
            + f'  <link rel="canonical" href="{SITE}/quizapp" />\n'
            + CSS_BASE + CSS + nav_compte.CSS)
    js = (JS.replace('__MATIERES__', json.dumps(MATIERES, ensure_ascii=False))
            .replace('__PRIX__', PRIX)
            .replace('__SERIE__', str(TAILLE_SERIE)).replace('__MAITRISE__', str(BONNES_POUR_MAITRISER))
            .replace('__INTERVALLES__', json.dumps(INTERVALLES_JOURS)).replace('__APRES_ERREUR__', str(APRES_ERREUR_JOURS)))
    return head + BODY_NAV + body + TABBAR + nav_compte.JS + js + TAIL


open(os.path.join(ROOT, 'landing', 'quizapp.html'), 'w', encoding='utf-8').write(page())
print('landing/quizapp.html')

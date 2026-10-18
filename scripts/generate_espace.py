#!/usr/bin/env python3
"""Génère la page « Mes outils » : /espace.

Un seul compte PassCRPE (projet Supabase « crpe ») donne accès aux deux outils. Après la connexion, la personne
choisit ici le tuteur IA (/app) ou le Quiz CRPE (/quizapp), avec l'état de chacun (essai, accès débloqué, test à passer…).
Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Données : /api/espace (app.js)
Sortie  : landing/espace.html
Usage   : python3 scripts/generate_espace.py
"""
import os

import nav_compte

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'

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

CSS = """
    /* MES OUTILS */
    .esp-wrap { max-width: 900px; margin: 0 auto; padding: 36px 20px 80px; color: var(--gray-700); }
    .esp-wrap h1 { font-size: clamp(28px, 4.5vw, 38px); font-weight: 900; color: var(--gray-900); letter-spacing: -.5px; margin-bottom: 8px; }
    .esp-lead { font-size: 16px; line-height: 1.6; margin-bottom: 28px; }
    .esp-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .esp-card { display: flex; flex-direction: column; border-radius: 22px; padding: 26px 24px; border: 1.5px solid var(--gray-200); background: #fff; }
    .esp-card.tuteur { background: linear-gradient(160deg, #eef2ff, #fff 55%); border-color: #c7d2fe; }
    .esp-card.quiz { background: linear-gradient(160deg, #fff7ed, #fff 55%); border-color: #fed7aa; }
    .esp-head { display: flex; gap: 14px; align-items: center; margin-bottom: 12px; }
    .esp-icon { width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
    .tuteur .esp-icon { background: #4f46e5; } .quiz .esp-icon { background: #f97316; }
    .esp-card h2 { font-size: 21px; font-weight: 900; color: var(--gray-900); }
    .esp-card p { font-size: 14.5px; line-height: 1.6; margin-bottom: 14px; }
    .esp-etat { align-self: flex-start; min-height: 26px; background: var(--gray-100); color: var(--gray-500); font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 100px; margin-bottom: 16px; }
    .esp-etat.ok { background: #dcfce7; color: #166534; } .esp-etat.essai { background: #e0e7ff; color: #3730a3; } .esp-etat.todo { background: #ffedd5; color: #9a3412; }
    .esp-btn { margin-top: auto; display: inline-flex; justify-content: center; padding: 13px 20px; border-radius: 12px; font-size: 15px; font-weight: 800; text-decoration: none; color: #fff; }
    .tuteur .esp-btn { background: #4f46e5; } .tuteur .esp-btn:hover { background: #4338ca; }
    .quiz .esp-btn { background: #f97316; } .quiz .esp-btn:hover { background: #ea580c; }
    .esp-compte { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; font-size: 13px; color: var(--gray-500); margin-top: 22px; }
    .esp-link { background: none; border: 0; font: inherit; font-size: 13px; color: var(--gray-500); text-decoration: underline; cursor: pointer; padding: 0; }
    .esp-msg { padding: 18px; border-radius: 16px; background: #fff; border: 1.5px solid var(--gray-200); font-size: 15px; line-height: 1.6; }
    .esp-msg a { color: #4f46e5; font-weight: 700; }
    @media (max-width: 720px) { .esp-grid { grid-template-columns: 1fr; } }
"""

JS = """<script>
(function () {
  var SB = window.passcrpeSB;
  var root = document.getElementById('espace');
  function esc(v) { return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function connexion() {
    root.innerHTML = '<div class="esp-msg">Connectez-vous à votre compte PassCRPE pour accéder à vos outils.<br><a href="/?auth=login">Se connecter</a> · <a href="/?auth=register">Créer un compte</a></div>';
  }
  var CLE = 'passcrpe-espace';
  // Les deux cartes s'affichent tout de suite ; l'état de chaque outil arrive ensuite (dernier état connu d'abord)
  function afficher(d) {
    var t = d && d.tuteur, q = d && d.quiz, attente = '<span class="esp-etat">…</span>';
    var etatT = !t ? attente : t.paid ? '<span class="esp-etat ok">Accès complet</span>' : '<span class="esp-etat essai">Essai gratuit</span>';
    var etatQ = !q ? attente : q.paid ? '<span class="esp-etat ok">Accès débloqué</span>'
      : q.positionnement ? '<span class="esp-etat todo">Test fait' + (q.score != null ? ' : ' + q.score + ' %' : '') + ' · à débloquer</span>'
      : '<span class="esp-etat todo">Test de positionnement gratuit à passer</span>';
    root.innerHTML = '<div class="esp-grid">' +
      '<div class="esp-card tuteur"><div class="esp-head"><div class="esp-icon">🤖</div><h2>Tuteur IA</h2></div>' + etatT +
      '<p>Des exercices en mathématiques et en français adaptés à votre niveau, corrigés selon les exigences du CRPE.</p>' +
      '<a class="esp-btn" href="/app">Ouvrir le tuteur IA →</a></div>' +
      '<div class="esp-card quiz"><div class="esp-head"><div class="esp-icon">🎯</div><h2>Quiz CRPE</h2></div>' + etatQ +
      '<p>3 232 questions dans les 9 matières du concours, en séries de 20, avec révisions espacées.</p>' +
      '<a class="esp-btn" href="/quizapp">' + (!q || q.paid ? 'Ouvrir le quiz →' : q.positionnement ? 'Voir mon résultat →' : 'Passer mon test gratuit →') + '</a></div>' +
      '</div>';
    var p = document.getElementById('esp-prenom'); if (p && d && d.prenom) p.textContent = 'Bonjour ' + d.prenom + ' !';
  }
  function lireCache(email) { try { var c = JSON.parse(localStorage.getItem(CLE)); return c && c.email === email ? c : null; } catch (e) { return null; } }
  SB.auth.getSession().then(function (r) {
    var s = r.data.session; if (!s) return connexion();
    var m = s.user.user_metadata || {};
    afficher(lireCache(s.user.email) || { prenom: m.prenom });
    return fetch('/api/espace', { headers: { Authorization: 'Bearer ' + s.access_token } }).then(function (res) {
      if (res.status === 401) return connexion();
      return res.json().then(function (d) {
        if (!res.ok) throw new Error(d.error);
        afficher(d); try { localStorage.setItem(CLE, JSON.stringify(d)); } catch (e) {}
      });
    });
  }).catch(function () { if (!document.querySelector('.esp-grid')) root.innerHTML = '<div class="esp-msg">Votre espace n\\'a pas pu être chargé. Rechargez la page.</div>'; });
})();
</script>
"""


def page():
    head = (HEAD_START
            + '  <title>Mes outils | PassCRPE</title>\n'
            + '  <meta name="description" content="Votre espace PassCRPE : le tuteur IA et le Quiz CRPE avec un seul compte." />\n'
            + '  <meta name="robots" content="noindex, nofollow" />\n'
            + f'  <link rel="canonical" href="{SITE}/espace" />\n'
            + CSS_BASE + CSS + nav_compte.CSS)
    body = '''<main class="esp-wrap">
  <h1 id="esp-prenom">Mes outils</h1>
  <p class="esp-lead">Un seul compte PassCRPE pour vos deux outils de préparation : choisissez celui que vous voulez utiliser.</p>
  <div id="espace"><div class="esp-msg">Chargement…</div></div>
</main>
'''
    js = nav_compte.JS + JS
    return head + BODY_NAV + body + js + TAIL


open(os.path.join(ROOT, 'landing', 'espace.html'), 'w', encoding='utf-8').write(page())
print('landing/espace.html')

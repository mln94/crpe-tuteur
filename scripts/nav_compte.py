"""Menu du compte dans l'en-tête (pages /espace et /quizapp).

Connecté : « Se connecter » et « Commencer » sont remplacés par le nom du profil, avec un menu déroulant
(Mes outils, Tuteur IA, Quiz CRPE, Se déconnecter).
Une page peut ajouter ses propres liens au menu avec window.passcrpeMenuExtra (HTML), défini avant ce script. Non connecté : l'en-tête reste celui du site.
Le client Supabase (projet « crpe ») est partagé avec la page : window.passcrpeSB.
"""

import re


SUPPORT_ICONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>'


def nav_application(nav, support_href):
    """En-tête des applications (tuteur IA, quiz) : logo, bouton Support et menu du compte, sans le menu du site."""
    nav = re.sub(r'\s*<ul class="nav-links">.*?</ul>', '', nav, flags=re.S)
    nav = re.sub(r'\s*<button[^>]*class="nav-login"[^>]*>.*?</button>', '', nav, flags=re.S)
    nav = re.sub(r'\s*<button[^>]*class="nav-cta[^"]*"[^>]*>.*?</button>', '', nav, flags=re.S)
    nav = re.sub(r'\s*<a[^>]*class="nav-(login|cta)[^"]*"[^>]*>.*?</a>', '', nav, flags=re.S)
    nav = re.sub(r'\s*<button type="button" class="nav-burger".*?</button>', '', nav, flags=re.S)
    nav = nav.replace('<nav class="site-nav">', '<nav class="site-nav nav-app">')
    if support_href:  # sans lien : pas de bouton Support dans l'en-tête (le quiz a son onglet Support)
        nav = nav.replace('<div class="nav-actions">', f'<div class="nav-actions">\n      <a class="nav-support" href="{support_href}">{SUPPORT_ICONE}<span class="lib">Support</span></a>', 1)
    return nav


SB_URL = 'https://zqwcermgfvcusuwjfviz.supabase.co'
SB_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inpxd2Nlcm1nZnZjdXN1d2pmdml6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMxNzkzMDYsImV4cCI6MjA4ODc1NTMwNn0.2QjrNafsARpnIA605-hh3jZWjMxZoyQzGTC3LL99Wr8'

CSS = """
    /* MENU DU COMPTE */
    .nav-compte { position: relative; }
    .nav-compte-btn { display: inline-flex; align-items: center; gap: 8px; padding: 5px 10px 5px 5px; border-radius: 100px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 13.5px; font-weight: 700; color: var(--gray-800); cursor: pointer; max-width: 240px; }
    .nav-compte-btn:hover { border-color: var(--indigo-600); }
    .nav-compte-btn .av { width: 28px; height: 28px; border-radius: 50%; background: var(--indigo-600); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 800; flex-shrink: 0; }
    .nav-compte-btn .nom { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .nav-compte-btn svg { width: 14px; height: 14px; flex-shrink: 0; }
    .nav-compte-menu { display: none; position: absolute; right: 0; top: calc(100% + 8px); min-width: 220px; background: #fff; border: 1px solid var(--gray-200); border-radius: 14px; box-shadow: 0 12px 32px rgba(0,0,0,.10); padding: 6px; z-index: 300; }
    .nav-compte.open .nav-compte-menu { display: block; }
    .nav-compte-menu .mail { font-size: 12px; color: var(--gray-500); padding: 8px 12px 6px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .nav-compte-menu a, .nav-compte-menu button { display: flex; align-items: center; gap: 10px; width: 100%; text-align: left; padding: 10px 12px; border-radius: 10px; border: 0; background: none; font: inherit; font-size: 14px; font-weight: 600; color: var(--gray-800); text-decoration: none; cursor: pointer; }
    .nav-compte-menu a:hover, .nav-compte-menu button:hover { background: var(--gray-50); }
    .nav-compte-menu hr { border: 0; border-top: 1px solid var(--gray-100); margin: 6px 4px; }
    .nav-compte-menu .out { color: #b91c1c; }
    .site-nav.connecte .nav-actions > .nav-login, .site-nav.connecte .nav-actions > .nav-cta { display: none !important; }
    .site-nav.connecte .nav-links li.nav-menu-account { display: none !important; }
    @media (max-width: 600px) { .nav-compte-btn .nom { max-width: 110px; } }
    /* En-tête des applications : bouton Support à côté du nom */
    .nav-app .nav-actions { gap: 10px; }
    .nav-support { display: inline-flex; align-items: center; gap: 6px; padding: 7px 12px; border-radius: 100px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 13.5px; font-weight: 700; color: var(--gray-700); text-decoration: none; cursor: pointer; }
    .nav-support:hover { border-color: var(--indigo-600); color: var(--indigo-600); }
    .nav-support svg { width: 16px; height: 16px; }
    @media (max-width: 480px) { .nav-support .lib { display: none; } }
"""

JS = """<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.js"></script>
<script>
  // Menu du compte dans l'en-tête : nom du profil et accès aux deux outils
  window.passcrpeSB = window.passcrpeSB || window.supabase.createClient('__SB_URL__', '__SB_KEY__');
  (function () {
    var nav = document.querySelector('.site-nav'), actions = nav && nav.querySelector('.nav-actions');
    if (!actions) return;
    function esc(v) { return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
    function afficher(user) {
      var old = actions.querySelector('.nav-compte'); if (old) old.remove();
      if (!user) { nav.classList.remove('connecte'); return; }
      var m = user.user_metadata || {}, nom = ((m.prenom || '') + ' ' + (m.nom || '')).trim() || user.email;
      var el = document.createElement('div'); el.className = 'nav-compte';
      el.innerHTML = '<button type="button" class="nav-compte-btn" aria-haspopup="true" aria-expanded="false"><span class="av">' + esc((nom[0] || '?').toUpperCase()) + '</span><span class="nom">' + esc(nom) +
        '</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>' +
        '<div class="nav-compte-menu" role="menu"><div class="mail">' + esc(user.email) + '</div>' +
        '<a href="/espace" role="menuitem">🏠 Mes outils</a><a href="/app" role="menuitem">🤖 Tuteur IA</a><a href="/quizapp" role="menuitem">🎯 Quiz CRPE</a>' +
        (window.passcrpeMenuExtra || '') + '<hr>' +
        '<button type="button" class="out" role="menuitem">Se déconnecter</button></div>';
      actions.insertBefore(el, actions.querySelector('.nav-burger'));
      nav.classList.add('connecte');
      var btn = el.querySelector('.nav-compte-btn');
      btn.addEventListener('click', function (e) { e.stopPropagation(); var o = el.classList.toggle('open'); btn.setAttribute('aria-expanded', o); });
      el.querySelector('.out').addEventListener('click', function () { window.passcrpeSB.auth.signOut().then(function () { window.location.href = '/'; }); });
    }
    document.addEventListener('click', function (e) { var c = actions.querySelector('.nav-compte.open'); if (c && !c.contains(e.target)) { c.classList.remove('open'); c.querySelector('.nav-compte-btn').setAttribute('aria-expanded', 'false'); } });
    window.passcrpeSB.auth.getSession().then(function (r) { afficher(r.data.session && r.data.session.user); });
    window.passcrpeSB.auth.onAuthStateChange(function (ev, s) { afficher(s && s.user); });
  })();
</script>
""".replace('__SB_URL__', SB_URL).replace('__SB_KEY__', SB_KEY)

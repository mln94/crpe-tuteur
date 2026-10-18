#!/usr/bin/env python3
"""Génère la page de contact : /contact.

Le formulaire (prénom, e-mail, raison du contact, message) crée un ticket dans le support (table support_tickets),
traité dans /admin-support : la raison y apparaît comme catégorie. ?raison=paiement présélectionne « Problème de
paiement » (lien depuis le paiement du quiz). Connecté, l'e-mail et le prénom sont préremplis et la réponse apparaît
aussi dans l'onglet Support du tuteur IA.
Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html ; API : /api/contact (app.js)
Sortie  : landing/contact.html
Usage   : python3 scripts/generate_contact.py
"""
import json
import os

import nav_compte

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'

# Doit rester aligné avec CONTACT_RAISONS (app.js) ; la clé sert dans l'adresse (?raison=…)
RAISONS = [
    ('paiement', 'Problème de paiement'),
    ('quiz', 'Question sur le Quiz CRPE'),
    ('tuteur', 'Question sur le Tuteur IA'),
    ('technique', 'Problème technique'),
    ('compte', 'Question sur mon compte'),
    ('remboursement', 'Demande de remboursement'),
    ('suggestion', "Suggestion d'amélioration"),
    ('partenariat', 'Partenariat ou presse'),
    ('autre', 'Autre'),
]

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
    /* CONTACT */
    .ct-wrap { max-width: 680px; margin: 0 auto; padding: 36px 20px 80px; color: var(--gray-700); }
    .ct-wrap h1 { font-size: clamp(28px, 4.5vw, 38px); font-weight: 900; color: var(--gray-900); letter-spacing: -.5px; margin-bottom: 8px; }
    .ct-lead { font-size: 16px; line-height: 1.6; margin-bottom: 24px; }
    .ct-card { background: #fff; border: 1.5px solid var(--gray-200); border-radius: 20px; padding: 26px; box-shadow: 0 8px 30px rgba(0,0,0,.04); }
    .ct-form { display: grid; gap: 16px; }
    .ct-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
    .ct-field label { display: block; font-size: 13px; font-weight: 700; color: var(--gray-700); margin-bottom: 6px; }
    .ct-field input, .ct-field select, .ct-field textarea { width: 100%; padding: 12px 14px; font: inherit; font-size: 15px; color: var(--gray-900); border: 1.5px solid var(--gray-200); border-radius: 12px; background: #fff; }
    .ct-field textarea { min-height: 160px; resize: vertical; line-height: 1.55; }
    .ct-field input:focus, .ct-field select:focus, .ct-field textarea:focus { outline: none; border-color: var(--indigo-600); box-shadow: 0 0 0 3px rgba(99,102,241,.12); }
    .ct-piege { position: absolute; left: -9999px; width: 1px; height: 1px; overflow: hidden; }
    .ct-btn { padding: 14px 22px; border-radius: 12px; border: 0; font: inherit; font-size: 15px; font-weight: 800; color: #fff; background: var(--indigo-600); cursor: pointer; }
    .ct-btn:hover { background: var(--indigo-700); }
    .ct-btn:disabled { background: #a5b4fc; cursor: not-allowed; }
    .ct-msg { font-size: 14px; line-height: 1.55; border-radius: 12px; padding: 12px 14px; }
    .ct-msg.ok { background: #dcfce7; color: #166534; } .ct-msg.ko { background: #fee2e2; color: #991b1b; }
    .ct-aide { font-size: 13px; color: var(--gray-500); line-height: 1.55; margin-top: 18px; }
    @media (max-width: 600px) { .ct-row { grid-template-columns: 1fr; } .ct-card { padding: 20px 16px; } }
"""

OPTIONS = ''.join(f'<option value="{label}" data-cle="{cle}">{label}</option>' for cle, label in RAISONS)

BODY = f'''<main class="ct-wrap">
  <h1>Contactez-nous</h1>
  <p class="ct-lead">Une question, un problème de paiement ou une suggestion ? Écrivez-nous : nous vous répondons par e-mail dans les meilleurs délais.</p>
  <div class="ct-card">
    <form class="ct-form" id="ct-form" novalidate>
      <div class="ct-row">
        <div class="ct-field"><label for="ct-prenom">Prénom</label><input id="ct-prenom" type="text" autocomplete="given-name" maxlength="80" placeholder="Marie"></div>
        <div class="ct-field"><label for="ct-email">Adresse e-mail</label><input id="ct-email" type="email" autocomplete="email" required placeholder="vous@exemple.fr"></div>
      </div>
      <div class="ct-field"><label for="ct-raison">Raison du contact</label>
        <select id="ct-raison" required><option value="">Choisir une raison…</option>{OPTIONS}</select></div>
      <div class="ct-field"><label for="ct-message">Votre message</label>
        <textarea id="ct-message" required maxlength="5000" placeholder="Décrivez votre demande. Pour un problème de paiement, indiquez la date et le moyen de paiement utilisé."></textarea></div>
      <div class="ct-piege" aria-hidden="true"><label for="ct-site">Site</label><input id="ct-site" type="text" tabindex="-1" autocomplete="off"></div>
      <div id="ct-retour" class="ct-msg" hidden></div>
      <button type="submit" class="ct-btn" id="ct-envoyer">Envoyer mon message</button>
    </form>
  </div>
  <p class="ct-aide">Vos données servent uniquement à traiter votre demande (<a href="/politique-de-confidentialite" target="_blank" rel="noopener">politique de confidentialité</a>).</p>
</main>
'''

JS = """<script>
(function () {
  var f = document.getElementById('ct-form'), sel = document.getElementById('ct-raison'), retour = document.getElementById('ct-retour'), btn = document.getElementById('ct-envoyer');
  // ?raison=paiement : raison présélectionnée (lien « Un problème avec le paiement ? » du quiz)
  var cle = new URLSearchParams(location.search).get('raison');
  if (cle) for (var i = 0; i < sel.options.length; i++) if (sel.options[i].dataset.cle === cle) sel.selectedIndex = i;
  var jeton = null;
  // Connecté : e-mail et prénom préremplis ; le ticket est rattaché au compte
  window.passcrpeSB.auth.getSession().then(function (r) {
    var s = r.data.session; if (!s) return;
    jeton = s.access_token;
    var m = s.user.user_metadata || {}, em = document.getElementById('ct-email'), pr = document.getElementById('ct-prenom');
    if (!em.value) em.value = s.user.email || ''; if (!pr.value) pr.value = m.prenom || '';
  });
  function montrer(t, ok) { retour.hidden = false; retour.className = 'ct-msg ' + (ok ? 'ok' : 'ko'); retour.textContent = t; }
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = { prenom: document.getElementById('ct-prenom').value.trim(), email: document.getElementById('ct-email').value.trim(),
      raison: sel.value, message: document.getElementById('ct-message').value.trim(), site: document.getElementById('ct-site').value };
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(d.email)) return montrer('Indiquez une adresse e-mail valide.');
    if (!d.raison) return montrer('Choisissez la raison de votre contact.');
    if (d.message.length < 10) return montrer('Votre message est un peu court : précisez votre demande.');
    btn.disabled = true; btn.textContent = 'Envoi…';
    var h = { 'Content-Type': 'application/json' }; if (jeton) h.Authorization = 'Bearer ' + jeton;
    fetch('/api/contact', { method: 'POST', headers: h, body: JSON.stringify(d) }).then(function (r) {
      return r.json().then(function (x) { if (!r.ok) throw new Error(x.error); });
    }).then(function () {
      f.querySelectorAll('input, select, textarea, button').forEach(function (x) { x.disabled = true; });
      montrer('✓ Message envoyé. Nous vous répondons par e-mail à ' + d.email + ' dans les meilleurs délais.', true);
      btn.textContent = 'Message envoyé';
    }).catch(function (err) { btn.disabled = false; btn.textContent = 'Envoyer mon message'; montrer(err.message || "Votre message n'a pas pu être envoyé. Réessayez."); });
  });
})();
</script>
"""


def page():
    head = (HEAD_START
            + '  <title>Contact | PassCRPE</title>\n'
            + '  <meta name="description" content="Contactez l\'équipe PassCRPE : question sur le Quiz CRPE ou le tuteur IA, problème de paiement, suggestion." />\n'
            + f'  <link rel="canonical" href="{SITE}/contact" />\n'
            + CSS_BASE + CSS + nav_compte.CSS)
    return head + BODY_NAV + BODY + nav_compte.JS + JS + TAIL


open(os.path.join(ROOT, 'landing', 'contact.html'), 'w', encoding='utf-8').write(page())
print('landing/contact.html')

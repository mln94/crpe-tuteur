#!/usr/bin/env python3
"""Génère les pages « Outils » : /outils, /outils/entraineur-crpe et /politique-de-confidentialite.

Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Sorties : landing/outils.html, landing/entraineur-crpe.html, landing/politique-de-confidentialite.html
Usage   : python3 scripts/generate_outils.py
"""
import json
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'

# Réglages affichés dans les textes (les vraies limites sont dans entraineur/routes.js)
QUESTIONS_PER_SET = 5
WEEKLY_REPORT_LIMIT = 1

# ── Gabarit commun ───────────────────────────────────────────────────────────
tpl = open(TEMPLATE, encoding='utf-8').read()
HEAD_START = tpl[:tpl.index('  <title>')]
css_start = tpl.index('  <link rel="preconnect"')
css_end = tpl.index('  </style>', css_start)
CSS_BASE = tpl[css_start:css_end]
BODY_START = tpl[css_end:tpl.index('<div class="article-wrap">')]
TAIL = tpl[tpl.index('<footer>'):]

# Menu : « Ressources » actif, le blog ne l'est plus
NAV_RES = '<button type="button" class="nav-dropdown-toggle" '
NAV_BLOG = '<li><a href="/blog" class="active">Blog</a></li>'
assert BODY_START.count(NAV_RES) == 1 and BODY_START.count(NAV_BLOG) == 1
BODY_NAV_RES = (BODY_START.replace(NAV_RES, '<button type="button" class="nav-dropdown-toggle active" ')
                .replace(NAV_BLOG, '<li><a href="/blog">Blog</a></li>'))
BODY_NAV_NONE = BODY_START.replace(NAV_BLOG, '<li><a href="/blog">Blog</a></li>')

CSS = """
    /* OUTILS */
    .page-wrap { max-width: 860px; margin: 0 auto; padding: 32px 20px 72px; font-size: 16px; line-height: 1.7; color: var(--gray-700); }
    .page-wrap h1 { font-size: clamp(28px, 4.5vw, 40px); font-weight: 900; color: var(--gray-900); line-height: 1.15; letter-spacing: -.5px; margin-bottom: 14px; }
    .page-wrap h2 { font-size: 23px; font-weight: 800; color: var(--gray-900); margin: 44px 0 12px; letter-spacing: -.2px; }
    .page-wrap h3 { font-size: 17px; font-weight: 800; color: var(--gray-900); margin: 22px 0 8px; }
    .page-wrap p { margin-bottom: 14px; }
    .page-wrap ul, .page-wrap ol { margin: 0 0 16px 22px; }
    .page-wrap li { margin-bottom: 6px; }
    .page-wrap strong { color: var(--gray-900); }
    .page-wrap a { color: var(--indigo-600); }
    .lead { font-size: 17px; }
    .breadcrumb { position: static; z-index: auto; background: none; backdrop-filter: none; -webkit-backdrop-filter: none; border: 0; display: flex; flex-wrap: wrap; gap: 8px; font-size: 13px; color: var(--gray-400); margin-bottom: 20px; }
    .breadcrumb a { color: var(--gray-500); text-decoration: none; font-weight: 600; }
    .breadcrumb a:hover { color: var(--indigo-600); }
    .breadcrumb [aria-current] { color: var(--gray-700); font-weight: 600; }

    .tool-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; margin-top: 24px; }
    .tool-card { display: flex; flex-direction: column; gap: 10px; padding: 22px; border: 1px solid var(--gray-200); border-radius: 16px; background: #fff; box-shadow: 0 1px 3px rgba(15,23,42,.04); }
    .tool-card-icon { width: 44px; height: 44px; border-radius: 12px; background: var(--indigo-50); color: var(--indigo-600); display: flex; align-items: center; justify-content: center; }
    .tool-card-icon svg { width: 22px; height: 22px; }
    .tool-card h2 { font-size: 19px; margin: 0; }
    .tool-card p { margin: 0; font-size: 15px; color: var(--gray-500); flex: 1; }
    .tool-badge { align-self: flex-start; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .05em; color: #065f46; background: #d1fae5; padding: 3px 9px; border-radius: 20px; }

    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 20px; border-radius: 12px; border: 0; font-family: inherit; font-size: 15px; font-weight: 700; cursor: pointer; text-decoration: none; transition: background .15s, border-color .15s, color .15s; }
    .btn-primary { background: var(--indigo-600); color: #fff !important; }
    .btn-primary:hover { background: var(--indigo-700); }
    .btn-primary:disabled { opacity: .5; cursor: not-allowed; }
    .btn-ghost { background: #fff; color: var(--gray-700) !important; border: 1.5px solid var(--gray-200); }
    .btn-ghost:hover { border-color: var(--indigo-600); color: var(--indigo-600) !important; }
    .btn-ghost:disabled { opacity: .5; cursor: not-allowed; }
    :focus-visible { outline: 3px solid var(--indigo-600); outline-offset: 2px; }

    /* Outil */
    .tool { margin-top: 24px; border: 1px solid var(--gray-200); border-radius: 18px; background: #fff; box-shadow: 0 4px 24px rgba(15,23,42,.06); overflow: hidden; }
    .tool-counter { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 18px; background: var(--indigo-50); border-bottom: 1px solid var(--indigo-100); font-size: 14px; color: var(--indigo-700); font-weight: 600; }
    .tool-counter button { background: none; border: 0; padding: 0; font: inherit; color: var(--indigo-700); text-decoration: underline; cursor: pointer; }
    .tool-body { padding: 22px 18px 24px; }
    .tool-body > * + * { margin-top: 16px; }
    .subject-choice { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
    .subject-btn { display: flex; flex-direction: column; align-items: flex-start; gap: 4px; padding: 18px; border: 2px solid var(--gray-200); border-radius: 14px; background: #fff; font-family: inherit; text-align: left; cursor: pointer; transition: border-color .15s, background .15s; }
    .subject-btn:hover { border-color: var(--indigo-600); background: var(--indigo-50); }
    .subject-btn strong { font-size: 17px; }
    .subject-btn span { font-size: 13px; color: var(--gray-500); line-height: 1.4; }
    @media (max-width: 480px) { .subject-choice { grid-template-columns: 1fr; } }
    .badges { display: flex; flex-wrap: wrap; gap: 6px; }
    .badge { font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; background: var(--gray-100); color: var(--gray-700); }
    .badge-subject { background: var(--indigo-600); color: #fff; }
    .question-box { padding: 16px; border-radius: 14px; background: var(--gray-50, #f9fafb); border: 1px solid var(--gray-100); }
    .question-box .label { display: block; font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--gray-400); margin-bottom: 4px; }
    .question-box p { margin: 0 0 12px; white-space: normal; }
    .question-box p:last-child { margin-bottom: 0; }
    .question-box .q { font-weight: 700; color: var(--gray-900); }
    .support { border-left: 3px solid var(--indigo-200, #c7d2fe); padding-left: 12px; font-style: italic; }
    .figure { margin: 4px 0 12px; }
    .figure img { display: block; max-width: 100%; height: auto; background: #fff; border-radius: 8px; }
    .answer label { display: block; font-weight: 700; color: var(--gray-900); margin-bottom: 6px; }
    .answer textarea { width: 100%; min-height: 170px; padding: 12px 14px; border: 1.5px solid var(--gray-200); border-radius: 12px; font-family: inherit; font-size: 15px; line-height: 1.6; resize: vertical; }
    .answer textarea:focus { outline: none; border-color: var(--indigo-600); }
    .answer-meta { display: flex; justify-content: space-between; gap: 8px; font-size: 12px; color: var(--gray-500); margin-top: 4px; }
    .answer-meta .over { color: #b91c1c; font-weight: 700; }
    .actions { display: flex; flex-wrap: wrap; gap: 10px; }
    .notice { padding: 14px 16px; border-radius: 12px; font-size: 15px; }
    .notice-error { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }
    .notice-info { background: var(--indigo-50); color: var(--indigo-700); border: 1px solid var(--indigo-100); }
    .loading { display: flex; align-items: center; gap: 10px; color: var(--gray-500); font-weight: 600; }
    .spinner { width: 18px; height: 18px; border: 3px solid var(--indigo-100); border-top-color: var(--indigo-600); border-radius: 50%; animation: spin .8s linear infinite; }
    @keyframes spin { to { transform: rotate(360deg); } }

    .report { border: 1px solid var(--gray-200); border-radius: 14px; overflow: hidden; }
    .report > summary { list-style: none; cursor: pointer; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding: 12px 16px; background: var(--gray-50, #f9fafb); font-weight: 700; color: var(--gray-900); }
    .report > summary::-webkit-details-marker { display: none; }
    .report-body { padding: 14px 16px 6px; font-size: 15px; }
    .report-body h4 { font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: .04em; color: var(--gray-500); margin: 14px 0 6px; }
    .report-body h4:first-child { margin-top: 0; }
    .report-body ul { margin: 0 0 8px 18px; }
    .report-body blockquote { margin: 0 0 4px; padding: 2px 10px; border-left: 3px solid var(--gray-200); color: var(--gray-500); font-style: italic; }
    .level { font-size: 12px; font-weight: 800; padding: 3px 10px; border-radius: 20px; }
    .level-a_retravailler { background: #fee2e2; color: #991b1b; }
    .level-en_bonne_voie { background: #fef3c7; color: #92400e; }
    .level-attendu_atteint { background: #d1fae5; color: #065f46; }
    .note20 { font-size: 15px; font-weight: 900; color: var(--gray-900); }
    .tip { background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 10px; padding: 10px 12px; margin: 6px 0 10px; }
    .progress-note { background: var(--indigo-50); border-radius: 10px; padding: 10px 12px; margin-bottom: 10px; }
    .corrige { border: 2px solid #a7f3d0; background: #f0fdf4; border-radius: 14px; padding: 16px; }
    .corrige h3 { margin-top: 0; color: #065f46; }

    .lead-form { border: 1px solid var(--indigo-100); border-radius: 14px; padding: 18px; background: #fff; }
    .lead-form h3 { margin-top: 0; }
    .field { margin-bottom: 12px; }
    .field label { display: block; font-size: 14px; font-weight: 700; color: var(--gray-900); margin-bottom: 4px; }
    .field input { width: 100%; padding: 11px 12px; border: 1.5px solid var(--gray-200); border-radius: 10px; font-family: inherit; font-size: 15px; }
    .field input:focus { outline: none; border-color: var(--indigo-600); }
    .field-hint { display: block; font-size: 12px; color: var(--gray-500); margin-top: 3px; line-height: 1.45; }
    .field-row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
    @media (max-width: 480px) { .field-row { grid-template-columns: 1fr; } }
    .check { display: flex; gap: 10px; align-items: flex-start; font-size: 14px; margin-bottom: 8px; line-height: 1.45; cursor: pointer; }
    .check input { margin-top: 3px; width: 16px; height: 16px; accent-color: var(--indigo-600); flex-shrink: 0; }
    .legal { font-size: 12px; color: var(--gray-500); line-height: 1.55; margin-top: 10px; }

    .steps-list { counter-reset: s; list-style: none; margin-left: 0 !important; }
    .steps-list li { counter-increment: s; position: relative; padding-left: 40px; margin-bottom: 12px; }
    .steps-list li::before { content: counter(s); position: absolute; left: 0; top: 0; width: 28px; height: 28px; border-radius: 50%; background: var(--indigo-600); color: #fff; font-size: 14px; font-weight: 800; display: flex; align-items: center; justify-content: center; }
    .faq details { border-bottom: 1px solid var(--gray-200); padding: 12px 0; }
    .faq summary { cursor: pointer; font-weight: 700; color: var(--gray-900); }
    .faq details p { margin: 8px 0 0; }
    .placeholder { background: #fef3c7; padding: 0 4px; border-radius: 4px; }

    /* Parcours en 5 questions */
    .progress { height: 6px; border-radius: 6px; background: var(--gray-100); overflow: hidden; }
    .progress-bar { height: 100%; background: var(--indigo-600); border-radius: 6px; transition: width .3s; }
    .step-label { font-size: 13px; font-weight: 700; color: var(--gray-500); margin: 0; }
    .sent { text-align: center; padding: 16px 4px; }
    .sent-icon { width: 56px; height: 56px; margin: 0 auto 12px; border-radius: 50%; background: #d1fae5; color: #065f46; font-size: 28px; font-weight: 900; display: flex; align-items: center; justify-content: center; }
    .sent h3 { margin-top: 0; }

    /* Page du rapport */
    .report-kicker { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: .05em; color: var(--indigo-600); margin-bottom: 6px; }
    .report-score { display: flex; flex-wrap: wrap; align-items: center; gap: 16px; padding: 16px 18px; border: 1px solid var(--gray-200); border-radius: 14px; margin: 16px 0; }
    .score-big { display: block; font-size: 34px; font-weight: 900; color: var(--gray-900); line-height: 1; }
    .score-sub { font-size: 13px; color: var(--gray-500); }
    .report-q { border-top: 1px solid var(--gray-200); padding-top: 18px; margin-top: 24px; }
    .report-q > * + * { margin-top: 12px; }
    .report-q-head { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; }
    .report-q-head h3 { margin: 0; }
    .report-block h4, .corrige h4 { font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: .04em; color: var(--gray-500); margin: 12px 0 6px; }
    .report-block ul { margin: 0 0 8px 18px; }
    .report-block blockquote { margin: 0 0 4px; padding: 2px 10px; border-left: 3px solid var(--gray-200); color: var(--gray-500); font-style: italic; }
    .your-answer { padding: 12px 14px; background: #fff; border: 1px dashed var(--gray-300, #d1d5db); border-radius: 10px; }
    .corrige h4:first-child { margin-top: 0; color: #065f46; }
    .report-cta { margin-top: 32px; padding: 22px; border-radius: 16px; background: var(--indigo-50); text-align: center; }
    .report-cta h2 { margin-top: 0; }
    @media print {
      .site-nav, footer, .no-print, .breadcrumb, .auth-overlay, #authOverlay { display: none !important; }
      .page-wrap { padding: 0; max-width: none; }
      .report-q { break-inside: avoid-page; }
    }
"""


def page(title, description, canonical, body, og_title, ld, active_ressources=True, robots=None):
    lds = ''.join(f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    return (HEAD_START
        + f'''  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}" />
{f'  <meta name="robots" content="{robots}" />' + chr(10) if robots else ''}  <link rel="canonical" href="{SITE}{canonical}" />
  <meta property="og:title" content="{escape(og_title)}" />
  <meta property="og:description" content="{escape(description)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{SITE}{canonical}" />
{lds}'''
        + CSS_BASE + CSS + (BODY_NAV_RES if active_ressources else BODY_NAV_NONE) + body + '\n' + TAIL)


def breadcrumb(items):
    ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items)]}
    links = []
    for i, (n, u) in enumerate(items):
        links.append(f'<span aria-current="page">{escape(n)}</span>' if i == len(items) - 1 else f'<a href="{u}">{escape(n)}</a>')
    return ld, '<nav class="breadcrumb" aria-label="Fil d\'Ariane">' + ' <span aria-hidden="true">›</span> '.join(links) + '</nav>'


# ── /outils ──────────────────────────────────────────────────────────────────
def page_outils():
    ld, crumb = breadcrumb([('Accueil', '/'), ('Outils', '/outils')])
    body = f'''<main class="page-wrap">
  {crumb}
  <h1>Outils gratuits pour préparer le CRPE</h1>
  <p class="lead">Des outils simples pour t'entraîner aux épreuves du CRPE, en complément de ta préparation.</p>
  <div class="tool-cards">
    <article class="tool-card">
      <div class="tool-card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></div>
      <span class="tool-badge">Gratuit</span>
      <h2>Entraîneur CRPE</h2>
      <p>Réponds à 5 questions de maths ou de français tirées au hasard et reçois par e-mail un rapport détaillé : correction de chaque réponse et analyse de ta manière de répondre.</p>
      <a class="btn btn-primary" href="/outils/entraineur-crpe">Essayer gratuitement</a>
    </article>
  </div>
</main>'''
    return page('Outils gratuits pour préparer le CRPE | PassCRPE',
                "Outils gratuits pour réviser le CRPE : entraîne-toi sur des questions de maths et de français de niveau cycle 4, corrigées par l'IA.",
                '/outils', body, 'Outils gratuits pour préparer le CRPE', [ld])


# ── /outils/entraineur-crpe ──────────────────────────────────────────────────
FAQ = [
    ("L'Entraîneur CRPE est-il vraiment gratuit ?",
     f"Oui. Tu réponds à {QUESTIONS_PER_SET} questions, tu laisses ton prénom, ton nom et ton adresse e-mail, et tu reçois ton rapport détaillé gratuitement. Tu peux recevoir {WEEKLY_REPORT_LIMIT} rapport par semaine."),
    ("Que contient le rapport ?",
     "Pour chaque question : ta réponse, la réponse attendue, une note indicative, ce qui est juste, ce qui manque et tes erreurs de langue. Puis une analyse détaillée de ta manière de répondre (structure, justification, vocabulaire, rigueur, langue), tes habitudes récurrentes, tes 3 priorités de travail et un plan type de réponse."),
    ("La note donnée par l'IA est-elle fiable ?",
     "Elle est indicative. La correction est générée par une intelligence artificielle à partir d'un corrigé de référence : elle aide à progresser mais ne remplace pas un correcteur du concours et peut contenir des erreurs."),
    ("Quel est le niveau des questions ?",
     "Les questions sont de niveau cycle 4 (5e, 4e, 3e), le niveau attendu pour les connaissances disciplinaires en mathématiques et en français au CRPE."),
    ("Je n'ai pas reçu l'e-mail, que faire ?",
     "Vérifie tes courriers indésirables (spams) et l'onglet Promotions. L'e-mail arrive en général en quelques minutes. S'il n'arrive pas, écris-nous à contact@passcrpe.fr."),
]


def page_entraineur():
    ld, crumb = breadcrumb([('Accueil', '/'), ('Outils', '/outils'), ('Entraîneur CRPE', '/outils/entraineur-crpe')])
    faq_ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}
    app_ld = {'@context': 'https://schema.org', '@type': 'WebApplication', 'name': 'Entraîneur CRPE',
              'url': SITE + '/outils/entraineur-crpe', 'applicationCategory': 'EducationalApplication',
              'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'}, 'inLanguage': 'fr'}
    faq_html = ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in FAQ)
    body = f'''<main class="page-wrap">
  {crumb}
  <h1>Entraîneur CRPE : réponds à {QUESTIONS_PER_SET} questions, reçois ton rapport détaillé</h1>
  <p class="lead">Choisis une matière, rédige tes réponses à {QUESTIONS_PER_SET} questions de maths ou de français tirées au hasard, et reçois gratuitement par e-mail un rapport détaillé : la correction de chaque réponse et une analyse de ta manière de répondre, conforme aux attentes du CRPE.</p>

  <section class="tool" id="outil" aria-label="Entraîneur CRPE">
    <div class="tool-counter" id="counter" aria-live="polite">Gratuit · {QUESTIONS_PER_SET} questions · rapport détaillé par e-mail</div>
    <div class="tool-body" id="toolBody" aria-live="polite">
      <div class="loading"><span class="spinner" aria-hidden="true"></span>Chargement de l'outil…</div>
    </div>
  </section>

  <h2 id="comment-ca-marche">Comment ça marche ?</h2>
  <ol class="steps-list">
    <li><strong>Choisis ta matière</strong>, mathématiques ou français : l'outil tire {QUESTIONS_PER_SET} questions au hasard dans notre banque de questions. La catégorie de chaque question est indiquée au-dessus de l'énoncé.</li>
    <li><strong>Rédige tes réponses</strong> comme le jour du concours. Tes brouillons sont enregistrés sur ton appareil : tu peux revenir sur une question avant de terminer.</li>
    <li><strong>Laisse ton prénom, ton nom et ton adresse e-mail</strong> à la fin : ton rapport détaillé t'est envoyé par e-mail. Tu peux recevoir {WEEKLY_REPORT_LIMIT} rapport par semaine (recharge chaque lundi à 0 h, heure de Paris).</li>
    <li><strong>Ton rapport</strong> reprend chaque réponse avec la réponse attendue, une note indicative et des conseils, puis analyse ta manière de répondre : structure, justification, vocabulaire, rigueur et langue, avec tes 3 priorités de travail.</li>
    <li><strong>La correction est générée par une intelligence artificielle</strong> : la note est indicative, elle ne remplace pas un correcteur et peut contenir des erreurs.</li>
    <li><strong>Tes réponses</strong> sont enregistrées avec ton rapport pour te l'envoyer et améliorer l'outil, puis supprimées au bout de 12 mois au maximum. Elles ne sont ni publiées ni revendues. Détails dans notre <a href="/politique-de-confidentialite">politique de confidentialité</a>.</li>
    <li><strong>Niveau cycle 4</strong> (5e, 4e, 3e) : c'est le niveau attendu pour les connaissances disciplinaires du CRPE en mathématiques et en français.</li>
  </ol>

  <h2>Questions fréquentes</h2>
  <div class="faq">{faq_html}</div>
</main>
''' + COMMON_JS + ENTRAINEUR_JS
    return page(f"Entraîneur CRPE gratuit : {QUESTIONS_PER_SET} questions de maths ou de français et un rapport détaillé | PassCRPE",
                f"Entraîne-toi gratuitement au CRPE : réponds à {QUESTIONS_PER_SET} questions de maths ou de français de niveau cycle 4 et reçois par e-mail un rapport détaillé sur tes réponses et ta manière de répondre.",
                '/outils/entraineur-crpe', body, f"Entraîneur CRPE : réponds à {QUESTIONS_PER_SET} questions, reçois ton rapport détaillé", [ld, faq_ld, app_ld])


# Fonctions partagées par l'outil et la page du rapport
COMMON_JS = r'''<script>
window.EC = (function () {
  function esc(v) { return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  // Texte de la base : échappé, sauts de ligne conservés, puissances (2^3, x^(n+1)) en exposant
  function rich(v) {
    return esc(v).replace(/([\w)\]²³])\^(\(([^)]{1,12})\)|-?[\w.]{1,6})/g, function (_, b, e, inner) { return b + '<sup>' + (inner || e) + '</sup>'; }).replace(/\n/g, '<br>');
  }
  var SUBJECTS = { maths: 'Mathématiques', francais: 'Français' };
  function questionHtml(c, matiere) {
    var html = '<div class="badges"><span class="badge badge-subject">' + esc(SUBJECTS[matiere]) + '</span><span class="badge">' + esc(c.categorie) + '</span><span class="badge">Cycle 4' + (c.classe ? ' · ' + esc(c.classe) : '') + '</span></div>';
    html += '<div class="question-box">';
    if (c.enonce) html += '<span class="label">Énoncé</span><p>' + rich(c.enonce) + '</p>';
    if (c.figure) {
      var src = c.figure.type === 'path' ? esc(c.figure.src) : 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(c.figure.svg);
      html += '<div class="figure"><img src="' + src + '" alt="Figure accompagnant l\'énoncé" loading="lazy"></div>';
    }
    if (c.texte_support) html += '<span class="label">Texte support</span><p class="support">' + rich(c.texte_support) + '</p>';
    html += '<span class="label">Question</span><p class="q">' + rich(c.question) + '</p></div>';
    return html;
  }
  return { esc: esc, rich: rich, questionHtml: questionHtml, SUBJECTS: SUBJECTS };
})();
</script>
'''

ENTRAINEUR_JS = r'''<script>
(function () {
  var API = '/api/entraineur', MAX_LEN = 3000, N = __N__, KEY = 'entraineur-serie';
  var esc = EC.esc, SUBJECTS = EC.SUBJECTS;
  var body = document.getElementById('toolBody');
  // step : 'choose' | 'answer' | 'form' | 'sending' | 'sent'
  var state = { step: 'choose', serie: null, index: 0, busy: false, error: '', formError: '', email: '', limitReset: null };

  function save() { try { if (state.serie) localStorage.setItem(KEY, JSON.stringify({ serie: state.serie, index: state.index })); else localStorage.removeItem(KEY); } catch (e) {} }
  function restore() { try { var s = JSON.parse(localStorage.getItem(KEY) || 'null'); if (s && s.serie && s.serie.questions && s.serie.questions.length === N) { state.serie = s.serie; state.index = Math.min(s.index || 0, N); state.step = state.index >= N ? 'form' : 'answer'; } } catch (e) {} }
  function track(event, params) { try { (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: event }, params || {})); } catch (e) {} }
  function post(path, payload) {
    return fetch(API + path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { d._status = r.status; return d; }); })
      .catch(function () { return { _status: 0, error: 'Connexion impossible. Vérifie ta connexion internet.' }; });
  }
  function resetLabel(iso) { return new Date(iso).toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long', timeZone: 'Europe/Paris' }); }
  function answered() { return state.serie ? state.serie.reponses.filter(function (r) { return r && r.trim(); }).length : 0; }

  function chooserHtml() {
    return '<div><h3 style="margin-top:0">Choisis ta matière</h3><div class="subject-choice">' +
      '<button type="button" class="subject-btn" data-act="start" data-matiere="maths"><strong>Mathématiques</strong><span>Nombres et calculs, géométrie, proportionnalité, données et probabilités, pensée informatique</span></button>' +
      '<button type="button" class="subject-btn" data-act="start" data-matiere="francais"><strong>Français</strong><span>Lecture, écriture, vocabulaire et orthographe lexicale, grammaire et orthographe grammaticale</span></button>' +
      '</div><p style="font-size:13px;color:var(--gray-500);margin-top:10px">' + N + ' questions tirées au hasard · réponses rédigées · rapport détaillé envoyé par e-mail</p></div>';
  }

  function progressHtml() {
    var pct = Math.round(state.index / N * 100);
    return '<div class="progress" aria-hidden="true"><div class="progress-bar" style="width:' + pct + '%"></div></div>';
  }

  function answerHtml() {
    var s = state.serie, i = state.index, q = s.questions[i];
    return progressHtml() + '<p class="step-label">Question ' + (i + 1) + ' sur ' + N + '</p>' + EC.questionHtml(q, s.matiere) +
      '<form class="answer" id="answerForm"><label for="answer">Ta réponse</label>' +
      '<textarea id="answer" maxlength="' + MAX_LEN + '" placeholder="Rédige ta réponse comme le jour du concours : démarche, justification, vocabulaire précis." aria-describedby="answerCount">' + esc(s.reponses[i] || '') + '</textarea>' +
      '<div class="answer-meta"><span>Brouillon enregistré sur cet appareil</span><span id="answerCount"></span></div>' +
      '<div class="actions" style="margin-top:12px">' +
      (i > 0 ? '<button class="btn btn-ghost" type="button" data-act="prev">← Précédente</button>' : '') +
      '<button class="btn btn-primary" type="submit">' + (i === N - 1 ? 'Terminer' : 'Question suivante →') + '</button></div>' +
      '<p style="font-size:13px;color:var(--gray-500);margin-top:8px">Tu sèches ? Passe à la suite : la réponse attendue sera dans ton rapport.</p></form>';
  }

  function formHtml() {
    var n = answered();
    return progressHtml() + '<form class="lead-form" id="leadForm" novalidate><h3>Reçois ton rapport détaillé par e-mail</h3>' +
      '<p>Tu as répondu à <strong>' + n + ' question' + (n > 1 ? 's' : '') + ' sur ' + N + '</strong>. Laisse ton prénom, ton nom et ton adresse e-mail : ton rapport (correction de chaque réponse et analyse de ta manière de répondre) t\'est envoyé gratuitement.</p>' +
      '<div class="field-row"><div class="field"><label for="lf-prenom">Prénom</label><input id="lf-prenom" name="prenom" autocomplete="given-name" required maxlength="80"><span class="field-hint">Pour personnaliser ton rapport et nos e-mails.</span></div>' +
      '<div class="field"><label for="lf-nom">Nom</label><input id="lf-nom" name="nom" autocomplete="family-name" required maxlength="80"><span class="field-hint">Pour identifier ton rapport.</span></div></div>' +
      '<div class="field"><label for="lf-email">Adresse e-mail</label><input id="lf-email" name="email" type="email" autocomplete="email" required maxlength="254"><span class="field-hint">Pour t\'envoyer ton rapport et, seulement si tu l\'acceptes, nos conseils de préparation.</span></div>' +
      '<div class="field"><label for="lf-tel">Numéro de téléphone (facultatif)</label><input id="lf-tel" name="telephone" type="tel" autocomplete="tel" maxlength="30" placeholder="06 12 34 56 78"><span class="field-hint">Pour être contacté(e) par WhatsApp, SMS ou téléphone : te proposer une offre, partager un contenu ou avoir ton retour sur ton parcours de préparation.</span></div>' +
      '<label class="check"><input type="checkbox" name="consent_conseils"> <span>J\'accepte de recevoir par e-mail les conseils de préparation et les actualités de PassCRPE (facultatif).</span></label>' +
      '<label class="check"><input type="checkbox" name="consent_partenaires"> <span>J\'accepte de recevoir des offres de partenaires de PassCRPE (facultatif).</span></label>' +
      '<label class="check"><input type="checkbox" name="consent_contact_sms"> <span>J\'accepte d\'être contacté(e) par WhatsApp ou SMS pour recevoir des offres, des contenus ou donner mon avis sur ma préparation (facultatif, numéro requis).</span></label>' +
      (state.formError ? '<div class="notice notice-error" role="alert">' + esc(state.formError) + '</div>' : '') +
      '<div class="actions" style="margin-top:12px"><button class="btn btn-ghost" type="button" data-act="prev">← Revoir mes réponses</button><button class="btn btn-primary" type="submit">Recevoir mon rapport</button></div>' +
      '<p class="legal">Les cases facultatives n\'ont aucun effet sur l\'envoi de ton rapport. Tes données sont traitées par PassCRPE pour générer et t\'envoyer ton rapport (outil d\'envoi : Klaviyo ; correction par intelligence artificielle : Anthropic, sans tes coordonnées) et, si tu l\'acceptes, t\'envoyer nos e-mails. Si tu le donnes, ton numéro peut servir à t\'appeler (offre, contenu, retour sur ta préparation), et à t\'écrire par WhatsApp ou SMS seulement si tu as coché la case correspondante. Tu peux te désinscrire à tout moment et exercer tes droits d\'accès, de rectification et de suppression en écrivant à contact@passcrpe.fr. En savoir plus : <a href="/politique-de-confidentialite" target="_blank" rel="noopener">politique de confidentialité</a>.</p></form>';
  }

  function render() {
    var html = state.error ? '<div class="notice notice-error" role="alert">' + esc(state.error) + '</div>' : '';
    if (state.step === 'choose') html += state.busy ? '<div class="loading" role="status"><span class="spinner" aria-hidden="true"></span>Tirage des questions…</div>' : chooserHtml();
    else if (state.step === 'answer') html += answerHtml();
    else if (state.step === 'form') html += formHtml();
    else if (state.step === 'sending') html += '<div class="loading" role="status" style="flex-direction:column;align-items:flex-start;gap:6px"><span style="display:flex;gap:10px;align-items:center"><span class="spinner" aria-hidden="true"></span>Analyse de tes réponses en cours…</span><span style="font-weight:400;font-size:14px">Ton rapport détaillé est en préparation, cela prend environ 30 secondes. Ne ferme pas la page.</span></div>';
    else if (state.step === 'sent') html += state.reportUrl
      ? '<div class="sent"><div class="sent-icon" aria-hidden="true">✓</div><h3>Ton rapport est prêt</h3><p>L\'e-mail n\'a pas pu partir pour le moment : garde ce lien pour retrouver ton rapport.</p><a class="btn btn-primary" href="' + esc(state.reportUrl) + '">Voir mon rapport</a></div>'
      : '<div class="sent"><div class="sent-icon" aria-hidden="true">✓</div><h3>Ton rapport t\'a été envoyé par e-mail</h3><p>Tu vas le recevoir à <strong>' + esc(state.email) + '</strong> d\'ici quelques minutes. Pense à vérifier tes courriers indésirables et l\'onglet Promotions.</p></div>';
    else if (state.step === 'limit') html += '<div class="notice notice-info">Tu as déjà reçu un rapport cette semaine avec cette adresse e-mail. Tu pourras en demander un nouveau à partir du ' + resetLabel(state.limitReset) + ' à 0 h. Tes réponses restent enregistrées sur cet appareil d\'ici là.</div>' +
      '<div class="actions" style="margin-top:12px"><button class="btn btn-ghost" type="button" data-act="back-form">Revenir au formulaire</button></div>';
    body.innerHTML = html;
    updateCount();
  }

  function updateCount() {
    var t = document.getElementById('answer'), out = document.getElementById('answerCount');
    if (!t || !out) return;
    out.textContent = t.value.length + ' / ' + MAX_LEN + ' caractères';
  }
  function keepAnswer() {
    var t = document.getElementById('answer');
    if (t && state.serie) { state.serie.reponses[state.index] = t.value; save(); }
  }
  function scrollTop() { document.getElementById('outil').scrollIntoView({ behavior: 'smooth', block: 'start' }); }

  function start(matiere) {
    state.busy = true; state.error = ''; render();
    post('/questions', { matiere: matiere }).then(function (d) {
      state.busy = false;
      if (d._status === 200) {
        state.serie = { matiere: d.matiere, token: d.token, questions: d.questions, reponses: d.questions.map(function () { return ''; }) };
        state.index = 0; state.step = 'answer'; save();
        track('entraineur_start', { matiere: matiere });
      } else state.error = d.error || 'Une erreur est survenue.';
      render(); scrollTop();
    });
  }

  function submitLead(form) {
    var f = form.elements;
    var payload = {
      token: state.serie.token, reponses: state.serie.reponses,
      prenom: f.prenom.value.trim(), nom: f.nom.value.trim(), email: f.email.value.trim(), telephone: f.telephone.value.trim(),
      consent_conseils: f.consent_conseils.checked, consent_partenaires: f.consent_partenaires.checked, consent_contact_sms: f.consent_contact_sms.checked,
    };
    if (!payload.prenom || !payload.nom || !payload.email) { state.formError = 'Merci d\'indiquer ton prénom, ton nom et ton adresse e-mail.'; render(); return; }
    if (payload.consent_contact_sms && !payload.telephone) { state.formError = 'Indique ton numéro de téléphone pour être contacté(e) par WhatsApp ou SMS.'; render(); return; }
    if (!answered()) { state.formError = 'Réponds au moins à une question avant de demander ton rapport.'; render(); return; }
    state.formError = ''; state.error = ''; state.step = 'sending'; render(); scrollTop();
    post('/rapport', payload).then(function (d) {
      if (d._status === 200) {
        state.email = d.email; state.reportUrl = d.emailed ? '' : (d.report_url || ''); state.step = 'sent'; state.serie = null; save();
        track('entraineur_rapport', { emailed: !!d.emailed });
      } else if (d.error === 'weekly_limit') { state.step = 'limit'; state.limitReset = d.resetAt; }
      else if (d._status === 400 && /expiré|plus disponible/.test(d.error || '')) { state.serie = null; save(); state.step = 'choose'; state.error = d.error; }
      else { state.step = 'form'; state.formError = d.error || 'Le rapport n\'a pas pu être généré. Réessaie dans quelques instants.'; }
      render(); scrollTop();
    });
  }

  body.addEventListener('click', function (e) {
    var el = e.target.closest('[data-act]'); if (!el || state.busy) return;
    var act = el.getAttribute('data-act');
    if (act === 'start') start(el.getAttribute('data-matiere'));
    else if (act === 'prev') { keepAnswer(); state.index = Math.max(0, (state.step === 'form' ? N : state.index) - 1); state.step = 'answer'; save(); render(); scrollTop(); }
    else if (act === 'back-form') { state.step = 'form'; render(); }
  });
  body.addEventListener('submit', function (e) {
    e.preventDefault();
    if (e.target.id === 'answerForm') {
      keepAnswer();
      state.index += 1;
      state.step = state.index >= N ? 'form' : 'answer';
      save(); render(); scrollTop();
    } else if (e.target.id === 'leadForm') submitLead(e.target);
  });
  body.addEventListener('input', function (e) { if (e.target.id === 'answer') { keepAnswer(); updateCount(); } });

  restore();
  render();
})();
</script>'''.replace('__N__', str(QUESTIONS_PER_SET))


# ── /outils/entraineur-crpe/rapport/:token ───────────────────────────────────
def page_rapport():
    body = '''<main class="page-wrap report-page">
  <div id="report"><div class="loading" role="status"><span class="spinner" aria-hidden="true"></span>Chargement de ton rapport…</div></div>
</main>
''' + COMMON_JS + RAPPORT_JS
    return page('Ton rapport Entraîneur CRPE | PassCRPE',
                "Ton rapport détaillé de l'Entraîneur CRPE : correction de chaque réponse et analyse de ta manière de répondre.",
                '/outils/entraineur-crpe', body, 'Ton rapport Entraîneur CRPE', [], robots='noindex, nofollow')


RAPPORT_JS = r'''<script>
(function () {
  var esc = EC.esc, rich = EC.rich;
  var LEVELS = { a_retravailler: 'À retravailler', en_bonne_voie: 'En bonne voie', attendu_atteint: 'Attendu du CRPE atteint' };
  var DIMS = [['structure', 'Structure de tes réponses'], ['justification', 'Démarche et justification'], ['vocabulaire', 'Vocabulaire disciplinaire'], ['rigueur', 'Rigueur et exactitude'], ['langue', 'Maîtrise de la langue']];
  var el = document.getElementById('report');
  var parts = location.pathname.split('/').filter(Boolean);
  var token = new URLSearchParams(location.search).get('t') || parts[parts.length - 1];
  function note(n) { return String(n).replace('.', ',') + '/20'; }
  function list(items, tag) { tag = tag || 'ul'; return items && items.length ? '<' + tag + '>' + items.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</' + tag + '>' : '<p>Rien à signaler.</p>'; }
  function level(n) { return '<span class="level level-' + esc(n) + '">' + esc(LEVELS[n] || n) + '</span>'; }

  fetch('/api/entraineur/rapport/' + encodeURIComponent(token)).then(function (r) { return r.json().then(function (d) { d._status = r.status; return d; }); }).then(function (d) {
    if (d._status !== 200) { el.innerHTML = '<h1>Rapport introuvable</h1><p>Ce lien n\'est pas valide ou a expiré.</p>'; return; }
    var s = d.synthese, date = new Date(d.created_at).toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
    var html = '<p class="report-kicker">Entraîneur CRPE · ' + esc(EC.SUBJECTS[d.matiere]) + ' · ' + esc(date) + '</p>' +
      '<h1>Ton rapport détaillé' + (d.prenom ? ', ' + esc(d.prenom) : '') + '</h1>' +
      '<div class="report-score"><div><span class="score-big">' + note(d.note) + '</span><span class="score-sub">note indicative moyenne</span></div>' + level(s.niveau) + '</div>' +
      '<p class="lead">' + esc(s.appreciation_globale) + '</p>' +
      '<div class="actions no-print" style="margin:8px 0 8px"><button class="btn btn-ghost" type="button" onclick="window.print()">Télécharger en PDF</button></div>' +
      '<h2>Ta manière de répondre</h2>' + DIMS.map(function (k) { return '<h3>' + k[1] + '</h3><p>' + esc(s.analyse[k[0]]) + '</p>'; }).join('') +
      '<h3>Tes habitudes récurrentes</h3>' + list(s.habitudes) +
      '<h3>Tes points forts</h3>' + list(s.points_forts) +
      '<h2>Tes 3 priorités de travail</h2>' + list(s.priorites, 'ol') +
      '<h2>Plan type pour rédiger ta réponse au CRPE</h2>' + list(s.plan_type, 'ol') +
      '<h2>Correction question par question</h2>';
    d.questions.forEach(function (q, i) {
      var e = q.evaluation;
      html += '<section class="report-q"><div class="report-q-head"><h3>Question ' + (i + 1) + '</h3><span>' + level(e.niveau) + ' <span class="note20">' + note(e.note) + '</span></span></div>' +
        EC.questionHtml(q, d.matiere) +
        '<div class="report-block"><h4>Ta réponse</h4><p class="your-answer">' + (q.reponse ? esc(q.reponse).replace(/\n/g, '<br>') : '<em>Pas de réponse</em>') + '</p></div>' +
        '<div class="report-block"><h4>Appréciation</h4><p>' + esc(e.appreciation) + '</p>' +
        (e.points_forts.length ? '<h4>Ce qui est juste</h4>' + list(e.points_forts) : '') +
        (e.points_a_ameliorer.length ? '<h4>À améliorer</h4><ul>' + e.points_a_ameliorer.map(function (p) { return '<li>' + (p.citation ? '<blockquote>« ' + esc(p.citation) + ' »</blockquote>' : '') + esc(p.commentaire) + '</li>'; }).join('') + '</ul>' : '') +
        (e.elements_manquants.length ? '<h4>Éléments attendus manquants</h4>' + list(e.elements_manquants) : '') +
        (e.langue.length ? '<h4>Langue</h4><ul>' + e.langue.map(function (l) { return '<li>« ' + esc(l.citation) + ' » → <strong>' + esc(l.correction) + '</strong> <span class="badge">' + esc(l.type) + '</span></li>'; }).join('') + '</ul>' : '') +
        '</div><div class="corrige"><h4>Réponse attendue</h4><p>' + rich(q.reponse_attendue) + '</p><h4>Explication</h4><p>' + esc(e.explication) + '</p></div></section>';
    });
    html += '<p class="legal" style="margin-top:24px">Correction générée par une intelligence artificielle à partir d\'un corrigé de référence : les notes sont indicatives et peuvent contenir des erreurs. Elles ne remplacent pas un correcteur du concours.</p>' +
      '<div class="report-cta no-print"><h2>Envie d\'aller plus loin ?</h2><p>Avec PassCRPE, entraîne-toi sur des milliers d\'exercices corrigés en français et en maths, adaptés à ton niveau.</p><a class="btn btn-primary" href="/">Découvrir PassCRPE</a></div>';
    el.innerHTML = html;
    document.title = 'Ton rapport Entraîneur CRPE' + (d.prenom ? ' · ' + d.prenom : '') + ' | PassCRPE';
  }).catch(function () { el.innerHTML = '<p class="notice notice-error">Impossible de charger ton rapport. Vérifie ta connexion et recharge la page.</p>'; });
})();
</script>'''


# ── /politique-de-confidentialite ────────────────────────────────────────────
def ph(t):
    return f'<span class="placeholder">[{t}]</span>'


def page_confidentialite():
    ld, crumb = breadcrumb([('Accueil', '/'), ('Politique de confidentialité', '/politique-de-confidentialite')])
    body = f'''<main class="page-wrap">
  {crumb}
  <h1>Politique de confidentialité</h1>
  <p><em>Dernière mise à jour : 12 octobre 2026</em></p>
  <p>Cette politique explique quelles données personnelles PassCRPE collecte sur le site passcrpe.fr, pourquoi, combien de temps elles sont conservées et comment exercer tes droits, conformément au Règlement général sur la protection des données (RGPD) et à la loi Informatique et Libertés.</p>

  <h2>1. Responsable du traitement</h2>
  <p>Le responsable du traitement est {ph("Nom ou raison sociale de l'éditeur")}, {ph("forme juridique et numéro SIREN")}, dont le siège est situé {ph("adresse postale")}.<br>Contact : <a href="mailto:contact@passcrpe.fr">contact@passcrpe.fr</a>.</p>

  <h2>2. Données collectées</h2>
  <ul>
    <li><strong>Inscription à l'application PassCRPE</strong> : prénom, nom, adresse e-mail, mot de passe (chiffré), numéro de téléphone (facultatif), concours et académie visés.</li>
    <li><strong>Entraîneur CRPE</strong> : prénom, nom, adresse e-mail, numéro de téléphone (facultatif), choix de consentement, réponses rédigées et rapport détaillé généré (consultable via un lien personnel envoyé par e-mail). Nous n'enregistrons pas ton adresse IP.</li>
    <li><strong>Utilisation de l'application</strong> : réponses aux exercices, progression, échanges avec le support.</li>
    <li><strong>Paiement</strong> : le paiement est traité par PayPal ; PassCRPE ne reçoit pas tes coordonnées bancaires.</li>
    <li><strong>Mesure d'audience et publicité</strong> : cookies Google Analytics (via Google Tag Manager) et Meta Pixel.</li>
  </ul>

  <h2>3. Finalités et bases légales</h2>
  <ul>
    <li>Fournir l'application, l'Entraîneur CRPE et le support : exécution du service que tu demandes.</li>
    <li>Calculer les quotas de questions et éviter les abus : intérêt légitime.</li>
    <li>Corriger tes réponses avec une intelligence artificielle et améliorer la qualité des corrections : exécution du service et intérêt légitime.</li>
    <li>T'envoyer nos conseils de préparation, nos actualités ou des offres de partenaires par e-mail : <strong>uniquement avec ton consentement</strong>, que tu peux retirer à tout moment.</li>
    <li>Te contacter par téléphone avec le numéro donné (facultatif) dans l'Entraîneur CRPE, pour te proposer une offre, partager un contenu ou recueillir ton retour sur ton parcours de préparation : intérêt légitime, tu peux t'y opposer à tout moment.</li>
    <li>Te contacter par WhatsApp ou SMS pour les mêmes raisons : <strong>uniquement si tu as coché la case correspondante</strong>. Tu peux retirer ton accord à tout moment (répondre STOP ou écrire à contact@passcrpe.fr).</li>
    <li>Mesure d'audience et publicité ciblée : ton consentement aux cookies.</li>
  </ul>

  <h2>4. Destinataires et sous-traitants</h2>
  <p>Tes données sont destinées à PassCRPE. Elles ne sont jamais revendues. Nous faisons appel aux sous-traitants suivants :</p>
  <ul>
    <li><strong>Supabase</strong> : hébergement de la base de données (Union européenne) ;</li>
    <li><strong>Vercel</strong> : hébergement du site ;</li>
    <li><strong>Anthropic</strong> : génération des corrections par intelligence artificielle (la réponse rédigée et l'énoncé sont transmis, sans tes nom, e-mail ni téléphone) ;</li>
    <li><strong>Klaviyo</strong> : gestion des contacts et envoi des e-mails ;</li>
    <li><strong>PayPal</strong> : paiement ;</li>
    <li><strong>Google</strong> et <strong>Meta</strong> : mesure d'audience et publicité.</li>
  </ul>
  <p>Certains de ces prestataires peuvent traiter des données hors de l'Union européenne ; ces transferts sont encadrés par les garanties prévues par le RGPD (décision d'adéquation ou clauses contractuelles types).</p>

  <h2>5. Durées de conservation</h2>
  <ul>
    <li>Compte de l'application : pendant la durée de ton accès, puis 3 ans après ta dernière activité.</li>
    <li>Contacts de l'Entraîneur CRPE et prospects : 3 ans à compter du dernier contact de ta part.</li>
    <li>Réponses et rapports de l'Entraîneur CRPE : 12 mois au maximum.</li>
    <li>Données de facturation : 10 ans (obligation légale).</li>
    <li>Cookies : 13 mois au maximum.</li>
  </ul>

  <h2>6. Tes droits</h2>
  <p>Tu disposes d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité de tes données, ainsi que du droit de retirer ton consentement à tout moment et de définir des directives sur le sort de tes données après ton décès. Pour les exercer, écris à <a href="mailto:contact@passcrpe.fr">contact@passcrpe.fr</a>. Tu peux te désinscrire de nos e-mails à tout moment grâce au lien présent dans chacun d'eux.</p>
  <p>Si tu estimes que tes droits ne sont pas respectés, tu peux adresser une réclamation à la CNIL (<a href="https://www.cnil.fr" target="_blank" rel="noopener">cnil.fr</a>).</p>

  <h2>7. Cookies</h2>
  <p>Le site utilise des cookies nécessaires à son fonctionnement (connexion à l'application et accès à l'Entraîneur CRPE) et, sous réserve de ton consentement, des cookies de mesure d'audience et de publicité.</p>

  <h2>8. Sécurité</h2>
  <p>Les données sont transmises de façon chiffrée (HTTPS) et l'accès aux bases de données est restreint. Les corrections par intelligence artificielle sont générées côté serveur.</p>
</main>'''
    return page('Politique de confidentialité | PassCRPE',
                'Politique de confidentialité de PassCRPE : données collectées, finalités, durées de conservation, sous-traitants et exercice de tes droits RGPD.',
                '/politique-de-confidentialite', body, 'Politique de confidentialité de PassCRPE', [ld], active_ressources=False)


# ── Écriture ─────────────────────────────────────────────────────────────────
for name, html in [('outils.html', page_outils()), ('entraineur-crpe.html', page_entraineur()),
                   ('entraineur-rapport.html', page_rapport()), ('politique-de-confidentialite.html', page_confidentialite())]:
    open(os.path.join(ROOT, 'landing', name), 'w', encoding='utf-8').write(html)
print('Pages outils, entraîneur et politique de confidentialité générées.')

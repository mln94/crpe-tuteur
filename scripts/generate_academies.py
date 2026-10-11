#!/usr/bin/env python3
"""Génère la page hub « CRPE par académie » et les 30 pages académie.

Données : scripts/academies-data.json
Sorties : landing/crpe-par-academie.html et landing/academies/<slug>.html
Usage   : python3 scripts/generate_academies.py
"""
import json
import math
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'
HUB_URL = '/crpe-par-academie'

data = json.load(open(os.path.join(ROOT, 'scripts', 'academies-data.json'), encoding='utf-8'))
SESSION = data['session']
ACADS = data['academies']
BY_SLUG = {a['slug']: a for a in ACADS}
N = len(ACADS)

# ── Calculs ──────────────────────────────────────────────────────────────────
for a in ACADS:
    a['taux'] = a['admis'] / a['presents']
    a['tauxAdmissibilite'] = a['admissibles'] / a['presents']
    a['presentsParPoste'] = a['presents'] / a['postes']

def ranks(key):
    """Rang (1 = valeur la plus haute), ex aequo autorisés."""
    vals = sorted((a[key] for a in ACADS), reverse=True)
    return {a['slug']: vals.index(a[key]) + 1 for a in ACADS}

RANK_POSTES = ranks('postes')
RANK_ADMISSIBILITE = ranks('tauxAdmissibilite')
RANK_REUSSITE = ranks('taux')

# Sélectivité : 25 % des académies au taux de réussite le plus bas, 50 % du milieu, 25 % au taux le plus haut
SELECTIVITE = {}
for i, a in enumerate(sorted(ACADS, key=lambda x: x['taux'])):
    p = i / (N - 1)
    SELECTIVITE[a['slug']] = 'tres' if p <= 0.25 else ('peu' if p >= 0.75 else 'moyen')
SEL_LABEL = {'tres': 'Très sélective', 'moyen': 'Moyennement sélective', 'peu': 'Peu sélective'}

TOT = {k: sum(a[k] for a in ACADS) for k in ('postes', 'inscrits', 'presents', 'admissibles', 'admis', 'inscritsLC')}
TAUX_NATIONAL = TOT['admis'] / TOT['presents']
TAUX_ADMISSIBILITE_NATIONAL = TOT['admissibles'] / TOT['presents']

# ── Formats ──────────────────────────────────────────────────────────────────
def fint(n):
    return f'{n:,}'.replace(',', ' ')

def fpct(x):
    return f'{x * 100:.2f}'.replace('.', ',') + ' %'

def fdec(x):
    return f'{x:.1f}'.replace('.', ',')

def rang(r):
    return '1re' if r == 1 else f'{r}e'

def de(nom):
    return ("d'" if nom[0] in 'AEIOUYÉÈÎ' else 'de ') + nom

def url(a):
    return f'{HUB_URL}/{a["slug"]}'

# ── Gabarit commun (en-tête, menu, pied de page, fenêtre d'inscription) ──────
tpl = open(TEMPLATE, encoding='utf-8').read()
HEAD_START = tpl[:tpl.index('  <title>')]
css_start = tpl.index('  <link rel="preconnect"')
css_end = tpl.index('  </style>', css_start)
CSS_BASE = tpl[css_start:css_end]
BODY_START = tpl[css_end:tpl.index('<div class="article-wrap">')]
TAIL = tpl[tpl.index('<footer>'):]

# Le gabarit contient déjà le lien vers le hub : on le marque comme actif et on retire l'état actif du blog
NAV_HUB = f'<li><a href="{HUB_URL}">CRPE par académie</a></li>'
NAV_BLOG = '<li><a href="/blog" class="active">Blog</a></li>'
assert BODY_START.count(NAV_HUB) == 1 and BODY_START.count(NAV_BLOG) == 1
BODY_START = (BODY_START.replace(NAV_HUB, f'<li><a href="{HUB_URL}" class="active">CRPE par académie</a></li>')
              .replace(NAV_BLOG, '<li><a href="/blog">Blog</a></li>'))
assert TAIL.count(f'<a href="{HUB_URL}">CRPE par académie</a>') == 1

CSS = """
    /* ACADÉMIES */
    .acad-wrap { max-width: 1040px; margin: 0 auto; padding: 32px 24px 80px; font-size: 16px; line-height: 1.75; color: var(--gray-700); }
    .acad-wrap h1 { margin-bottom: 14px; }
    .acad-wrap h2 { font-size: 24px; font-weight: 800; color: var(--gray-900); margin: 48px 0 12px; letter-spacing: -.2px; }
    .acad-wrap h3 { font-size: 17px; font-weight: 800; color: var(--gray-900); margin: 24px 0 8px; }
    .acad-wrap p { margin-bottom: 16px; }
    .acad-wrap ul { margin: 0 0 18px 22px; }
    .acad-wrap li { margin-bottom: 6px; }
    .acad-wrap strong { color: var(--gray-900); }
    .lead { font-size: 17px; max-width: 780px; }
    .breadcrumb { display: flex; flex-wrap: wrap; gap: 8px; font-size: 13px; color: var(--gray-400); margin-bottom: 20px; }
    .breadcrumb a { color: var(--gray-500); text-decoration: none; font-weight: 600; }
    .breadcrumb a:hover { color: var(--indigo-600); }
    .breadcrumb [aria-current] { color: var(--gray-700); font-weight: 600; }

    .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 24px 0 8px; }
    .kpi { border: 1px solid var(--gray-200); border-radius: 14px; padding: 16px 18px; display: flex; flex-direction: column; gap: 2px; }
    .kpi-value { font-size: 26px; font-weight: 900; color: var(--gray-900); font-variant-numeric: tabular-nums; letter-spacing: -.4px; }
    .kpi-label { font-size: 13px; color: var(--gray-500); line-height: 1.4; }
    .kpi-accent { background: var(--indigo-50); border-color: var(--indigo-100); }
    .kpi-accent .kpi-value { color: var(--indigo-700); }

    .sel { display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 20px; white-space: nowrap; }
    .sel::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: currentColor; }
    .sel-tres { background: #fef2f2; color: #b91c1c; }
    .sel-moyen { background: #fffbeb; color: #b45309; }
    .sel-peu { background: #f0fdf4; color: #15803d; }

    .map-card { border: 1px solid var(--gray-200); border-radius: 16px; padding: 16px; margin: 16px 0 8px; }
    .fr-map { display: block; width: 100%; max-width: 640px; height: auto; margin: 0 auto; }
    .fr-map .land { fill: #eef2ff; stroke: #c7d2fe; stroke-width: 1.5; stroke-linejoin: round; }
    .fr-map a { cursor: pointer; }
    .fr-map circle { stroke: #fff; stroke-width: 2.5; transition: r .15s; }
    .fr-map a:hover circle, .fr-map a:focus circle { r: 10; }
    .fr-map text { font-size: 13px; font-weight: 700; fill: var(--gray-800); paint-order: stroke; stroke: #fff; stroke-width: 4px; stroke-linejoin: round; }
    .fr-map a:hover text, .fr-map a:focus text { fill: var(--indigo-700); text-decoration: underline; }
    .fr-map .current circle { stroke: var(--gray-900); stroke-width: 3; }
    .fr-map .current text { font-size: 15px; font-weight: 900; }
    .fr-map .dim { opacity: .45; }
    .dom-row { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 10px; }
    .dom-row .label { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--gray-400); align-self: center; margin-right: 4px; }
    .chip { display: inline-flex; align-items: center; gap: 6px; border: 1px solid var(--gray-200); border-radius: 20px; padding: 5px 12px; font-size: 13px; font-weight: 600; color: var(--gray-800); text-decoration: none; }
    .chip:hover { border-color: var(--indigo-600); color: var(--indigo-700); }
    .chip.current { border-color: var(--gray-900); font-weight: 800; }
    .dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
    .dot-tres { background: #dc2626; } .dot-moyen { background: #f59e0b; } .dot-peu { background: #16a34a; }
    .legend { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; font-size: 13px; color: var(--gray-600); margin-top: 14px; }
    .legend span { display: inline-flex; align-items: center; gap: 6px; }

    .acad-wrap .table-wrap { margin: 16px 0 8px; }
    .acad-wrap table { font-size: 14px; }
    .acad-wrap thead th { padding: 0; }
    .acad-wrap thead th button { all: unset; box-sizing: border-box; display: block; width: 100%; padding: 12px 14px; cursor: pointer; font-weight: 700; white-space: nowrap; }
    .acad-wrap thead th button::after { content: attr(data-arrow); margin-left: 6px; font-size: 10px; }
    .acad-wrap thead th button:focus-visible { outline: 2px solid #fff; outline-offset: -4px; }
    .acad-wrap td { padding: 10px 14px; white-space: nowrap; }
    .acad-wrap td a { color: var(--indigo-600); font-weight: 700; text-decoration: none; }
    .acad-wrap td a:hover { text-decoration: underline; }
    .num { text-align: right; font-variant-numeric: tabular-nums; }
    .acad-wrap thead th.num button { text-align: right; }

    .region-grid, .rank-grid, .voisins-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; }
    .card { border: 1px solid var(--gray-200); border-radius: 14px; padding: 16px 18px; }
    .card h3 { margin: 0 0 8px; font-size: 15px; }
    .region-grid ul { list-style: none; margin: 0; }
    .region-grid li { display: flex; justify-content: space-between; align-items: center; gap: 8px; font-size: 14px; margin-bottom: 4px; }
    .region-grid li a { color: var(--indigo-600); font-weight: 600; text-decoration: none; }
    .region-grid li a:hover { text-decoration: underline; }
    .rank-big { font-size: 34px; font-weight: 900; color: var(--gray-900); line-height: 1.1; }
    .rank-big small { font-size: 15px; font-weight: 600; color: var(--gray-400); }
    .card p { font-size: 14px; margin: 6px 0 0; }
    a.card { display: block; text-decoration: none; color: inherit; transition: box-shadow .2s, transform .2s, border-color .2s; }
    a.card:hover { box-shadow: 0 8px 24px rgba(0,0,0,.06); transform: translateY(-2px); border-color: var(--indigo-100); }
    a.card h3 { color: var(--indigo-700); }

    .funnel { display: flex; flex-direction: column; gap: 10px; margin: 16px 0 8px; }
    .funnel-row { display: grid; grid-template-columns: 120px 1fr; align-items: center; gap: 12px; font-size: 14px; }
    .funnel-label { font-weight: 700; color: var(--gray-800); }
    .funnel-track { background: var(--gray-100); border-radius: 8px; height: 32px; position: relative; }
    .funnel-bar { background: var(--indigo-600); border-radius: 8px; height: 100%; min-width: 4px; }
    .funnel-val { position: absolute; left: 10px; top: 50%; transform: translateY(-50%); font-weight: 700; font-variant-numeric: tabular-nums; color: var(--gray-900); paint-order: stroke; }
    .funnel-row.light .funnel-bar { background: #a5b4fc; }

    .callout { background: var(--indigo-50); border: 1px solid var(--indigo-100); border-radius: 14px; padding: 18px 22px; margin: 20px 0 24px; font-size: 15px; }
    .callout strong { color: var(--indigo-700); }
    .updated { font-size: 13px; color: var(--gray-400); margin-top: 32px; }
    .back-hub { display: inline-flex; margin-top: 24px; font-weight: 700; color: var(--indigo-600); text-decoration: none; }
    .back-hub:hover { text-decoration: underline; }

    .cta-section { background: linear-gradient(135deg, var(--indigo-600) 0%, #7c3aed 100%); padding: 96px 24px; text-align: center; position: relative; overflow: hidden; }
    .cta-section::before { content: ''; position: absolute; top: -80px; left: -80px; width: 320px; height: 320px; background: rgba(255,255,255,0.06); border-radius: 50%; }
    .cta-section::after { content: ''; position: absolute; bottom: -60px; right: -60px; width: 240px; height: 240px; background: rgba(255,255,255,0.04); border-radius: 50%; }
    .cta-section h2 { font-size: clamp(28px, 4vw, 44px); font-weight: 900; color: #fff; letter-spacing: -1px; line-height: 1.15; margin-bottom: 16px; position: relative; z-index: 1; }
    .cta-section p { font-size: 18px; color: rgba(255,255,255,0.75); max-width: 520px; margin: 0 auto 40px; line-height: 1.6; position: relative; z-index: 1; }
    .cta-form { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; position: relative; z-index: 1; }
    .btn-white { display: inline-flex; align-items: center; gap: 8px; background: #fff; color: var(--indigo-700); padding: 14px 28px; border-radius: 12px; font-size: 15px; font-weight: 700; border: none; cursor: pointer; font-family: inherit; text-decoration: none; transition: transform .15s, box-shadow .2s; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    .btn-white:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(0,0,0,0.2); }
    .cta-section .cta-note { font-size: 13px; color: rgba(255,255,255,0.55); margin: 16px 0 0; max-width: none; }

    @media (max-width: 640px) {
      .fr-map text { font-size: 17px; }
      .funnel-row { grid-template-columns: 92px 1fr; }
    }
    @media (max-width: 520px) { .nav-inner { padding: 0 16px; } .nav-login { display: none; } .nav-cta { padding: 8px 12px; } .acad-wrap { padding: 24px 16px 64px; } }
"""

# ── Carte de France ──────────────────────────────────────────────────────────
FRANCE = [(2.37,51.05),(2.55,51.09),(3.2,50.75),(4.15,50.3),(4.8,50.15),(4.85,49.8),(5.4,49.6),(5.9,49.5),(6.37,49.47),
    (7.0,49.15),(7.6,49.05),(8.2,48.97),(7.8,48.5),(7.55,47.6),(6.95,47.45),(6.45,46.95),(6.1,46.4),(6.8,46.4),(7.0,45.9),
    (6.8,45.7),(7.1,45.2),(6.65,45.0),(6.95,44.4),(7.5,44.1),(7.53,43.78),(7.27,43.7),(6.6,43.2),(5.9,43.1),(5.35,43.3),
    (4.8,43.4),(4.3,43.5),(3.6,43.3),(3.1,43.0),(3.17,42.44),(2.6,42.35),(1.7,42.5),(0.7,42.8),(-0.3,42.8),(-1.4,43.25),
    (-1.78,43.37),(-1.45,43.6),(-1.25,44.5),(-1.15,45.5),(-1.2,45.8),(-1.6,46.4),(-2.1,46.8),(-2.5,47.3),(-3.0,47.5),
    (-4.2,47.8),(-4.7,48.0),(-4.75,48.4),(-4.3,48.65),(-3.5,48.8),(-2.8,48.55),(-2.0,48.65),(-1.5,48.64),(-1.6,49.2),
    (-1.85,49.7),(-1.25,49.7),(-1.15,49.35),(-0.2,49.3),(0.2,49.45),(0.1,49.5),(0.6,49.85),(1.4,50.1),(1.6,50.4),(1.6,50.9)]
CORSE = [(9.4,43.0),(9.55,42.6),(9.5,42.0),(9.4,41.6),(9.2,41.37),(8.8,41.55),(8.6,41.9),(8.6,42.3),(8.7,42.6),(9.3,42.7)]
K, PAD = 56, 24
W, H = round((9.7 + 5) * math.cos(math.radians(46.5)) * K) + 2 * PAD, round((51.25 - 41.3) * K) + 2 * PAD

def proj(lon, lat):
    return round((lon + 5) * math.cos(math.radians(46.5)) * K + PAD, 1), round((51.25 - lat) * K + PAD, 1)

def poly(points):
    return 'M' + ' L'.join(f'{x},{y}' for x, y in (proj(*p) for p in points)) + ' Z'

def carte(current=None):
    marks = []
    for a in sorted(ACADS, key=lambda a: a['slug'] == (current or {}).get('slug')):  # l'académie courante au-dessus
        if a['outreMer']:
            continue
        x, y = proj(a['lon'], a['lat'])
        pos = a['libelle']
        tx, ty, anchor = {'r': (x + 12, y + 5, 'start'), 'l': (x - 12, y + 5, 'end'),
                          't': (x, y - 13, 'middle'), 'b': (x, y + 23, 'middle')}[pos]
        cls = ' class="current"' if current and a is current else (' class="dim"' if current else '')
        color = {'tres': '#dc2626', 'moyen': '#f59e0b', 'peu': '#16a34a'}[SELECTIVITE[a['slug']]]
        marks.append(f'<a href="{url(a)}"{cls} aria-label="Académie {escape(de(a["nom"]))} : {SEL_LABEL[SELECTIVITE[a["slug"]]].lower()}, {fpct(a["taux"])} de réussite">'
                     f'<circle cx="{x}" cy="{y}" r="7" fill="{color}"/>'
                     f'<text x="{tx}" y="{ty}" text-anchor="{anchor}">{escape(a["nom"])}</text></a>')
    dom = ''.join(
        f'<a class="chip{" current" if current and a is current else ""}" href="{url(a)}"><span class="dot dot-{SELECTIVITE[a["slug"]]}"></span>{escape(a["nom"])}</a>'
        for a in sorted(ACADS, key=lambda a: a['nom']) if a['outreMer'])
    return f'''<div class="map-card">
    <svg class="fr-map" viewBox="0 0 {W} {H}" role="img" aria-label="Carte de France des académies du CRPE">
      <path class="land" d="{poly(FRANCE)}"/><path class="land" d="{poly(CORSE)}"/>
      {''.join(marks)}
    </svg>
    <div class="dom-row"><span class="label">Outre-mer</span>{dom}</div>
    <div class="legend"><span><span class="dot dot-tres"></span>Très sélective</span><span><span class="dot dot-moyen"></span>Moyennement sélective</span><span><span class="dot dot-peu"></span>Peu sélective</span></div>
  </div>'''

def sel_badge(a):
    s = SELECTIVITE[a['slug']]
    return f'<span class="sel sel-{s}">{SEL_LABEL[s]}</span>'

METHODE = f'''<p>Pour classer les académies, nous avons calculé pour chacune le <strong>taux de réussite</strong> : le nombre d'admis divisé par le nombre de candidats présents aux épreuves. Les académies sont ensuite réparties en trois groupes :</p>
  <ul>
    <li><span class="sel sel-tres">Très sélective</span> : les 25 % d'académies au taux de réussite le plus bas ;</li>
    <li><span class="sel sel-moyen">Moyennement sélective</span> : les 50 % du milieu ;</li>
    <li><span class="sel sel-peu">Peu sélective</span> : les 25 % au taux de réussite le plus haut.</li>
  </ul>'''

def page(title, description, canonical, breadcrumb_ld, body, og_title):
    return (HEAD_START
        + f'''  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}" />
  <link rel="canonical" href="{SITE}{canonical}" />
  <meta property="og:title" content="{escape(og_title)}" />
  <meta property="og:description" content="{escape(description)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{SITE}{canonical}" />
  <script type="application/ld+json">{json.dumps(breadcrumb_ld, ensure_ascii=False)}</script>
'''
        + CSS_BASE + CSS + BODY_START + body + '\n' + BANNER + TAIL)

def breadcrumb_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items)]}

# Bandeau d'inscription, identique à celui de la page d'accueil
BANNER = '''<section class="cta-section" id="inscription">
  <div class="container">
    <h2>Commencez votre préparation aujourd'hui</h2>
    <p>Rejoignez plus de 1 200 candidats qui se préparent intelligemment au CRPE. Accès immédiat, sans engagement.</p>
    <div class="cta-form">
      <button type="button" class="btn-white cta-commencer" onclick="openAuth('register')">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        Commencer gratuitement
      </button>
    </div>
    <p class="cta-note">Essai gratuit · 359 € TTC à l'issue de l'essai · Sans carte bancaire · Annulable à tout moment</p>
  </div>
</section>

'''

UPDATED = f'<p class="updated">Dernière mise à jour : 11 octobre 2026 · Données : résultats du CRPE, session {SESSION}</p>'

# ── Page académie ────────────────────────────────────────────────────────────
def page_academie(a):
    nom, s = a['nom'], a['slug']
    sel = SELECTIVITE[s]
    compare = 'supérieur' if a['taux'] > TAUX_NATIONAL else 'inférieur'
    remarques = []
    if a['admis'] < a['postes']:
        remarques.append(f"<li><strong>Tous les postes n'ont pas été pourvus :</strong> {fint(a['admis'])} admis pour {fint(a['postes'])} postes offerts, soit {fint(a['postes'] - a['admis'])} postes restés vacants.</li>")
    if a['inscritsLC'] > 0:
        remarques.append(f"<li><strong>Liste complémentaire :</strong> {fint(a['inscritsLC'])} candidat{'s' if a['inscritsLC'] > 1 else ''} {'ont été inscrits' if a['inscritsLC'] > 1 else 'a été inscrit'} sur la liste complémentaire. Ces candidats peuvent être appelés si des admis renoncent à leur poste.</li>")
    else:
        remarques.append("<li><strong>Liste complémentaire :</strong> aucun candidat n'a été inscrit sur la liste complémentaire.</li>")

    funnel = ''.join(
        f'<div class="funnel-row{" light" if i < 2 else ""}"><span class="funnel-label">{lab}</span><div class="funnel-track"><div class="funnel-bar" style="width:{max(v / a["inscrits"] * 100, 1):.1f}%"></div><span class="funnel-val">{fint(v)}</span></div></div>'
        for i, (lab, v) in enumerate([('Inscrits', a['inscrits']), ('Présents', a['presents']), ('Admissibles', a['admissibles']), ('Admis', a['admis'])]))

    voisins = ''.join(
        f'''<a class="card" href="{url(v)}"><h3>Académie {escape(de(v['nom']))}</h3>{sel_badge(v)}<p>{fint(v['postes'])} postes · {fpct(v['taux'])} de réussite</p></a>'''
        for v in (BY_SLUG[x] for x in a['voisins']))

    body = f'''<div class="acad-wrap">

  <nav class="breadcrumb" aria-label="Fil d'Ariane">
    <a href="/">Accueil</a><span>›</span><a href="{HUB_URL}">CRPE par académie</a><span>›</span><span aria-current="page">Académie {escape(de(nom))}</span>
  </nav>

  {sel_badge(a)}
  <h1>CRPE {escape(nom)} : résultats {SESSION} de l'académie {escape(de(nom))}</h1>
  <p class="lead">Voici les résultats du concours CRPE {SESSION} dans l'académie {escape(de(nom))}. Lors de cette session, l'académie {escape(de(nom))} offrait <strong>{fint(a['postes'])} postes</strong>. Sur {fint(a['inscrits'])} inscrits, {fint(a['presents'])} candidats se sont présentés aux épreuves, {fint(a['admissibles'])} ont été admissibles et <strong>{fint(a['admis'])} ont été admis</strong>, soit un taux de réussite de <strong>{fpct(a['taux'])}</strong>, {compare} à la moyenne nationale ({fpct(TAUX_NATIONAL)}).</p>

  <section class="kpis" aria-label="Chiffres clés">
    <div class="kpi"><span class="kpi-value">{fint(a['postes'])}</span><span class="kpi-label">postes offerts</span></div>
    <div class="kpi"><span class="kpi-value">{fint(a['inscrits'])}</span><span class="kpi-label">inscrits</span></div>
    <div class="kpi"><span class="kpi-value">{fint(a['presents'])}</span><span class="kpi-label">présents</span></div>
    <div class="kpi"><span class="kpi-value">{fint(a['admissibles'])}</span><span class="kpi-label">admissibles</span></div>
    <div class="kpi"><span class="kpi-value">{fint(a['admis'])}</span><span class="kpi-label">admis</span></div>
    <div class="kpi kpi-accent"><span class="kpi-value">{fpct(a['taux'])}</span><span class="kpi-label">taux de réussite (admis / présents)</span></div>
    <div class="kpi"><span class="kpi-value">{fint(a['inscritsLC'])}</span><span class="kpi-label">inscrits sur liste complémentaire</span></div>
  </section>

  <h2>Inscrits, résultats d'admissibilité et admis au CRPE</h2>
  <p>Toutes les personnes inscrites ne se présentent pas le jour des épreuves. Dans l'académie {escape(de(nom))}, <strong>{fpct(a['presents'] / a['inscrits'])}</strong> des inscrits étaient présents. Parmi les présents, <strong>{fpct(a['tauxAdmissibilite'])}</strong> ont été admissibles (moyenne nationale : {fpct(TAUX_ADMISSIBILITE_NATIONAL)}), et {fpct(a['taux'])} ont finalement été admis.</p>
  <div class="funnel">{funnel}</div>
  <ul>
    <li><strong>Candidats présents par poste :</strong> {fdec(a['presentsParPoste'])} présents pour 1 poste.</li>
    {''.join(remarques)}
  </ul>

  <h2>Taux de réussite CRPE : les classements de l'académie {escape(de(nom))}</h2>
  <p>Comment l'académie {escape(de(nom))} se situe-t-elle par rapport aux {N - 1} autres académies ?</p>
  <div class="rank-grid">
    <div class="card"><h3>Nombre de postes</h3><div class="rank-big">{rang(RANK_POSTES[s])} <small>sur {N}</small></div><p>{fint(a['postes'])} postes offerts.</p></div>
    <div class="card"><h3>Taux d'admissibilité</h3><div class="rank-big">{rang(RANK_ADMISSIBILITE[s])} <small>sur {N}</small></div><p>{fpct(a['tauxAdmissibilite'])} des présents admissibles.</p></div>
    <div class="card"><h3>Taux de réussite</h3><div class="rank-big">{rang(RANK_REUSSITE[s])} <small>sur {N}</small></div><p>{fpct(a['taux'])} des présents admis.</p></div>
  </div>
  <p style="font-size:14px;color:var(--gray-500);margin-top:10px;">1re = le plus de postes, ou le taux le plus élevé.</p>

  <h2>Sélectivité : {SEL_LABEL[sel].lower()}</h2>
  <div class="callout">Avec un taux de réussite de <strong>{fpct(a['taux'])}</strong>, l'académie {escape(de(nom))} fait partie des académies <strong>{SEL_LABEL[sel].lower()}s</strong> du CRPE.</div>
  {METHODE}

  <h2>Situer l'académie {escape(de(nom))} sur la carte</h2>
  {carte(a)}

  <h2>Académies voisines</h2>
  <p>Vous hésitez encore ? Comparez avec les académies proches :</p>
  <div class="voisins-grid">{voisins}</div>
  <a class="back-hub" href="{HUB_URL}">← Voir toutes les académies</a>

  {UPDATED}


</div>'''
    title = f'CRPE {nom} {SESSION} : résultats, admis et taux de réussite | PassCRPE'
    desc = (f"Résultats du CRPE {SESSION} dans l'académie {de(nom)} : {fint(a['postes'])} postes, {fint(a['inscrits'])} inscrits, "
            f"{fint(a['admis'])} admis, {fpct(a['taux'])} de réussite. Classements, sélectivité et académies voisines.").replace(' ', ' ').replace(' ', ' ')
    return page(title, desc, url(a),
                breadcrumb_ld([('Accueil', '/'), ('CRPE par académie', HUB_URL), (f'Académie {de(nom)}', url(a))]),
                body, f"CRPE {nom} : résultats {SESSION} de l'académie {de(nom)}")

# ── Page hub ─────────────────────────────────────────────────────────────────
def page_hub():
    regions = {}
    for a in ACADS:
        regions.setdefault(a['region'], []).append(a)
    region_cards = ''.join(
        f'<div class="card"><h3>{escape(r)}</h3><ul>' + ''.join(
            f'<li><a href="{url(a)}">{escape(a["nom"])}</a><span class="dot dot-{SELECTIVITE[a["slug"]]}" title="{SEL_LABEL[SELECTIVITE[a["slug"]]]}"></span></li>'
            for a in sorted(regions[r], key=lambda a: a['nom'])) + '</ul></div>'
        for r in sorted(regions, key=lambda r: r.replace('Î', 'I')))
    rows = ''.join(f'''
        <tr>
          <td data-v="{escape(a['nom'])}"><a href="{url(a)}">{escape(a['nom'])}</a></td>
          <td class="num" data-v="{a['postes']}">{fint(a['postes'])}</td>
          <td class="num" data-v="{a['inscrits']}">{fint(a['inscrits'])}</td>
          <td class="num" data-v="{a['presents']}">{fint(a['presents'])}</td>
          <td class="num" data-v="{a['admissibles']}">{fint(a['admissibles'])}</td>
          <td class="num" data-v="{a['admis']}">{fint(a['admis'])}</td>
          <td class="num" data-v="{a['taux']:.6f}">{fpct(a['taux'])}</td>
          <td data-v="{['tres', 'moyen', 'peu'].index(SELECTIVITE[a['slug']])}">{sel_badge(a)}</td>
        </tr>''' for a in sorted(ACADS, key=lambda a: a['nom']))

    body = f'''<div class="acad-wrap">

  <nav class="breadcrumb" aria-label="Fil d'Ariane">
    <a href="/">Accueil</a><span>›</span><span aria-current="page">CRPE par académie</span>
  </nav>

  <h1>Résultats du CRPE {SESSION} par académie : inscrits, admis et taux de réussite</h1>
  <p class="lead">On ne passe pas le concours du CRPE « en France », mais dans <strong>une académie</strong>. C'est elle qui organise le concours et, si vous êtes reçu, vous affecte dans l'une de ses écoles. Choisir son académie, c'est donc choisir à la fois ses chances de réussite et l'endroit où l'on va enseigner. Voici les résultats du CRPE {SESSION} académie par académie : inscrits, résultats d'admissibilité, admis et taux de réussite. <strong>Cliquez sur une académie de la carte</strong> pour découvrir ses résultats détaillés.</p>

  <section class="kpis" aria-label="Chiffres nationaux">
    <div class="kpi"><span class="kpi-value">{fint(TOT['postes'])}</span><span class="kpi-label">postes offerts</span></div>
    <div class="kpi"><span class="kpi-value">{fint(TOT['inscrits'])}</span><span class="kpi-label">inscrits</span></div>
    <div class="kpi"><span class="kpi-value">{fint(TOT['presents'])}</span><span class="kpi-label">présents</span></div>
    <div class="kpi"><span class="kpi-value">{fint(TOT['admis'])}</span><span class="kpi-label">admis</span></div>
    <div class="kpi kpi-accent"><span class="kpi-value">{fpct(TAUX_NATIONAL)}</span><span class="kpi-label">taux de réussite national (admis / présents)</span></div>
  </section>

  <h2>La carte des académies CRPE</h2>
  <p>Chaque repère représente une académie, coloré selon sa sélectivité. Cliquez dessus pour ouvrir la page de l'académie.</p>
  {carte()}

  <h2>Résultats CRPE {SESSION} : le tableau comparatif des {N} académies</h2>
  <p>Cliquez sur un en-tête de colonne pour trier le tableau, et sur le nom d'une académie pour voir sa page.</p>
  <div class="table-wrap">
    <table id="acadTable">
      <thead>
        <tr>
          <th><button type="button" data-col="0" data-type="text">Académie</button></th>
          <th class="num"><button type="button" data-col="1">Postes</button></th>
          <th class="num"><button type="button" data-col="2">Inscrits</button></th>
          <th class="num"><button type="button" data-col="3">Présents</button></th>
          <th class="num"><button type="button" data-col="4">Admissibles</button></th>
          <th class="num"><button type="button" data-col="5">Admis</button></th>
          <th class="num"><button type="button" data-col="6">Taux de réussite</button></th>
          <th><button type="button" data-col="7">Sélectivité</button></th>
        </tr>
      </thead>
      <tbody>{rows}
      </tbody>
    </table>
  </div>

  <h2>Taux de réussite CRPE : comment est calculée la sélectivité ?</h2>
  {METHODE}

  <h2>Les académies CRPE par région académique</h2>
  <p>Les académies sont regroupées en <strong>régions académiques</strong>. L'Île-de-France, par exemple, compte trois académies : Paris, Créteil et Versailles. Si vous hésitez entre deux académies proches de chez vous, comparez d'abord celles de votre région.</p>
  <div class="region-grid">{region_cards}</div>

  <h2>Comment choisir son académie pour le concours CRPE ?</h2>
  <ul>
    <li><strong>Vos chances de réussite :</strong> regardez le taux de réussite et le nombre de candidats présents par poste. Une académie avec beaucoup de postes et peu de candidats est en général plus accessible.</li>
    <li><strong>Votre lieu de vie :</strong> si vous êtes reçu, vous serez affecté dans une école de cette académie. Une académie plus accessible mais loin de chez vous implique un déménagement, et un coût de la vie parfois plus élevé.</li>
    <li><strong>Votre affectation probable :</strong> dans une grande académie, l'école où vous serez affecté peut être loin de la ville principale. Renseignez-vous sur les départements qui la composent.</li>
  </ul>

  <h3>Peut-on s'inscrire dans une académie où l'on n'habite pas ?</h3>
  <p>Oui. Vous choisissez librement l'académie dans laquelle vous passez le concours, sans condition de domicile. En revanche, vous ne pouvez vous inscrire que dans une seule académie par session pour un même concours.</p>

  <div class="related-section">
    <p class="related-label">Lire aussi</p>
    <div class="related-grid">
      <a href="/blog/crpe-2026-reforme-concours-externes" target="_blank" rel="noopener" class="related-card">
        <span class="related-tag">Le concours</span>
        <h4>CRPE 2026 : qu'est-ce qui change pour les concours externes ?</h4>
        <p>Master M2E rémunéré, Licence LPE, nouveau parcours : tout ce qui change à partir de 2026.</p>
        <span class="related-cta">Lire l'article →</span>
      </a>
      <a href="/blog/crpe-bac3-structure-premiere-epreuve-admissibilite" target="_blank" rel="noopener" class="related-card">
        <span class="related-tag">Le concours</span>
        <h4>CRPE externe Bac+3 2026 : structure de l'épreuve d'admissibilité</h4>
        <p>Durée, barème, parties français et mathématiques : la structure complète de la première épreuve.</p>
        <span class="related-cta">Lire l'article →</span>
      </a>
      <a href="/blog/salaire-professeur-des-ecoles-remuneration" target="_blank" rel="noopener" class="related-card">
        <span class="related-tag">Le métier</span>
        <h4>Combien peut réellement toucher un professeur des écoles en début de carrière ?</h4>
        <p>Grades, primes REP et REP+, pacte enseignant : le salaire net d'un débutant, tableau à l'appui.</p>
        <span class="related-cta">Lire l'article →</span>
      </a>
    </div>
  </div>

  {UPDATED}


</div>

<script>
  // Tri du tableau comparatif
  (function () {{
    const table = document.getElementById('acadTable');
    const tbody = table.tBodies[0];
    let col = 0, dir = 1;
    table.querySelectorAll('th button').forEach(btn => btn.addEventListener('click', () => {{
      const c = +btn.dataset.col, text = btn.dataset.type === 'text';
      if (c === col) dir = -dir; else {{ col = c; dir = text ? 1 : -1; }}
      const rows = [...tbody.rows].sort((a, b) => {{
        const x = a.cells[c].dataset.v, y = b.cells[c].dataset.v;
        return (text ? x.localeCompare(y, 'fr') : x - y) * dir;
      }});
      rows.forEach(r => tbody.appendChild(r));
      table.querySelectorAll('th button').forEach(b => {{
        const on = +b.dataset.col === col;
        b.dataset.arrow = on ? (dir === 1 ? '▲' : '▼') : '';
        b.parentElement.setAttribute('aria-sort', on ? (dir === 1 ? 'ascending' : 'descending') : 'none');
      }});
    }}));
  }})();
</script>'''
    return page(f'Résultats CRPE {SESSION} par académie : admis, inscrits et taux de réussite | PassCRPE',
                f"Résultats du concours CRPE {SESSION} par académie : carte de France et comparatif des {N} académies CRPE, avec postes, inscrits, admis, résultats d'admissibilité et taux de réussite.",
                HUB_URL, breadcrumb_ld([('Accueil', '/'), ('CRPE par académie', HUB_URL)]), body,
                f'Résultats du CRPE {SESSION} par académie : inscrits, admis et taux de réussite')

# ── Écriture ─────────────────────────────────────────────────────────────────
out_dir = os.path.join(ROOT, 'landing', 'academies')
os.makedirs(out_dir, exist_ok=True)
for a in ACADS:
    open(os.path.join(out_dir, a['slug'] + '.html'), 'w', encoding='utf-8').write(page_academie(a))
open(os.path.join(ROOT, 'landing', 'crpe-par-academie.html'), 'w', encoding='utf-8').write(page_hub())
print(f'{N} pages académie + page hub générées.')

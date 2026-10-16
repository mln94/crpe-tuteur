#!/usr/bin/env python3
"""Génère les pages « Rapports de jury du CRPE par académie », une par session : /rapports-jury-crpe/<année>.

Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Sorties : landing/rapports-jury-crpe-<année>.html
Usage   : python3 scripts/generate_rapports_jury.py
"""
import json
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'
SLUG = 'rapports-jury-crpe'

# (académie, concours, lien officiel). Les liens « docutheque » mènent à une page, les autres au PDF.
SESSIONS = [
    ('2026', [
        ('Bordeaux', 'Bac+5', 'https://www.ac-bordeaux.fr/media/81835/download'),
        ('Bordeaux', 'Bac+3', 'https://www.ac-bordeaux.fr/media/81901/download'),
        ('Créteil', 'Bac+5', 'https://siec.education.fr/candidats/docutheque/concours/50/rapports-du-jury-crpe-academie-de-creteil-session-2026'),
        ('Créteil', 'Bac+3', 'https://siec.education.fr/candidats/docutheque/concours/50/crpe-rapports-du-jury-academie-de-creteil-session-l3-2026'),
        ('Dijon', 'Bac+5', 'https://www.ac-dijon.fr/media/61058/download'),
        ('Guyane', 'Bac+3 et bac+5', 'https://www.ac-guyane.fr/media/31052/download'),
        ('Lille', 'Bac+5', 'https://www1.ac-lille.fr/media/32120/download'),
        ('Lille', 'Bac+3', 'https://www1.ac-lille.fr/media/32121/download'),
        ('Limoges', 'Bac+5', 'https://www.ac-limoges.fr/media/41976/download'),
        ('Limoges', 'Bac+3', 'https://www.ac-limoges.fr/media/41978/download'),
        ('Montpellier', 'Bac+5', 'https://www.ac-montpellier.fr/media/43279/download'),
        ('Montpellier', 'Bac+3', 'https://www.ac-montpellier.fr/media/43280/download'),
        ('Nantes', 'Bac+5', 'https://www.ac-nantes.fr/media/44054/download'),
        ('Nantes', 'Bac+3', 'https://www.ac-nantes.fr/media/44055/download'),
        ('Versailles', 'Bac+3', 'https://siec.education.fr/candidats/docutheque/concours/50/crpe-licence3-rapport-du-jury-academie-de-versailles-session-2026'),
    ]),
    ('2025', [
        ('Aix-Marseille', 'Rapport de la session', 'https://www.ac-aix-marseille.fr/media/39070/download'),
        ('Amiens', 'Rapport de la session', 'https://www.ac-amiens.fr/media/21609/download'),
        ('Bordeaux', 'Rapport de la session', 'https://www.ac-bordeaux.fr/media/74034/download'),
        ('Clermont-Ferrand', 'Rapport de la session', 'https://www.ac-clermont.fr/media/54624/download'),
        ('Corse', 'Rapport de la session', 'https://www.ac-corse.fr/media/27828/download'),
        ('Créteil', 'Rapport de la session', 'https://siec.education.fr/candidats/docutheque/rapport-du-jury-crpe-academie-de-creteil-session-2025'),
        ('Dijon', 'Rapport de la session', 'https://www.ac-dijon.fr/media/58299/download'),
        ('Grenoble', 'Rapport de la session', 'https://www1.ac-grenoble.fr/media/43439/download'),
        ('Lille', 'Rapport de la session', 'https://www1.ac-lille.fr/media/30452/download'),
        ('Limoges', 'Rapport de la session', 'https://www.ac-limoges.fr/media/27284/download'),
        ('Lyon', 'Rapport de la session', 'https://www.ac-lyon.fr/media/60789/download'),
        ('Martinique', 'Rapport de la session', 'https://www.ac-martinique.fr/media/24434/download'),
        ('Montpellier', 'Rapport de la session', 'https://www.ac-montpellier.fr/media/40858/download'),
        ('Nantes', 'Rapport de la session', 'https://www.ac-nantes.fr/media/37930/download'),
        ('Nice', 'Rapport de la session', 'https://www.ac-nice.fr/media/19693/download'),
        ('Normandie', 'Rapport de la session', 'https://www.ac-normandie.fr/media/44909/download'),
        ('Orléans-Tours', 'Rapport de la session', 'https://www.ac-orleans-tours.fr/media/32504/download'),
        ('Paris', 'Rapport de la session', 'https://siec.education.fr/candidats/docutheque/concours/50/rapport-du-jury-crpe-academie-de-paris-session-2025'),
        ('Polynésie française', 'Rapport de la session', 'https://www.ac-polynesie.pf/media/23255/download'),
        ('Rennes', 'Rapport de la session', 'https://www.toutatice.fr/portail/share/va1L0l?l=wNsQIf'),
        ('Toulouse', 'Rapport de la session', 'https://www.ac-toulouse.fr/media/82774/download'),
        ('Versailles', 'Premier concours interne', 'https://siec.education.fr/candidats/docutheque/concours/50/rapport-de-jury-1er-interne-academie-de-versailles-session-2025'),
        ('Versailles', 'Concours interne exceptionnel', 'https://siec.education.fr/candidats/docutheque/concours/50/rapport-de-jury-crpe-interne-exceptionnelle-academie-de-versailles-session-2025'),
    ]),
]

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
BODY_NAV = (BODY_START.replace(NAV_RES, '<button type="button" class="nav-dropdown-toggle active" ')
            .replace(NAV_BLOG, '<li><a href="/blog">Blog</a></li>'))

CSS = """
    /* RAPPORTS DE JURY */
    .page-wrap { max-width: 860px; margin: 0 auto; padding: 32px 20px 72px; font-size: 16px; line-height: 1.7; color: var(--gray-700); }
    .page-wrap h1 { font-size: clamp(28px, 4.5vw, 40px); font-weight: 900; color: var(--gray-900); line-height: 1.15; letter-spacing: -.5px; margin-bottom: 14px; }
    .page-wrap h2 { font-size: 23px; font-weight: 800; color: var(--gray-900); margin: 44px 0 12px; letter-spacing: -.2px; }
    .page-wrap p { margin-bottom: 14px; }
    .page-wrap strong { color: var(--gray-900); }
    .page-wrap a { color: var(--indigo-600); }
    .lead { font-size: 17px; }
    .breadcrumb { position: static; z-index: auto; background: none; backdrop-filter: none; -webkit-backdrop-filter: none; border: 0; display: flex; flex-wrap: wrap; gap: 8px; font-size: 13px; color: var(--gray-400); margin-bottom: 20px; }
    .breadcrumb a { color: var(--gray-500); text-decoration: none; font-weight: 600; }
    .breadcrumb a:hover { color: var(--indigo-600); }
    .breadcrumb [aria-current] { color: var(--gray-700); font-weight: 600; }
    .session-count { font-size: 14px; color: var(--gray-500); margin: -4px 0 14px; }
    .reports { width: 100%; border-collapse: collapse; font-size: 15px; border: 1px solid var(--gray-200); border-radius: 12px; overflow: hidden; }
    .reports th { text-align: left; font-size: 12px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; color: var(--gray-500); background: var(--gray-50); padding: 10px 14px; border-bottom: 1px solid var(--gray-200); }
    .reports td { padding: 11px 14px; border-bottom: 1px solid var(--gray-100); vertical-align: middle; }
    .reports tr:last-child td { border-bottom: 0; }
    .reports td.ac { font-weight: 700; color: var(--gray-900); }
    .reports td.dl { text-align: right; white-space: nowrap; }
    .dl-link { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 700; padding: 6px 12px; border-radius: 8px; background: var(--indigo-50); color: var(--indigo-700) !important; text-decoration: none; }
    .dl-link:hover { background: var(--indigo-100); }
    .dl-link svg { width: 14px; height: 14px; }
    .callout { background: var(--indigo-50); border: 1px solid var(--indigo-100); border-radius: 14px; padding: 18px 20px; margin: 22px 0; font-size: 15px; }
    .callout p:last-child { margin-bottom: 0; }
    .page-cta { margin-top: 48px; background: linear-gradient(135deg, var(--indigo-600) 0%, #818cf8 100%); border-radius: 20px; padding: 32px; text-align: center; color: #fff; }
    .page-cta h2 { color: #fff; margin: 0 0 10px; font-size: 22px; }
    .page-cta p { opacity: .9; margin-bottom: 20px; }
    .page-cta a { display: inline-block; background: #fff; color: var(--indigo-700); font-size: 14px; font-weight: 800; padding: 12px 26px; border-radius: 10px; text-decoration: none; }
    @media (max-width: 600px) {
      .reports { font-size: 14px; }
      .reports th, .reports td { padding: 9px 10px; }
      .reports .col-concours { display: none; }
      .reports td.ac small { display: block; font-weight: 500; color: var(--gray-500); }
    }
    @media (min-width: 601px) { .reports td.ac small { display: none; } }
"""

ICON_DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'
ICON_OPEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>'


def table(rows, annee):
    out = []
    for ac, concours, url in rows:
        pdf = '/download' in url
        label = 'Télécharger' if pdf else 'Consulter'
        titre = f'Rapport de jury CRPE {annee}, académie de {ac}, {concours.lower()}'
        out.append(
            f'      <tr><td class="ac">{escape(ac)}<small>{escape(concours)}</small></td>'
            f'<td class="col-concours">{escape(concours)}</td>'
            f'<td class="dl"><a class="dl-link" href="{escape(url)}" target="_blank" rel="noopener" title="{escape(titre)}">'
            f'{ICON_DL if pdf else ICON_OPEN}{label}</a></td></tr>')
    return ('    <table class="reports">\n'
            '      <thead><tr><th>Académie</th><th class="col-concours">Concours</th><th></th></tr></thead>\n'
            '      <tbody>\n' + '\n'.join(out) + '\n      </tbody>\n    </table>')


INTRO = {
    '2026': ("La session 2026 est la première à réunir deux concours externes : le nouveau concours de niveau "
             "<strong>bac+3</strong> et le concours de niveau <strong>bac+5</strong>. Certaines académies publient "
             "un rapport par concours, d'autres un rapport commun."),
    '2025': ("En 2025, le concours externe était ouvert au niveau <strong>bac+5</strong> (master). Les rapports "
             "couvrent aussi, le plus souvent, le second concours interne et le troisième concours."),
}


def page(annee, rows):
    title = f'Rapports de jury du CRPE {annee} par académie : téléchargement'
    desc = (f"Téléchargez les rapports de jury officiels du CRPE {annee}, académie par académie"
            + (" (concours bac+3 et bac+5)" if annee == '2026' else '') + ". Liens directs vers les sites des académies.")
    url = f'{SITE}/{SLUG}/{annee}'
    ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': f'Rapports de jury CRPE {annee}', 'item': url}]}
    nb = len({r[0] for r in rows})
    lien = 'style="font-weight:600;" target="_blank" rel="noopener"'
    body = f'''<main class="page-wrap">
  <nav class="breadcrumb" aria-label="Fil d'Ariane">
    <a href="/">Accueil</a><span>›</span><span aria-current="page">Rapports de jury CRPE {annee}</span>
  </nav>
  <h1>Rapports de jury du CRPE {annee} par académie</h1>
  <p class="lead">Chaque année, les jurys du CRPE publient un <strong>rapport de jury</strong> par académie : les correcteurs y expliquent ce qu'ils ont valorisé, ce qu'ils ont pénalisé et les erreurs qui reviennent d'une copie à l'autre. {INTRO[annee]}</p>

  <div class="callout">
    <p><strong>Envie d'aller à l'essentiel ?</strong> Nous avons lu ces rapports et résumé les conseils des jurys, épreuve par épreuve, dans notre article <a href="/blog/rapport-jury-crpe-{annee}-conseils" {lien}>Rapport de jury CRPE {annee} : les conseils des jurys</a>.</p>
  </div>

  <h2>Rapports de jury CRPE {annee}</h2>
  <p class="session-count">{len(rows)} rapports, {nb} académies</p>
{table(rows, annee)}

  <p style="margin-top:28px;font-size:14px;color:var(--gray-500);">Les liens mènent aux sites officiels des académies et du ministère : « Télécharger » ouvre directement le PDF, « Consulter » ouvre la page de l'académie où se trouve le rapport. D'autres rapports sont aussi rassemblés sur <a href="https://www.devenirenseignant.gouv.fr/les-sujets-des-epreuves-ecrites-et-rapports-des-jurys-des-concours-de-recrutement-de-professeurs-des-1163" target="_blank" rel="noopener">devenirenseignant.gouv.fr</a>.</p>

  <div class="page-cta">
    <h2>Entraînez-vous comme le jury l'attend</h2>
    <p>Répondez à 5 questions de français ou de mathématiques et recevez un rapport détaillé sur votre manière de répondre.</p>
    <a href="/outils/entraineur-crpe" target="_blank" rel="noopener">Essayer l'Entraîneur CRPE gratuit →</a>
  </div>
</main>
'''
    head = (HEAD_START
            + f'  <title>{escape(title)} | PassCRPE</title>\n'
            + f'  <meta name="description" content="{escape(desc)}" />\n'
            + f'  <link rel="canonical" href="{url}" />\n'
            + f'  <meta property="og:title" content="{escape(title)}" />\n'
            + f'  <meta property="og:description" content="{escape(desc)}" />\n'
            + '  <meta property="og:type" content="website" />\n'
            + f'  <meta property="og:url" content="{url}" />\n'
            + f'  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
            + CSS_BASE + CSS)
    return head + BODY_NAV + body + TAIL


for annee, rows in SESSIONS:
    out = f'landing/{SLUG}-{annee}.html'
    open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(page(annee, rows))
    print(out)

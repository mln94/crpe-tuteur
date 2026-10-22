#!/usr/bin/env python3
"""Génère les pages « Rapports de jury du CRPE par académie », une par session : /rapports-jury-crpe/<année>.

Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Sorties : landing/rapports-jury-crpe-<année>.html
Usage   : python3 scripts/generate_rapports_jury.py
"""
import json
import os
import unicodedata
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'
SLUG = 'rapports-jury-crpe'

# (académie, concours, lien officiel). Les académies absentes d'une session (liste : scripts/academies-data.json)
# y sont ajoutées en « Non disponible ». Les liens « /download » ou « .pdf » mènent au PDF, les autres à une page.
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
        ('Besançon', 'Rapport de la session', 'https://cloud-aca.ac-besancon.fr/public.php/dav/files/5RrMspZcfNmpocY/RAPPORTS%20DE%20JURY/Rapport%20du%20jury%20-%20Session%202025.pdf'),
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
        ('Reims', 'Rapport de la session', 'https://www.ac-reims.fr/media/43031/download'),
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
    .reports tr.na td { color: var(--gray-500); }
    .reports tr.na td.ac { color: var(--gray-700); }
    .na-label { display: inline-block; font-size: 13px; font-weight: 600; padding: 6px 12px; border-radius: 8px; background: var(--gray-100); color: var(--gray-500); }
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


def cle(ac):
    return unicodedata.normalize('NFD', ac).encode('ascii', 'ignore').decode().lower()


def table(rows, annee):
    out = []
    for ac, concours, url in sorted(rows, key=lambda r: cle(r[0])):
        if url is None:
            out.append(
                f'      <tr class="na"><td class="ac">{escape(ac)}<small>{escape(concours)}</small></td>'
                f'<td class="col-concours">{escape(concours)}</td>'
                f'<td class="dl"><span class="na-label">Non disponible</span></td></tr>')
            continue
        pdf = '/download' in url or url.lower().endswith('.pdf')
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
    dispo = [r for r in rows if r[2]]
    nb = len({r[0] for r in dispo})
    manquants = len({r[0] for r in rows if not r[2]})
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
  <p class="session-count">{len(dispo)} rapports, {nb} académies · {manquants} académies sans rapport en ligne pour l'instant</p>
{table(rows, annee)}

  <p style="margin-top:28px;font-size:14px;color:var(--gray-500);">Les liens mènent aux sites officiels des académies et du ministère : « Télécharger » ouvre directement le PDF, « Consulter » ouvre la page de l'académie où se trouve le rapport. « Non disponible » signifie qu'aucun rapport n'est publié en ligne pour l'instant : la liste sera complétée dès sa parution. D'autres rapports sont aussi rassemblés sur <a href="https://www.devenirenseignant.gouv.fr/les-sujets-des-epreuves-ecrites-et-rapports-des-jurys-des-concours-de-recrutement-de-professeurs-des-1163" target="_blank" rel="noopener">devenirenseignant.gouv.fr</a>.</p>

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


ACADEMIES = [a['nom'] for a in json.load(open(os.path.join(ROOT, 'scripts', 'academies-data.json'), encoding='utf-8'))['academies']]

for annee, rows in SESSIONS:
    presentes = {r[0] for r in rows}
    rows = rows + [(nom, 'Pas de rapport en ligne', None) for nom in ACADEMIES if nom not in presentes]
    out = f'landing/{SLUG}-{annee}.html'
    open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(page(annee, rows))
    print(out)


# ── Page « Rapports de jury par discipline » : /rapports-jury-crpe/disciplines ──────────────────────────
# Le contenu est extrait, sans réécriture, des articles du blog sur les rapports de jury (une session par article).
# Chaque discipline reçoit les sections ou les points de liste qui la concernent ; sans contenu : état vide.
import re

DISCIPLINES = [
    # (id, épreuve, libellé, icône)
    ('admissibilite-francais', 'admissibilite', 'Français', '✍️'),
    ('admissibilite-mathematiques', 'admissibilite', 'Mathématiques', '🔢'),
    ('admissibilite-histoire-geographie', 'admissibilite', 'Histoire-géographie', '🌍'),
    ('admissibilite-sciences-technologie', 'admissibilite', 'Sciences et technologie', '🔬'),
    ('admissibilite-emc', 'admissibilite', 'EMC (enseignement moral et civique)', '⚖️'),
    ('admissibilite-arts', 'admissibilite', 'Arts', '🎨'),
    ('admissibilite-langue-vivante', 'admissibilite', 'Langue vivante étrangère', '🌐'),
    ('admissibilite-langues-regionales', 'admissibilite', 'Langues régionales', '🗺️'),
    ('admission-francais', 'admission', 'Français', '✍️'),
    ('admission-mathematiques', 'admission', 'Mathématiques', '🔢'),
    ('admission-eps', 'admission', 'EPS', '🏃'),
    ('admission-entretien', 'admission', 'Entretien avec le jury', '🗣️'),
    ('admission-langue-regionale', 'admission', 'Langue régionale', '🗺️'),
]
EPREUVES = {'admissibilite': 'Admissibilité (écrits)', 'admission': 'Admission (oraux)'}


def sections_article(annee):
    """[(niveau, titre, html, h2 parent)] des sections h2/h3 de l'article de la session."""
    s = open(os.path.join(ROOT, 'landing', f'rapport-jury-crpe-{annee}-conseils.html'), encoding='utf-8').read()
    body = s[s.index('<div class="article-body">'):]
    ms = list(re.finditer(r'<(h2|h3)[^>]*>(.*?)</\1>', body))
    out, parent = [], ''
    for i, m in enumerate(ms):
        fin = ms[i + 1].start() if i + 1 < len(ms) else len(body)
        if m.group(1) == 'h2':
            parent = m.group(2)
        out.append((m.group(1), m.group(2), body[m.end():fin].strip(), parent))
    return out


def section(secs, titre, parent=None):
    r = [x for x in secs if x[1] == titre and (parent is None or parent in x[3])]
    assert len(r) == 1, (titre, parent, len(r))
    return r[0][2]


def items(html):
    """Points de liste : [(étiquette en gras ou '', html du point)]."""
    out = []
    for li in re.findall(r'<li>(.*?)</li>', html, re.S):
        m = re.match(r'\s*<strong>([^<]{1,60})</strong>', li)
        out.append((m.group(1).strip().rstrip('.') if m else '', li.strip()))
    return out


def liste(points):
    return '<ul>' + ''.join(f'<li>{h}</li>' for _, h in points) + '</ul>' if points else ''


def texte(h):
    return re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', h)).strip()


def garder(points, etiquettes=None, exclure=()):
    return [(l, h) for l, h in points if (etiquettes is None or l in etiquettes) and not any(l.startswith(e) or texte(h).startswith(e) for e in exclure)]


def est_eps(p):
    return 'EPS' in p[0] or texte(p[1]).startswith('En EPS')


def contenus():
    data = {}
    # ── Session 2026 : un concours bac+3 et un concours bac+5 ──
    s = sections_article('2026')
    B3, B5 = 'Concours bac+3', 'Concours bac+5'
    app3 = items(section(s, "Épreuve écrite d'application", 'bac+3'))
    app5 = items(section(s, "Épreuve écrite d'application", 'bac+5'))
    commun3 = ('Conseils communs à l\'épreuve d\'application', B3, liste(garder(app3, ['Gérez votre temps'])))
    commun5 = ('Conseils communs à l\'épreuve d\'application', B5, liste(garder(app5, ['Justifiez vos choix pédagogiques'])))
    expo = items(section(s, 'Premier oral : exposé de français ou de mathématiques'))
    lecon = items(section(s, 'Épreuve orale de leçon'))
    oral2 = items(section(s, 'Second oral : EPS et entretien'))
    entr5 = items(section(s, "Épreuve orale d'entretien"))
    data['2026'] = {
        'admissibilite-francais': [
            ('Étude de la langue', B3, section(s, 'Écrit de français : étude de la langue')),
            ('Lexique', B3, section(s, 'Écrit de français : lexique')),
            ('Réflexion argumentée', B3, section(s, 'Écrit de français : réflexion argumentée')),
            ('Écrit de français', B5, section(s, 'Écrit de français', 'bac+5'))],
        'admissibilite-mathematiques': [
            ('Écrit de mathématiques', B3, section(s, 'Écrit de mathématiques', 'bac+3')),
            ('Écrit de mathématiques', B5, section(s, 'Écrit de mathématiques', 'bac+5'))],
        'admissibilite-histoire-geographie': [
            ("Épreuve d'application : histoire et géographie", B3, liste(garder(app3, ['Histoire', 'Géographie']))),
            ("Épreuve d'application : histoire-géographie et EMC", B5, liste(garder(app5, ['Histoire-géographie et EMC']))), commun3, commun5],
        'admissibilite-sciences-technologie': [
            ("Épreuve d'application : sciences", B3, liste(garder(app3, ['Sciences']))),
            ("Épreuve d'application : sciences", B5, liste(garder(app5, ['Sciences']))), commun3, commun5],
        'admissibilite-emc': [
            ("Épreuve d'application : EMC", B3, liste(garder(app3, ['EMC']))),
            ("Épreuve d'application : histoire-géographie et EMC", B5, liste(garder(app5, ['Histoire-géographie et EMC']))), commun3, commun5],
        'admissibilite-arts': [
            ("Épreuve d'application : arts", B3, liste(garder(app3, ['Arts']))),
            ("Épreuve d'application : arts", B5, liste(garder(app5, ['Arts']))), commun3, commun5],
        'admissibilite-langue-vivante': [
            ("Épreuve d'application : langue vivante", B3, liste(garder(app3, ['Langue vivante']))), commun3],
        'admission-francais': [
            ('Premier oral : exposé de français', B3, liste(garder(expo, exclure=('En mathématiques',)))),
            ('Épreuve orale de leçon', B5, liste(garder(lecon, exclure=('En mathématiques',))))],
        'admission-mathematiques': [
            ('Premier oral : exposé de mathématiques', B3, liste(garder(expo, exclure=('En français',)))),
            ('Épreuve orale de leçon', B5, liste(garder(lecon)))],
        'admission-eps': [
            ("Second oral : partie EPS", B3, liste([p for p in oral2 if est_eps(p)])),
            ("Épreuve orale d'entretien : partie EPS", B5, liste(garder(entr5, ['En EPS'])))],
        'admission-entretien': [
            ('Second oral : entretien', B3, liste([p for p in oral2 if not est_eps(p)])),
            ("Épreuve orale d'entretien", B5, liste(garder(entr5, exclure=('En EPS',))))],
    }
    # ── Session 2025 : concours bac+5 (externe, interne, troisième concours) ──
    s = sections_article('2025')
    C = 'Concours 2025'
    appli = section(s, "Épreuve écrite d'application : les conseils du jury")
    lecon = items(section(s, "Épreuve orale de leçon : les conseils du jury"))
    commun_app = [("Épreuve d'application : conseils communs aux trois domaines", C, appli)]
    data['2025'] = {
        'admissibilite-francais': [
            ('Étude de la langue', C, section(s, 'Étude de la langue : précision et exhaustivité')),
            ('Lexique', C, section(s, 'Lexique : formation des mots et sens en contexte')),
            ('Réflexion et développement', C, section(s, 'Réflexion et développement : une vraie argumentation'))],
        'admissibilite-mathematiques': [
            ('Rédiger et justifier chaque étape', C, section(s, 'Rédiger et justifier chaque étape')),
            ('Les erreurs les plus fréquentes', C, section(s, 'Les erreurs les plus fréquentes'))],
        'admissibilite-histoire-geographie': commun_app,
        'admissibilite-sciences-technologie': commun_app,
        'admissibilite-emc': commun_app,
        'admissibilite-arts': commun_app,
        'admission-francais': [('Épreuve orale de leçon', C, liste(lecon))],
        'admission-mathematiques': [('Épreuve orale de leçon', C, liste(garder(lecon, exclure=('En français',))))],
        'admission-eps': [("Épreuve d'entretien : la partie EPS", C, section(s, 'La partie EPS'))],
        'admission-entretien': [("Épreuve d'entretien : motivation et mises en situation", C, section(s, 'La motivation et les mises en situation'))],
    }
    # Contrôle : aucun bloc vide
    for an, d in data.items():
        for k, blocs in d.items():
            for t, c, h in blocs:
                assert re.sub('<[^>]+>', '', h).strip(), (an, k, t)
    return data




# Analyses rédigées à partir des rapports de jury : scripts/rapports_jury/<discipline>-<session>.html.
# Elles remplacent, pour cette session, les extraits des articles du blog.
ANALYSES = os.path.join(ROOT, 'scripts', 'rapports_jury')
DOSSIER = 'rapports-jury-disciplines'          # landing/<DOSSIER>/<id>.html, servi sous /rapports-jury-crpe/disciplines/<id>
EPREUVE_COURT = {'admissibilite': 'écrit', 'admission': 'oral'}
SEO = {
    'admissibilite-francais': (
        'Rapport de jury CRPE français (écrit) 2026 et 2025 : analyse et conseils',
        "Ce que disent les jurys du CRPE sur l'écrit de français en 2026 (bac+3 et bac+5) et en 2025 : barème, erreurs "
        "fréquentes en grammaire, en lexique et en réflexion, et conseils pour s'y préparer.",
        "Rapport de jury CRPE : l'écrit de français",
        "Étude de la langue, lexique, réflexion : ce que les jurys ont valorisé, les erreurs qu'ils ont relevées académie par "
        "académie, et ce qu'il faut travailler pour la prochaine session."),
}


def analyse(id_, annee):
    f = os.path.join(ANALYSES, f'{id_}-{annee}.html')
    return open(f, encoding='utf-8').read() if os.path.exists(f) else None


def url_disc(id_):
    return f'/{SLUG}/disciplines/{id_}'


CSS_DISC = """
    /* RAPPORTS PAR DISCIPLINE */
    .rd-wrap { max-width: 980px; }
    .rd-epreuve { margin-top: 30px; }
    .rd-epreuve h2 { margin: 0 0 12px; font-size: 21px; }
    .rd-grille { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 10px; }
    .rd-disc { display: flex; align-items: center; gap: 10px; border: 1.5px solid var(--gray-200); background: #fff; border-radius: 14px; padding: 13px 14px; font-size: 14.5px; font-weight: 700; color: var(--gray-700) !important; text-decoration: none; transition: border-color .15s, box-shadow .15s, transform .15s; }
    a.rd-disc:hover { border-color: var(--indigo-600); transform: translateY(-1px); box-shadow: 0 4px 14px rgba(79,70,229,.12); }
    .rd-disc[aria-current="page"] { border-color: var(--indigo-600); background: var(--indigo-50); color: var(--indigo-700) !important; }
    .rd-disc .ic { font-size: 20px; line-height: 1; }
    .rd-disc .info { display: block; margin-top: 2px; font-size: 12px; font-weight: 600; color: var(--gray-400); }
    .rd-disc .info.ok { color: var(--indigo-600); }
    span.rd-disc { color: var(--gray-400) !important; background: var(--gray-50); }
    .rd-autres { margin: 22px 0 6px; }
    .rd-autres .rd-label { font-size: 12px; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--gray-500); margin-bottom: 8px; }
    .rd-chips { display: flex; flex-wrap: wrap; gap: 8px; }
    .rd-chips a { font-size: 13.5px; font-weight: 700; padding: 7px 12px; border-radius: 100px; border: 1.5px solid var(--gray-200); color: var(--gray-700); text-decoration: none; background: #fff; }
    .rd-chips a:hover { border-color: var(--indigo-600); color: var(--indigo-700); }
    .rd-chips a[aria-current="page"] { background: var(--indigo-50); border-color: var(--indigo-600); color: var(--indigo-700); }
    .rd-tabs { position: sticky; top: 74px; z-index: 5; display: flex; gap: 4px; background: var(--gray-100); border-radius: 12px; padding: 4px; width: max-content; max-width: 100%; margin: 26px 0 18px; }
    .rd-tabs button { border: 0; background: none; font-family: inherit; font-size: 14px; font-weight: 700; color: var(--gray-600); padding: 9px 18px; border-radius: 9px; cursor: pointer; }
    .rd-tabs button[aria-selected="true"] { background: #fff; color: var(--indigo-700); box-shadow: 0 1px 4px rgba(17,24,39,.12); }
    .rd-rapport { border: 1px solid var(--gray-200); border-radius: 20px; padding: 30px; background: #fff; }
    .rd-sur { font-size: 12px; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--indigo-600); }
    .rd-rapport > h2:first-of-type { margin-top: 6px; }
    .rd-source { font-size: 14px; color: var(--gray-500); margin-bottom: 18px !important; }
    .rd-bloc { border-top: 1px solid var(--gray-100); padding-top: 18px; margin-top: 18px; }
    .rd-bloc h3 { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; font-size: 18px; font-weight: 800; color: var(--gray-900); margin-bottom: 10px; }
    .rd-concours { font-size: 11.5px; font-weight: 800; padding: 3px 10px; border-radius: 100px; background: var(--indigo-50); color: var(--indigo-700); }
    .rd-rapport ul, .rd-rapport ol { margin: 0 0 14px 22px; }
    .rd-rapport li { margin-bottom: 8px; }
    .rd-rapport li ul { margin-top: 8px; }
    .rd-vide { text-align: center; padding: 36px 16px; }
    .rd-vide .ic { font-size: 40px; margin-bottom: 10px; }
    .rd-vide h2 { font-size: 21px; margin: 0 0 8px; }
    .rd-vide p { max-width: 520px; margin: 0 auto 16px; }
    .rd-btn { display: inline-block; font-size: 14px; font-weight: 700; padding: 10px 18px; border-radius: 10px; text-decoration: none; margin: 4px; border: 1.5px solid var(--indigo-600); color: var(--indigo-700) !important; background: #fff; cursor: pointer; font-family: inherit; }
    .rd-btn.plein { background: var(--indigo-600); color: #fff !important; }
    /* Analyse rédigée */
    .rj-intro { font-size: 16.5px; }
    .rd-rapport h2 { font-size: 23px; margin: 40px 0 12px; scroll-margin-top: 130px; }
    .rd-rapport h3 { font-size: 18.5px; font-weight: 800; color: var(--gray-900); margin: 28px 0 10px; }
    .rj-sommaire { background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: 14px; padding: 16px 20px; margin: 18px 0 8px; font-size: 15px; }
    .rj-sommaire p { font-weight: 800; color: var(--gray-900); margin-bottom: 6px; }
    .rj-sommaire ol { margin: 0 0 0 20px !important; }
    .rj-sommaire li { margin-bottom: 3px !important; }
    .rj-retenir { background: var(--indigo-50); border: 1px solid var(--indigo-100); border-radius: 16px; padding: 18px 22px 8px; margin: 22px 0; }
    .rj-retenir-titre { font-weight: 900; color: var(--indigo-700); font-size: 16px; margin-bottom: 8px !important; }
    .rj-table-wrap { overflow-x: auto; margin: 14px 0 16px; border: 1px solid var(--gray-200); border-radius: 12px; }
    .rj-table { width: 100%; border-collapse: collapse; font-size: 14.5px; line-height: 1.5; }
    .rj-table th, .rj-table td { padding: 9px 12px; border-bottom: 1px solid var(--gray-100); text-align: left; vertical-align: top; }
    .rj-table thead th { font-size: 12px; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; color: var(--gray-500); background: var(--gray-50); }
    .rj-table tbody th { font-weight: 700; color: var(--gray-900); white-space: nowrap; }
    .rj-table tbody th small { font-weight: 500; color: var(--gray-500); }
    .rj-table tr:last-child th, .rj-table tr:last-child td { border-bottom: 0; }
    .rj-table tr.rj-sep td { background: var(--gray-50); font-weight: 800; color: var(--indigo-700); font-size: 13px; }
    .rj-note { font-size: 13.5px; color: var(--gray-500); }
    .rj-action { background: #ecfdf5; border-left: 4px solid #10b981; border-radius: 0 12px 12px 0; padding: 12px 16px; margin: 14px 0; }
    .rj-action + .rj-action-liste { margin-top: -8px !important; background: #ecfdf5; border-left: 4px solid #10b981; border-radius: 0 0 12px 0; padding: 4px 16px 10px 38px; margin-left: 0 !important; }
    .rj-action:has(+ .rj-action-liste) { border-radius: 0 12px 0 0; margin-bottom: 0; padding-bottom: 4px; }
    .rj-plan li { margin-bottom: 10px; }
    @media (max-width: 600px) {
      .rd-rapport { padding: 20px 16px; border-radius: 16px; }
      .rd-grille { grid-template-columns: 1fr; }
      .rd-tabs { top: 70px; }
      .rd-rapport h2 { font-size: 21px; }
      .rj-table { font-size: 13.5px; }
      .rj-table tbody th { white-space: normal; }
    }
"""


def tete(title, desc, url, ld):
    return (HEAD_START
            + f'  <title>{escape(title)} | PassCRPE</title>\n'
            + f'  <meta name="description" content="{escape(desc)}" />\n'
            + f'  <link rel="canonical" href="{url}" />\n'
            + f'  <meta property="og:title" content="{escape(title)}" />\n'
            + f'  <meta property="og:description" content="{escape(desc)}" />\n'
            + '  <meta property="og:type" content="article" />\n'
            + f'  <meta property="og:url" content="{url}" />\n'
            + f'  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
            + CSS_BASE + CSS + CSS_DISC)


def fil(*etapes):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(etapes)]}


CTA = '''  <div class="page-cta">
    <h2>Vérifiez votre niveau dans chaque discipline</h2>
    <p>Le Quiz CRPE : un test de positionnement gratuit sur les 9 matières, puis plus de 9 000 questions corrigées et expliquées.</p>
    <a href="/quizcrpe">Faire le test gratuit →</a>
  </div>'''


def sessions_dispo(data, id_):
    return [a for a, _ in SESSIONS if analyse(id_, a) or data.get(a, {}).get(id_)]


def page_hub(data):
    url = f'{SITE}/{SLUG}/disciplines'
    title = 'Rapports de jury du CRPE par discipline : les conseils des jurys'
    desc = ("Choisissez une discipline du CRPE, à l'écrit (admissibilité) ou à l'oral (admission), et lisez ce que les jurys "
            "ont valorisé et pénalisé, session par session.")
    blocs = []
    for ep, nom in EPREUVES.items():
        cartes = []
        for id_, e, label, ic in DISCIPLINES:
            if e != ep:
                continue
            dispo = sessions_dispo(data, id_)
            if dispo:
                riche = any(analyse(id_, a) for a in dispo)
                info = f'<span class="info ok">Analyse détaillée</span>' if riche else f'<span class="info">Sessions {" et ".join(dispo)}</span>'
                cartes.append(f'      <a class="rd-disc" href="{url_disc(id_)}"><span class="ic" aria-hidden="true">{ic}</span><span class="t">{escape(label)}{info}</span></a>')
            else:
                cartes.append(f'      <span class="rd-disc"><span class="ic" aria-hidden="true">{ic}</span><span class="t">{escape(label)}<span class="info">À venir</span></span></span>')
        blocs.append(f'  <section class="rd-epreuve">\n    <h2>{nom}</h2>\n    <div class="rd-grille">\n' + '\n'.join(cartes) + '\n    </div>\n  </section>')
    body = f'''<main class="page-wrap rd-wrap">
  <nav class="breadcrumb" aria-label="Fil d'Ariane">
    <a href="/">Accueil</a><span>›</span><span>Rapports de jury</span><span>›</span><span aria-current="page">Analyse par discipline</span>
  </nav>
  <h1>Rapports de jury du CRPE par discipline</h1>
  <p class="lead">Choisissez une discipline : vous lisez les conseils des jurys, ce qu'ils ont valorisé et ce qu'ils ont pénalisé, tirés des rapports officiels des académies pour les sessions 2026 et 2025.</p>
{chr(10).join(blocs)}

  <p style="margin-top:26px;font-size:14px;color:var(--gray-500);">Les conseils proviennent des rapports de jury officiels publiés par les académies. Pour lire un rapport complet, rendez-vous sur <a href="/{SLUG}/2026">la page de téléchargement des rapports</a>.</p>

{CTA}
</main>
<script>
// Anciennes adresses ?discipline=… : redirection vers la page de la discipline
(function () {{
  var d = new URLSearchParams(location.search).get('discipline');
  if (d && /^[a-z-]+$/.test(d) && {json.dumps([i for i, *_ in DISCIPLINES if sessions_dispo(data, i)])}.indexOf(d) >= 0) location.replace('/{SLUG}/disciplines/' + d);
}})();
</script>
'''
    ld = fil(('Accueil', SITE + '/'), ('Rapports de jury par discipline', url))
    return tete(title, desc, url, ld) + BODY_NAV + body + TAIL


def sommaire(html):
    titres = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
    if len(titres) < 3:
        return ''
    return ('<nav class="rj-sommaire" aria-label="Sommaire"><p>Sommaire</p><ol>'
            + ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in titres) + '</ol></nav>')


def panneau(data, id_, label, ic, annee, actif, autres):
    entete = f'<div class="rd-sur">{EPREUVES[dict((d[0], d[1]) for d in DISCIPLINES)[id_]]} · Session {annee}</div>'
    riche = analyse(id_, annee)
    blocs = data.get(annee, {}).get(id_)
    if riche:
        corps = (entete + f'<h2>{escape(label)} : l\'analyse des rapports {annee}</h2>'
                 + '<p class="rd-source">Synthèse rédigée par PassCRPE à partir des rapports de jury officiels publiés par les académies.</p>'
                 + riche.replace('</p>', '</p>' + sommaire(riche), 1))
    elif blocs:
        corps = (entete + f'<h2>{escape(label)}</h2>'
                 + f'<p class="rd-source">Synthèse des rapports de jury officiels, extraite de notre article <a href="/blog/rapport-jury-crpe-{annee}-conseils">Rapport de jury CRPE {annee}</a>.</p>'
                 + ''.join(f'<section class="rd-bloc"><h3>{escape(t)} <span class="rd-concours">{escape(c)}</span></h3>{h}</section>' for t, c, h in blocs))
    else:
        bouton = ''.join(f'<button type="button" class="rd-btn plein" data-session="{a}">Voir la session {a}</button>' for a in autres)
        corps = (f'<div class="rd-vide"><div class="ic" aria-hidden="true">{ic}</div>{entete}<h2>{escape(label)} : rapport à venir</h2>'
                 f'<p>Nous n\'avons pas encore de synthèse des jurys pour cette discipline en {annee}. Elle sera ajoutée ici dès que possible.</p>'
                 f'{bouton}<a class="rd-btn" href="/{SLUG}/{annee}">Télécharger les rapports officiels {annee}</a></div>')
    return (f'  <article class="rd-rapport" role="tabpanel" id="session-{annee}" aria-labelledby="onglet-{annee}"'
            + ('' if actif else ' hidden') + f'>\n{corps}\n  </article>')


def page_discipline(data, id_, ep, label, ic):
    court = EPREUVE_COURT[ep]
    url = SITE + url_disc(id_)
    title, desc, h1, lead = SEO.get(id_, (
        f'Rapport de jury CRPE {label} ({court}) 2026 et 2025 : les conseils des jurys',
        f"Ce que les jurys du CRPE ont valorisé et pénalisé en {label.lower() if label[:3] != 'EMC' else label} à l'{court}, "
        "sessions 2026 et 2025, d'après les rapports officiels des académies.",
        f'Rapport de jury CRPE : {label} à l\'{court}',
        f"Les conseils des jurys pour l'épreuve d'{EPREUVES[ep].split(' ')[0].lower()}, tirés des rapports officiels des académies."))
    sessions = [a for a, _ in SESSIONS]
    dispo = sessions_dispo(data, id_)
    defaut = dispo[0]
    onglets = ''.join(f'<button type="button" role="tab" id="onglet-{a}" aria-controls="session-{a}" aria-selected="{str(a == defaut).lower()}" data-session="{a}">Session {a}</button>' for a in sessions)
    panneaux = '\n'.join(panneau(data, id_, label, ic, a, a == defaut, [x for x in dispo if x != a]) for a in sessions)
    chips = ''.join(f'<a href="{url_disc(i)}"' + (' aria-current="page"' if i == id_ else '') + f'>{escape(l)}</a>'
                    for i, e, l, _ in DISCIPLINES if e == ep and sessions_dispo(data, i))
    body = f'''<main class="page-wrap rd-wrap">
  <nav class="breadcrumb" aria-label="Fil d'Ariane">
    <a href="/">Accueil</a><span>›</span><a href="/{SLUG}/disciplines">Analyse par discipline</a><span>›</span><span aria-current="page">{escape(label)} ({court})</span>
  </nav>
  <h1>{escape(h1)}</h1>
  <p class="lead">{lead}</p>
  <div class="rd-autres"><div class="rd-label">{EPREUVES[ep]} : autres disciplines</div><div class="rd-chips">{chips}</div></div>

  <div class="rd-tabs" role="tablist" aria-label="Session">{onglets}</div>
{panneaux}

  <p style="margin-top:22px;font-size:14px;color:var(--gray-500);">Les rapports complets sont disponibles sur nos pages de téléchargement : <a href="/{SLUG}/2026">session 2026</a> et <a href="/{SLUG}/2025">session 2025</a>.</p>

{CTA}
</main>
<script>
(function () {{
  var tabs = document.querySelector('.rd-tabs');
  function montrer(s, defiler) {{
    var p = document.getElementById('session-' + s); if (!p) return;
    document.querySelectorAll('.rd-tabs [role="tab"]').forEach(function (b) {{ b.setAttribute('aria-selected', String(b.dataset.session === s)); }});
    document.querySelectorAll('.rd-rapport[role="tabpanel"]').forEach(function (x) {{ x.hidden = x !== p; }});
    history.replaceState(null, '', '#session-' + s);
    if (defiler && tabs.getBoundingClientRect().top < 0) tabs.scrollIntoView({{ block: 'start' }});
  }}
  document.addEventListener('click', function (e) {{
    var b = e.target.closest && e.target.closest('[data-session]'); if (b) montrer(b.dataset.session, true);
  }});
  var h = location.hash, m = h.match(/^#session-(\\d{{4}})$/);
  if (m) montrer(m[1], false);
  else if (h) {{
    // Lien vers une section (#langue-2025…) : ouvrir l'onglet qui la contient
    var cible = document.getElementById(h.slice(1)), panneau = cible && cible.closest('[role="tabpanel"]');
    if (panneau && panneau.hidden) {{ montrer(panneau.id.replace('session-', ''), false); history.replaceState(null, '', h); cible.scrollIntoView(); }}
  }}
  document.querySelectorAll('.rj-sommaire a').forEach(function (a) {{
    a.addEventListener('click', function () {{ setTimeout(function () {{ history.replaceState(null, '', a.getAttribute('href')); }}, 0); }});
  }});
}})();
</script>
'''
    ld = fil(('Accueil', SITE + '/'), ('Rapports de jury par discipline', f'{SITE}/{SLUG}/disciplines'), (f'{label} ({court})', url))
    return tete(title, desc, url, ld) + BODY_NAV + body + TAIL


data = contenus()
out = f'landing/{SLUG}-disciplines.html'
open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(page_hub(data))
print(out)
os.makedirs(os.path.join(ROOT, 'landing', DOSSIER), exist_ok=True)
for id_, ep, label, ic in DISCIPLINES:
    if sessions_dispo(data, id_):
        out = f'landing/{DOSSIER}/{id_}.html'
        open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(page_discipline(data, id_, ep, label, ic))
        print(out)

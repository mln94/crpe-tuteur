#!/usr/bin/env python3
"""Génère les pages « Notions à maîtriser au CRPE » : une page d'ensemble et une page par discipline de l'admissibilité,
chacune avec un onglet « Concours bac+3 » et un onglet « Concours bac+5 ».

Gabarit  : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Contenus : scripts/notions_crpe/<discipline>-bac3.html et <discipline>-bac5.html (fragments HTML rédigés)
Sorties  : landing/notions-crpe.html (servie sous /notions-crpe)
           landing/notions-crpe/<discipline>.html (servies sous /notions-crpe/<discipline>)
Usage    : python3 scripts/generate_notions.py
"""
import json
import os
import re
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
CONTENUS = os.path.join(ROOT, 'scripts', 'notions_crpe')
SITE = 'https://www.passcrpe.fr'
SLUG = 'notions-crpe'
EXT = ' target="_blank" rel="noopener"'

# ── Sources officielles (citées dans les pages) ──────────────────────────────
SRC = {
    'prog_bac3': ('Le programme des épreuves des concours externes bac+3 (devenirenseignant.gouv.fr)',
                  'https://www.devenirenseignant.gouv.fr/le-programme-des-epreuves-des-concours-externes-bac3-de-recrutement-de-professeurs-des-ecoles-1382'),
    'prog_bac5': ('Programmes des concours de recrutement de professeurs des écoles, bac+5 (devenirenseignant.gouv.fr)',
                  'https://www.devenirenseignant.gouv.fr/programmes-des-concours-de-recrutement-de-professeurs-des-ecoles-1160'),
    'ep_bac3': ('Les épreuves du concours externe bac+3 (devenirenseignant.gouv.fr)',
                'https://www.devenirenseignant.gouv.fr/les-epreuves-du-concours-externe-bac3-de-recrutement-de-professeurs-des-ecoles-1380'),
    'ep_bac5': ('Les épreuves du concours externe bac+5 (devenirenseignant.gouv.fr)',
                'https://www.devenirenseignant.gouv.fr/les-epreuves-du-concours-externe-bac-5-de-recrutement-de-professeurs-des-ecoles-1009'),
    'bo_fr_maths_c4': ('Programmes de français et de mathématiques du cycle 4, arrêté du 18 février 2026 (BO n°10 du 5 mars 2026)',
                       'https://www.education.gouv.fr/bo/2026/Hebdo10/MENE2602912A'),
    'c4_2020': ('Programme du cycle 4 en vigueur à la rentrée 2020 (BOEN n°31 du 30 juillet 2020), programmes sur Éduscol',
                'https://eduscol.education.fr/74/j-enseigne'),
    'bo_emc': ("Programme d'enseignement moral et civique, arrêté du 29 mai 2024 (BO n°24 du 13 juin 2024)",
               'https://www.education.gouv.fr/bo/2024/Hebdo24/MENE2413934A'),
    'bo_hg_c3': ("Programme d'histoire-géographie du cycle 3 (BO n°22 du 28 mai 2026)",
                 'https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A'),
    'bo_lycee_fr': ('Programmes de français de seconde et de première, « L\'étude de la langue » (BOEN spécial n°1 du 22 janvier 2019)',
                    'https://www.education.gouv.fr/pid285/bulletin_officiel.html?pid_bo=38502'),
    'bo_maths_2nde': ('Programme de mathématiques de seconde, partie « Nombres et calculs, algèbre » (BOEN n°14 du 2 avril 2026)',
                      'https://www.education.gouv.fr/bo/2026/Hebdo14/MENE2602914A'),
    'eduscol': ('Programmes des cycles 1 à 4 (Éduscol)', 'https://eduscol.education.fr/74/j-enseigne'),
    'socle': ('Le socle commun de connaissances, de compétences et de culture (Éduscol)',
              'https://eduscol.education.fr/139/le-socle-commun-de-connaissances-de-competences-et-de-culture'),
    'sujets': ('Sujets des épreuves écrites et rapports des jurys du CRPE (devenirenseignant.gouv.fr)',
               'https://www.devenirenseignant.gouv.fr/les-sujets-des-epreuves-ecrites-et-rapports-des-jurys-des-crpe-1163'),
}

# ── Épreuves d'admissibilité ─────────────────────────────────────────────────
EP_BAC3_1 = {
    'nom': "Première épreuve écrite d'admissibilité : français et mathématiques",
    'duree': '4 heures', 'coef': '5',
    'note': "Sur 20 : partie français sur 10, partie mathématiques sur 10. Une note égale ou inférieure à 2,5 sur 10 à l'une des deux parties est éliminatoire.",
    'src': 'ep_bac3',
}
EP_BAC3_2 = {
    'nom': "Seconde épreuve écrite d'admissibilité : histoire-géographie et EMC, sciences et technologie, arts, langue vivante",
    'duree': '4 heures', 'coef': '3',
    'note': "Sur 20. Le candidat traite <strong>trois domaines de son choix parmi les quatre</strong>. Une note globale égale ou inférieure à 5 est éliminatoire.",
    'src': 'ep_bac3',
}
EP_BAC5_FR = {
    'nom': 'Épreuve écrite disciplinaire de français', 'duree': '3 heures', 'coef': '1',
    'note': 'Sur 20. Une note égale ou inférieure à 5 est éliminatoire.', 'src': 'ep_bac5',
}
EP_BAC5_MA = dict(EP_BAC5_FR, nom='Épreuve écrite disciplinaire de mathématiques')
EP_BAC5_APP = {
    'nom': "Épreuve écrite d'application : sciences et technologie, histoire-géographie-EMC ou arts",
    'duree': '3 heures', 'coef': '1',
    'note': "Sur 20. Le candidat choisit <strong>un des trois domaines</strong> au début de l'épreuve. Une note égale ou inférieure à 5 est éliminatoire.",
    'src': 'ep_bac5',
}

# (id, libellé, icône, page d'analyse des rapports de jury, {concours: (épreuve, description, [sources])})
DISCIPLINES = [
    ('francais', 'Français', '✍️', 'admissibilite-francais', {
        'bac3': (EP_BAC3_1, "Partie français : un texte support de 500 mots au plus (roman, nouvelle, littérature d'idées, essai…), puis trois phases : étude de la langue, lexique et compréhension lexicale, réflexion menée dans un court développement structuré.",
                 ['prog_bac3', 'ep_bac3', 'bo_fr_maths_c4', 'c4_2020']),
        'bac5': (EP_BAC5_FR, "Un texte d'environ 400 à 600 mots, puis trois parties : étude de la langue (syntaxe, grammaire, orthographe), lexique et compréhension lexicale, réflexion menée dans un développement structuré.",
                 ['prog_bac5', 'ep_bac5', 'bo_fr_maths_c4', 'bo_lycee_fr', 'c4_2020', 'socle', 'eduscol']),
    }),
    ('mathematiques', 'Mathématiques', '🔢', 'admissibilite-mathematiques', {
        'bac3': (EP_BAC3_1, "Partie mathématiques : plusieurs exercices ou problèmes. Le jury évalue la connaissance des notions du programme et leur mobilisation, le raisonnement et l'expression écrite.",
                 ['prog_bac3', 'ep_bac3', 'bo_fr_maths_c4', 'c4_2020']),
        'bac5': (EP_BAC5_MA, "Au moins trois exercices indépendants, qui vérifient les connaissances du candidat et sa capacité à les mobiliser avec le recul nécessaire pour enseigner aux cycles 1 à 3.",
                 ['prog_bac5', 'ep_bac5', 'bo_fr_maths_c4', 'bo_maths_2nde', 'c4_2020', 'socle', 'eduscol']),
    }),
    ('histoire-geographie', 'Histoire-géographie', '🌍', 'admissibilite-histoire-geographie', {
        'bac3': (EP_BAC3_2, "Domaine « histoire-géographie et EMC » : repères chronologiques et spatiaux, connaissances fondamentales, réponses rédigées et argumentées, carte, croquis, schéma ou frise à compléter, souvent à partir de documents.",
                 ['prog_bac3', 'ep_bac3', 'c4_2020', 'bo_emc']),
        'bac5': (EP_BAC5_APP, "Domaine « histoire, géographie, EMC » : à partir d'un dossier (documents pédagogiques, travaux de recherche), concevoir ou analyser une séquence ou des séances de l'école primaire, avec des questions de connaissances. La commission nationale retient, pour chaque session, deux composantes sur les trois (histoire, géographie, EMC).",
                 ['prog_bac5', 'ep_bac5', 'bo_hg_c3', 'c4_2020', 'eduscol']),
    }),
    ('emc', 'Enseignement moral et civique', '⚖️', 'admissibilite-emc', {
        'bac3': (EP_BAC3_2, "L'EMC fait partie du domaine « histoire-géographie et EMC » : connaissances fondamentales et réponses argumentées, souvent à partir de documents.",
                 ['prog_bac3', 'ep_bac3', 'bo_emc']),
        'bac5': (EP_BAC5_APP, "L'EMC est l'une des trois composantes du domaine « histoire, géographie, EMC » de l'épreuve d'application ; la commission nationale en retient deux sur trois pour chaque session.",
                 ['prog_bac5', 'ep_bac5', 'bo_emc', 'eduscol']),
    }),
    ('sciences-technologie', 'Sciences et technologie', '🔬', 'admissibilite-sciences-technologie', {
        'bac3': (EP_BAC3_2, "Domaine « sciences et technologie » : questions de physique-chimie, de sciences de la vie et de la Terre et de technologie, souvent appuyées sur des documents et des données à exploiter. Le jury évalue les connaissances et les démarches scientifiques et technologiques.",
                 ['prog_bac3', 'ep_bac3', 'c4_2020']),
        'bac5': (EP_BAC5_APP, "Domaine « sciences et technologie » : à partir d'un dossier, concevoir ou analyser une séquence ou des séances de l'école primaire (cycles 1 à 3), avec des questions de connaissances scientifiques.",
                 ['prog_bac5', 'ep_bac5', 'c4_2020', 'eduscol']),
    }),
    ('arts', 'Arts', '🎨', 'admissibilite-arts', {
        'bac3': (EP_BAC3_2, "Domaine « arts » : arts plastiques, éducation musicale et histoire des arts. La commission nationale retient deux composantes sur trois pour chaque session. Questions à partir de documents variés : culture artistique et analyse de la rencontre avec les œuvres.",
                 ['prog_bac3', 'ep_bac3', 'c4_2020']),
        'bac5': (EP_BAC5_APP, "Domaine « arts » : deux composantes sur trois (éducation musicale, arts plastiques, histoire des arts), retenues par la commission nationale pour chaque session, chacune notée sur 10.",
                 ['prog_bac5', 'ep_bac5', 'eduscol']),
    }),
    ('langue-vivante', 'Langue vivante étrangère', '🌐', 'admissibilite-langue-vivante', {
        'bac3': (EP_BAC3_2, "Domaine « langue vivante » (allemand, anglais, espagnol ou italien, au choix) : questions de compréhension sur des documents ancrés dans la culture de la langue, puis production d'un texte d'environ 120 mots. Niveau B1 du CECRL.",
                 ['prog_bac3', 'ep_bac3', 'c4_2020']),
        'bac5': (None, None, ['ep_bac5', 'prog_bac5']),
    }),
]
CONCOURS = {
    'bac3': ('Concours bac+3', 'Concours externe bac+3 · session 2027'),
    'bac5': ('Concours bac+5', 'Concours externe bac+5 (transitoire) · session 2027'),
}

# ── Gabarit commun ───────────────────────────────────────────────────────────
tpl = open(TEMPLATE, encoding='utf-8').read()
HEAD_START = tpl[:tpl.index('  <title>')]
css_start = tpl.index('  <link rel="preconnect"')
css_end = tpl.index('  </style>', css_start)
CSS_BASE = tpl[css_start:css_end]
BODY_START = tpl[css_end:tpl.index('<div class="article-wrap">')]
TAIL = tpl[tpl.index('<footer>'):]

NAV_RES = '<button type="button" class="nav-dropdown-toggle" '
NAV_BLOG = '<li><a href="/blog" class="active">Blog</a></li>'
assert BODY_START.count(NAV_RES) == 1 and BODY_START.count(NAV_BLOG) == 1
BODY_NAV = (BODY_START.replace(NAV_RES, '<button type="button" class="nav-dropdown-toggle active" ')
            .replace(NAV_BLOG, '<li><a href="/blog">Blog</a></li>'))

CSS = """
    /* NOTIONS À MAÎTRISER */
    .page-wrap { max-width: 980px; margin: 0 auto; padding: 32px 20px 72px; font-size: 16px; line-height: 1.7; color: var(--gray-700); }
    .page-wrap h1 { font-size: clamp(28px, 4.5vw, 40px); font-weight: 900; color: var(--gray-900); line-height: 1.15; letter-spacing: -.5px; margin-bottom: 14px; }
    .page-wrap h2 { font-size: 23px; font-weight: 800; color: var(--gray-900); margin: 40px 0 12px; letter-spacing: -.2px; scroll-margin-top: 90px; }
    .page-wrap h3 { font-size: 18.5px; font-weight: 800; color: var(--gray-900); margin: 26px 0 10px; scroll-margin-top: 90px; }
    .page-wrap p { margin-bottom: 14px; }
    .page-wrap strong { color: var(--gray-900); }
    .page-wrap a { color: var(--indigo-600); }
    .page-wrap ul, .page-wrap ol { margin: 0 0 14px 22px; }
    .page-wrap li { margin-bottom: 6px; }
    .page-wrap li ul { margin-top: 6px; }
    .lead { font-size: 17px; }
    .breadcrumb { position: static; z-index: auto; background: none; backdrop-filter: none; -webkit-backdrop-filter: none; border: 0; display: flex; flex-wrap: wrap; gap: 8px; font-size: 13px; color: var(--gray-400); margin-bottom: 20px; }
    .breadcrumb a { color: var(--gray-500); text-decoration: none; font-weight: 600; }
    .breadcrumb a:hover { color: var(--indigo-600); }
    .breadcrumb [aria-current] { color: var(--gray-700); font-weight: 600; }
    .nt-grille { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; margin: 16px 0 8px; }
    .nt-disc { display: flex; gap: 12px; border: 1.5px solid var(--gray-200); background: #fff; border-radius: 16px; padding: 16px; text-decoration: none; color: var(--gray-700) !important; transition: border-color .15s, box-shadow .15s, transform .15s; }
    .nt-disc:hover { border-color: var(--indigo-600); transform: translateY(-1px); box-shadow: 0 4px 14px rgba(79,70,229,.12); }
    .nt-disc .ic { font-size: 24px; line-height: 1.2; }
    .nt-disc strong { display: block; font-size: 16px; margin-bottom: 4px; }
    .nt-disc .t { font-size: 13.5px; line-height: 1.5; }
    .nt-badges { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }
    .nt-badge { font-size: 11.5px; font-weight: 800; padding: 3px 9px; border-radius: 100px; background: var(--indigo-50); color: var(--indigo-700); }
    .nt-badge.off { background: var(--gray-100); color: var(--gray-500); }
    .nt-chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 20px 0 4px; }
    .nt-chips a { font-size: 13.5px; font-weight: 700; padding: 7px 12px; border-radius: 100px; border: 1.5px solid var(--gray-200); color: var(--gray-700); text-decoration: none; background: #fff; }
    .nt-chips a:hover { border-color: var(--indigo-600); color: var(--indigo-700); }
    .nt-chips a[aria-current="page"] { background: var(--indigo-50); border-color: var(--indigo-600); color: var(--indigo-700); }
    .nt-tabs { display: flex; gap: 4px; background: var(--gray-100); border-radius: 12px; padding: 4px; width: max-content; max-width: 100%; margin: 24px 0 18px; }
    .nt-tabs button { border: 0; background: none; font-family: inherit; font-size: 14px; font-weight: 700; color: var(--gray-600); padding: 9px 18px; border-radius: 9px; cursor: pointer; }
    .nt-tabs button[aria-selected="true"] { background: #fff; color: var(--indigo-700); box-shadow: 0 1px 4px rgba(17,24,39,.12); }
    .nt-panneau { border: 1px solid var(--gray-200); border-radius: 20px; padding: 30px; background: #fff; }
    .nt-sur { font-size: 12px; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--indigo-600); }
    .nt-panneau > h2:first-of-type { margin-top: 6px; }
    .nt-epreuve { background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: 16px; padding: 16px 20px 6px; margin: 16px 0 20px; font-size: 15px; }
    .nt-epreuve-titre { font-weight: 900; color: var(--gray-900); margin-bottom: 8px !important; }
    .nt-faits { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 10px; }
    .nt-fait { font-size: 13px; font-weight: 700; padding: 5px 11px; border-radius: 8px; background: #fff; border: 1px solid var(--gray-200); color: var(--gray-700); }
    .nt-ref { background: var(--indigo-50); border: 1px solid var(--indigo-100); border-radius: 16px; padding: 16px 20px 6px; margin: 20px 0; font-size: 15px; }
    .nt-ref-titre { font-weight: 900; color: var(--indigo-700); margin-bottom: 8px !important; }
    .nt-attention { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #f59e0b; border-radius: 0 14px 14px 0; padding: 14px 18px 4px; margin: 18px 0; font-size: 15px; }
    .nt-niveaux { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 12px 0 16px; }
    .nt-niveau { border: 1px solid var(--gray-200); border-top: 4px solid var(--indigo-600); border-radius: 14px; padding: 12px 14px 4px; font-size: 14.5px; line-height: 1.55; }
    .nt-niveau h4 { font-size: 14px; font-weight: 900; color: var(--indigo-700); margin: 0 0 6px; }
    .nt-niveau ul { margin: 0 0 8px 16px !important; }
    .nt-niveau li { margin-bottom: 4px !important; }
    .nt-table-wrap { overflow-x: auto; margin: 14px 0 16px; border: 1px solid var(--gray-200); border-radius: 12px; }
    .nt-table { width: 100%; border-collapse: collapse; font-size: 14.5px; line-height: 1.5; }
    .nt-table th, .nt-table td { padding: 9px 12px; border-bottom: 1px solid var(--gray-100); text-align: left; vertical-align: top; }
    .nt-table thead th { font-size: 12px; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; color: var(--gray-500); background: var(--gray-50); }
    .nt-table tbody th { font-weight: 700; color: var(--gray-900); }
    .nt-table tr:last-child th, .nt-table tr:last-child td { border-bottom: 0; }
    .nt-sommaire { position: static; z-index: auto; backdrop-filter: none; -webkit-backdrop-filter: none; background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: 14px; padding: 14px 20px; margin: 18px 0 8px; font-size: 15px; }
    .nt-sommaire p { font-weight: 800; color: var(--gray-900); margin-bottom: 6px; }
    .nt-sommaire ol { margin: 0 0 0 20px !important; }
    .nt-sommaire li { margin-bottom: 3px !important; }
    .nt-jury { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; margin: 26px 0 8px; padding: 16px 20px; border-radius: 16px; background: #ecfdf5; border: 1px solid #a7f3d0; text-decoration: none; color: var(--gray-700) !important; }
    .nt-jury:hover { border-color: #10b981; }
    .nt-jury span { flex: 1 1 300px; font-size: 15px; }
    .nt-jury b { flex: none; font-size: 14px; color: #047857; }
    .nt-sources { border-top: 1px solid var(--gray-200); margin-top: 26px; padding-top: 14px; font-size: 14px; }
    .nt-sources p { font-weight: 800; color: var(--gray-900); margin-bottom: 6px; }
    .nt-sources ul { margin-left: 18px; }
    .nt-vide { text-align: center; padding: 30px 16px; }
    .nt-vide .ic { font-size: 40px; margin-bottom: 10px; }
    .nt-vide h2 { margin: 6px 0 8px !important; }
    .nt-vide p { max-width: 560px; margin: 0 auto 14px; }
    .nt-btn { display: inline-block; font-size: 14px; font-weight: 700; padding: 10px 18px; border-radius: 10px; text-decoration: none; margin: 4px; border: 1.5px solid var(--indigo-600); color: #fff !important; background: var(--indigo-600); cursor: pointer; font-family: inherit; }
    .page-cta { margin-top: 48px; background: linear-gradient(135deg, var(--indigo-600) 0%, #818cf8 100%); border-radius: 20px; padding: 32px; text-align: center; color: #fff; }
    .page-cta h2 { color: #fff; margin: 0 0 10px; font-size: 22px; }
    .page-cta p { opacity: .9; margin-bottom: 20px; }
    .page-cta a { display: inline-block; background: #fff; color: var(--indigo-700) !important; font-size: 14px; font-weight: 800; padding: 12px 26px; border-radius: 10px; text-decoration: none; }
    @media (max-width: 760px) { .nt-niveaux { grid-template-columns: 1fr; } }
    @media (max-width: 600px) {
      .nt-panneau { padding: 20px 16px; border-radius: 16px; }
      .page-wrap h2 { font-size: 21px; }
      .nt-table { font-size: 13.5px; }
    }
"""

IMAGE_PARTAGE = ('  <meta property="og:image" content="https://www.passcrpe.fr/images/partage-rapports-jury.jpg" />\n'
                 '  <meta property="og:image:type" content="image/jpeg" />\n'
                 '  <meta property="og:image:width" content="1200" />\n'
                 '  <meta property="og:image:height" content="630" />\n'
                 '  <meta name="twitter:card" content="summary_large_image" />\n')

CTA = '''  <div class="page-cta">
    <h2>Vérifiez où vous en êtes sur ces notions</h2>
    <p>Le Quiz CRPE : un test de positionnement gratuit sur les 9 matières, puis plus de 9 000 questions corrigées et expliquées.</p>
    <a href="/quizcrpe">Faire le test gratuit →</a>
  </div>'''


def lien(cle):
    titre, url = SRC[cle]
    return f'<a href="{escape(url)}"{EXT}>{escape(titre)}</a>'


def tete(title, desc, url, ld):
    return (HEAD_START
            + f'  <title>{escape(title)} | PassCRPE</title>\n'
            + f'  <meta name="description" content="{escape(desc)}" />\n'
            + f'  <link rel="canonical" href="{url}" />\n'
            + f'  <meta property="og:title" content="{escape(title)}" />\n'
            + f'  <meta property="og:description" content="{escape(desc)}" />\n'
            + '  <meta property="og:type" content="article" />\n'
            + f'  <meta property="og:url" content="{url}" />\n'
            + IMAGE_PARTAGE
            + f'  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
            + CSS_BASE + CSS)


def fil(*etapes):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(etapes)]}


def contenu(id_, c):
    """Fragment rédigé ; les liens externes s'ouvrent dans un nouvel onglet."""
    f = os.path.join(CONTENUS, f'{id_}-{c}.html')
    if not os.path.exists(f):
        return None
    html = open(f, encoding='utf-8').read().strip()
    # <!--inclure nom--> : fragment commun aux deux concours ; @C@ y devient bac3 ou bac5 (identifiants uniques)
    html = re.sub(r'<!--inclure ([a-z0-9-]+)-->',
                  lambda m: open(os.path.join(CONTENUS, m.group(1) + '.html'), encoding='utf-8').read().strip(), html)
    html = html.replace('@C@', c)
    return re.sub(r'<a href="(https?://[^"]+)"(?! target)', r'<a href="\1"' + EXT, html)


def sommaire(html, c):
    titres = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
    if len(titres) < 3:
        return ''
    items = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in titres)
    return f'<nav class="nt-sommaire" aria-label="Sommaire ({CONCOURS[c][0]})"><p>Sommaire</p><ol>{items}</ol></nav>'


def bloc_epreuve(ep, desc):
    return (f'<div class="nt-epreuve"><p class="nt-epreuve-titre">L\'épreuve : {ep["nom"]}</p>'
            f'<div class="nt-faits"><span class="nt-fait">⏱ {ep["duree"]}</span><span class="nt-fait">Coefficient {ep["coef"]}</span></div>'
            f'<p>{ep["note"]}</p><p>{desc} (Source : <a href="{escape(SRC[ep["src"]][1])}"{EXT}>devenirenseignant.gouv.fr</a>)</p></div>')


def panneau(id_, label, ic, jury, c, spec, actif, autre):
    ep, desc, sources = spec
    entete = f'<div class="nt-sur">Admissibilité · {CONCOURS[c][1]}</div>'
    srcs = ('<div class="nt-sources"><p>Sources utilisées</p><ul>'
            + ''.join(f'<li>{lien(s)}</li>' for s in sources) + '</ul></div>')
    if ep is None:
        corps = (f'<div class="nt-vide"><div class="ic" aria-hidden="true">{ic}</div>{entete}'
                 f'<h2>Pas d\'écrit de {escape(label.lower())} au concours bac+5</h2>'
                 f'<p>Les épreuves d\'admissibilité du concours externe bac+5 sont le français, les mathématiques et une épreuve '
                 f'd\'application (sciences et technologie, histoire-géographie-EMC ou arts). La langue vivante n\'y figure pas : '
                 f'c\'est l\'un des quatre domaines de la seconde épreuve écrite du concours bac+3.</p>'
                 f'<button type="button" class="nt-btn" data-concours="{autre}">Voir les notions du concours bac+3</button></div>'
                 + srcs)
    else:
        html = contenu(id_, c) or '<p>Contenu en cours de rédaction.</p>'
        corps = (entete + f'<h2>{escape(label)} : les notions à maîtriser</h2>'
                 + bloc_epreuve(ep, desc) + sommaire(html, c) + html
                 + f'<a class="nt-jury" href="/rapports-jury-crpe/disciplines/{jury}"><span><strong>Ce que les jurys attendent sur ces notions.</strong> '
                   f'Notre analyse des rapports de jury officiels en {escape(label.lower() if id_ != "emc" else "EMC")} : '
                   f'ce qui a été valorisé, les erreurs les plus fréquentes.</span><b>Lire l\'analyse →</b></a>'
                 + srcs)
    return (f'  <article class="nt-panneau" role="tabpanel" id="{c}" aria-labelledby="onglet-{c}"'
            + ('' if actif else ' hidden') + f'>\n{corps}\n  </article>')


SCRIPT_ONGLETS = '''<script>
(function () {
  var tabs = document.querySelector('.nt-tabs');
  function montrer(c, defiler) {
    var p = document.getElementById(c); if (!p || p.getAttribute('role') !== 'tabpanel') return;
    document.querySelectorAll('.nt-tabs [role="tab"]').forEach(function (b) { b.setAttribute('aria-selected', String(b.dataset.concours === c)); });
    document.querySelectorAll('.nt-panneau[role="tabpanel"]').forEach(function (x) { x.hidden = x !== p; });
    history.replaceState(null, '', '#' + c);
    if (defiler && tabs.getBoundingClientRect().top < 0) tabs.scrollIntoView({ block: 'start' });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-concours]'); if (b) montrer(b.dataset.concours, true);
  });
  var h = location.hash.slice(1);
  if (h === 'bac3' || h === 'bac5') montrer(h, false);
  else if (h) {
    // Lien vers une section (#bac5-lycee…) : ouvrir l'onglet qui la contient
    var cible = document.getElementById(h), p = cible && cible.closest('[role="tabpanel"]');
    if (p && p.hidden) { montrer(p.id, false); history.replaceState(null, '', '#' + h); cible.scrollIntoView(); }
  }
})();
</script>
'''


def url_disc(id_):
    return f'/{SLUG}/{id_}'


def page_discipline(id_, label, ic, jury, specs):
    url = SITE + url_disc(id_)
    title = f'CRPE : les notions à maîtriser en {label.lower() if id_ != "emc" else "EMC"} (bac+3 et bac+5)'
    desc = (f"Toutes les notions de {label.lower() if id_ != 'emc' else 'EMC'} au programme de l'admissibilité du CRPE, "
            "concours bac+3 et bac+5, d'après les programmes officiels, avec les liens vers les textes de référence.")
    h1 = f'{label} : les notions à maîtriser pour le CRPE'
    lead = (f"Ce qu'il faut savoir en {label.lower() if id_ != 'emc' else 'EMC'} pour l'écrit d'admissibilité, "
            "d'après les programmes officiels du concours. Choisissez votre concours : bac+3 (licence) ou bac+5 (master).")
    onglets = ''.join(f'<button type="button" role="tab" id="onglet-{c}" aria-controls="{c}" aria-selected="{str(c == "bac3").lower()}" data-concours="{c}">{CONCOURS[c][0]}</button>'
                      for c in CONCOURS)
    panneaux = '\n'.join(panneau(id_, label, ic, jury, c, specs[c], c == 'bac3', 'bac3' if c == 'bac5' else 'bac5') for c in CONCOURS)
    chips = ''.join(f'<a href="{url_disc(i)}"' + (' aria-current="page"' if i == id_ else '') + f'>{escape(l)}</a>'
                    for i, l, *_ in DISCIPLINES)
    body = f'''<main class="page-wrap">
  <nav class="breadcrumb" aria-label="Fil d'Ariane">
    <a href="/">Accueil</a><span>›</span><a href="/{SLUG}">Notions à maîtriser</a><span>›</span><span aria-current="page">{escape(label)}</span>
  </nav>
  <h1>{escape(h1)}</h1>
  <p class="lead">{lead}</p>
  <div class="nt-chips" aria-label="Autres disciplines">{chips}</div>

  <div class="nt-tabs" role="tablist" aria-label="Concours">{onglets}</div>
{panneaux}

  <p style="margin-top:22px;font-size:14px;color:var(--gray-500);">Cette page résume les programmes officiels ; en cas de doute, ce sont les textes officiels cités en source qui font foi. Retrouvez <a href="/{SLUG}">toutes les disciplines</a>.</p>

{CTA}
</main>
{SCRIPT_ONGLETS}'''
    ld = fil(('Accueil', SITE + '/'), ('Notions à maîtriser au CRPE', f'{SITE}/{SLUG}'), (label, url))
    return tete(title, desc, url, ld) + BODY_NAV + body + TAIL


RESUMES = {
    'francais': "Grammaire, conjugaison, orthographe, lexique, lecture et culture littéraire du cycle 4 ; en bac+5, l'étude de la langue du lycée en plus.",
    'mathematiques': "Nombres et calculs, géométrie, grandeurs, données et probabilités, proportionnalité et fonctions, algorithmique ; en bac+5, l'algèbre de seconde en plus.",
    'histoire-geographie': "Repères et thèmes d'histoire et de géographie du cycle 4 ; en bac+5, ceux du cycle 3 pour concevoir des séances.",
    'emc': "Valeurs et institutions de la République, droits et libertés, démocratie, laïcité, engagement : le programme 2024.",
    'sciences-technologie': "Physique-chimie, SVT et technologie du cycle 4, appuyées sur les sciences et technologie du cycle 3.",
    'arts': "Arts plastiques, éducation musicale, histoire des arts : les questionnements et les œuvres au programme de la session.",
    'langue-vivante': "Niveau B1 du CECRL, compréhension de documents et production écrite d'environ 120 mots (bac+3 uniquement).",
}


def page_hub():
    url = f'{SITE}/{SLUG}'
    title = 'CRPE : les notions à maîtriser dans chaque discipline (bac+3 et bac+5)'
    desc = ("Les notions au programme de l'admissibilité du CRPE, discipline par discipline, pour le concours bac+3 et le "
            "concours bac+5, d'après les programmes officiels, avec les liens vers les textes.")
    cartes = []
    for id_, label, ic, _, specs in DISCIPLINES:
        badges = ''.join(f'<span class="nt-badge{"" if specs[c][0] else " off"}">{"Bac+3" if c == "bac3" else "Bac+5"}{"" if specs[c][0] else " : pas d’écrit"}</span>'
                         for c in CONCOURS)
        cartes.append(f'    <a class="nt-disc" href="{url_disc(id_)}"><span class="ic" aria-hidden="true">{ic}</span>'
                      f'<span><strong>{escape(label)}</strong><span class="t">{RESUMES[id_]}</span><span class="nt-badges">{badges}</span></span></a>')
    body = f'''<main class="page-wrap">
  <nav class="breadcrumb" aria-label="Fil d'Ariane">
    <a href="/">Accueil</a><span>›</span><span>Ressources</span><span>›</span><span aria-current="page">Notions à maîtriser</span>
  </nav>
  <h1>CRPE : les notions à maîtriser pour l'admissibilité</h1>
  <p class="lead">Pour chaque discipline des écrits du concours, la liste des notions au programme, tirée des textes officiels. Chaque page distingue le <strong>concours bac+3</strong> (licence) et le <strong>concours bac+5</strong> (master), dont les épreuves et les programmes diffèrent.</p>

  <div class="nt-grille">
{chr(10).join(cartes)}
  </div>

  <h2 id="difference">Bac+3 ou bac+5 : ce qui change</h2>
  <div class="nt-table-wrap"><table class="nt-table">
    <thead><tr><th></th><th>Concours bac+3 (licence)</th><th>Concours bac+5 (master)</th></tr></thead>
    <tbody>
      <tr><th>Épreuves écrites</th><td>Deux épreuves de 4 h : français et mathématiques (coefficient 5) ; puis trois domaines au choix parmi quatre : histoire-géographie-EMC, sciences et technologie, arts, langue vivante (coefficient 3).</td><td>Trois épreuves de 3 h, coefficient 1 : français ; mathématiques ; épreuve d'application dans un domaine au choix (sciences et technologie, histoire-géographie-EMC ou arts).</td></tr>
      <tr><th>Niveau de référence</th><td>Les programmes du <strong>cycle 4</strong> (5e, 4e, 3e) en vigueur à la rentrée 2026 ; le cycle 3 en plus pour les sciences.</td><td>La maîtrise des programmes des <strong>cycles 1 à 4</strong> et du socle commun ; en plus, l'étude de la langue du lycée (français) et l'algèbre de seconde (mathématiques).</td></tr>
      <tr><th>Ce que l'on vous demande</th><td>Des connaissances disciplinaires : répondre juste, justifier, rédiger.</td><td>Des connaissances disciplinaires et, pour l'épreuve d'application, leur mise en œuvre dans une séquence pour l'école primaire (cycles 1 à 3).</td></tr>
    </tbody>
  </table></div>
  <p>Sources : {lien('prog_bac3')} ; {lien('prog_bac5')} ; {lien('ep_bac3')} ; {lien('ep_bac5')}.</p>

  <div class="nt-attention"><p><strong>Des programmes du collège en pleine transition.</strong> Les nouveaux programmes de français et de mathématiques du cycle 4 ({lien('bo_fr_maths_c4')}) s'appliquent en 5e depuis la rentrée 2026, puis en 4e en 2027 et en 3e en 2028. Le nouveau programme d'EMC ({lien('bo_emc')}) est appliqué à tous les niveaux à la rentrée 2026. Nos pages suivent ces textes et signalent, quand il le faut, ce qui vient de l'ancien programme.</p></div>

{CTA}
</main>
'''
    ld = fil(('Accueil', SITE + '/'), ('Notions à maîtriser au CRPE', url))
    return tete(title, desc, url, ld) + BODY_NAV + body + TAIL


if __name__ == '__main__':
    out = f'landing/{SLUG}.html'
    open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(page_hub())
    print(out)
    os.makedirs(os.path.join(ROOT, 'landing', SLUG), exist_ok=True)
    for id_, label, ic, jury, specs in DISCIPLINES:
        out = f'landing/{SLUG}/{id_}.html'
        open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(page_discipline(id_, label, ic, jury, specs))
        print(out)

#!/usr/bin/env python3
"""Génère la page de vente du Quiz CRPE : /quizz.

Gabarit : landing/index.html (styles, menu, pied de page, fenêtre de connexion/inscription et ses scripts)
Sortie  : landing/quizz.html
Usage   : python3 scripts/generate_quizz_vente.py

L'inscription est le même formulaire que sur la page d'accueil (compte Supabase + /api/klaviyo/signup).
Différences : window.SIGNUP_PARCOURS = 'quizcrpe', envoyé à Klaviyo dans la propriété « parcours », et
window.AFTER_SIGNUP_URL = '/quizzapp' : après l'inscription ou la connexion, la personne arrive sur le quiz.
Les comptes sont créés dans le projet Supabase « quizzcrpe » (window.SB_URL / SB_KEY), séparé du tuteur IA,
et le lien de l'e-mail de confirmation ramène sur /quizz pour se connecter (window.EMAIL_REDIRECT_URL).
À relancer après une modification du formulaire d'inscription, du menu ou du pied de page de l'accueil.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'landing', 'index.html')
OUT = os.path.join(ROOT, 'landing', 'quizz.html')
SITE = 'https://www.passcrpe.fr'
# Projet Supabase « quizzcrpe » : comptes des inscrits du quiz (clé publique anon)
QUIZ_SB_URL = 'https://uwsdfbmootumhsrufkmo.supabase.co'
QUIZ_SB_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV3c2RmYm1vb3R1bWhzcnVma21vIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTIyNDU1OTEsImV4cCI6MjEwNzgyMTU5MX0.W1uAsiBPR4mEoxjNBp308uNNhHt21dlXpGzPBHPXVuk'

PRIX_QUIZ = '49,99 €'
PRIX_PACK = '389 €'
PRIX_PACK_BARRE = '408,99 €'   # 359 € (tuteur IA) + 49,99 € (quiz)
ECONOMIE_PACK = '19,99 €'
QUESTIONS_PAR_MATIERE = 300

# (libellé, icône, exemples de thèmes)
MATIERES = [
    ('Français', '✍️', 'Grammaire, orthographe, lexique, littérature'),
    ('Mathématiques', '🔢', 'Nombres, calcul, géométrie, grandeurs, données'),
    ('Histoire-géographie', '🌍', 'Du Moyen Âge au monde actuel, territoires'),
    ('EMC', '⚖️', 'Valeurs de la République, droits, citoyenneté'),
    ('SVT', '🌱', 'La planète Terre, le vivant, le corps humain'),
    ('Physique-chimie', '⚗️', 'Matière, mouvement, énergie, signaux'),
    ('Technologie', '⚙️', 'Objets techniques, programmation, conception'),
    ('Arts', '🎨', 'Arts plastiques et éducation musicale'),
    ('Anglais', '🇬🇧', 'Grammaire, compréhension, culture anglophone'),
]

FAQ = [
    ("Sur quel programme les questions sont-elles construites ?",
     "Sur les programmes officiels du cycle 4 (5e, 4e, 3e), qui fixent le niveau de connaissances attendu à l'épreuve écrite "
     "du CRPE. Chaque question indique le thème, l'objectif du programme et la classe concernés."),
    ("Comment fonctionne la révision ?",
     "Vous répondez par séries de 20 questions et obtenez une note sur 20. Chaque notion est posée sous trois formulations "
     "différentes : trois bonnes réponses et elle est maîtrisée. En cas d'erreur, l'explication s'affiche et une question "
     "similaire revient plus tard, de façon espacée dans le temps."),
    ("Quels types de questions trouve-t-on ?",
     "Des QCM, des réponses numériques à saisir (calculs en mathématiques ou en physique-chimie) et des questions où l'on "
     "clique sur le bon mot d'une phrase, par exemple le complément d'objet ou le verbe conjugué."),
    ("Combien coûte le quiz ?",
     f"Le Quiz CRPE coûte {PRIX_QUIZ} TTC. Il existe aussi un pack avec le tuteur IA PassCRPE à {PRIX_PACK} TTC "
     f"au lieu de {PRIX_PACK_BARRE}."),
    ("Pourquoi créer un compte maintenant ?",
     "Votre compte PassCRPE vous permet d'être parmi les premiers à accéder au quiz et de profiter dès aujourd'hui de "
     "l'essai gratuit du tuteur IA en mathématiques et en français."),
]

CSS = """
    /* ── PAGE DE VENTE QUIZ ── */
    .qz-hero { padding: 72px 24px 80px; background: radial-gradient(ellipse at top, #fff7ed 0%, #fff 60%); }
    .qz-hero-inner { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1.1fr .9fr; gap: 48px; align-items: center; }
    .qz-hero .hero-badge { margin-bottom: 20px; }
    .qz-hero h1 { font-size: clamp(32px, 5vw, 52px); font-weight: 900; letter-spacing: -1.5px; line-height: 1.08; color: var(--gray-900); margin-bottom: 20px; }
    .qz-hero h1 em { font-style: normal; color: #ea580c; }
    .qz-hero .hero-sub { margin: 0 0 28px; text-align: left; max-width: none; }
    .qz-hero .hero-actions { justify-content: flex-start; }
    .qz-hero-price { margin-top: 16px; font-size: 14px; color: var(--gray-500); }
    .qz-hero-price strong { color: var(--gray-800); }
    .qz-stats { display: flex; gap: 28px; margin-top: 32px; flex-wrap: wrap; }
    .qz-stat strong { display: block; font-size: 28px; font-weight: 900; color: var(--gray-900); letter-spacing: -.5px; }
    .qz-stat span { font-size: 13px; color: var(--gray-500); }

    .qz-demo { background: #fff; border: 1.5px solid #fed7aa; border-radius: 22px; padding: 24px; box-shadow: 0 20px 50px rgba(234,88,12,.12); }
    .qz-demo-top { display: flex; justify-content: space-between; align-items: center; font-size: 12px; font-weight: 700; color: var(--gray-500); margin-bottom: 10px; }
    .qz-demo-bar { height: 6px; background: #ffedd5; border-radius: 6px; overflow: hidden; margin-bottom: 18px; }
    .qz-demo-bar span { display: block; height: 100%; width: 35%; background: #f97316; }
    .qz-demo-tag { display: inline-block; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 100px; background: #ffedd5; color: #9a3412; margin-bottom: 12px; }
    .qz-demo-q { font-size: 16px; font-weight: 700; color: var(--gray-900); line-height: 1.45; margin-bottom: 14px; }
    .qz-demo-choices { display: grid; gap: 8px; }
    .qz-demo-choice { padding: 11px 14px; border: 1.5px solid var(--gray-200); border-radius: 12px; font-size: 14px; color: var(--gray-700); }
    .qz-demo-choice.good { border-color: #22c55e; background: #f0fdf4; color: #166534; font-weight: 700; }
    .qz-demo-expl { margin-top: 14px; font-size: 13px; line-height: 1.55; color: var(--gray-600); background: var(--gray-50); border-radius: 12px; padding: 12px 14px; }
    .qz-demo-ref { margin-top: 10px; font-size: 11.5px; color: var(--gray-500); }

    .qz-matieres { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 40px; }
    .qz-matiere { display: flex; gap: 14px; align-items: flex-start; background: #fff; border: 1.5px solid var(--gray-200); border-radius: 18px; padding: 18px; }
    .qz-matiere-icon { width: 44px; height: 44px; border-radius: 12px; background: #fff7ed; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
    .qz-matiere h3 { font-size: 16px; font-weight: 800; color: var(--gray-900); }
    .qz-matiere p { font-size: 13px; color: var(--gray-500); line-height: 1.5; margin-top: 2px; }
    .qz-matiere .qz-count { font-size: 12px; font-weight: 700; color: #c2410c; margin-top: 6px; }

    .qz-features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 44px; }
    .qz-feature { background: #fff; border: 1.5px solid var(--gray-200); border-radius: 18px; padding: 24px; }
    .qz-feature-icon { font-size: 26px; margin-bottom: 12px; }
    .qz-feature h3 { font-size: 17px; font-weight: 800; color: var(--gray-900); margin-bottom: 8px; }
    .qz-feature p { font-size: 14px; color: var(--gray-600); line-height: 1.6; }

    .qz-prix { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 44px; max-width: 860px; margin-left: auto; margin-right: auto; }
    .qz-center { text-align: center; }
    .qz-center .section-sub { max-width: 680px; margin: 0 auto; }
    .faq-answer p { padding-right: 38px; }

    @media (max-width: 960px) {
      .qz-hero-inner { grid-template-columns: 1fr; gap: 36px; }
      .qz-matieres, .qz-features { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 640px) {
      .qz-hero { padding: 48px 16px 56px; }
      .qz-hero .hero-actions { justify-content: stretch; }
      .qz-matieres, .qz-features, .qz-prix { grid-template-columns: 1fr; }
      .qz-stats { gap: 20px; }
      section { padding-left: 16px; padding-right: 16px; }
    }
"""

ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'


def cut(s, start, end, include_end=False):
    i = s.index(start)
    j = s.index(end, i)
    return s[i:j + (len(end) if include_end else 0)]


def contenu():
    matieres = '\n'.join(
        f'''      <div class="qz-matiere fade-up">
        <div class="qz-matiere-icon">{ic}</div>
        <div>
          <h3>{nom}</h3>
          <p>{desc}</p>
          <p class="qz-count">{QUESTIONS_PAR_MATIERE} questions</p>
        </div>
      </div>''' for nom, ic, desc in MATIERES)
    faq = '\n'.join(
        f'''      <div class="faq-item">
        <button type="button" class="faq-question">{q}<span class="faq-icon">+</span></button>
        <div class="faq-answer"><p>{r}</p></div>
      </div>''' for q, r in FAQ)
    total = QUESTIONS_PAR_MATIERE * len(MATIERES)
    total_txt = f'{total:,}'.replace(',', ' ')
    return f'''
<!-- ═══════════════════════════════ HERO ═══════════════════════════════ -->
<header class="qz-hero">
  <div class="qz-hero-inner">
    <div>
      <div class="hero-badge"><span></span>Nouveau · Quiz CRPE</div>
      <h1>Arrivez au CRPE en <em>maîtrisant toutes les disciplines</em></h1>
      <p class="hero-sub">2 700 questions sur les 9 disciplines du concours, en séries de 20. À chaque série, une note sur 20, une explication pour chaque erreur, et des révisions qui reviennent au bon moment pour que vous n'oubliiez rien. Vous arrêtez de réviser au hasard.</p>
      <div class="hero-actions">
        <a href="#" class="btn-primary cta-commencer" onclick="openAuth(event,'register')">{ARROW}Vérifiez votre niveau gratuitement</a>
        <a href="#fonctionnement" class="btn-secondary">Voir comment ça marche</a>
      </div>
      <p class="qz-hero-price"><strong>{PRIX_QUIZ} TTC</strong> · ou <strong>{PRIX_PACK} TTC</strong> avec le tuteur IA PassCRPE</p>
      <div class="qz-stats">
        <div class="qz-stat"><strong>{total_txt}</strong><span>questions</span></div>
        <div class="qz-stat"><strong>{len(MATIERES)}</strong><span>disciplines</span></div>
        <div class="qz-stat"><strong>3</strong><span>types de questions</span></div>
      </div>
    </div>
    <div class="qz-demo" aria-label="Exemple de question du quiz">
      <div class="qz-demo-top"><span>Question 7 / 20</span><span>Physique-chimie · facile</span></div>
      <div class="qz-demo-bar"><span></span></div>
      <span class="qz-demo-tag">Énergie · Circuits électriques</span>
      <p class="qz-demo-q">Dans un montage en dérivation, si une lampe grille…</p>
      <div class="qz-demo-choices">
        <div class="qz-demo-choice">toutes les lampes s'éteignent</div>
        <div class="qz-demo-choice good">✓ les autres continuent de briller</div>
        <div class="qz-demo-choice">les autres brillent moins</div>
      </div>
      <p class="qz-demo-expl">Chaque lampe est sur sa propre boucle : c'est pourquoi les installations domestiques sont branchées en dérivation.</p>
      <p class="qz-demo-ref">Programme du cycle 4 · L'énergie et ses conversions</p>
    </div>
  </div>
</header>

<!-- ═══════════════════════════════ FONCTIONNEMENT ═══════════════════════════════ -->
<section id="fonctionnement" style="background:var(--gray-50)">
  <div class="container qz-center">
    <div class="section-eyebrow">Comment ça marche</div>
    <h2 class="section-title">Une méthode pensée pour retenir durablement</h2>
    <p class="section-sub">Pas de longues séances : quelques minutes par jour suffisent, et le quiz s'occupe de vous reposer les bonnes questions au bon moment.</p>
    <div class="steps">
      <div class="step"><div class="step-num">1</div><h3>Choisissez une discipline</h3><p>Français, maths, histoire-géographie, sciences, arts, anglais…</p></div>
      <div class="step"><div class="step-num">2</div><h3>Répondez à 20 questions</h3><p>QCM, calcul à saisir ou mot à cliquer, du plus facile au plus difficile.</p></div>
      <div class="step"><div class="step-num">3</div><h3>Obtenez votre note sur 20</h3><p>Avec l'explication de chaque erreur et le récapitulatif de la série.</p></div>
      <div class="step"><div class="step-num">4</div><h3>Révisez au bon moment</h3><p>Les notions à revoir reviennent plus tard, reformulées, jusqu'à être maîtrisées.</p></div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════ ATOUTS ═══════════════════════════════ -->
<section>
  <div class="container qz-center">
    <div class="section-eyebrow">Pourquoi le Quiz CRPE</div>
    <h2 class="section-title">Savoir où vous en êtes, notion par notion</h2>
    <div class="qz-features">
      <div class="qz-feature fade-up"><div class="qz-feature-icon">🎯</div><h3>3 formulations par notion</h3><p>Une notion n'est considérée comme maîtrisée qu'après trois bonnes réponses à trois questions différentes : fini les réponses apprises par cœur.</p></div>
      <div class="qz-feature fade-up"><div class="qz-feature-icon">🔁</div><h3>Révision espacée</h3><p>Une erreur ? L'explication s'affiche et une question similaire revient le lendemain. Une bonne réponse ? La suivante revient quelques jours plus tard.</p></div>
      <div class="qz-feature fade-up"><div class="qz-feature-icon">📚</div><h3>Rattaché au programme officiel</h3><p>Chaque question indique son thème, l'objectif du programme et la classe : vous savez précisément ce que vous révisez.</p></div>
      <div class="qz-feature fade-up"><div class="qz-feature-icon">📈</div><h3>Une progression par thème</h3><p>Des barres de progression par thème montrent ce qui est acquis et ce qui reste à consolider avant le concours.</p></div>
      <div class="qz-feature fade-up"><div class="qz-feature-icon">⏱️</div><h3>Des séries courtes</h3><p>Une série de 20 questions se fait en quelques minutes : idéal dans les transports ou entre deux révisions plus longues.</p></div>
      <div class="qz-feature fade-up"><div class="qz-feature-icon">🧮</div><h3>Pas seulement des QCM</h3><p>Calculs à saisir en mathématiques et en physique-chimie, mots à cliquer en grammaire : on vérifie vraiment le savoir-faire.</p></div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════ MATIÈRES ═══════════════════════════════ -->
<section id="matieres" style="background:var(--gray-50)">
  <div class="container qz-center">
    <div class="section-eyebrow">Les disciplines</div>
    <h2 class="section-title">{len(MATIERES)} disciplines, {QUESTIONS_PAR_MATIERE} questions chacune</h2>
    <p class="section-sub">Dans chaque discipline : 150 questions faciles, 100 intermédiaires et 50 difficiles.</p>
    <div class="qz-matieres" style="text-align:left">
{matieres}
    </div>
  </div>
</section>

<!-- ═══════════════════════════════ TARIF ═══════════════════════════════ -->
<section id="tarif">
  <div class="container qz-center">
    <div class="section-eyebrow">Tarif</div>
    <h2 class="section-title">Un prix simple, sans abonnement caché</h2>
    <div class="qz-prix" style="text-align:left">
      <div class="offre-card offre-quiz fade-up">
        <span class="offre-badge">Bientôt disponible</span>
        <div class="offre-head">
          <div class="offre-icon">🎯</div>
          <div><h3>Quiz CRPE</h3><p class="offre-tagline">Réviser vite, dans toutes les disciplines</p></div>
        </div>
        <div class="offre-price"><strong>{PRIX_QUIZ}</strong><span>TTC</span></div>
        <ul class="offre-list">
          <li>{total_txt} questions dans {len(MATIERES)} disciplines</li>
          <li>Séries de 20 questions notées sur 20</li>
          <li>Explication de chaque erreur et révision espacée</li>
          <li>Progression par thème du programme</li>
        </ul>
        <div class="offre-cta">
          <a href="#" class="btn-primary cta-commencer" onclick="openAuth(event,'register')">Créer mon compte</a>
          <p class="offre-note">Créez votre compte pour accéder au quiz parmi les premiers.</p>
        </div>
      </div>
      <div class="offre-card offre-pack fade-up" style="animation-delay:.1s">
        <span class="offre-badge">Le plus complet</span>
        <div class="offre-head">
          <div class="offre-icon">🎁</div>
          <div><h3>Pack Tuteur IA + Quiz CRPE</h3><p class="offre-tagline">Les deux outils réunis</p></div>
        </div>
        <div class="offre-price"><strong>{PRIX_PACK}</strong><span>TTC</span><span class="old">{PRIX_PACK_BARRE}</span></div>
        <span class="pack-save">{ECONOMIE_PACK} d'économie</span>
        <ul class="offre-list">
          <li>Le Quiz CRPE complet</li>
          <li>1 an d'accès au tuteur IA : exercices corrigés en mathématiques et en français</li>
          <li>Des révisions rapides et un entraînement à la rédaction</li>
        </ul>
        <div class="offre-cta">
          <a href="#" class="btn-white cta-commencer" onclick="openAuth(event,'register')" style="width:100%;justify-content:center">Créer mon compte</a>
          <p class="offre-note" style="color:rgba(255,255,255,.75)">Essai gratuit du tuteur IA dès l'inscription.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════ FAQ ═══════════════════════════════ -->
<section id="faq" style="background:var(--gray-50)">
  <div class="container" style="max-width:760px">
    <div class="section-eyebrow">Questions fréquentes</div>
    <h2 class="section-title">Tout savoir sur le Quiz CRPE</h2>
    <div class="faq-list">
{faq}
    </div>
  </div>
</section>

<!-- ═══════════════════════════════ CTA ═══════════════════════════════ -->
<section class="cta-section" id="inscription">
  <div class="container">
    <h2>Prêt à réviser toutes les disciplines du CRPE ?</h2>
    <p>Créez votre compte PassCRPE en moins de 2 minutes.</p>
    <div class="cta-form">
      <button type="button" class="btn-white cta-commencer" onclick="openAuth(event,'register')">{ARROW}Vérifiez votre niveau gratuitement</button>
    </div>
    <p class="cta-note">Quiz CRPE · {PRIX_QUIZ} TTC</p>
  </div>
</section>
'''


def main():
    src = open(SRC, encoding='utf-8').read()

    # En-tête : styles et suivi de l'accueil, titre et description propres à la page
    head = src[:src.index('</head>')]
    head = re.sub(r'<title>.*?</title>', '<title>Quiz CRPE : arrivez au CRPE en maîtrisant toutes les disciplines</title>', head, flags=re.S)
    head = re.sub(r'<meta name="description"[^>]*/>',
                  '<meta name="description" content="Le Quiz CRPE : 300 questions par discipline sur le programme du cycle 4, '
                  'des séries de 20 notées sur 20, l\'explication de chaque erreur et des révisions espacées. 49,99 € TTC." />\n'
                  f'  <link rel="canonical" href="{SITE}/quizz" />', head)
    head = head.replace('href="favicon.svg"', 'href="/favicon.svg"')
    head = head.replace('  </style>', CSS + '  </style>', 1)
    assert CSS in head

    # Début du corps (balises noscript) et menu, avec des liens propres à la page
    body_pre = cut(src, '<body>', '<!-- ═══════════════════════════════ NAV')
    nav = cut(src, '<!-- ═══════════════════════════════ NAV', '</nav>', include_end=True)
    liens = re.search(r'      <li><a href="#crpe">.*?<li><a href="#offres">Offres</a></li>\n', nav, re.S)
    assert liens
    nav = nav.replace(liens.group(0),
                      '      <li><a href="/">Tuteur IA</a></li>\n'
                      '      <li><a href="#fonctionnement">Le quiz</a></li>\n'
                      '      <li><a href="#matieres">Disciplines</a></li>\n'
                      '      <li><a href="#tarif">Tarif</a></li>\n')
    nav = nav.replace('<a href="#" class="nav-logo">', '<a href="/" class="nav-logo">')
    nav = nav.replace('Commencer<span class="nav-cta-long"> gratuitement</span> →', "S'inscrire →")

    # Pied de page : liens vers l'accueil, sauf la FAQ de cette page
    footer = cut(src, '<!-- ═══════════════════════════════ FOOTER', '</footer>', include_end=True)
    footer = footer.replace('<li><a href="#offres">Quiz CRPE</a></li>', '<li><a href="/quizz">Quiz CRPE</a></li>')
    footer = re.sub(r'href="#(?!faq")([a-z]+)"', r'href="/#\1"', footer)

    # Fenêtres de confirmation et de connexion/inscription, identiques à l'accueil
    modales = cut(src, '<!-- ═══════════════════════ CONFIRMATION POPUP', '<script>\n  /* ── FAQ accordion')

    # Scripts de l'accueil (FAQ, animations, inscription, menus), sans le formulaire de newsletter absent de cette page
    scripts = src[src.index('<script>\n  /* ── FAQ accordion'):src.index('</body>')]
    nl = cut(scripts, '  /* ── Newsletter form ── */', '  function translateSupabaseError')
    scripts = scripts.replace(nl, '')
    assert 'nl-form' not in scripts and "window.SIGNUP_PARCOURS || 'passcrpe'" in scripts

    page = (head + '</head>\n' + body_pre + nav + '\n' + contenu() + '\n' + footer + '\n\n' + modales
            + "<script>\n  // Parcours Klaviyo des inscriptions faites sur cette page\n  window.SIGNUP_PARCOURS = 'quizcrpe';\n  // Après l'inscription ou la connexion, direction l'application du quiz\n  window.AFTER_SIGNUP_URL = '/quizzapp';\n"
            + "  // Comptes du quiz : projet Supabase « quizzcrpe », séparé du tuteur IA\n"
            + f"  window.SB_PROJET = 'quizzcrpe';\n  window.SB_URL = '{QUIZ_SB_URL}';\n  window.SB_KEY = '{QUIZ_SB_KEY}';\n"
            + f"  // Lien de l'e-mail de confirmation : retour sur cette page, qui affiche « Votre compte est activé » et le bouton Se connecter\n"
            + f"  window.EMAIL_REDIRECT_URL = '{SITE}/quizz';\n</script>\n"
            + scripts + '</body>\n</html>\n')
    open(OUT, 'w', encoding='utf-8').write(page)
    print('Écrit :', os.path.relpath(OUT, ROOT), f'({len(page) // 1024} ko)')


if __name__ == '__main__':
    main()

# Bac+5, session 2025, session supplémentaire (académies de Créteil, Versailles et Paris)
from slib import S, Q, N, C, epreuve

ARNAUD = ("Texte : Clara Arnaud, Et vous passerez comme des vents fous (2023). Gaspard, berger dans les Pyrénées, mène son troupeau "
          "de brebis en haute montagne avec sa chienne Lunita.")
JEU = ("Exercice 1 : un triangle ABC rectangle en B, avec AB = 140 m et BC = 105 m. D est sur [BC] avec BD = 75 m ; "
       "la parallèle à (AC) passant par D coupe (AB) en E.")
BALISE = "Exercice 1, partie C : une balise est un tronc de cône, obtenu à partir d'un cône de hauteur 15 cm et de rayon de base 10 cm, coupé à 3 cm du sommet."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 16702, [
        S('francais', 'Lexique · formation des mots', Q(
            "Quels sont les deux éléments qui forment le nom « téléphone » ?",
            ["Télé- (loin) et -phone (la voix, le son)", "Télé- (écran) et -phone (appareil)", "Tél- (fil) et -éphone (parler)", "Un seul élément d'origine anglaise"], "Télé- (loin) et -phone (la voix, le son)",
            "Deux éléments grecs : télévision, télescope ; microphone, francophone. Le téléphone transmet la voix au loin."), ARNAUD),
        S('francais', 'Lexique · antonymes', Q(
            "« Dans ce camp éphémère, tout était réduit à l'essentiel. » Quel antonyme convient à « éphémère » ?",
            ["Durable", "Provisoire", "Fragile", "Petit"], "Durable",
            "Éphémère : qui dure peu (le camp d'estive est démonté à la fin de l'été). Antonymes : durable, permanent, pérenne. « Provisoire » est un synonyme."), ARNAUD),
        S('francais', 'Lexique · antonymes', Q(
            "« Le moindre mouvement trop véhément de la chienne aurait pu faire dérocher une partie du troupeau. » Quel antonyme convient à « véhément » ?",
            ["Doux", "Violent", "Rapide", "Bruyant"], "Doux",
            "Véhément : impétueux, violent. Ici, le berger chuchote ses ordres : il faut des gestes doux, mesurés, pour ne pas affoler les brebis au bord du vide."), ARNAUD),
        S('francais', 'Lexique · sens en contexte', Q(
            "« … de petits morceaux de pelouse que les brebis savaient gagner en funambules. » Que signifie « en funambules » ?",
            ["En équilibre, avec adresse, sur des passages étroits et dangereux", "En courant très vite", "En bêlant fort", "En groupe serré"],
            "En équilibre, avec adresse, sur des passages étroits et dangereux",
            "Le funambule marche sur un fil : la métaphore souligne l'agilité des brebis sur les éboulis, « en lisière du vide »."), ARNAUD),
        S('francais', 'Lexique · sens en contexte', Q(
            "« Ici, on se faufilait plus qu'on ne progressait. » Quel antonyme de « progressait » convient en contexte ?",
            ["Reculait", "Avançait", "Montait", "Marchait"], "Reculait",
            "Progresser, c'est avancer. Le « ne » de « qu'on ne progressait » est un ne explétif, qui n'a pas de valeur négative après une comparaison."), ARNAUD),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16705, [
        S('mathematiques', 'Exercice 1 · Pythagore', N(
            "ABC est rectangle en B, AB = 140 m et BC = 105 m. Combien mesure AC, en m ?", 175,
            "AC² = 140² + 105² = 19 600 + 11 025 = 30 625, donc AC = 175 m."), JEU),
        S('mathematiques', 'Exercice 1 · Thalès', N(
            "Avec BD = 75 m et (DE) parallèle à (AC), combien mesure BE, en m ?", 100,
            "Théorème de Thalès dans le triangle BAC : BE/BA = BD/BC, donc BE = 140 × 75 ÷ 105 = 100 m."), JEU),
        S('mathematiques', 'Exercice 1 · aires', N(
            "Quelle est l'aire du quadrilatère AEDC, en m² ? (BE = 100 m, BD = 75 m)", 3600,
            "Aire de ABC : 140 × 105 ÷ 2 = 7 350 m². Aire de EBD : 100 × 75 ÷ 2 = 3 750 m². AEDC : 7 350 − 3 750 = 3 600 m²."), JEU),
        S('mathematiques', 'Exercice 1 · vitesses', Q(
            "L'équipe 1 court à 11 km/h ; l'équipe 2, à une allure de 6 min 10 s par km. Laquelle est la plus rapide ?",
            ["L'équipe 1 : elle met environ 5 min 27 s par km", "L'équipe 2", "Elles vont aussi vite", "On ne peut pas comparer une vitesse et une allure"], "L'équipe 1 : elle met environ 5 min 27 s par km",
            "À 11 km/h, 1 km prend 60 ÷ 11 ≈ 5,45 min, soit environ 5 min 27 s, moins que 6 min 10 s. On peut aussi convertir l'allure : 60 ÷ 6,17 ≈ 9,7 km/h."), None),
        S('mathematiques', 'Exercice 1 · réduction', Q(
            "Le petit cône (hauteur 3 cm) est une réduction du grand cône (hauteur 15 cm). Par combien son volume est-il divisé ?",
            ["Par 125 (coefficient 1/5, au cube)", "Par 5", "Par 25", "Par 3"], "Par 125 (coefficient 1/5, au cube)",
            "Coefficient de réduction : 3/15 = 1/5. Les longueurs sont divisées par 5, les aires par 25, les volumes par 5³ = 125."), BALISE),
        S('mathematiques', 'Exercice 1 · volumes', Q(
            "Quel est le volume exact de la balise (grand cône moins petit cône) ?",
            ["496π cm³", "500π cm³", "1 500π cm³", "4π cm³"], "496π cm³",
            "Grand cône : π × 10² × 15 ÷ 3 = 500π cm³. Petit cône : 500π ÷ 125 = 4π cm³. Balise : 496π ≈ 1 558 cm³."), BALISE),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 16708, [
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "Pour quelle œuvre de Molière Lully a-t-il composé la « Marche pour la cérémonie des Turcs » (1670) ?",
            ["Le Bourgeois gentilhomme", "Le Malade imaginaire", "L'Avare", "Tartuffe"], "Le Bourgeois gentilhomme",
            "Cette comédie-ballet de Molière et Lully a été créée en 1670 devant Louis XIV. Lully est le compositeur majeur de la cour du roi, à l'époque baroque."),
          "Dossier d'éducation musicale (cycle 3) : Jean-Baptiste Lully, Marche pour la cérémonie des Turcs, 1670."),
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "À quelle période musicale appartient Lully ?",
            ["Baroque", "Romantique", "Classique", "Moyen Âge"], "Baroque",
            "Lully (1632-1687) compose à la cour de Louis XIV : opéras, ballets, comédies-ballets. La période baroque s'étend environ de 1600 à 1750."), None),
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "Que signifie une « écoute incarnée », évoquée par un document du dossier ?",
            ["Une écoute qui engage le corps : bouger, frapper la pulsation, mimer pour ressentir la musique", "Une écoute en silence total, immobile", "La lecture de la partition", "Une écoute réservée aux musiciens"],
            "Une écoute qui engage le corps : bouger, frapper la pulsation, mimer pour ressentir la musique",
            "Une marche s'y prête bien : les élèves peuvent marcher sur la pulsation, repérer les changements de caractère et les instruments."),
          "Document 3 : Andrea Giomi, « Pour une approche de l'écoute incarnée. Corps, … »."),
        S('arts', 'Arts plastiques · expression des émotions', Q(
            "Une fiche de préparation « Ma créature fantastique » (cycle 2) se termine par la projection du film « Dragons » (2010). Quel défaut peut-on y relever ?",
            ["Montrer le film seulement en fin de séance ne nourrit pas la pratique ; il faudrait plutôt des références artistiques variées et un temps d'expérimentation", "Il n'y a pas de dragon dans le film", "Les élèves de cycle 2 sont trop jeunes pour dessiner", "Une créature fantastique n'est pas un sujet d'arts plastiques"],
            "Montrer le film seulement en fin de séance ne nourrit pas la pratique ; il faudrait plutôt des références artistiques variées et un temps d'expérimentation",
            "Le sujet demandait une analyse critique au regard du programme : « exprimer sa sensibilité et son imagination », « expérimenter les effets des couleurs, des matériaux, des supports »."),
          "Dossier d'arts plastiques (cycle 2) : une fiche de préparation « Ma créature fantastique », à analyser."),
    ]),
]

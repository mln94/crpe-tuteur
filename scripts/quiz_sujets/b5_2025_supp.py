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
    # ── Ajout : questions complémentaires (dont l'histoire et l'EMC, récupérées par OCR) ──
    epreuve('Épreuve écrite disciplinaire de français', 16702, [
        S('francais', 'Lexique · antonymes', Q(
            "« … des gestes hâtifs. » Quel antonyme convient à « hâtifs » ?",
            ["Lents", "Rapides", "Brusques", "Précipités"], "Lents",
            "Hâtif : fait trop vite, précipité. Antonymes : lent, réfléchi, posé. Un antonyme doit avoir la même nature (adjectif)."), ARNAUD),
        S('francais', 'Lexique · formation des mots', Q(
            "Quel mot est formé avec le même premier élément que « téléphone » ?",
            ["Télescope", "Microphone", "Phonétique", "Saxophone"], "Télescope",
            "Télé- (loin) : télescope, télévision, télécommande. -phone (le son, la voix) : microphone, saxophone, francophone."), ARNAUD),
        S('francais', 'Lexique · notes du texte', Q(
            "Selon les notes du sujet, qu'est-ce qu'une « estive » ?",
            ["Un pâturage de haute montagne et, par extension, le séjour des troupeaux dans ces pâturages", "Une fête d'été", "Un chemin de transhumance", "Un abri de berger"], "Un pâturage de haute montagne et, par extension, le séjour des troupeaux dans ces pâturages",
            "Les « drailles », elles, sont les chemins de transhumance ; « dérocher », c'est tomber d'une paroi rocheuse."), ARNAUD),
        S('francais', 'Lexique · sens en contexte', Q(
            "« Il retrouvait le temps élastique du voyage. » Que suggère l'adjectif « élastique » ?",
            ["Un temps qui semble s'étirer, ralentir, sans contraintes d'horaires", "Un temps très court", "Un temps mesuré précisément", "Un temps dangereux"],
            "Un temps qui semble s'étirer, ralentir, sans contraintes d'horaires",
            "L'image est prolongée par « les heures qui s'étalent dans un ennui tiède » : la solitude en montagne change le rapport au temps."), ARNAUD),
        S('francais', 'Réflexion · la solitude dans la nature', Q(
            "Le sujet de réflexion portait sur l'expérience de la solitude dans la nature. Laquelle de ces œuvres traite de ce thème ?",
            ["Walden ou la Vie dans les bois, de Henry David Thoreau", "Le Bourgeois gentilhomme, de Molière", "Le Cid, de Corneille", "Les Misérables, de Victor Hugo"],
            "Walden ou la Vie dans les bois, de Henry David Thoreau",
            "Thoreau raconte deux années passées seul dans une cabane au bord d'un lac. On peut aussi citer Robinson Crusoé ou les Rêveries du promeneur solitaire de Rousseau."), None),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16705, [
        S('mathematiques', 'Exercice 1 · aires', N(
            "Quelle est l'aire du triangle ABC rectangle en B, avec AB = 140 m et BC = 105 m, en m² ?", 7350,
            "Aire d'un triangle rectangle : (côté × côté) ÷ 2 = 140 × 105 ÷ 2 = 7 350 m²."), JEU),
        S('mathematiques', 'Exercice 1 · aires', N(
            "La zone de jeu est le quadrilatère AEDC (3 600 m²) plus un demi-disque de diamètre [DC] = 30 m. Quelle est son aire, arrondie au m² ?", 3953,
            "Demi-disque de rayon 15 m : π × 15² ÷ 2 = 112,5π ≈ 353,4 m². Total ≈ 3 953 m².", tol=1), JEU),
        S('mathematiques', 'Exercice 1 · statistiques', Q(
            "L'étendue des temps pour atteindre une balise est de 2,9 min et l'équipe 2 est la plus rapide. Comment obtenir le temps de l'équipe la plus lente ?",
            ["Temps de l'équipe 2 + 2,9 min", "Temps de l'équipe 2 − 2,9 min", "2,9 × le nombre d'équipes", "La moyenne des temps"], "Temps de l'équipe 2 + 2,9 min",
            "L'étendue est la différence entre la plus grande et la plus petite valeur."), None),
        S('mathematiques', 'Exercice 1 · volumes', N(
            "Quel est le volume du cône de hauteur 15 cm et de rayon 10 cm, en valeur exacte divisée par π (c'est-à-dire le nombre devant π) ?", 500,
            "V = π × 10² × 15 ÷ 3 = 500π cm³."), BALISE),
        S('mathematiques', 'Exercice 2 · statistiques', Q(
            "Un garçon court 2 500 m en 12 minutes. Quel est son indice de forme d'après le barème (insuffisant < 2 000 m ; suffisant 2 000-2 400 ; bon 2 400-3 000 ; très bon > 3 000) ?",
            ["Bon", "Suffisant", "Très bon", "Insuffisant"], "Bon",
            "2 500 m est compris entre 2 400 et 3 000 m. Le barème des filles est décalé de 200 m."), None),
        S('mathematiques', 'Exercice 2 · vitesses', N(
            "Un enfant parcourt 2 400 m en 12 minutes. Quelle est sa vitesse moyenne en km/h ?", 12,
            "2,4 km en 12 min = 2,4 km en 0,2 h : 2,4 ÷ 0,2 = 12 km/h."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 16708, [
        S('histoire_geographie', 'Histoire · Napoléon Bonaparte', Q(
            "Quel coup d'État, en 1799, porte Bonaparte au pouvoir ?",
            ["Le coup d'État du 18 Brumaire", "La prise de la Bastille", "Le 2 décembre 1851", "La journée des Barricades"], "Le coup d'État du 18 Brumaire",
            "Le 18 brumaire an VIII (9 novembre 1799) met fin au Directoire ; Bonaparte devient Premier consul, puis empereur en 1804."), "Sujet d'histoire : Napoléon Bonaparte et la construction de sa légende, à partir de tableaux et d'une bande dessinée historique."),
        S('histoire_geographie', 'Histoire · Napoléon Bonaparte', Q(
            "En quelle année Napoléon Bonaparte est-il sacré empereur ?",
            ["1804", "1799", "1815", "1789"], "1804",
            "Le sacre a lieu à Notre-Dame de Paris le 2 décembre 1804. L'Empire prend fin après Waterloo, en 1815."), None),
        S('histoire_geographie', 'Histoire · Napoléon Bonaparte', Q(
            "Le tableau de David « L'Empereur dans son cabinet de travail » (1812) montre Napoléon :",
            ["En chef d'État actif et travailleur, à quatre heures du matin", "Sur un champ de bataille", "En exil à Sainte-Hélène", "Pendant son sacre"],
            "En chef d'État actif et travailleur, à quatre heures du matin",
            "L'horloge et la bougie consumée suggèrent qu'il travaille la nuit pour la France : c'est une image construite pour la propagande."), "Document 4 : Jacques-Louis David, L'Empereur dans son cabinet de travail, 1812."),
        S('histoire_geographie', 'Histoire · Napoléon Bonaparte', Q(
            "Pourquoi le tableau de Delaroche (1848) montrant Bonaparte franchissant les Alpes est-il un document à manier avec précaution ?",
            ["Il est peint près de 50 ans après l'événement : c'est une représentation, pas un témoignage direct", "Il est faux car Bonaparte n'a jamais franchi les Alpes", "Il a été peint par Bonaparte lui-même", "Il date de 1800"],
            "Il est peint près de 50 ans après l'événement : c'est une représentation, pas un témoignage direct",
            "Tout document doit être daté et attribué : son auteur et son époque orientent la représentation de l'événement."), "Document 5 : Paul Delaroche, Bonaparte franchissant les Alpes au col du Grand-Saint-Bernard en 1800, peint en 1848."),
        S('histoire_geographie', 'Histoire · Napoléon Bonaparte', Q(
            "Qu'appelle-t-on la « légende napoléonienne » ?",
            ["L'image glorieuse que Napoléon a construite de lui-même par la propagande (tableaux, bulletins de la Grande Armée)", "Un conte pour enfants", "Une chanson populaire", "La liste de ses batailles perdues"],
            "L'image glorieuse que Napoléon a construite de lui-même par la propagande (tableaux, bulletins de la Grande Armée)",
            "Le texte du dossier rappelle l'expression « menteur comme un Bulletin » : l'historien doit étudier cette mise en scène pour ne pas s'y laisser prendre."), "Document 7 : A. Lignereux et Krassinsky, La folie Napoléon, bande dessinée historique, 2022."),
        S('emc', "EMC · vivre ensemble à l'école maternelle", Q(
            "Quelle différence faire comprendre à des élèves de maternelle entre « rigoler » et « se moquer » ?",
            ["Rire ensemble fait plaisir à tous ; se moquer, c'est rire de quelqu'un et lui faire de la peine", "Ce sont deux mots pour la même chose", "Se moquer est toujours drôle", "Rigoler est interdit à l'école"],
            "Rire ensemble fait plaisir à tous ; se moquer, c'est rire de quelqu'un et lui faire de la peine",
            "Le dossier proposait les affichages « RIGOLER » et « SE MOQUER » d'une école maternelle et un poster des P'tits Philosophes : « Ça fait rire ? Ça fait mal ? »."), "Sujet d'EMC : à l'école maternelle, distinguer rire et se moquer pour apprendre à vivre ensemble."),
        S('emc', "EMC · vivre ensemble à l'école maternelle", Q(
            "Dans l'album « L'éléphant à la trop petite trompe », que ressent l'éléphant quand les enfants chantent pour se moquer de lui ?",
            ["Il est triste et en meurt de honte", "Il trouve cela drôle", "Il chante avec eux", "Il ne remarque rien"], "Il est triste et en meurt de honte",
            "La littérature de jeunesse permet de s'identifier à un personnage tout en gardant une distance, comme le dit le programme de maternelle : elle développe l'empathie."), "Document 9 : Chun-ming Hwang, L'éléphant à la trop petite trompe, 2006."),
        S('emc', "EMC · vivre ensemble à l'école maternelle", Q(
            "Selon le programme de maternelle, quel est l'enjeu central de l'école maternelle ?",
            ["« Apprendre ensemble et vivre ensemble »", "Apprendre à lire couramment", "Préparer les évaluations", "Apprendre une langue étrangère"], "« Apprendre ensemble et vivre ensemble »",
            "Le programme cite une première sensibilité aux expériences morales : empathie, expression du juste et de l'injuste, questionnement des stéréotypes."), "Document 7 : programme de l'école maternelle (2021)."),
        S('emc', "EMC · vivre ensemble à l'école maternelle", Q(
            "Quelle compétence l'enseignant de maternelle développe-t-il pour prévenir les moqueries ?",
            ["Identifier et exprimer verbalement ses émotions et celles des autres", "Recopier des mots", "Compter jusqu'à 10", "Reconnaître les couleurs"],
            "Identifier et exprimer verbalement ses émotions et celles des autres",
            "Le programme demande que les enfants puissent développer leur estime de soi, s'entraider et partager avec les autres."), None),
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "La « Marche pour la cérémonie des Turcs » de Lully est :",
            ["Une parodie de musique de cérémonie, pour une scène comique de Molière", "Une musique funèbre", "Un hymne national turc", "Une berceuse"],
            "Une parodie de musique de cérémonie, pour une scène comique de Molière",
            "Dans Le Bourgeois gentilhomme, monsieur Jourdain est fait « Mamamouchi » lors d'une fausse cérémonie turque : la musique grandiose est comique."), None),
        S('arts', 'Arts plastiques · la créature fantastique', Q(
            "Dans la fiche « Ma créature fantastique », les élèves froissent, déchirent, découpent des matériaux. Quelle notion du programme travaillent-ils ?",
            ["Transformer des matériaux pour expérimenter leurs effets plastiques", "Copier un modèle", "Mesurer des longueurs", "Classer des animaux"],
            "Transformer des matériaux pour expérimenter leurs effets plastiques",
            "« Expérimenter les effets des couleurs, des matériaux, des supports » : c'était l'un des points du programme cités par le sujet."), None),
    ]),
]

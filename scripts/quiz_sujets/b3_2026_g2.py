# Bac+3, session 2026, groupement 2
from slib import S, Q, N, C, epreuve

JAB = "Texte : Ivan Jablonka, En camping-car (2018). Le narrateur fait le portrait de sa mère, professeure de lettres classiques, pendant les vacances familiales en Méditerranée."
DES = "Exercice 1 : Enzo lance deux dés à quatre faces (numérotées de 1 à 4) et additionne les deux nombres obtenus."
PROG = ("Exercice 2 : Programme A : choisir un nombre, ajouter 4, multiplier le résultat par 3, retrancher 11. "
        "Programme B : choisir un nombre, le multiplier par −4, ajouter 5 au résultat.")
OMBRE = ("Exercice 3 : spectacle d'ombres chinoises. La source lumineuse A est à 9 m de l'écran. Un objet [DE] de 0,2 m de haut, "
         "parallèle à l'écran, projette sur l'écran une ombre [BC] de 1,2 m de haut. A, D et B sont alignés, ainsi que A, E et C.")
JO = ("Exercice 4 : aux Jeux olympiques de Paris 2024, 63 pays ont reçu au moins une médaille d'or. Répartition : 1 or : 23 pays ; 2 : 12 ; 3 : 9 ; 4 : 4 ; "
      "5, 6, 8, 9, 10 : 1 pays chacun ; 12 : 2 ; 13, 14, 15, 16, 18, 20 : 1 pays chacun ; 40 : 2 pays.")
NINO = "Sujet de sciences : les phénomènes climatiques El Niño et La Niña."
GUARDIAN = ("Text: “The headteacher bringing play back to the classroom”, The Guardian, 11 June 2025. Tina Farr, headteacher of an Oxford primary school, "
            "has put play back on the curriculum in year 2 (six- and seven-year-olds). Play-based learning usually stops when children leave reception "
            "(the first year of primary school); lessons then become desk-based, focused on reading and writing.")

QUESTIONS = [
    epreuve('Première épreuve écrite (français et mathématiques)', 20280, [
        # ── Français ──
        S('francais', "Étude de la langue · degrés de l'adjectif", Q(
            "« Ma mère est la plus élégante du groupe. » Comment nomme-t-on la tournure « la plus élégante du groupe » ?",
            ["Superlatif relatif de supériorité", "Superlatif absolu", "Comparatif de supériorité", "Degré positif"], "Superlatif relatif de supériorité",
            "On compare la mère aux autres membres d'un ensemble (« du groupe ») : superlatif relatif. Le superlatif absolu exprime un très haut degré sans comparaison (« très élégante »)."), JAB),
        S('francais', "Étude de la langue · degrés de l'adjectif", Q(
            "Lequel de ces groupes est un superlatif absolu de l'adjectif « élégant » ?",
            ["Très élégante", "Plus élégante que sa sœur", "Aussi élégante que sa sœur", "La moins élégante du groupe"], "Très élégante",
            "Les degrés de l'adjectif : positif (élégante), comparatif (plus, aussi, moins élégante que…), superlatif relatif (la plus / la moins élégante de…), superlatif absolu (très, extrêmement élégante)."), JAB),
        S('francais', 'Étude de la langue · type et formes de phrase', Q(
            "« Le soir, ce n'est jamais elle qui lève le toit. » Type et formes de cette phrase ?",
            ["Déclarative ; négative et emphatique (mise en relief par « c'est… qui »)", "Interrogative ; négative", "Exclamative ; emphatique", "Déclarative ; affirmative et passive"],
            "Déclarative ; négative et emphatique (mise en relief par « c'est… qui »)",
            "Une phrase n'a qu'un type (déclaratif, interrogatif, injonctif) mais peut cumuler des formes : négative (ne… jamais), emphatique (« c'est… qui » met « elle » en relief), active."), JAB),
        S('francais', 'Étude de la langue · conjugaison', Q(
            "Transposez « Les photos la montrent » au passé composé.",
            ["Les photos l'ont montrée", "Les photos l'ont montré", "Les photos l'ont montrés", "Les photos la montrèrent"], "Les photos l'ont montrée",
            "Avec l'auxiliaire avoir, le participe passé s'accorde avec le COD placé avant le verbe : « la » (la mère), féminin singulier, donc « montrée »."), JAB),
        S('francais', 'Étude de la langue · conjugaison', Q(
            "Transposez « Les photos la montrent » au passé simple.",
            ["Les photos la montrèrent", "Les photos la montraient", "Les photos la montreront", "Les photos l'eurent montrée"], "Les photos la montrèrent",
            "Verbe du 1er groupe au passé simple, 3e personne du pluriel : -èrent. Montraient est l'imparfait, montreront le futur, eurent montrée le passé antérieur."), JAB),
        S('francais', 'Étude de la langue · conjugaison', Q(
            "Transposez « Les photos la montrent » au futur antérieur.",
            ["Les photos l'auront montrée", "Les photos l'avaient montrée", "Les photos la montreront", "Les photos l'auraient montrée"], "Les photos l'auront montrée",
            "Futur antérieur = auxiliaire au futur (auront) + participe passé, accordé avec le COD « la » placé avant. « L'avaient montrée » est le plus-que-parfait."), JAB),
        S('francais', 'Étude de la langue · nature et fonction', Q(
            "« Les photos la montrent en robe. » Nature et fonction de « la » ?",
            ["Pronom personnel, COD du verbe montrer", "Article défini, déterminant", "Pronom personnel, sujet", "Pronom personnel, COI du verbe montrer"], "Pronom personnel, COD du verbe montrer",
            "« La » remplace « ma mère » : les photos montrent qui ? la mère. Pas de préposition : complément d'objet direct."), JAB),
        S('francais', 'Lexique · sens en contexte', Q(
            "« Il n'exhibe pas ses ruines, son écroulement, mais son apogée éclatant. » Que signifie « apogée » ?",
            ["Le point culminant, le plus haut degré de puissance et de rayonnement", "Le déclin, la chute", "Les fondations, l'origine", "Une place publique de la ville grecque"],
            "Le point culminant, le plus haut degré de puissance et de rayonnement",
            "Le texte oppose l'apogée aux « ruines » et à l'« écroulement » : le monde grec apparaît à son sommet. (L'agora est la place publique.)"), JAB),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé « inconcevable » ?",
            ["Préfixe in- (négation) + base concev(oir) + suffixe -able", "Préfixe incon- + base cevable", "Composition de « in » et « concevable » comme deux mots", "Base inconce- + suffixe -vable"],
            "Préfixe in- (négation) + base concev(oir) + suffixe -able",
            "Dérivation par préfixation et suffixation : -able (« qu'on peut… »), in- (négation). Inconcevable : qu'on ne peut pas concevoir, imaginer."), JAB),
        S('francais', 'Lexique · famille de mots', Q(
            "Quel mot n'appartient pas à la même famille que « inconcevable » ?",
            ["Convenable", "Concevoir", "Conception", "Concevable"], "Convenable",
            "Concevoir, conception, concevable, conceptuel viennent du latin concipere. « Convenable » vient de convenir : une ressemblance de forme ne suffit pas."), JAB),
        # ── Mathématiques ──
        S('mathematiques', 'Exercice 1 · probabilités', Q(
            "Quelle est la probabilité d'obtenir une somme égale à 2 ?",
            ["1/16", "1/7", "1/8", "2/16"], "1/16",
            "Il y a 4 × 4 = 16 issues équiprobables. Seule l'issue (1 ; 1) donne 2 : probabilité 1/16. Il y a 7 sommes possibles (2 à 8), mais elles ne sont pas équiprobables : 1/7 est faux."), DES),
        S('mathematiques', 'Exercice 1 · probabilités', Q(
            "L'événement « obtenir 5 » est-il plus probable que « obtenir 6 » ?",
            ["Oui : 4/16 contre 3/16", "Non : ils ont la même probabilité", "Non : 6 est plus probable", "Oui : 5/16 contre 3/16"], "Oui : 4/16 contre 3/16",
            "Somme 5 : (1;4), (2;3), (3;2), (4;1), soit 4 issues : 1/4. Somme 6 : (2;4), (3;3), (4;2), soit 3 issues : 3/16."), DES),
        S('mathematiques', 'Exercice 2 · programmes de calcul', N(
            "Quel nombre obtient-on avec le programme A en choisissant −5 ?", -14,
            "−5 + 4 = −1 ; −1 × 3 = −3 ; −3 − 11 = −14."), PROG),
        S('mathematiques', 'Exercice 2 · programmes de calcul', N(
            "Quel nombre faut-il choisir au départ pour obtenir −25 avec le programme B ?", 7.5,
            "−4x + 5 = −25 donne −4x = −30, x = 7,5. Vérification : −4 × 7,5 + 5 = −30 + 5 = −25."), PROG),
        S('mathematiques', 'Exercice 2 · programmes de calcul', Q(
            "Avec x le nombre de départ, quel est le résultat du programme A ?",
            ["3x + 1", "3x + 12", "x + 1", "3x − 7"], "3x + 1",
            "(x + 4) × 3 − 11 = 3x + 12 − 11 = 3x + 1. Il faut développer avec la distributivité, sans oublier de multiplier le 4 par 3."), PROG),
        S('mathematiques', 'Exercice 2 · fonctions', N(
            "g(x) = −4x + 5. Quel est l'antécédent de −3 par la fonction g ?", 2,
            "−4x + 5 = −3 donne x = 2. Graphiquement, on part de −3 sur l'axe des ordonnées, on rejoint la droite, puis on lit l'abscisse."), PROG),
        S('mathematiques', 'Exercice 2 · fonctions', Q(
            "f(x) = 3x + 1 et g(x) = −4x + 5. Quelle est l'abscisse du point d'intersection de leurs représentations graphiques ?",
            ["4/7", "7/4", "4", "−4/7"], "4/7",
            "3x + 1 = −4x + 5 donne 7x = 4, x = 4/7. C'est le nombre de départ qui donne le même résultat avec les deux programmes."), PROG),
        S('mathematiques', 'Exercice 3 · Thalès', N(
            "À quelle distance AD de la source lumineuse faut-il placer l'objet, en mètres ?", 1.5,
            "(DE) et (BC) sont parallèles (toutes deux parallèles à l'écran, ou perpendiculaires au sol). Thalès : AD/AB = DE/BC, donc AD = 9 × 0,2 / 1,2 = 1,5 m."), OMBRE),
        S('mathematiques', 'Exercice 3 · agrandissement', N(
            "L'objet est une plaque rectangulaire de 20 cm sur 10 cm. Par quel nombre faut-il multiplier son aire pour obtenir l'aire de l'ombre ?", 36,
            "Le coefficient d'agrandissement des longueurs est 1,2 ÷ 0,2 = 6. Les aires sont multipliées par 6² = 36."), OMBRE),
        S('mathematiques', 'Exercice 4 · statistiques', N(
            "Quel est le nombre moyen de médailles d'or par pays, arrondi au dixième ?", 5.2,
            "Total : 23 + 24 + 27 + 16 + 5 + 6 + 8 + 9 + 10 + 24 + 13 + 14 + 15 + 16 + 18 + 20 + 80 = 328 médailles. 328 ÷ 63 ≈ 5,2.", tol=0.05), JO),
        S('mathematiques', 'Exercice 4 · statistiques', N(
            "Quelle est la médiane de cette série ?", 2,
            "63 valeurs : la médiane est la 32e. Les 23 premières valent 1, les 12 suivantes (rangs 24 à 35) valent 2 : la médiane est 2. Les 9 médailles du Canada sont donc au-dessus."), JO),
        S('mathematiques', 'Exercice 4 · pourcentages', N(
            "Une médaille d'or pèse 529 g ; l'or pur représente 1,13 % de sa masse. Masse d'or pur, à l'unité près, en grammes ?", 6,
            "529 × 1,13 / 100 ≈ 5,98 g, soit 6 g à l'unité près."), None),
        S('mathematiques', 'Exercice 4 · Scratch', N(
            "Pour tracer un hexagone régulier avec Scratch, de combien de degrés le lutin doit-il tourner après chaque côté ?", 60,
            "Le lutin tourne de l'angle extérieur : 360° ÷ 6 = 60°. Tourner de 120° (l'angle intérieur) trace un triangle équilatéral."), None),
        S('mathematiques', 'Exercice 5 · vrai ou faux', Q(
            "Affirmation : « Un prix augmenté de 50 % puis baissé de 40 % a augmenté de 10 %. » Vrai ou faux ?",
            ["Faux : il a baissé de 10 %", "Vrai", "Faux : il a augmenté de 90 %", "Faux : il n'a pas changé"], "Faux : il a baissé de 10 %",
            "Les coefficients se multiplient : 1,5 × 0,6 = 0,9. Le prix final vaut 90 % du prix initial : baisse de 10 %. On n'additionne pas des pourcentages successifs."), None),
        S('mathematiques', 'Exercice 5 · vrai ou faux', Q(
            "Affirmation : « Le nombre de dizaines de 6 727 est 112 fois plus grand que son nombre de milliers. » Vrai ou faux ?",
            ["Vrai", "Faux"], "Vrai",
            "Nombre de dizaines de 6 727 : 672. Nombre de milliers : 6. 672 ÷ 6 = 112. Attention : le « nombre de dizaines » n'est pas le « chiffre des dizaines » (2)."), None),
        S('mathematiques', 'Exercice 5 · vrai ou faux', N(
            "Affirmation : « Ajouter 13 dixièmes à 25,606 donne 25,736. » Quel est le bon résultat ?", 26.906,
            "13 dixièmes = 1,3. 25,606 + 1,3 = 26,906 : l'affirmation est fausse (25,736 correspond à l'ajout de 13 centièmes)."), None),
        S('mathematiques', 'Exercice 5 · vrai ou faux', Q(
            "Affirmation : « 22/25 est un nombre décimal. » Vrai ou faux ?",
            ["Vrai : 22/25 = 88/100 = 0,88", "Faux : c'est une fraction", "Faux : 25 n'est pas une puissance de 10", "Vrai : tout quotient est décimal"], "Vrai : 22/25 = 88/100 = 0,88",
            "Un nombre est décimal s'il peut s'écrire a/10ⁿ avec a entier. 22/25 = 88/100. (Tout quotient n'est pas décimal : 1/3 ne l'est pas.)"), None),
    ]),
    epreuve('Seconde épreuve écrite (domaines au choix)', 20271, [
        # ── Histoire-géographie ──
        S('histoire_geographie', "Histoire · l'Église dans l'Occident médiéval", Q(
            "Comment s'appelle l'impôt prélevé par l'Église sur les récoltes des paysans au Moyen Âge ?",
            ["La dîme", "La taille", "La gabelle", "Le cens"], "La dîme",
            "La dîme (environ un dixième des récoltes) fait vivre le clergé. La taille est un impôt seigneurial puis royal, la gabelle l'impôt sur le sel."),
          "Question du sujet : « Comment l'Église encadre-t-elle la société dans l'Occident médiéval ? »"),
        S('histoire_geographie', "Histoire · l'Église dans l'Occident médiéval", Q(
            "Qu'est-ce qui distingue le clergé régulier du clergé séculier ?",
            ["Le clergé régulier vit selon une règle, à l'écart du monde (moines) ; le séculier vit parmi les fidèles (curés, évêques)", "Le clergé régulier est formé des évêques, le séculier des moines", "Le clergé séculier ne célèbre pas de messe", "Il n'y a aucune différence"],
            "Le clergé régulier vit selon une règle, à l'écart du monde (moines) ; le séculier vit parmi les fidèles (curés, évêques)",
            "Regula = règle ; saeculum = le siècle, le monde. Les moines (par exemple bénédictins, cisterciens) vivent dans des monastères ; curés et évêques encadrent les paroisses et les diocèses."),
          "Question du sujet : « Comment l'Église encadre-t-elle la société dans l'Occident médiéval ? »"),
        S('histoire_geographie', "Histoire · l'Église dans l'Occident médiéval", Q(
            "Par quoi l'Église encadre-t-elle la vie des fidèles « de la naissance à la mort » ?",
            ["Les sacrements (baptême, mariage, extrême-onction…), le calendrier des fêtes et les cloches", "Les impôts royaux", "Les assemblées de citoyens", "L'école obligatoire"],
            "Les sacrements (baptême, mariage, extrême-onction…), le calendrier des fêtes et les cloches",
            "L'Église rythme le temps (cloches, fêtes, jours chômés), marque les étapes de la vie par les sacrements et encadre l'espace (paroisse, cimetière autour de l'église)."),
          "Question du sujet : « Comment l'Église encadre-t-elle la société dans l'Occident médiéval ? »"),
        S('histoire_geographie', 'Géographie · les littoraux méditerranéens', Q(
            "Le document 3 parle d'un « tourisme héliotropique ». Qu'est-ce que c'est ?",
            ["Un tourisme attiré par le soleil", "Un tourisme de montagne", "Un tourisme lié aux monuments religieux", "Un tourisme d'affaires"], "Un tourisme attiré par le soleil",
            "Hélio- = soleil, -trope = qui se tourne vers. C'est l'un des moteurs de l'attractivité de Menton et des littoraux méditerranéens, surtout en été."),
          "Documents du sujet : Menton (Alpes-Maritimes), vue aérienne du centre ancien, plan touristique, et un texte sur « un littoral méditerranéen sous pression climatique et touristique »."),
        S('histoire_geographie', 'Géographie · les littoraux méditerranéens', Q(
            "Selon le document 3, laquelle de ces menaces pèse sur le littoral méditerranéen ?",
            ["La montée du niveau marin, les canicules et les incendies", "Le recul de l'urbanisation", "La baisse du nombre de touristes", "Le refroidissement du climat"],
            "La montée du niveau marin, les canicules et les incendies",
            "Le texte cite aussi l'artificialisation, la pression sur l'eau et les plages, la gestion des déchets liée à la surfréquentation estivale, et l'arrivée de nouvelles espèces."),
          "Document 3 : « Un littoral méditerranéen sous pression climatique et touristique », 2024."),
        S('histoire_geographie', 'Géographie · les littoraux méditerranéens', Q(
            "Dans quel département se trouve Menton ?",
            ["Les Alpes-Maritimes", "Le Var", "Les Bouches-du-Rhône", "L'Hérault"], "Les Alpes-Maritimes",
            "Menton est la dernière ville de la Côte d'Azur avant la frontière italienne. Sur un croquis de paysage : mer, vieille ville, front de mer, relief en arrière-plan, avec un titre et une légende."), None),
        # ── EMC ──
        S('emc', 'EMC · laïcité et discriminations', Q(
            "Quelle loi sépare les Églises et l'État en France ?",
            ["La loi du 9 décembre 1905", "La loi Ferry de 1882", "La loi du 15 mars 2004", "La Constitution de 1946"], "La loi du 9 décembre 1905",
            "Elle garantit la liberté de conscience et le libre exercice des cultes, et pose que la République ne reconnaît ni ne subventionne aucun culte."),
          "Question du sujet : « Comment le principe de laïcité contribue-t-il à la lutte contre les discriminations à l'école ? »"),
        S('emc', 'EMC · laïcité et discriminations', Q(
            "Que prévoit la loi du 15 mars 2004 ?",
            ["L'interdiction des signes religieux ostensibles à l'école, au collège et au lycée publics", "La gratuité de l'école", "La création de la Charte de la laïcité", "L'interdiction de l'enseignement religieux privé"],
            "L'interdiction des signes religieux ostensibles à l'école, au collège et au lycée publics",
            "Elle s'applique aux élèves. La Charte de la laïcité à l'École, affichée dans les établissements, date de 2013."), None),
        S('emc', 'EMC · laïcité et discriminations', Q(
            "En quoi la laïcité aide-t-elle à lutter contre les discriminations à l'école ?",
            ["Elle garantit à chaque élève le même traitement, quelles que soient ses convictions, et le protège de toute pression", "Elle interdit aux élèves d'avoir une religion", "Elle réserve certaines activités aux élèves croyants", "Elle supprime l'enseignement de l'histoire des religions"],
            "Elle garantit à chaque élève le même traitement, quelles que soient ses convictions, et le protège de toute pression",
            "La laïcité protège la liberté de conscience et assure l'égalité de tous ; elle refuse les comportements qui rejettent l'autre en raison de ses convictions (Charte de la laïcité à l'École)."),
          "Question du sujet : « Comment le principe de laïcité contribue-t-il à la lutte contre les discriminations à l'école ? »"),
        # ── Sciences ──
        S('physique_chimie', "Sciences · les états de l'eau", Q(
            "La liquéfaction de la vapeur d'eau est-elle une transformation chimique ou physique ?",
            ["Physique : c'est un changement d'état, l'eau reste de l'eau", "Chimique : il se forme une nouvelle espèce", "Chimique : la température change", "Ni l'une ni l'autre"],
            "Physique : c'est un changement d'état, l'eau reste de l'eau",
            "Lors d'un changement d'état (gaz → liquide), les molécules d'eau ne changent pas : aucune nouvelle espèce chimique ne se forme."), NINO),
        S('physique_chimie', "Sciences · les états de l'eau", Q(
            "Quel test permet de prouver que la buée formée est de l'eau ?",
            ["Le sulfate de cuivre anhydre, blanc, devient bleu", "L'eau de chaux se trouble", "Une allumette se rallume", "Le papier pH devient rouge"],
            "Le sulfate de cuivre anhydre, blanc, devient bleu",
            "C'est le test caractéristique de l'eau. L'eau de chaux sert à identifier le dioxyde de carbone ; la bûchette incandescente qui se ravive, le dioxygène."), NINO),
        S('physique_chimie', "Sciences · l'anémomètre", N(
            "L'anémomètre a un rayon de 5 cm et supporte au plus 50 tours par seconde. Quelle vitesse du vent, en m/s, peut-il mesurer au maximum ? (π ≈ 3)", 15,
            "Un tour = 2πr = 2 × 3 × 0,05 = 0,3 m. 50 tours par seconde : 50 × 0,3 = 15 m/s. Les rafales annoncées (environ 18 m/s) dépassent cette limite : l'anémomètre ne les supportera pas."), NINO),
        S('technologie', "Sciences · la station météorologique", Q(
            "Quel est le rôle de l'anémomètre dans la station météorologique ?",
            ["Mesurer la vitesse du vent", "Mesurer la température de l'air", "Mesurer la quantité de pluie", "Mesurer la pression atmosphérique"], "Mesurer la vitesse du vent",
            "Ses coupelles tournent d'autant plus vite que le vent est fort. Le thermomètre mesure la température, le pluviomètre les précipitations, le baromètre la pression."), NINO),
        S('technologie', 'Sciences · la station météorologique', Q(
            "Dans la maquette Arduino, quel élément est un capteur ?",
            ["Le capteur de température", "Le buzzer", "Le voyant lumineux", "La pile"], "Le capteur de température",
            "Les capteurs (température, anémomètre) acquièrent l'information ; la carte Arduino la traite ; le buzzer et le voyant sont des actionneurs (ils signalent) ; la pile alimente."), NINO),
        S('technologie', 'Sciences · la station météorologique', Q(
            "Quel algorithme avertit quand la température de l'air dépasse 26 °C ?",
            ["Répéter : mesurer la température ; si température > 26 °C alors allumer le voyant, sinon l'éteindre", "Allumer le voyant puis mesurer la température une seule fois", "Si température < 26 °C alors allumer le voyant", "Faire sonner le buzzer toutes les 26 secondes"],
            "Répéter : mesurer la température ; si température > 26 °C alors allumer le voyant, sinon l'éteindre",
            "La mesure doit être répétée en boucle ; la condition compare la valeur mesurée au seuil de 26 °C, température au-delà de laquelle les cyclones s'intensifient."), NINO),
        S('svt', 'Sciences · El Niño et les anchois', Q(
            "Pourquoi El Niño fait-il diminuer les anchois au large du Pérou ?",
            ["Les alizés faiblissent, l'upwelling diminue : moins de nutriments, donc moins de plancton dont dépendent les anchois", "L'eau chaude tue directement tous les anchois", "Les pêcheurs pêchent davantage pendant El Niño", "Les anchois migrent vers l'Australie pour se reproduire"],
            "Les alizés faiblissent, l'upwelling diminue : moins de nutriments, donc moins de plancton dont dépendent les anchois",
            "Chaîne alimentaire : phytoplancton → zooplancton → anchois. Moins de remontée d'eaux froides riches en nutriments, c'est moins de phytoplancton à la base de la chaîne."), NINO),
        S('svt', 'Sciences · relations entre espèces', Q(
            "Dans la simulation, les raies dévorent des crevettes grises. Quelle est la relation entre ces deux espèces ?",
            ["Une relation proie-prédateur : la raie est le prédateur, la crevette la proie", "Une symbiose", "Une compétition pour la nourriture", "Un parasitisme"],
            "Une relation proie-prédateur : la raie est le prédateur, la crevette la proie",
            "Le prédateur se nourrit de la proie ; l'effectif de chacune dépend de l'autre."), NINO),
        S('svt', "Sciences · l'équilibre d'un écosystème", N(
            "Simulation : 4 raies et 32 crevettes adultes. Chaque couple de crevettes pond 1 larve ; chaque raie mange 1/8 des crevettes adultes ; une raie juvénile naît pour 8 crevettes mangées ; la moitié des raies adultes meurt ; les juvéniles deviennent adultes. Combien y a-t-il de crevettes adultes après un trimestre ?", 32,
            "16 couples → 16 larves. Chaque raie mange 4 crevettes : 16 mangées, il en reste 16. 16 + 16 larves devenues adultes = 32 crevettes. Côté raies : 2 juvéniles naissent, 2 adultes survivent, soit 4. On retrouve l'état de départ : l'écosystème est à l'équilibre."), NINO),
        # ── Arts ──
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "Quel procédé plastique principal Claes Oldenburg et Coosje van Bruggen utilisent-ils dans « Bicyclette ensevelie » (1990) ?",
            ["Le changement d'échelle : un objet du quotidien agrandi à une taille monumentale", "La miniaturisation d'un objet", "L'abstraction géométrique", "Le trompe-l'œil peint sur toile"],
            "Le changement d'échelle : un objet du quotidien agrandi à une taille monumentale",
            "Roue, guidon, selle et pédale émergent du sol du parc de la Villette sur 46 m : l'objet banal devient sculpture, et le spectateur imagine la bicyclette enfouie."),
          "Œuvre du sujet : Claes Oldenburg et Coosje van Bruggen, « Bicyclette ensevelie », 1990, parc de la Villette, Paris (acier, aluminium, plastique, peinture)."),
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "À quel mouvement artistique est associé Claes Oldenburg ?",
            ["Le pop art", "L'impressionnisme", "Le cubisme", "Le surréalisme"], "Le pop art",
            "Le pop art (années 1960) s'empare des objets de consommation et de la culture populaire. Oldenburg est célèbre pour ses sculptures molles et géantes d'objets ordinaires."), None),
        S('arts', 'Éducation musicale · la virtuosité romantique', Q(
            "Le sujet présente une caricature de Franz Liszt. Qui est-il ?",
            ["Un pianiste virtuose et compositeur romantique du XIXe siècle", "Un chef d'orchestre baroque", "Un compositeur de musique de film", "Un violoniste classique du XVIIIe siècle"],
            "Un pianiste virtuose et compositeur romantique du XIXe siècle",
            "Liszt (1811-1886) a fait du récital de piano un spectacle : il incarne la figure du virtuose romantique, admiré comme un « dieu », décrite dans le texte de Léo-Pol Morin."),
          "Documents du sujet : un texte de Léo-Pol Morin sur le virtuose (1946) et une caricature de Franz Liszt (La vie parisienne, 1886)."),
        S('arts', 'Éducation musicale · la virtuosité romantique', Q(
            "Pour quel instrument Chopin a-t-il écrit sa Ballade n° 1 ?",
            ["Le piano seul", "Le violon et l'orchestre", "La voix et le piano", "L'orgue"], "Le piano seul",
            "Frédéric Chopin (1810-1849) a écrit presque toute son œuvre pour le piano. La virtuosité de la Ballade n° 1 s'entend dans les traits rapides, les contrastes de nuances et la coda très agitée."),
          "Question du sujet : « Selon vous, comment s'exprime la virtuosité dans la ballade n° 1 de Chopin ? »"),
        # ── Anglais ──
        S('anglais', 'Anglais · compréhension', Q(
            "Who is Tina Farr?", ["The headteacher of an Oxford primary school", "A year 2 pupil", "A journalist at The Guardian", "A neuroscientist"], "The headteacher of an Oxford primary school",
            "« When Tina Farr visits the year 2 classroom at her Oxford primary school… », « the headteacher says »."), GUARDIAN),
        S('anglais', 'Anglais · compréhension', Q(
            "In the British school system, when does play-based learning usually stop?",
            ["When children leave reception, the first year of primary school", "At the end of secondary school", "When children are ten", "It never stops"],
            "When children leave reception, the first year of primary school",
            "« Play-based learning […] usually stops when they leave reception. Lessons then become desk-based, focused on reading and writing. »"), GUARDIAN),
        S('anglais', 'Anglais · compréhension', Q(
            "What does Tina Farr notice in the year 2 classroom since play came back?",
            ["Energy, children working together and making things", "Silence and children sitting at their desks", "Children who refuse to read", "More homework for the pupils"],
            "Energy, children working together and making things",
            "« I just feel the energy. The children come running up with things they have made […] They are always working together. »"), GUARDIAN),
        S('anglais', 'Anglais · compréhension', Q(
            "Why did Tina Farr feel free to change the way her school teaches?",
            ["The national curriculum says schools are free to arrange the school day as they like", "Parents asked her to remove reading lessons", "The government ordered all schools to use play", "Her school does not follow the national curriculum"],
            "The national curriculum says schools are free to arrange the school day as they like",
            "« It says we are free to arrange the school day any way we like – it actually says that at point 3.4 in the national curriculum. »"), GUARDIAN),
        S('anglais', 'Anglais · compréhension', Q(
            "“If a time traveller arrived from Victorian times into a school, they would recognise it immediately.” What does it mean?",
            ["Schools have hardly changed since the 19th century, although knowledge about the brain has", "Victorian schools used play-based learning", "Schools are full of old buildings", "Time travel will soon be taught at school"],
            "Schools have hardly changed since the 19th century, although knowledge about the brain has",
            "Farr believes « the outdated system needs to urgently change »: the world and neuroscience have changed, classrooms have not."), GUARDIAN),
        S('anglais', 'Anglais · lexique', Q(
            "In “there is always a shop on the go so they will be pricing up something or finding change”, what does “change” mean?",
            ["The money given back after paying", "A transformation", "Different clothes", "A new teacher"], "The money given back after paying",
            "Dans le jeu de la marchande, les élèves calculent les prix et rendent la monnaie (« change ») : on apprend les mathématiques en jouant."), GUARDIAN),
        # ── Compléments (mêmes documents) ──
        S('physique_chimie', "Sciences · les états de l'eau", Q(
            "Quand la température de l'océan s'élève, l'évaporation s'intensifie. Qu'est-ce que l'évaporation ?",
            ["Le passage lent de l'état liquide à l'état gazeux, à la surface du liquide", "Le passage de l'état gazeux à l'état liquide", "Le passage de l'état solide à l'état liquide", "Une transformation chimique de l'eau"],
            "Le passage lent de l'état liquide à l'état gazeux, à la surface du liquide",
            "La vapeur d'eau monte, se refroidit, puis se condense en gouttelettes (liquéfaction) qui forment les nuages."), NINO),
        S('physique_chimie', "Sciences · l'anémomètre", N(
            "Météo France annonce des rafales à 65 km/h. Combien cela fait-il en m/s, arrondi à l'unité ?", 18,
            "65 km/h = 65 000 m ÷ 3 600 s ≈ 18 m/s. Pour passer des km/h aux m/s, on divise par 3,6.", tol=0.5), NINO),
        S('technologie', 'Sciences · la station météorologique', Q(
            "Dans la maquette, quel est le rôle du buzzer ?",
            ["C'est un actionneur : il émet un son pour avertir quand l'anémomètre tourne trop vite", "C'est un capteur de vitesse", "Il fournit l'énergie électrique", "Il mesure la température"],
            "C'est un actionneur : il émet un son pour avertir quand l'anémomètre tourne trop vite",
            "Le buzzer et le voyant lumineux sont des actionneurs de signalisation ; ils sont commandés par la carte Arduino à partir des informations des capteurs."), NINO),
        S('technologie', 'Sciences · la station météorologique', Q(
            "Dans la maquette, quel est le rôle de la pile ?",
            ["Alimenter le système en énergie électrique", "Mesurer la vitesse du vent", "Stocker le programme", "Émettre un signal sonore"], "Alimenter le système en énergie électrique",
            "Un système technique a une chaîne d'énergie (alimenter, distribuer, convertir) et une chaîne d'information (acquérir, traiter, communiquer)."), NINO),
        S('svt', 'Sciences · El Niño et les anchois', Q(
            "Qu'est-ce que l'upwelling ?",
            ["La remontée d'eaux profondes, froides et riches en nutriments, vers la surface", "Une tempête tropicale", "Le réchauffement des eaux de surface", "La migration des anchois vers le large"],
            "La remontée d'eaux profondes, froides et riches en nutriments, vers la surface",
            "Au large du Pérou, les alizés poussent les eaux chaudes vers l'ouest et provoquent cette remontée, « indispensable à la biodiversité marine »."), NINO),
        S('svt', 'Sciences · El Niño et les anchois', Q(
            "Dans la chaîne alimentaire phytoplancton → zooplancton → anchois, quel est le rôle du phytoplancton ?",
            ["C'est un producteur primaire : il fabrique sa matière organique par photosynthèse", "C'est un prédateur des anchois", "C'est un décomposeur", "C'est un consommateur secondaire"],
            "C'est un producteur primaire : il fabrique sa matière organique par photosynthèse",
            "Les flèches d'une chaîne alimentaire signifient « est mangé par ». Le phytoplancton est à la base : moins de nutriments, moins de phytoplancton, donc moins d'anchois."), NINO),
        S('emc', 'EMC · laïcité et discriminations', Q(
            "En quelle année la Charte de la laïcité à l'École a-t-elle été publiée et affichée dans les établissements publics ?",
            ["2013", "1905", "1882", "2004"], "2013",
            "Ses 15 articles rappellent que la laïcité garantit la liberté de conscience et l'égalité de tous, et refuse toute discrimination."), None),
        S('emc', 'EMC · laïcité et discriminations', Q(
            "Qu'est-ce qu'une discrimination ?",
            ["Traiter une personne de façon défavorable en raison d'un critère interdit par la loi (origine, sexe, religion, handicap…)", "Refuser de prêter son matériel", "Être en désaccord avec quelqu'un", "Donner une mauvaise note justifiée"],
            "Traiter une personne de façon défavorable en raison d'un critère interdit par la loi (origine, sexe, religion, handicap…)",
            "La loi énumère plus de vingt critères de discrimination. À l'école, la laïcité et l'égalité de traitement protègent chaque élève."), None),
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "Où se trouve « Bicyclette ensevelie » d'Oldenburg et van Bruggen ?",
            ["Au parc de la Villette, à Paris", "Au musée du Louvre", "Devant le Centre Pompidou-Metz", "Au jardin des Tuileries"], "Au parc de la Villette, à Paris",
            "L'œuvre est installée en plein air depuis 1990 : l'espace public fait partie de l'œuvre, que l'on parcourt comme un paysage."), None),
    ]),
]

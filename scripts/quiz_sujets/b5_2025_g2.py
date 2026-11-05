# Bac+5, session 2025, groupement 2
from slib import S, Q, N, C, epreuve

COLETTE = ("Texte : Colette, Les Heures longues (articles publiés de 1914 à 1917). À Saint-Malo, en août 1914, la population "
           "apprend la mobilisation générale.")
BEURRE = ("Exercice 2 : Claire fabrique du beurre. 8 L de lait donnent 1 L de crème ; 3 L de crème donnent 1 kg de beurre. "
          "Elle a 248 vaches, qui fournissent chacune 30 L de lait par jour.")
SAUT = ("Exercice 3 : saut en longueur. À chaque saut, « toucher la planche », « dépasser la planche » et « réussir le saut » sont équiprobables ; "
        "les sauts sont indépendants. L'athlète « mord » s'il touche ou dépasse la planche. Il fait deux sauts.")
OCEAN = "Sujet de sciences et technologie : l'océan, réservoir de biodiversité, ressource à préserver et réseau mondial de communication."
FRANCOIS = "Sujet d'histoire et EMC : en CM1, François Ier et la construction du royaume de France ; puis l'empathie contre le harcèlement."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 16573, [
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« Les détails de cette heure me sont pénibles, comme ceux d'un rêve que je voudrais ensemble quitter et poursuivre. » Temps et mode de « voudrais » ?",
            ["Conditionnel présent", "Imparfait de l'indicatif", "Futur simple", "Subjonctif présent"], "Conditionnel présent",
            "Terminaison -rais sur le radical du futur (voudr-) : conditionnel présent, rangé parmi les temps de l'indicatif dans la terminologie actuelle."), COLETTE),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« Des gens l'escaladent, […] comme s'ils avaient grimpé sur un mur. » Temps et mode de « avaient grimpé » ?",
            ["Plus-que-parfait de l'indicatif", "Passé composé de l'indicatif", "Conditionnel passé", "Passé antérieur"], "Plus-que-parfait de l'indicatif",
            "Auxiliaire avoir à l'imparfait + participe passé. Après « comme si », on emploie l'imparfait ou le plus-que-parfait, jamais le conditionnel."), COLETTE),
        S('francais', 'Étude de la langue · propositions', Q(
            "« On n'écoute pas ce qu'il lit parce qu'on le sait. » Nature et fonction de « parce qu'on le sait » ?",
            ["Subordonnée conjonctive circonstancielle de cause, complément de phrase", "Subordonnée relative, complément du nom", "Subordonnée complétive, COD", "Proposition indépendante"],
            "Subordonnée conjonctive circonstancielle de cause, complément de phrase",
            "« Parce que » introduit la cause. « Ce qu'il lit », introduit par le pronom relatif « que » avec l'antécédent « ce », est COD de « écoute »."), COLETTE),
        S('francais', 'Étude de la langue · réécriture', Q(
            "Au singulier : « Des adolescents pâlissent et regardent devant eux en somnambules. »",
            ["Un adolescent pâlit et regarde devant lui en somnambule.", "Un adolescent pâlissent et regarde devant lui en somnambule.", "Un adolescent pâlit et regarde devant eux en somnambules.", "L'adolescent pâlissait et regardait devant lui en somnambule."],
            "Un adolescent pâlit et regarde devant lui en somnambule.",
            "« Pâlir » est un verbe du 2e groupe : il pâlit / ils pâlissent. « Eux » devient « lui » et « somnambules » passe au singulier. Le temps ne change pas."), COLETTE),
        S('francais', 'Étude de la langue · réécriture', Q(
            "Au pluriel : « L'automobile qui nous porte s'arrête, étroitement insérée dans la foule qui se fige contre ses roues. »",
            ["Les automobiles qui nous portent s'arrêtent, étroitement insérées dans la foule qui se fige contre leurs roues.",
             "Les automobiles qui nous portent s'arrêtent, étroitement insérés dans la foule qui se figent contre leurs roues.",
             "Les automobiles qui nous porte s'arrêtent, étroitement insérées dans les foules qui se figent contre leur roues.",
             "Les automobiles qui nous portent s'arrête, étroitement insérées dans la foule qui se fige contre ses roues."],
            "Les automobiles qui nous portent s'arrêtent, étroitement insérées dans la foule qui se fige contre leurs roues.",
            "« Automobile » est féminin : « insérées ». « La foule » reste au singulier, donc « se fige ». « Ses roues » devient « leurs roues »."), COLETTE),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé « avidement », et que signifie-t-il ?",
            ["Adjectif « avide » + suffixe -ment : avec avidité, ardemment", "Préfixe a- + « videment » : sans rien", "Nom « avidité » + suffixe -ment", "Verbe « vider » + suffixe -ment"],
            "Adjectif « avide » + suffixe -ment : avec avidité, ardemment",
            "Le suffixe -ment, ajouté à un adjectif (souvent au féminin), forme un adverbe de manière."), COLETTE),
        S('francais', 'Lexique · sens en contexte', Q(
            "Dans « les rues étranglées », quel est le sens de « étranglées » ?",
            ["Très étroites, resserrées (par la foule)", "Où l'on a commis un crime", "Bruyantes", "Désertes"], "Très étroites, resserrées (par la foule)",
            "Sens figuré : les rues semblent serrées comme une gorge qu'on étrangle, une image qui dit aussi l'angoisse de la population à l'annonce de la guerre."), COLETTE),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16576, [
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « 35/7 n'est pas un nombre décimal. » Vrai ou faux ?",
            ["Faux : 35/7 = 5, un entier, donc un décimal", "Vrai : c'est une fraction", "Vrai : 7 n'est pas une puissance de 10", "Faux : 35/7 = 0,5"], "Faux : 35/7 = 5, un entier, donc un décimal",
            "Tout entier est décimal (5 = 5/10⁰). On regarde la fraction simplifiée, pas son écriture de départ."), None),
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « La somme de sept nombres entiers consécutifs est un multiple de 7. » Vrai ou faux ?",
            ["Vrai : n + (n + 1) + … + (n + 6) = 7n + 21 = 7(n + 3)", "Faux : 1 + 2 + … + 7 = 28", "Vrai, mais seulement si n est pair", "Faux : cela dépend du premier nombre"], "Vrai : n + (n + 1) + … + (n + 6) = 7n + 21 = 7(n + 3)",
            "Le calcul littéral prouve le cas général. (28 est d'ailleurs bien un multiple de 7.)"), None),
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Un nombre parfait est égal à la somme de ses diviseurs stricts (6 = 1 + 2 + 3). Affirmation : « 496 est un nombre parfait. » Vrai ou faux ?",
            ["Vrai", "Faux"], "Vrai",
            "Diviseurs stricts de 496 = 2⁴ × 31 : 1, 2, 4, 8, 16, 31, 62, 124, 248. Leur somme vaut 496."), None),
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « Pour tout réel positif x, √x ≤ x. » Vrai ou faux ?",
            ["Faux : √0,25 = 0,5 > 0,25", "Vrai", "Faux : √4 = 2 < 4", "Vrai, car la racine carrée diminue toujours"], "Faux : √0,25 = 0,5 > 0,25",
            "Entre 0 et 1, la racine carrée d'un nombre est plus grande que ce nombre. Un contre-exemple suffit (√4 = 2 < 4 ne prouve rien)."), None),
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « Tout rectangle a pour axes de symétrie ses diagonales. » Vrai ou faux ?",
            ["Faux : ses axes sont les médiatrices de ses côtés (sauf pour le carré)", "Vrai", "Faux : un rectangle n'a aucun axe de symétrie", "Vrai pour les rectangles très allongés"], "Faux : ses axes sont les médiatrices de ses côtés (sauf pour le carré)",
            "Un rectangle (non carré) a deux axes de symétrie : les médiatrices de ses côtés. Seul le carré a en plus ses diagonales pour axes."), None),
        S('mathematiques', 'Exercice 2 · proportionnalité', N(
            "Quelle masse de beurre, en kg, Claire peut-elle produire par jour avec tout son lait ?", 310,
            "Lait : 248 × 30 = 7 440 L. Crème : 7 440 ÷ 8 = 930 L. Beurre : 930 ÷ 3 = 310 kg."), BEURRE),
        S('mathematiques', 'Exercice 2 · pourcentages', N(
            "Passer de 8 L de lait à 1 L de crème : de quel pourcentage le volume diminue-t-il ?", 87.5,
            "Il reste 1/8 = 12,5 % du volume : la réduction est de 100 − 12,5 = 87,5 %."), BEURRE),
        S('mathematiques', 'Exercice 2 · aires', Q(
            "Une plaquette de beurre est un pavé de 10 cm × 6,5 cm × 3,5 cm. Quelle est l'aire totale de ses faces ?",
            ["245,5 cm²", "227,5 cm²", "122,75 cm²", "460 cm²"], "245,5 cm²",
            "A = 2 × (10 × 6,5 + 10 × 3,5 + 6,5 × 3,5) = 2 × (65 + 35 + 22,75) = 245,5 cm². 227,5 cm³ est son volume."), None),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "Quelle est la probabilité que l'athlète réussisse ses deux sauts ?",
            ["1/9", "1/3", "2/9", "1/6"], "1/9",
            "Réussir un saut : 1/3 (un cas sur trois équiprobables). Deux sauts indépendants : 1/3 × 1/3 = 1/9."), SAUT),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "Quelle est la probabilité qu'il « morde » au moins une fois ?",
            ["8/9", "4/9", "2/3", "5/9"], "8/9",
            "Événement contraire de « réussir les deux sauts » : 1 − 1/9 = 8/9. Mordre exactement une fois : 2 × 2/3 × 1/3 = 4/9."), SAUT),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 16570, [
        # ── Sciences ──
        S('svt', 'Sciences · la classification', Q(
            "Quelle différence y a-t-il entre trier, ranger et classer ?",
            ["Trier : séparer selon un critère ; ranger : ordonner selon une grandeur ; classer : regrouper selon des attributs partagés", "Ce sont trois synonymes", "Classer : ordonner du plus petit au plus grand", "Ranger : regrouper selon des attributs"],
            "Trier : séparer selon un critère ; ranger : ordonner selon une grandeur ; classer : regrouper selon des attributs partagés",
            "Faire distinguer ces trois verbes aux élèves prépare la classification scientifique, qui regroupe les espèces en groupes emboîtés."), OCEAN),
        S('svt', 'Sciences · les relations entre êtres vivants', Q(
            "Dans les chaînes alimentaires marines, quel rôle jouent la laitue de mer et le phytoplancton ?",
            ["Producteurs primaires : ils fabriquent leur matière organique par photosynthèse", "Prédateurs", "Décomposeurs", "Consommateurs secondaires"], "Producteurs primaires : ils fabriquent leur matière organique par photosynthèse",
            "Ils sont le premier maillon des chaînes alimentaires : tous les autres êtres vivants en dépendent directement ou indirectement."), OCEAN),
        S('svt', 'Sciences · les relations entre êtres vivants', Q(
            "Lequel de ces exemples illustre une relation autre que la prédation ?",
            ["Le poisson-clown et l'anémone de mer, qui vivent en symbiose", "La mouette qui mange un poisson", "Le phoque qui chasse le hareng", "La baleine qui avale du krill"], "Le poisson-clown et l'anémone de mer, qui vivent en symbiose",
            "Autres relations : symbiose ou mutualisme (chacun y gagne), parasitisme, compétition pour une ressource."), OCEAN),
        S('physique_chimie', "Sciences · le dessalement de l'eau de mer", Q(
            "Dans quel ordre les changements d'état ont-ils lieu lors d'une distillation ?",
            ["Vaporisation, puis liquéfaction (condensation)", "Fusion, puis solidification", "Liquéfaction, puis vaporisation", "Sublimation, puis fusion"], "Vaporisation, puis liquéfaction (condensation)",
            "L'eau salée est chauffée : l'eau se vaporise et le sel reste. La vapeur se refroidit et se liquéfie : on recueille de l'eau douce."), OCEAN),
        S('physique_chimie', "Sciences · le dessalement de l'eau de mer", Q(
            "Un élève demande : « Peut-on faire fondre du sel dans l'eau dessalée ? » Quelle est l'erreur de vocabulaire ?",
            ["Il faut dire « dissoudre » : le sel se dissout dans l'eau, il ne fond pas", "Il faut dire « évaporer »", "Il faut dire « condenser »", "Il n'y a pas d'erreur"],
            "Il faut dire « dissoudre » : le sel se dissout dans l'eau, il ne fond pas",
            "La fusion est un changement d'état (solide → liquide) sous l'effet de la chaleur. La dissolution est le mélange d'un solide dans un liquide."), OCEAN),
        S('physique_chimie', "Sciences · l'acidification de l'océan", Q(
            "Lequel de ces gaz est, comme le dioxyde de carbone, un gaz à effet de serre ?",
            ["Le méthane", "Le dioxygène", "Le diazote", "L'argon"], "Le méthane",
            "Gaz à effet de serre : dioxyde de carbone, méthane, protoxyde d'azote, vapeur d'eau. Le CO₂ dissous dans l'océan le rend aussi plus acide (le pH baisse)."), OCEAN),
        S('svt', "Sciences · l'élévation du niveau des océans", Q(
            "Quelle cause de l'élévation du niveau des océans est souvent confondue par les élèves ?",
            ["La fonte de la banquise, qui flotte déjà : c'est surtout la fonte des glaces continentales et la dilatation de l'eau qui font monter le niveau", "La pluie", "Les marées", "Les bateaux"],
            "La fonte de la banquise, qui flotte déjà : c'est surtout la fonte des glaces continentales et la dilatation de l'eau qui font monter le niveau",
            "Un glaçon qui fond dans un verre ne fait pas déborder l'eau ; la glace des glaciers et des calottes, posée sur la terre, ajoute de l'eau à l'océan. L'eau qui se réchauffe se dilate aussi."), OCEAN),
        S('technologie', 'Sciences · une bouée communicante', Q(
            "Une bouée mesure la température de l'eau et transmet ses données à terre. Quels éléments assurent ces deux fonctions ?",
            ["Un capteur de température et un émetteur (module de communication sans fil)", "Un moteur et une hélice", "Une batterie et un panneau solaire", "Un flotteur et une ancre"],
            "Un capteur de température et un émetteur (module de communication sans fil)",
            "Chaîne d'information : acquérir (capteur), traiter (carte programmable), communiquer (émetteur). La batterie et le panneau solaire assurent l'alimentation."), OCEAN),
        S('technologie', 'Sciences · la démarche technologique', Q(
            "Quelle est la première étape de la démarche technologique pour concevoir une bouée en classe ?",
            ["Étudier le cahier des charges : le besoin et les contraintes", "Programmer la carte", "Peindre la bouée", "Tester la bouée dans l'eau"], "Étudier le cahier des charges : le besoin et les contraintes",
            "Puis on recherche des solutions, on conçoit, on réalise un prototype, on le teste et on le valide au regard du cahier des charges."), OCEAN),
        # ── Histoire et EMC ──
        S('histoire_geographie', 'Histoire · François Ier', Q(
            "Que décide l'ordonnance de Villers-Cotterêts (1539) ?",
            ["Les actes officiels et de justice doivent être rédigés en français, et les curés doivent tenir des registres des baptêmes", "L'école devient obligatoire", "La religion protestante est interdite", "Le roi partage son pouvoir avec un parlement élu"],
            "Les actes officiels et de justice doivent être rédigés en français, et les curés doivent tenir des registres des baptêmes",
            "Elle renforce l'unité du royaume et l'administration royale : c'est l'un des documents du dossier sur la construction du royaume par François Ier."), FRANCOIS),
        S('histoire_geographie', 'Histoire · François Ier', Q(
            "Quelle victoire marque le début du règne de François Ier, en 1515 ?",
            ["Marignan", "Azincourt", "Bouvines", "Austerlitz"], "Marignan",
            "Bouvines (1214) est une victoire de Philippe Auguste ; Azincourt (1415), une défaite française ; Austerlitz (1805), une victoire de Napoléon."), FRANCOIS),
        S('histoire_geographie', 'Histoire · François Ier', Q(
            "Quel château de la Loire, dont le dossier présentait le plan, François Ier fait-il construire ?",
            ["Chambord", "Versailles", "Le Louvre", "Fontainebleau"], "Chambord",
            "Chambord, commencé en 1519, illustre la Renaissance et le prestige du roi, mécène qui accueille aussi Léonard de Vinci."), FRANCOIS),
        S('emc', "EMC · l'empathie", Q(
            "Pourquoi l'empathie est-elle un « moteur pour lutter contre les discriminations, la violence et le harcèlement » ?",
            ["Comprendre ce que ressent l'autre aide à ne pas lui nuire et à le défendre", "Elle oblige à aimer tout le monde", "Elle remplace les règles de l'école", "Elle punit les harceleurs"],
            "Comprendre ce que ressent l'autre aide à ne pas lui nuire et à le défendre",
            "Elle est travaillée en CM1 avec les notions de fraternité et d'égalité. Le dossier proposait un « kit empathie » (2024) et une affiche primée au prix « Non au harcèlement »."), FRANCOIS),
        S('emc', "EMC · l'empathie", Q(
            "Qu'est-ce qu'une communication empathique ?",
            ["Écouter l'autre, reformuler ce qu'il ressent et exprimer ses propres émotions sans l'attaquer", "Parler le plus fort possible", "Donner raison à tout le monde", "Éviter de parler de ses émotions"],
            "Écouter l'autre, reformuler ce qu'il ressent et exprimer ses propres émotions sans l'attaquer",
            "En classe : messages clairs (« je me sens… quand… »), cercles de parole, jeux de rôle."), FRANCOIS),
        # ── Arts ──
        S('arts', 'Arts plastiques · expression des émotions', Q(
            "Jean Tinguely, présent dans le dossier avec Picasso, est connu pour :",
            ["Ses sculptures-machines animées, faites d'objets récupérés", "Ses peintures de nymphéas", "Ses portraits de la Renaissance", "Ses photographies de mode"],
            "Ses sculptures-machines animées, faites d'objets récupérés",
            "Tinguely (1925-1991), artiste suisse du Nouveau Réalisme, a créé avec Niki de Saint Phalle la fontaine Stravinsky, à Paris."),
          "Dossier d'arts plastiques (cycle 2) : « L'expression des émotions », expérimenter les couleurs, les matériaux et les supports."),
        S('arts', 'Éducation musicale · chanter et interpréter', Q(
            "Que signifie « reproduire un modèle rythmique », au programme du cycle 3 ?",
            ["Répéter fidèlement une suite de durées (frappée, parlée ou chantée) proposée par un modèle", "Inventer une mélodie", "Écrire une partition", "Chanter le plus fort possible"],
            "Répéter fidèlement une suite de durées (frappée, parlée ou chantée) proposée par un modèle",
            "Le sujet demandait une analyse critique d'une séance de 30 minutes sur les compétences « chanter et interpréter » et « écouter, comparer et commenter »."), None),
    ]),
    # ── Ajout : questions complémentaires tirées du même sujet ──
    epreuve('Épreuve écrite disciplinaire de français', 16573, [
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« Des gens l'escaladent, pour mieux voir et entendre. » Temps et mode de « escaladent » ?",
            ["Présent de l'indicatif", "Présent du subjonctif", "Imparfait de l'indicatif", "Impératif présent"], "Présent de l'indicatif",
            "Présent de narration, qui rend la scène vivante. Au subjonctif, ce serait aussi « escaladent » : seul le contexte (aucune subordination) tranche."), COLETTE),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« Dans quelques jours, qui saura si ceci est tien ou mien ? » Temps et mode de « saura » ?",
            ["Futur simple de l'indicatif", "Conditionnel présent", "Passé simple", "Présent du subjonctif"], "Futur simple de l'indicatif",
            "Verbe savoir au futur : je saurai, il saura. Le conditionnel serait « saurait »."), COLETTE),
        S('francais', 'Étude de la langue · type de phrase', Q(
            "« Dans quelques jours, qui saura si ceci est tien ou mien ? » Quel est le type de cette phrase ?",
            ["Interrogative (question rhétorique)", "Déclarative", "Injonctive", "Exclamative"], "Interrogative (question rhétorique)",
            "Le pronom interrogatif « qui » et le point d'interrogation en font une phrase interrogative ; elle n'attend pas de réponse et exprime l'inquiétude devant la guerre."), COLETTE),
        S('francais', 'Étude de la langue · nature des mots', Q(
            "« C'était pourtant la guerre, cette Cancalaise dure… » Nature de « pourtant » ?",
            ["Adverbe (de liaison, à valeur d'opposition)", "Conjonction de coordination", "Préposition", "Adjectif"], "Adverbe (de liaison, à valeur d'opposition)",
            "« Pourtant » est un adverbe connecteur d'opposition ; il n'appartient pas à la liste des conjonctions de coordination (mais, ou, et, donc, or, ni, car)."), COLETTE),
        S('francais', 'Lexique · sens en contexte', Q(
            "Dans « les journaux assoupis de l'été », que signifie « assoupis » ?",
            ["Calmes, sans grandes nouvelles, comme endormis", "Imprimés la nuit", "Mouillés par la pluie", "Interdits par la censure"], "Calmes, sans grandes nouvelles, comme endormis",
            "C'est une personnification : avant la mobilisation d'août 1914, l'actualité estivale semble dormir."), COLETTE),
        S('francais', 'Lexique · champ lexical des émotions', Q(
            "À l'annonce de la mobilisation générale, quelles émotions le texte prête-t-il à la population ?",
            ["Stupeur, angoisse et gravité (des adolescents pâlissent, regardent « en somnambules »)", "Joie et enthousiasme", "Indifférence totale", "Colère contre le maire"],
            "Stupeur, angoisse et gravité (des adolescents pâlissent, regardent « en somnambules »)",
            "Le sujet demandait d'identifier ces émotions à partir du lexique : pâlir, somnambules, les détails « pénibles »…"), COLETTE),
        S('francais', 'Culture littéraire · Colette', Q(
            "En quelle année a lieu la mobilisation générale décrite par Colette dans « Les Heures longues » ?",
            ["1914", "1939", "1870", "1918"], "1914",
            "Le 1er août 1914, l'ordre de mobilisation générale annonce l'entrée de la France dans la Première Guerre mondiale."), None),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 16576, [
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « 22,9 est un nombre rationnel. » Vrai ou faux ?",
            ["Vrai : 22,9 = 229/10", "Faux : c'est un décimal", "Faux : il a une virgule", "Vrai seulement s'il est entier"], "Vrai : 22,9 = 229/10",
            "Tout décimal est rationnel : il s'écrit comme quotient de deux entiers. Les ensembles sont emboîtés : entiers ⊂ décimaux ⊂ rationnels."), None),
        S('mathematiques', 'Exercice 2 · volumes', N(
            "Quel est le volume d'une plaquette de beurre de 10 cm × 6,5 cm × 3,5 cm, en cm³ ?", 227.5,
            "Volume d'un pavé : longueur × largeur × hauteur = 10 × 6,5 × 3,5 = 227,5 cm³."), None),
        S('mathematiques', 'Exercice 2 · masse volumique', Q(
            "Une plaquette de 250 g a un volume de 227,5 cm³. Comparez la masse volumique du beurre à celle du lait (1,03 kg/L).",
            ["Le beurre est plus dense : environ 1,10 kg/L", "Le beurre est moins dense : environ 0,91 kg/L", "Ils ont la même masse volumique", "On ne peut pas comparer"], "Le beurre est plus dense : environ 1,10 kg/L",
            "250 ÷ 227,5 ≈ 1,10 g/cm³, soit 1,10 kg/L, plus que 1,03 kg/L."), None),
        S('mathematiques', 'Exercice 2 · pourcentages', Q(
            "L'aire de la plaquette (245,5 cm²) représente-t-elle au moins 60 % de la feuille de 23 cm × 20 cm ?",
            ["Non : environ 53 %", "Oui : environ 65 %", "Oui : exactement 60 %", "Non : environ 10 %"], "Non : environ 53 %",
            "Feuille : 23 × 20 = 460 cm². 245,5 ÷ 460 ≈ 0,534, soit environ 53 %."), None),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "Quelle est la probabilité que l'athlète « morde » au premier saut et réussisse le second ?",
            ["2/9", "1/9", "4/9", "1/3"], "2/9",
            "Mordre (toucher ou dépasser) : 2/3. Réussir : 1/3. Sauts indépendants : 2/3 × 1/3 = 2/9."), SAUT),
        S('mathematiques', 'Exercice 3 · probabilités', Q(
            "Quelle est la probabilité qu'il « morde » exactement une fois sur les deux sauts ?",
            ["4/9", "2/9", "8/9", "1/3"], "4/9",
            "Mordre puis réussir (2/9) ou réussir puis mordre (2/9) : 4/9."), SAUT),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 16570, [
        S('svt', 'Sciences · la classification', Q(
            "Quel mode de classification scientifique est travaillé en classe avec des groupes emboîtés ?",
            ["La classification phylogénétique, fondée sur les attributs partagés", "La classification alphabétique", "Le classement par milieu de vie", "Le classement par taille"],
            "La classification phylogénétique, fondée sur les attributs partagés",
            "Elle reflète les liens de parenté entre espèces. Elle peut aussi se représenter par un arbre (arbre phylogénétique)."), OCEAN),
        S('svt', 'Sciences · la classification', Q(
            "Quel autre mode de représentation utilise-t-on en classification, à côté des groupes emboîtés ?",
            ["L'arbre phylogénétique", "La frise chronologique", "Le diagramme circulaire", "La carte de géographie"], "L'arbre phylogénétique",
            "Les deux représentations disent la même chose : quels êtres vivants partagent quels attributs."), OCEAN),
        S('physique_chimie', "Sciences · l'acidification de l'océan", Q(
            "Pourquoi réaliser en même temps une expérience et une expérience témoin pour étudier l'acidification ?",
            ["Pour comparer et montrer que seul le facteur étudié (le CO₂) explique la différence", "Pour gagner du temps", "Pour avoir deux résultats identiques", "Pour décorer la classe"],
            "Pour comparer et montrer que seul le facteur étudié (le CO₂) explique la différence",
            "Le témoin est identique en tout sauf sur le facteur testé : sans lui, on ne peut pas conclure."), OCEAN),
        S('physique_chimie', "Sciences · l'acidification de l'océan", Q(
            "Quelle consigne de protection donner aux élèves pour une expérience avec du vinaigre ou de l'eau gazeuse et des coquillages ?",
            ["Porter des lunettes de protection et ne rien goûter", "Aucune", "Chauffer le mélange", "Mélanger avec les doigts"], "Porter des lunettes de protection et ne rien goûter",
            "Même avec des produits courants, on apprend les gestes de sécurité du laboratoire."), OCEAN),
        S('technologie', 'Sciences · une bouée communicante', Q(
            "Une bouée communicante est alimentée par un panneau solaire et une batterie. Quelle est la fonction de la batterie ?",
            ["Stocker l'énergie pour fonctionner la nuit ou par mauvais temps", "Mesurer la température", "Émettre les données", "Faire flotter la bouée"], "Stocker l'énergie pour fonctionner la nuit ou par mauvais temps",
            "Chaîne d'énergie : alimenter (panneau solaire), stocker (batterie), distribuer, convertir."), OCEAN),
        S('technologie', 'Sciences · programmer un système', Q(
            "Un programme doit envoyer une alerte si la température de l'eau dépasse un seuil. Quelle structure faut-il ?",
            ["Une boucle qui répète la mesure, avec une condition « si température > seuil alors envoyer une alerte »", "Une seule mesure au démarrage", "Une boucle sans condition", "Une condition sans mesure"],
            "Une boucle qui répète la mesure, avec une condition « si température > seuil alors envoyer une alerte »",
            "Les erreurs d'élèves analysées dans le sujet portaient sur ce type de programme."), OCEAN),
        S('histoire_geographie', 'Histoire · François Ier', Q(
            "Que dit l'article 111 de l'ordonnance de Villers-Cotterêts ?",
            ["Que les actes de justice soient rédigés « en langage maternel françois et non autrement », et non plus en latin", "Que le roi soit élu", "Que l'école soit obligatoire", "Que le latin devienne la seule langue du royaume"],
            "Que les actes de justice soient rédigés « en langage maternel françois et non autrement », et non plus en latin",
            "L'article 110 veut des actes clairs, sans ambiguïté : le français doit rendre la justice compréhensible par tous."), "Document 4 : ordonnance de Villers-Cotterêts, 25 août 1539, articles 110 et 111."),
        S('histoire_geographie', 'Histoire · François Ier', Q(
            "Comment les historiens qualifient-ils les règnes de François Ier et d'Henri II ?",
            ["Le « premier absolutisme »", "La monarchie parlementaire", "La féodalité", "La République"], "Le « premier absolutisme »",
            "« La volonté du roi est tout désormais », écrit un ambassadeur vénitien en 1546 (document 2). Mais l'application concrète de cette volonté reste limitée."), "Document 2 : Joël Cornette, L'affirmation de l'État absolu 1515-1652."),
        S('histoire_geographie', 'Histoire · François Ier', Q(
            "Quel artiste italien, accueilli par François Ier, aurait inspiré le célèbre escalier à double révolution de Chambord ?",
            ["Léonard de Vinci", "Michel-Ange", "Raphaël", "Botticelli"], "Léonard de Vinci",
            "Chambord associe idées italiennes de la Renaissance et formes françaises « gothiques » : c'est le premier « château absolu » (document 6)."), "Document 6 : Joël Cornette, « Chambord, le premier château absolu »."),
        S('histoire_geographie', 'Histoire · François Ier', Q(
            "Qui a peint le portrait officiel de François Ier conservé au Louvre (vers 1525-1527) ?",
            ["Jean Clouet", "Léonard de Vinci", "Jacques-Louis David", "Hyacinthe Rigaud"], "Jean Clouet",
            "Le portrait montre la majesté du roi : un document à analyser comme une image du pouvoir. Rigaud a peint Louis XIV, David Napoléon."), "Document 3 : Jean Clouet, François Ier, roi de France, vers 1525-1527."),
        S('emc', "EMC · l'empathie", Q(
            "Selon le « kit empathie » (2024), qu'est-ce que la reformulation empathique ?",
            ["Mettre en mots ce que l'autre est en train de vivre et de nous dire", "Répéter mot pour mot ce que dit l'autre", "Donner son avis immédiatement", "Corriger les fautes de l'autre"],
            "Mettre en mots ce que l'autre est en train de vivre et de nous dire",
            "La communication empathique comprend aussi la compréhension empathique, l'écoute silencieuse et l'écoute active (questions ouvertes)."), "Document 9 : Éduscol, kit empathie, volume 1, janvier 2024."),
        S('emc', "EMC · l'empathie", Q(
            "Selon le kit empathie, quel besoin psychologique la communication empathique satisfait-elle ?",
            ["Le besoin de reconnaissance et d'acceptation de soi", "Le besoin de manger", "Le besoin de gagner", "Le besoin de silence"], "Le besoin de reconnaissance et d'acceptation de soi",
            "Se sentir compris renforce l'estime de soi ; reconnaître la détresse de l'autre encourage l'altruisme et la coopération."), "Document 9 : Éduscol, kit empathie."),
        S('emc', "EMC · l'empathie", Q(
            "Qu'est-ce que l'écoute active ?",
            ["Écouter en reformulant et en posant des questions ouvertes", "Écouter en faisant autre chose", "Écouter sans jamais répondre", "Parler en même temps que l'autre"], "Écouter en reformulant et en posant des questions ouvertes",
            "C'est l'un des savoir-faire de la communication empathique à travailler en CM1."), None),
        S('arts', 'Arts plastiques · expression des émotions', Q(
            "En arts plastiques au cycle 2, comment faire exprimer une émotion ?",
            ["En jouant sur les couleurs, les matériaux, les gestes et la composition", "En écrivant le nom de l'émotion", "En recopiant un tableau", "En utilisant une seule couleur imposée"],
            "En jouant sur les couleurs, les matériaux, les gestes et la composition",
            "Point de programme du sujet : « Expérimenter les effets des couleurs, des matériaux, des supports… en explorant l'organisation et la composition plastiques »."), None),
        S('arts', 'Éducation musicale · écouter, comparer', Q(
            "Que signifie « décrire et comparer des éléments sonores issus de contextes variés » ?",
            ["Repérer et nommer des caractéristiques (timbre, tempo, nuances) de sons ou d'œuvres différentes, avec un vocabulaire précis", "Classer les chansons par date", "Chanter plus fort que les autres", "Apprendre le nom des compositeurs"],
            "Repérer et nommer des caractéristiques (timbre, tempo, nuances) de sons ou d'œuvres différentes, avec un vocabulaire précis",
            "C'est l'une des compétences du cycle 3 citées par le sujet pour l'analyse de la séance."), None),
    ]),
]

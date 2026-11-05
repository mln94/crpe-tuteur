# Bac+5, session 2026, session supplémentaire (académies de Créteil, Versailles et Paris)
from slib import S, Q, N, C, epreuve

VERNE = ("Texte : Jules Verne, De la Terre à la Lune (1865). Devant les membres du Gun-Club, désœuvrés depuis la fin de la guerre, "
         "le président Barbicane annonce un projet grandiose : aller sur la Lune.")
SORTIE = ("Exercice 1 : une sortie pour 40 élèves et 4 accompagnateurs, 150 km aller-retour. Transport : compagnie A, 350 € + 1,80 €/km TTC ; "
          "compagnie B, 290 € + 2,45 €/km TTC ; compagnie C, 585 € HT avec une TVA de 10 %. Musée : 35 € par adulte, 23 € par élève. "
          "Repas : 7,95 € par adulte, 4,55 € par élève.")
ALESIA = "Exercice 3 : le siège d'Alésia. Les Romains construisent deux palissades circulaires concentriques, de rayons 2,5 km et 3,4 km."
DES = "Exercice 4 : Soan lance deux dés à six faces ; Thaïs lance un dé à quatre faces et un dé à huit faces. Chacun additionne les deux nombres."
CUBES = "Exercice 5 : un motif de cubes compte 2 cubes à l'étape 1, 5 cubes à l'étape 2 et 10 cubes à l'étape 3."
BLE = "Sujet de sciences et technologie : le cycle de vie du blé, l'agriculture de précision et la fabrication du pain."
EDIT = "Sujet d'histoire et EMC : en CM1, « Henri IV et l'édit de Nantes » ; en CE1, la fraternité, valeur de la République."

QUESTIONS = [
    epreuve('Épreuve écrite disciplinaire de français', 20151, [
        S('francais', 'Étude de la langue · temps, mode et voix', Q(
            "« Barbicane, comme s'il eût été mû par un ressort, se redressa subitement. » Temps, mode et voix de « eût été mû » ?",
            ["Plus-que-parfait du subjonctif, voix passive", "Passé antérieur de l'indicatif, voix active", "Conditionnel passé, voix passive", "Plus-que-parfait de l'indicatif, voix pronominale"],
            "Plus-que-parfait du subjonctif, voix passive",
            "« Eût été » est l'auxiliaire être au plus-que-parfait du subjonctif ; « mû » (participe de mouvoir) marque la voix passive : il est mû par un ressort."), VERNE),
        S('francais', 'Étude de la langue · propositions', Q(
            "Dans la même phrase, quelle est la nature de « comme s'il eût été mû par un ressort » ?",
            ["Subordonnée conjonctive circonstancielle de comparaison", "Subordonnée relative", "Subordonnée circonstancielle de cause", "Subordonnée interrogative indirecte"],
            "Subordonnée conjonctive circonstancielle de comparaison",
            "« Comme si » introduit une comparaison hypothétique. La phrase compte aussi une subordonnée de temps (« Lorsque huit heures sonnèrent… ») et la principale « Barbicane se redressa subitement »."), VERNE),
        S('francais', 'Étude de la langue · les sujets', C(
            "Cliquez sur le sujet du verbe « est résultée ».",
            "J'ai donc cherché, travaillé, calculé, et de mes études est résultée [cette conviction] que nous devons réussir.",
            "Le sujet est inversé : qu'est-ce qui est résulté ? « cette conviction (que nous devons réussir…) ». Le participe s'accorde avec lui : « résultée », au féminin."), VERNE),
        S('francais', 'Étude de la langue · temps, mode et voix', Q(
            "« Il n'est aucun de vous qui n'ait vu la Lune. » Temps et mode de « ait vu » ?",
            ["Passé du subjonctif", "Passé composé de l'indicatif", "Plus-que-parfait du subjonctif", "Conditionnel passé"], "Passé du subjonctif",
            "Auxiliaire avoir au subjonctif présent (ait) + participe passé. Le subjonctif s'explique par la relative après une principale négative (« il n'est aucun de vous qui… »)."), VERNE),
        S('francais', 'Étude de la langue · discours indirect', Q(
            "Au discours indirect : « Depuis quelques mois, mes braves collègues, je me suis demandé si nous ne pourrions pas entreprendre quelque grande expérience. » Quelle transposition est correcte ?",
            ["Barbicane déclara à ses braves collègues que, depuis quelques mois, il s'était demandé s'ils ne pourraient pas entreprendre quelque grande expérience.",
             "Barbicane déclara à ses braves collègues que, depuis quelques mois, je me suis demandé si nous ne pourrions pas entreprendre quelque grande expérience.",
             "Barbicane déclara à ses braves collègues que, depuis quelques mois, il se demande s'ils ne peuvent pas entreprendre quelque grande expérience.",
             "Barbicane déclara à ses braves collègues : depuis quelques mois, il s'était demandé s'ils ne pourraient pas entreprendre quelque grande expérience."],
            "Barbicane déclara à ses braves collègues que, depuis quelques mois, il s'était demandé s'ils ne pourraient pas entreprendre quelque grande expérience.",
            "Verbe introducteur au passé : le passé composé devient plus-que-parfait (s'était demandé), le conditionnel reste conditionnel. Les pronoms changent : je → il, nous → ils. L'apostrophe « mes braves collègues » disparaît."), VERNE),
        S('francais', 'Lexique · polysémie', Q(
            "« La photographie a donné de notre satellite des épreuves d'une incomparable beauté. » Que signifie « épreuves » ici ?",
            ["Des tirages photographiques", "Des examens", "Des malheurs, des souffrances", "Des compétitions sportives"], "Des tirages photographiques",
            "« Épreuve » est polysémique : un tirage photographique (ici), un examen, une difficulté douloureuse, une compétition, une feuille d'imprimerie à corriger."), VERNE),
        S('francais', 'Lexique · sens en contexte', Q(
            "Barbicane appelle J.-T. Maston, qui vient de crier « Oui, la guerre ! », « mon honorable interrupteur ». Que traduit cette expression ?",
            ["Une politesse ironique, à la manière des débats parlementaires, envers celui qui l'a interrompu", "Une insulte directe", "Un compliment sincère sur son discours", "Le titre officiel de Maston au Gun-Club"],
            "Une politesse ironique, à la manière des débats parlementaires, envers celui qui l'a interrompu",
            "« Interrupteur » désigne ici celui qui interrompt (et non l'objet électrique) ; « honorable » est la formule de politesse des assemblées."), VERNE),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé « impraticable » ?",
            ["Préfixe in- (im-, négation) + base pratic- (pratiquer) + suffixe -able", "Composition de « impr » et « aticable »", "Préfixe impra- + base ticable", "Mot simple sans préfixe"],
            "Préfixe in- (im-, négation) + base pratic- (pratiquer) + suffixe -able",
            "Impraticable : qu'on ne peut pas mettre en pratique, réaliser. In- devient im- devant p, b, m."), VERNE),
    ]),
    epreuve('Épreuve écrite disciplinaire de mathématiques', 20163, [
        S('mathematiques', 'Exercice 1 · comparer des tarifs', Q(
            "Quelle compagnie de transport est la moins chère pour 150 km ?",
            ["La compagnie A : 620 €", "La compagnie B : 657,50 €", "La compagnie C : 643,50 €", "Elles coûtent toutes le même prix"], "La compagnie A : 620 €",
            "A : 350 + 1,80 × 150 = 620 €. B : 290 + 2,45 × 150 = 657,50 €. C : 585 × 1,10 = 643,50 € TTC (on ajoute la TVA de 10 % au prix HT)."), SORTIE),
        S('mathematiques', 'Exercice 1 · budget', N(
            "Avec la compagnie A, quel est le budget global TTC de la sortie, en euros ?", 1893.8,
            "Transport 620 € ; musée 4 × 35 + 40 × 23 = 1 060 € ; repas 4 × 7,95 + 40 × 4,55 = 213,80 €. Total : 1 893,80 €."), SORTIE),
        S('mathematiques', 'Exercice 1 · pourcentages', N(
            "La mairie verse 8 € par élève ; la coopérative prend en charge 20 % du montant restant. Combien paie la coopérative, en euros ?", 314.76,
            "Mairie : 8 × 40 = 320 €. Reste : 1 893,80 − 320 = 1 573,80 €. 20 % de 1 573,80 = 314,76 €."), SORTIE),
        S('mathematiques', 'Exercice 2 · vrai ou faux', Q(
            "Affirmation : « La somme de deux nombres rationnels non entiers est un nombre rationnel non entier. » Vrai ou faux ?",
            ["Faux : 1/2 + 1/2 = 1", "Vrai", "Faux : la somme de deux rationnels n'est jamais rationnelle", "Vrai si les deux nombres sont positifs"], "Faux : 1/2 + 1/2 = 1",
            "Un contre-exemple suffit : 1/2 et 1/2 ne sont pas entiers, mais leur somme est l'entier 1."), None),
        S('mathematiques', 'Exercice 2 · vrai ou faux', Q(
            "A, B, D alignés ; A, C, E alignés ; AB = 5 cm, BD = 15 cm, AC = 7 cm, AE = 21 cm. Les droites (BC) et (DE) sont-elles parallèles ?",
            ["Non : AB/AD = 5/20 = 1/4 mais AC/AE = 7/21 = 1/3", "Oui : 5/15 = 7/21", "Oui, d'après le théorème de Thalès", "On ne peut pas conclure"], "Non : AB/AD = 5/20 = 1/4 mais AC/AE = 7/21 = 1/3",
            "Attention : BD n'est pas AD. AD = AB + BD = 20 cm. Les rapports AB/AD et AC/AE sont différents : les droites ne sont pas parallèles (contraposée du théorème de Thalès)."), None),
        S('mathematiques', 'Exercice 3 · périmètre', N(
            "Combien de jours faut-il pour construire la palissade de rayon 2,5 km, à 650 m par jour ?", 25,
            "Longueur : 2 × π × 2,5 ≈ 15,71 km = 15 710 m. 15 710 ÷ 650 ≈ 24,2 : il faut 25 jours (on arrondit à l'entier supérieur)."), ALESIA),
        S('mathematiques', 'Exercice 3 · aire', N(
            "Quelle est l'aire comprise entre les deux palissades, arrondie au km² ?", 17,
            "Aire de la couronne : π × (3,4² − 2,5²) = π × 5,31 ≈ 16,7 km², soit environ 17 km²."), ALESIA),
        S('mathematiques', 'Exercice 3 · nombres premiers', Q(
            "Quelle est la décomposition de 62 426 en produit de facteurs premiers ?",
            ["2 × 7⁴ × 13", "2 × 13 × 311", "2² × 7³ × 13", "7 × 8 918"], "2 × 7⁴ × 13",
            "62 426 = 2 × 31 213 ; 31 213 = 7 × 4 459 = 7² × 637 = 7³ × 91 = 7⁴ × 13. (8 086 = 2 × 13 × 311.)"), None),
        S('mathematiques', 'Exercice 3 · diviseurs communs', N(
            "62 426 fantassins et 8 086 cavaliers doivent être répartis en troupes identiques. Combien de troupes au maximum ?", 26,
            "Diviseurs communs de 62 426 = 2 × 7⁴ × 13 et 8 086 = 2 × 13 × 311 : 1, 2, 13 et 26. Avec 26 troupes : 2 401 fantassins et 311 cavaliers par troupe."), None),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "Quelle est la probabilité que Soan obtienne une somme strictement supérieure à 10 ?",
            ["1/12", "1/6", "3/11", "1/18"], "1/12",
            "36 issues. Somme 11 : (5;6), (6;5) ; somme 12 : (6;6). 3 issues : 3/36 = 1/12."), DES),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "Quelle est la probabilité que Thaïs obtienne une somme multiple de 3 ?",
            ["11/32", "1/3", "3/8", "10/32"], "11/32",
            "4 × 8 = 32 issues. Avec 1 : b = 2, 5, 8 ; avec 2 : b = 1, 4, 7 ; avec 3 : b = 3, 6 ; avec 4 : b = 2, 5, 8. Soit 11 issues : 11/32."), DES),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "Soan dit : « J'ai plus de chances d'obtenir une somme égale à 8 que Thaïs. » A-t-il raison ?",
            ["Oui : 5/36 ≈ 0,139 contre 4/32 = 0,125", "Non : Thaïs a 4/32, plus que Soan", "Non : ils ont la même probabilité", "Oui : 5/36 contre 1/32"], "Oui : 5/36 ≈ 0,139 contre 4/32 = 0,125",
            "Soan : (2;6), (3;5), (4;4), (5;3), (6;2), soit 5/36. Thaïs : (1;7), (2;6), (3;5), (4;4), soit 4/32 = 1/8."), DES),
        S('mathematiques', 'Exercice 5 · motif évolutif', N(
            "Combien de cubes faut-il à l'étape 50 ?", 2501,
            "Le motif compte n² + 1 cubes à l'étape n (2, 5, 10, 17…). Étape 50 : 2 500 + 1 = 2 501 cubes."), CUBES),
        S('mathematiques', 'Exercice 5 · motif évolutif', N(
            "À quelle étape le motif compte-t-il 626 cubes ?", 25,
            "n² + 1 = 626 donne n² = 625, n = 25. En revanche, 172 cubes est impossible : 171 n'est pas un carré parfait."), CUBES),
        S('mathematiques', 'Exercice 5 · volumes', N(
            "Combien de cubes d'arête 1 cm faut-il pour remplir un cube d'un litre ?", 1000,
            "1 L = 1 dm³ = 10 cm × 10 cm × 10 cm = 1 000 cm³."), None),
    ]),
    epreuve("Épreuve écrite d'application (sciences, histoire-géographie-EMC ou arts)", 20175, [
        # ── Sciences ──
        S('svt', 'Sciences · le cycle de vie du blé', Q(
            "Dans une fleur, quels sont les organes mâles et les organes femelles ?",
            ["Mâles : les étamines (qui produisent le pollen) ; femelles : le pistil (ovaire contenant les ovules)", "Mâles : les pétales ; femelles : les sépales", "Mâles : le pistil ; femelles : les étamines", "Mâles : la tige ; femelles : les racines"],
            "Mâles : les étamines (qui produisent le pollen) ; femelles : le pistil (ovaire contenant les ovules)",
            "Après pollinisation et fécondation, l'ovaire se transforme en fruit et les ovules en graines : chez le blé, le grain."), BLE),
        S('svt', 'Sciences · le cycle de vie du blé', Q(
            "Quel est le mode de reproduction d'un plant de blé sauvage dans la nature ?",
            ["La reproduction sexuée, par les fleurs et les graines", "Le bouturage", "Le marcottage", "La division des racines"], "La reproduction sexuée, par les fleurs et les graines",
            "Le blé se reproduit par ses graines, issues de la fécondation. Le blé est surtout autogame : le pollen féconde le plus souvent la fleur qui l'a produit."), BLE),
        S('svt', 'Sciences · la germination', Q(
            "Pour montrer le rôle de l'eau dans la germination, quel protocole est valable ?",
            ["Deux lots de graines identiques, dans les mêmes conditions, l'un arrosé, l'autre non", "Un lot arrosé à la lumière et un lot sec dans le noir", "Un seul lot arrosé, observé chaque jour", "Deux lots de graines différentes arrosés différemment"],
            "Deux lots de graines identiques, dans les mêmes conditions, l'un arrosé, l'autre non",
            "On ne fait varier qu'un seul facteur à la fois. Changer à la fois l'eau et la lumière, c'est le défaut du protocole d'élève analysé dans le sujet : on ne peut plus savoir quel facteur agit."), BLE),
        S('physique_chimie', 'Sciences · la fabrication du pain', Q(
            "Quel gaz, produit par les levures, fait gonfler la pâte à pain ?",
            ["Le dioxyde de carbone, CO₂", "Le dioxygène, O₂", "L'azote, N₂", "La vapeur d'eau, H₂O"], "Le dioxyde de carbone, CO₂",
            "La fermentation transforme le glucose en éthanol et en dioxyde de carbone : C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂. Des réactifs disparaissent et des produits apparaissent : c'est une transformation chimique."), BLE),
        S('physique_chimie', 'Sciences · la fabrication du pain', Q(
            "L'éthanol bout à 78 °C ; le pain cuit à 240 °C. Que devient l'éthanol pendant la cuisson ?",
            ["Il passe à l'état gazeux (vaporisation) et s'échappe de la pâte", "Il se solidifie", "Il reste liquide dans le pain", "Il se transforme en sucre"],
            "Il passe à l'état gazeux (vaporisation) et s'échappe de la pâte",
            "Au-dessus de sa température d'ébullition, un liquide se vaporise. C'est pourquoi le pain cuit ne contient presque plus d'alcool."), BLE),
        S('physique_chimie', 'Sciences · la fabrication du pain', Q(
            "Sans verre doseur, comment mesurer précisément 300 mL d'eau ?",
            ["Peser 300 g d'eau, car 1 L d'eau a une masse de 1 kg", "Remplir trois verres", "Compter 30 cuillères", "Mesurer la hauteur d'eau dans un bol"], "Peser 300 g d'eau, car 1 L d'eau a une masse de 1 kg",
            "Masse volumique de l'eau : 1 kg/L, donc 1 g/mL. 300 mL d'eau pèsent 300 g : une balance suffit."), BLE),
        S('physique_chimie', 'Sciences · la fabrication du pain', Q(
            "Parmi les valeurs pH = 1, 5, 8 et 12, laquelle convient le mieux à l'activité des levures ?",
            ["pH = 5 (légèrement acide)", "pH = 1 (très acide)", "pH = 12 (très basique)", "pH = 8"], "pH = 5 (légèrement acide)",
            "Les levures sont des êtres vivants (champignons microscopiques) : les milieux très acides ou très basiques les détruisent. Elles préfèrent un milieu légèrement acide."), BLE),
        S('technologie', "Sciences · l'agriculture de précision", Q(
            "Un robot d'arrosage repère les zones sèches et avertit l'agriculteur. À quel objectif de développement durable cela contribue-t-il ?",
            ["Une gestion durable de l'eau : arroser seulement là où c'est nécessaire", "La réduction du temps de travail scolaire", "L'égalité entre les sexes", "La paix et la justice"],
            "Une gestion durable de l'eau : arroser seulement là où c'est nécessaire",
            "L'agriculture de précision utilise capteurs, satellites et programmes pour économiser l'eau et les intrants (ODD 6 et 12, par exemple)."), BLE),
        S('technologie', "Sciences · la modélisation de l'arrosage", Q(
            "Dans un robot, quel élément permet de « détecter une zone sèche » ?",
            ["Un capteur (d'humidité ou de couleur)", "Le moteur", "La batterie", "Les roues"], "Un capteur (d'humidité ou de couleur)",
            "La fonction « identifier les zones à arroser » est assurée par un capteur ; l'avertissement de l'utilisateur, par un actionneur (son, lumière) commandé par le programme."), BLE),
        # ── Histoire et EMC ──
        S('histoire_geographie', "Histoire · Henri IV et l'édit de Nantes", Q(
            "En quelle année Henri IV signe-t-il l'édit de Nantes ?",
            ["1598", "1572", "1685", "1515"], "1598",
            "L'édit met fin aux guerres de Religion (1562-1598). Il sera révoqué par Louis XIV en 1685 (édit de Fontainebleau)."), EDIT),
        S('histoire_geographie', "Histoire · Henri IV et l'édit de Nantes", Q(
            "Que garantit l'édit de Nantes aux protestants ?",
            ["Une liberté de culte limitée et l'égalité civile avec les catholiques", "L'interdiction du catholicisme", "La création d'un État protestant indépendant", "L'expulsion hors du royaume"],
            "Une liberté de culte limitée et l'égalité civile avec les catholiques",
            "Le catholicisme reste la religion du roi et du royaume, mais les protestants peuvent pratiquer leur culte dans certains lieux, accéder aux charges et disposent de places de sûreté."), EDIT),
        S('histoire_geographie', "Histoire · Henri IV et l'édit de Nantes", Q(
            "Quel massacre de protestants a eu lieu à Paris le 24 août 1572, pendant les guerres de Religion ?",
            ["Le massacre de la Saint-Barthélemy", "La journée des Barricades", "La Fronde", "Le massacre de Wassy"], "Le massacre de la Saint-Barthélemy",
            "Le massacre de Wassy (1562) déclenche les guerres de Religion ; la Saint-Barthélemy (1572) en est l'épisode le plus sanglant."), EDIT),
        S('emc', 'EMC · la fraternité', Q(
            "Où la fraternité est-elle inscrite comme valeur de la République ?",
            ["Dans la devise « Liberté, Égalité, Fraternité », inscrite dans la Constitution de 1958", "Uniquement dans la Charte de la laïcité", "Dans le Code de la route", "Dans la loi de 1905"],
            "Dans la devise « Liberté, Égalité, Fraternité », inscrite dans la Constitution de 1958",
            "La devise devient officielle sous la IIe République (1848) ; l'article 2 de la Constitution de 1958 la reprend. En 2018, le Conseil constitutionnel a reconnu la fraternité comme un principe à valeur constitutionnelle."), EDIT),
        S('emc', 'EMC · la fraternité', Q(
            "Que signifie la fraternité pour des élèves de CE1 ?",
            ["Se considérer comme membres d'une même communauté, s'entraider et être solidaires, sans exclure personne", "Être frères et sœurs dans la même famille", "Toujours être d'accord avec ses camarades", "Ne jamais se disputer"],
            "Se considérer comme membres d'une même communauté, s'entraider et être solidaires, sans exclure personne",
            "La fraternité dépasse les liens familiaux : elle se vit à l'école par l'entraide, le tutorat, l'accueil d'un nouvel élève, les projets solidaires."), EDIT),
        S('emc', 'EMC · la fraternité', Q(
            "Lequel de ces gestes d'école illustre le mieux la fraternité ?",
            ["Aider un camarade en difficulté ou accueillir un nouvel élève", "Ranger ses propres affaires", "Lever la main pour parler", "Faire ses devoirs seul"],
            "Aider un camarade en difficulté ou accueillir un nouvel élève",
            "Le Conseil des sages de la laïcité propose une « école de la fraternité » : apprendre à reconnaître l'autre comme un semblable et à agir pour lui."), None),
        # ── Arts ──
        S('arts', 'Histoire des arts · le japonisme', Q(
            "Qui est l'auteur de l'estampe « La Grande Vague de Kanagawa » ?",
            ["Hokusai", "Hiroshige", "Utamaro", "Eiichiro Oda"], "Hokusai",
            "Katsushika Hokusai (1760-1849), vers 1830, série des Trente-six vues du mont Fuji. Le dossier la rapprochait d'une planche du manga One Piece d'Eiichiro Oda (2019)."),
          "Dossier d'histoire des arts (cycle 3) : Hokusai, La Grande Vague de Kanagawa ; La Vague (vers 1903, onyx) ; une planche de One Piece ; un haïku ; un texte sur Debussy."),
        S('arts', 'Histoire des arts · le japonisme', Q(
            "Qu'est-ce que le japonisme ?",
            ["L'influence de l'art japonais sur les artistes européens à partir des années 1860", "Un style de peinture inventé au Japon au XXe siècle", "Une technique de sculpture sur onyx", "Un mouvement littéraire japonais"],
            "L'influence de l'art japonais sur les artistes européens à partir des années 1860",
            "Après l'ouverture du Japon au commerce, ses estampes sont exposées à Londres (1862) et à Paris (1867) ; Monet, Van Gogh, Claudel ou Debussy s'en inspirent."),
          "Document 3 : « Au XIXe siècle, l'influence de l'Orient sur l'Europe se manifeste essentiellement au travers du japonisme. »"),
        S('arts', 'Histoire des arts · le japonisme', Q(
            "Quelle œuvre de Debussy a paru avec la « Grande Vague » d'Hokusai sur la couverture de sa partition ?",
            ["La Mer (1905)", "Le Boléro", "Clair de lune", "Le Carnaval des animaux"], "La Mer (1905)",
            "Debussy, admirateur du japonisme, choisit l'estampe d'Hokusai pour la couverture de « La Mer ». Le Boléro est de Ravel, le Carnaval des animaux de Saint-Saëns."), None),
        S('arts', 'Histoire des arts · le japonisme', Q(
            "Qu'est-ce qu'un haïku ?",
            ["Un poème japonais très bref, traditionnellement de trois vers (5, 7, 5 syllabes)", "Une estampe japonaise", "Un instrument de musique japonais", "Une sculpture en onyx"],
            "Un poème japonais très bref, traditionnellement de trois vers (5, 7, 5 syllabes)",
            "Le dossier proposait un haïku de Santoka Taneda (1880-1940), poète qui pratiquait un haïku libre. Le haïku saisit un instant, souvent lié à la nature et aux saisons."), None),
    ]),
]

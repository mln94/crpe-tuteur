# Bac+3, session 2026, groupement 3
from slib import S, Q, N, C, epreuve

DES = ("Texte : François-Henri Désérable, Chagrin d'un chant inachevé (2025). Enfant, le narrateur rêvait devant la carte du monde de la classe ; "
       "devenu écrivain, il part à son tour sur les traces des grands voyageurs.")
CREPES = "Exercice 2 : recette de crêpes pour 4 personnes : 250 g de farine, 2 œufs, 60 cl de lait, 25 g de beurre fondu, 1 cuillère à soupe de sucre."
PARTERRE = "Exercice 3 : un parterre rectangulaire de 8 m sur 6 m contient en son centre un bassin circulaire de 3 m de diamètre ; le reste sera ensemencé de fleurs."
TRANSPORT = "Exercice 4 : 240 élèves. Moyen de transport : voiture 120, transports en commun 72, vélo 36, autre 12."
AQUA = "Sujet de sciences : l'aquaponie, un système en circuit fermé qui associe l'élevage de poissons et la culture de plantes hors sol, grâce à des bactéries."
BRADFORD = ("Text: “One third of schoolchildren don't play outside”, BBC, 25 October 2025. The Born in Bradford (BiB) research programme studied the lifestyles of "
            "2,568 children aged 7 to 12. 34% of children did not play outdoors on school days, while 20% stayed indoors on weekends.")

QUESTIONS = [
    epreuve('Première épreuve écrite (français et mathématiques)', 20283, [
        # ── Français ──
        S('francais', 'Étude de la langue · fonctions', Q(
            "« J'étais riche de mes seuls yeux intranquilles, en proie au doute et désœuvré. » Quelle est la fonction de « riche » ?",
            ["Attribut du sujet « je »", "Épithète du nom « yeux »", "Complément d'objet direct", "Complément circonstanciel de manière"], "Attribut du sujet « je »",
            "« Riche » est relié au sujet par le verbe d'état « être » : c'est un attribut du sujet. « Désœuvré » a la même fonction."), DES),
        S('francais', 'Étude de la langue · sujet et COD', C(
            "Cliquez sur le sujet du verbe « luisaient ».",
            "Je poussais la porte d'un bar clandestin où luisaient dans la pénombre [le canon d'un colt et les braises d'un cigare].",
            "Le sujet est inversé, placé après le verbe : qu'est-ce qui luisait ? « le canon d'un colt et les braises d'un cigare ». D'où l'accord au pluriel."), DES),
        S('francais', 'Étude de la langue · sujet et COD', C(
            "Cliquez sur le complément d'objet direct du verbe « poussais ».",
            "Je poussais [la porte d'un bar clandestin] où luisaient dans la pénombre le canon d'un colt et les braises d'un cigare.",
            "On pousse quoi ? « la porte d'un bar clandestin » : groupe nominal COD, complété par la relative « où luisaient… »."), DES),
        S('francais', 'Étude de la langue · temps et modes', Q(
            "« J'aurais volontiers emprunté la formule. » À quel temps est la forme verbale ?",
            ["Conditionnel passé", "Plus-que-parfait de l'indicatif", "Futur antérieur", "Subjonctif plus-que-parfait"], "Conditionnel passé",
            "Auxiliaire au conditionnel présent (aurais) + participe passé : conditionnel passé, rangé parmi les temps de l'indicatif dans la terminologie actuelle."), DES),
        S('francais', 'Étude de la langue · conjugaison', Q(
            "Conjuguez « emprunter » à la 1re personne du singulier du passé simple.",
            ["J'empruntai", "J'empruntais", "J'emprunterai", "J'emprunterais"], "J'empruntai",
            "Passé simple des verbes en -er : -ai. Ne confondez pas avec l'imparfait (j'empruntais), le futur (j'emprunterai) et le conditionnel (j'emprunterais)."), DES),
        S('francais', 'Étude de la langue · discours indirect', Q(
            "Transposez au discours indirect : « Faites comme lui, disait-il, et vous n'irez jamais loin. »",
            ["Il leur disait de faire comme lui et qu'ils n'iraient jamais loin.", "Il leur disait : faites comme lui et vous n'irez jamais loin.", "Il leur disait qu'ils feront comme lui et qu'ils n'iront jamais loin.", "Il leur disait de faire comme lui et que vous n'irez jamais loin."],
            "Il leur disait de faire comme lui et qu'ils n'iraient jamais loin.",
            "L'impératif devient un infinitif (de faire) ; « vous » devient « ils » ; le futur devient conditionnel présent (futur dans le passé), car le verbe introducteur est au passé."), DES),
        S('francais', 'Étude de la langue · propositions', Q(
            "« Les écrivains eux-mêmes avaient tant voyagé qu'on ne pouvait prendre une seule direction sans se mettre aussitôt dans leurs pas. » Nature de la proposition introduite par « qu' » ?",
            ["Subordonnée conjonctive circonstancielle de conséquence", "Subordonnée relative", "Subordonnée complétive, COD", "Subordonnée circonstancielle de but"],
            "Subordonnée conjonctive circonstancielle de conséquence",
            "La corrélation « tant… que » exprime la conséquence : ils avaient tant voyagé que (résultat) toutes les directions étaient déjà prises."), DES),
        S('francais', 'Étude de la langue · type et forme', Q(
            "« C'est la contemplation silencieuse des atlas […] qui donne ainsi l'envie de tout planter là. » Type et forme de la phrase ?",
            ["Déclarative ; forme emphatique", "Exclamative ; forme négative", "Interrogative ; forme emphatique", "Déclarative ; forme passive"], "Déclarative ; forme emphatique",
            "« C'est… qui » extrait et met en relief le sujet « la contemplation silencieuse des atlas » : c'est la forme emphatique (phrase clivée)."), DES),
        S('francais', 'Lexique · formation des mots', Q(
            "Comment est formé « intranquille », et que signifie-t-il ?",
            ["Préfixe privatif in- + tranquille : qui n'est pas tranquille, inquiet", "Préfixe intra- (à l'intérieur) + quille", "Préfixe inter- + tranquille : entre deux états", "Composition de « intra » et « tranquille » : très calme"],
            "Préfixe privatif in- + tranquille : qui n'est pas tranquille, inquiet",
            "Dérivation par préfixation : in- a une valeur négative. Le mot, rare, dit l'inquiétude et l'agitation du narrateur, « en proie au doute »."), DES),
        S('francais', 'Lexique · compréhension', Q(
            "« Il nous parlait additions, soustractions, figures géométriques, et moi je m'enivrais des noms de villes inconnues. » Que montre cette phrase ?",
            ["L'opposition entre les leçons concrètes du maître et la rêverie de l'élève, grisé par les noms de villes", "L'élève adore les mathématiques", "Le maître enseigne la géographie", "L'élève est malade en classe"],
            "L'opposition entre les leçons concrètes du maître et la rêverie de l'élève, grisé par les noms de villes",
            "« M'enivrais » est une métaphore : les noms de villes inconnues grisent l'enfant comme une boisson. La construction en deux temps (« il… et moi… ») souligne le décalage."), DES),
        # ── Mathématiques ──
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « Lorsqu'on divise un nombre décimal par 10, on ne peut pas obtenir un nombre entier. » Vrai ou faux ?",
            ["Faux : 30 ÷ 10 = 3", "Vrai", "Faux : 3,5 ÷ 10 = 35", "Vrai : on obtient toujours une virgule"], "Faux : 30 ÷ 10 = 3",
            "Un entier est aussi un nombre décimal : 30 est décimal et 30 ÷ 10 = 3 est entier. Un contre-exemple suffit."), None),
        S('mathematiques', 'Exercice 1 · vrai ou faux', Q(
            "Affirmation : « Un quadrilatère dont les diagonales sont perpendiculaires et ont la même longueur est un carré. » Vrai ou faux ?",
            ["Faux : il faut aussi que les diagonales se coupent en leur milieu", "Vrai", "Faux : un carré n'a pas de diagonales perpendiculaires", "Vrai, c'est la définition du carré"],
            "Faux : il faut aussi que les diagonales se coupent en leur milieu",
            "Deux segments de même longueur, perpendiculaires mais qui ne se coupent pas en leur milieu, donnent un quadrilatère qui n'est pas un carré. Un carré a des diagonales de même milieu, perpendiculaires et de même longueur."), None),
        S('mathematiques', 'Exercice 1 · probabilités', Q(
            "On lance deux dés cubiques équilibrés (faces 1 à 6). Quelle est la probabilité que le produit des deux résultats soit égal à 12 ?",
            ["1/9", "1/12", "1/36", "1/6"], "1/9",
            "36 issues équiprobables. Produit 12 : (2;6), (6;2), (3;4), (4;3), soit 4 issues : 4/36 = 1/9."), None),
        S('mathematiques', 'Exercice 1 · QCM', N(
            "La lumière va à environ 3 × 10⁵ km/s ; la distance Terre-Soleil est d'environ 150 millions de km. Combien de secondes met la lumière du Soleil pour nous parvenir ?", 500,
            "t = d ÷ v = 150 000 000 ÷ 300 000 = 500 s, soit un peu plus de 8 minutes."), None),
        S('mathematiques', 'Exercice 1 · QCM', N(
            "ABC est rectangle en B, avec AC = 13 cm et BC = 5 cm. Combien vaut AB, en cm ?", 12,
            "Pythagore : AB² = AC² − BC² = 169 − 25 = 144, donc AB = 12 cm. [AC] est l'hypoténuse, côté opposé à l'angle droit."), None),
        S('mathematiques', 'Exercice 1 · QCM', Q(
            "Série : 51 ; 70 ; 81 ; 13 ; 63 ; 57 ; 99. Quelle affirmation est vraie ?",
            ["La médiane de cette série est 63", "La médiane de cette série est 13", "L'étendue de cette série est 99", "La moyenne de cette série est 63"], "La médiane de cette série est 63",
            "Rangée : 13 ; 51 ; 57 ; 63 ; 70 ; 81 ; 99. La 4e valeur sur 7, 63, est la médiane. Étendue : 99 − 13 = 86. Moyenne : 434 ÷ 7 = 62. Il faut toujours ranger la série avant de chercher la médiane."), None),
        S('mathematiques', 'Exercice 2 · proportionnalité', N(
            "Quelle masse de farine faut-il pour 6 personnes, en grammes ?", 375,
            "6 personnes = 1,5 fois la recette pour 4 : 250 × 1,5 = 375 g. On peut aussi passer par 2 personnes (125 g) puis multiplier par 3."), CREPES),
        S('mathematiques', 'Exercice 2 · fractions', Q(
            "Le beurre est vendu en plaquettes de 250 g. Quelle fraction de plaquette la recette pour 4 utilise-t-elle ?",
            ["1/10", "1/25", "25/250", "1/4"], "1/10",
            "25/250 = 1/10 sous forme irréductible. 25/250 est juste mais n'est pas irréductible, comme le demandait le sujet."), CREPES),
        S('mathematiques', 'Exercice 2 · proportionnalité', Q(
            "Avec 5 kg de farine et 3 douzaines d'œufs, peut-on faire des crêpes pour 70 élèves avec cette recette ?",
            ["Oui : les œufs permettent 72 parts et la farine 80", "Non : il manque des œufs", "Non : il manque de la farine", "Oui, avec exactement 70 parts"], "Oui : les œufs permettent 72 parts et la farine 80",
            "Farine : 5 000 ÷ 250 = 20 recettes, soit 80 parts. Œufs : 36 ÷ 2 = 18 recettes, soit 72 parts. Le facteur limitant (les œufs) suffit pour 70 élèves."), CREPES),
        S('mathematiques', 'Exercice 2 · pourcentages', Q(
            "La quantité de lait passe de 60 cl à 50 cl. De quel pourcentage environ a-t-elle diminué ?",
            ["Environ 16,7 %", "10 %", "20 %", "Environ 83,3 %"], "Environ 16,7 %",
            "Diminution de 10 cl sur 60 cl : 10/60 ≈ 0,167, soit environ 16,7 %. On rapporte toujours la variation à la valeur de départ (60), pas à la valeur d'arrivée (50 donnerait 20 %)."), CREPES),
        S('mathematiques', 'Exercice 2 · énigme', N(
            "Énigme : je suis un nombre décimal. Mon chiffre des centièmes est égal à mon nombre de centaines. Mon produit par 10 a pour chiffre des unités 4 et pour chiffre des dizaines 7. Mon quotient par 10 a pour chiffre des millièmes 2 et pour chiffre des unités 3. Qui suis-je ?", 237.42,
            "Produit par 10 : unités 4 et dizaines 7, donc le nombre a 7 unités et 4 dixièmes. Quotient par 10 : millièmes 2 et unités 3, donc 2 centièmes et 3 dizaines. Centièmes = 2 = nombre de centaines : 237,42."), None),
        S('mathematiques', 'Exercice 3 · aires', N(
            "Quelle est l'aire à ensemencer, en m², arrondie au dixième ? (Utilisez π de la calculatrice.)", 40.9,
            "Parterre : 8 × 6 = 48 m². Bassin : π × 1,5² ≈ 7,07 m² (le rayon vaut 1,5 m, pas 3 m). 48 − 7,07 ≈ 40,9 m².", tol=0.05), PARTERRE),
        S('mathematiques', 'Exercice 3 · aires', N(
            "Un sac de graines couvre 15 m². Combien de sacs faut-il au minimum pour environ 40,9 m² ?", 3,
            "40,9 ÷ 15 ≈ 2,73 : 2 sacs ne suffisent pas, il en faut 3. On arrondit à l'entier supérieur."), PARTERRE),
        S('mathematiques', 'Exercice 3 · échelle', Q(
            "Sur un plan à l'échelle 1/50, quelles sont les dimensions du parterre de 8 m sur 6 m ?",
            ["16 cm sur 12 cm", "1,6 cm sur 1,2 cm", "160 cm sur 120 cm", "4 cm sur 3 cm"], "16 cm sur 12 cm",
            "800 cm ÷ 50 = 16 cm ; 600 cm ÷ 50 = 12 cm. Convertissez d'abord en centimètres."), PARTERRE),
        S('mathematiques', 'Exercice 4 · diagramme circulaire', N(
            "Dans un diagramme circulaire, quel serait l'angle du secteur « Vélo », en degrés ?", 54,
            "36 élèves sur 240 : 36/240 × 360° = 54°."), TRANSPORT),
        S('mathematiques', 'Exercice 4 · probabilités', Q(
            "On choisit un élève au hasard. Quelle est la probabilité qu'il ne vienne pas en transports en commun ?",
            ["7/10", "3/10", "72/240", "1/2"], "7/10",
            "240 − 72 = 168 élèves : 168/240 = 7/10. On peut aussi calculer 1 − 72/240 = 1 − 3/10."), TRANSPORT),
        S('mathematiques', 'Exercice 4 · pourcentages', N(
            "De combien d'élèves l'effectif des cyclistes doit-il augmenter pour que 20 % des élèves viennent à vélo ?", 12,
            "20 % de 240 = 48 cyclistes. Il y en a 36 : il en faut 12 de plus (venant de la voiture, l'effectif total ne change pas)."), TRANSPORT),
        S('mathematiques', 'Exercice 5 · programmes de calcul', Q(
            "Programme B : choisir un nombre, le multiplier par 3, soustraire 4. Pour quel nombre de départ le résultat est-il nul ?",
            ["4/3", "3/4", "−4/3", "4"], "4/3",
            "f(x) = 3x − 4 = 0 donne x = 4/3. La valeur exacte est 4/3 : 1,33 n'en est qu'une valeur approchée."), None),
    ]),
    epreuve('Seconde épreuve écrite (domaines au choix)', 20274, [
        # ── Histoire-géographie ──
        S('histoire_geographie', 'Géographie · espace rural et espace urbain', Q(
            "Quel critère l'INSEE utilise-t-il pour définir une unité urbaine ?",
            ["Un bâti continu (moins de 200 m entre deux constructions) et au moins 2 000 habitants", "Plus de 100 000 habitants", "La présence d'une mairie", "Un territoire sans aucune activité agricole"],
            "Un bâti continu (moins de 200 m entre deux constructions) et au moins 2 000 habitants",
            "On distingue aussi rural et urbain par la densité de population, la continuité du bâti, les activités et les services. Depuis 2020, l'INSEE classe les communes selon une grille de densité."),
          "Question du sujet : « Indiquez les critères qui distinguent un espace rural d'un espace urbain. »"),
        S('histoire_geographie', "Histoire · l'industrialisation de la France", Q(
            "Quelle source d'énergie est au cœur de l'industrialisation de la France au XIXe siècle ?",
            ["Le charbon, qui alimente les machines à vapeur", "Le pétrole", "L'électricité nucléaire", "L'énergie solaire"], "Le charbon, qui alimente les machines à vapeur",
            "Charbon, machine à vapeur, chemin de fer, grandes usines (textile, sidérurgie) : la France s'industrialise surtout à partir des années 1840-1850, et la classe ouvrière se développe."),
          "Question du sujet : « Indiquez les principales caractéristiques de l'industrialisation de la France au XIXe siècle. »"),
        S('histoire_geographie', "Histoire · l'industrialisation de la France", Q(
            "Comment appelle-t-on le départ massif des habitants des campagnes vers les villes industrielles ?",
            ["L'exode rural", "La périurbanisation", "La décentralisation", "La métropolisation"], "L'exode rural",
            "Au XIXe siècle, l'industrie attire une main-d'œuvre venue des campagnes : les villes ouvrières grandissent et le monde ouvrier se forme."), None),
        S('histoire_geographie', 'Histoire · la condition féminine', N(
            "D'après le témoignage de Lucie Baud, à quel âge est-elle entrée comme apprentie à l'usine de tissage ?", 12,
            "« J'avais alors douze ans. » Elle décrit des journées de 12 à 14 heures, l'accélération des machines et la baisse des salaires, puis la grève de 1905."),
          "Document 2 : témoignage de Lucie Baud, ouvrière de la soie à Vizille, publié dans Le Mouvement socialiste en 1908."),
        S('histoire_geographie', 'Histoire · la condition féminine', Q(
            "Qu'apprend-on sur la condition des ouvrières dans le témoignage de Lucie Baud ?",
            ["Des journées très longues, des salaires en baisse avec chaque nouvelle machine, et une grève menée par 200 femmes en 1905", "Des journées de 8 heures et des salaires en hausse", "Les femmes n'avaient pas le droit de travailler en usine", "Les patrons acceptaient toutes les revendications"],
            "Des journées très longues, des salaires en baisse avec chaque nouvelle machine, et une grève menée par 200 femmes en 1905",
            "Le témoignage montre l'exploitation (12 à 14 heures par jour, deux métiers à conduire), mais aussi l'engagement des femmes : « Nous étions 200 grévistes femmes »."),
          "Document 2 : témoignage de Lucie Baud, ouvrière de la soie à Vizille."),
        # ── EMC ──
        S('emc', "EMC · l'empathie", Q(
            "Qu'est-ce que l'empathie ?",
            ["La capacité à comprendre ce que ressent autrui, à se mettre à sa place", "Le fait d'être d'accord avec tout le monde", "La pitié envers les plus faibles", "L'obéissance aux règles"],
            "La capacité à comprendre ce que ressent autrui, à se mettre à sa place",
            "L'empathie fait partie des compétences psychosociales. Elle aide à respecter autrui, à résoudre les conflits et à prévenir le harcèlement : elle permet de mieux vivre ensemble."),
          "Question du sujet : « Expliquez pourquoi développer une aptitude à l'empathie permet de mieux vivre ensemble. »"),
        S('emc', "EMC · l'empathie", Q(
            "Quel dispositif de l'école s'appuie sur l'empathie pour lutter contre le harcèlement ?",
            ["Le programme pHARe et les cours d'empathie", "Le livret scolaire unique", "Les évaluations nationales", "Le conseil d'école"], "Le programme pHARe et les cours d'empathie",
            "Le programme pHARe (prévention du harcèlement) est généralisé depuis 2021 ; des séances dédiées à l'empathie sont progressivement mises en place à l'école depuis 2024."), None),
        S('emc', "EMC · l'empathie", Q(
            "Parmi les finalités de l'EMC, laquelle l'empathie sert-elle le plus directement ?",
            ["Respecter autrui", "Connaître les institutions européennes", "Apprendre le Code de la route", "Savoir voter"], "Respecter autrui",
            "Les trois finalités de l'EMC : respecter autrui, acquérir et partager les valeurs de la République, construire une culture civique."), None),
        # ── Sciences ──
        S('svt', "Sciences · l'aquaponie", Q(
            "Dans un système aquaponique, à quoi servent les bactéries ?",
            ["Elles transforment les déjections des poissons en nutriments assimilables par les plantes", "Elles nourrissent directement les poissons", "Elles produisent la lumière nécessaire aux plantes", "Elles chauffent l'eau du bac"],
            "Elles transforment les déjections des poissons en nutriments assimilables par les plantes",
            "Poissons, bactéries et plantes vivent en symbiose : les plantes absorbent ces nutriments et l'eau, purifiée, retourne aux poissons."), AQUA),
        S('svt', "Sciences · l'aquaponie", Q(
            "Quels sont les deux avantages de la nitrification ?",
            ["Elle élimine les ions ammonium, toxiques pour les poissons, et produit des nitrates utilisables par les plantes", "Elle réchauffe l'eau et la rend plus salée", "Elle produit du dioxygène pour les poissons", "Elle remplace la photosynthèse des plantes"],
            "Elle élimine les ions ammonium, toxiques pour les poissons, et produit des nitrates utilisables par les plantes",
            "Les déchets azotés donnent des ions ammonium NH₄⁺, nocifs à forte concentration ; les bactéries nitrifiantes les transforment en nitrites puis en nitrates NO₃⁻."), AQUA),
        S('svt', 'Sciences · la photosynthèse', Q(
            "Quels sont les produits de la photosynthèse ?",
            ["De la matière organique (sucres) et du dioxygène", "Du dioxyde de carbone et de l'eau", "Des sels minéraux", "De l'azote et de l'ammonium"], "De la matière organique (sucres) et du dioxygène",
            "Besoins : lumière, dioxyde de carbone, eau et sels minéraux. Produits : matière organique (glucose, amidon) et dioxygène rejeté dans l'air."), AQUA),
        S('svt', 'Sciences · la reproduction des plantes', Q(
            "Dans quel ordre se forment les tomates sur un plant en fleurs ?",
            ["Fleur, pollinisation, fécondation, transformation de la fleur en fruit contenant des graines", "Graine, fleur, racine, fruit", "Fruit, fleur, pollinisation, graine", "Pollinisation, germination, fleur, fruit"],
            "Fleur, pollinisation, fécondation, transformation de la fleur en fruit contenant des graines",
            "Le pollen est transporté jusqu'au pistil (pollinisation), la fécondation a lieu, puis l'ovaire de la fleur se transforme en fruit (la tomate) et les ovules en graines."), AQUA),
        S('physique_chimie', 'Sciences · la nitrification', Q(
            "Équation : NH₄⁺ + 2 O₂ → NO₃⁻ + 2 H⁺ + H₂O. Quelles espèces sont consommées ?",
            ["L'ion ammonium NH₄⁺ et le dioxygène O₂", "L'ion nitrate NO₃⁻ et l'eau H₂O", "Les ions hydrogène H⁺", "L'eau et le dioxygène"], "L'ion ammonium NH₄⁺ et le dioxygène O₂",
            "Les réactifs, à gauche de la flèche, sont consommés : ion ammonium et dioxygène. Les produits, à droite : ion nitrate, ions hydrogène et eau."), AQUA),
        S('physique_chimie', 'Sciences · la nitrification', Q(
            "Pourquoi faut-il oxygéner l'eau du bac ?",
            ["Les poissons respirent le dioxygène dissous, et les bactéries nitrifiantes en ont besoin (milieu aérobie)", "Pour refroidir l'eau", "Pour colorer l'eau", "Pour produire des ions ammonium"],
            "Les poissons respirent le dioxygène dissous, et les bactéries nitrifiantes en ont besoin (milieu aérobie)",
            "L'équation le montre : la nitrification consomme du dioxygène (2 O₂). Et les bactéries vivent « dans des conditions aérobies »."), AQUA),
        S('technologie', "Sciences · le choix d'une pompe", N(
            "Le bac contient 3 000 L d'eau, qui doivent circuler au moins 3 fois par heure. Quel débit minimal faut-il, en m³/h ?", 9,
            "3 000 L = 3 m³ ; 3 × 3 = 9 m³/h. Pompes : A 5,1 ; B 7,2 ; C 10,1 ; D 15,9 m³/h. Seules C et D conviennent."), AQUA),
        S('technologie', "Sciences · le choix d'une pompe", Q(
            "Pompe C : 100 W, 10,1 m³/h. Pompe D : 200 W, 15,9 m³/h. Le kWh coûte 0,20 €. Laquelle est la plus économique, et combien coûte-t-elle par jour ?",
            ["La pompe C : 0,1 kW × 24 h × 0,20 € = 0,48 € par jour", "La pompe D : 0,96 € par jour", "La pompe C : 4,80 € par jour", "Elles coûtent le même prix"],
            "La pompe C : 0,1 kW × 24 h × 0,20 € = 0,48 € par jour",
            "Les deux respectent le débit minimal ; C consomme deux fois moins (100 W contre 200 W) : 2,4 kWh par jour, soit 0,48 €, contre 0,96 € pour D."), AQUA),
        S('technologie', 'Sciences · la régulation de la serre', Q(
            "La température de la serre est régulée par un ventilateur piloté par une carte Micro:bit. Quel est le rôle du capteur dans ce système ?",
            ["Mesurer la température pour que le programme décide d'allumer ou non le ventilateur", "Faire tourner le ventilateur", "Alimenter la carte en énergie", "Afficher l'heure"],
            "Mesurer la température pour que le programme décide d'allumer ou non le ventilateur",
            "Chaîne d'information : capteur (acquérir), carte programmable (traiter), ventilateur (agir). Le programme compare la température mesurée à un seuil."), AQUA),
        # ── Arts ──
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "En quel matériau Lucio Fontana a-t-il réalisé « Cocodrillo » (1936-1937) ?",
            ["En terre cuite vernissée et peinte", "En bronze patiné", "En marbre blanc", "En bois sculpté"], "En terre cuite vernissée et peinte",
            "Vert, rouge et jaune sur la terre modelée : la matière travaillée au geste et la couleur non naturaliste éloignent le crocodile d'une simple copie du réel."),
          "Œuvre du sujet : Lucio Fontana (1899-1968), « Cocodrillo », 1936-1937, terre cuite vernissée et peinte, 18 × 130 × 42 cm."),
        S('arts', 'Arts plastiques · questionner la ressemblance', Q(
            "Pour quelles œuvres Lucio Fontana est-il surtout connu ?",
            ["Ses toiles fendues ou trouées (« Concetti spaziali »)", "Ses portraits de cour", "Ses fresques religieuses de la Renaissance", "Ses photographies de paysages"], "Ses toiles fendues ou trouées (« Concetti spaziali »)",
            "Fontana, fondateur du spatialisme, entaille ou perce la toile pour ouvrir l'œuvre sur l'espace. Le « Cocodrillo », plus ancien, montre déjà un travail expressif de la matière."), None),
        S('arts', 'Éducation musicale · le lied romantique', Q(
            "Qu'est-ce qu'un lied ?",
            ["Un chant pour voix et piano sur un poème, en langue allemande", "Une danse de cour à trois temps", "Une œuvre pour orchestre sans voix", "Un chant religieux en latin"], "Un chant pour voix et piano sur un poème, en langue allemande",
            "Le lied romantique unit musique et poésie. Schubert en a composé plus de 600, dont « Le Roi des aulnes » (Erlkönig) sur un poème de Goethe et les cycles « La Belle Meunière » et « Le Voyage d'hiver »."),
          "Question du sujet : « En vous appuyant sur quelques exemples musicaux de la période romantique, définissez ce qu'est le genre du lied. »"),
        S('arts', 'Éducation musicale · le lied romantique', Q(
            "D'après le souvenir de Mayrhofer cité dans le sujet, quelle atmosphère domine le « Voyage d'hiver » de Schubert ?",
            ["Grave et désespérée : « l'hiver avait commencé pour lui »", "Joyeuse et dansante", "Héroïque et triomphale", "Comique et légère"], "Grave et désespérée : « l'hiver avait commencé pour lui »",
            "Malade et éprouvé, Schubert choisit des poèmes de Wilhelm Müller sur l'errance et la solitude ; Mayrhofer parle d'une « ironie issue du désespoir »."),
          "Extrait du sujet : Johann Mayrhofer, Souvenirs sur Franz Schubert, 1829."),
        # ── Anglais ──
        S('anglais', 'Anglais · compréhension', Q(
            "According to the research, what proportion of children in Bradford do not play outdoors after school?",
            ["More than one in three (34%)", "One in ten", "Half of them", "Nine out of ten"], "More than one in three (34%)",
            "« More than one in three children in Bradford do not play outdoors after school and one in five do not at weekends. »"), BRADFORD),
        S('anglais', 'Anglais · compréhension', Q(
            "How old were the children in the study?", ["Between 7 and 12", "Between 3 and 6", "Between 12 and 18", "Under 2"], "Between 7 and 12",
            "« The lifestyles of 2,568 children in the city aged between 7 and 12. »"), BRADFORD),
        S('anglais', 'Anglais · compréhension', Q(
            "According to Dr Mark Ferguson, why is the decline in playing outdoors worrying?",
            ["It is linked to health issues such as obesity, anxiety and depression", "Children get dirty", "Parents have less free time", "Schools have fewer playgrounds"],
            "It is linked to health issues such as obesity, anxiety and depression",
            "« Our finding of a decline in playing outdoors is worrying because it is linked to various health issues, including obesity, anxiety and depression. »"), BRADFORD),
        S('anglais', 'Anglais · compréhension', Q(
            "What benefits do children who play outside more often have?",
            ["Better social skills and fewer behavioural and emotional problems", "Better marks in English", "More screen time", "Longer holidays"],
            "Better social skills and fewer behavioural and emotional problems",
            "« Children who played outside more often tended to have better social skills and fewer behavioural and emotional problems. »"), BRADFORD),
        S('anglais', 'Anglais · compréhension', Q(
            "Which “simple measures” are suggested to encourage outdoor play?",
            ["Organising outdoor events and creating safe play spaces", "Banning screens at school", "Giving children more homework", "Building more shopping centres"],
            "Organising outdoor events and creating safe play spaces",
            "He said “simple measures”, like organising outdoor events and creating safe play spaces, “can make a big difference”."), BRADFORD),
        S('anglais', 'Anglais · compréhension', Q(
            "What does Prof Rosie McEachan say children should do for their mental health?",
            ["Get off their screens and play outdoors after school and at weekends", "Sleep more at weekends", "Read more books indoors", "Do more sport at school only"],
            "Get off their screens and play outdoors after school and at weekends",
            "The research « shows how important it is for children's mental health to get off their screens and play outdoors after school and at weekends »."), BRADFORD),
        S('anglais', 'Anglais · lexique', Q(
            "In the text, the Born in Bradford programme “tracks” the health of mothers and children. “To track” means:",
            ["To follow and monitor over time", "To forget", "To cure", "To hide"], "To follow and monitor over time",
            "The programme collects data « over 18 years », from pregnancy onwards: it follows the same families over time."), BRADFORD),
        # ── Compléments (mêmes documents) ──
        S('physique_chimie', 'Sciences · la nitrification', Q(
            "La nitrification produit des ions hydrogène H⁺. Quel effet ont-ils sur l'eau du bac ?",
            ["Ils la rendent plus acide : le pH diminue", "Ils la rendent plus basique : le pH augmente", "Ils n'ont aucun effet", "Ils la rendent salée"], "Ils la rendent plus acide : le pH diminue",
            "Plus la concentration en ions H⁺ est grande, plus la solution est acide et plus son pH est faible. C'est pourquoi on surveille le pH en aquaponie."), AQUA),
        S('physique_chimie', 'Sciences · la nitrification', Q(
            "Quelle est la formule de l'ion nitrate, assimilable par les plantes ?",
            ["NO₃⁻", "NO₂⁻", "NH₄⁺", "H⁺"], "NO₃⁻",
            "NH₄⁺ est l'ion ammonium (toxique pour les poissons), NO₂⁻ l'ion nitrite (étape intermédiaire), NO₃⁻ l'ion nitrate."), AQUA),
        S('technologie', "Sciences · le choix d'une pompe", N(
            "La pompe C (100 W) fonctionne 24 heures sur 24. Quelle énergie consomme-t-elle par jour, en kWh ?", 2.4,
            "E = P × t = 0,1 kW × 24 h = 2,4 kWh. À 0,20 € le kWh, cela coûte 0,48 € par jour."), AQUA),
        S('technologie', "Sciences · le choix d'une pompe", Q(
            "Que mesure le débit d'une pompe, exprimé en m³/h ?",
            ["Le volume d'eau qui circule par heure", "La puissance électrique de la pompe", "La pression de l'eau", "La vitesse du moteur en tours par minute"], "Le volume d'eau qui circule par heure",
            "Le sujet le rappelle : « le débit est le volume d'eau qui circule pour une durée donnée ». La puissance, elle, s'exprime en watts."), AQUA),
        S('svt', "Sciences · l'aquaponie", Q(
            "Quelle relation unit poissons, plantes et bactéries dans un système aquaponique ?",
            ["Une symbiose : chacun profite de la présence des autres", "Une relation proie-prédateur", "Une compétition pour la lumière", "Un parasitisme des poissons par les plantes"], "Une symbiose : chacun profite de la présence des autres",
            "Les poissons fournissent les déjections, les bactéries les transforment en nutriments, les plantes les absorbent et purifient l'eau des poissons."), AQUA),
        S('svt', "Sciences · l'aquaponie", Q(
            "Grâce à quels êtres vivants la nitrification a-t-elle lieu ?",
            ["Des bactéries nitrifiantes (nitrosomonas et nitrobacter)", "Les poissons", "Les racines des tomates", "Des champignons"], "Des bactéries nitrifiantes (nitrosomonas et nitrobacter)",
            "Ces bactéries vivent en présence de dioxygène (aérobies) : elles transforment l'ammonium en nitrites, puis en nitrates."), AQUA),
        S('emc', "EMC · l'empathie", Q(
            "Lequel de ces gestes montre de l'empathie envers un camarade ?",
            ["Remarquer qu'il est mis à l'écart et lui proposer de jouer", "Rire avec les autres quand on se moque de lui", "Ne rien dire pour ne pas avoir d'ennuis", "Le dénoncer pour une faute qu'il n'a pas commise"],
            "Remarquer qu'il est mis à l'écart et lui proposer de jouer",
            "L'empathie, c'est percevoir ce que ressent l'autre et en tenir compte dans son comportement : elle est au cœur de la prévention du harcèlement."), None),
        S('emc', "EMC · l'empathie", Q(
            "Parmi ces dispositifs de classe, lequel développe l'écoute et l'empathie ?",
            ["Le débat réglé, où chacun écoute et reformule le point de vue des autres", "La dictée", "Le calcul mental", "La copie des leçons"],
            "Le débat réglé, où chacun écoute et reformule le point de vue des autres",
            "Les débats réglés, les conseils d'élèves et les jeux de rôle sont des démarches de l'EMC qui font travailler l'écoute de l'autre."), None),
        S('arts', 'Éducation musicale · le lied romantique', Q(
            "Sur quel poème de Goethe Schubert a-t-il composé l'un de ses lieder les plus célèbres ?",
            ["Le Roi des aulnes (Erlkönig)", "Le Bateau ivre", "Les Fleurs du mal", "Le Lac"], "Le Roi des aulnes (Erlkönig)",
            "Dans Le Roi des aulnes (1815), le piano imite le galop du cheval tandis qu'un seul chanteur fait entendre le père, l'enfant et le roi des aulnes."), None),
    ]),
]

from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('P-1', 0, I, 'pc-calcul-masse-volumique', [
  N("Un liquide de volume 200 mL a une masse de 160 g. Quelle est sa masse volumique (en g/mL) ?", 0.8, "ρ = m / V = 160 / 200 = 0,8 g/mL."),
  N("Un bloc d'aluminium a une masse volumique de 2,7 g/cm³ et un volume de 10 cm³. Quelle est sa masse (en g) ?", 27, "m = ρ × V = 2,7 × 10 = 27 g."),
  N("Un objet de masse 50 g a une masse volumique de 2,5 g/cm³. Quel est son volume (en cm³) ?", 20, "V = m / ρ = 50 / 2,5 = 20 cm³."),
]),
notion('P-1', 0, I, 'pc-modele-particulaire', [
  Q("Dans un solide, les particules sont…", ["éloignées et désordonnées", "proches et liées, souvent ordonnées", "proches et très mobiles", "absentes"], "proches et liées, souvent ordonnées", "C'est pourquoi un solide a une forme propre."),
  Q("Dans un gaz, les particules sont…", ["serrées et immobiles", "éloignées les unes des autres et très agitées", "rangées en réseau", "collées entre elles"], "éloignées les unes des autres et très agitées", "Les espaces entre particules expliquent que le gaz est compressible."),
  Q("Quand on chauffe un corps, que deviennent ses particules ?", ["Elles grossissent", "Elles s'agitent davantage", "Elles disparaissent", "Elles s'immobilisent"], "Elles s'agitent davantage", "La température mesure l'agitation des particules ; les particules elles-mêmes ne grossissent pas."),
]),
notion('P-1', 0, I, 'pc-solubilite', [
  N("La solubilité du sel dans l'eau est d'environ 360 g/L. Quelle masse maximale de sel (en g) peut-on dissoudre dans 0,5 L d'eau ?", 180, "360 × 0,5 = 180 g ; au-delà, la solution est saturée."),
  Q("Quand on augmente la température de l'eau, la solubilité du sucre…", ["diminue", "augmente", "reste nulle", "devient négative"], "augmente", "Pour la plupart des solides, la solubilité augmente avec la température."),
  Q("L'huile est-elle soluble dans l'eau ?", ["Oui", "Non, l'huile et l'eau sont non miscibles", "Seulement chaude", "Seulement salée"], "Non, l'huile et l'eau sont non miscibles", "L'huile, moins dense, forme une couche au-dessus de l'eau."),
]),
notion('P-1', 0, I, 'pc-concentration', [
  N("On dissout 20 g de sucre dans de l'eau pour obtenir 0,5 L de solution. Quelle est la concentration en masse (en g/L) ?", 40, "C = m / V = 20 / 0,5 = 40 g/L."),
  N("Une solution contient 15 g/L de sel. Quelle masse de sel (en g) y a-t-il dans 2 L ?", 30, "m = C × V = 15 × 2 = 30 g."),
  Q("Si l'on ajoute de l'eau à une solution, sa concentration…", ["augmente", "diminue", "reste la même", "devient infinie"], "diminue", "C'est une dilution : la masse de soluté reste la même, mais le volume augmente."),
]),
notion('P-1', 0, I, 'pc-separation-avancee', [
  Q("Quelle technique sépare les colorants d'une encre ?", ["La filtration", "La chromatographie", "La décantation", "L'aimantation"], "La chromatographie", "Les colorants migrent à des vitesses différentes sur le papier."),
  Q("Quelle technique permet d'obtenir de l'eau pure à partir d'eau salée ?", ["La filtration", "La distillation", "La décantation", "La chromatographie"], "La distillation", "L'eau est vaporisée puis liquéfiée ; le sel reste dans le récipient."),
  Q("Comment sépare-t-on la limaille de fer d'un mélange avec du sable ?", ["Par filtration", "À l'aide d'un aimant", "Par évaporation", "Par distillation"], "À l'aide d'un aimant", "Le fer est attiré par l'aimant, pas le sable."),
]),
notion('P-1', 1, I, 'pc-equation-reaction', [
  Q("Dans la combustion du méthane (CH₄ + 2 O₂ → CO₂ + 2 H₂O), quels sont les réactifs ?", ["CO₂ et H₂O", "CH₄ et O₂", "CH₄ et CO₂", "O₂ et H₂O"], "CH₄ et O₂", "Les réactifs sont à gauche de la flèche, les produits à droite."),
  Q("Pourquoi faut-il équilibrer une équation de réaction ?", ["Pour la décoration", "Parce que les atomes se conservent au cours d'une transformation chimique", "Parce que la masse disparaît", "Pour changer les produits"], "Parce que les atomes se conservent au cours d'une transformation chimique", "Il doit y avoir autant d'atomes de chaque sorte de part et d'autre."),
  N("Dans l'équation C + O₂ → CO₂, combien d'atomes d'oxygène y a-t-il de chaque côté ?", 2, "Deux atomes d'oxygène à gauche (O₂) et deux à droite (CO₂) : l'équation est équilibrée."),
]),
notion('P-1', 1, I, 'pc-conservation-masse-reaction', [
  N("Lors d'une réaction, 12 g de carbone réagissent entièrement avec 32 g de dioxygène. Quelle masse de CO₂ (en g) se forme ?", 44, "La masse se conserve : 12 + 32 = 44 g."),
  Q("Qui a énoncé au XVIIIe siècle « Rien ne se perd, rien ne se crée, tout se transforme » ?", ["Newton", "Lavoisier", "Pasteur", "Curie"], "Lavoisier", "Lavoisier a montré la conservation de la masse lors des transformations chimiques."),
  Q("On fait brûler du bois dans un récipient ouvert : il reste peu de cendres. La masse a-t-elle disparu ?", ["Oui", "Non, elle est partie sous forme de gaz (CO₂, vapeur d'eau)", "Oui, la chaleur l'a détruite", "Non, elle est restée dans les cendres"], "Non, elle est partie sous forme de gaz (CO₂, vapeur d'eau)", "En récipient fermé, on constaterait la conservation de la masse."),
]),
notion('P-1', 1, I, 'pc-acides-metaux', [
  Q("Quel gaz se dégage quand un acide réagit avec du fer ?", ["Le dioxygène", "Le dihydrogène", "Le CO₂", "Le diazote"], "Le dihydrogène", "Le dihydrogène produit une petite détonation au contact d'une flamme."),
  Q("Comment évolue le pH d'une solution acide qu'on dilue avec de l'eau ?", ["Il diminue", "Il augmente en se rapprochant de 7", "Il reste le même", "Il dépasse 14"], "Il augmente en se rapprochant de 7", "La solution devient moins acide."),
  Q("Quelle précaution prendre pour diluer un acide concentré ?", ["Verser l'eau dans l'acide", "Verser l'acide dans l'eau, lentement, avec lunettes et gants", "Mélanger à la main", "Chauffer l'acide"], "Verser l'acide dans l'eau, lentement, avec lunettes et gants", "Verser l'eau dans l'acide peut provoquer des projections dangereuses."),
]),
notion('P-1', 1, I, 'pc-ions', [
  Q("Qu'est-ce qu'un ion ?", ["Une molécule neutre", "Un atome ou un groupe d'atomes ayant gagné ou perdu des électrons", "Un noyau seul", "Un photon"], "Un atome ou un groupe d'atomes ayant gagné ou perdu des électrons", "Na⁺ a perdu un électron ; Cl⁻ en a gagné un."),
  Q("Quel ion est responsable du caractère acide d'une solution ?", ["L'ion hydroxyde HO⁻", "L'ion hydrogène H⁺", "L'ion sodium Na⁺", "L'ion chlorure Cl⁻"], "L'ion hydrogène H⁺", "Plus il y a d'ions H⁺, plus la solution est acide ; les ions HO⁻ rendent une solution basique."),
  Q("Le sel de cuisine (chlorure de sodium) est constitué…", ["d'ions Na⁺ et Cl⁻", "de molécules NaCl neutres liées en chaîne", "d'atomes d'or", "d'eau"], "d'ions Na⁺ et Cl⁻", "Dans l'eau, ces ions se dispersent : c'est pourquoi l'eau salée conduit le courant."),
]),
notion('P-1', 0, I, 'pc-atome-structure', [
  Q("De quoi est constitué un atome ?", ["D'un noyau entouré d'électrons", "De molécules", "De cellules", "D'ions seulement"], "D'un noyau entouré d'électrons", "Le noyau contient des protons et des neutrons."),
  Q("Quelle est la charge électrique d'un atome ?", ["Positive", "Négative", "Nulle : il est électriquement neutre", "Variable"], "Nulle : il est électriquement neutre", "Il y a autant d'électrons (négatifs) que de protons (positifs)."),
  Q("Où est concentrée presque toute la masse d'un atome ?", ["Dans les électrons", "Dans le noyau", "Dans le vide autour", "Elle est répartie uniformément"], "Dans le noyau", "L'atome est essentiellement constitué de vide."),
]),
notion('P-1', 2, I, 'pc-systeme-solaire-structure', [
  Q("Quelles planètes sont dites telluriques (rocheuses) ?", ["Jupiter, Saturne, Uranus, Neptune", "Mercure, Vénus, Terre, Mars", "Seulement la Terre", "Toutes"], "Mercure, Vénus, Terre, Mars", "Les quatre planètes externes sont des planètes géantes, gazeuses ou glacées."),
  Q("Quelle est la plus grande planète du système solaire ?", ["Saturne", "Jupiter", "La Terre", "Neptune"], "Jupiter", "Jupiter est plus de 300 fois plus massive que la Terre."),
  Q("Où se trouve la ceinture principale d'astéroïdes ?", ["Entre la Terre et Mars", "Entre Mars et Jupiter", "Au-delà de Neptune", "Autour de la Lune"], "Entre Mars et Jupiter", "Au-delà de Neptune se trouve la ceinture de Kuiper, où se situe Pluton."),
]),
notion('P-1', 2, I, 'pc-big-bang', [
  Q("Selon le modèle du Big Bang, l'Univers…", ["est immobile et éternel", "est en expansion depuis environ 13,8 milliards d'années", "a 6 000 ans", "rétrécit"], "est en expansion depuis environ 13,8 milliards d'années", "L'expansion a été observée grâce à l'éloignement des galaxies."),
  Q("D'où viennent la plupart des atomes plus lourds que l'hélium, comme le carbone de notre corps ?", ["Du noyau de la Terre", "Des réactions nucléaires au cœur des étoiles", "Des volcans", "Des océans"], "Des réactions nucléaires au cœur des étoiles", "« Nous sommes des poussières d'étoiles. »"),
  Q("Quelle est l'origine de l'énergie du Soleil ?", ["La combustion du charbon", "La fusion nucléaire de l'hydrogène en hélium", "L'électricité", "La rotation de la Terre"], "La fusion nucléaire de l'hydrogène en hélium", "La fusion libère une énergie considérable."),
]),
notion('P-2', 0, I, 'pc-vitesse-unites', [
  N("Un TGV roule à 324 km/h. Quelle est sa vitesse en m/s ?", 90, "324 ÷ 3,6 = 90 m/s."),
  N("Une voiture roule à 90 km/h. Quelle distance (en km) parcourt-elle en 20 minutes ?", 30, "20 min = 1/3 h ; d = 90 × 1/3 = 30 km."),
  N("Un nageur parcourt 50 m en 25 s. Quelle est sa vitesse en km/h ?", 7.2, "v = 50 / 25 = 2 m/s, et 2 × 3,6 = 7,2 km/h."),
]),
notion('P-2', 0, I, 'pc-mouvement-accelere', [
  Q("Une balle lâchée sans vitesse initiale tombe. Son mouvement est…", ["uniforme", "accéléré", "ralenti", "circulaire"], "accéléré", "Son poids augmente sa vitesse au cours de la chute."),
  Q("Sur une chronophotographie, les positions d'un objet sont de plus en plus rapprochées. Son mouvement est…", ["accéléré", "ralenti", "uniforme", "circulaire"], "ralenti", "Des intervalles réguliers de temps, des distances de plus en plus courtes : l'objet ralentit."),
  Q("Sur une chronophotographie, les positions sont régulièrement espacées et alignées. Le mouvement est…", ["rectiligne uniforme", "circulaire accéléré", "rectiligne ralenti", "immobile"], "rectiligne uniforme", "Distances égales pendant des durées égales : vitesse constante."),
]),
notion('P-2', 1, I, 'pc-diagramme-interactions', [
  Q("Un livre est posé sur une table. Quelles actions s'exercent sur lui ?", ["Aucune", "Son poids et l'action de la table (réaction du support)", "Seulement son poids", "Seulement l'action de la table"], "Son poids et l'action de la table (réaction du support)", "Les deux actions se compensent : le livre reste immobile."),
  Q("Si les actions qui s'exercent sur un objet immobile se compensent, l'objet…", ["accélère", "reste immobile", "tombe", "tourne"], "reste immobile", "C'est le principe d'inertie : sans action non compensée, le mouvement ne change pas."),
  Q("Comment représente-t-on une force sur un schéma ?", ["Par un point", "Par une flèche (direction, sens, valeur, point d'application)", "Par un cercle", "Par un nombre seul"], "Par une flèche (direction, sens, valeur, point d'application)", "La longueur de la flèche est proportionnelle à la valeur de la force."),
]),
notion('P-2', 1, I, 'pc-poids-lune', [
  N("Un astronaute a une masse de 80 kg. Quel est son poids (en N) sur la Lune, où g = 1,6 N/kg ?", 128, "P = m × g = 80 × 1,6 = 128 N."),
  N("Un objet de masse 3 kg pèse 29,4 N sur Terre. Quelle est la valeur de g (en N/kg) ?", 9.8, "g = P / m = 29,4 / 3 = 9,8 N/kg."),
  Q("Pourquoi pèse-t-on moins sur la Lune que sur Terre ?", ["Notre masse diminue", "L'attraction de la Lune est plus faible car sa masse est plus petite", "Il n'y a pas d'air", "La Lune tourne plus vite"], "L'attraction de la Lune est plus faible car sa masse est plus petite", "L'intensité de la pesanteur lunaire vaut environ 1/6 de celle de la Terre."),
]),
notion('P-2', 0, I, 'pc-distance-freinage', [
  Q("La distance d'arrêt d'un véhicule est la somme…", ["de la vitesse et du temps", "de la distance parcourue pendant le temps de réaction et de la distance de freinage", "de la longueur et de la largeur de la voiture", "de deux temps de réaction"], "de la distance parcourue pendant le temps de réaction et de la distance de freinage", "La distance de freinage augmente avec le carré de la vitesse."),
  N("Un conducteur roule à 20 m/s et met 1 s à réagir. Quelle distance (en m) parcourt-il pendant ce temps ?", 20, "d = v × t = 20 × 1 = 20 m."),
  Q("Si la vitesse double, la distance de freinage est multipliée par…", ["2", "4", "1", "8"], "4", "L'énergie cinétique, donc la distance de freinage, est proportionnelle au carré de la vitesse."),
]),
notion('P-3', 1, I, 'pc-energie-cinetique', [
  Q("Quelle est la formule de l'énergie cinétique ?", ["Ec = m × v", "Ec = ½ × m × v²", "Ec = m × g", "Ec = U × I"], "Ec = ½ × m × v²", "Avec m en kg et v en m/s, l'énergie est en joules."),
  N("Quelle est l'énergie cinétique (en J) d'un objet de 2 kg se déplaçant à 3 m/s ?", 9, "Ec = ½ × 2 × 3² = 9 J."),
  N("Quelle est l'énergie cinétique (en J) d'une balle de 0,5 kg lancée à 10 m/s ?", 25, "Ec = ½ × 0,5 × 10² = 25 J."),
]),
notion('P-3', 1, I, 'pc-energie-potentielle', [
  Q("Quelle forme d'énergie possède un objet placé en hauteur ?", ["L'énergie cinétique", "L'énergie de position (potentielle de pesanteur)", "L'énergie chimique", "L'énergie lumineuse"], "L'énergie de position (potentielle de pesanteur)", "Elle augmente avec la masse et l'altitude : Ep = m × g × h."),
  N("Quelle est l'énergie de position (en J) d'un objet de 2 kg à 5 m de hauteur (g = 10 N/kg) ?", 100, "Ep = m × g × h = 2 × 10 × 5 = 100 J."),
  Q("Lors de la chute d'un objet, en négligeant les frottements…", ["l'énergie de position se transforme en énergie cinétique", "l'énergie cinétique diminue", "l'énergie disparaît", "l'énergie de position augmente"], "l'énergie de position se transforme en énergie cinétique", "L'énergie mécanique (somme des deux) se conserve en l'absence de frottements."),
]),
notion('P-3', 1, I, 'pc-puissance-energie', [
  N("Un radiateur de 2 000 W fonctionne pendant 3 h. Quelle énergie (en kWh) consomme-t-il ?", 6, "E = P × t = 2 kW × 3 h = 6 kWh."),
  N("Une lampe de 10 W fonctionne 100 h. Combien de kWh consomme-t-elle ?", 1, "E = 10 W × 100 h = 1 000 Wh = 1 kWh."),
  N("Le kWh coûte 0,25 €. Combien coûte (en €) le fonctionnement d'un four de 2,5 kW pendant 2 h ?", 1.25, "E = 2,5 × 2 = 5 kWh, et 5 × 0,25 = 1,25 €."),
]),
notion('P-3', 1, I, 'pc-chaine-energetique', [
  Q("Dans une centrale thermique à gaz, quelle est la chaîne d'énergie ?", ["Lumineuse → électrique", "Chimique → thermique → mécanique → électrique", "Électrique → chimique", "Nucléaire → lumineuse"], "Chimique → thermique → mécanique → électrique", "La combustion chauffe de l'eau ; la vapeur fait tourner une turbine reliée à un alternateur."),
  Q("Quel élément commun transforme l'énergie mécanique en énergie électrique dans la plupart des centrales ?", ["La pile", "L'alternateur", "Le panneau solaire", "La lampe"], "L'alternateur", "L'alternateur est présent dans les centrales nucléaires, hydrauliques, thermiques et les éoliennes."),
  Q("Pourquoi les centrales électriques ont-elles toutes des « pertes » ?", ["Par mauvaise construction", "Une partie de l'énergie est inévitablement dissipée sous forme de chaleur", "L'énergie disparaît", "Elles ne fonctionnent pas"], "Une partie de l'énergie est inévitablement dissipée sous forme de chaleur", "Le rendement d'une centrale nucléaire est d'environ 33 %."),
]),
notion('P-3', 2, I, 'pc-loi-ohm', [
  Q("Quelle est la loi d'Ohm ?", ["U = R × I", "P = U / I", "E = m × c²", "v = d × t"], "U = R × I", "La tension aux bornes d'un conducteur ohmique est proportionnelle à l'intensité."),
  N("Une résistance de 100 Ω est traversée par un courant de 0,05 A. Quelle est la tension (en V) à ses bornes ?", 5, "U = R × I = 100 × 0,05 = 5 V."),
  N("Une résistance est soumise à une tension de 12 V et traversée par 0,2 A. Quelle est sa valeur (en Ω) ?", 60, "R = U / I = 12 / 0,2 = 60 Ω."),
]),
notion('P-3', 2, I, 'pc-puissance-electrique', [
  Q("Quelle relation relie la puissance électrique, la tension et l'intensité ?", ["P = U × I", "P = U / I", "P = U + I", "P = R × I"], "P = U × I", "Avec U en volts et I en ampères, P est en watts."),
  N("Un appareil fonctionne sous 230 V et est traversé par un courant de 2 A. Quelle est sa puissance (en W) ?", 460, "P = U × I = 230 × 2 = 460 W."),
  N("Une bouilloire de 2 300 W fonctionne sous 230 V. Quelle est l'intensité (en A) du courant ?", 10, "I = P / U = 2 300 / 230 = 10 A."),
]),
notion('P-3', 2, I, 'pc-lois-circuits', [
  Q("Dans un circuit en série, l'intensité du courant…", ["est la même en tout point", "diminue après chaque lampe", "est nulle", "double après chaque lampe"], "est la même en tout point", "C'est la loi d'unicité de l'intensité dans un circuit en série."),
  N("Dans un circuit en série, le générateur délivre 6 V. La tension aux bornes d'une lampe est 2,5 V. Quelle est la tension (en V) aux bornes de la seconde lampe ?", 3.5, "Loi d'additivité des tensions : 6 − 2,5 = 3,5 V."),
  N("Dans un circuit en dérivation, la branche principale est parcourue par 0,5 A et une branche dérivée par 0,2 A. Quelle est l'intensité (en A) dans l'autre branche ?", 0.3, "Loi des nœuds : 0,5 = 0,2 + I, donc I = 0,3 A."),
]),
notion('P-3', 0, I, 'pc-energie-nucleaire', [
  Q("Quelle part environ de l'électricité française est produite par le nucléaire ?", ["10 %", "Environ deux tiers", "100 %", "Moins de 1 %"], "Environ deux tiers", "Le nucléaire a fourni environ 65 à 70 % de l'électricité française ces dernières années."),
  Q("Quel est le principal avantage du nucléaire pour le climat ?", ["Il ne produit aucun déchet", "Il émet très peu de CO₂ par kWh produit", "Il est renouvelable", "Il ne nécessite pas d'eau"], "Il émet très peu de CO₂ par kWh produit", "Son principal inconvénient est la gestion des déchets radioactifs à très longue durée de vie."),
  Q("Quelle réaction se produit dans les réacteurs des centrales nucléaires actuelles ?", ["La fusion de l'hydrogène", "La fission de noyaux d'uranium", "La combustion du charbon", "La photosynthèse"], "La fission de noyaux d'uranium", "La fission casse des noyaux lourds ; la fusion, au cœur des étoiles, assemble des noyaux légers."),
]),
notion('P-4', 0, I, 'pc-distance-orage', [
  N("On entend le tonnerre 6 s après avoir vu l'éclair. À quelle distance (en m) est l'orage (son : 340 m/s) ?", 2040, "d = 340 × 6 = 2 040 m, soit environ 2 km."),
  N("Un orage est à 1 700 m. Combien de secondes s'écoulent entre l'éclair et le tonnerre (son : 340 m/s) ?", 5, "t = 1 700 / 340 = 5 s."),
  Q("Pourquoi peut-on négliger la durée de trajet de la lumière de l'éclair ?", ["Elle est infinie", "Elle est très brève car la lumière est environ un million de fois plus rapide que le son", "Elle est nulle", "La lumière est plus lente"], "Elle est très brève car la lumière est environ un million de fois plus rapide que le son", "La lumière parcourt 2 km en quelques millionièmes de seconde."),
]),
notion('P-4', 0, I, 'pc-son-milieux', [
  Q("Dans quel milieu le son se propage-t-il le plus vite ?", ["L'air", "L'eau", "L'acier", "Le vide"], "L'acier", "Environ 340 m/s dans l'air, 1 500 m/s dans l'eau et 5 000 m/s dans l'acier."),
  N("Quelle est la vitesse approximative du son dans l'eau (en m/s) ?", 1500, "Le son va environ 4 fois plus vite dans l'eau que dans l'air."),
  Q("Pourquoi les astronautes ne peuvent-ils pas se parler directement dans l'espace, sans radio ?", ["Ils portent des casques épais", "Le son ne se propage pas dans le vide", "Le froid bloque le son", "Ils sont trop loin"], "Le son ne se propage pas dans le vide", "Les ondes radio, électromagnétiques, se propagent, elles, dans le vide."),
]),
notion('P-4', 0, I, 'pc-periode-frequence', [
  Q("Quelle est la relation entre fréquence et période ?", ["f = T", "f = 1 / T", "f = T × 2", "f = T²"], "f = 1 / T", "La période T est la durée d'une vibration (en s), la fréquence f le nombre de vibrations par seconde (en Hz)."),
  N("Un son a une période de 0,002 s. Quelle est sa fréquence (en Hz) ?", 500, "f = 1 / T = 1 / 0,002 = 500 Hz."),
  N("Le « la » du diapason a une fréquence de 440 Hz. Combien de vibrations effectue-t-il en 2 secondes ?", 880, "440 vibrations par seconde × 2 s = 880 vibrations."),
]),
notion('P-4', 1, I, 'pc-reflexion-refraction', [
  Q("Que se passe-t-il quand la lumière rencontre un miroir ?", ["Elle est absorbée totalement", "Elle est réfléchie", "Elle accélère", "Elle s'arrête"], "Elle est réfléchie", "L'angle de réflexion est égal à l'angle d'incidence."),
  Q("Pourquoi une paille plongée dans un verre d'eau paraît-elle brisée ?", ["La paille se plie", "La lumière change de direction en passant de l'eau à l'air (réfraction)", "L'eau déforme la paille", "C'est une illusion sans cause physique"], "La lumière change de direction en passant de l'eau à l'air (réfraction)", "La réfraction est le changement de direction de la lumière quand elle change de milieu."),
  Q("Sur quel principe repose une loupe ?", ["La réflexion", "La réfraction de la lumière par une lentille convergente", "L'absorption", "La diffusion"], "La réfraction de la lumière par une lentille convergente", "La lentille convergente fait converger les rayons et grossit l'image."),
]),
notion('P-4', 1, I, 'pc-synthese-couleurs', [
  Q("Quelles sont les trois couleurs primaires de la synthèse additive (écrans) ?", ["Rouge, jaune, bleu", "Rouge, vert, bleu", "Cyan, magenta, jaune", "Noir, blanc, gris"], "Rouge, vert, bleu", "Superposées, ces trois lumières colorées donnent du blanc."),
  Q("Quelle couleur obtient-on en superposant des lumières rouge et verte ?", ["Marron", "Jaune", "Bleu", "Noir"], "Jaune", "En synthèse additive, rouge + vert = jaune."),
  Q("Quelles sont les couleurs primaires de la synthèse soustractive (imprimante) ?", ["Rouge, vert, bleu", "Cyan, magenta, jaune", "Noir et blanc", "Orange, violet, vert"], "Cyan, magenta, jaune", "Les encres absorbent (soustraient) une partie de la lumière."),
]),
notion('P-4', 1, I, 'pc-codage-information', [
  Q("Qu'est-ce qu'un signal numérique ?", ["Un signal qui varie de façon continue", "Un signal codé par une suite de valeurs discrètes, souvent 0 et 1", "Un signal uniquement sonore", "Un signal lumineux visible"], "Un signal codé par une suite de valeurs discrètes, souvent 0 et 1", "L'information est codée en binaire (bits)."),
  N("Combien de bits y a-t-il dans un octet ?", 8, "Un octet = 8 bits, ce qui permet 256 combinaisons différentes."),
  N("Combien de valeurs différentes peut-on coder avec 3 bits ?", 8, "2³ = 8 valeurs, de 000 à 111."),
]),
notion('P-4', 0, I, 'pc-protection-auditive', [
  Q("À partir de quel niveau sonore environ y a-t-il un risque pour l'audition en cas d'exposition prolongée ?", ["30 dB", "85 dB", "10 dB", "0 dB"], "85 dB", "Au-delà de 120 dB, le son devient douloureux (seuil de douleur)."),
  Q("Quel geste protège l'audition lors d'un concert ?", ["Se placer près des enceintes", "Porter des bouchons d'oreilles et faire des pauses", "Augmenter le son du casque", "Crier pour s'habituer"], "Porter des bouchons d'oreilles et faire des pauses", "Les lésions de l'oreille interne sont irréversibles."),
  Q("Comment appelle-t-on le sifflement persistant dans l'oreille après une exposition à un bruit intense ?", ["Un acouphène", "Un écho", "Une otite", "Une réverbération"], "Un acouphène", "Les acouphènes peuvent devenir permanents."),
]),
notion('P-2', 1, I, 'pc-frottements', [
  Q("Pourquoi une bille qui roule sur le sol finit-elle par s'arrêter ?", ["Elle est fatiguée", "À cause des frottements qui s'opposent au mouvement", "À cause de son poids seul", "Par hasard"], "À cause des frottements qui s'opposent au mouvement", "Sans frottement, elle continuerait à vitesse constante (principe d'inertie)."),
  Q("Pourquoi les pneus des voitures ont-ils des sculptures ?", ["Pour la décoration", "Pour augmenter l'adhérence, notamment sur route mouillée", "Pour réduire la masse", "Pour faire du bruit"], "Pour augmenter l'adhérence, notamment sur route mouillée", "Les sculptures évacuent l'eau et limitent l'aquaplaning."),
  Q("Quelle forme réduit la résistance de l'air pour un véhicule ?", ["Une forme carrée", "Une forme aérodynamique profilée", "Une forme plate face au vent", "La forme n'a aucune importance"], "Une forme aérodynamique profilée", "Un véhicule profilé consomme moins d'énergie à grande vitesse."),
  N("Une voiture de 1 000 kg roule à 20 m/s. Quelle est son énergie cinétique (en kJ) ?", 200, "Ec = ½ × 1 000 × 20² = 200 000 J = 200 kJ, dissipés en chaleur lors du freinage."),
]),
]

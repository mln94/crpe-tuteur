from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('P-1', 0, D, 'pc-courbe-changement-etat', [
  Q("On chauffe de la glace à −10 °C jusqu'à obtenir de l'eau à 20 °C. Combien de paliers de température observe-t-on ?", ["Aucun", "Un, à 0 °C", "Deux", "Trois"], "Un, à 0 °C", "Un seul changement d'état (la fusion) se produit dans cet intervalle, à température constante."),
  Q("Pourquoi l'eau salée gèle-t-elle à une température inférieure à 0 °C ?", ["Le sel la réchauffe", "Le sel dissous abaisse la température de solidification", "Le sel est un isolant", "Elle ne gèle jamais"], "Le sel dissous abaisse la température de solidification", "C'est pourquoi on sale les routes en hiver."),
  Q("En haute montagne, l'eau bout à une température…", ["supérieure à 100 °C", "inférieure à 100 °C", "égale à 100 °C", "supérieure à 150 °C"], "inférieure à 100 °C", "La pression atmosphérique est plus faible en altitude : environ 70 °C au sommet de l'Everest."),
]),
notion('P-1', 1, D, 'pc-equilibrer', [
  Q("Quelle équation de combustion du méthane est correctement équilibrée ?", ["CH₄ + O₂ → CO₂ + H₂O", "CH₄ + 2 O₂ → CO₂ + 2 H₂O", "CH₄ + 3 O₂ → 2 CO₂ + H₂O", "2 CH₄ + O₂ → CO₂ + H₂O"], "CH₄ + 2 O₂ → CO₂ + 2 H₂O", "À gauche : 1 C, 4 H, 4 O ; à droite : 1 C, 4 H, 2 + 2 = 4 O."),
  N("Équilibrez : … H₂ + O₂ → 2 H₂O. Quel coefficient faut-il devant H₂ ?", 2, "2 H₂ + O₂ → 2 H₂O : 4 atomes H et 2 atomes O de chaque côté."),
  N("Dans la combustion complète du propane C₃H₈ + 5 O₂ → 3 CO₂ + … H₂O, quel coefficient faut-il devant H₂O ?", 4, "8 atomes d'hydrogène à gauche, donc 4 H₂O à droite ; on vérifie : 10 O de chaque côté."),
]),
notion('P-1', 1, D, 'pc-combustion-incomplete', [
  Q("Quel gaz mortel produit une combustion incomplète (manque de dioxygène) ?", ["Le dioxyde de carbone", "Le monoxyde de carbone", "Le dioxygène", "L'hélium"], "Le monoxyde de carbone", "Incolore et inodore, il provoque chaque année des intoxications ; il faut aérer et faire entretenir chaudières et poêles."),
  Q("Quel indice signale une combustion incomplète d'une flamme de gaz ?", ["Une flamme bleue", "Une flamme jaune qui noircit les ustensiles (suie)", "Une absence de flamme", "Une flamme verte"], "Une flamme jaune qui noircit les ustensiles (suie)", "La suie est du carbone non brûlé."),
  Q("Quel appareil permet de prévenir une intoxication au monoxyde de carbone ?", ["Un détecteur de fumée", "Un détecteur de monoxyde de carbone", "Un thermomètre", "Un baromètre"], "Un détecteur de monoxyde de carbone", "Le détecteur de fumée, obligatoire dans les logements, ne détecte pas le CO."),
]),
notion('P-1', 1, D, 'pc-ph-dilution', [
  Q("Quand on dilue 10 fois une solution acide de pH 2, son pH devient environ…", ["1", "3", "7", "20"], "3", "Diluer 10 fois une solution acide augmente son pH d'environ une unité."),
  Q("Peut-on obtenir une solution basique en diluant une solution acide avec de l'eau pure ?", ["Oui", "Non, le pH se rapproche de 7 sans le dépasser", "Oui, si on dilue beaucoup", "Seulement à chaud"], "Non, le pH se rapproche de 7 sans le dépasser", "L'eau pure est neutre."),
  Q("Que se passe-t-il quand on mélange un acide et une base en proportions adaptées ?", ["Rien", "Une réaction qui peut conduire à une solution neutre", "Une explosion obligatoire", "La solution devient plus acide"], "Une réaction qui peut conduire à une solution neutre", "C'est une réaction acido-basique, qui dégage de la chaleur."),
]),
notion('P-1', 2, D, 'pc-distances-astronomiques', [
  N("La lumière parcourt 300 000 km/s. Quelle distance (en millions de km) parcourt-elle en 500 s ?", 150, "300 000 × 500 = 150 000 000 km, soit la distance Terre-Soleil."),
  Q("Quand on observe une étoile située à 100 années-lumière, on la voit…", ["telle qu'elle est maintenant", "telle qu'elle était il y a 100 ans", "telle qu'elle sera dans 100 ans", "telle qu'elle était il y a 100 secondes"], "telle qu'elle était il y a 100 ans", "Regarder loin, c'est regarder dans le passé."),
  Q("Quelle est l'unité astronomique (ua) ?", ["La distance Terre-Lune", "La distance moyenne Terre-Soleil, environ 150 millions de km", "Une année-lumière", "Le rayon de la Terre"], "La distance moyenne Terre-Soleil, environ 150 millions de km", "L'ua est commode pour les distances dans le système solaire."),
]),
notion('P-2', 0, D, 'pc-vitesse-moyenne-pieges', [
  N("Un cycliste monte une côte de 10 km à 10 km/h puis la redescend à 30 km/h. Quelle est sa vitesse moyenne (en km/h) sur l'aller-retour ?", 15, "Durées : 1 h + 1/3 h = 4/3 h pour 20 km ; v = 20 / (4/3) = 15 km/h, et non 20 km/h."),
  N("Un train parcourt 150 km en 1 h 15 min. Quelle est sa vitesse moyenne (en km/h) ?", 120, "1 h 15 min = 1,25 h ; v = 150 / 1,25 = 120 km/h."),
  N("Sur une chronophotographie, deux positions successives d'une bille sont séparées de 5 cm et prises à 0,1 s d'intervalle. Quelle est sa vitesse (en m/s) ?", 0.5, "v = 0,05 m / 0,1 s = 0,5 m/s."),
  N("Une sonde est à 225 millions de km de la Terre. Combien de minutes un signal radio (300 000 km/s) met-il pour lui parvenir ?", 12.5, "t = 225 000 000 / 300 000 = 750 s = 12,5 min."),
]),
notion('P-2', 1, D, 'pc-gravitation-loi', [
  Q("Comment varie l'attraction gravitationnelle entre deux objets si leur distance double ?", ["Elle double", "Elle est divisée par 4", "Elle est divisée par 2", "Elle ne change pas"], "Elle est divisée par 4", "La force est inversement proportionnelle au carré de la distance."),
  Q("De quoi dépend la force de gravitation entre deux corps ?", ["De leurs couleurs", "De leurs masses et de la distance qui les sépare", "De leur température", "De leur vitesse uniquement"], "De leurs masses et de la distance qui les sépare", "F = G × m₁ × m₂ / d²."),
  Q("La Terre attire la Lune. La Lune attire-t-elle la Terre ?", ["Non", "Oui, avec une force de même valeur", "Oui, avec une force beaucoup plus faible", "Seulement la nuit"], "Oui, avec une force de même valeur", "Les deux forces ont même valeur et sens opposés : c'est l'interaction réciproque. L'effet de la Lune sur la Terre se voit dans les marées."),
]),
notion('P-2', 1, D, 'pc-principe-inertie', [
  Q("Selon le principe d'inertie, un objet sur lequel les actions se compensent…", ["s'arrête toujours", "reste immobile ou garde un mouvement rectiligne uniforme", "accélère", "tourne en rond"], "reste immobile ou garde un mouvement rectiligne uniforme", "Une sonde spatiale loin de tout astre continue en ligne droite sans moteur."),
  Q("Pourquoi les passagers sont-ils projetés vers l'avant lors d'un freinage brusque ?", ["Une force les pousse vers l'avant", "Par inertie, leur corps tend à conserver son mouvement", "À cause du vent", "À cause de la gravité"], "Par inertie, leur corps tend à conserver son mouvement", "D'où l'importance de la ceinture de sécurité."),
  Q("Un parachutiste descend à vitesse constante en ligne droite. Que peut-on dire des actions qui s'exercent sur lui ?", ["Son poids est plus grand que la résistance de l'air", "Elles se compensent", "Il n'y a aucune action", "La résistance de l'air est plus grande que son poids"], "Elles se compensent", "Mouvement rectiligne uniforme : poids et résistance de l'air se compensent."),
]),
notion('P-3', 1, D, 'pc-energie-cinetique-vitesse', [
  N("Si la vitesse d'un véhicule passe de 50 km/h à 100 km/h, par combien son énergie cinétique est-elle multipliée ?", 4, "Ec est proportionnelle à v² : (100/50)² = 4."),
  N("Une voiture de 1 200 kg roule à 72 km/h. Quelle est son énergie cinétique (en kJ) ?", 240, "72 km/h = 20 m/s ; Ec = ½ × 1 200 × 20² = 240 000 J = 240 kJ."),
  N("Un objet de 4 kg a une énergie cinétique de 200 J. Quelle est sa vitesse (en m/s) ?", 10, "v² = 2 × Ec / m = 400 / 4 = 100, donc v = 10 m/s."),
]),
notion('P-3', 1, D, 'pc-conservation-energie-mecanique', [
  N("Un objet est lâché sans vitesse d'une hauteur de 5 m (g = 10 N/kg, frottements négligés). Quelle est sa vitesse (en m/s) en arrivant au sol ?", 10, "m g h = ½ m v², donc v² = 2 × 10 × 5 = 100 et v = 10 m/s."),
  Q("Un skateur descend une rampe. Si l'on néglige les frottements, son énergie mécanique…", ["augmente", "diminue", "se conserve", "devient nulle"], "se conserve", "L'énergie de position se transforme en énergie cinétique."),
  Q("Pourquoi une balle qui rebondit remonte-t-elle de moins en moins haut ?", ["Sa masse diminue", "Une partie de son énergie mécanique est dissipée (chaleur, son, déformation)", "La gravité augmente", "L'énergie est détruite"], "Une partie de son énergie mécanique est dissipée (chaleur, son, déformation)", "L'énergie totale se conserve, mais l'énergie mécanique diminue."),
]),
notion('P-3', 1, D, 'pc-rendement', [
  N("Un moteur reçoit 500 J d'énergie électrique et fournit 400 J d'énergie mécanique. Quel est son rendement (en %) ?", 80, "η = 400 / 500 = 0,8, soit 80 %."),
  N("Une lampe de rendement 20 % reçoit 50 J. Combien de joules d'énergie lumineuse produit-elle ?", 10, "50 × 0,20 = 10 J ; les 40 J restants sont dissipés en chaleur."),
  Q("Un rendement peut-il être supérieur à 100 % ?", ["Oui, pour les bons appareils", "Non, l'énergie utile ne peut pas dépasser l'énergie reçue", "Oui, pour les panneaux solaires", "Oui, en hiver"], "Non, l'énergie utile ne peut pas dépasser l'énergie reçue", "Ce serait contraire à la conservation de l'énergie."),
]),
notion('P-3', 2, D, 'pc-protection-installation', [
  Q("Quel est le rôle de la prise de terre dans une installation électrique ?", ["Augmenter la puissance", "Évacuer vers le sol un courant de fuite pour protéger les personnes", "Économiser l'électricité", "Faire briller les lampes"], "Évacuer vers le sol un courant de fuite pour protéger les personnes", "Associée au disjoncteur différentiel, elle évite l'électrocution."),
  Q("Que détecte un disjoncteur différentiel ?", ["Une surtension", "Une différence entre le courant qui entre et celui qui sort, signe d'une fuite", "La couleur des fils", "La température"], "Une différence entre le courant qui entre et celui qui sort, signe d'une fuite", "Il coupe le courant dès qu'une fuite (par exemple à travers une personne) est détectée."),
  N("On branche sur une multiprise un radiateur de 2 000 W et un four de 1 680 W, sous 230 V. Quelle est l'intensité totale (en A) ?", 16, "I = P / U = 3 680 / 230 = 16 A : c'est la limite de nombreuses multiprises."),
]),
notion('P-3', 2, D, 'pc-ohm-circuits', [
  N("Deux résistances de 100 Ω et 200 Ω sont en série sous 6 V. Quelle est l'intensité (en A) du courant ?", 0.02, "La résistance équivalente vaut 300 Ω ; I = 6 / 300 = 0,02 A."),
  N("Dans le même montage (100 Ω et 200 Ω en série, 0,02 A), quelle est la tension (en V) aux bornes de la résistance de 200 Ω ?", 4, "U = R × I = 200 × 0,02 = 4 V ; l'autre résistance a 2 V, et 2 + 4 = 6 V."),
  Q("Quand on ajoute une lampe en série dans un circuit, l'intensité du courant…", ["augmente", "diminue", "reste la même", "devient infinie"], "diminue", "La résistance totale du circuit augmente."),
]),
notion('P-4', 0, D, 'pc-ondes-comparaison', [
  Q("Laquelle de ces affirmations est vraie ?", ["Le son et la lumière se propagent tous deux dans le vide", "La lumière se propage dans le vide, pas le son", "Le son se propage dans le vide, pas la lumière", "Aucun ne se propage dans le vide"], "La lumière se propage dans le vide, pas le son", "Le son est une onde mécanique ; la lumière, une onde électromagnétique."),
  N("Une onde sonore de 680 Hz se propage dans l'air à 340 m/s. Quelle est sa longueur d'onde (en m) ?", 0.5, "λ = v / f = 340 / 680 = 0,5 m."),
  Q("Les ondes radio, la lumière visible et les rayons X sont tous des…", ["ondes sonores", "ondes électromagnétiques", "ondes mécaniques", "particules de matière"], "ondes électromagnétiques", "Elles diffèrent par leur longueur d'onde et voyagent toutes à la vitesse de la lumière dans le vide."),
]),
notion('P-4', 1, D, 'pc-debit-numerique', [
  N("Un fichier de 40 mégaoctets est téléchargé à 8 mégaoctets par seconde. Combien de secondes dure le téléchargement ?", 5, "t = 40 / 8 = 5 s."),
  N("Un débit de 80 mégabits par seconde correspond à combien de mégaoctets par seconde ?", 10, "1 octet = 8 bits, donc 80 / 8 = 10 Mo/s."),
  N("Combien de valeurs différentes peut-on coder avec un octet ?", 256, "2⁸ = 256 valeurs, de 0 à 255 : c'est le nombre de niveaux de chaque couleur d'un pixel."),
]),
notion('P-4', 1, D, 'pc-couleur-objets', [
  Q("Un objet qui paraît rouge en lumière blanche est éclairé en lumière verte. Il paraît…", ["rouge", "vert", "noir", "blanc"], "noir", "Il absorbe le vert et ne diffuse que le rouge, absent de l'éclairage."),
  Q("Un objet blanc éclairé en lumière bleue paraît…", ["blanc", "bleu", "noir", "jaune"], "bleu", "Un objet blanc diffuse toutes les couleurs qu'il reçoit."),
  Q("Pourquoi le ciel est-il bleu en journée ?", ["L'air est bleu", "L'atmosphère diffuse davantage la lumière bleue du Soleil", "Il reflète la couleur des océans", "Le Soleil est bleu"], "L'atmosphère diffuse davantage la lumière bleue du Soleil", "Les courtes longueurs d'onde (bleu) sont davantage diffusées par les molécules de l'air."),
  Q("Pourquoi le Soleil paraît-il rouge au coucher ?", ["Il change de température", "Sa lumière traverse plus d'atmosphère et perd une grande partie de son bleu par diffusion", "La Terre le colore", "C'est une illusion"], "Sa lumière traverse plus d'atmosphère et perd une grande partie de son bleu par diffusion", "Il reste surtout les couleurs orange et rouge."),
]),
]

from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('M1', 6, F, 'm-priorites', [
  N("Calculez : 3 + 4 × 5", 23, "La multiplication est prioritaire sur l'addition : 4 × 5 = 20, puis 3 + 20 = 23."),
  N("Calculez : 20 − 12 ÷ 4", 17, "La division passe avant la soustraction : 12 ÷ 4 = 3, puis 20 − 3 = 17."),
  N("Calculez : (6 + 4) × 3 − 2", 28, "On calcule d'abord la parenthèse (10), puis la multiplication (30), enfin la soustraction : 30 − 2 = 28."),
]),
notion('M1', 8, F, 'm-multiples-diviseurs', [
  Q("Lequel de ces nombres est un diviseur de 48 ?", ["5", "7", "9", "12"], "12", "48 = 12 × 4 : la division de 48 par 12 tombe juste. 5, 7 et 9 ne divisent pas 48."),
  Q("Lequel de ces nombres est un multiple de 7 ?", ["54", "63", "75", "86"], "63", "63 = 7 × 9. Les autres nombres ne sont pas dans la table de 7."),
  Q("Quelle affirmation est vraie ?", ["15 est un multiple de 45", "45 est un diviseur de 15", "45 est un multiple de 15", "15 et 45 n'ont aucun lien"], "45 est un multiple de 15", "45 = 15 × 3 : 45 est un multiple de 15, et 15 est un diviseur de 45."),
]),
notion('M1', 9, F, 'm-divisibilite-3-9', [
  Q("Lequel de ces nombres est divisible par 3 ?", ["124", "251", "372", "410"], "372", "Un nombre est divisible par 3 si la somme de ses chiffres l'est : 3 + 7 + 2 = 12, divisible par 3."),
  Q("Lequel de ces nombres est divisible par 9 ?", ["1 234", "2 017", "3 105", "4 114"], "3 105", "Un nombre est divisible par 9 si la somme de ses chiffres l'est : 3 + 1 + 0 + 5 = 9. Pour les autres, la somme vaut 10."),
  Q("La somme des chiffres d'un nombre est 21. Ce nombre est…", ["divisible par 3 et par 9", "divisible par 3 mais pas par 9", "divisible par 9 mais pas par 3", "divisible ni par 3 ni par 9"], "divisible par 3 mais pas par 9", "21 est divisible par 3 (21 = 3 × 7) mais pas par 9 : le nombre est donc divisible par 3, pas par 9."),
]),
notion('M1', 2, F, 'm-division-decimal', [
  N("Calculez : 12 ÷ 0,5", 24, "Diviser par 0,5 revient à multiplier par 2 : 12 ÷ 0,5 = 24."),
  N("Calculez : 3,6 ÷ 0,4", 9, "On multiplie les deux nombres par 10 pour diviser par un entier : 36 ÷ 4 = 9."),
  N("Calculez : 7 ÷ 0,1", 70, "Diviser par 0,1 revient à multiplier par 10 : 7 ÷ 0,1 = 70."),
]),
notion('M1', 5, F, 'm-vocabulaire-operations', [
  Q("Dans le calcul 5 × 8, comment appelle-t-on 5 et 8 ?", ["Des termes", "Des facteurs", "Des quotients", "Des différences"], "Des facteurs", "Les nombres que l'on multiplie sont des facteurs ; le résultat est le produit. Les termes sont les nombres d'une somme ou d'une différence."),
  Q("Le calcul 3 × (4 + 5) est…", ["une somme", "un produit", "une différence", "un quotient"], "un produit", "La dernière opération effectuée est la multiplication (la parenthèse est calculée avant) : c'est un produit."),
  Q("Comment appelle-t-on le résultat d'une division ?", ["Le produit", "La somme", "Le quotient", "La différence"], "Le quotient", "Le résultat d'une division est un quotient ; celui d'une multiplication est un produit."),
]),
notion('M2', 1, F, 'm-oppose-valeur-absolue', [
  Q("Quel est l'opposé de −7 ?", ["−7", "7", "1/7", "−1/7"], "7", "Deux nombres opposés ont une somme nulle : −7 + 7 = 0. Ne pas confondre avec l'inverse (1/7)."),
  Q("Quelle est la distance à zéro du nombre −4,5 ?", ["−4,5", "4,5", "0", "9"], "4,5", "La distance à zéro (valeur absolue) est toujours positive : celle de −4,5 est 4,5."),
  N("Calculez la somme d'un nombre et de son opposé, par exemple 12,3 + (−12,3).", 0, "La somme de deux nombres opposés est toujours égale à 0."),
]),
notion('M2', 5, F, 'm-comparer-relatifs', [
  Q("Quel est le plus petit de ces nombres ?", ["−2", "−5", "0", "1"], "−5", "Entre deux nombres négatifs, le plus petit est celui qui a la plus grande distance à zéro : −5 < −2."),
  Q("Quelle comparaison est vraie ?", ["−3 > −1", "−3 < −1", "−3 = −1", "−3 > 0"], "−3 < −1", "Sur une droite graduée, −3 est à gauche de −1 : −3 est plus petit."),
  Q("Comment ranger −1,5 ; −2 ; 0,5 dans l'ordre croissant ?", ["−1,5 < −2 < 0,5", "−2 < −1,5 < 0,5", "0,5 < −1,5 < −2", "−2 < 0,5 < −1,5"], "−2 < −1,5 < 0,5", "L'ordre croissant va du plus petit au plus grand : −2 est le plus éloigné de zéro du côté négatif."),
]),
notion('M2', 6, F, 'm-addition-relatifs', [
  N("Calculez : (−8) + 5", -3, "Signes différents : on soustrait les distances à zéro (8 − 5 = 3) et on garde le signe de celui qui a la plus grande distance : −3."),
  N("Calculez : (−4) + (−7)", -11, "Même signe : on additionne les distances à zéro (4 + 7 = 11) et on garde le signe commun : −11."),
  N("Calculez : 6,5 + (−9)", -2.5, "9 − 6,5 = 2,5, et −9 a la plus grande distance à zéro : le résultat est −2,5."),
]),
notion('M2', 8, F, 'm-soustraction-relatifs', [
  N("Calculez : 3 − (−5)", 8, "Soustraire un nombre revient à ajouter son opposé : 3 − (−5) = 3 + 5 = 8."),
  N("Calculez : (−2) − 6", -8, "(−2) − 6 = (−2) + (−6) = −8."),
  N("Calculez : (−10) − (−4)", -6, "(−10) − (−4) = (−10) + 4 = −6."),
]),
notion('M2', 3, F, 'm-relatifs-grandeurs', [
  N("Le matin, il fait −3 °C. L'après-midi, la température a augmenté de 8 °C. Quelle est la température l'après-midi (en °C) ?", 5, "−3 + 8 = 5 : il fait 5 °C."),
  N("Un plongeur est à −12 m. Il remonte de 5 m. À quelle altitude se trouve-t-il (en m) ?", -7, "−12 + 5 = −7 : il est à 7 m sous la surface."),
  N("À Moscou il fait −15 °C et à Paris 4 °C. Quel est l'écart de température entre les deux villes (en °C) ?", 19, "Écart = 4 − (−15) = 4 + 15 = 19 °C."),
]),
notion('M3', 0, F, 'm-comparer-fractions', [
  Q("Quelle fraction est la plus grande ?", ["3/7", "5/7", "2/7", "4/7"], "5/7", "Fractions de même dénominateur : la plus grande est celle qui a le plus grand numérateur."),
  Q("Quelle comparaison est vraie ?", ["3/4 < 2/3", "3/4 > 2/3", "3/4 = 2/3", "On ne peut pas comparer"], "3/4 > 2/3", "On met au même dénominateur : 3/4 = 9/12 et 2/3 = 8/12, donc 3/4 > 2/3."),
  Q("Quelle fraction est égale à 1/2 ?", ["2/3", "4/8", "3/5", "5/12"], "4/8", "4/8 se simplifie par 4 : 4/8 = 1/2."),
]),
notion('M3', 1, F, 'm-addition-fractions', [
  Q("Calculez : 2/9 + 5/9", ["7/18", "7/9", "10/9", "7/81"], "7/9", "Même dénominateur : on additionne les numérateurs et on garde le dénominateur : 7/9."),
  Q("Calculez : 1/2 + 1/4", ["2/6", "1/6", "3/4", "2/4"], "3/4", "1/2 = 2/4, donc 2/4 + 1/4 = 3/4. On n'additionne jamais les dénominateurs."),
  Q("Calculez : 1 − 3/8", ["5/8", "2/8", "3/8", "−2/8"], "5/8", "1 = 8/8, donc 8/8 − 3/8 = 5/8."),
]),
notion('M4', 1, F, 'm-carres', [
  N("Combien vaut 7² ?", 49, "7² = 7 × 7 = 49. Ne pas confondre avec 7 × 2 = 14."),
  N("Combien vaut 12² ?", 144, "12² = 12 × 12 = 144."),
  N("Quel nombre entier positif a pour carré 81 ?", 9, "9 × 9 = 81."),
]),
notion('M4', 2, F, 'm-puissances-notation', [
  N("Combien vaut 10³ ?", 1000, "10³ = 10 × 10 × 10 = 1 000 : il y a 3 zéros."),
  N("Combien vaut 2³ ?", 8, "2³ = 2 × 2 × 2 = 8. Ne pas confondre avec 2 × 3 = 6."),
  N("Combien vaut 5² + 2³ ?", 33, "5² = 25 et 2³ = 8, donc 25 + 8 = 33."),
]),
notion('M5', 1, F, 'm-substitution', [
  N("Calculez 3x + 2 pour x = 4.", 14, "On remplace x par 4 : 3 × 4 + 2 = 12 + 2 = 14."),
  N("Calculez 5 − 2a pour a = 3.", -1, "5 − 2 × 3 = 5 − 6 = −1."),
  N("Calculez x² + 1 pour x = 6.", 37, "6² + 1 = 36 + 1 = 37."),
]),
notion('M5', 3, F, 'm-somme-ou-produit', [
  Q("L'expression 4(x + 1) est…", ["une somme", "un produit", "une différence", "un quotient"], "un produit", "C'est 4 multiplié par (x + 1) : la dernière opération est une multiplication, c'est un produit."),
  Q("L'expression 3x + 7 est…", ["une somme", "un produit", "un quotient", "une puissance"], "une somme", "On calcule 3x puis on ajoute 7 : la dernière opération est une addition, c'est une somme."),
  Q("L'expression (a + 2)(a − 3) est…", ["une somme", "une différence", "un produit", "un quotient"], "un produit", "C'est le produit de deux facteurs, (a + 2) et (a − 3)."),
]),
notion('M5', 11, F, 'm-equation-simple', [
  N("Résolvez : x + 7 = 15", 8, "On soustrait 7 aux deux membres : x = 15 − 7 = 8."),
  N("Résolvez : 4x = 28", 7, "On divise les deux membres par 4 : x = 28 ÷ 4 = 7."),
  N("Résolvez : x − 3,5 = 6", 9.5, "On ajoute 3,5 aux deux membres : x = 6 + 3,5 = 9,5."),
]),
notion('M5', 0, F, 'm-produire-formule', [
  Q("Quelle formule donne le périmètre P d'un carré de côté c ?", ["P = c²", "P = 4c", "P = 2c", "P = c + 4"], "P = 4c", "Un carré a 4 côtés de même longueur : P = c + c + c + c = 4c."),
  Q("Quelle expression représente le double d'un nombre n augmenté de 3 ?", ["2n + 3", "2(n + 3)", "n² + 3", "2 + 3n"], "2n + 3", "Le double de n est 2n, auquel on ajoute 3 : 2n + 3. 2(n + 3) serait le double de (n + 3)."),
  Q("Quelle formule donne l'aire A d'un rectangle de longueur L et de largeur l ?", ["A = 2L + 2l", "A = L + l", "A = L × l", "A = L²"], "A = L × l", "L'aire d'un rectangle est le produit de sa longueur par sa largeur. 2L + 2l est son périmètre."),
]),
notion('M7', 0, F, 'm-simplifier-fraction', [
  Q("Simplifiez 12/18.", ["6/9", "2/3", "4/6", "3/2"], "2/3", "On divise numérateur et dénominateur par leur plus grand diviseur commun, 6 : 12/18 = 2/3."),
  Q("Quelle fraction est égale à 15/25 ?", ["3/5", "5/3", "1/5", "3/4"], "3/5", "On divise par 5 : 15/25 = 3/5."),
  Q("Simplifiez 28/35.", ["7/5", "4/5", "14/15", "4/7"], "4/5", "On divise par 7 : 28/35 = 4/5."),
]),
notion('M7', 5, F, 'm-inverse', [
  Q("Quel est l'inverse de 4 ?", ["−4", "1/4", "4/1", "0,4"], "1/4", "Deux nombres sont inverses si leur produit vaut 1 : 4 × 1/4 = 1. −4 est l'opposé de 4."),
  Q("Quel est l'inverse de 2/5 ?", ["−2/5", "5/2", "2/5", "1/5"], "5/2", "On échange numérateur et dénominateur : 2/5 × 5/2 = 1."),
  Q("Quel est l'inverse de 0,5 ?", ["2", "−0,5", "5", "0,2"], "2", "0,5 × 2 = 1, donc l'inverse de 0,5 est 2."),
]),
notion('M9', 0, F, 'm-racine-carree', [
  N("Combien vaut √64 ?", 8, "√64 est le nombre positif dont le carré vaut 64 : 8 × 8 = 64."),
  N("Combien vaut √121 ?", 11, "11 × 11 = 121, donc √121 = 11."),
  N("Combien vaut √(9 × 16) ?", 12, "9 × 16 = 144 et √144 = 12 (on peut aussi écrire √9 × √16 = 3 × 4)."),
]),
notion('M16', 1, F, 'm-coordonnees', [
  Q("Dans un repère, le point A a pour coordonnées (3 ; −2). Que vaut son abscisse ?", ["−2", "3", "1", "5"], "3", "Dans (x ; y), le premier nombre est l'abscisse, le second l'ordonnée : l'abscisse de A est 3."),
  Q("Un point a une abscisse nulle. Où se trouve-t-il ?", ["Sur l'axe des abscisses", "Sur l'axe des ordonnées", "À l'origine forcément", "Hors du repère"], "Sur l'axe des ordonnées", "Une abscisse nulle signifie x = 0 : le point est sur l'axe vertical, l'axe des ordonnées."),
  Q("Le point B est 4 unités à gauche de l'origine et 1 unité au-dessus. Quelles sont ses coordonnées ?", ["(4 ; 1)", "(−4 ; 1)", "(1 ; −4)", "(−1 ; 4)"], "(−4 ; 1)", "À gauche de l'origine, l'abscisse est négative (−4) ; au-dessus, l'ordonnée est positive (1)."),
]),
notion('M17', 2, F, 'm-volume-pave', [
  N("Quel est le volume (en cm³) d'un pavé droit de 5 cm × 3 cm × 2 cm ?", 30, "Volume = longueur × largeur × hauteur = 5 × 3 × 2 = 30 cm³."),
  N("Quel est le volume (en cm³) d'un cube de 4 cm d'arête ?", 64, "Volume d'un cube = arête³ = 4 × 4 × 4 = 64 cm³."),
  N("Un aquarium mesure 50 cm × 20 cm × 30 cm. Quel est son volume en dm³ ?", 30, "En dm : 5 × 2 × 3 = 30 dm³ (soit 30 litres)."),
]),
notion('M17', 3, F, 'm-conversions-volumes', [
  N("Combien de litres y a-t-il dans 1 m³ ?", 1000, "1 m³ = 1 000 dm³ et 1 dm³ = 1 L, donc 1 m³ = 1 000 L."),
  N("Convertissez 2,5 L en cL.", 250, "1 L = 100 cL, donc 2,5 L = 250 cL."),
  N("Convertissez 750 cm³ en litres.", 0.75, "1 L = 1 000 cm³, donc 750 cm³ = 0,75 L."),
]),
notion('M18', 1, F, 'm-symetrie-centrale', [
  Q("Que conserve une symétrie centrale ?", ["Les longueurs, les angles et les aires", "Seulement les longueurs", "Seulement l'orientation", "Rien du tout"], "Les longueurs, les angles et les aires", "Une symétrie centrale est un demi-tour : la figure obtenue est superposable à la figure de départ."),
  Q("Le symétrique d'une droite par une symétrie centrale est…", ["une droite perpendiculaire", "une droite parallèle", "un cercle", "un point"], "une droite parallèle", "Par symétrie centrale, une droite a pour image une droite qui lui est parallèle."),
  Q("A' est le symétrique de A par rapport au point O. Que représente O pour le segment [AA'] ?", ["Une extrémité", "Son milieu", "Un point quelconque", "Le centre d'un cercle passant par A seulement"], "Son milieu", "Dans la symétrie de centre O, O est le milieu de chaque segment qui relie un point à son image."),
]),
notion('M20', 0, F, 'm-somme-angles-triangle', [
  N("Un triangle a deux angles de 50° et 70°. Combien mesure le troisième angle (en degrés) ?", 60, "La somme des angles d'un triangle vaut 180° : 180 − 50 − 70 = 60°."),
  N("Un triangle rectangle a un angle de 35°. Combien mesure son troisième angle (en degrés) ?", 55, "180 − 90 − 35 = 55°."),
  N("Combien mesure chaque angle d'un triangle équilatéral (en degrés) ?", 60, "Ses trois angles sont égaux : 180 ÷ 3 = 60°."),
]),
notion('M20', 3, F, 'm-aire-triangle', [
  N("Quelle est l'aire (en cm²) d'un triangle de base 8 cm et de hauteur 5 cm ?", 20, "Aire = base × hauteur ÷ 2 = 8 × 5 ÷ 2 = 20 cm²."),
  N("Quelle est l'aire (en cm²) d'un triangle rectangle dont les côtés de l'angle droit mesurent 6 cm et 4 cm ?", 12, "Les côtés de l'angle droit sont une base et sa hauteur : 6 × 4 ÷ 2 = 12 cm²."),
  N("Un triangle a une aire de 30 cm² et une base de 12 cm. Quelle est sa hauteur (en cm) ?", 5, "30 = 12 × h ÷ 2, donc 12 × h = 60 et h = 5 cm."),
]),
notion('M21', 4, F, 'm-parallelogrammes-particuliers', [
  Q("Un parallélogramme qui a un angle droit est…", ["un losange", "un rectangle", "un trapèze", "un cerf-volant"], "un rectangle", "Un parallélogramme avec un angle droit a en fait quatre angles droits : c'est un rectangle."),
  Q("Un parallélogramme qui a deux côtés consécutifs de même longueur est…", ["un rectangle", "un losange", "un trapèze", "un triangle"], "un losange", "Si deux côtés consécutifs sont égaux, les quatre côtés le sont : c'est un losange."),
  Q("Un quadrilatère qui est à la fois un rectangle et un losange est…", ["un trapèze", "un carré", "un parallélogramme quelconque", "impossible"], "un carré", "Le carré a les propriétés du rectangle (angles droits) et du losange (côtés égaux)."),
]),
notion('M21', 6, F, 'm-aire-parallelogramme', [
  N("Quelle est l'aire (en cm²) d'un parallélogramme de base 7 cm et de hauteur 4 cm ?", 28, "Aire d'un parallélogramme = base × hauteur = 7 × 4 = 28 cm²."),
  N("Quelle est l'aire (en m²) d'un rectangle de 12 m sur 3,5 m ?", 42, "12 × 3,5 = 42 m²."),
  N("Quelle est l'aire (en cm²) d'un carré de 9 cm de côté ?", 81, "9 × 9 = 81 cm²."),
]),
notion('M21', 7, F, 'm-conversions-aires', [
  N("Combien de cm² y a-t-il dans 1 m² ?", 10000, "1 m = 100 cm, donc 1 m² = 100 × 100 = 10 000 cm²."),
  N("Convertissez 3,2 m² en dm².", 320, "1 m² = 100 dm², donc 3,2 m² = 320 dm²."),
  N("Convertissez 1 hectare en m².", 10000, "1 ha = 1 hm² = 100 m × 100 m = 10 000 m²."),
]),
notion('M26', 1, F, 'm-pythagore-calcul', [
  N("Un triangle ABC est rectangle en A, avec AB = 3 cm et AC = 4 cm. Combien mesure BC (en cm) ?", 5, "D'après le théorème de Pythagore : BC² = 3² + 4² = 9 + 16 = 25, donc BC = 5 cm."),
  N("Un triangle est rectangle ; ses côtés de l'angle droit mesurent 6 cm et 8 cm. Combien mesure l'hypoténuse (en cm) ?", 10, "Hypoténuse² = 36 + 64 = 100, donc hypoténuse = 10 cm."),
  N("Dans un triangle rectangle, l'hypoténuse mesure 13 cm et un côté 5 cm. Combien mesure le troisième côté (en cm) ?", 12, "13² = 5² + x², donc x² = 169 − 25 = 144 et x = 12 cm."),
]),
notion('M31', 1, F, 'm-frequence', [
  N("Dans une classe de 25 élèves, 10 ont un chien. Quelle est la fréquence des élèves ayant un chien, en pourcentage ?", 40, "Fréquence = 10 ÷ 25 = 0,4, soit 40 %."),
  N("Sur 50 lancers, une pièce est tombée 22 fois sur pile. Quelle est la fréquence de pile, en pourcentage ?", 44, "22 ÷ 50 = 0,44, soit 44 %."),
  N("Dans un sondage, 3 personnes sur 4 sont satisfaites. Quel pourcentage cela représente-t-il ?", 75, "3/4 = 0,75, soit 75 %."),
]),
notion('M31', 5, F, 'm-moyenne', [
  N("Quelle est la moyenne de 12, 15 et 18 ?", 15, "(12 + 15 + 18) ÷ 3 = 45 ÷ 3 = 15."),
  N("Un élève a eu 8, 14, 11 et 15. Quelle est sa moyenne ?", 12, "(8 + 14 + 11 + 15) ÷ 4 = 48 ÷ 4 = 12."),
  N("Quelle est la moyenne de 2,5 ; 3,5 et 6 ?", 4, "(2,5 + 3,5 + 6) ÷ 3 = 12 ÷ 3 = 4."),
]),
notion('M32', 2, F, 'm-probabilite-simple', [
  Q("On tire une carte au hasard dans un jeu de 32 cartes. Quelle est la probabilité de tirer un as ?", ["1/32", "4/32 = 1/8", "1/4", "1/13"], "4/32 = 1/8", "Il y a 4 as sur 32 cartes, tirage équiprobable : 4/32 = 1/8."),
  Q("Une urne contient 3 boules rouges et 7 boules bleues. On en tire une au hasard. Quelle est la probabilité qu'elle soit rouge ?", ["3/7", "3/10", "7/10", "1/3"], "3/10", "3 issues favorables sur 10 boules au total : 3/10."),
  Q("On lance un dé équilibré à 6 faces. Quelle est la probabilité d'obtenir 5 ?", ["1/5", "5/6", "1/6", "1/2"], "1/6", "Une issue favorable sur 6 issues équiprobables : 1/6."),
]),
notion('M32', 1, F, 'm-vocabulaire-probabilites', [
  Q("On lance un dé. « Obtenir 7 » est un événement…", ["certain", "impossible", "probable", "équiprobable"], "impossible", "Aucune face ne porte 7 : l'événement ne peut pas se réaliser, sa probabilité est 0."),
  Q("On lance un dé. « Obtenir un nombre inférieur à 10 » est un événement…", ["impossible", "certain", "contraire", "élémentaire"], "certain", "Toutes les issues (1 à 6) sont inférieures à 10 : l'événement est certain, sa probabilité est 1."),
  Q("Dans une expérience aléatoire, comment appelle-t-on chacun des résultats possibles ?", ["Une issue", "Une fréquence", "Un effectif", "Une moyenne"], "Une issue", "Les résultats possibles d'une expérience aléatoire sont ses issues ; un événement est un ensemble d'issues."),
]),
notion('M33', 2, F, 'm-etendue', [
  N("Quelle est l'étendue de la série 4 ; 9 ; 2 ; 15 ; 7 ?", 13, "Étendue = plus grande valeur − plus petite valeur = 15 − 2 = 13."),
  N("Les températures d'une semaine vont de −2 °C à 11 °C. Quelle est l'étendue (en °C) ?", 13, "11 − (−2) = 13 °C."),
  N("Quelle est l'étendue de la série 12 ; 12 ; 18 ; 20 ; 14 ?", 8, "20 − 12 = 8."),
]),
notion('M37', 1, F, 'm-pourcentage-nombre', [
  N("Combien font 20 % de 150 ?", 30, "20 % de 150 = 150 × 20/100 = 30."),
  N("Combien font 15 % de 80 ?", 12, "80 × 0,15 = 12."),
  N("Un article à 60 € est soldé à −25 %. Quel est le montant de la remise (en €) ?", 15, "25 % de 60 = 60 × 0,25 = 15 €."),
]),
notion('M37', 3, F, 'm-prix-unitaire', [
  N("3 kg de pommes coûtent 7,50 €. Combien coûte 1 kg (en €) ?", 2.5, "Prix unitaire = 7,50 ÷ 3 = 2,50 €."),
  N("5 cahiers coûtent 12 €. Combien coûtent 8 cahiers (en €) ?", 19.2, "Un cahier coûte 12 ÷ 5 = 2,40 €, donc 8 cahiers coûtent 8 × 2,40 = 19,20 €."),
  N("Une voiture roule à 90 km/h. Quelle distance (en km) parcourt-elle en 2 h ?", 180, "Distance = vitesse × durée = 90 × 2 = 180 km."),
]),
notion('M37', 2, F, 'm-reconnaitre-proportionnalite', [
  Q("Laquelle de ces situations est une situation de proportionnalité ?", ["L'âge et la taille d'un enfant", "Le prix payé et la quantité d'essence achetée", "La température et l'heure de la journée", "Le poids et l'âge d'une personne"], "Le prix payé et la quantité d'essence achetée", "Le prix payé est égal au prix du litre multiplié par le nombre de litres : c'est proportionnel."),
  Q("Le tableau « 2 → 6 ; 5 → 15 ; 7 → 21 » est-il un tableau de proportionnalité ?", ["Oui, le coefficient est 3", "Non", "Oui, le coefficient est 4", "On ne peut pas savoir"], "Oui, le coefficient est 3", "Chaque nombre de la deuxième ligne est obtenu en multipliant par 3 : 2 × 3 = 6, 5 × 3 = 15, 7 × 3 = 21."),
  Q("Le tableau « 1 → 4 ; 2 → 7 ; 3 → 10 » est-il un tableau de proportionnalité ?", ["Oui, coefficient 4", "Non", "Oui, coefficient 3", "Oui, coefficient 7"], "Non", "4/1 = 4 mais 7/2 = 3,5 : les quotients ne sont pas égaux, ce n'est pas proportionnel."),
]),
notion('M38', 1, F, 'm-tableau-valeurs', [
  N("On considère la formule y = 2x + 1. Quelle valeur de y correspond à x = 5 ?", 11, "y = 2 × 5 + 1 = 11."),
  N("Avec la formule P = 4c, quel est P lorsque c = 2,5 ?", 10, "P = 4 × 2,5 = 10."),
  N("Avec la formule y = x² − 3, quelle valeur de y correspond à x = −2 ?", 1, "(−2)² − 3 = 4 − 3 = 1."),
]),
notion('M39', 3, F, 'm-quatrieme-proportionnelle', [
  N("Pour 4 personnes, il faut 200 g de farine. Combien en faut-il (en g) pour 6 personnes ?", 300, "Pour 1 personne : 200 ÷ 4 = 50 g, donc pour 6 personnes : 6 × 50 = 300 g."),
  N("Sur une carte à l'échelle 1/100 000, 3 cm représentent combien de km ?", 3, "1 cm représente 100 000 cm = 1 km, donc 3 cm représentent 3 km."),
  N("6 stylos coûtent 9 €. Combien coûtent 10 stylos (en €) ?", 15, "Un stylo coûte 9 ÷ 6 = 1,50 €, donc 10 stylos coûtent 15 €."),
]),
notion('M43', 4, F, 'm-programme-calcul', [
  N("Programme : choisir un nombre, le multiplier par 3, puis ajouter 4. Quel est le résultat avec 5 ?", 19, "5 × 3 = 15, puis 15 + 4 = 19."),
  N("Programme : choisir un nombre, lui ajouter 2, puis multiplier le résultat par 5. Quel est le résultat avec 4 ?", 30, "4 + 2 = 6, puis 6 × 5 = 30."),
  N("Programme : choisir un nombre, le mettre au carré, puis soustraire 10. Quel est le résultat avec −3 ?", -1, "(−3)² = 9, puis 9 − 10 = −1."),
]),
notion('M43', 6, F, 'm-boucle-repeter', [
  Q("Dans Scratch, quelle figure trace le script « répéter 4 fois : avancer de 50, tourner de 90° » ?", ["Un triangle", "Un carré", "Un hexagone", "Un cercle"], "Un carré", "4 côtés de même longueur et 4 angles droits : c'est un carré."),
  Q("Pour tracer un triangle équilatéral avec une boucle « répéter 3 fois : avancer, tourner », de quel angle faut-il tourner ?", ["60°", "90°", "120°", "180°"], "120°", "Le lutin tourne de l'angle extérieur : 360° ÷ 3 = 120°, et non de l'angle intérieur (60°)."),
  Q("Combien de fois le lutin dit-il « Bonjour » avec « répéter 5 fois : dire Bonjour » ?", ["1 fois", "4 fois", "5 fois", "6 fois"], "5 fois", "La boucle exécute son contenu exactement le nombre de fois indiqué : 5 fois."),
]),
notion('M17', 4, F, 'm-aire-disque', [
  Q("Quelle formule donne l'aire d'un disque de rayon r ?", ["2πr", "πr²", "πd", "2r²"], "πr²", "Aire du disque = π × r². 2πr est le périmètre du cercle."),
  Q("Quelle formule donne le périmètre d'un cercle de rayon r ?", ["πr²", "2πr", "πr", "4r"], "2πr", "Périmètre = 2 × π × r, soit π × diamètre."),
  N("Quelle est l'aire d'un disque de rayon 10 cm, en prenant π ≈ 3,14 (en cm²) ?", 314, "A = 3,14 × 10² = 3,14 × 100 = 314 cm²."),
]),
notion('M24', 0, F, 'm-reconnaitre-solides', [
  Q("Quel solide a une base polygonale et des faces latérales triangulaires qui se rejoignent en un sommet ?", ["Un prisme", "Une pyramide", "Un cylindre", "Un pavé"], "Une pyramide", "Les faces latérales d'une pyramide sont des triangles qui se rejoignent au sommet."),
  Q("Combien de faces a un cube ?", ["4", "6", "8", "12"], "6", "Un cube a 6 faces carrées, 12 arêtes et 8 sommets."),
  Q("Quel solide a deux bases en forme de disque ?", ["Un cône", "Une sphère", "Un cylindre", "Une pyramide"], "Un cylindre", "Le cylindre de révolution a deux bases circulaires ; le cône n'en a qu'une."),
]),
notion('M28', 0, F, 'm-boule-sphere', [
  Q("Quelle est la différence entre une sphère et une boule ?", ["Aucune", "La sphère est la surface, la boule est le solide plein", "La boule est la surface, la sphère est pleine", "La sphère est plate"], "La sphère est la surface, la boule est le solide plein", "La sphère est l'ensemble des points à la distance r du centre ; la boule comprend aussi l'intérieur."),
  Q("Un ballon de football gonflé ressemble plutôt à…", ["une boule", "une sphère", "un cylindre", "un cône"], "une sphère", "On s'intéresse à son enveloppe, la surface : c'est une sphère (une bille pleine serait une boule)."),
  Q("Comment appelle-t-on un segment qui relie deux points d'une sphère en passant par son centre ?", ["Un rayon", "Un diamètre", "Une corde quelconque", "Une génératrice"], "Un diamètre", "Un diamètre passe par le centre ; sa longueur vaut deux fois le rayon."),
]),
notion('M12', 2, F, 'm-notation-scientifique', [
  Q("Quelle est la notation scientifique de 45 000 ?", ["45 × 10³", "4,5 × 10⁴", "0,45 × 10⁵", "4,5 × 10³"], "4,5 × 10⁴", "En notation scientifique, le premier nombre est compris entre 1 et 10 (exclu) : 45 000 = 4,5 × 10⁴."),
  Q("Quelle est la notation scientifique de 0,003 ?", ["3 × 10⁻³", "3 × 10³", "0,3 × 10⁻²", "30 × 10⁻⁴"], "3 × 10⁻³", "0,003 = 3 ÷ 1 000 = 3 × 10⁻³."),
  Q("Quel nombre s'écrit 2,1 × 10⁵ ?", ["2 100", "21 000", "210 000", "2 100 000"], "210 000", "Multiplier par 10⁵ décale la virgule de 5 rangs vers la droite : 210 000."),
]),
notion('M6', 0, F, 'm-multiplication-relatifs', [
  N("Calculez : (−4) × 6", -24, "Signes différents : le produit est négatif. 4 × 6 = 24, donc −24."),
  N("Calculez : (−5) × (−3)", 15, "Deux facteurs négatifs : le produit est positif, 15."),
  N("Calculez : (−2) × (−2) × (−2)", -8, "Trois facteurs négatifs (nombre impair) : le produit est négatif, −8."),
]),
notion('M10', 3, F, 'm-equation-ax-b', [
  N("Résolvez : 2x + 3 = 11", 4, "2x = 11 − 3 = 8, donc x = 8 ÷ 2 = 4."),
  N("Résolvez : 5x − 4 = 21", 5, "5x = 21 + 4 = 25, donc x = 5."),
  N("Résolvez : 3x + 7 = 1", -2, "3x = 1 − 7 = −6, donc x = −2."),
]),
notion('M33', 1, F, 'm-mediane-simple', [
  N("Quelle est la médiane de la série 3 ; 8 ; 5 ; 12 ; 6 ?", 6, "On range : 3 ; 5 ; 6 ; 8 ; 12. Il y a 5 valeurs, la médiane est la 3e : 6."),
  N("Quelle est la médiane de la série 10 ; 14 ; 11 ; 17 ; 13 ; 20 ; 15 ?", 14, "Rangée : 10 ; 11 ; 13 ; 14 ; 15 ; 17 ; 20. 7 valeurs : la médiane est la 4e, 14."),
  N("Quelle est la médiane de la série 2 ; 4 ; 6 ; 8 ?", 5, "4 valeurs rangées : la médiane est la moyenne des deux valeurs centrales, (4 + 6) ÷ 2 = 5."),
]),
]

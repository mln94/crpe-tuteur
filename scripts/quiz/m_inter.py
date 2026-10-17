from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('M1', 7, I, 'm-distributivite-numerique', [
  N("Calculez astucieusement : 7 × 102", 714, "7 × 102 = 7 × (100 + 2) = 700 + 14 = 714 (distributivité)."),
  N("Calculez astucieusement : 25 × 99", 2475, "25 × 99 = 25 × (100 − 1) = 2 500 − 25 = 2 475."),
  N("Calculez astucieusement : 13 × 7 + 13 × 3", 130, "On factorise par 13 : 13 × (7 + 3) = 13 × 10 = 130."),
]),
notion('M2', 11, I, 'm-enchainer-relatifs', [
  N("Calculez : −5 + 8 − 12 + 3", -6, "On regroupe : (8 + 3) − (5 + 12) = 11 − 17 = −6."),
  N("Calculez : 4 − (−6) + (−9)", 1, "4 + 6 − 9 = 1."),
  N("Calculez : −2,5 − 1,5 + 7", 3, "−2,5 − 1,5 = −4, puis −4 + 7 = 3."),
]),
notion('M3', 2, I, 'm-probleme-fractions', [
  N("Un élève a lu 1/3 d'un livre lundi et 1/4 mardi. Quelle fraction du livre lui reste-t-il ? Donnez la réponse sous forme décimale arrondie au centième.", 0.42, "1/3 + 1/4 = 4/12 + 3/12 = 7/12 lus, il reste 5/12 ≈ 0,42.", 0.005),
  Q("Dans une classe, 2/5 des élèves sont externes et 1/3 sont demi-pensionnaires ; les autres sont internes. Quelle fraction est interne ?", ["4/15", "3/8", "11/15", "1/5"], "4/15", "2/5 + 1/3 = 6/15 + 5/15 = 11/15, donc 1 − 11/15 = 4/15."),
  Q("On verse 3/4 L puis 5/8 L d'eau dans une bouteille vide. Combien de litres contient-elle ?", ["8/12 L", "11/8 L", "15/32 L", "1 L"], "11/8 L", "3/4 = 6/8, donc 6/8 + 5/8 = 11/8 L, soit 1,375 L."),
]),
notion('M4', 4, I, 'm-expressions-puissances', [
  N("Calculez : 2 × 3² − 4", 14, "La puissance est prioritaire : 3² = 9, puis 2 × 9 = 18 et 18 − 4 = 14."),
  N("Calculez : (2 × 3)² − 4", 32, "La parenthèse d'abord : 6² = 36, puis 36 − 4 = 32."),
  N("Calculez : −3² + 10", 1, "Attention : −3² = −(3²) = −9 (le carré ne porte que sur 3). Donc −9 + 10 = 1."),
]),
notion('M5', 4, I, 'm-developper-simple', [
  Q("Développez 3(x + 5).", ["3x + 5", "3x + 15", "x + 15", "3x + 8"], "3x + 15", "On multiplie 3 par chaque terme : 3 × x + 3 × 5 = 3x + 15."),
  Q("Développez −2(a − 4).", ["−2a − 8", "−2a + 8", "2a − 8", "−2a − 4"], "−2a + 8", "−2 × a = −2a et −2 × (−4) = +8."),
  Q("Développez 5(2x − 1).", ["10x − 1", "10x − 5", "7x − 5", "10x + 5"], "10x − 5", "5 × 2x = 10x et 5 × (−1) = −5."),
]),
notion('M5', 5, I, 'm-reduire', [
  Q("Réduisez 4x + 3 + 2x − 7.", ["6x − 4", "6x + 10", "2x − 4", "9x − 4x"], "6x − 4", "On regroupe les x (4x + 2x = 6x) et les nombres (3 − 7 = −4)."),
  Q("Réduisez 5a − 2a + a.", ["2a", "3a", "4a", "8a"], "4a", "5a − 2a + a = (5 − 2 + 1)a = 4a."),
  Q("Réduisez 3x × 4x.", ["7x", "12x", "12x²", "7x²"], "12x²", "3 × 4 = 12 et x × x = x², donc 12x². Ne pas confondre avec 3x + 4x = 7x."),
]),
notion('M5', 7, I, 'm-contre-exemple', [
  Q("« Le carré d'un nombre est toujours plus grand que ce nombre. » Quel nombre est un contre-exemple ?", ["3", "10", "0,5", "−2"], "0,5", "0,5² = 0,25, qui est plus petit que 0,5 : l'affirmation est fausse. Pour −2, (−2)² = 4 > −2."),
  Q("« La somme de deux nombres premiers est toujours paire. » Quel exemple la contredit ?", ["3 + 5", "5 + 7", "2 + 3", "11 + 13"], "2 + 3", "2 + 3 = 5, qui est impair. 2 est le seul nombre premier pair."),
  Q("Combien de contre-exemples faut-il pour prouver qu'une affirmation générale est fausse ?", ["Un seul suffit", "Au moins deux", "Au moins dix", "Il faut une démonstration générale"], "Un seul suffit", "Un seul cas où l'affirmation est fausse suffit à la réfuter ; en revanche, des exemples ne prouvent pas qu'elle est vraie."),
]),
notion('M6', 1, I, 'm-division-relatifs', [
  N("Calculez : (−36) ÷ 4", -9, "Signes différents : le quotient est négatif. 36 ÷ 4 = 9, donc −9."),
  N("Calculez : (−45) ÷ (−9)", 5, "Même signe : le quotient est positif, 5."),
  N("Calculez : 7,2 ÷ (−0,8)", -9, "72 ÷ 8 = 9 et les signes sont différents : −9."),
]),
notion('M7', 3, I, 'm-produit-fractions', [
  Q("Calculez : 2/3 × 9/4", ["18/7", "3/2", "11/7", "6/12"], "3/2", "2/3 × 9/4 = 18/12 = 3/2 (on multiplie numérateurs et dénominateurs, puis on simplifie)."),
  Q("Calculez : 5/6 × 3/10", ["8/16", "1/4", "15/16", "1/2"], "1/4", "5 × 3 = 15 et 6 × 10 = 60, donc 15/60 = 1/4."),
  Q("Calculez : 4 × 3/8", ["12/32", "3/2", "7/8", "7/32"], "3/2", "4 × 3/8 = 12/8 = 3/2. On ne multiplie que le numérateur par 4."),
]),
notion('M7', 4, I, 'm-fraction-quantite', [
  N("Combien font les 3/4 de 60 ?", 45, "60 ÷ 4 = 15, puis 15 × 3 = 45."),
  N("Un réservoir de 50 L est rempli aux 2/5. Combien de litres contient-il ?", 20, "50 ÷ 5 × 2 = 20 L."),
  N("Combien font les 2/3 des 3/4 de 120 ?", 60, "3/4 de 120 = 90, puis 2/3 de 90 = 60 (ou 2/3 × 3/4 = 1/2 de 120)."),
]),
notion('M7', 7, I, 'm-diviser-fractions', [
  Q("Calculez : 3/4 ÷ 1/2", ["3/8", "3/2", "4/6", "1/4"], "3/2", "Diviser par 1/2 revient à multiplier par son inverse, 2 : 3/4 × 2 = 6/4 = 3/2."),
  Q("Calculez : 2/5 ÷ 4", ["8/5", "1/10", "1/20", "4/5"], "1/10", "Diviser par 4 revient à multiplier par 1/4 : 2/5 × 1/4 = 2/20 = 1/10."),
  Q("Calculez : 6 ÷ 3/5", ["18/5", "10", "2/5", "3/10"], "10", "6 × 5/3 = 30/3 = 10."),
]),
notion('M8', 1, I, 'm-produit-puissances', [
  Q("Écrivez sous la forme d'une seule puissance : 2³ × 2⁴", ["2⁷", "2¹²", "4⁷", "2¹"], "2⁷", "Même base : on additionne les exposants, 3 + 4 = 7."),
  Q("Écrivez sous la forme d'une seule puissance : 10⁵ × 10²", ["10¹⁰", "10⁷", "100⁷", "10³"], "10⁷", "10⁵ × 10² = 10⁵⁺² = 10⁷."),
  Q("Écrivez sous la forme d'une seule puissance : (3²)³", ["3⁵", "3⁶", "9⁶", "3⁸"], "3⁶", "Puissance d'une puissance : on multiplie les exposants, 2 × 3 = 6."),
]),
notion('M9', 1, I, 'm-encadrer-racine', [
  Q("Entre quels entiers consécutifs se trouve √50 ?", ["6 et 7", "7 et 8", "24 et 25", "5 et 6"], "7 et 8", "7² = 49 < 50 < 64 = 8², donc 7 < √50 < 8."),
  Q("Entre quels entiers consécutifs se trouve √20 ?", ["3 et 4", "4 et 5", "10 et 11", "19 et 21"], "4 et 5", "16 < 20 < 25, donc 4 < √20 < 5."),
  Q("Quel entier est le plus proche de √99 ?", ["9", "10", "11", "50"], "10", "√100 = 10 et 99 est très proche de 100 : √99 ≈ 9,95, donc le plus proche est 10."),
]),
notion('M10', 1, I, 'm-factoriser', [
  Q("Factorisez 6x + 9.", ["3(2x + 3)", "6(x + 9)", "3(2x + 9)", "9(x + 1)"], "3(2x + 3)", "6x et 9 ont 3 en facteur commun : 6x + 9 = 3 × 2x + 3 × 3 = 3(2x + 3)."),
  Q("Factorisez 5a − 5b.", ["5(a + b)", "5(a − b)", "a − b", "5ab"], "5(a − b)", "5 est facteur commun : 5a − 5b = 5(a − b)."),
  Q("Factorisez x² + 4x.", ["x(x + 4)", "4x(x + 1)", "x(x + 4x)", "(x + 2)²"], "x(x + 4)", "x est facteur commun : x × x + x × 4 = x(x + 4)."),
]),
notion('M10', 4, I, 'm-mise-en-equation', [
  N("Le triple d'un nombre augmenté de 5 vaut 26. Quel est ce nombre ?", 7, "3x + 5 = 26, donc 3x = 21 et x = 7."),
  N("Paul a 12 ans de plus que sa fille. Ensemble, ils ont 48 ans. Quel âge a la fille ?", 18, "x + (x + 12) = 48, donc 2x = 36 et x = 18 ans."),
  N("Un cinéma propose une place à 8 € ou un abonnement de 30 € puis 5 € la place. À partir de combien de places les deux formules coûtent-elles le même prix ?", 10, "8x = 30 + 5x, donc 3x = 30 et x = 10 places."),
]),
notion('M11', 0, I, 'm-fraction-irreductible', [
  Q("Quelle est la forme irréductible de 84/126 ?", ["42/63", "2/3", "14/21", "4/6"], "2/3", "Le PGCD de 84 et 126 est 42 : 84/126 = 2/3. 42/63 et 14/21 ne sont pas encore irréductibles."),
  Q("Quelle fraction est irréductible ?", ["15/27", "14/35", "9/16", "21/28"], "9/16", "9 = 3² et 16 = 2⁴ n'ont aucun diviseur commun autre que 1."),
  Q("Quelle est la forme irréductible de 45/75 ?", ["9/15", "3/5", "15/25", "5/3"], "3/5", "Le PGCD de 45 et 75 est 15 : 45/75 = 3/5."),
]),
notion('M12', 0, I, 'm-puissances-negatives', [
  Q("Combien vaut 10⁻² ?", ["−100", "0,01", "−0,01", "0,1"], "0,01", "10⁻² = 1/10² = 1/100 = 0,01. Un exposant négatif ne rend pas le nombre négatif."),
  Q("Combien vaut 2⁻³ ?", ["−8", "−6", "1/8", "1/6"], "1/8", "2⁻³ = 1/2³ = 1/8."),
  Q("À quoi est égal 5⁰ ?", ["0", "1", "5", "Ce n'est pas défini"], "1", "Par convention, tout nombre non nul élevé à la puissance 0 vaut 1."),
]),
notion('M17', 4, I, 'm-volume-cylindre', [
  N("Quel est le volume (en cm³) d'un cylindre de rayon 2 cm et de hauteur 10 cm ? Prenez π ≈ 3,14.", 125.6, "V = π × r² × h = 3,14 × 4 × 10 = 125,6 cm³."),
  N("Une boîte cylindrique a un rayon de 5 cm et une hauteur de 4 cm. Quel est son volume (en cm³), avec π ≈ 3,14 ?", 314, "V = 3,14 × 25 × 4 = 314 cm³."),
  Q("Si on double le rayon d'un cylindre sans changer sa hauteur, son volume est…", ["doublé", "multiplié par 4", "multiplié par 8", "inchangé"], "multiplié par 4", "Le volume dépend du carré du rayon : (2r)² = 4r², donc le volume est multiplié par 4."),
]),
notion('M19', 0, I, 'm-angles-paralleles', [
  Q("Deux droites parallèles sont coupées par une sécante. Deux angles alternes-internes sont…", ["supplémentaires", "égaux", "complémentaires", "sans lien"], "égaux", "Avec des droites parallèles, les angles alternes-internes ont la même mesure."),
  N("Deux droites parallèles sont coupées par une sécante. Un angle mesure 65°. Combien mesure l'angle correspondant (en degrés) ?", 65, "Des angles correspondants formés par des parallèles et une sécante sont égaux : 65°."),
  Q("Deux angles alternes-internes formés par deux droites et une sécante ont la même mesure. Que peut-on dire des deux droites ?", ["Elles sont perpendiculaires", "Elles sont parallèles", "Elles sont sécantes", "On ne peut rien conclure"], "Elles sont parallèles", "C'est la propriété réciproque : si des angles alternes-internes sont égaux, les droites sont parallèles."),
]),
notion('M20', 2, I, 'm-cercle-circonscrit', [
  Q("Où se trouve le centre du cercle circonscrit à un triangle ?", ["Au point de concours des médianes", "Au point de concours des médiatrices", "Au point de concours des hauteurs", "Au milieu du plus grand côté, toujours"], "Au point de concours des médiatrices", "Le centre est à égale distance des trois sommets : c'est l'intersection des médiatrices des côtés."),
  Q("Dans un triangle rectangle, où se trouve le centre du cercle circonscrit ?", ["Au sommet de l'angle droit", "Au milieu de l'hypoténuse", "Au centre de gravité", "À l'extérieur du triangle"], "Au milieu de l'hypoténuse", "L'hypoténuse est un diamètre du cercle circonscrit : son milieu en est le centre."),
  N("Un triangle est rectangle et son hypoténuse mesure 10 cm. Quel est le rayon (en cm) de son cercle circonscrit ?", 5, "L'hypoténuse est un diamètre, le rayon vaut 10 ÷ 2 = 5 cm."),
]),
notion('M24', 2, I, 'm-volume-pyramide-cone', [
  N("Quel est le volume (en cm³) d'une pyramide dont la base a une aire de 36 cm² et la hauteur mesure 10 cm ?", 120, "V = aire de la base × hauteur ÷ 3 = 36 × 10 ÷ 3 = 120 cm³."),
  Q("Le volume d'un cône comparé à celui d'un cylindre de même base et de même hauteur est…", ["le même", "la moitié", "le tiers", "le double"], "le tiers", "V(cône) = (1/3) × aire de la base × hauteur, soit le tiers du cylindre correspondant."),
  N("Une pyramide à base carrée de 6 cm de côté a une hauteur de 5 cm. Quel est son volume (en cm³) ?", 60, "Aire de la base = 36 cm², donc V = 36 × 5 ÷ 3 = 60 cm³."),
]),
notion('M26', 1, I, 'm-reciproque-pythagore', [
  Q("Un triangle a des côtés de 5 cm, 12 cm et 13 cm. Est-il rectangle ?", ["Oui, car 5² + 12² = 13²", "Non, car 5 + 12 ≠ 13", "Oui, car c'est un triangle isocèle", "On ne peut pas savoir sans figure"], "Oui, car 5² + 12² = 13²", "25 + 144 = 169 = 13² : d'après la réciproque du théorème de Pythagore, il est rectangle."),
  Q("Un triangle a des côtés de 4 cm, 6 cm et 7 cm. Est-il rectangle ?", ["Oui", "Non, car 4² + 6² ≠ 7²", "Oui, car 4 + 6 > 7", "Seulement s'il est isocèle"], "Non, car 4² + 6² ≠ 7²", "16 + 36 = 52 ≠ 49 : l'égalité de Pythagore n'est pas vérifiée, le triangle n'est pas rectangle (contraposée)."),
  Q("Pour appliquer la réciproque du théorème de Pythagore, quel côté faut-il comparer à la somme des carrés des deux autres ?", ["Le plus petit", "Le plus grand", "N'importe lequel", "Celui du milieu"], "Le plus grand", "Si le triangle est rectangle, l'hypoténuse est forcément le plus grand côté : c'est son carré qu'on compare."),
]),
notion('M26', 0, I, 'm-droite-des-milieux', [
  N("Dans le triangle ABC, I est le milieu de [AB] et J celui de [AC]. BC = 14 cm. Combien mesure IJ (en cm) ?", 7, "D'après le théorème des milieux, IJ = BC ÷ 2 = 7 cm et (IJ) est parallèle à (BC)."),
  Q("Dans un triangle, la droite qui passe par les milieux de deux côtés est…", ["perpendiculaire au troisième côté", "parallèle au troisième côté", "confondue avec une médiane", "une hauteur"], "parallèle au troisième côté", "C'est le théorème de la droite des milieux."),
  N("Dans un triangle, le segment qui joint les milieux de deux côtés mesure 4,5 cm. Combien mesure le troisième côté (en cm) ?", 9, "Ce segment mesure la moitié du troisième côté : 4,5 × 2 = 9 cm."),
]),
notion('M33', 0, I, 'm-moyenne-ponderee', [
  N("Un élève a 12 (coefficient 2) et 15 (coefficient 1). Quelle est sa moyenne ?", 13, "(12 × 2 + 15 × 1) ÷ (2 + 1) = 39 ÷ 3 = 13."),
  N("Dans une classe, 10 élèves ont 8 et 15 élèves ont 13. Quelle est la moyenne de la classe ?", 11, "(10 × 8 + 15 × 13) ÷ 25 = (80 + 195) ÷ 25 = 275 ÷ 25 = 11."),
  N("Notes : 10 (coef. 1), 14 (coef. 3). Quelle est la moyenne ?", 13, "(10 + 14 × 3) ÷ 4 = 52 ÷ 4 = 13."),
]),
notion('M33', 3, I, 'm-mediane-moyenne-extreme', [
  Q("On ajoute une valeur très grande à une série. Quel indicateur est le plus modifié ?", ["La médiane", "La moyenne", "Aucun", "Les deux autant"], "La moyenne", "La moyenne tient compte de toutes les valeurs et est tirée vers le haut ; la médiane, valeur centrale, bouge peu."),
  N("Série : 2 ; 3 ; 4 ; 5 ; 100. Quelle est la médiane ?", 4, "La valeur centrale de la série rangée est 4, malgré la valeur extrême 100."),
  N("Série : 2 ; 3 ; 4 ; 5 ; 100. Quelle est la moyenne ?", 22.8, "(2 + 3 + 4 + 5 + 100) ÷ 5 = 114 ÷ 5 = 22,8 : la valeur extrême tire la moyenne vers le haut."),
]),
notion('M34', 2, I, 'm-evenement-contraire', [
  Q("La probabilité qu'il pleuve demain est 0,3. Quelle est la probabilité qu'il ne pleuve pas ?", ["0,3", "0,7", "1,3", "0"], "0,7", "P(non A) = 1 − P(A) = 1 − 0,3 = 0,7."),
  Q("On lance un dé. Quel est l'événement contraire de « obtenir un nombre pair » ?", ["Obtenir 6", "Obtenir un nombre impair", "Obtenir un multiple de 3", "Ne pas lancer le dé"], "Obtenir un nombre impair", "Le contraire est formé de toutes les issues qui ne sont pas paires : 1, 3 et 5."),
  N("La probabilité de gagner à un jeu est 2/9. Quelle est la probabilité de perdre ? Donnez la réponse arrondie au centième.", 0.78, "1 − 2/9 = 7/9 ≈ 0,78.", 0.005),
]),
notion('M34', 3, I, 'm-deux-epreuves', [
  Q("On lance deux pièces. Quelle est la probabilité d'obtenir deux fois pile ?", ["1/2", "1/3", "1/4", "2/4"], "1/4", "Issues équiprobables : PP, PF, FP, FF. Une seule est favorable : 1/4."),
  Q("On lance deux pièces. Quelle est la probabilité d'obtenir exactement un pile ?", ["1/4", "1/2", "3/4", "1/3"], "1/2", "PF et FP sont favorables : 2 issues sur 4, soit 1/2."),
  Q("On lance deux dés. Combien y a-t-il d'issues possibles ?", ["12", "24", "36", "6"], "36", "6 issues pour le premier dé × 6 pour le second = 36 issues équiprobables."),
]),
notion('M39', 5, I, 'm-coefficient-multiplicatif', [
  N("Par quel nombre multiplie-t-on un prix pour l'augmenter de 15 % ?", 1.15, "Augmenter de 15 % revient à multiplier par 1 + 0,15 = 1,15."),
  N("Par quel nombre multiplie-t-on un prix pour le diminuer de 30 % ?", 0.7, "Diminuer de 30 % revient à multiplier par 1 − 0,30 = 0,7."),
  N("Un article coûte 80 €. Son prix augmente de 10 %. Quel est le nouveau prix (en €) ?", 88, "80 × 1,1 = 88 €."),
]),
notion('M39', 7, I, 'm-partage-proportionnel', [
  N("On partage 60 € entre deux enfants proportionnellement à leur âge : 4 ans et 8 ans. Combien reçoit le plus jeune (en €) ?", 20, "4 + 8 = 12 parts, une part vaut 60 ÷ 12 = 5 €, le plus jeune reçoit 4 × 5 = 20 €."),
  N("Une recette demande farine et sucre dans le ratio 3 : 1. Pour 400 g de mélange, combien faut-il de farine (en g) ?", 300, "3 + 1 = 4 parts de 100 g, la farine représente 3 parts : 300 g."),
  N("Trois amis partagent un gain de 900 € proportionnellement à leurs mises : 100 €, 200 € et 300 €. Combien reçoit celui qui a misé 300 € (en €) ?", 450, "Mises totales : 600 €, sa part est 300/600 = 1/2 du gain, soit 450 €."),
]),
notion('M40', 1, I, 'm-remonter-programme', [
  N("Programme : choisir un nombre, multiplier par 4, puis soustraire 3. Le résultat est 25. Quel nombre a-t-on choisi ?", 7, "On remonte : 25 + 3 = 28, puis 28 ÷ 4 = 7."),
  N("Programme : choisir un nombre, ajouter 5, puis multiplier par 2. Le résultat est 18. Quel nombre a-t-on choisi ?", 4, "18 ÷ 2 = 9, puis 9 − 5 = 4."),
  N("Programme : choisir un nombre, le diviser par 3, puis ajouter 7. Le résultat est 12. Quel nombre a-t-on choisi ?", 15, "12 − 7 = 5, puis 5 × 3 = 15."),
]),
notion('M42', 1, I, 'm-image-antecedent', [
  N("Soit f(x) = 3x − 2. Quelle est l'image de 4 par f ?", 10, "f(4) = 3 × 4 − 2 = 10."),
  N("Soit f(x) = 2x + 6. Quel est l'antécédent de 0 par f ?", -3, "On résout 2x + 6 = 0, donc x = −3."),
  N("Soit g(x) = x² + 1. Quelle est l'image de −3 par g ?", 10, "g(−3) = (−3)² + 1 = 9 + 1 = 10."),
]),
notion('M44', 1, I, 'm-instruction-conditionnelle', [
  Q("Script : « si nombre > 10 alors dire Grand sinon dire Petit ». Que dit le lutin pour 10 ?", ["Grand", "Petit", "Rien", "10"], "Petit", "10 > 10 est faux (10 n'est pas strictement supérieur à 10) : le lutin exécute le « sinon »."),
  Q("Script : « si nombre modulo 2 = 0 alors dire Pair sinon dire Impair ». Que dit le lutin pour 7 ?", ["Pair", "Impair", "0", "7"], "Impair", "Le reste de 7 divisé par 2 vaut 1, la condition est fausse : « Impair »."),
  Q("Dans un programme, à quoi sert une instruction « si… alors… sinon » ?", ["À répéter des instructions", "À choisir entre deux actions selon une condition", "À créer une variable", "À arrêter le programme"], "À choisir entre deux actions selon une condition", "L'instruction conditionnelle exécute un bloc si la condition est vraie, un autre sinon."),
]),
notion('M39', 0, I, 'm-grandeurs-quotients', [
  N("Un train parcourt 240 km en 2 h 30 min. Quelle est sa vitesse moyenne (en km/h) ?", 96, "2 h 30 min = 2,5 h, donc v = 240 ÷ 2,5 = 96 km/h."),
  N("Convertissez 36 km/h en m/s.", 10, "36 km/h = 36 000 m pour 3 600 s, soit 10 m/s (on divise par 3,6)."),
  N("Un cycliste roule à 20 km/h pendant 45 min. Quelle distance (en km) parcourt-il ?", 15, "45 min = 0,75 h, donc d = 20 × 0,75 = 15 km."),
  N("Un robinet débite 12 L par minute. Combien de minutes faut-il pour remplir une baignoire de 150 L ?", 12.5, "150 ÷ 12 = 12,5 minutes (soit 12 min 30 s)."),
]),
]

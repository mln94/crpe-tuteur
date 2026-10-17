from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('M15', 4, D, 'm-identites-remarquables', [
  Q("Développez (2x − 3)².", ["4x² − 9", "4x² − 12x + 9", "4x² + 9", "2x² − 12x + 9"], "4x² − 12x + 9", "(a − b)² = a² − 2ab + b² avec a = 2x et b = 3 : 4x² − 12x + 9. Oublier le double produit est l'erreur classique."),
  Q("Factorisez x² − 49.", ["(x − 7)²", "(x − 7)(x + 7)", "(x − 49)(x + 1)", "x(x − 49)"], "(x − 7)(x + 7)", "C'est une différence de deux carrés : a² − b² = (a − b)(a + b) avec a = x et b = 7."),
  Q("Factorisez 9x² + 6x + 1.", ["(3x + 1)²", "(9x + 1)²", "(3x − 1)²", "3x(3x + 2) + 1"], "(3x + 1)²", "9x² = (3x)², 1 = 1² et 6x = 2 × 3x × 1 : c'est (3x + 1)²."),
  N("Calculez mentalement 101² à l'aide d'une identité remarquable.", 10201, "101² = (100 + 1)² = 10 000 + 200 + 1 = 10 201."),
]),
notion('M15', 1, D, 'm-double-distributivite', [
  Q("Développez (x + 2)(x + 5).", ["x² + 10", "x² + 7x + 10", "x² + 7x + 7", "2x + 7"], "x² + 7x + 10", "x × x + 5x + 2x + 10 = x² + 7x + 10 : chaque terme du premier facteur multiplie chaque terme du second."),
  Q("Développez (2a − 1)(a + 3).", ["2a² + 5a − 3", "2a² − 3", "2a² + 7a − 3", "2a² + 5a + 3"], "2a² + 5a − 3", "2a × a + 2a × 3 − a − 3 = 2a² + 6a − a − 3 = 2a² + 5a − 3."),
  Q("Développez (3 − x)(x − 4).", ["−x² + 7x − 12", "x² − 7x + 12", "−x² − 12", "−x² + x − 12"], "−x² + 7x − 12", "3x − 12 − x² + 4x = −x² + 7x − 12."),
]),
notion('M15', 2, D, 'm-inequation', [
  Q("Résolvez l'inéquation 3x − 5 > 7.", ["x > 4", "x < 4", "x > 2/3", "x > 12"], "x > 4", "3x > 12, puis on divise par 3 (positif) : x > 4."),
  Q("Résolvez l'inéquation −2x ≥ 8.", ["x ≥ −4", "x ≤ −4", "x ≥ 4", "x ≤ 4"], "x ≤ −4", "On divise par −2, un nombre négatif : le sens de l'inégalité change, x ≤ −4."),
  Q("Quel nombre est solution de 5 − x < 2 ?", ["1", "2", "3", "4"], "4", "5 − x < 2 donne −x < −3, donc x > 3 : seul 4 convient."),
]),
notion('M15', 3, D, 'm-equation-produit-nul', [
  Q("Quelles sont les solutions de (x − 3)(x + 5) = 0 ?", ["3 et 5", "−3 et 5", "3 et −5", "Il n'y en a pas"], "3 et −5", "Un produit est nul si l'un de ses facteurs est nul : x − 3 = 0 ou x + 5 = 0, donc x = 3 ou x = −5."),
  Q("Quelles sont les solutions de x² = 5x ?", ["5 seulement", "0 et 5", "0 seulement", "−5 et 5"], "0 et 5", "x² − 5x = 0 s'écrit x(x − 5) = 0 : x = 0 ou x = 5. Diviser par x ferait perdre la solution 0."),
  Q("Quelles sont les solutions de (2x − 1)(x + 4) = 0 ?", ["1/2 et −4", "2 et 4", "−1/2 et 4", "1 et −4"], "1/2 et −4", "2x − 1 = 0 donne x = 1/2 ; x + 4 = 0 donne x = −4."),
]),
notion('M29', 0, D, 'm-thales', [
  N("Dans un triangle ABC, M est sur [AB] et N sur [AC], avec (MN) parallèle à (BC). AM = 3 cm, AB = 9 cm et BC = 12 cm. Combien mesure MN (en cm) ?", 4, "D'après le théorème de Thalès, AM/AB = MN/BC, soit 3/9 = MN/12, donc MN = 4 cm."),
  N("Avec (MN) parallèle à (BC), AM = 4 cm, AB = 10 cm et AN = 6 cm. Combien mesure AC (en cm) ?", 15, "AM/AB = AN/AC donne 4/10 = 6/AC, donc AC = 6 × 10 ÷ 4 = 15 cm."),
  Q("Pour prouver avec la réciproque de Thalès que (MN) // (BC), que faut-il vérifier en plus de l'égalité AM/AB = AN/AC ?", ["Que le triangle est rectangle", "Que les points A, M, B et A, N, C sont alignés dans le même ordre", "Que MN = BC", "Que M et N sont des milieux"], "Que les points A, M, B et A, N, C sont alignés dans le même ordre", "Sans cette condition d'alignement dans le même ordre, l'égalité des rapports ne suffit pas à conclure au parallélisme."),
  N("Un arbre projette une ombre de 12 m. Au même moment, un bâton de 1,5 m projette une ombre de 2 m. Quelle est la hauteur de l'arbre (en m) ?", 9, "Les situations sont proportionnelles (Thalès) : h/12 = 1,5/2, donc h = 9 m."),
]),
notion('M29', 1, D, 'm-trigonometrie', [
  Q("Dans un triangle rectangle, le cosinus d'un angle aigu est égal à…", ["côté opposé / hypoténuse", "côté adjacent / hypoténuse", "côté opposé / côté adjacent", "hypoténuse / côté adjacent"], "côté adjacent / hypoténuse", "cos = adjacent/hypoténuse, sin = opposé/hypoténuse, tan = opposé/adjacent (« CAH SOH TOA »)."),
  N("Un triangle ABC est rectangle en A, avec BC = 10 cm et l'angle B = 30°. Combien mesure AC (en cm) ? On rappelle que sin 30° = 0,5.", 5, "AC est le côté opposé à l'angle B : sin B = AC/BC, donc AC = 10 × 0,5 = 5 cm."),
  N("Une échelle de 5 m est posée contre un mur ; son pied est à 3 m du mur. Quel est le cosinus de l'angle entre l'échelle et le sol ?", 0.6, "Le côté adjacent à l'angle au sol mesure 3 m et l'hypoténuse (l'échelle) 5 m : cos = 3/5 = 0,6."),
]),
notion('M28', 3, D, 'm-volume-boule', [
  Q("Quelle formule donne le volume d'une boule de rayon r ?", ["4πr²", "(4/3)πr³", "πr²h", "(1/3)πr²"], "(4/3)πr³", "V = (4/3) × π × r³. 4πr² est l'aire de la sphère."),
  N("Quel est le volume (en cm³) d'une boule de rayon 3 cm ? Prenez π ≈ 3,14 et arrondissez à l'unité.", 113, "V = 4/3 × 3,14 × 27 = 113,04, soit environ 113 cm³.", 0.5),
  Q("Si on double le rayon d'une boule, son volume est multiplié par…", ["2", "4", "6", "8"], "8", "Le volume dépend du cube du rayon : 2³ = 8."),
]),
notion('M35', 1, D, 'm-quartiles', [
  N("Série rangée : 2 ; 4 ; 5 ; 7 ; 8 ; 10 ; 12 ; 15. Quel est le premier quartile Q1 ?", 4, "8 valeurs : Q1 est la plus petite valeur telle qu'au moins 25 % des données lui sont inférieures ou égales, soit la 2e valeur (8 × 0,25 = 2) : 4."),
  N("Même série : 2 ; 4 ; 5 ; 7 ; 8 ; 10 ; 12 ; 15. Quel est le troisième quartile Q3 ?", 10, "8 × 0,75 = 6 : Q3 est la 6e valeur de la série rangée, soit 10. Au moins 75 % des valeurs lui sont inférieures ou égales."),
  Q("Que représente l'écart interquartile Q3 − Q1 ?", ["L'écart entre la plus grande et la plus petite valeur", "L'étendue de la moitié centrale des données", "La moyenne de la série", "L'écart entre la moyenne et la médiane"], "L'étendue de la moitié centrale des données", "Entre Q1 et Q3 se trouvent environ 50 % des valeurs, celles du centre de la série."),
]),
notion('M36', 0, D, 'm-probabilite-reunion', [
  N("P(A) = 0,5 ; P(B) = 0,4 ; P(A et B) = 0,2. Calculez P(A ou B).", 0.7, "P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 0,5 + 0,4 − 0,2 = 0,7."),
  N("Dans une classe, 60 % des élèves font du sport, 30 % de la musique et 10 % les deux. Quelle proportion (en %) fait du sport ou de la musique ?", 80, "60 + 30 − 10 = 80 % : on retire les 10 % comptés deux fois."),
  Q("A et B sont incompatibles, P(A) = 0,25 et P(B) = 0,35. Combien vaut P(A ou B) ?", ["0,0875", "0,6", "0,1", "1"], "0,6", "Événements incompatibles : P(A ∩ B) = 0, donc P(A ∪ B) = 0,25 + 0,35 = 0,6."),
]),
notion('M41', 0, D, 'm-pourcentages-successifs', [
  N("Un prix baisse de 20 %, puis augmente de 20 %. Par rapport au prix initial, quel est le pourcentage de baisse finale ?", 4, "0,8 × 1,2 = 0,96 : le prix final vaut 96 % du prix initial, soit 4 % de baisse."),
  N("Après une hausse de 25 %, un article coûte 50 €. Quel était son prix initial (en €) ?", 40, "Prix initial × 1,25 = 50, donc prix initial = 50 ÷ 1,25 = 40 €. On ne retire pas 25 % de 50."),
  N("Une population augmente de 10 % deux années de suite. De quel pourcentage a-t-elle augmenté au total ?", 21, "1,1 × 1,1 = 1,21 : hausse de 21 %, et non de 20 %."),
]),
notion('M42', 5, D, 'm-fonction-affine', [
  Q("La fonction f(x) = −3x + 2 est…", ["linéaire", "affine, de coefficient directeur −3", "affine, de coefficient directeur 2", "constante"], "affine, de coefficient directeur −3", "f(x) = ax + b avec a = −3 (coefficient directeur) et b = 2 (ordonnée à l'origine)."),
  Q("Une droite passe par les points (0 ; 1) et (2 ; 7). Quelle fonction affine représente-t-elle ?", ["f(x) = 3x + 1", "f(x) = 7x + 1", "f(x) = 3x + 7", "f(x) = 6x + 1"], "f(x) = 3x + 1", "b = 1 (ordonnée à l'origine) et a = (7 − 1) ÷ (2 − 0) = 3."),
  Q("Quelle fonction est linéaire ?", ["f(x) = 2x + 1", "f(x) = x²", "f(x) = −5x", "f(x) = 3"], "f(x) = −5x", "Une fonction linéaire s'écrit f(x) = ax : sa représentation passe par l'origine. Elle traduit une situation de proportionnalité."),
]),
notion('M12', 1, D, 'm-calculs-puissances', [
  Q("Écrivez sous la forme 10ⁿ : 10⁷ ÷ 10³", ["10¹⁰", "10⁴", "10²¹", "1⁴"], "10⁴", "Quotient de puissances de même base : on soustrait les exposants, 7 − 3 = 4."),
  Q("Quelle est la notation scientifique de (3 × 10⁴) × (5 × 10³) ?", ["15 × 10⁷", "1,5 × 10⁸", "1,5 × 10⁷", "8 × 10⁷"], "1,5 × 10⁸", "3 × 5 = 15 et 10⁴ × 10³ = 10⁷, donc 15 × 10⁷ = 1,5 × 10⁸."),
  Q("Écrivez sous la forme 2ⁿ : 2⁵ × 2⁻⁸", ["2⁻³", "2¹³", "2⁻⁴⁰", "2³"], "2⁻³", "5 + (−8) = −3."),
]),
notion('M13', 0, D, 'm-equation-carre', [
  Q("Quelles sont les solutions de x² = 25 ?", ["5 seulement", "−5 et 5", "12,5", "Aucune"], "−5 et 5", "5² = 25 et (−5)² = 25 : l'équation a deux solutions. Oublier la solution négative est fréquent."),
  Q("Quelles sont les solutions de x² = −4 ?", ["2 et −2", "−2", "Aucune", "4"], "Aucune", "Un carré est toujours positif ou nul : x² ne peut pas valoir −4."),
  Q("Quelles sont les solutions de x² = 7 ?", ["√7 et −√7", "3,5 et −3,5", "√7 seulement", "49"], "√7 et −√7", "Pour a > 0, x² = a a deux solutions : √a et −√a."),
]),
notion('M14', None, D, 'm-nombres-premiers', [
  Q("Quelle est la décomposition en produit de facteurs premiers de 60 ?", ["6 × 10", "2² × 3 × 5", "2 × 30", "4 × 15"], "2² × 3 × 5", "60 = 2 × 2 × 3 × 5 : tous les facteurs doivent être premiers (6, 10, 4, 15 et 30 ne le sont pas)."),
  Q("Lequel de ces nombres est premier ?", ["51", "57", "61", "91"], "61", "61 n'a que deux diviseurs, 1 et 61. 51 = 3 × 17, 57 = 3 × 19, 91 = 7 × 13."),
  Q("Quel est le plus grand diviseur commun de 84 et 120 ?", ["6", "12", "24", "42"], "12", "84 = 2² × 3 × 7 et 120 = 2³ × 3 × 5 : les facteurs communs donnent 2² × 3 = 12."),
]),
notion('M45', 2, D, 'm-boucle-conditionnelle', [
  Q("Script : « mettre n à 1 ; répéter jusqu'à ce que n > 20 : mettre n à n × 2 ». Quelle est la valeur finale de n ?", ["16", "20", "32", "64"], "32", "n prend les valeurs 1, 2, 4, 8, 16, 32 : la boucle s'arrête dès que n > 20, donc à 32."),
  Q("Quelle est la différence entre « répéter 10 fois » et « répéter jusqu'à ce que… » ?", ["Aucune", "La première répète un nombre fixé de fois, la seconde s'arrête quand une condition devient vraie", "La seconde ne s'exécute jamais", "La première est conditionnelle"], "La première répète un nombre fixé de fois, la seconde s'arrête quand une condition devient vraie", "« Répéter jusqu'à » est une boucle conditionnelle : on ne connaît pas à l'avance le nombre de tours."),
  Q("Script : « mettre s à 0 ; mettre k à 1 ; répéter jusqu'à ce que k > 4 : ajouter k à s ; ajouter 1 à k ». Que vaut s à la fin ?", ["4", "6", "10", "15"], "10", "s = 1 + 2 + 3 + 4 = 10 ; la boucle s'arrête quand k vaut 5."),
]),
notion('M30', 3, D, 'm-vecteurs-chasles', [
  Q("D'après la relation de Chasles, à quoi est égal le vecteur AB + BC ?", ["Le vecteur AC", "Le vecteur CA", "Le vecteur BA", "Le vecteur nul"], "Le vecteur AC", "AB + BC = AC : on enchaîne les deux translations de A vers B puis de B vers C."),
  Q("À quoi est égal le vecteur AB + BA ?", ["Le vecteur 2AB", "Le vecteur nul", "Le vecteur AA'", "Le vecteur BB"], "Le vecteur nul", "BA est l'opposé de AB : leur somme est le vecteur nul."),
  Q("ABCD est un parallélogramme. Quelle égalité de vecteurs est vraie ?", ["AB = CD", "AB = DC", "AB = BC", "AC = BD"], "AB = DC", "Dans le parallélogramme ABCD, les vecteurs AB et DC ont même direction, même sens et même longueur."),
]),
]

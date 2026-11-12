# Mathématiques : 100 questions ajoutées (20 par thème), surtout sur des objectifs du programme du cycle 4
# encore peu ou pas couverts
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── Nombres et calculs ──
notion('M1', 0, F, 'm-problemes-quatre-operations', [
  N("Un cinéma vend 128 places à 7 € et 64 places à 5 €. Quelle est la recette totale, en euros ?", 1216, "128 × 7 = 896 et 64 × 5 = 320 ; 896 + 320 = 1 216 €."),
  N("On partage 255 bonbons entre 15 enfants. Combien chacun en reçoit-il ?", 17, "255 ÷ 15 = 17. On contrôle : 15 × 17 = 255."),
  Q("Léa calcule le prix de 9 cahiers à 2,95 € et trouve 265,50 €. Que peut-on dire ?", ["Son résultat est plausible", "Son résultat n'est pas vraisemblable : 9 × 3 € font environ 27 €", "Il faut multiplier par 100", "Le bon résultat est 2,65 €"], "Son résultat n'est pas vraisemblable : 9 × 3 € font environ 27 €", "Un ordre de grandeur (9 × 3 = 27) permet de contrôler : le bon prix est 26,55 €."),
]),
notion('M2', 4, F, 'm-droite-graduee-relatifs', [
  Q("Sur une droite graduée de 1 en 1, le point A est à 3 graduations à gauche de l'origine. Quelle est son abscisse ?", ["3", "−3", "0,3", "−0,3"], "−3", "À gauche de l'origine se trouvent les nombres négatifs."),
  N("Sur une droite graduée, A a pour abscisse −2 et B a pour abscisse 5. Quelle est la distance AB ?", 7, "De −2 à 0 il y a 2 unités, de 0 à 5 il y en a 5 : 2 + 5 = 7."),
  Q("Quel nombre est situé exactement au milieu de −4 et 2 sur une droite graduée ?", ["−1", "1", "−2", "3"], "−1", "(−4 + 2) ÷ 2 = −1."),
]),
notion('M8', 0, I, 'm-puissances-definition', [
  N("Que vaut 2⁵ ?", 32, "2⁵ = 2 × 2 × 2 × 2 × 2 = 32."),
  Q("Que signifie 7⁴ ?", ["7 × 4", "7 + 7 + 7 + 7", "7 × 7 × 7 × 7", "4 × 4 × 4 × 4 × 4 × 4 × 4"], "7 × 7 × 7 × 7", "L'exposant indique le nombre de facteurs égaux à 7."),
  N("Que vaut (−3)³ ?", -27, "(−3) × (−3) × (−3) = 9 × (−3) = −27 : un nombre impair de facteurs négatifs donne un résultat négatif."),
  Q("Pour tout nombre a, que vaut a¹ ?", ["1", "a", "0", "a²"], "a", "Une puissance d'exposant 1 n'a qu'un seul facteur : a¹ = a."),
]),
notion('M10', 0, I, 'm-formules-pairs-impairs', [
  Q("n désigne un nombre entier. Quelle expression désigne toujours un nombre pair ?", ["n + 1", "2n", "n²", "3n"], "2n", "Un nombre pair est un multiple de 2 : il s'écrit 2n."),
  Q("n désigne un nombre entier. Quelle expression désigne toujours un nombre impair ?", ["2n + 1", "2n", "n + 2", "4n"], "2n + 1", "Un nombre impair est un nombre pair augmenté de 1."),
  Q("Quelle est l'aire d'un rectangle de longueur L et de largeur ℓ ?", ["L + ℓ", "2(L + ℓ)", "L × ℓ", "L²"], "L × ℓ", "2(L + ℓ) est le périmètre du rectangle, L × ℓ son aire."),
]),
notion('M15', 0, D, 'm-simplifier-quotients', [
  Q("Simplifier (6x) ÷ (3x), pour x non nul.", ["2", "2x", "3x", "x"], "2", "6x ÷ 3x = (6 ÷ 3) × (x ÷ x) = 2 × 1 = 2."),
  Q("Simplifier la fraction (12a²) / (4a), pour a non nul.", ["3a", "3a²", "8a", "3"], "3a", "12 ÷ 4 = 3 et a² ÷ a = a."),
  Q("Simplifier (15 × 7) / (21 × 5).", ["1", "5/7", "3/5", "105"], "1", "15 × 7 = 105 et 21 × 5 = 105 : le quotient vaut 1. On peut aussi simplifier 15/5 = 3 et 7/21 = 1/3."),
]),
notion('M7', 8, I, 'm-expressions-fractions', [
  Q("Calculer 1/2 + 1/3 × 3/4.", ["3/4", "5/8", "1/2", "2/3"], "3/4", "La multiplication est prioritaire : 1/3 × 3/4 = 1/4, puis 1/2 + 1/4 = 3/4."),
  Q("Calculer (1/2 + 1/3) × 6.", ["5", "3", "6", "1"], "5", "1/2 + 1/3 = 5/6, puis 5/6 × 6 = 5."),
  Q("Calculer 2/3 ÷ 4/9.", ["3/2", "8/27", "2/3", "6"], "3/2", "Diviser par 4/9, c'est multiplier par 9/4 : 2/3 × 9/4 = 18/12 = 3/2."),
  Q("Calculer 1 − 2/5 × 5/4.", ["1/2", "3/4", "1/4", "3/10"], "1/2", "2/5 × 5/4 = 10/20 = 1/2, puis 1 − 1/2 = 1/2."),
]),
# ── Espace et géométrie ──
notion('M20', 4, F, 'm-hauteurs-triangle', [
  Q("Qu'est-ce qu'une hauteur d'un triangle ?", ["La droite passant par un sommet et perpendiculaire au côté opposé", "La droite passant par un sommet et le milieu du côté opposé", "La perpendiculaire à un côté en son milieu", "Le plus grand côté"], "La droite passant par un sommet et perpendiculaire au côté opposé", "La droite passant par un sommet et le milieu du côté opposé est une médiane ; la perpendiculaire en son milieu, une médiatrice."),
  Q("Comment s'appelle le point de concours des trois hauteurs d'un triangle ?", ["L'orthocentre", "Le centre de gravité", "Le centre du cercle circonscrit", "Le milieu"], "L'orthocentre", "Les trois hauteurs d'un triangle sont concourantes en un point appelé orthocentre."),
  N("Un triangle a un côté de 8 cm, et la hauteur relative à ce côté mesure 5 cm. Quelle est son aire, en cm² ?", 20, "Aire = base × hauteur ÷ 2 = 8 × 5 ÷ 2 = 20 cm²."),
]),
notion('M20', 6, F, 'm-medianes', [
  Q("Qu'est-ce qu'une médiane d'un triangle ?", ["La droite passant par un sommet et le milieu du côté opposé", "La perpendiculaire à un côté passant par le sommet opposé", "La bissectrice d'un angle", "La perpendiculaire à un côté en son milieu"], "La droite passant par un sommet et le milieu du côté opposé", "Les trois médianes se coupent au centre de gravité du triangle."),
  Q("Une médiane partage un triangle en deux triangles. Que peut-on dire de leurs aires ?", ["Elles sont égales", "L'une est le double de l'autre", "Cela dépend du triangle", "Leur somme est nulle"], "Elles sont égales", "Les deux triangles ont des bases égales (les deux moitiés du côté) et la même hauteur."),
  N("Un triangle a une aire de 30 cm². Quelle est l'aire de chacun des deux triangles formés par une médiane, en cm² ?", 15, "La médiane partage le triangle en deux triangles de même aire : 30 ÷ 2 = 15 cm²."),
]),
notion('M21', 2, F, 'm-proprietes-parallelogramme', [
  Q("Que peut-on dire des diagonales d'un parallélogramme ?", ["Elles ont le même milieu", "Elles sont toujours perpendiculaires", "Elles ont toujours la même longueur", "Elles ne se coupent pas"], "Elles ont le même milieu", "Un quadrilatère est un parallélogramme si et seulement si ses diagonales se coupent en leur milieu."),
  Q("Que peut-on dire des côtés opposés d'un parallélogramme ?", ["Ils sont parallèles et de même longueur", "Ils sont perpendiculaires", "Ils sont de longueurs différentes", "Ils se coupent"], "Ils sont parallèles et de même longueur", "C'est une propriété caractéristique du parallélogramme."),
  Q("Un quadrilatère a des diagonales de même milieu et de même longueur. Quelle est sa nature ?", ["Un rectangle", "Un losange", "Un trapèze", "Un cerf-volant"], "Un rectangle", "Diagonales de même milieu : parallélogramme ; de même longueur en plus : rectangle."),
  Q("Un quadrilatère a des diagonales de même milieu et perpendiculaires. Quelle est sa nature ?", ["Un losange", "Un rectangle", "Un trapèze", "On ne peut pas savoir"], "Un losange", "Un parallélogramme aux diagonales perpendiculaires est un losange."),
]),
notion('M25', 0, I, 'm-translation', [
  Q("Que fait une translation sur une figure ?", ["Elle la fait glisser sans la tourner ni la déformer", "Elle la retourne comme dans un miroir", "Elle la fait tourner autour d'un point", "Elle l'agrandit"], "Elle la fait glisser sans la tourner ni la déformer", "Tous les points se déplacent dans la même direction, le même sens et de la même longueur."),
  Q("Quelle propriété une translation ne conserve-t-elle pas forcément ?", ["La position de la figure", "Les longueurs", "Les angles", "Les aires"], "La position de la figure", "Une translation conserve les longueurs, les angles, les aires et le parallélisme : seule la position change."),
  Q("La translation qui transforme A en B transforme C en D. Quelle est la nature du quadrilatère ABDC ?", ["Un parallélogramme (éventuellement aplati)", "Un trapèze quelconque", "Un triangle", "Un cerf-volant"], "Un parallélogramme (éventuellement aplati)", "C'est la définition ponctuelle de la translation : ABDC est un parallélogramme."),
]),
notion('M28', 2, D, 'm-sections-solides', [
  Q("Quelle est la section d'un pavé droit par un plan parallèle à une face ?", ["Un rectangle de mêmes dimensions que cette face", "Un triangle", "Un cercle", "Un trapèze"], "Un rectangle de mêmes dimensions que cette face", "La section parallèle à une face est un rectangle superposable à cette face."),
  Q("Quelle est la section d'un cylindre par un plan perpendiculaire à son axe ?", ["Un disque de même rayon que la base", "Un rectangle", "Une ellipse", "Un triangle"], "Un disque de même rayon que la base", "Coupé parallèlement à son axe, le cylindre donne un rectangle."),
  Q("Quelle est la section d'une boule par un plan ?", ["Un disque", "Un carré", "Un anneau", "Une sphère"], "Un disque", "Le disque est le plus grand quand le plan passe par le centre (grand cercle)."),
]),
notion('M26', 3, I, 'm-triangle-rectangle-cercle', [
  Q("Un triangle ABC est inscrit dans un cercle de diamètre [BC]. Que peut-on en déduire ?", ["ABC est rectangle en A", "ABC est rectangle en B", "ABC est équilatéral", "ABC est isocèle"], "ABC est rectangle en A", "Si un triangle est inscrit dans un cercle ayant pour diamètre l'un de ses côtés, il est rectangle au sommet opposé à ce côté."),
  Q("Où se trouve le centre du cercle circonscrit à un triangle rectangle ?", ["Au milieu de l'hypoténuse", "Au sommet de l'angle droit", "Au centre de gravité", "Hors du triangle"], "Au milieu de l'hypoténuse", "L'hypoténuse est un diamètre du cercle circonscrit."),
  N("Un triangle rectangle a une hypoténuse de 10 cm. Quel est le rayon de son cercle circonscrit, en cm ?", 5, "L'hypoténuse est un diamètre : rayon = 10 ÷ 2 = 5 cm."),
  N("Dans un triangle ABC rectangle en A, M est le milieu de [BC] et BC = 12 cm. Combien mesure AM, en cm ?", 6, "M est le centre du cercle circonscrit : MA = MB = MC = 12 ÷ 2 = 6 cm."),
]),
# ── Organisation et gestion de données et probabilités ──
notion('M31', 4, F, 'm-choisir-representation', [
  Q("Pour montrer la répartition des élèves d'une classe selon leur moyen de transport (en parts du total), quel graphique choisir ?", ["Un diagramme circulaire", "Un graphique cartésien", "Une droite graduée", "Un nuage de points"], "Un diagramme circulaire", "Le diagramme circulaire montre la part de chaque catégorie dans le total."),
  Q("Pour montrer l'évolution de la température heure par heure au cours d'une journée, quel graphique choisir ?", ["Un graphique cartésien (courbe)", "Un diagramme circulaire", "Un tableau à double entrée", "Une boîte à moustaches"], "Un graphique cartésien (courbe)", "Une courbe met en évidence une évolution dans le temps."),
  N("Dans un diagramme circulaire, une catégorie représente 25 % de l'effectif. Quel angle faut-il lui attribuer, en degrés ?", 90, "25 % de 360° = 90°."),
]),
notion('M32', 3, F, 'm-repeter-experience', [
  N("On lance une pièce 50 fois et on obtient 27 fois « pile ». Quelle est la fréquence de « pile », en pourcentage ?", 54, "27 ÷ 50 = 0,54, soit 54 %."),
  Q("On lance un dé 60 fois et on obtient 13 fois le 6. Que peut-on dire ?", ["Le dé est forcément truqué", "La fréquence observée (environ 0,22) est proche de la probabilité 1/6 ≈ 0,17 : rien d'anormal sur si peu de lancers", "La probabilité d'obtenir 6 vaut 13/60", "On aurait dû obtenir exactement 10 fois le 6"], "La fréquence observée (environ 0,22) est proche de la probabilité 1/6 ≈ 0,17 : rien d'anormal sur si peu de lancers", "La fréquence fluctue d'une série de lancers à l'autre ; elle n'est pas égale à la probabilité."),
  Q("Dans un tableau de résultats, quelle est la somme des fréquences de toutes les issues ?", ["1 (ou 100 %)", "0", "Le nombre de lancers", "Cela dépend de l'expérience"], "1 (ou 100 %)", "Chaque fréquence est effectif ÷ effectif total ; leur somme vaut donc 1."),
]),
notion('M34', 1, I, 'm-evenements-ensembles', [
  Q("On tire un nombre entier de 1 à 10. A = « le nombre est pair », B = « le nombre est supérieur à 6 ». Quel est l'évènement A ∩ B (A et B) ?", ["{8 ; 10}", "{2 ; 4 ; 6 ; 7 ; 8 ; 9 ; 10}", "{7 ; 9}", "{6 ; 8 ; 10}"], "{8 ; 10}", "A ∩ B contient les issues qui réalisent A et B à la fois : pairs et strictement supérieurs à 6."),
  Q("Même expérience (entier de 1 à 10). Combien d'issues compte A ∪ B (A ou B), avec A = « pair » et B = « supérieur à 6 » ?", ["7", "5", "4", "2"], "7", "A ∪ B = {2 ; 4 ; 6 ; 7 ; 8 ; 9 ; 10}, soit 7 issues."),
  Q("Comment appelle-t-on un évènement qui ne contient aucune issue ?", ["Un évènement impossible (ensemble vide)", "Un évènement certain", "Un évènement contraire", "Un évènement élémentaire"], "Un évènement impossible (ensemble vide)", "Sa probabilité vaut 0."),
  Q("On lance un dé à six faces. Quel est le complémentaire de l'évènement « obtenir 1 ou 2 » ?", ["Obtenir 3, 4, 5 ou 6", "Obtenir 1", "Obtenir 6", "Ne pas lancer le dé"], "Obtenir 3, 4, 5 ou 6", "Le complémentaire (évènement contraire) regroupe toutes les autres issues."),
]),
notion('M35', 0, D, 'm-effectifs-cumules', [
  Q("Notes d'une classe : 8 (3 élèves), 10 (5 élèves), 12 (7 élèves), 15 (5 élèves). Quel est l'effectif cumulé croissant de la note 12 ?", ["15", "7", "20", "8"], "15", "3 + 5 + 7 = 15 élèves ont une note inférieure ou égale à 12."),
  Q("Avec la même série (8 : 3 élèves ; 10 : 5 ; 12 : 7 ; 15 : 5), quelle est la médiane ?", ["12", "10", "11", "11,25"], "12", "Effectif total 20 : la médiane est entre la 10e et la 11e valeur. Les effectifs cumulés (3, 8, 15) montrent que les deux valent 12."),
  Q("À quoi sert la colonne des effectifs cumulés croissants ?", ["À savoir combien de valeurs sont inférieures ou égales à chaque valeur, pour trouver la médiane et les quartiles", "À calculer l'étendue", "À calculer la moyenne", "À tracer un diagramme circulaire"], "À savoir combien de valeurs sont inférieures ou égales à chaque valeur, pour trouver la médiane et les quartiles", "On repère la valeur à partir de laquelle l'effectif cumulé atteint la moitié (médiane) ou le quart (Q1)."),
]),
notion('M36', 2, D, 'm-stabilisation-frequences', [
  Q("Que se passe-t-il pour la fréquence d'apparition de « pile » quand on lance une pièce un très grand nombre de fois ?", ["Elle se rapproche de la probabilité 0,5", "Elle vaut exactement 0,5 dès 10 lancers", "Elle augmente sans cesse", "Elle tend vers 0"], "Elle se rapproche de la probabilité 0,5", "C'est la stabilisation des fréquences (loi des grands nombres)."),
  Q("Pour estimer la probabilité qu'une punaise tombe pointe en l'air, que faire ?", ["La lancer un grand nombre de fois et calculer la fréquence observée", "Dire qu'elle vaut 1/2", "La lancer une seule fois", "Ce n'est pas possible"], "La lancer un grand nombre de fois et calculer la fréquence observée", "Sans équiprobabilité, on estime la probabilité par une fréquence sur un grand nombre d'essais."),
  Q("Deux élèves simulent 20 lancers d'un dé ; leurs fréquences de 6 diffèrent. Que montre-t-on ?", ["La fluctuation d'échantillonnage", "Une erreur de calcul", "Que le dé est truqué", "Que la probabilité change"], "La fluctuation d'échantillonnage", "Sur un petit nombre de répétitions, les fréquences varient d'une série à l'autre."),
]),
notion('M33', 6, I, 'm-tableur-stats', [
  Q("Dans un tableur, quelle formule calcule la moyenne des cellules A1 à A20 ?", ["=MOYENNE(A1:A20)", "=SOMME(A1:A20)", "=MEDIANE(A1:A20)", "=A1+A20/2"], "=MOYENNE(A1:A20)", "Une formule de tableur commence par le signe =."),
  Q("Quelle formule de tableur donne la médiane des valeurs de B2 à B30 ?", ["=MEDIANE(B2:B30)", "=MOYENNE(B2:B30)", "=MAX(B2:B30)", "=B30-B2"], "=MEDIANE(B2:B30)", "La fonction MEDIANE trie les valeurs et renvoie la valeur centrale."),
  Q("Comment calculer l'étendue des valeurs de C1 à C15 avec un tableur ?", ["=MAX(C1:C15)-MIN(C1:C15)", "=SOMME(C1:C15)", "=C15-C1", "=MOYENNE(C1:C15)"], "=MAX(C1:C15)-MIN(C1:C15)", "L'étendue est la différence entre la plus grande et la plus petite valeur, pas entre la dernière et la première cellule."),
  Q("Une formule « =SOMME(A1:A10)/10 » calcule…", ["la moyenne des 10 valeurs", "la médiane", "l'étendue", "l'effectif total"], "la moyenne des 10 valeurs", "Somme des valeurs divisée par leur nombre : c'est la moyenne."),
]),
# ── Proportionnalité, fonctions ──
notion('M37', 6, F, 'm-nuage-proportionnalite', [
  Q("Dans un repère, les points représentant une situation de proportionnalité sont…", ["alignés avec l'origine du repère", "alignés, mais pas avec l'origine", "disposés au hasard", "sur une courbe en cloche"], "alignés avec l'origine du repère", "C'est la caractérisation graphique de la proportionnalité."),
  Q("Des points sont alignés sur une droite qui ne passe pas par l'origine. La situation est-elle proportionnelle ?", ["Non", "Oui", "Seulement si la droite monte", "On ne peut pas savoir"], "Non", "Il faut que la droite passe par l'origine : par exemple, un prix avec un abonnement fixe n'est pas proportionnel."),
  Q("Le prix d'un taxi est de 3 € de prise en charge plus 2 € par kilomètre. La représentation graphique est…", ["une droite qui ne passe pas par l'origine : ce n'est pas proportionnel", "une droite passant par l'origine", "une courbe", "un ensemble de points non alignés"], "une droite qui ne passe pas par l'origine : ce n'est pas proportionnel", "Pour 0 km, on paie déjà 3 € : le point (0 ; 3) n'est pas l'origine."),
]),
notion('M37', 0, F, 'm-echelles', [
  N("Sur une carte à l'échelle 1/25 000, deux villages sont à 4 cm l'un de l'autre. Quelle est la distance réelle, en km ?", 1, "4 × 25 000 = 100 000 cm = 1 000 m = 1 km."),
  N("Un plan est à l'échelle 1/100. Une pièce mesure 5 m de long. Quelle est sa longueur sur le plan, en cm ?", 5, "5 m = 500 cm ; 500 ÷ 100 = 5 cm."),
  Q("Que signifie une échelle de 1/50 000 ?", ["1 cm sur la carte représente 50 000 cm (500 m) dans la réalité", "1 cm représente 50 000 km", "1 km représente 50 000 cm", "La carte est 50 000 fois plus grande que la réalité"], "1 cm sur la carte représente 50 000 cm (500 m) dans la réalité", "L'échelle est le coefficient de proportionnalité entre distances sur la carte et distances réelles, dans la même unité."),
  Q("Une maquette d'avion est à l'échelle 1/72. L'avion réel mesure 36 m. Quelle est la longueur de la maquette ?", ["50 cm", "2 m", "72 cm", "5 cm"], "50 cm", "36 m = 3 600 cm ; 3 600 ÷ 72 = 50 cm."),
]),
notion('M38', 0, F, 'm-en-fonction-de', [
  Q("« Le périmètre d'un carré en fonction de son côté c » s'écrit…", ["P = 4c", "P = c²", "P = c + 4", "P = 2c"], "P = 4c", "Le périmètre dépend du côté : à chaque valeur de c correspond une seule valeur de P."),
  Q("Le prix payé dépend du nombre de croissants achetés, à 1,20 € pièce. Quelle phrase est correcte ?", ["Le prix est fonction du nombre de croissants", "Le nombre de croissants est fonction du prix du pain", "Le prix ne dépend de rien", "Le prix et le nombre de croissants sont égaux"], "Le prix est fonction du nombre de croissants", "« En fonction de » exprime la dépendance d'une grandeur par rapport à une autre."),
  N("L'aire A d'un carré en fonction de son côté c est A = c². Que vaut A pour c = 6 ?", 36, "6² = 6 × 6 = 36."),
]),
notion('M40', 2, I, 'm-formule-dependance', [
  Q("Un abonnement de streaming coûte 9 € par mois. Quelle formule donne le coût C en fonction du nombre de mois m ?", ["C = 9m", "C = m + 9", "C = 9/m", "C = m²"], "C = 9m", "Le coût est proportionnel au nombre de mois."),
  Q("Une salle de sport demande 30 € d'inscription puis 15 € par mois. Quel est le coût C en fonction du nombre de mois m ?", ["C = 30 + 15m", "C = 45m", "C = 15 + 30m", "C = 30m + 15m"], "C = 30 + 15m", "Partie fixe (30 €) et partie variable (15 € × m)."),
  N("Avec la formule C = 30 + 15m, quel est le coût pour 8 mois, en euros ?", 150, "30 + 15 × 8 = 30 + 120 = 150 €."),
]),
notion('M42', 6, D, 'm-coefficients-affine', [
  Q("La droite représentant la fonction affine f(x) = 2x + 3 coupe l'axe des ordonnées au point d'ordonnée…", ["3", "2", "0", "−3"], "3", "L'ordonnée à l'origine est b = f(0) = 3."),
  Q("La droite d'une fonction affine passe par (0 ; 1) et (2 ; 7). Quelle est cette fonction ?", ["f(x) = 3x + 1", "f(x) = 2x + 1", "f(x) = 7x + 1", "f(x) = x + 3"], "f(x) = 3x + 1", "b = 1 (ordonnée à l'origine) ; a = (7 − 1) ÷ (2 − 0) = 3."),
  Q("Pour f(x) = −2x + 5, que se passe-t-il quand x augmente de 1 ?", ["f(x) diminue de 2", "f(x) augmente de 2", "f(x) augmente de 5", "f(x) ne change pas"], "f(x) diminue de 2", "Le coefficient directeur a = −2 indique la variation de f(x) quand x augmente de 1."),
  Q("La droite d'une fonction affine est parallèle à l'axe des abscisses. Que vaut son coefficient directeur ?", ["0", "1", "−1", "Il n'existe pas"], "0", "La fonction est alors constante : f(x) = b."),
]),
notion('M42', 7, D, 'm-fonction-carre', [
  N("Pour la fonction carré f(x) = x², que vaut f(−4) ?", 16, "(−4)² = (−4) × (−4) = 16."),
  Q("Quels nombres ont pour image 9 par la fonction carré ?", ["3 et −3", "3 seulement", "81", "4,5"], "3 et −3", "3² = 9 et (−3)² = 9 : 9 a deux antécédents."),
  Q("Quelle est l'allure de la représentation graphique de la fonction carré ?", ["Une parabole, symétrique par rapport à l'axe des ordonnées", "Une droite passant par l'origine", "Une droite horizontale", "Un cercle"], "Une parabole, symétrique par rapport à l'axe des ordonnées", "La courbe n'est pas une droite : la fonction carré n'est pas affine."),
]),
# ── La pensée informatique ──
notion('M43', 2, F, 'm-info-formule-blocs', [
  Q("Quelle expression informatique correspond à « le double de x augmenté de 5 » ?", ["(2 * x) + 5", "2 * (x + 5)", "2 + x * 5", "x * x + 5"], "(2 * x) + 5", "En programmation, la multiplication s'écrit souvent avec *. On double x, puis on ajoute 5."),
  Q("Quelle formule correspond à l'emboîtement de blocs « ( (a) + (b) ) / (2) » ?", ["(a + b) ÷ 2", "a + b ÷ 2", "a + (b ÷ 2)", "2 ÷ (a + b)"], "(a + b) ÷ 2", "Le bloc intérieur (a + b) est calculé en premier : c'est la moyenne de a et b."),
  N("Un programme calcule « (côté) * (côté) * (côté) ». Que donne-t-il pour un côté de 3 ?", 27, "3 × 3 × 3 = 27 : c'est le volume d'un cube de côté 3."),
]),
notion('M43', 6, F, 'm-info-boucle-trace', [
  N("x vaut 0. On exécute « répéter 5 fois : ajouter 3 à x ». Que vaut x à la fin ?", 15, "5 × 3 = 15."),
  N("x vaut 1. On exécute « répéter 4 fois : mettre x à x × 2 ». Que vaut x à la fin ?", 16, "1 → 2 → 4 → 8 → 16."),
  Q("Un lutin exécute « répéter 3 fois : avancer de 100, tourner de 120° ». Que trace-t-il ?", ["Un triangle équilatéral", "Un carré", "Un hexagone", "Un segment"], "Un triangle équilatéral", "3 côtés égaux et 3 × 120° = 360° : la figure se referme."),
  N("Combien de fois le bloc « dire Bonjour » est-il exécuté dans « répéter 3 fois : répéter 4 fois : dire Bonjour » ?", 12, "Boucles imbriquées : 3 × 4 = 12."),
]),
notion('M44', 0, I, 'm-info-comparaisons', [
  Q("Quelle condition teste si un âge est compris entre 12 et 18 ans inclus ?", ["âge ≥ 12 et âge ≤ 18", "âge ≥ 12 ou âge ≤ 18", "âge = 12 et âge = 18", "âge > 18"], "âge ≥ 12 et âge ≤ 18", "Les deux conditions doivent être vraies en même temps."),
  Q("Pour x = 7, quelle condition est fausse ?", ["x > 7", "x ≥ 7", "x < 10", "x ≠ 0"], "x > 7", "7 > 7 est faux : 7 n'est pas strictement supérieur à lui-même."),
  Q("« Si note ≥ 10 alors dire Admis sinon dire Refusé. » La note vaut 9,5. Qu'affiche le programme ?", ["Refusé", "Admis", "Rien", "9,5"], "Refusé", "9,5 ≥ 10 est faux : le programme exécute la partie « sinon »."),
]),
notion('M44', 2, I, 'm-info-compteur', [
  N("« score » vaut 0. On exécute « répéter 10 fois : si le nombre tiré est pair, ajouter 1 à score ». Les tirages sont 2, 5, 8, 3, 6, 1, 4, 7, 10, 9. Que vaut score ?", 5, "Les nombres pairs tirés sont 2, 8, 6, 4 et 10 : score vaut 5."),
  N("« vies » vaut 3. Le joueur touche deux obstacles et le programme exécute deux fois « ajouter −1 à vies ». Que vaut vies ?", 1, "3 − 1 − 1 = 1."),
  Q("Pourquoi faut-il souvent « mettre score à 0 » au début d'un programme ?", ["Pour initialiser la variable, sinon elle garde la valeur de la partie précédente", "Pour l'effacer de l'écran", "Pour accélérer le programme", "Ce n'est jamais utile"], "Pour initialiser la variable, sinon elle garde la valeur de la partie précédente", "Initialiser une variable, c'est lui donner sa valeur de départ."),
  N("a vaut 5 et b vaut 8. On exécute « mettre a à b », puis « mettre b à a ». Que vaut b ?", 8, "Après la première instruction, a vaut déjà 8 ; b reçoit donc 8. Pour échanger deux variables, il faut une variable intermédiaire."),
]),
notion('M45', 3, D, 'm-info-structurer', [
  Q("Dans Scratch, à quoi sert un bloc personnalisé (« Créer un bloc ») ?", ["À regrouper une suite d'instructions réutilisable, appelée par un seul bloc", "À changer le costume du lutin", "À arrêter le programme", "À créer une variable"], "À regrouper une suite d'instructions réutilisable, appelée par un seul bloc", "Découper un programme en sous-programmes le rend plus lisible et évite de répéter du code."),
  Q("Un bloc personnalisé « carré (côté) » trace un carré de la taille donnée. Comment appelle-t-on « côté » ?", ["Un paramètre", "Une boucle", "Un capteur", "Un évènement"], "Un paramètre", "Le paramètre permet d'utiliser le même bloc avec des valeurs différentes."),
  Q("Quel est l'intérêt de structurer un long programme en plusieurs sous-programmes ?", ["Il est plus lisible, plus facile à corriger et à réutiliser", "Il s'exécute forcément plus vite", "Il n'a plus besoin de variables", "Il ne peut plus avoir d'erreur"], "Il est plus lisible, plus facile à corriger et à réutiliser", "Chaque sous-programme réalise une tâche précise."),
]),
notion('M45', 4, D, 'm-info-probleme', [
  Q("Quel programme affiche les multiples de 7 inférieurs à 50 ?", ["Mettre n à 7 ; répéter jusqu'à n > 50 : dire n, ajouter 7 à n", "Répéter 50 fois : dire 7", "Mettre n à 0 ; dire n × 50", "Si n = 7 alors dire 50"], "Mettre n à 7 ; répéter jusqu'à n > 50 : dire n, ajouter 7 à n", "La boucle conditionnelle s'arrête dès que n dépasse 50 : 7, 14, …, 49."),
  N("Un programme ajoute 15 € chaque mois à une tirelire qui contient 40 €, jusqu'à atteindre au moins 200 €. Combien de mois faut-il ?", 11, "40 + 15 × 10 = 190 € (insuffisant) ; 40 + 15 × 11 = 205 € : il faut 11 mois."),
  Q("Pour qu'un programme demande un mot de passe jusqu'à ce qu'il soit correct, quelle structure faut-il ?", ["Une boucle « répéter jusqu'à ce que réponse = mot de passe »", "Une boucle « répéter 3 fois »", "Une seule instruction « demander »", "Une condition sans boucle"], "Une boucle « répéter jusqu'à ce que réponse = mot de passe »", "On ne sait pas à l'avance combien d'essais seront nécessaires : il faut une boucle conditionnelle."),
]),
]

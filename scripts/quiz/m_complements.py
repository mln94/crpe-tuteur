# Mathématiques : notions ajoutées pour rééquilibrer les thèmes (pensée informatique 12 → 42 questions,
# données et probabilités 36 → 42, proportionnalité et fonctions 37 → 43)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── La pensée informatique ──
notion('M43', 0, F, 'm-info-sequence', [
  Q("Un lutin exécute « avancer de 10 », puis « tourner de 90° à droite », puis « avancer de 10 ». Qu'a-t-il tracé ?", ["Un segment de 20 pas", "Deux segments formant un angle droit", "Un carré", "Un cercle"], "Deux segments formant un angle droit", "Les instructions s'exécutent dans l'ordre : l'ordre (la séquence) change le résultat."),
  Q("Pourquoi l'ordre des instructions est-il important dans un programme ?", ["Il ne l'est pas", "Les instructions s'exécutent l'une après l'autre : changer l'ordre peut changer le résultat", "Seule la dernière instruction compte", "L'ordinateur les trie seul"], "Les instructions s'exécutent l'une après l'autre : changer l'ordre peut changer le résultat", "Un programme est une suite ordonnée d'instructions."),
  N("x vaut 2. On exécute « ajouter 3 à x », puis « multiplier x par 4 ». Que vaut x ?", 20, "(2 + 3) × 4 = 20. Dans l'autre ordre, on obtiendrait 2 × 4 + 3 = 11."),
]),
notion('M43', 1, F, 'm-info-entrees-sorties', [
  Q("Dans un programme qui demande l'âge de l'utilisateur puis affiche « Vous êtes majeur » ou « Vous êtes mineur », l'âge saisi est…", ["une sortie", "une entrée", "une boucle", "une variable cachée"], "une entrée", "Une entrée est une donnée fournie au programme ; ce qu'il affiche est une sortie."),
  Q("Dans le même programme, le message affiché est…", ["une entrée", "une sortie", "une condition", "un capteur"], "une sortie", "Le programme produit une sortie à partir des entrées."),
  Q("Dans Scratch, quel bloc permet de récupérer une entrée de l'utilisateur ?", ["« demander … et attendre »", "« avancer de 10 »", "« dire Bonjour »", "« répéter 10 fois »"], "« demander … et attendre »", "La réponse est ensuite stockée dans la variable « réponse »."),
]),
notion('M43', 3, F, 'm-info-calcul-blocs', [
  N("Un programme par blocs calcule « (5 + 3) × 2 ». Quel résultat affiche-t-il ?", 16, "Les parenthèses (ou l'emboîtement des blocs) font calculer 5 + 3 = 8 d'abord, puis 8 × 2 = 16."),
  N("Un programme demande un nombre, le multiplie par 3 puis retire 4. On saisit 6. Quel nombre affiche-t-il ?", 14, "6 × 3 = 18, puis 18 − 4 = 14."),
  N("Un programme calcule le périmètre d'un carré : « côté × 4 ». On saisit 7. Quel résultat affiche-t-il ?", 28, "7 × 4 = 28."),
]),
notion('M43', 5, F, 'm-info-parametres', [
  Q("Pour qu'un programme trace un carré plus grand, que faut-il modifier dans « répéter 4 fois : avancer de 50, tourner de 90° » ?", ["Le nombre de répétitions", "La longueur « 50 »", "L'angle « 90 »", "Rien"], "La longueur « 50 »", "La longueur fixe la taille du côté ; l'angle et le nombre de répétitions fixent la forme."),
  Q("Pour transformer ce programme afin qu'il trace un hexagone régulier, que faut-il changer ?", ["Répéter 6 fois et tourner de 60°", "Répéter 4 fois et tourner de 60°", "Répéter 6 fois et tourner de 90°", "Avancer de 60"], "Répéter 6 fois et tourner de 60°", "Pour un polygone régulier à n côtés, on tourne de 360° ÷ n."),
  N("De combien de degrés le lutin doit-il tourner à chaque fois pour tracer un pentagone régulier ?", 72, "360° ÷ 5 = 72°."),
]),
notion('M44', 0, I, 'm-info-condition-simple', [
  Q("Quelle condition teste si un nombre n est pair ?", ["n > 2", "le reste de la division de n par 2 vaut 0", "n = 2", "n est un multiple de 3"], "le reste de la division de n par 2 vaut 0", "Un nombre est pair si sa division par 2 tombe juste."),
  Q("« Si température < 0 alors afficher Gel. » Il fait 3 °C. Qu'affiche le programme ?", ["Gel", "Rien", "3", "Une erreur"], "Rien", "La condition est fausse : l'instruction n'est pas exécutée."),
  Q("Quelle condition est vraie pour x = 5 ?", ["x > 5", "x < 5", "x ≥ 5", "x = 4"], "x ≥ 5", "« ≥ » signifie supérieur ou égal : 5 ≥ 5 est vrai."),
]),
notion('M44', 2, I, 'm-info-variable', [
  N("La variable « points » vaut 10. On exécute « ajouter 5 à points » trois fois. Que vaut « points » ?", 25, "10 + 3 × 5 = 25."),
  N("a vaut 4. On exécute « mettre a à a × a ». Que vaut a ?", 16, "La nouvelle valeur de a est calculée avec l'ancienne : 4 × 4 = 16."),
  Q("Qu'est-ce qu'une variable dans un programme ?", ["Une valeur qui ne change jamais", "Un nom associé à une valeur qui peut changer pendant l'exécution", "Une boucle", "Un affichage"], "Un nom associé à une valeur qui peut changer pendant l'exécution", "On peut lire, modifier et réutiliser la valeur d'une variable."),
]),
notion('M44', 3, I, 'm-info-ecrire-programme', [
  Q("Quel programme affiche les nombres de 1 à 10 ?", ["Mettre n à 1 ; répéter 10 fois : dire n, ajouter 1 à n", "Répéter 10 fois : dire 10", "Mettre n à 10 ; dire n", "Répéter 1 fois : dire 1 à 10"], "Mettre n à 1 ; répéter 10 fois : dire n, ajouter 1 à n", "La variable n augmente de 1 à chaque tour de boucle."),
  Q("Pour calculer la somme 1 + 2 + … + 100, que faut-il ?", ["Une seule instruction « dire 100 »", "Une boucle et une variable qui accumule la somme", "Une condition seulement", "Aucune variable"], "Une boucle et une variable qui accumule la somme", "À chaque tour, on ajoute le nombre courant à la variable « somme »."),
  N("Quel est le résultat de la somme 1 + 2 + … + 10 calculée par un programme ?", 55, "1 + 2 + … + 10 = 55."),
]),
notion('M44', 4, I, 'm-info-modifier-programme', [
  Q("« Répéter 5 fois : avancer de 20. » Comment faire avancer le lutin deux fois plus loin au total ?", ["Répéter 10 fois, ou avancer de 40", "Répéter 2 fois", "Tourner de 20°", "Avancer de 10"], "Répéter 10 fois, ou avancer de 40", "La distance totale est 5 × 20 = 100 ; il faut obtenir 200."),
  Q("Un programme affiche « Bravo » si le score est supérieur à 15. Comment l'afficher aussi pour un score de 15 ?", ["Remplacer « > 15 » par « ≥ 15 »", "Remplacer « > 15 » par « < 15 »", "Supprimer la condition", "Remplacer 15 par 16"], "Remplacer « > 15 » par « ≥ 15 »", "« Supérieur ou égal » inclut la valeur 15."),
  N("« Répéter 4 fois : ajouter 3 à x », avec x = 0 au départ. On remplace « 4 » par « 7 ». Que vaut x à la fin ?", 21, "7 × 3 = 21."),
]),
notion('M45', 0, D, 'm-info-variables-avancees', [
  Q("On veut échanger les valeurs de a et b. Quelle suite d'instructions est correcte ?", ["mettre a à b ; mettre b à a", "mettre c à a ; mettre a à b ; mettre b à c", "mettre b à a ; mettre a à b", "mettre a à a + b"], "mettre c à a ; mettre a à b ; mettre b à c", "Sans variable intermédiaire, la valeur de a serait perdue."),
  N("a = 3 et b = 8. On exécute : « mettre c à a », « mettre a à b », « mettre b à c ». Que vaut b ?", 3, "c garde l'ancienne valeur de a (3), qui est ensuite donnée à b."),
  N("Un compteur commence à 0. Dans une boucle de 6 tours, on ajoute 2 si le tour est pair (2, 4, 6) et 1 sinon. Que vaut le compteur ?", 9, "Tours impairs : 1 + 1 + 1 = 3 ; tours pairs : 2 + 2 + 2 = 6 ; total 9."),
]),
notion('M45', 1, D, 'm-info-conditions-composees', [
  Q("« Si âge ≥ 18 ET permis = oui alors conduire. » Une personne a 20 ans sans permis. Peut-elle conduire selon le programme ?", ["Oui", "Non", "Seulement le jour", "On ne peut pas savoir"], "Non", "Avec ET, les deux conditions doivent être vraies."),
  Q("« Si note < 5 OU absences > 10 alors convoquer. » Un élève a 12 de moyenne et 14 absences. Est-il convoqué ?", ["Oui", "Non", "Seulement s'il a moins de 5", "On ne peut pas savoir"], "Oui", "Avec OU, une seule condition vraie suffit : 14 > 10."),
  Q("Quelle condition décrit un nombre x compris entre 10 et 20 inclus ?", ["x ≥ 10 OU x ≤ 20", "x ≥ 10 ET x ≤ 20", "x > 10 ET x > 20", "x = 10 OU x = 20"], "x ≥ 10 ET x ≤ 20", "Avec OU, tous les nombres vérifieraient la condition."),
]),
# ── Organisation et gestion de données et probabilités ──
notion('M31', 2, F, 'm-donnees-lecture-diagramme', [
  Q("Dans un diagramme en barres, que représente la hauteur de chaque barre ?", ["La couleur", "L'effectif (ou la fréquence) de la catégorie", "Le nombre de catégories", "La moyenne"], "L'effectif (ou la fréquence) de la catégorie", "Plus la barre est haute, plus la catégorie est représentée."),
  N("Dans un diagramme circulaire, une catégorie occupe un quart du disque. Quel pourcentage représente-t-elle ?", 25, "Un quart correspond à 25 %, soit un angle de 90°."),
  N("Un diagramme en barres indique : rouge 6 élèves, bleu 9 élèves, vert 5 élèves. Combien d'élèves ont été interrogés ?", 20, "6 + 9 + 5 = 20 élèves."),
]),
notion('M33', 5, I, 'm-donnees-comparer-series', [
  Q("Deux classes ont la même moyenne de 12. Dans la classe A, les notes vont de 10 à 14 ; dans la classe B, de 4 à 19. Que peut-on dire ?", ["Les deux classes sont identiques", "Les notes de la classe B sont plus dispersées", "La classe A a de meilleures notes", "La classe B a une meilleure moyenne"], "Les notes de la classe B sont plus dispersées", "La moyenne ne suffit pas : l'étendue (4 contre 15) mesure la dispersion."),
  N("Série A : 8, 10, 12. Série B : 2, 10, 18. Quelle est la différence entre l'étendue de B et celle de A ?", 12, "Étendue de A : 12 − 8 = 4 ; étendue de B : 18 − 2 = 16 ; différence : 12."),
  Q("Pour comparer deux séries de notes, quels indicateurs utiliser ensemble ?", ["Seulement la note maximale", "Un indicateur de position (moyenne ou médiane) et un indicateur de dispersion (étendue)", "Seulement l'effectif", "Seulement la première note"], "Un indicateur de position (moyenne ou médiane) et un indicateur de dispersion (étendue)", "Position et dispersion se complètent pour décrire une série."),
]),
# ── Proportionnalité, fonctions ──
notion('M39', 1, I, 'm-prop-ratio', [
  Q("Dans une classe, il y a 12 filles et 8 garçons. Quel est le ratio filles : garçons sous sa forme la plus simple ?", ["12 : 8", "3 : 2", "2 : 3", "4 : 3"], "3 : 2", "12 : 8 se simplifie en divisant par 4 : 3 : 2."),
  N("Une boisson se prépare avec un ratio sirop : eau de 1 : 5. Combien de cL d'eau faut-il pour 4 cL de sirop ?", 20, "Pour 1 cL de sirop, 5 cL d'eau : 4 × 5 = 20 cL."),
  N("On partage 60 € entre deux personnes selon le ratio 2 : 3. Combien reçoit la personne qui a la plus grande part (en €) ?", 36, "60 ÷ (2 + 3) = 12 € par part ; 3 × 12 = 36 €."),
]),
notion('M41', 2, D, 'm-prop-fonction-lineaire', [
  Q("Laquelle de ces fonctions est linéaire ?", ["f(x) = 3x", "f(x) = 3x + 2", "f(x) = x²", "f(x) = 3"], "f(x) = 3x", "Une fonction linéaire est de la forme f(x) = ax : elle traduit une situation de proportionnalité."),
  N("f est linéaire et f(4) = 12. Quel est son coefficient a ?", 3, "a = f(4) ÷ 4 = 12 ÷ 4 = 3, donc f(x) = 3x."),
  Q("Comment est représentée graphiquement une fonction linéaire ?", ["Par une droite passant par l'origine", "Par une droite qui ne passe pas par l'origine", "Par une parabole", "Par une courbe en escalier"], "Par une droite passant par l'origine", "f(0) = 0 : la droite passe par l'origine du repère."),
]),
]

from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('T-2', 2, D, 'tec-trace-programme', [
  N("a = 3, b = 5. On exécute : « mettre a à a + b », « mettre b à a − b », « mettre a à a − b ». Que vaut a ?", 5, "a = 8 ; b = 8 − 5 = 3 ; a = 8 − 3 = 5 : les valeurs de a et b ont été échangées."),
  N("n = 0. « Répéter 4 fois : ajouter 1 à i ; ajouter i à n », avec i = 0 au départ. Que vaut n ?", 10, "n = 1 + 2 + 3 + 4 = 10."),
  N("Que vaut p après : p = 1, puis « répéter 5 fois : mettre p à p × 2 » ?", 32, "p double 5 fois : 2⁵ = 32."),
  N("x = 100. « Répéter jusqu'à ce que x < 10 : mettre x à x / 2 ». Que vaut x à la fin ?", 6.25, "100 → 50 → 25 → 12,5 → 6,25."),
]),
notion('T-2', 2, D, 'tec-conditions-imbriquees', [
  Q("« Si température > 25 alors ouvrir fenêtre ; sinon si température < 18 alors chauffer ; sinon ne rien faire. » Il fait 20 °C. Que se passe-t-il ?", ["La fenêtre s'ouvre", "Le chauffage s'allume", "Rien ne se passe", "Les deux actions"], "Rien ne se passe", "20 n'est ni > 25 ni < 18."),
  Q("« Si (A ou B) et non C alors allumer. » A est vrai, B est faux, C est vrai. La lampe…", ["s'allume", "reste éteinte", "clignote", "on ne peut pas savoir"], "reste éteinte", "(A ou B) est vrai, mais « non C » est faux : la conjonction est fausse."),
  N("Un programme note : si score ≥ 15 alors 3 étoiles, sinon si score ≥ 10 alors 2 étoiles, sinon 1 étoile. Combien d'étoiles pour un score de 15 ?", 3, "15 ≥ 15 : la première condition est vraie, on n'examine pas les suivantes."),
]),
notion('T-2', 2, D, 'tec-listes', [
  Q("En programmation, qu'est-ce qu'une liste ?", ["Une seule valeur", "Une structure qui stocke plusieurs valeurs ordonnées sous un même nom", "Un bloc d'événement", "Un capteur"], "Une structure qui stocke plusieurs valeurs ordonnées sous un même nom", "Dans Scratch, on peut ajouter, supprimer ou lire l'élément n d'une liste."),
  N("La liste L contient [4, 7, 2, 9]. Que vaut l'élément 3 de L (numérotation à partir de 1, comme dans Scratch) ?", 2, "Élément 1 : 4 ; élément 2 : 7 ; élément 3 : 2."),
  N("On parcourt la liste [4, 7, 2, 9] en ajoutant chaque élément à une variable somme initialisée à 0. Que vaut somme ?", 22, "4 + 7 + 2 + 9 = 22."),
]),
notion('T-2', 0, D, 'tec-couple-vitesse', [
  Q("Dans un réducteur de vitesse, si la vitesse de sortie diminue, le couple (la force de rotation)…", ["diminue aussi", "augmente", "reste nul", "ne change jamais"], "augmente", "En négligeant les pertes, la puissance se conserve : moins de vitesse, plus de couple."),
  N("Un moteur tourne à 3 000 tr/min. Un réducteur de rapport 1/50 est placé en sortie. À combien de tours par minute tourne l'axe de sortie ?", 60, "3 000 / 50 = 60 tr/min."),
  N("Un engrenage à trois roues : A (20 dents) entraîne B (40 dents) qui entraîne C (10 dents). A fait 1 tour. Combien de tours fait C ?", 2, "La roue intermédiaire ne modifie pas le rapport global : 20 / 10 = 2 tours."),
]),
notion('T-2', 0, D, 'tec-energie-systeme', [
  N("Un moteur reçoit 50 W et fournit 40 W de puissance mécanique. Quel est son rendement (en %) ?", 80, "40 / 50 = 0,8 = 80 %."),
  N("Une batterie de 3,7 V a une capacité de 4 Ah. Quelle énergie (en Wh) stocke-t-elle ?", 14.8, "E = U × Q = 3,7 × 4 = 14,8 Wh."),
  N("Une ampoule LED de 8 W remplace une ampoule de 60 W et fonctionne 1 000 h. Combien de kWh économise-t-on ?", 52, "(60 − 8) × 1 000 = 52 000 Wh = 52 kWh."),
]),
notion('T-2', 0, D, 'tec-reseaux-structure', [
  Q("Qu'est-ce qu'une adresse IPv4 ?", ["Un nombre de 4 octets, noté par exemple 192.168.1.10", "Une adresse de courriel", "Un nom de domaine", "Un numéro de téléphone"], "Un nombre de 4 octets, noté par exemple 192.168.1.10", "IPv6, sur 16 octets, permet beaucoup plus d'adresses."),
  N("Combien d'adresses IPv4 différentes existe-t-il au maximum (en milliards, arrondi à l'unité) ?", 4, "2³² ≈ 4,3 milliards : c'est pourquoi on est passé à IPv6."),
  Q("Quel est le rôle d'un routeur ?", ["Stocker des fichiers", "Acheminer les paquets de données entre différents réseaux", "Afficher des pages web", "Imprimer"], "Acheminer les paquets de données entre différents réseaux", "Le commutateur (switch), lui, relie des appareils au sein d'un même réseau local."),
]),
notion('T-1', 1, D, 'tec-donnees-algorithmes', [
  Q("Qu'est-ce que le RGPD ?", ["Un logiciel de sécurité", "Le règlement européen sur la protection des données personnelles, appliqué depuis 2018", "Un réseau social", "Une norme électrique"], "Le règlement européen sur la protection des données personnelles, appliqué depuis 2018", "Il impose notamment le consentement et le droit d'accès et d'effacement."),
  Q("En France, à partir de quel âge un mineur peut-il consentir seul au traitement de ses données par un réseau social ?", ["10 ans", "15 ans", "18 ans", "13 ans"], "15 ans", "La France a fixé cet âge à 15 ans ; en dessous, l'accord des parents est requis."),
  Q("Qu'est-ce qu'une « bulle de filtre » ?", ["Un filtre à eau", "L'enfermement d'un utilisateur dans des contenus proches de ses goûts, sélectionnés par des algorithmes", "Un antivirus", "Un réseau privé"], "L'enfermement d'un utilisateur dans des contenus proches de ses goûts, sélectionnés par des algorithmes", "Elle réduit la diversité des informations reçues."),
]),
notion('T-1', 2, D, 'tec-choix-materiaux-multicriteres', [
  Q("Pour un cadre de vélo de course, quel matériau offre le meilleur rapport rigidité/masse ?", ["L'acier", "La fibre de carbone (composite)", "Le bois massif", "Le PVC"], "La fibre de carbone (composite)", "Elle est très légère et rigide, mais coûteuse et difficile à recycler."),
  Q("Pourquoi les bouteilles d'eau sont-elles souvent en PET plutôt qu'en verre ?", ["Le PET est plus écologique dans tous les cas", "Le PET est léger et incassable, ce qui réduit le coût du transport", "Le verre est toxique", "Le PET se recycle à l'infini"], "Le PET est léger et incassable, ce qui réduit le coût du transport", "Le verre, lui, est réutilisable et se recycle sans perte de qualité : chaque choix a ses compromis."),
  Q("Pourquoi faut-il tenir compte de la fin de vie lors du choix d'un matériau ?", ["Ce n'est pas utile", "Parce que certains matériaux, comme les composites, sont difficiles à séparer et à recycler", "Parce que tous se recyclent pareil", "Pour augmenter le prix"], "Parce que certains matériaux, comme les composites, sont difficiles à séparer et à recycler", "L'éco-conception anticipe le démontage et le recyclage."),
]),
notion('T-3', 2, D, 'tec-algorithmes-classiques', [
  Q("Quel est l'intérêt de la recherche dichotomique dans une liste triée ?", ["Elle est plus lente", "Elle divise par deux l'espace de recherche à chaque étape", "Elle fonctionne sur une liste non triée", "Elle trie la liste"], "Elle divise par deux l'espace de recherche à chaque étape", "Pour 1 000 éléments, une dizaine d'étapes suffisent."),
  N("Avec une recherche dichotomique, combien d'étapes au maximum pour trouver un nombre entre 1 et 1 024 ?", 10, "2¹⁰ = 1 024 : 10 divisions par deux suffisent."),
  Q("Dans le jeu « devine le nombre » entre 1 et 100, quelle première proposition est la plus efficace ?", ["1", "50", "100", "Un nombre au hasard"], "50", "Proposer le milieu élimine la moitié des possibilités, quelle que soit la réponse."),
]),
notion('T-3', 2, D, 'tec-python', [
  Q("En Python, que fait l'instruction for i in range(5): ?", ["Elle répète le bloc 5 fois, avec i allant de 0 à 4", "Elle répète le bloc 4 fois", "Elle affiche 5", "Elle crée une liste de 5 zéros"], "Elle répète le bloc 5 fois, avec i allant de 0 à 4", "range(5) produit 0, 1, 2, 3, 4."),
  N("Que vaut s après : s = 0, puis for i in range(1, 4): s = s + i ?", 6, "range(1, 4) donne 1, 2, 3 ; s = 1 + 2 + 3 = 6."),
  Q("En Python, que fait l'instruction if x % 2 == 0: ?", ["Elle teste si x est pair", "Elle divise x par 2", "Elle teste si x vaut 2", "Elle multiplie x par 2"], "Elle teste si x est pair", "% donne le reste de la division euclidienne : un reste nul par 2 signifie que x est pair."),
  Q("En Python, quel symbole teste l'égalité de deux valeurs ?", ["=", "==", "!=", ":="], "==", "Le signe = affecte une valeur à une variable ; == compare."),
]),
notion('T-3', 1, D, 'tec-tests-statistiques', [
  N("Trois essais de résistance donnent 12 kg, 14 kg et 13 kg. Quelle est la charge moyenne supportée (en kg) ?", 13, "(12 + 14 + 13) / 3 = 13 kg."),
  Q("Un prototype doit supporter 10 kg avec un coefficient de sécurité de 2. Quelle charge doit-il supporter lors du test ?", ["5 kg", "10 kg", "20 kg", "12 kg"], "20 kg", "Le coefficient de sécurité multiplie la charge prévue pour tenir compte des incertitudes."),
  Q("Pourquoi ne modifier qu'un seul paramètre à la fois lors d'une série d'essais ?", ["Pour aller plus vite", "Pour savoir quel paramètre est responsable de l'effet observé", "Parce que c'est plus joli", "Ce n'est pas nécessaire"], "Pour savoir quel paramètre est responsable de l'effet observé", "C'est le principe de la démarche expérimentale."),
]),
notion('T-1', 0, D, 'tec-innovation-rupture', [
  Q("Qu'est-ce qu'une innovation de rupture ?", ["Une petite amélioration d'un produit", "Une innovation qui transforme profondément un marché ou des usages", "Une panne", "Un objet cassé"], "Une innovation qui transforme profondément un marché ou des usages", "Le smartphone a fait disparaître ou transformé de nombreux objets (appareil photo, GPS, baladeur)."),
  Q("Qu'est-ce qu'une innovation incrémentale ?", ["Une invention totalement nouvelle", "Une amélioration progressive d'un produit existant", "Un brevet refusé", "Un recyclage"], "Une amélioration progressive d'un produit existant", "Chaque nouvelle génération de téléphone apporte des améliorations incrémentales."),
  Q("Quelle condition est nécessaire pour qu'une invention devienne une innovation ?", ["Qu'elle soit brevetée", "Qu'elle soit adoptée par des utilisateurs", "Qu'elle soit chère", "Qu'elle soit inventée par un ingénieur"], "Qu'elle soit adoptée par des utilisateurs", "Beaucoup d'inventions n'ont jamais trouvé leur marché."),
]),
notion('T-2', 1, D, 'tec-diagnostic-avance', [
  Q("Un capteur de température affiche toujours 0 °C quelle que soit la température. Quelle hypothèse est la plus probable ?", ["Le programme est parfait", "Le capteur est mal branché ou défectueux", "Il fait toujours 0 °C", "L'écran est trop grand"], "Le capteur est mal branché ou défectueux", "Une valeur figée signale souvent un problème de câblage ou de capteur."),
  Q("Un robot tourne toujours à droite au lieu d'avancer droit. Quelle cause est plausible ?", ["Les deux moteurs tournent à la même vitesse", "Un moteur tourne moins vite que l'autre ou un ordre est inversé", "La batterie est pleine", "Le robot est neuf"], "Un moteur tourne moins vite que l'autre ou un ordre est inversé", "On teste chaque moteur séparément pour isoler le défaut."),
  Q("Quelle démarche suivre pour un dysfonctionnement ?", ["Remplacer toutes les pièces", "Observer, formuler une hypothèse, tester, conclure, réparer", "Recommencer le projet", "Ignorer le problème"], "Observer, formuler une hypothèse, tester, conclure, réparer", "C'est une démarche d'investigation appliquée à la technique."),
]),
notion('T-2', 0, D, 'tec-compression', [
  Q("Qu'est-ce que la compression d'un fichier ?", ["L'effacer", "Réduire sa taille en codant l'information plus efficacement", "L'imprimer", "Le chiffrer obligatoirement"], "Réduire sa taille en codant l'information plus efficacement", "Le format ZIP compresse sans perte ; le JPEG ou le MP3, avec perte."),
  Q("Qu'est-ce qu'une compression avec perte ?", ["Une compression qui ne réduit pas la taille", "Une compression qui supprime des informations jugées peu perceptibles", "Une compression qui efface le fichier", "Une compression réversible à l'identique"], "Une compression qui supprime des informations jugées peu perceptibles", "Le fichier d'origine ne peut pas être retrouvé exactement."),
  N("Un fichier de 12 Mo est compressé avec un taux de 75 % de réduction. Quelle est sa nouvelle taille (en Mo) ?", 3, "12 × (1 − 0,75) = 3 Mo."),
]),
notion('T-3', 0, D, 'tec-normes-securite', [
  Q("Pourquoi les objets techniques doivent-ils respecter des normes ?", ["Pour augmenter leur prix", "Pour garantir sécurité, compatibilité et qualité", "Pour les rendre identiques", "Pour empêcher l'innovation"], "Pour garantir sécurité, compatibilité et qualité", "Les normes (NF, ISO, EN) facilitent aussi les échanges."),
  Q("Quel exemple illustre l'intérêt de la normalisation ?", ["Les prises USB-C, qui permettent d'utiliser un même chargeur pour de nombreux appareils", "Les couleurs des objets", "Les noms de marques", "Les publicités"], "Les prises USB-C, qui permettent d'utiliser un même chargeur pour de nombreux appareils", "L'Union européenne impose l'USB-C comme chargeur commun depuis fin 2024."),
  Q("Qu'est-ce que l'accessibilité numérique (RGAA en France) ?", ["Le prix d'un abonnement", "L'ensemble des règles pour que les sites soient utilisables par les personnes en situation de handicap", "La vitesse d'Internet", "La sécurité des mots de passe"], "L'ensemble des règles pour que les sites soient utilisables par les personnes en situation de handicap", "Textes alternatifs pour les images, contrastes, navigation au clavier…"),
]),
notion('T-2', 2, D, 'tec-chiffrement', [
  Q("À quoi sert le chiffrement des données ?", ["À les compresser", "À les rendre illisibles pour toute personne qui ne possède pas la clé", "À les effacer", "À les accélérer"], "À les rendre illisibles pour toute personne qui ne possède pas la clé", "Le cadenas « https » indique une connexion chiffrée."),
  Q("Avec le chiffrement de César de décalage 3, comment s'écrit « ABC » ?", ["BCD", "DEF", "XYZ", "CBA"], "DEF", "Chaque lettre est décalée de 3 rangs dans l'alphabet."),
  Q("Que signifie le « s » de « https » ?", ["Simple", "Sécurisé (connexion chiffrée)", "Serveur", "Site"], "Sécurisé (connexion chiffrée)", "Il garantit que les échanges entre le navigateur et le site sont chiffrés."),
]),
]

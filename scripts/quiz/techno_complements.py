# Technologie : notions ajoutées pour couvrir chaque sous-thème du programme en quatre thèmes (au moins 15 questions)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── Design, innovation et créativité · Réaliser le prototype d'un objet communicant ──
notion('DI-2', 0, I, 'tec-prototypage', [
  Q("Qu'est-ce qu'un prototype ?", ["Un premier exemplaire d'un objet, réalisé pour tester et valider une solution", "L'objet vendu en magasin", "Le mode d'emploi d'un objet", "Un brevet"], "Un premier exemplaire d'un objet, réalisé pour tester et valider une solution", "Le prototype permet de vérifier que la solution répond au cahier des charges."),
  Q("Quelle machine fabrique un objet en déposant de la matière couche par couche ?", ["Une imprimante 3D", "Une perceuse", "Une scie à ruban", "Une plieuse"], "Une imprimante 3D", "On parle de fabrication additive, très utilisée pour le prototypage rapide."),
  Q("Quel type de carte est souvent utilisé au collège pour prototyper un objet communicant ?", ["Une carte programmable à microcontrôleur (micro:bit, Arduino…)", "Une carte bancaire", "Une carte routière", "Une carte mère d'ordinateur portable"], "Une carte programmable à microcontrôleur (micro:bit, Arduino…)", "On y branche capteurs et actionneurs, puis on la programme."),
]),
# ── Les objets techniques et la société · Exprimer sa pensée à l'aide d'outils de description adaptés ──
notion('OT-2', 0, F, 'tec-carte-mentale', [
  Q("Comment appelle-t-on un schéma qui organise des idées autour d'un thème central ?", ["Une carte heuristique (ou carte mentale)", "Un plan de masse", "Un diagramme circulaire", "Une nomenclature"], "Une carte heuristique (ou carte mentale)", "Elle aide à chercher et à organiser des idées en projet."),
  Q("Comment appelle-t-on la représentation graphique des étapes d'un algorithme ?", ["Un algorigramme (ou logigramme)", "Un croquis", "Une perspective", "Une cotation"], "Un algorigramme (ou logigramme)", "Chaque forme a un rôle : début et fin, action, condition."),
  Q("Dans un algorigramme, quelle forme représente une condition (un test) ?", ["Un losange", "Un rectangle", "Un ovale", "Une flèche"], "Un losange", "Le losange a deux sorties : « oui » et « non »."),
]),
notion('OT-2', 0, I, 'tec-dessin-technique', [
  Q("Comment appelle-t-on la représentation d'un objet en trois dimensions réalisée avec un logiciel ?", ["Une modélisation volumique (ou 3D)", "Un croquis à main levée", "Une nomenclature", "Un organigramme"], "Une modélisation volumique (ou 3D)", "Elle est réalisée avec un logiciel de CAO."),
  Q("Qu'est-ce qu'une perspective en dessin technique ?", ["Une représentation qui donne une impression de volume", "Une vue de face uniquement", "La liste des pièces", "Un schéma électrique"], "Une représentation qui donne une impression de volume", "Les vues de face, de dessus et de côté, elles, sont planes."),
  Q("Pourquoi utiliser des symboles normalisés sur un schéma électrique ?", ["Pour que le schéma soit compris par tous de la même façon", "Pour décorer le schéma", "Pour le rendre plus long", "Parce que c'est plus rapide à dessiner que tout autre symbole"], "Pour que le schéma soit compris par tous de la même façon", "La normalisation est un langage commun aux techniciens."),
]),
# ── La modélisation et la simulation · Utiliser une modélisation et simuler le comportement d'un objet ──
notion('MS-3', 0, I, 'tec-cao-modele', [
  Q("Que signifie le sigle CAO ?", ["Conception assistée par ordinateur", "Commande automatique d'objets", "Calcul approché d'ondes", "Centre d'analyse des objets"], "Conception assistée par ordinateur", "La CAO permet de concevoir et de visualiser un objet avant de le fabriquer."),
  Q("Quel est l'intérêt de simuler le comportement d'un objet avant de le fabriquer ?", ["Tester virtuellement des solutions et éviter des prototypes coûteux", "Supprimer toute phase de test réel", "Rendre l'objet plus beau", "Raccourcir son mode d'emploi"], "Tester virtuellement des solutions et éviter des prototypes coûteux", "La simulation ne remplace pas totalement les essais sur le prototype."),
  Q("Comment appelle-t-on une représentation simplifiée d'un objet réel, utilisée pour l'étudier ?", ["Un modèle", "Un brevet", "Un cahier des charges", "Une notice"], "Un modèle", "Un modèle ne garde que ce qui est utile à l'étude."),
]),
notion('MS-3', 1, D, 'tec-ecarts', [
  Q("Une simulation prévoit qu'une passerelle supporte 50 kg, mais le prototype cède à 42 kg. Que faut-il faire ?", ["Analyser l'écart, puis corriger le modèle ou la conception", "Ignorer l'essai réel", "Conclure que la simulation est toujours exacte", "Abandonner le projet"], "Analyser l'écart, puis corriger le modèle ou la conception", "Comparer simulation, mesure et cahier des charges fait partie de la démarche."),
  Q("Pourquoi les résultats d'une simulation diffèrent-ils parfois de la réalité ?", ["Parce que le modèle simplifie la réalité", "Parce que les ordinateurs se trompent toujours", "Parce que la réalité ne respecte pas les lois physiques", "Ils ne diffèrent jamais"], "Parce que le modèle simplifie la réalité", "Matériaux, frottements ou défauts de fabrication ne sont pas toujours modélisés."),
  N("Le cahier des charges exige 10 minutes d'autonomie ; le prototype en tient 8. Quel est l'écart en pourcentage par rapport à l'exigence ?", 20, "(10 − 8) ÷ 10 = 0,2, soit 20 %."),
]),
# ── L'informatique et la programmation · Comprendre le fonctionnement d'un réseau informatique ──
notion('IP-1', 0, F, 'tec-reseau-local', [
  Q("Comment appelle-t-on un réseau limité à un bâtiment, comme celui du collège ?", ["Un réseau local (LAN)", "Internet", "Un réseau satellite", "Un réseau électrique"], "Un réseau local (LAN)", "Il relie ordinateurs, imprimantes et serveurs d'un même lieu."),
  Q("Quel appareil, à la maison, relie les équipements au réseau local et donne accès à Internet ?", ["La box (routeur)", "L'écran", "Le clavier", "L'imprimante"], "La box (routeur)", "Elle aiguille les données entre le réseau local et Internet."),
  Q("Qu'est-ce qu'une adresse IP ?", ["Un numéro qui identifie un appareil sur un réseau", "Un mot de passe", "L'adresse postale du fournisseur d'accès", "Le nom d'un site web"], "Un numéro qui identifie un appareil sur un réseau", "Les données circulent d'une adresse IP à une autre."),
]),
notion('IP-1', 2, I, 'tec-sobriete-numerique', [
  Q("Qu'est-ce qu'un centre de données (data center) ?", ["Un bâtiment rempli de serveurs qui stockent et traitent des données", "Une bibliothèque municipale", "Un magasin d'informatique", "Un logiciel de traitement de texte"], "Un bâtiment rempli de serveurs qui stockent et traitent des données", "Nos photos, vidéos et messages en ligne y sont stockés."),
  Q("Pourquoi les centres de données consomment-ils beaucoup d'électricité ?", ["Pour faire fonctionner les serveurs et les refroidir en permanence", "Pour éclairer les bureaux", "Pour charger les téléphones des visiteurs", "Ils n'en consomment presque pas"], "Pour faire fonctionner les serveurs et les refroidir en permanence", "Les serveurs fonctionnent jour et nuit."),
  Q("Quel geste réduit l'impact environnemental de nos données ?", ["Supprimer les fichiers inutiles et limiter les vidéos en haute définition", "Envoyer davantage de pièces jointes", "Stocker plusieurs copies de chaque photo en ligne", "Laisser tourner les vidéos en arrière-plan"], "Supprimer les fichiers inutiles et limiter les vidéos en haute définition", "C'est une démarche de sobriété numérique."),
]),
]

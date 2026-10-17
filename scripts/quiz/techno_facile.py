from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('T-1', 0, F, 'tec-objet-technique', [
  Q("Qu'est-ce qu'un objet technique ?", ["Un objet présent dans la nature", "Un objet fabriqué par l'être humain pour répondre à un besoin", "Un objet uniquement électronique", "Une œuvre d'art"], "Un objet fabriqué par l'être humain pour répondre à un besoin", "Un caillou est un objet naturel ; un marteau est un objet technique."),
  Q("Lequel de ces objets est un objet technique ?", ["Une pomme de pin", "Un tire-bouchon", "Un galet", "Une coquille"], "Un tire-bouchon", "Il a été conçu et fabriqué pour une fonction précise."),
  Q("À quelle question répond l'étude du besoin d'un objet ?", ["De quelle couleur est-il ?", "À qui rend-il service, sur quoi agit-il, dans quel but ?", "Combien pèse-t-il ?", "Où a-t-il été acheté ?"], "À qui rend-il service, sur quoi agit-il, dans quel but ?", "C'est le « diagramme bête à cornes » utilisé en technologie."),
]),
notion('T-1', 0, F, 'tec-fonction-usage', [
  Q("Qu'est-ce que la fonction d'usage d'un objet ?", ["Sa couleur", "Ce à quoi il sert", "Son prix", "Sa matière"], "Ce à quoi il sert", "La fonction d'usage d'un parapluie : protéger de la pluie."),
  Q("Quelle est la fonction d'usage d'une lampe de poche ?", ["Chauffer", "Éclairer", "Mesurer", "Couper"], "Éclairer", "Une fonction d'usage s'exprime par un verbe à l'infinitif."),
  Q("Qu'est-ce que la fonction d'estime d'un objet ?", ["Ce qui le rend agréable ou attractif (forme, couleur, marque)", "Son usage principal", "Son mode de fabrication", "Sa durée de vie"], "Ce qui le rend agréable ou attractif (forme, couleur, marque)", "Deux montres ont la même fonction d'usage mais des fonctions d'estime différentes."),
]),
notion('T-1', 0, F, 'tec-evolution-objets', [
  Q("Comment appelle-t-on l'ensemble des objets qui, au cours du temps, répondent au même besoin ?", ["Une famille d'objets", "Une lignée d'objets", "Une marque", "Un brevet"], "Une lignée d'objets", "La lignée des objets pour s'éclairer : torche, lampe à huile, bougie, ampoule, LED."),
  Q("Quel objet est apparu le plus récemment dans la lignée des objets pour écrire ?", ["La plume d'oie", "Le stylo à bille", "Le calame", "La tablette numérique avec stylet"], "La tablette numérique avec stylet", "Le stylo à bille se répand au milieu du XXe siècle ; les tablettes, au XXIe siècle."),
  Q("Qu'est-ce qui pousse le plus souvent un objet à évoluer ?", ["Le hasard", "De nouveaux besoins, de nouvelles techniques et de nouveaux matériaux", "La météo", "Rien, les objets ne changent pas"], "De nouveaux besoins, de nouvelles techniques et de nouveaux matériaux", "Les progrès techniques et les attentes des utilisateurs font évoluer les objets."),
]),
notion('T-1', 0, F, 'tec-inventions', [
  Q("Qui a inventé l'imprimerie à caractères mobiles en Europe vers 1450 ?", ["Gutenberg", "Edison", "Watt", "Pascal"], "Gutenberg", "L'imprimerie a permis une diffusion massive des livres."),
  Q("Quelle invention de James Watt améliore la machine à vapeur au XVIIIe siècle ?", ["Le condenseur séparé", "L'ampoule", "Le téléphone", "Le moteur électrique"], "Le condenseur séparé", "Elle rend la machine à vapeur beaucoup plus efficace, moteur de la révolution industrielle."),
  Q("Quel ingénieur français invente au XIXe siècle un système d'écriture en relief pour les personnes aveugles ?", ["Louis Braille", "Louis Pasteur", "Gustave Eiffel", "Blaise Pascal"], "Louis Braille", "L'alphabet braille, créé par Louis Braille, utilise des combinaisons de 6 points."),
]),
notion('T-1', 1, F, 'tec-impact-environnement', [
  Q("Qu'est-ce que le cycle de vie d'un objet ?", ["Sa durée de garantie", "Les étapes de sa vie : extraction des matières, fabrication, transport, utilisation, fin de vie", "Le nombre de ses propriétaires", "Sa date d'invention"], "Les étapes de sa vie : extraction des matières, fabrication, transport, utilisation, fin de vie", "Chaque étape a un impact sur l'environnement."),
  Q("Qu'est-ce que l'obsolescence programmée ?", ["Une réparation gratuite", "La réduction volontaire de la durée de vie d'un produit pour en augmenter le renouvellement", "Un type de recyclage", "Une garantie à vie"], "La réduction volontaire de la durée de vie d'un produit pour en augmenter le renouvellement", "Elle est interdite en France depuis 2015 (loi sur la transition énergétique)."),
  Q("À quelle étape un smartphone a-t-il le plus d'impact environnemental ?", ["Son utilisation", "Sa fabrication", "Son emballage", "Sa publicité"], "Sa fabrication", "L'extraction des métaux et la fabrication représentent l'essentiel de son empreinte : il vaut mieux le garder longtemps."),
]),
notion('T-1', 1, F, 'tec-indice-reparabilite', [
  Q("Que mesure l'indice de réparabilité affiché sur certains appareils en France ?", ["Le prix", "La facilité à réparer l'appareil", "La consommation d'énergie", "La vitesse"], "La facilité à réparer l'appareil", "Il est noté sur 10 et obligatoire depuis 2021 pour plusieurs catégories de produits."),
  Q("Qu'est-ce qu'un repair café ?", ["Un café vendu en magasin", "Un lieu où des bénévoles aident à réparer gratuitement ses objets", "Une marque d'électroménager", "Un service après-vente payant"], "Un lieu où des bénévoles aident à réparer gratuitement ses objets", "Réparer prolonge la durée de vie des objets."),
  Q("Que signifie l'étiquette énergie A à G sur un appareil électroménager ?", ["Sa couleur", "Son niveau de consommation d'énergie", "Son pays de fabrication", "Sa taille"], "Son niveau de consommation d'énergie", "La classe A correspond aux appareils les plus économes."),
]),
notion('T-1', 2, F, 'tec-materiaux-familles', [
  Q("À quelle famille de matériaux appartient l'aluminium ?", ["Les matériaux organiques", "Les métaux", "Les céramiques", "Les plastiques"], "Les métaux", "On distingue métaux, matériaux organiques (bois, plastiques), céramiques (verre, terre cuite) et composites."),
  Q("À quelle famille de matériaux appartient le bois ?", ["Les métaux", "Les matériaux organiques d'origine naturelle", "Les céramiques", "Les composites"], "Les matériaux organiques d'origine naturelle", "Le bois provient des arbres ; c'est une ressource renouvelable."),
  Q("Qu'est-ce qu'un matériau composite ?", ["Un matériau pur", "L'assemblage de plusieurs matériaux pour combiner leurs propriétés", "Un métal recyclé", "Un plastique coloré"], "L'assemblage de plusieurs matériaux pour combiner leurs propriétés", "La fibre de carbone ou le béton armé sont des composites."),
]),
notion('T-1', 2, F, 'tec-proprietes-materiaux', [
  Q("Quelle propriété est recherchée pour la poignée d'une casserole ?", ["Bon conducteur thermique", "Isolant thermique", "Magnétique", "Transparent"], "Isolant thermique", "La poignée ne doit pas chauffer pour éviter les brûlures."),
  Q("Pourquoi les fils électriques sont-ils en cuivre ?", ["Le cuivre est un bon conducteur électrique", "Le cuivre est transparent", "Le cuivre est isolant", "Le cuivre est le moins cher des métaux"], "Le cuivre est un bon conducteur électrique", "Le cuivre conduit très bien le courant et se plie facilement."),
  Q("Quel matériau choisir pour une vitre ?", ["L'acier", "Le verre (transparent)", "Le bois", "Le béton"], "Le verre (transparent)", "La transparence est ici le critère essentiel."),
]),
notion('T-1', 2, F, 'tec-cahier-charges', [
  Q("Qu'est-ce qu'un cahier des charges ?", ["Un cahier de brouillon", "Un document qui précise les besoins et les contraintes auxquels doit répondre un objet", "Le mode d'emploi", "Une facture"], "Un document qui précise les besoins et les contraintes auxquels doit répondre un objet", "Il sert de référence pour concevoir puis valider l'objet."),
  Q("Qu'est-ce qu'une contrainte dans un cahier des charges ?", ["Une couleur préférée", "Une exigence que la solution doit respecter (coût, masse, sécurité…)", "Le nom du fabricant", "Un défaut"], "Une exigence que la solution doit respecter (coût, masse, sécurité…)", "Par exemple : « l'objet doit peser moins de 200 g »."),
  Q("Qu'est-ce qu'un critère d'appréciation ?", ["Un avis personnel", "Une caractéristique mesurable permettant de vérifier qu'une fonction est remplie", "Un dessin", "Une publicité"], "Une caractéristique mesurable permettant de vérifier qu'une fonction est remplie", "Un critère s'accompagne d'un niveau (une valeur à atteindre)."),
]),
notion('T-2', 0, F, 'tec-chaine-energie', [
  Q("Quelles sont les fonctions de la chaîne d'énergie d'un objet ?", ["Acquérir, traiter, communiquer", "Alimenter, distribuer, convertir, transmettre", "Dessiner, fabriquer, vendre", "Mesurer, peser, compter"], "Alimenter, distribuer, convertir, transmettre", "La chaîne d'énergie produit l'action (mouvement, lumière, chaleur…)."),
  Q("Dans un ventilateur, quel élément convertit l'énergie électrique en énergie mécanique ?", ["La prise", "Le moteur", "L'interrupteur", "Les pales"], "Le moteur", "Le moteur assure la fonction « convertir »."),
  Q("Dans une lampe de poche, quel élément assure la fonction « alimenter » ?", ["L'ampoule", "Les piles", "L'interrupteur", "Le boîtier"], "Les piles", "L'interrupteur assure la fonction « distribuer »."),
]),
notion('T-2', 0, F, 'tec-chaine-information', [
  Q("Quelles sont les fonctions de la chaîne d'information ?", ["Alimenter, distribuer, convertir", "Acquérir, traiter, communiquer", "Couper, plier, coller", "Chauffer, refroidir"], "Acquérir, traiter, communiquer", "Les capteurs acquièrent, le microcontrôleur traite, l'information est ensuite transmise."),
  Q("Quel composant acquiert une information dans un objet technique ?", ["Un moteur", "Un capteur", "Une pile", "Un engrenage"], "Un capteur", "Capteur de température, de lumière, de présence…"),
  Q("Quel composant traite les informations dans un robot programmable ?", ["Le capteur", "Le microcontrôleur (carte programmable)", "La batterie", "La roue"], "Le microcontrôleur (carte programmable)", "Il exécute le programme et décide des actions."),
]),
notion('T-2', 0, F, 'tec-capteurs', [
  Q("Quel capteur déclenche l'éclairage automatique d'un couloir au passage d'une personne ?", ["Un capteur de température", "Un détecteur de présence (infrarouge)", "Un capteur d'humidité", "Un micro"], "Un détecteur de présence (infrarouge)", "Il détecte le rayonnement infrarouge du corps humain."),
  Q("Quel capteur permet d'allumer les lampadaires à la tombée de la nuit ?", ["Un capteur de luminosité", "Un capteur de pression", "Un capteur de son", "Un capteur de vitesse"], "Un capteur de luminosité", "Il mesure la lumière ambiante."),
  Q("Quel capteur utilise un thermostat de chauffage ?", ["Un capteur de température", "Un capteur de lumière", "Un capteur de présence", "Un capteur de distance"], "Un capteur de température", "Le thermostat compare la température mesurée à la consigne."),
]),
notion('T-2', 0, F, 'tec-actionneurs', [
  Q("Qu'est-ce qu'un actionneur ?", ["Un élément qui mesure", "Un élément qui agit (moteur, lampe, vérin, haut-parleur)", "Un élément qui stocke des données", "Un logiciel"], "Un élément qui agit (moteur, lampe, vérin, haut-parleur)", "L'actionneur convertit l'énergie pour produire l'action attendue."),
  Q("Lequel de ces éléments est un actionneur ?", ["Un thermomètre", "Un moteur électrique", "Un bouton-poussoir", "Un détecteur de fumée"], "Un moteur électrique", "Le bouton-poussoir et le détecteur sont des capteurs."),
  Q("Dans une alarme, quel élément est l'actionneur ?", ["Le détecteur d'ouverture", "La sirène", "Le clavier", "La carte de commande"], "La sirène", "Elle produit l'action (le son) commandée par la carte."),
]),
notion('T-2', 0, F, 'tec-transmission-mouvement', [
  Q("Quel système transmet un mouvement de rotation entre deux axes éloignés, comme sur un vélo ?", ["Un engrenage seul", "Une chaîne et des pignons", "Un levier", "Une vis"], "Une chaîne et des pignons", "Sur un vélo, la chaîne relie le plateau au pignon de la roue arrière."),
  Q("Qu'est-ce qu'un engrenage ?", ["Deux roues dentées qui s'entraînent", "Une courroie", "Un ressort", "Un câble"], "Deux roues dentées qui s'entraînent", "Deux roues dentées en contact tournent en sens contraires."),
  Q("Deux roues dentées en prise tournent…", ["dans le même sens", "en sens contraires", "sans bouger", "au hasard"], "en sens contraires", "Avec une chaîne ou une courroie, les deux roues tournent dans le même sens."),
]),
notion('T-2', 0, F, 'tec-energie-objets', [
  Q("Quelle énergie stocke la batterie d'un téléphone ?", ["Mécanique", "Chimique", "Nucléaire", "Lumineuse"], "Chimique", "La batterie convertit l'énergie chimique en énergie électrique, et inversement à la recharge."),
  Q("Quelle source d'énergie alimente une calculatrice solaire ?", ["Le vent", "La lumière", "La chaleur du corps", "Le son"], "La lumière", "Une petite cellule photovoltaïque convertit la lumière en électricité."),
  Q("Quelle source d'énergie stocke un ressort de jouet remonté ?", ["Électrique", "Mécanique (énergie élastique)", "Chimique", "Lumineuse"], "Mécanique (énergie élastique)", "En se détendant, le ressort restitue l'énergie et met le jouet en mouvement."),
]),
notion('T-2', 1, F, 'tec-depannage', [
  Q("Une lampe de poche ne s'allume plus. Que vérifier en premier ?", ["La couleur du boîtier", "L'état des piles et de l'ampoule", "Le poids", "La marque"], "L'état des piles et de l'ampoule", "On teste les éléments un par un, du plus probable au moins probable."),
  Q("Comment appelle-t-on une démarche qui consiste à rechercher méthodiquement la cause d'une panne ?", ["Un diagnostic", "Une publicité", "Un brevet", "Une notice"], "Un diagnostic", "Le diagnostic précède la réparation."),
  Q("Quel document aide l'utilisateur à résoudre un problème simple ?", ["La facture", "La notice (rubrique « en cas de problème »)", "Le ticket de caisse", "L'emballage"], "La notice (rubrique « en cas de problème »)", "La notice décrit l'utilisation, l'entretien et les pannes courantes."),
]),
notion('T-2', 2, F, 'tec-algorithme', [
  Q("Qu'est-ce qu'un algorithme ?", ["Un ordinateur", "Une suite finie d'instructions permettant de résoudre un problème", "Un langage secret", "Un composant électronique"], "Une suite finie d'instructions permettant de résoudre un problème", "Une recette de cuisine est un algorithme."),
  Q("Qu'est-ce qu'un programme ?", ["Un algorithme traduit dans un langage compréhensible par une machine", "Un dessin", "Une émission de télévision seulement", "Une pièce mécanique"], "Un algorithme traduit dans un langage compréhensible par une machine", "Scratch, Python sont des langages de programmation."),
  Q("Quel logiciel de programmation par blocs est très utilisé au collège ?", ["Excel", "Scratch", "Word", "Photoshop"], "Scratch", "Scratch permet de programmer en assemblant des blocs."),
]),
notion('T-2', 2, F, 'tec-boucles', [
  Q("Quelle instruction permet de répéter plusieurs fois une même action ?", ["Une condition", "Une boucle", "Une variable", "Un événement"], "Une boucle", "Dans Scratch : « répéter 10 fois » ou « répéter indéfiniment »."),
  N("Un lutin exécute « répéter 4 fois : avancer de 50 pas, tourner de 90° ». Combien de pas parcourt-il au total ?", 200, "4 × 50 = 200 pas : il trace un carré."),
  N("Pour tracer un triangle équilatéral avec « répéter 3 fois : avancer, tourner de … degrés », de combien de degrés le lutin doit-il tourner ?", 120, "L'angle de rotation est 360° / 3 = 120°, l'angle extérieur du triangle."),
]),
notion('T-2', 2, F, 'tec-conditions', [
  Q("Quelle instruction permet d'exécuter une action seulement si une situation est vraie ?", ["Une boucle", "Une condition « si… alors »", "Une variable", "Un compteur"], "Une condition « si… alors »", "Exemple : si le capteur détecte un obstacle, alors le robot s'arrête."),
  Q("Que fait l'instruction « si… alors… sinon » ?", ["Elle répète une action", "Elle exécute une action si la condition est vraie et une autre si elle est fausse", "Elle arrête le programme", "Elle crée une variable"], "Elle exécute une action si la condition est vraie et une autre si elle est fausse", "C'est une structure alternative."),
  Q("Dans un programme d'éclairage automatique, quelle condition est logique ?", ["Si la luminosité est faible, alors allumer la lampe", "Si la lampe est allumée, alors acheter une lampe", "Répéter 10 fois allumer", "Si le soleil brille, alors allumer"], "Si la luminosité est faible, alors allumer la lampe", "La condition porte sur la valeur du capteur."),
]),
notion('T-2', 2, F, 'tec-variables', [
  Q("Qu'est-ce qu'une variable en programmation ?", ["Un bug", "Une « boîte » nommée qui stocke une valeur pouvant changer", "Une boucle", "Un capteur"], "Une « boîte » nommée qui stocke une valeur pouvant changer", "Exemple : une variable « score » augmente à chaque point marqué."),
  N("La variable score vaut 0. On exécute 5 fois « ajouter 2 à score ». Que vaut score ?", 10, "0 + 5 × 2 = 10."),
  N("La variable x vaut 10. On exécute « mettre x à x − 3 » puis « mettre x à x × 2 ». Que vaut x ?", 14, "10 − 3 = 7, puis 7 × 2 = 14."),
]),
notion('T-2', 2, F, 'tec-evenements', [
  Q("Dans Scratch, quel bloc lance un programme quand on clique sur le drapeau vert ?", ["« Répéter indéfiniment »", "« Quand le drapeau vert est cliqué »", "« Si… alors »", "« Attendre 1 seconde »"], "« Quand le drapeau vert est cliqué »", "C'est un bloc événement qui déclenche le script."),
  Q("Qu'est-ce qu'un événement en programmation ?", ["Une erreur", "Une action (clic, touche, message) qui déclenche l'exécution d'un script", "Une variable", "Une boucle infinie"], "Une action (clic, touche, message) qui déclenche l'exécution d'un script", "La programmation événementielle réagit aux actions de l'utilisateur ou de capteurs."),
  Q("Quel bloc permet à un lutin de réagir à l'appui sur la touche espace ?", ["« Quand la touche espace est pressée »", "« Avancer de 10 »", "« Dire bonjour »", "« Stop tout »"], "« Quand la touche espace est pressée »", "C'est un autre bloc événement."),
]),
notion('T-2', 2, F, 'tec-bug', [
  Q("Comment appelle-t-on une erreur dans un programme ?", ["Un bug (bogue)", "Une boucle", "Une variable", "Un octet"], "Un bug (bogue)", "Le débogage consiste à trouver et corriger ces erreurs."),
  Q("Comment trouver un bug dans un programme ?", ["Effacer tout le programme", "Tester le programme pas à pas et observer ce qui ne se passe pas comme prévu", "Changer d'ordinateur", "Attendre"], "Tester le programme pas à pas et observer ce qui ne se passe pas comme prévu", "On compare le comportement observé au comportement attendu."),
  Q("Un lutin doit tracer un carré mais trace un triangle. Quelle erreur est probable ?", ["Le nombre de répétitions ou l'angle de rotation", "La couleur du stylo", "Le nom du lutin", "Le fond d'écran"], "Le nombre de répétitions ou l'angle de rotation", "Un carré : 4 répétitions et des rotations de 90°."),
]),
notion('T-3', 0, F, 'tec-demarche-projet', [
  Q("Quelle est la première étape d'un projet technique ?", ["Fabriquer", "Identifier le besoin", "Vendre", "Recycler"], "Identifier le besoin", "On part du besoin, puis on rédige le cahier des charges, on cherche des solutions, on réalise et on teste."),
  Q("Qu'est-ce qu'un prototype ?", ["Un objet vendu en magasin", "Un premier modèle réalisé pour tester une solution", "Un dessin", "Une notice"], "Un premier modèle réalisé pour tester une solution", "Le prototype permet de valider ou d'améliorer la conception."),
  Q("Qu'est-ce qu'un croquis ?", ["Un dessin à main levée qui représente une idée de solution", "Un plan coté précis", "Une photo", "Un programme"], "Un dessin à main levée qui représente une idée de solution", "Le croquis précède les dessins techniques plus précis."),
]),
notion('T-3', 0, F, 'tec-recherche-solutions', [
  Q("Comment appelle-t-on une séance où l'on propose librement un maximum d'idées sans les juger ?", ["Un brainstorming (remue-méninges)", "Un contrôle", "Un test", "Un diagnostic"], "Un brainstorming (remue-méninges)", "Les idées sont triées et évaluées ensuite."),
  Q("Pourquoi chercher plusieurs solutions à un même problème ?", ["Pour perdre du temps", "Pour pouvoir les comparer et choisir la mieux adaptée au cahier des charges", "Parce que c'est obligatoire", "Pour compliquer le projet"], "Pour pouvoir les comparer et choisir la mieux adaptée au cahier des charges", "La comparaison se fait selon des critères (coût, efficacité, faisabilité)."),
  Q("Qu'est-ce que le biomimétisme ?", ["Copier un objet existant", "S'inspirer de la nature pour concevoir des solutions techniques", "Fabriquer en plastique", "Un type de moteur"], "S'inspirer de la nature pour concevoir des solutions techniques", "Le velcro s'inspire des fruits de la bardane."),
]),
notion('T-3', 0, F, 'tec-eco-conception', [
  Q("Qu'est-ce que l'éco-conception ?", ["Concevoir des objets les moins chers possible", "Concevoir un objet en réduisant ses impacts sur l'environnement tout au long de son cycle de vie", "Peindre les objets en vert", "Fabriquer uniquement en bois"], "Concevoir un objet en réduisant ses impacts sur l'environnement tout au long de son cycle de vie", "Choix des matériaux, réparabilité, recyclage, consommation…"),
  Q("Quel choix relève de l'éco-conception ?", ["Coller toutes les pièces pour qu'on ne puisse pas les séparer", "Utiliser des vis pour faciliter la réparation et le recyclage", "Multiplier les emballages", "Utiliser des matériaux rares"], "Utiliser des vis pour faciliter la réparation et le recyclage", "Un objet démontable est plus facile à réparer et à trier."),
  Q("Pourquoi choisir des matériaux recyclés ?", ["Ils sont toujours plus solides", "Pour économiser les ressources et l'énergie", "Pour la couleur", "Parce qu'ils sont obligatoires"], "Pour économiser les ressources et l'énergie", "Recycler l'aluminium demande environ 95 % d'énergie en moins que le produire."),
]),
notion('T-3', 0, F, 'tec-fabrication', [
  Q("Quel outil permet de couper une planche de bois ?", ["Une scie", "Un tournevis", "Une pince", "Un marteau"], "Une scie", "On trace d'abord, puis on scie en maintenant la pièce."),
  Q("Quelle machine fabrique un objet couche par couche à partir d'un fichier numérique ?", ["Une scie à ruban", "Une imprimante 3D", "Une perceuse", "Une ponceuse"], "Une imprimante 3D", "C'est la fabrication additive."),
  Q("Quel équipement de protection faut-il porter lors d'un perçage ?", ["Des gants de cuisine", "Des lunettes de protection", "Un casque audio", "Rien"], "Des lunettes de protection", "Elles protègent les yeux des copeaux projetés."),
]),
notion('T-3', 0, F, 'tec-assemblages', [
  Q("Quel type d'assemblage permet de démonter facilement deux pièces ?", ["Le collage", "Le vissage", "La soudure", "Le rivetage"], "Le vissage", "Le collage et la soudure sont des assemblages permanents (non démontables)."),
  Q("Qu'est-ce qu'une liaison encastrement ?", ["Une liaison qui permet la rotation", "Une liaison qui bloque tout mouvement entre deux pièces", "Une liaison qui permet le glissement", "Une liaison magnétique"], "Une liaison qui bloque tout mouvement entre deux pièces", "Une liaison pivot, elle, permet une rotation (comme une charnière)."),
  Q("Quelle liaison permet à une porte de tourner autour de ses gonds ?", ["L'encastrement", "La liaison pivot", "La liaison glissière", "Le collage"], "La liaison pivot", "La liaison glissière permet une translation, comme un tiroir."),
]),
notion('T-3', 1, F, 'tec-tests', [
  Q("Pourquoi teste-t-on un prototype ?", ["Pour le casser", "Pour vérifier qu'il répond au cahier des charges", "Pour le décorer", "Pour le vendre directement"], "Pour vérifier qu'il répond au cahier des charges", "On compare les résultats des tests aux critères attendus."),
  Q("Qu'est-ce qu'un protocole de test ?", ["Une règle de politesse", "La description précise des étapes et conditions d'un essai", "Un résultat", "Une notice de montage"], "La description précise des étapes et conditions d'un essai", "Un protocole précis permet de reproduire le test et de comparer les résultats."),
  Q("Pourquoi utiliser une simulation numérique avant de fabriquer ?", ["C'est plus amusant", "Pour tester une solution sans dépenser de matière et gagner du temps", "Pour remplacer définitivement la fabrication", "Pour changer de cahier des charges"], "Pour tester une solution sans dépenser de matière et gagner du temps", "La simulation permet d'anticiper des défauts."),
]),
notion('T-3', 0, F, 'tec-modelisation-3d', [
  Q("Quel type de logiciel permet de dessiner un objet en trois dimensions ?", ["Un traitement de texte", "Un logiciel de CAO (conception assistée par ordinateur)", "Un tableur", "Un navigateur"], "Un logiciel de CAO (conception assistée par ordinateur)", "La CAO produit des modèles 3D et des plans."),
  Q("Qu'est-ce qu'une maquette numérique ?", ["Une photo de l'objet fini", "Une représentation 3D d'un objet, créée sur ordinateur", "Un jeu vidéo", "Un brouillon papier"], "Une représentation 3D d'un objet, créée sur ordinateur", "Elle permet de visualiser, simuler et préparer la fabrication."),
  Q("Qu'est-ce qu'une cote sur un dessin technique ?", ["Une couleur", "Une dimension indiquée sur le dessin", "Un commentaire", "Un prix"], "Une dimension indiquée sur le dessin", "Les cotes sont généralement exprimées en millimètres."),
]),
notion('T-1', 1, F, 'tec-reseaux-internet', [
  Q("Qu'est-ce qu'Internet ?", ["Un logiciel", "Un réseau mondial qui relie des millions de réseaux informatiques", "Un site web", "Un ordinateur géant"], "Un réseau mondial qui relie des millions de réseaux informatiques", "Le Web n'est qu'un des services d'Internet, comme le courriel."),
  Q("Quel appareil relie le réseau d'une maison à Internet ?", ["L'imprimante", "La box (routeur)", "La souris", "L'écran"], "La box (routeur)", "Elle aiguille les données entre les appareils de la maison et Internet."),
  Q("Qu'est-ce qu'une adresse IP ?", ["Un mot de passe", "Un numéro qui identifie un appareil sur un réseau", "Une adresse de courriel", "Le nom d'un site"], "Un numéro qui identifie un appareil sur un réseau", "Chaque appareil connecté possède une adresse IP."),
]),
notion('T-1', 1, F, 'tec-donnees-personnelles', [
  Q("Laquelle de ces informations est une donnée personnelle ?", ["La météo du jour", "Son adresse postale", "La capitale de la France", "Le prix du pain"], "Son adresse postale", "Une donnée personnelle permet d'identifier une personne directement ou indirectement."),
  Q("Quelle autorité française veille à la protection des données personnelles ?", ["Le CSA", "La CNIL", "L'INSEE", "La SNCF"], "La CNIL", "La Commission nationale de l'informatique et des libertés applique notamment le RGPD."),
  Q("Qu'est-ce qu'un mot de passe robuste ?", ["Sa date de naissance", "Un mot de passe long, mêlant lettres, chiffres et symboles, différent pour chaque compte", "« 123456 »", "Son prénom"], "Un mot de passe long, mêlant lettres, chiffres et symboles, différent pour chaque compte", "Un gestionnaire de mots de passe aide à en utiliser de différents."),
]),
notion('T-1', 1, F, 'tec-stockage-donnees', [
  Q("Où sont stockées les données « dans le cloud » ?", ["Dans les nuages", "Dans des serveurs de centres de données (data centers)", "Dans l'ordinateur de l'utilisateur uniquement", "Nulle part"], "Dans des serveurs de centres de données (data centers)", "Le cloud consomme de l'énergie pour alimenter et refroidir ces serveurs."),
  N("Combien d'octets y a-t-il dans 1 kilooctet (selon le système international) ?", 1000, "Dans le système international, 1 ko = 1 000 octets (le kibioctet vaut 1 024 octets)."),
  Q("Quelle unité est la plus grande ?", ["Le mégaoctet", "Le gigaoctet", "Le téraoctet", "Le kilooctet"], "Le téraoctet", "ko < Mo < Go < To, chaque unité valant 1 000 fois la précédente."),
]),
notion('T-2', 0, F, 'tec-maison-connectee', [
  Q("Qu'est-ce que la domotique ?", ["L'étude des animaux domestiques", "L'ensemble des techniques qui automatisent et pilotent les équipements d'un logement", "La décoration intérieure", "Le ménage"], "L'ensemble des techniques qui automatisent et pilotent les équipements d'un logement", "Volets, chauffage ou éclairage peuvent être commandés à distance."),
  Q("Quel avantage peut apporter un thermostat connecté ?", ["Il chauffe plus", "Il adapte le chauffage aux horaires de présence et économise de l'énergie", "Il supprime le chauffage", "Il refroidit la maison en hiver"], "Il adapte le chauffage aux horaires de présence et économise de l'énergie", "Baisser de 1 °C le chauffage réduit la consommation d'environ 7 %."),
  Q("Qu'est-ce que l'Internet des objets ?", ["Un réseau réservé aux ordinateurs", "La connexion d'objets du quotidien à Internet pour échanger des données", "Un magasin en ligne", "Un jeu vidéo"], "La connexion d'objets du quotidien à Internet pour échanger des données", "Montres, enceintes, compteurs Linky sont des objets connectés."),
]),
notion('T-1', 2, F, 'tec-criteres-choix', [
  Q("Pour choisir un vélo de ville, quel critère est le plus pertinent ?", ["Sa couleur uniquement", "Son adaptation à l'usage : confort, éclairage, garde-boue, porte-bagages", "Son nom", "Le magasin le plus proche"], "Son adaptation à l'usage : confort, éclairage, garde-boue, porte-bagages", "On choisit selon des critères liés à l'usage, au coût et à l'environnement."),
  Q("Quel critère environnemental peut guider l'achat d'un appareil ?", ["Sa publicité", "Sa consommation d'énergie et sa réparabilité", "Sa couleur", "Son emballage brillant"], "Sa consommation d'énergie et sa réparabilité", "L'étiquette énergie et l'indice de réparabilité aident à comparer."),
  Q("Comment comparer objectivement plusieurs objets ?", ["Au hasard", "À l'aide d'un tableau de critères", "En choisissant le plus cher", "En choisissant le plus récent"], "À l'aide d'un tableau de critères", "Le tableau permet de noter chaque objet selon les mêmes critères."),
]),
notion('T-2', 0, F, 'tec-energie-maison', [
  Q("Quel appareil consomme en général le plus d'énergie dans un logement ?", ["Le chargeur de téléphone", "Le chauffage", "La box Internet", "La radio"], "Le chauffage", "Le chauffage représente environ les deux tiers de l'énergie consommée par un logement en France."),
  Q("Quel appareil mesure la consommation électrique d'un logement ?", ["Le disjoncteur", "Le compteur électrique", "La prise", "L'interrupteur"], "Le compteur électrique", "Le compteur Linky transmet les relevés à distance."),
  Q("Qu'est-ce qu'un logement à énergie positive ?", ["Un logement qui consomme beaucoup", "Un logement qui produit plus d'énergie qu'il n'en consomme", "Un logement sans électricité", "Un logement très ensoleillé"], "Un logement qui produit plus d'énergie qu'il n'en consomme", "Il combine isolation poussée et production renouvelable."),
]),
notion('T-1', 0, F, 'tec-transports', [
  Q("Quel moyen de transport a révolutionné les déplacements au XIXe siècle ?", ["L'avion", "Le chemin de fer", "La fusée", "La trottinette électrique"], "Le chemin de fer", "La première ligne de voyageurs française ouvre dans les années 1830."),
  Q("En quelle année le premier TGV commercial circule-t-il en France ?", ["1950", "1981", "2000", "2015"], "1981", "Le TGV relie Paris et Lyon à partir de 1981."),
  Q("Quel est l'intérêt principal d'un véhicule électrique en ville ?", ["Il ne consomme aucune énergie", "Il n'émet pas de gaz d'échappement localement", "Il est plus lourd", "Il ne nécessite aucun entretien"], "Il n'émet pas de gaz d'échappement localement", "Son bilan global dépend de la fabrication de la batterie et de l'origine de l'électricité."),
]),
notion('T-2', 0, F, 'tec-schemas', [
  Q("À quoi sert un schéma fonctionnel ?", ["À décorer un rapport", "À représenter les fonctions d'un objet et les échanges entre ses éléments", "À montrer la couleur", "À calculer un prix"], "À représenter les fonctions d'un objet et les échanges entre ses éléments", "Il montre les flux d'énergie et d'information."),
  Q("Que représente une vue éclatée ?", ["Un objet cassé", "Les pièces d'un objet séparées pour montrer comment elles s'assemblent", "Un objet en couleur", "Une photo floue"], "Les pièces d'un objet séparées pour montrer comment elles s'assemblent", "On la trouve souvent dans les notices de montage."),
  Q("Qu'est-ce qu'une nomenclature ?", ["Une liste des pièces d'un objet, avec leur nombre et leur matière", "Le nom du fabricant", "Un programme", "Une couleur"], "Une liste des pièces d'un objet, avec leur nombre et leur matière", "Elle accompagne la vue éclatée ou le dessin d'ensemble."),
]),
notion('T-3', 2, F, 'tec-robot-programme', [
  Q("Un robot doit avancer jusqu'à un mur puis s'arrêter. Quel capteur utiliser ?", ["Un capteur de température", "Un capteur de distance (ultrasons)", "Un capteur de lumière", "Un micro"], "Un capteur de distance (ultrasons)", "Il mesure la distance par l'écho d'ultrasons."),
  Q("Quel bloc de programme permet au robot d'avancer tant qu'il n'y a pas d'obstacle ?", ["« Répéter jusqu'à ce que la distance soit inférieure à 10 cm : avancer »", "« Dire bonjour »", "« Attendre 100 secondes »", "« Changer de costume »"], "« Répéter jusqu'à ce que la distance soit inférieure à 10 cm : avancer »", "La boucle conditionnelle s'arrête quand la condition devient vraie."),
  Q("Après avoir écrit un programme pour un robot, que faut-il faire ?", ["Le tester et le corriger si nécessaire", "Le jeter", "Le recopier à la main", "Rien"], "Le tester et le corriger si nécessaire", "Écrire, tester, corriger : c'est la mise au point du programme."),
]),
notion('T-1', 0, F, 'tec-objets-quotidien', [
  Q("Quel principe technique permet à une bicyclette de transformer la force des jambes en mouvement ?", ["La combustion", "La transmission du mouvement par le pédalier, la chaîne et les pignons", "L'électricité", "Le magnétisme"], "La transmission du mouvement par le pédalier, la chaîne et les pignons", "Le mouvement de rotation des pédales est transmis à la roue arrière."),
  Q("Quel objet utilise le principe du levier pour décupler la force ?", ["Une paire de ciseaux", "Une ampoule", "Une pile", "Un thermomètre"], "Une paire de ciseaux", "Ciseaux, pinces et casse-noix sont des leviers."),
  Q("Quel principe permet de soulever une charge lourde avec moins d'effort grâce à plusieurs poulies ?", ["Le palan (moufle)", "Le ressort", "Le thermostat", "Le capteur"], "Le palan (moufle)", "En multipliant les brins, on divise l'effort à fournir."),
]),
notion('T-2', 1, F, 'tec-securite-objets', [
  Q("Que signifie le marquage CE sur un produit ?", ["Fabriqué en Chine", "Le fabricant déclare que le produit respecte les exigences européennes de sécurité", "Produit écologique", "Produit gratuit"], "Le fabricant déclare que le produit respecte les exigences européennes de sécurité", "Il est obligatoire pour de nombreux produits (jouets, appareils électriques)."),
  Q("Pourquoi certains jouets portent-ils la mention « Ne convient pas aux enfants de moins de 36 mois » ?", ["Ils sont trop chers", "Ils contiennent de petites pièces qui peuvent être avalées", "Ils sont trop lourds", "Ils sont électriques"], "Ils contiennent de petites pièces qui peuvent être avalées", "Le risque d'étouffement est la principale raison de cette mention."),
  Q("Que signifie ce pictogramme sur un produit : une poubelle barrée ?", ["Le produit est dangereux", "Le produit ne doit pas être jeté avec les ordures ménagères mais déposé dans une filière de collecte", "Le produit est recyclé", "Le produit est gratuit"], "Le produit ne doit pas être jeté avec les ordures ménagères mais déposé dans une filière de collecte", "Les appareils électriques et les piles se rapportent en magasin ou en déchèterie."),
]),
notion('T-3', 0, F, 'tec-design', [
  Q("Qu'est-ce que l'ergonomie d'un objet ?", ["Son prix", "Son adaptation à l'utilisateur, pour un usage confortable et efficace", "Sa couleur", "Son poids uniquement"], "Son adaptation à l'utilisateur, pour un usage confortable et efficace", "Une poignée ergonomique épouse la forme de la main."),
  Q("Qu'est-ce que la conception universelle (accessibilité) ?", ["Concevoir pour un seul type d'utilisateur", "Concevoir des objets utilisables par le plus grand nombre, y compris les personnes en situation de handicap", "Concevoir des objets identiques partout", "Concevoir des objets jetables"], "Concevoir des objets utilisables par le plus grand nombre, y compris les personnes en situation de handicap", "Rampes, boutons en relief, sous-titres en sont des exemples."),
  Q("Quel métier conçoit l'apparence et l'usage des objets fabriqués en série ?", ["Le designer", "Le comptable", "Le géologue", "Le pharmacien"], "Le designer", "Le designer travaille avec les ingénieurs sur la forme et l'usage."),
]),
notion('T-2', 2, F, 'tec-coordonnees-scratch', [
  Q("Dans Scratch, que représente la coordonnée x d'un lutin ?", ["Sa position verticale", "Sa position horizontale", "Sa taille", "Sa couleur"], "Sa position horizontale", "x va de −240 à 240 ; y (vertical) de −180 à 180."),
  Q("Dans Scratch, où se trouve le point de coordonnées (0 ; 0) ?", ["En haut à gauche", "Au centre de la scène", "En bas à droite", "Hors de la scène"], "Au centre de la scène", "C'est l'origine du repère."),
  N("Un lutin est en x = 50. Il exécute « ajouter 30 à x ». Quelle est sa nouvelle abscisse ?", 80, "50 + 30 = 80 : le lutin s'est déplacé vers la droite."),
]),
notion('T-1', 1, F, 'tec-sante-numerique', [
  Q("Qu'est-ce que le cyberharcèlement ?", ["Un jeu vidéo", "Un harcèlement exercé par les outils numériques (messages, réseaux sociaux)", "Une panne d'Internet", "Un virus informatique"], "Un harcèlement exercé par les outils numériques (messages, réseaux sociaux)", "Le numéro 3018 permet de signaler le cyberharcèlement."),
  Q("Quel numéro gratuit permet de signaler un cyberharcèlement en France ?", ["3018", "15", "112", "3615"], "3018", "Le 3018 est joignable par téléphone, application et tchat."),
  Q("Pourquoi faut-il réfléchir avant de publier une photo en ligne ?", ["Elle peut être copiée, partagée et rester en ligne très longtemps", "Elle disparaît au bout d'une heure", "Personne ne la verra", "Ce n'est pas autorisé"], "Elle peut être copiée, partagée et rester en ligne très longtemps", "C'est l'identité numérique : on maîtrise mal ce qui est publié."),
]),
notion('T-1', 1, F, 'tec-fake-news', [
  Q("Comment vérifier une information trouvée sur Internet ?", ["La croire si elle est partagée souvent", "Identifier la source et la croiser avec d'autres sources fiables", "La partager tout de suite", "Regarder seulement le titre"], "Identifier la source et la croiser avec d'autres sources fiables", "Le nombre de partages ne garantit pas la véracité."),
  Q("Qu'est-ce qu'une « infox » (fake news) ?", ["Une information vérifiée", "Une fausse information diffusée comme si elle était vraie", "Une publicité", "Un journal télévisé"], "Une fausse information diffusée comme si elle était vraie", "Elle se propage souvent plus vite qu'une information vraie."),
  Q("Qu'est-ce qu'un moteur de recherche ?", ["Un moteur de voiture", "Un service qui trouve des pages web à partir de mots-clés", "Un réseau social", "Un ordinateur"], "Un service qui trouve des pages web à partir de mots-clés", "Les résultats sont classés par un algorithme, pas par ordre de fiabilité."),
]),
notion('T-3', 1, F, 'tec-mesures', [
  Q("Quel instrument permet de mesurer précisément une petite longueur, au dixième de millimètre ?", ["Un mètre ruban", "Un pied à coulisse", "Une règle de 1 m", "Un rapporteur"], "Un pied à coulisse", "Le pied à coulisse est utilisé en atelier pour vérifier les dimensions."),
  N("Combien de millimètres y a-t-il dans 4,5 cm ?", 45, "1 cm = 10 mm, donc 4,5 cm = 45 mm."),
  Q("Pourquoi répéter plusieurs fois une mesure lors d'un test ?", ["Pour perdre du temps", "Pour limiter l'effet des erreurs et obtenir une valeur fiable", "Parce que la première est toujours fausse", "Pour changer de résultat"], "Pour limiter l'effet des erreurs et obtenir une valeur fiable", "On peut calculer la moyenne des mesures."),
]),
notion('T-2', 0, F, 'tec-energies-renouvelables-objets', [
  Q("Quel objet technique utilise l'énergie du vent ?", ["Un barrage", "Une éolienne", "Un panneau photovoltaïque", "Une centrale à charbon"], "Une éolienne", "Ses pales entraînent un alternateur."),
  Q("Quel objet utilise la chaleur du Soleil pour chauffer de l'eau ?", ["Un chauffe-eau solaire", "Une éolienne", "Un ventilateur", "Une pile"], "Un chauffe-eau solaire", "Les capteurs solaires thermiques chauffent un liquide."),
  Q("Quelle installation utilise l'énergie de l'eau en mouvement ?", ["Une centrale hydroélectrique", "Une centrale à gaz", "Un panneau solaire", "Une pile à combustible"], "Une centrale hydroélectrique", "L'eau fait tourner une turbine reliée à un alternateur."),
]),
notion('T-3', 0, F, 'tec-propriete-intellectuelle', [
  Q("Qu'est-ce qu'un brevet ?", ["Un diplôme du collège uniquement", "Un titre qui protège une invention et donne à son auteur un droit exclusif d'exploitation", "Une notice", "Un plan de fabrication gratuit"], "Un titre qui protège une invention et donne à son auteur un droit exclusif d'exploitation", "En France, il protège une invention pendant 20 ans maximum."),
  Q("Quel organisme délivre les brevets en France ?", ["La CNIL", "L'INPI (Institut national de la propriété industrielle)", "L'INSEE", "La SNCF"], "L'INPI (Institut national de la propriété industrielle)", "L'INPI enregistre aussi les marques et les dessins et modèles."),
  Q("Qu'est-ce qu'un logiciel libre ?", ["Un logiciel volé", "Un logiciel que l'on peut utiliser, étudier, modifier et redistribuer librement", "Un logiciel toujours payant", "Un logiciel sans code"], "Un logiciel que l'on peut utiliser, étudier, modifier et redistribuer librement", "Firefox ou LibreOffice sont des logiciels libres."),
]),
notion('T-1', 0, F, 'tec-revolution-numerique', [
  Q("Quand le Web a-t-il été inventé ?", ["En 1789", "Vers 1989-1990, au CERN", "En 2010", "En 1950"], "Vers 1989-1990, au CERN", "Tim Berners-Lee invente le World Wide Web au CERN, près de Genève."),
  Q("Quel objet a permis l'informatique personnelle à partir des années 1970-1980 ?", ["Le télégraphe", "Le micro-ordinateur", "La machine à vapeur", "Le télescope"], "Le micro-ordinateur", "La miniaturisation des composants (microprocesseur) a rendu possible l'ordinateur personnel."),
  Q("Quel service français a précédé Internet pour le grand public dans les années 1980 ?", ["Le Minitel", "Le fax", "La radio", "Le télégraphe"], "Le Minitel", "Le Minitel a été arrêté en 2012."),
]),
notion('T-2', 0, F, 'tec-binaire', [
  Q("Quel système de numération utilisent les ordinateurs pour coder l'information ?", ["Le système décimal", "Le système binaire (0 et 1)", "Les chiffres romains", "L'alphabet"], "Le système binaire (0 et 1)", "Un bit vaut 0 ou 1 : courant ou absence de courant."),
  N("Quelle est la valeur décimale du nombre binaire 101 ?", 5, "101 = 1 × 4 + 0 × 2 + 1 × 1 = 5."),
  N("Quelle est la valeur décimale du nombre binaire 1000 ?", 8, "1000 = 1 × 8 = 8 : chaque rang vaut le double du précédent."),
]),
notion('T-3', 0, F, 'tec-planning-projet', [
  Q("Pourquoi établir un planning dans un projet technique ?", ["Pour décorer le cahier", "Pour organiser les tâches dans le temps et répartir le travail", "Pour éviter de tester", "Ce n'est jamais utile"], "Pour organiser les tâches dans le temps et répartir le travail", "Le planning fixe l'ordre des tâches et les échéances."),
  Q("Dans un travail d'équipe en projet, qu'est-ce qu'un rôle ?", ["Une sanction", "Une responsabilité confiée à un membre (chef de projet, rapporteur…)", "Une note", "Un outil"], "Une responsabilité confiée à un membre (chef de projet, rapporteur…)", "La répartition des rôles rend l'équipe plus efficace."),
  Q("À quoi sert la présentation finale d'un projet ?", ["À rien", "À expliquer la démarche, les choix effectués et les résultats des tests", "À vendre l'objet", "À remplacer le prototype"], "À expliquer la démarche, les choix effectués et les résultats des tests", "Elle développe les compétences de communication."),
]),
]

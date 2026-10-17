from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('T-1', 0, I, 'tec-revolutions-industrielles', [
  Q("Quelle source d'énergie caractérise la première révolution industrielle (fin XVIIIe – XIXe siècle) ?", ["L'électricité", "Le charbon et la machine à vapeur", "Le nucléaire", "Le solaire"], "Le charbon et la machine à vapeur", "La deuxième révolution industrielle repose sur l'électricité et le pétrole."),
  Q("Qu'est-ce que le travail à la chaîne, développé par Ford au début du XXe siècle ?", ["Un travail artisanal", "Une organisation où chaque ouvrier réalise une tâche répétitive sur un produit qui défile", "Un travail à domicile", "Un travail sans machine"], "Une organisation où chaque ouvrier réalise une tâche répétitive sur un produit qui défile", "Il permet la production en grande série de la Ford T."),
  Q("Qu'appelle-t-on « industrie 4.0 » ?", ["L'industrie du charbon", "Une industrie qui intègre objets connectés, robots et données numériques", "Une industrie sans machine", "L'artisanat"], "Une industrie qui intègre objets connectés, robots et données numériques", "Elle succède à l'automatisation électronique des années 1970."),
]),
notion('T-1', 1, I, 'tec-analyse-cycle-vie', [
  Q("Qu'est-ce qu'une analyse du cycle de vie (ACV) ?", ["Le calcul du prix de vente", "L'évaluation des impacts environnementaux d'un produit de l'extraction des matières à sa fin de vie", "Une notice d'utilisation", "La durée de garantie"], "L'évaluation des impacts environnementaux d'un produit de l'extraction des matières à sa fin de vie", "Elle permet de comparer des solutions de façon objective."),
  Q("Qu'est-ce que l'économie circulaire ?", ["Une économie fondée sur « extraire, fabriquer, jeter »", "Une économie qui vise à réduire les déchets en réutilisant, réparant et recyclant", "Une économie de la monnaie", "Le commerce international"], "Une économie qui vise à réduire les déchets en réutilisant, réparant et recyclant", "Elle s'oppose à l'économie linéaire."),
  Q("Que signifie le principe des « 3R » ?", ["Rapide, robuste, rentable", "Réduire, réutiliser, recycler", "Réparer, revendre, racheter", "Rouler, rouler, rouler"], "Réduire, réutiliser, recycler", "Réduire passe en premier : le meilleur déchet est celui qu'on ne produit pas."),
]),
notion('T-1', 1, I, 'tec-impact-numerique', [
  Q("Quelle part environ des émissions mondiales de gaz à effet de serre est attribuée au numérique ?", ["Moins de 0,1 %", "Environ 3 à 4 %", "50 %", "90 %"], "Environ 3 à 4 %", "Une part comparable à celle du transport aérien, et en croissance."),
  Q("En France, quelle part de l'empreinte carbone du numérique vient de la fabrication des terminaux ?", ["Une part négligeable", "La plus grande part (environ 80 %)", "Exactement 10 %", "Aucune"], "La plus grande part (environ 80 %)", "Selon l'ADEME et l'Arcep, les terminaux (écrans, ordinateurs, téléphones) dominent l'empreinte."),
  Q("Quel geste réduit le plus l'impact environnemental du numérique ?", ["Supprimer quelques courriels", "Garder ses appareils plus longtemps", "Changer de téléphone chaque année", "Laisser la box allumée"], "Garder ses appareils plus longtemps", "La fabrication pèse beaucoup plus que l'usage."),
]),
notion('T-1', 2, I, 'tec-materiaux-proprietes-avancees', [
  Q("Que signifie qu'un matériau est ductile ?", ["Il se casse facilement", "Il peut être étiré en fils sans se rompre", "Il est transparent", "Il conduit la chaleur"], "Il peut être étiré en fils sans se rompre", "Le cuivre et l'or sont très ductiles."),
  Q("Pourquoi utilise-t-on l'aluminium dans l'aéronautique ?", ["Il est très lourd", "Il est léger et résistant à la corrosion", "Il est magnétique", "Il est transparent"], "Il est léger et résistant à la corrosion", "Sa masse volumique est d'environ 2,7 g/cm³, près de 3 fois moins que l'acier."),
  Q("Quel matériau est biodégradable ?", ["Le PVC", "Le carton", "L'acier inoxydable", "Le verre"], "Le carton", "Un matériau biodégradable est décomposé par des micro-organismes."),
]),
notion('T-1', 2, I, 'tec-recyclage-materiaux', [
  Q("Pourquoi trie-t-on les plastiques selon leur nature (PET, PEHD…) ?", ["Pour la couleur", "Parce que chaque plastique se recycle selon un procédé différent", "Pour les brûler", "Ce n'est pas utile"], "Parce que chaque plastique se recycle selon un procédé différent", "Le PET des bouteilles peut redevenir bouteille ou fibre textile."),
  Q("Comment sépare-t-on l'acier des autres déchets dans un centre de tri ?", ["À la main uniquement", "Avec un aimant (overband)", "Avec de l'eau", "Par la couleur"], "Avec un aimant (overband)", "L'acier est magnétique ; l'aluminium est séparé par courants de Foucault."),
  Q("Qu'est-ce qu'un métal « critique » ou « stratégique » ?", ["Un métal sans valeur", "Un métal indispensable à certaines technologies et dont l'approvisionnement est à risque", "Un métal recyclé", "Un métal radioactif"], "Un métal indispensable à certaines technologies et dont l'approvisionnement est à risque", "Lithium, cobalt et terres rares sont utilisés dans les batteries et l'électronique."),
]),
notion('T-2', 0, I, 'tec-chaines-completes', [
  Q("Dans un portail automatique, quel élément appartient à la chaîne d'information ?", ["Le moteur", "La télécommande et le récepteur", "Le bras articulé", "Le portail lui-même"], "La télécommande et le récepteur", "Le récepteur acquiert l'ordre transmis par la télécommande."),
  Q("Dans un portail automatique, quel élément assure la fonction « transmettre » de la chaîne d'énergie ?", ["La cellule photoélectrique", "Le bras et le réducteur qui transmettent le mouvement au portail", "La carte électronique", "Le voyant clignotant"], "Le bras et le réducteur qui transmettent le mouvement au portail", "Le moteur convertit ; le réducteur et le bras transmettent."),
  Q("Quel élément relie la chaîne d'information à la chaîne d'énergie ?", ["Le capteur", "Le préactionneur (relais, carte de commande du moteur)", "La batterie", "Le boîtier"], "Le préactionneur (relais, carte de commande du moteur)", "Il distribue l'énergie aux actionneurs selon les ordres reçus."),
]),
notion('T-2', 0, I, 'tec-rapport-transmission', [
  N("Une roue menante de 40 dents entraîne une roue menée de 20 dents. Combien de tours fait la roue menée quand la menante fait 1 tour ?", 2, "Rapport = 40 / 20 = 2 : la petite roue tourne deux fois plus vite."),
  N("Sur un vélo, le plateau a 48 dents et le pignon 16 dents. Combien de tours fait la roue arrière pour un tour de pédalier ?", 3, "48 / 16 = 3 tours de roue par tour de pédale."),
  Q("Pour monter une côte facilement à vélo, on choisit…", ["un grand plateau et un petit pignon", "un petit plateau et un grand pignon", "le plus grand plateau et le plus petit pignon", "n'importe quel braquet"], "un petit plateau et un grand pignon", "Le rapport est faible : on fait moins de chemin par tour de pédale, mais l'effort est réduit."),
]),
notion('T-2', 0, I, 'tec-transformation-mouvement', [
  Q("Quel système transforme un mouvement de rotation en mouvement de translation ?", ["Un engrenage droit", "Un système pignon-crémaillère", "Une courroie", "Une chaîne"], "Un système pignon-crémaillère", "On le trouve dans la direction des voitures ou les portails coulissants."),
  Q("Quel système transforme le mouvement de translation des pistons d'un moteur en rotation ?", ["Le système bielle-manivelle", "La poulie", "Le levier", "Le ressort"], "Le système bielle-manivelle", "Il transforme le va-et-vient des pistons en rotation du vilebrequin."),
  Q("Quel système transforme une rotation en translation, comme dans un étau ou un cric ?", ["Le système vis-écrou", "L'engrenage conique", "La chaîne", "La courroie"], "Le système vis-écrou", "En tournant la vis, l'écrou (ou la mâchoire) se déplace en ligne droite."),
]),
notion('T-2', 0, I, 'tec-reseau-communication', [
  Q("Qu'est-ce qu'un protocole de communication en réseau ?", ["Un câble", "Un ensemble de règles permettant à des machines d'échanger des données", "Un ordinateur", "Un mot de passe"], "Un ensemble de règles permettant à des machines d'échanger des données", "TCP/IP est le protocole de base d'Internet."),
  Q("Comment les données circulent-elles sur Internet ?", ["En un seul bloc", "Découpées en paquets qui peuvent emprunter des chemins différents", "Par courrier", "Uniquement par satellite"], "Découpées en paquets qui peuvent emprunter des chemins différents", "Les paquets sont réassemblés à l'arrivée."),
  Q("Quel est le rôle d'un serveur DNS ?", ["Stocker des vidéos", "Traduire un nom de domaine (exemple.fr) en adresse IP", "Envoyer des courriels", "Protéger des virus"], "Traduire un nom de domaine (exemple.fr) en adresse IP", "C'est l'« annuaire » d'Internet."),
]),
notion('T-2', 0, I, 'tec-transmission-sans-fil', [
  Q("Quelle technologie permet de relier un casque à un téléphone sur quelques mètres ?", ["La fibre optique", "Le Bluetooth", "Le câble Ethernet", "Le satellite"], "Le Bluetooth", "Le Bluetooth utilise des ondes radio à courte portée."),
  Q("Quelle technologie sans contact utilise une carte bancaire pour payer en approchant le terminal ?", ["Le Wi-Fi", "Le NFC (communication en champ proche)", "La 5G", "Le GPS"], "Le NFC (communication en champ proche)", "Le NFC fonctionne à quelques centimètres seulement."),
  Q("Comment un récepteur GPS détermine-t-il sa position ?", ["Grâce aux antennes Wi-Fi uniquement", "En calculant sa distance à plusieurs satellites à partir des signaux qu'ils émettent", "En demandant à l'utilisateur", "Grâce à une boussole"], "En calculant sa distance à plusieurs satellites à partir des signaux qu'ils émettent", "Il faut au moins 4 satellites pour une position précise ; l'Europe a son propre système, Galileo."),
]),
notion('T-2', 1, I, 'tec-diagnostic-methode', [
  Q("Un robot programmé n'avance pas. Le moteur fonctionne quand on le branche directement sur la pile. Où chercher la panne ?", ["Dans le moteur", "Dans la chaîne d'information (programme, câblage de commande, carte)", "Dans la couleur du robot", "Dans les roues uniquement"], "Dans la chaîne d'information (programme, câblage de commande, carte)", "On isole les éléments un par un pour localiser la panne."),
  Q("Quel appareil permet de vérifier si un fil conduit le courant ?", ["Un thermomètre", "Un multimètre en mode continuité (ohmmètre)", "Une balance", "Un pied à coulisse"], "Un multimètre en mode continuité (ohmmètre)", "Le multimètre émet un bip si le circuit est continu."),
  Q("Quelle règle de sécurité respecter avant de dépanner un appareil électrique sur secteur ?", ["Le laisser branché pour tester", "Le débrancher (mise hors tension)", "Mouiller ses mains", "Retirer l'isolant des fils"], "Le débrancher (mise hors tension)", "On ne travaille jamais sous tension."),
]),
notion('T-2', 1, I, 'tec-maintenance', [
  Q("Qu'est-ce que la maintenance préventive ?", ["Réparer après une panne", "Entretenir un appareil régulièrement pour éviter les pannes", "Jeter l'appareil", "Acheter un appareil neuf"], "Entretenir un appareil régulièrement pour éviter les pannes", "La vidange d'une voiture est de la maintenance préventive."),
  Q("Qu'est-ce que la maintenance corrective ?", ["L'entretien régulier", "La réparation d'un appareil après une panne", "La fabrication", "Le recyclage"], "La réparation d'un appareil après une panne", "Elle intervient après la défaillance."),
  Q("Pourquoi dépoussiérer régulièrement les grilles d'aération d'un ordinateur ?", ["Pour la couleur", "Pour éviter la surchauffe des composants", "Pour accélérer Internet", "Ce n'est pas utile"], "Pour éviter la surchauffe des composants", "La surchauffe réduit les performances et la durée de vie."),
]),
notion('T-2', 2, I, 'tec-boucles-conditionnelles', [
  Q("Que fait la boucle « répéter jusqu'à ce que… » ?", ["Elle répète un nombre fixe de fois", "Elle répète tant que la condition n'est pas vraie", "Elle ne répète jamais", "Elle arrête le programme"], "Elle répète tant que la condition n'est pas vraie", "Elle s'arrête dès que la condition devient vraie."),
  N("x vaut 1. Le programme exécute « répéter jusqu'à ce que x > 20 : mettre x à x × 2 ». Que vaut x à la fin ?", 32, "1 → 2 → 4 → 8 → 16 → 32 : la boucle s'arrête quand x dépasse 20."),
  N("Un compteur vaut 0. « Répéter 3 fois : répéter 4 fois : ajouter 1 au compteur ». Que vaut le compteur ?", 12, "Boucles imbriquées : 3 × 4 = 12."),
]),
notion('T-2', 2, I, 'tec-operateurs-logiques', [
  Q("La condition « A et B » est vraie…", ["si A ou B est vrai", "seulement si A et B sont vrais tous les deux", "si A est faux", "jamais"], "seulement si A et B sont vrais tous les deux", "C'est l'opérateur logique ET."),
  Q("La condition « A ou B » est fausse…", ["si l'un des deux est faux", "seulement si A et B sont faux tous les deux", "toujours", "si A est vrai"], "seulement si A et B sont faux tous les deux", "OU est vrai dès qu'au moins une des conditions est vraie."),
  Q("Une lampe s'allume « si il fait nuit et si une présence est détectée ». Il fait nuit mais personne ne passe. La lampe…", ["s'allume", "reste éteinte", "clignote", "grille"], "reste éteinte", "Avec ET, les deux conditions doivent être vraies."),
]),
notion('T-2', 2, I, 'tec-messages-scratch', [
  Q("Dans Scratch, à quoi sert le bloc « envoyer à tous le message… » ?", ["À écrire une bulle", "À déclencher des scripts chez d'autres lutins ou sur la scène", "À supprimer un lutin", "À créer une variable"], "À déclencher des scripts chez d'autres lutins ou sur la scène", "Les messages permettent de synchroniser plusieurs lutins."),
  Q("Quel bloc reçoit un message envoyé par un autre lutin ?", ["« Quand je reçois… »", "« Dire… »", "« Avancer de… »", "« Si… alors »"], "« Quand je reçois… »", "C'est un bloc événement."),
  Q("Pourquoi utiliser des messages plutôt que des attentes chronométrées entre lutins ?", ["C'est plus lent", "Les actions s'enchaînent de façon fiable, quelle que soit leur durée", "Cela supprime les lutins", "Cela évite les variables"], "Les actions s'enchaînent de façon fiable, quelle que soit leur durée", "Les attentes chronométrées se désynchronisent facilement."),
]),
notion('T-2', 2, I, 'tec-lecture-programme', [
  N("Un lutin part de x = 0. « Répéter 5 fois : ajouter 10 à x ; si x = 30 alors ajouter 100 à x ». Que vaut x à la fin ?", 150, "10, 20, 30 → 130, 140, 150."),
  N("Score = 0. « Répéter 10 fois : si score < 5 alors ajouter 1 à score ». Que vaut score ?", 5, "Le score augmente jusqu'à 5, puis la condition devient fausse."),
  Q("Un programme contient « répéter indéfiniment » sans condition d'arrêt. Que se passe-t-il ?", ["Il s'arrête après 10 tours", "Il tourne sans fin, jusqu'à l'arrêt manuel", "Il ne démarre pas", "Il plante l'ordinateur"], "Il tourne sans fin, jusqu'à l'arrêt manuel", "C'est utile pour un jeu ou un objet qui surveille en permanence un capteur."),
]),
notion('T-3', 0, I, 'tec-cahier-charges-fonctionnel', [
  Q("Dans un cahier des charges, que désigne la « fonction principale » ?", ["La couleur", "La raison d'être de l'objet, le service rendu à l'utilisateur", "Le prix", "Le fournisseur"], "La raison d'être de l'objet, le service rendu à l'utilisateur", "Les fonctions contraintes s'y ajoutent (sécurité, environnement, coût)."),
  Q("Quel outil représente les relations entre un objet et les éléments de son environnement ?", ["Le diagramme pieuvre", "Le planning", "L'algorithme", "La nomenclature"], "Le diagramme pieuvre", "Il fait apparaître fonctions principales et fonctions contraintes."),
  Q("Quel critère est mesurable ?", ["« L'objet doit être joli »", "« L'objet doit peser moins de 500 g »", "« L'objet doit plaire »", "« L'objet doit être moderne »"], "« L'objet doit peser moins de 500 g »", "Un critère mesurable permet une validation objective."),
]),
notion('T-3', 0, I, 'tec-choix-solution', [
  Q("Qu'est-ce qu'une matrice de décision ?", ["Un programme", "Un tableau qui note plusieurs solutions selon des critères pondérés", "Un dessin technique", "Un capteur"], "Un tableau qui note plusieurs solutions selon des critères pondérés", "Elle aide à choisir objectivement la meilleure solution."),
  N("Dans une matrice, le critère « coût » a un coefficient 3 et la solution A obtient 4/5. Combien de points rapporte ce critère ?", 12, "Note pondérée = 3 × 4 = 12."),
  Q("Pourquoi pondérer les critères ?", ["Pour compliquer", "Parce que certains critères sont plus importants que d'autres", "Pour favoriser une solution choisie à l'avance", "Pour supprimer des critères"], "Parce que certains critères sont plus importants que d'autres", "La sécurité peut peser plus que l'esthétique, par exemple."),
]),
notion('T-3', 0, I, 'tec-fabrication-numerique', [
  Q("Que fait une découpeuse laser ?", ["Elle colle des pièces", "Elle découpe ou grave des plaques (bois, carton, acrylique) à partir d'un fichier numérique", "Elle imprime en couleur", "Elle soude des métaux"], "Elle découpe ou grave des plaques (bois, carton, acrylique) à partir d'un fichier numérique", "C'est une fabrication soustractive pilotée par ordinateur."),
  Q("Comment appelle-t-on un lieu ouvert au public équipé de machines de fabrication numérique ?", ["Un fablab", "Une usine", "Un datacenter", "Une déchèterie"], "Un fablab", "Les fablabs proposent imprimantes 3D, découpeuses laser, fraiseuses…"),
  Q("Quel matériau est le plus utilisé en impression 3D à l'école ?", ["L'acier", "Le PLA, un plastique d'origine végétale", "Le verre", "Le béton"], "Le PLA, un plastique d'origine végétale", "Le PLA est fabriqué à partir d'amidon de maïs, par exemple."),
]),
notion('T-3', 1, I, 'tec-validation', [
  Q("Un prototype de pont en carton doit supporter 2 kg. Il casse à 1,5 kg. Que faire ?", ["Valider quand même", "Analyser la rupture, modifier la conception et refaire le test", "Abandonner le projet", "Changer le cahier des charges sans raison"], "Analyser la rupture, modifier la conception et refaire le test", "La démarche est itérative : concevoir, tester, améliorer."),
  Q("Qu'est-ce qu'une démarche itérative ?", ["Une démarche faite une seule fois", "Une démarche qui répète des cycles de conception, de test et d'amélioration", "Une démarche au hasard", "Une démarche sans test"], "Une démarche qui répète des cycles de conception, de test et d'amélioration", "Chaque cycle rapproche la solution du cahier des charges."),
  Q("Pourquoi noter les résultats des tests dans un tableau ?", ["Pour faire joli", "Pour comparer les résultats aux critères du cahier des charges et garder une trace", "Pour les cacher", "Ce n'est pas utile"], "Pour comparer les résultats aux critères du cahier des charges et garder une trace", "La traçabilité est essentielle en conception."),
]),
notion('T-3', 2, I, 'tec-decomposition-probleme', [
  Q("Face à un programme complexe, quelle démarche adopter ?", ["Tout écrire d'un coup", "Décomposer le problème en sous-problèmes plus simples", "Copier un programme au hasard", "Abandonner"], "Décomposer le problème en sous-problèmes plus simples", "Chaque sous-problème est programmé et testé séparément."),
  Q("Dans Scratch, à quoi sert un « bloc personnalisé » (Mes blocs) ?", ["À changer la couleur", "À regrouper une suite d'instructions réutilisable sous un nom", "À supprimer un lutin", "À enregistrer un son"], "À regrouper une suite d'instructions réutilisable sous un nom", "C'est l'équivalent d'une fonction ou d'une procédure."),
  Q("Pourquoi donner des noms explicites aux variables ?", ["Pour les rendre secrètes", "Pour rendre le programme plus lisible et plus facile à corriger", "Parce que c'est obligatoire", "Pour accélérer le programme"], "Pour rendre le programme plus lisible et plus facile à corriger", "« score » est plus clair que « a »."),
]),
notion('T-1', 1, I, 'tec-securite-informatique', [
  Q("Qu'est-ce que l'hameçonnage (phishing) ?", ["Une technique de pêche", "Une technique de fraude qui imite un organisme de confiance pour voler des informations", "Un antivirus", "Un réseau social"], "Une technique de fraude qui imite un organisme de confiance pour voler des informations", "Il ne faut jamais communiquer ses identifiants par courriel."),
  Q("À quoi sert l'authentification à deux facteurs ?", ["À se connecter deux fois plus vite", "À renforcer la sécurité en demandant une seconde preuve d'identité (code par SMS, application)", "À partager son compte", "À supprimer le mot de passe"], "À renforcer la sécurité en demandant une seconde preuve d'identité (code par SMS, application)", "Même si le mot de passe est volé, le compte reste protégé."),
  Q("Pourquoi faire régulièrement les mises à jour des logiciels ?", ["Pour changer les couleurs", "Pour corriger des failles de sécurité", "Pour ralentir l'ordinateur", "Ce n'est pas utile"], "Pour corriger des failles de sécurité", "Les mises à jour comblent des vulnérabilités connues."),
]),
notion('T-1', 1, I, 'tec-ia', [
  Q("Sur quoi repose principalement l'apprentissage automatique (machine learning) ?", ["Sur des règles écrites à la main pour chaque cas", "Sur l'analyse de grandes quantités de données pour repérer des régularités", "Sur le hasard", "Sur la conscience des machines"], "Sur l'analyse de grandes quantités de données pour repérer des régularités", "La qualité des données d'entraînement influence les résultats."),
  Q("Pourquoi une intelligence artificielle peut-elle reproduire des biais ?", ["Elle est méchante", "Les données sur lesquelles elle a été entraînée peuvent contenir des biais", "Elle est toujours neutre", "Elle choisit au hasard"], "Les données sur lesquelles elle a été entraînée peuvent contenir des biais", "D'où l'importance de vérifier ses réponses et ses sources."),
  Q("Quelle attitude adopter face à un texte produit par une IA générative ?", ["Le croire sans vérifier", "Le relire avec esprit critique et vérifier les faits", "Le recopier sans le citer", "L'ignorer systématiquement"], "Le relire avec esprit critique et vérifier les faits", "Les IA génératives peuvent produire des erreurs plausibles."),
]),
notion('T-2', 0, I, 'tec-stockage-energie', [
  Q("Pourquoi stocker l'électricité produite par des panneaux solaires ?", ["Pour la gaspiller", "Parce que la production ne coïncide pas toujours avec la consommation", "Parce que c'est obligatoire", "Pour refroidir les panneaux"], "Parce que la production ne coïncide pas toujours avec la consommation", "On produit le jour, on consomme aussi le soir."),
  Q("Quelle installation stocke de l'énergie en pompant de l'eau vers un bassin en hauteur ?", ["Une STEP (station de transfert d'énergie par pompage)", "Une éolienne", "Un panneau solaire", "Une centrale à charbon"], "Une STEP (station de transfert d'énergie par pompage)", "L'eau est turbinée plus tard, quand la demande augmente."),
  Q("Quel type de batterie équipe la plupart des téléphones et voitures électriques ?", ["Plomb", "Lithium-ion", "Nickel-cadmium", "Charbon"], "Lithium-ion", "Elle offre une grande capacité pour une masse réduite."),
]),
notion('T-1', 0, I, 'tec-architecture-ouvrages', [
  Q("Pourquoi la forme en arc est-elle utilisée dans les ponts depuis l'Antiquité ?", ["Pour la décoration", "Elle transforme les charges en efforts de compression que la pierre supporte bien", "Elle est plus légère", "Elle évite la rouille"], "Elle transforme les charges en efforts de compression que la pierre supporte bien", "La pierre résiste bien à la compression, mal à la traction."),
  Q("Quel matériau a permis la construction de la tour Eiffel en 1889 ?", ["Le béton armé", "Le fer puddlé", "Le bois", "L'aluminium"], "Le fer puddlé", "Plus de 18 000 pièces métalliques assemblées par rivets."),
  Q("Qu'est-ce que le béton armé ?", ["Du béton peint", "Du béton renforcé par des barres d'acier", "Du béton léger", "Du béton sans ciment"], "Du béton renforcé par des barres d'acier", "L'acier reprend les efforts de traction que le béton supporte mal."),
]),
notion('T-2', 0, I, 'tec-signal-analogique-numerique', [
  Q("Quelle est la différence entre un signal analogique et un signal numérique ?", ["Aucune", "L'analogique varie de façon continue ; le numérique prend des valeurs discrètes", "Le numérique est toujours sonore", "L'analogique est plus récent"], "L'analogique varie de façon continue ; le numérique prend des valeurs discrètes", "La conversion analogique-numérique échantillonne le signal."),
  Q("Qu'est-ce que l'échantillonnage d'un son ?", ["Le découper en morceaux de musique", "Mesurer sa valeur à intervalles de temps réguliers", "Le rendre plus fort", "L'effacer"], "Mesurer sa valeur à intervalles de temps réguliers", "Un CD audio échantillonne le son 44 100 fois par seconde."),
  Q("Quel est l'intérêt du numérique pour transmettre une information ?", ["Il est toujours plus lent", "Il est moins sensible aux parasites et facile à copier sans perte", "Il ne peut pas être compressé", "Il consomme moins de bits"], "Il est moins sensible aux parasites et facile à copier sans perte", "Des codes correcteurs détectent et corrigent les erreurs."),
]),
notion('T-2', 0, I, 'tec-images-numeriques', [
  Q("Qu'est-ce qu'un pixel ?", ["Un fichier", "Le plus petit élément d'une image numérique", "Un logiciel", "Un écran"], "Le plus petit élément d'une image numérique", "Chaque pixel a une couleur codée en nombres."),
  N("Une image fait 100 pixels de large et 50 de haut. Combien de pixels contient-elle ?", 5000, "100 × 50 = 5 000 pixels."),
  N("Chaque pixel d'une image en couleurs est codé sur 3 octets (rouge, vert, bleu). Combien d'octets pour une image de 1 000 pixels, sans compression ?", 3000, "1 000 × 3 = 3 000 octets."),
]),
notion('T-3', 0, I, 'tec-design-thinking', [
  Q("Que place au centre la démarche de « design thinking » ?", ["Le prix", "Les besoins réels des utilisateurs", "La machine", "Le fournisseur"], "Les besoins réels des utilisateurs", "Elle passe par l'observation, l'idéation, le prototypage et le test."),
  Q("Pourquoi observer des utilisateurs avant de concevoir ?", ["C'est inutile", "Pour comprendre leurs difficultés et leurs besoins réels", "Pour les surveiller", "Pour les copier"], "Pour comprendre leurs difficultés et leurs besoins réels", "On découvre souvent des besoins que les utilisateurs n'expriment pas."),
  Q("Qu'est-ce qu'une innovation ?", ["Une idée jamais réalisée", "Une nouveauté qui trouve des utilisateurs et se diffuse", "Un brevet seul", "Une copie"], "Une nouveauté qui trouve des utilisateurs et se diffuse", "Une invention devient une innovation quand elle est adoptée."),
]),
notion('T-1', 2, I, 'tec-cout-objet', [
  Q("Quels éléments entrent dans le coût de revient d'un objet ?", ["Uniquement les matériaux", "Les matériaux, la main-d'œuvre, l'énergie, les machines, le transport…", "Uniquement la publicité", "Uniquement la TVA"], "Les matériaux, la main-d'œuvre, l'énergie, les machines, le transport…", "Le prix de vente ajoute la marge et les taxes."),
  N("Un objet coûte 12 € de matériaux, 20 € de main-d'œuvre et 3 € d'énergie. Quel est son coût de revient (en €) ?", 35, "12 + 20 + 3 = 35 €."),
  Q("Pourquoi produire en grande série réduit-il souvent le coût unitaire ?", ["Les matériaux sont gratuits", "Les coûts fixes (machines, conception) sont répartis sur un grand nombre d'objets", "La main-d'œuvre disparaît", "Ce n'est jamais le cas"], "Les coûts fixes (machines, conception) sont répartis sur un grand nombre d'objets", "Ce sont les économies d'échelle."),
]),
notion('T-2', 0, I, 'tec-automatisme', [
  Q("Qu'est-ce qu'un système automatisé ?", ["Un système qui fonctionne sans intervention humaine une fois lancé", "Un système manuel", "Un système sans énergie", "Un système cassé"], "Un système qui fonctionne sans intervention humaine une fois lancé", "Feux tricolores, portes automatiques, barrières de parking."),
  Q("Qu'est-ce qu'une consigne dans un système régulé ?", ["Un ordre de punition", "La valeur souhaitée que le système doit atteindre (température, vitesse…)", "Une mesure", "Une panne"], "La valeur souhaitée que le système doit atteindre (température, vitesse…)", "Le système compare la mesure à la consigne et agit en conséquence."),
  Q("Un radiateur avec thermostat réglé à 19 °C. La pièce est à 21 °C. Que fait-il ?", ["Il chauffe plus fort", "Il coupe le chauffage", "Il refroidit la pièce", "Il clignote"], "Il coupe le chauffage", "La température mesurée dépasse la consigne."),
  Q("Qu'est-ce qu'une boucle de rétroaction (asservissement) ?", ["Une boucle de programme infinie", "Un fonctionnement où le système mesure le résultat de son action pour la corriger", "Un câble en boucle", "Un bug"], "Un fonctionnement où le système mesure le résultat de son action pour la corriger", "Le régulateur de vitesse d'une voiture en est un exemple."),
]),
notion('T-2', 0, I, 'tec-microcontroleur', [
  Q("Quelle carte programmable, conçue pour l'éducation, possède une matrice de 25 LED et des boutons ?", ["Une carte micro:bit", "Une carte mère d'ordinateur", "Une carte bancaire", "Une carte SIM"], "Une carte micro:bit", "Elle se programme par blocs (MakeCode) ou en Python."),
  Q("Que signifie « téléverser » un programme ?", ["L'imprimer", "Le transférer de l'ordinateur vers la carte programmable", "L'effacer", "Le traduire en anglais"], "Le transférer de l'ordinateur vers la carte programmable", "La carte exécute ensuite le programme de façon autonome."),
  Q("Qu'est-ce qu'une entrée sur une carte programmable ?", ["Une broche où l'on branche un actionneur", "Une broche qui reçoit une information, par exemple d'un capteur", "Une prise de courant", "Un écran"], "Une broche qui reçoit une information, par exemple d'un capteur", "Les actionneurs se branchent sur les sorties."),
]),
notion('T-3', 1, I, 'tec-simulation', [
  Q("Que permet un logiciel de simulation mécanique ?", ["Dessiner des personnages", "Prévoir le comportement d'une structure soumise à des efforts avant de la construire", "Programmer un jeu", "Écrire un texte"], "Prévoir le comportement d'une structure soumise à des efforts avant de la construire", "Il montre les zones les plus sollicitées."),
  Q("Quelle est la limite d'une simulation ?", ["Elle est toujours parfaite", "Elle repose sur un modèle simplifié qui doit être confronté au réel", "Elle remplace tout essai", "Elle ne sert à rien"], "Elle repose sur un modèle simplifié qui doit être confronté au réel", "On valide ensuite par des essais réels."),
  Q("Un simulateur de circuit électrique sert à…", ["construire réellement le circuit", "tester un montage virtuellement sans risque", "mesurer la température de la pièce", "remplacer les piles"], "tester un montage virtuellement sans risque", "On évite les erreurs de câblage et les courts-circuits."),
]),
notion('T-1', 0, I, 'tec-objets-societe', [
  Q("Quel objet a profondément modifié la vie domestique au XXe siècle en réduisant le temps des tâches ménagères ?", ["Le télégraphe", "Le lave-linge", "La machine à vapeur", "La boussole"], "Le lave-linge", "L'électroménager se diffuse en France surtout dans les années 1950-1970."),
  Q("Quel objet a transformé la communication en permettant d'être joignable partout dès les années 1990 ?", ["La radio", "Le téléphone mobile", "Le télégraphe", "Le fax"], "Le téléphone mobile", "Le smartphone, à partir de 2007, y ajoute Internet."),
  Q("Quelle conséquence sociale peut avoir l'automatisation ?", ["Aucune", "La transformation des métiers : certains disparaissent, d'autres apparaissent", "La fin de tout travail", "L'arrêt de la production"], "La transformation des métiers : certains disparaissent, d'autres apparaissent", "L'évolution technique modifie l'organisation du travail."),
]),
]

from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('S-1', 0, F, 'svt-structure-terre', [
  Q("Quelles sont, de la surface vers le centre, les grandes enveloppes de la Terre ?", ["Noyau, manteau, croûte", "Croûte, manteau, noyau", "Manteau, croûte, noyau", "Croûte, noyau, manteau"], "Croûte, manteau, noyau", "La croûte (continentale ou océanique) repose sur le manteau ; le noyau, au centre, est surtout composé de fer."),
  Q("Comment appelle-t-on l'enveloppe rigide externe de la Terre, découpée en plaques ?", ["L'atmosphère", "La lithosphère", "L'hydrosphère", "Le noyau"], "La lithosphère", "La lithosphère comprend la croûte et la partie supérieure du manteau ; elle est découpée en plaques."),
  Q("De quoi le noyau terrestre est-il principalement composé ?", ["De granite", "De fer et de nickel", "D'eau", "De basalte"], "De fer et de nickel", "Le noyau est métallique ; sa partie externe, liquide, est à l'origine du champ magnétique terrestre."),
]),
notion('S-1', 0, F, 'svt-plaques', [
  Q("Comment appelle-t-on les grands morceaux de lithosphère qui se déplacent lentement à la surface de la Terre ?", ["Les continents", "Les plaques lithosphériques (tectoniques)", "Les océans", "Les volcans"], "Les plaques lithosphériques (tectoniques)", "Les plaques se déplacent de quelques centimètres par an."),
  Q("À quelle vitesse moyenne se déplacent les plaques ?", ["Quelques centimètres par an", "Quelques kilomètres par an", "Un mètre par jour", "Elles ne bougent pas"], "Quelques centimètres par an", "C'est environ la vitesse de pousse des ongles."),
  Q("Où se produisent la plupart des séismes et des éruptions volcaniques ?", ["Au centre des plaques", "Aux limites des plaques", "Uniquement en Europe", "Au pôle Nord"], "Aux limites des plaques", "Les frontières de plaques concentrent l'activité sismique et volcanique, comme autour du Pacifique."),
]),
notion('S-1', 0, F, 'svt-seismes', [
  Q("Comment appelle-t-on le point en profondeur où se produit la rupture des roches lors d'un séisme ?", ["L'épicentre", "Le foyer", "La faille", "Le cratère"], "Le foyer", "Le foyer est en profondeur ; l'épicentre est le point de la surface situé à sa verticale."),
  Q("Qu'est-ce que l'épicentre d'un séisme ?", ["Le point en profondeur où les roches cassent", "Le point de la surface situé à la verticale du foyer", "Le volcan le plus proche", "La ville la plus touchée"], "Le point de la surface situé à la verticale du foyer", "C'est généralement près de l'épicentre que les dégâts sont les plus importants."),
  Q("Que mesure la magnitude d'un séisme ?", ["Les dégâts observés", "L'énergie libérée", "La durée", "La profondeur"], "L'énergie libérée", "La magnitude (échelle de Richter) mesure l'énergie ; l'intensité décrit les effets observés."),
]),
notion('S-1', 0, F, 'svt-volcans', [
  Q("Comment appelle-t-on la roche fondue qui sort d'un volcan ?", ["Le granite", "La lave", "Le calcaire", "Le sable"], "La lave", "En profondeur, la roche fondue s'appelle le magma ; en surface, c'est la lave."),
  Q("Un volcan qui émet des coulées de lave fluide est de type…", ["explosif", "effusif", "éteint", "sédimentaire"], "effusif", "Les éruptions effusives (Hawaï, Piton de la Fournaise) produisent des coulées de lave fluide ; les explosives projettent cendres et blocs."),
  Q("Quel volcan actif se trouve sur l'île de La Réunion ?", ["L'Etna", "Le Piton de la Fournaise", "La montagne Pelée", "Le Vésuve"], "Le Piton de la Fournaise", "C'est l'un des volcans les plus actifs du monde ; la montagne Pelée se trouve en Martinique."),
]),
notion('S-1', 1, F, 'svt-meteo-climat', [
  Q("Quelle est la différence entre météo et climat ?", ["Il n'y en a pas", "La météo décrit le temps sur quelques jours ; le climat, les conditions moyennes sur au moins 30 ans", "Le climat ne concerne que la pluie", "La météo concerne seulement les pôles"], "La météo décrit le temps sur quelques jours ; le climat, les conditions moyennes sur au moins 30 ans", "On ne peut pas déduire l'évolution du climat d'une seule journée froide ou chaude."),
  Q("Quel instrument mesure la pression atmosphérique ?", ["Le thermomètre", "Le baromètre", "Le pluviomètre", "L'anémomètre"], "Le baromètre", "Le pluviomètre mesure les précipitations et l'anémomètre la vitesse du vent."),
  Q("Quel instrument mesure la vitesse du vent ?", ["L'anémomètre", "Le baromètre", "L'hygromètre", "Le thermomètre"], "L'anémomètre", "L'hygromètre mesure l'humidité de l'air."),
]),
notion('S-1', 1, F, 'svt-cycle-eau', [
  Q("Quel phénomène transforme l'eau des océans en vapeur d'eau dans le cycle de l'eau ?", ["La condensation", "L'évaporation", "L'infiltration", "La solidification"], "L'évaporation", "Chauffée par le Soleil, l'eau s'évapore ; la vapeur se condense ensuite en nuages."),
  Q("Comment se forment les nuages ?", ["Par évaporation de la vapeur", "Par condensation de la vapeur d'eau en fines gouttelettes", "Par fusion de la glace", "Par infiltration"], "Par condensation de la vapeur d'eau en fines gouttelettes", "En se refroidissant en altitude, la vapeur se condense en gouttelettes ou en cristaux de glace."),
  Q("Comment appelle-t-on l'eau qui pénètre dans le sol pour rejoindre les nappes souterraines ?", ["Le ruissellement", "L'infiltration", "La transpiration", "La condensation"], "L'infiltration", "Le ruissellement est l'eau qui s'écoule à la surface vers les rivières."),
]),
notion('S-1', 2, F, 'svt-effet-serre', [
  Q("Sans effet de serre naturel, la température moyenne sur Terre serait d'environ…", ["+15 °C", "−18 °C", "+40 °C", "0 °C"], "−18 °C", "L'effet de serre naturel maintient une température moyenne d'environ +15 °C, favorable à la vie."),
  Q("Pourquoi le climat se réchauffe-t-il actuellement ?", ["À cause d'un rapprochement du Soleil", "À cause du renforcement de l'effet de serre par les gaz émis par les activités humaines", "À cause des volcans uniquement", "Le climat ne change pas"], "À cause du renforcement de l'effet de serre par les gaz émis par les activités humaines", "Le CO₂ et le méthane rejetés par l'activité humaine renforcent l'effet de serre."),
  Q("Lequel de ces gaz est un gaz à effet de serre ?", ["Le méthane", "Le dioxygène", "Le diazote", "L'argon"], "Le méthane", "Le méthane (élevage, rizières, décharges) est un puissant gaz à effet de serre, comme le CO₂."),
]),
notion('S-1', 3, F, 'svt-ressources', [
  Q("Laquelle de ces ressources est renouvelable à l'échelle humaine ?", ["Le pétrole", "Le bois des forêts gérées durablement", "Le charbon", "L'uranium"], "Le bois des forêts gérées durablement", "Une ressource est renouvelable si elle se reconstitue au rythme de son utilisation."),
  Q("Comment se sont formés le pétrole et le charbon ?", ["Par refroidissement de la lave", "Par transformation, sur des millions d'années, de restes d'êtres vivants", "Par condensation de l'eau", "Par l'activité humaine"], "Par transformation, sur des millions d'années, de restes d'êtres vivants", "Ce sont des combustibles fossiles, donc des ressources non renouvelables."),
  Q("Quel geste réduit la consommation de ressources ?", ["Jeter les objets réparables", "Trier, réparer et réutiliser les objets", "Laisser les appareils en veille", "Imprimer tous les courriels"], "Trier, réparer et réutiliser les objets", "Réduire, réutiliser, recycler limite l'exploitation des ressources et les déchets."),
]),
notion('S-1', 2, F, 'svt-pollution', [
  Q("Qu'est-ce que le tri sélectif des déchets ?", ["Brûler tous les déchets", "Séparer les déchets selon leur nature pour les recycler ou les traiter", "Enfouir tous les déchets", "Jeter les déchets dans la nature"], "Séparer les déchets selon leur nature pour les recycler ou les traiter", "Le tri permet le recyclage du verre, du papier, des emballages…"),
  Q("Quelle pollution menace particulièrement les océans ?", ["Les déchets plastiques", "Le sable", "Les coquillages", "Le sel"], "Les déchets plastiques", "Les plastiques se fragmentent en microplastiques ingérés par les animaux marins."),
  Q("Quel matériau peut être recyclé à l'infini sans perdre ses qualités ?", ["Le verre", "Le papier", "Le plastique", "Le carton"], "Le verre", "Le verre se recycle indéfiniment ; les fibres de papier s'abîment à chaque recyclage."),
]),
notion('S-1', 2, F, 'svt-biodiversite-menaces', [
  Q("Quelle est la principale cause actuelle de perte de biodiversité ?", ["Les volcans", "La destruction et la fragmentation des milieux naturels", "Les marées", "La lumière de la Lune"], "La destruction et la fragmentation des milieux naturels", "Urbanisation, déforestation, agriculture intensive détruisent les habitats ; s'y ajoutent pollution, surexploitation, espèces invasives et changement climatique."),
  Q("Comment appelle-t-on une espèce introduite par l'humain qui prolifère au détriment des espèces locales ?", ["Une espèce endémique", "Une espèce exotique envahissante", "Une espèce protégée", "Une espèce fossile"], "Une espèce exotique envahissante", "Le frelon asiatique en France en est un exemple."),
  Q("Quels insectes jouent un rôle essentiel dans la pollinisation des cultures ?", ["Les moustiques", "Les abeilles", "Les puces", "Les fourmis seulement"], "Les abeilles", "Les pollinisateurs, menacés notamment par certains pesticides, sont indispensables à de nombreuses cultures."),
]),
notion('S-1', 0, F, 'svt-terre-systeme-solaire', [
  N("Quel est le rang de la Terre dans l'ordre des planètes à partir du Soleil ?", 3, "Mercure, Vénus, Terre : la Terre est la troisième planète."),
  Q("Combien de temps la Terre met-elle pour faire un tour autour du Soleil ?", ["24 heures", "Environ 365 jours", "28 jours", "10 ans"], "Environ 365 jours", "C'est la révolution de la Terre ; elle tourne sur elle-même en environ 24 heures."),
  N("Combien de planètes compte le système solaire ?", 8, "Mercure, Vénus, Terre, Mars, Jupiter, Saturne, Uranus et Neptune ; Pluton est une planète naine depuis 2006."),
]),
notion('S-1', 1, F, 'svt-saisons', [
  Q("Quelle est la cause des saisons ?", ["La distance Terre-Soleil", "L'inclinaison de l'axe de rotation de la Terre", "La rotation de la Lune", "Les nuages"], "L'inclinaison de l'axe de rotation de la Terre", "L'axe incliné d'environ 23° fait varier l'inclinaison des rayons et la durée du jour au cours de l'année."),
  Q("En France, quand les journées sont-elles les plus longues ?", ["Au solstice d'hiver", "Au solstice d'été", "À l'équinoxe de printemps", "À l'équinoxe d'automne"], "Au solstice d'été", "Le solstice d'été (vers le 21 juin) correspond au jour le plus long dans l'hémisphère Nord."),
  Q("Quand l'hémisphère Nord est en été, quelle saison connaît l'hémisphère Sud ?", ["L'été aussi", "L'hiver", "Le printemps", "Il n'y a pas de saisons"], "L'hiver", "Les saisons sont inversées entre les deux hémisphères."),
]),
notion('S-1', 0, F, 'svt-fossiles-roches', [
  Q("Qu'est-ce qu'un fossile ?", ["Une roche volcanique", "Un reste ou une trace d'être vivant conservé dans une roche", "Un cristal", "Un minéral précieux"], "Un reste ou une trace d'être vivant conservé dans une roche", "Les fossiles se forment surtout dans les roches sédimentaires."),
  Q("Dans quel type de roche trouve-t-on le plus souvent des fossiles ?", ["Les roches sédimentaires", "Les roches magmatiques", "Le granite", "Le basalte"], "Les roches sédimentaires", "Les sédiments, déposés en couches, enfouissent et conservent les restes d'êtres vivants."),
  Q("Le calcaire est une roche…", ["volcanique", "sédimentaire", "métallique", "liquide"], "sédimentaire", "Le calcaire se forme souvent à partir de coquilles et squelettes accumulés au fond des mers."),
]),
notion('S-2', 0, F, 'svt-cellule', [
  Q("Quelle est l'unité de base de tout être vivant ?", ["L'organe", "La cellule", "Le tissu", "L'atome"], "La cellule", "Tous les êtres vivants sont formés d'une ou de plusieurs cellules."),
  Q("Quel instrument permet d'observer des cellules ?", ["La loupe à main seule", "Le microscope", "Le télescope", "Le thermomètre"], "Le microscope", "La plupart des cellules mesurent quelques dizaines de micromètres : il faut un microscope."),
  Q("Quel élément se trouve dans toutes les cellules végétales mais pas dans les cellules animales ?", ["Le noyau", "La paroi", "La membrane", "Le cytoplasme"], "La paroi", "Les cellules végétales ont une paroi (cellulose) et souvent des chloroplastes, absents chez les animaux."),
]),
notion('S-2', 3, F, 'svt-adn-chromosomes', [
  Q("Où se trouvent les chromosomes dans une cellule humaine ?", ["Dans la membrane", "Dans le noyau", "Dans le sang uniquement", "À l'extérieur de la cellule"], "Dans le noyau", "Les chromosomes, formés d'ADN, portent l'information génétique."),
  N("Combien de chromosomes contient une cellule humaine (hors cellules reproductrices) ?", 46, "46 chromosomes, soit 23 paires ; les gamètes en contiennent 23."),
  Q("Quelle molécule porte l'information génétique ?", ["Le glucose", "L'ADN", "L'amidon", "L'hémoglobine"], "L'ADN", "L'ADN contient les gènes, qui déterminent les caractères héréditaires."),
]),
notion('S-2', 1, F, 'svt-photosynthese', [
  Q("De quoi une plante verte a-t-elle besoin pour fabriquer sa matière organique ?", ["De sucre et d'oxygène", "De lumière, d'eau, de dioxyde de carbone et de sels minéraux", "De terre uniquement", "De viande"], "De lumière, d'eau, de dioxyde de carbone et de sels minéraux", "Grâce à la photosynthèse, la plante produit sa matière (glucides) et rejette du dioxygène."),
  Q("Quel gaz les plantes vertes rejettent-elles à la lumière ?", ["Le dioxyde de carbone", "Le dioxygène", "L'azote", "Le méthane"], "Le dioxygène", "La photosynthèse libère du dioxygène."),
  Q("Dans quels éléments des cellules se déroule la photosynthèse ?", ["Les mitochondries", "Les chloroplastes", "Le noyau", "La paroi"], "Les chloroplastes", "Les chloroplastes contiennent la chlorophylle, pigment vert qui capte la lumière."),
]),
notion('S-2', 1, F, 'svt-respiration-etres-vivants', [
  Q("Quel gaz les êtres vivants absorbent-ils en respirant ?", ["Le dioxyde de carbone", "Le dioxygène", "L'hélium", "Le méthane"], "Le dioxygène", "Les cellules utilisent le dioxygène pour produire de l'énergie et rejettent du CO₂."),
  Q("Les plantes respirent-elles ?", ["Non, jamais", "Oui, jour et nuit", "Seulement la nuit", "Seulement en hiver"], "Oui, jour et nuit", "Les plantes respirent en permanence ; le jour, la photosynthèse masque cette respiration."),
  Q("Par quel organe un poisson prélève-t-il le dioxygène dissous dans l'eau ?", ["Les poumons", "Les branchies", "La peau uniquement", "Les nageoires"], "Les branchies", "Chaque organe respiratoire est adapté au milieu de vie."),
]),
notion('S-2', 2, F, 'svt-chaine-alimentaire', [
  Q("Dans une chaîne alimentaire, que signifie la flèche « herbe → lapin » ?", ["Le lapin est mangé par l'herbe", "L'herbe est mangée par le lapin", "Ils vivent ensemble", "Ils sont de la même espèce"], "L'herbe est mangée par le lapin", "La flèche signifie « est mangé par » : elle indique le sens de transfert de la matière."),
  Q("Comment appelle-t-on un animal qui se nourrit uniquement de végétaux ?", ["Un carnivore", "Un herbivore", "Un omnivore", "Un décomposeur"], "Un herbivore", "L'omnivore mange des végétaux et des animaux."),
  Q("Quel est toujours le premier maillon d'une chaîne alimentaire ?", ["Un carnivore", "Un végétal chlorophyllien (producteur)", "Un décomposeur", "Un herbivore"], "Un végétal chlorophyllien (producteur)", "Les producteurs fabriquent leur matière grâce à la photosynthèse."),
]),
notion('S-2', 1, F, 'svt-decomposeurs', [
  Q("Quel est le rôle des décomposeurs (vers de terre, champignons, bactéries) ?", ["Produire de la lumière", "Transformer la matière morte en matière minérale", "Polliniser les fleurs", "Chasser les herbivores"], "Transformer la matière morte en matière minérale", "Ils recyclent la matière et enrichissent le sol en sels minéraux utilisés par les plantes."),
  Q("Comment appelle-t-on la couche de sol riche en matière organique en décomposition ?", ["L'humus", "Le granite", "Le sable", "La lave"], "L'humus", "L'humus, issu de la décomposition des feuilles et des êtres morts, rend le sol fertile."),
  Q("Qu'obtient-on en compostant des épluchures ?", ["Du plastique", "Un engrais naturel (compost)", "Du pétrole", "Du verre"], "Un engrais naturel (compost)", "Le compost est produit par l'action des décomposeurs."),
]),
notion('S-2', 2, F, 'svt-vertebres', [
  Q("Qu'ont en commun tous les vertébrés ?", ["Des plumes", "Un squelette interne avec une colonne vertébrale", "Des écailles", "Six pattes"], "Un squelette interne avec une colonne vertébrale", "Poissons, amphibiens, reptiles, oiseaux et mammifères sont des vertébrés."),
  Q("Quel caractère est propre aux mammifères ?", ["Pondre des œufs", "Avoir des mamelles et des poils", "Avoir des plumes", "Respirer par des branchies"], "Avoir des mamelles et des poils", "Les mammifères allaitent leurs petits ; l'ornithorynque pond pourtant des œufs."),
  Q("À quel groupe appartient la chauve-souris ?", ["Les oiseaux", "Les mammifères", "Les insectes", "Les reptiles"], "Les mammifères", "Elle vole, mais elle a des poils et allaite ses petits."),
]),
notion('S-2', 2, F, 'svt-classification', [
  Q("Sur quoi repose la classification scientifique actuelle du vivant ?", ["Le lieu de vie", "Les attributs (caractères) partagés par les êtres vivants", "La taille", "L'utilité pour l'humain"], "Les attributs (caractères) partagés par les êtres vivants", "On regroupe les êtres vivants qui partagent des attributs, en groupes emboîtés."),
  Q("Pourquoi la baleine n'est-elle pas classée avec les poissons ?", ["Parce qu'elle est grande", "Parce qu'elle possède des mamelles, des poumons et des poils, comme les mammifères", "Parce qu'elle vit dans l'océan", "Parce qu'elle mange du plancton"], "Parce qu'elle possède des mamelles, des poumons et des poils, comme les mammifères", "On classe selon ce que les êtres vivants ont, pas selon leur milieu de vie."),
  Q("Combien de pattes ont les insectes ?", ["4", "6", "8", "10"], "6", "Les insectes ont 6 pattes ; les araignées (arachnides) en ont 8."),
]),
notion('S-2', 3, F, 'svt-reproduction-plantes', [
  Q("Quel organe de la plante assure la reproduction sexuée ?", ["La racine", "La fleur", "La tige", "La feuille"], "La fleur", "La fleur contient les organes reproducteurs : étamines (pollen) et pistil (ovules)."),
  Q("Comment appelle-t-on le transport du pollen d'une fleur à une autre ?", ["La germination", "La pollinisation", "La photosynthèse", "La fécondation interne"], "La pollinisation", "Elle est assurée par le vent ou les animaux (insectes surtout)."),
  Q("Que devient le pistil d'une fleur après la fécondation ?", ["Une racine", "Un fruit contenant des graines", "Une feuille", "Une tige"], "Un fruit contenant des graines", "Les ovules fécondés deviennent des graines, et l'ovaire devient le fruit."),
]),
notion('S-2', 3, F, 'svt-germination', [
  Q("De quoi une graine a-t-elle besoin pour germer ?", ["De lumière obligatoirement", "D'eau, d'une température favorable et de dioxygène", "D'engrais chimique", "De sel"], "D'eau, d'une température favorable et de dioxygène", "La plupart des graines n'ont pas besoin de lumière pour germer ; la plantule en aura besoin ensuite."),
  Q("Que contient une graine ?", ["Un embryon de plante et des réserves nutritives", "Seulement de l'eau", "Une fleur", "Un fruit"], "Un embryon de plante et des réserves nutritives", "Les réserves nourrissent l'embryon pendant la germination."),
  Q("Comment appelle-t-on la jeune plante qui sort de la graine ?", ["La plantule", "Le bourgeon", "La racine adulte", "Le pétale"], "La plantule", "La plantule développe ensuite racines, tige et feuilles."),
]),
notion('S-2', 4, F, 'svt-evolution', [
  Q("Quel naturaliste publie en 1859 L'Origine des espèces ?", ["Lamarck", "Charles Darwin", "Pasteur", "Mendel"], "Charles Darwin", "Darwin explique l'évolution des espèces par la sélection naturelle."),
  Q("Que montrent les fossiles sur l'histoire de la vie ?", ["Que les espèces n'ont jamais changé", "Que des espèces ont disparu et que d'autres sont apparues au cours du temps", "Que les dinosaures vivent encore", "Rien"], "Que des espèces ont disparu et que d'autres sont apparues au cours du temps", "Les fossiles témoignent de l'évolution du vivant."),
  Q("Les êtres humains et les chimpanzés…", ["descendent l'un de l'autre", "partagent un ancêtre commun", "n'ont aucun lien de parenté", "sont la même espèce"], "partagent un ancêtre commun", "Ils ne descendent pas l'un de l'autre mais d'un ancêtre commun ayant vécu il y a environ 7 millions d'années."),
]),
notion('S-2', 3, F, 'svt-espece', [
  Q("Qu'est-ce qu'une espèce ?", ["Des êtres vivants qui se ressemblent un peu", "Des individus qui peuvent se reproduire entre eux et avoir une descendance fertile", "Tous les animaux d'un même pays", "Les animaux de même couleur"], "Des individus qui peuvent se reproduire entre eux et avoir une descendance fertile", "Le cheval et l'âne donnent une mule stérile : ce sont deux espèces différentes."),
  Q("Qu'est-ce que la biodiversité ?", ["Le nombre d'humains", "La diversité du vivant : écosystèmes, espèces et diversité génétique des individus", "Le nombre d'arbres d'une forêt", "La variété des roches"], "La diversité du vivant : écosystèmes, espèces et diversité génétique des individus", "La biodiversité s'observe à trois échelles."),
  Q("Pourquoi deux individus d'une même espèce ne sont-ils pas identiques ?", ["Parce qu'ils ont exactement les mêmes gènes", "Parce qu'ils ont des versions différentes de certains gènes (allèles) et vivent dans des environnements différents", "Par hasard uniquement", "Ils le sont toujours"], "Parce qu'ils ont des versions différentes de certains gènes (allèles) et vivent dans des environnements différents", "La diversité génétique et l'environnement expliquent les différences entre individus."),
]),
notion('S-3', 1, F, 'svt-appareil-digestif', [
  Q("Dans quel ordre les aliments traversent-ils le tube digestif ?", ["Bouche, estomac, œsophage, intestin", "Bouche, œsophage, estomac, intestin grêle, gros intestin", "Bouche, intestin, estomac, œsophage", "Estomac, bouche, intestin"], "Bouche, œsophage, estomac, intestin grêle, gros intestin", "Les aliments sont progressivement transformés en nutriments."),
  Q("Dans quel organe les nutriments passent-ils dans le sang ?", ["L'estomac", "L'intestin grêle", "L'œsophage", "La bouche"], "L'intestin grêle", "La paroi de l'intestin grêle, très repliée, permet l'absorption des nutriments."),
  Q("Comment appelle-t-on la transformation des aliments en nutriments ?", ["La respiration", "La digestion", "La circulation", "La photosynthèse"], "La digestion", "La digestion est mécanique (dents, estomac) et chimique (enzymes des sucs digestifs)."),
]),
notion('S-3', 0, F, 'svt-respiration-humaine', [
  Q("Où se font les échanges de gaz entre l'air et le sang ?", ["Dans la trachée", "Dans les alvéoles pulmonaires", "Dans le cœur", "Dans l'estomac"], "Dans les alvéoles pulmonaires", "Le dioxygène passe dans le sang et le CO₂ en sort à travers la paroi très fine des alvéoles."),
  Q("Quel gaz l'air expiré contient-il en plus grande quantité que l'air inspiré ?", ["Le dioxygène", "Le dioxyde de carbone", "L'azote", "L'hélium"], "Le dioxyde de carbone", "Le CO₂ produit par les cellules est rejeté par les poumons."),
  Q("Quel muscle permet principalement l'entrée de l'air dans les poumons ?", ["Le biceps", "Le diaphragme", "Le cœur", "Le quadriceps"], "Le diaphragme", "En se contractant, le diaphragme augmente le volume de la cage thoracique : l'air entre."),
]),
notion('S-3', 0, F, 'svt-coeur-circulation', [
  N("Combien de cavités compte le cœur humain ?", 4, "Deux oreillettes et deux ventricules."),
  Q("Quel est le rôle du cœur ?", ["Filtrer le sang", "Mettre le sang en mouvement dans les vaisseaux", "Produire les globules rouges", "Digérer les aliments"], "Mettre le sang en mouvement dans les vaisseaux", "Le cœur est un muscle qui fonctionne comme une pompe."),
  Q("Comment appelle-t-on les vaisseaux qui partent du cœur ?", ["Les veines", "Les artères", "Les nerfs", "Les tendons"], "Les artères", "Les artères partent du cœur ; les veines y ramènent le sang."),
]),
notion('S-3', 0, F, 'svt-sang', [
  Q("Quel est le rôle des globules rouges ?", ["Défendre l'organisme", "Transporter le dioxygène", "Coaguler le sang", "Digérer"], "Transporter le dioxygène", "Ils contiennent l'hémoglobine qui fixe le dioxygène."),
  Q("Quel est le rôle des plaquettes ?", ["Transporter le dioxygène", "Participer à la coagulation du sang", "Combattre les microbes", "Produire des hormones"], "Participer à la coagulation du sang", "Les plaquettes permettent d'arrêter un saignement."),
  Q("Quel est le rôle des globules blancs ?", ["Défendre l'organisme contre les micro-organismes", "Transporter les nutriments", "Coaguler le sang", "Donner sa couleur au sang"], "Défendre l'organisme contre les micro-organismes", "Ils sont les acteurs du système immunitaire."),
]),
notion('S-3', 0, F, 'svt-systeme-nerveux', [
  Q("Quel organe commande les mouvements volontaires ?", ["Le cœur", "Le cerveau", "L'estomac", "Le foie"], "Le cerveau", "Le cerveau envoie des messages nerveux aux muscles par la moelle épinière et les nerfs."),
  Q("Par quoi circulent les messages nerveux entre le cerveau et les organes ?", ["Par les artères", "Par les nerfs et la moelle épinière", "Par les os", "Par l'air"], "Par les nerfs et la moelle épinière", "Le message nerveux est de nature électrique le long des neurones."),
  Q("Comment appelle-t-on les cellules du système nerveux ?", ["Les neurones", "Les globules", "Les alvéoles", "Les chromosomes"], "Les neurones", "Le cerveau humain contient environ 86 milliards de neurones."),
]),
notion('S-3', 0, F, 'svt-mouvement', [
  Q("Que fait un muscle quand il se contracte ?", ["Il s'allonge", "Il se raccourcit et tire sur l'os", "Il disparaît", "Il produit du sang"], "Il se raccourcit et tire sur l'os", "Les muscles sont reliés aux os par les tendons ; en se contractant, ils font bouger les os au niveau des articulations."),
  Q("Qu'est-ce qui relie un muscle à un os ?", ["Un ligament", "Un tendon", "Un nerf", "Une veine"], "Un tendon", "Les ligaments, eux, relient les os entre eux au niveau des articulations."),
  Q("Comment appelle-t-on la zone où deux os se rejoignent et peuvent bouger l'un par rapport à l'autre ?", ["Une articulation", "Un tendon", "Un muscle", "Une vertèbre"], "Une articulation", "Le genou, le coude ou l'épaule sont des articulations."),
]),
notion('S-3', 1, F, 'svt-microbes', [
  Q("Les bactéries sont…", ["toutes dangereuses", "des êtres vivants unicellulaires, dont beaucoup sont utiles", "des virus", "des champignons"], "des êtres vivants unicellulaires, dont beaucoup sont utiles", "Le microbiote intestinal, composé de bactéries, est indispensable à la santé ; certaines bactéries sont pathogènes."),
  Q("Un virus peut-il se multiplier seul, hors d'une cellule ?", ["Oui", "Non, il doit infecter une cellule pour se multiplier", "Seulement dans l'eau", "Seulement la nuit"], "Non, il doit infecter une cellule pour se multiplier", "Le virus utilise la machinerie de la cellule qu'il infecte."),
  Q("Quel aliment est fabriqué grâce à des micro-organismes ?", ["Le yaourt", "Le sel", "Le sucre en morceaux", "L'eau minérale"], "Le yaourt", "Des bactéries transforment le lait en yaourt ; des levures font lever le pain."),
]),
notion('S-3', 3, F, 'svt-vaccination', [
  Q("Comment agit un vaccin ?", ["Il tue directement les microbes", "Il prépare le système immunitaire à reconnaître un microbe avant d'y être exposé", "Il remplace les globules blancs", "Il guérit toutes les maladies"], "Il prépare le système immunitaire à reconnaître un microbe avant d'y être exposé", "La vaccination crée une mémoire immunitaire."),
  Q("Quel savant met au point le vaccin contre la rage en 1885 ?", ["Louis Pasteur", "Marie Curie", "Robert Koch", "Alexander Fleming"], "Louis Pasteur", "Pasteur vaccine avec succès le jeune Joseph Meister en 1885."),
  Q("Pourquoi dit-on que la vaccination protège aussi les autres ?", ["Elle n'a aucun effet sur les autres", "Plus la population est vaccinée, moins le microbe circule, ce qui protège aussi les personnes fragiles", "Elle rend contagieux", "Elle remplace l'hygiène"], "Plus la population est vaccinée, moins le microbe circule, ce qui protège aussi les personnes fragiles", "C'est l'immunité collective."),
]),
notion('S-3', 3, F, 'svt-antibiotiques', [
  Q("Contre quels microbes les antibiotiques sont-ils efficaces ?", ["Les virus", "Les bactéries", "Tous les microbes", "Les champignons uniquement"], "Les bactéries", "Les antibiotiques n'agissent pas sur les virus (grippe, rhume…)."),
  Q("Qui découvre la pénicilline, premier antibiotique, en 1928 ?", ["Louis Pasteur", "Alexander Fleming", "Charles Darwin", "Claude Bernard"], "Alexander Fleming", "Fleming observe qu'une moisissure empêche le développement de bactéries."),
  Q("Pourquoi faut-il éviter de prendre des antibiotiques sans nécessité ?", ["Ils coûtent cher seulement", "Cela favorise l'apparition de bactéries résistantes", "Ils rendent malade à coup sûr", "Ils sont interdits"], "Cela favorise l'apparition de bactéries résistantes", "« Les antibiotiques, c'est pas automatique » : leur abus rend les bactéries résistantes."),
]),
notion('S-3', 3, F, 'svt-hygiene', [
  Q("Quel geste simple limite le plus la transmission des microbes ?", ["Se laver les mains régulièrement au savon", "Boire beaucoup d'eau", "Dormir plus", "Manger des sucreries"], "Se laver les mains régulièrement au savon", "Le lavage des mains réduit fortement la transmission des infections."),
  Q("Que faut-il faire d'une plaie pour éviter l'infection ?", ["La laisser sale", "La nettoyer et la désinfecter", "La couvrir de terre", "La gratter"], "La nettoyer et la désinfecter", "Un antiseptique limite la prolifération des microbes."),
  Q("Pourquoi éternuer dans son coude ?", ["C'est plus confortable", "Pour éviter de contaminer ses mains et les objets", "Pour faire moins de bruit", "Cela n'a aucune utilité"], "Pour éviter de contaminer ses mains et les objets", "Les mains transmettent ensuite les microbes à ce qu'elles touchent."),
]),
notion('S-3', 2, F, 'svt-puberte', [
  Q("Comment appelle-t-on la période où le corps devient capable de se reproduire ?", ["L'enfance", "La puberté", "La ménopause", "La vieillesse"], "La puberté", "La puberté commence généralement entre 9 et 14 ans, sous l'effet d'hormones."),
  Q("Quelles cellules reproductrices les testicules produisent-ils ?", ["Les ovules", "Les spermatozoïdes", "Les globules", "Les neurones"], "Les spermatozoïdes", "Les ovaires produisent les ovules."),
  Q("Qu'est-ce qui déclenche les transformations de la puberté ?", ["Les hormones sexuelles", "L'alimentation seule", "Le sport", "Le hasard"], "Les hormones sexuelles", "Testostérone chez les garçons, œstrogènes et progestérone chez les filles."),
]),
notion('S-3', 2, F, 'svt-fecondation', [
  Q("Comment appelle-t-on la rencontre d'un spermatozoïde et d'un ovule ?", ["La pollinisation", "La fécondation", "La digestion", "La germination"], "La fécondation", "La fécondation donne une cellule-œuf, première cellule d'un nouvel individu."),
  Q("Où a lieu la fécondation chez l'être humain ?", ["Dans l'utérus", "Dans une trompe (oviducte)", "Dans l'ovaire", "Dans le vagin"], "Dans une trompe (oviducte)", "La cellule-œuf migre ensuite vers l'utérus où elle s'implante."),
  N("Combien de mois dure environ une grossesse humaine ?", 9, "Une grossesse dure environ 9 mois, soit environ 38 semaines après la fécondation."),
]),
notion('S-3', 3, F, 'svt-ist-contraception', [
  Q("Quel moyen protège à la fois des infections sexuellement transmissibles et d'une grossesse ?", ["La pilule", "Le préservatif", "Le stérilet", "L'implant"], "Le préservatif", "Le préservatif est le seul contraceptif qui protège aussi des IST."),
  Q("Le VIH est…", ["une bactérie", "un virus", "un champignon", "un parasite"], "un virus", "Le VIH s'attaque au système immunitaire ; il se transmet notamment lors de rapports sexuels non protégés."),
  Q("Qu'est-ce qu'une IST ?", ["Une infection sexuellement transmissible", "Un instrument scientifique", "Une institution", "Une vitamine"], "Une infection sexuellement transmissible", "Le dépistage et la protection sont les meilleurs moyens de lutter contre les IST."),
]),
notion('S-3', 3, F, 'svt-alimentation-equilibree', [
  Q("Quel groupe d'aliments fournit principalement des protéines ?", ["Les fruits", "La viande, le poisson, les œufs et les légumineuses", "Les sucreries", "Les matières grasses"], "La viande, le poisson, les œufs et les légumineuses", "Les protéines servent à construire et entretenir les cellules."),
  Q("Quels nutriments fournissent surtout de l'énergie rapidement utilisable ?", ["Les glucides", "Les vitamines", "Les sels minéraux", "L'eau"], "Les glucides", "Pâtes, pain, riz, féculents apportent des glucides, carburant des cellules."),
  Q("Combien de portions de fruits et légumes est-il recommandé de manger par jour ?", ["Une", "Au moins cinq", "Aucune", "Vingt"], "Au moins cinq", "C'est la recommandation du Programme national nutrition santé."),
]),
notion('S-3', 3, F, 'svt-sommeil', [
  Q("Pourquoi le sommeil est-il indispensable ?", ["Il ne sert à rien", "Il permet la récupération du corps, la croissance et la mémorisation", "Il remplace l'alimentation", "Il évite d'aller à l'école"], "Il permet la récupération du corps, la croissance et la mémorisation", "Pendant le sommeil, l'hormone de croissance est sécrétée et les apprentissages se consolident."),
  Q("Combien d'heures de sommeil sont recommandées pour un enfant de 6 à 12 ans ?", ["4 à 5 heures", "9 à 12 heures", "15 à 18 heures", "6 heures"], "9 à 12 heures", "Les recommandations pour cet âge vont de 9 à 12 heures par nuit."),
  Q("Pourquoi éviter les écrans juste avant de dormir ?", ["Ils fatiguent les jambes", "Leur lumière retarde l'endormissement", "Ils font grossir", "Ils refroidissent la chambre"], "Leur lumière retarde l'endormissement", "La lumière bleue perturbe la sécrétion de mélatonine, hormone du sommeil."),
]),
notion('S-3', 0, F, 'svt-effort', [
  Q("Que se passe-t-il pendant un effort physique ?", ["Le cœur ralentit", "Les fréquences cardiaque et respiratoire augmentent", "La respiration s'arrête", "Rien ne change"], "Les fréquences cardiaque et respiratoire augmentent", "Les muscles ont besoin de plus de dioxygène et de nutriments."),
  Q("Pourquoi le cœur bat-il plus vite pendant l'effort ?", ["Pour apporter plus de dioxygène et de nutriments aux muscles", "Pour digérer", "Pour dormir", "Par hasard"], "Pour apporter plus de dioxygène et de nutriments aux muscles", "Le débit sanguin augmente vers les muscles en activité."),
  Q("Combien de temps d'activité physique par jour est recommandé pour les enfants et adolescents ?", ["10 minutes", "Au moins 60 minutes", "3 heures minimum", "Aucune"], "Au moins 60 minutes", "L'OMS recommande au moins une heure d'activité physique modérée à intense par jour."),
]),
notion('S-3', 3, F, 'svt-tabac-alcool', [
  Q("Quelle substance du tabac est responsable de la dépendance ?", ["Le goudron", "La nicotine", "Le monoxyde de carbone", "L'eau"], "La nicotine", "La nicotine rend dépendant ; les goudrons sont cancérigènes."),
  Q("Quel organe est particulièrement abîmé par une consommation excessive d'alcool ?", ["Le foie", "Les ongles", "Les cheveux", "Les dents uniquement"], "Le foie", "L'alcool est toxique pour le foie et le cerveau, surtout pendant l'adolescence."),
  Q("La vente de tabac et d'alcool aux mineurs est…", ["autorisée", "interdite", "autorisée le week-end", "autorisée avec un adulte"], "interdite", "La loi interdit la vente d'alcool et de tabac aux moins de 18 ans."),
]),
notion('S-3', 0, F, 'svt-organes-sens', [
  Q("Quel organe des sens capte les sons ?", ["L'œil", "L'oreille", "La peau", "Le nez"], "L'oreille", "L'oreille transforme les vibrations sonores en messages nerveux envoyés au cerveau."),
  Q("Quelle partie de l'œil reçoit l'image et la transmet au cerveau ?", ["La pupille", "La rétine", "L'iris", "Le cristallin seul"], "La rétine", "La rétine contient des cellules sensibles à la lumière reliées au nerf optique."),
  Q("Quel organe intervient aussi dans l'équilibre ?", ["L'oreille interne", "L'estomac", "Le foie", "La peau"], "L'oreille interne", "L'oreille interne contient des organes de l'équilibre."),
]),
notion('S-3', 3, F, 'svt-ecrans-sante', [
  Q("Quel risque peut entraîner une exposition excessive aux écrans chez l'enfant ?", ["Une meilleure vue", "Des troubles du sommeil, de l'attention et de la sédentarité", "Une croissance plus rapide", "Aucun risque"], "Des troubles du sommeil, de l'attention et de la sédentarité", "Les recommandations limitent fortement les écrans chez les plus jeunes."),
  Q("Qu'est-ce que la sédentarité ?", ["Faire beaucoup de sport", "Rester longtemps assis ou allongé sans activité physique", "Dormir la nuit", "Manger équilibré"], "Rester longtemps assis ou allongé sans activité physique", "Elle augmente les risques cardiovasculaires et d'obésité."),
  Q("Que recommandent les autorités de santé pour les enfants de moins de 3 ans ?", ["Au moins 2 heures d'écran par jour", "Pas d'exposition aux écrans", "Une tablette personnelle", "La télévision pendant les repas"], "Pas d'exposition aux écrans", "Le rapport de la commission « Enfants et écrans » (2024) recommande aucun écran avant 3 ans."),
]),
notion('S-3', 1, F, 'svt-microbiote', [
  Q("Comment appelle-t-on l'ensemble des micro-organismes qui vivent dans notre intestin ?", ["Le microbiote intestinal", "Le système nerveux", "Le plasma", "Les anticorps"], "Le microbiote intestinal", "Il participe à la digestion et à la défense de l'organisme."),
  Q("Le microbiote intestinal est…", ["toujours dangereux", "utile à la santé", "composé de virus seulement", "inexistant chez l'enfant"], "utile à la santé", "Il compte des milliers de milliards de bactéries bénéfiques."),
  Q("Quel aliment favorise un microbiote équilibré ?", ["Les aliments riches en fibres (fruits, légumes, céréales complètes)", "Les sodas", "Les bonbons", "Les chips"], "Les aliments riches en fibres (fruits, légumes, céréales complètes)", "Les fibres nourrissent les bonnes bactéries de l'intestin."),
]),
notion('S-1', 3, F, 'svt-eau-potable', [
  Q("Comment rend-on l'eau des rivières potable ?", ["En la chauffant seulement", "En la traitant dans une usine de potabilisation (filtration, désinfection…)", "En y ajoutant du sucre", "On ne peut pas"], "En la traitant dans une usine de potabilisation (filtration, désinfection…)", "L'eau est décantée, filtrée et désinfectée avant d'être distribuée."),
  Q("Où vont les eaux usées d'une maison raccordée au réseau ?", ["Directement à la rivière", "À la station d'épuration", "Dans le réservoir d'eau potable", "Dans la mer sans traitement"], "À la station d'épuration", "La station d'épuration nettoie l'eau avant son rejet dans le milieu naturel."),
  Q("Quel geste économise l'eau ?", ["Prendre une douche plutôt qu'un bain", "Laisser couler le robinet en se brossant les dents", "Laver la voiture tous les jours", "Arroser en plein soleil"], "Prendre une douche plutôt qu'un bain", "Une douche consomme en général bien moins d'eau qu'un bain."),
]),
notion('S-1', 2, F, 'svt-deforestation', [
  Q("Quelle est une conséquence de la déforestation ?", ["Plus de biodiversité", "La perte d'habitats et l'augmentation du CO₂ dans l'atmosphère", "Une baisse des températures", "Plus d'oxygène dans l'air"], "La perte d'habitats et l'augmentation du CO₂ dans l'atmosphère", "Les forêts stockent du carbone et abritent une grande partie de la biodiversité terrestre."),
  Q("Quelle forêt est souvent appelée « poumon de la planète » ?", ["La forêt amazonienne", "La forêt de Fontainebleau", "La taïga canadienne seulement", "La forêt des Landes"], "La forêt amazonienne", "Elle abrite une biodiversité exceptionnelle et stocke beaucoup de carbone."),
  Q("Qu'est-ce qu'un puits de carbone ?", ["Un trou dans le sol", "Un milieu qui absorbe et stocke plus de carbone qu'il n'en rejette (forêt, océan…)", "Une mine de charbon", "Une centrale électrique"], "Un milieu qui absorbe et stocke plus de carbone qu'il n'en rejette (forêt, océan…)", "Forêts, océans et sols sont les principaux puits de carbone."),
]),
notion('S-2', 3, F, 'svt-heredite', [
  Q("Comment appelle-t-on un caractère transmis des parents aux enfants ?", ["Un caractère acquis", "Un caractère héréditaire", "Un caractère inventé", "Un caractère obligatoire"], "Un caractère héréditaire", "Le groupe sanguin est héréditaire ; une cicatrice est acquise."),
  Q("Lequel de ces caractères n'est pas héréditaire ?", ["Le groupe sanguin", "La couleur naturelle des yeux", "Une cicatrice", "La forme du lobe de l'oreille"], "Une cicatrice", "Une cicatrice résulte d'un événement de la vie : c'est un caractère acquis."),
  Q("Pourquoi un enfant ressemble-t-il à ses deux parents ?", ["Il reçoit la moitié de ses chromosomes de chacun d'eux", "Il ne reçoit des gènes que de sa mère", "Il ne reçoit des gènes que de son père", "Par hasard uniquement"], "Il reçoit la moitié de ses chromosomes de chacun d'eux", "Chaque parent transmet 23 chromosomes par ses cellules reproductrices."),
]),
notion('S-1', 0, F, 'svt-relief-erosion', [
  Q("Comment appelle-t-on l'usure des roches par l'eau, le vent ou la glace ?", ["L'érosion", "La sédimentation", "La fusion", "La subduction"], "L'érosion", "L'érosion façonne les paysages ; les particules arrachées sont transportées puis déposées."),
  Q("Comment appelle-t-on le dépôt de particules (sable, argile…) au fond de l'eau ?", ["La sédimentation", "L'érosion", "L'évaporation", "Le volcanisme"], "La sédimentation", "Les sédiments accumulés deviennent, avec le temps, des roches sédimentaires."),
  Q("Quel agent d'érosion a creusé les vallées en forme de U dans les montagnes ?", ["Les glaciers", "Le vent seul", "Les animaux", "Les volcans"], "Les glaciers", "Les glaciers creusent des vallées en U ; les rivières des vallées en V."),
]),
notion('S-2', 1, F, 'svt-besoins-animaux', [
  Q("Pourquoi les animaux doivent-ils se nourrir ?", ["Pour fabriquer eux-mêmes leur matière par photosynthèse", "Pour obtenir la matière et l'énergie nécessaires à leur fonctionnement et à leur croissance", "Uniquement pour se réchauffer", "Ils n'en ont pas besoin"], "Pour obtenir la matière et l'énergie nécessaires à leur fonctionnement et à leur croissance", "Contrairement aux végétaux chlorophylliens, les animaux dépendent d'autres êtres vivants pour se nourrir."),
  Q("Comment appelle-t-on les êtres vivants qui doivent consommer de la matière organique produite par d'autres ?", ["Des producteurs", "Des consommateurs", "Des minéraux", "Des photosynthétiques"], "Des consommateurs", "Herbivores, carnivores et omnivores sont des consommateurs."),
  Q("Comment certains animaux passent-ils l'hiver en réduisant fortement leur activité, comme la marmotte ?", ["En migrant", "En hibernant", "En muant", "En se reproduisant"], "En hibernant", "L'hibernation permet de survivre quand la nourriture manque ; d'autres animaux migrent."),
]),
]

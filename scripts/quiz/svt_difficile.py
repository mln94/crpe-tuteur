from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('S-1', 0, D, 'svt-datation-relative', [
  Q("Selon le principe de superposition, dans une série de couches sédimentaires non déformées…", ["la couche du haut est la plus ancienne", "la couche du bas est la plus ancienne", "toutes ont le même âge", "on ne peut rien dire"], "la couche du bas est la plus ancienne", "Les couches se déposent les unes sur les autres : la plus profonde s'est déposée la première."),
  Q("Selon le principe de recoupement, une faille qui traverse plusieurs couches est…", ["plus ancienne que les couches", "plus récente que les couches qu'elle recoupe", "du même âge", "sans rapport"], "plus récente que les couches qu'elle recoupe", "Un événement qui recoupe une structure lui est postérieur."),
  Q("Quelle méthode permet de donner un âge chiffré à une roche ?", ["La datation relative", "La datation radiochronologique (absolue)", "L'observation des couleurs", "La mesure de la dureté"], "La datation radiochronologique (absolue)", "Elle utilise la désintégration d'éléments radioactifs, comme le carbone 14 pour les restes récents."),
]),
notion('S-1', 0, D, 'svt-wegener-preuves', [
  Q("Quel scientifique propose en 1912 la théorie de la dérive des continents ?", ["Charles Darwin", "Alfred Wegener", "Louis Pasteur", "Isaac Newton"], "Alfred Wegener", "Wegener s'appuie sur la forme des côtes, les fossiles et les roches identiques de part et d'autre de l'Atlantique."),
  Q("Quel argument Wegener utilise-t-il pour sa théorie ?", ["Les marées", "La présence des mêmes fossiles sur des continents aujourd'hui séparés par l'océan", "Le climat actuel", "La vitesse du vent"], "La présence des mêmes fossiles sur des continents aujourd'hui séparés par l'océan", "Des fossiles de Mesosaurus se trouvent en Amérique du Sud et en Afrique."),
  Q("Pourquoi la théorie de Wegener a-t-elle été longtemps rejetée ?", ["Elle était prouvée fausse", "Il ne pouvait pas expliquer le moteur du déplacement des continents", "Elle contredisait la Bible uniquement", "Il n'avait aucun argument"], "Il ne pouvait pas expliquer le moteur du déplacement des continents", "Elle a été reprise dans les années 1960 avec la tectonique des plaques et l'étude des fonds océaniques."),
]),
notion('S-1', 1, D, 'svt-courants-oceaniques', [
  Q("Quel courant océanique adoucit le climat de l'Europe de l'Ouest ?", ["Le courant de Humboldt", "Le Gulf Stream (dérive nord-atlantique)", "Le courant du Labrador", "Le courant des Canaries"], "Le Gulf Stream (dérive nord-atlantique)", "Ce courant chaud transporte de la chaleur vers le nord-est de l'Atlantique."),
  Q("Comment appelle-t-on le phénomène de réchauffement anormal des eaux du Pacifique équatorial est, aux effets climatiques mondiaux ?", ["La mousson", "El Niño", "Le mistral", "La marée"], "El Niño", "El Niño modifie les précipitations et les températures dans de nombreuses régions du globe."),
  Q("Qu'est-ce que l'albédo ?", ["La température d'une surface", "La part du rayonnement solaire réfléchie par une surface", "La quantité de pluie", "La vitesse du vent"], "La part du rayonnement solaire réfléchie par une surface", "La glace a un albédo élevé ; sa fonte fait absorber plus de chaleur à la Terre."),
]),
notion('S-1', 2, D, 'svt-retroactions-climat', [
  Q("Pourquoi la fonte de la banquise accélère-t-elle le réchauffement ?", ["Elle refroidit l'océan", "L'océan sombre absorbe davantage de rayonnement que la glace claire (baisse de l'albédo)", "Elle libère de l'oxygène", "Elle n'a aucun effet"], "L'océan sombre absorbe davantage de rayonnement que la glace claire (baisse de l'albédo)", "C'est une rétroaction positive qui amplifie le réchauffement."),
  Q("Quel risque fait peser le dégel du pergélisol (permafrost) ?", ["Aucun", "La libération de grandes quantités de CO₂ et de méthane", "Une baisse du niveau des mers", "Une augmentation de la banquise"], "La libération de grandes quantités de CO₂ et de méthane", "Le pergélisol contient de la matière organique qui, en se décomposant, émet des gaz à effet de serre."),
  Q("Quel rôle l'océan joue-t-il face au CO₂ émis par l'humanité ?", ["Il n'en absorbe pas", "Il en absorbe une partie importante, ce qui provoque son acidification", "Il le transforme en oxygène pur", "Il le rejette entièrement"], "Il en absorbe une partie importante, ce qui provoque son acidification", "L'acidification menace les coraux et les organismes à coquille calcaire."),
]),
notion('S-2', 1, D, 'svt-equations-energie', [
  Q("Quelle équation résume la photosynthèse ?", ["Glucose + dioxygène → CO₂ + eau + énergie", "CO₂ + eau + énergie lumineuse → glucose + dioxygène", "Eau → hydrogène + oxygène", "Amidon → glucose"], "CO₂ + eau + énergie lumineuse → glucose + dioxygène", "La respiration cellulaire réalise la transformation inverse en libérant l'énergie du glucose."),
  Q("Quelle équation résume la respiration cellulaire ?", ["Glucose + dioxygène → CO₂ + eau + énergie", "CO₂ + eau → glucose + dioxygène", "Glucose → amidon", "Eau + sels minéraux → sève"], "Glucose + dioxygène → CO₂ + eau + énergie", "Elle se déroule dans les mitochondries de toutes les cellules eucaryotes."),
  Q("Comment appelle-t-on la transformation du glucose en énergie sans dioxygène, utilisée par les levures pour faire lever la pâte ?", ["La respiration", "La fermentation", "La photosynthèse", "La digestion"], "La fermentation", "La fermentation alcoolique produit de l'éthanol et du CO₂, qui fait lever la pâte."),
  Q("Sous quelle forme les plantes stockent-elles souvent le glucose produit par la photosynthèse ?", ["Sous forme d'amidon", "Sous forme de protéines", "Sous forme de sel", "Sous forme d'ADN"], "Sous forme d'amidon", "L'amidon s'accumule dans les organes de réserve (tubercules, graines) ; l'eau iodée le colore en bleu-noir."),
]),
notion('S-2', 3, D, 'svt-genotype-phenotype', [
  Q("Qu'est-ce que le phénotype ?", ["L'ensemble des gènes d'un individu", "L'ensemble des caractères observables d'un individu", "Un chromosome", "Une maladie"], "L'ensemble des caractères observables d'un individu", "Le phénotype dépend du génotype et de l'environnement."),
  Q("Qu'est-ce que le génotype ?", ["L'ensemble des allèles d'un individu", "La couleur des yeux", "La taille", "Le groupe sanguin seulement"], "L'ensemble des allèles d'un individu", "Le génotype s'exprime, en interaction avec l'environnement, en phénotype."),
  Q("Une personne de génotype AO a le groupe sanguin A. Que peut-on dire de l'allèle O ?", ["Il est dominant", "Il est récessif par rapport à A", "Il est absent", "Il est muté"], "Il est récessif par rapport à A", "L'allèle A s'exprime et masque O : A est dominant sur O."),
]),
notion('S-2', 3, D, 'svt-anomalies-chromosomiques', [
  Q("Quelle est la cause de la trisomie 21 ?", ["Un virus", "La présence de trois chromosomes 21 au lieu de deux", "Un manque de vitamines", "Une infection pendant la grossesse"], "La présence de trois chromosomes 21 au lieu de deux", "Elle résulte le plus souvent d'une anomalie de répartition des chromosomes lors de la méiose."),
  N("Combien de chromosomes possèdent les cellules d'une personne atteinte de trisomie 21 ?", 47, "Elles possèdent 47 chromosomes au lieu de 46."),
  Q("Comment appelle-t-on la représentation ordonnée des chromosomes d'une cellule ?", ["Un électrocardiogramme", "Un caryotype", "Un arbre généalogique", "Un génotype"], "Un caryotype", "Le caryotype classe les chromosomes par paires, selon leur taille."),
]),
notion('S-2', 4, D, 'svt-speciation', [
  Q("Comment appelle-t-on l'apparition d'une nouvelle espèce ?", ["La mutation", "La spéciation", "La sélection artificielle", "L'hybridation stérile"], "La spéciation", "Elle se produit souvent quand des populations isolées accumulent des différences jusqu'à ne plus pouvoir se reproduire entre elles."),
  Q("Comment appelle-t-on la variation aléatoire de la fréquence des allèles, particulièrement forte dans les petites populations ?", ["La dérive génétique", "La sélection naturelle", "La migration", "La mutation dirigée"], "La dérive génétique", "Contrairement à la sélection, la dérive est due au hasard de la reproduction."),
  Q("Quel facteur favorise la spéciation ?", ["Le brassage permanent des populations", "L'isolement géographique de populations", "L'absence de mutations", "Une population unique et immense"], "L'isolement géographique de populations", "Les pinsons des Galápagos, étudiés par Darwin, en sont un exemple."),
]),
notion('S-2', 2, D, 'svt-parente', [
  Q("Sur quoi se fonde la construction d'un arbre de parenté (phylogénétique) ?", ["Sur la taille des animaux", "Sur les attributs partagés hérités d'un ancêtre commun", "Sur le régime alimentaire", "Sur le lieu de vie"], "Sur les attributs partagés hérités d'un ancêtre commun", "Plus deux espèces partagent d'attributs, plus leur ancêtre commun est récent."),
  Q("De qui le crocodile est-il le plus proche parent parmi ces animaux ?", ["Le lézard", "L'oiseau", "Le serpent", "La tortue"], "L'oiseau", "Crocodiles et oiseaux forment ensemble le groupe des archosaures."),
  Q("Les données génétiques (comparaison de l'ADN) servent-elles à établir les parentés ?", ["Non, jamais", "Oui, elles confirment ou précisent les parentés établies par l'anatomie", "Seulement chez les humains", "Seulement chez les plantes"], "Oui, elles confirment ou précisent les parentés établies par l'anatomie", "Plus deux séquences d'ADN sont proches, plus les espèces sont apparentées."),
]),
notion('S-3', 0, D, 'svt-synapse', [
  Q("Comment appelle-t-on la zone de communication entre deux neurones ?", ["Un nerf", "Une synapse", "Un axone", "Une alvéole"], "Une synapse", "Le message y est transmis par des molécules chimiques, les neurotransmetteurs."),
  Q("Comment le message nerveux traverse-t-il une synapse ?", ["Il saute électriquement", "Grâce à la libération de neurotransmetteurs", "Par le sang", "Il ne la traverse pas"], "Grâce à la libération de neurotransmetteurs", "Certaines drogues perturbent le fonctionnement des synapses."),
  Q("Pourquoi les drogues sont-elles dangereuses pour le cerveau ?", ["Elles n'ont aucun effet", "Elles perturbent la transmission synaptique et peuvent créer une dépendance", "Elles renforcent la mémoire", "Elles soignent les neurones"], "Elles perturbent la transmission synaptique et peuvent créer une dépendance", "Elles agissent notamment sur le circuit de la récompense."),
]),
notion('S-3', 1, D, 'svt-memoire-immunitaire', [
  Q("Pourquoi attrape-t-on rarement deux fois la varicelle ?", ["Le virus disparaît de la Terre", "L'organisme garde une mémoire immunitaire (lymphocytes mémoire)", "On devient allergique", "Par hasard"], "L'organisme garde une mémoire immunitaire (lymphocytes mémoire)", "Lors d'un second contact, la réponse est plus rapide et plus forte."),
  Q("Quels lymphocytes détruisent directement les cellules infectées par un virus ?", ["Les lymphocytes B", "Les lymphocytes T cytotoxiques", "Les globules rouges", "Les plaquettes"], "Les lymphocytes T cytotoxiques", "Les lymphocytes B produisent des anticorps ; les T cytotoxiques éliminent les cellules infectées."),
  Q("Pourquoi faut-il parfois des rappels de vaccin ?", ["Le vaccin se périme dans le corps", "Pour entretenir la mémoire immunitaire qui diminue avec le temps", "Pour changer de maladie", "Ce n'est jamais nécessaire"], "Pour entretenir la mémoire immunitaire qui diminue avec le temps", "C'est le cas du tétanos, avec des rappels à certains âges."),
]),
notion('S-3', 3, D, 'svt-antibioresistance', [
  Q("Comment apparaît la résistance d'une population de bactéries à un antibiotique ?", ["Les bactéries « apprennent » à résister", "Des bactéries portant par hasard une mutation de résistance survivent et se multiplient sous l'effet de l'antibiotique", "L'antibiotique les rend plus fortes", "Par contagion des humains"], "Des bactéries portant par hasard une mutation de résistance survivent et se multiplient sous l'effet de l'antibiotique", "L'antibiotique sélectionne les bactéries résistantes préexistantes."),
  Q("Quel comportement limite l'antibiorésistance ?", ["Arrêter le traitement dès qu'on va mieux", "Ne prendre des antibiotiques que sur prescription et suivre le traitement jusqu'au bout", "En prendre contre la grippe", "Partager ses antibiotiques"], "Ne prendre des antibiotiques que sur prescription et suivre le traitement jusqu'au bout", "Un usage raisonné ralentit la sélection de bactéries résistantes."),
  Q("Quelle approche considère ensemble la santé humaine, animale et environnementale ?", ["Une seule santé (One Health)", "La médecine du travail", "La santé publique locale", "La pharmacologie"], "Une seule santé (One Health)", "Les antibiotiques utilisés en élevage contribuent aussi à l'antibiorésistance."),
]),
notion('S-3', 2, D, 'svt-hormones', [
  Q("Quelle glande, située sous le cerveau, contrôle de nombreuses autres glandes, dont les ovaires et les testicules ?", ["La thyroïde", "L'hypophyse", "Le pancréas", "Les surrénales"], "L'hypophyse", "L'hypophyse, commandée par l'hypothalamus, sécrète des hormones qui agissent sur les organes reproducteurs."),
  Q("Qu'est-ce qu'une hormone ?", ["Un microbe", "Une molécule produite par une glande, transportée par le sang et agissant sur des organes cibles", "Un nerf", "Un nutriment"], "Une molécule produite par une glande, transportée par le sang et agissant sur des organes cibles", "L'insuline, la testostérone ou l'adrénaline sont des hormones."),
  Q("Quelle hormone, produite par les testicules, est responsable des caractères sexuels masculins ?", ["La progestérone", "La testostérone", "L'insuline", "L'adrénaline"], "La testostérone", "Les ovaires produisent les œstrogènes et la progestérone."),
]),
notion('S-3', 3, D, 'svt-zoonoses', [
  Q("Qu'est-ce qu'une zoonose ?", ["Une maladie génétique", "Une maladie transmissible de l'animal à l'être humain", "Une maladie des plantes", "Une allergie alimentaire"], "Une maladie transmissible de l'animal à l'être humain", "La rage, la grippe aviaire ou la maladie de Lyme sont des zoonoses."),
  Q("Quel animal transmet la maladie de Lyme ?", ["Le moustique", "La tique", "Le chat", "La mouche"], "La tique", "La bactérie responsable est transmise par la piqûre d'une tique infectée."),
  Q("Pourquoi le moustique tigre est-il surveillé en France métropolitaine ?", ["Il pique seulement les animaux", "Il peut transmettre la dengue, le chikungunya ou le Zika", "Il détruit les cultures", "Il est venimeux"], "Il peut transmettre la dengue, le chikungunya ou le Zika", "Il s'est installé dans la plupart des départements, favorisé par le réchauffement."),
]),
notion('S-1', 3, D, 'svt-transition-energetique', [
  Q("Quelle source d'électricité émet le moins de CO₂ par kWh produit sur son cycle de vie, parmi celles-ci ?", ["Le charbon", "L'éolien", "Le fioul", "Le gaz naturel"], "L'éolien", "L'éolien, le nucléaire et l'hydraulique émettent très peu de CO₂ par kWh, contrairement aux énergies fossiles."),
  Q("Quel est l'inconvénient principal des énergies solaire et éolienne ?", ["Elles émettent beaucoup de CO₂", "Leur production est intermittente et dépend de la météo", "Elles sont épuisables", "Elles sont interdites"], "Leur production est intermittente et dépend de la météo", "D'où l'intérêt du stockage et d'un mix énergétique diversifié."),
  Q("Qu'est-ce que la sobriété énergétique ?", ["Consommer plus pour stocker", "Réduire ses besoins en énergie par des choix d'usage et d'organisation", "Utiliser uniquement le nucléaire", "Interdire l'électricité"], "Réduire ses besoins en énergie par des choix d'usage et d'organisation", "Elle complète l'efficacité énergétique (consommer moins pour le même service)."),
  Q("Quel objectif l'Union européenne s'est-elle fixé pour 2050 ?", ["Doubler ses émissions", "La neutralité carbone", "Sortir de l'électricité", "Interdire les voitures"], "La neutralité carbone", "La neutralité carbone vise un équilibre entre émissions et absorptions de gaz à effet de serre."),
]),
notion('S-2', 0, D, 'svt-organisation-vivant', [
  Q("Quels êtres vivants ont des cellules sans noyau ?", ["Les animaux", "Les bactéries", "Les plantes", "Les champignons"], "Les bactéries", "Les bactéries sont des procaryotes ; animaux, plantes et champignons sont des eucaryotes."),
  Q("Les champignons sont-ils des végétaux ?", ["Oui", "Non, ils forment un groupe à part et ne font pas de photosynthèse", "Seulement les champignons verts", "Oui, car ils poussent dans le sol"], "Non, ils forment un groupe à part et ne font pas de photosynthèse", "Les champignons sont plus proches des animaux que des plantes."),
  Q("Comment appelle-t-on le niveau d'organisation qui va de la molécule à la biosphère ?", ["L'échelle des niveaux d'organisation du vivant", "La chaîne alimentaire", "Le cycle de l'eau", "La classification"], "L'échelle des niveaux d'organisation du vivant", "Molécule, cellule, tissu, organe, organisme, population, écosystème, biosphère."),
]),
]

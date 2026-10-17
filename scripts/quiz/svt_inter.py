from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('S-1', 0, I, 'svt-subduction-dorsale', [
  Q("Comment appelle-t-on la zone où une plaque océanique plonge sous une autre plaque ?", ["Une dorsale", "Une zone de subduction", "Un rift", "Un point chaud"], "Une zone de subduction", "La subduction s'accompagne de séismes profonds et d'un volcanisme explosif (Andes, Japon)."),
  Q("Que se passe-t-il au niveau d'une dorsale océanique ?", ["Deux plaques se rapprochent", "Deux plaques s'écartent et du nouveau plancher océanique se forme", "Une plaque disparaît", "Il ne se passe rien"], "Deux plaques s'écartent et du nouveau plancher océanique se forme", "Le magma remonte et crée de la lithosphère océanique : c'est l'accrétion."),
  Q("Quelle chaîne de montagnes résulte de la collision de l'Inde avec l'Asie ?", ["Les Alpes", "L'Himalaya", "Les Andes", "Les Rocheuses"], "L'Himalaya", "La collision continentale, toujours active, fait encore s'élever l'Himalaya."),
]),
notion('S-1', 0, I, 'svt-prevention-sismique', [
  Q("Peut-on prévoir la date exacte d'un séisme ?", ["Oui, à la minute près", "Non, mais on peut connaître les zones à risque et construire en conséquence", "Oui, grâce aux animaux", "Oui, avec la météo"], "Non, mais on peut connaître les zones à risque et construire en conséquence", "La prévention repose sur la connaissance de l'aléa, les normes parasismiques et l'éducation de la population."),
  Q("Quelle mesure réduit la vulnérabilité face aux séismes ?", ["Construire selon des normes parasismiques", "Construire en hauteur sans renfort", "Interdire les exercices d'évacuation", "Ignorer les cartes d'aléa"], "Construire selon des normes parasismiques", "Les bâtiments parasismiques résistent mieux aux secousses."),
  Q("Quelle vague géante peut être déclenchée par un séisme sous-marin ?", ["Un cyclone", "Un tsunami", "Une marée d'équinoxe", "Une avalanche"], "Un tsunami", "Le tsunami de 2004 dans l'océan Indien a fait plus de 200 000 victimes."),
]),
notion('S-1', 1, I, 'svt-anticyclone-depression', [
  Q("À quel type de temps un anticyclone est-il généralement associé ?", ["Un temps pluvieux et venté", "Un temps sec et ensoleillé", "Des orages violents", "La neige uniquement"], "Un temps sec et ensoleillé", "L'anticyclone est une zone de hautes pressions ; la dépression, de basses pressions, apporte nuages et pluie."),
  Q("Les vents soufflent des zones de…", ["basses pressions vers les hautes pressions", "hautes pressions vers les basses pressions", "pressions égales", "l'océan vers le pôle seulement"], "hautes pressions vers les basses pressions", "L'air se déplace des hautes vers les basses pressions."),
  Q("Quelle est l'origine de l'énergie qui met en mouvement l'atmosphère et les océans ?", ["Le noyau terrestre", "Le Soleil, qui chauffe inégalement la Terre", "La Lune", "Les volcans"], "Le Soleil, qui chauffe inégalement la Terre", "Les différences de température entre l'équateur et les pôles provoquent les mouvements de l'air et de l'eau."),
]),
notion('S-1', 1, I, 'svt-giec', [
  Q("Quel organisme international évalue l'état des connaissances sur le changement climatique ?", ["Le GIEC", "L'OMS", "L'UNESCO", "Le FMI"], "Le GIEC", "Le Groupe d'experts intergouvernemental sur l'évolution du climat publie des rapports de synthèse."),
  Q("De combien la température moyenne mondiale a-t-elle augmenté environ depuis l'ère préindustrielle ?", ["0,1 °C", "Environ 1,2 °C", "5 °C", "10 °C"], "Environ 1,2 °C", "Le réchauffement atteint environ 1,1 à 1,3 °C, avec des valeurs annuelles proches de 1,5 °C en 2024."),
  Q("Comment les scientifiques connaissent-ils les climats du passé lointain ?", ["Par les journaux anciens uniquement", "Grâce aux carottes de glace, aux sédiments et aux fossiles", "Par des sondages", "Ils ne peuvent pas les connaître"], "Grâce aux carottes de glace, aux sédiments et aux fossiles", "Les bulles d'air piégées dans les glaces polaires renseignent sur l'atmosphère d'il y a des centaines de milliers d'années."),
]),
notion('S-1', 2, I, 'svt-agriculture-environnement', [
  Q("Comment appelle-t-on la prolifération d'algues due à un excès d'engrais dans l'eau ?", ["L'eutrophisation", "La photosynthèse", "La sédimentation", "L'érosion"], "L'eutrophisation", "Les nitrates et phosphates favorisent les algues, qui appauvrissent l'eau en dioxygène (marées vertes en Bretagne)."),
  Q("Quelle pratique agricole limite l'usage des pesticides ?", ["La monoculture intensive", "La lutte biologique (coccinelles contre les pucerons…)", "Le labour profond systématique", "Le brûlage des haies"], "La lutte biologique (coccinelles contre les pucerons…)", "L'agroécologie utilise les régulations naturelles."),
  Q("Pourquoi les haies sont-elles utiles en milieu agricole ?", ["Elles n'ont aucun intérêt", "Elles abritent la biodiversité, limitent l'érosion et coupent le vent", "Elles polluent", "Elles empêchent la photosynthèse"], "Elles abritent la biodiversité, limitent l'érosion et coupent le vent", "Les haies servent de refuge aux auxiliaires des cultures."),
]),
notion('S-1', 3, I, 'svt-empreinte-carbone', [
  Q("Qu'est-ce que l'empreinte carbone ?", ["Le poids d'une personne", "La quantité de gaz à effet de serre émise par une activité, un produit ou une personne", "La surface d'une forêt", "La pollution de l'eau"], "La quantité de gaz à effet de serre émise par une activité, un produit ou une personne", "Elle s'exprime en équivalent CO₂."),
  Q("Quel moyen de transport émet le moins de CO₂ par voyageur sur un trajet moyen en France ?", ["L'avion", "Le train", "La voiture seule", "Le bateau de croisière"], "Le train", "Le train, largement électrifié en France, émet beaucoup moins que l'avion ou la voiture."),
  Q("Quel secteur émet le plus de gaz à effet de serre en France ?", ["Les transports", "La culture", "L'éducation", "Le tourisme"], "Les transports", "Les transports sont le premier secteur émetteur en France, devant l'agriculture, l'industrie et les bâtiments."),
]),
notion('S-1', 0, I, 'svt-age-terre', [
  Q("Quel est l'âge approximatif de la Terre ?", ["6 000 ans", "4,6 milliards d'années", "65 millions d'années", "100 milliards d'années"], "4,6 milliards d'années", "La Terre s'est formée il y a environ 4,6 milliards d'années, en même temps que le système solaire."),
  Q("Depuis combien de temps environ la vie existe-t-elle sur Terre ?", ["10 000 ans", "Environ 3,5 milliards d'années", "1 million d'années", "100 ans"], "Environ 3,5 milliards d'années", "Les plus anciennes traces de vie (bactéries) datent d'environ 3,5 milliards d'années, voire plus."),
  Q("Depuis combien de temps environ notre espèce, Homo sapiens, existe-t-elle ?", ["Environ 300 000 ans", "4 milliards d'années", "65 millions d'années", "2 000 ans"], "Environ 300 000 ans", "Les plus anciens fossiles d'Homo sapiens connus (Djebel Irhoud, Maroc) ont environ 300 000 ans."),
]),
notion('S-2', 0, I, 'svt-uni-pluricellulaire', [
  Q("Lequel de ces êtres vivants est unicellulaire ?", ["Un chêne", "Une paramécie", "Un chat", "Un champignon de Paris"], "Une paramécie", "La paramécie, comme les bactéries, est formée d'une seule cellule."),
  Q("Comment appelle-t-on un ensemble de cellules semblables qui remplissent une même fonction ?", ["Un organe", "Un tissu", "Un appareil", "Un organisme"], "Un tissu", "Cellules → tissus → organes → appareils (ou systèmes) → organisme."),
  Q("Quelle cellule n'a pas de noyau ?", ["Une cellule de feuille", "Une bactérie", "Un neurone", "Une cellule de peau"], "Une bactérie", "Les bactéries sont des procaryotes : leur ADN n'est pas enfermé dans un noyau."),
]),
notion('S-2', 1, I, 'svt-nutrition-plante', [
  Q("Par où une plante absorbe-t-elle l'eau et les sels minéraux du sol ?", ["Par les feuilles", "Par les poils absorbants des racines", "Par les fleurs", "Par la tige"], "Par les poils absorbants des racines", "Ces cellules très fines augmentent la surface d'échange avec le sol."),
  Q("Comment appelle-t-on la sève qui transporte l'eau et les sels minéraux des racines vers les feuilles ?", ["La sève élaborée", "La sève brute", "Le latex", "La résine"], "La sève brute", "La sève élaborée, riche en sucres produits par la photosynthèse, circule des feuilles vers les autres organes."),
  Q("Par quelles ouvertures des feuilles le CO₂ entre-t-il dans la plante ?", ["Les stomates", "Les racines", "Les pétales", "Les nervures"], "Les stomates", "Les stomates permettent aussi la sortie de vapeur d'eau (transpiration)."),
]),
notion('S-2', 2, I, 'svt-dynamique-populations', [
  Q("Dans un milieu, que se passe-t-il généralement si le nombre de proies diminue fortement ?", ["Le nombre de prédateurs augmente", "Le nombre de prédateurs diminue ensuite", "Rien", "Les prédateurs deviennent herbivores"], "Le nombre de prédateurs diminue ensuite", "Les populations de proies et de prédateurs sont liées et fluctuent ensemble."),
  Q("Comment appelle-t-on l'ensemble des êtres vivants et de leur milieu de vie en interaction ?", ["Un écosystème", "Une espèce", "Une cellule", "Un organe"], "Un écosystème", "Un écosystème associe un biotope (milieu) et une biocénose (êtres vivants)."),
  Q("Comment appelle-t-on l'ensemble des relations alimentaires d'un écosystème ?", ["Une chaîne isolée", "Un réseau trophique", "Une classification", "Un arbre généalogique"], "Un réseau trophique", "Les chaînes alimentaires s'entrecroisent pour former un réseau trophique."),
]),
notion('S-2', 2, I, 'svt-groupes-emboites', [
  Q("Dans une classification en groupes emboîtés, que signifie l'emboîtement de deux groupes ?", ["Ils n'ont rien en commun", "Le groupe intérieur possède tous les attributs du groupe qui l'englobe, plus d'autres", "Ils vivent au même endroit", "Ils ont la même taille"], "Le groupe intérieur possède tous les attributs du groupe qui l'englobe, plus d'autres", "Les mammifères sont emboîtés dans les vertébrés : ils ont une colonne vertébrale, plus des mamelles et des poils."),
  Q("Quel attribut partagent les tétrapodes ?", ["Des écailles", "Quatre membres (ou des descendants qui en avaient)", "Des plumes", "Des branchies"], "Quatre membres (ou des descendants qui en avaient)", "Les serpents sont des tétrapodes : leurs ancêtres avaient quatre membres."),
  Q("Pourquoi le mot « poisson » ne correspond-il pas à un groupe unique dans la classification actuelle ?", ["Parce que les poissons n'existent pas", "Parce que les animaux appelés « poissons » ne forment pas un groupe réunissant un ancêtre commun et tous ses descendants", "Parce qu'ils vivent dans l'eau", "Parce qu'ils sont trop nombreux"], "Parce que les animaux appelés « poissons » ne forment pas un groupe réunissant un ancêtre commun et tous ses descendants", "Certains « poissons » sont plus proches des tétrapodes que d'autres poissons."),
]),
notion('S-2', 3, I, 'svt-mitose', [
  Q("Comment appelle-t-on la division cellulaire qui donne deux cellules identiques à la cellule de départ ?", ["La méiose", "La mitose", "La fécondation", "La mutation"], "La mitose", "La mitose permet la croissance et le renouvellement des cellules."),
  Q("Après une mitose, combien de chromosomes possède chaque cellule humaine fille ?", ["23", "46", "92", "12"], "46", "Les deux cellules filles reçoivent la même information génétique que la cellule mère."),
  Q("À quoi sert la mitose chez un être humain ?", ["À fabriquer les gamètes", "À la croissance et à la réparation des tissus", "À la digestion", "À la photosynthèse"], "À la croissance et à la réparation des tissus", "La cicatrisation d'une plaie repose sur des mitoses."),
]),
notion('S-2', 3, I, 'svt-meiose', [
  Q("Quelle division cellulaire produit les cellules reproductrices (gamètes) ?", ["La mitose", "La méiose", "La photosynthèse", "La digestion"], "La méiose", "La méiose produit des cellules à 23 chromosomes chez l'être humain."),
  Q("Pourquoi les enfants d'un même couple sont-ils tous différents (sauf vrais jumeaux) ?", ["Par hasard de l'alimentation", "Car chaque gamète reçoit une combinaison différente de chromosomes, et la fécondation associe deux gamètes au hasard", "Car ils ont des parents différents", "Car l'ADN change chaque jour"], "Car chaque gamète reçoit une combinaison différente de chromosomes, et la fécondation associe deux gamètes au hasard", "La méiose et la fécondation créent une diversité génétique unique pour chaque individu."),
  Q("Comment expliquer l'existence de vrais jumeaux ?", ["Deux ovules fécondés par deux spermatozoïdes", "Une seule cellule-œuf qui se divise en deux embryons", "Une erreur de la méiose", "Une mutation"], "Une seule cellule-œuf qui se divise en deux embryons", "Les vrais jumeaux ont le même patrimoine génétique ; les faux jumeaux viennent de deux cellules-œufs."),
]),
notion('S-2', 3, I, 'svt-alleles', [
  Q("Qu'est-ce qu'un allèle ?", ["Un chromosome entier", "Une version d'un gène", "Une cellule reproductrice", "Un organe"], "Une version d'un gène", "Un même gène (par exemple celui du groupe sanguin) peut exister sous plusieurs allèles (A, B, O)."),
  Q("Combien d'allèles d'un même gène une cellule humaine (non reproductrice) possède-t-elle ?", ["Un", "Deux, un sur chaque chromosome de la paire", "Quatre", "46"], "Deux, un sur chaque chromosome de la paire", "On reçoit un allèle de chaque parent."),
  Q("Où se trouve un gène ?", ["Dans le sang uniquement", "À un emplacement précis d'un chromosome", "Dans la membrane cellulaire", "Dans l'estomac"], "À un emplacement précis d'un chromosome", "Un gène est une portion d'ADN située à un endroit précis d'un chromosome."),
]),
notion('S-2', 4, I, 'svt-selection-naturelle', [
  Q("Selon la théorie de Darwin, quels individus ont le plus de descendants ?", ["Les plus gros", "Ceux dont les caractères sont les plus avantageux dans leur milieu", "Les plus vieux", "Tous à égalité"], "Ceux dont les caractères sont les plus avantageux dans leur milieu", "C'est la sélection naturelle : les caractères avantageux deviennent plus fréquents au fil des générations."),
  Q("Quel exemple illustre la sélection naturelle ?", ["Un chien entraîné à rapporter une balle", "Des bactéries devenant majoritairement résistantes après l'usage d'un antibiotique", "Un arbre taillé par un jardinier", "Un humain qui apprend une langue"], "Des bactéries devenant majoritairement résistantes après l'usage d'un antibiotique", "Les bactéries résistantes survivent et se multiplient : le milieu a sélectionné ce caractère."),
  Q("Un caractère acquis au cours de la vie (muscles développés par le sport) se transmet-il aux enfants ?", ["Oui, toujours", "Non, seuls les caractères inscrits dans l'ADN des gamètes se transmettent", "Oui, si on s'entraîne longtemps", "Seulement aux garçons"], "Non, seuls les caractères inscrits dans l'ADN des gamètes se transmettent", "C'est l'une des idées de Lamarck que la génétique a écartée."),
]),
notion('S-2', 4, I, 'svt-mutations', [
  Q("Qu'est-ce qu'une mutation ?", ["Une maladie contagieuse", "Une modification de la séquence de l'ADN", "Un changement de saison", "Une division cellulaire normale"], "Une modification de la séquence de l'ADN", "Les mutations peuvent créer de nouveaux allèles, source de diversité génétique."),
  Q("Quel facteur peut augmenter la fréquence des mutations ?", ["Les rayons ultraviolets", "Le sommeil", "L'eau potable", "Le sport modéré"], "Les rayons ultraviolets", "Les UV, certains produits chimiques et les radiations sont des agents mutagènes."),
  Q("Une mutation dans une cellule de la peau se transmet-elle aux enfants ?", ["Oui", "Non, seules les mutations des cellules reproductrices peuvent être transmises", "Oui, si elle est visible", "Seulement aux filles"], "Non, seules les mutations des cellules reproductrices peuvent être transmises", "Une mutation de la peau peut toutefois provoquer un cancer chez l'individu."),
]),
notion('S-2', 4, I, 'svt-extinctions', [
  N("Il y a combien de millions d'années les dinosaures non aviens ont-ils disparu ?", 66, "La crise de la fin du Crétacé, il y a environ 66 millions d'années, est liée notamment à la chute d'une météorite."),
  Q("Quels animaux actuels sont des descendants de dinosaures ?", ["Les crocodiles", "Les oiseaux", "Les lézards", "Les mammifères"], "Les oiseaux", "Les oiseaux sont des dinosaures à plumes ayant survécu à la crise de la fin du Crétacé."),
  Q("Comment appelle-t-on une disparition rapide d'un grand nombre d'espèces à l'échelle de la planète ?", ["Une mutation", "Une crise biologique (extinction de masse)", "Une migration", "Une adaptation"], "Une crise biologique (extinction de masse)", "On en compte cinq majeures ; beaucoup de scientifiques parlent d'une sixième en cours."),
]),
notion('S-3', 0, I, 'svt-double-circulation', [
  Q("Vers quel organe le ventricule droit envoie-t-il le sang ?", ["Vers tout le corps", "Vers les poumons", "Vers le cerveau uniquement", "Vers l'intestin"], "Vers les poumons", "La petite circulation (pulmonaire) oxygène le sang ; le ventricule gauche l'envoie ensuite dans tout le corps."),
  Q("Pourquoi la paroi du ventricule gauche est-elle plus épaisse que celle du ventricule droit ?", ["Par hasard", "Parce qu'il propulse le sang dans tout l'organisme", "Parce qu'il reçoit l'air", "Parce qu'il produit le sang"], "Parce qu'il propulse le sang dans tout l'organisme", "Il doit exercer une pression plus forte que le ventricule droit."),
  Q("Le sang qui revient des poumons au cœur est…", ["pauvre en dioxygène", "riche en dioxygène", "riche en nutriments seulement", "sans gaz"], "riche en dioxygène", "Les veines pulmonaires ramènent au cœur gauche un sang oxygéné."),
]),
notion('S-3', 0, I, 'svt-reflexe', [
  Q("Quel centre nerveux commande le réflexe rotulien (coup sur le genou) ?", ["Le cerveau", "La moelle épinière", "Le cœur", "L'estomac"], "La moelle épinière", "Un réflexe est une réponse involontaire et rapide commandée par la moelle épinière."),
  Q("Quel est le trajet du message nerveux lors d'un réflexe ?", ["Muscle → cerveau → peau", "Récepteur → nerf sensitif → moelle épinière → nerf moteur → muscle", "Cœur → poumons → muscle", "Muscle → os → muscle"], "Récepteur → nerf sensitif → moelle épinière → nerf moteur → muscle", "Le circuit nerveux du réflexe ne passe pas par le cerveau."),
  Q("Pourquoi retire-t-on la main d'un objet brûlant avant même de ressentir la douleur ?", ["Par habitude", "Grâce à un réflexe commandé par la moelle épinière", "Grâce à la vue", "Par réflexion consciente"], "Grâce à un réflexe commandé par la moelle épinière", "La perception consciente de la douleur, par le cerveau, arrive juste après."),
]),
notion('S-3', 0, I, 'svt-plasticite-cerebrale', [
  Q("Qu'est-ce que la plasticité cérébrale ?", ["La capacité du cerveau à se modifier en fonction des apprentissages et des expériences", "Une maladie du cerveau", "La dureté du crâne", "La couleur du cerveau"], "La capacité du cerveau à se modifier en fonction des apprentissages et des expériences", "Les connexions entre neurones se renforcent avec l'entraînement."),
  Q("Quelle partie du cerveau est spécialisée dans le langage chez la plupart des droitiers ?", ["L'hémisphère droit uniquement", "Des aires de l'hémisphère gauche (aires de Broca et de Wernicke)", "Le cervelet", "La moelle épinière"], "Des aires de l'hémisphère gauche (aires de Broca et de Wernicke)", "Le cerveau comporte des aires spécialisées (motricité, vision, langage)."),
  Q("Quel organe du système nerveux joue un rôle majeur dans l'équilibre et la coordination des mouvements ?", ["Le cervelet", "Le cœur", "Le foie", "L'hypophyse"], "Le cervelet", "Le cervelet coordonne les mouvements et participe à l'équilibre."),
]),
notion('S-3', 1, I, 'svt-enzymes', [
  Q("Quelles molécules accélèrent la transformation des aliments en nutriments ?", ["Les hormones", "Les enzymes digestives", "Les anticorps", "Les vitamines"], "Les enzymes digestives", "L'amylase de la salive, par exemple, transforme l'amidon en sucres plus simples."),
  Q("Quelle enzyme de la salive commence la digestion de l'amidon ?", ["La pepsine", "L'amylase", "La lipase", "L'insuline"], "L'amylase", "La pepsine (estomac) digère les protéines ; la lipase, les lipides."),
  Q("Quel organe produit la bile, qui facilite la digestion des graisses ?", ["L'estomac", "Le foie", "Le pancréas", "Le gros intestin"], "Le foie", "La bile est stockée dans la vésicule biliaire avant d'être déversée dans l'intestin."),
]),
notion('S-3', 1, I, 'svt-glycemie', [
  Q("Qu'est-ce que la glycémie ?", ["Le taux de sucre (glucose) dans le sang", "Le nombre de globules rouges", "La pression du sang", "Le taux de graisse"], "Le taux de sucre (glucose) dans le sang", "Elle est maintenue autour de 1 g/L par des hormones."),
  Q("Quelle hormone fait baisser la glycémie ?", ["L'adrénaline", "L'insuline", "Le glucagon", "La testostérone"], "L'insuline", "L'insuline, produite par le pancréas, fait baisser la glycémie ; le glucagon la fait remonter."),
  Q("Comment appelle-t-on la maladie liée à une glycémie durablement trop élevée ?", ["L'anémie", "Le diabète", "L'asthme", "La grippe"], "Le diabète", "Le diabète de type 1 est dû à un manque d'insuline ; le type 2 est souvent lié au mode de vie."),
]),
notion('S-3', 1, I, 'svt-reaction-inflammatoire', [
  Q("Quels signes caractérisent une réaction inflammatoire ?", ["Rougeur, chaleur, gonflement et douleur", "Fièvre et toux uniquement", "Perte de cheveux", "Aucun signe"], "Rougeur, chaleur, gonflement et douleur", "C'est la réponse immunitaire rapide et non spécifique après une infection."),
  Q("Comment appelle-t-on l'action de certains globules blancs qui englobent et digèrent les microbes ?", ["La phagocytose", "La photosynthèse", "La mitose", "La coagulation"], "La phagocytose", "Les phagocytes interviennent en premier contre les microbes."),
  Q("La réaction inflammatoire est une réponse immunitaire…", ["spécifique et lente", "non spécifique et rapide", "uniquement après vaccination", "inutile"], "non spécifique et rapide", "Elle s'oppose à la réponse adaptative, spécifique et plus lente."),
]),
notion('S-3', 1, I, 'svt-anticorps', [
  Q("Quelles cellules produisent les anticorps ?", ["Les globules rouges", "Des lymphocytes (lymphocytes B)", "Les neurones", "Les plaquettes"], "Des lymphocytes (lymphocytes B)", "Les anticorps se fixent spécifiquement sur un antigène et aident à éliminer le microbe."),
  Q("Un anticorps est-il efficace contre n'importe quel microbe ?", ["Oui", "Non, il est spécifique d'un antigène donné", "Seulement contre les virus", "Seulement contre les bactéries"], "Non, il est spécifique d'un antigène donné", "C'est pourquoi un vaccin cible une maladie précise."),
  Q("Comment appelle-t-on une molécule reconnue comme étrangère par le système immunitaire ?", ["Un antigène", "Un anticorps", "Une enzyme", "Une hormone"], "Un antigène", "Les antigènes sont portés par les microbes ou d'autres éléments étrangers."),
]),
notion('S-3', 2, I, 'svt-cycle-menstruel', [
  N("Combien de jours dure en moyenne un cycle menstruel ?", 28, "Le cycle dure en moyenne 28 jours, avec des variations normales d'une personne à l'autre."),
  Q("Vers quel jour d'un cycle de 28 jours a généralement lieu l'ovulation ?", ["Le 1er jour", "Vers le 14e jour", "Le 28e jour", "Pendant les règles"], "Vers le 14e jour", "L'ovulation libère un ovule ; les règles marquent le début d'un nouveau cycle."),
  Q("Que sont les règles ?", ["La libération d'un ovule", "L'élimination de la muqueuse de l'utérus en l'absence de grossesse", "Une maladie", "La fécondation"], "L'élimination de la muqueuse de l'utérus en l'absence de grossesse", "La muqueuse utérine se reconstitue ensuite au cours du cycle."),
]),
notion('S-3', 2, I, 'svt-contraception', [
  Q("Comment agit la pilule contraceptive le plus souvent ?", ["Elle tue les spermatozoïdes", "Elle bloque l'ovulation grâce à des hormones de synthèse", "Elle protège des IST", "Elle provoque les règles"], "Elle bloque l'ovulation grâce à des hormones de synthèse", "La pilule ne protège pas des IST."),
  Q("Qu'est-ce que la contraception d'urgence (« pilule du lendemain ») ?", ["Une contraception régulière", "Une méthode à utiliser après un rapport non protégé, le plus tôt possible", "Un vaccin", "Un traitement des IST"], "Une méthode à utiliser après un rapport non protégé, le plus tôt possible", "Elle est délivrée gratuitement en pharmacie, sans ordonnance, y compris aux mineures."),
  Q("Qui peut accéder gratuitement à la contraception en France jusqu'à 25 ans ?", ["Seulement les femmes majeures", "Toutes les personnes de moins de 26 ans", "Personne", "Seulement les étudiants"], "Toutes les personnes de moins de 26 ans", "Depuis 2022, la contraception est prise en charge à 100 % jusqu'à 25 ans inclus."),
]),
notion('S-3', 3, I, 'svt-maladies-tabac', [
  Q("Quel gaz contenu dans la fumée de cigarette prend la place du dioxygène dans le sang ?", ["Le dioxyde de carbone", "Le monoxyde de carbone", "L'azote", "L'hélium"], "Le monoxyde de carbone", "Le monoxyde de carbone se fixe sur l'hémoglobine et réduit le transport du dioxygène."),
  Q("Quelle maladie est fortement liée au tabagisme ?", ["La rougeole", "Le cancer du poumon", "La varicelle", "La rage"], "Le cancer du poumon", "Le tabac est la première cause de mortalité évitable en France."),
  Q("Qu'est-ce que le tabagisme passif ?", ["Arrêter de fumer", "Respirer la fumée de tabac des autres", "Fumer une cigarette électronique", "Ne jamais fumer"], "Respirer la fumée de tabac des autres", "Il est nocif, notamment pour les enfants et les femmes enceintes."),
]),
notion('S-3', 3, I, 'svt-maladies-cardiovasculaires', [
  Q("Quel facteur augmente le risque de maladies cardiovasculaires ?", ["L'activité physique régulière", "Le tabac, la sédentarité et une alimentation trop riche en graisses et en sel", "Le sommeil suffisant", "La consommation de fruits"], "Le tabac, la sédentarité et une alimentation trop riche en graisses et en sel", "Ces facteurs favorisent le dépôt de graisses dans les artères (athérosclérose)."),
  Q("Qu'est-ce qu'un infarctus du myocarde ?", ["Une fracture", "La mort d'une partie du muscle cardiaque, privée de sang par l'obstruction d'une artère coronaire", "Une infection des poumons", "Une maladie de peau"], "La mort d'une partie du muscle cardiaque, privée de sang par l'obstruction d'une artère coronaire", "Appeler le 15 sans attendre augmente les chances de survie."),
  Q("Qu'est-ce que l'hypertension artérielle ?", ["Une pression du sang trop basse", "Une pression du sang trop élevée dans les artères", "Une fièvre", "Un manque de globules rouges"], "Une pression du sang trop élevée dans les artères", "Elle fatigue le cœur et abîme les vaisseaux ; l'excès de sel la favorise."),
]),
notion('S-3', 0, I, 'svt-vision', [
  Q("Quel élément de l'œil se déforme pour faire la mise au point (accommodation) ?", ["La rétine", "Le cristallin", "L'iris", "La cornée seule"], "Le cristallin", "Le cristallin, une lentille souple, change de forme pour voir net de près ou de loin."),
  Q("Quel est le rôle de l'iris ?", ["Former l'image", "Régler l'ouverture de la pupille selon la lumière", "Transmettre le message au cerveau", "Produire les larmes"], "Régler l'ouverture de la pupille selon la lumière", "La pupille se rétrécit à la lumière vive et s'agrandit dans l'obscurité."),
  Q("Quel défaut de la vision empêche de voir net de loin ?", ["La myopie", "L'hypermétropie", "La presbytie uniquement", "Le daltonisme"], "La myopie", "La myopie, en forte progression chez les jeunes, est corrigée par des verres divergents."),
]),
notion('S-1', 2, I, 'svt-bio-indicateurs', [
  Q("Qu'est-ce qu'un bio-indicateur ?", ["Un appareil électronique", "Un être vivant dont la présence ou l'absence renseigne sur la qualité d'un milieu", "Un engrais", "Un pesticide"], "Un être vivant dont la présence ou l'absence renseigne sur la qualité d'un milieu", "Lichens (air) ou larves d'insectes aquatiques (eau) sont des bio-indicateurs."),
  Q("Que signifie l'abondance de lichens variés sur les arbres d'une ville ?", ["Un air très pollué", "Un air de bonne qualité", "Un sol trop sec", "Une forte chaleur"], "Un air de bonne qualité", "Beaucoup de lichens sont sensibles à la pollution atmosphérique."),
  Q("La présence de larves de perles ou d'éphémères dans une rivière indique…", ["une eau très polluée", "une eau de bonne qualité", "une eau salée", "une eau stagnante"], "une eau de bonne qualité", "Ces larves sont sensibles à la pollution : elles disparaissent des eaux dégradées."),
  Q("Pourquoi utilise-t-on des bio-indicateurs plutôt que de simples mesures ponctuelles ?", ["Ils sont plus jolis", "Ils intègrent l'état du milieu sur une longue durée", "Ils sont obligatoires", "Ils remplacent toute analyse chimique"], "Ils intègrent l'état du milieu sur une longue durée", "Un être vivant reflète les conditions qu'il a subies au fil du temps."),
]),
notion('S-2', 1, I, 'svt-respiration-cellulaire', [
  Q("Que produisent les cellules en utilisant le glucose et le dioxygène ?", ["Du glucose et du dioxygène", "De l'énergie, du dioxyde de carbone et de l'eau", "De la chlorophylle", "Des sels minéraux"], "De l'énergie, du dioxyde de carbone et de l'eau", "C'est la respiration cellulaire, qui libère l'énergie utilisée par les cellules."),
  Q("Dans quels éléments de la cellule se déroule principalement la respiration cellulaire ?", ["Les chloroplastes", "Les mitochondries", "Le noyau", "La paroi"], "Les mitochondries", "Les mitochondries sont présentes dans les cellules animales et végétales."),
  Q("Comment le dioxygène arrive-t-il jusqu'aux cellules des muscles ?", ["Par les nerfs", "Transporté par le sang", "Par les os", "Directement par la peau"], "Transporté par le sang", "Le sang, mis en mouvement par le cœur, distribue dioxygène et nutriments à toutes les cellules."),
]),
notion('S-3', 1, I, 'svt-conservation-aliments', [
  Q("Pourquoi conserve-t-on les aliments au réfrigérateur ?", ["Pour tuer tous les microbes", "Pour ralentir la multiplication des micro-organismes", "Pour les rendre plus sucrés", "Pour les sécher"], "Pour ralentir la multiplication des micro-organismes", "Le froid ralentit les microbes sans les tuer ; la cuisson ou la stérilisation les détruisent."),
  Q("Quel procédé, mis au point par Pasteur, consiste à chauffer un liquide pour détruire une grande partie des microbes ?", ["La congélation", "La pasteurisation", "La lyophilisation", "Le salage"], "La pasteurisation", "La pasteurisation chauffe à moins de 100 °C ; la stérilisation, plus forte, détruit tous les microbes."),
  Q("Pourquoi ne faut-il pas recongeler un aliment décongelé ?", ["Il change de couleur", "Les microbes se sont multipliés pendant la décongélation", "Il devient toxique par le froid", "Il perd ses vitamines instantanément"], "Les microbes se sont multipliés pendant la décongélation", "Recongeler ne détruit pas les microbes qui se sont développés."),
]),
notion('S-1', 0, I, 'svt-volcanisme-contexte', [
  Q("Dans quel contexte géologique trouve-t-on surtout des volcans explosifs ?", ["Au niveau des dorsales", "Au niveau des zones de subduction", "Au centre des continents sans plaques", "Dans les déserts"], "Au niveau des zones de subduction", "Le magma, visqueux et riche en gaz, provoque des éruptions explosives (Mont Saint Helens, Pinatubo)."),
  Q("Comment appelle-t-on un nuage brûlant de gaz et de cendres qui dévale les pentes d'un volcan explosif ?", ["Une coulée de lave", "Une nuée ardente", "Un geyser", "Un tsunami"], "Une nuée ardente", "La nuée ardente de la montagne Pelée détruit Saint-Pierre (Martinique) en 1902."),
  Q("Le volcanisme d'Hawaï, au milieu d'une plaque, s'explique par…", ["une zone de subduction", "un point chaud", "une collision", "l'érosion"], "un point chaud", "Un panache de magma venu du manteau perce la plaque qui se déplace au-dessus, formant un chapelet d'îles."),
]),
]

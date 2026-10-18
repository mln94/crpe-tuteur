# Géographie 5e · Des ressources limitées, à gérer et à renouveler : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G5-2', 0, F, 'geo5-petrole', [
  Q("Quelle énergie fossile sert surtout à fabriquer l'essence et le gazole ?", ["Le pétrole", "Le charbon", "Le vent", "L'uranium"], "Le pétrole", "Il est extrait dans des gisements souterrains ou en mer."),
  Q("Quelle région du monde possède les plus grandes réserves de pétrole ?", ["Le Moyen-Orient", "L'Europe de l'Ouest", "L'Océanie", "L'Antarctique"], "Le Moyen-Orient", "L'Arabie saoudite en fait partie."),
  Q("Pourquoi dit-on que le pétrole est une ressource non renouvelable ?", ["Ses réserves s'épuisent car il met des millions d'années à se former", "Il se recrée chaque année", "Il est fabriqué en usine", "Il vient du vent"], "Ses réserves s'épuisent car il met des millions d'années à se former", "On l'appelle énergie fossile."),
]),
notion('G5-2', 0, F, 'geo5-solaire', [
  Q("Quel équipement transforme la lumière du soleil en électricité ?", ["Le panneau photovoltaïque", "L'éolienne", "Le barrage", "La centrale à charbon"], "Le panneau photovoltaïque", "L'énergie solaire est renouvelable."),
  Q("Quelles régions sont les plus favorables à l'énergie solaire ?", ["Les régions très ensoleillées, comme les déserts", "Les régions polaires", "Les forêts équatoriales très nuageuses", "Les grottes"], "Les régions très ensoleillées, comme les déserts", "Le Sahara a un potentiel immense."),
  Q("Quel pays produit le plus d'électricité solaire dans le monde ?", ["La Chine", "La France", "Le Canada", "La Norvège"], "La Chine", "Elle fabrique aussi la plupart des panneaux."),
]),
notion('G5-2', 0, F, 'geo5-economies-energie', [
  Q("Lequel de ces gestes permet d'économiser l'énergie ?", ["Éteindre la lumière en quittant une pièce", "Laisser la télévision en veille", "Chauffer avec les fenêtres ouvertes", "Prendre la voiture pour 200 mètres"], "Éteindre la lumière en quittant une pièce", "La sobriété énergétique commence par des gestes simples."),
  Q("Comment appelle-t-on l'isolation d'un logement pour consommer moins de chauffage ?", ["La rénovation énergétique", "L'urbanisation", "La déforestation", "L'irrigation"], "La rénovation énergétique", "Les « passoires thermiques » consomment beaucoup."),
  Q("Quel moyen de transport consomme le moins d'énergie par personne en ville ?", ["Le vélo", "La voiture individuelle", "L'avion", "Le camion"], "Le vélo", "La marche aussi !"),
]),
notion('G5-2', 0, F, 'geo5-cycle-eau', [
  Q("Comment appelle-t-on le circuit de l'eau entre océans, atmosphère et continents ?", ["Le cycle de l'eau", "Le cycle du carbone", "L'effet de serre", "La photosynthèse"], "Le cycle de l'eau", "Évaporation, condensation, précipitations, ruissellement."),
  Q("Comment appelle-t-on l'eau stockée dans le sous-sol ?", ["Les nappes phréatiques", "Les glaciers", "Les océans", "Les nuages"], "Les nappes phréatiques", "On y puise par des forages et des puits."),
  Q("Où se trouve la plus grande partie de l'eau douce de la planète ?", ["Dans les glaciers et les calottes polaires", "Dans les rivières", "Dans les lacs", "Dans les nuages"], "Dans les glaciers et les calottes polaires", "Elle est donc peu accessible."),
]),
notion('G5-2', 0, F, 'geo5-eau-quotidien', [
  Q("Combien de litres d'eau un Français consomme-t-il environ par jour à domicile ?", ["Environ 150 litres", "Environ 5 litres", "Environ 1 000 litres", "Environ 20 litres"], "Environ 150 litres", "Douches, toilettes, cuisine, lessive…"),
  Q("Quel geste permet d'économiser l'eau ?", ["Prendre une douche plutôt qu'un bain", "Laisser couler le robinet en se brossant les dents", "Arroser en plein midi", "Laver la voiture chaque jour"], "Prendre une douche plutôt qu'un bain", "Une douche consomme 3 à 4 fois moins d'eau."),
  Q("Qui va souvent chercher l'eau au puits dans les campagnes des pays pauvres ?", ["Les femmes et les enfants", "Les hommes d'affaires", "Les touristes", "Les fonctionnaires"], "Les femmes et les enfants", "Cela peut prendre plusieurs heures par jour."),
]),
notion('G5-2', 0, F, 'geo5-barrages', [
  Q("Quelle énergie produit-on grâce aux barrages ?", ["L'hydroélectricité", "L'énergie nucléaire", "L'énergie solaire", "L'énergie fossile"], "L'hydroélectricité", "C'est une énergie renouvelable."),
  Q("À quoi peut servir l'eau retenue par un barrage, en plus de produire de l'électricité ?", ["À irriguer les cultures et à fournir de l'eau potable", "À fabriquer du pétrole", "À créer des déserts", "À rien d'autre"], "À irriguer les cultures et à fournir de l'eau potable", "Les barrages régulent aussi les crues."),
  Q("Quel inconvénient un grand barrage peut-il avoir ?", ["Il oblige parfois à déplacer des populations et noie des terres", "Il pollue l'air", "Il produit des déchets nucléaires", "Il n'a aucun inconvénient"], "Il oblige parfois à déplacer des populations et noie des terres", "Les Trois-Gorges ont déplacé plus d'un million de personnes."),
]),
notion('G5-2', 1, F, 'geo5-cereales', [
  Q("Quelles sont les trois céréales les plus produites dans le monde ?", ["Le maïs, le riz et le blé", "L'orge, le seigle et l'avoine", "Le soja, le café et le cacao", "La pomme de terre, la tomate et le haricot"], "Le maïs, le riz et le blé", "Elles fournissent une grande partie de l'alimentation humaine."),
  Q("Quelle céréale est la base de l'alimentation en Asie ?", ["Le riz", "Le blé", "Le maïs", "L'orge"], "Le riz", "La Chine et l'Inde en sont les premiers producteurs."),
  Q("Quel pays est l'un des plus grands exportateurs de blé ?", ["La Russie", "Le Japon", "L'Égypte", "La Suisse"], "La Russie", "L'Égypte est au contraire un grand importateur."),
]),
notion('G5-2', 1, F, 'geo5-elevage', [
  Q("Quel animal fournit le lait, la viande et le cuir ?", ["La vache", "Le poulet", "Le cochon", "Le saumon"], "La vache", "L'élevage bovin est répandu dans le monde."),
  Q("Quel pays est le premier exportateur mondial de viande bovine ?", ["Le Brésil", "La France", "Le Japon", "L'Inde"], "Le Brésil", "Ses élevages progressent aux dépens de l'Amazonie."),
  Q("Pourquoi manger moins de viande peut-il aider à préserver les ressources ?", ["L'élevage consomme beaucoup d'eau, de terres et émet des gaz à effet de serre", "La viande est inutile", "Les animaux mangent du pétrole", "Ce n'est pas le cas"], "L'élevage consomme beaucoup d'eau, de terres et émet des gaz à effet de serre", "Il faut plusieurs kilos de céréales pour 1 kg de bœuf."),
]),
notion('G5-2', 1, F, 'geo5-famines', [
  Q("Qu'est-ce qu'une famine ?", ["Un manque grave de nourriture qui touche toute une population", "Un repas oublié", "Un régime alimentaire", "Une fête traditionnelle"], "Un manque grave de nourriture qui touche toute une population", "Elle peut provoquer de nombreux morts."),
  Q("Quelle est aujourd'hui la principale cause des famines ?", ["Les guerres et les conflits", "Le manque de terres sur la planète", "Le froid", "Le manque de pluie seul"], "Les guerres et les conflits", "Le Soudan, Gaza ou le Yémen en sont des exemples."),
  Q("Quel organisme de l'ONU distribue de la nourriture lors des crises ?", ["Le Programme alimentaire mondial (PAM)", "L'OMS", "L'Unesco", "Le FMI"], "Le Programme alimentaire mondial (PAM)", "Il a reçu le prix Nobel de la paix en 2020."),
]),
notion('G5-2', 1, F, 'geo5-circuits-courts', [
  Q("Qu'est-ce qu'un circuit court ?", ["Une vente avec au plus un intermédiaire entre le producteur et le consommateur", "Une course de vélo", "Un circuit électrique", "Un long voyage des marchandises"], "Une vente avec au plus un intermédiaire entre le producteur et le consommateur", "Les AMAP et les marchés de producteurs en sont des exemples."),
  Q("Pourquoi manger des fruits de saison produits localement ?", ["Pour limiter les transports et le chauffage des serres", "Parce qu'ils sont toujours plus chers", "Parce que c'est obligatoire", "Pour gaspiller"], "Pour limiter les transports et le chauffage des serres", "C'est une consommation plus durable."),
  Q("Que signifie le sigle AMAP ?", ["Association pour le maintien d'une agriculture paysanne", "Agence des marchés agricoles publics", "Association des mangeurs à Paris", "Atelier municipal d'alimentation populaire"], "Association pour le maintien d'une agriculture paysanne", "Les consommateurs s'engagent auprès d'un agriculteur."),
]),
notion('G5-2', 1, F, 'geo5-gaspillage', [
  Q("Combien de kilos de nourriture un Français jette-t-il environ par an ?", ["Environ 30 kg", "Environ 1 kg", "Environ 500 kg", "Rien du tout"], "Environ 30 kg", "Dont environ 7 kg d'aliments encore emballés."),
  Q("Quel geste limite le gaspillage alimentaire à la cantine ?", ["Ne prendre que ce qu'on va manger", "Prendre double portion", "Jeter le pain", "Refuser de goûter"], "Ne prendre que ce qu'on va manger", "Beaucoup de cantines pèsent leurs déchets."),
  Q("Que doivent faire les supermarchés de leurs invendus alimentaires depuis 2016 en France ?", ["Les donner à des associations plutôt que les jeter", "Les brûler", "Les jeter dans la mer", "Les vendre plus cher"], "Les donner à des associations plutôt que les jeter", "C'est la loi Garot."),
]),
notion('G5-2', 0, F, 'geo5-nucleaire', [
  Q("Quel combustible utilisent les centrales nucléaires ?", ["L'uranium", "Le charbon", "Le bois", "Le gaz"], "L'uranium", "Il n'est pas renouvelable."),
  Q("Quel avantage présente l'énergie nucléaire pour le climat ?", ["Elle émet très peu de CO2", "Elle ne produit aucun déchet", "Elle est renouvelable", "Elle n'a besoin d'aucune eau"], "Elle émet très peu de CO2", "Mais elle produit des déchets radioactifs."),
  Q("Quel problème pose l'énergie nucléaire ?", ["La gestion des déchets radioactifs et le risque d'accident", "Elle pollue l'air de fumées noires", "Elle dépend du vent", "Elle fait fondre les glaciers directement"], "La gestion des déchets radioactifs et le risque d'accident", "Certains déchets restent dangereux des milliers d'années."),
]),
# ══ Intermédiaire ══
notion('G5-2', 0, I, 'geo5i-mix-energetique', [
  Q("Comment appelle-t-on la répartition des différentes sources d'énergie utilisées par un pays ?", ["Le mix (ou bouquet) énergétique", "Le cycle de l'eau", "Le PIB", "L'empreinte écologique"], "Le mix (ou bouquet) énergétique", "Il varie beaucoup selon les pays."),
  Q("Quelle part de l'énergie consommée dans le monde provient encore des énergies fossiles ?", ["Environ 80 %", "Environ 10 %", "Environ 40 %", "Presque 100 %"], "Environ 80 %", "Pétrole, gaz et charbon dominent encore."),
  Q("Quel pays produit l'essentiel de son électricité grâce à l'hydroélectricité ?", ["La Norvège", "La Pologne", "L'Arabie saoudite", "Le Qatar"], "La Norvège", "Plus de 85 % de son électricité est hydraulique."),
]),
notion('G5-2', 0, I, 'geo5i-charbon', [
  Q("Quel pays est le premier producteur et consommateur de charbon du monde ?", ["La Chine", "La France", "Le Brésil", "Le Japon"], "La Chine", "Elle consomme plus de la moitié du charbon mondial."),
  Q("Pourquoi le charbon est-il l'énergie la plus nocive pour le climat ?", ["C'est l'énergie fossile qui émet le plus de CO2 par unité d'énergie", "Il est radioactif", "Il est rare", "Il ne brûle pas"], "C'est l'énergie fossile qui émet le plus de CO2 par unité d'énergie", "Il pollue aussi l'air localement."),
  Q("En quelle année la dernière mine de charbon française a-t-elle fermé ?", ["2004", "1950", "1870", "2023"], "2004", "C'était la mine de La Houve, en Moselle."),
]),
notion('G5-2', 0, I, 'geo5i-opep', [
  Q("Quelle organisation regroupe de grands pays exportateurs de pétrole ?", ["L'OPEP", "L'OTAN", "L'ONU", "L'OMS"], "L'OPEP", "Elle est créée en 1960."),
  Q("Quel pays est le premier producteur de pétrole du monde ?", ["Les États-Unis", "La France", "L'Inde", "Le Japon"], "Les États-Unis", "Grâce au pétrole de schiste."),
  Q("Pourquoi les prix du pétrole peuvent-ils varier fortement ?", ["À cause des guerres, des décisions de l'OPEP et de la demande", "Ils ne varient jamais", "À cause de la météo seulement", "À cause des élections françaises"], "À cause des guerres, des décisions de l'OPEP et de la demande", "Les chocs pétroliers de 1973 et 1979 l'ont montré."),
]),
notion('G5-2', 0, I, 'geo5i-eolien', [
  Q("Où trouve-t-on les éoliennes les plus puissantes ?", ["En mer (éolien offshore)", "Dans les forêts", "En ville", "Dans les déserts sans vent"], "En mer (éolien offshore)", "Le vent y est plus fort et plus régulier."),
  Q("Quel est le principal inconvénient des énergies solaire et éolienne ?", ["Leur production est intermittente", "Elles émettent beaucoup de CO2", "Elles produisent des déchets radioactifs", "Elles sont épuisables"], "Leur production est intermittente", "Il faut stocker l'énergie ou combiner les sources."),
  Q("Quel est le premier parc éolien en mer mis en service en France, en 2022 ?", ["Celui de Saint-Nazaire", "Celui de Marseille", "Celui de Lyon", "Celui de Strasbourg"], "Celui de Saint-Nazaire", "Il compte 80 éoliennes."),
]),
notion('G5-2', 0, I, 'geo5i-acces-eau', [
  Q("Environ combien de personnes n'ont pas accès à une eau potable gérée en toute sécurité ?", ["Environ 2 milliards", "Environ 20 millions", "Environ 200 000", "Personne"], "Environ 2 milliards", "Surtout en Afrique subsaharienne et en Asie du Sud."),
  Q("Quel jour est célébrée la Journée mondiale de l'eau ?", ["Le 22 mars", "Le 5 juin", "Le 1er mai", "Le 14 juillet"], "Le 22 mars", "Elle est instituée par l'ONU en 1993."),
  Q("Quelles maladies l'eau insalubre peut-elle transmettre ?", ["Le choléra et la diarrhée", "La grippe", "La myopie", "L'asthme"], "Le choléra et la diarrhée", "Les diarrhées tuent encore des centaines de milliers d'enfants par an."),
]),
notion('G5-2', 0, I, 'geo5i-tensions-eau', [
  Q("Quels pays se disputent l'eau du Tigre et de l'Euphrate ?", ["La Turquie, la Syrie et l'Irak", "La France et l'Espagne", "Le Canada et les États-Unis", "Le Brésil et l'Argentine"], "La Turquie, la Syrie et l'Irak", "La Turquie a construit de grands barrages en amont."),
  Q("Quel avantage a un pays situé en amont d'un fleuve ?", ["Il peut contrôler le débit qui arrive aux pays en aval", "Il reçoit plus de pluie", "Il a plus de poissons", "Aucun"], "Il peut contrôler le débit qui arrive aux pays en aval", "C'est une source de tensions."),
  Q("Quelle mer d'Asie centrale a presque disparu à cause de l'irrigation du coton ?", ["La mer d'Aral", "La mer Noire", "La mer Caspienne", "La mer Morte"], "La mer d'Aral", "C'est l'une des pires catastrophes environnementales."),
]),
notion('G5-2', 0, I, 'geo5i-eau-agriculture', [
  Q("Quelle part de l'eau douce prélevée dans le monde sert à l'agriculture ?", ["Environ 70 %", "Environ 10 %", "Environ 30 %", "Environ 95 %"], "Environ 70 %", "Surtout pour l'irrigation."),
  Q("Comment appelle-t-on l'apport artificiel d'eau aux cultures ?", ["L'irrigation", "Le drainage", "L'assolement", "La jachère"], "L'irrigation", "Elle permet de cultiver dans des régions sèches."),
  Q("Pourquoi les « méga-bassines » font-elles débat en France ?", ["Elles stockent l'eau pour l'irrigation mais sont accusées de favoriser quelques agriculteurs", "Ce sont des piscines publiques", "Elles produisent de l'électricité", "Elles servent à la pêche"], "Elles stockent l'eau pour l'irrigation mais sont accusées de favoriser quelques agriculteurs", "Le conflit de Sainte-Soline en 2023 en est un exemple."),
]),
notion('G5-2', 0, I, 'geo5i-eau-virtuelle', [
  Q("Qu'appelle-t-on l'eau virtuelle ?", ["L'eau utilisée pour produire un bien", "L'eau des jeux vidéo", "L'eau de pluie", "L'eau de mer"], "L'eau utilisée pour produire un bien", "Il faut environ 15 000 litres d'eau pour 1 kg de bœuf."),
  Q("Combien de litres d'eau environ faut-il pour produire un jean ?", ["Plusieurs milliers", "10", "100", "1"], "Plusieurs milliers", "Surtout pour cultiver le coton."),
  Q("Qu'est-ce que l'empreinte eau d'un pays ?", ["Le volume total d'eau nécessaire pour produire ce qu'il consomme", "La surface de ses lacs", "La longueur de ses fleuves", "Son nombre de piscines"], "Le volume total d'eau nécessaire pour produire ce qu'il consomme", "Importer des produits, c'est aussi importer de l'eau."),
]),
notion('G5-2', 1, I, 'geo5i-revolution-verte', [
  Q("Dans quel pays la révolution verte a-t-elle permis d'éviter les famines dans les années 1960-1970 ?", ["L'Inde", "La France", "Le Canada", "L'Australie"], "L'Inde", "Grâce à des variétés à haut rendement."),
  Q("Quels sont les inconvénients de la révolution verte ?", ["Épuisement des sols et des nappes, pollution par les engrais", "Baisse des rendements", "Disparition de l'irrigation", "Aucun"], "Épuisement des sols et des nappes, pollution par les engrais", "Le Pendjab en subit aujourd'hui les effets."),
  Q("Quel agronome américain, « père de la révolution verte », reçoit le prix Nobel de la paix en 1970 ?", ["Norman Borlaug", "Albert Einstein", "Martin Luther King", "Al Gore"], "Norman Borlaug", "Il a créé des variétés de blé à haut rendement."),
]),
notion('G5-2', 1, I, 'geo5i-agriculture-productiviste', [
  Q("Quelle région des États-Unis est célèbre pour ses immenses cultures de maïs ?", ["La Corn Belt", "La Sun Belt", "La Silicon Valley", "La Rust Belt"], "La Corn Belt", "Elle se situe dans le Midwest."),
  Q("Qu'est-ce qu'une agriculture productiviste ?", ["Une agriculture qui cherche à produire le plus possible avec des intrants et des machines", "Une agriculture sans machines", "Une agriculture de subsistance", "Une agriculture biologique"], "Une agriculture qui cherche à produire le plus possible avec des intrants et des machines", "Elle obtient de forts rendements."),
  Q("Comment appelle-t-on les engrais, pesticides et semences achetés par l'agriculteur ?", ["Les intrants", "Les extrants", "Les rendements", "Les jachères"], "Les intrants", "Ils augmentent les rendements mais coûtent cher."),
]),
notion('G5-2', 1, I, 'geo5i-soja-amazonie', [
  Q("Pourquoi la culture du soja progresse-t-elle au Brésil ?", ["Pour nourrir le bétail en Chine et en Europe", "Pour faire du pain", "Pour fabriquer des vêtements", "Pour produire de l'électricité"], "Pour nourrir le bétail en Chine et en Europe", "Le Brésil en est le premier exportateur mondial."),
  Q("Quelle conséquence l'extension du soja et de l'élevage a-t-elle en Amazonie ?", ["La déforestation", "L'augmentation des forêts", "La baisse des températures", "La fonte des glaces"], "La déforestation", "On parle de front pionnier agricole."),
  Q("Comment appelle-t-on une zone où l'on défriche pour mettre en culture de nouvelles terres ?", ["Un front pionnier", "Un désert", "Une métropole", "Une ZEE"], "Un front pionnier", "L'Amazonie brésilienne en est l'exemple type."),
]),
notion('G5-2', 1, I, 'geo5i-dependance-alimentaire', [
  Q("Quel pays est le premier importateur mondial de blé ?", ["L'Égypte", "La Russie", "La France", "Le Canada"], "L'Égypte", "Le pain est subventionné par l'État."),
  Q("Quelle crise de 2022 a fait flamber les prix du blé dans le monde ?", ["La guerre en Ukraine", "La crise de 1929", "La chute du mur de Berlin", "Le Brexit"], "La guerre en Ukraine", "L'Ukraine est un grand exportateur de céréales."),
  Q("Comment appelle-t-on la capacité d'un pays à produire lui-même sa nourriture ?", ["La souveraineté (ou l'autosuffisance) alimentaire", "La sécurité routière", "La croissance démographique", "L'urbanisation"], "La souveraineté (ou l'autosuffisance) alimentaire", "C'est un enjeu stratégique."),
]),
notion('G5-2', 1, I, 'geo5i-peche', [
  Q("Quel pays est le premier producteur mondial de poissons, par la pêche et l'aquaculture ?", ["La Chine", "La France", "Le Mali", "La Suisse"], "La Chine", "Elle domine surtout l'aquaculture."),
  Q("Quelle part des stocks de poissons marins est surexploitée selon la FAO ?", ["Plus d'un tiers", "Presque aucun", "La totalité", "Environ 5 %"], "Plus d'un tiers", "La part a fortement augmenté depuis 1970."),
  Q("Comment appelle-t-on les règles qui limitent les quantités de poissons pêchés ?", ["Les quotas de pêche", "Les droits de douane", "Les ZEE", "Les labels bio"], "Les quotas de pêche", "L'Union européenne les fixe chaque année."),
]),
notion('G5-2', 1, I, 'geo5i-obesite', [
  Q("Quelle maladie liée à l'alimentation progresse dans le monde, y compris dans les pays du Sud ?", ["L'obésité", "Le scorbut", "La peste", "La lèpre"], "L'obésité", "Plus d'un milliard de personnes sont obèses."),
  Q("Comment appelle-t-on la coexistence de la sous-alimentation et de l'obésité dans un même pays ?", ["Le double fardeau de la malnutrition", "La révolution verte", "La transition démographique", "La sécurité alimentaire"], "Le double fardeau de la malnutrition", "C'est le cas en Inde ou au Mexique."),
  Q("Quel logo informe sur la qualité nutritionnelle des aliments en France ?", ["Le Nutri-Score", "Le label bio", "Le marquage CE", "L'étiquette énergie"], "Le Nutri-Score", "Il va de A (vert) à E (rouge)."),
]),
notion('G5-2', 1, I, 'geo5i-agroecologie', [
  Q("Qu'est-ce que l'agroécologie ?", ["Une agriculture qui s'appuie sur les équilibres naturels pour produire durablement", "Une agriculture sans plantes", "Une agriculture uniquement en serre", "Une agriculture qui utilise plus de pesticides"], "Une agriculture qui s'appuie sur les équilibres naturels pour produire durablement", "Haies, rotations, couverts végétaux…"),
  Q("Qu'est-ce que l'agroforesterie ?", ["Associer des arbres aux cultures ou à l'élevage", "Couper toutes les forêts", "Planter uniquement des arbres", "Cultiver en ville"], "Associer des arbres aux cultures ou à l'élevage", "Les arbres protègent les sols et stockent du carbone."),
  Q("Pourquoi replante-t-on des haies dans les campagnes françaises ?", ["Pour protéger la biodiversité, les sols et l'eau", "Pour gêner les tracteurs", "Pour décorer uniquement", "Pour produire du pétrole"], "Pour protéger la biodiversité, les sols et l'eau", "Le remembrement en avait supprimé beaucoup."),
]),
# ══ Avancé ══
notion('G5-2', 0, D, 'geo5d-transition-energetique', [
  Q("Comment appelle-t-on le passage d'un système fondé sur les énergies fossiles à un système fondé sur les énergies bas carbone ?", ["La transition énergétique", "La transition démographique", "La révolution industrielle", "L'exode rural"], "La transition énergétique", "Elle est au cœur de la lutte contre le changement climatique."),
  Q("Quel métal, indispensable aux batteries, est surtout extrait en Australie, au Chili et en Argentine ?", ["Le lithium", "L'or", "Le plomb", "L'étain"], "Le lithium", "Le « triangle du lithium » est en Amérique du Sud."),
  Q("Quel pays raffine la grande majorité des métaux critiques nécessaires à la transition énergétique ?", ["La Chine", "La France", "Le Brésil", "Le Royaume-Uni"], "La Chine", "Cela crée une forte dépendance pour les autres pays."),
]),
notion('G5-2', 0, D, 'geo5d-gaz-schiste', [
  Q("Quelle technique permet d'extraire le gaz et le pétrole de schiste ?", ["La fracturation hydraulique", "La géothermie", "La photosynthèse", "La désalinisation"], "La fracturation hydraulique", "Elle est interdite en France depuis 2011."),
  Q("Quel pays est devenu le premier exportateur mondial de gaz naturel liquéfié (GNL) grâce au gaz de schiste ?", ["Les États-Unis", "La France", "L'Allemagne", "Le Japon"], "Les États-Unis", "Ils exportent par méthaniers."),
  Q("Pourquoi l'Europe a-t-elle cherché d'autres fournisseurs de gaz après 2022 ?", ["Pour réduire sa dépendance au gaz russe", "Parce que le gaz est devenu gratuit", "Parce que le gaz était épuisé en Europe", "Pour fermer toutes les centrales nucléaires"], "Pour réduire sa dépendance au gaz russe", "La guerre en Ukraine a provoqué une crise énergétique."),
]),
notion('G5-2', 0, D, 'geo5d-precarite-energetique', [
  Q("Qu'est-ce que la précarité énergétique ?", ["La difficulté à payer l'énergie nécessaire pour se chauffer ou s'éclairer", "La faiblesse des éoliennes", "Le manque de pétrole dans un pays", "La fermeture des centrales"], "La difficulté à payer l'énergie nécessaire pour se chauffer ou s'éclairer", "Elle touche des millions de Français."),
  Q("Qu'est-ce qu'une « passoire thermique » ?", ["Un logement mal isolé, classé F ou G au diagnostic de performance énergétique", "Un ustensile de cuisine", "Une centrale électrique", "Un barrage fuyant"], "Un logement mal isolé, classé F ou G au diagnostic de performance énergétique", "La loi interdit progressivement de les louer."),
  Q("Quel document classe un logement de A à G selon sa consommation d'énergie ?", ["Le diagnostic de performance énergétique (DPE)", "Le cadastre", "Le permis de construire", "Le plan local d'urbanisme"], "Le diagnostic de performance énergétique (DPE)", "Il est obligatoire pour vendre ou louer."),
]),
notion('G5-2', 0, D, 'geo5d-nucleaire-france', [
  Q("Quelle part de l'électricité française vient du nucléaire ?", ["Environ 65 à 70 %", "Environ 10 %", "Environ 30 %", "100 %"], "Environ 65 à 70 %", "C'est la part la plus élevée du monde."),
  Q("Combien de réacteurs nucléaires sont en service en France ?", ["57", "5", "200", "12"], "57", "Le réacteur EPR de Flamanville a été raccordé fin 2024."),
  Q("Où se trouve le projet de stockage profond des déchets radioactifs les plus dangereux (Cigéo) ?", ["À Bure, dans la Meuse", "À Paris", "En Corse", "En Guyane"], "À Bure, dans la Meuse", "Il est très contesté."),
]),
notion('G5-2', 0, D, 'geo5d-geothermie-biomasse', [
  Q("Qu'est-ce que la géothermie ?", ["L'utilisation de la chaleur du sous-sol", "L'énergie des marées", "L'énergie du vent", "L'énergie du soleil"], "L'utilisation de la chaleur du sous-sol", "L'Islande en tire une grande partie de son énergie."),
  Q("Qu'est-ce que la biomasse énergie ?", ["L'énergie tirée du bois, des déchets agricoles ou organiques", "L'énergie nucléaire", "L'énergie du pétrole", "L'énergie des volcans"], "L'énergie tirée du bois, des déchets agricoles ou organiques", "C'est la première énergie renouvelable en France."),
  Q("Quelle usine française produit de l'électricité grâce aux marées depuis 1966 ?", ["L'usine marémotrice de la Rance", "La centrale de Flamanville", "Le barrage de Serre-Ponçon", "La centrale de Fessenheim"], "L'usine marémotrice de la Rance", "Elle se trouve en Bretagne, près de Saint-Malo."),
]),
notion('G5-2', 0, D, 'geo5d-stress-hydrique', [
  Q("En dessous de quel volume d'eau disponible par habitant et par an parle-t-on de pénurie d'eau ?", ["1 000 m³", "100 000 m³", "10 m³", "50 000 m³"], "1 000 m³", "En dessous de 1 700 m³, on parle de stress hydrique."),
  Q("Quelle région du monde est la plus touchée par le stress hydrique ?", ["Le Moyen-Orient et l'Afrique du Nord", "L'Europe du Nord", "L'Amazonie", "Le Canada"], "Le Moyen-Orient et l'Afrique du Nord", "Ces régions sont arides et très peuplées."),
  Q("Quelle grande ville a failli manquer d'eau en 2018, menacée d'un « jour zéro » ?", ["Le Cap, en Afrique du Sud", "Londres", "Oslo", "Vancouver"], "Le Cap, en Afrique du Sud", "Les habitants ont dû réduire drastiquement leur consommation."),
]),
notion('G5-2', 0, D, 'geo5d-gestion-eau-france', [
  Q("Quels organismes gèrent l'eau par grands bassins versants en France ?", ["Les agences de l'eau", "Les préfectures maritimes", "Les régions", "Les chambres de commerce"], "Les agences de l'eau", "Il en existe six en métropole."),
  Q("Qu'est-ce qu'un bassin versant ?", ["Le territoire dont toutes les eaux s'écoulent vers un même cours d'eau", "Un bassin de piscine", "Une baignoire", "Un port"], "Le territoire dont toutes les eaux s'écoulent vers un même cours d'eau", "C'est l'échelle naturelle de gestion de l'eau."),
  Q("Qu'est-ce que la réutilisation des eaux usées traitées (REUT) ?", ["Utiliser les eaux sorties des stations d'épuration pour irriguer ou arroser", "Boire l'eau de mer", "Jeter les eaux usées dans la rivière", "Faire de la neige artificielle"], "Utiliser les eaux sorties des stations d'épuration pour irriguer ou arroser", "La France l'utilise encore très peu."),
]),
notion('G5-2', 0, D, 'geo5d-desalinisation', [
  Q("Quel pays tire la majorité de son eau potable du dessalement de l'eau de mer ?", ["Israël", "La France", "La Norvège", "Le Canada"], "Israël", "Il recycle aussi la majorité de ses eaux usées."),
  Q("Quel est l'inconvénient du dessalement de l'eau de mer ?", ["Il consomme beaucoup d'énergie et rejette de la saumure", "Il ne produit pas d'eau douce", "Il pollue l'air de fumées toxiques", "Il est gratuit"], "Il consomme beaucoup d'énergie et rejette de la saumure", "La saumure est très salée et nuit aux fonds marins."),
  Q("Quelle région du monde possède le plus d'usines de dessalement ?", ["Le golfe Persique", "L'Europe du Nord", "L'Amazonie", "La Sibérie"], "Le golfe Persique", "L'Arabie saoudite et les Émirats en dépendent."),
]),
notion('G5-2', 1, D, 'geo5d-faim-chiffres', [
  Q("Quelle part de la population mondiale souffre de la faim au milieu des années 2020 ?", ["Environ 9 %", "Environ 50 %", "Environ 0,1 %", "Environ 30 %"], "Environ 9 %", "Soit environ 700 millions de personnes."),
  Q("La production agricole mondiale serait-elle suffisante pour nourrir toute l'humanité ?", ["Oui, le problème est surtout l'accès à la nourriture", "Non, elle est bien trop faible", "Elle ne nourrit que l'Europe", "Elle ne nourrit que l'Asie"], "Oui, le problème est surtout l'accès à la nourriture", "La pauvreté et les conflits empêchent l'accès."),
  Q("Quel économiste indien a montré que les famines viennent souvent d'un défaut d'accès plutôt que d'un manque de nourriture ?", ["Amartya Sen", "Thomas Malthus", "Adam Smith", "Karl Marx"], "Amartya Sen", "Il a étudié la famine du Bengale de 1943."),
]),
notion('G5-2', 1, D, 'geo5d-pac-agriculture-ue', [
  Q("Quelle politique européenne soutient les revenus des agriculteurs depuis 1962 ?", ["La politique agricole commune (PAC)", "Le plan Marshall", "Le pacte vert seul", "La politique de cohésion"], "La politique agricole commune (PAC)", "C'est l'un des premiers postes du budget européen."),
  Q("Quel accord commercial entre l'UE et des pays d'Amérique du Sud inquiète les agriculteurs français ?", ["L'accord avec le Mercosur", "L'accord de Schengen", "Le traité de l'Élysée", "L'accord de Paris"], "L'accord avec le Mercosur", "Ils craignent une concurrence aux normes moins strictes."),
  Q("Quelle part environ des actifs français travaille dans l'agriculture ?", ["Moins de 3 %", "Environ 30 %", "Environ 50 %", "Environ 15 %"], "Moins de 3 %", "Mais la France reste une grande puissance agricole."),
]),
notion('G5-2', 1, D, 'geo5d-semences-ogm', [
  Q("Qu'est-ce qu'un OGM ?", ["Un organisme dont le patrimoine génétique a été modifié en laboratoire", "Un engrais naturel", "Un produit bio", "Un insecte nuisible"], "Un organisme dont le patrimoine génétique a été modifié en laboratoire", "Leur culture est interdite en France."),
  Q("Quel pays cultive le plus d'OGM dans le monde ?", ["Les États-Unis", "La France", "Le Japon", "L'Italie"], "Les États-Unis", "Maïs, soja et coton surtout."),
  Q("Quelle réserve mondiale de graines est creusée dans le permafrost de l'archipel du Svalbard ?", ["La Réserve mondiale de semences du Svalbard", "Le Muséum d'histoire naturelle", "La banque de France", "Le Jardin des Plantes"], "La Réserve mondiale de semences du Svalbard", "Elle protège la diversité des plantes cultivées."),
]),
notion('G5-2', 1, D, 'geo5d-agriculture-urbaine', [
  Q("Qu'est-ce que l'agriculture urbaine ?", ["La production de nourriture en ville, sur des toits ou des friches", "L'agriculture des grandes plaines", "L'élevage en montagne", "La pêche en mer"], "La production de nourriture en ville, sur des toits ou des friches", "Elle reste marginale en volume."),
  Q("Quelle ville a vu son agriculture urbaine se développer à grande échelle après 1990, faute d'importations ?", ["La Havane, à Cuba", "Paris", "Londres", "Tokyo"], "La Havane, à Cuba", "Après la fin de l'aide soviétique."),
  Q("Qu'est-ce que la culture hydroponique ?", ["La culture de plantes hors-sol, dans de l'eau enrichie", "La culture sur brûlis", "La culture en terrasses", "La culture du riz inondé"], "La culture de plantes hors-sol, dans de l'eau enrichie", "Elle est utilisée dans les fermes verticales."),
]),
notion('G5-2', 1, D, 'geo5d-sols', [
  Q("Pourquoi les sols sont-ils une ressource précieuse ?", ["Ils se forment très lentement et nourrissent les cultures", "Ils se reforment en un an", "Ils sont infinis", "Ils ne servent qu'à construire"], "Ils se forment très lentement et nourrissent les cultures", "Il faut des siècles pour former quelques centimètres de sol."),
  Q("Comment appelle-t-on la perte de sol emportée par l'eau ou le vent ?", ["L'érosion", "L'irrigation", "L'urbanisation", "La sédimentation marine"], "L'érosion", "Elle est aggravée par la déforestation et le labour."),
  Q("Quelle technique aide à protéger les sols en pente ?", ["Les cultures en terrasses", "Le labour dans le sens de la pente", "La déforestation", "Le brûlis"], "Les cultures en terrasses", "Les rizières d'Asie en sont un bel exemple."),
]),
notion('G5-2', 0, D, 'geo5d-sobriete-efficacite', [
  Q("Quelle différence y a-t-il entre sobriété et efficacité énergétiques ?", ["La sobriété réduit les besoins ; l'efficacité consomme moins pour le même service", "Elles sont identiques", "La sobriété augmente la consommation", "L'efficacité supprime l'énergie"], "La sobriété réduit les besoins ; l'efficacité consomme moins pour le même service", "Baisser le chauffage (sobriété), isoler (efficacité)."),
  Q("Quel objectif la France s'est-elle fixé pour 2050 ?", ["La neutralité carbone", "Doubler sa consommation de pétrole", "Fermer toutes ses usines", "Abandonner l'électricité"], "La neutralité carbone", "C'est la stratégie nationale bas-carbone."),
  Q("Qu'est-ce que l'« effet rebond » ?", ["Quand des économies d'énergie sont annulées par une hausse de l'usage", "Un rebond de ballon", "Une hausse des prix", "Une baisse de la population"], "Quand des économies d'énergie sont annulées par une hausse de l'usage", "Une voiture plus économe peut inciter à rouler davantage."),
]),
]

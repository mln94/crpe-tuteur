# Géographie 3e · Dynamiques territoriales de la France contemporaine : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G3-1', 0, F, 'geo3-grandes-villes-france', [
  Q("Quelle est la troisième ville de France par sa population (commune) ?", ["Lyon", "Lille", "Nice", "Nantes"], "Lyon", "Après Paris et Marseille."),
  Q("Quelle ville est la plus peuplée du sud-ouest de la France ?", ["Toulouse", "Bordeaux", "Montpellier", "Pau"], "Toulouse", "C'est la quatrième commune de France."),
  Q("Quelle grande ville se trouve au bord de la Garonne ?", ["Bordeaux", "Lyon", "Strasbourg", "Lille"], "Bordeaux", "Son port de la Lune est classé à l'Unesco."),
]),
notion('G3-1', 0, F, 'geo3-fleuves-villes', [
  Q("Quel fleuve traverse Paris ?", ["La Seine", "La Loire", "Le Rhône", "La Garonne"], "La Seine", "Elle se jette dans la Manche au Havre."),
  Q("Quel est le plus long fleuve de France ?", ["La Loire", "La Seine", "Le Rhône", "La Garonne"], "La Loire", "Environ 1 000 km."),
  Q("À la confluence de quels cours d'eau se trouve Lyon ?", ["Le Rhône et la Saône", "La Seine et la Marne", "La Loire et le Cher", "La Garonne et la Dordogne"], "Le Rhône et la Saône", "La confluence est un lieu de passage historique."),
]),
notion('G3-1', 0, F, 'geo3-periurbain-vie', [
  Q("Quel mode de transport domine dans les espaces périurbains ?", ["La voiture", "Le métro", "Le vélo", "Le bateau"], "La voiture", "Les transports en commun y sont rares."),
  Q("Quel type de logement domine dans les communes périurbaines ?", ["La maison individuelle", "Le gratte-ciel", "Le grand ensemble", "Le château"], "La maison individuelle", "Souvent dans des lotissements."),
  Q("Pourquoi de nombreuses familles s'installent-elles dans le périurbain ?", ["Pour avoir une maison avec jardin à un prix plus abordable", "Pour être plus près de leur travail en centre-ville", "Pour éviter de prendre la voiture", "Parce que c'est obligatoire"], "Pour avoir une maison avec jardin à un prix plus abordable", "Le foncier y est moins cher qu'en ville."),
]),
notion('G3-1', 0, F, 'geo3-paris-region', [
  Q("Quelle région française est la plus peuplée ?", ["L'Île-de-France", "La Bretagne", "La Corse", "La Normandie"], "L'Île-de-France", "Plus de 12 millions d'habitants."),
  Q("Quelle part du PIB français est produite en Île-de-France ?", ["Environ 30 %", "Environ 5 %", "Environ 70 %", "Environ 10 %"], "Environ 30 %", "La région concentre les sièges sociaux."),
  Q("Combien de régions compte la France métropolitaine depuis 2016 ?", ["13", "22", "18", "5"], "13", "Avec les 5 régions d'outre-mer, on en compte 18."),
]),
notion('G3-1', 1, F, 'geo3-secteurs-activite', [
  Q("À quel secteur appartient l'agriculture ?", ["Le secteur primaire", "Le secteur secondaire", "Le secteur tertiaire", "Aucun secteur"], "Le secteur primaire", "Il comprend aussi la pêche et l'exploitation forestière."),
  Q("À quel secteur appartient l'industrie ?", ["Le secteur secondaire", "Le secteur primaire", "Le secteur tertiaire", "Le secteur quaternaire"], "Le secteur secondaire", "Il transforme les matières premières."),
  Q("Quel secteur emploie le plus de Français ?", ["Le secteur tertiaire (services)", "Le secteur primaire", "Le secteur secondaire", "Ils emploient autant"], "Le secteur tertiaire (services)", "Environ trois actifs sur quatre."),
]),
notion('G3-1', 1, F, 'geo3-vignoble', [
  Q("Quelles régions françaises sont célèbres pour leurs vins ?", ["La Bourgogne, le Bordelais, la Champagne", "La Beauce et la Brie", "Le Massif central et les Landes", "La Lorraine et le Nord"], "La Bourgogne, le Bordelais, la Champagne", "La viticulture est une production de qualité."),
  Q("Que garantit une appellation d'origine protégée (AOP) ?", ["Qu'un produit est fabriqué dans une zone précise selon un savoir-faire reconnu", "Qu'il est bon marché", "Qu'il est importé", "Qu'il est industriel"], "Qu'un produit est fabriqué dans une zone précise selon un savoir-faire reconnu", "Le roquefort ou le comté sont des AOP."),
  Q("Quel fromage AOP est produit dans le Jura ?", ["Le comté", "Le camembert", "Le roquefort", "Le brie de Meaux"], "Le comté", "C'est le premier fromage AOP de France en volume."),
]),
notion('G3-1', 1, F, 'geo3-industries-france', [
  Q("Quel constructeur automobile français a son siège près de Paris, à Boulogne-Billancourt ?", ["Renault", "Toyota", "Volkswagen", "Fiat"], "Renault", "Stellantis (Peugeot, Citroën) est l'autre grand groupe."),
  Q("Quelle industrie est très développée autour de Toulouse et de Bordeaux ?", ["L'aéronautique et le spatial", "Le textile", "La sidérurgie", "Le charbon"], "L'aéronautique et le spatial", "On parle d'« Aerospace Valley »."),
  Q("Dans quelle ville se trouve le siège de Michelin ?", ["Clermont-Ferrand", "Lyon", "Lille", "Rennes"], "Clermont-Ferrand", "C'est un grand fabricant de pneumatiques."),
]),
notion('G3-1', 1, F, 'geo3-tourisme-productif', [
  Q("Le tourisme est-il une activité productive importante en France ?", ["Oui, il représente environ 8 % du PIB", "Non, il est négligeable", "Il est interdit", "Seulement à Paris"], "Oui, il représente environ 8 % du PIB", "La France est le pays le plus visité au monde."),
  Q("Quel espace productif touristique attire en été sur la côte méditerranéenne ?", ["La Côte d'Azur", "La Beauce", "Le Morvan", "La Lorraine"], "La Côte d'Azur", "Nice, Cannes, Saint-Tropez…"),
  Q("Quelle région française attire de nombreux skieurs l'hiver ?", ["Auvergne-Rhône-Alpes", "Bretagne", "Normandie", "Hauts-de-France"], "Auvergne-Rhône-Alpes", "Les Alpes du Nord ont les plus grandes stations."),
]),
notion('G3-1', 2, F, 'geo3-montagnes-france', [
  Q("Quel est le plus haut sommet de France ?", ["Le mont Blanc", "Le puy de Dôme", "Le Vignemale", "Le Ventoux"], "Le mont Blanc", "Il culmine à environ 4 805 m."),
  Q("Quel massif sépare la France de l'Espagne ?", ["Les Pyrénées", "Les Alpes", "Les Vosges", "Le Jura"], "Les Pyrénées", "Le Vignemale est le plus haut sommet pyrénéen français."),
  Q("Quel massif ancien se trouve au centre de la France ?", ["Le Massif central", "Les Alpes", "Les Pyrénées", "Le Jura"], "Le Massif central", "Il compte de nombreux volcans éteints."),
]),
notion('G3-1', 2, F, 'geo3-campagnes-services', [
  Q("Quel service ferme parfois dans les petits villages ?", ["L'école, la poste ou le commerce", "L'aéroport international", "La bourse", "Le métro"], "L'école, la poste ou le commerce", "C'est un défi pour les espaces de faible densité."),
  Q("Qu'est-ce qu'une maison France Services ?", ["Un guichet unique qui aide les habitants dans leurs démarches administratives", "Un musée", "Un centre commercial", "Une maison de retraite"], "Un guichet unique qui aide les habitants dans leurs démarches administratives", "Il en existe plus de 2 800."),
  Q("Quel commerce ambulant passe encore dans certains villages ?", ["Le boulanger ou l'épicier en camionnette", "Le grand magasin", "L'hypermarché", "La banque"], "Le boulanger ou l'épicier en camionnette", "Il maintient un lien social."),
]),
notion('G3-1', 2, F, 'geo3-parcs-naturels', [
  Q("Quel parc national protège les falaises et les criques près de Marseille ?", ["Le parc national des Calanques", "Le parc de la Vanoise", "Le parc des Cévennes", "Le parc des Écrins"], "Le parc national des Calanques", "Il est créé en 2012."),
  Q("Qu'est-ce qu'un parc naturel régional ?", ["Un territoire rural qui associe protection du patrimoine et développement local", "Un zoo", "Un jardin public en ville", "Une réserve de chasse"], "Un territoire rural qui associe protection du patrimoine et développement local", "La France en compte 59."),
  Q("Quel parc national se trouve dans le Massif central ?", ["Le parc national des Cévennes", "Le parc de la Vanoise", "Le parc des Pyrénées", "Le parc de Port-Cros"], "Le parc national des Cévennes", "Il est habité à l'année."),
]),
notion('G3-1', 0, F, 'geo3-metropoles-regionales', [
  Q("Quelle métropole régionale est la capitale de la région Auvergne-Rhône-Alpes ?", ["Lyon", "Grenoble", "Clermont-Ferrand", "Saint-Étienne"], "Lyon", "C'est la deuxième agglomération de France."),
  Q("Quelle ville est la capitale de la région Hauts-de-France ?", ["Lille", "Amiens", "Calais", "Arras"], "Lille", "Elle est proche de la Belgique."),
  Q("Quelle ville est la capitale de la région Grand Est ?", ["Strasbourg", "Nancy", "Metz", "Reims"], "Strasbourg", "Elle accueille le Parlement européen."),
]),
notion('G3-1', 1, F, 'geo3-commerce-france', [
  Q("Quel est le premier partenaire commercial de la France ?", ["L'Allemagne", "La Chine", "Le Brésil", "Le Japon"], "L'Allemagne", "Les échanges sont surtout européens."),
  Q("Quels produits la France exporte-t-elle beaucoup ?", ["Avions, produits de luxe, vins, médicaments", "Pétrole brut", "Riz et thé", "Charbon"], "Avions, produits de luxe, vins, médicaments", "Elle importe beaucoup d'énergie et de biens manufacturés."),
  Q("Quel groupe français est le premier groupe de luxe du monde ?", ["LVMH", "Renault", "Carrefour", "SNCF"], "LVMH", "Il possède Louis Vuitton, Dior, Moët…"),
]),
# ══ Intermédiaire ══
notion('G3-1', 0, I, 'geo3i-aires-attraction', [
  Q("Quelle est la population de l'aire d'attraction de Paris ?", ["Environ 13 millions d'habitants", "Environ 2 millions", "Environ 30 millions", "Environ 500 000"], "Environ 13 millions d'habitants", "C'est la première aire d'Europe de l'Ouest avec Londres."),
  Q("Combien d'aires d'attraction des villes dépassent 700 000 habitants en France ?", ["Une quinzaine", "Deux", "Cent", "Aucune"], "Une quinzaine", "Ce sont les principales métropoles."),
  Q("Quelle est la différence entre la commune de Paris et l'aire d'attraction de Paris ?", ["La commune compte environ 2 millions d'habitants, l'aire environ 13 millions", "Elles ont la même population", "La commune est plus grande", "L'aire ne compte que les touristes"], "La commune compte environ 2 millions d'habitants, l'aire environ 13 millions", "Il faut préciser l'échelle utilisée."),
]),
notion('G3-1', 0, I, 'geo3i-metropoles-dynamiques', [
  Q("Quelles métropoles françaises connaissent une forte croissance démographique ?", ["Toulouse, Bordeaux, Montpellier, Nantes, Rennes", "Saint-Étienne et Le Havre", "Mulhouse et Roubaix", "Aucune"], "Toulouse, Bordeaux, Montpellier, Nantes, Rennes", "Elles attirent par leur dynamisme et leur cadre de vie."),
  Q("Pourquoi les métropoles de l'Ouest et du Sud attirent-elles ?", ["Emplois qualifiés, universités, climat et littoral", "Elles ont des mines de charbon", "Elles sont moins chères que tout le reste", "Elles ont des stations de ski"], "Emplois qualifiés, universités, climat et littoral", "On parle d'héliotropisme pour l'attrait du soleil."),
  Q("Comment appelle-t-on l'attrait des populations pour les régions ensoleillées ?", ["L'héliotropisme", "La littoralisation", "La périurbanisation", "La métropolisation"], "L'héliotropisme", "Il explique la croissance du Sud."),
]),
notion('G3-1', 0, I, 'geo3i-villes-moyennes', [
  Q("Comment appelle-t-on les villes de 20 000 à 100 000 habitants environ ?", ["Les villes moyennes", "Les métropoles", "Les mégapoles", "Les villages"], "Les villes moyennes", "Elles maillent le territoire."),
  Q("Quel problème rencontrent de nombreuses villes moyennes ?", ["La dévitalisation de leur centre-ville", "La surpopulation", "Trop de gratte-ciel", "Trop d'aéroports"], "La dévitalisation de leur centre-ville", "Commerces vacants, logements vides…"),
  Q("Pourquoi la crise sanitaire de 2020 a-t-elle redonné de l'attrait aux villes moyennes ?", ["Le télétravail et la recherche d'un cadre de vie plus calme", "Elles ont construit des aéroports", "Les métropoles ont fermé", "Elles sont devenues gratuites"], "Le télétravail et la recherche d'un cadre de vie plus calme", "Le mouvement reste toutefois modéré."),
]),
notion('G3-1', 0, I, 'geo3i-transports-metropoles', [
  Q("Quelle ville française a inauguré le premier tramway moderne en 1985 ?", ["Nantes", "Paris", "Lyon", "Bordeaux"], "Nantes", "De nombreuses villes ont suivi."),
  Q("Quel métro automatique sans conducteur a été inauguré à Lille en 1983 ?", ["Le VAL", "Le RER", "Le TGV", "Le Thalys"], "Le VAL", "C'était une première mondiale."),
  Q("Pourquoi certaines villes rendent-elles les transports en commun gratuits ?", ["Pour réduire l'usage de la voiture et aider les ménages", "Pour gagner de l'argent", "Pour supprimer les bus", "Par obligation légale"], "Pour réduire l'usage de la voiture et aider les ménages", "Dunkerque et Montpellier l'ont fait."),
]),
notion('G3-1', 1, I, 'geo3i-agroalimentaire', [
  Q("Quelle région française est la première région agricole et agroalimentaire pour l'élevage ?", ["La Bretagne", "L'Île-de-France", "La Corse", "Le Grand Est"], "La Bretagne", "Porcs, volailles, lait…"),
  Q("Quel problème environnemental l'élevage intensif provoque-t-il en Bretagne ?", ["La prolifération d'algues vertes", "La désertification", "Les avalanches", "Les séismes"], "La prolifération d'algues vertes", "Elle est liée aux nitrates."),
  Q("Comment appelle-t-on l'industrie qui transforme les produits agricoles en aliments ?", ["L'industrie agroalimentaire", "La sidérurgie", "La pétrochimie", "L'aéronautique"], "L'industrie agroalimentaire", "C'est le premier secteur industriel français par l'emploi."),
]),
notion('G3-1', 1, I, 'geo3i-technopoles', [
  Q("Quelle technopole de la Côte d'Azur est la plus ancienne de France ?", ["Sophia Antipolis", "La Défense", "Euralille", "Part-Dieu"], "Sophia Antipolis", "Elle est créée en 1969 près d'Antibes."),
  Q("Quel plateau au sud de Paris concentre universités, grandes écoles et laboratoires ?", ["Le plateau de Saclay", "Le plateau de Langres", "Le plateau de Millevaches", "Le plateau du Larzac"], "Le plateau de Saclay", "On le compare à une « Silicon Valley » française."),
  Q("Quelle ville des Alpes est un grand pôle de recherche en microélectronique ?", ["Grenoble", "Annecy", "Chambéry", "Gap"], "Grenoble", "Elle accueille le CEA et STMicroelectronics."),
]),
notion('G3-1', 1, I, 'geo3i-desindustrialisation', [
  Q("Quelles régions françaises ont été les plus touchées par la désindustrialisation ?", ["Le Nord et la Lorraine", "La Côte d'Azur", "L'Île-de-France", "La Corse"], "Le Nord et la Lorraine", "Mines, textile et sidérurgie y ont fermé."),
  Q("Comment appelle-t-on le transfert d'usines vers des pays où la main-d'œuvre est moins chère ?", ["La délocalisation", "La relocalisation", "La métropolisation", "La décentralisation"], "La délocalisation", "Elle a touché l'automobile et le textile."),
  Q("Quel bassin minier du Nord est inscrit au patrimoine mondial de l'Unesco depuis 2012 ?", ["Le bassin minier du Nord-Pas-de-Calais", "Le bassin de Lacq", "Le bassin parisien", "Le bassin d'Arcachon"], "Le bassin minier du Nord-Pas-de-Calais", "Terrils, corons et chevalements en témoignent."),
]),
notion('G3-1', 1, I, 'geo3i-reindustrialisation', [
  Q("Comment appelle-t-on les usines de batteries électriques qui s'installent dans les Hauts-de-France ?", ["Des « gigafactories »", "Des manufactures royales", "Des comptoirs", "Des hauts fourneaux"], "Des « gigafactories »", "On parle de « vallée de la batterie »."),
  Q("Quel plan d'investissement de 2021 vise à réindustrialiser la France ?", ["France 2030", "Le plan Marshall", "Le plan Freycinet", "La PAC"], "France 2030", "Il finance l'hydrogène, le nucléaire, les batteries…"),
  Q("Pourquoi la France veut-elle relocaliser certaines productions ?", ["Pour réduire sa dépendance, notamment pour les médicaments et les composants", "Pour augmenter les importations", "Pour fermer ses usines", "Pour réduire l'emploi"], "Pour réduire sa dépendance, notamment pour les médicaments et les composants", "La crise sanitaire a révélé ces dépendances."),
]),
notion('G3-1', 1, I, 'geo3i-ports-logistique', [
  Q("Comment appelle-t-on les grands entrepôts qui stockent et distribuent les marchandises ?", ["Des plateformes logistiques", "Des technopoles", "Des CBD", "Des usines sidérurgiques"], "Des plateformes logistiques", "Elles s'installent près des autoroutes."),
  Q("Quel axe logistique majeur relie le nord et le sud de la France ?", ["L'axe Seine-Rhône (Lille-Paris-Lyon-Marseille)", "L'axe Brest-Nantes", "L'axe Bordeaux-Toulouse", "L'axe Strasbourg-Mulhouse"], "L'axe Seine-Rhône (Lille-Paris-Lyon-Marseille)", "C'est l'axe le plus important du pays."),
  Q("Quel port du Nord accueille de grandes industries sidérurgiques et énergétiques ?", ["Dunkerque", "Calais", "Boulogne-sur-Mer", "Saint-Malo"], "Dunkerque", "C'est le troisième port français."),
]),
notion('G3-1', 1, I, 'geo3i-agriculture-espace', [
  Q("Quelle région agricole au sud-ouest de Paris est le « grenier à blé » de la France ?", ["La Beauce", "La Camargue", "Les Landes", "Le Morvan"], "La Beauce", "Ses grandes plaines sont très mécanisées."),
  Q("Quelle région du sud de la France est connue pour la riziculture ?", ["La Camargue", "La Beauce", "La Brie", "L'Alsace"], "La Camargue", "Dans le delta du Rhône."),
  Q("Quelle région française est un grand bassin de production de fruits et légumes ?", ["La vallée du Rhône et la Provence", "La Lorraine", "Le Nord", "Le Limousin"], "La vallée du Rhône et la Provence", "Grâce au climat et à l'irrigation."),
]),
notion('G3-1', 2, I, 'geo3i-faible-densite-definition', [
  Q("En dessous de quelle densité parle-t-on généralement d'espace de faible densité ?", ["Moins de 30 habitants par km²", "Moins de 1 000 hab./km²", "Moins de 500 hab./km²", "Plus de 100 hab./km²"], "Moins de 30 habitants par km²", "La moyenne française est d'environ 120 hab./km²."),
  Q("Quelle part du territoire français est composée d'espaces de faible densité ?", ["Environ 40 %", "Environ 5 %", "Environ 90 %", "Environ 10 %"], "Environ 40 %", "Ils n'abritent pourtant qu'environ 5 % de la population."),
  Q("Quel département est le moins peuplé de France ?", ["La Lozère", "Paris", "Le Nord", "Les Bouches-du-Rhône"], "La Lozère", "Environ 77 000 habitants."),
]),
notion('G3-1', 2, I, 'geo3i-montagne-economie', [
  Q("Quelle loi de 1985 protège et aide au développement des espaces de montagne ?", ["La loi Montagne", "La loi Littoral", "La loi SRU", "La loi Ferry"], "La loi Montagne", "Elle a été actualisée en 2016."),
  Q("Quelle activité de montagne se développe pour diversifier les stations au-delà du ski ?", ["Le tourisme quatre saisons", "L'industrie lourde", "La pêche", "La riziculture"], "Le tourisme quatre saisons", "Randonnée, VTT, thermalisme…"),
  Q("Quelle production agricole de qualité est typique des montagnes françaises ?", ["Les fromages (beaufort, comté, reblochon)", "Le riz", "Le coton", "La canne à sucre"], "Les fromages (beaufort, comté, reblochon)", "L'élevage laitier valorise les alpages."),
]),
notion('G3-1', 2, I, 'geo3i-rural-attractif', [
  Q("Quelles campagnes françaises attirent de nouveaux habitants ?", ["Celles proches des villes, du littoral ou bien reliées", "Celles sans route ni internet", "Aucune", "Uniquement les montagnes isolées"], "Celles proches des villes, du littoral ou bien reliées", "Les campagnes les plus isolées continuent souvent de perdre des habitants."),
  Q("Quel groupe de population s'installe souvent dans les campagnes du Sud-Ouest ou de Bretagne ?", ["Des retraités et des actifs en télétravail", "Uniquement des étudiants", "Des mineurs", "Des marins-pêcheurs"], "Des retraités et des actifs en télétravail", "Certains sont étrangers, notamment britanniques."),
  Q("Qu'est-ce qu'une résidence secondaire ?", ["Un logement utilisé pour les vacances ou les week-ends", "Un logement social", "Un hôtel", "Une maison de retraite"], "Un logement utilisé pour les vacances ou les week-ends", "Elles sont nombreuses sur les littoraux et en montagne."),
]),
notion('G3-1', 2, I, 'geo3i-energies-rurales', [
  Q("Quelles installations se multiplient dans les campagnes françaises pour produire de l'énergie ?", ["Éoliennes, panneaux solaires et méthaniseurs", "Centrales à charbon", "Raffineries de pétrole", "Plateformes pétrolières"], "Éoliennes, panneaux solaires et méthaniseurs", "Elles apportent des revenus aux communes."),
  Q("Qu'est-ce qu'un méthaniseur ?", ["Une installation qui produit du biogaz à partir de déchets agricoles", "Une éolienne", "Un panneau solaire", "Un barrage"], "Une installation qui produit du biogaz à partir de déchets agricoles", "Fumier, lisier, résidus de culture…"),
  Q("Pourquoi les éoliennes suscitent-elles parfois des oppositions locales ?", ["Elles modifient les paysages et peuvent gêner les riverains", "Elles polluent l'air", "Elles produisent des déchets radioactifs", "Elles consomment du pétrole"], "Elles modifient les paysages et peuvent gêner les riverains", "Les débats sont vifs dans certaines campagnes."),
]),
# ══ Avancé ══
notion('G3-1', 0, D, 'geo3d-grille-densite', [
  Q("Quelle grille l'Insee utilise-t-il depuis 2020 pour définir le rural ?", ["La grille communale de densité", "Le découpage en cantons", "La carte des départements", "Le cadastre"], "La grille communale de densité", "Selon elle, environ un tiers des Français vit dans une commune rurale."),
  Q("Selon cette nouvelle définition, quelle part des communes françaises est rurale ?", ["Environ 88 %", "Environ 20 %", "Environ 50 %", "Environ 5 %"], "Environ 88 %", "Le rural n'est donc pas marginal."),
  Q("Pourquoi cette nouvelle définition a-t-elle changé la vision du rural ?", ["Elle montre qu'un Français sur trois vit dans le rural, et non environ 5 %", "Elle a supprimé le rural", "Elle compte les touristes", "Elle ne change rien"], "Elle montre qu'un Français sur trois vit dans le rural, et non environ 5 %", "L'ancien zonage rattachait beaucoup de communes rurales aux villes."),
]),
notion('G3-1', 0, D, 'geo3d-artificialisation', [
  Q("Combien d'hectares environ sont artificialisés chaque année en France ?", ["Environ 20 000 à 25 000 hectares", "Environ 100 hectares", "Environ 1 million d'hectares", "Aucun"], "Environ 20 000 à 25 000 hectares", "Soit l'équivalent de plusieurs terrains de football par heure."),
  Q("Quelle est la principale cause de l'artificialisation des sols en France ?", ["La construction de logements", "L'agriculture biologique", "Le reboisement", "Le tourisme spatial"], "La construction de logements", "Surtout de maisons individuelles."),
  Q("Quel objectif intermédiaire fixe la loi Climat et résilience pour 2031 ?", ["Diviser par deux le rythme d'artificialisation par rapport à 2011-2021", "Doubler l'artificialisation", "Supprimer toutes les maisons", "Aucun"], "Diviser par deux le rythme d'artificialisation par rapport à 2011-2021", "Avant d'atteindre le « zéro artificialisation nette » en 2050."),
]),
notion('G3-1', 0, D, 'geo3d-gares-tgv-metropoles', [
  Q("Quel quartier d'affaires lillois s'est développé autour de la gare TGV depuis 1994 ?", ["Euralille", "La Défense", "Part-Dieu", "Euroméditerranée"], "Euralille", "Lille est au carrefour Paris-Londres-Bruxelles."),
  Q("Quelle grande opération d'aménagement transforme les quartiers du port de Marseille ?", ["Euroméditerranée", "Euralille", "Confluence", "La Défense"], "Euroméditerranée", "C'est l'une des plus grandes opérations de rénovation urbaine d'Europe."),
  Q("Quel quartier de Lyon a été reconverti entre Rhône et Saône sur d'anciens terrains industriels ?", ["Confluence", "Croix-Rousse", "Vieux-Lyon", "Fourvière"], "Confluence", "C'est un écoquartier."),
]),
notion('G3-1', 0, D, 'geo3d-mobilites-residentielles', [
  Q("Vers quelles régions les Français migrent-ils le plus à l'intérieur du pays ?", ["L'Ouest et le Sud (façade atlantique et méditerranéenne)", "Le Nord-Est", "Le Massif central uniquement", "L'Île-de-France uniquement"], "L'Ouest et le Sud (façade atlantique et méditerranéenne)", "L'Île-de-France a un solde migratoire interne négatif."),
  Q("Pourquoi l'Île-de-France gagne-t-elle quand même des habitants ?", ["Grâce à un fort excédent des naissances sur les décès", "Grâce aux migrations internes", "Grâce aux retraités", "Elle perd des habitants"], "Grâce à un fort excédent des naissances sur les décès", "Sa population est jeune."),
  Q("Quelle région perd des habitants en raison de son déclin industriel et démographique ?", ["Une partie du Grand Est et du Nord-Est", "L'Occitanie", "La Nouvelle-Aquitaine", "Les Pays de la Loire"], "Une partie du Grand Est et du Nord-Est", "La « diagonale » et le Nord-Est sont en difficulté."),
]),
notion('G3-1', 1, D, 'geo3d-poles-competitivite', [
  Q("Quel pôle de compétitivité regroupe les acteurs de l'aéronautique et du spatial en Occitanie et Nouvelle-Aquitaine ?", ["Aerospace Valley", "Cosmetic Valley", "Lyonbiopôle", "Mer Méditerranée"], "Aerospace Valley", "C'est l'un des plus grands pôles français."),
  Q("Quel pôle de compétitivité est spécialisé dans la parfumerie et la cosmétique, autour de Chartres ?", ["Cosmetic Valley", "Aerospace Valley", "Minalogic", "Systematic"], "Cosmetic Valley", "Il réunit des centaines d'entreprises."),
  Q("Pourquoi les entreprises ont-elles intérêt à se regrouper dans un même territoire ?", ["Pour partager savoirs, main-d'œuvre qualifiée et projets de recherche", "Pour payer plus d'impôts", "Pour réduire la concurrence à zéro", "Par obligation légale"], "Pour partager savoirs, main-d'œuvre qualifiée et projets de recherche", "On parle de clusters."),
]),
notion('G3-1', 1, D, 'geo3d-economie-residentielle', [
  Q("Qu'appelle-t-on l'économie présentielle ?", ["Les activités qui répondent aux besoins des personnes présentes (habitants, touristes)", "L'industrie exportatrice", "L'agriculture d'exportation", "La finance internationale"], "Les activités qui répondent aux besoins des personnes présentes (habitants, touristes)", "Commerces, santé, services à la personne…"),
  Q("Quels territoires vivent beaucoup de l'économie présentielle ?", ["Les littoraux touristiques et les régions de retraités", "Les zones industrialo-portuaires", "Les technopoles", "Les bassins miniers actifs"], "Les littoraux touristiques et les régions de retraités", "Les revenus viennent souvent d'ailleurs (pensions, tourisme)."),
  Q("Quel géographe a mis en évidence l'importance de cette économie dans La Circulation invisible ?", ["Laurent Davezies", "Christophe Guilluy", "Jean Gottmann", "Paul Vidal de La Blache"], "Laurent Davezies", "Il montre les transferts de revenus entre territoires."),
]),
notion('G3-1', 1, D, 'geo3d-ports-fluviaux', [
  Q("Quel est le premier port fluvial de France ?", ["Le port de Paris (Gennevilliers)", "Le port de Strasbourg", "Le port de Lyon", "Le port de Toulouse"], "Le port de Paris (Gennevilliers)", "Il fait partie d'HAROPA."),
  Q("Quel grand projet doit relier la Seine au réseau fluvial du nord de l'Europe ?", ["Le canal Seine-Nord Europe", "Le canal du Midi", "Le canal de Suez", "Le canal de Bourgogne"], "Le canal Seine-Nord Europe", "Sa mise en service est prévue au début des années 2030."),
  Q("Quel avantage présente le transport fluvial ?", ["Il émet peu de CO2 par tonne transportée", "Il est le plus rapide", "Il dessert tous les villages", "Il ne nécessite aucune infrastructure"], "Il émet peu de CO2 par tonne transportée", "Une péniche remplace des dizaines de camions."),
]),
notion('G3-1', 1, D, 'geo3d-zones-franches-zi', [
  Q("Pourquoi la vallée de l'Arve, en Haute-Savoie, est-elle connue industriellement ?", ["Pour le décolletage (pièces de précision)", "Pour le textile", "Pour le pétrole", "Pour la sidérurgie lourde"], "Pour le décolletage (pièces de précision)", "C'est un système productif local spécialisé."),
  Q("Comment appelle-t-on un regroupement d'entreprises d'une même spécialité dans un territoire, comme l'horlogerie dans le Jura ?", ["Un système productif local", "Une ZEE", "Un front pionnier", "Une aire urbaine"], "Un système productif local", "Ces districts industriels reposent sur des savoir-faire anciens."),
  Q("Quelle ville du Pays basque est un pôle de l'industrie de la glisse (surf) ?", ["Hossegor et la côte basco-landaise", "Lille", "Metz", "Limoges"], "Hossegor et la côte basco-landaise", "De grandes marques de surf y sont implantées."),
]),
notion('G3-1', 1, D, 'geo3d-agriculture-mutations', [
  Q("Combien d'exploitations agricoles compte environ la France aujourd'hui ?", ["Environ 390 000", "Environ 4 millions", "Environ 39 000", "Environ 1,5 million"], "Environ 390 000", "Il y en avait plus de 1,5 million en 1970."),
  Q("Quel défi démographique touche l'agriculture française ?", ["Le vieillissement des agriculteurs et le renouvellement des générations", "Trop de jeunes agriculteurs", "Trop d'exploitations", "La hausse rapide du nombre d'agriculteurs"], "Le vieillissement des agriculteurs et le renouvellement des générations", "Une grande partie partira à la retraite d'ici 2030."),
  Q("Comment évolue la taille moyenne des exploitations agricoles françaises ?", ["Elle augmente", "Elle diminue", "Elle reste stable", "Elle est divisée par dix"], "Elle augmente", "Elle dépasse 70 hectares."),
]),
notion('G3-1', 2, D, 'geo3d-diagonale', [
  Q("Comment appelle-t-on la bande de faibles densités qui va de la Meuse aux Landes ?", ["La « diagonale du vide » (ou des faibles densités)", "La Banane bleue", "L'arc atlantique", "Le croissant fertile"], "La « diagonale du vide » (ou des faibles densités)", "Les géographes préfèrent parler de faibles densités."),
  Q("Pourquoi l'expression « diagonale du vide » est-elle critiquée ?", ["Ces espaces ne sont pas vides : ils sont habités et ont des atouts", "Elle est trop longue", "Elle n'existe pas sur les cartes", "Elle désigne une autoroute"], "Ces espaces ne sont pas vides : ils sont habités et ont des atouts", "Elle donne une image négative."),
  Q("Quel territoire du Limousin est souvent cité pour son dynamisme dans l'accueil de nouveaux habitants ?", ["Les communes du plateau de Millevaches", "Paris", "Lyon", "Nice"], "Les communes du plateau de Millevaches", "Des projets collectifs y attirent de nouveaux arrivants."),
]),
notion('G3-1', 2, D, 'geo3d-revitalisation-rurale', [
  Q("Quel programme de l'État soutient depuis 2020 les petites communes qui jouent un rôle de centralité ?", ["Petites villes de demain", "Action cœur de ville", "Le Grand Paris", "France Travail"], "Petites villes de demain", "Il concerne environ 1 600 communes."),
  Q("Quel dispositif fiscal aide les entreprises qui s'installent dans les zones rurales fragiles ?", ["Les zones France ruralités revitalisation (FRR)", "Les zones franches urbaines", "Les zones de libre-échange", "La ZEE"], "Les zones France ruralités revitalisation (FRR)", "Elles remplacent les ZRR depuis 2024."),
  Q("Pourquoi la fibre optique est-elle un enjeu pour les campagnes ?", ["Elle permet le télétravail et l'installation d'entreprises", "Elle remplace les routes", "Elle produit de l'électricité", "Elle est inutile"], "Elle permet le télétravail et l'installation d'entreprises", "Le plan France Très Haut Débit la déploie."),
]),
notion('G3-1', 2, D, 'geo3d-deserts-medicaux', [
  Q("Quelle part environ de la population française vit dans un désert médical ?", ["Environ un tiers", "Environ 1 %", "Environ 90 %", "Personne"], "Environ un tiers", "Selon les définitions retenues."),
  Q("Quelle solution se développe pour améliorer l'accès aux soins dans les campagnes ?", ["Les maisons de santé pluriprofessionnelles et la télémédecine", "La fermeture des hôpitaux", "La suppression des pharmacies", "L'interdiction des médecins"], "Les maisons de santé pluriprofessionnelles et la télémédecine", "Elles regroupent plusieurs professionnels."),
  Q("Quel indicateur mesure l'accès aux médecins généralistes ?", ["L'accessibilité potentielle localisée (APL)", "Le PIB", "Le taux de natalité", "La densité routière"], "L'accessibilité potentielle localisée (APL)", "Elle tient compte de la distance et de l'offre."),
]),
notion('G3-1', 0, D, 'geo3d-gentrification-periurbain', [
  Q("Comment appelle-t-on l'extension des villes au-delà des banlieues, en mitant les campagnes ?", ["La périurbanisation", "La gentrification", "La littoralisation", "La métropolisation"], "La périurbanisation", "Elle s'accélère en France à partir des années 1970."),
  Q("Quel phénomène touche les centres anciens de Bordeaux ou Nantes, devenus très recherchés ?", ["La gentrification et la hausse des prix immobiliers", "Le dépeuplement massif", "La désindustrialisation récente", "L'installation de bidonvilles"], "La gentrification et la hausse des prix immobiliers", "Les ménages modestes partent vers la périphérie."),
  Q("Comment appelle-t-on l'espace intermédiaire, ni vraiment urbain ni vraiment rural, autour des villes ?", ["Le périurbain (ou espace rurbain)", "Le CBD", "Le centre historique", "La ZEE"], "Le périurbain (ou espace rurbain)", "On parle aussi de « tiers espace »."),
]),
notion('G3-1', 2, D, 'geo3d-fractures-territoriales', [
  Q("Quel mouvement social de 2018-2019 a mis en lumière les difficultés des périphéries et des campagnes ?", ["Les Gilets jaunes", "Mai 68", "Nuit debout", "Le Front populaire"], "Les Gilets jaunes", "Il est parti de la hausse des taxes sur le carburant."),
  Q("Quel géographe a popularisé l'expression « France périphérique » ?", ["Christophe Guilluy", "Jean Gottmann", "Roger Brunet", "Paul Vidal de La Blache"], "Christophe Guilluy", "Sa thèse est discutée par d'autres géographes."),
  Q("Pourquoi la dépendance à la voiture est-elle un facteur de vulnérabilité dans le périurbain et le rural ?", ["Les ménages sont très exposés à la hausse du prix du carburant", "La voiture est gratuite", "Il n'y a pas de routes", "Les distances sont très courtes"], "Les ménages sont très exposés à la hausse du prix du carburant", "On parle de précarité énergétique liée aux transports."),
]),
]

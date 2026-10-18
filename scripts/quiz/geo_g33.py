# Géographie 3e · La France et l'Union européenne : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G3-3', 0, F, 'geo3-pays-ue', [
  Q("Lequel de ces pays fait partie de l'Union européenne ?", ["L'Espagne", "La Suisse", "La Norvège", "Le Royaume-Uni"], "L'Espagne", "Elle a rejoint la CEE en 1986."),
  Q("Lequel de ces pays n'est PAS membre de l'Union européenne ?", ["La Suisse", "La Belgique", "L'Italie", "La Pologne"], "La Suisse", "Elle a des accords bilatéraux avec l'UE."),
  Q("Quelle est la capitale de la Belgique, où siègent de nombreuses institutions européennes ?", ["Bruxelles", "Anvers", "Liège", "Bruges"], "Bruxelles", "On la surnomme la « capitale de l'Europe »."),
]),
notion('G3-3', 0, F, 'geo3-euro-pays', [
  Q("Quelle est la monnaie commune de la majorité des pays de l'Union européenne ?", ["L'euro", "Le dollar", "La livre", "Le franc suisse"], "L'euro", "Elle circule depuis 2002."),
  Q("Combien de pays utilisent l'euro en 2026 ?", ["21", "27", "12", "5"], "21", "La Bulgarie l'a adopté le 1er janvier 2026."),
  Q("Quel pays de l'UE n'a pas adopté l'euro ?", ["La Pologne", "La France", "L'Allemagne", "L'Italie"], "La Pologne", "Elle garde le zloty, comme la Suède sa couronne."),
]),
notion('G3-3', 0, F, 'geo3-voisins-france', [
  Q("Combien de pays ont une frontière terrestre avec la France métropolitaine ?", ["8", "3", "12", "5"], "8", "Belgique, Luxembourg, Allemagne, Suisse, Italie, Monaco, Andorre, Espagne."),
  Q("Quel pays voisin de la France est à l'est, au-delà du Rhin ?", ["L'Allemagne", "L'Espagne", "L'Italie", "La Belgique"], "L'Allemagne", "Le Rhin forme une partie de la frontière."),
  Q("Avec quel pays la France partage-t-elle une frontière en Amérique du Sud ?", ["Le Brésil", "L'Argentine", "Le Chili", "Le Pérou"], "Le Brésil", "Grâce à la Guyane ; c'est la plus longue frontière terrestre de la France."),
]),
notion('G3-3', 0, F, 'geo3-erasmus-jeunes', [
  Q("Que permet le programme Erasmus+ ?", ["D'étudier ou de se former dans un autre pays européen", "De voter dans un autre pays", "De voyager gratuitement en avion", "D'obtenir la nationalité d'un autre pays"], "D'étudier ou de se former dans un autre pays européen", "Il est aussi ouvert aux apprentis et aux enseignants."),
  Q("Quel dispositif offre à des jeunes de 18 ans des pass pour voyager en train en Europe ?", ["DiscoverEU", "Erasmus Mundus", "Interrail Senior", "Schengen Junior"], "DiscoverEU", "Des milliers de pass sont tirés au sort."),
  Q("Quelle carte permet d'être soigné dans un autre pays de l'UE ?", ["La carte européenne d'assurance maladie", "La carte bleue", "La carte d'électeur", "La carte grise"], "La carte européenne d'assurance maladie", "Elle est gratuite."),
]),
notion('G3-3', 0, F, 'geo3-libre-circulation', [
  Q("Que permet la libre circulation dans l'Union européenne ?", ["Vivre, travailler et étudier dans un autre pays de l'UE", "Ne plus payer d'impôts", "Voter à toutes les élections nationales", "Rouler sans permis"], "Vivre, travailler et étudier dans un autre pays de l'UE", "C'est un droit des citoyens européens."),
  Q("Qu'est-ce que l'itinérance téléphonique sans frais dans l'UE (roaming) ?", ["Pouvoir téléphoner dans les pays de l'UE au même prix qu'en France", "Un appel gratuit vers le monde entier", "Un nouveau téléphone", "Un réseau social"], "Pouvoir téléphoner dans les pays de l'UE au même prix qu'en France", "Les frais de roaming ont été supprimés en 2017."),
  Q("Quel pays non membre de l'UE fait partie de l'espace Schengen ?", ["La Suisse", "Le Royaume-Uni", "L'Irlande", "La Turquie"], "La Suisse", "Avec la Norvège, l'Islande et le Liechtenstein."),
]),
notion('G3-3', 0, F, 'geo3-europe-carte', [
  Q("Quel est le plus grand pays de l'Union européenne par la superficie ?", ["La France", "L'Allemagne", "L'Espagne", "La Pologne"], "La France", "Outre-mer compris, elle est loin devant."),
  Q("Quel est le plus petit pays de l'Union européenne ?", ["Malte", "Le Luxembourg", "Chypre", "La Belgique"], "Malte", "Il compte environ 550 000 habitants."),
  Q("Quel pays de l'UE est une île de la Méditerranée orientale ?", ["Chypre", "Malte", "L'Irlande", "La Sicile"], "Chypre", "La Sicile est une région italienne, pas un pays."),
]),
notion('G3-3', 0, F, 'geo3-ue-population', [
  Q("Combien d'habitants compte environ l'Union européenne ?", ["Environ 450 millions", "Environ 45 millions", "Environ 1 milliard", "Environ 150 millions"], "Environ 450 millions", "C'est le troisième ensemble le plus peuplé après la Chine et l'Inde."),
  Q("Quel est le deuxième pays le plus peuplé de l'Union européenne ?", ["La France", "L'Italie", "L'Espagne", "La Pologne"], "La France", "Après l'Allemagne."),
  Q("Quelle est la plus grande ville de l'Union européenne ?", ["Paris (agglomération)", "Rome", "Madrid", "Vienne"], "Paris (agglomération)", "Berlin est la commune la plus peuplée."),
]),
notion('G3-3', 0, F, 'geo3-symboles-ue-carte', [
  Q("Quelle ville est le siège de la Banque centrale européenne ?", ["Francfort", "Paris", "Bruxelles", "Rome"], "Francfort", "Elle gère l'euro."),
  Q("Dans quelle ville siège la Cour de justice de l'Union européenne ?", ["Luxembourg", "Strasbourg", "La Haye", "Genève"], "Luxembourg", "Elle veille à l'application du droit européen."),
  Q("Quel jour fête-t-on l'Europe ?", ["Le 9 mai", "Le 14 juillet", "Le 1er janvier", "Le 11 novembre"], "Le 9 mai", "En souvenir de la déclaration Schuman de 1950."),
]),
notion('G3-3', 1, F, 'geo3-france-monde-langue', [
  Q("Sur combien de continents le français est-il parlé ?", ["Sur les cinq continents", "Uniquement en Europe", "Seulement en Afrique", "Seulement en Amérique"], "Sur les cinq continents", "Le français est langue officielle dans environ 30 pays."),
  Q("Quel est le pays où vivent le plus de francophones après la France ?", ["La république démocratique du Congo", "Le Canada", "La Belgique", "La Suisse"], "La république démocratique du Congo", "Kinshasa est la plus grande ville francophone."),
  Q("Quelle province canadienne a le français pour seule langue officielle ?", ["Le Québec", "L'Ontario", "La Colombie-Britannique", "L'Alberta"], "Le Québec", "Le Nouveau-Brunswick est bilingue."),
]),
notion('G3-3', 1, F, 'geo3-france-culture-monde', [
  Q("Quel festival de cinéma français est l'un des plus célèbres du monde ?", ["Le Festival de Cannes", "Le festival d'Avignon", "Les Vieilles Charrues", "Le festival de Cornouaille"], "Le Festival de Cannes", "Il décerne la Palme d'or."),
  Q("Quel événement sportif mondial la France a-t-elle accueilli à Paris en 2024 ?", ["Les Jeux olympiques et paralympiques", "La Coupe du monde de football", "Le Super Bowl", "Les Jeux du Commonwealth"], "Les Jeux olympiques et paralympiques", "Paris les avait déjà accueillis en 1900 et 1924."),
  Q("Quelle course cycliste française est suivie dans le monde entier ?", ["Le Tour de France", "Paris-Brest", "Le Giro", "La Vuelta"], "Le Tour de France", "Créé en 1903."),
]),
notion('G3-3', 1, F, 'geo3-france-economie-monde', [
  Q("Dans quel secteur la France est-elle l'un des leaders mondiaux ?", ["Le luxe et l'aéronautique", "Le pétrole", "Les jeux vidéo exclusivement", "Le charbon"], "Le luxe et l'aéronautique", "Airbus et LVMH en sont des exemples."),
  Q("Quel avionneur européen a son assemblage principal à Toulouse ?", ["Airbus", "Boeing", "Embraer", "Bombardier"], "Airbus", "C'est l'un des deux géants mondiaux avec Boeing."),
  Q("Quel produit agricole français est exporté dans le monde entier ?", ["Le vin et les spiritueux", "Le riz", "Le café", "Le cacao"], "Le vin et les spiritueux", "Champagne et cognac sont des produits phares."),
]),
notion('G3-3', 1, F, 'geo3-france-diplomatie', [
  Q("Quel groupe réunit les sept grandes puissances économiques, dont la France ?", ["Le G7", "Les BRICS", "L'OPEP", "Le Mercosur"], "Le G7", "Avec les États-Unis, le Japon, l'Allemagne, le Royaume-Uni, l'Italie et le Canada."),
  Q("De quelle alliance militaire la France est-elle membre ?", ["L'OTAN", "Le pacte de Varsovie", "L'ASEAN", "La Ligue arabe"], "L'OTAN", "Elle en est membre fondateur depuis 1949."),
  Q("Dans quelle ville siège le ministère des Affaires étrangères, surnommé « le Quai d'Orsay » ?", ["Paris", "Lyon", "Strasbourg", "Bruxelles"], "Paris", "Le nom vient de son adresse."),
]),
notion('G3-3', 1, F, 'geo3-france-armee-monde', [
  Q("Dans quel pays d'Afrique la France a-t-elle une base militaire au débouché de la mer Rouge ?", ["Djibouti", "Le Maroc", "L'Égypte", "Le Kenya"], "Djibouti", "C'est la principale base française à l'étranger."),
  Q("Quel porte-avions est le navire amiral de la Marine nationale ?", ["Le Charles-de-Gaulle", "Le Clemenceau", "Le Foch", "Le Richelieu"], "Le Charles-de-Gaulle", "C'est un porte-avions à propulsion nucléaire."),
  Q("Pourquoi la France est-elle présente militairement dans tous les océans ?", ["Grâce à ses territoires d'outre-mer et ses bases", "Parce qu'elle est une île", "Parce que l'ONU l'oblige", "Elle n'y est pas présente"], "Grâce à ses territoires d'outre-mer et ses bases", "Elle protège aussi sa ZEE."),
]),
notion('G3-3', 1, F, 'geo3-ue-commerce-monde', [
  Q("L'Union européenne est-elle une grande puissance commerciale ?", ["Oui, l'une des premières du monde", "Non, elle commerce très peu", "Seulement avec l'Afrique", "Elle n'exporte rien"], "Oui, l'une des premières du monde", "Avec la Chine et les États-Unis."),
  Q("Quel pays de l'UE est le premier exportateur européen ?", ["L'Allemagne", "Malte", "Chypre", "La Lettonie"], "L'Allemagne", "Grâce à ses machines et ses voitures."),
  Q("Quel port de l'UE est le premier d'Europe ?", ["Rotterdam", "Marseille", "Gênes", "Le Pirée"], "Rotterdam", "Il est situé aux Pays-Bas."),
]),
# ══ Intermédiaire ══
notion('G3-3', 0, I, 'geo3i-candidats-ue', [
  Q("Quel pays a obtenu le statut de candidat à l'UE en 2022, en pleine guerre ?", ["L'Ukraine", "La Russie", "La Norvège", "La Suisse"], "L'Ukraine", "La Moldavie aussi."),
  Q("Quel pays candidat depuis 1999 voit ses négociations d'adhésion bloquées ?", ["La Turquie", "La Croatie", "La Slovénie", "Malte"], "La Turquie", "Les négociations sont gelées depuis 2018."),
  Q("Quels critères un pays doit-il remplir pour entrer dans l'UE ?", ["Démocratie, État de droit, économie de marché et reprise du droit européen", "Être riche et peuplé", "Avoir l'euro", "Être une île"], "Démocratie, État de droit, économie de marché et reprise du droit européen", "Ce sont les critères de Copenhague (1993)."),
]),
notion('G3-3', 0, I, 'geo3i-inegalites-ue', [
  Q("Quelles régions de l'UE sont les plus riches ?", ["Les grandes métropoles et la dorsale européenne", "Les régions rurales de l'Est", "Le sud de l'Italie", "Les régions ultrapériphériques"], "Les grandes métropoles et la dorsale européenne", "Luxembourg, Dublin, Paris, Munich…"),
  Q("Quel pays de l'UE a le PIB par habitant le plus faible ?", ["La Bulgarie", "Le Luxembourg", "L'Irlande", "Le Danemark"], "La Bulgarie", "Avec la Roumanie et la Grèce."),
  Q("Comment appelle-t-on la politique européenne qui réduit les écarts entre régions ?", ["La politique de cohésion", "La PAC", "La politique monétaire", "La politique étrangère"], "La politique de cohésion", "Elle est financée par les fonds structurels."),
]),
notion('G3-3', 0, I, 'geo3i-transfrontalier-france', [
  Q("Quelle région transfrontalière réunit Strasbourg et la région allemande de Kehl ?", ["L'Eurodistrict Strasbourg-Ortenau", "La Banane bleue", "Le Grand Paris", "L'arc alpin"], "L'Eurodistrict Strasbourg-Ortenau", "Un tramway relie Strasbourg à Kehl depuis 2017."),
  Q("Quel aéroport est franco-suisse, avec une partie sur chaque territoire ?", ["L'EuroAirport Bâle-Mulhouse-Fribourg", "Roissy", "Nice", "Lyon-Saint-Exupéry"], "L'EuroAirport Bâle-Mulhouse-Fribourg", "Il est situé en France mais géré avec la Suisse."),
  Q("Quel grand bassin d'emploi transfrontalier attire de nombreux Français de l'Ain et de Haute-Savoie ?", ["Le Grand Genève", "Le Grand Lyon", "Le Grand Nancy", "Le Grand Paris"], "Le Grand Genève", "Le Léman Express relie les deux côtés."),
]),
notion('G3-3', 0, I, 'geo3i-corridors', [
  Q("Quel réseau européen de transport relie les grands corridors de l'UE ?", ["Le RTE-T (réseau transeuropéen de transport)", "Le RER", "Le TER", "Le Transsibérien"], "Le RTE-T (réseau transeuropéen de transport)", "Il comprend des autoroutes, voies ferrées et voies navigables."),
  Q("Quel tunnel ferroviaire, le plus long du monde, traverse les Alpes suisses ?", ["Le tunnel de base du Saint-Gothard", "Le tunnel sous la Manche", "Le tunnel du Mont-Blanc", "Le tunnel du Fréjus"], "Le tunnel de base du Saint-Gothard", "57 km, ouvert en 2016."),
  Q("Quel fleuve est un grand axe de transport fluvial en Europe ?", ["Le Rhin", "La Loire", "Le Tage", "La Garonne"], "Le Rhin", "Il relie la Suisse à Rotterdam."),
]),
notion('G3-3', 0, I, 'geo3i-agriculture-europe', [
  Q("Quel pays de l'UE est le premier exportateur mondial de produits agricoles après les États-Unis ?", ["Les Pays-Bas", "Malte", "Le Luxembourg", "Chypre"], "Les Pays-Bas", "Grâce à leurs serres et à leur port."),
  Q("Quelle région d'Espagne est surnommée la « mer de plastique » pour ses serres ?", ["Almería", "Madrid", "La Galice", "Le Pays basque"], "Almería", "Elle fournit fruits et légumes à toute l'Europe."),
  Q("Quel pays européen est le premier producteur de vin du monde ?", ["L'Italie (ou la France selon les années)", "L'Allemagne", "La Suède", "La Pologne"], "L'Italie (ou la France selon les années)", "Les deux pays se disputent la première place."),
]),
notion('G3-3', 0, I, 'geo3i-industrie-europe', [
  Q("Quel pays de l'UE est le premier producteur d'automobiles ?", ["L'Allemagne", "La Grèce", "Le Portugal", "L'Irlande"], "L'Allemagne", "Volkswagen, BMW, Mercedes…"),
  Q("Pourquoi des constructeurs automobiles ont-ils installé des usines en Europe centrale ?", ["Pour une main-d'œuvre qualifiée moins chère et proche des marchés", "Parce que c'est obligatoire", "Pour le climat", "Pour éviter l'euro"], "Pour une main-d'œuvre qualifiée moins chère et proche des marchés", "La Slovaquie produit le plus de voitures par habitant au monde."),
  Q("Quel projet européen développe un système de navigation par satellite indépendant du GPS ?", ["Galileo", "Erasmus", "Copernicus seul", "Schengen"], "Galileo", "Il est opérationnel depuis 2016."),
]),
notion('G3-3', 0, I, 'geo3i-fonds-europeens-france', [
  Q("Quel fonds européen aide les personnes à se former et à trouver un emploi ?", ["Le Fonds social européen (FSE+)", "Le FMI", "La BCE", "Le fonds Barnier"], "Le Fonds social européen (FSE+)", "Il finance des formations."),
  Q("Quel plan européen de 2020, financé par un emprunt commun, a aidé les pays après la crise du Covid ?", ["NextGenerationEU", "Le plan Marshall", "Le plan Juncker de 2014", "Le pacte de stabilité"], "NextGenerationEU", "Il représente plus de 700 milliards d'euros."),
  Q("La France reçoit-elle plus d'argent de l'UE qu'elle n'en verse ?", ["Non, elle est contributrice nette", "Oui, beaucoup plus", "Elle ne verse rien", "Elle ne reçoit rien"], "Non, elle est contributrice nette", "Elle reçoit cependant beaucoup au titre de la PAC."),
]),
notion('G3-3', 1, I, 'geo3i-ue-monde', [
  Q("Quelle organisation regroupe l'UE et ses partenaires commerciaux dans les négociations mondiales ?", ["L'OMC", "L'OTAN", "L'OPEP", "L'Unesco"], "L'OMC", "L'UE y négocie d'une seule voix."),
  Q("Quel est le premier partenaire commercial de l'Union européenne ?", ["Les États-Unis", "La Suisse", "Le Brésil", "L'Australie"], "Les États-Unis", "La Chine suit de près."),
  Q("Quelle est la première source d'aide au développement dans le monde ?", ["L'Union européenne et ses États membres", "Les États-Unis seuls", "La Chine seule", "L'Inde"], "L'Union européenne et ses États membres", "Environ 40 % de l'aide mondiale."),
]),
notion('G3-3', 1, I, 'geo3i-soft-power-france', [
  Q("Comment appelle-t-on la capacité d'un pays à influencer par sa culture et ses valeurs ?", ["Le soft power", "Le hard power", "Le protectionnisme", "La dissuasion"], "Le soft power", "Le hard power repose sur la force militaire et économique."),
  Q("Quelle chaîne d'information française internationale diffuse en plusieurs langues ?", ["France 24", "TF1", "M6", "Canal+"], "France 24", "Elle est diffusée dans le monde entier."),
  Q("Quel réseau d'établissements scolaires français scolarise des élèves dans le monde ?", ["Le réseau de l'AEFE (lycées français)", "Le réseau Erasmus", "Le réseau des CROUS", "Le réseau des CAF"], "Le réseau de l'AEFE (lycées français)", "Environ 600 établissements dans 140 pays."),
]),
notion('G3-3', 1, I, 'geo3i-france-attractivite', [
  Q("La France est-elle attractive pour les investissements étrangers ?", ["Oui, elle est l'un des premiers pays européens pour les projets d'investissement", "Non, aucun investisseur ne vient", "Seulement pour le tourisme", "Elle interdit les investissements étrangers"], "Oui, elle est l'un des premiers pays européens pour les projets d'investissement", "Selon le baromètre EY, elle est en tête depuis plusieurs années."),
  Q("Quel sommet annuel est organisé à Versailles pour attirer les investisseurs étrangers ?", ["Choose France", "Vivatech", "Le Salon de l'agriculture", "Le Mondial de l'auto"], "Choose France", "Il est lancé en 2018."),
  Q("Quelle place la France occupe-t-elle environ parmi les économies mondiales ?", ["Septième", "Première", "Vingtième", "Cinquantième"], "Septième", "Elle oscille entre la sixième et la septième place."),
]),
notion('G3-3', 1, I, 'geo3i-espace-europe', [
  Q("Quelle agence européenne développe les fusées Ariane ?", ["L'Agence spatiale européenne (ESA)", "La NASA", "L'OTAN", "La BCE"], "L'Agence spatiale européenne (ESA)", "Ariane 6 a réalisé son premier vol en 2024."),
  Q("D'où sont lancées les fusées Ariane ?", ["De Kourou, en Guyane", "De Toulouse", "De Paris", "De Bruxelles"], "De Kourou, en Guyane", "La proximité de l'équateur facilite les lancements."),
  Q("Quel programme européen observe la Terre par satellite pour l'environnement ?", ["Copernicus", "Galileo", "Erasmus", "Horizon"], "Copernicus", "Il suit le climat, les océans, les catastrophes."),
]),
notion('G3-3', 1, I, 'geo3i-ue-defense', [
  Q("Pourquoi l'Union européenne renforce-t-elle sa défense depuis 2022 ?", ["À cause de la guerre en Ukraine et des incertitudes sur l'allié américain", "Pour envahir d'autres pays", "Parce que l'OTAN a disparu", "Pour remplacer les armées nationales"], "À cause de la guerre en Ukraine et des incertitudes sur l'allié américain", "On parle d'« autonomie stratégique »."),
  Q("Quelle est la seule puissance nucléaire de l'Union européenne depuis le Brexit ?", ["La France", "L'Allemagne", "L'Italie", "La Pologne"], "La France", "Le Royaume-Uni est sorti de l'UE en 2020."),
  Q("Quel pays a rejoint l'OTAN en 2024 en abandonnant sa neutralité ?", ["La Suède", "La Suisse", "L'Autriche", "L'Irlande"], "La Suède", "La Finlande l'avait rejoint en 2023."),
]),
notion('G3-3', 0, I, 'geo3i-dorsale', [
  Q("Quel est l'autre nom de la « dorsale européenne », la région la plus riche d'Europe ?", ["La Banane bleue", "La Sun Belt", "La diagonale du vide", "Le croissant fertile"], "La Banane bleue", "L'expression vient du géographe Roger Brunet (1989)."),
  Q("Quelles régions françaises sont proches de la dorsale européenne ?", ["L'Alsace et le Nord", "La Bretagne et l'Aquitaine", "La Corse et la Provence", "Le Limousin et l'Auvergne"], "L'Alsace et le Nord", "Paris en est proche sans en faire strictement partie."),
  Q("Comment appelle-t-on les régions de l'UE éloignées des centres et moins dynamiques ?", ["Les périphéries (ou marges)", "Les centres", "Les métropoles", "Les hubs"], "Les périphéries (ou marges)", "Le modèle centre-périphérie s'applique à l'UE."),
]),
notion('G3-3', 0, I, 'geo3i-langues-ue', [
  Q("Combien de langues officielles compte l'Union européenne ?", ["24", "1", "3", "100"], "24", "Les textes officiels sont traduits dans toutes ces langues."),
  Q("Quelle est la devise de l'Union européenne qui reflète sa diversité ?", ["« Unie dans la diversité »", "« Un pour tous, tous pour un »", "« Liberté, égalité, fraternité »", "« E pluribus unum »"], "« Unie dans la diversité »", "Elle est adoptée en 2000."),
  Q("Quelle langue est la plus parlée comme langue maternelle dans l'UE ?", ["L'allemand", "Le français", "L'anglais", "L'espagnol"], "L'allemand", "L'anglais reste la langue étrangère la plus apprise."),
]),
# ══ Avancé ══
notion('G3-3', 0, D, 'geo3d-elargissements-geo', [
  Q("Quelle conséquence géographique ont eu les élargissements de 2004 et 2007 ?", ["Le centre de gravité de l'UE s'est déplacé vers l'est", "L'UE s'est réduite", "La France est devenue périphérique au sud", "L'UE a quitté l'Europe"], "Le centre de gravité de l'UE s'est déplacé vers l'est", "Douze pays sont entrés, dont dix d'Europe centrale et orientale."),
  Q("Quels pays des Balkans occidentaux sont candidats à l'adhésion ?", ["La Serbie, le Monténégro, l'Albanie, la Macédoine du Nord", "La Norvège et l'Islande", "La Suisse et le Liechtenstein", "Le Maroc et la Tunisie"], "La Serbie, le Monténégro, l'Albanie, la Macédoine du Nord", "Le Monténégro est le plus avancé."),
  Q("Quel pays a refusé deux fois par référendum d'adhérer à l'Union européenne ?", ["La Norvège", "La Suède", "La Finlande", "L'Autriche"], "La Norvège", "En 1972 et en 1994."),
]),
notion('G3-3', 0, D, 'geo3d-frontieres-ue', [
  Q("Quelle agence de l'UE contrôle les frontières extérieures de l'espace Schengen ?", ["Frontex", "Europol", "Eurojust", "Eurostat"], "Frontex", "Son siège est à Varsovie."),
  Q("Quelle est la plus longue frontière extérieure terrestre de l'UE ?", ["La frontière avec la Russie (Finlande, pays baltes)", "La frontière avec la Suisse", "La frontière avec Andorre", "La frontière avec Monaco"], "La frontière avec la Russie (Finlande, pays baltes)", "La Finlande l'a fermée en 2023."),
  Q("Quels pays de l'UE ont rejoint pleinement l'espace Schengen en 2025 ?", ["La Roumanie et la Bulgarie", "L'Irlande et Chypre", "La Pologne et la Hongrie", "La France et l'Allemagne"], "La Roumanie et la Bulgarie", "Les contrôles aux frontières terrestres ont été levés le 1er janvier 2025."),
]),
notion('G3-3', 0, D, 'geo3d-regions-transfrontalieres', [
  Q("Comment appelle-t-on les structures de coopération entre régions frontalières de plusieurs pays ?", ["Les eurorégions (ou GECT)", "Les ZEE", "Les métropoles", "Les DROM"], "Les eurorégions (ou GECT)", "Groupement européen de coopération territoriale."),
  Q("Quelle région transfrontalière réunit la Lorraine, la Sarre, le Luxembourg et la Wallonie ?", ["La Grande Région", "La Banane bleue", "L'Euregio Meuse-Rhin", "Le Benelux"], "La Grande Région", "Elle compte plus de 250 000 travailleurs frontaliers."),
  Q("Quel traité de 2019 renforce la coopération franco-allemande, notamment transfrontalière ?", ["Le traité d'Aix-la-Chapelle", "Le traité de l'Élysée", "Le traité de Versailles", "Le traité de Rome"], "Le traité d'Aix-la-Chapelle", "Il complète le traité de l'Élysée de 1963."),
]),
notion('G3-3', 0, D, 'geo3d-desequilibres-demographiques-ue', [
  Q("Quel problème démographique touche une grande partie de l'Union européenne ?", ["Le vieillissement et une faible fécondité", "Une fécondité très élevée", "Une population très jeune", "Une explosion démographique"], "Le vieillissement et une faible fécondité", "La fécondité moyenne est d'environ 1,4 enfant par femme."),
  Q("Quelles régions de l'UE perdent le plus d'habitants ?", ["Les régions rurales d'Europe de l'Est et du Sud", "Les grandes métropoles", "L'Île-de-France", "La Bavière"], "Les régions rurales d'Europe de l'Est et du Sud", "Par l'émigration et le vieillissement."),
  Q("Comment appelle-t-on l'Espagne intérieure qui se dépeuple ?", ["La « España vaciada » (Espagne vidée)", "La Costa del Sol", "La Catalogne", "La Meseta urbaine"], "La « España vaciada » (Espagne vidée)", "C'est l'équivalent de la diagonale des faibles densités."),
]),
notion('G3-3', 0, D, 'geo3d-marche-unique', [
  N("En quelle année le marché unique européen entre-t-il en vigueur ?", 1993, "Le 1er janvier 1993."),
  Q("Quelles sont les « quatre libertés » du marché unique ?", ["Libre circulation des marchandises, des services, des capitaux et des personnes", "Liberté d'expression, de culte, de presse et d'association", "Libre choix de la monnaie, de la langue, du drapeau et de l'hymne", "Liberté de vote, de grève, de manifester et de pétitionner"], "Libre circulation des marchandises, des services, des capitaux et des personnes", "Elles fondent l'intégration économique."),
  Q("Quel acte de 1986 a préparé le marché unique ?", ["L'Acte unique européen", "Le traité de Lisbonne", "Le traité de Nice", "Le traité d'Amsterdam"], "L'Acte unique européen", "Sous l'impulsion de Jacques Delors."),
]),
notion('G3-3', 0, D, 'geo3d-strasbourg-europe', [
  Q("Pourquoi Strasbourg a-t-elle été choisie comme capitale européenne ?", ["Elle symbolise la réconciliation franco-allemande", "Elle est la plus grande ville d'Europe", "Elle est au centre géographique exact de l'UE", "Elle a la plus grande gare"], "Elle symbolise la réconciliation franco-allemande", "La ville a changé plusieurs fois de pays."),
  Q("Quelle organisation, distincte de l'UE, a son siège à Strasbourg et compte 46 États membres ?", ["Le Conseil de l'Europe", "Le Conseil européen", "La Commission européenne", "L'OTAN"], "Le Conseil de l'Europe", "Il veille aux droits de l'homme ; la CEDH en dépend."),
  Q("Quelle différence y a-t-il entre le Conseil européen et le Conseil de l'Europe ?", ["Le Conseil européen réunit les chefs d'État de l'UE ; le Conseil de l'Europe est une autre organisation", "Ce sont deux noms de la même institution", "Le Conseil de l'Europe dirige l'euro", "Le Conseil européen siège à Strasbourg"], "Le Conseil européen réunit les chefs d'État de l'UE ; le Conseil de l'Europe est une autre organisation", "Une confusion fréquente."),
]),
notion('G3-3', 1, D, 'geo3d-puissance-normative', [
  Q("Pourquoi dit-on que l'UE est une « puissance normative » ?", ["Ses normes (RGPD, environnement, sécurité) s'imposent aux entreprises du monde entier", "Elle a la plus grande armée", "Elle n'a aucune règle", "Elle impose sa langue"], "Ses normes (RGPD, environnement, sécurité) s'imposent aux entreprises du monde entier", "On parle d'« effet Bruxelles »."),
  Q("Quelle règle européenne impose un chargeur USB-C commun pour les téléphones depuis 2024 ?", ["La directive sur le chargeur universel", "Le RGPD", "La PAC", "Le traité de Lisbonne"], "La directive sur le chargeur universel", "Apple a dû adapter ses iPhone."),
  Q("Quelle amende maximale l'UE peut-elle infliger aux plateformes qui ne respectent pas le DSA ?", ["6 % de leur chiffre d'affaires mondial", "1 euro", "100 euros", "Aucune"], "6 % de leur chiffre d'affaires mondial", "Le DSA encadre les grandes plateformes numériques."),
]),
notion('G3-3', 1, D, 'geo3d-francophonie-geo', [
  Q("Où vivront la majorité des francophones vers 2050 ?", ["En Afrique", "En Europe", "En Amérique du Nord", "En Asie"], "En Afrique", "Grâce à la croissance démographique africaine."),
  Q("Combien d'États et gouvernements sont membres de l'OIF (membres et observateurs) ?", ["Environ 90", "Environ 9", "Environ 200", "Environ 30"], "Environ 90", "Tous ne sont pas francophones de langue."),
  Q("Quel sommet de la Francophonie s'est tenu en France en 2024 ?", ["Le sommet de Villers-Cotterêts et Paris", "Le sommet de Lyon", "Le sommet de Marseille", "Le sommet de Lille"], "Le sommet de Villers-Cotterêts et Paris", "Villers-Cotterêts accueille la Cité internationale de la langue française."),
]),
notion('G3-3', 1, D, 'geo3d-france-indopacifique', [
  Q("Pourquoi la France se présente-t-elle comme une puissance de l'Indo-Pacifique ?", ["Elle y possède des territoires (Réunion, Mayotte, Nouvelle-Calédonie, Polynésie) et l'essentiel de sa ZEE", "Elle y a sa capitale", "Elle n'y a aucun territoire", "Elle y produit son pétrole"], "Elle y possède des territoires (Réunion, Mayotte, Nouvelle-Calédonie, Polynésie) et l'essentiel de sa ZEE", "Plus de 90 % de sa ZEE s'y trouve."),
  Q("Quel accord de sous-marins avec l'Australie a été rompu en 2021 au profit des États-Unis et du Royaume-Uni ?", ["Le contrat des sous-marins français (crise AUKUS)", "L'accord de Paris", "Le traité de l'Élysée", "L'accord Mercosur"], "Le contrat des sous-marins français (crise AUKUS)", "Ce fut une grave crise diplomatique."),
  Q("Quelle part de la population française d'outre-mer vit dans l'Indo-Pacifique ?", ["Environ 1,7 million de personnes", "Environ 1 000 personnes", "Environ 20 millions", "Personne"], "Environ 1,7 million de personnes", "La Réunion en est le territoire le plus peuplé."),
]),
notion('G3-3', 1, D, 'geo3d-france-puissance-moyenne', [
  Q("Comment qualifie-t-on souvent la France dans la hiérarchie des puissances ?", ["Une puissance moyenne à influence mondiale", "Une superpuissance", "Un pays sans influence", "Une hyperpuissance"], "Une puissance moyenne à influence mondiale", "L'expression est attribuée à Valéry Giscard d'Estaing."),
  Q("Quels sont les atouts de la France pour peser dans le monde ?", ["Siège permanent à l'ONU, arme nucléaire, réseau diplomatique, outre-mer", "La plus grande population du monde", "La première économie mondiale", "Le plus grand territoire terrestre"], "Siège permanent à l'ONU, arme nucléaire, réseau diplomatique, outre-mer", "Son réseau diplomatique est l'un des trois premiers du monde."),
  Q("Quelle limite pèse sur la puissance française ?", ["Un poids économique et démographique moyen face aux géants", "L'absence d'armée", "L'absence de diplomatie", "Son isolement total"], "Un poids économique et démographique moyen face aux géants", "D'où l'importance de l'échelle européenne."),
]),
notion('G3-3', 1, D, 'geo3d-ue-dependances', [
  Q("Pour quelles ressources l'UE est-elle très dépendante de l'extérieur ?", ["L'énergie et les matières premières critiques", "Le blé", "Le vin", "Le lait"], "L'énergie et les matières premières critiques", "Elle importe plus de la moitié de son énergie."),
  Q("Quel règlement européen de 2024 vise à sécuriser l'approvisionnement en matières premières critiques ?", ["Le Critical Raw Materials Act", "Le RGPD", "Le DSA", "Le traité de Rome"], "Le Critical Raw Materials Act", "Il fixe des objectifs d'extraction et de recyclage en Europe."),
  Q("Quel pays fournissait l'essentiel du gaz importé par l'UE avant 2022 ?", ["La Russie", "La Norvège seule", "Le Japon", "Le Brésil"], "La Russie", "Environ 40 % du gaz importé."),
]),
notion('G3-3', 1, D, 'geo3d-mercosur-accords', [
  Q("Quel accord commercial l'UE a-t-elle conclu en 2024 avec le Brésil, l'Argentine, l'Uruguay et le Paraguay ?", ["L'accord UE-Mercosur", "L'ALENA", "Le CETA", "L'accord de Schengen"], "L'accord UE-Mercosur", "La France y est opposée en l'état."),
  Q("Quel accord commercial lie l'UE et le Canada depuis 2017 (application provisoire) ?", ["Le CETA", "Le TAFTA", "L'ALENA", "L'accord de Cotonou"], "Le CETA", "Il n'a pas été ratifié par la France."),
  Q("Qui négocie les accords commerciaux au nom des États membres de l'UE ?", ["La Commission européenne", "Chaque État séparément", "Le Parlement français", "La BCE"], "La Commission européenne", "Le commerce est une compétence exclusive de l'UE."),
]),
notion('G3-3', 0, D, 'geo3d-pacte-vert-territoires', [
  Q("Quel objectif l'UE s'est-elle fixé pour 2040 en matière de climat ?", ["Réduire ses émissions de 90 % par rapport à 1990", "Doubler ses émissions", "Supprimer toute énergie", "Aucun objectif"], "Réduire ses émissions de 90 % par rapport à 1990", "Objectif proposé en 2024 et adopté en 2025."),
  Q("Quel fonds européen aide les régions dépendantes du charbon à se reconvertir ?", ["Le Fonds pour une transition juste", "Le FMI", "La PAC", "Le fonds Barnier"], "Le Fonds pour une transition juste", "La Silésie polonaise en est une grande bénéficiaire."),
  Q("Quel réseau européen protège des espaces naturels remarquables ?", ["Natura 2000", "Erasmus", "Galileo", "Schengen"], "Natura 2000", "C'est le plus grand réseau d'aires protégées au monde."),
]),
]

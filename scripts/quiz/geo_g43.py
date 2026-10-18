# Géographie 4e · Des espaces transformés par la mondialisation : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G4-3', 0, F, 'geo4-oceans', [
  Q("Quel est le plus grand océan du monde ?", ["L'océan Pacifique", "L'océan Atlantique", "L'océan Indien", "L'océan Arctique"], "L'océan Pacifique", "Il couvre environ un tiers de la planète."),
  Q("Quelle part de la surface de la Terre est couverte par les océans ?", ["Environ 70 %", "Environ 30 %", "Environ 50 %", "Environ 90 %"], "Environ 70 %", "On parle de « planète bleue »."),
  Q("Quel océan sépare l'Europe de l'Amérique ?", ["L'océan Atlantique", "L'océan Pacifique", "L'océan Indien", "L'océan Austral"], "L'océan Atlantique", "C'est un axe majeur des échanges."),
]),
notion('G4-3', 0, F, 'geo4-porte-conteneurs', [
  Q("Comment appelle-t-on un navire qui transporte des conteneurs ?", ["Un porte-conteneurs", "Un pétrolier", "Un paquebot", "Un chalutier"], "Un porte-conteneurs", "Les plus grands transportent plus de 24 000 conteneurs."),
  Q("Comment appelle-t-on un navire qui transporte du pétrole ?", ["Un pétrolier (tanker)", "Un porte-conteneurs", "Un ferry", "Un voilier"], "Un pétrolier (tanker)", "Les marées noires sont dues à leurs naufrages."),
  Q("Pourquoi le transport maritime est-il le plus utilisé pour les marchandises ?", ["Il permet de transporter d'énormes quantités à faible coût", "Il est le plus rapide", "Il ne pollue pas du tout", "Il est gratuit"], "Il permet de transporter d'énormes quantités à faible coût", "Il est lent mais très économique."),
]),
notion('G4-3', 0, F, 'geo4-ports-francais', [
  Q("Quel est le premier port français pour l'ensemble des marchandises ?", ["Marseille-Fos", "Brest", "Bordeaux", "La Rochelle"], "Marseille-Fos", "Le Havre domine pour les conteneurs."),
  Q("Quel ensemble portuaire réunit Le Havre, Rouen et Paris le long de la Seine ?", ["HAROPA", "Euromed", "Port-Vendres", "Calais Port"], "HAROPA", "C'est l'axe Seine."),
  Q("Quel port français est le premier pour le trafic de passagers vers le Royaume-Uni ?", ["Calais", "Marseille", "Toulon", "Nice"], "Calais", "Avec le tunnel sous la Manche à proximité."),
]),
notion('G4-3', 0, F, 'geo4-detroits', [
  Q("Qu'est-ce qu'un détroit ?", ["Un passage maritime étroit entre deux terres", "Un fleuve", "Une île", "Un lac salé"], "Un passage maritime étroit entre deux terres", "Les détroits sont des points de passage stratégiques."),
  Q("Quel détroit sépare la France de l'Angleterre ?", ["Le pas de Calais", "Le détroit de Gibraltar", "Le Bosphore", "Le détroit d'Ormuz"], "Le pas de Calais", "C'est l'un des plus fréquentés du monde."),
  Q("Quel détroit relie la mer Noire à la Méditerranée en traversant Istanbul ?", ["Le Bosphore", "Le détroit de Malacca", "Le pas de Calais", "Le détroit de Béring"], "Le Bosphore", "Avec les Dardanelles."),
]),
notion('G4-3', 0, F, 'geo4-ressources-mer', [
  Q("Quelle ressource énergétique est extraite au fond des mers grâce à des plateformes ?", ["Le pétrole et le gaz", "Le charbon", "Le bois", "Le blé"], "Le pétrole et le gaz", "On parle d'exploitation offshore."),
  Q("Quelle activité fournit une grande partie des protéines consommées dans le monde ?", ["La pêche", "Le tourisme", "Le transport", "L'éolien"], "La pêche", "Avec l'aquaculture."),
  Q("Quel produit est extrait de l'eau de mer dans les marais salants ?", ["Le sel", "Le sucre", "Le pétrole", "Le fer"], "Le sel", "Comme à Guérande ou Aigues-Mortes."),
]),
notion('G4-3', 1, F, 'geo4-etats-unis-base', [
  Q("Quelle est la capitale des États-Unis ?", ["Washington", "New York", "Los Angeles", "Chicago"], "Washington", "New York est la plus grande ville."),
  Q("Combien d'États composent les États-Unis ?", ["50", "13", "100", "27"], "50", "Plus le district de Columbia."),
  Q("Combien d'habitants comptent environ les États-Unis ?", ["Environ 340 millions", "Environ 50 millions", "Environ 1 milliard", "Environ 120 millions"], "Environ 340 millions", "C'est le troisième pays le plus peuplé du monde."),
]),
notion('G4-3', 1, F, 'geo4-usa-villes', [
  Q("Quelle ville de Californie est le centre mondial du cinéma ?", ["Los Angeles (Hollywood)", "San Diego", "Sacramento", "Las Vegas"], "Los Angeles (Hollywood)", "C'est la deuxième ville des États-Unis."),
  Q("Quelle ville des Grands Lacs est la troisième des États-Unis ?", ["Chicago", "Détroit", "Cleveland", "Toronto"], "Chicago", "Elle est un grand carrefour de transports."),
  Q("Quelle ville du Texas accueille le centre spatial de la NASA ?", ["Houston", "Dallas", "Austin", "Miami"], "Houston", "C'est aussi la capitale du pétrole."),
]),
notion('G4-3', 1, F, 'geo4-usa-puissance', [
  Q("Quelle est la monnaie des États-Unis, utilisée dans le monde entier ?", ["Le dollar", "L'euro", "La livre", "Le yuan"], "Le dollar", "C'est la principale monnaie des échanges internationaux."),
  Q("Quelles grandes entreprises américaines du numérique dominent le monde ?", ["Google, Apple, Meta, Amazon, Microsoft", "Renault, Peugeot, Michelin", "Toyota, Sony, Honda", "Nestlé, Rolex, Novartis"], "Google, Apple, Meta, Amazon, Microsoft", "On les surnomme les GAFAM."),
  Q("Quel pays a la plus forte armée et les plus grosses dépenses militaires du monde ?", ["Les États-Unis", "La France", "Le Brésil", "Le Japon"], "Les États-Unis", "Ils dépensent plus que les neuf pays suivants réunis."),
]),
notion('G4-3', 1, F, 'geo4-usa-agriculture', [
  Q("Les États-Unis sont-ils une grande puissance agricole ?", ["Oui, l'un des premiers exportateurs agricoles du monde", "Non, ils importent toute leur nourriture", "Seulement pour les fruits tropicaux", "Non, ils n'ont pas d'agriculture"], "Oui, l'un des premiers exportateurs agricoles du monde", "Maïs, soja, blé, viande…"),
  Q("Quelle grande région agricole est au centre des États-Unis ?", ["Les Grandes Plaines", "Les Rocheuses", "Les Appalaches", "La Floride"], "Les Grandes Plaines", "On y cultive le blé et le maïs."),
  Q("Quel État produit la majorité des fruits et légumes des États-Unis ?", ["La Californie", "L'Alaska", "Le Maine", "Le Montana"], "La Californie", "Grâce à l'irrigation."),
]),
notion('G4-3', 2, F, 'geo4-afrique-ouest-pays', [
  Q("Quelle est la plus grande ville du Nigeria ?", ["Lagos", "Abuja", "Kano", "Accra"], "Lagos", "C'est l'une des plus grandes métropoles d'Afrique."),
  Q("Quel pays d'Afrique de l'Ouest a pour capitale Dakar ?", ["Le Sénégal", "Le Mali", "La Guinée", "Le Niger"], "Le Sénégal", "Dakar est un grand port atlantique."),
  Q("Quelle est la capitale économique de la Côte d'Ivoire ?", ["Abidjan", "Yamoussoukro", "Bouaké", "Accra"], "Abidjan", "Yamoussoukro est la capitale politique."),
]),
notion('G4-3', 2, F, 'geo4-afrique-ressources', [
  Q("Quelle ressource fait la richesse du Ghana et de la Côte d'Ivoire ?", ["Le cacao", "Le blé", "Le café arabica d'Éthiopie", "Le riz"], "Le cacao", "Ces deux pays produisent près des deux tiers du cacao mondial."),
  Q("Quel métal précieux est extrait au Mali, au Burkina Faso et au Ghana ?", ["L'or", "L'argent", "Le platine", "Le lithium"], "L'or", "L'or est la première exportation de plusieurs pays du Sahel."),
  Q("Pourquoi dit-on que de nombreuses économies africaines dépendent des matières premières ?", ["Elles exportent surtout des produits bruts non transformés", "Elles exportent surtout des voitures", "Elles n'exportent rien", "Elles importent des matières premières"], "Elles exportent surtout des produits bruts non transformés", "La valeur ajoutée est réalisée ailleurs."),
]),
notion('G4-3', 2, F, 'geo4-afrique-jeunesse', [
  Q("Quel continent a la population la plus jeune ?", ["L'Afrique", "L'Europe", "L'Asie de l'Est", "L'Amérique du Nord"], "L'Afrique", "Plus de 40 % des Africains ont moins de 15 ans."),
  Q("Combien d'habitants compte environ l'Afrique ?", ["Environ 1,5 milliard", "Environ 150 millions", "Environ 5 milliards", "Environ 500 millions"], "Environ 1,5 milliard", "Elle pourrait atteindre 2,5 milliards en 2050."),
  Q("Quel outil numérique est très répandu en Afrique, même dans les zones rurales ?", ["Le téléphone portable", "L'ordinateur de bureau", "Le minitel", "Le fax"], "Le téléphone portable", "Il sert aussi à payer et à envoyer de l'argent."),
]),
notion('G4-3', 2, F, 'geo4-afrique-milieux', [
  Q("Quel est le plus grand désert chaud du monde ?", ["Le Sahara", "Le Kalahari", "Le Gobi", "L'Atacama"], "Le Sahara", "Il couvre une grande partie de l'Afrique du Nord."),
  Q("Quel est le plus long fleuve d'Afrique ?", ["Le Nil", "Le Niger", "Le Congo", "Le Zambèze"], "Le Nil", "Il traverse notamment l'Égypte et le Soudan."),
  Q("Quel grand bassin forestier d'Afrique centrale est le deuxième poumon vert de la planète ?", ["Le bassin du Congo", "Le Sahel", "Le Maghreb", "Le Kalahari"], "Le bassin du Congo", "Après l'Amazonie."),
]),
notion('G4-3', 0, F, 'geo4-marees-noires', [
  Q("Qu'est-ce qu'une marée noire ?", ["Une nappe de pétrole répandue en mer après un accident", "Une marée très haute", "Une algue toxique", "Une vague géante"], "Une nappe de pétrole répandue en mer après un accident", "Elle souille les côtes et tue de nombreux animaux."),
  Q("Quel pétrolier a provoqué une marée noire en Bretagne en 1978 ?", ["L'Amoco Cadiz", "Le Titanic", "Le Clemenceau", "Le Charles-de-Gaulle"], "L'Amoco Cadiz", "L'Erika a aussi touché la Bretagne en 1999."),
  Q("Quels animaux sont souvent les premières victimes visibles des marées noires ?", ["Les oiseaux marins", "Les chameaux", "Les ours", "Les chevaux"], "Les oiseaux marins", "Leur plumage englué les empêche de voler."),
]),
# ══ Intermédiaire ══
notion('G4-3', 0, I, 'geo4i-maritimisation', [
  Q("Que signifie la « maritimisation » de l'économie ?", ["La part croissante des échanges et des activités qui passent par la mer", "La disparition des ports", "La montée des eaux", "La fin de la pêche"], "La part croissante des échanges et des activités qui passent par la mer", "Les littoraux concentrent les activités."),
  Q("Comment appelle-t-on la concentration d'activités industrielles et portuaires au bord de la mer ?", ["Une zone industrialo-portuaire (ZIP)", "Un CBD", "Une station de ski", "Un bidonville"], "Une zone industrialo-portuaire (ZIP)", "Comme Fos-sur-Mer ou Dunkerque."),
  Q("Quelle région du monde concentre la majorité des grands ports de conteneurs ?", ["L'Asie de l'Est", "L'Afrique", "L'Amérique du Sud", "L'Océanie"], "L'Asie de l'Est", "La Chine domine le classement."),
]),
notion('G4-3', 0, I, 'geo4i-routes-maritimes', [
  Q("Quelle route maritime relie l'Asie à l'Europe par le canal de Suez ?", ["L'axe Asie-Europe par l'océan Indien et la mer Rouge", "La route du cap Horn", "Le passage du Nord-Ouest", "La route du Pacifique Sud"], "L'axe Asie-Europe par l'océan Indien et la mer Rouge", "C'est l'un des axes les plus fréquentés."),
  Q("Pourquoi les attaques en mer Rouge depuis fin 2023 ont-elles perturbé le commerce mondial ?", ["Les navires évitent Suez et contournent l'Afrique, ce qui allonge les trajets", "Le canal de Suez a été fermé par l'Égypte", "La mer Rouge s'est asséchée", "Elles n'ont eu aucun effet"], "Les navires évitent Suez et contournent l'Afrique, ce qui allonge les trajets", "Les rebelles houthis du Yémen visent les navires."),
  Q("Quel cap au sud de l'Afrique est contourné quand Suez est évité ?", ["Le cap de Bonne-Espérance", "Le cap Horn", "Le cap Nord", "Le cap Vert"], "Le cap de Bonne-Espérance", "Cela ajoute une dizaine de jours de navigation."),
]),
notion('G4-3', 0, I, 'geo4i-canal-panama', [
  Q("Quel canal relie l'Atlantique et le Pacifique en Amérique centrale ?", ["Le canal de Panama", "Le canal de Suez", "Le canal de Corinthe", "Le canal du Midi"], "Le canal de Panama", "Il est inauguré en 1914."),
  Q("Pourquoi le trafic du canal de Panama a-t-il dû être réduit en 2023-2024 ?", ["Une sécheresse a fait baisser le niveau du lac qui l'alimente", "Une guerre", "Un séisme", "Une grève des marins"], "Une sécheresse a fait baisser le niveau du lac qui l'alimente", "Le canal fonctionne avec de l'eau douce."),
  Q("Comment appelle-t-on les points de passage obligés du commerce maritime ?", ["Des passages stratégiques (ou points de contrôle)", "Des ZEE", "Des hinterlands", "Des aires urbaines"], "Des passages stratégiques (ou points de contrôle)", "Suez, Panama, Ormuz, Malacca…"),
]),
notion('G4-3', 0, I, 'geo4i-zee-france', [
  Q("Quelle est la superficie de la ZEE française ?", ["Environ 10 millions de km²", "Environ 500 000 km²", "Environ 100 km²", "Environ 50 millions de km²"], "Environ 10 millions de km²", "Elle est la deuxième du monde."),
  Q("Grâce à quels territoires la France possède-t-elle une si grande ZEE ?", ["Ses outre-mer", "La Bretagne", "La Corse seule", "Les Alpes"], "Ses outre-mer", "Surtout la Polynésie française et la Nouvelle-Calédonie."),
  Q("Quelle convention de 1982 définit les ZEE ?", ["La convention de Montego Bay", "La convention de Genève", "Le traité de Rome", "L'accord de Paris"], "La convention de Montego Bay", "C'est la convention des Nations unies sur le droit de la mer."),
]),
notion('G4-3', 0, I, 'geo4i-piraterie', [
  Q("Dans quelle région la piraterie a-t-elle fortement menacé le trafic maritime vers 2008-2012 ?", ["Au large de la Somalie", "En mer du Nord", "En mer Baltique", "Au large de la Norvège"], "Au large de la Somalie", "Dans le golfe d'Aden."),
  Q("Quelle opération européenne lutte contre la piraterie au large de la Somalie ?", ["L'opération Atalante", "L'opération Sentinelle", "L'opération Barkhane", "L'opération Overlord"], "L'opération Atalante", "Elle est lancée en 2008."),
  Q("Quel golfe d'Afrique de l'Ouest est aussi touché par la piraterie ?", ["Le golfe de Guinée", "Le golfe de Gascogne", "Le golfe du Lion", "Le golfe Persique"], "Le golfe de Guinée", "Les navires pétroliers y sont visés."),
]),
notion('G4-3', 1, I, 'geo4i-usa-frontieres-flux', [
  Q("Quel est le premier partenaire commercial des États-Unis ?", ["Le Mexique", "La France", "Le Brésil", "L'Inde"], "Le Mexique", "Devant le Canada et la Chine."),
  Q("Quelle façade des États-Unis s'est renforcée avec la croissance du commerce avec l'Asie ?", ["La façade pacifique", "La façade atlantique uniquement", "Les Grands Lacs", "L'Alaska"], "La façade pacifique", "Los Angeles, Seattle, San Francisco…"),
  Q("Quel fleuve forme une partie de la frontière entre les États-Unis et le Mexique ?", ["Le Rio Grande", "Le Mississippi", "Le Colorado", "L'Hudson"], "Le Rio Grande", "Les Mexicains l'appellent Río Bravo."),
]),
notion('G4-3', 1, I, 'geo4i-usa-reindustrialisation', [
  Q("Quelle loi de 2022 subventionne les industries vertes aux États-Unis ?", ["L'Inflation Reduction Act (IRA)", "Le New Deal", "Le plan Marshall", "L'ALENA"], "L'Inflation Reduction Act (IRA)", "Elle a attiré des usines de batteries et de panneaux solaires."),
  Q("Pourquoi les États-Unis cherchent-ils à relocaliser la production de puces électroniques ?", ["Pour réduire leur dépendance à l'Asie, notamment à Taïwan", "Parce que les puces sont interdites", "Pour fermer leurs usines", "Pour exporter du pétrole"], "Pour réduire leur dépendance à l'Asie, notamment à Taïwan", "C'est le CHIPS Act de 2022."),
  Q("Comment appelle-t-on le retour d'usines dans leur pays d'origine ?", ["La relocalisation", "La délocalisation", "La métropolisation", "La maritimisation"], "La relocalisation", "C'est l'inverse de la délocalisation."),
]),
notion('G4-3', 1, I, 'geo4i-usa-hispaniques', [
  Q("Quel groupe forme la première minorité aux États-Unis ?", ["Les Hispaniques (Latinos)", "Les Européens du Nord", "Les Asiatiques", "Les Amérindiens"], "Les Hispaniques (Latinos)", "Ils représentent près de 20 % de la population."),
  Q("Quels États du sud-ouest ont une forte population hispanique ?", ["La Californie, le Texas, l'Arizona, le Nouveau-Mexique", "Le Maine, le Vermont", "L'Alaska, Hawaï", "Le Dakota du Nord"], "La Californie, le Texas, l'Arizona, le Nouveau-Mexique", "Ces territoires ont appartenu au Mexique."),
  Q("Quelle ville de Floride est une grande porte d'entrée des immigrés d'Amérique latine et des Caraïbes ?", ["Miami", "Orlando", "Tampa", "Jacksonville"], "Miami", "La communauté cubaine y est très présente."),
]),
notion('G4-3', 1, I, 'geo4i-usa-numerique', [
  Q("Quelle entreprise de Seattle est le leader mondial du commerce en ligne ?", ["Amazon", "Apple", "Netflix", "Tesla"], "Amazon", "Elle domine aussi le cloud avec AWS."),
  Q("Pourquoi la Silicon Valley attire-t-elle les entreprises technologiques ?", ["Universités de pointe (Stanford), capitaux et ingénieurs du monde entier", "Des terrains gratuits", "L'absence de concurrence", "Un climat froid"], "Universités de pointe (Stanford), capitaux et ingénieurs du monde entier", "C'est un technopôle de rang mondial."),
  Q("Quelle ville du Texas est devenue un nouveau pôle technologique ?", ["Austin", "El Paso", "Laredo", "Amarillo"], "Austin", "Tesla y a installé son siège."),
]),
notion('G4-3', 2, I, 'geo4i-sahel', [
  Q("Quels pays sont situés dans le Sahel ?", ["Le Mali, le Niger, le Burkina Faso, le Tchad", "Le Maroc, la Tunisie", "Le Kenya, la Tanzanie", "L'Afrique du Sud, le Botswana"], "Le Mali, le Niger, le Burkina Faso, le Tchad", "C'est une bande semi-aride au sud du Sahara."),
  Q("Quelle difficulté majeure touche le Sahel depuis les années 2010 ?", ["L'insécurité liée à des groupes armés jihadistes", "Des inondations permanentes", "Le froid extrême", "La surpopulation de villes géantes"], "L'insécurité liée à des groupes armés jihadistes", "Elle provoque d'importants déplacements de population."),
  Q("Quel projet vise à planter une bande d'arbres à travers l'Afrique, du Sénégal à Djibouti ?", ["La Grande Muraille verte", "Le canal de Suez", "La route transsaharienne", "Le barrage d'Assouan"], "La Grande Muraille verte", "Pour lutter contre la désertification."),
]),
notion('G4-3', 2, I, 'geo4i-afrique-urbanisation', [
  Q("Quelle mégapole d'Afrique centrale est la plus grande ville francophone du monde ?", ["Kinshasa", "Paris", "Abidjan", "Montréal"], "Kinshasa", "Elle dépasse 17 millions d'habitants."),
  Q("Quel est le principal défi des grandes villes africaines ?", ["Une croissance si rapide que logements, transports et services ne suivent pas", "Leur vieillissement", "Leur dépeuplement", "Le manque de jeunes"], "Une croissance si rapide que logements, transports et services ne suivent pas", "L'habitat informel y domine."),
  Q("Quel pays d'Afrique de l'Est a la capitale Nairobi ?", ["Le Kenya", "L'Éthiopie", "La Tanzanie", "L'Ouganda"], "Le Kenya", "Nairobi est un pôle régional."),
]),
notion('G4-3', 2, I, 'geo4i-afrique-chine', [
  Q("Quel projet chinois finance des infrastructures dans le monde, dont de nombreux pays africains ?", ["Les nouvelles routes de la soie", "Le plan Marshall", "La PAC", "Le New Deal"], "Les nouvelles routes de la soie", "Lancé en 2013."),
  Q("Quel chemin de fer construit par la Chine relie Addis-Abeba à Djibouti ?", ["La ligne Addis-Abeba-Djibouti", "Le Transsibérien", "L'Orient-Express", "Le Shinkansen"], "La ligne Addis-Abeba-Djibouti", "Elle désenclave l'Éthiopie."),
  Q("Pourquoi Djibouti accueille-t-il plusieurs bases militaires étrangères ?", ["Il contrôle le détroit de Bab-el-Mandeb, à l'entrée de la mer Rouge", "Il est très peuplé", "Il est au centre de l'Afrique", "Il produit beaucoup de pétrole"], "Il contrôle le détroit de Bab-el-Mandeb, à l'entrée de la mer Rouge", "France, États-Unis, Chine, Japon y sont présents."),
]),
notion('G4-3', 2, I, 'geo4i-afrique-ports', [
  Q("Quel port marocain est devenu le premier port à conteneurs d'Afrique et de Méditerranée ?", ["Tanger Med", "Casablanca", "Dakar", "Alger"], "Tanger Med", "Il est situé face au détroit de Gibraltar."),
  Q("Pourquoi de nombreux pays africains enclavés dépendent-ils des ports de leurs voisins ?", ["Ils n'ont pas d'accès à la mer", "Ils ont trop de ports", "Ils refusent le commerce", "Ils sont des îles"], "Ils n'ont pas d'accès à la mer", "Le Mali dépend de Dakar et d'Abidjan."),
  Q("Quel port d'Afrique de l'Ouest est le principal débouché du Burkina Faso et du Mali ?", ["Abidjan", "Le Cap", "Mombasa", "Alexandrie"], "Abidjan", "Avec Dakar et Lomé."),
]),
# ══ Avancé ══
notion('G4-3', 0, D, 'geo4d-arctique', [
  Q("Pourquoi les routes maritimes arctiques suscitent-elles l'intérêt ?", ["La fonte de la banquise ouvre des routes plus courtes entre l'Asie et l'Europe", "L'Arctique se refroidit", "Il n'y a aucun intérêt", "Les icebergs ont disparu partout"], "La fonte de la banquise ouvre des routes plus courtes entre l'Asie et l'Europe", "La route du Nord longe la Sibérie."),
  Q("Quel pays contrôle la route maritime du Nord, le long de la Sibérie ?", ["La Russie", "Le Canada", "La Norvège", "Les États-Unis"], "La Russie", "Le passage du Nord-Ouest longe le Canada."),
  Q("Quelle île arctique, territoire autonome du Danemark, suscite la convoitise des États-Unis ?", ["Le Groenland", "L'Islande", "Le Svalbard", "Terre-Neuve"], "Le Groenland", "Pour ses ressources et sa position stratégique."),
]),
notion('G4-3', 0, D, 'geo4d-mer-chine', [
  Q("Quelle mer fait l'objet de fortes tensions entre la Chine et ses voisins ?", ["La mer de Chine méridionale", "La mer du Nord", "La mer Baltique", "La mer des Sargasses"], "La mer de Chine méridionale", "La Chine y revendique la quasi-totalité des eaux."),
  Q("Quels archipels sont disputés en mer de Chine méridionale ?", ["Les Spratleys et les Paracels", "Les Baléares", "Les Canaries", "Les Hébrides"], "Les Spratleys et les Paracels", "La Chine y a construit des îles artificielles."),
  Q("Quel tribunal international a rejeté en 2016 les revendications chinoises, à la demande des Philippines ?", ["La Cour permanente d'arbitrage de La Haye", "La Cour pénale internationale", "La CEDH", "La Cour suprême des États-Unis"], "La Cour permanente d'arbitrage de La Haye", "La Chine refuse cette décision."),
]),
notion('G4-3', 0, D, 'geo4d-haute-mer', [
  Q("Qu'est-ce que la haute mer ?", ["L'espace maritime au-delà des ZEE, qui n'appartient à aucun État", "La mer près des côtes", "La partie profonde d'un lac", "Une mer fermée"], "L'espace maritime au-delà des ZEE, qui n'appartient à aucun État", "Elle couvre près de la moitié de la planète."),
  Q("Quel traité de l'ONU adopté en 2023 vise à protéger la biodiversité en haute mer ?", ["Le traité BBNJ (sur la haute mer)", "Le traité de Rome", "Le protocole de Kyoto", "Le traité de l'Antarctique"], "Le traité BBNJ (sur la haute mer)", "Il est entré en vigueur en 2026."),
  Q("Pourquoi l'exploitation minière des grands fonds marins inquiète-t-elle les scientifiques ?", ["Elle pourrait détruire des écosystèmes encore très mal connus", "Il n'y a rien au fond des mers", "Elle est trop peu chère", "Elle crée des îles"], "Elle pourrait détruire des écosystèmes encore très mal connus", "La France plaide pour un moratoire."),
]),
notion('G4-3', 0, D, 'geo4d-pavillons', [
  Q("Qu'est-ce qu'un pavillon de complaisance ?", ["L'immatriculation d'un navire dans un pays aux règles et impôts peu exigeants", "Un drapeau décoratif", "Un bâtiment portuaire", "Une cabine de luxe"], "L'immatriculation d'un navire dans un pays aux règles et impôts peu exigeants", "Panama, le Liberia et les îles Marshall en sont les principaux."),
  Q("Quel pays possède la plus grande flotte marchande immatriculée ?", ["Le Panama (ou le Liberia)", "La Suisse", "La Bolivie", "Le Mali"], "Le Panama (ou le Liberia)", "Les navires appartiennent pourtant souvent à des armateurs grecs, chinois ou japonais."),
  Q("Quel armateur français est l'un des trois premiers du monde pour le transport de conteneurs ?", ["CMA CGM", "Air France", "SNCF", "Renault"], "CMA CGM", "Son siège est à Marseille."),
]),
notion('G4-3', 0, D, 'geo4d-cables-sousmarins', [
  Q("Quelle part du trafic Internet intercontinental passe par les câbles sous-marins ?", ["Plus de 95 %", "Environ 10 %", "Environ 50 %", "Aucune, tout passe par satellite"], "Plus de 95 %", "Les satellites ne transportent qu'une petite part."),
  Q("Pourquoi les câbles sous-marins sont-ils considérés comme stratégiques ?", ["Leur coupure peut paralyser les communications d'un pays", "Ils produisent de l'électricité", "Ils transportent du pétrole", "Ils sont décoratifs"], "Leur coupure peut paralyser les communications d'un pays", "Des sabotages ont été signalés en mer Baltique."),
  Q("Quelles entreprises financent aujourd'hui une grande partie des nouveaux câbles ?", ["Les géants du numérique (Google, Meta, Microsoft, Amazon)", "Les compagnies aériennes", "Les constructeurs automobiles", "Les banques centrales"], "Les géants du numérique (Google, Meta, Microsoft, Amazon)", "Ils contrôlent une part croissante du réseau."),
]),
notion('G4-3', 1, D, 'geo4d-usa-territoire', [
  Q("Quel État est le plus peuplé des États-Unis ?", ["La Californie", "Le Texas", "New York", "La Floride"], "La Californie", "Environ 39 millions d'habitants."),
  Q("Vers quels États se déplace le centre de gravité démographique des États-Unis ?", ["Vers le sud et l'ouest (Sun Belt)", "Vers le nord-est", "Vers l'Alaska", "Il ne bouge pas"], "Vers le sud et l'ouest (Sun Belt)", "Le Texas et la Floride gagnent beaucoup d'habitants."),
  Q("Quelle région, ancien cœur industriel, a vu ses villes perdre des habitants ?", ["La Rust Belt (Manufacturing Belt)", "La Sun Belt", "La Silicon Valley", "La Corn Belt"], "La Rust Belt (Manufacturing Belt)", "Détroit, Cleveland, Pittsburgh…"),
]),
notion('G4-3', 1, D, 'geo4d-usa-protectionnisme', [
  Q("Quelle politique commerciale les États-Unis ont-ils fortement renforcée en 2025 ?", ["Des droits de douane élevés sur de nombreuses importations", "Le libre-échange total", "La suppression de toutes les taxes", "L'interdiction des exportations"], "Des droits de douane élevés sur de nombreuses importations", "Sous la présidence de Donald Trump."),
  Q("Comment appelle-t-on une politique qui taxe les importations pour protéger l'industrie nationale ?", ["Le protectionnisme", "Le libre-échange", "Le mercantilisme bancaire", "Le multilatéralisme"], "Le protectionnisme", "Il s'oppose au libre-échange."),
  Q("Quelle organisation internationale encadre les règles du commerce mondial ?", ["L'OMC", "L'OTAN", "L'OPEP", "L'OMS"], "L'OMC", "Organisation mondiale du commerce, créée en 1995."),
]),
notion('G4-3', 1, D, 'geo4d-usa-gateways', [
  Q("Quel complexe portuaire du Texas est le premier des États-Unis pour le tonnage, grâce au pétrole ?", ["Houston", "Boston", "Seattle", "Baltimore"], "Houston", "Il se trouve sur le golfe du Mexique."),
  Q("Quel aéroport des États-Unis est l'un des plus fréquentés du monde ?", ["Atlanta", "Denver", "Phoenix", "Salt Lake City"], "Atlanta", "Il est le hub de Delta Air Lines."),
  Q("Comment appelle-t-on les grandes portes d'entrée d'un territoire dans la mondialisation ?", ["Des interfaces (ou gateways)", "Des fronts pionniers", "Des déserts", "Des marges"], "Des interfaces (ou gateways)", "Ports et aéroports internationaux."),
]),
notion('G4-3', 1, D, 'geo4d-usa-inegalites', [
  Q("Quelle part de la population américaine vit sous le seuil de pauvreté fédéral ?", ["Environ 11 %", "Environ 1 %", "Environ 40 %", "Environ 70 %"], "Environ 11 %", "Près de 37 millions de personnes."),
  Q("Quels territoires américains sont restés à l'écart de la mondialisation ?", ["Des espaces ruraux de l'intérieur et des Appalaches", "Manhattan", "La Silicon Valley", "Los Angeles"], "Des espaces ruraux de l'intérieur et des Appalaches", "La mondialisation crée des territoires gagnants et perdants."),
  Q("Quels peuples vivent souvent dans des réserves aux États-Unis ?", ["Les Amérindiens", "Les Hispaniques", "Les Afro-Américains", "Les Asiatiques"], "Les Amérindiens", "Ils comptent parmi les plus pauvres du pays."),
]),
notion('G4-3', 2, D, 'geo4d-afrique-zlecaf', [
  Q("Combien de pays africains environ ont adhéré à la ZLECAf ?", ["Plus de 50", "Environ 5", "Environ 15", "Aucun"], "Plus de 50", "C'est la plus grande zone de libre-échange du monde par le nombre de pays."),
  Q("Quelle part du commerce des pays africains se fait entre pays africains ?", ["Environ 15 %", "Environ 70 %", "Environ 50 %", "Environ 90 %"], "Environ 15 %", "C'est beaucoup moins qu'en Europe ou en Asie."),
  Q("Quel obstacle freine le commerce entre pays africains ?", ["Le manque d'infrastructures de transport", "Le trop grand nombre de routes", "L'absence de frontières", "La monnaie unique"], "Le manque d'infrastructures de transport", "Les réseaux ont souvent été tournés vers les ports coloniaux."),
]),
notion('G4-3', 2, D, 'geo4d-nigeria', [
  Q("Quel pays a le PIB le plus élevé d'Afrique selon les années, avec l'Afrique du Sud et l'Égypte ?", ["Le Nigeria", "Le Niger", "Le Tchad", "Le Mali"], "Le Nigeria", "Son économie dépend beaucoup du pétrole."),
  Q("Quelle industrie du cinéma nigériane est l'une des plus prolifiques du monde ?", ["Nollywood", "Bollywood", "Hollywood", "Cinecittà"], "Nollywood", "Elle produit des milliers de films par an."),
  Q("Quelle région du Nigeria concentre la production de pétrole, avec de graves pollutions ?", ["Le delta du Niger", "Le Sahel", "Le plateau de Jos", "Le lac Tchad"], "Le delta du Niger", "Les fuites d'oléoducs ravagent les mangroves."),
]),
notion('G4-3', 2, D, 'geo4d-afrique-terres', [
  Q("Pourquoi des États et des entreprises étrangers achètent-ils ou louent-ils de vastes terres en Afrique ?", ["Pour produire de la nourriture ou des agrocarburants destinés à l'exportation", "Pour y construire des stations de ski", "Pour en faire des parcs nationaux", "Pour les laisser en friche"], "Pour produire de la nourriture ou des agrocarburants destinés à l'exportation", "On parle d'accaparement des terres."),
  Q("Quel pays d'Afrique de l'Est a accordé de vastes concessions agricoles à des investisseurs étrangers ?", ["L'Éthiopie", "Le Maroc", "La Tunisie", "Le Lesotho"], "L'Éthiopie", "Des populations locales ont été déplacées."),
  Q("Quelle ressource minière de la RDC est indispensable aux batteries électriques ?", ["Le cobalt", "L'or", "Le diamant", "Le sel"], "Le cobalt", "La RDC produit environ 70 % du cobalt mondial."),
]),
notion('G4-3', 2, D, 'geo4d-afrique-numerique', [
  Q("Quel service de paiement mobile, lancé au Kenya en 2007, a révolutionné les échanges ?", ["M-Pesa", "PayPal", "Lydia", "Apple Pay"], "M-Pesa", "Il permet d'envoyer de l'argent par SMS."),
  Q("Quelle ville d'Afrique de l'Ouest est un pôle de start-up, surnommée « Yabacon Valley » pour un de ses quartiers ?", ["Lagos", "Niamey", "Bamako", "Nouakchott"], "Lagos", "Le quartier de Yaba concentre les start-up."),
  Q("Comment appelle-t-on le fait de passer directement à une technologie récente sans passer par les précédentes ?", ["Le saut technologique (leapfrog)", "La désindustrialisation", "Le protectionnisme", "La périurbanisation"], "Le saut technologique (leapfrog)", "L'Afrique est passée directement au téléphone mobile."),
]),
notion('G4-3', 2, D, 'geo4d-afrique-ouest-integration', [
  Q("Quels pays ont quitté la CEDEAO en 2025 pour former l'Alliance des États du Sahel ?", ["Le Mali, le Burkina Faso et le Niger", "Le Sénégal, la Gambie et la Guinée", "Le Ghana, le Togo et le Bénin", "Le Nigeria, le Cameroun et le Tchad"], "Le Mali, le Burkina Faso et le Niger", "Ces trois pays sont dirigés par des juntes militaires."),
  Q("Quelle monnaie est partagée par huit pays d'Afrique de l'Ouest ?", ["Le franc CFA", "Le naira", "Le cedi", "Le dirham"], "Le franc CFA", "Sa réforme vers l'« eco » est en discussion."),
  Q("Pourquoi les pays d'Afrique de l'Ouest sont-ils inégalement intégrés à la mondialisation ?", ["Les littoraux et les capitales sont mieux connectés que l'intérieur sahélien", "Tous sont également intégrés", "Aucun n'est intégré", "Seuls les pays sans littoral sont intégrés"], "Les littoraux et les capitales sont mieux connectés que l'intérieur sahélien", "On observe une opposition entre littoral et intérieur."),
]),
]

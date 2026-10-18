# Géographie 4e · L'urbanisation du monde : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G4-1', 0, F, 'geo4-ville-campagne', [
  Q("Qu'est-ce qu'un citadin ?", ["Une personne qui vit en ville", "Une personne qui vit à la campagne", "Un agriculteur", "Un touriste"], "Une personne qui vit en ville", "On dit aussi un urbain."),
  Q("Comment appelle-t-on un espace où dominent les champs, les forêts et les villages ?", ["Un espace rural", "Un espace urbain", "Une métropole", "Un CBD"], "Un espace rural", "Il s'oppose à l'espace urbain."),
  Q("Quelle part des Français vit en ville ?", ["Environ 80 %", "Environ 20 %", "Environ 50 %", "100 %"], "Environ 80 %", "La France est un pays très urbanisé."),
]),
notion('G4-1', 0, F, 'geo4-plan-ville', [
  Q("Quel document représente une ville vue du dessus avec ses rues ?", ["Un plan", "Un diagramme climatique", "Une pyramide des âges", "Un graphique"], "Un plan", "On y repère les quartiers et les axes."),
  Q("Comment appelle-t-on les grandes voies qui contournent une ville ?", ["Une rocade ou un périphérique", "Une ruelle", "Un chemin de terre", "Un sentier"], "Une rocade ou un périphérique", "Le boulevard périphérique entoure Paris."),
  Q("Qu'est-ce qu'un quartier ?", ["Une partie d'une ville qui a sa propre identité", "Une ville entière", "Une région", "Un pays"], "Une partie d'une ville qui a sa propre identité", "Chaque quartier a sa fonction et son paysage."),
]),
notion('G4-1', 0, F, 'geo4-transports-urbains', [
  Q("Quel moyen de transport souterrain circule dans les grandes villes ?", ["Le métro", "Le tramway", "Le TGV", "Le bateau"], "Le métro", "Celui de Paris a été inauguré en 1900."),
  Q("Pourquoi les villes développent-elles le tramway et les pistes cyclables ?", ["Pour réduire la pollution et les embouteillages", "Pour gêner les piétons", "Pour augmenter le bruit", "Pour supprimer les bus"], "Pour réduire la pollution et les embouteillages", "On parle de mobilités douces."),
  Q("Comment appelle-t-on les ralentissements de circulation aux heures de pointe ?", ["Les embouteillages", "Les migrations", "Les crues", "Les marées"], "Les embouteillages", "Ils sont liés aux trajets domicile-travail."),
]),
notion('G4-1', 0, F, 'geo4-grandes-villes', [
  Q("Quelle est l'agglomération la plus peuplée du monde ?", ["Tokyo", "Paris", "Londres", "Berlin"], "Tokyo", "Elle compte environ 37 millions d'habitants."),
  Q("Quelle est la plus grande agglomération d'Europe de l'Ouest ?", ["Paris", "Lyon", "Rome", "Bruxelles"], "Paris", "Avec Londres, elle dépasse 10 millions d'habitants."),
  Q("Quelle mégapole indienne est la capitale du pays ?", ["Delhi", "Mumbai", "Calcutta", "Chennai"], "Delhi", "Son agglomération dépasse 30 millions d'habitants."),
]),
notion('G4-1', 0, F, 'geo4-gratte-ciel', [
  Q("Comment appelle-t-on un immeuble de très grande hauteur ?", ["Un gratte-ciel", "Un pavillon", "Une chaumière", "Un bungalow"], "Un gratte-ciel", "Ils sont nés à Chicago et New York."),
  Q("Quel est le plus haut gratte-ciel du monde ?", ["Le Burj Khalifa à Dubaï", "La tour Eiffel", "L'Empire State Building", "La tour Montparnasse"], "Le Burj Khalifa à Dubaï", "Il mesure 828 mètres."),
  Q("Pourquoi construit-on des gratte-ciel dans les centres des affaires ?", ["Parce que le terrain y est rare et très cher", "Parce qu'il y a beaucoup de place", "Pour la vue seulement", "Parce que c'est interdit ailleurs"], "Parce que le terrain y est rare et très cher", "On gagne de la place en hauteur."),
]),
notion('G4-1', 0, F, 'geo4-croissance-urbaine', [
  Q("Où les villes grandissent-elles le plus vite aujourd'hui ?", ["En Afrique et en Asie", "En Europe", "En Amérique du Nord", "En Océanie"], "En Afrique et en Asie", "La croissance urbaine y est très rapide."),
  Q("Pourquoi de nombreux ruraux partent-ils vivre en ville ?", ["Pour trouver du travail, des écoles et des soins", "Pour cultiver la terre", "Pour être plus isolés", "Pour fuir l'électricité"], "Pour trouver du travail, des écoles et des soins", "C'est l'exode rural."),
  Q("Comment appelle-t-on le départ des habitants des campagnes vers les villes ?", ["L'exode rural", "La périurbanisation", "La gentrification", "La métropolisation"], "L'exode rural", "Il a été massif en Europe au XIXe siècle."),
]),
notion('G4-1', 0, F, 'geo4-banlieues', [
  Q("Comment appelle-t-on les communes urbaines autour d'une grande ville ?", ["La banlieue", "Le centre-ville", "La campagne isolée", "Le CBD"], "La banlieue", "Elle forme avec la ville-centre une agglomération."),
  Q("Quels types de logements trouve-t-on souvent dans les banlieues françaises ?", ["Des grands ensembles et des pavillons", "Uniquement des châteaux", "Uniquement des fermes", "Des gratte-ciel de 800 m"], "Des grands ensembles et des pavillons", "Les paysages de banlieue sont variés."),
  Q("Qu'est-ce qu'un lotissement ?", ["Un ensemble de maisons individuelles construites sur des parcelles", "Un immeuble de bureaux", "Un centre commercial", "Une usine"], "Un ensemble de maisons individuelles construites sur des parcelles", "On en trouve beaucoup dans le périurbain."),
]),
notion('G4-1', 0, F, 'geo4-centres-commerciaux', [
  Q("Où se trouvent souvent les grands centres commerciaux en France ?", ["En périphérie des villes, près des routes", "Au cœur des centres historiques", "En haute montagne", "Au bord des plages uniquement"], "En périphérie des villes, près des routes", "Ils sont accessibles en voiture."),
  Q("Quel problème les centres commerciaux de périphérie posent-ils aux centres-villes ?", ["Ils attirent les clients et font fermer des commerces du centre", "Ils n'ont aucun effet", "Ils font baisser la circulation", "Ils plantent des arbres"], "Ils attirent les clients et font fermer des commerces du centre", "Les vitrines vides se multiplient dans certaines villes moyennes."),
  Q("Comment appelle-t-on une grande surface de vente de plus de 2 500 m² ?", ["Un hypermarché", "Une épicerie", "Une boulangerie", "Un kiosque"], "Un hypermarché", "Le premier a ouvert en France en 1963."),
]),
notion('G4-1', 1, F, 'geo4-new-york', [
  Q("Quel quartier de New York est célèbre pour ses gratte-ciel ?", ["Manhattan", "Brooklyn", "Le Bronx", "Queens"], "Manhattan", "C'est une île entre deux fleuves."),
  Q("Quelle organisation internationale a son siège à New York ?", ["L'ONU", "L'Union européenne", "L'OTAN", "L'Unesco"], "L'ONU", "Le siège est à Manhattan."),
  Q("Quelle statue accueille les arrivants à l'entrée du port de New York ?", ["La statue de la Liberté", "Le Christ rédempteur", "La statue de Zeus", "Le Sphinx"], "La statue de la Liberté", "Elle a été offerte par la France en 1886."),
]),
notion('G4-1', 1, F, 'geo4-internet-ville', [
  Q("Quel réseau permet aux villes d'échanger instantanément des informations dans le monde ?", ["Internet", "Le canal de Suez", "La route de la soie", "Le télégraphe optique"], "Internet", "Les grandes métropoles sont les mieux connectées."),
  Q("Comment appelle-t-on les grands bâtiments qui stockent les données informatiques ?", ["Des centres de données (data centers)", "Des entrepôts de céréales", "Des musées", "Des gares"], "Des centres de données (data centers)", "Ils consomment beaucoup d'électricité."),
  Q("Pourquoi certaines zones rurales sont-elles moins bien connectées ?", ["Le déploiement de la fibre y est plus coûteux", "Internet y est interdit", "Il n'y a pas d'électricité", "Elles le sont mieux"], "Le déploiement de la fibre y est plus coûteux", "On parle de « zones blanches »."),
]),
notion('G4-1', 1, F, 'geo4-capitales', [
  Q("Quelle est la capitale du Brésil ?", ["Brasília", "Rio de Janeiro", "São Paulo", "Buenos Aires"], "Brasília", "Elle a été construite dans les années 1950."),
  Q("Quelle est la capitale de l'Australie ?", ["Canberra", "Sydney", "Melbourne", "Perth"], "Canberra", "Sydney est la plus grande ville."),
  Q("Quelle est la capitale du Nigeria depuis 1991 ?", ["Abuja", "Lagos", "Kano", "Ibadan"], "Abuja", "Lagos reste la plus grande ville."),
]),
notion('G4-1', 1, F, 'geo4-aeroports', [
  Q("Quel est le principal aéroport de Paris ?", ["Roissy-Charles-de-Gaulle", "Orly", "Beauvais", "Le Bourget"], "Roissy-Charles-de-Gaulle", "C'est l'un des plus grands hubs d'Europe."),
  Q("Quel aéroport du golfe Persique est l'un des premiers du monde pour les passagers internationaux ?", ["Dubaï", "Riyad", "Bagdad", "Téhéran"], "Dubaï", "C'est une plaque tournante entre Europe, Asie et Afrique."),
  Q("Pourquoi les grandes villes ont-elles souvent plusieurs aéroports ?", ["Pour accueillir des millions de passagers et relier le monde", "Pour décorer", "Pour remplacer les gares", "Par obligation légale"], "Pour accueillir des millions de passagers et relier le monde", "Londres en a six."),
]),
notion('G4-1', 1, F, 'geo4-ville-mondiale-paris', [
  Q("Quel quartier d'affaires de l'agglomération parisienne est le premier d'Europe continentale ?", ["La Défense", "Montmartre", "Le Marais", "Belleville"], "La Défense", "Il accueille les sièges de grandes entreprises."),
  Q("Quelle organisation internationale a son siège à Paris ?", ["L'Unesco", "L'ONU", "L'OTAN", "Le FMI"], "L'Unesco", "L'OCDE y a aussi son siège."),
  Q("Pourquoi Paris est-elle une ville mondiale ?", ["Elle concentre des fonctions politiques, économiques, culturelles et touristiques", "Elle est la plus grande ville du monde", "Elle n'a pas d'aéroport", "Elle est au centre de l'Afrique"], "Elle concentre des fonctions politiques, économiques, culturelles et touristiques", "Elle est parmi les villes les plus visitées."),
]),
# ══ Intermédiaire ══
notion('G4-1', 0, I, 'geo4i-etalement', [
  Q("Quel est le principal inconvénient de l'étalement urbain ?", ["Il consomme des terres agricoles et rend les habitants dépendants de la voiture", "Il réduit la circulation", "Il protège la nature", "Il diminue les distances"], "Il consomme des terres agricoles et rend les habitants dépendants de la voiture", "On parle d'artificialisation des sols."),
  Q("Comment appelle-t-on les villes très étalées d'Amérique du Nord, organisées autour de la voiture ?", ["Des villes diffuses (urban sprawl)", "Des villes compactes", "Des villes médiévales", "Des villages"], "Des villes diffuses (urban sprawl)", "Los Angeles en est l'exemple type."),
  Q("Quel modèle de ville cherche-t-on à développer pour limiter l'étalement ?", ["La ville compacte, plus dense", "La ville diffuse", "La ville sans transports", "La ville à la campagne"], "La ville compacte, plus dense", "Elle réduit les déplacements."),
]),
notion('G4-1', 0, I, 'geo4i-bidonvilles-vie', [
  Q("Combien de personnes environ vivent dans des bidonvilles dans le monde ?", ["Plus d'un milliard", "Environ 10 millions", "Environ 100 000", "Personne"], "Plus d'un milliard", "Surtout en Afrique et en Asie."),
  Q("Quels services manquent souvent dans les bidonvilles ?", ["Eau courante, assainissement, électricité", "Supermarchés de luxe", "Aéroports", "Musées"], "Eau courante, assainissement, électricité", "Les habitants n'ont souvent pas de titre de propriété."),
  Q("Comment s'appelle le plus grand bidonville de Nairobi, au Kenya ?", ["Kibera", "Dharavi", "Rocinha", "Soweto"], "Kibera", "Dharavi est à Mumbai, Rocinha à Rio."),
]),
notion('G4-1', 0, I, 'geo4i-politique-ville', [
  Q("Comment appelle-t-on les quartiers défavorisés aidés en priorité par l'État en France ?", ["Les quartiers prioritaires de la politique de la ville (QPV)", "Les zones industrielles", "Les centres historiques", "Les parcs nationaux"], "Les quartiers prioritaires de la politique de la ville (QPV)", "Il y en a environ 1 600."),
  Q("Quelle agence finance la rénovation des grands ensembles depuis 2004 ?", ["L'ANRU (Agence nationale pour la rénovation urbaine)", "L'Insee", "La SNCF", "Météo-France"], "L'ANRU (Agence nationale pour la rénovation urbaine)", "Elle démolit et reconstruit des logements."),
  Q("Quelle loi de 2000 impose aux communes un minimum de logements sociaux ?", ["La loi SRU", "La loi Ferry", "La loi Veil", "La loi Evin"], "La loi SRU", "Le taux est de 20 ou 25 % selon les communes."),
]),
notion('G4-1', 0, I, 'geo4i-modeles-villes', [
  Q("Quelle est une caractéristique des villes européennes ?", ["Un centre historique ancien et dense, souvent valorisé", "L'absence de centre", "Uniquement des gratte-ciel", "Aucun transport public"], "Un centre historique ancien et dense, souvent valorisé", "Les plus aisés y vivent souvent."),
  Q("Quel plan de rues en damier caractérise de nombreuses villes américaines ?", ["Le plan orthogonal", "Le plan radioconcentrique", "Le plan irrégulier médiéval", "Le plan circulaire"], "Le plan orthogonal", "Les rues se croisent à angle droit."),
  Q("Quel plan, en cercles autour d'un centre, caractérise des villes comme Paris ?", ["Le plan radioconcentrique", "Le plan orthogonal", "Le plan linéaire", "Le plan en damier"], "Le plan radioconcentrique", "Les boulevards forment des anneaux successifs."),
]),
notion('G4-1', 0, I, 'geo4i-mobilites-pendulaires', [
  Q("Comment appelle-t-on les trajets quotidiens entre domicile et lieu de travail ?", ["Les migrations pendulaires", "Les migrations internationales", "L'exode rural", "Le tourisme"], "Les migrations pendulaires", "Comme le balancier d'une pendule."),
  Q("Quel réseau ferré transporte chaque jour des millions de Franciliens ?", ["Le RER", "Le TGV", "L'Eurostar", "Le TER Bretagne"], "Le RER", "Réseau express régional."),
  Q("Quel grand projet de métro automatique doit relier les banlieues d'Île-de-France sans passer par Paris ?", ["Le Grand Paris Express", "Le tramway de Nice", "La ligne Lyon-Turin", "Le CDG Express seulement"], "Le Grand Paris Express", "Il compte environ 200 km de lignes nouvelles."),
]),
notion('G4-1', 0, I, 'geo4i-ville-durable', [
  Q("Qu'est-ce qu'une ville durable ?", ["Une ville qui concilie qualité de vie, économie et respect de l'environnement", "Une ville très ancienne", "Une ville sans habitants", "Une ville construite en pierre"], "Une ville qui concilie qualité de vie, économie et respect de l'environnement", "Transports doux, nature en ville, mixité sociale…"),
  Q("Quelle ville allemande est souvent citée comme modèle avec son quartier Vauban ?", ["Fribourg-en-Brisgau", "Berlin", "Munich", "Hambourg"], "Fribourg-en-Brisgau", "Le quartier limite fortement la voiture."),
  Q("Qu'est-ce qu'une zone à faibles émissions (ZFE) ?", ["Une zone où les véhicules les plus polluants sont restreints", "Une zone sans habitants", "Une zone industrielle", "Une zone de pêche"], "Une zone où les véhicules les plus polluants sont restreints", "Elle s'appuie sur les vignettes Crit'Air."),
]),
notion('G4-1', 0, I, 'geo4i-megapoles-asie', [
  Q("Quelle mégapole chinoise est le premier port de conteneurs du monde ?", ["Shanghai", "Pékin", "Chongqing", "Wuhan"], "Shanghai", "Elle est située à l'embouchure du Yangzi."),
  Q("Quelle région urbaine chinoise, autour de Canton, Shenzhen et Hong Kong, est l'une des plus peuplées du monde ?", ["Le delta de la rivière des Perles", "Le Tibet", "La Mandchourie", "Le désert de Gobi"], "Le delta de la rivière des Perles", "On parle de « Greater Bay Area »."),
  Q("Quelle ville chinoise est passée d'un village de pêcheurs à une mégapole depuis 1980 ?", ["Shenzhen", "Pékin", "Xi'an", "Nankin"], "Shenzhen", "Elle a été la première zone économique spéciale."),
]),
notion('G4-1', 0, I, 'geo4i-segregation-exemples', [
  Q("Quel quartier de Johannesburg était réservé aux Noirs pendant l'apartheid ?", ["Soweto", "Manhattan", "La Défense", "Copacabana"], "Soweto", "La ségrégation était inscrite dans la loi."),
  Q("Comment appelle-t-on la concentration de populations pauvres dans certains quartiers ?", ["La ségrégation socio-spatiale", "La gentrification", "La métropolisation", "La littoralisation"], "La ségrégation socio-spatiale", "Elle peut être choisie ou subie."),
  Q("Quels quartiers fermés se multiplient en Amérique latine pour les plus aisés ?", ["Les condominios fechados", "Les favelas", "Les townships", "Les kibboutz"], "Les condominios fechados", "Ce sont des gated communities."),
]),
notion('G4-1', 1, I, 'geo4i-hierarchie-villes', [
  Q("Quelles sont les trois villes mondiales les plus influentes ?", ["New York, Londres et Tokyo", "Lyon, Lille et Nantes", "Bamako, Dakar et Niamey", "Quito, Lima et La Paz"], "New York, Londres et Tokyo", "On les appelle parfois les « villes globales »."),
  Q("Quelle sociologue a popularisé l'expression « ville globale » en 1991 ?", ["Saskia Sassen", "Hannah Arendt", "Simone de Beauvoir", "Jane Jacobs"], "Saskia Sassen", "Elle étudie New York, Londres et Tokyo."),
  Q("Qu'est-ce qui distingue une métropole d'une simple grande ville ?", ["Ses fonctions de commandement et son rayonnement", "Uniquement sa population", "Sa superficie", "Son climat"], "Ses fonctions de commandement et son rayonnement", "Une métropole commande un territoire."),
]),
notion('G4-1', 1, I, 'geo4i-ports-hubs', [
  Q("Comment appelle-t-on la plateforme où un port échange avec son arrière-pays par fer, route et fleuve ?", ["Une plateforme multimodale", "Une ZEE", "Un CBD", "Un bidonville"], "Une plateforme multimodale", "Elle relie plusieurs modes de transport."),
  Q("Comment appelle-t-on l'espace desservi par un port ?", ["L'hinterland (arrière-pays)", "L'avant-pays", "Le front de mer", "La ZEE"], "L'hinterland (arrière-pays)", "L'avant-pays, ce sont les régions reliées par la mer."),
  Q("Quel hub aérien du Moyen-Orient relie l'Europe à l'Asie et à l'Océanie ?", ["Doha", "Bagdad", "Damas", "Amman"], "Doha", "Avec Dubaï et Abu Dhabi."),
]),
notion('G4-1', 1, I, 'geo4i-villes-delaissees', [
  Q("Comment appelle-t-on une ville qui perd des habitants et des emplois ?", ["Une ville en décroissance (shrinking city)", "Une mégapole", "Une ville globale", "Une métropole"], "Une ville en décroissance (shrinking city)", "Détroit en est l'exemple le plus connu."),
  Q("Pourquoi certaines villes sont-elles moins connectées à la mondialisation ?", ["Leur économie repose sur des activités en déclin ou elles sont enclavées", "Elles sont trop riches", "Elles sont au bord de la mer", "Elles ont trop d'aéroports"], "Leur économie repose sur des activités en déclin ou elles sont enclavées", "La mondialisation crée des gagnants et des perdants."),
  Q("Quelle région allemande a connu une forte crise de ses villes industrielles (charbon, acier) ?", ["La Ruhr", "La Bavière", "Berlin", "Hambourg"], "La Ruhr", "Elle s'est reconvertie dans les services et la culture."),
]),
notion('G4-1', 1, I, 'geo4i-cbd-londres', [
  Q("Quel quartier d'affaires s'est développé dans les anciens docks de Londres ?", ["Canary Wharf", "La City médiévale", "Soho", "Notting Hill"], "Canary Wharf", "C'est un exemple de reconversion de friches portuaires."),
  Q("Qu'est-ce qu'une friche ?", ["Un espace abandonné après la fin d'une activité", "Un parc protégé", "Un centre commercial actif", "Un champ cultivé"], "Un espace abandonné après la fin d'une activité", "Les friches peuvent être reconverties."),
  Q("Quelle ville espagnole a été transformée par l'ouverture du musée Guggenheim en 1997 ?", ["Bilbao", "Madrid", "Séville", "Valence"], "Bilbao", "On parle d'« effet Guggenheim »."),
]),
notion('G4-1', 1, I, 'geo4i-sieges-sociaux', [
  Q("Où se concentrent les sièges sociaux des grandes firmes multinationales ?", ["Dans les métropoles des pays riches et émergents", "Dans les villages", "Dans les déserts", "Dans les îles isolées"], "Dans les métropoles des pays riches et émergents", "Tokyo, New York, Londres, Paris, Pékin…"),
  Q("Comment appelle-t-on une entreprise implantée dans plusieurs pays ?", ["Une firme multinationale (FMN)", "Une PME locale", "Une coopérative agricole", "Une association"], "Une firme multinationale (FMN)", "Elle participe à la mondialisation."),
  Q("Quelle place boursière est la plus importante du monde ?", ["New York", "Paris", "Francfort", "Madrid"], "New York", "Le NYSE et le Nasdaq y sont installés."),
]),
notion('G4-1', 1, I, 'geo4i-tgv-metropoles', [
  Q("Quel train relie Paris à Londres sous la Manche ?", ["L'Eurostar", "Le Thalys", "Le RER B", "L'Orient-Express"], "L'Eurostar", "Le trajet dure environ 2 h 15."),
  Q("Pourquoi les lignes à grande vitesse renforcent-elles les métropoles ?", ["Elles relient rapidement les grandes villes entre elles", "Elles desservent surtout les villages", "Elles ralentissent les échanges", "Elles évitent les grandes villes"], "Elles relient rapidement les grandes villes entre elles", "On parle d'« effet tunnel » pour les territoires traversés sans arrêt."),
  Q("Quel pays possède le plus grand réseau de trains à grande vitesse du monde ?", ["La Chine", "La France", "Le Japon", "L'Espagne"], "La Chine", "Plus de 45 000 km de lignes."),
]),
# ══ Avancé ══
notion('G4-1', 0, D, 'geo4d-aire-attraction', [
  Q("Comment l'Insee définit-il une aire d'attraction d'une ville depuis 2020 ?", ["Un pôle de population et d'emploi et les communes dont au moins 15 % des actifs y travaillent", "Une ville et ses parcs", "Une région administrative", "Un département"], "Un pôle de population et d'emploi et les communes dont au moins 15 % des actifs y travaillent", "Elle remplace la notion d'aire urbaine."),
  Q("Comment appelle-t-on une agglomération dont le bâti est continu ?", ["Une unité urbaine", "Une aire d'attraction", "Une commune rurale", "Un canton"], "Une unité urbaine", "Pas de coupure de plus de 200 m entre deux constructions."),
  Q("Quel indicateur montre la puissance d'attraction d'une ville sur ses alentours ?", ["Les navettes domicile-travail", "La couleur des façades", "Le nombre de fontaines", "L'altitude"], "Les navettes domicile-travail", "Elles dessinent l'aire d'influence."),
]),
notion('G4-1', 0, D, 'geo4d-taux-urbanisation', [
  Q("Quel continent a le taux d'urbanisation le plus élevé ?", ["L'Amérique (latine et du Nord)", "L'Afrique", "L'Asie du Sud", "L'Océanie insulaire"], "L'Amérique (latine et du Nord)", "Environ 80 % de la population y est urbaine."),
  Q("Quel continent a le taux d'urbanisation le plus faible ?", ["L'Afrique", "L'Europe", "L'Amérique du Nord", "L'Amérique latine"], "L'Afrique", "Environ 45 %, mais il augmente très vite."),
  Q("Pourquoi un taux d'urbanisation ne se compare-t-il pas toujours facilement d'un pays à l'autre ?", ["Chaque pays définit la ville selon ses propres critères", "Parce que les villes changent de taille chaque jour", "Parce que l'ONU l'interdit", "Il se compare toujours facilement"], "Chaque pays définit la ville selon ses propres critères", "Au Danemark, 200 habitants suffisent ; au Japon, il en faut 50 000."),
]),
notion('G4-1', 0, D, 'geo4d-macrocephalie', [
  Q("Comment appelle-t-on la situation d'un pays où une ville écrase toutes les autres par sa taille ?", ["La macrocéphalie urbaine", "La métropolisation douce", "La périurbanisation", "La gentrification"], "La macrocéphalie urbaine", "C'est le cas de Bangkok ou de Lima."),
  Q("Quelle ville est un exemple de primatie dans un pays européen ?", ["Paris en France", "Berlin en Allemagne", "Rome en Italie", "Madrid en Espagne"], "Paris en France", "Son agglomération est plus de cinq fois plus peuplée que celle de Lyon."),
  Q("Quelle est la conséquence de la macrocéphalie sur le territoire ?", ["Un déséquilibre au profit de la capitale", "Un équilibre parfait", "La disparition de la capitale", "La croissance de toutes les villes moyennes"], "Un déséquilibre au profit de la capitale", "L'aménagement cherche à le corriger."),
]),
notion('G4-1', 0, D, 'geo4d-informalite-logement', [
  Q("Comment appelle-t-on un habitat construit sans autorisation sur un terrain que l'on ne possède pas ?", ["Un habitat informel (ou illégal)", "Un lotissement", "Un HLM", "Une résidence secondaire"], "Un habitat informel (ou illégal)", "Il domine dans de nombreuses villes du Sud."),
  Q("Quelle politique consiste à améliorer un bidonville sur place plutôt qu'à le raser ?", ["La réhabilitation in situ", "Le déguerpissement", "La gentrification", "L'étalement urbain"], "La réhabilitation in situ", "Les favelas de Rio en ont bénéficié."),
  Q("Comment appelle-t-on l'expulsion forcée des habitants d'un quartier informel ?", ["Le déguerpissement", "La réhabilitation", "La densification", "La métropolisation"], "Le déguerpissement", "Le terme est employé en Afrique francophone."),
]),
notion('G4-1', 0, D, 'geo4d-transports-sud', [
  Q("Quel système de bus à haut niveau de service, inventé à Curitiba, s'est diffusé dans le monde ?", ["Le BRT (bus rapid transit)", "Le métro automatique", "Le téléphérique urbain", "Le tramway à cheval"], "Le BRT (bus rapid transit)", "Bogota l'a développé avec le TransMilenio."),
  Q("Quelle ville colombienne a relié ses quartiers pauvres des collines par des téléphériques ?", ["Medellín", "Bogota", "Cali", "Carthagène"], "Medellín", "Le Metrocable a transformé ces quartiers."),
  Q("Comment appelle-t-on les minibus collectifs souvent informels des villes africaines ?", ["Les « taxis-brousse » ou matatus", "Les tramways", "Les RER", "Les TGV"], "Les « taxis-brousse » ou matatus", "Ils assurent l'essentiel des déplacements."),
]),
notion('G4-1', 0, D, 'geo4d-villes-nouvelles', [
  Q("Comment appelle-t-on les villes créées ex nihilo autour de Paris dans les années 1970 ?", ["Les villes nouvelles", "Les villes médiévales", "Les bastides", "Les cités-jardins"], "Les villes nouvelles", "Cergy-Pontoise, Marne-la-Vallée, Évry…"),
  Q("Quelle nouvelle capitale l'Égypte construit-elle dans le désert à l'est du Caire ?", ["La Nouvelle Capitale administrative", "Alexandrie", "Louxor", "Assouan"], "La Nouvelle Capitale administrative", "Elle vise à désengorger Le Caire."),
  Q("Quel pays transfère sa capitale de Jakarta vers Nusantara, sur l'île de Bornéo ?", ["L'Indonésie", "La Malaisie", "Les Philippines", "La Thaïlande"], "L'Indonésie", "Jakarta s'enfonce et est menacée par la mer."),
]),
notion('G4-1', 0, D, 'geo4d-gentrification-exemples', [
  Q("Quel quartier populaire de l'est de Paris a connu une forte gentrification ?", ["Belleville et le Faubourg-Saint-Antoine", "Neuilly-sur-Seine", "Le 16e arrondissement", "Versailles"], "Belleville et le Faubourg-Saint-Antoine", "Les prix de l'immobilier y ont fortement augmenté."),
  Q("Quelle conséquence la gentrification a-t-elle pour les habitants modestes ?", ["Ils sont repoussés vers les périphéries par la hausse des loyers", "Leurs loyers baissent", "Ils deviennent propriétaires automatiquement", "Aucune"], "Ils sont repoussés vers les périphéries par la hausse des loyers", "La composition sociale du quartier change."),
  Q("Quel dispositif limite les loyers dans certaines villes françaises comme Paris ?", ["L'encadrement des loyers", "Le blocage des salaires", "La gratuité des logements", "La loi Ferry"], "L'encadrement des loyers", "Il fixe un loyer de référence au m²."),
]),
notion('G4-1', 0, D, 'geo4d-mixite-fonctionnelle', [
  Q("Qu'est-ce que le zonage en urbanisme ?", ["La séparation des fonctions (habiter, travailler, consommer) dans des quartiers distincts", "Le mélange des activités", "La construction de murs", "Le découpage en départements"], "La séparation des fonctions (habiter, travailler, consommer) dans des quartiers distincts", "Il a été promu par la Charte d'Athènes (1933)."),
  Q("Quel architecte franco-suisse a inspiré l'urbanisme fonctionnaliste ?", ["Le Corbusier", "Haussmann", "Vauban", "Gaudí"], "Le Corbusier", "Sa Cité radieuse est à Marseille."),
  Q("Qu'est-ce que la « ville du quart d'heure » ?", ["Une ville où l'on accède aux services essentiels à 15 minutes à pied ou à vélo", "Une ville construite en 15 minutes", "Une ville de 15 habitants", "Un quartier ouvert 15 minutes par jour"], "Une ville où l'on accède aux services essentiels à 15 minutes à pied ou à vélo", "Le concept est de l'urbaniste Carlos Moreno."),
]),
notion('G4-1', 1, D, 'geo4d-classements-villes', [
  Q("Quel réseau de chercheurs classe les villes mondiales en catégories Alpha, Beta et Gamma ?", ["Le GaWC (Globalization and World Cities)", "L'Insee", "L'Unesco", "La FIFA"], "Le GaWC (Globalization and World Cities)", "Londres et New York sont classées « Alpha++ »."),
  Q("Sur quoi reposent ces classements de villes mondiales ?", ["La présence de services avancés aux entreprises (finance, conseil, droit)", "Le nombre de monuments", "La température moyenne", "La taille des stades"], "La présence de services avancés aux entreprises (finance, conseil, droit)", "Ils mesurent l'intégration aux réseaux mondiaux."),
  Q("Quelle ville du Golfe a fortement progressé dans la hiérarchie des villes mondiales ?", ["Dubaï", "Sanaa", "Mascate", "Koweït City"], "Dubaï", "Grâce au commerce, à la finance et au tourisme."),
]),
notion('G4-1', 1, D, 'geo4d-reseaux-numeriques', [
  Q("Quelle ville française accueille de nombreux câbles sous-marins grâce à sa position méditerranéenne ?", ["Marseille", "Lille", "Strasbourg", "Clermont-Ferrand"], "Marseille", "Elle est l'un des grands hubs numériques mondiaux."),
  Q("Qu'est-ce que la fracture numérique ?", ["L'inégal accès aux technologies numériques entre territoires et populations", "La casse d'un câble", "Un virus informatique", "Une panne d'électricité"], "L'inégal accès aux technologies numériques entre territoires et populations", "Elle existe entre pays et à l'intérieur des pays."),
  Q("Pourquoi les métropoles attirent-elles les entreprises du numérique ?", ["Elles offrent des talents, des universités, des capitaux et de bonnes connexions", "Le terrain y est gratuit", "Il n'y a pas d'impôts", "Il y a moins de concurrence"], "Elles offrent des talents, des universités, des capitaux et de bonnes connexions", "On parle d'effets d'agglomération."),
]),
notion('G4-1', 1, D, 'geo4d-villes-emergentes', [
  Q("Quelle ville africaine est devenue un pôle technologique surnommé « Silicon Savannah » ?", ["Nairobi", "Kinshasa", "Bamako", "Niamey"], "Nairobi", "Le paiement mobile M-Pesa y est né."),
  Q("Quelle ville indienne est surnommée la « Silicon Valley de l'Inde » ?", ["Bangalore (Bengaluru)", "Calcutta", "Varanasi", "Jaipur"], "Bangalore (Bengaluru)", "Elle concentre les entreprises informatiques."),
  Q("Quelle ville brésilienne est le premier centre économique et financier d'Amérique du Sud ?", ["São Paulo", "Brasília", "Salvador", "Manaus"], "São Paulo", "Son agglomération dépasse 20 millions d'habitants."),
]),
notion('G4-1', 1, D, 'geo4d-metropoles-francaises', [
  Q("Combien de métropoles (statut intercommunal) compte la France ?", ["22", "3", "100", "13"], "22", "Créées par les lois de 2014 et 2017."),
  Q("Quelles métropoles ont un statut particulier en France ?", ["Le Grand Paris, Aix-Marseille-Provence et Lyon", "Lille, Nantes et Rennes", "Brest, Nice et Metz", "Toulouse, Bordeaux et Dijon"], "Le Grand Paris, Aix-Marseille-Provence et Lyon", "La métropole de Lyon est même une collectivité territoriale à part entière."),
  Q("Pourquoi les métropoles régionales françaises cherchent-elles à s'internationaliser ?", ["Pour attirer entreprises, étudiants et touristes face à la concurrence mondiale", "Pour quitter la France", "Pour réduire leur population", "Par obligation européenne"], "Pour attirer entreprises, étudiants et touristes face à la concurrence mondiale", "Lyon et Toulouse ont un fort rayonnement européen."),
]),
notion('G4-1', 0, D, 'geo4d-ville-climat', [
  Q("Quelle part des émissions mondiales de CO2 est liée aux villes ?", ["Environ 70 %", "Environ 5 %", "Environ 20 %", "100 %"], "Environ 70 %", "Les villes occupent pourtant moins de 3 % des terres."),
  Q("Quel réseau mondial rassemble de grandes villes engagées pour le climat ?", ["Le C40", "Le G7", "L'OPEP", "Le Mercosur"], "Le C40", "Paris en fait partie."),
  Q("Quelle mégapole s'enfonce de plusieurs centimètres par an à cause du pompage des nappes ?", ["Jakarta", "Londres", "Madrid", "Oslo"], "Jakarta", "Mexico est aussi concernée."),
]),
notion('G4-1', 1, D, 'geo4d-megalopoles', [
  Q("Comment appelle-t-on une chaîne de grandes villes reliées entre elles sur des centaines de kilomètres ?", ["Une mégalopole", "Une mégapole", "Une conurbation de village", "Une ZEE"], "Une mégalopole", "À ne pas confondre avec la mégapole (une seule ville géante)."),
  Q("Quelle mégalopole japonaise s'étend de Tokyo à Osaka ?", ["La mégalopole du Tokaido", "La BosWash", "La Banane bleue", "La Sun Belt"], "La mégalopole du Tokaido", "Elle est reliée par le Shinkansen."),
  Q("Quel géographe français a forgé le mot « mégalopole » en 1961 ?", ["Jean Gottmann", "Paul Vidal de La Blache", "Élisée Reclus", "Roger Brunet"], "Jean Gottmann", "Il étudiait le nord-est des États-Unis."),
]),
]

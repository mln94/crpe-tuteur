# Géographie 4e · Les mobilités humaines transnationales : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G4-2', 0, F, 'geo4-emigration-immigration', [
  Q("Comment appelle-t-on le fait de quitter son pays pour aller vivre ailleurs ?", ["L'émigration", "L'immigration", "Le tourisme", "L'exode rural"], "L'émigration", "Pour le pays d'arrivée, on parle d'immigration."),
  Q("Comment appelle-t-on une personne qui arrive dans un pays pour s'y installer ?", ["Un immigré", "Un émigré", "Un touriste", "Un frontalier"], "Un immigré", "Une même personne est émigrée pour son pays d'origine et immigrée pour son pays d'accueil."),
  Q("Quel pays est le point de départ de nombreux migrants vers les États-Unis ?", ["Le Mexique", "La Norvège", "Le Japon", "L'Australie"], "Le Mexique", "C'est le premier couloir migratoire du monde."),
]),
notion('G4-2', 0, F, 'geo4-raisons-migrer', [
  Q("Laquelle de ces raisons pousse des personnes à migrer ?", ["La guerre, la pauvreté, la recherche d'un emploi ou les études", "L'envie de rester chez soi", "Le beau temps uniquement", "L'obligation légale"], "La guerre, la pauvreté, la recherche d'un emploi ou les études", "Les causes sont souvent multiples."),
  Q("Comment appelle-t-on les facteurs qui poussent à partir ?", ["Les facteurs répulsifs", "Les facteurs attractifs", "Les facteurs touristiques", "Les facteurs climatiques uniquement"], "Les facteurs répulsifs", "Les facteurs attractifs attirent vers le pays d'arrivée."),
  Q("Qu'est-ce qu'un regroupement familial ?", ["La venue des membres de la famille d'un immigré installé", "Une fête de famille", "Un voyage scolaire", "Un mariage"], "La venue des membres de la famille d'un immigré installé", "C'est une cause importante d'immigration en Europe."),
]),
notion('G4-2', 0, F, 'geo4-mediterranee-migrants', [
  Q("Quelle mer de nombreux migrants traversent-ils pour rejoindre l'Europe ?", ["La Méditerranée", "La mer du Nord", "La mer Baltique", "La mer Caspienne"], "La Méditerranée", "Ces traversées sont très dangereuses."),
  Q("Quelle île italienne est une porte d'entrée des migrants en Europe ?", ["Lampedusa", "La Sardaigne", "La Corse", "Malte"], "Lampedusa", "Elle est très proche des côtes tunisiennes."),
  Q("Quel archipel espagnol, au large de l'Afrique, voit arriver de nombreux migrants ?", ["Les Canaries", "Les Baléares", "Les Açores", "Madère"], "Les Canaries", "La route atlantique est particulièrement meurtrière."),
]),
notion('G4-2', 0, F, 'geo4-etudiants-internationaux', [
  Q("Quel pays accueille le plus d'étudiants étrangers ?", ["Les États-Unis", "Le Niger", "La Mongolie", "Le Népal"], "Les États-Unis", "Suivis du Royaume-Uni, du Canada et de l'Australie."),
  Q("Pourquoi des jeunes vont-ils étudier à l'étranger ?", ["Pour obtenir un diplôme reconnu et découvrir une autre culture", "Pour éviter d'apprendre", "Parce que c'est obligatoire partout", "Pour faire du tourisme seulement"], "Pour obtenir un diplôme reconnu et découvrir une autre culture", "Ce sont des migrations temporaires."),
  Q("Quel pays fournit le plus d'étudiants internationaux dans le monde ?", ["La Chine", "La France", "Le Luxembourg", "Monaco"], "La Chine", "Suivie de l'Inde."),
]),
notion('G4-2', 0, F, 'geo4-immigration-france', [
  Q("Quelle part environ de la population française est immigrée ?", ["Environ 11 %", "Environ 50 %", "Environ 1 %", "Environ 30 %"], "Environ 11 %", "Soit environ 7 millions de personnes."),
  Q("De quel continent vient la majorité des immigrés en France aujourd'hui ?", ["L'Afrique", "L'Océanie", "L'Antarctique", "L'Amérique du Sud"], "L'Afrique", "Surtout du Maghreb, puis d'Afrique subsaharienne."),
  Q("Quel pays européen a fourni de nombreux immigrés à la France dans les années 1960-1970 ?", ["Le Portugal", "La Suède", "La Finlande", "L'Islande"], "Le Portugal", "L'Italie et l'Espagne aussi."),
]),
notion('G4-2', 0, F, 'geo4-frontieres', [
  Q("Qu'est-ce qu'une frontière ?", ["Une limite qui sépare deux États", "Une route nationale", "Un fleuve quelconque", "Une ville"], "Une limite qui sépare deux États", "Elle peut être ouverte ou fermée."),
  Q("Quel document faut-il souvent pour entrer dans un pays étranger ?", ["Un passeport, parfois avec un visa", "Une carte de cantine", "Un ticket de métro", "Un permis de pêche"], "Un passeport, parfois avec un visa", "Le visa est une autorisation d'entrée."),
  Q("Quel mur a été construit sur une partie de la frontière entre les États-Unis et le Mexique ?", ["Une barrière frontalière de plusieurs centaines de kilomètres", "Le mur de Berlin", "La Grande Muraille", "Le mur d'Hadrien"], "Une barrière frontalière de plusieurs centaines de kilomètres", "Elle vise à limiter l'immigration irrégulière."),
]),
notion('G4-2', 0, F, 'geo4-travailleurs-frontaliers', [
  Q("Comment appelle-t-on une personne qui vit dans un pays et travaille dans le pays voisin ?", ["Un travailleur frontalier", "Un réfugié", "Un touriste", "Un expatrié définitif"], "Un travailleur frontalier", "Il traverse la frontière chaque jour."),
  Q("Vers quel pays partent chaque jour de nombreux frontaliers français de Haute-Savoie ?", ["La Suisse", "L'Espagne", "Le Royaume-Uni", "Le Portugal"], "La Suisse", "Les salaires y sont plus élevés, notamment à Genève."),
  Q("Quel petit pays accueille chaque jour plus de 100 000 frontaliers venus de France, de Belgique et d'Allemagne ?", ["Le Luxembourg", "Andorre", "Monaco seul", "Le Liechtenstein"], "Le Luxembourg", "Près de la moitié de ses salariés sont frontaliers."),
]),
notion('G4-2', 1, F, 'geo4-sites-touristiques', [
  Q("Quel monument parisien est l'un des plus visités au monde ?", ["La tour Eiffel", "La tour de Pise", "Big Ben", "Le Colisée"], "La tour Eiffel", "Environ 6 millions de visiteurs par an."),
  Q("Quel parc d'attractions près de Paris est le plus visité d'Europe ?", ["Disneyland Paris", "Le Puy du Fou", "Le Futuroscope", "Le parc Astérix"], "Disneyland Paris", "Il a ouvert en 1992 à Marne-la-Vallée."),
  Q("Quel site normand est l'un des plus visités de France ?", ["Le Mont-Saint-Michel", "Le pont du Gard", "Carcassonne", "Rocamadour"], "Le Mont-Saint-Michel", "Il est inscrit au patrimoine mondial de l'Unesco."),
]),
notion('G4-2', 1, F, 'geo4-types-tourisme', [
  Q("Comment appelle-t-on le tourisme au bord de la mer ?", ["Le tourisme balnéaire", "Le tourisme vert", "Le tourisme d'affaires", "Le tourisme culturel"], "Le tourisme balnéaire", "Il est concentré en été."),
  Q("Comment appelle-t-on le tourisme à la campagne, au contact de la nature ?", ["Le tourisme vert", "Le tourisme balnéaire", "Le tourisme urbain", "Le tourisme spatial"], "Le tourisme vert", "Gîtes, randonnées, fermes…"),
  Q("Comment appelle-t-on le tourisme qui consiste à visiter musées et monuments ?", ["Le tourisme culturel", "Le tourisme d'hiver", "Le tourisme médical", "Le tourisme balnéaire"], "Le tourisme culturel", "Il est surtout urbain."),
]),
notion('G4-2', 1, F, 'geo4-patrimoine-mondial', [
  Q("Quelle organisation établit la liste du patrimoine mondial ?", ["L'Unesco", "L'OMS", "L'OTAN", "La FIFA"], "L'Unesco", "Elle a son siège à Paris."),
  Q("Pourquoi un site inscrit au patrimoine mondial attire-t-il les touristes ?", ["Le label lui donne une renommée internationale", "Il devient gratuit", "Il est plus proche des villes", "Il est interdit d'y aller"], "Le label lui donne une renommée internationale", "Il doit aussi être protégé."),
  Q("Quel site péruvien inscrit au patrimoine mondial est menacé par l'afflux de visiteurs ?", ["Le Machu Picchu", "Le Taj Mahal", "Angkor", "Pétra"], "Le Machu Picchu", "Le nombre de visiteurs y est limité chaque jour."),
]),
notion('G4-2', 1, F, 'geo4-croisieres', [
  Q("Qu'est-ce qu'une croisière ?", ["Un voyage touristique à bord d'un grand navire avec plusieurs escales", "Un trajet en métro", "Une randonnée en montagne", "Un voyage d'affaires en avion"], "Un voyage touristique à bord d'un grand navire avec plusieurs escales", "Le marché des croisières est en forte croissance."),
  Q("Quelle mer est la première destination des croisières dans le monde ?", ["La mer des Caraïbes", "La mer Baltique", "La mer Blanche", "La mer de Ross"], "La mer des Caraïbes", "La Méditerranée est deuxième."),
  Q("Quel problème posent les grands paquebots de croisière dans des villes comme Venise ?", ["Pollution et afflux massif de visiteurs", "Ils manquent de passagers", "Ils sont trop petits", "Aucun"], "Pollution et afflux massif de visiteurs", "Les plus gros navires sont interdits dans la lagune depuis 2021."),
]),
notion('G4-2', 1, F, 'geo4-tourisme-montagne', [
  Q("Quelle activité touristique fait vivre de nombreuses stations des Alpes en hiver ?", ["Le ski", "La plongée", "Le surf", "La voile"], "Le ski", "La France possède l'un des plus grands domaines skiables du monde."),
  Q("Comment appelle-t-on une station créée de toutes pièces en altitude pour le ski ?", ["Une station intégrée", "Une station balnéaire", "Une station de métro", "Une station-service"], "Une station intégrée", "Comme Avoriaz ou Flaine."),
  Q("Quelle activité estivale se développe en montagne ?", ["La randonnée et le VTT", "Le ski alpin", "La plongée sous-marine", "Le surf"], "La randonnée et le VTT", "Les stations cherchent à attirer toute l'année."),
]),
notion('G4-2', 1, F, 'geo4-touristes-francais', [
  Q("Où partent en vacances la majorité des Français ?", ["En France", "En Asie", "En Océanie", "En Antarctique"], "En France", "Environ 80 % des séjours se font en France."),
  Q("Quelle région française accueille le plus de touristes ?", ["L'Île-de-France", "La Corse", "Le Limousin", "La Lorraine"], "L'Île-de-France", "Grâce à Paris et Disneyland."),
  Q("Pourquoi les départs en vacances provoquent-ils de grands embouteillages en été ?", ["Beaucoup de vacanciers partent en même temps vers les côtes", "Les routes sont fermées", "Il y a moins de voitures", "Il neige"], "Beaucoup de vacanciers partent en même temps vers les côtes", "Bison Futé donne des prévisions de trafic."),
]),
# ══ Intermédiaire ══
notion('G4-2', 0, I, 'geo4i-routes-migratoires', [
  Q("Comment appelle-t-on l'itinéraire emprunté par des migrants entre leur pays d'origine et leur pays d'arrivée ?", ["Une route migratoire", "Un couloir aérien", "Une autoroute", "Une ligne de démarcation"], "Une route migratoire", "Elle compte souvent de nombreuses étapes."),
  Q("Quelle route relie la Libye ou la Tunisie à l'Italie ?", ["La route de la Méditerranée centrale", "La route des Balkans", "La route de la soie", "La route du Cap"], "La route de la Méditerranée centrale", "C'est la plus meurtrière."),
  Q("Quelle route a été empruntée massivement en 2015 par des réfugiés syriens, de la Turquie vers l'Allemagne ?", ["La route des Balkans", "La route atlantique", "La route du Pacifique", "La route arctique"], "La route des Balkans", "L'Allemagne a accueilli près d'un million de demandeurs d'asile."),
]),
notion('G4-2', 0, I, 'geo4i-passeurs', [
  Q("Comment appelle-t-on les personnes qui font payer aux migrants le passage illégal d'une frontière ?", ["Des passeurs", "Des douaniers", "Des diplomates", "Des guides touristiques"], "Des passeurs", "Ils forment souvent des réseaux criminels."),
  Q("Quelle traversée, très dangereuse, tentent des migrants entre la France et le Royaume-Uni ?", ["La traversée de la Manche en petites embarcations", "La traversée des Alpes à ski", "La traversée du Rhin", "La traversée de la Garonne"], "La traversée de la Manche en petites embarcations", "On parle de « small boats »."),
  Q("Comment appelle-t-on une migration sans autorisation légale ?", ["Une migration irrégulière", "Une migration pendulaire", "Une migration saisonnière légale", "Une migration interne"], "Une migration irrégulière", "Les médias parlent parfois de clandestins."),
]),
notion('G4-2', 0, I, 'geo4i-pays-depart-arrivee', [
  Q("Quel pays du Golfe compte une majorité d'immigrés dans sa population ?", ["Les Émirats arabes unis", "Le Yémen", "L'Iran", "L'Irak"], "Les Émirats arabes unis", "Près de 9 habitants sur 10 sont étrangers."),
  Q("Quel pays européen accueille le plus d'immigrés ?", ["L'Allemagne", "La Pologne", "La Grèce", "L'Islande"], "L'Allemagne", "Elle a besoin de main-d'œuvre face au vieillissement."),
  Q("Quel pays d'Asie compte des millions d'émigrés travaillant dans le monde, notamment comme marins et infirmiers ?", ["Les Philippines", "Le Japon", "La Corée du Nord", "Le Bhoutan"], "Les Philippines", "Leurs envois d'argent pèsent lourd dans l'économie."),
]),
notion('G4-2', 0, I, 'geo4i-deplaces-internes', [
  Q("Comment appelle-t-on une personne qui fuit la guerre sans quitter son pays ?", ["Un déplacé interne", "Un réfugié", "Un touriste", "Un expatrié"], "Un déplacé interne", "Ils sont plus nombreux que les réfugiés."),
  Q("Environ combien de personnes sont déracinées de force dans le monde au milieu des années 2020 ?", ["Plus de 120 millions", "Environ 1 million", "Environ 10 millions", "Environ 1 milliard"], "Plus de 120 millions", "Selon le HCR."),
  Q("Quel pays a connu l'une des plus grandes crises de déplacement au monde depuis 2023 ?", ["Le Soudan", "La Suisse", "Le Canada", "La Norvège"], "Le Soudan", "La guerre civile y a déplacé plus de 10 millions de personnes."),
]),
notion('G4-2', 0, I, 'geo4i-pays-accueil-refugies', [
  Q("Où vivent la majorité des réfugiés du monde ?", ["Dans des pays voisins de leur pays d'origine, souvent pauvres", "En Europe de l'Ouest", "Aux États-Unis", "En Australie"], "Dans des pays voisins de leur pays d'origine, souvent pauvres", "Environ 70 % sont accueillis dans un pays voisin."),
  Q("Quel pays accueille l'un des plus grands nombres de réfugiés, venus d'Afghanistan ?", ["L'Iran", "Le Japon", "Le Brésil", "Le Canada"], "L'Iran", "La Turquie a aussi accueilli des millions de Syriens."),
  Q("Quel pays européen a accueilli le plus de réfugiés ukrainiens après 2022 ?", ["L'Allemagne (et la Pologne)", "Le Portugal", "L'Irlande", "Malte"], "L'Allemagne (et la Pologne)", "Les Ukrainiens bénéficient d'une protection temporaire dans l'UE."),
]),
notion('G4-2', 0, I, 'geo4i-hcr', [
  Q("Quelle agence de l'ONU protège les réfugiés ?", ["Le HCR (Haut-Commissariat des Nations unies pour les réfugiés)", "L'OMS", "La FAO", "L'Unesco"], "Le HCR (Haut-Commissariat des Nations unies pour les réfugiés)", "Il a reçu deux fois le prix Nobel de la paix."),
  Q("Quel organisme français examine les demandes d'asile ?", ["L'Ofpra", "L'Insee", "La CAF", "Pôle emploi"], "L'Ofpra", "Office français de protection des réfugiés et apatrides."),
  Q("Qu'est-ce qu'un camp de réfugiés ?", ["Un lieu d'accueil, souvent temporaire, pour des personnes qui fuient", "Un camp de vacances", "Une base militaire", "Un village de pêcheurs"], "Un lieu d'accueil, souvent temporaire, pour des personnes qui fuient", "Certains existent depuis des décennies."),
]),
notion('G4-2', 0, I, 'geo4i-migrations-sud-sud', [
  Q("Quel pays d'Afrique de l'Ouest accueille de nombreux migrants de la région, notamment burkinabés ?", ["La Côte d'Ivoire", "L'Islande", "Le Japon", "La Mongolie"], "La Côte d'Ivoire", "Pour les plantations de cacao et l'économie urbaine."),
  Q("Pourquoi les migrations entre pays du Sud sont-elles si nombreuses ?", ["La proximité, le coût réduit et les liens culturels", "Parce que les pays du Nord sont fermés à toute migration", "Parce qu'elles sont obligatoires", "Elles sont rares"], "La proximité, le coût réduit et les liens culturels", "Elles représentent environ un tiers des migrations internationales."),
  Q("Quelle communauté économique permet la libre circulation des personnes en Afrique de l'Ouest ?", ["La CEDEAO", "L'Union européenne", "L'ALENA", "L'ASEAN"], "La CEDEAO", "Communauté économique des États de l'Afrique de l'Ouest."),
]),
notion('G4-2', 1, I, 'geo4i-flux-touristiques', [
  Q("D'où viennent la majorité des touristes internationaux ?", ["Des pays riches et émergents", "Des pays les moins avancés", "Uniquement d'Afrique", "Uniquement d'Océanie"], "Des pays riches et émergents", "Le tourisme suppose des revenus et des congés."),
  Q("Quel pays fournit le plus grand nombre de touristes internationaux en dépenses ?", ["La Chine", "Le Niger", "La Bolivie", "Le Laos"], "La Chine", "Ses touristes ont fortement augmenté depuis 2000."),
  Q("Quelle est la part de l'Europe dans les arrivées de touristes internationaux ?", ["Environ la moitié", "Environ 5 %", "Environ 90 %", "Environ 20 %"], "Environ la moitié", "Elle reste la première région touristique."),
]),
notion('G4-2', 1, I, 'geo4i-litoral-tourisme', [
  Q("Quelle mission d'aménagement a créé des stations comme La Grande-Motte dans les années 1960 ?", ["La mission Racine", "La DATAR seule", "Le plan Marshall", "La mission Marchand"], "La mission Racine", "Pour aménager le littoral du Languedoc-Roussillon."),
  Q("Quelle loi de 1986 protège le littoral français de l'urbanisation excessive ?", ["La loi Littoral", "La loi Montagne", "La loi SRU", "La loi Ferry"], "La loi Littoral", "Elle interdit de construire dans la bande des 100 mètres hors zones urbanisées."),
  Q("Comment appelle-t-on la concentration des hommes et des activités sur les côtes ?", ["La littoralisation", "La périurbanisation", "La métropolisation", "La désertification"], "La littoralisation", "Le tourisme y contribue fortement."),
]),
notion('G4-2', 1, I, 'geo4i-tourisme-economie', [
  Q("Quelle part du PIB mondial représente le tourisme environ ?", ["Environ 10 %", "Environ 1 %", "Environ 50 %", "Environ 0,1 %"], "Environ 10 %", "C'est l'un des premiers secteurs d'emploi."),
  Q("Quel pays insulaire dépend très fortement du tourisme ?", ["Les Maldives", "Le Japon", "Le Royaume-Uni", "L'Islande"], "Les Maldives", "Le tourisme y représente une grande part du PIB."),
  Q("Quelle crise a fait s'effondrer le tourisme international en 2020 ?", ["La pandémie de Covid-19", "La crise de 1929", "Le choc pétrolier", "La chute du mur de Berlin"], "La pandémie de Covid-19", "Les arrivées ont chuté de près de 75 %."),
]),
notion('G4-2', 1, I, 'geo4i-tourisme-urbain', [
  Q("Quelle ville est l'une des plus visitées du monde par les touristes internationaux ?", ["Bangkok", "Oulan-Bator", "Niamey", "Reykjavik"], "Bangkok", "Avec Paris, Londres et Dubaï."),
  Q("Qu'est-ce qu'un « city break » ?", ["Un court séjour touristique dans une ville", "Une panne d'électricité", "Une grève des transports", "Une démolition"], "Un court séjour touristique dans une ville", "Les compagnies à bas coût l'ont développé."),
  Q("Quelles compagnies aériennes ont rendu les voyages moins chers en Europe ?", ["Les compagnies à bas coût (low cost)", "Les compagnies nationales seulement", "Les compagnies maritimes", "Les compagnies ferroviaires"], "Les compagnies à bas coût (low cost)", "Ryanair ou easyJet par exemple."),
]),
notion('G4-2', 1, I, 'geo4i-tourisme-durable', [
  Q("Qu'est-ce que le tourisme durable ?", ["Un tourisme qui limite ses effets sur l'environnement et profite aux populations locales", "Un tourisme qui dure longtemps", "Un tourisme de luxe", "Un tourisme sans voyage"], "Un tourisme qui limite ses effets sur l'environnement et profite aux populations locales", "Il veut concilier visite et préservation."),
  Q("Quel moyen de voyager est le plus émetteur de CO2 par kilomètre ?", ["L'avion", "Le train", "Le vélo", "Le car"], "L'avion", "Le train est bien moins émetteur."),
  Q("Quel pays d'Amérique centrale est réputé pour son écotourisme ?", ["Le Costa Rica", "Le Mexique", "Le Panama", "Le Honduras"], "Le Costa Rica", "Une grande partie de son territoire est protégée."),
]),
notion('G4-2', 1, I, 'geo4i-pelerinages-religieux', [
  Q("Quel pèlerinage rassemble chaque année des millions de musulmans en Arabie saoudite ?", ["Le hajj, à La Mecque", "Le pèlerinage de Lourdes", "Le Kumbh Mela", "Saint-Jacques-de-Compostelle"], "Le hajj, à La Mecque", "C'est l'un des piliers de l'islam."),
  Q("Quelle ville française accueille chaque année des millions de pèlerins catholiques ?", ["Lourdes", "Nice", "Lille", "Brest"], "Lourdes", "C'est l'une des premières villes hôtelières de France."),
  Q("Quel rassemblement hindou, au bord du Gange, réunit parfois plusieurs dizaines de millions de personnes ?", ["La Kumbh Mela", "Le hajj", "Le Ramadan", "Le pèlerinage de Fatima"], "La Kumbh Mela", "C'est le plus grand rassemblement humain du monde."),
]),
# ══ Avancé ══
notion('G4-2', 0, D, 'geo4d-transferts-fonds', [
  Q("Quel montant représentent environ les envois de fonds des migrants vers les pays à revenu faible et intermédiaire ?", ["Plus de 650 milliards de dollars par an", "Environ 1 milliard", "Environ 50 millions", "Plus de 100 000 milliards"], "Plus de 650 milliards de dollars par an", "C'est plus que l'aide publique au développement."),
  Q("Dans quel pays les envois des émigrés représentent-ils plus d'un quart du PIB ?", ["Le Tadjikistan (ou le Népal)", "La France", "Les États-Unis", "L'Allemagne"], "Le Tadjikistan (ou le Népal)", "Ces pays dépendent fortement de leurs émigrés."),
  Q("Comment appelle-t-on le départ à l'étranger de personnes très qualifiées ?", ["La fuite des cerveaux", "L'exode rural", "Le regroupement familial", "Le tourisme d'affaires"], "La fuite des cerveaux", "Elle prive les pays d'origine de compétences."),
]),
notion('G4-2', 0, D, 'geo4d-politiques-migratoires', [
  Q("Quel accord européen de 2024 réforme la gestion de l'asile et des migrations ?", ["Le pacte sur la migration et l'asile", "Le traité de Rome", "L'accord de Paris", "La convention de Genève"], "Le pacte sur la migration et l'asile", "Il entre en application en 2026."),
  Q("Quel règlement européen désigne en principe le pays de première entrée comme responsable de la demande d'asile ?", ["Le règlement de Dublin", "Le règlement de Maastricht", "Le traité de Lisbonne", "Le code Schengen"], "Le règlement de Dublin", "Il fait peser une forte charge sur l'Italie et la Grèce."),
  Q("Quel pays a signé un accord en 2016 avec l'UE pour retenir les migrants sur son territoire contre une aide financière ?", ["La Turquie", "Le Maroc", "La Norvège", "La Suisse"], "La Turquie", "L'UE a promis 6 milliards d'euros."),
]),
notion('G4-2', 0, D, 'geo4d-diasporas', [
  Q("Quelle diaspora est très présente en Asie du Sud-Est, où elle joue un grand rôle économique ?", ["La diaspora chinoise", "La diaspora islandaise", "La diaspora suisse", "La diaspora finlandaise"], "La diaspora chinoise", "On parle de « Chinois d'outre-mer »."),
  Q("Quel pays compte plus de descendants d'émigrés à l'étranger que d'habitants sur son sol ?", ["L'Irlande", "La Chine", "L'Inde", "La Russie"], "L'Irlande", "Plus de 30 millions d'Américains se disent d'origine irlandaise."),
  Q("Quelle diaspora, dispersée après le génocide de 1915, est très présente en France ?", ["La diaspora arménienne", "La diaspora japonaise", "La diaspora norvégienne", "La diaspora coréenne"], "La diaspora arménienne", "Charles Aznavour en est une figure."),
]),
notion('G4-2', 0, D, 'geo4d-migrations-europe-histoire', [
  Q("Quel continent était un continent d'émigration massive au XIXe siècle ?", ["L'Europe", "L'Afrique", "L'Océanie", "L'Antarctique"], "L'Europe", "Environ 50 millions d'Européens sont partis vers les Amériques."),
  Q("À partir de quand l'Europe devient-elle surtout un continent d'immigration ?", ["Après 1945, avec la reconstruction et les Trente Glorieuses", "Au Moyen Âge", "Au XVIIIe siècle", "Après 2020 seulement"], "Après 1945, avec la reconstruction et les Trente Glorieuses", "Les pays industrialisés recrutent des travailleurs."),
  Q("Quel accord de 1961 organise la venue de travailleurs turcs en Allemagne ?", ["Un accord de recrutement de main-d'œuvre", "Le traité de Rome", "L'accord de Schengen", "Le pacte de Varsovie"], "Un accord de recrutement de main-d'œuvre", "Les « Gastarbeiter » devaient être temporaires."),
]),
notion('G4-2', 0, D, 'geo4d-migrants-morts', [
  Q("Combien de migrants environ sont morts ou disparus en Méditerranée depuis 2014 selon l'OIM ?", ["Plus de 30 000", "Environ 300", "Environ 3 000", "Aucun"], "Plus de 30 000", "C'est la route migratoire la plus meurtrière du monde."),
  Q("Quelle organisation intergouvernementale suit les migrations et compte les migrants disparus ?", ["L'OIM (Organisation internationale pour les migrations)", "L'OMC", "L'OPEP", "L'OCDE"], "L'OIM (Organisation internationale pour les migrations)", "Elle est rattachée à l'ONU depuis 2016."),
  Q("Quels navires d'ONG secourent les migrants en Méditerranée ?", ["Des navires humanitaires comme l'Ocean Viking", "Des paquebots de croisière", "Des sous-marins militaires", "Des cargos de céréales"], "Des navires humanitaires comme l'Ocean Viking", "Le droit de la mer impose de porter secours."),
]),
notion('G4-2', 0, D, 'geo4d-mobilites-qualifiees', [
  Q("Comment appelle-t-on une personne envoyée par son entreprise travailler à l'étranger ?", ["Un expatrié", "Un réfugié", "Un frontalier", "Un déplacé"], "Un expatrié", "Ce sont des migrations souvent valorisées."),
  Q("Quel pays recrute de nombreux informaticiens indiens grâce à un visa spécial (H-1B) ?", ["Les États-Unis", "Le Népal", "Le Bangladesh", "Le Mali"], "Les États-Unis", "Surtout dans la Silicon Valley."),
  Q("Quel dispositif européen facilite la venue de travailleurs hautement qualifiés ?", ["La carte bleue européenne", "Le passe Navigo", "La carte Vitale", "Le permis à points"], "La carte bleue européenne", "Elle est créée en 2009."),
]),
notion('G4-2', 0, D, 'geo4d-calais-mayotte', [
  Q("Quelle ville française est un point de passage de migrants qui veulent rejoindre le Royaume-Uni ?", ["Calais", "Marseille", "Strasbourg", "Bordeaux"], "Calais", "La « jungle » de Calais a été démantelée en 2016."),
  Q("Quel département français d'outre-mer connaît une très forte immigration irrégulière venue des Comores ?", ["Mayotte", "La Martinique", "La Réunion", "Saint-Pierre-et-Miquelon"], "Mayotte", "Les traversées se font en kwassa-kwassa."),
  Q("Quelle réforme a été adoptée en 2025 pour Mayotte ?", ["Un durcissement du droit du sol", "La suppression de la préfecture", "L'indépendance", "La fin du statut de département"], "Un durcissement du droit du sol", "Les deux parents doivent désormais être en situation régulière depuis plus d'un an."),
]),
notion('G4-2', 0, D, 'geo4d-stats-migrants', [
  Q("Quelle part de la population mondiale est constituée de migrants internationaux ?", ["Environ 3,7 %", "Environ 30 %", "Environ 0,1 %", "Environ 50 %"], "Environ 3,7 %", "Soit environ 300 millions de personnes."),
  Q("Quelle est la définition d'un migrant international pour l'ONU ?", ["Une personne qui vit hors de son pays de naissance depuis au moins un an", "Un touriste de passage", "Une personne qui déménage dans sa ville", "Un étudiant Erasmus de trois jours"], "Une personne qui vit hors de son pays de naissance depuis au moins un an", "Les touristes ne sont pas des migrants."),
  Q("Quelle différence y a-t-il entre un immigré et un étranger en France ?", ["Un immigré est né étranger à l'étranger ; un étranger n'a pas la nationalité française", "Il n'y en a aucune", "Un étranger est forcément immigré", "Un immigré ne peut jamais devenir français"], "Un immigré est né étranger à l'étranger ; un étranger n'a pas la nationalité française", "Un immigré naturalisé n'est plus étranger."),
]),
notion('G4-2', 1, D, 'geo4d-tourisme-mondialisation', [
  Q("Environ combien d'arrivées de touristes internationaux ont été comptées en 2024 ?", ["Environ 1,4 milliard", "Environ 140 millions", "Environ 14 milliards", "Environ 14 millions"], "Environ 1,4 milliard", "Le niveau d'avant la pandémie est retrouvé."),
  Q("Quel organisme de l'ONU suit le tourisme mondial ?", ["ONU Tourisme (ex-OMT)", "L'OMS", "L'Unesco", "Le PNUD"], "ONU Tourisme (ex-OMT)", "Son siège est à Madrid."),
  Q("Pourquoi dit-on que le tourisme est un facteur de mondialisation ?", ["Il met en relation des lieux et des sociétés du monde entier", "Il ferme les frontières", "Il réduit les échanges", "Il ne concerne qu'un pays"], "Il met en relation des lieux et des sociétés du monde entier", "Les flux touristiques sont des flux mondiaux."),
]),
notion('G4-2', 1, D, 'geo4d-surtourisme-mesures', [
  Q("Quelle ville espagnole a vu des manifestations d'habitants contre le surtourisme en 2024 ?", ["Barcelone", "Madrid", "Burgos", "Tolède"], "Barcelone", "Les habitants dénoncent la hausse des loyers."),
  Q("Quelle mesure Amsterdam a-t-elle prise contre le surtourisme ?", ["Limiter les nouveaux hôtels et augmenter la taxe de séjour", "Construire de nouveaux aéroports", "Supprimer la taxe de séjour", "Interdire les vélos"], "Limiter les nouveaux hôtels et augmenter la taxe de séjour", "La ville veut réduire les nuitées."),
  Q("Quelle calanque près de Marseille impose une réservation l'été pour limiter la fréquentation ?", ["La calanque de Sugiton", "La calanque de Porto", "La calanque de Piana", "Aucune"], "La calanque de Sugiton", "C'est une mesure du parc national des Calanques."),
]),
notion('G4-2', 1, D, 'geo4d-enclaves-touristiques', [
  Q("Comment appelle-t-on un espace touristique fermé, coupé de la population locale ?", ["Une enclave touristique", "Un quartier populaire", "Un front pionnier", "Une ZEE"], "Une enclave touristique", "Les clubs « tout compris » en sont un exemple."),
  Q("Quelle station mexicaine a été créée de toutes pièces pour le tourisme dans les années 1970 ?", ["Cancún", "Mexico", "Guadalajara", "Monterrey"], "Cancún", "Elle est sur la péninsule du Yucatán."),
  Q("Pourquoi les retombées économiques du tourisme profitent-elles parfois peu aux habitants ?", ["Les hôtels appartiennent souvent à des groupes étrangers et importent leurs produits", "Les touristes ne dépensent rien", "Le tourisme est gratuit", "Les habitants refusent l'argent"], "Les hôtels appartiennent souvent à des groupes étrangers et importent leurs produits", "On parle de « fuites » économiques."),
]),
notion('G4-2', 1, D, 'geo4d-tourisme-memoire', [
  Q("Comment appelle-t-on le tourisme sur les lieux de mémoire (champs de bataille, camps) ?", ["Le tourisme de mémoire", "Le tourisme balnéaire", "Le tourisme d'affaires", "Le tourisme spatial"], "Le tourisme de mémoire", "Les plages du Débarquement en Normandie en sont un exemple."),
  Q("Quel mémorial de la Somme accueille de nombreux visiteurs britanniques et du Commonwealth ?", ["Le mémorial de Thiepval", "Le Panthéon", "Le Louvre", "Versailles"], "Le mémorial de Thiepval", "Il porte les noms de plus de 72 000 soldats disparus."),
  Q("Quel ancien camp nazi est le lieu de mémoire le plus visité de Pologne ?", ["Auschwitz-Birkenau", "Dachau", "Drancy", "Buchenwald"], "Auschwitz-Birkenau", "Plus d'1,5 million de visiteurs par an."),
]),
notion('G4-2', 1, D, 'geo4d-tourisme-spatial-extremes', [
  Q("Quel continent, protégé par un traité de 1959, voit croître un tourisme de croisière ?", ["L'Antarctique", "L'Europe", "L'Asie", "L'Afrique"], "L'Antarctique", "Plus de 100 000 visiteurs par saison."),
  Q("Quel sommet attire chaque année des centaines d'alpinistes, avec des embouteillages près du sommet ?", ["L'Everest", "Le mont Blanc", "Le Kilimandjaro", "L'Aconcagua"], "L'Everest", "Le Népal délivre des permis coûteux."),
  Q("Comment appelle-t-on le fait de voyager pour se faire soigner dans un autre pays ?", ["Le tourisme médical", "Le tourisme vert", "Le tourisme de mémoire", "Le tourisme balnéaire"], "Le tourisme médical", "La Thaïlande et la Turquie en sont des destinations."),
]),
notion('G4-2', 1, D, 'geo4d-plateformes-locations', [
  Q("Quelle plateforme de location entre particuliers a transformé le tourisme urbain ?", ["Airbnb", "Wikipédia", "Pronote", "Doctolib"], "Airbnb", "Elle est créée en 2008 à San Francisco."),
  Q("Combien de nuits par an une résidence principale peut-elle être louée en meublé de tourisme à Paris ?", ["90 nuits", "365 nuits", "10 nuits", "Aucune"], "90 nuits", "La limite a été abaissée de 120 à 90 nuits en 2025."),
  Q("Pourquoi des villes limitent-elles les meublés de tourisme ?", ["Ils retirent des logements du marché et font monter les loyers", "Ils sont trop bon marché", "Ils attirent trop peu de touristes", "Ils sont interdits par l'ONU"], "Ils retirent des logements du marché et font monter les loyers", "La loi « Le Meur » de 2024 renforce les pouvoirs des maires."),
]),
notion('G4-2', 1, D, 'geo4d-mise-en-tourisme', [
  Q("Comment appelle-t-on le processus par lequel un lieu devient touristique ?", ["La mise en tourisme (touristification)", "La désindustrialisation", "La métropolisation", "L'exode rural"], "La mise en tourisme (touristification)", "Il transforme les paysages et l'économie."),
  Q("Quelle ville du Monténégro, inscrite à l'Unesco, est submergée par les croisiéristes ?", ["Kotor", "Podgorica", "Belgrade", "Sarajevo"], "Kotor", "Comme Dubrovnik en Croatie."),
  Q("Quelle série télévisée a fortement accru le tourisme à Dubrovnik ?", ["Game of Thrones", "Friends", "Les Simpson", "Breaking Bad"], "Game of Thrones", "On parle de « set-jetting » ou ciné-tourisme."),
]),
]

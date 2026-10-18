# Géographie 5e · L'environnement, du local au planétaire : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G5-3', 0, F, 'geo5-effet-serre', [
  Q("Qu'est-ce que l'effet de serre ?", ["Un phénomène naturel qui retient une partie de la chaleur du Soleil dans l'atmosphère", "Une technique de jardinage uniquement", "La pollution des rivières", "Un trou dans la couche d'ozone"], "Un phénomène naturel qui retient une partie de la chaleur du Soleil dans l'atmosphère", "Sans lui, la Terre serait glacée (environ -18 °C)."),
  Q("Pourquoi l'effet de serre se renforce-t-il ?", ["À cause des gaz rejetés par les activités humaines", "À cause des volcans uniquement", "À cause de la Lune", "Il ne se renforce pas"], "À cause des gaz rejetés par les activités humaines", "Transports, industrie, chauffage, agriculture…"),
  Q("Quel gaz, émis notamment par l'élevage des ruminants, renforce l'effet de serre ?", ["Le méthane", "L'oxygène", "L'azote", "L'hélium"], "Le méthane", "Il est bien plus réchauffant que le CO2, mais dure moins longtemps."),
]),
notion('G5-3', 0, F, 'geo5-climat-meteo', [
  Q("Quelle différence y a-t-il entre la météo et le climat ?", ["La météo décrit le temps d'un jour ; le climat, les moyennes sur au moins 30 ans", "Ce sont deux mots identiques", "Le climat change chaque jour", "La météo dure 30 ans"], "La météo décrit le temps d'un jour ; le climat, les moyennes sur au moins 30 ans", "Un hiver froid ne contredit pas le réchauffement."),
  Q("De combien la température moyenne mondiale a-t-elle augmenté depuis l'époque préindustrielle ?", ["D'environ 1,2 à 1,5 °C", "De 10 °C", "De 0,01 °C", "Elle a baissé"], "D'environ 1,2 à 1,5 °C", "2024 a été l'année la plus chaude jamais mesurée."),
  Q("Quel graphique présente les températures et les précipitations moyennes d'un lieu ?", ["Le diagramme ombrothermique (climatique)", "La pyramide des âges", "Le croquis", "Le plan de ville"], "Le diagramme ombrothermique (climatique)", "Les barres sont les pluies, la courbe les températures."),
]),
notion('G5-3', 0, F, 'geo5-canicules', [
  Q("Qu'est-ce qu'une canicule ?", ["Une période de très fortes chaleurs le jour et la nuit, durant plusieurs jours", "Une pluie violente", "Une tempête de neige", "Un séisme"], "Une période de très fortes chaleurs le jour et la nuit, durant plusieurs jours", "Elles sont plus fréquentes avec le réchauffement."),
  Q("Quelle canicule a fait environ 15 000 morts en France en 2003 ?", ["La canicule d'août 2003", "La canicule de 1789", "La canicule de 1950", "Aucune"], "La canicule d'août 2003", "Les personnes âgées ont été les plus touchées."),
  Q("Quel conseil donne-t-on pendant une canicule ?", ["Boire régulièrement et rester au frais", "Faire du sport en plein soleil", "Fermer les volets la nuit et les ouvrir le jour", "Boire de l'alcool"], "Boire régulièrement et rester au frais", "Il faut aussi prendre des nouvelles des personnes isolées."),
]),
notion('G5-3', 0, F, 'geo5-banquise-ours', [
  Q("Qu'est-ce que la banquise ?", ["De l'eau de mer gelée flottant dans les régions polaires", "Un glacier de montagne", "Une île", "Un iceberg en Afrique"], "De l'eau de mer gelée flottant dans les régions polaires", "Elle recule fortement en Arctique."),
  Q("Quel animal est menacé par la fonte de la banquise arctique ?", ["L'ours polaire", "Le lion", "Le kangourou", "Le chameau"], "L'ours polaire", "Il chasse les phoques sur la banquise."),
  Q("La fonte de la banquise fait-elle monter le niveau des mers ?", ["Très peu, car elle flotte déjà ; ce sont surtout les glaciers terrestres qui le font monter", "Oui, de plusieurs mètres", "Elle le fait baisser", "Oui, chaque jour de 1 mètre"], "Très peu, car elle flotte déjà ; ce sont surtout les glaciers terrestres qui le font monter", "Comme un glaçon qui fond dans un verre."),
]),
notion('G5-3', 0, F, 'geo5-gestes-climat', [
  Q("Lequel de ces gestes réduit les émissions de gaz à effet de serre ?", ["Prendre les transports en commun plutôt que la voiture", "Prendre l'avion pour un court trajet", "Laisser le chauffage allumé fenêtres ouvertes", "Acheter beaucoup de vêtements neufs"], "Prendre les transports en commun plutôt que la voiture", "Les transports sont le premier poste d'émissions en France."),
  Q("Pourquoi planter des arbres aide-t-il à lutter contre le réchauffement ?", ["Les arbres absorbent du CO2 en grandissant", "Ils produisent du pétrole", "Ils refroidissent le Soleil", "Ils ne servent à rien"], "Les arbres absorbent du CO2 en grandissant", "Les forêts sont des puits de carbone."),
  Q("Qu'est-ce que l'empreinte carbone ?", ["La quantité de gaz à effet de serre émise par nos activités", "La trace de nos chaussures", "Le nombre d'arbres d'un pays", "La quantité de charbon d'une mine"], "La quantité de gaz à effet de serre émise par nos activités", "Celle d'un Français est d'environ 9 tonnes par an."),
]),
notion('G5-3', 0, F, 'geo5-cop', [
  Q("Comment s'appellent les grandes conférences annuelles de l'ONU sur le climat ?", ["Les COP", "Les JO", "Les G7", "Les ODD"], "Les COP", "COP signifie « conférence des parties »."),
  Q("Dans quelle ville a été signé l'accord de 2015 sur le climat ?", ["Paris", "Kyoto", "Rio de Janeiro", "New York"], "Paris", "C'était la COP21."),
  Q("Quel objectif fixe l'accord de Paris ?", ["Limiter le réchauffement bien en dessous de 2 °C, si possible à 1,5 °C", "Augmenter la température de 3 °C", "Supprimer tous les nuages", "Arrêter les saisons"], "Limiter le réchauffement bien en dessous de 2 °C, si possible à 1,5 °C", "Par rapport à l'ère préindustrielle."),
]),
notion('G5-3', 1, F, 'geo5-seismes', [
  Q("Qu'est-ce qu'un séisme ?", ["Un tremblement de terre", "Une éruption volcanique", "Une inondation", "Une tempête"], "Un tremblement de terre", "Il est dû aux mouvements des plaques."),
  Q("Quelle échelle mesure l'énergie (la magnitude) d'un séisme ?", ["L'échelle de Richter", "L'échelle de Beaufort", "L'échelle de Celsius", "L'échelle de Saffir-Simpson"], "L'échelle de Richter", "L'échelle de Beaufort mesure le vent."),
  Q("Quel réflexe adopter pendant un séisme si l'on est dans un bâtiment ?", ["S'abriter sous une table solide, loin des fenêtres", "Prendre l'ascenseur", "Courir dans l'escalier", "Se mettre à la fenêtre"], "S'abriter sous une table solide, loin des fenêtres", "Il ne faut sortir qu'après les secousses."),
]),
notion('G5-3', 1, F, 'geo5-inondations', [
  Q("Qu'est-ce qu'une crue ?", ["La montée du niveau d'un cours d'eau", "La baisse d'une rivière", "Un séisme", "Une sécheresse"], "La montée du niveau d'un cours d'eau", "Elle peut provoquer une inondation."),
  Q("Quel est le premier risque naturel en France ?", ["L'inondation", "Le séisme", "L'éruption volcanique", "Le tsunami"], "L'inondation", "Une commune sur trois y est exposée."),
  Q("Pourquoi l'urbanisation aggrave-t-elle les inondations ?", ["Les sols bétonnés empêchent l'eau de s'infiltrer", "Les villes attirent la pluie", "Les immeubles bloquent les nuages", "Elle ne les aggrave pas"], "Les sols bétonnés empêchent l'eau de s'infiltrer", "On parle d'imperméabilisation des sols."),
]),
notion('G5-3', 1, F, 'geo5-volcans', [
  Q("Comment appelle-t-on la roche en fusion qui sort d'un volcan ?", ["La lave", "Le sable", "La glace", "Le calcaire"], "La lave", "Sous terre, on parle de magma."),
  Q("Quel volcan italien a détruit Pompéi en 79 ?", ["Le Vésuve", "L'Etna", "Le Stromboli", "Le Piton de la Fournaise"], "Le Vésuve", "Il menace toujours la région de Naples."),
  Q("Pourquoi de nombreuses personnes vivent-elles près des volcans malgré le danger ?", ["Les sols volcaniques sont très fertiles", "Il y fait toujours frais", "C'est obligatoire", "Il n'y a aucun danger"], "Les sols volcaniques sont très fertiles", "C'est le cas à Java ou autour de l'Etna."),
]),
notion('G5-3', 1, F, 'geo5-cyclones', [
  Q("Comment appelle-t-on une violente tempête tropicale, avec des vents très forts ?", ["Un cyclone (ouragan, typhon)", "Une averse", "Une canicule", "Une avalanche"], "Un cyclone (ouragan, typhon)", "Le nom change selon l'océan."),
  Q("Quel ouragan a dévasté La Nouvelle-Orléans en 2005 ?", ["Katrina", "Irma", "Sandy", "Chido"], "Katrina", "Les digues ont cédé et la ville a été inondée."),
  Q("Quel cyclone a dévasté Mayotte en décembre 2024 ?", ["Chido", "Katrina", "Irma", "Xynthia"], "Chido", "C'est le plus violent qu'ait connu l'île depuis près d'un siècle."),
]),
notion('G5-3', 1, F, 'geo5-alerte-risques', [
  Q("Quel service prévient la population des dangers météorologiques en France ?", ["Météo-France avec la vigilance météo", "La SNCF", "La Poste", "Le ministère de la Culture"], "Météo-France avec la vigilance météo", "Les niveaux vont du vert au rouge."),
  Q("Quelle couleur de vigilance météo signale un danger exceptionnel ?", ["Rouge", "Vert", "Jaune", "Bleu"], "Rouge", "Il faut alors suivre strictement les consignes."),
  Q("Pourquoi fait-on des exercices d'évacuation à l'école ?", ["Pour savoir quoi faire en cas de danger", "Pour se reposer", "Pour sortir plus tôt", "Pour le sport uniquement"], "Pour savoir quoi faire en cas de danger", "Les bons réflexes sauvent des vies."),
]),
notion('G5-3', 0, F, 'geo5-biodiversite', [
  Q("Qu'est-ce que la biodiversité ?", ["La diversité des êtres vivants et des milieux", "Le nombre d'habitants d'une ville", "La quantité de pétrole", "La diversité des langues"], "La diversité des êtres vivants et des milieux", "Elle est menacée par les activités humaines."),
  Q("Quel milieu terrestre abrite la plus grande biodiversité ?", ["La forêt tropicale humide", "Le désert", "La banquise", "La toundra"], "La forêt tropicale humide", "L'Amazonie en est le plus grand exemple."),
  Q("Quelle est une cause majeure de la perte de biodiversité ?", ["La destruction des milieux naturels", "La création de parcs nationaux", "La protection des espèces", "Le recyclage"], "La destruction des milieux naturels", "Déforestation, urbanisation, pollution…"),
]),
# ══ Intermédiaire ══
notion('G5-3', 0, I, 'geo5i-giec-rapports', [
  Q("Que conclut le GIEC sur l'origine du réchauffement actuel ?", ["Il est sans équivoque dû aux activités humaines", "Il est dû uniquement au Soleil", "Il n'existe pas", "Il est dû aux volcans"], "Il est sans équivoque dû aux activités humaines", "Ce constat figure dans son 6e rapport (2021-2023)."),
  Q("Qui sont les membres du GIEC ?", ["Des scientifiques du monde entier qui synthétisent les recherches", "Des militaires", "Des chefs d'entreprise", "Des sportifs"], "Des scientifiques du monde entier qui synthétisent les recherches", "Il est créé en 1988."),
  Q("Quel prix le GIEC a-t-il reçu en 2007 ?", ["Le prix Nobel de la paix", "La Palme d'or", "Le Ballon d'or", "Le prix Goncourt"], "Le prix Nobel de la paix", "Partagé avec Al Gore."),
]),
notion('G5-3', 0, I, 'geo5i-montee-mers', [
  Q("Quelles sont les deux causes principales de la montée du niveau des océans ?", ["La fonte des glaciers terrestres et la dilatation de l'eau qui se réchauffe", "La pluie et le vent", "Les volcans et les séismes", "Les bateaux et les ports"], "La fonte des glaciers terrestres et la dilatation de l'eau qui se réchauffe", "L'eau chaude occupe plus de place."),
  Q("De combien le niveau des mers a-t-il monté environ depuis 1900 ?", ["Environ 20 cm", "Environ 2 m", "Environ 2 mm", "Il a baissé"], "Environ 20 cm", "La montée s'accélère."),
  Q("Quel pays a signé en 2023 un accord avec l'Australie pour accueillir ses habitants menacés par la montée des eaux ?", ["Tuvalu", "La Suisse", "Le Népal", "La Mongolie"], "Tuvalu", "C'est un petit archipel du Pacifique."),
]),
notion('G5-3', 0, I, 'geo5i-climat-france', [
  Q("Quelle région française est particulièrement exposée à l'érosion des côtes ?", ["La côte aquitaine (dunes)", "L'Alsace", "La Bourgogne", "L'Auvergne"], "La côte aquitaine (dunes)", "L'immeuble Le Signal, à Soulac-sur-Mer, a dû être démoli."),
  Q("Quel effet le réchauffement a-t-il sur les stations de ski de moyenne montagne ?", ["Le manque de neige menace leur activité", "Elles ont plus de neige", "Aucun effet", "Elles deviennent des stations balnéaires"], "Le manque de neige menace leur activité", "Certaines ferment ou se diversifient."),
  Q("Quel effet le réchauffement a-t-il sur les vendanges en France ?", ["Elles ont lieu de plus en plus tôt", "Elles ont lieu plus tard", "Elles n'ont plus lieu", "Aucun effet"], "Elles ont lieu de plus en plus tôt", "Elles ont avancé d'environ trois semaines en 50 ans."),
]),
notion('G5-3', 0, I, 'geo5i-emetteurs', [
  Q("Quel pays émet le plus de CO2 aujourd'hui ?", ["La Chine", "La France", "Le Brésil", "L'Inde"], "La Chine", "Elle émet environ 30 % du total mondial."),
  Q("Quel pays a émis le plus de CO2 au total depuis le début de l'ère industrielle ?", ["Les États-Unis", "La Chine", "La France", "Le Japon"], "Les États-Unis", "On parle d'émissions cumulées ou historiques."),
  Q("Pourquoi les pays du Sud réclament-ils une « justice climatique » ?", ["Ils ont peu émis mais subissent fortement les effets du réchauffement", "Ils émettent le plus", "Ils ne sont pas touchés", "Ils veulent arrêter de produire"], "Ils ont peu émis mais subissent fortement les effets du réchauffement", "La COP27 a créé un fonds « pertes et dommages »."),
]),
notion('G5-3', 0, I, 'geo5i-deforestation', [
  Q("Quelle est la plus grande forêt tropicale du monde ?", ["L'Amazonie", "La forêt de Brocéliande", "La taïga sibérienne", "La forêt du Congo"], "L'Amazonie", "Elle s'étend sur neuf pays, surtout le Brésil."),
  Q("Pourquoi la déforestation aggrave-t-elle le changement climatique ?", ["Les arbres coupés ou brûlés relâchent leur carbone et n'en absorbent plus", "Les arbres produisent du pétrole", "Elle n'a aucun effet", "Elle refroidit la planète"], "Les arbres coupés ou brûlés relâchent leur carbone et n'en absorbent plus", "La déforestation représente environ 10 % des émissions."),
  Q("Quelle culture d'Asie du Sud-Est est une cause majeure de déforestation en Indonésie ?", ["Le palmier à huile", "Le blé", "La vigne", "La pomme de terre"], "Le palmier à huile", "L'orang-outan en est menacé."),
]),
notion('G5-3', 0, I, 'geo5i-adaptation-villes', [
  Q("Qu'est-ce qu'un îlot de chaleur urbain ?", ["Une zone de la ville plus chaude que la campagne autour, à cause du béton et de l'asphalte", "Une île tropicale", "Un quartier sans électricité", "Un parc très frais"], "Une zone de la ville plus chaude que la campagne autour, à cause du béton et de l'asphalte", "L'écart peut atteindre plusieurs degrés la nuit."),
  Q("Quelle solution rafraîchit les villes en été ?", ["Végétaliser : planter des arbres et créer des parcs", "Construire plus de parkings", "Goudronner les cours d'école", "Supprimer les fontaines"], "Végétaliser : planter des arbres et créer des parcs", "Paris transforme des cours d'école en « cours oasis »."),
  Q("Qu'est-ce qu'une « ville éponge » ?", ["Une ville aménagée pour absorber et stocker l'eau de pluie", "Une ville au bord de la mer", "Une ville sans pluie", "Une ville industrielle"], "Une ville aménagée pour absorber et stocker l'eau de pluie", "Le concept est développé en Chine."),
]),
notion('G5-3', 1, I, 'geo5i-alea-vulnerabilite', [
  Q("Comment se calcule simplement un risque en géographie ?", ["Risque = aléa × vulnérabilité (enjeux)", "Risque = population + superficie", "Risque = pluie − soleil", "Risque = PIB ÷ habitants"], "Risque = aléa × vulnérabilité (enjeux)", "Sans enjeux humains, il n'y a pas de risque."),
  Q("Pourquoi un même séisme fait-il plus de victimes dans un pays pauvre ?", ["Les bâtiments y sont moins solides et les secours moins organisés", "Les séismes y sont toujours plus forts", "Les habitants sont plus nombreux partout", "Ce n'est pas le cas"], "Les bâtiments y sont moins solides et les secours moins organisés", "Haïti en 2010 en est un exemple tragique."),
  Q("Quels sont les enjeux exposés à un risque ?", ["Les personnes, les biens, les activités et l'environnement", "Uniquement les arbres", "Uniquement les routes", "Les nuages"], "Les personnes, les biens, les activités et l'environnement", "Plus il y a d'enjeux, plus le risque est grand."),
]),
notion('G5-3', 1, I, 'geo5i-japon-risques', [
  Q("Pourquoi le Japon est-il très exposé aux séismes ?", ["Il se trouve à la rencontre de plusieurs plaques tectoniques", "Il est au milieu d'un continent", "Il est en Europe", "Il est près du pôle Sud"], "Il se trouve à la rencontre de plusieurs plaques tectoniques", "Il connaît des milliers de secousses par an."),
  Q("Comment le Japon se protège-t-il des séismes ?", ["Normes de construction parasismiques, alertes et exercices réguliers", "Il n'a aucune protection", "Il interdit les immeubles", "Il évacue tout le pays chaque année"], "Normes de construction parasismiques, alertes et exercices réguliers", "C'est un modèle de prévention."),
  Q("Comment appelle-t-on la vague géante provoquée par un séisme sous-marin ?", ["Un tsunami", "Un cyclone", "Une marée", "Une crue"], "Un tsunami", "Le mot est japonais."),
]),
notion('G5-3', 1, I, 'geo5i-risques-sanitaires', [
  Q("Comment appelle-t-on une maladie transmise de l'animal à l'humain ?", ["Une zoonose", "Une pandémie", "Une allergie", "Une épidémie saisonnière"], "Une zoonose", "Le Covid-19 en serait une."),
  Q("Pourquoi les épidémies se diffusent-elles plus vite aujourd'hui ?", ["À cause de l'intensité des déplacements dans le monde", "Parce que les virus sont plus gros", "Parce qu'il n'y a plus de médecins", "Elles se diffusent moins vite"], "À cause de l'intensité des déplacements dans le monde", "L'avion transporte les virus d'un continent à l'autre en quelques heures."),
  Q("Quel moustique, qui transmet la dengue, s'étend en France métropolitaine ?", ["Le moustique tigre", "Le moustique géant", "La mouche tsé-tsé", "Le frelon asiatique"], "Le moustique tigre", "Il est présent dans la majorité des départements."),
]),
notion('G5-3', 1, I, 'geo5i-feux-foret', [
  Q("Pourquoi les incendies de forêt sont-ils plus fréquents ?", ["Sécheresses et chaleurs plus intenses avec le réchauffement", "Il pleut davantage", "Les forêts sont plus humides", "Ils sont moins fréquents"], "Sécheresses et chaleurs plus intenses avec le réchauffement", "La plupart sont déclenchés par des activités humaines."),
  Q("Quelle région française a connu de très grands incendies en 2022 ?", ["La Gironde (forêt des Landes)", "L'Alsace", "La Normandie", "Paris"], "La Gironde (forêt des Landes)", "Plus de 30 000 hectares ont brûlé."),
  Q("Quel geste est interdit en forêt en été pour prévenir les incendies ?", ["Faire un barbecue ou jeter un mégot", "Se promener", "Ramasser des déchets", "Prendre des photos"], "Faire un barbecue ou jeter un mégot", "Les obligations de débroussaillement protègent aussi les maisons."),
]),
notion('G5-3', 1, I, 'geo5i-catnat', [
  Q("Que permet la reconnaissance de l'état de catastrophe naturelle en France ?", ["L'indemnisation des victimes par leur assurance", "L'interdiction de reconstruire", "L'évacuation de tout le pays", "La fermeture des écoles pour un an"], "L'indemnisation des victimes par leur assurance", "Elle est décidée par un arrêté interministériel."),
  Q("Qui déclenche le plan ORSEC en cas de catastrophe ?", ["Le préfet", "Le maire de Paris", "Le président de la région", "Le pompier le plus proche"], "Le préfet", "Il coordonne tous les secours du département."),
  Q("Qui est responsable de la sécurité des habitants dans sa commune ?", ["Le maire", "Le député", "Le sénateur", "Le président de la République"], "Le maire", "Il dispose de pouvoirs de police."),
]),
notion('G5-3', 1, I, 'geo5i-xynthia', [
  Q("Quelle tempête a provoqué une submersion marine meurtrière en Vendée en 2010 ?", ["Xynthia", "Lothar", "Katrina", "Chido"], "Xynthia", "Elle a fait 47 morts en France."),
  Q("Pourquoi Xynthia a-t-elle fait autant de victimes à La Faute-sur-Mer ?", ["Des maisons avaient été construites dans des zones basses derrière une digue", "La ville était en montagne", "Il n'y avait aucune habitation", "Parce qu'il faisait très chaud"], "Des maisons avaient été construites dans des zones basses derrière une digue", "Des centaines de maisons ont ensuite été détruites."),
  Q("Qu'est-ce qu'une submersion marine ?", ["L'inondation de terres littorales par la mer", "Une plongée sous-marine", "Une crue de rivière", "La fonte d'un glacier"], "L'inondation de terres littorales par la mer", "Elle combine tempête et forte marée."),
]),
notion('G5-3', 0, I, 'geo5i-aires-protegees', [
  Q("Combien de parcs nationaux compte la France ?", ["11", "3", "50", "100"], "11", "Le dernier créé est celui des Forêts, en 2019."),
  Q("Quel accord de 2022 vise à protéger 30 % des terres et des mers d'ici 2030 ?", ["Le cadre mondial de Kunming-Montréal sur la biodiversité", "L'accord de Paris", "Le protocole de Kyoto", "Le traité de Rome"], "Le cadre mondial de Kunming-Montréal sur la biodiversité", "On parle de l'objectif « 30x30 »."),
  Q("Qu'est-ce qu'une aire marine protégée ?", ["Un espace marin où les activités humaines sont encadrées pour protéger la nature", "Un port de commerce", "Une zone de pêche industrielle", "Une base militaire"], "Un espace marin où les activités humaines sont encadrées pour protéger la nature", "La France en possède de très vastes outre-mer."),
]),
notion('G5-3', 0, I, 'geo5i-pollution-plastique', [
  Q("Combien de tonnes de plastique environ finissent dans les océans chaque année ?", ["Plusieurs millions", "Quelques kilos", "Quelques tonnes", "Aucune"], "Plusieurs millions", "Ils se fragmentent en microplastiques."),
  Q("Qu'est-ce qu'un microplastique ?", ["Un fragment de plastique de moins de 5 mm", "Un sac plastique géant", "Un plastique biodégradable", "Un bouchon de bouteille"], "Un fragment de plastique de moins de 5 mm", "On en trouve jusque dans le sang humain."),
  Q("Depuis quand les sacs plastiques à usage unique sont-ils interdits en caisse en France ?", ["2016", "1990", "2030", "Ils ne le sont pas"], "2016", "D'autres objets jetables ont suivi."),
]),
# ══ Avancé ══
notion('G5-3', 0, D, 'geo5d-scenarios-giec', [
  Q("Selon le GIEC, quel réchauffement pourrait atteindre la planète en 2100 si les émissions restent très élevées ?", ["Environ +4 à +5 °C", "Environ +0,1 °C", "Environ +20 °C", "Un refroidissement"], "Environ +4 à +5 °C", "C'est le scénario le plus pessimiste."),
  Q("Quelle trajectoire de réchauffement la France prépare-t-elle pour son adaptation ?", ["+4 °C en France en 2100", "+1 °C en 2100", "Aucun réchauffement", "+10 °C en 2030"], "+4 °C en France en 2100", "C'est la trajectoire de référence (TRACC) adoptée en 2024-2025."),
  Q("Pourquoi la France se réchauffe-t-elle plus vite que la moyenne mondiale ?", ["Les continents se réchauffent plus vite que les océans", "Parce qu'elle est près de l'équateur", "Parce qu'elle a plus de volcans", "Ce n'est pas le cas"], "Les continents se réchauffent plus vite que les océans", "La France s'est réchauffée d'environ 1,7 °C."),
]),
notion('G5-3', 0, D, 'geo5d-permafrost', [
  Q("Qu'est-ce que le pergélisol (permafrost) ?", ["Un sol gelé en permanence depuis au moins deux ans", "Un glacier flottant", "Une neige fraîche", "Un sol désertique"], "Un sol gelé en permanence depuis au moins deux ans", "Il couvre une grande partie de la Sibérie et du Canada."),
  Q("Pourquoi le dégel du pergélisol inquiète-t-il les climatologues ?", ["Il libère du méthane et du CO2, ce qui aggrave le réchauffement", "Il refroidit la planète", "Il crée des océans", "Il n'a aucun effet"], "Il libère du méthane et du CO2, ce qui aggrave le réchauffement", "C'est une boucle de rétroaction."),
  Q("Qu'appelle-t-on un « point de bascule » climatique ?", ["Un seuil au-delà duquel un système change brutalement et durablement", "Un panneau routier", "Un sommet de montagne", "Une saison"], "Un seuil au-delà duquel un système change brutalement et durablement", "La fonte du Groenland ou de l'Amazonie en sont des exemples possibles."),
]),
notion('G5-3', 0, D, 'geo5d-refugies-climatiques', [
  Q("Pourquoi l'expression « réfugié climatique » n'a-t-elle pas de valeur juridique ?", ["La convention de Genève ne prend pas en compte les causes environnementales", "Parce qu'il n'y a pas de migrations climatiques", "Parce que l'ONU l'a interdite", "Parce qu'elle a été inventée en 2025"], "La convention de Genève ne prend pas en compte les causes environnementales", "On parle plutôt de « déplacés environnementaux »."),
  Q("Quel pays d'Asie est particulièrement menacé par la montée des eaux et les cyclones, avec un immense delta ?", ["Le Bangladesh", "La Mongolie", "Le Népal", "L'Afghanistan"], "Le Bangladesh", "Le delta du Gange et du Brahmapoutre est très bas."),
  Q("Où se font la majorité des déplacements liés aux catastrophes naturelles ?", ["À l'intérieur des pays", "Vers l'Europe", "Vers l'Antarctique", "Vers les États-Unis uniquement"], "À l'intérieur des pays", "Ce sont surtout des déplacés internes."),
]),
notion('G5-3', 0, D, 'geo5d-protocole-kyoto', [
  N("En quelle année est adopté le protocole de Kyoto ?", 1997, "Il fixe des objectifs de réduction aux pays industrialisés."),
  Q("Quelle conférence de 1992 a créé la convention-cadre des Nations unies sur le changement climatique ?", ["Le sommet de la Terre de Rio", "La COP21 de Paris", "La conférence de Yalta", "Le G20 de Londres"], "Le sommet de la Terre de Rio", "Les COP sont les réunions de cette convention."),
  Q("Quel pays s'est retiré à deux reprises de l'accord de Paris ?", ["Les États-Unis", "La France", "La Chine", "Le Royaume-Uni"], "Les États-Unis", "Sous les présidences de Donald Trump (2017 et 2025)."),
]),
notion('G5-3', 0, D, 'geo5d-marche-carbone', [
  Q("Qu'est-ce que le marché du carbone européen ?", ["Un système où les industries doivent acheter des quotas pour émettre du CO2", "Une foire au charbon", "Un marché de fruits", "Une bourse d'actions"], "Un système où les industries doivent acheter des quotas pour émettre du CO2", "Il est créé en 2005."),
  Q("Comment appelle-t-on le plan européen qui vise la neutralité climatique en 2050 ?", ["Le Pacte vert (Green Deal)", "Le plan Marshall", "La PAC", "Le plan Schuman"], "Le Pacte vert (Green Deal)", "Il est lancé en 2019."),
  Q("Quel mécanisme européen taxe le carbone des produits importés depuis 2026 ?", ["Le mécanisme d'ajustement carbone aux frontières", "Le Nutri-Score", "Le label bio", "La TVA sociale"], "Le mécanisme d'ajustement carbone aux frontières", "Il concerne l'acier, le ciment, l'aluminium…"),
]),
notion('G5-3', 0, D, 'geo5d-glaciers-alpes', [
  Q("Quel glacier, le plus grand de France, recule fortement depuis un siècle ?", ["La Mer de Glace", "Le glacier d'Aletsch", "Le Perito Moreno", "Le Vatnajökull"], "La Mer de Glace", "Il a perdu plus de 2 km de longueur."),
  Q("Quel risque le recul des glaciers fait-il peser sur les vallées ?", ["Des pénuries d'eau en été et des vidanges brutales de lacs glaciaires", "Plus de neige", "Des séismes", "Aucun"], "Des pénuries d'eau en été et des vidanges brutales de lacs glaciaires", "Les glaciers sont des châteaux d'eau."),
  Q("Quel pays est devenu en 2024 le premier pays d'Amérique du Sud à perdre tous ses glaciers ?", ["Le Venezuela", "Le Chili", "L'Argentine", "Le Pérou"], "Le Venezuela", "Le glacier Humboldt a été déclassé en champ de glace."),
]),
notion('G5-3', 0, D, 'geo5d-acidification', [
  Q("Pourquoi les océans s'acidifient-ils ?", ["Ils absorbent une partie du CO2 émis par les activités humaines", "À cause du sel", "À cause des poissons", "Ils ne s'acidifient pas"], "Ils absorbent une partie du CO2 émis par les activités humaines", "Environ un quart du CO2 émis."),
  Q("Quels écosystèmes marins sont menacés par le réchauffement et l'acidification ?", ["Les récifs coralliens", "Les déserts", "Les toundras", "Les steppes"], "Les récifs coralliens", "On parle de blanchissement des coraux."),
  Q("Quel grand récif australien subit des épisodes répétés de blanchissement ?", ["La Grande Barrière de corail", "Le lagon de Bora-Bora", "Les récifs de la mer du Nord", "La barrière de Tahiti"], "La Grande Barrière de corail", "C'est la plus grande structure vivante du monde."),
]),
notion('G5-3', 0, D, 'geo5d-sixieme-extinction', [
  Q("Quel organisme international établit la Liste rouge des espèces menacées ?", ["L'UICN", "L'OMS", "L'OMC", "L'OTAN"], "L'UICN", "Union internationale pour la conservation de la nature."),
  Q("Quel groupe d'experts, équivalent du GIEC pour la biodiversité, a été créé en 2012 ?", ["L'IPBES", "Le GIEC", "La FAO", "Le PNUE"], "L'IPBES", "Il estime qu'un million d'espèces sont menacées d'extinction."),
  Q("Pourquoi parle-t-on d'une « sixième extinction » ?", ["Les espèces disparaissent à un rythme comparable aux grandes crises du passé", "Il n'y a eu que six espèces sur Terre", "Six pays protègent la nature", "Six espèces ont disparu"], "Les espèces disparaissent à un rythme comparable aux grandes crises du passé", "La cinquième a vu disparaître les dinosaures."),
]),
notion('G5-3', 1, D, 'geo5d-seveso-lubrizol', [
  Q("Quel incendie d'usine chimique a frappé Rouen en 2019 ?", ["L'incendie de Lubrizol", "L'explosion d'AZF", "La catastrophe de Bhopal", "L'accident de Seveso"], "L'incendie de Lubrizol", "Un panache de fumée noire a recouvert l'agglomération."),
  Q("Dans quelle ville italienne un nuage de dioxine s'échappe-t-il d'une usine en 1976 ?", ["Seveso", "Milan", "Naples", "Venise"], "Seveso", "La directive européenne sur les sites dangereux porte son nom."),
  Q("Quelle explosion de nitrate d'ammonium a dévasté le port de Beyrouth en 2020 ?", ["L'explosion du 4 août 2020", "L'explosion d'AZF", "L'incendie de Lubrizol", "La catastrophe de Fukushima"], "L'explosion du 4 août 2020", "Elle a fait plus de 200 morts."),
]),
notion('G5-3', 1, D, 'geo5d-ppr', [
  Q("Que contient un plan de prévention des risques (PPR) ?", ["Des zones où l'on interdit ou encadre les constructions selon les risques", "Le budget de la commune", "Les horaires des écoles", "La liste des élus"], "Des zones où l'on interdit ou encadre les constructions selon les risques", "Les zones rouges sont inconstructibles."),
  Q("Quelle information doit être donnée à un acheteur ou un locataire depuis 2006 ?", ["L'état des risques auxquels le logement est exposé", "Le nombre de voisins", "La couleur des murs", "L'âge du propriétaire"], "L'état des risques auxquels le logement est exposé", "C'est l'information acquéreurs-locataires."),
  Q("Quel fonds finance des mesures de prévention des risques naturels (rachat de maisons exposées, travaux) ?", ["Le fonds Barnier", "Le fonds Marshall", "Le FMI", "Le fonds vert pour le climat"], "Le fonds Barnier", "Il porte le nom de Michel Barnier, ministre de l'Environnement en 1995."),
]),
notion('G5-3', 1, D, 'geo5d-haiti-2010', [
  N("En quelle année un séisme dévaste-t-il Port-au-Prince, en Haïti ?", 2010, "Il fait plus de 200 000 morts."),
  Q("Pourquoi le séisme d'Haïti a-t-il été si meurtrier ?", ["Une forte densité, des constructions fragiles et un État faible", "Une magnitude record de 10", "Une éruption volcanique simultanée", "Un tsunami géant"], "Une forte densité, des constructions fragiles et un État faible", "Un séisme de magnitude comparable fait peu de victimes au Japon."),
  Q("Quelle épidémie a suivi le séisme d'Haïti en 2010 ?", ["Le choléra", "La grippe espagnole", "La peste", "Le Covid-19"], "Le choléra", "Elle a été introduite par des Casques bleus."),
]),
notion('G5-3', 1, D, 'geo5d-resilience-reconstruction', [
  Q("Qu'est-ce qu'une culture du risque ?", ["La connaissance par la population des risques et des bons comportements", "Une culture agricole", "Une exposition d'art", "L'absence de prévention"], "La connaissance par la population des risques et des bons comportements", "Elle réduit la vulnérabilité."),
  Q("Que signifie « reconstruire mieux » (build back better) après une catastrophe ?", ["Reconstruire en réduisant la vulnérabilité, plutôt qu'à l'identique", "Reconstruire plus vite sans normes", "Ne rien reconstruire", "Reconstruire au même endroit sans changement"], "Reconstruire en réduisant la vulnérabilité, plutôt qu'à l'identique", "Le principe est adopté par l'ONU en 2015 (cadre de Sendai)."),
  Q("Quel cadre international de 2015 guide la réduction des risques de catastrophe ?", ["Le cadre de Sendai", "L'accord de Paris", "Le protocole de Kyoto", "Le traité de Lisbonne"], "Le cadre de Sendai", "Il est adopté au Japon."),
]),
notion('G5-3', 1, D, 'geo5d-risque-nucleaire', [
  Q("Quelle est la plus ancienne centrale nucléaire française arrêtée en 2020 ?", ["Fessenheim", "Flamanville", "Gravelines", "Tricastin"], "Fessenheim", "Elle se trouvait en Alsace."),
  Q("Quel comprimé est distribué aux habitants proches d'une centrale pour protéger la thyroïde ?", ["L'iode", "Le paracétamol", "La vitamine C", "Le fer"], "L'iode", "Il sature la thyroïde pour éviter l'iode radioactif."),
  Q("Quel organisme contrôle la sûreté nucléaire en France ?", ["L'Autorité de sûreté nucléaire et de radioprotection (ASNR)", "La CNIL", "Météo-France", "L'Insee"], "L'Autorité de sûreté nucléaire et de radioprotection (ASNR)", "Elle naît en 2025 de la fusion de l'ASN et de l'IRSN."),
]),
notion('G5-3', 1, D, 'geo5d-risques-montagne', [
  Q("Quel risque naturel menace les stations de ski et les randonneurs en hiver ?", ["Les avalanches", "Les tsunamis", "Les cyclones", "Les canicules"], "Les avalanches", "Un bulletin d'estimation du risque d'avalanche est publié chaque jour."),
  Q("Quel phénomène a enseveli une grande partie du village suisse de Blatten en mai 2025 ?", ["L'effondrement d'un glacier", "Un tsunami", "Une éruption volcanique", "Un cyclone"], "L'effondrement d'un glacier", "Le village avait été évacué à temps."),
  Q("Pourquoi les éboulements augmentent-ils en haute montagne ?", ["Le dégel du pergélisol fragilise les parois rocheuses", "Il y a plus de touristes", "Les montagnes grandissent", "Il neige davantage"], "Le dégel du pergélisol fragilise les parois rocheuses", "Le massif du Mont-Blanc est très touché."),
]),
notion('G5-3', 1, D, 'geo5d-une-seule-sante', [
  Q("Que désigne l'approche « Une seule santé » (One Health) ?", ["Le lien entre santé humaine, santé animale et santé des écosystèmes", "Un seul hôpital par pays", "Une seule maladie mondiale", "Un vaccin unique"], "Le lien entre santé humaine, santé animale et santé des écosystèmes", "La destruction des milieux favorise les zoonoses."),
  Q("Quelle épidémie a frappé l'Afrique de l'Ouest de 2014 à 2016, faisant plus de 11 000 morts ?", ["Ebola", "Le Covid-19", "La grippe aviaire", "La rougeole"], "Ebola", "La Guinée, la Sierra Leone et le Liberia ont été les plus touchés."),
  Q("Quelle ville chinoise est le point de départ connu de la pandémie de Covid-19 ?", ["Wuhan", "Pékin", "Shanghai", "Hong Kong"], "Wuhan", "Les premiers cas sont signalés fin 2019."),
]),
]

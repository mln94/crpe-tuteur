# Géographie 3e · Pourquoi et comment aménager le territoire ? : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('G3-2', 0, F, 'geo3-amenagements-exemples', [
  Q("Lequel de ces équipements est un aménagement ?", ["Une ligne de tramway", "Une forêt sauvage", "Un nuage", "Une montagne"], "Une ligne de tramway", "Un aménagement est une action volontaire sur un territoire."),
  Q("Pourquoi construit-on un pont ou un tunnel ?", ["Pour franchir un obstacle et relier des territoires", "Pour décorer", "Pour ralentir la circulation", "Pour isoler une ville"], "Pour franchir un obstacle et relier des territoires", "Le viaduc de Millau franchit la vallée du Tarn."),
  Q("Quel grand pont autoroutier, le plus haut du monde, se trouve dans l'Aveyron ?", ["Le viaduc de Millau", "Le pont de Normandie", "Le pont du Gard", "Le pont Neuf"], "Le viaduc de Millau", "Il est inauguré en 2004."),
]),
notion('G3-2', 0, F, 'geo3-acteurs-amenagement', [
  Q("Quel élu décide des aménagements de sa commune ?", ["Le maire, avec le conseil municipal", "Le président de la République", "Le pape", "Un député européen"], "Le maire, avec le conseil municipal", "Places, écoles, voirie…"),
  Q("Quelle collectivité organise les transports régionaux (TER) ?", ["La région", "La commune", "Le département", "L'Union européenne"], "La région", "Elle gère aussi les lycées."),
  Q("Qui peut s'opposer à un projet d'aménagement ?", ["Des habitants et des associations", "Personne", "Uniquement le maire", "Uniquement le préfet"], "Des habitants et des associations", "Les projets donnent souvent lieu à des débats."),
]),
notion('G3-2', 0, F, 'geo3-autoroutes', [
  Q("Quelle forme a le réseau autoroutier français ?", ["Une étoile centrée sur Paris", "Un cercle autour de Lyon", "Un carré", "Une ligne droite"], "Une étoile centrée sur Paris", "C'est l'héritage d'une organisation centralisée."),
  Q("Quelle autoroute relie Paris à Marseille par Lyon ?", ["L'A6 puis l'A7", "L'A1", "L'A10", "L'A13"], "L'A6 puis l'A7", "On l'appelle « l'autoroute du Soleil »."),
  Q("Pourquoi faut-il payer sur la plupart des autoroutes françaises ?", ["Elles sont gérées par des sociétés concessionnaires qui perçoivent un péage", "C'est une amende", "Pour payer les radars", "Elles sont gratuites"], "Elles sont gérées par des sociétés concessionnaires qui perçoivent un péage", "Certaines portions restent gratuites."),
]),
notion('G3-2', 0, F, 'geo3-tgv-reseau', [
  Q("Que signifie TGV ?", ["Train à grande vitesse", "Train grande voie", "Transport général de voyageurs", "Train gare-ville"], "Train à grande vitesse", "Il roule jusqu'à 320 km/h."),
  Q("Quel est l'effet du TGV sur les villes desservies ?", ["Elles sont rapprochées de Paris et des autres métropoles", "Elles s'éloignent", "Elles perdent tous leurs habitants", "Aucun effet"], "Elles sont rapprochées de Paris et des autres métropoles", "On mesure la distance en temps de trajet."),
  Q("Combien de temps faut-il environ pour aller de Paris à Lyon en TGV ?", ["Environ 2 heures", "Environ 8 heures", "Environ 30 minutes", "Environ 5 heures"], "Environ 2 heures", "Contre plus de 4 heures avant le TGV."),
]),
notion('G3-2', 0, F, 'geo3-inegalites-territoires', [
  Q("Quels territoires français sont souvent les plus riches ?", ["Les grandes métropoles et l'Île-de-France", "Les campagnes isolées", "Les anciens bassins miniers", "Les quartiers prioritaires"], "Les grandes métropoles et l'Île-de-France", "Elles concentrent les emplois qualifiés."),
  Q("Quels territoires connaissent souvent un fort chômage ?", ["Les anciennes régions industrielles et certains quartiers de banlieue", "Les centres des métropoles", "Les technopoles", "Les stations de ski de luxe"], "Les anciennes régions industrielles et certains quartiers de banlieue", "Le Nord et le pourtour méditerranéen sont touchés."),
  Q("Pourquoi l'État cherche-t-il à réduire les inégalités entre territoires ?", ["Au nom de l'égalité des citoyens et de la cohésion nationale", "Pour favoriser Paris", "Pour vider les campagnes", "Par obligation de l'ONU"], "Au nom de l'égalité des citoyens et de la cohésion nationale", "C'est l'objectif de l'aménagement du territoire."),
]),
notion('G3-2', 0, F, 'geo3-renovation-urbaine', [
  Q("Que fait-on lors d'une rénovation urbaine ?", ["On démolit, reconstruit ou rénove des logements et des espaces publics", "On construit une autoroute", "On plante des vignes", "On ferme toutes les écoles"], "On démolit, reconstruit ou rénove des logements et des espaces publics", "Elle vise surtout les grands ensembles."),
  Q("Pourquoi rénove-t-on les grands ensembles construits dans les années 1960 ?", ["Ils sont vieillissants et souvent mal reliés au reste de la ville", "Ils sont trop récents", "Ils sont vides", "Ils sont classés monuments historiques"], "Ils sont vieillissants et souvent mal reliés au reste de la ville", "On cherche à désenclaver les quartiers."),
  Q("Qu'est-ce que la mixité sociale ?", ["La présence de populations aux revenus variés dans un même quartier", "Un mélange de couleurs", "Un sport", "Une école de musique"], "La présence de populations aux revenus variés dans un même quartier", "C'est un objectif de la politique de la ville."),
]),
notion('G3-2', 0, F, 'geo3-croquis', [
  Q("Qu'est-ce qu'un croquis en géographie ?", ["Une représentation simplifiée d'un espace, réalisée à la main avec une légende", "Une photographie", "Un texte", "Un tableau de chiffres"], "Une représentation simplifiée d'un espace, réalisée à la main avec une légende", "Il doit avoir un titre."),
  Q("Comment représente-t-on une ville sur un croquis ?", ["Par un figuré ponctuel (un point ou un cercle)", "Par une flèche", "Par une surface colorée de toute la carte", "On ne la représente pas"], "Par un figuré ponctuel (un point ou un cercle)", "Sa taille peut varier avec la population."),
  Q("Comment représente-t-on une région agricole sur un croquis ?", ["Par un figuré de surface (aplat de couleur)", "Par un point", "Par une flèche", "Par un texte"], "Par un figuré de surface (aplat de couleur)", "Les surfaces, les points et les lignes sont les trois types de figurés."),
]),
notion('G3-2', 1, F, 'geo3-drom-noms', [
  Q("Quelle île française des Antilles a pour chef-lieu Fort-de-France ?", ["La Martinique", "La Guadeloupe", "La Réunion", "Mayotte"], "La Martinique", "Le chef-lieu de la Guadeloupe est Basse-Terre."),
  Q("Quel est le chef-lieu de La Réunion ?", ["Saint-Denis", "Saint-Pierre", "Cayenne", "Mamoudzou"], "Saint-Denis", "C'est la plus grande ville d'outre-mer."),
  Q("Quel est le chef-lieu de la Guyane ?", ["Cayenne", "Kourou", "Fort-de-France", "Nouméa"], "Cayenne", "La Guyane est le plus grand département français."),
]),
notion('G3-2', 1, F, 'geo3-com', [
  Q("Quelle collectivité française du Pacifique compte 118 îles, dont Tahiti ?", ["La Polynésie française", "La Nouvelle-Calédonie", "Wallis-et-Futuna", "Clipperton"], "La Polynésie française", "Sa capitale est Papeete."),
  Q("Quel archipel français se trouve près du Canada ?", ["Saint-Pierre-et-Miquelon", "Les Kerguelen", "Les Marquises", "Les Glorieuses"], "Saint-Pierre-et-Miquelon", "Il est situé au sud de Terre-Neuve."),
  Q("Quelle île française du Pacifique est riche en nickel ?", ["La Nouvelle-Calédonie", "La Martinique", "La Réunion", "Saint-Barthélemy"], "La Nouvelle-Calédonie", "Elle possède une grande partie des réserves mondiales."),
]),
notion('G3-2', 1, F, 'geo3-outre-mer-milieux', [
  Q("Quel type de climat domine dans la plupart des outre-mer ?", ["Un climat tropical", "Un climat polaire", "Un climat continental", "Un climat océanique tempéré"], "Un climat tropical", "Sauf Saint-Pierre-et-Miquelon et les Terres australes."),
  Q("Quelle forêt couvre plus de 90 % de la Guyane ?", ["La forêt amazonienne", "La forêt de pins", "La taïga", "La forêt méditerranéenne"], "La forêt amazonienne", "La Guyane est la seule partie de l'UE en Amazonie."),
  Q("Quel risque naturel menace particulièrement les Antilles françaises ?", ["Les cyclones et les séismes", "Les avalanches", "Les tempêtes de neige", "Le froid polaire"], "Les cyclones et les séismes", "La montagne Pelée est aussi un volcan actif."),
]),
notion('G3-2', 1, F, 'geo3-outre-mer-economie', [
  Q("Quelle production agricole est importante aux Antilles ?", ["La banane et la canne à sucre", "Le blé", "La vigne", "Les pommes"], "La banane et la canne à sucre", "Le rhum est un produit phare."),
  Q("Quelle activité économique est très importante dans les outre-mer ?", ["Le tourisme", "L'industrie automobile", "La sidérurgie", "La production de charbon"], "Le tourisme", "Plages, plongée, randonnées…"),
  Q("Pourquoi la vie est-elle plus chère dans les outre-mer qu'en métropole ?", ["De nombreux produits sont importés de loin", "Les salaires sont plus bas", "Il n'y a pas de magasins", "La TVA y est de 50 %"], "De nombreux produits sont importés de loin", "La « vie chère » provoque des mouvements sociaux."),
]),
notion('G3-2', 1, F, 'geo3-outre-mer-carte', [
  Q("Dans quel océan se trouve Mayotte ?", ["L'océan Indien", "L'océan Atlantique", "L'océan Pacifique", "L'océan Arctique"], "L'océan Indien", "Dans l'archipel des Comores."),
  Q("Dans quel océan se trouve la Polynésie française ?", ["L'océan Pacifique", "L'océan Indien", "L'océan Atlantique", "La mer Méditerranée"], "L'océan Pacifique", "À environ 16 000 km de Paris."),
  Q("Sur quel continent se trouve la Guyane ?", ["L'Amérique du Sud", "L'Afrique", "L'Asie", "L'Océanie"], "L'Amérique du Sud", "Entre le Suriname et le Brésil."),
]),
notion('G3-2', 0, F, 'geo3-espaces-verts', [
  Q("Pourquoi les villes créent-elles des parcs et des espaces verts ?", ["Pour améliorer le cadre de vie, rafraîchir l'air et protéger la biodiversité", "Pour supprimer les logements", "Pour augmenter la pollution", "Pour gêner les piétons"], "Pour améliorer le cadre de vie, rafraîchir l'air et protéger la biodiversité", "Ils sont essentiels face aux canicules."),
  Q("Qu'est-ce qu'une piste cyclable ?", ["Une voie réservée aux vélos", "Une autoroute", "Une voie ferrée", "Un canal"], "Une voie réservée aux vélos", "Les villes en développent beaucoup."),
  Q("Qu'est-ce qu'une zone piétonne ?", ["Une rue ou un quartier réservé aux piétons", "Un parking", "Une route rapide", "Une zone industrielle"], "Une rue ou un quartier réservé aux piétons", "Elle redynamise souvent le commerce."),
]),
# ══ Intermédiaire ══
notion('G3-2', 0, I, 'geo3i-histoire-amenagement', [
  Q("Quel livre de 1947 dénonce le déséquilibre entre la capitale et le reste du pays ?", ["Paris et le désert français", "La France périphérique", "Le Tour de la France par deux enfants", "Germinal"], "Paris et le désert français", "Il est écrit par Jean-François Gravier."),
  Q("Quelle politique des années 1960 crée des « métropoles d'équilibre » face à Paris ?", ["La politique d'aménagement de la DATAR", "La politique agricole commune", "La loi Ferry", "La politique de la ville de 2010"], "La politique d'aménagement de la DATAR", "Lyon, Marseille, Lille, Toulouse… en font partie."),
  Q("Quel organisme a remplacé la DATAR ?", ["L'Agence nationale de la cohésion des territoires (ANCT)", "L'Insee", "La SNCF", "L'Ademe"], "L'Agence nationale de la cohésion des territoires (ANCT)", "Elle est créée en 2020."),
]),
notion('G3-2', 0, I, 'geo3i-plu-scot', [
  Q("Quel document fixe les règles de construction dans une commune ?", ["Le plan local d'urbanisme (PLU)", "Le règlement intérieur", "Le budget", "La Constitution"], "Le plan local d'urbanisme (PLU)", "Il est souvent élaboré à l'échelle intercommunale (PLUi)."),
  Q("Quel document coordonne l'aménagement à l'échelle d'un bassin de vie ?", ["Le schéma de cohérence territoriale (SCoT)", "Le PLU", "Le permis de construire", "Le cadastre"], "Le schéma de cohérence territoriale (SCoT)", "Il fixe les grandes orientations."),
  Q("Quel document faut-il obtenir avant de construire une maison ?", ["Un permis de construire", "Un permis de conduire", "Un passeport", "Un certificat de scolarité"], "Un permis de construire", "Il est délivré par le maire."),
]),
notion('G3-2', 0, I, 'geo3i-intercommunalite', [
  Q("Comment appelle-t-on le regroupement de communes pour gérer ensemble des services ?", ["Une intercommunalité", "Un département", "Une région", "Un canton"], "Une intercommunalité", "Communautés de communes, d'agglomération, métropoles…"),
  Q("Pourquoi les communes se regroupent-elles ?", ["Pour mutualiser les moyens (transports, déchets, eau)", "Pour supprimer les maires", "Pour fusionner les pays", "Par goût de la compétition"], "Pour mutualiser les moyens (transports, déchets, eau)", "La France compte environ 35 000 communes."),
  Q("Combien de communes compte environ la France ?", ["Environ 35 000", "Environ 3 500", "Environ 350 000", "Environ 101"], "Environ 35 000", "C'est l'un des records d'Europe."),
]),
notion('G3-2', 0, I, 'geo3i-projets-contestes', [
  Q("Quel projet d'aéroport près de Nantes a été abandonné en 2018 après une longue contestation ?", ["Notre-Dame-des-Landes", "Roissy", "Orly", "Blagnac"], "Notre-Dame-des-Landes", "Une « ZAD » occupait le site."),
  Q("Que signifie « ZAD » pour les opposants à un projet ?", ["Zone à défendre", "Zone d'activités durables", "Zone d'aménagement différé uniquement", "Zone à démolir"], "Zone à défendre", "C'est un détournement du sigle administratif."),
  Q("Quel projet d'autoroute dans le Tarn a été très contesté dans les années 2020 ?", ["L'A69 entre Toulouse et Castres", "L'A1", "L'A6", "L'A86"], "L'A69 entre Toulouse et Castres", "Les opposants dénoncent l'abattage d'arbres et le coût."),
]),
notion('G3-2', 0, I, 'geo3i-transports-desenclavement', [
  Q("Qu'est-ce qu'un territoire enclavé ?", ["Un territoire difficile d'accès, mal relié au reste du pays", "Un territoire très connecté", "Une île touristique", "Un quartier d'affaires"], "Un territoire difficile d'accès, mal relié au reste du pays", "Le désenclavement vise à mieux le relier."),
  Q("Quel type de train relie les villes moyennes d'une même région ?", ["Le TER", "Le TGV", "L'Eurostar", "Le métro"], "Le TER", "Il est géré par les régions."),
  Q("Quels trains de nuit ont été relancés en France depuis 2021 ?", ["Paris-Nice, Paris-Lourdes, Paris-Briançon…", "Paris-New York", "Lyon-Tokyo", "Lille-Pékin"], "Paris-Nice, Paris-Lourdes, Paris-Briançon…", "Ils offrent une alternative à l'avion."),
]),
notion('G3-2', 0, I, 'geo3i-transition-territoires', [
  Q("Quel organisme public aide les collectivités dans la transition écologique ?", ["L'Ademe", "L'Insee", "La CNIL", "La Banque de France"], "L'Ademe", "Agence de la transition écologique."),
  Q("Qu'est-ce qu'un territoire à énergie positive ?", ["Un territoire qui produit plus d'énergie renouvelable qu'il n'en consomme", "Un territoire très ensoleillé", "Un territoire sans électricité", "Un territoire nucléaire"], "Un territoire qui produit plus d'énergie renouvelable qu'il n'en consomme", "Certaines communes rurales y parviennent."),
  Q("Comment appelle-t-on l'aménagement du littoral face à la montée des eaux par le déplacement des constructions ?", ["La recomposition spatiale (ou repli stratégique)", "La poldérisation", "La métropolisation", "La littoralisation"], "La recomposition spatiale (ou repli stratégique)", "Lacanau ou Soulac en sont des exemples."),
]),
notion('G3-2', 0, I, 'geo3i-europe-amenagement', [
  Q("Quel fonds européen finance des projets dans les régions les moins développées ?", ["Le FEDER", "Le FMI", "La PAC", "Le fonds Barnier"], "Le FEDER", "Fonds européen de développement régional."),
  Q("Quels territoires français reçoivent une aide renforcée de l'UE en tant que régions moins développées ?", ["Les DROM", "L'Île-de-France", "Les Hauts-de-Seine", "La Haute-Savoie"], "Les DROM", "Ce sont des régions ultrapériphériques."),
  Q("Quel panneau signale souvent un aménagement cofinancé par l'Union européenne ?", ["Un panneau avec le drapeau européen", "Un panneau stop", "Un drapeau rouge", "Rien"], "Un panneau avec le drapeau européen", "L'UE finance routes, médiathèques, zones d'activités…"),
]),
notion('G3-2', 1, I, 'geo3i-outre-mer-statuts', [
  Q("Quelle différence y a-t-il entre un DROM et une COM ?", ["Le DROM applique le droit commun français ; la COM a un statut particulier", "Ils sont identiques", "La COM n'est pas française", "Le DROM est indépendant"], "Le DROM applique le droit commun français ; la COM a un statut particulier", "La Polynésie française est une COM."),
  Q("Quelle collectivité d'outre-mer a un statut unique, avec un processus de décolonisation en cours ?", ["La Nouvelle-Calédonie", "La Martinique", "La Réunion", "La Guyane"], "La Nouvelle-Calédonie", "Trois référendums ont eu lieu entre 2018 et 2021."),
  Q("Combien d'habitants comptent environ les outre-mer français ?", ["Environ 2,8 millions", "Environ 28 millions", "Environ 280 000", "Environ 28 000"], "Environ 2,8 millions", "Soit environ 4 % de la population française."),
]),
notion('G3-2', 1, I, 'geo3i-outre-mer-contraintes', [
  Q("Pourquoi les outre-mer sont-ils qualifiés de territoires « ultrapériphériques » par l'UE ?", ["Ils sont très éloignés du continent européen", "Ils sont très peuplés", "Ils sont très riches", "Ils sont en Europe"], "Ils sont très éloignés du continent européen", "L'éloignement entraîne des coûts élevés."),
  Q("Quel est le taux de chômage dans les DROM par rapport à la métropole ?", ["Il est nettement plus élevé", "Il est plus faible", "Il est identique", "Il n'y a pas de chômage"], "Il est nettement plus élevé", "Surtout chez les jeunes."),
  Q("Quelle pollution agricole touche durablement les sols de Martinique et de Guadeloupe ?", ["Le chlordécone", "Le nucléaire", "Le pétrole", "Les microplastiques uniquement"], "Le chlordécone", "Ce pesticide a été utilisé dans les bananeraies jusqu'en 1993."),
]),
notion('G3-2', 1, I, 'geo3i-guyane', [
  Q("Quelle est la superficie de la Guyane par rapport à la métropole ?", ["Environ un sixième de la métropole", "Plus grande que la métropole", "La taille d'une ville", "La taille de la Corse"], "Environ un sixième de la métropole", "Environ 84 000 km²."),
  Q("Quelle activité illégale menace la forêt guyanaise ?", ["L'orpaillage clandestin", "La pêche à la ligne", "Le tourisme", "La culture du blé"], "L'orpaillage clandestin", "Il pollue les rivières au mercure."),
  Q("Quel fleuve forme la frontière entre la Guyane et le Brésil ?", ["L'Oyapock", "Le Maroni", "L'Amazone", "L'Orénoque"], "L'Oyapock", "Le Maroni sépare la Guyane du Suriname."),
]),
notion('G3-2', 1, I, 'geo3i-reunion', [
  Q("Combien d'habitants compte environ La Réunion ?", ["Environ 900 000", "Environ 90 000", "Environ 9 millions", "Environ 9 000"], "Environ 900 000", "C'est le plus peuplé des DROM."),
  Q("Quel cirque réunionnais, accessible seulement à pied ou en hélicoptère, est célèbre ?", ["Le cirque de Mafate", "Le cirque de Gavarnie", "Le cirque d'Hiver", "Le cirque de Navacelles"], "Le cirque de Mafate", "Il est inscrit au patrimoine mondial avec les pitons et remparts."),
  Q("Où se concentre la population de La Réunion ?", ["Sur le littoral", "Au sommet des volcans", "Au centre de l'île uniquement", "Elle est répartie également"], "Sur le littoral", "L'intérieur est montagneux."),
]),
notion('G3-2', 0, I, 'geo3i-politique-ville-outils', [
  Q("Quel dispositif accorde des exonérations fiscales aux entreprises qui s'installent dans certains quartiers prioritaires ?", ["Les zones franches urbaines (ZFU)", "Les ZEE", "Les zones blanches", "Les parcs nationaux"], "Les zones franches urbaines (ZFU)", "Elles visent à créer des emplois."),
  Q("Quel programme aide depuis 2018 plus de 200 villes moyennes à revitaliser leur centre ?", ["Action cœur de ville", "Le Grand Paris", "France 2030", "Petites villes de demain"], "Action cœur de ville", "Il soutient le commerce et le logement."),
  Q("Quel indicateur sert à définir les quartiers prioritaires ?", ["Le revenu médian des habitants", "Le nombre de monuments", "L'altitude", "Le nombre de touristes"], "Le revenu médian des habitants", "Les QPV ont des revenus très inférieurs à la moyenne."),
]),
notion('G3-2', 0, I, 'geo3i-numerique-territoire', [
  Q("Quel plan national déploie la fibre optique dans tout le pays ?", ["Le plan France Très Haut Débit", "Le plan Marshall", "Le plan Vigipirate", "Le plan ORSEC"], "Le plan France Très Haut Débit", "Il est lancé en 2013."),
  Q("Comment appelle-t-on une zone non couverte par la téléphonie mobile ?", ["Une zone blanche", "Une zone rouge", "Une zone franche", "Une zone bleue"], "Une zone blanche", "Le « New Deal mobile » de 2018 vise à les résorber."),
  Q("Pourquoi le numérique est-il un enjeu d'aménagement ?", ["Il conditionne l'accès aux services, à l'emploi et au télétravail", "Il remplace les routes", "Il n'a aucun lien avec le territoire", "Il ne concerne que Paris"], "Il conditionne l'accès aux services, à l'emploi et au télétravail", "C'est un facteur d'attractivité."),
]),
# ══ Avancé ══
notion('G3-2', 0, D, 'geo3d-solidarite-territoriale', [
  Q("Comment appelle-t-on le mécanisme qui redistribue des ressources des collectivités riches vers les plus pauvres ?", ["La péréquation", "La décentralisation", "La métropolisation", "La privatisation"], "La péréquation", "Elle est inscrite dans la Constitution depuis 2003."),
  Q("Quelle dotation de l'État finance une grande partie du budget des collectivités ?", ["La dotation globale de fonctionnement (DGF)", "La TVA européenne", "Le FEDER", "La taxe de séjour"], "La dotation globale de fonctionnement (DGF)", "Elle est versée chaque année."),
  Q("Quel impôt local a été supprimé pour les résidences principales entre 2020 et 2023 ?", ["La taxe d'habitation", "La taxe foncière", "La TVA", "L'impôt sur le revenu"], "La taxe d'habitation", "Elle subsiste pour les résidences secondaires."),
]),
notion('G3-2', 0, D, 'geo3d-sraddet', [
  Q("Quel schéma régional fixe les grandes orientations d'aménagement et de développement durable ?", ["Le SRADDET", "Le PLU", "Le permis de construire", "Le DICRIM"], "Le SRADDET", "Il est élaboré par chaque région depuis la loi NOTRe."),
  Q("Quelle loi de 2015 a renforcé les compétences des régions ?", ["La loi NOTRe", "La loi SRU", "La loi Littoral", "La loi Montagne"], "La loi NOTRe", "Nouvelle organisation territoriale de la République."),
  Q("Quelle loi de 2014 a réduit le nombre de régions métropolitaines de 22 à 13 ?", ["La loi sur la délimitation des régions", "La loi Defferre", "La loi Ferry", "La loi Pasqua"], "La loi sur la délimitation des régions", "Les nouvelles régions sont entrées en vigueur en 2016."),
]),
notion('G3-2', 0, D, 'geo3d-grand-paris', [
  Q("Combien de nouvelles gares le Grand Paris Express doit-il compter ?", ["68", "6", "200", "12"], "68", "Pour environ 200 km de lignes."),
  Q("Quelle structure intercommunale réunit Paris et 130 communes depuis 2016 ?", ["La métropole du Grand Paris", "La région Île-de-France", "Le département de Paris", "L'aire d'attraction de Paris"], "La métropole du Grand Paris", "Elle compte environ 7 millions d'habitants."),
  Q("Pourquoi le Grand Paris Express relie-t-il les banlieues entre elles ?", ["Pour éviter de passer par Paris et désenclaver des quartiers", "Pour remplacer le TGV", "Pour aller à Londres", "Pour supprimer le RER"], "Pour éviter de passer par Paris et désenclaver des quartiers", "La ligne 15 est une rocade autour de Paris."),
]),
notion('G3-2', 0, D, 'geo3d-debat-public', [
  Q("Quelle autorité organise le débat public sur les grands projets d'aménagement ?", ["La Commission nationale du débat public (CNDP)", "Le Conseil constitutionnel", "L'Arcom", "La CNIL"], "La Commission nationale du débat public (CNDP)", "Elle est indépendante."),
  Q("Qu'est-ce qu'une enquête publique ?", ["Une procédure qui permet aux citoyens de donner leur avis sur un projet avant décision", "Une enquête de police", "Un sondage commercial", "Un recensement"], "Une procédure qui permet aux citoyens de donner leur avis sur un projet avant décision", "Un commissaire enquêteur rend ensuite un avis."),
  Q("Que signifie l'acronyme NIMBY utilisé pour certaines oppositions locales ?", ["« Pas dans mon jardin » (Not In My Back Yard)", "« Nouveaux investissements maritimes »", "« Non à l'industrie minière »", "« Nature et biodiversité »"], "« Pas dans mon jardin » (Not In My Back Yard)", "Il désigne le refus d'un équipement près de chez soi."),
]),
notion('G3-2', 0, D, 'geo3d-montagne-littoral-lois', [
  Q("Quelle règle de la loi Littoral interdit de construire hors zones urbanisées près du rivage ?", ["L'inconstructibilité de la bande des 100 mètres", "La règle des 10 kilomètres", "L'interdiction de toute plage", "L'obligation de construire des digues"], "L'inconstructibilité de la bande des 100 mètres", "Elle protège les espaces naturels du littoral."),
  Q("Quel organisme public achète des terrains littoraux pour les protéger ?", ["Le Conservatoire du littoral", "La SNCF", "L'Insee", "La Banque de France"], "Le Conservatoire du littoral", "Il est créé en 1975."),
  Q("Quelle part du linéaire côtier français est protégée par le Conservatoire du littoral ?", ["Environ 16 %", "Environ 1 %", "Environ 80 %", "100 %"], "Environ 16 %", "Son objectif est d'atteindre un tiers."),
]),
notion('G3-2', 0, D, 'geo3d-fret-ferroviaire', [
  Q("Quelle part du transport de marchandises se fait par la route en France ?", ["Environ 85 %", "Environ 20 %", "Environ 50 %", "Environ 5 %"], "Environ 85 %", "Le fret ferroviaire ne représente qu'environ 10 %."),
  Q("Qu'est-ce que le ferroutage ?", ["Le transport de camions ou de remorques sur des trains", "Une route pour vélos", "Un bateau de croisière", "Un tunnel routier"], "Le transport de camions ou de remorques sur des trains", "Il réduit le trafic routier et la pollution."),
  Q("Pourquoi la France cherche-t-elle à développer le fret ferroviaire ?", ["Pour réduire les émissions de CO2 et les camions sur les routes", "Pour supprimer les trains de voyageurs", "Pour augmenter la pollution", "Pour fermer les ports"], "Pour réduire les émissions de CO2 et les camions sur les routes", "L'objectif est de doubler sa part d'ici 2030."),
]),
notion('G3-2', 0, D, 'geo3d-ruptures-territoriales', [
  Q("Comment appelle-t-on une coupure dans le territoire, comme une autoroute qui sépare deux quartiers ?", ["Une rupture (ou coupure) urbaine", "Une continuité", "Un axe de développement", "Une centralité"], "Une rupture (ou coupure) urbaine", "Les aménageurs cherchent à recoudre la ville."),
  Q("Quel projet a transformé une autoroute urbaine en boulevard à Lyon, le long du Rhône ?", ["L'aménagement des berges du Rhône", "La Défense", "Euralille", "Le Grand Paris Express"], "L'aménagement des berges du Rhône", "Les quais ont été rendus aux piétons et aux cyclistes."),
  Q("Qu'est-ce qu'un « effet tunnel » en aménagement ?", ["Un territoire traversé par une infrastructure sans en profiter faute d'arrêt", "Un tunnel de montagne", "Un embouteillage dans un tunnel", "Une gare souterraine"], "Un territoire traversé par une infrastructure sans en profiter faute d'arrêt", "Les campagnes traversées par le TGV en sont un exemple."),
]),
notion('G3-2', 1, D, 'geo3d-mayotte', [
  N("En quelle année Mayotte devient-elle un département français ?", 2011, "Après un référendum en 2009."),
  Q("Quel est le principal défi de Mayotte ?", ["La pauvreté, l'immigration irrégulière et le manque d'infrastructures (eau, logement)", "Le froid", "Le vieillissement", "Le surplus d'eau"], "La pauvreté, l'immigration irrégulière et le manque d'infrastructures (eau, logement)", "Le cyclone Chido de 2024 a aggravé la situation."),
  Q("Quelle part de la population de Mayotte a moins de 18 ans ?", ["Environ la moitié", "Environ 5 %", "Environ 90 %", "Environ 20 %"], "Environ la moitié", "C'est le département le plus jeune de France."),
]),
notion('G3-2', 1, D, 'geo3d-nouvelle-caledonie', [
  Q("Quels accords de 1998 organisent l'avenir institutionnel de la Nouvelle-Calédonie ?", ["Les accords de Nouméa", "Les accords d'Évian", "Les accords de Matignon de 1936", "Les accords de Schengen"], "Les accords de Nouméa", "Ils font suite aux accords de Matignon-Oudinot de 1988."),
  Q("Quel peuple autochtone vit en Nouvelle-Calédonie ?", ["Les Kanak", "Les Inuits", "Les Maoris", "Les Amérindiens"], "Les Kanak", "Ils représentent environ 40 % de la population."),
  Q("Quel événement de 2024 a provoqué de graves violences en Nouvelle-Calédonie ?", ["Un projet de réforme du corps électoral", "Un cyclone", "Un tsunami", "La découverte de pétrole"], "Un projet de réforme du corps électoral", "Les émeutes ont fait plusieurs morts."),
]),
notion('G3-2', 1, D, 'geo3d-taaf-iles', [
  Q("Quel territoire français, sans habitants permanents, comprend les îles Kerguelen et la terre Adélie ?", ["Les Terres australes et antarctiques françaises (TAAF)", "La Polynésie française", "Wallis-et-Futuna", "Saint-Martin"], "Les Terres australes et antarctiques françaises (TAAF)", "Seuls des scientifiques et militaires y séjournent."),
  Q("Quel îlot français du Pacifique, inhabité, apporte une vaste ZEE ?", ["Clipperton", "Belle-Île", "Ouessant", "Porquerolles"], "Clipperton", "Il se trouve au large du Mexique."),
  Q("Quel intérêt ces îles présentent-elles pour la France ?", ["Une immense ZEE, des ressources marines et des bases scientifiques", "Une forte population", "Des industries lourdes", "Aucun"], "Une immense ZEE, des ressources marines et des bases scientifiques", "Elles renforcent la présence française dans le monde."),
]),
notion('G3-2', 1, D, 'geo3d-outre-mer-vie-chere', [
  Q("Quelle est l'écart moyen des prix alimentaires entre les DROM et la métropole ?", ["Environ 30 à 40 % plus chers", "Ils sont moins chers", "Identiques", "Dix fois plus chers"], "Environ 30 à 40 % plus chers", "Selon l'Insee (2022)."),
  Q("Quel mouvement social contre la vie chère a touché la Martinique en 2024 ?", ["Des manifestations et des barrages contre les prix élevés", "Une grève des pêcheurs uniquement", "Une marche pour le climat", "Une révolte contre le tourisme"], "Des manifestations et des barrages contre les prix élevés", "Un accord de baisse des prix a été signé."),
  Q("Qu'est-ce que l'« octroi de mer » ?", ["Une taxe sur les produits importés dans les DROM", "Un droit de pêche", "Une subvention européenne", "Un impôt sur le revenu"], "Une taxe sur les produits importés dans les DROM", "Elle finance les communes mais renchérit les prix."),
]),
notion('G3-2', 1, D, 'geo3d-outre-mer-biodiversite', [
  Q("Quelle part de la biodiversité française se trouve dans les outre-mer ?", ["Environ 80 %", "Environ 5 %", "Environ 20 %", "Aucune"], "Environ 80 %", "Ce sont des « points chauds » de biodiversité."),
  Q("Quel lagon d'outre-mer est inscrit au patrimoine mondial de l'Unesco ?", ["Les lagons de Nouvelle-Calédonie", "Le lac Léman", "L'étang de Berre", "Le lac d'Annecy"], "Les lagons de Nouvelle-Calédonie", "Ils abritent l'une des plus grandes barrières de corail du monde."),
  Q("Quel parc national protège une grande partie du sud de la Guyane ?", ["Le Parc amazonien de Guyane", "Le parc des Calanques", "Le parc de la Vanoise", "Le parc des Écrins"], "Le Parc amazonien de Guyane", "C'est le plus grand parc national de France et de l'UE."),
]),
notion('G3-2', 1, D, 'geo3d-rup', [
  Q("Combien de régions ultrapériphériques (RUP) compte l'Union européenne ?", ["9", "2", "27", "50"], "9", "Dont 6 françaises, plus les Açores, Madère et les Canaries."),
  Q("Quelle différence y a-t-il entre une RUP et un PTOM ?", ["Une RUP fait partie de l'UE ; un PTOM y est seulement associé", "Elles sont identiques", "Un PTOM est en Europe", "Une RUP est indépendante"], "Une RUP fait partie de l'UE ; un PTOM y est seulement associé", "La Polynésie française est un PTOM."),
  Q("Quelle monnaie est utilisée en Polynésie française et en Nouvelle-Calédonie ?", ["Le franc Pacifique (CFP)", "L'euro", "Le dollar australien", "Le yen"], "Le franc Pacifique (CFP)", "Les DROM utilisent l'euro."),
]),
notion('G3-2', 0, D, 'geo3d-ports-amenagement', [
  Q("Quel grand aménagement portuaire a créé une zone industrielle à l'ouest de Marseille dans les années 1960-1970 ?", ["Fos-sur-Mer", "Le Vieux-Port", "La Joliette", "L'Estaque"], "Fos-sur-Mer", "On y trouve sidérurgie et pétrochimie."),
  Q("Quel terminal du Havre, ouvert en 2006, accueille les plus grands porte-conteneurs ?", ["Port 2000", "Port-Vendres", "Port-Cros", "Port-Royal"], "Port 2000", "Il permet au Havre de rivaliser avec les ports du Nord de l'Europe."),
  Q("Pourquoi les ports français perdent-ils des parts de marché face à Rotterdam ou Anvers ?", ["Leur hinterland est moins bien desservi par le rail et le fleuve", "Ils sont trop proches de la mer", "Ils n'ont pas de quais", "Ils sont interdits aux conteneurs"], "Leur hinterland est moins bien desservi par le rail et le fleuve", "Une part des marchandises françaises passe par ces ports étrangers."),
]),
notion('G3-2', 1, D, 'geo3d-outre-mer-cooperation', [
  Q("Avec quels pays les Antilles françaises coopèrent-elles dans une organisation régionale ?", ["Les États de la Caraïbe orientale (OECO)", "Les pays nordiques", "Les pays du Golfe", "L'ASEAN"], "Les États de la Caraïbe orientale (OECO)", "La Martinique en est membre associé."),
  Q("Quelle organisation de l'océan Indien la France intègre-t-elle au titre de La Réunion ?", ["La Commission de l'océan Indien", "L'ASEAN", "Le Mercosur", "L'OTAN"], "La Commission de l'océan Indien", "Avec Madagascar, Maurice, les Comores et les Seychelles."),
  Q("Pourquoi l'intégration régionale des outre-mer est-elle difficile ?", ["Leurs échanges sont surtout tournés vers la métropole et l'UE", "Ils n'ont pas de voisins", "Ils refusent tout commerce", "Ils sont tous indépendants"], "Leurs échanges sont surtout tournés vers la métropole et l'UE", "On parle de relation « mère-filles » ou de dépendance."),
]),
]

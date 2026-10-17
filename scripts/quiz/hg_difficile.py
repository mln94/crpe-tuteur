from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('H5-1', 0, D, 'hg-schisme-1054', [
  N("En quelle année se produit le schisme entre l'Église de Rome et l'Église de Constantinople ?", 1054, "En 1054, le pape et le patriarche de Constantinople s'excommunient mutuellement : c'est le grand schisme d'Orient."),
  Q("Quelles Églises se séparent lors du schisme de 1054 ?", ["Catholique et protestante", "Catholique romaine et orthodoxe", "Orthodoxe et copte", "Anglicane et catholique"], "Catholique romaine et orthodoxe", "Le schisme sépare la chrétienté latine (Rome) de la chrétienté grecque (Constantinople)."),
  Q("Quelle querelle religieuse divise l'Empire byzantin aux VIIIe et IXe siècles ?", ["La querelle des Investitures", "La querelle des images (iconoclasme)", "La querelle janséniste", "La Réforme"], "La querelle des images (iconoclasme)", "Les iconoclastes interdisent la vénération des images saintes (icônes), rétablie en 843."),
]),
notion('H5-3', 1, D, 'hg-contre-reforme', [
  Q("Quel concile organise la réponse de l'Église catholique à la Réforme protestante ?", ["Le concile de Nicée", "Le concile de Trente", "Le concile de Clermont", "Le concile Vatican II"], "Le concile de Trente", "Le concile de Trente (1545-1563) réaffirme les dogmes catholiques et réforme l'Église : c'est la Réforme catholique."),
  Q("Quel ordre religieux fondé par Ignace de Loyola joue un grand rôle dans la Réforme catholique ?", ["Les franciscains", "Les jésuites", "Les cisterciens", "Les templiers"], "Les jésuites", "La Compagnie de Jésus (1540) développe l'enseignement et les missions."),
  Q("Sur quel point les protestants s'opposent-ils notamment à l'Église catholique ?", ["Le rejet de la Bible", "Le salut par la foi et l'autorité de la seule Bible", "L'obligation du culte des saints", "L'infaillibilité du pape"], "Le salut par la foi et l'autorité de la seule Bible", "Pour Luther, le salut vient de la foi seule, et la Bible seule fait autorité (et non la tradition de l'Église)."),
]),
notion('H4-1', 1, D, 'hg-despotisme-eclaire', [
  Q("Comment appelle-t-on le gouvernement de souverains absolus qui s'inspirent des idées des Lumières, comme Frédéric II de Prusse ?", ["La monarchie parlementaire", "Le despotisme éclairé", "La république", "Le totalitarisme"], "Le despotisme éclairé", "Frédéric II ou Catherine II de Russie réforment leurs États en s'inspirant des philosophes, sans renoncer à l'absolutisme."),
  Q("Quelle souveraine russe correspond avec Voltaire et Diderot ?", ["Élisabeth Ire", "Catherine II", "Marie-Thérèse", "Anne d'Autriche"], "Catherine II", "Catherine II (1762-1796) accueille Diderot à Saint-Pétersbourg."),
  Q("Quel pays devient au XVIIIe siècle un modèle de monarchie limitée, admiré par Montesquieu et Voltaire ?", ["L'Espagne", "L'Angleterre", "La Russie", "La Prusse"], "L'Angleterre", "Depuis la Glorieuse Révolution (1688-1689) et le Bill of Rights, le pouvoir du roi y est limité par le Parlement."),
]),
notion('H4-1', 2, D, 'hg-constitution-1791', [
  Q("Quel régime la Constitution de 1791 établit-elle ?", ["Une république", "Une monarchie constitutionnelle", "Un empire", "Une monarchie absolue"], "Une monarchie constitutionnelle", "Le roi conserve le pouvoir exécutif, mais doit respecter la Constitution ; l'Assemblée vote les lois."),
  Q("Quel type de suffrage la Constitution de 1791 instaure-t-elle ?", ["Universel", "Censitaire", "Féminin", "Direct pour tous"], "Censitaire", "Seuls les citoyens « actifs », payant un impôt minimum, peuvent voter."),
  Q("Quel épisode de juin 1791 ruine la confiance dans le roi ?", ["La prise des Tuileries", "La fuite à Varennes", "Le serment du Jeu de paume", "La fête de la Fédération"], "La fuite à Varennes", "Arrêté à Varennes alors qu'il tentait de fuir, Louis XVI perd la confiance d'une partie des Français."),
]),
notion('H4-3', 0, D, 'hg-revolutions-xixe', [
  Q("Quelle révolution de juillet 1830 renverse Charles X ?", ["Les Trois Glorieuses", "La Commune", "Les Cent-Jours", "La Fronde"], "Les Trois Glorieuses", "Les 27, 28 et 29 juillet 1830, Paris se soulève ; Louis-Philippe devient roi des Français."),
  Q("Quelle insurrection parisienne de 1871 est réprimée lors de la « Semaine sanglante » ?", ["La Commune de Paris", "Les journées de Juin", "La révolution de 1848", "Les Trois Glorieuses"], "La Commune de Paris", "La Commune (mars-mai 1871) est écrasée par le gouvernement de Versailles."),
  Q("Quel régime remplace la monarchie de Juillet en février 1848 ?", ["Le Second Empire", "La IIe République", "La IIIe République", "La Restauration"], "La IIe République", "La révolution de février 1848 renverse Louis-Philippe ; la IIe République est proclamée."),
]),
notion('H3-1', 1, D, 'hg-caracteristiques-totalitarisme', [
  Q("Quel trait caractérise un régime totalitaire ?", ["Le pluralisme politique", "Le contrôle de toute la société par un parti unique et la terreur", "La séparation des pouvoirs", "La liberté de la presse"], "Le contrôle de toute la société par un parti unique et la terreur", "Le totalitarisme vise à encadrer toute la société : parti unique, culte du chef, propagande, police politique, terreur."),
  Q("Comment s'appelle le système de camps de travail forcé en URSS ?", ["Le Goulag", "Le kolkhoze", "Le Komintern", "La NKVD"], "Le Goulag", "Le Goulag est l'administration des camps de travail forcé où des millions de personnes sont déportées."),
  Q("Quelles lois de 1935 excluent les Juifs de la citoyenneté allemande ?", ["Les lois de Nuremberg", "Les lois de Weimar", "Les lois de Munich", "Les lois de Versailles"], "Les lois de Nuremberg", "Les lois de Nuremberg privent les Juifs de leurs droits civiques et interdisent les mariages mixtes."),
]),
notion('H3-2', 3, D, 'hg-monde-apres-1989', [
  Q("Quel événement de 2001 marque un tournant dans les relations internationales après la guerre froide ?", ["La chute du mur de Berlin", "Les attentats du 11 septembre aux États-Unis", "Le traité de Maastricht", "La crise de Cuba"], "Les attentats du 11 septembre aux États-Unis", "Les attentats du 11 septembre 2001 ouvrent une période de « guerre contre le terrorisme »."),
  Q("Quel conflit des années 1990 déchire l'ex-Yougoslavie ?", ["La guerre de Corée", "Les guerres de Yougoslavie", "La guerre du Golfe seulement", "La guerre d'Afghanistan"], "Les guerres de Yougoslavie", "Les guerres de Yougoslavie (1991-2001) sont marquées par des crimes de masse, comme à Srebrenica en 1995."),
  Q("Quelle expression désigne la domination des États-Unis comme seule superpuissance après 1991 ?", ["Le monde bipolaire", "L'hyperpuissance", "Le non-alignement", "La coexistence pacifique"], "L'hyperpuissance", "Après la disparition de l'URSS, les États-Unis deviennent la seule superpuissance : on parle d'hyperpuissance."),
]),
notion('H3-3', 1, D, 'hg-institutions-ve', [
  Q("Quel article de la Constitution de 1958 permet au président d'exercer des pouvoirs exceptionnels en cas de crise grave ?", ["L'article 1", "L'article 16", "L'article 49-3", "L'article 89"], "L'article 16", "L'article 16 donne au président des pouvoirs exceptionnels ; il n'a été utilisé qu'en 1961."),
  Q("Que permet l'article 49 alinéa 3 de la Constitution ?", ["Dissoudre l'Assemblée", "Faire adopter un texte sans vote, sauf si une motion de censure est votée", "Organiser un référendum", "Élire le président"], "Faire adopter un texte sans vote, sauf si une motion de censure est votée", "Le gouvernement engage sa responsabilité ; le texte est adopté si aucune motion de censure n'est votée."),
  N("En quelle année un référendum instaure-t-il l'élection du président au suffrage universel direct ?", 1962, "Le référendum d'octobre 1962 renforce la légitimité du président."),
  Q("Depuis 2000, quelle est la durée du mandat du président de la République ?", ["4 ans", "5 ans", "7 ans", "6 ans"], "5 ans", "Le référendum de 2000 a remplacé le septennat par le quinquennat, appliqué depuis 2002."),
]),
notion('H3-2', 0, D, 'hg-bandung', [
  N("En quelle année se tient la conférence de Bandung, qui réunit des pays d'Asie et d'Afrique ?", 1955, "La conférence de Bandung (Indonésie, 1955) condamne le colonialisme et affirme la voie des pays du « tiers-monde »."),
  Q("Qui invente l'expression « tiers-monde » en 1952 ?", ["Frantz Fanon", "Alfred Sauvy", "Nehru", "Senghor"], "Alfred Sauvy", "Le démographe Alfred Sauvy compare ces pays au tiers état d'avant 1789."),
  Q("Quels accords mettent fin à la guerre d'Algérie en 1962 ?", ["Les accords de Genève", "Les accords d'Évian", "Les accords de Matignon", "Les accords de Grenelle"], "Les accords d'Évian", "Signés le 18 mars 1962, ils prévoient un cessez-le-feu et l'autodétermination de l'Algérie."),
]),
notion('G5-1', 1, D, 'geo-mesures-developpement', [
  Q("Quels indicateurs composent l'IDH ?", ["PIB total, superficie, population", "Espérance de vie, durée de scolarisation, revenu par habitant", "Taux de chômage, inflation, exportations", "Natalité, mortalité, migrations"], "Espérance de vie, durée de scolarisation, revenu par habitant", "L'IDH combine santé, éducation et niveau de vie, au-delà de la seule richesse."),
  Q("Pourquoi le PIB par habitant ne suffit-il pas à mesurer le développement ?", ["Il est toujours faux", "Il ne dit rien de la répartition des richesses, de la santé ou de l'éducation", "Il ne concerne que les pays riches", "Il mesure la superficie"], "Il ne dit rien de la répartition des richesses, de la santé ou de l'éducation", "Un PIB élevé peut cacher de fortes inégalités ; d'où l'usage d'indicateurs complémentaires."),
  Q("Quels pays ont aujourd'hui les IDH les plus faibles ?", ["Des pays d'Europe du Nord", "Des pays d'Afrique subsaharienne", "Des pays d'Amérique du Nord", "Des pays d'Asie de l'Est"], "Des pays d'Afrique subsaharienne", "Des pays comme le Soudan du Sud, la Somalie ou le Tchad ont les IDH les plus bas."),
]),
notion('G4-1', 1, D, 'geo-villes-mondiales', [
  Q("Quelles villes sont généralement placées au sommet de la hiérarchie des villes mondiales ?", ["Lagos et Kinshasa", "New York et Londres", "Bordeaux et Lille", "Le Caire et Lima"], "New York et Londres", "New York et Londres concentrent les principales fonctions de commandement financier et économique mondial."),
  Q("Comment appelle-t-on le processus de concentration des activités et des pouvoirs dans les grandes métropoles ?", ["La métropolisation", "La périurbanisation", "La désindustrialisation", "La ruralisation"], "La métropolisation", "La métropolisation renforce le poids des plus grandes villes, connectées entre elles dans la mondialisation."),
  Q("Quelle ville est l'exemple d'une ville en déclin après la crise de son industrie automobile ?", ["Detroit", "San Francisco", "Shanghai", "Dubaï"], "Detroit", "Detroit, ancienne capitale de l'automobile, a perdu plus de la moitié de sa population : on parle de « ville rétrécissante »."),
]),
notion('G4-3', 2, D, 'geo-afrique', [
  Q("Quel pays d'Afrique est le plus peuplé ?", ["L'Afrique du Sud", "Le Nigeria", "L'Égypte", "L'Éthiopie"], "Le Nigeria", "Le Nigeria compte plus de 220 millions d'habitants."),
  Q("Quelle est la principale mégapole d'Afrique de l'Ouest ?", ["Dakar", "Lagos", "Abidjan", "Accra"], "Lagos", "Lagos, au Nigeria, compte plus de 15 millions d'habitants."),
  Q("Pourquoi dit-on que l'Afrique est « inégalement intégrée » à la mondialisation ?", ["Elle n'a aucun échange", "Certains espaces (ports, métropoles, zones minières) sont très connectés quand d'autres restent en marge", "Elle commerce uniquement avec l'Europe", "Elle est la première puissance commerciale"], "Certains espaces (ports, métropoles, zones minières) sont très connectés quand d'autres restent en marge", "La mondialisation sélectionne des espaces : littoraux, métropoles, gisements, au détriment d'espaces enclavés."),
]),
notion('G3-1', 1, D, 'geo-technopoles', [
  Q("Comment appelle-t-on un espace qui associe universités, laboratoires et entreprises de haute technologie, comme Sophia Antipolis ?", ["Un technopôle", "Une zone franche", "Un grand ensemble", "Un pôle rural"], "Un technopôle", "Le technopôle favorise l'innovation par la proximité entre recherche, formation et entreprises."),
  Q("Comment appelle-t-on les réseaux d'entreprises et de laboratoires d'un même domaine, labellisés par l'État depuis 2005 ?", ["Les pôles de compétitivité", "Les zones d'emploi", "Les bassins miniers", "Les métropoles d'équilibre"], "Les pôles de compétitivité", "Aerospace Valley (Toulouse-Bordeaux) ou Minalogic (Grenoble) en sont des exemples."),
  Q("Quelle est une conséquence de la mondialisation sur l'industrie française ?", ["La relocalisation de toutes les usines", "Des délocalisations vers des pays à bas coûts et une spécialisation dans le haut de gamme", "La disparition des services", "La fin des exportations"], "Des délocalisations vers des pays à bas coûts et une spécialisation dans le haut de gamme", "L'industrie française se recentre sur des secteurs à forte valeur ajoutée (aéronautique, luxe, pharmacie)."),
]),
notion('G3-3', 1, D, 'geo-france-dans-le-monde', [
  Q("Quel rang occupe la ZEE française parmi les plus grandes du monde ?", ["Premier", "Deuxième", "Dixième", "Vingtième"], "Deuxième", "Grâce à ses territoires ultramarins, la France possède la deuxième ZEE du monde, environ 10,2 millions de km²."),
  Q("De quel organe de l'ONU la France est-elle membre permanent ?", ["L'UNESCO", "Le Conseil de sécurité", "L'Assemblée générale seulement", "La Cour pénale internationale"], "Le Conseil de sécurité", "La France est l'un des cinq membres permanents du Conseil de sécurité, avec un droit de veto."),
  Q("Quelle organisation regroupe les pays ayant le français en partage ?", ["Le Commonwealth", "L'Organisation internationale de la francophonie", "L'Union africaine", "L'OCDE"], "L'Organisation internationale de la francophonie", "L'OIF rassemble des États et gouvernements partageant la langue française."),
  N("Combien de membres permanents compte le Conseil de sécurité de l'ONU ?", 5, "États-Unis, Russie, Chine, Royaume-Uni et France sont les cinq membres permanents."),
]),
notion('G5-2', 1, D, 'geo-nourrir-humanite', [
  Q("Comment appelle-t-on l'achat ou la location de vastes terres agricoles par des États ou des entreprises étrangères ?", ["L'accaparement des terres", "La réforme agraire", "Le remembrement", "La jachère"], "L'accaparement des terres", "Ce phénomène touche notamment l'Afrique : il peut priver les populations locales de terres vivrières."),
  Q("Comment appelle-t-on l'intensification agricole des années 1960-1970 en Asie, fondée sur des variétés à haut rendement ?", ["La révolution verte", "La révolution industrielle", "L'agroécologie", "La révolution numérique"], "La révolution verte", "Elle a fortement augmenté les rendements, mais avec un usage important d'engrais, de pesticides et d'eau."),
  Q("Quel organisme de l'ONU est chargé de l'alimentation et de l'agriculture ?", ["L'OMS", "La FAO", "L'UNESCO", "L'OMC"], "La FAO", "La FAO (Food and Agriculture Organization) lutte contre la faim et pour une agriculture durable."),
]),
notion('H3-1', 2, D, 'hg-processus-genocidaire', [
  Q("Quelle conférence de janvier 1942 organise la mise en œuvre de la « solution finale » ?", ["La conférence de Munich", "La conférence de Wannsee", "La conférence de Yalta", "La conférence de Potsdam"], "La conférence de Wannsee", "À Wannsee, des hauts responsables nazis coordonnent l'extermination des Juifs d'Europe."),
  Q("Comment appelle-t-on les unités mobiles qui fusillent massivement les Juifs à l'Est à partir de 1941 ?", ["Les Einsatzgruppen", "La Wehrmacht seule", "Les SA", "La Gestapo française"], "Les Einsatzgruppen", "Ces unités assassinent plus d'un million de Juifs par fusillades : on parle de « Shoah par balles »."),
  Q("Quel génocide les nazis commettent-ils aussi contre les Tsiganes ?", ["Le Porajmos (Samudaripen)", "L'Holodomor", "Le génocide arménien", "Le génocide des Tutsi"], "Le Porajmos (Samudaripen)", "Les Roms et Sinti sont persécutés et exterminés ; ce génocide est désigné par les termes Porajmos ou Samudaripen."),
]),
]

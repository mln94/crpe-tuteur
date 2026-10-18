# Histoire 4e · L'Europe et le monde au XIXe siècle : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H4-2', 0, F, 'hg4-usine', [
  Q("Comment appelle-t-on le grand bâtiment où des ouvriers produisent en série grâce à des machines ?", ["Une usine", "Un atelier d'artisan", "Une ferme", "Un comptoir"], "Une usine", "L'usine remplace peu à peu le travail à domicile."),
  Q("Quelle industrie est la première à se mécaniser en Angleterre ?", ["Le textile (coton)", "L'automobile", "L'aviation", "L'électronique"], "Le textile (coton)", "Les métiers à tisser mécaniques se multiplient."),
  Q("Qui fixe le rythme de travail des ouvriers dans l'usine ?", ["La machine et le patron", "Les ouvriers eux-mêmes", "Le curé", "Le maire"], "La machine et le patron", "Les journées dépassent souvent 12 heures."),
]),
notion('H4-2', 0, F, 'hg4-charbon-mines', [
  Q("Comment appelle-t-on l'ouvrier qui extrait le charbon au fond de la mine ?", ["Un mineur", "Un forgeron", "Un tisserand", "Un cheminot"], "Un mineur", "Le travail est dangereux et épuisant."),
  Q("Quelle région du nord de la France devient un grand bassin minier au XIXe siècle ?", ["Le Nord-Pas-de-Calais", "La Bretagne", "La Provence", "La Corse"], "Le Nord-Pas-de-Calais", "Les terrils en sont la trace."),
  Q("Quel roman d'Émile Zola raconte la vie et la grève des mineurs ?", ["Germinal", "Les Misérables", "Madame Bovary", "Le Rouge et le Noir"], "Germinal", "Il paraît en 1885."),
]),
notion('H4-2', 0, F, 'hg4-travail-enfants', [
  Q("Les enfants travaillent-ils dans les usines et les mines au début du XIXe siècle ?", ["Oui, dès 6 ou 8 ans", "Non, c'est interdit", "Seulement après 18 ans", "Seulement le dimanche"], "Oui, dès 6 ou 8 ans", "Ils sont moins payés que les adultes."),
  Q("Pourquoi les patrons emploient-ils des enfants ?", ["Ils sont moins payés et peuvent se glisser dans les petits espaces", "Ils sont plus forts", "La loi l'oblige", "Ils sont plus instruits"], "Ils sont moins payés et peuvent se glisser dans les petits espaces", "Le travail des enfants est peu à peu limité par la loi."),
  Q("Quelle loi de 1882 éloigne les enfants du travail en les obligeant à aller à l'école ?", ["La loi Ferry", "La loi Falloux", "Le Code civil", "La loi Guizot"], "La loi Ferry", "L'école devient obligatoire de 6 à 13 ans."),
]),
notion('H4-2', 0, F, 'hg4-villes-industrielles', [
  Q("Comment évoluent les villes avec l'industrialisation ?", ["Elles grandissent rapidement", "Elles se vident", "Elles restent identiques", "Elles disparaissent"], "Elles grandissent rapidement", "On parle d'urbanisation."),
  Q("Où vivent souvent les ouvriers dans les villes industrielles ?", ["Dans des quartiers pauvres et insalubres", "Dans des châteaux", "Dans les beaux quartiers", "À la campagne uniquement"], "Dans des quartiers pauvres et insalubres", "Les logements sont surpeuplés."),
  Q("Quelle ville anglaise, surnommée « Cottonopolis », est le symbole de la ville industrielle ?", ["Manchester", "Oxford", "Cambridge", "Bath"], "Manchester", "Elle vit de l'industrie du coton."),
]),
notion('H4-2', 0, F, 'hg4-inventions-xixe', [
  Q("Qui invente le télégraphe électrique et un alphabet de points et de traits ?", ["Samuel Morse", "Thomas Edison", "Graham Bell", "James Watt"], "Samuel Morse", "Le code Morse permet de communiquer à distance."),
  Q("Quel inventeur américain met au point l'ampoule électrique ?", ["Thomas Edison", "Louis Pasteur", "Nicéphore Niépce", "Gustave Eiffel"], "Thomas Edison", "Il dépose plus de mille brevets."),
  Q("Quels frères français inventent le cinématographe en 1895 ?", ["Les frères Lumière", "Les frères Montgolfier", "Les frères Wright", "Les frères Goncourt"], "Les frères Lumière", "Leur première projection publique a lieu à Paris."),
]),
notion('H4-2', 0, F, 'hg4-tour-eiffel', [
  N("Pour quelle Exposition universelle la tour Eiffel est-elle construite ?", 1889, "Elle célèbre aussi le centenaire de la Révolution."),
  Q("En quel matériau est construite la tour Eiffel ?", ["En fer", "En béton", "En pierre", "En bois"], "En fer", "Elle symbolise le progrès industriel."),
  Q("À quoi servent les Expositions universelles du XIXe siècle ?", ["À montrer les progrès techniques et la puissance des pays", "À vendre des esclaves", "À élire le président", "À organiser les Jeux olympiques"], "À montrer les progrès techniques et la puissance des pays", "Elles attirent des millions de visiteurs."),
]),
notion('H4-2', 0, F, 'hg4-chemin-de-fer', [
  Q("Quel ingénieur anglais construit l'une des premières locomotives à vapeur efficaces ?", ["George Stephenson", "James Watt", "Isambard Brunel", "Gustave Eiffel"], "George Stephenson", "Sa « Rocket » est célèbre en 1829."),
  Q("Comment évolue la durée d'un voyage Paris-Marseille grâce au train ?", ["Elle passe de plusieurs jours à quelques heures", "Elle augmente", "Elle ne change pas", "Elle double"], "Elle passe de plusieurs jours à quelques heures", "Le train transforme le rapport à l'espace."),
  Q("Quelle conséquence le chemin de fer a-t-il sur l'industrie ?", ["Il stimule la production de fer, d'acier et de charbon", "Il fait baisser la production", "Il supprime les usines", "Il n'a aucun effet"], "Il stimule la production de fer, d'acier et de charbon", "Il faut des rails, des locomotives et du combustible."),
]),
notion('H4-2', 0, F, 'hg4-bourgeoisie', [
  Q("Quel groupe social s'enrichit grâce à l'industrie au XIXe siècle ?", ["La bourgeoisie", "La noblesse", "Le clergé", "La paysannerie"], "La bourgeoisie", "Elle possède les usines, les banques et les commerces."),
  Q("Comment appelle-t-on le propriétaire d'une usine ?", ["Un patron", "Un ouvrier", "Un contremaître", "Un apprenti"], "Un patron", "On parle aussi d'industriel."),
  Q("Quelle famille dirige les grandes usines du Creusot au XIXe siècle ?", ["Les Schneider", "Les Médicis", "Les Bourbons", "Les Rothschild"], "Les Schneider", "Le Creusot devient une ville-usine."),
]),
notion('H4-2', 1, F, 'hg4-algerie', [
  Q("Quelle ville d'Algérie les Français prennent-ils en 1830 ?", ["Alger", "Oran", "Constantine", "Tunis"], "Alger", "C'est le début de la conquête de l'Algérie."),
  Q("Quel chef algérien résiste à la conquête française jusqu'en 1847 ?", ["L'émir Abd el-Kader", "Bourguiba", "Mohammed V", "Samory Touré"], "L'émir Abd el-Kader", "Il est un héros de la résistance algérienne."),
  Q("Quels territoires la France conquiert-elle dans la seconde moitié du XIXe siècle ?", ["En Afrique et en Asie", "En Amérique du Nord", "En Australie", "En Europe de l'Est"], "En Afrique et en Asie", "L'empire colonial devient le deuxième du monde."),
]),
notion('H4-2', 1, F, 'hg4-raisons-colonisation', [
  Q("Quelle raison économique pousse les Européens à coloniser ?", ["Trouver des matières premières et des débouchés", "Fuir la guerre", "Trouver de la neige", "Acheter des usines"], "Trouver des matières premières et des débouchés", "Les colonies doivent enrichir la métropole."),
  Q("Quelle raison politique pousse les pays européens à coloniser ?", ["Montrer leur puissance face aux autres pays", "Réduire leur armée", "Plaire aux colonisés", "Respecter la paix"], "Montrer leur puissance face aux autres pays", "La rivalité entre puissances est forte."),
  Q("Comment appelle-t-on le pays qui possède des colonies ?", ["La métropole", "Le protectorat", "Le comptoir", "La province"], "La métropole", "Elle dirige ses colonies."),
]),
notion('H4-2', 1, F, 'hg4-explorateurs-afrique', [
  Q("Quel explorateur britannique parcourt l'Afrique australe et centrale au XIXe siècle ?", ["David Livingstone", "James Cook", "Christophe Colomb", "Marco Polo"], "David Livingstone", "Il cherche les sources du Nil."),
  Q("Quel explorateur d'origine italienne prend possession du Congo au nom de la France ?", ["Pierre Savorgnan de Brazza", "Henry Stanley", "René Caillié", "Jacques Cartier"], "Pierre Savorgnan de Brazza", "La ville de Brazzaville porte son nom."),
  Q("Quelle formule célèbre aurait prononcée Stanley en retrouvant Livingstone ?", ["« Docteur Livingstone, je présume ? »", "« Veni, vidi, vici »", "« Terre ! Terre ! »", "« Eurêka ! »"], "« Docteur Livingstone, je présume ? »", "La rencontre a lieu en 1871."),
]),
notion('H4-2', 1, F, 'hg4-vie-colonies', [
  Q("Quels produits les colonies fournissent-elles à l'Europe ?", ["Matières premières : coton, caoutchouc, arachide, minerais", "Voitures", "Ordinateurs", "Machines à vapeur"], "Matières premières : coton, caoutchouc, arachide, minerais", "Ils alimentent les usines européennes."),
  Q("Quelle est la situation des colonisés par rapport aux colons ?", ["Ils ont beaucoup moins de droits", "Ils ont les mêmes droits", "Ils dirigent la colonie", "Ils ont plus de droits"], "Ils ont beaucoup moins de droits", "La société coloniale est inégalitaire."),
  Q("Comment appelle-t-on le travail imposé aux colonisés sans salaire ou presque ?", ["Le travail forcé", "Le travail volontaire", "Le télétravail", "Le compagnonnage"], "Le travail forcé", "Il sert à construire routes et chemins de fer."),
]),
notion('H4-2', 0, F, 'hg4-ouvriers-conditions', [
  Q("Combien d'heures par jour travaille un ouvrier au milieu du XIXe siècle ?", ["Souvent 12 à 15 heures", "4 heures", "7 heures", "35 heures par semaine"], "Souvent 12 à 15 heures", "Le repos hebdomadaire n'est pas garanti."),
  Q("Comment appelle-t-on l'arrêt collectif du travail pour obtenir de meilleures conditions ?", ["La grève", "Le chômage", "Les congés", "La retraite"], "La grève", "Elle est autorisée en France en 1864."),
  Q("Comment appelle-t-on l'association d'ouvriers qui défend leurs intérêts ?", ["Un syndicat", "Une corporation", "Une banque", "Une académie"], "Un syndicat", "Les syndicats sont légalisés en 1884."),
]),
# ══ Intermédiaire ══
notion('H4-2', 0, I, 'hg4i-capitalisme', [
  Q("Comment appelle-t-on le système économique fondé sur la propriété privée des moyens de production et la recherche du profit ?", ["Le capitalisme", "Le socialisme", "Le féodalisme", "Le mercantilisme"], "Le capitalisme", "Il s'affirme avec l'industrialisation."),
  Q("Quel type d'entreprise permet de réunir des capitaux en vendant des actions ?", ["La société anonyme", "L'atelier familial", "La corporation", "La coopérative agricole"], "La société anonyme", "Les actions s'échangent en Bourse."),
  Q("Quel rôle jouent les banques dans l'industrialisation ?", ["Elles prêtent l'argent nécessaire aux investissements", "Elles fabriquent les machines", "Elles interdisent les usines", "Elles payent les ouvriers directement"], "Elles prêtent l'argent nécessaire aux investissements", "Le Crédit lyonnais ou la Société générale sont créés sous le Second Empire."),
]),
notion('H4-2', 0, I, 'hg4i-acier-electricite', [
  Q("Quel procédé, inventé par Bessemer, permet de produire de l'acier en grande quantité ?", ["Le convertisseur", "Le haut fourneau au bois", "La machine à vapeur", "Le métier Jacquard"], "Le convertisseur", "L'acier remplace peu à peu le fer."),
  Q("Quel moteur, inventé à la fin du XIXe siècle, permet l'essor de l'automobile ?", ["Le moteur à explosion", "La machine à vapeur", "Le moteur électrique", "Le moulin"], "Le moteur à explosion", "Il fonctionne au pétrole raffiné."),
  Q("Quel pays devient la première puissance industrielle mondiale à la fin du XIXe siècle ?", ["Les États-Unis", "La France", "L'Espagne", "La Russie"], "Les États-Unis", "L'Allemagne dépasse aussi le Royaume-Uni dans certains secteurs."),
]),
notion('H4-2', 0, I, 'hg4i-socialisme', [
  Q("Quel penseur allemand analyse le capitalisme dans Le Capital ?", ["Karl Marx", "Adam Smith", "Victor Hugo", "Bismarck"], "Karl Marx", "Le premier tome paraît en 1867."),
  Q("Quelle organisation internationale ouvrière est fondée à Londres en 1864 ?", ["La Première Internationale (AIT)", "L'ONU", "La SDN", "La CGT"], "La Première Internationale (AIT)", "Elle réunit des militants de plusieurs pays."),
  Q("Quelle confédération syndicale est créée en France en 1895 ?", ["La CGT", "La CFDT", "Le MEDEF", "FO"], "La CGT", "Confédération générale du travail."),
]),
notion('H4-2', 0, I, 'hg4i-paternalisme', [
  Q("Comment appelle-t-on l'attitude d'un patron qui loge, soigne et éduque ses ouvriers pour mieux les contrôler ?", ["Le paternalisme", "Le syndicalisme", "Le libéralisme", "Le socialisme"], "Le paternalisme", "Les Schneider au Creusot en sont un exemple."),
  Q("Quel industriel construit un « familistère » pour ses ouvriers à Guise ?", ["Jean-Baptiste Godin", "Eugène Schneider", "Louis Renault", "André Citroën"], "Jean-Baptiste Godin", "Il s'inspire des idées de Fourier."),
  Q("Comment appelle-t-on les logements construits par les patrons près des usines ou des mines ?", ["Les cités ouvrières (corons dans le Nord)", "Les HLM", "Les hôtels particuliers", "Les villas"], "Les cités ouvrières (corons dans le Nord)", "Elles appartiennent à l'entreprise."),
]),
notion('H4-2', 0, I, 'hg4i-exode-rural', [
  Q("Pourquoi de nombreux paysans quittent-ils les campagnes au XIXe siècle ?", ["Pour trouver du travail mieux payé en ville", "Pour fuir la mer", "Parce que les villes sont moins peuplées", "Pour devenir nobles"], "Pour trouver du travail mieux payé en ville", "La mécanisation agricole réduit aussi les besoins en bras."),
  Q("Quel pays européen reste longtemps plus rural que le Royaume-Uni ?", ["La France", "La Belgique", "L'Angleterre", "Les Pays-Bas"], "La France", "La moitié des Français vivent encore à la campagne en 1914."),
  Q("Comment appelle-t-on le paysan venu en ville pour une saison, comme les maçons de la Creuse ?", ["Un migrant saisonnier", "Un colon", "Un rentier", "Un notable"], "Un migrant saisonnier", "Beaucoup finissent par s'installer en ville."),
]),
notion('H4-2', 0, I, 'hg4i-haussmann', [
  Q("Quel préfet transforme Paris sous le Second Empire ?", ["Le baron Haussmann", "Gustave Eiffel", "Jules Ferry", "Colbert"], "Le baron Haussmann", "Il perce de larges avenues."),
  Q("Quel est l'un des buts des grands boulevards haussmanniens ?", ["Assainir la ville et faciliter le maintien de l'ordre", "Créer des champs", "Construire des remparts", "Loger tous les ouvriers au centre"], "Assainir la ville et faciliter le maintien de l'ordre", "Les ouvriers sont repoussés vers les faubourgs."),
  Q("Quel équipement Haussmann développe-t-il sous les rues de Paris ?", ["Les égouts", "Le métro", "Les catacombes", "Les parkings"], "Les égouts", "L'ingénieur Belgrand modernise l'eau et l'assainissement."),
]),
notion('H4-2', 1, I, 'hg4i-afrique-1914', [
  Q("Quels sont les deux seuls États africains indépendants en 1914 ?", ["L'Éthiopie et le Liberia", "Le Maroc et l'Égypte", "Le Congo et le Kenya", "L'Algérie et la Tunisie"], "L'Éthiopie et le Liberia", "Le reste de l'Afrique est colonisé."),
  Q("Quelle victoire éthiopienne de 1896 stoppe la conquête italienne ?", ["Adoua", "Isandhlwana", "Omdurman", "Fachoda"], "Adoua", "C'est une victoire africaine majeure."),
  Q("Quel incident oppose la France et le Royaume-Uni au Soudan en 1898 ?", ["La crise de Fachoda", "L'affaire Dreyfus", "La crise d'Agadir", "La guerre des Boers"], "La crise de Fachoda", "La France doit céder."),
]),
notion('H4-2', 1, I, 'hg4i-empire-britannique', [
  Q("Quel territoire est surnommé « le joyau de la Couronne » britannique ?", ["L'Inde", "Le Canada", "L'Australie", "L'Égypte"], "L'Inde", "La reine Victoria en devient impératrice en 1877."),
  Q("Quelle expression désigne l'empire britannique du XIXe siècle ?", ["« L'empire sur lequel le soleil ne se couche jamais »", "« Le pays du soleil levant »", "« La vieille Europe »", "« Le Nouveau Monde »"], "« L'empire sur lequel le soleil ne se couche jamais »", "Il s'étend sur tous les continents."),
  N("En quelle année est inauguré le canal de Suez ?", 1869, "Il raccourcit la route maritime vers l'Inde."),
]),
notion('H4-2', 1, I, 'hg4i-resistances-colonisation', [
  Q("Quel chef africain résiste aux Français en Afrique de l'Ouest jusqu'en 1898 ?", ["Samory Touré", "Abd el-Kader", "Toussaint Louverture", "Mandela"], "Samory Touré", "Il est capturé puis exilé au Gabon."),
  Q("Quelle reine de Madagascar est exilée après la conquête française ?", ["Ranavalona III", "Victoria", "Cléopâtre", "Nzinga"], "Ranavalona III", "Elle est exilée en Algérie."),
  Q("Quelle révolte de 1871 en Kabylie est réprimée par la France ?", ["L'insurrection de Mokrani", "La révolte des Boxers", "La révolte des Cipayes", "La révolte des Canuts"], "L'insurrection de Mokrani", "Des terres sont confisquées au profit des colons."),
]),
notion('H4-2', 1, I, 'hg4i-exposition-coloniale', [
  Q("Comment appelle-t-on les spectacles où des colonisés étaient exhibés devant le public européen ?", ["Les « zoos humains »", "Les foires agricoles", "Les Expositions universelles des sciences", "Les cirques équestres"], "Les « zoos humains »", "Ils diffusent des préjugés racistes."),
  N("En quelle année se tient la grande Exposition coloniale de Paris, au bois de Vincennes ?", 1931, "Elle attire des millions de visiteurs."),
  Q("Quelle idée ces expositions diffusent-elles auprès des Européens ?", ["Une prétendue supériorité européenne", "L'égalité des peuples", "L'indépendance des colonies", "La fin de l'esclavage"], "Une prétendue supériorité européenne", "Elles servent la propagande coloniale."),
]),
notion('H4-2', 0, I, 'hg4i-agriculture-xixe', [
  Q("Quelle maladie de la pomme de terre provoque la grande famine irlandaise ?", ["Le mildiou", "Le phylloxéra", "La peste", "La rouille"], "Le mildiou", "C'est un champignon parasite."),
  Q("Quel insecte détruit une grande partie du vignoble français à partir de 1863 ?", ["Le phylloxéra", "Le doryphore", "Le criquet", "Le hanneton"], "Le phylloxéra", "On replante avec des plants américains résistants."),
  Q("Quels engrais permettent d'augmenter les rendements agricoles au XIXe siècle ?", ["Les engrais chimiques", "Les engrais nucléaires", "Aucun", "Le sel"], "Les engrais chimiques", "La chimie transforme l'agriculture."),
]),
notion('H4-2', 0, I, 'hg4i-religion-ouvriers', [
  Q("Quel pape publie en 1891 l'encyclique Rerum novarum sur la condition ouvrière ?", ["Léon XIII", "Pie IX", "Jean-Paul II", "Grégoire VII"], "Léon XIII", "C'est le texte fondateur de la doctrine sociale de l'Église."),
  Q("Que condamne Rerum novarum ?", ["À la fois le socialisme et les excès du capitalisme", "Uniquement les grèves", "La science", "L'école publique"], "À la fois le socialisme et les excès du capitalisme", "Elle demande un juste salaire."),
  Q("Quel médecin enquête en 1840 sur l'état physique et moral des ouvriers du textile ?", ["Louis-René Villermé", "Louis Pasteur", "Claude Bernard", "Charcot"], "Louis-René Villermé", "Son rapport inspire la loi de 1841."),
]),
# ══ Avancé ══
notion('H4-2', 0, D, 'hg4d-luddisme', [
  Q("Comment appelle-t-on le mouvement d'ouvriers anglais qui brisent les machines vers 1811-1812 ?", ["Le luddisme", "Le chartisme", "Le fouriérisme", "Le saint-simonisme"], "Le luddisme", "Ils voient dans les machines la cause de leur misère."),
  Q("Quelle révolte d'ouvriers de la soie éclate à Lyon en 1831 ?", ["La révolte des Canuts", "La Commune", "La Jacquerie", "La révolte des Croquants"], "La révolte des Canuts", "Leur devise : « Vivre en travaillant ou mourir en combattant »."),
  Q("Quel mouvement anglais réclame dans les années 1840 le suffrage universel masculin ?", ["Le chartisme", "Le luddisme", "Le travaillisme", "Le fabianisme"], "Le chartisme", "Il tire son nom de la « Charte du peuple »."),
]),
notion('H4-2', 0, D, 'hg4d-libre-echange', [
  N("En quelle année le traité Cobden-Chevalier instaure-t-il le libre-échange entre la France et le Royaume-Uni ?", 1860, "Il réduit fortement les droits de douane."),
  Q("Comment appelle-t-on une politique qui taxe les importations pour protéger l'industrie nationale ?", ["Le protectionnisme", "Le libre-échange", "Le mercantilisme bancaire", "Le colbertisme agricole"], "Le protectionnisme", "La France y revient avec les tarifs Méline en 1892."),
  Q("Quelle crise économique frappe l'Europe à partir de 1873 ?", ["La Grande Dépression", "La crise de 1929", "Le krach de 1987", "La crise des subprimes"], "La Grande Dépression", "Elle dure jusqu'au milieu des années 1890."),
]),
notion('H4-2', 0, D, 'hg4d-saint-simoniens', [
  Q("Quel courant de pensée, influent sous le Second Empire, voit dans l'industrie et les réseaux la clé du progrès ?", ["Le saint-simonisme", "Le luddisme", "L'anarchisme", "Le physiocratisme"], "Le saint-simonisme", "Les frères Pereire en sont proches."),
  Q("Quel ingénieur français dirige le percement du canal de Suez ?", ["Ferdinand de Lesseps", "Gustave Eiffel", "Haussmann", "Sadi Carnot"], "Ferdinand de Lesseps", "Il échoue ensuite à Panama."),
  Q("Quel scandale financier éclate en 1892 autour d'un canal en Amérique centrale ?", ["Le scandale de Panama", "L'affaire Dreyfus", "L'affaire Stavisky", "Le krach de l'Union générale"], "Le scandale de Panama", "Des parlementaires ont été corrompus."),
]),
notion('H4-2', 0, D, 'hg4d-lois-sociales', [
  N("En quelle année une loi limite-t-elle la journée de travail à 10 heures en Angleterre (Ten Hours Act) ?", 1847, "Elle concerne les femmes et les enfants du textile."),
  Q("Quel chancelier allemand crée les premières assurances sociales obligatoires dans les années 1880 ?", ["Bismarck", "Guillaume II", "Marx", "Metternich"], "Bismarck", "Maladie, accidents, vieillesse."),
  Q("Quelle loi française de 1898 rend le patron responsable des accidents du travail ?", ["La loi sur les accidents du travail", "La loi Le Chapelier", "La loi Falloux", "La loi Ferry"], "La loi sur les accidents du travail", "L'ouvrier blessé est indemnisé sans avoir à prouver une faute."),
]),
notion('H4-2', 0, D, 'hg4d-commune', [
  N("En quelle année a lieu la Commune de Paris ?", 1871, "Elle dure de mars à mai."),
  Q("Comment appelle-t-on l'écrasement de la Commune par l'armée versaillaise fin mai 1871 ?", ["La Semaine sanglante", "Les Trois Glorieuses", "Les journées de Juin", "La Terreur"], "La Semaine sanglante", "Des milliers de communards sont tués."),
  Q("Quelle institutrice communarde est déportée en Nouvelle-Calédonie ?", ["Louise Michel", "George Sand", "Olympe de Gouges", "Marie Curie"], "Louise Michel", "Elle devient une figure de l'anarchisme."),
]),
notion('H4-2', 0, D, 'hg4d-nations-europe', [
  N("En quelle année est proclamé l'Empire allemand dans la galerie des Glaces de Versailles ?", 1871, "Guillaume Ier en devient l'empereur."),
  Q("Quel homme d'État piémontais dirige l'unification italienne ?", ["Cavour", "Mazzini", "Bismarck", "Metternich"], "Cavour", "Garibaldi conquiert le Sud avec ses Chemises rouges."),
  Q("Quel pays obtient son indépendance de l'Empire ottoman en 1830 ?", ["La Grèce", "La Bulgarie", "La Roumanie", "La Serbie"], "La Grèce", "Les Européens l'ont soutenue."),
]),
notion('H4-2', 1, D, 'hg4d-code-indigenat', [
  Q("Que permet le code de l'indigénat aux administrateurs coloniaux ?", ["Punir les colonisés sans jugement pour des infractions spécifiques", "Donner la citoyenneté aux colonisés", "Supprimer l'impôt", "Élire des députés"], "Punir les colonisés sans jugement pour des infractions spécifiques", "Il est aboli en 1946."),
  Q("Quel décret de 1870 donne la citoyenneté française aux juifs d'Algérie ?", ["Le décret Crémieux", "Le décret d'Allarde", "L'édit de Nantes", "Le sénatus-consulte"], "Le décret Crémieux", "Les musulmans d'Algérie en restent exclus."),
  Q("Comment l'Algérie est-elle administrée à partir de 1848 ?", ["Elle est divisée en départements français", "Elle devient un protectorat", "Elle devient indépendante", "Elle est confiée à une compagnie"], "Elle est divisée en départements français", "Alger, Oran et Constantine."),
]),
notion('H4-2', 1, D, 'hg4d-protectorat', [
  Q("Qu'est-ce qu'un protectorat ?", ["Un territoire qui garde son souverain mais est contrôlé par une puissance étrangère", "Une colonie de peuplement", "Un pays indépendant", "Un département"], "Un territoire qui garde son souverain mais est contrôlé par une puissance étrangère", "La Tunisie (1881) et le Maroc (1912) sont des protectorats français."),
  N("En quelle année le Maroc devient-il un protectorat français ?", 1912, "Le résident général Lyautey l'administre."),
  Q("Quel pays devient protectorat français en 1881 par le traité du Bardo ?", ["La Tunisie", "Le Maroc", "L'Égypte", "La Libye"], "La Tunisie", "Le bey reste en place."),
]),
notion('H4-2', 1, D, 'hg4d-congo-leopold', [
  Q("Quel roi possède le Congo à titre personnel de 1885 à 1908 ?", ["Léopold II de Belgique", "Guillaume II", "Victor-Emmanuel II", "Napoléon III"], "Léopold II de Belgique", "On parle de l'« État indépendant du Congo »."),
  Q("Quelle ressource est exploitée par le travail forcé dans le Congo de Léopold II ?", ["Le caoutchouc", "Le pétrole", "Le café", "Le coton"], "Le caoutchouc", "Les violences font des millions de morts."),
  Q("Que se passe-t-il en 1908 face au scandale international ?", ["Le Congo est transféré à l'État belge", "Le Congo devient indépendant", "Le Congo est vendu à la France", "Rien"], "Le Congo est transféré à l'État belge", "Il devient le Congo belge."),
]),
notion('H4-2', 1, D, 'hg4d-asie-colonisee', [
  Q("Quelle guerre oppose le Royaume-Uni à la Chine de 1839 à 1842 ?", ["La guerre de l'opium", "La guerre des Boxers", "La guerre de Crimée", "La guerre des Boers"], "La guerre de l'opium", "La Chine doit céder Hong Kong."),
  Q("Quelle grande révolte de soldats indiens éclate contre les Britanniques en 1857 ?", ["La révolte des Cipayes", "La révolte des Boxers", "La révolte de Mokrani", "La révolte des Taiping"], "La révolte des Cipayes", "Après elle, la Couronne gouverne directement l'Inde."),
  Q("Quel pays d'Asie se modernise rapidement à partir de 1868 pour échapper à la colonisation ?", ["Le Japon (ère Meiji)", "La Chine", "L'Inde", "Le Vietnam"], "Le Japon (ère Meiji)", "Il devient lui-même une puissance coloniale."),
]),
notion('H4-2', 1, D, 'hg4d-anticolonialisme', [
  Q("Quel député socialiste s'oppose à la colonisation et à Jules Ferry ?", ["Clemenceau, puis Jaurès", "Lyautey", "Gallieni", "Thiers"], "Clemenceau, puis Jaurès", "Clemenceau s'oppose à Ferry dès 1885."),
  Q("Quel écrivain dénonce les abus de la colonisation au Congo dans Voyage au Congo (1927) ?", ["André Gide", "Victor Hugo", "Émile Zola", "Jules Verne"], "André Gide", "Le livre fait scandale."),
  Q("Quel argument Clemenceau oppose-t-il à Ferry en 1885 ?", ["Il refuse l'idée de « races supérieures » et veut se concentrer sur la revanche contre l'Allemagne", "Il veut coloniser l'Europe", "Il réclame plus de colonies", "Il veut vendre l'Algérie"], "Il refuse l'idée de « races supérieures » et veut se concentrer sur la revanche contre l'Allemagne", "Le débat est vif à la Chambre."),
]),
notion('H4-2', 1, D, 'hg4d-guerre-boers', [
  Q("Quelle guerre oppose le Royaume-Uni aux colons d'origine néerlandaise d'Afrique du Sud (1899-1902) ?", ["La guerre des Boers", "La guerre des Zoulous", "La guerre de Crimée", "La guerre de Sécession"], "La guerre des Boers", "Les Britanniques y utilisent des camps de concentration."),
  Q("Quelle ressource attise la convoitise britannique en Afrique du Sud ?", ["L'or et les diamants", "Le pétrole", "Le café", "Le coton"], "L'or et les diamants", "Les mines du Transvaal sont immenses."),
  Q("Quel homme d'affaires britannique rêve d'un empire « du Cap au Caire » ?", ["Cecil Rhodes", "Henry Stanley", "Livingstone", "Disraeli"], "Cecil Rhodes", "La Rhodésie porte son nom."),
]),
notion('H4-2', 0, D, 'hg4d-migrations-europe', [
  Q("Combien d'Européens environ émigrent-ils entre 1815 et 1914 ?", ["Entre 50 et 60 millions", "Environ 500 000", "Environ 5 millions", "Plus de 300 millions"], "Entre 50 et 60 millions", "La plupart partent vers les Amériques."),
  Q("Par quelle île les immigrants arrivent-ils à New York à partir de 1892 ?", ["Ellis Island", "Long Island", "Staten Island", "Manhattan"], "Ellis Island", "Ils y subissent des contrôles médicaux."),
  Q("Quel massacre de travailleurs italiens a lieu à Aigues-Mortes en 1893 ?", ["Des ouvriers des salins sont tués par des ouvriers français", "Un naufrage", "Une épidémie", "Un incendie d'usine"], "Des ouvriers des salins sont tués par des ouvriers français", "La xénophobie touche aussi la France."),
]),
notion('H4-2', 1, D, 'hg4d-mission-civilisatrice', [
  Q("Quel écrivain britannique parle du « fardeau de l'homme blanc » en 1899 ?", ["Rudyard Kipling", "Charles Dickens", "Oscar Wilde", "Lewis Carroll"], "Rudyard Kipling", "Le poème justifie l'impérialisme."),
  Q("Quel maréchal français est le premier résident général au Maroc ?", ["Lyautey", "Gallieni", "Bugeaud", "Foch"], "Lyautey", "Il pratique une politique d'« association »."),
  Q("Quel maréchal mène une conquête brutale de l'Algérie dans les années 1840 ?", ["Bugeaud", "Lyautey", "Joffre", "Pétain"], "Bugeaud", "Les « enfumades » en sont un exemple."),
]),
]

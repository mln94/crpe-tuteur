# Anglais : notions pour les axes culturels de chaque classe (programme du collège, annexe 3), au moins 9 questions par axe
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Classe de 6e ══
# Pays et paysages
notion('C6-3', 0, I, 'ang-paysages-anglophones', [
  Q("Quel grand fleuve traverse les États-Unis du nord au sud jusqu'au golfe du Mexique ?", ["Le Mississippi", "La Tamise", "Le Saint-Laurent", "Le Shannon"], "Le Mississippi", "Mark Twain a raconté la vie sur ce fleuve dans Les Aventures de Huckleberry Finn."),
  Q("Comment appelle-t-on la région montagneuse du nord de l'Écosse, avec ses lochs ?", ["Les Highlands", "Les Midlands", "Les Cotswolds", "Les Lowlands"], "Les Highlands", "Le loch Ness s'y trouve."),
  Q("Quel pays anglophone d'Afrique de l'Est est célèbre pour ses parcs nationaux et ses safaris, comme le Masai Mara ?", ["Le Kenya", "L'Égypte", "Le Maroc", "Le Sénégal"], "Le Kenya", "On y observe lions, éléphants, girafes et zèbres."),
]),
# Imaginaire, contes et légendes
notion('C6-4', 0, F, 'ang-magie-fiction', [
  Q("Quel célèbre magicien conseille le roi Arthur dans les légendes britanniques ?", ["Merlin", "Gandalf", "Dumbledore", "Prospero"], "Merlin", "Les légendes arthuriennes sont un motif récurrent de la fiction britannique."),
  Q("Quelle autrice britannique a créé le jeune sorcier Harry Potter ?", ["J. K. Rowling", "Agatha Christie", "Jane Austen", "Beatrix Potter"], "J. K. Rowling", "Le premier tome paraît en 1997."),
  Q("Comment dit-on « sorcière » en anglais ?", ["A witch", "A wizard", "A ghost", "A fairy"], "A witch", "A wizard est un sorcier, a fairy une fée, a ghost un fantôme."),
]),
notion('C6-4', 0, I, 'ang-legendes-irlande-dragons', [
  Q("Dans le folklore irlandais, quel petit personnage cache un chaudron d'or au pied de l'arc-en-ciel ?", ["Le leprechaun", "Le hobbit", "Le gobelin", "Le troll"], "Le leprechaun", "Il porte souvent un habit vert et un chapeau."),
  Q("Quel animal fabuleux figure sur le drapeau du pays de Galles ?", ["Un dragon rouge", "Une licorne", "Un lion", "Un griffon"], "Un dragon rouge", "Y Ddraig Goch, le dragon rouge, est l'emblème du pays."),
  Q("Quel saint, patron de l'Angleterre, terrasse un dragon dans la légende ?", ["Saint George", "Saint Patrick", "Saint Andrew", "Saint David"], "Saint George", "La croix rouge de saint George figure sur le drapeau anglais."),
]),
notion('C6-4', 0, D, 'ang-dr-seuss', [
  Q("Quel auteur américain a écrit The Cat in the Hat (Le Chat chapeauté) ?", ["Dr. Seuss", "Roald Dahl", "Lewis Carroll", "Mark Twain"], "Dr. Seuss", "Ses albums jouent avec les rimes et la musicalité de l'anglais."),
  Q("Quel personnage de Dr. Seuss, ronchon et vert, veut voler Noël ?", ["Le Grinch", "Le Lorax", "Shrek", "Gollum"], "Le Grinch", "How the Grinch Stole Christmas! paraît en 1957."),
  Q("Quel auteur britannique a imaginé Alice au pays des merveilles (1865) ?", ["Lewis Carroll", "Charles Dickens", "Oscar Wilde", "Rudyard Kipling"], "Lewis Carroll", "Le livre est riche en jeux de mots et en nonsense."),
]),
# Arts et expression des sentiments
notion('C6-5', 0, F, 'ang-fetes-fin-annee', [
  Q("Comment appelle-t-on, au Royaume-Uni, le jour qui suit Noël, le 26 décembre ?", ["Boxing Day", "Thanksgiving", "Bonfire Night", "Halloween"], "Boxing Day", "C'est un jour férié, connu aussi pour ses soldes."),
  Q("Quel personnage apporte les cadeaux de Noël dans les pays anglophones ?", ["Santa Claus (Father Christmas)", "The Easter Bunny", "The Tooth Fairy", "Jack-o'-lantern"], "Santa Claus (Father Christmas)", "Les enfants suspendent une chaussette (stocking) pour ses cadeaux."),
  Q("Quelle plante décore les maisons à Noël, et sous laquelle on s'embrasse ?", ["Le gui (mistletoe)", "Le houx (holly)", "Le lierre (ivy)", "Le trèfle (shamrock)"], "Le gui (mistletoe)", "Le houx est aussi une décoration de Noël."),
]),
notion('C6-5', 0, I, 'ang-musicalite-langue', [
  Q("Dans quel film musical Mary Poppins chante-t-elle « Supercalifragilisticexpialidocious » ?", ["Mary Poppins", "The Sound of Music", "Grease", "Annie"], "Mary Poppins", "Ce mot inventé joue sur la musicalité de la langue anglaise."),
  Q("Comment appelle-t-on une phrase difficile à prononcer, comme « She sells seashells by the seashore » ?", ["Un tongue twister (virelangue)", "Un proverbe", "Un slogan", "Une devinette"], "Un tongue twister (virelangue)", "Les virelangues entraînent la prononciation."),
  Q("Comment appelle-t-on une comptine traditionnelle anglaise pour enfants, comme « Twinkle, Twinkle, Little Star » ?", ["A nursery rhyme", "A ballad", "A sonnet", "A limerick"], "A nursery rhyme", "Les nursery rhymes accompagnent l'apprentissage des sons et du rythme."),
]),
# ══ Classe de 5e ══
# Portrait, autoportrait
notion('C5-1', 0, F, 'ang-yearbook', [
  Q("Qu'est-ce qu'un yearbook dans les écoles américaines ?", ["Un album annuel avec les photos et les souvenirs des élèves", "Un manuel de mathématiques", "Un calendrier des vacances", "Un carnet de notes"], "Un album annuel avec les photos et les souvenirs des élèves", "On y élit parfois « the most likely to succeed »."),
  Q("Comment dit-on « autoportrait » en anglais ?", ["A self-portrait", "A selfie-picture", "An own-portrait", "A me-portrait"], "A self-portrait", "Le selfie est la version numérique et instantanée de l'autoportrait."),
  Q("Comment demande-t-on « À quoi ressemble-t-il ? » en anglais ?", ["What does he look like?", "How does he like?", "What is he like to look?", "Who does he look?"], "What does he look like?", "« What is he like? » interroge plutôt sur le caractère."),
]),
notion('C5-1', 0, I, 'ang-portraits-britanniques', [
  Q("Quel musée de Londres rassemble les portraits des grandes figures de l'histoire britannique ?", ["La National Portrait Gallery", "Le British Museum", "La Tate Modern", "Le Science Museum"], "La National Portrait Gallery", "Elle a été fondée en 1856."),
  Q("Quel peintre allemand, installé à Londres, réalise les célèbres portraits du roi Henri VIII ?", ["Hans Holbein le Jeune", "Rembrandt", "Albrecht Dürer", "Van Dyck"], "Hans Holbein le Jeune", "Ses portraits fixent l'image royale des Tudor."),
  Q("Quel genre de portrait représente une famille réunie, comme les familles présidentielles américaines ?", ["Un portrait de groupe", "Une nature morte", "Un paysage", "Une marine"], "Un portrait de groupe", "Les photos officielles construisent une image publique."),
]),
notion('C5-1', 0, D, 'ang-familles-presidentielles', [
  Q("Quelle famille américaine compte deux présidents, père et fils, au XXe et au XXIe siècle ?", ["Les Bush", "Les Kennedy", "Les Obama", "Les Roosevelt"], "Les Bush", "George H. W. Bush puis George W. Bush ont été présidents."),
  Q("Comment appelle-t-on l'épouse du président des États-Unis ?", ["La First Lady", "La Queen", "La Lady Mayor", "La Speaker"], "La First Lady", "Michelle Obama a été First Lady de 2009 à 2017."),
  Q("Quel président américain, assassiné en 1963, formait avec sa famille une image très médiatisée ?", ["John F. Kennedy", "Abraham Lincoln", "Richard Nixon", "Ronald Reagan"], "John F. Kennedy", "Les photos de la famille Kennedy ont marqué l'imaginaire américain."),
]),
# Le quotidien : lieux, rythmes, saisons
notion('C5-2', 0, F, 'ang-deplacements', [
  Q("Quel bus rouge à deux étages est un symbole de Londres ?", ["Le double-decker", "Le school bus", "Le cable car", "Le tram"], "Le double-decker", "Les bus scolaires américains, eux, sont jaunes."),
  Q("Comment dit-on « l'automne » en anglais américain ?", ["Fall", "Spring", "Winter", "Summer"], "Fall", "Les Britanniques disent plutôt autumn."),
  Q("Comment appelle-t-on le traditionnel petit-déjeuner britannique avec œufs, bacon et haricots ?", ["A full English breakfast", "A continental breakfast", "A brunch", "Afternoon tea"], "A full English breakfast", "« Autour de la table » est un objet d'étude de l'axe."),
]),
# Le réel et l'imaginaire
notion('C5-3', 0, F, 'ang-roald-dahl', [
  Q("Quel livre de Roald Dahl raconte la visite d'une chocolaterie extraordinaire ?", ["Charlie et la chocolaterie", "Matilda", "Le Bon Gros Géant", "James et la grosse pêche"], "Charlie et la chocolaterie", "Roald Dahl s'est inspiré des chocolatiers anglais de son enfance."),
  Q("Quelle famille de chocolatiers anglais a construit au XIXe siècle la cité-jardin de Bournville pour ses ouvriers ?", ["Les Cadbury", "Les Ford", "Les Disney", "Les Rockefeller"], "Les Cadbury", "Une « cité idéale » bien réelle, près de Birmingham."),
  Q("Dans Matilda de Roald Dahl, quel pouvoir possède l'héroïne ?", ["Elle déplace les objets par la pensée", "Elle vole", "Elle devient invisible", "Elle parle aux animaux"], "Elle déplace les objets par la pensée", "Le roman mêle le réel de l'école et l'imaginaire."),
]),
notion('C5-3', 0, I, 'ang-mark-twain', [
  Q("Quel auteur américain a créé les personnages de Tom Sawyer et Huckleberry Finn ?", ["Mark Twain", "Jack London", "Edgar Allan Poe", "John Steinbeck"], "Mark Twain", "Ses héros naviguent sur le Mississippi."),
  Q("Sur quoi Huckleberry Finn descend-il le Mississippi ?", ["Un radeau", "Un sous-marin", "Un paquebot", "Un avion"], "Un radeau", "Le voyage sur le fleuve est un parcours initiatique."),
  Q("D'où vient le pseudonyme « Mark Twain » ?", ["D'un terme de navigation sur le Mississippi indiquant deux brasses de profondeur", "Du nom de son chat", "D'une ville anglaise", "D'un héros de légende"], "D'un terme de navigation sur le Mississippi indiquant deux brasses de profondeur", "L'auteur avait été pilote de bateau à vapeur."),
]),
notion('C5-3', 0, D, 'ang-cliches-medias', [
  Q("Quel cliché sur les Britanniques est souvent véhiculé par les médias ?", ["Ils boivent du thé à cinq heures", "Ils mangent des escargots à chaque repas", "Ils ne parlent jamais de la météo", "Ils roulent tous à vélo"], "Ils boivent du thé à cinq heures", "Un cliché simplifie une réalité plus diverse."),
  Q("Comment appelle-t-on une image simplifiée et figée d'un groupe ou d'un pays ?", ["Un stéréotype (cliché)", "Un portrait", "Un reportage", "Une statistique"], "Un stéréotype (cliché)", "L'axe invite à interroger les images véhiculées par les médias."),
  Q("Quel genre littéraire, avec Tolkien ou C. S. Lewis, crée des mondes imaginaires pour penser le réel ?", ["La fantasy", "Le roman policier", "L'autobiographie", "Le reportage"], "La fantasy", "Le Seigneur des anneaux et Narnia en sont des exemples."),
]),
# École et loisirs
notion('C5-4', 0, I, 'ang-vie-scolaire', [
  Q("Comment appelle-t-on, dans les universités américaines, les associations d'étudiants désignées par des lettres grecques ?", ["Les fraternités et sororités", "Les clubs de sport", "Les conseils d'élèves", "Les syndicats"], "Les fraternités et sororités", "Elles organisent la vie sociale de nombreux étudiants."),
  Q("Comment appelle-t-on un petit groupe fermé d'élèves, souvent représenté dans les films sur le lycée américain ?", ["A clique", "A crew", "A team", "A class"], "A clique", "Les « jocks » ou les « nerds » sont des clichés de ces films."),
  Q("Dans les écoles britanniques, comment appelle-t-on les équipes qui regroupent les élèves de différentes classes ?", ["Les houses", "Les clubs", "Les forms", "Les terms"], "Les houses", "Comme les maisons de Poudlard dans Harry Potter."),
]),
# Des langues, des lieux, des histoires
notion('C5-5', 0, F, 'ang-fetes-histoire-usa', [
  Q("Quelle fête commémore, le 19 juin, la fin de l'esclavage aux États-Unis ?", ["Juneteenth", "Labor Day", "Memorial Day", "Columbus Day"], "Juneteenth", "Elle est devenue un jour férié fédéral en 2021."),
  Q("Quel jour férié américain d'octobre rappelle l'arrivée de Christophe Colomb en Amérique ?", ["Columbus Day", "Thanksgiving", "Independence Day", "Presidents' Day"], "Columbus Day", "Il est aujourd'hui souvent célébré comme Indigenous Peoples' Day."),
  Q("Quel navire amène en 1620 les colons appelés « Pilgrims » en Amérique ?", ["Le Mayflower", "Le Titanic", "La Santa María", "L'Endeavour"], "Le Mayflower", "Leur premier repas de récolte est à l'origine de Thanksgiving."),
]),
notion('C5-5', 0, D, 'ang-evolution-langue', [
  Q("De quelle langue viennent de nombreux mots anglais comme « beef », « pork » ou « justice » ?", ["Du français normand, après 1066", "De l'allemand moderne", "De l'espagnol", "De l'arabe"], "Du français normand, après 1066", "La conquête normande a profondément enrichi l'anglais."),
  Q("Quel grand auteur a introduit de nombreux mots et expressions dans la langue anglaise au XVIe siècle ?", ["William Shakespeare", "Charles Dickens", "J. K. Rowling", "Jane Austen"], "William Shakespeare", "On lui attribue des mots comme « bedroom » ou « lonely »."),
  Q("Quel mot anglais vient de l'hindi, à l'époque de l'Empire britannique en Inde ?", ["Shampoo", "Window", "Castle", "Bread"], "Shampoo", "D'autres mots comme « bungalow » ou « pyjamas » viennent aussi de l'Inde."),
]),
# ══ Classe de 4e ══
# Sport et société
notion('C4-1', 0, F, 'ang-sports-nationaux', [
  Q("Quel sport, très populaire dans le Commonwealth, se joue avec une batte plate et des guichets (wickets) ?", ["Le cricket", "Le baseball", "Le golf", "Le hockey"], "Le cricket", "Il est roi en Inde, en Australie et au Royaume-Uni."),
  Q("Quel sport est une véritable institution au Canada ?", ["Le hockey sur glace", "Le cricket", "Le rugby à XV", "Le polo"], "Le hockey sur glace", "La Coupe Stanley récompense le champion de la ligue nord-américaine (NHL)."),
  Q("Quel match de football américain, la finale de la NFL, est l'un des événements les plus regardés aux États-Unis ?", ["Le Super Bowl", "Le World Series", "Wimbledon", "Le Six Nations"], "Le Super Bowl", "Les publicités diffusées pendant le match sont elles-mêmes un événement."),
]),
notion('C4-1', 0, I, 'ang-sport-universitaire', [
  Q("Quelle organisation gère le sport universitaire aux États-Unis ?", ["La NCAA", "La NBA", "Le CIO", "La FIFA"], "La NCAA", "De nombreux athlètes y obtiennent une bourse d'études."),
  Q("Quel sport australien, joué sur un terrain ovale, porte le nom d'« Aussie Rules » ?", ["Le football australien", "Le cricket", "Le surf", "Le rugby à XIII"], "Le football australien", "Il incarne des valeurs fortes de la société australienne."),
  Q("Quel célèbre tournoi de tennis se joue sur gazon à Londres chaque été ?", ["Wimbledon", "Roland-Garros", "l'US Open", "l'Open d'Australie"], "Wimbledon", "Les joueurs y sont tenus de s'habiller en blanc."),
]),
notion('C4-1', 0, D, 'ang-sport-enjeux', [
  Q("Quel boxeur américain, champion olympique en 1960, s'est engagé contre la guerre du Vietnam et pour les droits civiques ?", ["Mohamed Ali", "Mike Tyson", "Rocky Balboa", "Joe Louis"], "Mohamed Ali", "Le sport peut devenir un espace d'engagement."),
  Q("Quel athlète afro-américain remporte quatre médailles d'or aux Jeux olympiques de Berlin en 1936 ?", ["Jesse Owens", "Carl Lewis", "Usain Bolt", "Michael Jordan"], "Jesse Owens", "Sa victoire contredit la propagande nazie."),
  Q("Pourquoi le sport représente-t-il un enjeu économique majeur dans les pays anglophones ?", ["Droits télévisés, sponsoring et billetterie génèrent des milliards", "Parce qu'il est gratuit pour tous", "Parce qu'il est interdit à la télévision", "Il n'en représente aucun"], "Droits télévisés, sponsoring et billetterie génèrent des milliards", "La Premier League anglaise est l'un des championnats les plus riches du monde."),
]),
# Voyages et explorations
notion('C4-2', 0, F, 'ang-explorateurs', [
  Q("Quel navigateur britannique du XVIIIe siècle a exploré le Pacifique et cartographié la Nouvelle-Zélande ?", ["James Cook", "Christophe Colomb", "Magellan", "Vasco de Gama"], "James Cook", "Son navire, l'Endeavour, est célèbre."),
  Q("Quel astronaute américain est le premier à marcher sur la Lune, en 1969 ?", ["Neil Armstrong", "Buzz Aldrin", "Youri Gagarine", "Thomas Pesquet"], "Neil Armstrong", "« That's one small step for man, one giant leap for mankind. »"),
  Q("Comment dit-on « voyage » (déplacement long) en anglais ?", ["A journey", "A travel bag", "A trip-trap", "A road sign"], "A journey", "« Journée » se dit day : attention aux faux amis."),
]),
notion('C4-2', 0, I, 'ang-exploration-polaire', [
  Q("Quel explorateur britannique voit son navire, l'Endurance, broyé par les glaces de l'Antarctique en 1915 ?", ["Ernest Shackleton", "Robert Scott", "Roald Amundsen", "David Livingstone"], "Ernest Shackleton", "Tout son équipage a survécu, après un sauvetage héroïque."),
  Q("Quel explorateur norvégien atteint le premier le pôle Sud, en 1911, avant le Britannique Robert Scott ?", ["Roald Amundsen", "Ernest Shackleton", "Fridtjof Nansen", "Paul-Émile Victor"], "Roald Amundsen", "Scott et ses compagnons meurent sur le chemin du retour."),
  Q("Quelle phrase célèbre est attribuée à Stanley lorsqu'il retrouve l'explorateur Livingstone en Afrique en 1871 ?", ["« Dr Livingstone, I presume? »", "« Houston, we have a problem »", "« Eureka! »", "« Land ho! »"], "« Dr Livingstone, I presume? »", "La rencontre a lieu près du lac Tanganyika."),
]),
notion('C4-2', 0, D, 'ang-conquete-spatiale', [
  Q("Quelle agence spatiale américaine a conduit le programme Apollo ?", ["La NASA", "L'ESA", "Le CNES", "SpaceX"], "La NASA", "Elle est créée en 1958, en pleine guerre froide."),
  N("En quelle année l'équipage d'Apollo 11 se pose-t-il sur la Lune ?", 1969, "Le 20 juillet 1969."),
  Q("Dans quel contexte se déroule la course à l'espace entre les États-Unis et l'URSS ?", ["La guerre froide", "La Première Guerre mondiale", "La guerre d'indépendance américaine", "La révolution industrielle"], "La guerre froide", "L'URSS envoie le premier satellite (Spoutnik, 1957) et le premier homme (Gagarine, 1961)."),
]),
# Villes, villages, quartiers
notion('C4-3', 0, I, 'ang-soweto-apartheid', [
  Q("Quel régime de ségrégation raciale a été appliqué en Afrique du Sud de 1948 au début des années 1990 ?", ["L'apartheid", "Le Commonwealth", "Le fédéralisme", "La monarchie"], "L'apartheid", "Il séparait les populations selon leur couleur de peau."),
  Q("Quel township de Johannesburg est un lieu emblématique de la lutte contre l'apartheid ?", ["Soweto", "Brooklyn", "Notting Hill", "Harlem"], "Soweto", "Le soulèvement des écoliers de Soweto, en 1976, a marqué le monde."),
  Q("Quel leader sud-africain, emprisonné 27 ans, devient président en 1994 ?", ["Nelson Mandela", "Desmond Tutu", "Steve Biko", "Frederik de Klerk"], "Nelson Mandela", "Il reçoit le prix Nobel de la paix en 1993."),
]),
notion('C4-3', 0, D, 'ang-vivre-ensemble-villes', [
  Q("Qu'est-ce qu'une gated community aux États-Unis ?", ["Un quartier résidentiel fermé et surveillé", "Un parc public", "Un quartier d'affaires", "Une école"], "Un quartier résidentiel fermé et surveillé", "Ces quartiers posent la question d'une nouvelle forme de ségrégation."),
  Q("Quelle ville australienne est surnommée « the Garden City » ?", ["Melbourne", "Sydney", "Perth", "Darwin"], "Melbourne", "Elle est réputée pour ses nombreux parcs et jardins."),
  Q("Comment appelle-t-on, en anglais britannique, le voisinage et ses habitants ?", ["The neighbourhood", "The township", "The suburbs only", "The countryside"], "The neighbourhood", "En anglais américain, on écrit neighborhood."),
]),
# Inventer, innover, créer
notion('C4-4', 0, F, 'ang-inventeurs', [
  Q("Quel inventeur, né en Écosse, dépose en 1876 le brevet du téléphone aux États-Unis ?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "James Watt"], "Alexander Graham Bell", "Il est aussi reconnu pour son travail auprès des personnes sourdes."),
  Q("Quels frères américains réalisent en 1903 le premier vol motorisé ?", ["Les frères Wright", "Les frères Lumière", "Les frères Montgolfier", "Les frères Grimm"], "Les frères Wright", "Le vol a lieu à Kitty Hawk, en Caroline du Nord."),
  Q("Quel scientifique britannique a inventé le World Wide Web en 1989 ?", ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Alan Turing"], "Tim Berners-Lee", "Il travaillait alors au CERN, près de Genève."),
]),
notion('C4-4', 0, I, 'ang-innovation-numerique', [
  Q("Quelle région de Californie concentre les géants du numérique ?", ["La Silicon Valley", "Hollywood", "Wall Street", "Las Vegas"], "La Silicon Valley", "Apple, Google ou Meta y ont leur siège."),
  Q("Quel mathématicien britannique, pionnier de l'informatique, a contribué à déchiffrer le code Enigma ?", ["Alan Turing", "Isaac Newton", "Charles Darwin", "Stephen Hawking"], "Alan Turing", "Le film The Imitation Game raconte son histoire."),
  Q("Quelle créatrice britannique a popularisé la minijupe dans les années 1960 ?", ["Mary Quant", "Coco Chanel", "Vivienne Westwood", "Stella McCartney"], "Mary Quant", "La mode des « Swinging Sixties » faisait de Londres une capitale avant-gardiste."),
]),
notion('C4-4', 0, D, 'ang-creation-contemporaine', [
  Q("Quel artiste de rue britannique anonyme est connu pour ses pochoirs engagés ?", ["Banksy", "Andy Warhol", "David Hockney", "Damien Hirst"], "Banksy", "Sa Petite Fille au ballon s'est autodétruite lors d'une vente aux enchères en 2018."),
  Q("Quelle créatrice britannique, figure du mouvement punk, est devenue une icône de la mode ?", ["Vivienne Westwood", "Mary Poppins", "Agatha Christie", "Twiggy"], "Vivienne Westwood", "Elle a aussi défendu de nombreuses causes environnementales."),
  Q("Comment appelle-t-on en anglais l'intelligence artificielle ?", ["Artificial intelligence (AI)", "Machine brain", "Computer mind", "Robot thinking"], "Artificial intelligence (AI)", "La révolution numérique transforme le travail et la création."),
]),
# Langages et messages artistiques
notion('C4-5', 0, F, 'ang-gag-cinema', [
  Q("Quel acteur britannique du cinéma muet incarne le personnage de Charlot (the Tramp) ?", ["Charlie Chaplin", "Buster Keaton", "Laurel", "Rowan Atkinson"], "Charlie Chaplin", "Ses gags sont compris dans le monde entier, sans paroles."),
  Q("Quel personnage comique britannique, presque muet, est joué par Rowan Atkinson ?", ["Mr. Bean", "Sherlock Holmes", "James Bond", "Paddington"], "Mr. Bean", "Il illustre la mécanique du gag visuel."),
  Q("Quel quartier de Los Angeles est le symbole de l'industrie du cinéma américain ?", ["Hollywood", "Broadway", "Manhattan", "Beverly Hills"], "Hollywood", "Broadway, à New York, est le cœur du théâtre et des comédies musicales."),
]),
notion('C4-5', 0, I, 'ang-musique-engagee', [
  Q("Quel chanteur américain, prix Nobel de littérature en 2016, a écrit « Blowin' in the Wind » ?", ["Bob Dylan", "Elvis Presley", "Bruce Springsteen", "Johnny Cash"], "Bob Dylan", "La chanson est devenue un hymne du mouvement des droits civiques."),
  Q("Quel groupe de Liverpool a révolutionné la musique pop dans les années 1960 ?", ["The Beatles", "The Rolling Stones", "Queen", "U2"], "The Beatles", "John Lennon a ensuite chanté la paix avec « Imagine »."),
  Q("Quel genre musical afro-américain, né au début du XXe siècle, est souvent associé à La Nouvelle-Orléans ?", ["Le jazz", "Le punk", "La techno", "Le reggae"], "Le jazz", "Louis Armstrong en est l'une des grandes figures."),
]),
notion('C4-5', 0, D, 'ang-theatre-tradition', [
  Q("Quel théâtre londonien, reconstruit à l'identique en 1997, était celui de la troupe de Shakespeare ?", ["Le Globe", "Le Royal Albert Hall", "L'Old Vic", "Le Palladium"], "Le Globe", "Le public debout au pied de la scène était appelé « the groundlings »."),
  Q("Quel quartier de New York est célèbre pour ses théâtres et ses comédies musicales ?", ["Broadway", "Harlem", "Wall Street", "Brooklyn"], "Broadway", "Le West End joue le même rôle à Londres."),
  Q("Quelle tradition musicale écossaise utilise un instrument à vent avec une poche d'air ?", ["La cornemuse (bagpipes)", "Le banjo", "Le didgeridoo", "Le ukulélé"], "La cornemuse (bagpipes)", "Les traditions se transmettent aussi par l'art."),
]),
# ══ Classe de 3e ══
# À la rencontre de l'autre
notion('C3-1', 0, F, 'ang-rencontres-couples', [
  Q("Quel couple de jeunes amants de Shakespeare appartient à deux familles ennemies de Vérone ?", ["Roméo et Juliette", "Antoine et Cléopâtre", "Tristan et Iseut", "Orphée et Eurydice"], "Roméo et Juliette", "La pièce est jouée pour la première fois vers 1597."),
  Q("Quelle jeune femme amérindienne est associée dans la légende aux premiers colons anglais de Virginie ?", ["Pocahontas", "Sacagawea", "Mulan", "Moana"], "Pocahontas", "Le récit de sa rencontre avec John Smith mêle histoire et légende."),
  Q("Comment dit-on « rencontrer quelqu'un » en anglais ?", ["To meet someone", "To encounter-make", "To find out someone", "To join with"], "To meet someone", "« Nice to meet you » se dit lors d'une première rencontre."),
]),
notion('C3-1', 0, D, 'ang-cook-maoris', [
  Q("Quel traité est signé en 1840 entre la Couronne britannique et des chefs maoris ?", ["Le traité de Waitangi", "Le traité de Paris", "Le traité de Versailles", "Le traité de Tordesillas"], "Le traité de Waitangi", "Il est considéré comme le document fondateur de la Nouvelle-Zélande."),
  Q("Quelle danse rituelle maorie est exécutée par les All Blacks avant leurs matchs ?", ["Le haka", "La gigue", "Le moonwalk", "La valse"], "Le haka", "Elle rappelle la place de la culture maorie dans le pays."),
  Q("Comment les Maoris appellent-ils la Nouvelle-Zélande ?", ["Aotearoa", "Oz", "Down Under", "Uluru"], "Aotearoa", "Ce nom signifie souvent « le pays du long nuage blanc »."),
]),
# Travailler hier, aujourd'hui, demain
notion('C3-2', 0, F, 'ang-teen-jobs', [
  Q("Comment appelle-t-on les petits boulots des adolescents aux États-Unis ?", ["Teen jobs", "Full-time careers", "Gap years", "Night shifts only"], "Teen jobs", "Babysitting, distribution de journaux ou service dans les fast-foods en sont des exemples."),
  Q("Comment dit-on « faire du baby-sitting » en anglais ?", ["To babysit", "To baby-watch", "To child-keep", "To nanny-do"], "To babysit", "Le baby-sitting est un petit boulot très répandu."),
  Q("Comment dit-on « postuler à un emploi » en anglais ?", ["To apply for a job", "To post a job", "To ask a work", "To candidate"], "To apply for a job", "On envoie alors un CV, appelé resume aux États-Unis."),
]),
notion('C3-2', 0, I, 'ang-organisation-travail', [
  Q("Quel industriel américain introduit en 1913 le travail à la chaîne pour fabriquer la Ford T ?", ["Henry Ford", "Thomas Edison", "Andrew Carnegie", "Walt Disney"], "Henry Ford", "Les États-Unis sont souvent vus comme un laboratoire de l'organisation du travail."),
  Q("Quel romancier anglais a décrit le travail des enfants dans l'Angleterre industrielle, notamment dans Oliver Twist ?", ["Charles Dickens", "Jane Austen", "Lewis Carroll", "Oscar Wilde"], "Charles Dickens", "Lui-même a travaillé enfant dans une usine de cirage."),
  Q("Que désigne l'expression « glass ceiling » (plafond de verre) ?", ["Les obstacles invisibles qui freinent l'accès des femmes aux postes les plus élevés", "Un toit en verre", "Un métier du bâtiment", "Un plafond de salaire légal"], "Les obstacles invisibles qui freinent l'accès des femmes aux postes les plus élevés", "Dépasser les stéréotypes est un objet d'étude de l'axe."),
]),
notion('C3-2', 0, D, 'ang-travail-enjeux', [
  Q("Comment appelle-t-on, en anglais, le télétravail ?", ["Remote work (working from home)", "Far job", "Tele-labour", "Home business only"], "Remote work (working from home)", "Il s'est fortement développé depuis 2020."),
  Q("Comment appelle-t-on l'économie des petits boulots via des plateformes numériques (livraison, VTC) ?", ["La gig economy", "Le New Deal", "Le free market", "Le welfare state"], "La gig economy", "Elle soulève la question de la protection des travailleurs."),
  Q("Quel jour férié américain de septembre célèbre les travailleurs ?", ["Labor Day", "Memorial Day", "Thanksgiving", "Veterans Day"], "Labor Day", "Il est fêté le premier lundi de septembre."),
]),
# Voyages et migrations
notion('C3-3', 0, F, 'ang-ellis-island', [
  Q("Quelle île de New York a accueilli des millions d'immigrants entre 1892 et 1954 ?", ["Ellis Island", "Manhattan", "Coney Island", "Long Island"], "Ellis Island", "C'est aujourd'hui un musée de l'immigration."),
  Q("Comment dit-on « immigré » en anglais ?", ["An immigrant", "An imigrator", "A stranger-in", "A foreigner-out"], "An immigrant", "Un émigrant est « an emigrant »."),
  Q("Quelle route mythique traversait les États-Unis de Chicago à Los Angeles ?", ["La Route 66", "La Wild Atlantic Way", "La Pan-Americana", "L'Oregon Trail"], "La Route 66", "Elle est le symbole du road trip américain."),
]),
notion('C3-3', 0, I, 'ang-migrations-internes', [
  Q("Comment appelle-t-on le départ de millions d'Afro-Américains du Sud vers les villes du Nord au XXe siècle ?", ["La Grande Migration", "La ruée vers l'or", "La conquête de l'Ouest", "Le Dust Bowl"], "La Grande Migration", "Ils fuyaient la ségrégation et cherchaient du travail."),
  Q("Quel roman de John Steinbeck raconte l'exode de fermiers vers la Californie pendant la Grande Dépression ?", ["Les Raisins de la colère", "Gatsby le Magnifique", "Moby Dick", "Sur la route"], "Les Raisins de la colère", "Il paraît en 1939."),
  Q("Quel écrivain de la « Beat Generation » a écrit Sur la route (On the Road), éloge du vagabondage ?", ["Jack Kerouac", "Ernest Hemingway", "Mark Twain", "Jack London"], "Jack Kerouac", "La figure du vagabond est un objet d'étude de l'axe."),
]),
notion('C3-3', 0, D, 'ang-migration-australie', [
  Q("Comment surnommait-on les Britanniques partis s'installer en Australie après 1945 pour un billet de dix livres ?", ["Les « Ten Pound Poms »", "Les « Pilgrims »", "Les « Cowboys »", "Les « Yankees »"], "Les « Ten Pound Poms »", "L'Australie cherchait alors à attirer des immigrés."),
  Q("Quelle politique d'immigration réservée aux Européens l'Australie a-t-elle abandonnée dans les années 1970 ?", ["La « White Australia Policy »", "Le Brexit", "Le New Deal", "Le Commonwealth"], "La « White Australia Policy »", "L'Australie est aujourd'hui une société multiculturelle."),
  Q("Quelle région, très touristique, est formée d'îles anglophones comme la Jamaïque ou la Barbade ?", ["Les Caraïbes", "La Polynésie", "La Méditerranée", "La Scandinavie"], "Les Caraïbes", "Le tourisme de masse y pose des questions économiques et environnementales."),
]),
# Langages et médias
notion('C3-4', 0, I, 'ang-grands-discours', [
  Q("Quel pasteur américain prononce en 1963 le discours « I Have a Dream » ?", ["Martin Luther King", "Malcolm X", "Barack Obama", "John F. Kennedy"], "Martin Luther King", "Il le prononce devant le Lincoln Memorial, à Washington."),
  Q("Quel Premier ministre britannique déclare en 1940 « We shall fight on the beaches » ?", ["Winston Churchill", "Margaret Thatcher", "Tony Blair", "Neville Chamberlain"], "Winston Churchill", "Ses discours ont soutenu le moral des Britanniques pendant la guerre."),
  Q("Quel président américain prononce en 1863 le célèbre discours de Gettysburg ?", ["Abraham Lincoln", "George Washington", "Theodore Roosevelt", "Thomas Jefferson"], "Abraham Lincoln", "Il y défend « le gouvernement du peuple, par le peuple, pour le peuple »."),
]),
notion('C3-4', 0, D, 'ang-langue-marqueur', [
  Q("Comment appelle-t-on l'accent populaire de l'est de Londres, connu pour son « rhyming slang » ?", ["Le cockney", "Le scouse", "Le yankee", "L'aussie"], "Le cockney", "La langue est un marqueur social et géographique."),
  Q("Combien de langues officielles l'Afrique du Sud reconnaît-elle, dont l'anglais ?", ["Douze", "Deux", "Une", "Cinquante"], "Douze", "La langue des signes sud-africaine est devenue la douzième en 2023."),
  Q("Environ combien de locuteurs natifs l'anglais compte-t-il dans le monde, selon le programme ?", ["Environ quatre cents millions", "Environ quarante millions", "Environ quatre milliards", "Environ quatre millions"], "Environ quatre cents millions", "L'anglais est langue officielle dans plus de cinquante pays."),
]),
# Formes de l'engagement
notion('C3-5', 0, F, 'ang-engagement-droits', [
  Q("Quelle Afro-Américaine refuse en 1955 de céder sa place dans un bus à Montgomery ?", ["Rosa Parks", "Michelle Obama", "Harriet Tubman", "Oprah Winfrey"], "Rosa Parks", "Son geste lance le boycott des bus de Montgomery."),
  Q("Comment appelle-t-on les militantes britanniques qui luttaient pour le droit de vote des femmes au début du XXe siècle ?", ["Les suffragettes", "Les Pilgrims", "Les Beatles", "Les Tudors"], "Les suffragettes", "Emmeline Pankhurst en est une figure majeure."),
  Q("Quelle jeune Pakistanaise, installée au Royaume-Uni, reçoit le prix Nobel de la paix en 2014 pour son combat pour l'éducation des filles ?", ["Malala Yousafzai", "Greta Thunberg", "Emma Watson", "Michelle Obama"], "Malala Yousafzai", "Elle est la plus jeune lauréate du prix Nobel."),
]),
notion('C3-5', 0, I, 'ang-mouvement-droits-civiques', [
  Q("Comment appelle-t-on le mouvement des années 1950-1960 contre la ségrégation raciale aux États-Unis ?", ["Le mouvement des droits civiques (Civil Rights Movement)", "Le New Deal", "La conquête de l'Ouest", "Le Brexit"], "Le mouvement des droits civiques (Civil Rights Movement)", "Il aboutit au Civil Rights Act de 1964."),
  Q("Quel mouvement, né en 2013, dénonce les violences policières envers les Afro-Américains ?", ["Black Lives Matter", "Me Too", "Occupy Wall Street", "Greenpeace"], "Black Lives Matter", "Il prend une ampleur mondiale en 2020."),
  Q("Quelle femme, ancienne esclave, a guidé de nombreux esclaves vers la liberté par le « chemin de fer clandestin » ?", ["Harriet Tubman", "Rosa Parks", "Eleanor Roosevelt", "Amelia Earhart"], "Harriet Tubman", "L'Underground Railroad était un réseau d'aide aux esclaves en fuite."),
]),
notion('C3-5', 0, D, 'ang-philanthropie-benevolat', [
  Q("Quel industriel américain de l'acier a financé des milliers de bibliothèques publiques ?", ["Andrew Carnegie", "Henry Ford", "Bill Gates", "John D. Rockefeller"], "Andrew Carnegie", "La philanthropie est une longue tradition aux États-Unis."),
  Q("Comment dit-on « faire du bénévolat » en anglais ?", ["To volunteer", "To benefit", "To charity-work", "To free-job"], "To volunteer", "Une association caritative se dit « a charity »."),
  Q("Que sont Children in Need ou Comic Relief au Royaume-Uni ?", ["Des opérations caritatives télévisées de collecte de dons", "Des tournois de tennis", "Des élections locales", "Des festivals de musique classique"], "Des opérations caritatives télévisées de collecte de dons", "Ces soirées mêlent humour, musique et collecte de fonds."),
]),
]

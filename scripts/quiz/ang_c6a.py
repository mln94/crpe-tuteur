# Anglais · Repères culturels, 6e : Personnes et personnages ; Le quotidien : vivre, jouer, apprendre (25 questions par niveau)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ C6-1 · Personnes et personnages ══
notion('C6-1', 0, F, 'ang6-se-presenter', [
  Q("Comment dit-on « Je m'appelle Tom » en anglais ?", ["My name is Tom.", "I am called of Tom.", "Me name Tom.", "I have Tom."], "My name is Tom.", "On peut aussi dire « I'm Tom »."),
  Q("Que répond-on à « How old are you? » ?", ["I'm twelve.", "I have twelve years.", "I'm fine.", "I'm from London."], "I'm twelve.", "En anglais, on « est » un âge : I am twelve (years old)."),
  Q("Que signifie « Where are you from? » ?", ["D'où viens-tu ?", "Où vas-tu ?", "Où habites-tu ?", "Comment vas-tu ?"], "D'où viens-tu ?", "Réponse : I'm from France."),
]),
notion('C6-1', 0, F, 'ang6-famille-2', [
  Q("Comment dit-on « frère » en anglais ?", ["Brother", "Sister", "Father", "Uncle"], "Brother", "Sister = sœur."),
  Q("Que signifie « grandfather » ?", ["Grand-père", "Grand-mère", "Arrière-grand-père", "Beau-père"], "Grand-père", "Grandparents = grands-parents."),
  Q("Comment dit-on « tante » en anglais ?", ["Aunt", "Uncle", "Niece", "Cousin"], "Aunt", "Uncle = oncle."),
]),
notion('C6-1', 0, F, 'ang6-description-physique', [
  Q("Que signifie « She has got long brown hair » ?", ["Elle a de longs cheveux bruns.", "Elle a les yeux bruns.", "Elle a les cheveux courts.", "Elle est grande et brune."], "Elle a de longs cheveux bruns.", "En anglais, hair est indénombrable : pas de -s."),
  Q("Comment dit-on « Il est grand » (taille) ?", ["He is tall.", "He is big.", "He is long.", "He is high."], "He is tall.", "Tall pour une personne ; high pour un objet ou une montagne."),
  Q("Que signifie « blue eyes » ?", ["Des yeux bleus", "Des cheveux bleus", "Des lunettes bleues", "Une robe bleue"], "Des yeux bleus", "L'adjectif se place avant le nom."),
]),
notion('C6-1', 0, F, 'ang6-caractere', [
  Q("Que signifie « funny » ?", ["Drôle", "Méchant", "Timide", "Fatigué"], "Drôle", "A funny story = une histoire drôle."),
  Q("Comment dit-on « gentil » en anglais ?", ["Kind (ou nice)", "Rude", "Lazy", "Shy"], "Kind (ou nice)", "Lazy = paresseux, shy = timide."),
  Q("Que signifie « brave » en anglais ?", ["Courageux", "Brave et gentil", "Bête", "Peureux"], "Courageux", "C'est un faux ami partiel : brave = courageux."),
]),
notion('C6-1', 0, F, 'ang6-heros-bd', [
  Q("Quel super-héros américain est surnommé « l'homme d'acier » et vient de la planète Krypton ?", ["Superman", "Batman", "Spider-Man", "Iron Man"], "Superman", "Il apparaît en 1938."),
  Q("Quel héros de Marvel est un adolescent new-yorkais piqué par une araignée ?", ["Spider-Man (Peter Parker)", "Captain America", "Hulk", "Thor"], "Spider-Man (Peter Parker)", "Il a été créé en 1962."),
  Q("Comment dit-on « bande dessinée » en anglais américain ?", ["A comic book", "A drawn band", "A cartoon strip only", "A novel"], "A comic book", "Les comics sont un genre majeur aux États-Unis."),
]),
notion('C6-1', 0, F, 'ang6-personnages-celebres', [
  Q("Quel personnage de Walt Disney est une souris aux grandes oreilles rondes ?", ["Mickey Mouse", "Donald Duck", "Bugs Bunny", "Tom"], "Mickey Mouse", "Il apparaît en 1928."),
  Q("Quel ours en peluche britannique aime le miel et vit dans la forêt des Cent Acres ?", ["Winnie l'Ourson (Winnie-the-Pooh)", "Paddington", "Baloo", "Rupert"], "Winnie l'Ourson (Winnie-the-Pooh)", "Il est créé par A. A. Milne en 1926."),
  Q("Quel ours venu du Pérou, qui adore la marmelade, arrive à une gare de Londres ?", ["Paddington", "Winnie", "Teddy", "Yogi"], "Paddington", "Il porte un chapeau et un duffle-coat."),
]),
notion('C6-1', 0, I, 'ang6i-he-she-his-her', [
  Q("Complétez : « This is my sister. ___ name is Emma. »", ["Her", "His", "She", "Its"], "Her", "Le possessif s'accorde avec le possesseur : her pour une femme."),
  Q("Complétez : « This is Tom. ___ dog is black. »", ["His", "Her", "He", "Their"], "His", "His = son, sa, ses (possesseur masculin)."),
  Q("Complétez : « The children love ___ teacher. »", ["their", "there", "they", "his"], "their", "Their = leur, leurs."),
]),
notion('C6-1', 0, I, 'ang6i-has-got', [
  Q("Complétez : « She ___ two brothers. »", ["has got", "have got", "is got", "haves"], "has got", "À la 3e personne du singulier : has got."),
  Q("Quelle est la forme négative de « I have got a cat » ?", ["I haven't got a cat.", "I don't got a cat.", "I have not a cat got.", "I haven't a cat got."], "I haven't got a cat.", "On peut aussi dire : I don't have a cat."),
  Q("Quelle question est correcte ?", ["Have you got a pet?", "Do you got a pet?", "Are you got a pet?", "Got you a pet?"], "Have you got a pet?", "Réponse : Yes, I have. / No, I haven't."),
]),
notion('C6-1', 0, I, 'ang6i-genitif', [
  Q("Comment dit-on « le vélo de Tom » ?", ["Tom's bike", "The bike of Tom's", "Tom bike's", "The Tom bike"], "Tom's bike", "C'est le génitif (ou cas possessif) avec 's."),
  Q("Comment dit-on « la maison de mes parents » ?", ["My parents' house", "My parents's house", "My parent's houses", "The house my parents"], "My parents' house", "Après un pluriel en -s, on ajoute seulement l'apostrophe."),
  Q("Que signifie « my friend's mother » ?", ["La mère de mon ami", "Les mères de mes amis", "Mon ami et sa mère", "La mère est mon amie"], "La mère de mon ami", "Le possesseur vient avant ce qui est possédé."),
]),
notion('C6-1', 0, I, 'ang6i-nationalites', [
  Q("Comment dit-on « Elle est galloise » ?", ["She is Welsh.", "She is Wales.", "She is Galloise.", "She is Walish."], "She is Welsh.", "Les adjectifs de nationalité prennent une majuscule en anglais."),
  Q("Quel adjectif correspond à l'Écosse ?", ["Scottish", "Scotchy", "Scotland", "Scotish"], "Scottish", "Scotland = l'Écosse ; Scottish = écossais."),
  Q("Comment dit-on « Je suis français » ?", ["I'm French.", "I'm France.", "I'm french.", "I'm Frenchy."], "I'm French.", "Toujours une majuscule : French."),
]),
notion('C6-1', 0, I, 'ang6i-reine-roi', [
  Q("Quel roi a succédé à Élisabeth II en 2022 ?", ["Charles III", "William V", "George VII", "Edward IX"], "Charles III", "Il a été couronné en mai 2023."),
  Q("Combien d'années a duré le règne d'Élisabeth II ?", ["70 ans", "25 ans", "50 ans", "90 ans"], "70 ans", "De 1952 à 2022 : le plus long règne britannique."),
  Q("Qui est l'héritier du trône britannique ?", ["Le prince William", "Le prince Harry", "La princesse Anne", "Le prince George"], "Le prince William", "Il est prince de Galles."),
]),
notion('C6-1', 0, I, 'ang6i-heros-litterature', [
  Q("Quel garçon qui ne veut jamais grandir vit au Pays imaginaire ?", ["Peter Pan", "Oliver Twist", "Tom Sawyer", "Harry Potter"], "Peter Pan", "Il est créé par J. M. Barrie en 1904."),
  Q("Quel détective vit au 221B Baker Street, à Londres ?", ["Sherlock Holmes", "Hercule Poirot", "James Bond", "Tintin"], "Sherlock Holmes", "Il est créé par Arthur Conan Doyle."),
  Q("Quel personnage de Roald Dahl est une petite fille très douée qui lit énormément ?", ["Matilda", "Alice", "Wendy", "Mary Poppins"], "Matilda", "Le roman paraît en 1988."),
]),
notion('C6-1', 0, I, 'ang6i-sportifs-celebres', [
  Q("Quel footballeur anglais a été capitaine de l'équipe d'Angleterre et a joué au Real Madrid ?", ["David Beckham", "Lionel Messi", "Zinédine Zidane", "Cristiano Ronaldo"], "David Beckham", "Il est aujourd'hui propriétaire d'un club à Miami."),
  Q("Quelle joueuse de tennis américaine a remporté 23 titres du Grand Chelem ?", ["Serena Williams", "Venus Williams", "Coco Gauff", "Maria Sharapova"], "Serena Williams", "Sa sœur Venus est aussi championne."),
  Q("Quel athlète jamaïcain détient le record du monde du 100 mètres ?", ["Usain Bolt", "Carl Lewis", "Mo Farah", "Jesse Owens"], "Usain Bolt", "9 secondes 58, en 2009."),
]),
notion('C6-1', 0, I, 'ang6i-describing-people', [
  Q("Comment demande-t-on à quoi ressemble quelqu'un ?", ["What does he look like?", "How does he look like?", "What is he like look?", "Who does he look?"], "What does he look like?", "« What is he like? » interroge plutôt sur le caractère."),
  Q("Que signifie « He wears glasses » ?", ["Il porte des lunettes.", "Il boit dans des verres.", "Il casse des verres.", "Il a de grands yeux."], "Il porte des lunettes.", "To wear = porter (vêtements, lunettes)."),
  Q("Que signifie « She has freckles » ?", ["Elle a des taches de rousseur.", "Elle a des boucles.", "Elle a des rides.", "Elle a des fossettes."], "Elle a des taches de rousseur.", "Curly hair = cheveux bouclés."),
]),
notion('C6-1', 0, I, 'ang6i-personnages-historiques', [
  Q("Quelle infirmière britannique, surnommée « la dame à la lampe », a soigné les soldats pendant la guerre de Crimée ?", ["Florence Nightingale", "Elizabeth Fry", "Mary Seacole", "Edith Cavell"], "Florence Nightingale", "Elle est une pionnière des soins infirmiers."),
  Q("Quel président américain a aboli l'esclavage pendant la guerre de Sécession ?", ["Abraham Lincoln", "George Washington", "John F. Kennedy", "Thomas Jefferson"], "Abraham Lincoln", "Le 13e amendement est adopté en 1865."),
  Q("Quel pasteur américain a prononcé le discours « I have a dream » en 1963 ?", ["Martin Luther King", "Malcolm X", "Barack Obama", "Nelson Mandela"], "Martin Luther King", "Il lutte pour les droits civiques."),
]),
notion('C6-1', 0, D, 'ang6d-descriptions-avancees', [
  Q("Quelle phrase est correcte ?", ["She is a tall, slim woman with curly red hair.", "She is a woman tall slim with hair red curly.", "She is tall woman slim with red curly hair.", "She is a woman slim tall with curly hair red."], "She is a tall, slim woman with curly red hair.", "Les adjectifs se placent avant le nom, la taille avant la couleur."),
  Q("Que signifie « He takes after his father » ?", ["Il ressemble à son père.", "Il suit son père.", "Il s'occupe de son père.", "Il part après son père."], "Il ressemble à son père.", "To take after = tenir de."),
  Q("Que signifie « She is in her early twenties » ?", ["Elle a un peu plus de vingt ans.", "Elle se lève tôt.", "Elle a vingt-deux ans exactement.", "Elle a moins de vingt ans."], "Elle a un peu plus de vingt ans.", "Early / mid / late twenties."),
]),
notion('C6-1', 0, D, 'ang6d-adjectifs-composes', [
  Q("Que signifie « a blue-eyed boy » ?", ["Un garçon aux yeux bleus", "Un garçon vêtu de bleu", "Un garçon triste", "Un garçon qui a un œil au beurre noir"], "Un garçon aux yeux bleus", "Adjectif composé : adjectif + nom + -ed."),
  Q("Comment dit-on « une fille aux cheveux longs » ?", ["A long-haired girl", "A girl long hairs", "A long hair's girl", "A girl of long hairs"], "A long-haired girl", "Hair reste au singulier."),
  Q("Que signifie « a twelve-year-old girl » ?", ["Une fille de douze ans", "Douze filles d'un an", "Une fille âgée de douze mois", "Une vieille fille"], "Une fille de douze ans", "Dans un adjectif composé, year ne prend pas de -s."),
]),
notion('C6-1', 0, D, 'ang6d-auteurs-jeunesse', [
  Q("Quelle autrice britannique a créé le Club des Cinq (The Famous Five) ?", ["Enid Blyton", "J. K. Rowling", "Beatrix Potter", "Agatha Christie"], "Enid Blyton", "Ses livres paraissent à partir de 1942."),
  Q("Quel personnage de Beatrix Potter est un lapin désobéissant qui entre dans le jardin de M. McGregor ?", ["Peter Rabbit (Pierre Lapin)", "Bugs Bunny", "Roger Rabbit", "Le Lapin blanc"], "Peter Rabbit (Pierre Lapin)", "Le livre paraît en 1902."),
  Q("Quel auteur américain a créé Tom Sawyer et Huckleberry Finn ?", ["Mark Twain", "Jack London", "Ernest Hemingway", "Edgar Allan Poe"], "Mark Twain", "Ses héros vivent au bord du Mississippi."),
]),
notion('C6-1', 0, D, 'ang6d-portraits-parole', [
  Q("Quelle question pose-t-on pour connaître le métier de quelqu'un ?", ["What does she do?", "What is she doing?", "What does she like?", "How does she do?"], "What does she do?", "What is she doing? = que fait-elle en ce moment ?"),
  Q("Complétez : « My father is ___ engineer. »", ["an", "a", "the", "—"], "an", "En anglais, on met l'article devant un métier : He is a teacher, an engineer."),
  Q("Que signifie « She is good at drawing » ?", ["Elle est douée pour le dessin.", "Elle aime dessiner.", "Elle dessine bien des chevaux.", "Elle apprend à dessiner."], "Elle est douée pour le dessin.", "Be good at + V-ing."),
]),
notion('C6-1', 0, D, 'ang6d-heros-mythes', [
  Q("Quel héros légendaire anglais vole aux riches pour donner aux pauvres dans la forêt de Sherwood ?", ["Robin des Bois (Robin Hood)", "Le roi Arthur", "Lancelot", "Guillaume Tell"], "Robin des Bois (Robin Hood)", "Son ennemi est le shérif de Nottingham."),
  Q("Quelle épée le jeune Arthur retire-t-il de la pierre selon la légende ?", ["Excalibur", "Durandal", "Joyeuse", "Glamdring"], "Excalibur", "Ce geste fait de lui le roi."),
  Q("Comment s'appellent les chevaliers réunis autour du roi Arthur ?", ["Les chevaliers de la Table ronde", "Les mousquetaires", "Les templiers", "Les chevaliers Jedi"], "Les chevaliers de la Table ronde", "Lancelot, Gauvain, Perceval…"),
]),
notion('C6-1', 0, D, 'ang6d-celebrites-actuelles', [
  Q("Quel jeune acteur britannique a incarné Harry Potter au cinéma ?", ["Daniel Radcliffe", "Rupert Grint", "Tom Holland", "Robert Pattinson"], "Daniel Radcliffe", "Le premier film sort en 2001."),
  Q("Quelle chanteuse américaine a fait en 2023-2024 une tournée record appelée « The Eras Tour » ?", ["Taylor Swift", "Beyoncé", "Lady Gaga", "Billie Eilish"], "Taylor Swift", "C'est la tournée la plus lucrative de l'histoire."),
  Q("Quel acteur britannique joue Spider-Man dans les films Marvel depuis 2016 ?", ["Tom Holland", "Andrew Garfield", "Tobey Maguire", "Daniel Craig"], "Tom Holland", "Il est né à Londres."),
]),
notion('C6-1', 0, D, 'ang6d-pronoms-relatifs-personnes', [
  Q("Complétez : « She is the girl ___ won the race. »", ["who", "which", "what", "whose"], "who", "Who pour une personne."),
  Q("Complétez : « He is the boy ___ father is a pilot. »", ["whose", "who", "which", "whom"], "whose", "Whose = dont le / dont la."),
  Q("Que signifie « the man I met yesterday » ?", ["L'homme que j'ai rencontré hier", "L'homme qui m'a rencontré hier", "J'ai rencontré l'homme demain", "L'homme d'hier"], "L'homme que j'ai rencontré hier", "Le relatif complément (who/that) peut être omis."),
]),
notion('C6-1', 0, D, 'ang6d-biographie', [
  Q("Quel temps utilise-t-on pour raconter la vie d'une personne décédée ?", ["Le prétérit (past simple)", "Le présent simple", "Le futur", "Le present perfect"], "Le prétérit (past simple)", "She was born in 1926. She died in 2022."),
  Q("Comment dit-on « Il est né en 2012 » ?", ["He was born in 2012.", "He is born in 2012.", "He borned in 2012.", "He has born in 2012."], "He was born in 2012.", "To be born se met au passé."),
  Q("Quel est le prétérit du verbe « become » ?", ["became", "becomed", "become", "becomes"], "became", "Become, became, become."),
]),
notion('C6-1', 0, D, 'ang6d-reines-histoire', [
  Q("Quelle reine a régné sur le Royaume-Uni de 1837 à 1901, donnant son nom à une époque ?", ["Victoria", "Élisabeth Ire", "Anne", "Marie Tudor"], "Victoria", "On parle de l'époque victorienne."),
  Q("Quelle reine d'Angleterre, fille d'Henri VIII, a régné de 1558 à 1603 ?", ["Élisabeth Ire", "Victoria", "Élisabeth II", "Jane Grey"], "Élisabeth Ire", "Shakespeare écrit sous son règne."),
  Q("Quel roi d'Angleterre a eu six épouses ?", ["Henri VIII", "Richard III", "Charles Ier", "George III"], "Henri VIII", "Il rompt avec Rome en 1534."),
]),
# ══ C6-2 · Le quotidien : vivre, jouer, apprendre ══
notion('C6-2', 0, F, 'ang6-routine', [
  Q("Que signifie « I get up at seven » ?", ["Je me lève à sept heures.", "Je me couche à sept heures.", "J'ai sept ans.", "Je mange à sept heures."], "Je me lève à sept heures.", "To go to bed = se coucher."),
  Q("Comment dit-on « prendre le petit déjeuner » ?", ["To have breakfast", "To take lunch", "To do dinner", "To make breakfast up"], "To have breakfast", "Lunch = déjeuner, dinner = dîner."),
  Q("Que signifie « I brush my teeth » ?", ["Je me brosse les dents.", "Je me coiffe.", "Je me lave les mains.", "Je m'habille."], "Je me brosse les dents.", "I comb my hair = je me coiffe."),
]),
notion('C6-2', 0, F, 'ang6-jours-mois', [
  Q("Comment dit-on « mercredi » en anglais ?", ["Wednesday", "Thursday", "Tuesday", "Weekend"], "Wednesday", "Les jours prennent une majuscule en anglais."),
  Q("Quel est le premier mois de l'année en anglais ?", ["January", "June", "July", "March"], "January", "Les mois prennent aussi une majuscule."),
  Q("Que signifie « weekend » ?", ["La fin de semaine (samedi et dimanche)", "Une semaine entière", "Le lundi", "Un jour férié"], "La fin de semaine (samedi et dimanche)", "On dit « at the weekend » (GB) ou « on the weekend » (US)."),
]),
notion('C6-2', 0, F, 'ang6-maison', [
  Q("Comment dit-on « cuisine » (la pièce) en anglais ?", ["Kitchen", "Bedroom", "Bathroom", "Living room"], "Kitchen", "Bedroom = chambre."),
  Q("Que signifie « bathroom » ?", ["Salle de bains", "Chambre", "Grenier", "Garage"], "Salle de bains", "Bath = baignoire, bain."),
  Q("Comment dit-on « jardin » en anglais britannique ?", ["Garden", "Yard only", "Park", "Field"], "Garden", "Les Américains disent souvent yard."),
]),
notion('C6-2', 0, F, 'ang6-nourriture', [
  Q("Que signifie « bread » ?", ["Pain", "Beurre", "Fromage", "Lait"], "Pain", "Butter = beurre, cheese = fromage."),
  Q("Comment dit-on « pomme » en anglais ?", ["Apple", "Pear", "Peach", "Plum"], "Apple", "Pear = poire."),
  Q("Quel plat britannique associe poisson pané et frites ?", ["Fish and chips", "Shepherd's pie", "Haggis", "Bangers and mash"], "Fish and chips", "En anglais britannique, chips = frites ; crisps = chips."),
]),
notion('C6-2', 0, F, 'ang6-sports-loisirs', [
  Q("Comment dit-on « faire du vélo » ?", ["To ride a bike", "To make bike", "To do a bicycle", "To drive a bike"], "To ride a bike", "On dit aussi to cycle."),
  Q("Que signifie « I like reading » ?", ["J'aime lire.", "Je lis maintenant.", "Je vais lire.", "Je n'aime pas lire."], "J'aime lire.", "Like + V-ing pour exprimer un goût."),
  Q("Complétez : « I ___ judo on Wednesdays. »", ["do", "play", "make", "go"], "do", "Do pour les sports de combat et la gymnastique ; play pour les jeux de ballon."),
]),
notion('C6-2', 0, F, 'ang6-meteo', [
  Q("Que signifie « It's raining » ?", ["Il pleut.", "Il neige.", "Il fait beau.", "Il y a du vent."], "Il pleut.", "It's snowing = il neige."),
  Q("Comment dit-on « Il fait froid » ?", ["It's cold.", "It's hot.", "It's cool.", "It's warm."], "It's cold.", "Hot = chaud, warm = doux."),
  Q("Que signifie « It's sunny » ?", ["Il y a du soleil.", "Il fait nuit.", "C'est nuageux.", "Il y a de l'orage."], "Il y a du soleil.", "Cloudy = nuageux, windy = venteux."),
]),
notion('C6-2', 0, I, 'ang6i-present-simple', [
  Q("Complétez : « She ___ to school by bus. »", ["goes", "go", "going", "is go"], "goes", "Au présent simple, on ajoute -s (ou -es) à la 3e personne du singulier."),
  Q("Quelle est la forme négative de « He plays football » ?", ["He doesn't play football.", "He don't play football.", "He doesn't plays football.", "He not plays football."], "He doesn't play football.", "Doesn't + base verbale, sans -s."),
  Q("Quelle question est correcte ?", ["Does she like cats?", "Do she like cats?", "Does she likes cats?", "Is she like cats?"], "Does she like cats?", "Does + sujet + base verbale."),
]),
notion('C6-2', 0, I, 'ang6i-frequence', [
  Q("Que signifie « always » ?", ["Toujours", "Jamais", "Parfois", "Souvent"], "Toujours", "Never = jamais, sometimes = parfois, often = souvent."),
  Q("Où place-t-on l'adverbe de fréquence dans « I ___ eat vegetables » ?", ["Entre le sujet et le verbe : I often eat vegetables.", "En fin de phrase uniquement", "Au début uniquement", "Après le complément"], "Entre le sujet et le verbe : I often eat vegetables.", "Mais après be : I am often late."),
  Q("Complétez : « He is ___ late. » (jamais)", ["never", "ever", "not never", "no"], "never", "Never porte déjà la négation."),
]),
notion('C6-2', 0, I, 'ang6i-heure', [
  Q("Comment dit-on « Il est huit heures et demie » ?", ["It's half past eight.", "It's half eight past.", "It's eight and half.", "It's thirty to eight."], "It's half past eight.", "En anglais britannique familier : half eight."),
  Q("Que signifie « It's quarter to five » ?", ["Il est cinq heures moins le quart.", "Il est cinq heures et quart.", "Il est quatre heures et quart.", "Il est cinq heures."], "Il est cinq heures moins le quart.", "Quarter past = et quart."),
  Q("Que signifie « 3 p.m. » ?", ["15 heures", "3 heures du matin", "13 heures", "3 heures et quart"], "15 heures", "a.m. = le matin, p.m. = l'après-midi et le soir."),
]),
notion('C6-2', 0, I, 'ang6i-matieres', [
  Q("Comment dit-on « histoire-géographie » en anglais ?", ["History and geography", "Story and geography", "Histoire and geo", "Historic geography"], "History and geography", "Story = une histoire racontée."),
  Q("Que signifie « PE » à l'école britannique ?", ["L'éducation physique et sportive", "La physique", "La musique", "Les arts plastiques"], "L'éducation physique et sportive", "Physical Education."),
  Q("Comment dit-on « Mon cours préféré est les maths » ?", ["My favourite subject is maths.", "My favourite lesson are maths.", "I prefer the maths subject my.", "My favourite course is the mathematics."], "My favourite subject is maths.", "Les Américains disent math."),
]),
notion('C6-2', 0, I, 'ang6i-repas-gb', [
  Q("À quelle heure prend-on souvent le thé l'après-midi au Royaume-Uni ?", ["Vers 16 heures (afternoon tea)", "À minuit", "À 7 heures", "À 12 heures"], "Vers 16 heures (afternoon tea)", "Il est accompagné de scones."),
  Q("Que contient un « full English breakfast » ?", ["Œufs, bacon, saucisses, haricots blancs, tomates", "Croissant et café", "Céréales seulement", "Riz et poisson"], "Œufs, bacon, saucisses, haricots blancs, tomates", "Il est très copieux."),
  Q("Que signifie « packed lunch » ?", ["Un repas froid emporté de la maison", "Un repas au restaurant", "Un repas chaud à la cantine", "Un goûter"], "Un repas froid emporté de la maison", "Beaucoup d'élèves britanniques en ont un."),
]),
notion('C6-2', 0, I, 'ang6i-fetes', [
  Q("Quelle fête américaine est célébrée le quatrième jeudi de novembre avec une dinde ?", ["Thanksgiving", "Halloween", "Independence Day", "Easter"], "Thanksgiving", "Elle remercie pour les récoltes."),
  Q("Que disent les enfants qui sonnent aux portes à Halloween ?", ["Trick or treat!", "Merry Christmas!", "Happy Easter!", "Cheers!"], "Trick or treat!", "« Une farce ou une friandise ! »"),
  Q("Que fête-t-on le 5 novembre au Royaume-Uni avec des feux d'artifice ?", ["Bonfire Night (Guy Fawkes Night)", "Halloween", "Boxing Day", "Pancake Day"], "Bonfire Night (Guy Fawkes Night)", "En souvenir de la conspiration des Poudres de 1605."),
]),
notion('C6-2', 0, I, 'ang6i-can-ability', [
  Q("Complétez : « I ___ swim. » (je sais nager)", ["can", "cans", "can to", "am can"], "can", "Can ne prend jamais de -s et n'est pas suivi de to."),
  Q("Quelle est la forme négative de « She can dance » ?", ["She can't dance.", "She doesn't can dance.", "She cans not dance.", "She not can dance."], "She can't dance.", "Can't = cannot."),
  Q("Quelle question est correcte ?", ["Can you play the guitar?", "Do you can play the guitar?", "Can you to play the guitar?", "Are you can play the guitar?"], "Can you play the guitar?", "On inverse can et le sujet."),
]),
notion('C6-2', 0, I, 'ang6i-animaux-compagnie', [
  Q("Que signifie « pet » ?", ["Un animal de compagnie", "Un animal sauvage", "Un oiseau", "Un poisson"], "Un animal de compagnie", "Have you got a pet?"),
  Q("Comment dit-on « lapin » en anglais ?", ["Rabbit", "Hamster", "Guinea pig", "Mouse"], "Rabbit", "Guinea pig = cochon d'Inde."),
  Q("Quel est le pluriel de « mouse » (souris) ?", ["Mice", "Mouses", "Mices", "Mousen"], "Mice", "C'est un pluriel irrégulier."),
]),
notion('C6-2', 0, I, 'ang6i-maison-prepositions', [
  Q("Que signifie « The cat is under the table » ?", ["Le chat est sous la table.", "Le chat est sur la table.", "Le chat est à côté de la table.", "Le chat est derrière la table."], "Le chat est sous la table.", "On = sur, next to = à côté de, behind = derrière."),
  Q("Comment dit-on « entre le lit et la fenêtre » ?", ["Between the bed and the window", "Among the bed and the window", "In the bed and the window", "Next the bed window"], "Between the bed and the window", "Between = entre deux éléments."),
  Q("Que signifie « in front of the house » ?", ["Devant la maison", "Dans la maison", "Derrière la maison", "Loin de la maison"], "Devant la maison", "Behind = derrière."),
]),
notion('C6-2', 0, D, 'ang6d-present-be-ing', [
  Q("Quelle phrase décrit une action en cours ?", ["She is reading now.", "She reads every day.", "She read yesterday.", "She will read."], "She is reading now.", "Be + V-ing : présent en be + ing (continu)."),
  Q("Complétez : « Listen! The baby ___. »", ["is crying", "cries", "cry", "cried"], "is crying", "Listen! signale une action en train de se faire."),
  Q("Quel verbe ne s'emploie normalement pas en be + ing ?", ["To know", "To play", "To run", "To eat"], "To know", "Les verbes d'état (know, like, want) se mettent au présent simple."),
]),
notion('C6-2', 0, D, 'ang6d-ecole-gb-us', [
  Q("Comment appelle-t-on la classe de 6e (11-12 ans) en Angleterre ?", ["Year 7", "Grade 6", "Sixth form", "Year 11"], "Year 7", "La sixth form correspond au lycée (16-18 ans)."),
  Q("Comment appelle-t-on le collège-lycée public aux États-Unis, de 14 à 18 ans ?", ["High school", "Public school", "Grammar school", "Boarding school"], "High school", "En Angleterre, une « public school » est une école privée prestigieuse."),
  Q("Que sont les « houses » dans certaines écoles britanniques ?", ["Des groupes d'élèves qui gagnent des points, comme à Poudlard", "Des maisons où logent les professeurs", "Des salles de classe", "Des cantines"], "Des groupes d'élèves qui gagnent des points, comme à Poudlard", "Elles créent un esprit d'équipe."),
]),
notion('C6-2', 0, D, 'ang6d-sports-anglophones', [
  Q("Quel sport, très populaire en Angleterre et en Inde, se joue avec une batte et un guichet (wicket) ?", ["Le cricket", "Le baseball", "Le rugby", "Le hockey"], "Le cricket", "Les matchs peuvent durer plusieurs jours."),
  Q("Quel sport est le plus populaire aux États-Unis, avec le Super Bowl ?", ["Le football américain", "Le soccer", "Le cricket", "Le hurling"], "Le football américain", "Aux États-Unis, le football est appelé soccer."),
  Q("Comment appelle-t-on le football (avec un ballon rond) aux États-Unis ?", ["Soccer", "Football", "Rugby", "Hockey"], "Soccer", "Football désigne le football américain."),
]),
notion('C6-2', 0, D, 'ang6d-jeux-video-jeux', [
  Q("Que signifie « board game » ?", ["Un jeu de société", "Un jeu vidéo", "Un jeu de cartes", "Un jeu de plein air"], "Un jeu de société", "Monopoly, Scrabble, Cluedo…"),
  Q("Quel jeu de société, créé aux États-Unis, consiste à acheter des rues et des gares ?", ["Monopoly", "Scrabble", "Cluedo", "Trivial Pursuit"], "Monopoly", "La version britannique utilise les rues de Londres."),
  Q("Quel jeu de lettres consiste à former des mots croisés sur un plateau ?", ["Scrabble", "Monopoly", "Chess", "Uno"], "Scrabble", "Il est inventé aux États-Unis dans les années 1930."),
]),
notion('C6-2', 0, D, 'ang6d-likes-dislikes', [
  Q("Que signifie « I can't stand homework » ?", ["Je déteste les devoirs.", "Je ne peux pas faire mes devoirs debout.", "Je n'ai pas de devoirs.", "J'adore les devoirs."], "Je déteste les devoirs.", "Can't stand = ne pas supporter."),
  Q("Complétez : « I'm fond ___ music. »", ["of", "to", "with", "for"], "of", "Be fond of = beaucoup aimer."),
  Q("Quelle phrase exprime une préférence ?", ["I prefer tea to coffee.", "I prefer tea than coffee.", "I prefer tea that coffee.", "I prefer tea of coffee."], "I prefer tea to coffee.", "Prefer A to B."),
]),
notion('C6-2', 0, D, 'ang6d-chores', [
  Q("Que signifie « to do the washing-up » ?", ["Faire la vaisselle", "Faire la lessive", "Se laver", "Ranger sa chambre"], "Faire la vaisselle", "To do the laundry (US) / washing (GB) = faire la lessive."),
  Q("Comment dit-on « mettre la table » ?", ["To lay (set) the table", "To put the table", "To make the table", "To do the table"], "To lay (set) the table", "To clear the table = débarrasser."),
  Q("Que signifie « pocket money » ?", ["L'argent de poche", "La monnaie", "Un porte-monnaie", "Le salaire"], "L'argent de poche", "Certains enfants le gagnent en faisant des tâches ménagères."),
]),
notion('C6-2', 0, D, 'ang6d-horaires-ecole', [
  Q("Que signifie « break time » à l'école ?", ["La récréation", "L'heure des examens", "Les vacances", "Le cours de sport"], "La récréation", "Les Américains disent recess."),
  Q("Comment appelle-t-on l'assemblée de toute l'école le matin au Royaume-Uni ?", ["Assembly", "Meeting", "Council", "Parliament"], "Assembly", "Le chef d'établissement y fait des annonces."),
  Q("Que signifie « timetable » ?", ["L'emploi du temps", "La table de multiplication", "L'horloge", "Le calendrier des vacances"], "L'emploi du temps", "Les Américains disent aussi schedule."),
]),
notion('C6-2', 0, D, 'ang6d-quantites-nourriture', [
  Q("Complétez : « Is there ___ milk in the fridge? »", ["any", "some", "a", "many"], "any", "Any dans les questions et les phrases négatives."),
  Q("Complétez : « How ___ apples do you want? »", ["many", "much", "lot", "more"], "many", "Many avec un nom dénombrable ; much avec un indénombrable."),
  Q("Quel nom est indénombrable en anglais ?", ["Water", "Apple", "Egg", "Sandwich"], "Water", "On ne dit pas « a water » mais « a glass of water »."),
]),
notion('C6-2', 0, D, 'ang6d-fetes-avancees', [
  Q("Quelle fête britannique, le mardi gras, est célébrée par des courses de crêpes ?", ["Pancake Day (Shrove Tuesday)", "Boxing Day", "Burns Night", "Bonfire Night"], "Pancake Day (Shrove Tuesday)", "On fait sauter les crêpes en courant."),
  Q("Quelle fête irlandaise, le 17 mars, est célébrée dans le monde entier en vert ?", ["La Saint-Patrick (St Patrick's Day)", "La Saint-Georges", "La Saint-André", "La Saint-David"], "La Saint-Patrick (St Patrick's Day)", "Saint Patrick est le patron de l'Irlande."),
  Q("Que fête-t-on aux États-Unis le 4 juillet ?", ["L'indépendance (Independence Day)", "Thanksgiving", "Memorial Day", "Labor Day"], "L'indépendance (Independence Day)", "En souvenir de la Déclaration de 1776."),
]),
]

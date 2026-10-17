from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('L-2', 1, F, 'ang-be-present', [
  Q("Complétez : « She ___ a teacher. »", ["am", "is", "are", "be"], "is", "To be au présent : I am, you are, he/she/it is, we/you/they are."),
  Q("Complétez : « We ___ in the classroom. »", ["is", "am", "are", "be"], "are", "We are : « nous sommes »."),
  Q("Quelle est la forme négative de « I am happy » ?", ["I don't happy", "I am not happy", "I not am happy", "I isn't happy"], "I am not happy", "On place not après le verbe be ; contraction : I'm not."),
]),
notion('L-2', 1, F, 'ang-have-got', [
  Q("Complétez : « He ___ two brothers. »", ["have got", "has got", "is got", "haves got"], "has got", "À la 3e personne du singulier : he/she/it has got."),
  Q("Complétez : « They ___ a big house. »", ["has", "have", "is", "does"], "have", "They have (got) a big house."),
  Q("Quelle question est correcte ?", ["Do you have a pet?", "Have you a pet got?", "Does you have a pet?", "You have got a pet?"], "Do you have a pet?", "On peut aussi dire : Have you got a pet?"),
]),
notion('L-2', 1, F, 'ang-present-simple-s', [
  Q("Complétez : « My father ___ in a hospital. »", ["work", "works", "working", "is work"], "works", "Au présent simple, on ajoute -s à la 3e personne du singulier."),
  C("Cliquez sur le verbe conjugué à la 3e personne du singulier.", "Every morning, Tom [drinks] a glass of milk.", "Drinks prend un -s car le sujet Tom est à la 3e personne du singulier."),
  Q("Complétez : « She ___ TV every evening. »", ["watch", "watches", "watchs", "watching"], "watches", "Après -ch, -sh, -s, -x, -o, on ajoute -es."),
]),
notion('L-2', 1, F, 'ang-present-simple-negatif', [
  Q("Quelle est la forme négative de « He plays football » ?", ["He don't play football", "He doesn't play football", "He doesn't plays football", "He not plays football"], "He doesn't play football", "Après doesn't, le verbe revient à la base verbale (sans -s)."),
  Q("Complétez : « I ___ like spinach. »", ["doesn't", "don't", "isn't", "am not"], "don't", "I/you/we/they don't ; he/she/it doesn't."),
  Q("Quelle question est correcte ?", ["Does she likes music?", "Does she like music?", "Do she like music?", "She does like music?"], "Does she like music?", "Does + sujet + base verbale."),
]),
notion('L-2', 1, F, 'ang-present-continu', [
  Q("Complétez : « Look! The children ___ in the garden. »", ["play", "are playing", "plays", "is playing"], "are playing", "Le présent en be + -ing décrit une action en cours."),
  C("Cliquez sur le verbe au présent en be + -ing.", "Be quiet, the baby [is sleeping] now.", "Is sleeping décrit une action en train de se dérouler."),
  Q("Quel mot signale souvent le présent en be + -ing ?", ["Every day", "Right now", "Usually", "Never"], "Right now", "Now, right now, look!, listen! accompagnent l'action en cours ; every day, le présent simple."),
]),
notion('L-1', 1, F, 'ang-pronoms-sujets', [
  Q("Quel pronom remplace « my sister » ?", ["he", "she", "it", "they"], "she", "She remplace un nom féminin singulier de personne."),
  Q("Quel pronom remplace « the dog » ?", ["he", "she", "it", "we"], "it", "It s'emploie pour les animaux et les objets (sauf animal familier personnalisé)."),
  Q("Quel pronom remplace « Tom and I » ?", ["they", "we", "you", "us"], "we", "Tom et moi = nous."),
]),
notion('L-2', 1, F, 'ang-possessifs', [
  Q("Complétez : « This is Anna. ___ bag is red. »", ["His", "Her", "Its", "Their"], "Her", "En anglais, le possessif s'accorde avec le possesseur : Anna → her."),
  Q("Complétez : « This is Paul. ___ bike is new. »", ["Her", "His", "Its", "Our"], "His", "Paul est un garçon → his."),
  Q("Complétez : « The children love ___ teacher. »", ["his", "their", "her", "its"], "their", "Les enfants (pluriel) → their."),
]),
notion('L-2', 1, F, 'ang-cas-possessif', [
  Q("Comment dit-on « le chat de Marie » ?", ["The cat of Marie", "Marie's cat", "Marie cat", "The Marie's cat"], "Marie's cat", "Le cas possessif : possesseur + 's + objet possédé."),
  Q("Comment dit-on « la chambre de mes parents » ?", ["My parent's room", "My parents' room", "My parents's room", "The room my parents"], "My parents' room", "Après un pluriel en -s, on ajoute seulement l'apostrophe."),
  Q("Comment dit-on « les jouets des enfants » ?", ["The children's toys", "The childrens' toys", "The toys of the childs", "The children toys"], "The children's toys", "Children est un pluriel irrégulier sans -s : on ajoute 's."),
]),
notion('L-1', 1, F, 'ang-pluriels', [
  Q("Quel est le pluriel de « child » ?", ["childs", "children", "childrens", "childes"], "children", "C'est un pluriel irrégulier."),
  Q("Quel est le pluriel de « mouse » ?", ["mouses", "mice", "mices", "mouse"], "mice", "Autres irréguliers : man → men, woman → women, tooth → teeth, foot → feet."),
  Q("Quel est le pluriel de « box » ?", ["boxs", "boxes", "boxies", "box"], "boxes", "Après -x, -s, -sh, -ch, on ajoute -es."),
]),
notion('L-1', 1, F, 'ang-nombres', [
  N("Écrivez en chiffres : « forty-five ».", 45, "Forty (40) + five (5) = 45. Attention : forty s'écrit sans u."),
  N("Écrivez en chiffres : « a hundred and twelve ».", 112, "En anglais britannique, on place and entre les centaines et les dizaines."),
  N("Écrivez en chiffres : « thirteen ».", 13, "Thirteen (13) ≠ thirty (30) : l'accent tonique aide à les distinguer."),
]),
notion('L-1', 1, F, 'ang-heure', [
  Q("Que signifie « It's half past seven » ?", ["Il est 7 h 30", "Il est 6 h 30", "Il est 7 h 15", "Il est 7 h 45"], "Il est 7 h 30", "Half past = et demie."),
  Q("Que signifie « It's a quarter to nine » ?", ["Il est 9 h 15", "Il est 8 h 45", "Il est 9 h 45", "Il est 8 h 15"], "Il est 8 h 45", "A quarter to nine = 9 heures moins le quart."),
  Q("Que signifie « It's a quarter past three » ?", ["Il est 3 h 15", "Il est 2 h 45", "Il est 3 h 45", "Il est 3 h 30"], "Il est 3 h 15", "Past = après l'heure ; to = avant l'heure."),
]),
notion('L-1', 1, F, 'ang-jours-mois', [
  Q("Quel jour vient après « Tuesday » ?", ["Monday", "Wednesday", "Thursday", "Friday"], "Wednesday", "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday."),
  Q("Quel est le premier mois de l'année ?", ["June", "January", "July", "December"], "January", "Les jours et les mois prennent une majuscule en anglais."),
  Q("Comment écrit-on correctement le jour « jeudi » ?", ["thursday", "Thursday", "Thirsday", "Tursday"], "Thursday", "Majuscule obligatoire en anglais pour les jours de la semaine."),
]),
notion('L-1', 1, F, 'ang-couleurs', [
  Q("Comment dit-on « jaune » en anglais ?", ["yellow", "green", "purple", "brown"], "yellow", "Red, blue, green, yellow, orange, purple, pink, brown, black, white."),
  Q("Que signifie « purple » ?", ["rose", "violet", "marron", "gris"], "violet", "Pink = rose ; grey (GB) / gray (US) = gris."),
  Q("Où se place l'adjectif de couleur en anglais ?", ["Après le nom : a car red", "Avant le nom : a red car", "N'importe où", "Après le verbe uniquement"], "Avant le nom : a red car", "L'adjectif anglais se place avant le nom et ne s'accorde pas."),
]),
notion('L-1', 1, F, 'ang-famille', [
  Q("Que signifie « grandmother » ?", ["tante", "grand-mère", "cousine", "belle-mère"], "grand-mère", "Grandfather = grand-père ; grandparents = grands-parents."),
  Q("Comment dit-on « oncle » ?", ["uncle", "aunt", "cousin", "nephew"], "uncle", "Aunt = tante ; nephew = neveu ; niece = nièce."),
  Q("Que signifie « cousin » en anglais ?", ["Uniquement un cousin garçon", "Un cousin ou une cousine", "Un oncle", "Un ami"], "Un cousin ou une cousine", "Cousin est invariable en genre en anglais."),
]),
notion('L-1', 1, F, 'ang-corps', [
  Q("Que signifie « knee » ?", ["genou", "coude", "cheville", "épaule"], "genou", "Le k initial ne se prononce pas : /niː/."),
  Q("Comment dit-on « dents » ?", ["tooths", "teeth", "tooth", "teeths"], "teeth", "Tooth (une dent), teeth (des dents)."),
  Q("Que signifie « shoulder » ?", ["épaule", "coude", "nuque", "poignet"], "épaule", "Elbow = coude ; wrist = poignet ; neck = cou."),
]),
notion('L-1', 1, F, 'ang-ecole', [
  Q("Que signifie « rubber » en anglais britannique ?", ["une règle", "une gomme", "un crayon", "un cahier"], "une gomme", "En anglais américain, on dit plutôt eraser."),
  Q("Comment dit-on « une trousse » ?", ["a pencil case", "a schoolbag", "a ruler", "a sharpener"], "a pencil case", "Ruler = règle ; sharpener = taille-crayon ; schoolbag = cartable."),
  Q("Que signifie « playground » ?", ["la cantine", "la cour de récréation", "le gymnase", "la bibliothèque"], "la cour de récréation", "Canteen = cantine ; library = bibliothèque (et non librairie)."),
]),
notion('L-1', 1, F, 'ang-faux-amis', [
  Q("Que signifie « library » ?", ["librairie", "bibliothèque", "liberté", "livre"], "bibliothèque", "C'est un faux ami : librairie se dit bookshop."),
  Q("Que signifie « actually » ?", ["actuellement", "en fait", "activement", "à l'instant"], "en fait", "Actuellement se dit currently ou at the moment."),
  Q("Que signifie « sensible » en anglais ?", ["sensible", "raisonnable, sensé", "sensuel", "fragile"], "raisonnable, sensé", "Sensible (français) se dit sensitive."),
]),
notion('L-2', 0, F, 'ang-salutations', [
  Q("Quelle réponse convient à « How are you? » ?", ["I'm ten.", "I'm fine, thanks.", "My name is Tom.", "I'm from London."], "I'm fine, thanks.", "How are you? = comment vas-tu ? ; How old are you? = quel âge as-tu ?"),
  Q("Que dit-on pour se présenter ?", ["My name is Léa.", "I have Léa.", "I call Léa.", "Me is Léa."], "My name is Léa.", "On peut aussi dire I'm Léa."),
  Q("Quelle réponse convient à « Where are you from? » ?", ["I'm eleven.", "I'm from France.", "I'm fine.", "I'm a student."], "I'm from France.", "Where are you from? = d'où viens-tu ?"),
]),
notion('L-2', 0, F, 'ang-age', [
  Q("Comment dit-on « J'ai dix ans » ?", ["I have ten years.", "I am ten years old.", "I have ten.", "I am ten years."], "I am ten years old.", "En anglais, l'âge s'exprime avec to be."),
  Q("Quelle question demande l'âge ?", ["How are you?", "How old are you?", "What's your name?", "Where do you live?"], "How old are you?", "On répond : I'm ten (years old)."),
  Q("Comment dit-on « Elle a vingt ans » ?", ["She has twenty years.", "She is twenty.", "She have twenty.", "She are twenty."], "She is twenty.", "Erreur fréquente des francophones : *She has twenty years."),
]),
notion('L-2', 0, F, 'ang-gouts', [
  Q("Comment dit-on « J'adore lire » ?", ["I love reading.", "I love read.", "I am love reading.", "I loves reading."], "I love reading.", "Après like, love, hate, on emploie souvent la forme en -ing."),
  Q("Quelle phrase exprime une absence de goût ?", ["I like pizza.", "I don't like pizza.", "I love pizza.", "I'm fond of pizza."], "I don't like pizza.", "I hate exprime un dégoût plus fort."),
  Q("Que signifie « I can't stand rap music » ?", ["J'adore le rap", "Je ne supporte pas le rap", "Je joue du rap", "Je ne connais pas le rap"], "Je ne supporte pas le rap", "Can't stand = ne pas supporter."),
]),
notion('L-2', 1, F, 'ang-can', [
  Q("Complétez : « She ___ swim very well. »", ["cans", "can", "can to", "is can"], "can", "Can est invariable et suivi de la base verbale."),
  Q("Quelle est la forme négative de « I can dance » ?", ["I don't can dance.", "I can't dance.", "I can dance not.", "I not can dance."], "I can't dance.", "Can't = cannot."),
  Q("Quelle question est correcte ?", ["Do you can play chess?", "Can you play chess?", "Can you to play chess?", "You can play chess?"], "Can you play chess?", "On inverse can et le sujet pour poser la question."),
]),
notion('L-2', 1, F, 'ang-there-is', [
  Q("Complétez : « ___ a cat on the sofa. »", ["There is", "There are", "It are", "They is"], "There is", "There is + singulier ; there are + pluriel."),
  Q("Complétez : « ___ three apples in the bag. »", ["There is", "There are", "It is", "They are"], "There are", "Three apples est au pluriel."),
  Q("Quelle phrase est correcte ?", ["There isn't any milk.", "There aren't any milk.", "There is no any milk.", "It isn't any milk."], "There isn't any milk.", "Milk est indénombrable : il s'emploie au singulier."),
]),
notion('L-2', 1, F, 'ang-prepositions-lieu', [
  Q("Complétez : « The book is ___ the table. » (sur)", ["in", "on", "under", "behind"], "on", "On = sur ; in = dans ; under = sous ; behind = derrière."),
  Q("Complétez : « The cat is ___ the bed. » (sous)", ["on", "under", "next", "in"], "under", "Under = sous."),
  Q("Complétez : « The bank is ___ the post office. » (à côté de)", ["next to", "in", "under", "on"], "next to", "Between = entre ; opposite = en face de."),
]),
notion('L-2', 1, F, 'ang-imperatif', [
  Q("Quelle phrase est à l'impératif ?", ["You are quiet.", "Be quiet!", "He is quiet.", "Quiet you are."], "Be quiet!", "L'impératif utilise la base verbale sans sujet."),
  Q("Comment dit-on « Ne cours pas ! » ?", ["Not run!", "Don't run!", "No run!", "Run not!"], "Don't run!", "Impératif négatif : don't + base verbale."),
  Q("Comment dit-on « Allons au parc ! » ?", ["Let's go to the park!", "We go to the park!", "Go we to the park!", "Let go to the park!"], "Let's go to the park!", "Let's = let us : propose une action collective."),
]),
notion('L-2', 1, F, 'ang-question-words', [
  Q("Quel mot interrogatif demande un lieu ?", ["When", "Where", "Who", "Why"], "Where", "Where = où ; when = quand ; who = qui ; why = pourquoi."),
  Q("Quel mot interrogatif demande une raison ?", ["Why", "What", "How", "Which"], "Why", "On répond souvent par Because…"),
  Q("Complétez : « ___ is your favourite colour? »", ["Who", "What", "Where", "When"], "What", "What = quoi, quel."),
]),
notion('L-2', 1, F, 'ang-preterit-be', [
  Q("Complétez : « Yesterday, I ___ tired. »", ["am", "was", "were", "be"], "was", "Prétérit de be : I/he/she/it was ; you/we/they were."),
  Q("Complétez : « They ___ at school last Monday. »", ["was", "were", "are", "is"], "were", "They → were."),
  Q("Quelle est la forme négative de « She was happy » ?", ["She didn't happy.", "She wasn't happy.", "She weren't happy.", "She not was happy."], "She wasn't happy.", "Wasn't = was not."),
]),
notion('L-2', 1, F, 'ang-preterit-reguliers', [
  Q("Quel est le prétérit de « play » ?", ["plaied", "played", "playd", "plaid"], "played", "Verbes réguliers : base + -ed."),
  C("Cliquez sur le verbe au prétérit.", "Last summer, we [visited] London with our cousins.", "Visited est le prétérit régulier de visit."),
  Q("Quel est le prétérit de « stop » ?", ["stoped", "stopped", "stopt", "stopping"], "stopped", "On double la consonne finale après une voyelle brève accentuée."),
]),
notion('L-1', 1, F, 'ang-preterit-irreguliers', [
  Q("Quel est le prétérit de « go » ?", ["goed", "went", "gone", "goes"], "went", "Go – went – gone."),
  Q("Quel est le prétérit de « see » ?", ["seed", "saw", "seen", "sawn"], "saw", "See – saw – seen."),
  Q("Quel est le prétérit de « eat » ?", ["eated", "ate", "eaten", "eat"], "ate", "Eat – ate – eaten."),
]),
notion('L-2', 1, F, 'ang-adjectifs', [
  Q("Quelle phrase est correcte ?", ["She has a dress blue.", "She has a blue dress.", "She has a blues dress.", "She has blue a dress."], "She has a blue dress.", "L'adjectif se place avant le nom."),
  Q("Quelle phrase est correcte ?", ["They are talls.", "They are tall.", "They are tall ones.", "They tall are."], "They are tall.", "L'adjectif anglais ne prend jamais de marque du pluriel."),
  C("Cliquez sur l'adjectif.", "We live in a [small] house near the river.", "Small est un adjectif placé devant le nom house."),
]),
notion('L-2', 1, F, 'ang-articles', [
  Q("Complétez : « I have ___ orange. »", ["a", "an", "the", "–"], "an", "On emploie an devant un son voyelle."),
  Q("Complétez : « She is ___ university student. »", ["a", "an", "–", "some"], "a", "University commence par le son /j/ (consonne) : on dit a university."),
  Q("Complétez : « ___ dogs are friendly animals. » (en général)", ["The", "A", "–", "An"], "–", "Pour une généralité au pluriel, on n'emploie pas d'article : Dogs are friendly."),
]),
notion('L-1', 0, F, 'ang-comprehension-consignes', [
  Q("Que signifie la consigne « Listen and repeat » ?", ["Lis et écris", "Écoute et répète", "Regarde et dessine", "Écoute et réponds"], "Écoute et répète", "Consignes fréquentes : read, write, draw, match, circle, tick."),
  Q("Que signifie « Tick the right answer » ?", ["Barre la bonne réponse", "Coche la bonne réponse", "Écris la bonne réponse", "Souligne la bonne réponse"], "Coche la bonne réponse", "Tick = cocher ; circle = entourer ; underline = souligner."),
  Q("Que signifie « Match the words with the pictures » ?", ["Dessine les mots", "Relie les mots aux images", "Colorie les images", "Recopie les mots"], "Relie les mots aux images", "Match = associer, relier."),
]),
notion('L-1', 0, F, 'ang-comprehension-texte', [
  Q("« Tom gets up at 7. He has breakfast and walks to school. » Comment Tom va-t-il à l'école ?", ["En bus", "À pied", "À vélo", "En voiture"], "À pied", "Walk = marcher, aller à pied."),
  Q("« Sarah's favourite sport is swimming, but she doesn't like running. » Quel sport Sarah n'aime-t-elle pas ?", ["La natation", "La course", "Le football", "Le tennis"], "La course", "Running = la course à pied."),
  Q("« It's raining, so take your umbrella. » Quel temps fait-il ?", ["Il fait beau", "Il pleut", "Il neige", "Il y a du vent"], "Il pleut", "It's raining = il pleut ; umbrella = parapluie."),
]),
notion('L-1', 1, F, 'ang-meteo', [
  Q("Que signifie « It's sunny » ?", ["Il pleut", "Il fait beau (ensoleillé)", "Il neige", "Il fait froid"], "Il fait beau (ensoleillé)", "Cloudy = nuageux ; windy = venteux ; snowy = neigeux."),
  Q("Comment dit-on « Il fait froid » ?", ["It's cold.", "It's hot.", "It's cool.", "It's warm."], "It's cold.", "Hot = chaud ; warm = doux, tiède."),
  Q("Que signifie « foggy » ?", ["Brumeux (il y a du brouillard)", "Orageux", "Neigeux", "Ensoleillé"], "Brumeux (il y a du brouillard)", "Stormy = orageux."),
]),
notion('L-1', 1, F, 'ang-nourriture', [
  Q("Que signifie « chicken » ?", ["Poulet", "Cuisine", "Fromage", "Poisson"], "Poulet", "Kitchen = cuisine ; cheese = fromage ; fish = poisson."),
  Q("Comment dit-on « petit-déjeuner » ?", ["lunch", "breakfast", "dinner", "snack"], "breakfast", "Lunch = déjeuner ; dinner = dîner."),
  Q("Que signifie « I'm hungry » ?", ["J'ai soif", "J'ai faim", "J'ai froid", "J'ai sommeil"], "J'ai faim", "I'm thirsty = j'ai soif."),
]),
notion('L-1', 1, F, 'ang-vetements', [
  Q("Que signifie « trousers » ?", ["une trousse", "un pantalon", "une chemise", "des chaussures"], "un pantalon", "Faux ami ! Une trousse = a pencil case."),
  Q("Comment dit-on « une écharpe » ?", ["a scarf", "a hat", "a coat", "a glove"], "a scarf", "Hat = chapeau ; coat = manteau ; gloves = gants."),
  Q("Que signifie « shoes » ?", ["chaussettes", "chaussures", "chemises", "short"], "chaussures", "Socks = chaussettes ; shorts = short."),
]),
notion('L-1', 1, F, 'ang-ville', [
  Q("Que signifie « bakery » ?", ["boucherie", "boulangerie", "pharmacie", "banque"], "boulangerie", "Butcher's = boucherie ; chemist's (GB) / pharmacy = pharmacie."),
  Q("Comment dit-on « la gare » ?", ["the train station", "the bus stop", "the airport", "the harbour"], "the train station", "Bus stop = arrêt de bus ; harbour = port."),
  Q("Que signifie « Turn left » ?", ["Tourne à droite", "Tourne à gauche", "Va tout droit", "Arrête-toi"], "Tourne à gauche", "Turn right = à droite ; go straight on = tout droit."),
]),
notion('L-1', 1, F, 'ang-sports-loisirs', [
  Q("Comment dit-on « jouer au football » ?", ["play football", "do football", "make football", "go football"], "play football", "Play + sport de ballon ; go + -ing (go swimming) ; do + activité (do judo)."),
  Q("Complétez : « I ___ swimming every Saturday. »", ["play", "go", "do", "make"], "go", "Go swimming, go skiing, go cycling."),
  Q("Comment dit-on « jouer du piano » ?", ["play piano", "play the piano", "do the piano", "make piano"], "play the piano", "Avec les instruments, on emploie the."),
]),
notion('L-2', 1, F, 'ang-adverbes-frequence', [
  Q("Que signifie « always » ?", ["jamais", "toujours", "parfois", "souvent"], "toujours", "Always > usually > often > sometimes > rarely > never."),
  Q("Où se place l'adverbe de fréquence dans « I ___ eat vegetables » ?", ["Avant le verbe : I often eat vegetables", "À la fin seulement", "Avant le sujet", "Il n'y a pas de règle"], "Avant le verbe : I often eat vegetables", "Mais après be : She is often late."),
  Q("Que signifie « never » ?", ["jamais", "parfois", "toujours", "souvent"], "jamais", "I never drink coffee : je ne bois jamais de café."),
]),
notion('L-2', 1, F, 'ang-comparatif-court', [
  Q("Quel est le comparatif de « tall » ?", ["more tall", "taller", "tallest", "the tall"], "taller", "Adjectifs courts : -er + than."),
  Q("Complétez : « An elephant is ___ than a mouse. »", ["big", "bigger", "biggest", "more big"], "bigger", "On double la consonne finale : big → bigger."),
  Q("Quel est le comparatif de « good » ?", ["gooder", "better", "best", "more good"], "better", "Good – better – the best ; bad – worse – the worst."),
]),
notion('L-3', 1, F, 'ang-uk-pays', [
  Q("Quels pays forment le Royaume-Uni ?", ["Angleterre, Écosse, pays de Galles, Irlande du Nord", "Angleterre et Irlande", "Angleterre, Écosse et Irlande", "Angleterre seulement"], "Angleterre, Écosse, pays de Galles, Irlande du Nord", "La république d'Irlande est un État indépendant."),
  Q("Quelle est la capitale de l'Écosse ?", ["Glasgow", "Édimbourg", "Cardiff", "Belfast"], "Édimbourg", "Cardiff est la capitale du pays de Galles ; Belfast, celle de l'Irlande du Nord."),
  Q("Quel est le symbole floral de l'Écosse ?", ["La rose", "Le chardon", "Le trèfle", "La jonquille"], "Le chardon", "La rose pour l'Angleterre, le trèfle pour l'Irlande, la jonquille (ou le poireau) pour le pays de Galles."),
]),
notion('L-3', 0, F, 'ang-londres', [
  Q("Quel fleuve traverse Londres ?", ["La Tamise (Thames)", "La Seine", "Le Rhin", "La Severn"], "La Tamise (Thames)", "La Severn est le plus long fleuve du Royaume-Uni."),
  Q("Qu'est-ce que Big Ben ?", ["Un pont", "La grosse cloche de la tour Elizabeth, au palais de Westminster", "Un musée", "Un parc"], "La grosse cloche de la tour Elizabeth, au palais de Westminster", "Par extension, on appelle souvent la tour elle-même Big Ben."),
  Q("Comment appelle-t-on le métro londonien ?", ["The subway", "The Underground (the Tube)", "The metro", "The train"], "The Underground (the Tube)", "Subway est le terme américain."),
]),
notion('L-3', 0, F, 'ang-usa', [
  N("Combien d'États compte les États-Unis ?", 50, "Les deux derniers admis sont l'Alaska et Hawaï, en 1959."),
  Q("Quelle est la capitale des États-Unis ?", ["New York", "Washington, D.C.", "Los Angeles", "Chicago"], "Washington, D.C.", "New York est la plus grande ville, mais pas la capitale."),
  Q("Quelle fête américaine est célébrée le 4 juillet ?", ["Thanksgiving", "Independence Day", "Halloween", "Memorial Day"], "Independence Day", "Elle commémore la déclaration d'indépendance de 1776."),
]),
notion('L-3', 1, F, 'ang-fetes', [
  Q("Quelle fête est célébrée le 31 octobre ?", ["Thanksgiving", "Halloween", "Bonfire Night", "Easter"], "Halloween", "Les enfants disent « Trick or treat! »."),
  Q("Quel jour de novembre est célébré Thanksgiving aux États-Unis ?", ["Le premier lundi", "Le quatrième jeudi", "Le 11 novembre", "Le dernier dimanche"], "Le quatrième jeudi", "On y mange traditionnellement de la dinde."),
  Q("Que célèbre-t-on au Royaume-Uni le 5 novembre (Bonfire Night) ?", ["La fin de la guerre", "L'échec de la Conspiration des poudres de Guy Fawkes en 1605", "La naissance de la reine", "Le Nouvel An"], "L'échec de la Conspiration des poudres de Guy Fawkes en 1605", "On allume des feux de joie et des feux d'artifice."),
]),
notion('L-3', 1, F, 'ang-monnaie', [
  Q("Quelle est la monnaie du Royaume-Uni ?", ["L'euro", "La livre sterling", "Le dollar", "Le franc"], "La livre sterling", "Son symbole est £."),
  N("Combien de pence y a-t-il dans une livre sterling ?", 100, "1 pound = 100 pence depuis la décimalisation de 1971."),
  Q("Quelle est la monnaie du Canada ?", ["Le dollar canadien", "La livre", "L'euro", "Le dollar américain"], "Le dollar canadien", "L'Australie et la Nouvelle-Zélande ont aussi leur propre dollar."),
]),
notion('L-3', 1, F, 'ang-ecole-uk', [
  Q("Que portent la plupart des élèves dans les écoles britanniques ?", ["Des vêtements libres", "Un uniforme", "Un costume", "Une blouse de laboratoire"], "Un uniforme", "L'uniforme comprend souvent un blazer, une cravate et des couleurs propres à l'école."),
  Q("Comment appelle-t-on le chef d'établissement dans une école britannique ?", ["The headteacher", "The mayor", "The principal officer", "The coach"], "The headteacher", "On dit souvent principal aux États-Unis."),
  Q("À quel âge l'école est-elle obligatoire en Angleterre ?", ["À partir de 3 ans", "À partir de 5 ans (environ)", "À partir de 7 ans", "À partir de 10 ans"], "À partir de 5 ans (environ)", "En pratique, beaucoup d'enfants entrent en Reception vers 4 ans."),
]),
notion('L-3', 0, F, 'ang-pays-anglophones', [
  Q("Dans lequel de ces pays l'anglais est-il une langue officielle ?", ["Le Brésil", "L'Australie", "Le Mexique", "L'Argentine"], "L'Australie", "Autres pays anglophones : Nouvelle-Zélande, Canada, Irlande, Afrique du Sud, Inde (langue officielle associée)…"),
  Q("Quelle est la capitale de l'Australie ?", ["Sydney", "Canberra", "Melbourne", "Perth"], "Canberra", "Sydney est la plus grande ville."),
  Q("Quelles sont les deux langues officielles du Canada au niveau fédéral ?", ["L'anglais et l'espagnol", "L'anglais et le français", "Le français et l'inuktitut", "L'anglais seulement"], "L'anglais et le français", "Le Québec est majoritairement francophone."),
]),
notion('L-2', 0, F, 'ang-politesse', [
  Q("Comment demande-t-on poliment un verre d'eau ?", ["Give me water.", "Could I have a glass of water, please?", "I want water.", "Water now."], "Could I have a glass of water, please?", "Could I…? et please marquent la politesse."),
  Q("Que répond-on à « Thank you » ?", ["Sorry.", "You're welcome.", "Excuse me.", "Please."], "You're welcome.", "On peut aussi dire « No problem » ou « My pleasure »."),
  Q("Que dit-on pour attirer poliment l'attention d'un inconnu ?", ["Sorry!", "Excuse me…", "Hey you!", "Thank you"], "Excuse me…", "Sorry s'emploie surtout pour s'excuser."),
]),
notion('L-2', 1, F, 'ang-some-any', [
  Q("Complétez : « I'd like ___ bread, please. »", ["any", "some", "a", "many"], "some", "Some dans les phrases affirmatives et les demandes polies."),
  Q("Complétez : « Have you got ___ brothers? »", ["some", "any", "a", "much"], "any", "Any dans les questions et les phrases négatives."),
  Q("Complétez : « There aren't ___ chairs in the room. »", ["some", "any", "a", "no"], "any", "Négation : not… any."),
]),
notion('L-2', 1, F, 'ang-futur-going-to', [
  Q("Complétez : « Look at the clouds! It ___ rain. »", ["is going to", "goes to", "go to", "will going to"], "is going to", "Be going to exprime une prévision fondée sur un indice présent ou une intention."),
  Q("Comment dit-on « Je vais rendre visite à ma grand-mère demain » ?", ["I'm going to visit my grandmother tomorrow.", "I go visit my grandmother tomorrow.", "I'm go to visit my grandmother tomorrow.", "I going to visit my grandmother tomorrow."], "I'm going to visit my grandmother tomorrow.", "Be + going to + base verbale."),
  Q("Quelle phrase exprime une intention future ?", ["I played tennis.", "I'm going to play tennis.", "I play tennis.", "I was playing tennis."], "I'm going to play tennis.", "Les autres phrases expriment le passé ou une habitude."),
]),
notion('L-1', 1, F, 'ang-prononciation', [
  Q("Dans « knife », quelle lettre ne se prononce pas ?", ["n", "k", "i", "f"], "k", "Le k est muet devant n : knife, know, knee."),
  Q("Quel mot se prononce comme « sea » ?", ["see", "say", "she", "so"], "see", "Sea (mer) et see (voir) sont des homophones."),
  Q("Dans « hour », le h se prononce-t-il ?", ["Oui", "Non, il est muet", "Seulement aux États-Unis", "Seulement au pluriel"], "Non, il est muet", "C'est pourquoi on dit an hour."),
]),
]

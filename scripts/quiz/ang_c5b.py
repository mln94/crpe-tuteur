# Anglais · Repères culturels, 5e : École et loisirs ; Des langues, des lieux, des histoires ; Le Royaume-Uni (25 questions par niveau)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ C5-4 · École et loisirs ══
notion('C5-4', 0, F, 'ang5-fournitures', [
  Q("Comment dit-on « une règle » en anglais ?", ["A ruler", "A rubber", "A pencil case", "A scissor"], "A ruler", "Rubber (GB) / eraser (US) = gomme."),
  Q("Que signifie « exercise book » ?", ["Un cahier", "Un manuel", "Un exercice de sport", "Un livre de recettes"], "Un cahier", "Textbook = manuel."),
  Q("Comment dit-on « des ciseaux » ?", ["Scissors", "A scissor", "Cutters", "Knives"], "Scissors", "Le mot est toujours au pluriel : a pair of scissors."),
]),
notion('C5-4', 0, F, 'ang5-classe-consignes', [
  Q("Que signifie « Open your books! » ?", ["Ouvrez vos livres !", "Fermez vos livres !", "Lisez vos livres !", "Rangez vos livres !"], "Ouvrez vos livres !", "Close your books! = fermez vos livres !"),
  Q("Que signifie « Can I go to the toilet, please? » ?", ["Puis-je aller aux toilettes, s'il vous plaît ?", "Où sont les toilettes ?", "Je vais aux toilettes.", "Les toilettes sont fermées."], "Puis-je aller aux toilettes, s'il vous plaît ?", "Can I…? pour demander une permission."),
  Q("Comment dit-on « Je ne comprends pas » ?", ["I don't understand.", "I not understand.", "I doesn't understand.", "I no understand."], "I don't understand.", "Can you repeat, please? = Pouvez-vous répéter ?"),
]),
notion('C5-4', 0, F, 'ang5-loisirs-ecrans', [
  Q("Que signifie « to watch TV » ?", ["Regarder la télé", "Réparer la télé", "Acheter une télé", "Éteindre la télé"], "Regarder la télé", "To watch = regarder (quelque chose qui bouge)."),
  Q("Comment dit-on « jouer aux jeux vidéo » ?", ["To play video games", "To do video games", "To make video games play", "To game the videos"], "To play video games", "A gamer = un joueur."),
  Q("Que signifie « to chat with friends » ?", ["Discuter avec des amis", "Jouer avec un chat", "Écrire une lettre", "Se disputer"], "Discuter avec des amis", "Faux ami : chat = discussion, cat = chat."),
]),
notion('C5-4', 0, F, 'ang5-clubs', [
  Q("Que signifie « after-school club » ?", ["Une activité après les cours", "Un club de football professionnel", "Une boîte de nuit", "Une cantine"], "Une activité après les cours", "Drama club, chess club, choir…"),
  Q("Que signifie « drama club » ?", ["Un club de théâtre", "Un club de drames", "Un club de natation", "Un club de dessin"], "Un club de théâtre", "Drama = théâtre (à l'école)."),
  Q("Comment dit-on « la chorale » ?", ["The choir", "The chorus line", "The band", "The orchestra"], "The choir", "Band = groupe de musique."),
]),
notion('C5-4', 0, F, 'ang5-sports-ecole', [
  Q("Que signifie « swimming pool » ?", ["Une piscine", "Une plage", "Un lac", "Une douche"], "Une piscine", "To swim = nager."),
  Q("Comment dit-on « gagner un match » ?", ["To win a match", "To earn a match", "To gain a game", "To beat a match"], "To win a match", "To lose = perdre."),
  Q("Que signifie « sports day » dans les écoles britanniques ?", ["Une journée de compétitions sportives", "Un jour sans sport", "Un match professionnel", "Une sortie au stade"], "Une journée de compétitions sportives", "Course en sac, course à l'œuf…"),
]),
notion('C5-4', 0, F, 'ang5-uniforme', [
  Q("Quel vêtement fait souvent partie de l'uniforme scolaire britannique ?", ["Une cravate et un blazer", "Un jean troué", "Un maillot de bain", "Un costume de clown"], "Une cravate et un blazer", "Les couleurs varient selon les écoles."),
  Q("Que signifie « blazer » ?", ["Une veste d'uniforme", "Un pull", "Une cravate", "Un pantalon"], "Une veste d'uniforme", "Elle porte souvent l'écusson de l'école."),
  Q("Les élèves américains portent-ils généralement un uniforme dans les écoles publiques ?", ["Non, le plus souvent", "Oui, toujours", "Seulement les filles", "Seulement en hiver"], "Non, le plus souvent", "Certaines écoles en imposent un."),
]),
notion('C5-4', 0, F, 'ang5-heures-ecole', [
  Q("Que signifie « lunch break » ?", ["La pause déjeuner", "La récréation du matin", "La fin des cours", "Le petit-déjeuner"], "La pause déjeuner", "Elle est souvent courte au Royaume-Uni."),
  Q("À quelle heure finissent souvent les cours au Royaume-Uni ?", ["Vers 15 h 30", "Vers 18 heures", "Vers midi", "Vers 20 heures"], "Vers 15 h 30", "Les élèves ont ensuite des clubs."),
  Q("Que signifie « homework » ?", ["Les devoirs", "Le travail à la maison des parents", "Le ménage", "La maison"], "Les devoirs", "Homework est indénombrable : no « homeworks »."),
]),
notion('C5-4', 0, F, 'ang5-vacances-loisirs', [
  Q("Que signifie « holidays » en anglais britannique ?", ["Les vacances", "Les jours fériés uniquement", "Les hôtels", "Les voyages d'affaires"], "Les vacances", "Les Américains disent vacation."),
  Q("Comment dit-on « aller au cinéma » ?", ["To go to the cinema", "To go at cinema", "To do cinema", "To make the movies"], "To go to the cinema", "Aux États-Unis : to go to the movies."),
  Q("Que signifie « to go camping » ?", ["Faire du camping", "Aller au camp militaire", "Acheter une tente", "Faire une randonnée"], "Faire du camping", "Go + V-ing pour certaines activités."),
]),
notion('C5-4', 0, F, 'ang5-musique-ecoute', [
  Q("Que signifie « to listen to music » ?", ["Écouter de la musique", "Jouer de la musique", "Écrire de la musique", "Danser"], "Écouter de la musique", "Listen est suivi de to."),
  Q("Comment dit-on « une chanson » ?", ["A song", "A sing", "A singer", "A sound"], "A song", "Singer = chanteur."),
  Q("Que signifie « headphones » ?", ["Un casque audio", "Un téléphone", "Un micro", "Un haut-parleur"], "Un casque audio", "Earphones = écouteurs."),
]),
notion('C5-4', 0, I, 'ang5i-gcse-key-stages', [
  Q("À quel âge les élèves anglais quittent-ils l'école obligatoire en continuant une formation ?", ["À 18 ans (éducation ou formation obligatoire)", "À 12 ans", "À 14 ans", "À 21 ans"], "À 18 ans (éducation ou formation obligatoire)", "L'école à temps plein est obligatoire jusqu'à 16 ans."),
  Q("Comment appelle-t-on les deux dernières années du lycée en Angleterre ?", ["La sixth form", "La high school", "Le college d'université", "Les grades 11-12"], "La sixth form", "Les élèves y préparent les A-levels."),
  Q("Quels examens permettent d'entrer à l'université en Angleterre ?", ["Les A-levels", "Les GCSE", "Le SAT", "Le baccalauréat"], "Les A-levels", "Les GCSE se passent vers 16 ans."),
]),
notion('C5-4', 0, I, 'ang5i-detention-punitions', [
  Q("Qu'est-ce qu'une « detention » dans une école britannique ?", ["Une retenue", "Une prison", "Un examen", "Une récompense"], "Une retenue", "L'élève reste après les cours."),
  Q("Que signifie « to be late for school » ?", ["Être en retard à l'école", "Rester tard à l'école", "Arriver en avance", "Sécher l'école"], "Être en retard à l'école", "To skip school = sécher."),
  Q("Qu'est-ce qu'un « head teacher » ?", ["Le chef d'établissement", "Le professeur principal uniquement", "Le surveillant", "Le délégué de classe"], "Le chef d'établissement", "Aux États-Unis : the principal."),
]),
notion('C5-4', 0, I, 'ang5i-loisirs-gerondif', [
  Q("Complétez : « I enjoy ___ in the park. » (walk)", ["walking", "to walk", "walk", "walked"], "walking", "Enjoy + V-ing."),
  Q("Complétez : « She is interested ___ photography. »", ["in", "on", "by", "of"], "in", "Be interested in."),
  Q("Complétez : « I'm keen ___ skateboarding. »", ["on", "of", "in", "at"], "on", "Be keen on = être passionné par."),
]),
notion('C5-4', 0, I, 'ang5i-scoutisme', [
  Q("Quel mouvement de jeunesse a été fondé en 1907 par le Britannique Baden-Powell ?", ["Le scoutisme", "Les Jeunesses musicales", "Le Duke of Edinburgh Award", "La Croix-Rouge"], "Le scoutisme", "Le premier camp a lieu sur l'île de Brownsea."),
  Q("Quel programme britannique récompense les jeunes pour leur engagement, leur sport et une expédition ?", ["Le Duke of Edinburgh's Award", "Le BAFA", "Le GCSE", "Le Nobel junior"], "Le Duke of Edinburgh's Award", "Il existe dans de nombreux pays."),
  Q("Quelle est la devise des scouts ?", ["« Be prepared » (Sois prêt)", "« Never give up »", "« Keep calm »", "« Just do it »"], "« Be prepared » (Sois prêt)", "Les initiales de Baden-Powell : B. P."),
]),
notion('C5-4', 0, I, 'ang5i-usa-high-school-vie', [
  Q("Comment appelle-t-on les pom-pom girls qui encouragent les équipes américaines ?", ["Les cheerleaders", "Les majorettes", "Les supporters", "Les mascots"], "Les cheerleaders", "Le cheerleading est devenu un sport."),
  Q("Qu'est-ce qu'un « locker » dans un lycée américain ?", ["Un casier individuel", "Un vestiaire de sport", "Une salle de classe", "Un professeur"], "Un casier individuel", "Il est souvent dans les couloirs."),
  Q("Comment appelle-t-on la remise de diplôme à la fin du lycée américain ?", ["La graduation", "Le prom", "Le yearbook", "Le homecoming"], "La graduation", "Les élèves lancent leur chapeau carré."),
]),
notion('C5-4', 0, I, 'ang5i-must-mustnt', [
  Q("Complétez : « You ___ use your phone in class. » (interdiction)", ["mustn't", "don't have to", "must", "can"], "mustn't", "Mustn't = interdiction."),
  Q("Que signifie « You don't have to wear a uniform » ?", ["Tu n'es pas obligé de porter un uniforme.", "Tu ne dois pas porter d'uniforme.", "Tu dois porter un uniforme.", "Tu ne peux pas porter d'uniforme."], "Tu n'es pas obligé de porter un uniforme.", "Don't have to = absence d'obligation."),
  Q("Complétez : « Students ___ arrive on time. » (obligation)", ["must", "mustn't", "can't", "might"], "must", "Must = obligation."),
]),
notion('C5-4', 0, I, 'ang5i-jeux-video-industrie', [
  Q("Quel jeu vidéo de construction, créé par un Suédois, est le plus vendu de l'histoire ?", ["Minecraft", "Fortnite", "Tetris", "Mario Kart"], "Minecraft", "Il appartient aujourd'hui à Microsoft."),
  Q("Que signifie « to level up » dans un jeu vidéo ?", ["Passer au niveau supérieur", "Recommencer", "Perdre une vie", "Mettre en pause"], "Passer au niveau supérieur", "Level = niveau."),
  Q("Que signifie « screen time » ?", ["Le temps passé devant les écrans", "L'heure du film", "La taille de l'écran", "Un jeu"], "Le temps passé devant les écrans", "Les parents le limitent souvent."),
]),
notion('C5-4', 0, D, 'ang5d-boarding-school', [
  Q("Qu'est-ce qu'une « boarding school » ?", ["Un internat", "Une école de surf", "Une école de nuit", "Une école en ligne"], "Un internat", "Eton ou Harrow en sont de célèbres exemples."),
  Q("Quelle école privée prestigieuse a formé une vingtaine de Premiers ministres britanniques ?", ["Eton College", "Hogwarts", "Harvard", "Sorbonne"], "Eton College", "Elle est située près de Windsor."),
  Q("Quelles universités britanniques sont les plus anciennes et les plus prestigieuses ?", ["Oxford et Cambridge", "Harvard et Yale", "Manchester et Leeds", "Dublin et Cork"], "Oxford et Cambridge", "On les surnomme « Oxbridge »."),
]),
notion('C5-4', 0, D, 'ang5d-ivy-league', [
  Q("Comment appelle-t-on le groupe des huit universités les plus prestigieuses du nord-est des États-Unis ?", ["L'Ivy League", "L'Oxbridge", "La Big Ten", "La Premier League"], "L'Ivy League", "Harvard, Yale, Princeton…"),
  Q("Quelle est la plus ancienne université des États-Unis, fondée en 1636 ?", ["Harvard", "Yale", "Stanford", "MIT"], "Harvard", "Elle se trouve à Cambridge, près de Boston."),
  Q("Pourquoi beaucoup d'étudiants américains contractent-ils un « student loan » ?", ["Pour payer des frais de scolarité très élevés", "Pour acheter une voiture", "Pour voyager", "Parce que l'université est gratuite"], "Pour payer des frais de scolarité très élevés", "La dette étudiante est un grand enjeu aux États-Unis."),
]),
notion('C5-4', 0, D, 'ang5d-gap-year', [
  Q("Qu'est-ce qu'une « gap year » ?", ["Une année de pause entre le lycée et l'université", "Une année de redoublement", "Une année sabbatique d'un professeur", "Une année bissextile"], "Une année de pause entre le lycée et l'université", "Les jeunes voyagent, travaillent ou font du bénévolat."),
  Q("Qu'est-ce qu'un « exchange student » ?", ["Un élève en échange scolaire à l'étranger", "Un élève qui change de classe", "Un élève qui échange ses cours", "Un étudiant en commerce"], "Un élève en échange scolaire à l'étranger", "Il vit souvent dans une famille d'accueil (host family)."),
  Q("Que signifie « host family » ?", ["Une famille d'accueil", "Une famille nombreuse", "Une famille royale", "Une famille d'hôtes de restaurant"], "Une famille d'accueil", "To host = accueillir."),
]),
notion('C5-4', 0, D, 'ang5d-sport-universitaire', [
  Q("Quelle célèbre course d'aviron oppose chaque année Oxford et Cambridge sur la Tamise ?", ["The Boat Race", "The Regatta Cup", "Le Tour de la Tamise", "The Henley Derby"], "The Boat Race", "Elle existe depuis 1829."),
  Q("Pourquoi des sportifs américains obtiennent-ils des bourses universitaires ?", ["Le sport universitaire est très suivi et rapporte beaucoup", "Le sport est interdit au lycée", "Les universités n'ont pas d'étudiants", "Par tirage au sort"], "Le sport universitaire est très suivi et rapporte beaucoup", "Les matchs universitaires remplissent des stades."),
  Q("Quel tournoi de basket universitaire américain est surnommé « March Madness » ?", ["Le championnat NCAA", "La NBA", "Le Super Bowl", "La World Series"], "Le championnat NCAA", "Il se déroule en mars."),
]),
notion('C5-4', 0, D, 'ang5d-present-perfect-for-since', [
  Q("Complétez : « I have played the piano ___ five years. »", ["for", "since", "during", "ago"], "for", "For + durée."),
  Q("Complétez : « She has been in this school ___ 2023. »", ["since", "for", "ago", "from"], "since", "Since + point de départ."),
  Q("Comment demande-t-on depuis combien de temps quelqu'un apprend l'anglais ?", ["How long have you been learning English?", "Since when you learn English?", "How long do you learn English?", "For how much time you learn English?"], "How long have you been learning English?", "Present perfect en be + ing."),
]),
notion('C5-4', 0, D, 'ang5d-lecture-loisirs', [
  Q("Quel journal intime fictif d'un collégien a été écrit par Jeff Kinney ?", ["Journal d'un dégonflé (Diary of a Wimpy Kid)", "Le Journal d'Anne Frank", "Matilda", "Wonder"], "Journal d'un dégonflé (Diary of a Wimpy Kid)", "Le héros s'appelle Greg Heffley."),
  Q("Quel roman de R. J. Palacio raconte l'entrée au collège d'un garçon au visage différent ?", ["Wonder", "Holes", "Hatchet", "Frindle"], "Wonder", "Le héros s'appelle Auggie."),
  Q("Que signifie « bookworm » ?", ["Un rat de bibliothèque (grand lecteur)", "Un ver dans un livre", "Un libraire", "Un marque-page"], "Un rat de bibliothèque (grand lecteur)", "Worm = ver."),
]),
notion('C5-4', 0, D, 'ang5d-netflix-series', [
  Q("Que signifie « to binge-watch » ?", ["Regarder plusieurs épisodes d'affilée", "Regarder un film au cinéma", "Zapper", "Éteindre la télévision"], "Regarder plusieurs épisodes d'affilée", "Les plateformes de streaming l'ont popularisé."),
  Q("Que signifie « spoiler » ?", ["Une révélation de la fin d'une histoire", "Une bande-annonce", "Un acteur", "Un épisode pilote"], "Une révélation de la fin d'une histoire", "« No spoilers, please! »"),
  Q("Que signifie « subtitles » ?", ["Les sous-titres", "Les titres", "Les génériques", "Les doublages"], "Les sous-titres", "Regarder en VO sous-titrée aide à progresser."),
]),
notion('C5-4', 0, D, 'ang5d-pocket-money-jobs', [
  Q("Que signifie « paper round » au Royaume-Uni ?", ["La tournée de distribution de journaux, petit job d'adolescent", "Un rouleau de papier", "Un examen écrit", "Un journal scolaire"], "La tournée de distribution de journaux, petit job d'adolescent", "On peut la faire dès 13 ans."),
  Q("Que signifie « babysitting » ?", ["Garder des enfants", "S'asseoir avec un bébé", "Une crèche", "Un jouet"], "Garder des enfants", "C'est un petit job courant chez les adolescents."),
  Q("Qu'est-ce qu'une « lemonade stand » aux États-Unis ?", ["Un petit stand où des enfants vendent de la limonade", "Une usine de boissons", "Un restaurant", "Une marque"], "Un petit stand où des enfants vendent de la limonade", "C'est un symbole de l'esprit d'entreprise."),
]),
# ══ C5-5 · Des langues, des lieux, des histoires ══
notion('C5-5', 0, F, 'ang5-langues-uk', [
  Q("Quelle langue celtique, en plus de l'anglais, est officielle au pays de Galles ?", ["Le gallois", "Le gaélique écossais", "L'irlandais", "Le breton"], "Le gallois", "Les panneaux y sont bilingues."),
  Q("Quelle langue est parlée, avec l'anglais, dans certaines régions des Highlands ?", ["Le gaélique écossais", "Le gallois", "Le cornique", "Le scots"], "Le gaélique écossais", "Il est minoritaire."),
  Q("Quelle langue est officielle en république d'Irlande avec l'anglais ?", ["L'irlandais (gaélique)", "Le gallois", "Le français", "Le scots"], "L'irlandais (gaélique)", "Elle est enseignée à l'école."),
]),
notion('C5-5', 0, F, 'ang5-mots-anglais-francais', [
  Q("Lequel de ces mots anglais est utilisé en français ?", ["Week-end", "Butterfly", "Kitchen", "Window"], "Week-end", "Parking, football, shopping aussi."),
  Q("Quel mot français est utilisé en anglais ?", ["Rendezvous", "Hello", "Goodbye", "Thanks"], "Rendezvous", "Déjà vu, menu, café aussi."),
  Q("Pourquoi l'anglais contient-il beaucoup de mots d'origine française ?", ["À cause de la conquête normande de 1066", "À cause de l'Union européenne", "Par hasard", "À cause d'Internet"], "À cause de la conquête normande de 1066", "Le français a été la langue de la cour pendant trois siècles."),
]),
notion('C5-5', 0, F, 'ang5-accents', [
  Q("Dans quel pays dit-on « G'day, mate! » pour dire bonjour ?", ["En Australie", "En Écosse", "Au Canada", "En Inde"], "En Australie", "Mate = copain."),
  Q("Comment dit-on « appartement » en anglais américain ?", ["Apartment", "Flat", "House", "Building"], "Apartment", "En anglais britannique, on dit flat."),
  Q("Que signifie « cookie » en anglais américain ?", ["Un biscuit", "Un cuisinier", "Une cuisine", "Un gâteau d'anniversaire"], "Un biscuit", "En anglais britannique : biscuit."),
]),
notion('C5-5', 0, F, 'ang5-pays-anglophones', [
  Q("Dans combien de pays environ l'anglais est-il langue officielle ?", ["Plus de 50", "Environ 5", "Environ 10", "Plus de 150"], "Plus de 50", "Sur tous les continents."),
  Q("Lequel de ces pays d'Asie a l'anglais comme langue officielle ?", ["Singapour", "La Chine", "Le Japon", "La Corée du Sud"], "Singapour", "Avec le chinois, le malais et le tamoul."),
  Q("Quel pays d'Afrique australe compte onze langues officielles, dont l'anglais ?", ["L'Afrique du Sud", "Le Maroc", "L'Égypte", "Le Sénégal"], "L'Afrique du Sud", "Douze depuis 2023 avec la langue des signes."),
]),
notion('C5-5', 0, F, 'ang5-noms-lieux', [
  Q("Pourquoi une ville américaine s'appelle-t-elle New York ?", ["En hommage au duc d'York", "Parce qu'elle est neuve", "Parce que c'était un nom amérindien", "En hommage à une ville d'Irlande"], "En hommage au duc d'York", "Elle s'appelait d'abord La Nouvelle-Amsterdam."),
  Q("Quel État américain porte le nom d'une reine d'Angleterre surnommée « la reine vierge » ?", ["La Virginie", "Le Maryland", "La Géorgie", "La Caroline"], "La Virginie", "En hommage à Élisabeth Ire."),
  Q("Quelle ville américaine porte un nom français, en hommage au régent Philippe d'Orléans ?", ["La Nouvelle-Orléans", "Boston", "Seattle", "Chicago"], "La Nouvelle-Orléans", "Elle est fondée en 1718 par des colons français."),
]),
notion('C5-5', 0, F, 'ang5-salutations-variantes', [
  Q("Que signifie « Cheers! » au Royaume-Uni, en plus de « Santé ! » ?", ["Merci !", "Au revoir à jamais !", "Bonjour !", "Pardon !"], "Merci !", "C'est un usage familier."),
  Q("Que signifie « Howdy! » dans le sud des États-Unis ?", ["Salut !", "Au revoir !", "Merci !", "À l'aide !"], "Salut !", "Contraction de « How do you do? »."),
  Q("Que signifie « See you later! » ?", ["À plus tard !", "Je te vois maintenant !", "Regarde !", "Bonjour !"], "À plus tard !", "See you soon! = à bientôt !"),
]),
notion('C5-5', 0, F, 'ang5-pilgrims-mayflower', [
  Q("Comment appelle-t-on les colons anglais arrivés en 1620 à bord du Mayflower ?", ["Les Pères pèlerins (Pilgrim Fathers)", "Les conquistadors", "Les Vikings", "Les pionniers de l'Ouest"], "Les Pères pèlerins (Pilgrim Fathers)", "Ils fuyaient les persécutions religieuses."),
  Q("Quelle fête américaine rappelle le premier repas partagé entre les Pilgrims et les Amérindiens ?", ["Thanksgiving", "Halloween", "Independence Day", "Labor Day"], "Thanksgiving", "Le premier aurait eu lieu en 1621."),
  Q("Dans quelle région des États-Unis les Pilgrims se sont-ils installés ?", ["La Nouvelle-Angleterre", "La Californie", "Le Texas", "La Floride"], "La Nouvelle-Angleterre", "À Plymouth, dans le Massachusetts."),
]),
notion('C5-5', 0, F, 'ang5-mots-voyageurs', [
  Q("De quelle langue vient le mot anglais « pyjamas » ?", ["De l'hindi (ou ourdou)", "Du latin", "Du grec", "Du japonais"], "De l'hindi (ou ourdou)", "Comme shampoo et bungalow."),
  Q("De quelle langue vient le mot « kangaroo » ?", ["D'une langue aborigène d'Australie", "Du français", "De l'allemand", "Du chinois"], "D'une langue aborigène d'Australie", "Il est noté par l'explorateur James Cook en 1770."),
  Q("De quelle langue vient le mot anglais « tycoon » (magnat) ?", ["Du japonais", "De l'arabe", "Du russe", "De l'espagnol"], "Du japonais", "Il signifie « grand seigneur »."),
]),
notion('C5-5', 0, I, 'ang5i-anglais-histoire', [
  Q("Quel peuple germanique a donné son nom à l'Angleterre (England) ?", ["Les Angles", "Les Saxons", "Les Normands", "Les Vikings"], "Les Angles", "England = la terre des Angles."),
  Q("Comment appelle-t-on l'ancien anglais, parlé avant 1100 ?", ["Le vieil anglais (Old English)", "Le moyen anglais", "L'anglais moderne", "Le scots"], "Le vieil anglais (Old English)", "Beowulf est écrit en vieil anglais."),
  Q("Quel poète du XIVe siècle a écrit Les Contes de Canterbury en moyen anglais ?", ["Geoffrey Chaucer", "Shakespeare", "John Milton", "Lord Byron"], "Geoffrey Chaucer", "On le considère comme le père de la littérature anglaise."),
]),
notion('C5-5', 0, I, 'ang5i-gb-us-vocabulaire', [
  Q("Comment dit-on « autoroute » en anglais américain ?", ["Highway (freeway)", "Motorway", "Lane", "Path"], "Highway (freeway)", "En anglais britannique : motorway."),
  Q("Comment dit-on « ascenseur » en anglais britannique ?", ["Lift", "Elevator", "Escalator", "Stairs"], "Lift", "En anglais américain : elevator."),
  Q("Que signifie « gas » en anglais américain ?", ["L'essence", "Le gaz uniquement", "Le gazon", "La vapeur"], "L'essence", "En anglais britannique : petrol."),
]),
notion('C5-5', 0, I, 'ang5i-orthographe-gb-us', [
  Q("Comment écrit-on « couleur » en anglais américain ?", ["Color", "Colour", "Coulor", "Collor"], "Color", "En anglais britannique : colour."),
  Q("Quel mot est écrit à la britannique ?", ["Centre", "Center", "Theater", "Favorite"], "Centre", "Les Américains écrivent center, theater, favorite."),
  Q("Quel lexicographe américain a simplifié l'orthographe américaine au XIXe siècle ?", ["Noah Webster", "Samuel Johnson", "Mark Twain", "Benjamin Franklin"], "Noah Webster", "Son dictionnaire paraît en 1828."),
]),
notion('C5-5', 0, I, 'ang5i-colonisation-amerique', [
  Q("Quelle est la première colonie anglaise permanente en Amérique, fondée en 1607 ?", ["Jamestown, en Virginie", "Plymouth", "New York", "Boston"], "Jamestown, en Virginie", "Pocahontas y joue un rôle célèbre."),
  Q("Combien de colonies anglaises fondent les États-Unis en 1776 ?", ["13", "50", "7", "20"], "13", "Elles sont représentées par les 13 bandes du drapeau."),
  Q("Quelle jeune Amérindienne est associée à la colonie de Jamestown ?", ["Pocahontas", "Sacagawea", "Mulan", "Moana"], "Pocahontas", "Elle épouse le colon John Rolfe et meurt en Angleterre."),
]),
notion('C5-5', 0, I, 'ang5i-langue-internationale', [
  Q("Pourquoi l'anglais est-il devenu une langue internationale ?", ["Grâce à l'Empire britannique puis à la puissance des États-Unis", "Parce qu'il est la plus ancienne langue", "Par décision de l'ONU", "Parce qu'il est le plus facile"], "Grâce à l'Empire britannique puis à la puissance des États-Unis", "On parle de langue de communication mondiale."),
  Q("Comment appelle-t-on une langue utilisée pour communiquer entre locuteurs de langues différentes ?", ["Une lingua franca", "Une langue morte", "Un dialecte", "Un argot"], "Une lingua franca", "L'anglais joue ce rôle aujourd'hui."),
  Q("Quelle langue compte le plus de locuteurs natifs dans le monde ?", ["Le chinois mandarin", "L'anglais", "L'espagnol", "Le hindi"], "Le chinois mandarin", "L'anglais compte le plus de locuteurs au total, langues secondes comprises."),
]),
notion('C5-5', 0, I, 'ang5i-noms-lieux-celtes', [
  Q("Que signifie le préfixe « Loch » dans « Loch Ness » ?", ["Lac (en gaélique)", "Monstre", "Montagne", "Château"], "Lac (en gaélique)", "En Irlande, on dit lough."),
  Q("Que signifie le préfixe gaélique « Bally- » dans des noms irlandais comme Ballymena ?", ["Ville, lieu habité", "Rivière", "Colline", "Château"], "Ville, lieu habité", "Du gaélique baile."),
  Q("Que signifie « Kil- » dans des noms comme Kilkenny ?", ["Église (cellule de moine)", "Roi", "Forêt", "Mer"], "Église (cellule de moine)", "Du gaélique cill."),
]),
notion('C5-5', 0, I, 'ang5i-australie-histoire', [
  Q("Qui sont les premiers colons britanniques envoyés en Australie en 1788 ?", ["Des bagnards (convicts)", "Des marchands", "Des missionnaires", "Des soldats uniquement"], "Des bagnards (convicts)", "La « First Fleet » arrive à Sydney."),
  Q("Quel navigateur a exploré la côte est de l'Australie en 1770 ?", ["James Cook", "Christophe Colomb", "Magellan", "Vasco de Gama"], "James Cook", "Il la revendique pour la Couronne britannique."),
  Q("Comment appelle-t-on les générations d'enfants aborigènes retirés de force à leurs familles ?", ["Les « générations volées » (Stolen Generations)", "Les pionniers", "Les convicts", "Les Anzacs"], "Les « générations volées » (Stolen Generations)", "Le gouvernement australien s'est excusé en 2008."),
]),
notion('C5-5', 0, I, 'ang5i-expressions-idiomatiques', [
  Q("Que signifie « It's a piece of cake » ?", ["C'est du gâteau (c'est facile).", "C'est un morceau de gâteau.", "C'est délicieux.", "C'est mon anniversaire."], "C'est du gâteau (c'est facile).", "Expression idiomatique."),
  Q("Que signifie « to break the ice » ?", ["Briser la glace (détendre l'atmosphère)", "Patiner", "Casser un glaçon", "Avoir froid"], "Briser la glace (détendre l'atmosphère)", "L'expression existe aussi en français."),
  Q("Que signifie « Break a leg! » au théâtre ?", ["Bonne chance !", "Attention, tu vas tomber !", "Casse-toi la jambe !", "Bravo !"], "Bonne chance !", "C'est l'équivalent de « Merde ! »."),
]),
notion('C5-5', 0, D, 'ang5d-empire-britannique', [
  Q("Quelle organisation regroupe aujourd'hui une cinquantaine de pays, surtout d'anciennes colonies britanniques ?", ["Le Commonwealth", "L'OTAN", "L'Union européenne", "L'ONU"], "Le Commonwealth", "Elle compte 56 membres."),
  Q("Dans combien de pays du Commonwealth le roi Charles III est-il chef d'État ?", ["15 (les royaumes du Commonwealth)", "56", "1", "100"], "15 (les royaumes du Commonwealth)", "Dont le Canada, l'Australie et la Nouvelle-Zélande."),
  Q("Quel pays du Commonwealth compte le plus d'habitants ?", ["L'Inde", "Le Royaume-Uni", "Le Canada", "L'Australie"], "L'Inde", "Elle est devenue une république en 1950."),
]),
notion('C5-5', 0, D, 'ang5d-langues-creoles', [
  Q("Comment appelle-t-on une langue née du contact entre l'anglais et des langues locales, comme en Jamaïque ?", ["Un créole", "Un dialecte écossais", "Un argot", "Une langue morte"], "Un créole", "Le patois jamaïcain en est un exemple."),
  Q("Quelle langue de Papouasie-Nouvelle-Guinée est issue de l'anglais ?", ["Le tok pisin", "Le swahili", "Le maori", "Le cornique"], "Le tok pisin", "Pisin vient de « pidgin »."),
  Q("Qu'est-ce que le « Hinglish » ?", ["Un mélange d'hindi et d'anglais", "Un dialecte écossais", "L'anglais de Hong Kong", "L'anglais de la Reine"], "Un mélange d'hindi et d'anglais", "Il est très utilisé dans les médias indiens."),
]),
notion('C5-5', 0, D, 'ang5d-dictionnaires', [
  Q("Quel dictionnaire britannique, commencé en 1857, est la référence de la langue anglaise ?", ["L'Oxford English Dictionary", "Le Larousse", "Le Webster", "Le Collins Junior"], "L'Oxford English Dictionary", "Il retrace l'histoire de chaque mot."),
  Q("Quel écrivain anglais a publié un célèbre dictionnaire en 1755 ?", ["Samuel Johnson", "Shakespeare", "Charles Dickens", "John Locke"], "Samuel Johnson", "Il l'a rédigé presque seul en neuf ans."),
  Q("Combien de mots environ Shakespeare aurait-il introduits ou popularisés dans la langue anglaise ?", ["Plus de 1 500", "Environ 10", "Environ 100 000", "Aucun"], "Plus de 1 500", "Comme « lonely » ou « eyeball »."),
]),
notion('C5-5', 0, D, 'ang5d-histoires-migrations-langue', [
  Q("De quelle langue viennent les mots anglais « sky », « egg » et « knife » ?", ["Du vieux norrois (des Vikings)", "Du latin", "Du français normand", "Du grec"], "Du vieux norrois (des Vikings)", "Les Vikings se sont installés dans le nord de l'Angleterre."),
  Q("Pourquoi dit-on « beef » pour la viande mais « cow » pour l'animal ?", ["Les nobles normands mangeaient la viande, les paysans saxons élevaient les animaux", "Par hasard", "À cause des Vikings", "À cause des Romains"], "Les nobles normands mangeaient la viande, les paysans saxons élevaient les animaux", "Beef vient du français « bœuf »."),
  Q("Quel quartier de Londres est connu pour sa communauté bangladaise et sa « Banglatown » ?", ["Brick Lane", "Chelsea", "Mayfair", "Notting Hill"], "Brick Lane", "On y trouve de nombreux restaurants de curry."),
]),
notion('C5-5', 0, D, 'ang5d-new-zealand', [
  Q("Comment les Maoris appellent-ils la Nouvelle-Zélande ?", ["Aotearoa (le pays du long nuage blanc)", "Oz", "Down Under", "Kiwiland"], "Aotearoa (le pays du long nuage blanc)", "Le maori est langue officielle."),
  Q("Quel traité de 1840 a été signé entre la Couronne britannique et des chefs maoris ?", ["Le traité de Waitangi", "Le traité de Paris", "Le traité de Versailles", "Le traité d'Utrecht"], "Le traité de Waitangi", "Il est considéré comme fondateur du pays."),
  Q("Quelle est la plus grande ville de Nouvelle-Zélande ?", ["Auckland", "Wellington", "Christchurch", "Sydney"], "Auckland", "La capitale est Wellington."),
]),
notion('C5-5', 0, D, 'ang5d-gullah-amerindiens', [
  Q("Quels mots anglais viennent de langues amérindiennes ?", ["Raccoon, moose, canoe", "Beef, pork, mutton", "Sky, egg, knife", "Shampoo, pyjamas, jungle"], "Raccoon, moose, canoe", "Ils désignent souvent des réalités du Nouveau Monde."),
  Q("Combien d'États américains portent un nom d'origine amérindienne ?", ["Environ la moitié", "Aucun", "Deux", "Tous"], "Environ la moitié", "Comme le Massachusetts, l'Ohio ou le Dakota."),
  Q("Quelle langue amérindienne a servi de code secret à l'armée américaine pendant la Seconde Guerre mondiale ?", ["Le navajo", "Le cherokee", "Le sioux", "L'apache"], "Le navajo", "Ces soldats sont appelés « code talkers »."),
]),
notion('C5-5', 0, D, 'ang5d-vrais-faux-amis', [
  Q("Que signifie « actually » ?", ["En fait", "Actuellement", "Activement", "Exactement"], "En fait", "Actuellement = currently."),
  Q("Que signifie « sensible » ?", ["Raisonnable", "Sensible", "Sensationnel", "Sensuel"], "Raisonnable", "Sensible (français) = sensitive."),
  Q("Que signifie « eventually » ?", ["Finalement", "Éventuellement", "Évidemment", "Événement"], "Finalement", "Éventuellement = possibly."),
]),
notion('C5-5', 0, D, 'ang5d-canada-bilinguisme', [
  Q("Quelle province canadienne a le français pour langue officielle ?", ["Le Québec", "L'Ontario", "L'Alberta", "La Colombie-Britannique"], "Le Québec", "Le Nouveau-Brunswick est officiellement bilingue."),
  Q("Comment appelle-t-on les francophones des provinces maritimes canadiennes, déportés en 1755 ?", ["Les Acadiens", "Les Cajuns uniquement", "Les Québécois", "Les Métis"], "Les Acadiens", "Certains se sont installés en Louisiane : les Cajuns."),
  Q("Quel pays a pour langues officielles l'anglais et le français, sur les billets et les produits ?", ["Le Canada", "Les États-Unis", "L'Australie", "L'Irlande"], "Le Canada", "Le bilinguisme fédéral date de 1969."),
]),
# ══ C5-6 · Le Royaume-Uni ══
notion('C5-6', 0, F, 'ang5-londres-lieux', [
  Q("Quelle grande roue offre une vue sur Londres au bord de la Tamise ?", ["Le London Eye", "Big Ben", "Le Shard", "Tower Bridge"], "Le London Eye", "Elle a été inaugurée en 2000."),
  Q("Quel pont de Londres s'ouvre pour laisser passer les bateaux ?", ["Tower Bridge", "London Bridge", "Westminster Bridge", "Millennium Bridge"], "Tower Bridge", "On le confond souvent avec London Bridge."),
  Q("Quel grand parc londonien abrite le Speakers' Corner, où chacun peut prendre la parole ?", ["Hyde Park", "Central Park", "Regent's Park", "Green Park"], "Hyde Park", "Central Park est à New York."),
]),
notion('C5-6', 0, F, 'ang5-symboles-nations', [
  Q("Quel est le symbole floral de l'Angleterre ?", ["La rose", "Le chardon", "Le trèfle", "La jonquille"], "La rose", "Le chardon pour l'Écosse, la jonquille et le poireau pour le pays de Galles."),
  Q("Quel est le symbole du pays de Galles, avec le poireau ?", ["La jonquille", "La rose", "Le trèfle", "Le chardon"], "La jonquille", "On la porte le 1er mars, jour de la Saint-David."),
  Q("Quel symbole représente l'Irlande du Nord et l'Irlande ?", ["Le trèfle (shamrock)", "La rose", "Le chardon", "La tulipe"], "Le trèfle (shamrock)", "Saint Patrick l'aurait utilisé pour expliquer la Trinité."),
]),
notion('C5-6', 0, F, 'ang5-sport-uk', [
  Q("Quel tournoi de tennis sur gazon se joue chaque été à Londres ?", ["Wimbledon", "Roland-Garros", "L'US Open", "L'Open d'Australie"], "Wimbledon", "On y mange des fraises à la crème."),
  Q("Quel sport a été codifié en Angleterre dans une école portant son nom ?", ["Le rugby", "Le football", "Le golf", "Le hockey"], "Le rugby", "L'école de Rugby, dans les Midlands."),
  Q("Quel championnat de football anglais est le plus regardé du monde ?", ["La Premier League", "La Liga", "La Serie A", "La MLS"], "La Premier League", "Avec des clubs comme Liverpool ou Manchester United."),
]),
notion('C5-6', 0, F, 'ang5-tea-culture', [
  Q("Quelle boisson est traditionnellement associée aux Britanniques ?", ["Le thé", "Le café", "Le vin", "Le jus d'orange"], "Le thé", "Souvent servi avec un nuage de lait."),
  Q("Que mange-t-on avec la confiture et la crème lors de l'afternoon tea ?", ["Des scones", "Des croissants", "Des crêpes", "Des tacos"], "Des scones", "La « clotted cream » vient des Cornouailles."),
  Q("Quel petit gâteau anglais est souvent servi au petit-déjeuner, grillé avec du beurre ?", ["Le crumpet", "Le cupcake", "Le donut", "Le brownie"], "Le crumpet", "Les crumpets sont pleins de petits trous."),
]),
notion('C5-6', 0, F, 'ang5-garde-royale', [
  Q("Que portent sur la tête les gardes devant Buckingham Palace ?", ["Un grand bonnet en fourrure noire (bearskin)", "Un chapeau de paille", "Une casquette", "Un casque de moto"], "Un grand bonnet en fourrure noire (bearskin)", "Ils portent une tunique rouge."),
  Q("Comment appelle-t-on la cérémonie de remplacement des gardes ?", ["La relève de la garde (Changing of the Guard)", "Le défilé militaire", "Le couronnement", "Le Trooping the Colour"], "La relève de la garde (Changing of the Guard)", "Elle attire de nombreux touristes."),
  Q("Quels gardiens en costume rouge et noir surveillent la tour de Londres ?", ["Les Beefeaters", "Les Bobbies", "Les Highlanders", "Les Marines"], "Les Beefeaters", "Ils veillent aussi sur les corbeaux de la tour."),
]),
notion('C5-6', 0, I, 'ang5i-parlement-westminster', [
  Q("Qui dirige le gouvernement au Royaume-Uni ?", ["Le Premier ministre", "Le roi", "Le président", "Le maire de Londres"], "Le Premier ministre", "Le roi règne mais ne gouverne pas."),
  Q("Quelle chambre du Parlement britannique est élue par les citoyens ?", ["La Chambre des communes", "La Chambre des lords", "Le Sénat", "Le Conseil privé"], "La Chambre des communes", "Les lords sont nommés ou héréditaires."),
  Q("Que signifie le surnom « the Mother of Parliaments » donné au Parlement de Westminster ?", ["Il a servi de modèle à de nombreux parlements", "Il est dirigé par une femme", "Il est le plus récent", "Il siège dans une église"], "Il a servi de modèle à de nombreux parlements", "Il remonte au XIIIe siècle."),
]),
notion('C5-6', 0, I, 'ang5i-ecosse', [
  Q("Quel vêtement traditionnel écossais est une jupe à motifs écossais ?", ["Le kilt", "Le sari", "Le kimono", "Le poncho"], "Le kilt", "Le motif s'appelle le tartan."),
  Q("Quel instrument de musique est emblématique de l'Écosse ?", ["La cornemuse (bagpipes)", "Le banjo", "Le violon", "Le didgeridoo"], "La cornemuse (bagpipes)", "Le didgeridoo est aborigène."),
  Q("Quel festival d'arts et de théâtre a lieu chaque été à Édimbourg ?", ["L'Edinburgh Festival Fringe", "Glastonbury", "Coachella", "Woodstock"], "L'Edinburgh Festival Fringe", "C'est le plus grand festival d'arts du monde."),
]),
notion('C5-6', 0, I, 'ang5i-pays-de-galles', [
  Q("Quelle est la capitale du pays de Galles ?", ["Cardiff", "Swansea", "Belfast", "Édimbourg"], "Cardiff", "Elle compte un grand stade de rugby."),
  Q("Quel sport est le plus populaire au pays de Galles ?", ["Le rugby", "Le cricket", "Le baseball", "Le hockey sur glace"], "Le rugby", "Le pays participe au Tournoi des Six Nations."),
  Q("Quel est le titre traditionnel de l'héritier du trône britannique ?", ["Prince de Galles", "Duc d'York", "Prince d'Écosse", "Lord de Londres"], "Prince de Galles", "William porte ce titre depuis 2022."),
]),
notion('C5-6', 0, I, 'ang5i-irlande-nord', [
  Q("Quel accord de 1998 a mis fin à trente ans de violences en Irlande du Nord ?", ["L'accord du Vendredi saint (Good Friday Agreement)", "Le traité de Versailles", "L'accord de Paris", "Le traité de Rome"], "L'accord du Vendredi saint (Good Friday Agreement)", "Il est signé le 10 avril 1998."),
  Q("Comment appelle-t-on la période de conflit en Irlande du Nord de 1968 à 1998 ?", ["Les Troubles", "La Grande Famine", "La guerre des Deux-Roses", "Le Blitz"], "Les Troubles", "Elle a fait environ 3 500 morts."),
  Q("Quelle merveille naturelle d'Irlande du Nord est formée de colonnes de basalte ?", ["La Chaussée des Géants (Giant's Causeway)", "Les falaises de Moher", "Stonehenge", "Ben Nevis"], "La Chaussée des Géants (Giant's Causeway)", "La légende l'attribue au géant Finn McCool."),
]),
notion('C5-6', 0, I, 'ang5i-monuments-anciens', [
  Q("Quel monument préhistorique formé de grandes pierres dressées se trouve dans le sud de l'Angleterre ?", ["Stonehenge", "Avebury Castle", "Hadrian's Wall", "Big Ben"], "Stonehenge", "Il a environ 4 500 ans."),
  Q("Quel mur romain traversait le nord de l'Angleterre pour se protéger des peuples du nord ?", ["Le mur d'Hadrien", "La Grande Muraille", "Le mur de Berlin", "Le mur des Lamentations"], "Le mur d'Hadrien", "Il est construit à partir de 122."),
  Q("Quel nom les Romains donnaient-ils à Londres ?", ["Londinium", "Lutèce", "Eboracum", "Camelot"], "Londinium", "Eboracum est York."),
]),
notion('C5-6', 0, I, 'ang5i-musique-uk', [
  Q("Quel grand festival de musique en plein air a lieu dans le Somerset ?", ["Glastonbury", "Woodstock", "Coachella", "Les Vieilles Charrues"], "Glastonbury", "Il existe depuis 1970."),
  Q("Quel mouvement musical des années 1960 désigne le succès des groupes britanniques aux États-Unis ?", ["L'invasion britannique (British Invasion)", "La Brit Pop des années 1990", "Le punk", "La Motown"], "L'invasion britannique (British Invasion)", "Les Beatles et les Rolling Stones en sont les têtes d'affiche."),
  Q("Quel groupe de Manchester, mené par les frères Gallagher, symbolise la Britpop ?", ["Oasis", "Blur", "Radiohead", "Coldplay"], "Oasis", "Le groupe s'est reformé en 2025."),
]),
notion('C5-6', 0, D, 'ang5d-brexit-consequences', [
  Q("En quelle année le Royaume-Uni a-t-il officiellement quitté l'Union européenne ?", ["2020", "2016", "2019", "2023"], "2020", "Le référendum avait eu lieu en 2016."),
  Q("Quelle nation du Royaume-Uni a voté majoritairement pour rester dans l'UE en 2016 ?", ["L'Écosse", "L'Angleterre", "Le pays de Galles", "Aucune"], "L'Écosse", "L'Irlande du Nord aussi."),
  Q("Quel mot-valise désigne la sortie du Royaume-Uni de l'UE ?", ["Brexit", "Grexit", "Britout", "Exitain"], "Brexit", "British + exit."),
]),
notion('C5-6', 0, D, 'ang5d-devolution', [
  Q("Comment appelle-t-on le transfert de pouvoirs à l'Écosse, au pays de Galles et à l'Irlande du Nord ?", ["La dévolution", "La décentralisation française", "Le fédéralisme américain", "L'indépendance"], "La dévolution", "Elle date de 1998-1999."),
  Q("En quelle année les Écossais ont-ils rejeté l'indépendance par référendum ?", ["2014", "1998", "2020", "2005"], "2014", "Le « non » l'a emporté avec 55 %."),
  Q("Dans quelle ville siège le Parlement écossais ?", ["Édimbourg", "Glasgow", "Aberdeen", "Inverness"], "Édimbourg", "Dans le quartier de Holyrood."),
]),
notion('C5-6', 0, D, 'ang5d-nhs-societe', [
  Q("Comment s'appelle le système de santé public britannique, créé en 1948 ?", ["Le NHS (National Health Service)", "La Sécurité sociale", "Medicare", "L'OMS"], "Le NHS (National Health Service)", "Les soins y sont gratuits au point d'accès."),
  Q("Comment appelle-t-on familièrement un policier britannique ?", ["A bobby", "A cop uniquement", "A sheriff", "A ranger"], "A bobby", "En hommage à Robert (Bobby) Peel, fondateur de la police londonienne."),
  Q("Quel rapport de 1942 de William Beveridge a inspiré l'État-providence britannique ?", ["Le rapport Beveridge", "Le rapport Brundtland", "Le rapport Marshall", "Le rapport Churchill"], "Le rapport Beveridge", "Il propose de protéger « du berceau à la tombe »."),
]),
notion('C5-6', 0, D, 'ang5d-histoire-uk-reperes', [
  Q("Quelle guerre civile a opposé deux branches de la famille royale anglaise au XVe siècle ?", ["La guerre des Deux-Roses", "La guerre de Cent Ans", "La guerre de Sécession", "La guerre des Boers"], "La guerre des Deux-Roses", "La rose rouge des Lancastre contre la rose blanche des York."),
  Q("Quel roi anglais a été exécuté en 1649 après la guerre civile ?", ["Charles Ier", "Henri VIII", "George III", "Jacques II"], "Charles Ier", "Oliver Cromwell dirige ensuite le pays."),
  Q("Quel Premier ministre a dirigé le Royaume-Uni pendant la Seconde Guerre mondiale ?", ["Winston Churchill", "Margaret Thatcher", "Tony Blair", "Neville Chamberlain"], "Winston Churchill", "Il entre en fonction en 1940."),
]),
notion('C5-6', 0, D, 'ang5d-diversite-uk', [
  Q("Comment appelle-t-on la génération d'immigrés caribéens arrivés au Royaume-Uni à partir de 1948 ?", ["La génération Windrush", "La génération X", "Les Pilgrims", "Les Mods"], "La génération Windrush", "Du nom du navire Empire Windrush."),
  Q("Quel grand carnaval caribéen a lieu chaque été dans un quartier de Londres ?", ["Le carnaval de Notting Hill", "Le carnaval de Rio", "Le Mardi gras", "Le carnaval de Venise"], "Le carnaval de Notting Hill", "C'est l'un des plus grands d'Europe."),
  Q("Quel maire de Londres, élu en 2016, est le premier maire musulman d'une grande capitale occidentale ?", ["Sadiq Khan", "Boris Johnson", "Ken Livingstone", "Rishi Sunak"], "Sadiq Khan", "Il est d'origine pakistanaise."),
]),
notion('C5-6', 0, D, 'ang5d-industrie-revolution-uk', [
  Q("Dans quel pays la révolution industrielle a-t-elle commencé au XVIIIe siècle ?", ["Le Royaume-Uni", "La France", "Les États-Unis", "L'Allemagne"], "Le Royaume-Uni", "Grâce au charbon et à la machine à vapeur."),
  Q("Quelle ville anglaise était le grand centre de l'industrie du coton au XIXe siècle ?", ["Manchester", "Oxford", "Bath", "Brighton"], "Manchester", "On la surnommait Cottonopolis."),
  Q("Quel ingénieur écossais a perfectionné la machine à vapeur ?", ["James Watt", "Isaac Newton", "Alexander Graham Bell", "Charles Darwin"], "James Watt", "L'unité de puissance porte son nom."),
]),
notion('C5-6', 0, D, 'ang5d-premiers-ministres', [
  Q("Quelle Première ministre conservatrice, surnommée « la Dame de fer », a gouverné de 1979 à 1990 ?", ["Margaret Thatcher", "Theresa May", "Liz Truss", "Élisabeth II"], "Margaret Thatcher", "Elle est la première femme à ce poste."),
  Q("Quel Premier ministre travailliste a été élu en 2024 ?", ["Keir Starmer", "Rishi Sunak", "Tony Blair", "Boris Johnson"], "Keir Starmer", "Il met fin à 14 ans de gouvernements conservateurs."),
  Q("Quels sont les deux grands partis politiques britanniques ?", ["Le Parti conservateur et le Parti travailliste", "Les démocrates et les républicains", "Les verts et les libéraux uniquement", "Le Sinn Féin et le SNP"], "Le Parti conservateur et le Parti travailliste", "Les conservateurs sont surnommés les Tories."),
]),
]

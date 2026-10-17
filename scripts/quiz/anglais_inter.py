from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('L-2', 1, I, 'ang-simple-vs-continu', [
  Q("Choisissez : « She usually ___ to school, but today she ___ the bus. »", ["walks / takes", "walks / is taking", "is walking / takes", "walk / is taking"], "walks / is taking", "Habitude (usually) → présent simple ; action en cours aujourd'hui → be + -ing."),
  Q("Quelle phrase est incorrecte ?", ["I am knowing the answer.", "I know the answer.", "I'm reading a book.", "She likes chocolate."], "I am knowing the answer.", "Les verbes d'état (know, like, want, believe) ne s'emploient généralement pas à la forme en -ing."),
  Q("Complétez : « Water ___ at 100 °C. »", ["is boiling", "boils", "boil", "boiled"], "boils", "Une vérité générale s'exprime au présent simple."),
]),
notion('L-2', 1, I, 'ang-preterit-questions', [
  Q("Quelle question au prétérit est correcte ?", ["Did you went to the cinema?", "Did you go to the cinema?", "Do you went to the cinema?", "Went you to the cinema?"], "Did you go to the cinema?", "Did + sujet + base verbale."),
  Q("Quelle est la forme négative de « He bought a car » ?", ["He didn't bought a car.", "He didn't buy a car.", "He doesn't bought a car.", "He not bought a car."], "He didn't buy a car.", "Après didn't, le verbe revient à la base verbale."),
  C("Cliquez sur l'auxiliaire qui marque le passé.", "Where [did] you spend your holidays last year?", "Did porte la marque du passé ; spend reste à la base verbale."),
]),
notion('L-1', 1, I, 'ang-irreguliers-2', [
  Q("Quel est le participe passé de « write » ?", ["wrote", "written", "writed", "writing"], "written", "Write – wrote – written."),
  Q("Quel est le prétérit de « think » ?", ["thinked", "thought", "thank", "taught"], "thought", "Think – thought – thought. Taught est le prétérit de teach."),
  Q("Quel est le prétérit de « bring » ?", ["brang", "brought", "bringed", "brung"], "brought", "Bring – brought – brought."),
]),
notion('L-2', 1, I, 'ang-present-perfect', [
  Q("Complétez : « I ___ never ___ to Australia. »", ["have / been", "did / go", "am / gone", "had / be"], "have / been", "Le present perfect (have + participe passé) relie le passé au présent : expérience de vie."),
  Q("Complétez : « She ___ in Paris since 2015. »", ["lives", "has lived", "lived", "is living"], "has lived", "Avec since, pour une situation qui dure encore, on emploie le present perfect (le français utilise le présent)."),
  Q("Quelle phrase est correcte ?", ["I have seen this film yesterday.", "I saw this film yesterday.", "I have saw this film yesterday.", "I seen this film yesterday."], "I saw this film yesterday.", "Avec un moment passé précis (yesterday), on emploie le prétérit."),
]),
notion('L-2', 1, I, 'ang-for-since', [
  Q("Complétez : « I have known her ___ ten years. »", ["since", "for", "during", "ago"], "for", "For + durée ; since + point de départ."),
  Q("Complétez : « They have lived here ___ 2010. »", ["for", "since", "ago", "during"], "since", "2010 est un point de départ dans le temps."),
  Q("Complétez : « I met him three years ___. »", ["for", "since", "ago", "before"], "ago", "Ago s'emploie avec le prétérit : il y a trois ans."),
]),
notion('L-2', 1, I, 'ang-will', [
  Q("Complétez : « I think it ___ be sunny tomorrow. »", ["will", "is", "going", "does"], "will", "Will + base verbale exprime une prédiction ou une décision spontanée."),
  Q("Quelle phrase exprime une décision prise sur le moment ?", ["I'm going to buy a car next year.", "The phone is ringing. I'll answer it!", "I bought a car.", "I have bought a car."], "The phone is ringing. I'll answer it!", "Will (I'll) pour une décision spontanée ; going to pour une intention déjà formée."),
  Q("Quelle est la forme négative de « will » ?", ["willn't", "won't", "don't will", "not will"], "won't", "Won't = will not."),
]),
notion('L-2', 1, I, 'ang-modaux', [
  Q("Complétez : « You ___ wear a seatbelt in a car. It's the law. »", ["can", "must", "may", "might"], "must", "Must exprime une obligation forte."),
  Q("Complétez : « You ___ eat too many sweets. It's bad for your teeth. »", ["shouldn't", "mustn't to", "don't should", "can"], "shouldn't", "Should exprime un conseil ; shouldn't, un conseil négatif."),
  Q("Que signifie « You don't have to come » ?", ["Tu ne dois pas venir (interdiction)", "Tu n'es pas obligé de venir", "Tu peux venir", "Tu viendras"], "Tu n'es pas obligé de venir", "Mustn't exprime une interdiction ; don't have to, une absence d'obligation."),
]),
notion('L-2', 1, I, 'ang-comparatif-long', [
  Q("Quel est le comparatif de « expensive » ?", ["expensiver", "more expensive", "most expensive", "expensivest"], "more expensive", "Adjectifs longs : more + adjectif + than."),
  Q("Complétez : « This is ___ book I have ever read. »", ["the more interesting", "the most interesting", "most interesting", "the interestingest"], "the most interesting", "Superlatif des adjectifs longs : the most + adjectif."),
  Q("Complétez : « Tom is as tall ___ his brother. »", ["than", "as", "that", "like"], "as", "Comparatif d'égalité : as + adjectif + as."),
]),
notion('L-2', 1, I, 'ang-superlatif', [
  Q("Quel est le superlatif de « happy » ?", ["the happyest", "the happiest", "the most happy", "the happier"], "the happiest", "Adjectif terminé par -y : y → i + -est."),
  Q("Quel est le superlatif de « bad » ?", ["the baddest", "the worst", "the worse", "the most bad"], "the worst", "Bad – worse – the worst."),
  Q("Complétez : « Mount Everest is the ___ mountain in the world. »", ["higher", "highest", "most high", "more high"], "highest", "High est court : the highest."),
]),
notion('L-2', 1, I, 'ang-relatifs', [
  Q("Complétez : « The girl ___ lives next door is my friend. »", ["which", "who", "where", "what"], "who", "Who pour une personne ; which pour une chose ; that pour les deux."),
  Q("Complétez : « This is the house ___ I was born. »", ["who", "which", "where", "when"], "where", "Where pour un lieu."),
  Q("Complétez : « The book ___ you lent me was great. »", ["who", "which", "where", "whose"], "which", "Ici, le relatif peut aussi être omis : The book you lent me…"),
]),
notion('L-2', 1, I, 'ang-pronoms-complements', [
  Q("Complétez : « Can you help ___? » (moi)", ["I", "me", "my", "mine"], "me", "Pronoms compléments : me, you, him, her, it, us, them."),
  Q("Complétez : « I like ___. » (eux)", ["they", "their", "them", "theirs"], "them", "They (sujet) → them (complément)."),
  Q("Complétez : « This bag is ___. » (à moi)", ["my", "me", "mine", "I"], "mine", "Pronoms possessifs : mine, yours, his, hers, ours, theirs."),
]),
notion('L-2', 1, I, 'ang-prepositions-temps', [
  Q("Complétez : « My birthday is ___ May. »", ["on", "in", "at", "to"], "in", "In + mois, saison, année ; on + jour, date ; at + heure."),
  Q("Complétez : « The film starts ___ 8 o'clock. »", ["in", "on", "at", "by"], "at", "At + heure précise."),
  Q("Complétez : « We have English ___ Monday. »", ["in", "at", "on", "to"], "on", "On + jour de la semaine."),
]),
notion('L-2', 1, I, 'ang-countable', [
  Q("Complétez : « How ___ sugar do you want? »", ["many", "much", "lot", "few"], "much", "Much + indénombrable ; many + dénombrable pluriel."),
  Q("Complétez : « How ___ students are there? »", ["much", "many", "lot", "little"], "many", "Students est dénombrable."),
  Q("Lequel de ces noms est indénombrable en anglais ?", ["chair", "information", "apple", "book"], "information", "Information, advice, furniture, news sont indénombrables en anglais : pas de -s."),
]),
notion('L-2', 1, I, 'ang-question-tags', [
  Q("Complétez : « You're French, ___? »", ["isn't it", "aren't you", "don't you", "are you"], "aren't you", "Le question tag reprend l'auxiliaire à la forme opposée."),
  Q("Complétez : « She doesn't like fish, ___? »", ["does she", "doesn't she", "is she", "did she"], "does she", "Phrase négative → tag affirmatif."),
  Q("Complétez : « They went to London, ___? »", ["didn't they", "don't they", "weren't they", "did they"], "didn't they", "Prétérit affirmatif → didn't."),
]),
notion('L-2', 1, I, 'ang-passif', [
  Q("Mettez au passif : « Shakespeare wrote Hamlet. »", ["Hamlet wrote by Shakespeare.", "Hamlet was written by Shakespeare.", "Hamlet is wrote by Shakespeare.", "Hamlet has write by Shakespeare."], "Hamlet was written by Shakespeare.", "Passif : be (au temps du verbe actif) + participe passé."),
  Q("Complétez : « English ___ in many countries. »", ["speaks", "is spoken", "is speaking", "spoke"], "is spoken", "Présent passif : is + spoken."),
  C("Cliquez sur le participe passé de la forme passive.", "The Eiffel Tower was [built] for the 1889 World's Fair.", "Was built : be au prétérit + participe passé."),
]),
notion('L-2', 1, I, 'ang-ing-to', [
  Q("Complétez : « I enjoy ___ to music. »", ["to listen", "listening", "listen", "listened"], "listening", "Enjoy, finish, mind, avoid sont suivis de -ing."),
  Q("Complétez : « I want ___ a doctor. »", ["being", "to be", "be", "been"], "to be", "Want, decide, hope, need sont suivis de to + base verbale."),
  Q("Complétez : « She is good at ___. »", ["to draw", "drawing", "draw", "drew"], "drawing", "Après une préposition (at, of, about…), on emploie -ing."),
]),
notion('L-2', 1, I, 'ang-conditionnel-1', [
  Q("Complétez : « If it rains, we ___ at home. »", ["stay", "will stay", "would stay", "stayed"], "will stay", "Condition réelle : if + présent, will + base verbale."),
  Q("Quelle phrase est correcte ?", ["If I will see him, I will tell him.", "If I see him, I will tell him.", "If I saw him, I will tell him.", "If I see him, I told him."], "If I see him, I will tell him.", "Pas de will après if."),
  Q("Complétez : « If you heat ice, it ___. »", ["melts", "will melting", "melted", "would melt"], "melts", "Vérité générale : if + présent, présent."),
]),
notion('L-2', 1, I, 'ang-preterit-continu', [
  Q("Complétez : « I ___ TV when the phone rang. »", ["watched", "was watching", "am watching", "have watched"], "was watching", "Was/were + -ing : action en cours dans le passé, interrompue par un événement au prétérit."),
  C("Cliquez sur le verbe au prétérit en be + -ing.", "While she [was cooking], the cat jumped on the table.", "Was cooking décrit l'action en cours ; jumped, l'événement ponctuel."),
  Q("Complétez : « What ___ you doing at 8 pm yesterday? »", ["was", "were", "did", "are"], "were", "You → were."),
]),
notion('L-1', 0, I, 'ang-comprehension-inference', [
  Q("« Emma put on her coat, took her umbrella and sighed when she looked outside. » Quel temps fait-il probablement ?", ["Il fait beau et chaud", "Il pleut", "Il fait nuit", "C'est l'été"], "Il pleut", "On déduit le temps des indices : manteau, parapluie, soupir."),
  Q("« Jack hasn't eaten since this morning and keeps looking at the clock before lunch. » Comment se sent Jack ?", ["Fatigué", "Affamé", "Triste", "En colère"], "Affamé", "Le texte ne le dit pas : il faut inférer."),
  Q("« The shop was closed, so Mia went home empty-handed. » Qu'a fait Mia ?", ["Elle a acheté beaucoup de choses", "Elle est rentrée sans rien acheter", "Elle est restée devant le magasin", "Elle a ouvert le magasin"], "Elle est rentrée sans rien acheter", "Empty-handed = les mains vides."),
]),
notion('L-1', 0, I, 'ang-connecteurs', [
  Q("Que signifie « however » ?", ["parce que", "cependant", "donc", "ensuite"], "cependant", "However introduit une opposition."),
  Q("Quel connecteur exprime la conséquence ?", ["although", "so", "but", "because"], "so", "So = donc ; because = parce que ; although = bien que."),
  Q("Que signifie « although » ?", ["bien que", "parce que", "donc", "afin de"], "bien que", "Although it was cold, we went out = bien qu'il fasse froid…"),
]),
notion('L-1', 1, I, 'ang-phrasal-verbs', [
  Q("Que signifie « give up » ?", ["donner", "abandonner, renoncer", "se lever", "ramasser"], "abandonner, renoncer", "Don't give up! = N'abandonne pas !"),
  Q("Que signifie « look for » ?", ["regarder", "chercher", "s'occuper de", "admirer"], "chercher", "Look after = s'occuper de ; look at = regarder."),
  Q("Que signifie « get up » ?", ["se lever", "monter", "obtenir", "partir"], "se lever", "Wake up = se réveiller."),
]),
notion('L-1', 1, I, 'ang-faux-amis-2', [
  Q("Que signifie « eventually » ?", ["éventuellement", "finalement", "parfois", "rapidement"], "finalement", "Éventuellement se dit possibly."),
  Q("Que signifie « to attend a meeting » ?", ["attendre une réunion", "assister à une réunion", "annuler une réunion", "organiser une réunion"], "assister à une réunion", "Attendre se dit to wait for."),
  Q("Que signifie « a journey » ?", ["une journée", "un voyage, un trajet", "un journal", "un jour férié"], "un voyage, un trajet", "Une journée se dit a day."),
]),
notion('L-1', 1, I, 'ang-gb-us', [
  Q("Comment dit-on « appartement » en anglais américain ?", ["flat", "apartment", "house", "room"], "apartment", "Flat est britannique."),
  Q("Quel mot britannique correspond à l'américain « fall » (automne) ?", ["winter", "autumn", "spring", "summer"], "autumn", "Fall est américain, autumn britannique."),
  Q("Comment dit-on « frites » en anglais britannique ?", ["chips", "fries", "crisps", "French chips"], "chips", "Chips (GB) = fries (US) ; crisps (GB) = chips (US) = chips en français."),
]),
notion('L-3', 0, I, 'ang-histoire-uk', [
  Q("En quelle année Guillaume le Conquérant envahit-il l'Angleterre ?", ["1066", "1215", "1492", "1789"], "1066", "La bataille d'Hastings marque le début de la domination normande."),
  Q("Quel document de 1215 limite le pouvoir du roi d'Angleterre ?", ["La Magna Carta", "La Déclaration d'indépendance", "Le Bill of Rights", "La Constitution"], "La Magna Carta", "Elle est considérée comme un texte fondateur des libertés."),
  Q("Quelle reine a régné le plus longtemps sur le Royaume-Uni ?", ["Victoria", "Elizabeth II", "Elizabeth Ire", "Anne"], "Elizabeth II", "Elizabeth II a régné de 1952 à 2022, soit 70 ans."),
]),
notion('L-3', 0, I, 'ang-histoire-usa', [
  Q("En quelle année les colonies américaines déclarent-elles leur indépendance ?", ["1620", "1776", "1865", "1914"], "1776", "La Déclaration d'indépendance est adoptée le 4 juillet 1776."),
  Q("Qui est le premier président des États-Unis ?", ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Benjamin Franklin"], "George Washington", "Il est président de 1789 à 1797."),
  Q("Quel pasteur prononce le discours « I Have a Dream » en 1963 ?", ["Malcolm X", "Martin Luther King", "Barack Obama", "Nelson Mandela"], "Martin Luther King", "Il le prononce lors de la marche sur Washington."),
]),
notion('L-3', 0, I, 'ang-litterature', [
  Q("Qui a écrit Roméo et Juliette ?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Oscar Wilde"], "William Shakespeare", "Shakespeare (1564-1616) est le plus célèbre dramaturge anglais."),
  Q("Quelle autrice britannique a créé Harry Potter ?", ["J. K. Rowling", "Agatha Christie", "Roald Dahl", "Virginia Woolf"], "J. K. Rowling", "Le premier tome paraît en 1997."),
  Q("Quel auteur britannique a écrit Charlie et la Chocolaterie ?", ["Roald Dahl", "Lewis Carroll", "C. S. Lewis", "J. R. R. Tolkien"], "Roald Dahl", "Lewis Carroll a écrit Alice au pays des merveilles."),
]),
notion('L-3', 1, I, 'ang-institutions-uk', [
  Q("Quel est le régime politique du Royaume-Uni ?", ["Une république présidentielle", "Une monarchie constitutionnelle et parlementaire", "Une monarchie absolue", "Une fédération"], "Une monarchie constitutionnelle et parlementaire", "Le roi règne, le gouvernement gouverne."),
  Q("Où réside officiellement le Premier ministre britannique ?", ["Buckingham Palace", "10 Downing Street", "Westminster Abbey", "The Tower of London"], "10 Downing Street", "Buckingham Palace est la résidence londonienne du souverain."),
  Q("Comment s'appellent les deux chambres du Parlement britannique ?", ["Le Sénat et l'Assemblée", "La Chambre des communes et la Chambre des lords", "Le Congrès et le Sénat", "La Chambre haute et la Diète"], "La Chambre des communes et la Chambre des lords", "Aux États-Unis : Chambre des représentants et Sénat (le Congrès)."),
]),
notion('L-3', 1, I, 'ang-ecole-usa', [
  Q("Comment appelle-t-on le lycée aux États-Unis ?", ["Primary school", "High school", "College", "Kindergarten"], "High school", "College désigne l'enseignement supérieur aux États-Unis."),
  Q("Comment appelle-t-on le bal de fin d'année d'un lycée américain ?", ["The prom", "The fair", "The party night", "The ball game"], "The prom", "Le prom est un moment important de la vie lycéenne américaine."),
  Q("Que désigne « grade » dans le système scolaire américain ?", ["Une matière", "Le niveau de classe (5th grade…) ou une note", "Un professeur", "Une école"], "Le niveau de classe (5th grade…) ou une note", "5th grade correspond à peu près au CM2."),
]),
notion('L-2', 0, I, 'ang-exprimer-opinion', [
  Q("Quelle expression introduit une opinion ?", ["In my opinion…", "Once upon a time…", "First of all, take…", "See you later"], "In my opinion…", "On peut aussi dire I think…, I believe…, As far as I'm concerned…"),
  Q("Comment exprime-t-on poliment son désaccord ?", ["You're wrong!", "I'm afraid I don't agree.", "No way!", "Shut up!"], "I'm afraid I don't agree.", "I'm afraid… adoucit le propos."),
  Q("Que signifie « I couldn't agree more » ?", ["Je ne suis pas du tout d'accord", "Je suis tout à fait d'accord", "Je ne sais pas", "Je ne peux pas répondre"], "Je suis tout à fait d'accord", "Littéralement : je ne pourrais pas être plus d'accord."),
]),
notion('L-2', 0, I, 'ang-ecrire-lettre', [
  Q("Comment commence-t-on une lettre formelle à une personne dont on ignore le nom ?", ["Hi!", "Dear Sir or Madam,", "Hello friend,", "Yo,"], "Dear Sir or Madam,", "On termine alors par Yours faithfully (GB)."),
  Q("Comment termine-t-on un courriel amical ?", ["Yours faithfully,", "Best wishes,", "To whom it may concern,", "Dear Sir,"], "Best wishes,", "On peut aussi écrire Love, See you soon, Take care."),
  Q("Comment commence-t-on un courriel à un ami ?", ["Dear Sir,", "Hi Tom,", "To whom it may concern,", "Madam,"], "Hi Tom,", "Le registre dépend du destinataire."),
]),
notion('L-1', 0, I, 'ang-comprehension-orale', [
  Q("Un message d'aéroport dit : « Flight BA 304 to London is now boarding at gate 12. » Que faut-il faire ?", ["Attendre le lendemain", "Se rendre porte 12 pour embarquer", "Récupérer ses bagages", "Changer de terminal"], "Se rendre porte 12 pour embarquer", "Boarding = embarquement ; gate = porte."),
  Q("Un répondeur dit : « I'm not available right now, please leave a message after the beep. » Que doit faire l'appelant ?", ["Rappeler plus tard obligatoirement", "Laisser un message après le bip", "Envoyer un courriel", "Raccrocher"], "Laisser un message après le bip", "Leave a message = laisser un message."),
  Q("Dans une gare, on entend : « The 10:15 train to Oxford is delayed by 20 minutes. » À quelle heure partira le train ?", ["10 h 15", "10 h 35", "10 h 20", "9 h 55"], "10 h 35", "Delayed by 20 minutes : 10 h 15 + 20 min = 10 h 35."),
]),
notion('L-2', 1, I, 'ang-ordre-mots', [
  Q("Quelle phrase a un ordre correct ?", ["I like very much chocolate.", "I like chocolate very much.", "I very much chocolate like.", "Very much I like chocolate."], "I like chocolate very much.", "En anglais, on ne sépare pas le verbe de son complément d'objet."),
  Q("Quelle phrase est correcte ?", ["Always she is late.", "She is always late.", "She always is late.", "She is late always."], "She is always late.", "L'adverbe de fréquence se place après be."),
  Q("Quelle question est correcte ?", ["Where you live?", "Where do you live?", "Where you do live?", "Where does you live?"], "Where do you live?", "Mot interrogatif + auxiliaire + sujet + verbe."),
  Q("Quelle phrase est correcte ?", ["Yesterday I went to the cinema with my friends.", "I went yesterday with my friends to the cinema.", "I went with my friends yesterday the cinema.", "To the cinema yesterday I went with friends my."], "Yesterday I went to the cinema with my friends.", "Ordre habituel : sujet + verbe + lieu + temps, le temps pouvant aussi ouvrir la phrase."),
]),
notion('L-3', 0, I, 'ang-symboles', [
  Q("Comment appelle-t-on le drapeau du Royaume-Uni ?", ["The Stars and Stripes", "The Union Jack (Union Flag)", "The Maple Leaf", "The Tricolour"], "The Union Jack (Union Flag)", "Il superpose les croix de saint Georges, saint André et saint Patrick."),
  Q("Que représentent les 50 étoiles du drapeau américain ?", ["Les présidents", "Les 50 États", "Les 50 plus grandes villes", "Les années d'indépendance"], "Les 50 États", "Les 13 bandes représentent les 13 colonies d'origine."),
  Q("Quel symbole figure sur le drapeau du Canada ?", ["Une feuille d'érable", "Un aigle", "Un lion", "Une étoile"], "Une feuille d'érable", "Ce drapeau est adopté en 1965."),
]),
]

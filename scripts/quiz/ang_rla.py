# Anglais · Repères linguistiques : compréhension, expression, interaction et médiation (25 questions par niveau)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ RL-1 · Compréhension de l'oral et de l'écrit ══
notion('RL-1', 0, F, 'angrl-consignes-2', [
  Q("Que signifie la consigne « Fill in the blanks » ?", ["Complétez les trous", "Coloriez les cases", "Lisez à voix haute", "Effacez les mots"], "Complétez les trous", "Blank = espace vide."),
  Q("Que signifie « Underline the verbs » ?", ["Soulignez les verbes", "Entourez les verbes", "Barrez les verbes", "Copiez les verbes"], "Soulignez les verbes", "To circle = entourer."),
  Q("Que signifie « Work in pairs » ?", ["Travaillez par deux", "Travaillez seul", "Travaillez en groupe de quatre", "Travaillez en silence"], "Travaillez par deux", "In groups = en groupes."),
]),
notion('RL-1', 0, F, 'angrl-mini-textes-1', [
  Q("« Lucy has a dog called Max. Max is black and very friendly. » De quelle couleur est Max ?", ["Noir", "Blanc", "Marron", "Gris"], "Noir", "On repère l'adjectif black."),
  Q("« My brother is twelve and I am ten. » Qui est le plus âgé ?", ["Le frère", "Le narrateur", "Ils ont le même âge", "On ne sait pas"], "Le frère", "Twelve (12) > ten (10)."),
  Q("« We go to the beach every summer. » Quand vont-ils à la plage ?", ["Chaque été", "Chaque hiver", "Une seule fois", "Tous les week-ends"], "Chaque été", "Every summer = chaque été."),
]),
notion('RL-1', 0, F, 'angrl-mini-textes-2', [
  Q("« The museum opens at 9 a.m. and closes at 5 p.m. » À quelle heure ferme le musée ?", ["17 heures", "9 heures", "15 heures", "21 heures"], "17 heures", "5 p.m. = 17 h."),
  Q("« Tickets cost £5 for children and £10 for adults. » Combien paie un enfant ?", ["5 livres", "10 livres", "15 livres", "Rien"], "5 livres", "£ = livre sterling."),
  Q("« No dogs allowed. » Que signifie ce panneau ?", ["Chiens interdits", "Chiens bienvenus", "Attention au chien", "Promenade des chiens"], "Chiens interdits", "Allowed = autorisé."),
]),
notion('RL-1', 0, F, 'angrl-panneaux', [
  Q("Que signifie le panneau « Exit » ?", ["Sortie", "Entrée", "Fermé", "Danger"], "Sortie", "Entrance = entrée."),
  Q("Que signifie « Mind the gap » dans le métro de Londres ?", ["Attention à l'espace entre le train et le quai", "Gardez votre ticket", "Pensez à l'écart de prix", "Ne courez pas"], "Attention à l'espace entre le train et le quai", "C'est une annonce célèbre."),
  Q("Que signifie « Out of order » sur une machine ?", ["En panne", "En ordre", "Hors de prix", "Vendu"], "En panne", "Order = ordre, commande."),
]),
notion('RL-1', 0, F, 'angrl-mots-questions', [
  Q("Que demande-t-on avec « When » ?", ["Le moment", "Le lieu", "La personne", "La raison"], "Le moment", "When = quand."),
  Q("Que demande-t-on avec « Who » ?", ["La personne", "Le lieu", "Le prix", "La manière"], "La personne", "Who = qui."),
  Q("Que demande-t-on avec « How much » ?", ["Une quantité ou un prix", "Un âge", "Un lieu", "Une heure"], "Une quantité ou un prix", "How much is it? = combien ça coûte ?"),
]),
notion('RL-1', 0, F, 'angrl-mots-transparents', [
  Q("Quel mot anglais est transparent (ressemble au français) ?", ["Important", "Weather", "Knife", "Bridge"], "Important", "Les mots transparents aident à comprendre un texte."),
  Q("Que signifie « restaurant » ?", ["Un restaurant", "Un reste", "Une restauration d'art", "Un repos"], "Un restaurant", "C'est un mot emprunté au français."),
  Q("Quelle stratégie aide à comprendre un texte en anglais ?", ["Repérer les mots connus et transparents", "Traduire chaque mot dans l'ordre", "Lire seulement la fin", "Ignorer le titre"], "Repérer les mots connus et transparents", "On s'appuie aussi sur le titre et les images."),
]),
notion('RL-1', 0, F, 'angrl-chiffres-oral', [
  Q("Quel nombre entend-on dans « fifty » ?", ["50", "15", "5", "500"], "50", "Fifteen = 15."),
  Q("Quel nombre entend-on dans « thirteen » ?", ["13", "30", "3", "33"], "13", "Thirty = 30 : attention à l'accent."),
  Q("Comment lit-on « 0 » dans un numéro de téléphone britannique ?", ["« Oh »", "« Zéro » uniquement en français", "« None »", "« Nothing »"], "« Oh »", "On dit aussi zero."),
]),
notion('RL-1', 0, I, 'angrl-inferences', [
  Q("« Ben was shivering and his teeth were chattering. » Que ressent Ben ?", ["Il a froid", "Il a chaud", "Il est content", "Il a faim"], "Il a froid", "On déduit à partir des indices."),
  Q("« She opened the present and her face lit up. » Comment se sent-elle ?", ["Ravie", "Déçue", "En colère", "Triste"], "Ravie", "Her face lit up = son visage s'illumina."),
  Q("« He slammed the door and didn't say a word. » Comment se sent-il ?", ["En colère", "Joyeux", "Fatigué", "Amoureux"], "En colère", "To slam = claquer."),
]),
notion('RL-1', 0, I, 'angrl-annonces', [
  Q("« Due to bad weather, today's match has been cancelled. » Que s'est-il passé ?", ["Le match est annulé à cause du mauvais temps", "Le match est avancé", "Le match a lieu à l'intérieur", "Le match est gratuit"], "Le match est annulé à cause du mauvais temps", "Due to = en raison de."),
  Q("« Please have your passports ready. » Que doit-on faire ?", ["Préparer son passeport", "Acheter un passeport", "Montrer son billet", "Ranger son passeport"], "Préparer son passeport", "Ready = prêt."),
  Q("« The shop will be closed on Sunday. » Quand le magasin est-il fermé ?", ["Dimanche", "Samedi", "Lundi", "Tous les jours"], "Dimanche", "Will be closed = sera fermé."),
]),
notion('RL-1', 0, I, 'angrl-texte-informatif', [
  Q("« Koalas sleep up to 20 hours a day because their food gives them little energy. » Pourquoi les koalas dorment-ils autant ?", ["Leur nourriture leur donne peu d'énergie", "Ils sont malades", "Ils vivent la nuit", "Ils ont peur"], "Leur nourriture leur donne peu d'énergie", "Because introduit la cause."),
  Q("« Although it was late, they kept working. » Que comprend-on ?", ["Malgré l'heure tardive, ils ont continué à travailler", "Ils sont partis car il était tard", "Ils ont commencé tard", "Ils ont arrêté"], "Malgré l'heure tardive, ils ont continué à travailler", "Although = bien que."),
  Q("« Plastic takes hundreds of years to break down. » Que signifie « break down » ici ?", ["Se décomposer", "Tomber en panne", "Casser", "S'effondrer de tristesse"], "Se décomposer", "Le contexte aide à choisir le sens."),
]),
notion('RL-1', 0, I, 'angrl-recette', [
  Q("« Mix the flour and the eggs, then add the milk. » Que fait-on en premier ?", ["Mélanger la farine et les œufs", "Ajouter le lait", "Cuire", "Manger"], "Mélanger la farine et les œufs", "Then = ensuite."),
  Q("Que signifie « preheat the oven » ?", ["Préchauffer le four", "Éteindre le four", "Nettoyer le four", "Ouvrir le four"], "Préchauffer le four", "Oven = four."),
  Q("Que signifie « a pinch of salt » ?", ["Une pincée de sel", "Un sac de sel", "Un verre de sel", "Du sel en morceaux"], "Une pincée de sel", "Pinch = pincée."),
]),
notion('RL-1', 0, I, 'angrl-meteo-bulletin', [
  Q("« Tomorrow will be cloudy with sunny spells in the afternoon. » Quel temps fera-t-il l'après-midi ?", ["Des éclaircies", "De la pluie", "De la neige", "De l'orage"], "Des éclaircies", "Sunny spells = éclaircies."),
  Q("« Temperatures will drop below zero tonight. » Que va-t-il se passer ?", ["Il va geler cette nuit", "Il va faire chaud", "Il va pleuvoir", "Il va y avoir du vent"], "Il va geler cette nuit", "To drop = baisser."),
  Q("« Heavy showers are expected. » Qu'annonce le bulletin ?", ["De fortes averses", "Une tempête de neige", "Du soleil", "Du brouillard léger"], "De fortes averses", "Shower = averse (ou douche)."),
]),
notion('RL-1', 0, I, 'angrl-message-oral', [
  Q("« Hi Mum, I'll be late, the bus broke down. Don't wait for me for dinner. » Pourquoi la personne sera-t-elle en retard ?", ["Le bus est tombé en panne", "Elle a raté le bus", "Elle dîne chez un ami", "Elle est malade"], "Le bus est tombé en panne", "Broke down = est tombé en panne."),
  Q("Dans le même message, que demande la personne ?", ["De ne pas l'attendre pour dîner", "De venir la chercher", "De préparer le dîner", "D'appeler un taxi"], "De ne pas l'attendre pour dîner", "Don't wait for me."),
  Q("« Can you pick me up at the station at six? » Que demande la personne ?", ["De venir la chercher à la gare à 18 heures", "De lui acheter un billet", "De l'attendre à la maison", "De prendre le train"], "De venir la chercher à la gare à 18 heures", "To pick up = aller chercher."),
]),
notion('RL-1', 0, I, 'angrl-titres-presse', [
  Q("Que signifie le titre « Local school wins national prize » ?", ["Une école locale remporte un prix national", "Une école locale ferme", "Le prix national est local", "L'école perd un prix"], "Une école locale remporte un prix national", "Les titres de presse sont souvent au présent simple."),
  Q("Que signifie « Thousands march for climate » ?", ["Des milliers de personnes manifestent pour le climat", "Le climat change en mars", "Des milliers de mars", "Une marche militaire"], "Des milliers de personnes manifestent pour le climat", "March = défiler."),
  Q("Que signifie « Prices soar » ?", ["Les prix s'envolent", "Les prix baissent", "Les prix sont stables", "Les prix sont annoncés"], "Les prix s'envolent", "To soar = monter en flèche."),
]),
notion('RL-1', 0, D, 'angrl-implicite', [
  Q("« Oh great, another Monday! » dit Tom d'un ton las. Que pense-t-il vraiment ?", ["Il n'aime pas le lundi (ironie)", "Il adore le lundi", "Il a oublié le jour", "Il est en vacances"], "Il n'aime pas le lundi (ironie)", "L'intonation révèle l'ironie."),
  Q("« I'm not saying it's your fault, but… » Que suggère la personne ?", ["Elle pense en fait que c'est un peu la faute de l'autre", "Elle est d'accord", "Elle s'excuse", "Elle ne pense rien"], "Elle pense en fait que c'est un peu la faute de l'autre", "« But » annonce la vraie pensée."),
  Q("« It's a bit chilly in here, isn't it? » Que demande implicitement la personne ?", ["De fermer la fenêtre ou de monter le chauffage", "D'ouvrir la fenêtre", "De sortir", "Un verre d'eau"], "De fermer la fenêtre ou de monter le chauffage", "Une remarque peut être une demande indirecte."),
]),
notion('RL-1', 0, D, 'angrl-texte-litteraire', [
  Q("« The house stood alone at the end of the lane, its windows dark like empty eyes. » Quelle impression crée cette phrase ?", ["Une impression inquiétante", "Une impression joyeuse", "Une impression comique", "Aucune impression"], "Une impression inquiétante", "La comparaison « like empty eyes » crée le malaise."),
  Q("Quelle figure de style est « like empty eyes » ?", ["Une comparaison", "Une métaphore", "Une rime", "Une onomatopée"], "Une comparaison", "Like ou as introduisent une comparaison."),
  Q("Dans un récit, que signifie « Meanwhile » ?", ["Pendant ce temps", "Finalement", "Auparavant", "Soudain"], "Pendant ce temps", "Il signale une action simultanée."),
]),
notion('RL-1', 0, D, 'angrl-registres', [
  Q("Quel registre emploie « Gonna grab a bite, wanna come? » ?", ["Familier", "Soutenu", "Officiel", "Littéraire ancien"], "Familier", "Gonna = going to, wanna = want to."),
  Q("Quel registre emploie « We regret to inform you that your application was unsuccessful » ?", ["Soutenu (formel)", "Familier", "Argotique", "Enfantin"], "Soutenu (formel)", "C'est une lettre de refus officielle."),
  Q("Que signifie « gotta » en anglais familier ?", ["Got to (devoir)", "Gotten", "Go to", "Good to"], "Got to (devoir)", "« I gotta go » = je dois y aller."),
]),
notion('RL-1', 0, D, 'angrl-dialogue-comprehension', [
  Q("« A: Fancy a cup of tea? — B: I wouldn't say no. » Que répond B ?", ["Oui, volontiers", "Non, merci", "Je ne sais pas", "Plus tard"], "Oui, volontiers", "Une double négation polie."),
  Q("« A: How was the film? — B: Not bad at all. » Qu'en pense B ?", ["Il l'a plutôt bien aimé", "Il l'a détesté", "Il ne l'a pas vu", "Il s'est endormi"], "Il l'a plutôt bien aimé", "Les Britanniques aiment l'euphémisme."),
  Q("« A: Shall we go? — B: Hang on a sec. » Que veut B ?", ["Que A attende un instant", "Partir tout de suite", "Rester à la maison", "Raccrocher"], "Que A attende un instant", "Hang on = attends."),
]),
notion('RL-1', 0, D, 'angrl-graphiques', [
  Q("« The number of cyclists has doubled since 2010. » Que comprend-on ?", ["Il y a deux fois plus de cyclistes qu'en 2010", "Il y a moitié moins de cyclistes", "Il y a autant de cyclistes", "Il n'y a plus de cyclistes"], "Il y a deux fois plus de cyclistes qu'en 2010", "To double = doubler."),
  Q("« Sales fell sharply in March. » Que s'est-il passé ?", ["Les ventes ont fortement baissé en mars", "Les ventes ont augmenté", "Les ventes ont été stables", "Les ventes ont commencé"], "Les ventes ont fortement baissé en mars", "Sharply = fortement."),
  Q("Que signifie « a quarter of the students » ?", ["Un quart des élèves", "La moitié des élèves", "Trois quarts des élèves", "Quatre élèves"], "Un quart des élèves", "Half = la moitié."),
]),
notion('RL-1', 0, D, 'angrl-strategies-ecoute', [
  Q("Quelle stratégie aide avant d'écouter un document audio ?", ["Formuler des hypothèses à partir du titre et des images", "Fermer les yeux et tout traduire", "Écouter une seule fois sans préparer", "Ignorer le contexte"], "Formuler des hypothèses à partir du titre et des images", "L'anticipation facilite la compréhension."),
  Q("Que repère-t-on en priorité lors d'une première écoute ?", ["Qui parle, où, quand et de quoi", "Chaque mot", "Uniquement les verbes", "Uniquement l'accent"], "Qui parle, où, quand et de quoi", "On affine lors des écoutes suivantes."),
  Q("Que signifie « gist » dans « listen for gist » ?", ["L'idée générale", "Les détails", "Les chiffres", "La prononciation"], "L'idée générale", "Listen for details = écouter les détails."),
]),
notion('RL-1', 0, D, 'angrl-humour-jeux-mots', [
  Q("Pourquoi cette blague est-elle drôle : « Why was the math book sad? Because it had too many problems. » ?", ["Problems signifie à la fois « exercices » et « soucis »", "Les livres pleurent", "Les maths sont tristes", "Elle n'est pas drôle"], "Problems signifie à la fois « exercices » et « soucis »", "C'est un jeu de mots (pun)."),
  Q("Comment appelle-t-on un jeu de mots en anglais ?", ["A pun", "A joke book", "A rhyme", "A riddle"], "A pun", "Riddle = devinette."),
  Q("Que signifie « knock-knock joke » ?", ["Une blague en dialogue commençant par « Toc toc »", "Une blague sur les portes", "Une devinette sans réponse", "Une histoire triste"], "Une blague en dialogue commençant par « Toc toc »", "« Who's there? »"),
]),
# ══ RL-2 · Expression orale et écrite ══
notion('RL-2', 0, F, 'angrl-se-decrire-ecrit', [
  Q("Comment dit-on « J'habite à Lyon » ?", ["I live in Lyon.", "I live at Lyon.", "I'm living Lyon.", "I habit in Lyon."], "I live in Lyon.", "In + ville."),
  Q("Comment dit-on « J'ai un frère et une sœur » ?", ["I have got a brother and a sister.", "I have a brother and sister one.", "I am a brother and a sister.", "I got brother sister."], "I have got a brother and a sister.", "Have got = avoir (possession)."),
  Q("Comment dit-on « Mon anniversaire est le 3 mars » ?", ["My birthday is on 3rd March.", "My birthday is in 3 March.", "My anniversary is 3 March.", "My birthday at March 3."], "My birthday is on 3rd March.", "Anniversary = anniversaire de mariage, d'un événement."),
]),
notion('RL-2', 0, F, 'angrl-decrire-lieu', [
  Q("Comment dit-on « Il y a un grand parc dans ma ville » ?", ["There is a big park in my town.", "It has a big park in my town.", "There are a big park in my town.", "Is a park big in my town."], "There is a big park in my town.", "There is = il y a."),
  Q("Comment dit-on « Ma maison est petite mais confortable » ?", ["My house is small but comfortable.", "My house is little but comfortably.", "My small house is but comfortable.", "My house small is comfortable."], "My house is small but comfortable.", "But = mais."),
  Q("Que signifie « My bedroom is next to the bathroom » ?", ["Ma chambre est à côté de la salle de bains.", "Ma chambre est dans la salle de bains.", "Ma chambre est loin de la salle de bains.", "Ma salle de bains est grande."], "Ma chambre est à côté de la salle de bains.", "Next to = à côté de."),
]),
notion('RL-2', 0, F, 'angrl-raconter-journee', [
  Q("Comment dit-on « Hier, je suis allé au cinéma » ?", ["Yesterday, I went to the cinema.", "Yesterday, I go to the cinema.", "Yesterday, I have gone cinema.", "Yesterday, I am going to the cinema."], "Yesterday, I went to the cinema.", "Yesterday + prétérit."),
  Q("Comment dit-on « D'abord, … Ensuite, … Enfin, … » ?", ["First, … Then, … Finally, …", "Before, … After, … End, …", "One, … Two, … Three, …", "Start, … Middle, … Stop, …"], "First, … Then, … Finally, …", "Ces mots organisent un récit."),
  Q("Comment dit-on « Le week-end dernier » ?", ["Last weekend", "The weekend last", "Next weekend", "This weekend before"], "Last weekend", "Next weekend = le week-end prochain."),
]),
notion('RL-2', 0, F, 'angrl-gouts-justifier', [
  Q("Comment justifie-t-on une préférence ?", ["I like football because it's exciting.", "I like football so it's exciting.", "I like football but it's exciting.", "I like football if exciting."], "I like football because it's exciting.", "Because = parce que."),
  Q("Comment dit-on « Mon plat préféré, ce sont les pâtes » ?", ["My favourite food is pasta.", "My preferred plate is pasta.", "My favourite dish are pastas.", "I prefer the pasta plate."], "My favourite food is pasta.", "Pasta est indénombrable."),
  Q("Comment dit-on « Je n'aime pas du tout les épinards » ?", ["I don't like spinach at all.", "I like not spinach all.", "I no like spinach.", "I don't like at all spinach."], "I don't like spinach at all.", "At all = du tout."),
]),
notion('RL-2', 0, F, 'angrl-carte-postale', [
  Q("Comment commence-t-on une carte postale à un ami ?", ["Dear Tom,", "To whom it may concern,", "Dear Sir,", "Yours faithfully,"], "Dear Tom,", "Dear = cher."),
  Q("Comment dit-on « Il fait beau et je m'amuse bien » ?", ["The weather is nice and I'm having fun.", "The weather does nice and I amuse well.", "It makes beautiful and I funny.", "The weather is good and I have funny."], "The weather is nice and I'm having fun.", "To have fun = s'amuser."),
  Q("Comment termine-t-on une carte postale amicale ?", ["Love, Emma / See you soon!", "Yours sincerely,", "Best regards, the director", "Kind regards, Sir"], "Love, Emma / See you soon!", "Le registre est familier."),
]),
notion('RL-2', 0, F, 'angrl-decrire-image-simple', [
  Q("Comment dit-on « Sur cette photo, je vois deux enfants » ?", ["In this picture, I can see two children.", "On this photo, I see two childs.", "In this picture, I am seeing two children.", "On this picture I look two children."], "In this picture, I can see two children.", "Child → children."),
  Q("Comment dit-on « Ils ont l'air heureux » ?", ["They look happy.", "They are looking happily.", "They have the air happy.", "They seem happily."], "They look happy.", "Look + adjectif = avoir l'air."),
  Q("Comment dit-on « au milieu de l'image » ?", ["In the middle of the picture", "At the half of the picture", "In the center at picture", "On middle picture"], "In the middle of the picture", "In the centre aussi."),
]),
notion('RL-2', 0, F, 'angrl-projets-futurs', [
  Q("Comment dit-on « L'été prochain, je vais visiter Londres » ?", ["Next summer, I'm going to visit London.", "Last summer, I visit London.", "Next summer, I visited London.", "Next summer, I visit going London."], "Next summer, I'm going to visit London.", "Be going to = projet."),
  Q("Comment dit-on « Plus tard, je voudrais être vétérinaire » ?", ["Later, I'd like to be a vet.", "Later, I like be vet.", "After, I would be vet.", "Later, I want being a vet."], "Later, I'd like to be a vet.", "Vet = vétérinaire."),
  Q("Comment dit-on « J'espère que… » ?", ["I hope that…", "I wait that…", "I wish to that…", "I hope to that…"], "I hope that…", "To hope = espérer."),
]),
notion('RL-2', 0, I, 'angrl-lettre-formelle', [
  Q("Comment termine-t-on une lettre formelle commencée par « Dear Sir or Madam » ?", ["Yours faithfully,", "Love,", "See you,", "Cheers,"], "Yours faithfully,", "Yours sincerely si l'on connaît le nom."),
  Q("Comment commence-t-on une lettre formelle à Mme Smith ?", ["Dear Ms Smith,", "Hi Smith!", "Dear Sir or Madam,", "Hello Mrs!"], "Dear Ms Smith,", "Ms ne précise pas la situation familiale."),
  Q("Quelle phrase introduit poliment une demande dans une lettre formelle ?", ["I would be grateful if you could…", "Give me…", "I want you to…", "Hurry up and…"], "I would be grateful if you could…", "C'est une formule très polie."),
]),
notion('RL-2', 0, I, 'angrl-connecteurs-ecrit', [
  Q("Quel connecteur ajoute une idée ?", ["Moreover", "However", "Therefore", "Although"], "Moreover", "Moreover / furthermore = de plus."),
  Q("Quel connecteur exprime une opposition ?", ["However", "Moreover", "Because", "So"], "However", "However = cependant."),
  Q("Quel connecteur exprime une conséquence ?", ["Therefore", "Although", "Whereas", "Unless"], "Therefore", "Therefore = par conséquent."),
]),
notion('RL-2', 0, I, 'angrl-argumenter', [
  Q("Comment introduit-on un premier argument ?", ["First of all,", "In conclusion,", "On the other hand,", "Last but not least,"], "First of all,", "Last but not least = enfin et surtout."),
  Q("Comment présente-t-on le point de vue opposé ?", ["On the other hand,", "First of all,", "To begin with,", "For example,"], "On the other hand,", "On the one hand… on the other hand…"),
  Q("Comment conclut-on un texte argumentatif ?", ["To sum up,", "First,", "By the way,", "Once upon a time,"], "To sum up,", "In conclusion est aussi possible."),
]),
notion('RL-2', 0, I, 'angrl-exprimer-sentiments', [
  Q("Comment dit-on « Je suis fier de toi » ?", ["I'm proud of you.", "I'm proud on you.", "I'm proud for you.", "I proud you."], "I'm proud of you.", "Proud of = fier de."),
  Q("Comment dit-on « J'ai hâte de te voir » ?", ["I look forward to seeing you.", "I look forward to see you.", "I'm hurry to see you.", "I wait to see you quickly."], "I look forward to seeing you.", "Look forward to + V-ing."),
  Q("Comment dit-on « Je suis désolé d'être en retard » ?", ["I'm sorry for being late.", "I'm sorry to late.", "I'm sad of late.", "Sorry I lated."], "I'm sorry for being late.", "Ou : I'm sorry I'm late."),
]),
notion('RL-2', 0, I, 'angrl-decrire-evolution', [
  Q("Comment dit-on « Ma ville a beaucoup changé » ?", ["My town has changed a lot.", "My town changed a lot since.", "My town is changing much.", "My town has change a lot."], "My town has changed a lot.", "Present perfect : résultat présent."),
  Q("Comment dit-on « Avant, il n'y avait pas de cinéma » ?", ["There used to be no cinema.", "There was not used cinema.", "Before, there isn't cinema.", "There didn't use cinema."], "There used to be no cinema.", "Used to = autrefois."),
  Q("Comment dit-on « de plus en plus de touristes » ?", ["More and more tourists", "Most and most tourists", "Many more more tourists", "Always more tourists of"], "More and more tourists", "Fewer and fewer = de moins en moins."),
]),
notion('RL-2', 0, I, 'angrl-resume', [
  Q("Que doit contenir un bon résumé (summary) ?", ["Les idées principales, sans détails inutiles", "Toutes les phrases du texte", "Uniquement le titre", "L'avis personnel uniquement"], "Les idées principales, sans détails inutiles", "Il est plus court que le texte."),
  Q("Comment commence-t-on souvent un résumé ?", ["This text is about…", "Once upon a time…", "Dear Sir,…", "To whom it may concern…"], "This text is about…", "Ou : The article deals with…"),
  Q("Que signifie « the main idea » ?", ["L'idée principale", "La meilleure idée", "La main", "Le titre"], "L'idée principale", "Main = principal."),
]),
notion('RL-2', 0, I, 'angrl-presentation-orale', [
  Q("Comment commence-t-on une présentation orale ?", ["Today, I'm going to talk about…", "Goodbye everybody…", "In conclusion…", "Thank you for listening…"], "Today, I'm going to talk about…", "On annonce le sujet."),
  Q("Comment termine-t-on poliment une présentation ?", ["Thank you for your attention. Do you have any questions?", "That's it, bye.", "Go away now.", "I'm finished, sit down."], "Thank you for your attention. Do you have any questions?", "On invite aux questions."),
  Q("Comment annonce-t-on une deuxième partie ?", ["Now, let's move on to…", "Firstly…", "Once upon a time…", "To sum up…"], "Now, let's move on to…", "To move on = passer à."),
]),
notion('RL-2', 0, I, 'angrl-recit-temps', [
  Q("Quels temps utilise-t-on principalement pour raconter une histoire au passé ?", ["Le prétérit simple et le prétérit en be + ing", "Le présent et le futur", "L'impératif", "Le conditionnel uniquement"], "Le prétérit simple et le prétérit en be + ing", "Le past perfect marque l'antériorité."),
  Q("Complétez : « While I ___ (walk) home, I ___ (see) a fox. »", ["was walking / saw", "walked / was seeing", "walk / see", "am walking / saw"], "was walking / saw", "Action en cours interrompue."),
  Q("Quel mot marque une action soudaine dans un récit ?", ["Suddenly", "Usually", "Always", "Often"], "Suddenly", "Soudain."),
]),
notion('RL-2', 0, D, 'angrl-essai-argumentatif', [
  Q("Comment présente-t-on un exemple dans un essai ?", ["For instance,", "However,", "Therefore,", "Although,"], "For instance,", "For example est synonyme."),
  Q("Comment nuance-t-on un argument ?", ["It is true that…, but…", "Obviously everybody knows…", "It's 100 % sure that…", "Nobody can deny that…"], "It is true that…, but…", "La concession rend l'argument plus convaincant."),
  Q("Que signifie « to a certain extent » ?", ["Dans une certaine mesure", "Jusqu'à la fin", "Absolument", "Pas du tout"], "Dans une certaine mesure", "Il permet de nuancer."),
]),
notion('RL-2', 0, D, 'angrl-registre-adapter', [
  Q("Quelle formule est adaptée à un e-mail formel ?", ["I am writing to enquire about…", "Hey, what's up?", "Gimme info!", "Yo, tell me about…"], "I am writing to enquire about…", "To enquire = se renseigner."),
  Q("Quelle version est plus formelle que « Can you send me the brochure? » ?", ["Could you possibly send me the brochure?", "Send the brochure!", "Wanna send the brochure?", "Brochure, please, now."], "Could you possibly send me the brochure?", "Could est plus poli que can."),
  Q("Quelle formule convient pour remercier dans une lettre formelle ?", ["Thank you in advance for your help.", "Thanks a mil, mate!", "Cheers!", "Ta!"], "Thank you in advance for your help.", "In advance = d'avance."),
]),
notion('RL-2', 0, D, 'angrl-structures-emphase', [
  Q("Que met en relief « What I love about London is its parks » ?", ["Ce que j'aime à Londres, ce sont ses parcs", "J'aime Londres et ses parcs", "Londres n'a pas de parcs", "Je n'aime que les parcs"], "Ce que j'aime à Londres, ce sont ses parcs", "C'est une phrase clivée."),
  Q("Complétez pour insister : « It was Tom ___ broke the window. »", ["who", "which", "what", "whom"], "who", "It was… who… = C'est… qui…"),
  Q("Que signifie « I do like your dress! » ?", ["J'aime vraiment ta robe !", "Je fais ta robe.", "Je n'aime pas ta robe.", "J'aimerais une robe."], "J'aime vraiment ta robe !", "Do d'insistance."),
]),
notion('RL-2', 0, D, 'angrl-paraphraser', [
  Q("Quelle phrase a le même sens que « It's not worth it » ?", ["It doesn't deserve the effort.", "It costs a lot.", "It's very valuable.", "It's worth a lot."], "It doesn't deserve the effort.", "Not worth = ne vaut pas la peine."),
  Q("Quelle phrase a le même sens que « She's fed up with homework » ?", ["She's tired of homework.", "She loves homework.", "She has finished her homework.", "She eats her homework."], "She's tired of homework.", "Fed up = en avoir assez."),
  Q("Que fait-on quand on ne connaît pas un mot à l'oral ?", ["On le décrit ou on utilise un synonyme", "On s'arrête de parler", "On parle français", "On invente un mot au hasard"], "On le décrit ou on utilise un synonyme", "C'est une stratégie de contournement."),
]),
notion('RL-2', 0, D, 'angrl-critique', [
  Q("Quelle phrase convient pour donner un avis nuancé sur un film ?", ["The plot was gripping, although the ending was disappointing.", "It was good.", "Film nice.", "I like."], "The plot was gripping, although the ending was disappointing.", "Plot = intrigue, gripping = captivant."),
  Q("Que signifie « I'd highly recommend it » ?", ["Je le recommande vivement", "Je ne le recommande pas", "Je le recommande un peu", "Je le déconseille"], "Je le recommande vivement", "Highly = vivement."),
  Q("Que signifie « overrated » ?", ["Surestimé", "Sous-estimé", "Démodé", "Trop cher"], "Surestimé", "Underrated = sous-estimé."),
]),
notion('RL-2', 0, D, 'angrl-hypotheses-oral', [
  Q("Quelle phrase permet de faire une hypothèse sur une image ?", ["It might be a festival.", "It is a festival, that's sure.", "Festival it is.", "It was festival."], "It might be a festival.", "Might = peut-être."),
  Q("Comment dit-on « Il semblerait que… » ?", ["It looks as if…", "It looks of…", "It seems like that…", "It appears to that…"], "It looks as if…", "As if = comme si."),
  Q("Comment dit-on « Je suppose que… » ?", ["I suppose (that)…", "I suppose to…", "I'm supposing of…", "Suppose me that…"], "I suppose (that)…", "I guess est plus familier."),
]),
notion('RL-2', 0, D, 'angrl-ecrire-recit', [
  Q("Qu'est-ce qu'un bon début de récit (hook) ?", ["Une phrase qui capte l'attention du lecteur", "Un résumé de la fin", "Une liste de personnages", "La date du jour"], "Une phrase qui capte l'attention du lecteur", "Hook = hameçon."),
  Q("Quel mot remplace « said » pour exprimer un murmure ?", ["Whispered", "Shouted", "Laughed", "Cried"], "Whispered", "Shouted = cria."),
  Q("Pourquoi varier les verbes de parole dans un récit ?", ["Pour préciser le ton et rendre le texte vivant", "Pour allonger le texte", "Parce que said est interdit", "Pour respecter une règle de grammaire"], "Pour préciser le ton et rendre le texte vivant", "Muttered, exclaimed, sighed…"),
]),
notion('RL-2', 0, D, 'angrl-proposer-solutions', [
  Q("Comment propose-t-on une solution dans un texte ?", ["One possible solution would be to…", "There is no solution.", "Solution: nothing.", "Do it now!"], "One possible solution would be to…", "Le conditionnel adoucit la proposition."),
  Q("Comment dit-on « Il est essentiel que nous agissions » ?", ["It is essential that we act.", "It is essential we acting.", "It's essential to we act.", "Essential is that act we."], "It is essential that we act.", "It is + adjectif + that…"),
  Q("Que signifie « In my view, … » ?", ["À mon avis, …", "Dans ma vue, …", "Je vois que…", "Selon toi, …"], "À mon avis, …", "In my opinion est synonyme."),
]),
notion('RL-2', 0, D, 'angrl-decrire-tendances', [
  Q("Comment dit-on « La plupart des élèves préfèrent… » ?", ["Most students prefer…", "The most of students prefer…", "Most of students prefers…", "The majority students prefer…"], "Most students prefer…", "Most + nom pluriel, sans the."),
  Q("Comment dit-on « Selon cette enquête… » ?", ["According to this survey…", "Following this survey…", "Says this survey…", "In accord to this survey…"], "According to this survey…", "Survey = enquête, sondage."),
  Q("Comment dit-on « Seule une minorité… » ?", ["Only a minority…", "Only minority…", "Just minority of…", "A minor only…"], "Only a minority…", "The majority = la majorité."),
]),
# ══ RL-3 · Interaction orale et écrite, médiation ══
notion('RL-3', 0, F, 'angrl-salutations', [
  Q("Que dit-on en arrivant le matin ?", ["Good morning!", "Good night!", "Goodbye!", "Good evening!"], "Good morning!", "Good night se dit en partant le soir ou au coucher."),
  Q("Comment prend-on congé ?", ["Goodbye! / See you!", "Hello!", "Good morning!", "Welcome!"], "Goodbye! / See you!", "Bye est plus familier."),
  Q("Que répond-on à « Have a nice day! » ?", ["Thanks, you too!", "No, thanks.", "Yes, I have.", "Good morning!"], "Thanks, you too!", "C'est une formule courante."),
]),
notion('RL-3', 0, F, 'angrl-demander-aide', [
  Q("Comment demande-t-on de répéter ?", ["Could you repeat, please?", "Repeat!", "What you say?", "Again you!"], "Could you repeat, please?", "Pardon? convient aussi."),
  Q("Comment demande-t-on comment on dit un mot en anglais ?", ["How do you say … in English?", "What is … English?", "How English …?", "Say me … in English."], "How do you say … in English?", "How do you spell…? = comment s'écrit… ?"),
  Q("Comment demande-t-on de parler plus lentement ?", ["Could you speak more slowly, please?", "Speak slow!", "Less fast you!", "Slowly speak more please you."], "Could you speak more slowly, please?", "Slowly est l'adverbe de slow."),
]),
notion('RL-3', 0, F, 'angrl-magasin', [
  Q("Que dit le vendeur pour proposer son aide ?", ["Can I help you?", "What do you want?", "Go away!", "Pay now!"], "Can I help you?", "On répond : I'm just looking, thanks."),
  Q("Comment dit-on « Je voudrais deux pommes, s'il vous plaît » ?", ["I'd like two apples, please.", "I want two apple please.", "Give two apples.", "Two apples I like please."], "I'd like two apples, please.", "I'd like est plus poli que I want."),
  Q("Comment demande-t-on si l'on peut payer par carte ?", ["Can I pay by card?", "Can I pay with card?", "Card pay can I?", "Do I pay card?"], "Can I pay by card?", "By card, in cash."),
]),
notion('RL-3', 0, F, 'angrl-telephone', [
  Q("Comment répond-on au téléphone en anglais ?", ["Hello?", "Goodbye?", "Yes, me?", "Who you?"], "Hello?", "Puis : Who's speaking?"),
  Q("Comment dit-on « C'est Paul à l'appareil » ?", ["It's Paul speaking.", "I am Paul here.", "This is Paul's phone.", "Paul calls."], "It's Paul speaking.", "Ou : This is Paul."),
  Q("Comment demande-t-on à parler à quelqu'un ?", ["Can I speak to Anna, please?", "I speak Anna?", "Give me Anna.", "Anna is here?"], "Can I speak to Anna, please?", "Hold on, please = ne quittez pas."),
]),
notion('RL-3', 0, F, 'angrl-inviter', [
  Q("Comment invite-t-on un ami au cinéma ?", ["Would you like to come to the cinema?", "Come cinema!", "You like cinema come?", "Do you want cinema?"], "Would you like to come to the cinema?", "Would you like to…? = voudrais-tu… ?"),
  Q("Comment accepte-t-on une invitation ?", ["Yes, I'd love to!", "No way!", "I don't know you.", "Maybe never."], "Yes, I'd love to!", "Avec plaisir !"),
  Q("Comment refuse-t-on poliment une invitation ?", ["I'm sorry, I can't. I have to study.", "No.", "Go away.", "I don't want you."], "I'm sorry, I can't. I have to study.", "On donne une raison."),
]),
notion('RL-3', 0, F, 'angrl-restaurant', [
  Q("Comment demande-t-on l'addition au Royaume-Uni ?", ["Could I have the bill, please?", "Give me the money!", "The ticket, please.", "How much I eat?"], "Could I have the bill, please?", "Aux États-Unis : the check."),
  Q("Que demande le serveur avec « Are you ready to order? » ?", ["Si vous êtes prêts à commander", "Si vous avez fini", "Si vous voulez partir", "Si vous avez réservé"], "Si vous êtes prêts à commander", "To order = commander."),
  Q("Comment dit-on « Je vais prendre le poulet » ?", ["I'll have the chicken.", "I'm taking chicken.", "I go chicken.", "Chicken for I."], "I'll have the chicken.", "I'll have… est la formule courante."),
]),
notion('RL-3', 0, F, 'angrl-s-excuser', [
  Q("Que dit-on quand on bouscule quelqu'un ?", ["Sorry!", "Thank you!", "You're welcome!", "Cheers!"], "Sorry!", "Excuse me pour attirer l'attention."),
  Q("Que répond-on à « Sorry! » ?", ["That's OK. / No problem.", "Yes, you are.", "Thank you.", "Goodbye."], "That's OK. / No problem.", "Don't worry convient aussi."),
  Q("Que signifie « Never mind » ?", ["Ce n'est pas grave", "Jamais", "N'y pense jamais", "Ne m'oublie pas"], "Ce n'est pas grave", "Il clôt une petite gêne."),
]),
notion('RL-3', 0, I, 'angrl-negocier', [
  Q("Comment propose-t-on une activité à un groupe ?", ["Why don't we go to the park?", "We go park!", "Park now!", "You must go park."], "Why don't we go to the park?", "Let's… est aussi possible."),
  Q("Comment fait-on un compromis ?", ["What if we go to the cinema first and then to the park?", "No, my idea only.", "I don't care.", "Whatever."], "What if we go to the cinema first and then to the park?", "What if… = et si…"),
  Q("Comment dit-on « Ça me va » ?", ["That suits me. / That's fine with me.", "It goes me.", "That's me go.", "It's suit."], "That suits me. / That's fine with me.", "To suit = convenir."),
]),
notion('RL-3', 0, I, 'angrl-mediation-resumer', [
  Q("Qu'est-ce que la médiation en langue ?", ["Transmettre ou reformuler un message pour quelqu'un qui ne le comprend pas", "Traduire mot à mot", "Se disputer", "Écrire un roman"], "Transmettre ou reformuler un message pour quelqu'un qui ne le comprend pas", "Par exemple, expliquer une affiche à un camarade."),
  Q("Un touriste anglophone ne comprend pas un panneau « Fermé le lundi ». Que lui dites-on ?", ["It's closed on Mondays.", "It's open on Mondays.", "It's closed today only.", "It's a museum."], "It's closed on Mondays.", "On reformule l'essentiel."),
  Q("Comment rapporte-t-on ce que dit une autre personne ?", ["She says that…", "She say that…", "She tells that…", "She is saying me that…"], "She says that…", "Discours indirect au présent."),
]),
notion('RL-3', 0, I, 'angrl-demander-chemin', [
  Q("Que répond-on à « Is it far? » quand c'est proche ?", ["No, it's just around the corner.", "Yes, it's next door.", "No, it's miles away.", "It's far near."], "No, it's just around the corner.", "Around the corner = tout près."),
  Q("Comment dit-on « Prenez la deuxième rue à droite » ?", ["Take the second street on the right.", "Take the two street right.", "Second right street take.", "Go second right on street."], "Take the second street on the right.", "On the left = à gauche."),
  Q("Comment dit-on « au carrefour » ?", ["At the crossroads", "In the cross", "On the road cross", "At the traffic"], "At the crossroads", "Traffic lights = feux."),
]),
notion('RL-3', 0, I, 'angrl-entretien-questions', [
  Q("Quelle question pose-t-on pour connaître les loisirs de quelqu'un ?", ["What do you do in your free time?", "What are you doing free?", "Do you have time free?", "What time is free?"], "What do you do in your free time?", "Free time = temps libre."),
  Q("Quelle question pose-t-on pour savoir depuis quand quelqu'un vit quelque part ?", ["How long have you lived here?", "How long do you live here?", "Since when you live here?", "When live you here?"], "How long have you lived here?", "Present perfect avec how long."),
  Q("Comment relance-t-on la conversation ?", ["Really? Tell me more!", "OK, stop.", "Boring.", "Whatever."], "Really? Tell me more!", "On montre son intérêt."),
]),
notion('RL-3', 0, I, 'angrl-reagir', [
  Q("Comment réagit-on à une bonne nouvelle ?", ["That's great news! / Congratulations!", "Oh no!", "What a pity!", "I'm sorry."], "That's great news! / Congratulations!", "Well done! = bravo !"),
  Q("Comment réagit-on à une mauvaise nouvelle ?", ["I'm sorry to hear that.", "Great!", "Lucky you!", "Congratulations!"], "I'm sorry to hear that.", "On montre de l'empathie."),
  Q("Comment exprime-t-on la surprise ?", ["Really? / No way!", "Of course.", "I knew it.", "Obviously."], "Really? / No way!", "No way! = Pas possible !"),
]),
notion('RL-3', 0, I, 'angrl-permission', [
  Q("Comment demande-t-on poliment la permission d'ouvrir la fenêtre ?", ["Do you mind if I open the window?", "I open window.", "Window open, OK?", "Must I open the window?"], "Do you mind if I open the window?", "On répond : No, go ahead."),
  Q("Que répond-on à « Do you mind if I sit here? » pour accepter ?", ["No, not at all.", "Yes, I do.", "Yes, please mind.", "Never."], "No, not at all.", "Mind = être dérangé : non, ça ne me dérange pas."),
  Q("Comment demande-t-on la permission de manière très polie ?", ["May I borrow your pen?", "Pen, give.", "I take your pen.", "Your pen I want."], "May I borrow your pen?", "May est plus formel que can."),
]),
notion('RL-3', 0, I, 'angrl-mediation-tableau', [
  Q("Un camarade anglophone demande « What does \"cantine\" mean? ». Que lui répond-on ?", ["It's the school canteen, where we have lunch.", "It's a bottle.", "It's a classroom.", "It's a teacher."], "It's the school canteen, where we have lunch.", "On explique avec des mots simples."),
  Q("Comment explique-t-on un mot qu'on ne sait pas traduire ?", ["It's a kind of… / It's something you use to…", "I don't know, sorry, bye.", "It's French, impossible.", "Nothing."], "It's a kind of… / It's something you use to…", "C'est une stratégie de médiation."),
  Q("Comment présente-t-on un document à quelqu'un ?", ["This document shows…", "This document are…", "The document he show…", "Look document."], "This document shows…", "Ou : This is a poster about…"),
]),
notion('RL-3', 0, I, 'angrl-conseiller', [
  Q("Comment donne-t-on un conseil à un ami ?", ["You should go to bed earlier.", "You go bed early!", "Bed now!", "You must not sleep."], "You should go to bed earlier.", "Should = conseil."),
  Q("Comment dit-on « Si j'étais toi, … » ?", ["If I were you, …", "If I was you are, …", "If I am you, …", "When I be you, …"], "If I were you, …", "Formule classique du conseil."),
  Q("Comment demande-t-on un conseil ?", ["What do you think I should do?", "What I do?", "Tell me do.", "Should what I?"], "What do you think I should do?", "Any advice? est plus familier."),
]),
notion('RL-3', 0, D, 'angrl-debat', [
  Q("Comment interrompt-on poliment dans un débat ?", ["Sorry to interrupt, but…", "Shut up!", "Stop talking!", "Me now!"], "Sorry to interrupt, but…", "Can I just say something? convient aussi."),
  Q("Comment reconnaît-on un argument adverse tout en gardant sa position ?", ["I see your point, but…", "You're wrong.", "That's stupid.", "No comment."], "I see your point, but…", "C'est une concession."),
  Q("Que signifie « I beg to differ » ?", ["Je me permets de ne pas être d'accord", "Je supplie", "Je suis d'accord", "Je demande la différence"], "Je me permets de ne pas être d'accord", "C'est très poli, voire soutenu."),
]),
notion('RL-3', 0, D, 'angrl-mediation-interpreter', [
  Q("Un touriste dit « Is this the right platform for Bordeaux? » à votre grand-père. Que lui traduisez-vous ?", ["Il demande si c'est le bon quai pour Bordeaux.", "Il veut un billet pour Bordeaux.", "Il dit que le train est en retard.", "Il cherche les toilettes."], "Il demande si c'est le bon quai pour Bordeaux.", "Platform = quai."),
  Q("Que fait un médiateur quand un détail culturel n'existe pas dans l'autre langue ?", ["Il l'explique au lieu de le traduire mot à mot", "Il l'ignore", "Il invente un mot", "Il arrête la conversation"], "Il l'explique au lieu de le traduire mot à mot", "Par exemple, « le brevet » = a national exam at 15."),
  Q("Comment résume-t-on une conversation pour un tiers ?", ["Basically, they agreed to meet on Friday.", "They said many things.", "I don't remember.", "Blah blah blah."], "Basically, they agreed to meet on Friday.", "Basically = en gros."),
]),
notion('RL-3', 0, D, 'angrl-politesse-indirecte', [
  Q("Quelle formule est la plus polie pour demander de l'aide ?", ["I was wondering if you could help me.", "Help me.", "Can you help?", "You help me now."], "I was wondering if you could help me.", "Le passé et le conditionnel adoucissent."),
  Q("Que signifie « Would you mind closing the door? » ?", ["Pourriez-vous fermer la porte ?", "Ça vous dérange que je ferme la porte ?", "Vous avez fermé la porte ?", "Fermez la porte !"], "Pourriez-vous fermer la porte ?", "Would you mind + V-ing."),
  Q("Pourquoi les Britanniques utilisent-ils souvent des formulations indirectes ?", ["Par politesse, pour ne pas paraître autoritaires", "Parce qu'ils ne savent pas parler", "Par obligation légale", "Pour gagner du temps"], "Par politesse, pour ne pas paraître autoritaires", "« I'm afraid… » adoucit une mauvaise nouvelle."),
]),
notion('RL-3', 0, D, 'angrl-email-pro', [
  Q("Comment répond-on à un e-mail en remerciant pour une réponse rapide ?", ["Thank you for your prompt reply.", "Thanks for fast.", "Good answer quick.", "You reply fast, thanks you."], "Thank you for your prompt reply.", "Prompt = rapide."),
  Q("Que signifie « Please find attached… » ?", ["Veuillez trouver ci-joint…", "Trouvez-moi…", "Attachez-vous…", "Veuillez chercher…"], "Veuillez trouver ci-joint…", "Attachment = pièce jointe."),
  Q("Que signifie « I look forward to hearing from you » ?", ["Dans l'attente de votre réponse", "J'espère vous entendre chanter", "Je vous écoute", "Je vous regarde"], "Dans l'attente de votre réponse", "Formule de fin courante."),
]),
notion('RL-3', 0, D, 'angrl-tags-reactions', [
  Q("Complétez : « It's a lovely day, ___? »", ["isn't it", "is it", "doesn't it", "aren't they"], "isn't it", "Question tag pour chercher l'accord."),
  Q("Que répond-on à « I'm hungry. » pour dire « moi aussi » ?", ["So am I.", "So do I.", "Me neither.", "Neither am I."], "So am I.", "So + auxiliaire + sujet."),
  Q("Que répond-on à « I don't like spiders. » pour dire « moi non plus » ?", ["Neither do I.", "So do I.", "Me too.", "Neither don't I."], "Neither do I.", "Ou : Me neither."),
]),
notion('RL-3', 0, D, 'angrl-plaintes', [
  Q("Comment se plaint-on poliment à l'hôtel ?", ["I'm afraid there's a problem with my room.", "Your room is rubbish!", "I want my money now!", "This is terrible, you idiot!"], "I'm afraid there's a problem with my room.", "I'm afraid = je crains que."),
  Q("Que signifie « I'd like a refund » ?", ["Je voudrais être remboursé", "Je voudrais un autre article", "Je voudrais une réduction", "Je voudrais une facture"], "Je voudrais être remboursé", "Refund = remboursement."),
  Q("Que signifie « I'd like to speak to the manager » ?", ["Je voudrais parler au responsable", "Je voudrais un manager de football", "Je voudrais un serveur", "Je voudrais partir"], "Je voudrais parler au responsable", "Manager = directeur, responsable."),
]),
notion('RL-3', 0, D, 'angrl-mediation-culturelle', [
  Q("Comment expliquer « le baccalauréat » à un ami américain ?", ["It's the final exam at the end of high school.", "It's a type of cheese.", "It's a university degree.", "It's a French holiday."], "It's the final exam at the end of high school.", "On cherche l'équivalent le plus proche."),
  Q("Quel équivalent britannique approximatif correspond au « collège » français ?", ["Secondary school (Years 7 to 10)", "College", "University", "Primary school"], "Secondary school (Years 7 to 10)", "Faux ami : college = études supérieures."),
  Q("Comment expliquer « la galette des rois » à un ami anglais ?", ["It's a cake we eat in January with a small figurine hidden inside.", "It's a king's hat.", "It's a Christmas tree.", "It's a French pancake."], "It's a cake we eat in January with a small figurine hidden inside.", "On décrit l'objet et la tradition."),
]),
notion('RL-3', 0, D, 'angrl-entretien-embauche-oral', [
  Q("Que répond-on à « Tell me about yourself » lors d'un entretien ?", ["Une courte présentation de son parcours et de ses qualités", "Son adresse complète", "Son plat préféré uniquement", "Rien"], "Une courte présentation de son parcours et de ses qualités", "C'est la question d'ouverture classique."),
  Q("Que signifie « What are your strengths? » ?", ["Quelles sont vos qualités (points forts) ?", "Êtes-vous fort physiquement ?", "Quel est votre salaire ?", "Où habitez-vous ?"], "Quelles sont vos qualités (points forts) ?", "Weaknesses = points faibles."),
  Q("Comment dit-on « Je suis motivé et j'aime travailler en équipe » ?", ["I'm motivated and I enjoy working in a team.", "I'm motivating and I like team work me.", "I motivate and team I like.", "I'm motived and enjoy team."], "I'm motivated and I enjoy working in a team.", "Enjoy + V-ing."),
]),
notion('RL-3', 0, D, 'angrl-forum-reseaux', [
  Q("Comment répond-on poliment à un avis contraire sur un forum ?", ["Thanks for sharing, but I see things differently.", "You're an idiot.", "Delete your post!", "LOL no."], "Thanks for sharing, but I see things differently.", "La « netiquette » invite au respect."),
  Q("Que signifie « IMO » dans un message ?", ["In my opinion", "I'm missing out", "Important message only", "I miss you"], "In my opinion", "IMHO = in my humble opinion."),
  Q("Que signifie « to troll » sur Internet ?", ["Provoquer volontairement les autres", "Chercher une information", "Publier une photo", "Faire un don"], "Provoquer volontairement les autres", "Don't feed the troll!"),
]),
]

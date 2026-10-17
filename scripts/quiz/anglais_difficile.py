from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('L-2', 1, D, 'ang-perfect-vs-preterit', [
  Q("Choisissez la phrase correcte.", ["I've lost my keys, so I can't get in.", "I lose my keys yesterday, so I can't get in.", "I've lost my keys last night.", "I have lose my keys."], "I've lost my keys, so I can't get in.", "Le present perfect souligne la conséquence présente ; on ne l'emploie pas avec un moment passé précis (last night)."),
  Q("Complétez : « How long ___ English? » (depuis combien de temps apprends-tu l'anglais ?)", ["do you learn", "have you been learning", "are you learning", "did you learn"], "have you been learning", "Present perfect en be + -ing pour une activité commencée dans le passé et toujours en cours."),
  Q("Complétez : « When ___ the Eiffel Tower? »", ["have you visited", "did you visit", "have you visit", "do you visited"], "did you visit", "When appelle un moment précis : prétérit."),
]),
notion('L-2', 1, D, 'ang-conditionnel-2', [
  Q("Complétez : « If I ___ rich, I would travel around the world. »", ["am", "were", "will be", "would be"], "were", "Hypothèse irréelle dans le présent : if + prétérit (were pour toutes les personnes en anglais soutenu), would + base verbale."),
  Q("Complétez : « If she had studied, she ___ the exam. »", ["would pass", "would have passed", "will pass", "passed"], "would have passed", "Hypothèse irréelle dans le passé : if + past perfect, would have + participe passé."),
  Q("Que signifie « I wish I knew the answer » ?", ["Je connais la réponse", "J'aimerais connaître la réponse (mais je ne la connais pas)", "J'ai connu la réponse", "Je connaîtrai la réponse"], "J'aimerais connaître la réponse (mais je ne la connais pas)", "I wish + prétérit exprime un regret sur le présent."),
]),
notion('L-2', 1, D, 'ang-discours-indirect', [
  Q("Mettez au discours indirect : He said, « I am tired. »", ["He said he is tired.", "He said he was tired.", "He said I was tired.", "He said that I am tired."], "He said he was tired.", "Après un verbe introducteur au passé, on recule d'un temps (am → was) et on adapte les pronoms."),
  Q("Mettez au discours indirect : She asked, « Where do you live? »", ["She asked where did I live.", "She asked where I lived.", "She asked where do I live.", "She asked me where I live?"], "She asked where I lived.", "Dans une question indirecte, on reprend l'ordre sujet + verbe, sans auxiliaire do."),
  Q("Au discours indirect, que devient « tomorrow » quand on rapporte des propos passés ?", ["tomorrow", "the next day (the following day)", "yesterday", "today"], "the next day (the following day)", "Les repères temporels sont transposés : yesterday → the day before."),
]),
notion('L-2', 1, D, 'ang-past-perfect', [
  Q("Complétez : « When we arrived, the film ___. »", ["already started", "had already started", "has already started", "already starts"], "had already started", "Le past perfect marque l'antériorité par rapport à un moment passé."),
  C("Cliquez sur le participe passé de la forme au past perfect.", "She was tired because she had [worked] all night.", "Had worked : had + participe passé."),
  Q("Quelle phrase indique qu'une action s'est produite avant une autre dans le passé ?", ["I ate when he arrived.", "I had eaten before he arrived.", "I eat before he arrives.", "I was eating when he arrives."], "I had eaten before he arrived.", "Had eaten est antérieur à arrived."),
]),
notion('L-2', 1, D, 'ang-modaux-deduction', [
  Q("Complétez : « He's been working all day. He ___ be exhausted. » (déduction quasi certaine)", ["can't", "must", "should", "mustn't"], "must", "Must exprime ici une forte probabilité."),
  Q("Complétez : « That ___ be John, he's in New York this week. » (impossibilité)", ["must", "can't", "may", "should"], "can't", "Can't exprime une déduction négative : c'est impossible."),
  Q("Complétez : « Take an umbrella, it ___ rain later. » (possibilité)", ["must", "might", "can't", "has to"], "might", "Might et may expriment une possibilité."),
]),
notion('L-2', 1, D, 'ang-causatif', [
  Q("Que signifie « I had my hair cut » ?", ["Je me suis coupé les cheveux moi-même", "Je me suis fait couper les cheveux", "J'avais les cheveux courts", "J'ai coupé les cheveux de quelqu'un"], "Je me suis fait couper les cheveux", "Have + objet + participe passé : faire faire quelque chose par quelqu'un."),
  Q("Complétez : « My teacher made me ___ the exercise again. »", ["to do", "do", "doing", "done"], "do", "Make + personne + base verbale (sans to)."),
  Q("Complétez : « My parents let me ___ out late. »", ["to go", "go", "going", "went"], "go", "Let + personne + base verbale : permettre."),
]),
notion('L-1', 1, D, 'ang-expressions-idiomatiques', [
  Q("Que signifie « It's raining cats and dogs » ?", ["Il pleut des animaux", "Il pleut des cordes", "Il fait beau", "Il y a de l'orage sans pluie"], "Il pleut des cordes", "Une expression idiomatique ne se traduit pas mot à mot."),
  Q("Que signifie « a piece of cake » ?", ["Un gâteau", "Quelque chose de très facile", "Un dessert difficile", "Une petite part"], "Quelque chose de très facile", "C'est l'équivalent de « du gâteau » ou « un jeu d'enfant »."),
  Q("Que signifie « to break the ice » ?", ["Casser de la glace", "Détendre l'atmosphère lors d'une première rencontre", "Faire du patin", "Se fâcher"], "Détendre l'atmosphère lors d'une première rencontre", "Les icebreakers sont des activités pour briser la glace."),
]),
notion('L-1', 1, D, 'ang-mots-proches', [
  Q("Quelle phrase utilise correctement « make » et « do » ?", ["I made my homework and did a cake.", "I did my homework and made a cake.", "I made my homework and made a cake.", "I did my homework and did a cake."], "I did my homework and made a cake.", "Do homework, do the dishes ; make a cake, make a mistake, make noise."),
  Q("Quelle phrase utilise correctement « say » et « tell » ?", ["He told me that he was ill.", "He said me that he was ill.", "He told that he was ill to me.", "He said to me he told ill."], "He told me that he was ill.", "Tell + personne ; say (to + personne)."),
  Q("Quelle phrase est correcte ?", ["I'm boring by this film.", "I'm bored by this film.", "This film is bored.", "I'm boring this film."], "I'm bored by this film.", "-ed décrit ce qu'on ressent ; -ing décrit ce qui provoque le sentiment (a boring film)."),
]),
notion('L-3', 0, D, 'ang-commonwealth', [
  Q("Qu'est-ce que le Commonwealth of Nations ?", ["Un pays", "Une organisation réunissant le Royaume-Uni et la plupart de ses anciennes colonies", "Une banque", "Une équipe sportive"], "Une organisation réunissant le Royaume-Uni et la plupart de ses anciennes colonies", "Il compte 56 États membres."),
  Q("En quelle année l'Inde obtient-elle son indépendance du Royaume-Uni ?", ["1919", "1947", "1960", "1989"], "1947", "Gandhi est une figure majeure de ce mouvement non violent."),
  Q("Quel pays anglophone d'Afrique est marqué par l'apartheid jusqu'au début des années 1990 ?", ["Le Kenya", "L'Afrique du Sud", "Le Nigeria", "Le Ghana"], "L'Afrique du Sud", "Nelson Mandela devient président en 1994."),
]),
notion('L-3', 0, D, 'ang-brexit-actualite', [
  Q("En quelle année le Royaume-Uni a-t-il voté par référendum pour quitter l'Union européenne ?", ["2010", "2016", "2020", "2022"], "2016", "La sortie effective (Brexit) a eu lieu le 31 janvier 2020."),
  Q("Quel roi a succédé à Elizabeth II en 2022 ?", ["William", "Charles III", "George VII", "Harry"], "Charles III", "Il est couronné le 6 mai 2023."),
  Q("Quel pays anglophone a été le premier à accorder le droit de vote aux femmes au niveau national, en 1893 ?", ["Les États-Unis", "La Nouvelle-Zélande", "Le Royaume-Uni", "Le Canada"], "La Nouvelle-Zélande", "Le Royaume-Uni l'accorde partiellement en 1918, pleinement en 1928."),
]),
notion('L-3', 1, D, 'ang-systeme-scolaire-comparer', [
  Q("Quel examen passent généralement les élèves britanniques vers 16 ans ?", ["Le GCSE", "Le SAT", "Le baccalauréat", "Le A-level"], "Le GCSE", "Les A-levels se passent vers 18 ans."),
  Q("Quel examen standardisé est souvent utilisé pour l'admission à l'université aux États-Unis ?", ["Le GCSE", "Le SAT", "Le brevet", "Le A-level"], "Le SAT", "Le SAT (ou l'ACT) évalue lecture, écriture et mathématiques."),
  Q("Que sont les « public schools » au Royaume-Uni ?", ["Des écoles publiques gratuites", "D'anciennes écoles privées payantes et prestigieuses, comme Eton", "Des écoles primaires", "Des universités"], "D'anciennes écoles privées payantes et prestigieuses, comme Eton", "C'est un faux ami culturel ; les écoles publiques gratuites sont des state schools."),
]),
notion('L-1', 0, D, 'ang-comprehension-nuance', [
  Q("« Hardly anyone came to the party. » Que comprend-on ?", ["Beaucoup de gens sont venus", "Presque personne n'est venu", "Tout le monde est venu", "La fête a été annulée"], "Presque personne n'est venu", "Hardly = à peine, presque pas."),
  Q("« I'd rather stay home tonight. » Que veut dire la personne ?", ["Elle doit rester à la maison", "Elle préférerait rester à la maison", "Elle est restée à la maison", "Elle déteste sa maison"], "Elle préférerait rester à la maison", "I'd rather = je préférerais."),
  Q("« He used to play the violin. » Que comprend-on ?", ["Il joue du violon actuellement", "Il jouait du violon autrefois (mais plus maintenant)", "Il va jouer du violon", "Il est habitué à jouer du violon"], "Il jouait du violon autrefois (mais plus maintenant)", "Used to + base verbale exprime une habitude passée révolue ; be used to + -ing = être habitué à."),
  Q("« You'd better hurry. » Que signifie cette phrase ?", ["Tu ferais mieux de te dépêcher", "Tu t'es dépêché", "Tu es meilleur quand tu te dépêches", "Tu n'as pas besoin de te dépêcher"], "Tu ferais mieux de te dépêcher", "Had better + base verbale = conseil appuyé, voire mise en garde."),
]),
notion('L-1', 1, D, 'ang-prononciation-avancee', [
  Q("Comment se prononce la terminaison -ed de « wanted » ?", ["/t/", "/d/", "/ɪd/", "Elle est muette"], "/ɪd/", "-ed se prononce /ɪd/ après t ou d, /t/ après une consonne sourde (walked), /d/ sinon (played)."),
  Q("Sur quelle syllabe porte l'accent de « photographer » ?", ["pho", "to", "gra", "pher"], "to", "PHOtograph mais phoTOgrapher : l'accent se déplace."),
  Q("Lequel de ces mots contient le son « th » sonore /ð/ ?", ["think", "this", "three", "thanks"], "this", "Think, three, thanks ont le th sourd /θ/."),
]),
notion('L-1', 1, D, 'ang-derivation', [
  Q("Quel suffixe permet de former un nom à partir de « happy » ?", ["-ful", "-ness", "-ly", "-less"], "-ness", "Happy → happiness."),
  Q("Que signifie « careless » ?", ["prudent", "négligent, insouciant", "soigneux", "inquiet"], "négligent, insouciant", "-less exprime le manque : careless = sans soin ; careful = soigneux."),
  Q("Quel préfixe donne le contraire de « possible » ?", ["un-", "im-", "dis-", "in-"], "im-", "Impossible ; unhappy, dislike, incorrect suivent d'autres préfixes."),
]),
notion('L-3', 1, D, 'ang-codes-culturels', [
  Q("Au Royaume-Uni, de quel côté de la route roule-t-on ?", ["À droite", "À gauche", "Au milieu", "Cela dépend des villes"], "À gauche", "C'est aussi le cas en Irlande, en Australie, en Inde ou en Afrique du Sud."),
  Q("Aux États-Unis, quel pourboire est généralement attendu au restaurant ?", ["Aucun", "Environ 15 à 20 % de l'addition", "1 dollar fixe", "50 % de l'addition"], "Environ 15 à 20 % de l'addition", "Le pourboire constitue une part importante de la rémunération des serveurs."),
  Q("Que désigne « afternoon tea » dans la tradition britannique ?", ["Un petit-déjeuner", "Une collation de l'après-midi avec thé, sandwichs et pâtisseries", "Un dîner", "Une pause café au bureau"], "Une collation de l'après-midi avec thé, sandwichs et pâtisseries", "La tradition est attribuée à la duchesse de Bedford au XIXe siècle."),
]),
notion('L-2', 1, D, 'ang-erreurs-francophones', [
  Q("Quelle phrase est correcte ?", ["I am agree with you.", "I agree with you.", "I am agreeing you.", "I'm agree to you."], "I agree with you.", "Agree est un verbe : pas de be devant."),
  Q("Quelle phrase est correcte ?", ["It depends of the weather.", "It depends on the weather.", "It depends from the weather.", "It depend the weather."], "It depends on the weather.", "Depend on (et non of)."),
  Q("Quelle phrase est correcte ?", ["Explain me the rule, please.", "Explain the rule to me, please.", "Explain to me the rule please me.", "Explain me to the rule, please."], "Explain the rule to me, please.", "Explain se construit avec to devant la personne : explain something to someone."),
  Q("Quelle phrase est correcte ?", ["I'm living here since five years.", "I've been living here for five years.", "I live here since five years.", "I'm here for five years ago."], "I've been living here for five years.", "Calque fréquent du français « j'habite ici depuis cinq ans »."),
]),
]

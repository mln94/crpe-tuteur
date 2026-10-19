# Anglais · Phonologie, lexique et outils linguistiques (grammaire de la 5e à la 3e) : 25 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ RL-4 · Phonologie et prosodie ══
notion('RL-4', 0, F, 'angph-lettres-muettes-2', [
  Q("Quelle lettre est muette dans « write » ?", ["Le w", "Le r", "Le t", "Le i"], "Le w", "Comme dans wrong, wrist."),
  Q("Quelle lettre est muette dans « lamb » ?", ["Le b", "Le l", "Le m", "Le a"], "Le b", "Comme dans climb, thumb."),
  Q("Quelle lettre est muette dans « island » ?", ["Le s", "Le i", "Le l", "Le d"], "Le s", "Isle se prononce aussi sans s."),
]),
notion('RL-4', 0, F, 'angph-homophones', [
  Q("Quel mot se prononce comme « two » ?", ["Too", "Tow", "Toe", "Twin"], "Too", "To, too et two sont homophones."),
  Q("Quel mot se prononce comme « right » ?", ["Write", "Rate", "Red", "Ride"], "Write", "Right, write et rite sont homophones."),
  Q("Quel mot se prononce comme « their » ?", ["There", "Three", "Tear", "Then"], "There", "They're aussi."),
]),
notion('RL-4', 0, F, 'angph-alphabet', [
  Q("Comment se prononce la lettre « E » en anglais ?", ["Comme « i »", "Comme « e »", "Comme « a »", "Comme « eu »"], "Comme « i »", "Les lettres E et I sont souvent confondues."),
  Q("Comment se prononce la lettre « I » en anglais ?", ["Comme « aï »", "Comme « i »", "Comme « é »", "Comme « eu »"], "Comme « aï »", "Comme le pronom I."),
  Q("Comment se prononce la lettre « H » en anglais ?", ["« eïtch »", "« ache »", "« hé »", "« hi »"], "« eïtch »", "On épelle souvent son nom en anglais."),
]),
notion('RL-4', 0, F, 'angph-son-th', [
  Q("Comment place-t-on la langue pour prononcer le son « th » ?", ["Entre les dents", "Collée au palais", "Derrière les dents du bas", "Hors de la bouche entièrement"], "Entre les dents", "Il n'existe pas en français."),
  Q("Lequel de ces mots commence par le son « th » sourd /θ/ ?", ["Think", "This", "That", "They"], "Think", "This, that, they ont le th sonore /ð/."),
  Q("Quel mot ne contient pas le son « th » ?", ["Tree", "Three", "Thanks", "Mother"], "Tree", "Attention à ne pas confondre tree et three."),
]),
notion('RL-4', 0, F, 'angph-h-aspire', [
  Q("Le « h » se prononce-t-il dans « house » ?", ["Oui, il est aspiré", "Non, jamais", "Seulement aux États-Unis", "Seulement à l'écrit"], "Oui, il est aspiré", "On souffle légèrement."),
  Q("Dans quel mot le « h » ne se prononce-t-il pas ?", ["Honest", "Happy", "Hello", "Horse"], "Honest", "Comme hour et heir."),
  Q("Pourquoi faut-il bien prononcer le h dans « hat » ?", ["Sinon on entend « at »", "Il est muet", "Pour faire anglais", "Ce n'est pas utile"], "Sinon on entend « at »", "Le h distingue des mots."),
]),
notion('RL-4', 0, F, 'angph-voyelles-longues', [
  Q("Quel mot contient un « i » long ?", ["Sheep", "Ship", "Sit", "Bit"], "Sheep", "Sheep (mouton) ≠ ship (bateau)."),
  Q("Quelle paire de mots oppose une voyelle courte et une voyelle longue ?", ["Live / leave", "Cat / hat", "Dog / log", "Pen / ten"], "Live / leave", "Il faut bien les distinguer."),
  Q("Quel mot contient un « ou » long ?", ["Food", "Foot", "Good", "Book"], "Food", "Foot, good, book ont un « ou » court."),
]),
notion('RL-4', 0, F, 'angph-ed-simple', [
  Q("Comment se prononce la terminaison -ed de « played » ?", ["/d/", "/ɪd/", "/t/", "Elle est muette"], "/d/", "Après un son sonore."),
  Q("Comment se prononce la terminaison -ed de « walked » ?", ["/t/", "/d/", "/ɪd/", "Elle est muette"], "/t/", "Après un son sourd comme /k/."),
  Q("Dans quel mot la terminaison -ed se prononce /ɪd/ ?", ["Needed", "Played", "Jumped", "Cleaned"], "Needed", "Après t ou d."),
]),
notion('RL-4', 0, I, 'angph-accent-mots', [
  Q("Sur quelle syllabe porte l'accent de « hotel » ?", ["Sur la deuxième (ho-TEL)", "Sur la première (HO-tel)", "Sur les deux", "Il n'y a pas d'accent"], "Sur la deuxième (ho-TEL)", "Attention aux mots transparents."),
  Q("Sur quelle syllabe porte l'accent de « banana » ?", ["La deuxième (ba-NA-na)", "La première", "La troisième", "Aucune"], "La deuxième (ba-NA-na)", "Les syllabes non accentuées sont réduites."),
  Q("Pourquoi l'accent de mot est-il important en anglais ?", ["Un mauvais accent peut rendre le mot incompréhensible", "Il n'a aucune importance", "Il change l'orthographe", "Il n'existe qu'en poésie"], "Un mauvais accent peut rendre le mot incompréhensible", "On le note par une apostrophe haute dans les dictionnaires."),
]),
notion('RL-4', 0, I, 'angph-accent-nom-verbe', [
  Q("Où est l'accent de « record » quand c'est un nom (un disque) ?", ["Sur la première syllabe (REcord)", "Sur la deuxième (reCORD)", "Sur les deux", "Aucun"], "Sur la première syllabe (REcord)", "Verbe : to reCORD."),
  Q("Où est l'accent de « present » quand c'est un verbe (présenter) ?", ["Sur la deuxième syllabe (preSENT)", "Sur la première (PREsent)", "Sur les deux", "Aucun"], "Sur la deuxième syllabe (preSENT)", "Nom : a PREsent (un cadeau)."),
  Q("Quelle règle concerne beaucoup de mots de deux syllabes ?", ["Nom accentué au début, verbe accentué à la fin", "Toujours accentués à la fin", "Toujours accentués au début", "Pas d'accent"], "Nom accentué au début, verbe accentué à la fin", "Export, import, increase…"),
]),
notion('RL-4', 0, I, 'angph-formes-faibles', [
  Q("Comment se prononce souvent « can » dans « I can swim » ?", ["De façon réduite /kən/", "Toujours /kæn/ accentué", "Il est muet", "Comme « cane »"], "De façon réduite /kən/", "C'est une forme faible."),
  Q("Comment se prononce « to » dans « I want to go » ?", ["De façon réduite /tə/", "Comme « two » accentué", "Il est muet", "Comme « toe »"], "De façon réduite /tə/", "Les mots grammaticaux sont souvent réduits."),
  Q("Quel est le son le plus fréquent en anglais, présent dans les syllabes non accentuées ?", ["Le schwa /ə/", "Le son /i:/", "Le son /æ/", "Le son /θ/"], "Le schwa /ə/", "Comme le « a » de « about »."),
]),
notion('RL-4', 0, I, 'angph-rythme', [
  Q("Quels mots sont généralement accentués dans une phrase anglaise ?", ["Les mots porteurs de sens (noms, verbes, adjectifs)", "Les articles", "Les prépositions", "Les pronoms uniquement"], "Les mots porteurs de sens (noms, verbes, adjectifs)", "On parle de langue accentuelle."),
  Q("Dans « I WANT to BUY a NEW CAR », que montrent les majuscules ?", ["Les syllabes accentuées", "Les mots importants à écrire", "Les fautes", "Les verbes"], "Les syllabes accentuées", "Le rythme de l'anglais repose sur ces accents."),
  Q("Pourquoi l'anglais semble-t-il « rapide » aux francophones ?", ["Les syllabes non accentuées sont très réduites", "Les Anglais parlent toujours vite", "Il y a moins de mots", "Les voyelles n'existent pas"], "Les syllabes non accentuées sont très réduites", "Le rythme est inégal."),
]),
notion('RL-4', 0, I, 'angph-intonation', [
  Q("Comment évolue l'intonation d'une question commençant par « Where » ?", ["Elle descend à la fin", "Elle monte à la fin", "Elle reste plate", "Elle monte au milieu"], "Elle descend à la fin", "Questions ouvertes (wh-) : intonation descendante."),
  Q("Comment évolue l'intonation d'une énumération comme « apples, pears and bananas » ?", ["Elle monte sur chaque élément puis descend sur le dernier", "Elle descend partout", "Elle reste plate", "Elle monte sur le dernier"], "Elle monte sur chaque élément puis descend sur le dernier", "On montre que la liste continue."),
  Q("Que peut exprimer une intonation montante sur « Really? » ?", ["La surprise ou le doute", "L'ordre", "La colère", "L'ennui"], "La surprise ou le doute", "L'intonation porte du sens."),
]),
notion('RL-4', 0, I, 'angph-voyelles-difficiles', [
  Q("Quels mots ne doivent pas être confondus à cause de leurs voyelles ?", ["Hat / hut / heart", "Dog / dogs", "Cat / cats", "Run / runs"], "Hat / hut / heart", "Trois voyelles différentes."),
  Q("Quel mot se prononce avec la diphtongue « aï » ?", ["Bike", "Bit", "Beat", "Bet"], "Bike", "Le « i » + e muet se prononce « aï »."),
  Q("Quelle règle explique la prononciation de « cake » ?", ["Le e final muet allonge la voyelle (a → « eï »)", "Le e se prononce « eu »", "Le a est toujours court", "Le k est muet"], "Le e final muet allonge la voyelle (a → « eï »)", "Comparez cap et cape."),
]),
notion('RL-4', 0, I, 'angph-mots-pieges', [
  Q("Comment se prononce le début de « women » ?", ["Comme « wimin »", "Comme « woman »", "Comme « wo-men »", "Comme « vou-men »"], "Comme « wimin »", "C'est un pluriel irrégulier à la prononciation surprenante."),
  Q("Combien de syllabes prononce-t-on dans « comfortable » ?", ["Trois (COMF-ta-ble)", "Quatre", "Cinq", "Deux"], "Trois (COMF-ta-ble)", "Une syllabe disparaît à l'oral."),
  Q("Comment se prononce « Leicester » (ville anglaise) ?", ["« Lester »", "« Lai-ces-ter »", "« Lei-chester »", "« Lis-ter »"], "« Lester »", "Les noms de lieux britanniques réservent des surprises."),
]),
notion('RL-4', 0, I, 'angph-contractions', [
  Q("Comment se prononce « I'm » ?", ["« aïm », en une seule syllabe", "« i-am » en deux syllabes", "« im »", "« am »"], "« aïm », en une seule syllabe", "Les contractions sont naturelles à l'oral."),
  Q("Quelle est la forme contractée de « will not » ?", ["Won't", "Willn't", "Wiln't", "Wont'"], "Won't", "À ne pas confondre avec want."),
  Q("Quelle est la forme contractée de « they are » ?", ["They're", "Their", "There", "They'r"], "They're", "They're, their et there se prononcent de la même façon."),
]),
notion('RL-4', 0, D, 'angph-phonetique', [
  Q("Que représente le symbole phonétique /ʃ/ ?", ["Le son « ch » de « she »", "Le son « s » de « sun »", "Le son « tch » de « chair »", "Le son « j » de « jam »"], "Le son « ch » de « she »", "L'alphabet phonétique international (API) note les sons."),
  Q("Que représente le symbole /ŋ/ ?", ["Le son final de « sing »", "Le son « n » de « no »", "Le son « gn » de « agneau »", "Le son « m »"], "Le son final de « sing »", "On ne prononce pas un g séparé."),
  Q("Que représente le symbole /æ/ ?", ["Le « a » ouvert de « cat »", "Le « a » long de « car »", "Le « e » de « bed »", "Le « u » de « cup »"], "Le « a » ouvert de « cat »", "Entre « a » et « è »."),
]),
notion('RL-4', 0, D, 'angph-r-britannique-americain', [
  Q("Prononce-t-on le « r » final de « car » en anglais britannique standard ?", ["Non, en général", "Oui, toujours fortement", "Seulement en Écosse", "Seulement le dimanche"], "Non, en général", "On dit que la RP est non rhotique."),
  Q("Dans quel accent prononce-t-on nettement le « r » de « car » ?", ["L'accent américain", "La Received Pronunciation", "Le Cockney", "Aucun"], "L'accent américain", "Ainsi que les accents écossais et irlandais."),
  Q("Comment se prononce souvent le « t » de « water » en anglais américain ?", ["Comme un « d » rapide", "Comme un « t » fort", "Il est muet", "Comme un « th »"], "Comme un « d » rapide", "On parle de flapping."),
]),
notion('RL-4', 0, D, 'angph-liaisons', [
  Q("Comment se prononce naturellement « an apple » ?", ["En liant le n au a : « a-napple »", "En séparant fortement les deux mots", "En supprimant le a", "En ajoutant un h"], "En liant le n au a : « a-napple »", "C'est une liaison consonne-voyelle."),
  Q("Comment se prononce souvent « Did you » à l'oral rapide ?", ["« Didja »", "« Did-iou » très séparé", "« Dou »", "« Diddy »"], "« Didja »", "C'est une assimilation."),
  Q("Comment se prononce souvent « going to » à l'oral familier ?", ["« Gonna »", "« Goingto »", "« Goto »", "« Gaine »"], "« Gonna »", "Il ne s'écrit ainsi qu'en registre familier."),
]),
notion('RL-4', 0, D, 'angph-accent-phrase-sens', [
  Q("Que signifie « I didn't take YOUR book » avec l'accent sur « your » ?", ["J'ai pris un livre, mais pas le tien", "Je n'ai rien pris", "Quelqu'un d'autre l'a pris", "J'ai pris ton cahier"], "J'ai pris un livre, mais pas le tien", "L'accent de phrase change le sens."),
  Q("Que signifie « I didn't take your book » avec l'accent sur « I » ?", ["Ce n'est pas moi qui l'ai pris", "Je l'ai acheté", "Je l'ai pris hier", "Je ne l'ai pas lu"], "Ce n'est pas moi qui l'ai pris", "On insiste sur le sujet."),
  Q("Comment appelle-t-on l'accent qui met en valeur un mot pour l'opposer à un autre ?", ["L'accent contrastif", "L'accent régional", "L'accent écrit", "L'accent tonique de mot"], "L'accent contrastif", "Il sert à corriger ou opposer."),
]),
notion('RL-4', 0, D, 'angph-s-pluriel-3', [
  Q("Comment se prononce le -s de « cats » ?", ["/s/", "/z/", "/ɪz/", "Il est muet"], "/s/", "Après un son sourd."),
  Q("Comment se prononce le -es de « buses » ?", ["/ɪz/", "/s/", "/z/", "Il est muet"], "/ɪz/", "Après s, z, ch, sh, x."),
  Q("Comment se prononce le -s de « plays » ?", ["/z/", "/s/", "/ɪz/", "Il est muet"], "/z/", "Après une voyelle ou un son sonore."),
]),
notion('RL-4', 0, D, 'angph-poesie-rythme', [
  Q("Quel mètre utilise souvent Shakespeare, avec cinq accents par vers ?", ["Le pentamètre iambique", "L'alexandrin", "L'hexamètre dactylique", "Le haïku"], "Le pentamètre iambique", "Da-DUM da-DUM da-DUM da-DUM da-DUM."),
  Q("Comment appelle-t-on la répétition d'un même son consonne en début de mots, comme « Peter Piper picked » ?", ["Une allitération", "Une rime", "Une assonance", "Une onomatopée"], "Une allitération", "Les virelangues l'utilisent beaucoup."),
  Q("Qu'est-ce qu'une onomatopée, comme « buzz » ou « splash » ?", ["Un mot qui imite un son", "Un mot étranger", "Un mot très long", "Un mot muet"], "Un mot qui imite un son", "Woof, meow, bang…"),
]),
# ══ RL-5 · Lexique ══
notion('RL-4', 0, D, 'angph-orthographe-son', [
  Q("Quel mot se prononce différemment des autres pour « ough » ?", ["Through", "Though", "Dough", "Although"], "Through", "Though, dough et although riment ; through se prononce « throu »."),
  Q("Comment se prononce « ough » dans « enough » ?", ["« eff »", "« oh »", "« ou »", "« aw »"], "« eff »", "Comme dans rough, tough."),
  Q("Quel mot ne rime pas avec « great » ?", ["Treat", "Late", "Wait", "Eight"], "Treat", "Great se prononce comme « grate »."),
]),
notion('RL-5', 0, F, 'anglex-corps', [
  Q("Que signifie « hand » ?", ["La main", "La tête", "Le pied", "Le bras"], "La main", "Arm = bras, foot = pied."),
  Q("Comment dit-on « le dos » ?", ["The back", "The belly", "The neck", "The leg"], "The back", "Neck = cou, leg = jambe."),
  Q("Quel est le pluriel de « foot » ?", ["Feet", "Foots", "Feets", "Footes"], "Feet", "Pluriel irrégulier, comme tooth → teeth."),
]),
notion('RL-5', 0, F, 'anglex-maison-objets', [
  Q("Que signifie « fridge » ?", ["Le réfrigérateur", "Le four", "L'évier", "La table"], "Le réfrigérateur", "Oven = four, sink = évier."),
  Q("Comment dit-on « une chaise » ?", ["A chair", "A chain", "A cheer", "A share"], "A chair", "Armchair = fauteuil."),
  Q("Que signifie « stairs » ?", ["Les escaliers", "Les étoiles", "Les étages", "Les murs"], "Les escaliers", "Stars = étoiles."),
]),
notion('RL-5', 0, F, 'anglex-vetements-2', [
  Q("Que signifie « trainers » en anglais britannique ?", ["Des baskets", "Des entraîneurs uniquement", "Des trains", "Des chaussettes"], "Des baskets", "Sneakers en anglais américain."),
  Q("Comment dit-on « un manteau » ?", ["A coat", "A coast", "A cot", "A cat"], "A coat", "Coast = côte."),
  Q("Que signifie « gloves » ?", ["Des gants", "Des lunettes", "Des bottes", "Des écharpes"], "Des gants", "Scarf = écharpe."),
]),
notion('RL-5', 0, F, 'anglex-transports', [
  Q("Que signifie « plane » ?", ["Un avion", "Une plaine", "Une planète", "Un plan"], "Un avion", "Airplane (US), aeroplane (GB)."),
  Q("Comment dit-on « un bateau » ?", ["A boat", "A boot", "A bat", "A boot camp"], "A boat", "Boot = botte."),
  Q("Que signifie « underground » ?", ["Le métro (à Londres)", "Le sous-sol uniquement", "Un parking", "Un tunnel routier"], "Le métro (à Londres)", "On dit aussi the Tube."),
]),
notion('RL-5', 0, F, 'anglex-animaux-ferme', [
  Q("Que signifie « cow » ?", ["Une vache", "Un cheval", "Un cochon", "Un mouton"], "Une vache", "Horse = cheval, pig = cochon."),
  Q("Comment dit-on « un mouton » ?", ["A sheep", "A ship", "A goat", "A lamb only"], "A sheep", "Le pluriel est aussi sheep."),
  Q("Que signifie « hen » ?", ["Une poule", "Un coq", "Un canard", "Une dinde"], "Une poule", "Rooster = coq, duck = canard."),
]),
notion('RL-5', 0, F, 'anglex-adjectifs-contraires', [
  Q("Quel est le contraire de « cheap » ?", ["Expensive", "Easy", "Small", "Clean"], "Expensive", "Cheap = bon marché."),
  Q("Quel est le contraire de « empty » ?", ["Full", "Heavy", "Late", "Open"], "Full", "Empty = vide."),
  Q("Quel est le contraire de « early » ?", ["Late", "Slow", "Old", "Near"], "Late", "Early = tôt."),
]),
notion('RL-5', 0, F, 'anglex-nourriture-2', [
  Q("Que signifie « strawberry » ?", ["Une fraise", "Une framboise", "Une paille", "Une cerise"], "Une fraise", "Raspberry = framboise, cherry = cerise."),
  Q("Comment dit-on « des carottes » ?", ["Carrots", "Carrot's", "Carotts", "Carottes"], "Carrots", "Attention à l'orthographe."),
  Q("Que signifie « vegetables » ?", ["Les légumes", "Les végétariens", "Les plantes vertes", "Les fruits"], "Les légumes", "On dit souvent veggies."),
]),
notion('RL-5', 0, F, 'anglex-nature', [
  Q("Que signifie « tree » ?", ["Un arbre", "Trois", "Une herbe", "Une fleur"], "Un arbre", "Three = trois."),
  Q("Comment dit-on « une fleur » ?", ["A flower", "A flour", "A floor", "A flow"], "A flower", "Flour = farine, floor = sol."),
  Q("Que signifie « river » ?", ["Une rivière, un fleuve", "Un rivage", "Une rive", "Un ruisseau uniquement"], "Une rivière, un fleuve", "Stream = ruisseau."),
]),
notion('RL-5', 0, I, 'anglex-familles-mots', [
  Q("Quel nom correspond à l'adjectif « strong » ?", ["Strength", "Strongness", "Strongity", "Strongment"], "Strength", "Long → length, wide → width."),
  Q("Quel adjectif correspond au nom « danger » ?", ["Dangerous", "Dangery", "Dangerful", "Dangerless only"], "Dangerous", "Le suffixe -ous forme des adjectifs."),
  Q("Quel nom correspond au verbe « to decide » ?", ["Decision", "Decidement", "Decidence", "Decidity"], "Decision", "To discuss → discussion."),
]),
notion('RL-5', 0, I, 'anglex-prefixes', [
  Q("Que signifie le préfixe « re- » dans « rewrite » ?", ["De nouveau", "Contre", "Avant", "Pas"], "De nouveau", "Réécrire."),
  Q("Quel préfixe donne le contraire de « happy » ?", ["Un-", "Dis-", "Im-", "Ir-"], "Un-", "Unhappy = malheureux."),
  Q("Quel préfixe donne le contraire de « agree » ?", ["Dis-", "Un-", "In-", "Non-"], "Dis-", "Disagree = ne pas être d'accord."),
]),
notion('RL-5', 0, I, 'anglex-suffixes', [
  Q("Que signifie le suffixe « -less » dans « homeless » ?", ["Sans", "Plein de", "Petit", "Très"], "Sans", "Homeless = sans abri."),
  Q("Que signifie le suffixe « -ful » dans « useful » ?", ["Plein de, qui a", "Sans", "Contraire de", "Qui fait"], "Plein de, qui a", "Useful = utile ; useless = inutile."),
  Q("Que désigne le suffixe « -er » dans « teacher » ?", ["La personne qui fait l'action", "Le lieu", "L'objet", "Le contraire"], "La personne qui fait l'action", "Driver, player, singer…"),
]),
notion('RL-5', 0, I, 'anglex-make-do', [
  Q("Complétez : « I always ___ my homework after school. »", ["do", "make", "take", "have"], "do", "Do homework, do the shopping."),
  Q("Complétez : « Don't ___ a noise! »", ["make", "do", "take", "give"], "make", "Make a noise, make a mistake."),
  Q("Complétez : « Can you ___ me a favour? »", ["do", "make", "give", "take"], "do", "Do someone a favour."),
]),
notion('RL-5', 0, I, 'anglex-verbes-confondus', [
  Q("Quelle différence y a-t-il entre « borrow » et « lend » ?", ["Borrow = emprunter ; lend = prêter", "Ils sont identiques", "Borrow = prêter", "Lend = voler"], "Borrow = emprunter ; lend = prêter", "Can I borrow your pen? / Can you lend me your pen?"),
  Q("Quelle différence y a-t-il entre « look », « see » et « watch » ?", ["Look = regarder ; see = voir ; watch = regarder quelque chose qui bouge", "Ils sont identiques", "See = regarder la télé", "Watch = voir sans regarder"], "Look = regarder ; see = voir ; watch = regarder quelque chose qui bouge", "Watch TV, look at a picture, see the sea."),
  Q("Quelle différence y a-t-il entre « win » et « earn » ?", ["Win = gagner (un match) ; earn = gagner (de l'argent en travaillant)", "Ils sont identiques", "Earn = gagner un match", "Win = travailler"], "Win = gagner (un match) ; earn = gagner (de l'argent en travaillant)", "Le français utilise un seul verbe."),
]),
notion('RL-5', 0, I, 'anglex-mots-composes', [
  Q("Que signifie « bookshop » ?", ["Une librairie", "Une bibliothèque", "Un livre de magasin", "Un cahier"], "Une librairie", "Book + shop."),
  Q("Que signifie « sunglasses » ?", ["Des lunettes de soleil", "Des verres au soleil", "Un coup de soleil", "Une crème solaire"], "Des lunettes de soleil", "Le premier élément précise le second."),
  Q("Que signifie « toothbrush » ?", ["Une brosse à dents", "Un dentifrice", "Un dentiste", "Une dent cassée"], "Une brosse à dents", "Toothpaste = dentifrice."),
]),
notion('RL-5', 0, I, 'anglex-phrasal-verbs-courants', [
  Q("Que signifie « to put on » un vêtement ?", ["Mettre", "Enlever", "Ranger", "Acheter"], "Mettre", "To take off = enlever."),
  Q("Que signifie « to turn down » le volume ?", ["Baisser", "Monter", "Couper", "Allumer"], "Baisser", "To turn up = monter."),
  Q("Que signifie « to find out » ?", ["Découvrir, apprendre", "Trouver dehors", "Perdre", "Chercher"], "Découvrir, apprendre", "I found out the truth."),
]),
notion('RL-5', 0, I, 'anglex-synonymes', [
  Q("Quel mot est un synonyme de « big » ?", ["Large", "Little", "Narrow", "Short"], "Large", "Faux ami : large = grand."),
  Q("Quel mot est un synonyme de « begin » ?", ["Start", "Stop", "End", "Finish"], "Start", "Begin, began, begun."),
  Q("Quel mot est un synonyme de « quick » ?", ["Fast", "Slow", "Late", "Heavy"], "Fast", "Rapid est plus soutenu."),
]),
notion('RL-5', 0, I, 'anglex-lexique-ecole', [
  Q("Que signifie « mark » (ou « grade » aux États-Unis) à l'école ?", ["Une note", "Une marque", "Un marqueur", "Un niveau de classe uniquement"], "Une note", "To mark = corriger."),
  Q("Que signifie « to revise » au Royaume-Uni ?", ["Réviser (ses leçons)", "Revoir un film", "Réécrire une loi", "Revenir"], "Réviser (ses leçons)", "Aux États-Unis : to review."),
  Q("Que signifie « to fail an exam » ?", ["Échouer à un examen", "Réussir un examen", "Passer un examen", "Annuler un examen"], "Échouer à un examen", "To pass = réussir (faux ami)."),
]),
notion('RL-5', 0, D, 'anglex-idiomes-2', [
  Q("Que signifie « to be over the moon » ?", ["Être aux anges", "Être sur la Lune", "Être distrait", "Être déçu"], "Être aux anges", "Expression de grande joie."),
  Q("Que signifie « to cost an arm and a leg » ?", ["Coûter les yeux de la tête", "Se casser un bras", "Être très bon marché", "Être fatigué"], "Coûter les yeux de la tête", "Le français parle d'yeux, l'anglais de bras et de jambe."),
  Q("Que signifie « to feel under the weather » ?", ["Ne pas se sentir bien", "Aimer la pluie", "Avoir froid", "Être de bonne humeur"], "Ne pas se sentir bien", "Légèrement malade."),
]),
notion('RL-5', 0, D, 'anglex-faux-amis-2', [
  Q("Que signifie « deception » en anglais ?", ["Une tromperie", "Une déception", "Une décision", "Une description"], "Une tromperie", "Déception = disappointment."),
  Q("Que signifie « to pretend » ?", ["Faire semblant", "Prétendre (affirmer)", "Préparer", "Présenter"], "Faire semblant", "Prétendre = to claim."),
  Q("Que signifie « injury » ?", ["Une blessure", "Une injure", "Une injustice", "Une injection"], "Une blessure", "Injure (insulte) = insult."),
]),
notion('RL-5', 0, D, 'anglex-collocations', [
  Q("Quelle expression est correcte en anglais ?", ["Heavy rain", "Strong rain", "Big rain", "Fat rain"], "Heavy rain", "Certaines associations de mots sont figées."),
  Q("Quelle expression est correcte ?", ["To take a photo", "To make a photo", "To do a photo", "To have a photo take"], "To take a photo", "To take a shower, take a break…"),
  Q("Quelle expression est correcte ?", ["Fast food", "Quick food", "Rapid food", "Speed food"], "Fast food", "Fast et quick ne sont pas toujours interchangeables."),
]),
notion('RL-5', 0, D, 'anglex-emprunts', [
  Q("De quelle langue vient le mot anglais « ballet » ?", ["Du français", "De l'italien", "Du russe", "Du grec"], "Du français", "Comme menu, chef, garage."),
  Q("De quelle langue vient le mot anglais « tsunami » ?", ["Du japonais", "Du chinois", "Du coréen", "Du hawaïen"], "Du japonais", "Comme karaoke, emoji, karate."),
  Q("De quelle langue vient le mot « kindergarten » utilisé en anglais américain ?", ["De l'allemand", "Du néerlandais", "Du français", "Du suédois"], "De l'allemand", "« Jardin d'enfants »."),
]),
notion('RL-5', 0, D, 'anglex-niveaux-langue', [
  Q("Quel mot est le plus familier pour dire « enfant » ?", ["Kid", "Child", "Offspring", "Minor"], "Kid", "Offspring est soutenu, minor est juridique."),
  Q("Quel mot est le plus soutenu pour dire « acheter » ?", ["Purchase", "Buy", "Get", "Grab"], "Purchase", "Grab est familier."),
  Q("Quel mot familier signifie « ami » au Royaume-Uni et en Australie ?", ["Mate", "Buddy only", "Fellow", "Comrade"], "Mate", "Buddy est plus américain."),
]),
notion('RL-5', 0, D, 'anglex-mots-recents', [
  Q("Que signifie « to unfriend » sur un réseau social ?", ["Retirer quelqu'un de ses amis", "Se faire un ami", "Inviter un ami", "Bloquer un site"], "Retirer quelqu'un de ses amis", "Le mot entre dans les dictionnaires en 2009."),
  Q("Que signifie « staycation » ?", ["Des vacances passées chez soi ou près de chez soi", "Une station de ski", "Un séjour à l'hôtel", "Un voyage d'affaires"], "Des vacances passées chez soi ou près de chez soi", "Stay + vacation."),
  Q("Que signifie « emoji » ?", ["Un petit pictogramme d'émotion", "Une émotion forte", "Un émigré", "Un e-mail"], "Un petit pictogramme d'émotion", "Le mot vient du japonais."),
]),
notion('RL-5', 0, D, 'anglex-sens-multiples', [
  Q("Que signifie « bank » dans « the bank of the river » ?", ["La rive", "La banque", "Le banc", "Le pont"], "La rive", "Le contexte donne le sens."),
  Q("Que signifie « fine » dans « You'll get a fine for parking here » ?", ["Une amende", "Bien", "Fin, mince", "Beau temps"], "Une amende", "I'm fine = je vais bien."),
  Q("Que signifie « bat » dans « a cricket bat » ?", ["Une batte", "Une chauve-souris", "Un bateau", "Un battement"], "Une batte", "Bat signifie aussi chauve-souris."),
]),
# ══ OG-1 · Le verbe ══
notion('OG-1', 0, D, 'anggr-verbe-avance-1', [
  Q("Complétez : « By next year, I ___ my studies. » (finish, futur antérieur)", ["will have finished", "will finish", "have finished", "finished"], "will have finished", "Will have + participe passé."),
  Q("Complétez : « I ___ here for two hours when he finally arrived. »", ["had been waiting", "have been waiting", "was waited", "am waiting"], "had been waiting", "Past perfect en be + ing : durée avant un moment passé."),
  Q("Complétez : « This time tomorrow, we ___ on the beach. »", ["will be lying", "will lie", "are lying", "lay"], "will be lying", "Futur en be + ing : action en cours à un moment futur."),
]),
notion('OG-1', 0, D, 'anggr-verbe-avance-2', [
  Q("Complétez : « She is said ___ very rich. »", ["to be", "being", "be", "that she is"], "to be", "Passif avec infinitif : on dit qu'elle est…"),
  Q("Complétez : « The house needs ___. » (paint)", ["painting", "to painting", "paint", "painted"], "painting", "Need + V-ing a un sens passif."),
  Q("Complétez : « I'd rather you ___ now. » (leave)", ["left", "leave", "to leave", "leaving"], "left", "I'd rather + sujet + prétérit."),
]),
notion('OG-1', 0, D, 'anggr-verbe-avance-3', [
  Q("Complétez : « It's time we ___ home. »", ["went", "go", "going", "will go"], "went", "It's time + sujet + prétérit (irréel)."),
  Q("Que signifie « You needn't have bought flowers » ?", ["Ce n'était pas la peine d'acheter des fleurs (mais tu l'as fait)", "Tu dois acheter des fleurs", "Tu n'as pas acheté de fleurs", "Tu achèteras des fleurs"], "Ce n'était pas la peine d'acheter des fleurs (mais tu l'as fait)", "Needn't have + participe passé."),
  Q("Complétez : « He might ___ the bus. » (miss, possibilité passée)", ["have missed", "missed", "miss", "missing"], "have missed", "Modal + have + participe passé."),
]),
notion('OG-1', 0, D, 'anggr-verbe-avance-4', [
  Q("Complétez : « I'm getting used to ___ on the left. »", ["driving", "drive", "drove", "be drive"], "driving", "Get used to + V-ing."),
  Q("Complétez : « She remembered ___ the door. » (souvenir d'une action passée)", ["locking", "to lock", "lock", "locked"], "locking", "Remember + V-ing = se souvenir d'avoir fait."),
  Q("Complétez : « Remember ___ the door before leaving! » (ne pas oublier)", ["to lock", "locking", "lock", "locked"], "to lock", "Remember + to = penser à faire."),
]),
# ══ OG-2 · Le nom et le groupe nominal ══
notion('OG-2', 0, F, 'anggr-gn-ordre', [
  Q("Quelle phrase a l'ordre correct des adjectifs ?", ["A big black dog", "A black big dog", "A dog big black", "A dog black big"], "A big black dog", "La taille avant la couleur."),
  Q("Les adjectifs anglais prennent-ils un -s au pluriel ?", ["Non, jamais", "Oui, toujours", "Seulement après un nom", "Seulement les couleurs"], "Non, jamais", "Red cars, pas « reds cars »."),
  Q("Complétez : « a ___ » (une boîte en carton)", ["cardboard box", "box cardboard", "box of cardboard's", "cardboards box"], "cardboard box", "Le nom qui précise se place devant."),
]),
notion('OG-2', 0, F, 'anggr-pluriels-irreguliers', [
  Q("Quel est le pluriel de « woman » ?", ["Women", "Womans", "Womens", "Woman"], "Women", "Man → men."),
  Q("Quel est le pluriel de « tooth » ?", ["Teeth", "Tooths", "Teeths", "Toothes"], "Teeth", "Foot → feet."),
  Q("Quel est le pluriel de « baby » ?", ["Babies", "Babys", "Babyes", "Babis"], "Babies", "Consonne + y → ies."),
]),
notion('OG-2', 0, I, 'anggr-articles-zero', [
  Q("Complétez : « ___ life is beautiful. » (en général)", ["—", "The", "A", "An"], "—", "Pas d'article pour une généralité."),
  Q("Complétez : « I go to ___ school by bus. » (l'école en tant qu'institution)", ["—", "the", "a", "an"], "—", "Go to school, go to bed, go to church."),
  Q("Complétez : « ___ Thames flows through London. »", ["The", "—", "A", "An"], "The", "The devant les fleuves, mers et océans."),
]),
notion('OG-2', 0, I, 'anggr-quantifieurs', [
  Q("Complétez : « I have ___ friends here, so I'm not lonely. » (quelques)", ["a few", "few", "a little", "little"], "a few", "A few = quelques (positif) ; few = peu (négatif)."),
  Q("Complétez : « There's ___ milk left. Buy some! » (peu)", ["little", "few", "a few", "many"], "little", "Little + indénombrable."),
  Q("Complétez : « ___ of my friends play tennis. » (aucun)", ["None", "No", "Any", "Nobody"], "None", "None of + pluriel."),
]),
notion('OG-2', 0, I, 'anggr-genitif-avance', [
  Q("Comment dit-on « le bureau de mon père et de ma mère » (un seul bureau commun) ?", ["My father and mother's office", "My father's and mother's office", "My father's and my mother office", "The office of my father's mother"], "My father and mother's office", "Le 's porte sur l'ensemble."),
  Q("Comment dit-on « chez le médecin » ?", ["At the doctor's", "At the doctor", "In doctor's", "At doctor home"], "At the doctor's", "Le nom de lieu est sous-entendu."),
  Q("Comment dit-on « un trajet de deux heures » ?", ["A two hours' journey (a two-hour journey)", "A journey of two hour", "A two hours journey's", "Two hours journey a"], "A two hours' journey (a two-hour journey)", "Génitif de mesure."),
]),
notion('OG-2', 0, I, 'anggr-indenombrables', [
  Q("Quel nom est indénombrable en anglais ?", ["Advice", "Idea", "Suggestion", "Tip"], "Advice", "A piece of advice = un conseil."),
  Q("Comment dit-on « une information » ?", ["A piece of information", "An information", "One informations", "A informations"], "A piece of information", "Information n'a pas de pluriel."),
  Q("Quelle phrase est correcte ?", ["My luggage is heavy.", "My luggages are heavy.", "My luggage are heavy.", "A luggage is heavy."], "My luggage is heavy.", "Luggage, furniture, news sont indénombrables."),
]),
notion('OG-2', 0, I, 'anggr-demonstratifs', [
  Q("Complétez : « ___ shoes are mine. » (ces chaussures-ci, proches)", ["These", "This", "Those", "That"], "These", "This/these : proche ; that/those : éloigné."),
  Q("Complétez : « Look at ___ birds in the sky! » (éloignés)", ["those", "these", "this", "that"], "those", "Those = ces… là-bas."),
  Q("Complétez : « ___ is my brother. » (en présentant)", ["This", "These", "Those", "Them"], "This", "This is… pour présenter quelqu'un."),
]),
notion('OG-2', 0, I, 'anggr-noms-composes', [
  Q("Quel est le pluriel de « bus stop » ?", ["Bus stops", "Buses stop", "Buses stops", "Bus's stops"], "Bus stops", "Seul le dernier élément prend la marque du pluriel."),
  Q("Quel est le pluriel de « mother-in-law » ?", ["Mothers-in-law", "Mother-in-laws", "Mothers-in-laws", "Mother-ins-law"], "Mothers-in-law", "C'est le nom principal qui prend le s."),
  Q("Que signifie « a coffee cup » ?", ["Une tasse à café", "Une tasse de café", "Un café en tasse", "Une cafetière"], "Une tasse à café", "A cup of coffee = une tasse de café."),
]),
notion('OG-2', 0, I, 'anggr-each-every', [
  Q("Complétez : « ___ student has a locker. »", ["Every", "All", "Both", "Many"], "Every", "Every + singulier."),
  Q("Complétez : « ___ of the two sisters is tall. »", ["Each", "Every", "All", "Some"], "Each", "Each of + pluriel, avec un verbe au singulier."),
  Q("Complétez : « ___ my friends came to the party. »", ["All", "Every", "Each", "Both of the all"], "All", "All + pluriel."),
]),
notion('OG-2', 0, I, 'anggr-some-any-avance', [
  Q("Complétez : « Would you like ___ tea? » (offre polie)", ["some", "any", "a", "many"], "some", "Some dans une offre, même à la forme interrogative."),
  Q("Complétez : « You can take ___ book you like. » (n'importe lequel)", ["any", "some", "no", "every"], "any", "Any = n'importe quel à la forme affirmative."),
  Q("Complétez : « There are ___ students in the classroom. » (aucun)", ["no", "any", "none", "not"], "no", "No + nom = aucun."),
]),
notion('OG-2', 0, D, 'anggr-gn-complexe', [
  Q("Que signifie « a hard-working, well-known English teacher » ?", ["Un professeur d'anglais travailleur et réputé", "Un enseignant anglais qui travaille dur à l'école célèbre", "Une école anglaise connue", "Un travail d'anglais difficile"], "Un professeur d'anglais travailleur et réputé", "On lit le groupe nominal de droite à gauche."),
  Q("Quelle phrase a l'ordre correct ?", ["A beautiful old Italian car", "An Italian old beautiful car", "An old beautiful Italian car", "A car Italian old beautiful"], "A beautiful old Italian car", "Opinion, âge, origine, puis nom."),
  Q("Que signifie « a ten-pound note » ?", ["Un billet de dix livres", "Dix billets d'une livre", "Une note sur dix", "Un poids de dix livres"], "Un billet de dix livres", "Pound reste au singulier dans l'adjectif composé."),
]),
notion('OG-2', 0, D, 'anggr-articles-avances', [
  Q("Complétez : « He plays ___ guitar, but he prefers ___ football. »", ["the / —", "— / the", "a / a", "the / the"], "the / —", "Play the + instrument ; play + sport sans article."),
  Q("Complétez : « ___ rich should help ___ poor. »", ["The / the", "— / —", "A / a", "The / a"], "The / the", "The + adjectif = un groupe de personnes."),
  Q("Complétez : « What ___ lovely weather! »", ["—", "a", "an", "the"], "—", "Weather est indénombrable : pas de a."),
]),
notion('OG-2', 0, D, 'anggr-noms-collectifs', [
  Q("Quel verbe peut suivre « The police » ?", ["Are (pluriel)", "Is (singulier)", "Be", "Was only"], "Are (pluriel)", "Police est toujours pluriel."),
  Q("Le mot « news » est-il singulier ou pluriel ?", ["Singulier : the news is…", "Pluriel : the news are…", "Les deux", "Il n'existe pas"], "Singulier : the news is…", "Malgré son -s final."),
  Q("Quel nom désigne un groupe et peut être suivi d'un verbe singulier ou pluriel en anglais britannique ?", ["Team (ou family)", "Information", "Advice", "Furniture"], "Team (ou family)", "The team is / are winning."),
]),
notion('OG-2', 0, D, 'anggr-suffixes-noms', [
  Q("Quel suffixe forme un nom abstrait à partir de « free » ?", ["-dom (freedom)", "-ness", "-ment", "-ship"], "-dom (freedom)", "Kingdom, boredom…"),
  Q("Quel suffixe forme un nom à partir de « friend » ?", ["-ship (friendship)", "-dom", "-ity", "-tion"], "-ship (friendship)", "Relationship, leadership…"),
  Q("Quel nom correspond à « improve » ?", ["Improvement", "Improvation", "Improvity", "Improvance"], "Improvement", "-ment forme des noms à partir de verbes."),
]),
notion('OG-2', 0, D, 'anggr-determinants-complexes', [
  Q("Complétez : « ___ of the twins is good at maths. » (aucun des deux)", ["Neither", "None", "Nor", "No"], "Neither", "Neither of = aucun des deux."),
  Q("Complétez : « You can take ___ bus; they both go downtown. »", ["either", "neither", "both", "all"], "either", "Either = l'un ou l'autre."),
  Q("Complétez : « ___ my parents are teachers. » (tous les deux)", ["Both", "Either", "All of", "Each"], "Both", "Both = les deux."),
]),
notion('OG-2', 0, D, 'anggr-pluriels-savants', [
  Q("Quel est le pluriel de « crisis » ?", ["Crises", "Crisises", "Crisis", "Crisii"], "Crises", "Mot d'origine grecque."),
  Q("Quel est le pluriel de « phenomenon » ?", ["Phenomena", "Phenomenons only", "Phenomenas", "Phenomeni"], "Phenomena", "Comme criterion → criteria."),
  Q("Quel est le pluriel de « fish » ?", ["Fish (ou fishes pour des espèces)", "Fishs", "Fishen", "Fishies"], "Fish (ou fishes pour des espèces)", "Comme sheep et deer."),
]),
notion('OG-2', 0, D, 'anggr-adjectifs-substantives', [
  Q("Comment dit-on « les Anglais » (le peuple) ?", ["The English", "The Englishes", "The Englishs", "English peoples"], "The English", "Comme the French, the Welsh."),
  Q("Comment dit-on « les chômeurs » ?", ["The unemployed", "The unemployeds", "Unemployed people's", "The unemploy"], "The unemployed", "The + adjectif."),
  Q("Comment dit-on « un Anglais » (une personne) ?", ["An Englishman", "An English", "A English", "An Englishe"], "An Englishman", "An Englishwoman au féminin."),
]),
# ══ OG-3 · Les pronoms ══
notion('OG-2', 0, D, 'anggr-nom-verbal', [
  Q("Que signifie « Swimming is good for you » ?", ["La natation est bonne pour toi", "Tu nages bien", "Nager est interdit", "Tu nageais"], "La natation est bonne pour toi", "Le gérondif peut être sujet."),
  Q("Complétez : « ___ too much sugar is unhealthy. »", ["Eating", "Eat", "To eating", "Eaten"], "Eating", "Gérondif sujet."),
  Q("Que signifie « his singing » ?", ["Sa façon de chanter, son chant", "Il chante", "Sa chanson écrite", "Son chanteur"], "Sa façon de chanter, son chant", "Possessif + gérondif."),
]),
notion('OG-3', 0, F, 'anggr-pronoms-sujets', [
  Q("Quel pronom remplace « my brothers » ?", ["They", "He", "We", "It"], "They", "They = ils, elles."),
  Q("Quel pronom remplace « you and I » ?", ["We", "They", "You", "Us"], "We", "We = nous."),
  Q("Quel pronom s'utilise pour un animal ou un objet ?", ["It", "He", "She", "They (singulier)"], "It", "On utilise parfois he ou she pour un animal familier."),
]),
notion('OG-3', 0, F, 'anggr-pronoms-complements', [
  Q("Complétez : « I love my grandma. I visit ___ every Sunday. »", ["her", "she", "hers", "his"], "her", "Her = la, lui (complément)."),
  Q("Complétez : « Where are the keys? I can't find ___. »", ["them", "they", "their", "it"], "them", "Them = les, leur."),
  Q("Complétez : « Listen to ___! » (moi)", ["me", "I", "my", "mine"], "me", "Me = moi (complément)."),
]),
notion('OG-3', 0, F, 'anggr-possessifs-adj', [
  Q("Complétez : « We love ___ house. »", ["our", "us", "ours", "we"], "our", "Our = notre, nos."),
  Q("Complétez : « The cat is eating ___ food. »", ["its", "it's", "his", "it"], "its", "Its = son, sa (chose ou animal) ; it's = it is."),
  Q("Complétez : « Is this ___ pen, Tom? »", ["your", "you", "yours", "you're"], "your", "You're = you are."),
]),
notion('OG-3', 0, F, 'anggr-interrogatifs', [
  Q("Complétez : « ___ is your brother? » — He's 14.", ["How old", "How", "What age", "How many"], "How old", "How old = quel âge."),
  Q("Complétez : « ___ book is this? » — It's Tom's.", ["Whose", "Who", "Who's", "Which"], "Whose", "Whose = à qui."),
  Q("Complétez : « ___ do you go to school? » — By bike.", ["How", "What", "Where", "Why"], "How", "How = comment."),
]),
notion('OG-3', 0, F, 'anggr-pronoms-possessifs', [
  Q("Complétez : « This bike is ___. » (à lui)", ["his", "him", "he's", "her"], "his", "His sert d'adjectif et de pronom."),
  Q("Complétez : « Those books are ___. » (à nous)", ["ours", "our", "us", "our's"], "ours", "Pas d'apostrophe : ours, yours, theirs."),
  Q("Complétez : « Is this pen yours or ___? » (à moi)", ["mine", "my", "me", "mines"], "mine", "Mine = le mien."),
]),
notion('OG-3', 0, F, 'anggr-something-anything', [
  Q("Complétez : « Is there ___ in the box? »", ["anything", "something", "nothing", "everything"], "anything", "Any- dans les questions."),
  Q("Complétez : « I want ___ to eat. »", ["something", "anything", "nothing", "anyone"], "something", "Some- à la forme affirmative."),
  Q("Complétez : « There's ___ at the door. » (quelqu'un)", ["somebody", "anybody", "nobody", "everybody"], "somebody", "Someone est synonyme."),
]),
notion('OG-3', 0, F, 'anggr-which-what', [
  Q("Complétez : « ___ colour do you prefer, red or blue? »", ["Which", "What", "Who", "Whose"], "Which", "Which = lequel (choix limité)."),
  Q("Complétez : « ___ time is it? »", ["What", "Which", "Who", "How"], "What", "What time is it? = quelle heure est-il ?"),
  Q("Complétez : « ___ did you call? » — My mum.", ["Who", "Whose", "Which", "What"], "Who", "Who peut être complément à l'oral."),
]),
notion('OG-3', 0, I, 'anggr-reflechis', [
  Q("Complétez : « She hurt ___. »", ["herself", "her", "himself", "itself"], "herself", "Pronom réfléchi."),
  Q("Complétez : « We made the cake ___. » (nous-mêmes)", ["ourselves", "ourself", "us", "ours"], "ourselves", "Pluriel : -selves."),
  Q("Que signifie « Help yourself! » ?", ["Servez-vous !", "Aidez-vous mutuellement !", "Aide-moi !", "Débrouille-toi seul !"], "Servez-vous !", "Formule d'hospitalité."),
]),
notion('OG-3', 0, I, 'anggr-each-other', [
  Q("Complétez : « Tom and Sarah love ___. » (l'un l'autre)", ["each other", "themselves", "them", "theirs"], "each other", "Each other = réciprocité."),
  Q("Quelle différence y a-t-il entre « They looked at themselves » et « They looked at each other » ?", ["Chacun s'est regardé lui-même / Ils se sont regardés mutuellement", "Aucune", "Ils ont regardé d'autres personnes", "Ils n'ont rien regardé"], "Chacun s'est regardé lui-même / Ils se sont regardés mutuellement", "Réfléchi ≠ réciproque."),
  Q("Complétez : « We help ___ with homework. » (mutuellement)", ["one another", "ourselves only", "us", "ours"], "one another", "One another = each other."),
]),
notion('OG-3', 0, I, 'anggr-relatifs-2', [
  Q("Complétez : « The man ___ car was stolen called the police. »", ["whose", "who", "which", "whom"], "whose", "Whose = dont."),
  Q("Complétez : « Paris, ___ is the capital of France, is beautiful. »", ["which", "that", "who", "what"], "which", "That est impossible après une virgule."),
  Q("Complétez : « I don't understand ___ he said. » (ce que)", ["what", "which", "that", "who"], "what", "What = ce que."),
]),
notion('OG-3', 0, I, 'anggr-one-ones', [
  Q("Complétez : « I don't like the red shirt. I prefer the blue ___. »", ["one", "ones", "it", "this"], "one", "One évite de répéter un nom singulier."),
  Q("Complétez : « These shoes are too small. I need bigger ___. »", ["ones", "one", "them", "it"], "ones", "Ones au pluriel."),
  Q("Complétez : « Which cake do you want? » — « The chocolate ___. »", ["one", "it", "ones", "this one's"], "one", "On évite la répétition."),
]),
notion('OG-3', 0, I, 'anggr-indefinis-negatifs', [
  Q("Complétez : « I saw ___ in the street. It was empty. »", ["nobody", "anybody", "somebody", "everybody"], "nobody", "Nobody = personne (sens négatif)."),
  Q("Complétez : « I didn't see ___. »", ["anybody", "nobody", "somebody", "everybody"], "anybody", "Une seule négation : didn't + anybody."),
  Q("Quelle phrase est correcte ?", ["I know nothing.", "I don't know nothing.", "I know anything not.", "I not know something."], "I know nothing.", "Pas de double négation en anglais standard."),
]),
notion('OG-3', 0, I, 'anggr-questions-sujet', [
  Q("Quelle question est correcte pour demander qui a cassé le vase ?", ["Who broke the vase?", "Who did break the vase?", "Who did broke the vase?", "Whom broke the vase?"], "Who broke the vase?", "Quand who est sujet, pas d'auxiliaire did."),
  Q("Quelle question est correcte ?", ["What happened?", "What did happen?", "What did happened?", "What happen?"], "What happened?", "What est sujet."),
  Q("Quelle question porte sur le complément ?", ["Who did you see?", "Who saw you?", "Who seen you?", "Who you saw?"], "Who did you see?", "Quand who est complément, on utilise did."),
]),
notion('OG-3', 0, D, 'anggr-relatifs-omis', [
  Q("Dans quelle phrase peut-on supprimer le pronom relatif ?", ["The film (that) we watched was great.", "The girl who lives here is nice.", "My sister, who is 20, studies law.", "The dog which bit me ran away."], "The film (that) we watched was great.", "Le relatif complément peut être omis."),
  Q("Complétez : « This is the house ___ I grew up in. »", ["(that)", "who", "what", "whose"], "(that)", "La préposition peut être rejetée en fin de phrase."),
  Q("Quelle version est plus soutenue ?", ["This is the house in which I grew up.", "This is the house I grew up in.", "This is the house what I grew up.", "This is house I grew up."], "This is the house in which I grew up.", "Préposition + which, registre soutenu."),
]),
notion('OG-3', 0, D, 'anggr-relatives-explicatives', [
  Q("Quelle phrase contient une relative explicative (non essentielle) ?", ["My mother, who is a nurse, works at night.", "The woman who called you is my mother.", "The book that I read was long.", "The man whose dog barks lives here."], "My mother, who is a nurse, works at night.", "Elle est entre virgules."),
  Q("Peut-on utiliser « that » dans une relative entre virgules ?", ["Non", "Oui, toujours", "Seulement pour les personnes", "Seulement au passé"], "Non", "On utilise who ou which."),
  Q("Complétez : « He failed the test, ___ surprised everybody. »", ["which", "what", "that", "who"], "which", "Which reprend toute la proposition."),
]),
notion('OG-3', 0, D, 'anggr-whoever-whatever', [
  Q("Que signifie « Whatever you do, don't panic » ?", ["Quoi que tu fasses, ne panique pas", "Tout ce que tu fais est panique", "Fais ce que tu veux", "Ne fais rien"], "Quoi que tu fasses, ne panique pas", "Whatever = quoi que."),
  Q("Complétez : « ___ wins will get a prize. » (quiconque)", ["Whoever", "Whatever", "Wherever", "Whichever"], "Whoever", "Whoever = quiconque."),
  Q("Que signifie « Sit wherever you like » ?", ["Assieds-toi où tu veux", "Assieds-toi là", "Ne t'assieds pas", "Assieds-toi quand tu veux"], "Assieds-toi où tu veux", "Wherever = n'importe où."),
]),
notion('OG-3', 0, D, 'anggr-it-there', [
  Q("Complétez : « ___ is important to drink water. »", ["It", "There", "This", "That"], "It", "It sujet apparent."),
  Q("Complétez : « ___ is no milk left. »", ["There", "It", "This", "Here"], "There", "There is = il y a."),
  Q("Complétez : « ___ takes two hours to get there. »", ["It", "There", "That", "They"], "It", "It takes… = il faut (durée)."),
]),
notion('OG-3', 0, D, 'anggr-one-generique', [
  Q("Que signifie « One should always be polite » ?", ["On devrait toujours être poli", "Une personne est polie", "Un seul doit être poli", "Sois poli une fois"], "On devrait toujours être poli", "One = on (soutenu)."),
  Q("Quel pronom est le plus courant à l'oral pour traduire « on » au sens général ?", ["You", "One", "It", "They uniquement"], "You", "You never know! = on ne sait jamais !"),
  Q("Comment traduit-on « On m'a dit que… » ?", ["I was told that…", "One told me that…", "It told me that…", "On said me that…"], "I was told that…", "Le passif traduit souvent « on »."),
]),
notion('OG-3', 0, D, 'anggr-pronoms-quantite', [
  Q("Complétez : « I asked two friends, but ___ of them could come. » (aucun des deux)", ["neither", "none", "either", "both"], "neither", "Neither pour deux personnes."),
  Q("Complétez : « I invited ten people, but ___ of them came. » (aucun)", ["none", "neither", "no", "either"], "none", "None pour plus de deux."),
  Q("Complétez : « Most ___ the students passed. »", ["of", "—", "from", "the"], "of", "Most of the + nom précis."),
]),
notion('OG-3', 0, D, 'anggr-emphatiques', [
  Q("Que signifie « I did it myself » ?", ["Je l'ai fait moi-même", "Je me le suis fait", "Je l'ai fait pour moi", "Je l'ai fait seul contre moi"], "Je l'ai fait moi-même", "Le réfléchi peut insister."),
  Q("Que signifie « The Queen herself opened the building » ?", ["La reine en personne a inauguré le bâtiment", "La reine s'est ouverte", "La reine était seule", "La reine a construit le bâtiment"], "La reine en personne a inauguré le bâtiment", "Pronom d'insistance."),
  Q("Que signifie « by myself » ?", ["Tout seul", "À côté de moi", "Par moi-même uniquement par écrit", "Pour moi"], "Tout seul", "On my own est synonyme."),
]),
# ══ OG-4 · Adverbes et groupes prépositionnels (temps et espace) ══
notion('OG-3', 0, D, 'anggr-pronoms-generiques-genre', [
  Q("Complétez : « If a student needs help, ___ should ask the teacher. »", ["they", "he only", "it", "one's"], "they", "Le « singular they » évite de préciser le genre."),
  Q("Complétez : « Everyone brought ___ own lunch. »", ["their", "his only", "its", "our"], "their", "Everyone + their dans l'usage courant."),
  Q("Quel pronom utilise-t-on pour un navire ou un pays dans un style traditionnel ?", ["She", "It uniquement", "He", "They"], "She", "Usage traditionnel : the ship… she."),
]),
notion('OG-3', 0, D, 'anggr-pronoms-interrogatifs-prep', [
  Q("Complétez : « ___ are you talking about? »", ["What", "Which about", "About what", "Who's"], "What", "La préposition se place en fin de question."),
  Q("Quelle question est la plus soutenue ?", ["To whom did you give it?", "Who did you give it to?", "Who you gave it to?", "To who you gave it?"], "To whom did you give it?", "Whom après une préposition."),
  Q("Complétez : « ___ is this present for? »", ["Who", "Whose", "Which", "Whom for"], "Who", "Who… for? = Pour qui… ?"),
]),
notion('OG-4', 0, F, 'anggr-ordinaux-dates', [
  Q("Comment écrit-on « le 2 juillet » en anglais britannique ?", ["2nd July", "2th July", "2st July", "July two"], "2nd July", "1st, 2nd, 3rd, 4th…"),
  Q("Comment dit-on « vingt et unième » ?", ["Twenty-first", "Twenty-oneth", "Twenty-one", "Twentieth-one"], "Twenty-first", "Abrégé : 21st."),
  Q("Comment écrit-on « le 3e étage » ?", ["The third floor", "The three floor", "The threeth floor", "The thirdth floor"], "The third floor", "Third = troisième."),
]),
notion('OG-4', 0, F, 'anggr-prepositions-lieu-2', [
  Q("Complétez : « The picture is ___ the wall. »", ["on", "in", "at", "under"], "on", "On = sur (une surface)."),
  Q("Complétez : « She is waiting ___ the bus stop. »", ["at", "in", "on", "into"], "at", "At = à (un point précis)."),
  Q("Complétez : « My keys are ___ my bag. »", ["in", "on", "at", "over"], "in", "In = dans."),
]),
notion('OG-4', 0, F, 'anggr-adverbes-temps', [
  Q("Que signifie « already » ?", ["Déjà", "Encore", "Toujours", "Bientôt"], "Déjà", "I've already finished."),
  Q("Que signifie « yet » dans une question au present perfect ?", ["Déjà", "Jamais", "Encore", "Toujours"], "Déjà", "Have you finished yet? / I haven't finished yet (pas encore)."),
  Q("Que signifie « soon » ?", ["Bientôt", "Tôt", "Tard", "Souvent"], "Bientôt", "See you soon!"),
]),
notion('OG-4', 0, F, 'anggr-adverbes-maniere', [
  Q("Quel est l'adverbe de « quick » ?", ["Quickly", "Quickely", "Quickfully", "Quick"], "Quickly", "On ajoute -ly."),
  Q("Quel est l'adverbe de « good » ?", ["Well", "Goodly", "Good", "Better"], "Well", "She sings well."),
  Q("Quel est l'adverbe de « fast » ?", ["Fast", "Fastly", "Fastily", "Faster"], "Fast", "He runs fast."),
]),
notion('OG-4', 0, I, 'anggr-ago-since-for', [
  Q("Complétez : « I arrived two hours ___. »", ["ago", "since", "for", "before"], "ago", "Ago + prétérit."),
  Q("Complétez : « I've been waiting ___ two hours. »", ["for", "since", "ago", "during"], "for", "For + durée."),
  Q("Complétez : « I've lived here ___ I was five. »", ["since", "for", "ago", "from"], "since", "Since + point de départ."),
]),
notion('OG-4', 0, I, 'anggr-during-while', [
  Q("Complétez : « I fell asleep ___ the film. »", ["during", "while", "for", "since"], "during", "During + nom."),
  Q("Complétez : « I fell asleep ___ I was watching the film. »", ["while", "during", "for", "since"], "while", "While + proposition."),
  Q("Complétez : « We stayed in Rome ___ a week. »", ["for", "during", "while", "since"], "for", "For + durée."),
]),
notion('OG-4', 0, I, 'anggr-prepositions-mouvement', [
  Q("Complétez : « The cat jumped ___ the wall. »", ["over", "under", "through", "into"], "over", "Over = par-dessus."),
  Q("Complétez : « They walked ___ the forest. »", ["through", "over", "on", "at"], "through", "Through = à travers."),
  Q("Complétez : « She ran ___ the room. » (entrer)", ["into", "in", "at", "on"], "into", "Into = dans (avec mouvement)."),
]),
notion('OG-4', 0, I, 'anggr-until-by', [
  Q("Complétez : « The shop is open ___ 8 p.m. » (jusqu'à)", ["until", "by", "since", "for"], "until", "Until = jusqu'à."),
  Q("Complétez : « Please finish ___ Friday. » (au plus tard)", ["by", "until", "since", "for"], "by", "By = d'ici, au plus tard."),
  Q("Complétez : « I'll wait ___ you come back. »", ["until", "by", "during", "for"], "until", "Until + proposition."),
]),
notion('OG-4', 0, I, 'anggr-place-adverbes', [
  Q("Où se place « often » dans « She ___ is late » ?", ["Après be : She is often late.", "Avant be : She often is late.", "En fin : She is late often only.", "Au début obligatoirement"], "Après be : She is often late.", "Avant le verbe, après be."),
  Q("Quelle phrase est correcte ?", ["I speak English very well.", "I speak very well English.", "I very well speak English.", "Very well I speak English."], "I speak English very well.", "Pas d'adverbe entre le verbe et son complément."),
  Q("Où se place généralement un complément de temps comme « yesterday » ?", ["En fin de phrase (ou au début)", "Entre le sujet et le verbe", "Entre le verbe et le complément", "Jamais dans la phrase"], "En fin de phrase (ou au début)", "I saw him yesterday."),
]),
notion('OG-4', 0, I, 'anggr-heure-prepositions', [
  Q("Complétez : « I was born ___ 15th May. »", ["on", "in", "at", "by"], "on", "On + date précise."),
  Q("Complétez : « We go skiing ___ winter. »", ["in", "on", "at", "during the"], "in", "In + saison."),
  Q("Complétez : « I'll call you ___ the weekend. » (GB)", ["at", "in", "on the", "by"], "at", "At the weekend (GB), on the weekend (US)."),
]),
notion('OG-4', 0, I, 'anggr-adverbes-degre', [
  Q("Que signifie « quite » dans « It's quite good » ?", ["Assez", "Très", "Pas du tout", "Trop"], "Assez", "Quite = assez, plutôt."),
  Q("Que signifie « too » dans « It's too hot » ?", ["Trop", "Aussi", "Très", "Assez"], "Trop", "Too = trop (ou aussi en fin de phrase)."),
  Q("Complétez : « He isn't old ___ to drive. »", ["enough", "too", "very", "so"], "enough", "Enough se place après l'adjectif."),
]),
notion('OG-4', 0, I, 'anggr-ago-before-later', [
  Q("Complétez : « Three days ___, she called me again. » (plus tard)", ["later", "ago", "before", "since"], "later", "Later = plus tard."),
  Q("Complétez : « I had met him two years ___. » (auparavant, dans un récit passé)", ["before", "ago", "later", "since"], "before", "Before (ou earlier) avec le past perfect."),
  Q("Que signifie « the day after tomorrow » ?", ["Après-demain", "Avant-hier", "Demain", "Hier"], "Après-demain", "The day before yesterday = avant-hier."),
]),
notion('OG-4', 0, D, 'anggr-adverbes-phrase', [
  Q("Que signifie « Hopefully, it will stop raining » ?", ["Espérons qu'il arrête de pleuvoir", "Il pleut avec espoir", "Il a arrêté de pleuvoir", "Il pleuvra sûrement"], "Espérons qu'il arrête de pleuvoir", "Adverbe de phrase."),
  Q("Que signifie « Apparently, he's moving to Canada » ?", ["Apparemment, il déménage au Canada", "Évidemment, il déménage", "Il est apparu au Canada", "Il ne déménage pas"], "Apparemment, il déménage au Canada", "Apparently = à ce qu'il paraît."),
  Q("Que signifie « Unfortunately » ?", ["Malheureusement", "Heureusement", "Fortement", "Inévitablement"], "Malheureusement", "Fortunately = heureusement."),
]),
notion('OG-4', 0, D, 'anggr-inversion-adverbes', [
  Q("Complétez : « Never ___ such a beautiful sunset. »", ["have I seen", "I have seen", "I saw", "saw I"], "have I seen", "Inversion après un adverbe négatif en tête."),
  Q("Complétez : « Hardly ___ arrived when it started to rain. »", ["had we", "we had", "we have", "did we have"], "had we", "Hardly… when… = à peine… que…"),
  Q("Complétez : « Not only ___ late, but he also forgot his book. »", ["was he", "he was", "he is", "is he being"], "was he", "Not only… but also…"),
]),
notion('OG-4', 0, D, 'anggr-prepositions-avancees', [
  Q("Complétez : « The village lies ___ the mountains and the sea. »", ["between", "among", "amid", "across"], "between", "Between = entre deux éléments."),
  Q("Complétez : « She was ___ the crowd. » (parmi)", ["among", "between", "through", "beyond"], "among", "Among = parmi."),
  Q("Complétez : « The lake is ___ those hills. » (au-delà de)", ["beyond", "behind only", "among", "between"], "beyond", "Beyond = au-delà de."),
]),
notion('OG-4', 0, D, 'anggr-temps-subordonnees', [
  Q("Complétez : « I'll call you when I ___ home. »", ["get", "will get", "got", "am going to get"], "get", "Pas de will après when (futur)."),
  Q("Complétez : « As soon as she ___, we'll start. »", ["arrives", "will arrive", "arrived", "arriving"], "arrives", "As soon as + présent pour le futur."),
  Q("Complétez : « Wait here until I ___ back. »", ["come", "will come", "came", "coming"], "come", "Until + présent."),
]),
notion('OG-4', 0, D, 'anggr-hard-hardly', [
  Q("Que signifie « He works hard » ?", ["Il travaille dur", "Il travaille à peine", "Il travaille difficilement", "Il travaille peu"], "Il travaille dur", "Hard est adjectif et adverbe."),
  Q("Que signifie « He hardly works » ?", ["Il travaille à peine", "Il travaille dur", "Il travaille durement", "Il travaille toujours"], "Il travaille à peine", "Hardly = à peine."),
  Q("Que signifie « lately » ?", ["Récemment, ces derniers temps", "Tardivement", "En retard", "Lentement"], "Récemment, ces derniers temps", "Late = en retard."),
]),
notion('OG-4', 0, D, 'anggr-reperes-temporels-recit', [
  Q("Au discours indirect, que devient « yesterday » ?", ["The day before (the previous day)", "Yesterday", "Today", "The next day"], "The day before (the previous day)", "Les repères temporels changent."),
  Q("Au discours indirect, que devient « here » ?", ["There", "Here", "Where", "Hereby"], "There", "This devient that."),
  Q("Au discours indirect, que devient « next week » ?", ["The following week", "Last week", "This week", "The week before"], "The following week", "Next week → the following week."),
]),
notion('OG-4', 0, D, 'anggr-at-in-on-lieux', [
  Q("Complétez : « She lives ___ 10 Downing Street. »", ["at", "in", "on", "by"], "at", "At + adresse précise."),
  Q("Complétez : « He lives ___ Oxford Street. »", ["on (US) / in (GB)", "at", "by", "into"], "on (US) / in (GB)", "On + nom de rue, en anglais américain surtout."),
  Q("Complétez : « They live ___ the third floor. »", ["on", "in", "at", "over"], "on", "On + étage."),
]),
notion('OG-4', 0, D, 'anggr-adverbes-ordre', [
  Q("Quel est l'ordre habituel des compléments en fin de phrase ?", ["Manière, lieu, temps : He worked hard at school yesterday.", "Temps, lieu, manière", "Lieu, temps, manière", "Il n'y a pas d'ordre"], "Manière, lieu, temps : He worked hard at school yesterday.", "Moyen mnémotechnique : MLT."),
  Q("Quelle phrase est correcte ?", ["She went to London by train last year.", "She went last year by train to London.", "She went by train last year London to.", "She last year went to London by train."], "She went to London by train last year.", "Lieu, moyen, temps."),
  Q("Où se place « still » dans « He ___ lives in Paris » ?", ["Avant le verbe : He still lives in Paris.", "En fin de phrase uniquement", "Après le verbe : He lives still", "Au début obligatoirement"], "Avant le verbe : He still lives in Paris.", "Still = toujours, encore."),
]),
# ══ OG-5 · La phrase et son organisation ══
notion('OG-4', 0, D, 'anggr-prepositions-verbes', [
  Q("Complétez : « It depends ___ the weather. »", ["on", "of", "from", "at"], "on", "Depend on."),
  Q("Complétez : « She is afraid ___ spiders. »", ["of", "from", "about", "with"], "of", "Be afraid of."),
  Q("Complétez : « I'm looking forward ___ the holidays. »", ["to", "for", "at", "on"], "to", "Look forward to."),
]),
notion('OG-5', 0, F, 'anggr-ordre-phrase', [
  Q("Quel est l'ordre normal d'une phrase affirmative anglaise ?", ["Sujet + verbe + complément", "Verbe + sujet + complément", "Complément + sujet + verbe", "Sujet + complément + verbe"], "Sujet + verbe + complément", "I like music."),
  Q("Quelle phrase est correcte ?", ["I play football on Saturdays.", "I football play on Saturdays.", "Play I football on Saturdays.", "On Saturdays football I play."], "I play football on Saturdays.", "SVO."),
  Q("Quelle phrase est correcte ?", ["She has a red car.", "She has a car red.", "She a red car has.", "Red car she has."], "She has a red car.", "L'adjectif précède le nom."),
]),
notion('OG-5', 0, F, 'anggr-negation', [
  Q("Quelle est la forme négative de « They live in London » ?", ["They don't live in London.", "They doesn't live in London.", "They not live in London.", "They live not in London."], "They don't live in London.", "Don't + base verbale."),
  Q("Quelle est la forme négative de « We are tired » ?", ["We aren't tired.", "We don't tired.", "We not are tired.", "We doesn't tired."], "We aren't tired.", "Avec be, on ajoute not."),
  Q("Quelle est la forme négative de « She went out » ?", ["She didn't go out.", "She didn't went out.", "She not went out.", "She wasn't go out."], "She didn't go out.", "Didn't + base verbale."),
]),
notion('OG-5', 0, F, 'anggr-questions-fermees', [
  Q("Quelle question est correcte ?", ["Do you like pizza?", "You like pizza?", "Like you pizza?", "Are you like pizza?"], "Do you like pizza?", "Do + sujet + verbe."),
  Q("Quelle réponse courte convient à « Is she your sister? » ?", ["Yes, she is.", "Yes, she does.", "Yes, she's.", "Yes, is she."], "Yes, she is.", "On reprend l'auxiliaire."),
  Q("Quelle réponse courte convient à « Did you finish? » ?", ["No, I didn't.", "No, I don't.", "No, I wasn't.", "No, I didn't finish not."], "No, I didn't.", "On reprend did."),
]),
notion('OG-5', 0, F, 'anggr-imperatif', [
  Q("Comment donne-t-on un ordre en anglais ?", ["Avec la base verbale : Sit down!", "Avec to : To sit down!", "Avec -ing : Sitting down!", "Avec le sujet : You sit down obligatoirement"], "Avec la base verbale : Sit down!", "L'impératif n'a pas de sujet exprimé."),
  Q("Comment dit-on « Ne touche pas ! » ?", ["Don't touch!", "Not touch!", "No touch!", "Touch not!"], "Don't touch!", "Don't + base verbale."),
  Q("Comment dit-on « Allons-y ! » ?", ["Let's go!", "We go!", "Go us!", "Let go!"], "Let's go!", "Let's = let us."),
]),
notion('OG-5', 0, F, 'anggr-conjonctions-simples', [
  Q("Que signifie « but » ?", ["Mais", "Et", "Ou", "Donc"], "Mais", "And = et, or = ou, so = donc."),
  Q("Complétez : « I was tired, ___ I went to bed. »", ["so", "but", "or", "because"], "so", "So exprime la conséquence."),
  Q("Complétez : « Do you want tea ___ coffee? »", ["or", "and", "but", "so"], "or", "Or = ou."),
]),
notion('OG-5', 0, F, 'anggr-exclamations-simples', [
  Q("Complétez : « ___ a nice day! »", ["What", "How", "So", "Such"], "What", "What + a + adjectif + nom."),
  Q("Complétez : « ___ cold it is! »", ["How", "What", "Such", "Very"], "How", "How + adjectif."),
  Q("Complétez : « It's ___ a good book! »", ["such", "so", "how", "what"], "such", "Such + a + adjectif + nom."),
]),
notion('OG-5', 0, F, 'anggr-because-so', [
  Q("Complétez : « I'm happy ___ it's my birthday. »", ["because", "so", "but", "or"], "because", "Because = parce que."),
  Q("Quelle question demande une cause ?", ["Why are you sad?", "Where are you sad?", "When are you sad?", "Who are you sad?"], "Why are you sad?", "Réponse : Because…"),
  Q("Complétez : « It was raining, ___ we stayed inside. »", ["so", "because", "but", "if"], "so", "Conséquence."),
]),
notion('OG-5', 0, F, 'anggr-ordre-question-wh', [
  Q("Quelle question est correcte ?", ["Where do you live?", "Where you live?", "Where live you?", "Where does you live?"], "Where do you live?", "Mot interrogatif + auxiliaire + sujet + verbe."),
  Q("Quelle question est correcte ?", ["What are you doing?", "What you are doing?", "What doing you are?", "What do you doing?"], "What are you doing?", "Inversion de be."),
  Q("Quelle question est correcte ?", ["When did she arrive?", "When she arrived?", "When did she arrived?", "When arrived she?"], "When did she arrive?", "Did + base verbale."),
]),
notion('OG-5', 0, I, 'anggr-subordonnees-but', [
  Q("Complétez : « I'm saving money ___ buy a bike. »", ["to", "for", "for to", "so"], "to", "To + base verbale = pour."),
  Q("Complétez : « He spoke slowly ___ everybody could understand. »", ["so that", "because", "although", "unless"], "so that", "So that = afin que."),
  Q("Complétez : « She took an umbrella ___ case it rained. »", ["in", "for", "by", "on"], "in", "In case = au cas où."),
]),
notion('OG-5', 0, I, 'anggr-questions-indirectes', [
  Q("Quelle question indirecte est correcte ?", ["Can you tell me where the station is?", "Can you tell me where is the station?", "Can you tell me where does the station is?", "Can you tell me the station where is?"], "Can you tell me where the station is?", "Pas d'inversion dans une question indirecte."),
  Q("Complétez : « I wonder ___ she will come. »", ["if", "that", "what if", "does"], "if", "If / whether = si."),
  Q("Quelle phrase est correcte ?", ["I don't know what time it is.", "I don't know what time is it.", "I don't know what is the time it.", "I don't know it is what time."], "I don't know what time it is.", "Ordre affirmatif après le mot interrogatif."),
]),
notion('OG-5', 0, I, 'anggr-concession', [
  Q("Complétez : « ___ it was raining, we went for a walk. »", ["Although", "Because", "So", "Unless"], "Although", "Although = bien que."),
  Q("Complétez : « ___ the rain, we went for a walk. »", ["Despite", "Although", "Even", "However"], "Despite", "Despite + nom."),
  Q("Complétez : « He's rich. ___, he isn't happy. »", ["However", "Although", "Despite", "Because"], "However", "However en début de phrase, suivi d'une virgule."),
]),
notion('OG-5', 0, I, 'anggr-relatives-structure', [
  Q("Quelle phrase réunit correctement les deux idées : « I have a friend. She lives in Dublin. » ?", ["I have a friend who lives in Dublin.", "I have a friend which lives in Dublin.", "I have a friend lives in Dublin.", "I have a friend she lives in Dublin."], "I have a friend who lives in Dublin.", "Who pour une personne."),
  Q("Quelle phrase réunit : « This is the book. I told you about it. » ?", ["This is the book I told you about.", "This is the book I told you about it.", "This is the book who I told you about.", "This is the book what I told you."], "This is the book I told you about.", "On ne répète pas le pronom."),
  Q("Quelle phrase est correcte ?", ["The town where I was born is small.", "The town which I was born is small.", "The town where I was born in it is small.", "The town I was born where is small."], "The town where I was born is small.", "Where pour un lieu."),
]),
notion('OG-5', 0, D, 'anggr-conditionnels-mixtes', [
  Q("Complétez : « If I had studied harder, I ___ a better job now. »", ["would have", "would have had", "will have", "had"], "would have", "Conditionnel mixte : condition passée, conséquence présente."),
  Q("Complétez : « ___ I known, I would have helped you. »", ["Had", "If", "Have", "Should"], "Had", "Inversion = If I had known."),
  Q("Complétez : « Provided that you ___ hard, you'll pass. »", ["work", "will work", "worked", "working"], "work", "Provided that = à condition que."),
]),
notion('OG-5', 0, D, 'anggr-participiales', [
  Q("Que signifie « Having finished his homework, he went out » ?", ["Après avoir fini ses devoirs, il est sorti", "Il finit ses devoirs en sortant", "Il n'a pas fini ses devoirs", "Il sortira après ses devoirs"], "Après avoir fini ses devoirs, il est sorti", "Proposition participiale."),
  Q("Complétez : « ___ the door, she saw a stranger. » (en ouvrant)", ["Opening", "Opened", "To open", "Open"], "Opening", "Participe présent : simultanéité."),
  Q("Que signifie « Built in 1890, the bridge is still used today » ?", ["Construit en 1890, le pont est toujours utilisé", "On construit le pont en 1890", "Le pont sera construit", "Le pont a été détruit"], "Construit en 1890, le pont est toujours utilisé", "Participe passé à valeur passive."),
]),
notion('OG-5', 0, D, 'anggr-cleft-emphase', [
  Q("Complétez : « It was in 1066 ___ William invaded England. »", ["that", "which", "who", "what"], "that", "It was… that… : mise en relief."),
  Q("Que met en relief « What I need is a holiday » ?", ["Des vacances (ce dont j'ai besoin)", "Le besoin en général", "Le travail", "Rien"], "Des vacances (ce dont j'ai besoin)", "Pseudo-clivée avec what."),
  Q("Complétez : « All I want ___ some peace. »", ["is", "are", "be", "being"], "is", "All I want is… = Tout ce que je veux, c'est…"),
]),
notion('OG-5', 0, D, 'anggr-subjonctif', [
  Q("Complétez : « The teacher insisted that he ___ the test again. »", ["take", "takes", "took", "will take"], "take", "Subjonctif après insist, suggest, demand."),
  Q("Complétez : « It is essential that everyone ___ on time. »", ["be", "is", "was", "being"], "be", "Subjonctif présent : base verbale."),
  Q("Complétez : « I suggest that she ___ a doctor. »", ["see", "sees", "saw", "to see"], "see", "Ou : I suggest she should see a doctor."),
]),
notion('OG-5', 0, D, 'anggr-causatif-structures', [
  Q("Complétez : « I'm going to have my car ___ tomorrow. » (repair)", ["repaired", "repair", "repairing", "to repair"], "repaired", "Have + objet + participe passé : faire faire."),
  Q("Complétez : « She got her brother ___ her with the boxes. »", ["to help", "help", "helping", "helped"], "to help", "Get + personne + to : persuader quelqu'un de faire."),
  Q("Complétez : « The film made me ___. »", ["cry", "to cry", "crying", "cried"], "cry", "Make + personne + base verbale."),
]),
notion('OG-5', 0, D, 'anggr-ellipses', [
  Q("Complétez : « She can swim, and so ___ I. »", ["can", "do", "am", "will"], "can", "On reprend l'auxiliaire."),
  Q("Complétez : « I haven't seen it, and neither ___ Tom. »", ["has", "have", "did", "does"], "has", "Neither + auxiliaire + sujet."),
  Q("Complétez : « He said he'd call, but he ___. »", ["didn't", "wasn't", "hasn't", "doesn't"], "didn't", "On évite de répéter le verbe."),
]),
]

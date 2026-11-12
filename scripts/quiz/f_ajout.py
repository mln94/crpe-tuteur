# Français : 100 questions ajoutées (25 par thème : culture littéraire et artistique, lecture,
# vocabulaire et orthographe lexicale, grammaire et orthographe grammaticale), programme du cycle 4
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── Culture littéraire et artistique ──
notion('F13', 2, F, 'f-cla-moliere', [
  Q("Dans quelle comédie de Molière Harpagon s'écrie-t-il « Au voleur ! au voleur ! » ?", ["L'Avare", "Le Malade imaginaire", "Les Fourberies de Scapin", "Le Bourgeois gentilhomme"], "L'Avare", "Harpagon, obsédé par son argent, croit qu'on lui a volé sa cassette."),
  Q("Dans « Le Bourgeois gentilhomme », que découvre M. Jourdain avec son maître de philosophie ?", ["Qu'il fait de la prose sans le savoir", "Qu'il est noble", "Qu'il sait chanter", "Qu'il est malade"], "Qu'il fait de la prose sans le savoir", "« Par ma foi ! il y a plus de quarante ans que je dis de la prose sans que j'en susse rien. »"),
  Q("Quelle formule latine résume l'ambition de la comédie classique ?", ["Castigat ridendo mores (elle corrige les mœurs en riant)", "Carpe diem", "Veni, vidi, vici", "Memento mori"], "Castigat ridendo mores (elle corrige les mœurs en riant)", "Molière fait rire des travers de la société pour mieux les dénoncer."),
]),
notion('F13', 3, F, 'f-cla-contes-recits', [
  Q("Qui a écrit les « Contes de ma mère l'Oye » (1697), dont « Le Petit Chaperon rouge » ?", ["Charles Perrault", "Les frères Grimm", "Hans Christian Andersen", "Jean de La Fontaine"], "Charles Perrault", "Chaque conte de Perrault se termine par une moralité en vers."),
  Q("Qui a écrit « La Petite Sirène » et « Le Vilain Petit Canard » ?", ["Hans Christian Andersen", "Charles Perrault", "Les frères Grimm", "Madame d'Aulnoy"], "Hans Christian Andersen", "Andersen est un écrivain danois du XIXe siècle."),
  Q("Quel recueil de contes orientaux est raconté par Shéhérazade ?", ["Les Mille et Une Nuits", "Le Roman de Renart", "Les Fables d'Ésope", "Le Décaméron"], "Les Mille et Une Nuits", "Shéhérazade suspend chaque nuit son récit pour échapper à la mort."),
]),
notion('F13', 1, F, 'f-cla-poesie-monde', [
  Q("Quel poète du XXe siècle a écrit « La Prose du Transsibérien » et « Du monde entier » ?", ["Blaise Cendrars", "Victor Hugo", "Joachim du Bellay", "Jean de La Fontaine"], "Blaise Cendrars", "L'intitulé de programme « Du monde entier au cœur du monde » reprend des titres de Cendrars."),
  Q("Qui a écrit « Les Contemplations » et « Demain, dès l'aube… » ?", ["Victor Hugo", "Arthur Rimbaud", "Paul Verlaine", "Charles Baudelaire"], "Victor Hugo", "Dans « Demain, dès l'aube… », le poète se rend sur la tombe de sa fille Léopoldine."),
  Q("Quel poète a composé des « Calligrammes », poèmes dont les mots dessinent une forme ?", ["Guillaume Apollinaire", "Pierre de Ronsard", "Jean Racine", "Alfred de Vigny"], "Guillaume Apollinaire", "Le recueil « Calligrammes » paraît en 1918."),
]),
notion('F14', 0, I, 'f-cla-fiction-limites', [
  Q("Dans « Le Horla » de Maupassant, de quoi le narrateur se croit-il victime ?", ["D'un être invisible qui le hante", "D'un naufrage", "D'une guerre", "D'un voleur de bijoux"], "D'un être invisible qui le hante", "Le doute entre explication rationnelle et surnaturelle est caractéristique du fantastique."),
  Q("Quel roman de Jules Verne raconte les aventures du capitaine Nemo à bord du Nautilus ?", ["Vingt Mille Lieues sous les mers", "Le Tour du monde en quatre-vingts jours", "Voyage au centre de la Terre", "De la Terre à la Lune"], "Vingt Mille Lieues sous les mers", "Le roman paraît en 1869-1870 ; il mêle aventure et anticipation scientifique."),
  Q("Quel roman de H. G. Wells imagine une invasion de la Terre par des Martiens ?", ["La Guerre des mondes", "L'Île du docteur Moreau", "Frankenstein", "1984"], "La Guerre des mondes", "« Frankenstein » est de Mary Shelley, « 1984 » de George Orwell."),
]),
notion('F14', 2, I, 'f-cla-conflits-scene', [
  Q("Dans « Le Cid » de Corneille, quel dilemme Rodrigue doit-il affronter ?", ["Venger l'honneur de son père ou garder l'amour de Chimène", "Partir en voyage ou rester", "Devenir roi ou moine", "Écrire ou se battre"], "Venger l'honneur de son père ou garder l'amour de Chimène", "On parle de « dilemme cornélien » : un choix déchirant entre devoir et passion."),
  Q("Dans « Antigone », pourquoi l'héroïne désobéit-elle au roi Créon ?", ["Pour donner une sépulture à son frère Polynice", "Pour prendre le pouvoir", "Pour épouser un étranger", "Pour fuir Thèbes"], "Pour donner une sépulture à son frère Polynice", "Le mythe a été repris par Sophocle puis par Jean Anouilh (1944)."),
  Q("Quel dramaturge du XVIIe siècle a écrit les tragédies « Phèdre » et « Andromaque » ?", ["Jean Racine", "Molière", "Pierre de Marivaux", "Edmond Rostand"], "Jean Racine", "La tragédie classique respecte la règle des trois unités : temps, lieu, action."),
]),
notion('F14', 3, I, 'f-cla-contes-philosophiques', [
  Q("Quel conte philosophique de Voltaire se moque de l'optimisme de Pangloss ?", ["Candide", "Les Lettres persanes", "Le Contrat social", "Les Misérables"], "Candide", "« Il faut cultiver notre jardin » : c'est la leçon finale de Candide."),
  Q("Dans les « Lettres persanes » (1721), qui observe et critique la société française ?", ["Deux voyageurs persans, Usbek et Rica", "Un enfant", "Un roi", "Un animal qui parle"], "Deux voyageurs persans, Usbek et Rica", "Montesquieu utilise le regard étranger pour faire la satire de la France."),
  Q("Quel ouvrage collectif dirigé par Diderot et d'Alembert symbolise les Lumières ?", ["L'Encyclopédie", "La Bible", "Les Essais", "Le Discours de la méthode"], "L'Encyclopédie", "Elle veut rassembler et diffuser les connaissances pour éclairer les esprits."),
]),
notion('F15', 0, D, 'f-cla-recits-guerre', [
  Q("Qui a écrit « Si c'est un homme », témoignage sur sa déportation à Auschwitz ?", ["Primo Levi", "Albert Camus", "Romain Gary", "Joseph Kessel"], "Primo Levi", "Chimiste italien, il témoigne en 1947 de l'expérience des camps."),
  Q("Quel roman d'Erich Maria Remarque décrit la vie des soldats allemands dans les tranchées de 1914-1918 ?", ["À l'ouest, rien de nouveau", "Le Feu", "Les Croix de bois", "Voyage au bout de la nuit"], "À l'ouest, rien de nouveau", "« Le Feu » est d'Henri Barbusse et « Les Croix de bois » de Roland Dorgelès : deux témoignages français."),
  Q("Quel journal intime d'une adolescente cachée à Amsterdam pendant la Seconde Guerre mondiale est devenu un témoignage majeur ?", ["Le Journal d'Anne Frank", "Le Journal de Jules Renard", "Les Mémoires d'outre-tombe", "Le Petit Prince"], "Le Journal d'Anne Frank", "Anne Frank meurt en déportation en 1945 ; son père fait publier son journal en 1947."),
]),
notion('F15', 3, D, 'f-cla-engagement', [
  Q("Quel écrivain publie « J'accuse… ! » en 1898 pour défendre le capitaine Dreyfus ?", ["Émile Zola", "Victor Hugo", "Voltaire", "Albert Camus"], "Émile Zola", "La lettre ouverte au président de la République paraît dans le journal L'Aurore."),
  Q("Quel écrivain a défendu Jean Calas et écrit le « Traité sur la tolérance » (1763) ?", ["Voltaire", "Rousseau", "Montesquieu", "Diderot"], "Voltaire", "Calas, protestant, avait été injustement exécuté ; Voltaire obtient sa réhabilitation."),
  Q("Quel roman de Victor Hugo s'attaque à la peine de mort ?", ["Le Dernier Jour d'un condamné", "Notre-Dame de Paris", "Les Contemplations", "Ruy Blas"], "Le Dernier Jour d'un condamné", "Hugo y donne la parole à un condamné dans ses dernières heures (1829)."),
  Q("Quel poème de Paul Éluard, parachuté par les avions alliés en 1942, célèbre un mot répété à la fin de chaque strophe ?", ["Liberté (« J'écris ton nom »)", "Le Pont Mirabeau", "Le Dormeur du val", "Booz endormi"], "Liberté (« J'écris ton nom »)", "C'est un poème de la Résistance ; « Le Dormeur du val » est un poème de Rimbaud contre la guerre de 1870."),
]),
# ── Lecture ──
notion('F1', 5, F, 'f-lec-incipit', [
  Q("Comment appelle-t-on le début d'un roman ?", ["L'incipit", "L'excipit", "Le dénouement", "La chute"], "L'incipit", "L'incipit présente souvent les personnages, le lieu et l'époque, et donne envie de lire."),
  Q("Comment appelle-t-on la fin d'un roman ?", ["L'excipit", "L'incipit", "Le prologue", "La préface"], "L'excipit", "On étudie souvent l'incipit et l'excipit en miroir."),
  Q("Quelle est la fonction principale d'un incipit ?", ["Informer le lecteur et éveiller son intérêt", "Résumer toute l'histoire", "Donner la morale", "Présenter l'auteur"], "Informer le lecteur et éveiller son intérêt", "Il pose le cadre du récit et crée des attentes chez le lecteur."),
]),
notion('F3', 1, I, 'f-lec-types-textes', [
  Q("« Fais chauffer l'eau, verse la farine, mélange pendant deux minutes. » Quel est le type de ce texte ?", ["Injonctif (prescriptif)", "Narratif", "Descriptif", "Argumentatif"], "Injonctif (prescriptif)", "Il donne des instructions, souvent à l'impératif ou à l'infinitif."),
  Q("Un texte cherche à défendre une opinion avec des arguments. De quel type est-il ?", ["Argumentatif", "Narratif", "Descriptif", "Explicatif"], "Argumentatif", "Il vise à convaincre ou à persuader."),
  Q("« Les volcans se forment lorsque le magma remonte à la surface de la Terre. » Quel est le type de ce texte ?", ["Explicatif", "Narratif", "Argumentatif", "Injonctif"], "Explicatif", "Il répond à une question (comment ? pourquoi ?) pour faire comprendre un phénomène."),
]),
notion('F8', 3, I, 'f-lec-formes-poetiques', [
  Q("Comment s'appellent les deux strophes de trois vers qui terminent un sonnet ?", ["Des tercets", "Des quatrains", "Des distiques", "Des quintils"], "Des tercets", "Un sonnet compte deux quatrains puis deux tercets : 4 + 4 + 3 + 3 = 14 vers."),
  Q("Quel petit poème d'origine japonaise compte trois vers (souvent 5, 7 et 5 syllabes) ?", ["Le haïku", "Le sonnet", "La ballade", "Le rondeau"], "Le haïku", "Le haïku saisit un instant, souvent lié à la nature et aux saisons."),
  Q("Comment appelle-t-on un poème écrit sans vers, en paragraphes ?", ["Un poème en prose", "Un calligramme", "Un sonnet", "Une ode"], "Un poème en prose", "Baudelaire en a écrit dans « Le Spleen de Paris »."),
]),
notion('F12', 0, D, 'f-lec-figures-de-son', [
  Q("« Pour qui sont ces serpents qui sifflent sur vos têtes ? » (Racine). Quelle figure de style repose sur la répétition du son [s] ?", ["Une allitération", "Une assonance", "Une anaphore", "Une métaphore"], "Une allitération", "L'allitération répète un son consonne ; ici, elle imite le sifflement des serpents."),
  Q("Comment s'appelle la répétition d'un même son voyelle dans un vers ?", ["Une assonance", "Une allitération", "Une rime", "Une antithèse"], "Une assonance", "Exemple : « Tout m'afflige et me nuit et conspire à me nuire » répète le son [i]."),
  Q("Quelle figure de son consiste à imiter un bruit par un mot (« boum », « tic-tac ») ?", ["L'onomatopée", "L'allitération", "La périphrase", "L'oxymore"], "L'onomatopée", "Les onomatopées sont fréquentes en bande dessinée et en poésie."),
]),
notion('F1', 5, F, 'f-lec-description', [
  Q("À quoi sert principalement une description dans un récit ?", ["À faire voir un lieu ou un personnage et à créer une atmosphère", "À faire avancer rapidement l'action", "À donner la morale", "À rapporter un dialogue"], "À faire voir un lieu ou un personnage et à créer une atmosphère", "La description fait une pause dans l'action ; elle peut aussi annoncer la suite."),
  Q("Quel temps est le plus souvent employé pour la description dans un récit au passé ?", ["L'imparfait", "Le passé simple", "Le futur", "Le présent de l'impératif"], "L'imparfait", "L'imparfait sert à l'arrière-plan ; le passé simple, aux actions de premier plan."),
  Q("Comment appelle-t-on la description physique et morale d'un personnage ?", ["Un portrait", "Un dialogue", "Un monologue", "Un résumé"], "Un portrait", "Le portrait peut être élogieux ou satirique."),
]),
notion('F7', 1, F, 'f-lec-quete-personnage', [
  Q("Dans un conte, comment appelle-t-on le personnage qui aide le héros dans sa quête ?", ["L'adjuvant", "L'opposant", "Le destinataire", "Le narrateur"], "L'adjuvant", "Dans le schéma actantiel, l'opposant fait obstacle au héros, l'adjuvant l'aide."),
  Q("Dans un récit, comment appelle-t-on le personnage qui s'oppose au héros ?", ["L'opposant", "L'adjuvant", "Le destinateur", "L'objet"], "L'opposant", "Le loup du « Petit Chaperon rouge » est un opposant."),
  Q("Dans le schéma actantiel, que désigne « l'objet » ?", ["Ce que le héros cherche à obtenir", "Un accessoire du décor", "Le livre lui-même", "Le lieu de l'action"], "Ce que le héros cherche à obtenir", "Par exemple, délivrer une princesse ou retrouver un trésor."),
]),
notion('F3', 1, D, 'f-lec-convaincre-persuader', [
  Q("Quelle est la différence entre convaincre et persuader ?", ["Convaincre s'adresse à la raison, persuader joue sur les émotions", "Ce sont des synonymes parfaits", "Convaincre se fait à l'oral, persuader à l'écrit", "Persuader s'appuie uniquement sur des chiffres"], "Convaincre s'adresse à la raison, persuader joue sur les émotions", "Un texte argumentatif mêle souvent les deux stratégies."),
  Q("« Certes, les écrans sont utiles, mais ils nuisent au sommeil. » Comment appelle-t-on le fait de reconnaître une idée adverse avant de la dépasser ?", ["Une concession", "Une thèse", "Un exemple", "Une hypothèse"], "Une concession", "La concession (« certes…, mais… ») rend l'argumentation plus nuancée et plus convaincante."),
  Q("« Le sport est bon pour la santé : une étude montre que 30 minutes de marche par jour réduisent les maladies cardiaques. » Quel rôle joue la deuxième partie de la phrase ?", ["Un exemple qui illustre l'argument", "La thèse", "Une objection", "Une concession"], "Un exemple qui illustre l'argument", "Un exemple concret rend l'argument plus convaincant."),
]),
notion('F8', 0, I, 'f-lec-procedes-theatre', [
  Q("Au théâtre, comment appelle-t-on une réplique qu'un personnage dit pour lui-même, sans être entendu des autres personnages ?", ["Un aparté", "Un monologue", "Une tirade", "Une didascalie"], "Un aparté", "Le public, lui, entend l'aparté : il en sait plus que les personnages."),
  Q("Comment appelle-t-on un malentendu où l'on prend une personne ou une chose pour une autre ?", ["Un quiproquo", "Un coup de théâtre", "Une exposition", "Un dénouement"], "Un quiproquo", "Le quiproquo est un ressort classique du comique."),
  Q("Comment appelle-t-on un événement inattendu qui change brusquement le cours de l'action ?", ["Un coup de théâtre", "Un aparté", "Une tirade", "Une stichomythie"], "Un coup de théâtre", "Il relance l'intrigue et surprend le spectateur."),
  Q("Comment appelle-t-on un échange rapide de répliques très courtes, souvent d'un vers chacune ?", ["Une stichomythie", "Une tirade", "Un monologue", "Un prologue"], "Une stichomythie", "Elle traduit un affrontement vif entre deux personnages."),
]),
# ── Vocabulaire et orthographe lexicale ──
notion('F37', 1, F, 'f-paronymes', [
  Q("Quel mot convient ? « Le volcan est entré en ……… cette nuit. »", ["éruption", "irruption", "érudition", "éviction"], "éruption", "Éruption (sortie violente de lave) et irruption (entrée brusque) sont des paronymes."),
  Q("Comment appelle-t-on des mots presque identiques par la forme mais de sens différents, comme « éruption » et « irruption » ?", ["Des paronymes", "Des synonymes", "Des antonymes", "Des homonymes"], "Des paronymes", "Une éruption volcanique ; faire irruption dans une pièce."),
  Q("Quel est le bon mot ? « Il a fait ……… dans la salle sans frapper. »", ["irruption", "éruption", "interruption", "érosion"], "irruption", "Faire irruption : entrer brusquement."),
]),
notion('F38', 0, I, 'f-locutions-expressions', [
  Q("Que signifie l'expression « avoir un poil dans la main » ?", ["Être paresseux", "Être malade", "Être très fort", "Être généreux"], "Être paresseux", "C'est une locution figée : son sens ne se déduit pas mot à mot."),
  Q("Que signifie « tomber des nues » ?", ["Être très surpris", "Tomber d'un avion", "S'évanouir", "Être déçu par la météo"], "Être très surpris", "Les nues sont les nuages : on tombe de haut tant la surprise est grande."),
  Q("Que signifie « prendre ses jambes à son cou » ?", ["S'enfuir très vite", "Faire de la gymnastique", "Tomber", "Se reposer"], "S'enfuir très vite", "Les expressions imagées enrichissent l'expression mais relèvent souvent du registre courant ou familier."),
]),
notion('F43', 2, I, 'f-racines-grecques', [
  Q("Que signifie la racine grecque « chrono », présente dans « chronologie » ?", ["Le temps", "La couleur", "La terre", "L'eau"], "Le temps", "Chronomètre, chronique, anachronisme…"),
  Q("Que signifie la racine grecque « hydro » ?", ["L'eau", "Le feu", "L'air", "Le soleil"], "L'eau", "Hydravion, hydrater, déshydratation…"),
  Q("Que désigne le suffixe d'origine grecque « -phobie » (« claustrophobie ») ?", ["La peur", "L'amour", "L'étude", "Le son"], "La peur", "À l'inverse, « -phile » signifie « qui aime » (bibliophile)."),
]),
notion('F43', 2, F, 'f-racines-latines', [
  Q("Que signifie la racine latine « aqua », présente dans « aquarium » ?", ["L'eau", "La terre", "Le ciel", "Le feu"], "L'eau", "Aquatique, aqueduc, aquarelle…"),
  Q("Que signifie l'élément latin « -cide » dans « insecticide » ?", ["Qui tue", "Qui protège", "Qui nourrit", "Qui attire"], "Qui tue", "Pesticide, herbicide, homicide…"),
  Q("Que signifie le préfixe latin « omni- » dans « omnivore » ?", ["Tout", "Rien", "Viande", "Plante"], "Tout", "Un omnivore mange de tout ; un herbivore, de l'herbe ; un carnivore, de la viande."),
]),
notion('F38', 3, F, 'f-hyperonymes', [
  Q("Dans la série « pomme, poire, banane », quel mot est un terme générique (hyperonyme) ?", ["Fruit", "Légume", "Arbre", "Dessert"], "Fruit", "Les mots pomme, poire, banane sont des hyponymes de « fruit »."),
  Q("Quel mot est un hyponyme de « véhicule » ?", ["Bicyclette", "Transport", "Route", "Moteur"], "Bicyclette", "L'hyponyme est plus précis que l'hyperonyme qui l'englobe."),
  Q("Quelle série est rangée du plus général au plus particulier ?", ["animal, mammifère, chien, caniche", "caniche, chien, animal, mammifère", "chien, animal, caniche, mammifère", "mammifère, caniche, animal, chien"], "animal, mammifère, chien, caniche", "On classe les mots selon leur degré de généralité."),
]),
notion('F40', 2, I, 'f-neologismes', [
  Q("Comment appelle-t-on un mot nouvellement créé, comme « courriel » ?", ["Un néologisme", "Un archaïsme", "Un synonyme", "Un paronyme"], "Un néologisme", "« Courriel » a été formé à partir de « courrier électronique »."),
  Q("« Franglais » est formé de « français » et « anglais ». Comment appelle-t-on ce procédé ?", ["Un mot-valise", "Un emprunt", "Une dérivation", "Une abréviation"], "Un mot-valise", "On fusionne le début d'un mot et la fin d'un autre."),
  Q("Le mot « week-end » vient de l'anglais. Comment appelle-t-on ce mode de formation ?", ["Un emprunt", "Une dérivation", "Une composition savante", "Un néologisme de sens"], "Un emprunt", "Le français emprunte à de nombreuses langues : « algèbre » (arabe), « kiosque » (turc)…"),
]),
notion('F48', 2, F, 'f-homophones-lexicaux', [
  Q("Quel mot convient ? « Le ……… et la comtesse donnent un bal dans leur château. »", ["comte", "compte", "conte", "comté"], "comte", "Comte (titre de noblesse), compte (calcul), conte (histoire), comté (territoire)."),
  Q("Quel mot convient ? « Il boit un ……… d'eau. »", ["verre", "vert", "ver", "vers"], "verre", "Verre (récipient), vert (couleur), ver (animal), vers (préposition ou ligne de poème)."),
  Q("Quel mot convient ? « En tombant, il a perdu un peu de ……… . »", ["sang", "sans", "cent", "sent"], "sang", "Sang (liquide), sans (préposition), cent (nombre), sent (verbe sentir) : le contexte permet de choisir."),
]),
notion('F46', 2, F, 'f-regularites-orthographe', [
  Q("Quelle lettre écrit-on devant m, b et p à la place de « n » ?", ["m", "n", "nn", "h"], "m", "On écrit « emporter », « tomber », « imbattable » ; exceptions : « bonbon », « néanmoins », « bonbonne »."),
  Q("Comment écrire le son [ʒ] devant « a » dans « nous man…ons » ?", ["mangeons", "mangons", "manjons", "manguons"], "mangeons", "On ajoute un « e » après le « g » pour garder le son [ʒ] devant a et o."),
  Q("Comment écrire le son [s] devant « o » dans « nous commen…ons » ?", ["commençons", "commenssons", "commencons", "commenzons"], "commençons", "La cédille permet au « c » de garder le son [s] devant a, o, u."),
  Q("Quelle est l'orthographe correcte ?", ["une attention", "une atension", "une attension", "une atention"], "une attention", "Le suffixe « -tion » s'écrit avec un t ; « attention » prend deux t."),
]),
# ── Grammaire et orthographe grammaticale ──
notion('F52', 1, F, 'f-cc-maniere-moyen', [
  Q("« Il a ouvert la porte avec une clé. » Quelle est la fonction de « avec une clé » ?", ["Complément circonstanciel de moyen", "COD", "Complément circonstanciel de lieu", "Complément du nom"], "Complément circonstanciel de moyen", "Il répond à la question « avec quoi ? »."),
  Q("« Elle parle doucement. » Quelle est la fonction de « doucement » ?", ["Complément circonstanciel de manière", "Complément circonstanciel de temps", "Attribut du sujet", "COD"], "Complément circonstanciel de manière", "Il répond à la question « comment ? »."),
  C("Cliquez sur le complément circonstanciel de manière.", "Les enfants traversent la rue [avec prudence] .", "« Avec prudence » indique comment ils traversent."),
]),
notion('F52', 5, F, 'f-pronoms-demonstratifs-indefinis', [
  Q("« Ce livre est le mien ; celui-ci est à toi. » Quelle est la nature de « celui-ci » ?", ["Pronom démonstratif", "Déterminant démonstratif", "Pronom personnel", "Pronom indéfini"], "Pronom démonstratif", "Il remplace un nom (« ce livre-ci ») ; « ce » est un déterminant car il accompagne « livre »."),
  Q("« Personne n'est venu. » Quelle est la nature de « personne » ?", ["Pronom indéfini", "Nom commun", "Pronom personnel", "Adverbe"], "Pronom indéfini", "Ici, « personne » ne désigne aucun être précis ; ce n'est pas le nom « une personne »."),
  C("Cliquez sur le pronom indéfini.", "[Chacun] apporte un gâteau pour la fête .", "« Chacun » désigne de façon imprécise chaque personne d'un ensemble."),
]),
notion('F61', 1, F, 'f-futur-ou-conditionnel', [
  Q("« Je partirai demain. » À quel temps est le verbe ?", ["Futur simple de l'indicatif", "Conditionnel présent", "Imparfait", "Passé simple"], "Futur simple de l'indicatif", "Terminaison -ai au futur, -ais au conditionnel."),
  Q("« Si j'avais le temps, je partirais. » À quel temps est « partirais » ?", ["Conditionnel présent", "Futur simple", "Imparfait", "Subjonctif présent"], "Conditionnel présent", "Le conditionnel se forme sur le radical du futur avec les terminaisons de l'imparfait."),
  Q("Comment distinguer à l'oral « je chanterai » (futur) de « je chanterais » (conditionnel) ?", ["On remplace par « nous » : nous chanterons / nous chanterions", "On ne peut pas", "On met la phrase au passé", "On remplace par « il »"], "On remplace par « nous » : nous chanterons / nous chanterions", "Avec « nous » (ou « tu »), la différence s'entend."),
]),
notion('F62', 4, I, 'f-verbes-irreguliers', [
  Q("Quelle est la forme correcte du verbe « venir » au passé simple, 3e personne du singulier ?", ["il vint", "il venit", "il vena", "il venut"], "il vint", "Venir et tenir ont un passé simple en -in- : il vint, il tint, ils vinrent."),
  Q("Quelle est la forme correcte de « voir » au futur simple, 3e personne du singulier ?", ["il verra", "il voira", "il vera", "il voirra"], "il verra", "Le radical du futur de « voir » est « verr- » : je verrai, il verra."),
  Q("Quelle est la forme correcte de « pouvoir » au présent, 3e personne du pluriel ?", ["ils peuvent", "ils pouvent", "ils peuvont", "ils peuve"], "ils peuvent", "Le radical de « pouvoir » varie : je peux, nous pouvons, ils peuvent."),
]),
notion('F53', 2, I, 'f-cc-opposition-condition', [
  Q("« Bien qu'il pleuve, nous sortirons. » Quelle est la fonction de la subordonnée ?", ["Complément circonstanciel d'opposition (concession)", "Complément circonstanciel de cause", "Complément circonstanciel de temps", "COD"], "Complément circonstanciel d'opposition (concession)", "« Bien que » est suivi du subjonctif."),
  Q("« Si tu travailles, tu réussiras. » Quelle est la fonction de « si tu travailles » ?", ["Complément circonstanciel de condition", "Complément circonstanciel de but", "Complément circonstanciel de cause", "Sujet"], "Complément circonstanciel de condition", "La réussite dépend de la condition exprimée."),
  Q("Quelle conjonction introduit une subordonnée d'opposition ?", ["quoique", "parce que", "afin que", "lorsque"], "quoique", "Parce que : cause ; afin que : but ; lorsque : temps."),
]),
notion('F63', 0, D, 'f-identifier-temps-texte', [
  Q("« Quand il eut fini son repas, il sortit. » À quel temps est « eut fini » ?", ["Passé antérieur", "Plus-que-parfait", "Passé composé", "Futur antérieur"], "Passé antérieur", "Auxiliaire au passé simple + participe passé : il marque une action antérieure à une autre au passé simple."),
  Q("« Elle avait déjà mangé quand nous sommes arrivés. » À quel temps est « avait mangé » ?", ["Plus-que-parfait", "Passé antérieur", "Imparfait", "Conditionnel passé"], "Plus-que-parfait", "Auxiliaire à l'imparfait + participe passé."),
  Q("« Il faut que tu viennes. » À quel temps et mode est « viennes » ?", ["Subjonctif présent", "Indicatif présent", "Impératif présent", "Conditionnel présent"], "Subjonctif présent", "« Il faut que » est toujours suivi du subjonctif."),
]),
notion('F67', 1, F, 'f-accord-attribut', [
  Q("Quelle phrase est correctement accordée ?", ["Les fleurs semblent fanées.", "Les fleurs semblent fané.", "Les fleurs semblent fanés.", "Les fleurs semblent fanée."], "Les fleurs semblent fanées.", "L'attribut du sujet s'accorde avec le sujet « les fleurs » (féminin pluriel)."),
  Q("Quelle phrase est correctement accordée ?", ["Ma sœur et mon frère sont contents.", "Ma sœur et mon frère sont contentes.", "Ma sœur et mon frère sont content.", "Ma sœur et mon frère sont contente."], "Ma sœur et mon frère sont contents.", "Masculin et féminin réunis : l'accord se fait au masculin pluriel."),
  C("Cliquez sur l'attribut du sujet.", "Ces exercices paraissent [faciles] .", "« Paraître » est un verbe attributif : « faciles » s'accorde avec « exercices »."),
]),
notion('F49', 6, I, 'f-reprises-anaphoriques', [
  Q("« Le chat entra. L'animal semblait affamé. » Comment appelle-t-on la reprise « l'animal » ?", ["Une reprise nominale (par un terme générique)", "Une reprise pronominale", "Une répétition", "Un connecteur"], "Une reprise nominale (par un terme générique)", "Varier les reprises évite les répétitions et assure la cohérence du texte."),
  Q("« Marie arriva en retard. Elle courait. » Quel mot reprend « Marie » ?", ["Elle", "arriva", "retard", "courait"], "Elle", "C'est une reprise pronominale."),
  Q("Pourquoi utilise-t-on des reprises (pronoms, synonymes, périphrases) dans un texte ?", ["Pour éviter les répétitions tout en désignant le même élément", "Pour changer de sujet", "Pour allonger le texte", "Pour introduire un nouveau personnage"], "Pour éviter les répétitions tout en désignant le même élément", "Ces substituts assurent la continuité du texte."),
  Q("« Victor Hugo publia Les Misérables en 1862. L'auteur des Contemplations était alors en exil. » Comment appelle-t-on la reprise « l'auteur des Contemplations » ?", ["Une périphrase", "Un pronom", "Une métaphore", "Un synonyme strict"], "Une périphrase", "Une périphrase désigne quelqu'un ou quelque chose par une expression plus longue."),
]),
]

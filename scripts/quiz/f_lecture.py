# Thème « Lecture » (français) : notions ajoutées pour rééquilibrer le thème (au moins 40 questions par niveau)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
notion('F8', 3, F, 'f-lec-genres', [
  Q("À quel genre littéraire appartient un texte écrit pour être joué sur scène par des comédiens ?", ["Le roman", "Le théâtre", "La poésie", "L'essai"], "Le théâtre", "Le texte de théâtre est destiné à la représentation : il se compose de répliques et de didascalies."),
  Q("Un récit en prose assez long, qui raconte une histoire inventée avec des personnages, est…", ["un roman", "une fable", "un poème", "une pièce de théâtre"], "un roman", "Le roman est un récit de fiction en prose, plus long que la nouvelle."),
  Q("Un court récit, souvent en vers, qui met en scène des animaux et se termine par une morale, est…", ["une nouvelle", "une fable", "un conte", "une épopée"], "une fable", "La Fontaine a écrit de nombreuses fables, comme « Le Corbeau et le Renard »."),
]),
notion('F8', 3, F, 'f-lec-theatre', [
  Q("Au théâtre, comment appelle-t-on les indications de l'auteur sur les gestes, le ton ou le décor ?", ["Les répliques", "Les didascalies", "Les tirades", "Les apartés"], "Les didascalies", "Les didascalies, souvent en italique, ne sont pas prononcées par les comédiens."),
  Q("Comment appelle-t-on une longue réplique prononcée par un personnage sans être interrompu ?", ["Une tirade", "Un aparté", "Une stichomythie", "Une didascalie"], "Une tirade", "La tirade de Cyrano sur son nez est célèbre."),
  Q("Comment appelle-t-on une réplique qu'un personnage dit pour lui-même, que le public entend mais pas les autres personnages ?", ["Un monologue", "Un aparté", "Un dialogue", "Une tirade"], "Un aparté", "L'aparté crée une complicité avec le public ; le monologue est un personnage seul en scène qui parle."),
]),
notion('F12', 0, F, 'f-lec-versification', [
  N("Combien de syllabes compte un alexandrin ?", 12, "L'alexandrin est le vers de 12 syllabes, très utilisé dans la poésie et le théâtre classiques."),
  N("Combien de vers compte un sonnet ?", 14, "Le sonnet compte 14 vers : deux quatrains puis deux tercets."),
  Q("Comment appelle-t-on un groupe de vers, séparé des autres par un blanc ?", ["Une strophe", "Une rime", "Un paragraphe", "Un refrain"], "Une strophe", "Une strophe de quatre vers est un quatrain ; de trois vers, un tercet."),
]),
notion('F1', 5, F, 'f-lec-narrateur', [
  Q("Dans un roman, qui raconte l'histoire ?", ["Toujours l'auteur lui-même", "Le narrateur, qui peut être différent de l'auteur", "Le lecteur", "Le personnage principal obligatoirement"], "Le narrateur, qui peut être différent de l'auteur", "L'auteur est la personne réelle qui écrit ; le narrateur est la voix qui raconte dans le texte."),
  Q("« Je marchais seul dans la nuit. » Le narrateur de ce récit est…", ["extérieur à l'histoire", "un personnage de l'histoire", "absent", "le lecteur"], "un personnage de l'histoire", "Le récit à la 1re personne indique un narrateur personnage."),
  Q("Dans un récit à la 3e personne (« il », « elle »), le narrateur est généralement…", ["un personnage qui dit « je »", "extérieur à l'histoire", "l'auteur qui parle de lui", "le héros"], "extérieur à l'histoire", "Le narrateur ne participe pas à l'action qu'il raconte."),
]),
notion('F2', 3, I, 'f-lec-point-de-vue', [
  Q("Quand le narrateur sait tout des personnages, de leurs pensées et de leur passé, on parle de point de vue…", ["interne", "externe", "omniscient", "subjectif"], "omniscient", "C'est la focalisation zéro, fréquente dans les romans réalistes du XIXe siècle."),
  Q("Quand l'histoire est perçue à travers les yeux et les pensées d'un seul personnage, le point de vue est…", ["omniscient", "interne", "externe", "neutre"], "interne", "Le lecteur ne sait que ce que sait ce personnage."),
  Q("Quand le narrateur décrit seulement ce qu'on voit de l'extérieur, comme une caméra, sans révéler les pensées, le point de vue est…", ["externe", "interne", "omniscient", "lyrique"], "externe", "Le point de vue externe entretient souvent le mystère."),
]),
notion('F12', 0, I, 'f-lec-figures', [
  Q("« Ses yeux brillaient comme des étoiles. » Quelle figure de style reconnaît-on ?", ["Une métaphore", "Une comparaison", "Une personnification", "Une hyperbole"], "Une comparaison", "La comparaison rapproche deux éléments à l'aide d'un outil (comme, tel, pareil à…)."),
  Q("« Cette femme est une perle. » Quelle figure de style reconnaît-on ?", ["Une comparaison", "Une métaphore", "Une litote", "Une antithèse"], "Une métaphore", "La métaphore rapproche deux éléments sans outil de comparaison."),
  Q("« Le vent hurlait dans la forêt. » Quelle figure de style reconnaît-on ?", ["Une personnification", "Une hyperbole", "Une comparaison", "Un oxymore"], "Une personnification", "La personnification prête des caractéristiques humaines à une chose ou un animal."),
]),
notion('F2', 1, I, 'f-lec-implicite', [
  Q("« Paul referma son parapluie ruisselant en entrant. » Que comprend-on sans que ce soit écrit ?", ["Il fait beau", "Il pleut dehors", "Paul est malade", "Paul part en vacances"], "Il pleut dehors", "Comprendre l'implicite, c'est faire une inférence à partir d'indices du texte."),
  Q("« Léa regarda l'horloge pour la dixième fois en tapant du pied. » Que ressent probablement Léa ?", ["De la joie", "De l'impatience", "De la fatigue", "De la peur"], "De l'impatience", "Les gestes répétés sont des indices de son état d'esprit."),
  Q("Qu'est-ce qu'une inférence en lecture ?", ["Une erreur de lecture", "Une information que le lecteur déduit à partir d'indices du texte", "Un résumé", "Une citation"], "Une information que le lecteur déduit à partir d'indices du texte", "Le travail des inférences est essentiel pour la compréhension, dès l'école primaire."),
]),
notion('F3', 1, I, 'f-lec-visees', [
  Q("Un texte qui cherche à convaincre le lecteur d'adopter une opinion a une visée…", ["narrative", "argumentative", "descriptive", "explicative"], "argumentative", "Le texte argumentatif défend une thèse avec des arguments et des exemples."),
  Q("Un mode d'emploi ou une recette a une visée…", ["injonctive (prescriptive)", "narrative", "poétique", "argumentative"], "injonctive (prescriptive)", "Le texte injonctif donne des consignes, souvent à l'impératif ou à l'infinitif."),
  Q("Un article d'encyclopédie qui fait comprendre un phénomène a une visée…", ["narrative", "explicative", "argumentative", "lyrique"], "explicative", "Le texte explicatif répond à la question « pourquoi » ou « comment »."),
]),
notion('F12', 2, D, 'f-lec-courants', [
  Q("Quel mouvement littéraire du XIXe siècle met en avant l'expression des sentiments et du « moi », avec Victor Hugo ou Lamartine ?", ["Le classicisme", "Le romantisme", "Le réalisme", "Le surréalisme"], "Le romantisme", "Le romantisme exalte le lyrisme, la nature et la sensibilité."),
  Q("Quel mouvement cherche à représenter la société telle qu'elle est, avec Balzac et Flaubert ?", ["Le réalisme", "L'humanisme", "Le baroque", "Le symbolisme"], "Le réalisme", "Le réalisme décrit avec précision les milieux sociaux du XIXe siècle."),
  Q("Quel mouvement de la Renaissance place l'être humain et le savoir antique au centre, avec Rabelais et Montaigne ?", ["L'humanisme", "Le romantisme", "Le naturalisme", "Le classicisme"], "L'humanisme", "L'humanisme se développe en Europe aux XVe et XVIe siècles."),
]),
notion('F3', 4, D, 'f-lec-registres', [
  Q("Un texte qui cherche à émouvoir le lecteur en montrant la souffrance d'un personnage relève du registre…", ["comique", "pathétique", "épique", "fantastique"], "pathétique", "Le registre pathétique suscite la pitié et la compassion."),
  Q("Un texte qui raconte des exploits héroïques, avec des combats grandioses et des hyperboles, relève du registre…", ["épique", "lyrique", "tragique", "satirique"], "épique", "Le registre épique magnifie les héros, comme dans les chansons de geste."),
  Q("Un texte où un personnage est écrasé par un destin auquel il ne peut échapper relève du registre…", ["comique", "tragique", "réaliste", "polémique"], "tragique", "Le tragique repose sur la fatalité, comme dans les tragédies de Racine."),
]),

# ── Facile ──
notion('F8', 3, F, 'f-lec-conte', [
  Q("Quelle formule ouvre traditionnellement un conte merveilleux ?", ["« Il était une fois »", "« Cher journal »", "« Mesdames et messieurs »", "« Chapitre premier »"], "« Il était une fois »", "Cette formule situe l'histoire dans un temps indéterminé, propre au conte."),
  Q("Quel élément est typique du conte merveilleux ?", ["Des faits historiques datés", "Des éléments surnaturels acceptés comme normaux (fées, objets magiques)", "Des statistiques", "Un narrateur journaliste"], "Des éléments surnaturels acceptés comme normaux (fées, objets magiques)", "Dans le merveilleux, le surnaturel n'étonne pas les personnages."),
  Q("Comment se termine le plus souvent un conte merveilleux ?", ["Par une fin heureuse", "Par une question au lecteur", "Par une bibliographie", "Sans dénouement"], "Par une fin heureuse", "« Ils vécurent heureux… » : le héros triomphe des épreuves."),
]),
notion('F1', 5, F, 'f-lec-schema-narratif', [
  Q("Dans le schéma narratif, quel événement rompt l'équilibre de la situation initiale ?", ["Le dénouement", "L'élément perturbateur (ou déclencheur)", "La situation finale", "La péripétie finale"], "L'élément perturbateur (ou déclencheur)", "Il lance l'action : sans lui, il n'y aurait pas d'histoire."),
  Q("Comment appelle-t-on les actions et rebondissements qui suivent l'élément perturbateur ?", ["Les péripéties", "Les didascalies", "Les strophes", "Les annexes"], "Les péripéties", "Les péripéties mènent jusqu'au dénouement."),
  Q("Quelle étape du schéma narratif résout le problème posé par l'élément perturbateur ?", ["La situation initiale", "Le dénouement", "Le titre", "L'incipit"], "Le dénouement", "Il est suivi de la situation finale, le nouvel équilibre."),
]),
notion('F7', 1, F, 'f-lec-personnages', [
  Q("Dans un récit, comment appelle-t-on le personnage principal ?", ["Le figurant", "Le protagoniste (ou héros)", "L'opposant", "Le narrataire"], "Le protagoniste (ou héros)", "C'est autour de lui que l'action s'organise."),
  Q("Un personnage qui aide le héros à atteindre son but est…", ["un opposant", "un adjuvant", "un destinataire", "un antagoniste"], "un adjuvant", "Ce vocabulaire vient du schéma actantiel."),
  Q("Le loup dans « Le Petit Chaperon rouge » est, pour l'héroïne…", ["un adjuvant", "un opposant", "un narrateur", "un objet"], "un opposant", "L'opposant fait obstacle à la quête du héros."),
]),
notion('F12', 0, F, 'f-lec-rimes', [
  Q("Des rimes disposées selon le schéma AABB sont des rimes…", ["plates (ou suivies)", "croisées", "embrassées", "libres"], "plates (ou suivies)", "Deux vers consécutifs riment ensemble."),
  Q("Des rimes disposées selon le schéma ABAB sont des rimes…", ["plates", "croisées", "embrassées", "internes"], "croisées", "Les rimes alternent d'un vers à l'autre."),
  Q("Des rimes disposées selon le schéma ABBA sont des rimes…", ["plates", "croisées", "embrassées", "pauvres"], "embrassées", "Les rimes B sont « embrassées » par les rimes A."),
]),
notion('F1', 5, F, 'f-lec-temps-recit', [
  Q("Dans un récit au passé, quel temps exprime le plus souvent les actions de premier plan, qui font avancer l'histoire ?", ["L'imparfait", "Le passé simple", "Le futur", "Le présent de vérité générale"], "Le passé simple", "Le passé simple présente des actions ponctuelles et successives."),
  Q("Dans un récit au passé, quel temps sert surtout aux descriptions et aux actions d'arrière-plan ?", ["Le passé simple", "L'imparfait", "Le passé antérieur", "L'impératif"], "L'imparfait", "L'imparfait installe le décor et les habitudes."),
  Q("« Il faisait nuit. Soudain, la porte s'ouvrit. » Quel verbe marque une action de premier plan ?", ["faisait", "s'ouvrit", "nuit", "aucun"], "s'ouvrit", "Le passé simple, souvent introduit par « soudain », marque l'événement."),
]),
notion('F10', 2, F, 'f-lec-auteurs', [
  Q("Qui a écrit « Les Misérables » ?", ["Émile Zola", "Victor Hugo", "Gustave Flaubert", "Alexandre Dumas"], "Victor Hugo", "Le roman paraît en 1862."),
  Q("Qui a écrit « Le Petit Prince » ?", ["Antoine de Saint-Exupéry", "Jules Verne", "Marcel Pagnol", "Albert Camus"], "Antoine de Saint-Exupéry", "Le livre paraît en 1943."),
  Q("Qui a écrit « Vingt mille lieues sous les mers » ?", ["Jules Verne", "Victor Hugo", "Guy de Maupassant", "Charles Perrault"], "Jules Verne", "Jules Verne est l'auteur des « Voyages extraordinaires »."),
]),
notion('F1', 5, F, 'f-lec-paratexte', [
  Q("Comment appelle-t-on le texte au dos d'un livre, qui résume l'histoire pour donner envie de le lire ?", ["La préface", "La quatrième de couverture", "Le sommaire", "L'épilogue"], "La quatrième de couverture", "Elle fait partie du paratexte, comme le titre et l'illustration de couverture."),
  Q("Qu'appelle-t-on le paratexte d'un livre ?", ["Tout ce qui entoure le texte : titre, couverture, résumé, sommaire…", "Le dernier chapitre", "Les dialogues", "Les fautes d'orthographe"], "Tout ce qui entoure le texte : titre, couverture, résumé, sommaire…", "Le paratexte aide à anticiper le contenu d'un livre."),
  Q("Comment appelle-t-on la première phrase ou les premières lignes d'un roman ?", ["L'incipit", "L'excipit", "L'épilogue", "La chute"], "L'incipit", "L'excipit désigne au contraire les dernières lignes."),
]),
notion('F1', 5, F, 'f-lec-dialogue', [
  Q("Dans un récit, quel signe de ponctuation marque souvent le changement d'interlocuteur dans un dialogue ?", ["Le tiret", "Le point-virgule", "Les points de suspension", "La parenthèse"], "Le tiret", "Les guillemets ouvrent et ferment le dialogue ; le tiret signale chaque nouvelle réplique."),
  Q("« Viens ici, dit sa mère. » Comment appelle-t-on « dit sa mère » ?", ["Une incise", "Une didascalie", "Une apostrophe", "Une citation"], "Une incise", "L'incise, avec inversion du sujet, indique qui parle."),
  Q("Lequel de ces verbes est un verbe de parole ?", ["murmurer", "courir", "dormir", "regarder"], "murmurer", "Les verbes de parole (dire, répondre, s'écrier, murmurer…) précisent la manière de parler."),
]),
notion('F1', 1, F, 'f-lec-strategies', [
  Q("Quelle stratégie de compréhension consiste à redire avec ses propres mots ce qu'on vient de lire ?", ["Reformuler", "Survoler", "Recopier", "Épeler"], "Reformuler", "Reformuler permet de vérifier sa compréhension."),
  Q("Imaginer la suite d'une histoire à partir d'indices avant de la lire, c'est…", ["anticiper (faire des hypothèses)", "résumer", "copier", "conjuguer"], "anticiper (faire des hypothèses)", "Les hypothèses sont ensuite vérifiées au fil de la lecture."),
  Q("Que doit faire un lecteur qui perd le fil de sa compréhension ?", ["Continuer sans s'arrêter", "Relire le passage et s'appuyer sur les indices du texte", "Fermer le livre", "Lire plus vite"], "Relire le passage et s'appuyer sur les indices du texte", "Contrôler sa compréhension fait partie des compétences du lecteur autonome."),
]),
# ── Intermédiaire ──
notion('F8', 3, I, 'f-lec-nouvelle', [
  Q("Qu'est-ce qui distingue principalement une nouvelle d'un roman ?", ["Elle est écrite en vers", "C'est un récit bref, centré sur peu de personnages et un événement", "Elle n'a pas de narrateur", "Elle est toujours autobiographique"], "C'est un récit bref, centré sur peu de personnages et un événement", "La brièveté impose une action resserrée."),
  Q("Comment appelle-t-on la fin inattendue qui surprend le lecteur dans certaines nouvelles ?", ["La chute", "Le prologue", "La morale", "La péripétie"], "La chute", "Les nouvelles de Maupassant, comme « La Parure », sont célèbres pour leur chute."),
  Q("Quel auteur du XIXe siècle est célèbre pour ses nouvelles, comme « La Parure » ?", ["Guy de Maupassant", "Jean Racine", "Pierre de Ronsard", "Molière"], "Guy de Maupassant", "Maupassant a écrit plus de 300 nouvelles."),
]),
notion('F8', 3, I, 'f-lec-fantastique', [
  Q("Qu'est-ce qui caractérise le récit fantastique ?", ["Le surnaturel est accepté sans surprise", "Le lecteur hésite entre une explication rationnelle et une explication surnaturelle", "Il n'y a aucun personnage", "Il se passe toujours dans le futur"], "Le lecteur hésite entre une explication rationnelle et une explication surnaturelle", "Cette hésitation définit le fantastique selon Todorov."),
  Q("En quoi le fantastique se distingue-t-il du merveilleux ?", ["Dans le fantastique, le surnaturel surgit dans un cadre réaliste et inquiète", "Le fantastique a toujours une fin heureuse", "Le merveilleux est toujours effrayant", "Il n'y a aucune différence"], "Dans le fantastique, le surnaturel surgit dans un cadre réaliste et inquiète", "Dans le merveilleux, le surnaturel est normal ; dans le fantastique, il dérange."),
  Q("Quelle nouvelle de Maupassant est un classique du fantastique ?", ["« Le Horla »", "« Les Misérables »", "« Le Cid »", "« Candide »"], "« Le Horla »", "Le narrateur y doute de sa raison face à un être invisible."),
]),
notion('F8', 3, I, 'f-lec-autobiographie', [
  Q("Dans une autobiographie, qui sont l'auteur, le narrateur et le personnage principal ?", ["Trois personnes différentes", "Une seule et même personne", "L'auteur et un personnage inventé", "Le lecteur et l'auteur"], "Une seule et même personne", "C'est le « pacte autobiographique » décrit par Philippe Lejeune."),
  Q("Quelle œuvre de Rousseau est considérée comme une autobiographie fondatrice ?", ["« Les Confessions »", "« Candide »", "« Les Fables »", "« Phèdre »"], "« Les Confessions »", "Rousseau y entreprend de se montrer « dans toute la vérité de la nature »."),
  Q("En quoi les mémoires se distinguent-ils de l'autobiographie ?", ["Ils racontent surtout les événements historiques dont l'auteur a été témoin", "Ils sont toujours en vers", "Ils sont écrits à la 3e personne par un inconnu", "Ils racontent une histoire inventée"], "Ils racontent surtout les événements historiques dont l'auteur a été témoin", "L'autobiographie se centre sur la personnalité et la vie intime de l'auteur."),
]),
notion('F11', 3, I, 'f-lec-argumentation', [
  Q("Dans un texte argumentatif, comment appelle-t-on l'opinion défendue par l'auteur ?", ["La thèse", "L'exemple", "La chute", "La morale"], "La thèse", "La thèse est soutenue par des arguments, illustrés par des exemples."),
  Q("Quel rôle joue un exemple dans une argumentation ?", ["Il illustre et rend concret un argument", "Il remplace la thèse", "Il conclut toujours le texte", "Il n'a aucun rôle"], "Il illustre et rend concret un argument", "Un argument est une idée ; l'exemple est un fait qui l'appuie."),
  Q("Quel connecteur logique introduit une opposition ?", ["cependant", "donc", "car", "de plus"], "cependant", "« Donc » marque la conséquence, « car » la cause, « de plus » l'addition."),
]),
notion('F2', 3, I, 'f-lec-ordre-recit', [
  Q("Comment appelle-t-on un retour en arrière dans un récit ?", ["Une analepse", "Une prolepse", "Une ellipse", "Une pause"], "Une analepse", "On parle aussi de « flash-back »."),
  Q("Comment appelle-t-on l'annonce anticipée d'un événement futur dans un récit ?", ["Une prolepse", "Une analepse", "Une litote", "Une incise"], "Une prolepse", "Exemple : « Il ne savait pas encore qu'il ne la reverrait jamais. »"),
  Q("« Dix ans passèrent. » Quel procédé le narrateur utilise-t-il ?", ["Une ellipse", "Une scène", "Une pause descriptive", "Une analepse"], "Une ellipse", "L'ellipse passe sous silence une période de l'histoire."),
]),
notion('F2', 3, I, 'f-lec-rythme-recit', [
  Q("Quand le narrateur résume en quelques lignes une longue période, il utilise…", ["un sommaire", "une scène", "une pause", "un dialogue"], "un sommaire", "Le sommaire accélère le récit."),
  Q("Un dialogue rapporté réplique par réplique, dont la durée de lecture est proche de celle de l'action, est…", ["une scène", "une ellipse", "un sommaire", "une prolepse"], "une scène", "La scène ralentit le récit au rythme de l'action."),
  Q("Quand l'action s'arrête pour décrire un lieu ou un personnage, on parle de…", ["pause descriptive", "ellipse", "sommaire", "chute"], "pause descriptive", "Le temps de l'histoire est suspendu pendant la description."),
]),
notion('F10', 2, I, 'f-lec-mythes', [
  Q("Quel héros grec met dix ans à rentrer à Ithaque dans « L'Odyssée » d'Homère ?", ["Ulysse", "Achille", "Hercule", "Thésée"], "Ulysse", "« L'Odyssée » raconte son retour après la guerre de Troie."),
  Q("Quel personnage de la mythologie grecque vole le feu aux dieux pour le donner aux hommes ?", ["Prométhée", "Icare", "Persée", "Narcisse"], "Prométhée", "Zeus le punit en l'enchaînant à un rocher."),
  Q("Quel héros grec tue le Minotaure dans le labyrinthe grâce au fil d'Ariane ?", ["Thésée", "Ulysse", "Jason", "Orphée"], "Thésée", "Ariane lui donne un fil pour retrouver la sortie."),
]),
notion('F10', 3, I, 'f-lec-jeunesse', [
  Q("Qui a publié « Le Petit Chaperon rouge » en 1697, dans « Histoires ou contes du temps passé » ?", ["Charles Perrault", "Les frères Grimm", "Hans Christian Andersen", "Jean de La Fontaine"], "Charles Perrault", "Les frères Grimm en ont publié une autre version au XIXe siècle."),
  Q("Qui a écrit « La Petite Sirène » ?", ["Hans Christian Andersen", "Charles Perrault", "Lewis Carroll", "Roald Dahl"], "Hans Christian Andersen", "Andersen est un conteur danois du XIXe siècle."),
  Q("Qui a écrit « Charlie et la chocolaterie » ?", ["Roald Dahl", "J. K. Rowling", "Jules Verne", "Antoine de Saint-Exupéry"], "Roald Dahl", "Roald Dahl est un auteur majeur de la littérature de jeunesse."),
]),
# ── Avancé ──
notion('F12', 0, D, 'f-lec-figures-oppositions', [
  Q("« Cette obscure clarté qui tombe des étoiles » (Corneille). Quelle figure de style reconnaît-on dans « obscure clarté » ?", ["Un oxymore", "Une litote", "Une anaphore", "Une métonymie"], "Un oxymore", "L'oxymore associe deux termes contradictoires dans un même groupe."),
  Q("« Va, je ne te hais point » (Chimène, dans « Le Cid »). Quelle figure de style reconnaît-on ?", ["Une litote", "Une hyperbole", "Une comparaison", "Une personnification"], "Une litote", "La litote dit moins pour faire entendre plus : Chimène avoue son amour."),
  Q("« Je vis, je meurs » (Louise Labé). Quelle figure de style oppose deux termes dans des groupes différents ?", ["Une antithèse", "Une métaphore", "Une allitération", "Un euphémisme"], "Une antithèse", "L'antithèse rapproche deux idées opposées pour souligner leur contraste."),
]),
notion('F3', 4, D, 'f-lec-figures-insistance', [
  Q("« Je meurs de faim. » Quelle figure de style exagère la réalité ?", ["Une hyperbole", "Une litote", "Un euphémisme", "Une antithèse"], "Une hyperbole", "L'hyperbole amplifie pour frapper l'esprit."),
  Q("« Il nous a quittés » pour dire « il est mort ». Quelle figure de style atténue une réalité pénible ?", ["Un euphémisme", "Une hyperbole", "Un oxymore", "Une anaphore"], "Un euphémisme", "L'euphémisme adoucit l'expression d'une idée désagréable."),
  Q("Comment appelle-t-on la répétition d'un même mot ou groupe de mots en début de vers ou de phrase ?", ["Une anaphore", "Une allitération", "Une ellipse", "Une gradation"], "Une anaphore", "Exemple : « Rome, l'unique objet de mon ressentiment ! / Rome, à qui… » (Corneille)."),
]),
notion('F12', 2, D, 'f-lec-classicisme', [
  Q("À quel siècle le classicisme s'épanouit-il en France ?", ["Au XVIIe siècle", "Au XVe siècle", "Au XIXe siècle", "Au XXe siècle"], "Au XVIIe siècle", "C'est le siècle de Louis XIV, de Molière, Racine, Corneille et La Fontaine."),
  Q("Quelle règle du théâtre classique impose une seule intrigue, en un seul lieu et en une seule journée ?", ["La règle des trois unités", "La règle de la chute", "Le pacte autobiographique", "La règle de l'alexandrin"], "La règle des trois unités", "Unité d'action, de lieu et de temps, avec la règle de bienséance."),
  Q("Lequel de ces auteurs est un dramaturge classique du XVIIe siècle ?", ["Jean Racine", "Victor Hugo", "Émile Zola", "Paul Éluard"], "Jean Racine", "Racine a écrit des tragédies comme « Phèdre » et « Andromaque »."),
]),
notion('F12', 2, D, 'f-lec-xix-xx', [
  Q("Quel auteur a écrit le cycle des « Rougon-Macquart », emblème du naturalisme ?", ["Émile Zola", "Honoré de Balzac", "Stendhal", "Marcel Proust"], "Émile Zola", "Zola applique au roman une démarche inspirée des sciences."),
  Q("Qui a écrit « Les Fleurs du mal » (1857) ?", ["Charles Baudelaire", "Arthur Rimbaud", "Victor Hugo", "Paul Verlaine"], "Charles Baudelaire", "Le recueil fut condamné pour atteinte à la morale publique dès sa parution."),
  Q("Quel mouvement du XXe siècle, fondé par André Breton, explore le rêve et l'inconscient ?", ["Le surréalisme", "Le classicisme", "L'humanisme", "Le réalisme"], "Le surréalisme", "Breton publie le « Manifeste du surréalisme » en 1924."),
]),
notion('F12', 3, D, 'f-lec-lumieres', [
  Q("Quel mouvement du XVIIIe siècle défend la raison, la tolérance et la critique des abus du pouvoir ?", ["Les Lumières", "Le romantisme", "Le surréalisme", "Le baroque"], "Les Lumières", "Voltaire, Montesquieu, Diderot et Rousseau en sont les grandes figures."),
  Q("Qui a écrit le conte philosophique « Candide » ?", ["Voltaire", "Rousseau", "Diderot", "Montesquieu"], "Voltaire", "« Candide ou l'Optimisme » paraît en 1759."),
  Q("Qui a dirigé « L'Encyclopédie » avec d'Alembert ?", ["Denis Diderot", "Voltaire", "Molière", "Jean-Jacques Rousseau"], "Denis Diderot", "L'Encyclopédie veut rassembler et diffuser les connaissances de son temps."),
]),
notion('F12', 0, D, 'f-lec-versification-avancee', [
  Q("Comment appelle-t-on chacune des deux moitiés d'un alexandrin, séparées par la césure ?", ["Un hémistiche", "Un tercet", "Un rejet", "Un quatrain"], "Un hémistiche", "La césure coupe classiquement l'alexandrin en 6 + 6 syllabes."),
  Q("Quand la phrase déborde d'un vers sur le vers suivant sans pause, on parle…", ["d'enjambement", "de diérèse", "de rime riche", "d'anaphore"], "d'enjambement", "Si un élément bref est rejeté au début du vers suivant, on parle de rejet."),
  Q("Prononcer « li-on » en deux syllabes au lieu d'une pour respecter le compte du vers, c'est faire…", ["une diérèse", "une synérèse", "une élision", "une césure"], "une diérèse", "La synérèse est l'inverse : deux voyelles prononcées en une seule syllabe."),
]),
notion('F8', 3, D, 'f-lec-tragedie-comedie', [
  Q("Comment se termine le plus souvent une tragédie classique ?", ["Par la mort ou la ruine du héros", "Par un mariage heureux", "Par une chanson", "Par une morale en vers"], "Par la mort ou la ruine du héros", "Le héros tragique est écrasé par la fatalité ou ses passions."),
  Q("Selon une formule attribuée à la comédie classique, quel est son but ?", ["Corriger les mœurs par le rire", "Faire pleurer le spectateur", "Raconter l'histoire de France", "Décrire la nature"], "Corriger les mœurs par le rire", "« Castigat ridendo mores » : Molière s'en réclame dans ses préfaces."),
  Q("Au théâtre, comment appelle-t-on la situation où un personnage est pris pour un autre, source de comique ?", ["Un quiproquo", "Un aparté", "Un monologue", "Une exposition"], "Un quiproquo", "Le quiproquo est un ressort du comique de situation."),
]),
notion('F3', 3, D, 'f-lec-discours-rapporte', [
  Q("« Il lui dit : « Je viendrai demain. » » Quel type de discours rapporté est utilisé ?", ["Le discours direct", "Le discours indirect", "Le discours indirect libre", "Le discours narrativisé"], "Le discours direct", "Les paroles sont citées telles quelles, entre guillemets."),
  Q("« Il lui dit qu'il viendrait le lendemain. » Quel type de discours rapporté est utilisé ?", ["Le discours indirect", "Le discours direct", "Le discours indirect libre", "Le monologue"], "Le discours indirect", "Les paroles sont intégrées dans une subordonnée, avec changement de temps et de repères."),
  Q("« Elle hésitait. Viendrait-il demain ? Rien n'était moins sûr. » Quel type de discours rapporté est utilisé ?", ["Le discours indirect libre", "Le discours direct", "Le discours indirect", "Le dialogue théâtral"], "Le discours indirect libre", "Les pensées du personnage sont fondues dans la narration, sans verbe introducteur ni guillemets."),
]),
notion('F3', 4, D, 'f-lec-ironie-registres', [
  Q("Quel procédé consiste à dire le contraire de ce que l'on pense pour critiquer ou se moquer ?", ["L'ironie", "Le lyrisme", "L'euphémisme", "La gradation"], "L'ironie", "Voltaire en fait un usage constant dans « Candide »."),
  Q("Un texte qui exprime les sentiments personnels du poète, souvent à la 1re personne, relève du registre…", ["lyrique", "épique", "satirique", "tragique"], "lyrique", "Le mot vient de la lyre, instrument qui accompagnait le chant poétique."),
  Q("Un texte qui se moque des défauts d'une société ou d'un groupe pour les dénoncer relève du registre…", ["satirique", "pathétique", "lyrique", "merveilleux"], "satirique", "La satire vise à la fois à faire rire et à critiquer."),
]),
notion('F11', 2, D, 'f-lec-reecritures', [
  Q("Comment appelle-t-on l'imitation du style d'un auteur, sans intention de s'en moquer ?", ["Un pastiche", "Une parodie", "Un plagiat", "Une traduction"], "Un pastiche", "La parodie, elle, détourne une œuvre pour faire rire."),
  Q("Comment appelle-t-on la reprise comique et détournée d'une œuvre connue ?", ["Une parodie", "Un pastiche", "Une adaptation fidèle", "Une préface"], "Une parodie", "Exemple : les réécritures parodiques des fables de La Fontaine."),
  Q("En 1944, Jean Anouilh réécrit une tragédie de Sophocle. Laquelle ?", ["Antigone", "Phèdre", "Le Cid", "Andromaque"], "Antigone", "Anouilh fait de l'héroïne antique une figure de résistance."),
]),
]

# Éducation musicale : 25 questions par niveau pour chaque point du programme
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ A-4 · Écouter, comparer, construire une culture musicale commune ══
notion('A-4', 0, D, 'musd-formes-classiques', [
  Q("Qu'est-ce qu'une forme rondo ?", ["Un refrain qui revient entre des couplets différents (ABACA…)", "Une danse en rond", "Une seule mélodie répétée", "Un silence"], "Un refrain qui revient entre des couplets différents (ABACA…)", "Le Rondo alla turca de Mozart en est un exemple."),
  Q("Qu'est-ce qu'un thème et variations ?", ["Une mélodie présentée puis transformée de plusieurs façons", "Un morceau sans mélodie", "Une improvisation libre", "Un chœur"], "Une mélodie présentée puis transformée de plusieurs façons", "Les variations « Ah ! vous dirai-je, maman » de Mozart."),
  Q("Combien de mouvements compte généralement une symphonie classique ?", ["Quatre", "Un", "Deux", "Dix"], "Quatre", "Rapide, lent, menuet ou scherzo, rapide."),
]),
notion('A-4', 1, D, 'musd-musiques-du-monde', [
  Q("Qu'est-ce qu'un gamelan ?", ["Un orchestre indonésien de percussions métalliques", "Un instrument africain", "Une danse indienne", "Un chant mongol"], "Un orchestre indonésien de percussions métalliques", "Debussy l'a découvert en 1889."),
  Q("Qu'est-ce qu'un raga dans la musique classique indienne ?", ["Un cadre mélodique associé à une humeur ou un moment", "Un instrument", "Une danse", "Un tambour"], "Un cadre mélodique associé à une humeur ou un moment", "Le sitar est souvent utilisé."),
  Q("Quel chant mongol permet de produire deux sons simultanés avec la voix ?", ["Le chant diphonique (khöömii)", "Le yodel", "Le chant grégorien", "Le scat"], "Le chant diphonique (khöömii)", "On entend un son grave et une mélodie aiguë."),
]),
notion('A-4', 1, D, 'musd-minimalisme', [
  Q("Quel courant musical américain des années 1960 repose sur la répétition de motifs courts ?", ["La musique minimaliste (répétitive)", "Le romantisme", "Le baroque", "Le punk"], "La musique minimaliste (répétitive)", "Steve Reich, Philip Glass, Terry Riley."),
  Q("Quelle pièce de Steve Reich se joue uniquement en frappant dans les mains ?", ["Clapping Music", "4'33\"", "In C", "Einstein on the Beach"], "Clapping Music", "Deux musiciens se décalent progressivement."),
  Q("Qu'est-ce qu'un déphasage chez Steve Reich ?", ["Un décalage progressif entre deux motifs identiques", "Une fausse note", "Un silence", "Un changement de tonalité"], "Un décalage progressif entre deux motifs identiques", "Il crée des motifs nouveaux."),
]),
notion('A-4', 2, D, 'musd-instruments-electroniques', [
  Q("Quel instrument électronique se joue sans le toucher, en approchant les mains d'antennes ?", ["Le thérémine", "Le synthétiseur", "L'orgue", "Le piano électrique"], "Le thérémine", "Il est inventé en 1920 par Léon Theremin."),
  Q("Quel instrument électronique français a été inventé par Maurice Martenot en 1928 ?", ["Les ondes Martenot", "Le thérémine", "Le Moog", "Le mellotron"], "Les ondes Martenot", "Messiaen les utilise dans la Turangalîla-Symphonie."),
  Q("Qu'est-ce qu'un synthétiseur ?", ["Un instrument électronique qui fabrique des sons", "Un logiciel de traitement de texte", "Une flûte", "Un micro"], "Un instrument électronique qui fabrique des sons", "Le Moog est un modèle célèbre."),
]),
notion('A-4', 1, D, 'musd-renaissance-polyphonie', [
  Q("Qu'est-ce que la polyphonie ?", ["Plusieurs voix ou lignes mélodiques indépendantes chantées ensemble", "Une seule voix", "Une danse", "Un instrument à cordes"], "Plusieurs voix ou lignes mélodiques indépendantes chantées ensemble", "Elle se développe au Moyen Âge et à la Renaissance."),
  Q("Quel compositeur de la Renaissance est célèbre pour ses messes polyphoniques, comme Josquin ou Palestrina ?", ["Palestrina", "Mozart", "Chopin", "Debussy"], "Palestrina", "Il travaille à Rome au XVIe siècle."),
  Q("Quel compositeur français de la Renaissance a écrit La Guerre (La Bataille de Marignan) ?", ["Clément Janequin", "Jean-Baptiste Lully", "Hector Berlioz", "Claude Debussy"], "Clément Janequin", "Les voix imitent les bruits de la bataille."),
]),
# ══ A-5 · Réaliser des projets musicaux d'interprétation ou de création ══
notion('A-5', 0, F, 'musf-respiration-chant', [
  Q("Pourquoi faut-il bien respirer pour chanter ?", ["Pour soutenir la voix et tenir les phrases musicales", "Pour chanter plus vite", "Pour ne pas entendre les autres", "Ce n'est pas utile"], "Pour soutenir la voix et tenir les phrases musicales", "On respire avec le ventre."),
  Q("Quelle posture est conseillée pour chanter ?", ["Debout, dos droit, épaules détendues", "Allongé", "Recroquevillé", "Assis bras croisés"], "Debout, dos droit, épaules détendues", "Le corps est l'instrument du chanteur."),
  Q("Qu'est-ce que l'articulation en chant ?", ["La prononciation claire des mots", "La vitesse", "Le volume", "La hauteur"], "La prononciation claire des mots", "Le public doit comprendre le texte."),
]),
notion('A-5', 1, F, 'musf-ecouter-autres', [
  Q("Pourquoi faut-il écouter les autres en chantant en groupe ?", ["Pour chanter ensemble, juste et en rythme", "Pour chanter plus fort qu'eux", "Pour les corriger", "Ce n'est pas utile"], "Pour chanter ensemble, juste et en rythme", "Le chœur est un travail collectif."),
  Q("Que signifie chanter « juste » ?", ["Chanter les bonnes hauteurs de notes", "Chanter fort", "Chanter vite", "Chanter seul"], "Chanter les bonnes hauteurs de notes", "Chanter faux, c'est se tromper de hauteur."),
  Q("Qu'est-ce qu'une interprétation musicale ?", ["La façon personnelle de jouer ou chanter une œuvre", "La traduction des paroles", "La composition d'une œuvre", "L'enregistrement d'un disque"], "La façon personnelle de jouer ou chanter une œuvre", "Deux interprètes ne jouent jamais pareil."),
]),
notion('A-5', 0, F, 'musf-sons-voix', [
  Q("Quelle différence y a-t-il entre un son aigu et un son grave ?", ["Le son aigu est haut, le grave est bas", "Le son aigu est fort, le grave est faible", "Le son aigu est long, le grave est court", "Il n'y en a pas"], "Le son aigu est haut, le grave est bas", "C'est la hauteur du son."),
  Q("Quelle différence y a-t-il entre un son fort et un son aigu ?", ["Fort concerne l'intensité, aigu concerne la hauteur", "Ils sont identiques", "Fort concerne la hauteur", "Aigu concerne la durée"], "Fort concerne l'intensité, aigu concerne la hauteur", "On les confond souvent."),
  Q("Quels sont les quatre paramètres du son ?", ["Hauteur, durée, intensité, timbre", "Rouge, bleu, jaune, vert", "Grave, aigu, lent, vite", "Début, milieu, fin, silence"], "Hauteur, durée, intensité, timbre", "Ils permettent de décrire tout son."),
]),
notion('A-5', 1, F, 'musf-spectacle', [
  Q("Que fait-on à la fin d'une interprétation devant un public ?", ["On salue ensemble", "On part en courant", "On recommence", "On se cache"], "On salue ensemble", "Le salut fait partie du spectacle."),
  Q("Pourquoi répète-t-on avant un concert ?", ["Pour maîtriser le morceau et jouer ensemble", "Pour fatiguer la voix", "Pour oublier le texte", "Ce n'est pas utile"], "Pour maîtriser le morceau et jouer ensemble", "Les répétitions sont essentielles."),
  Q("Qu'est-ce que le trac ?", ["L'appréhension ressentie avant de monter sur scène", "Un instrument", "Un tempo", "Une note"], "L'appréhension ressentie avant de monter sur scène", "La respiration aide à le gérer."),
]),
notion('A-5', 0, I, 'musi-accords-arpeges', [
  Q("Qu'est-ce qu'un accord ?", ["Plusieurs notes jouées en même temps", "Une seule note", "Un silence", "Un rythme"], "Plusieurs notes jouées en même temps", "Do-mi-sol forme l'accord de do majeur."),
  Q("Qu'est-ce qu'un arpège ?", ["Les notes d'un accord jouées l'une après l'autre", "Un instrument à cordes", "Un silence", "Un changement de tempo"], "Les notes d'un accord jouées l'une après l'autre", "Le mot vient de la harpe (arpa)."),
  Q("Quelles notes forment l'accord parfait de do majeur ?", ["Do, mi, sol", "Do, ré, mi", "Do, fa, la", "Do, sol, si"], "Do, mi, sol", "Une tierce majeure et une quinte."),
]),
notion('A-5', 0, I, 'musi-syncope-contretemps', [
  Q("Qu'est-ce qu'une syncope en rythme ?", ["Un son attaqué sur un temps faible et prolongé sur le temps fort", "Un évanouissement", "Un silence", "Un accord"], "Un son attaqué sur un temps faible et prolongé sur le temps fort", "Elle est fréquente dans le jazz."),
  Q("Qu'est-ce qu'un contretemps ?", ["Un son placé entre les temps, souvent suivi d'un silence sur le temps", "Un retard du chef", "Un tempo lent", "Une note grave"], "Un son placé entre les temps, souvent suivi d'un silence sur le temps", "Le reggae en est rempli."),
  Q("Qu'est-ce qu'une anacrouse ?", ["Une ou plusieurs notes qui précèdent le premier temps fort", "La dernière note", "Un accord final", "Un silence"], "Une ou plusieurs notes qui précèdent le premier temps fort", "« Joyeux anniversaire » commence par une anacrouse."),
]),
notion('A-5', 0, I, 'musi-articulations', [
  Q("Que signifie jouer « staccato » ?", ["Jouer les notes détachées et courtes", "Jouer les notes liées", "Jouer très fort", "Jouer très lentement"], "Jouer les notes détachées et courtes", "On le note par un point au-dessus de la note."),
  Q("Que signifie jouer « legato » ?", ["Jouer les notes liées, sans interruption", "Jouer détaché", "Jouer très vite", "Jouer en silence"], "Jouer les notes liées, sans interruption", "Une liaison courbe l'indique."),
  Q("Que signifie un accent (>) sur une note ?", ["Qu'il faut la jouer plus fort que les autres", "Qu'il faut la supprimer", "Qu'il faut la tenir longtemps", "Qu'il faut la jouer plus bas"], "Qu'il faut la jouer plus fort que les autres", "L'accent met en valeur un son."),
]),
notion('A-5', 1, I, 'musi-direction-choeur', [
  Q("Que signifie le geste du chef de chœur qui ouvre la main en éloignant les bras ?", ["Chanter plus fort (crescendo)", "Se taire", "Accélérer", "Changer de chanson"], "Chanter plus fort (crescendo)", "Les gestes guident les nuances."),
  Q("Pourquoi le chef de chœur donne-t-il une respiration avant le départ ?", ["Pour que tout le monde commence ensemble", "Pour se reposer", "Pour marquer la fin", "Par habitude"], "Pour que tout le monde commence ensemble", "C'est le geste d'attaque."),
  Q("Comment le chef indique-t-il la fin d'un son tenu ?", ["Par un geste de coupure de la main", "En criant", "En tapant du pied", "En éteignant la lumière"], "Par un geste de coupure de la main", "Tous s'arrêtent en même temps."),
]),
notion('A-5', 0, I, 'musi-creer-paysage', [
  Q("Qu'est-ce qu'une création musicale en classe ?", ["Inventer un morceau à partir de sons, de rythmes ou de voix", "Recopier une partition", "Écouter un disque", "Apprendre une chanson par cœur"], "Inventer un morceau à partir de sons, de rythmes ou de voix", "On peut partir d'une image ou d'un texte."),
  Q("Qu'est-ce qu'un bruitage ?", ["La création de sons qui imitent des bruits réels", "Une fausse note", "Un instrument cassé", "Un silence"], "La création de sons qui imitent des bruits réels", "Il accompagne un film, une histoire ou un conte."),
  Q("Quel outil permet de garder une trace d'une création sonore de classe ?", ["Un enregistrement audio", "Un dessin", "Une photo", "Rien"], "Un enregistrement audio", "On peut ensuite l'écouter et l'améliorer."),
]),
notion('A-5', 0, D, 'musd-intervalles', [
  Q("Quel intervalle sépare do et mi ?", ["Une tierce (majeure)", "Une quarte", "Une quinte", "Une octave"], "Une tierce (majeure)", "Do-ré-mi : trois notes."),
  Q("Quel intervalle sépare do et le do suivant ?", ["Une octave", "Une quinte", "Une septième", "Une sixte"], "Une octave", "Huit notes."),
  Q("Combien de demi-tons comporte une tierce majeure ?", ["4", "3", "5", "2"], "4", "La tierce mineure en compte 3."),
]),
notion('A-5', 0, D, 'musd-armure-tonalite', [
  Q("Qu'est-ce que l'armure d'une partition ?", ["Les dièses ou bémols placés au début de la portée", "Le titre", "La signature du compositeur", "Les paroles"], "Les dièses ou bémols placés au début de la portée", "Elle indique la tonalité."),
  Q("Combien d'altérations à la clé a la gamme de do majeur ?", ["Aucune", "Une", "Deux", "Sept"], "Aucune", "Elle n'utilise que les touches blanches du piano."),
  Q("Quelle gamme a un fa dièse à la clé ?", ["Sol majeur (ou mi mineur)", "Do majeur", "Fa majeur", "Ré majeur"], "Sol majeur (ou mi mineur)", "Chaque armure correspond à deux tonalités relatives."),
]),
notion('A-5', 0, D, 'musd-transposer', [
  Q("Qu'est-ce que transposer un morceau ?", ["Le jouer plus haut ou plus bas en gardant les mêmes intervalles", "Le jouer plus vite", "Le traduire", "Le réécrire en entier"], "Le jouer plus haut ou plus bas en gardant les mêmes intervalles", "On adapte une chanson à la voix des élèves."),
  Q("Pourquoi transpose-t-on souvent une chanson pour des enfants ?", ["Pour l'adapter à l'étendue de leur voix", "Pour la rendre plus difficile", "Pour changer les paroles", "Par habitude"], "Pour l'adapter à l'étendue de leur voix", "Les voix d'enfants sont plutôt aiguës."),
  Q("Qu'est-ce que la tessiture d'une voix ?", ["L'ensemble des notes qu'elle peut chanter confortablement", "Sa couleur", "Son volume", "Sa vitesse"], "L'ensemble des notes qu'elle peut chanter confortablement", "Elle varie selon les personnes."),
]),
notion('A-5', 0, D, 'musd-cadences', [
  Q("Qu'est-ce qu'une cadence en harmonie ?", ["Un enchaînement d'accords qui ponctue une phrase musicale", "Une vitesse", "Un instrument", "Un silence long"], "Un enchaînement d'accords qui ponctue une phrase musicale", "Comme une ponctuation."),
  Q("Quel effet produit une cadence parfaite (V-I) ?", ["Une impression de conclusion", "Une impression de suspension", "Un effet comique", "Aucun effet"], "Une impression de conclusion", "C'est le point final."),
  Q("Quel effet produit une demi-cadence (sur le Ve degré) ?", ["Une impression de suspension, comme une virgule", "Une conclusion", "Un silence", "Une accélération"], "Une impression de suspension, comme une virgule", "La phrase appelle une suite."),
]),
notion('A-5', 1, D, 'musd-polyrythmie', [
  Q("Qu'est-ce que la polyrythmie ?", ["La superposition de plusieurs rythmes différents", "Un seul rythme", "Une mélodie lente", "Un silence"], "La superposition de plusieurs rythmes différents", "Elle est très présente dans les musiques d'Afrique."),
  Q("Quelle polyrythmie superpose deux notes contre trois dans le même temps ?", ["Le 3 contre 2 (hémiole)", "Le 4/4", "Le 1 contre 1", "Le canon"], "Le 3 contre 2 (hémiole)", "On peut la jouer avec les deux mains."),
  Q("Pourquoi la polyrythmie est-elle difficile à réaliser en groupe ?", ["Chacun doit tenir son rythme sans se laisser entraîner par les autres", "Il n'y a pas de rythme", "Elle est très lente", "Elle se joue seul"], "Chacun doit tenir son rythme sans se laisser entraîner par les autres", "Elle demande écoute et concentration."),
]),
notion('A-5', 0, D, 'musd-mao', [
  Q("Que signifie MAO ?", ["Musique assistée par ordinateur", "Musique africaine orchestrale", "Méthode d'apprentissage oral", "Musique ancienne occidentale"], "Musique assistée par ordinateur", "Elle permet de composer et d'enregistrer."),
  Q("Qu'est-ce qu'un séquenceur ?", ["Un logiciel qui organise des sons et des pistes dans le temps", "Un instrument à vent", "Un micro", "Une partition papier"], "Un logiciel qui organise des sons et des pistes dans le temps", "On peut empiler des pistes."),
  Q("Qu'est-ce que le MIDI ?", ["Un langage qui permet aux instruments électroniques et aux ordinateurs de communiquer", "Une heure de la journée", "Un style musical", "Une note de musique"], "Un langage qui permet aux instruments électroniques et aux ordinateurs de communiquer", "Il transmet des notes, pas des sons."),
]),
notion('A-5', 1, D, 'musd-interpretation-historique', [
  Q("Qu'est-ce que l'interprétation historiquement informée ?", ["Jouer la musique ancienne avec les instruments et pratiques de son époque", "Jouer uniquement du rock", "Improviser librement", "Jouer avec des instruments électroniques"], "Jouer la musique ancienne avec les instruments et pratiques de son époque", "Par exemple sur clavecin ou violon baroque."),
  Q("Quel chef d'orchestre français est une figure du renouveau baroque avec Les Arts florissants ?", ["William Christie", "Herbert von Karajan", "Pierre Boulez", "Leonard Bernstein"], "William Christie", "Il a fait redécouvrir Rameau et Charpentier."),
  Q("Pourquoi le la de référence était-il souvent plus bas à l'époque baroque ?", ["Les diapasons n'étaient pas normalisés et souvent autour de 415 Hz", "Les instruments étaient cassés", "Par erreur", "Il était plus haut"], "Les diapasons n'étaient pas normalisés et souvent autour de 415 Hz", "Aujourd'hui, on utilise souvent 440 Hz."),
]),
]

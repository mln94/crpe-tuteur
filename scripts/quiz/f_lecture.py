# Thème « Lecture » (français) : notions ajoutées pour rééquilibrer le thème (13 → 43 questions)
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
]

# SVT : notions ajoutées pour que chaque sous-thème du programme compte au moins 15 questions
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── La planète Terre · Risques naturels et prévention ──
notion('PT-3', 1, F, 'svt-alea-risque', [
  Q("En sciences, qu'est-ce qu'un aléa ?", ["Un phénomène naturel potentiellement dangereux (séisme, crue, cyclone…)", "Une mesure de protection", "Une ville exposée", "Une assurance"], "Un phénomène naturel potentiellement dangereux (séisme, crue, cyclone…)", "L'aléa devient un risque lorsqu'il menace des populations ou des biens."),
  Q("Un risque naturel est d'autant plus grand que…", ["l'aléa est fort et que les enjeux humains sont nombreux et vulnérables", "la région est peu peuplée", "le phénomène est rare", "il fait beau"], "l'aléa est fort et que les enjeux humains sont nombreux et vulnérables", "Un séisme dans un désert inhabité représente un risque faible."),
  Q("Lequel de ces phénomènes peut être prévu plusieurs jours à l'avance ?", ["Un cyclone", "Un séisme", "Un glissement de terrain soudain", "La chute d'une météorite"], "Un cyclone", "Les satellites suivent la formation et la trajectoire des cyclones ; on ne sait pas prévoir la date d'un séisme."),
]),
notion('PT-3', 0, I, 'svt-cyclones-inondations', [
  Q("Comment appelle-t-on un cyclone tropical dans le nord-ouest de l'océan Pacifique ?", ["Un typhon", "Une tornade", "Un mistral", "Une mousson"], "Un typhon", "Dans l'Atlantique nord, on parle d'ouragan."),
  N("Au-dessus de quelle température environ (en °C) l'eau de mer permet-elle la formation des cyclones ?", 26, "L'évaporation d'une eau chaude, d'au moins 26 °C, fournit l'énergie du cyclone."),
  Q("Quelle mesure de prévention limite les dégâts des inondations ?", ["Interdire ou limiter les constructions dans les zones inondables", "Construire davantage au bord des rivières", "Imperméabiliser les sols", "Supprimer les zones humides"], "Interdire ou limiter les constructions dans les zones inondables", "C'est l'objet des plans de prévention des risques d'inondation (PPRI)."),
]),
notion('PT-3', 0, D, 'svt-tsunami', [
  Q("Quelle est la cause la plus fréquente d'un tsunami ?", ["Un séisme sous-marin", "Un orage violent", "La marée", "Le vent"], "Un séisme sous-marin", "Le mouvement brutal du fond océanique déplace une énorme masse d'eau."),
  Q("Quel tsunami a fait plus de 200 000 victimes en décembre 2004 ?", ["Celui de l'océan Indien", "Celui de la mer du Nord", "Celui du lac Léman", "Celui de la Méditerranée"], "Celui de l'océan Indien", "Il a touché l'Indonésie, le Sri Lanka, l'Inde et la Thaïlande."),
  Q("Qu'est-ce qui permet d'alerter à temps les populations côtières d'un tsunami ?", ["Un réseau de sismographes et de capteurs en mer relié à un système d'alerte", "Une hausse de la température de l'air", "Le chant des oiseaux", "Les marées"], "Un réseau de sismographes et de capteurs en mer relié à un système d'alerte", "Les vagues mettent parfois plusieurs heures à atteindre des côtes lointaines."),
]),
notion('PT-3', 1, I, 'svt-surveillance-volcans', [
  Q("Quels signes les scientifiques surveillent-ils pour prévoir une éruption ?", ["Les petits séismes, la déformation du sol et les émissions de gaz", "La couleur du ciel", "Le nombre de touristes", "La température de l'air"], "Les petits séismes, la déformation du sol et les émissions de gaz", "La montée du magma provoque ces signes avant-coureurs."),
  Q("Quel volcan de La Réunion, très actif, est surveillé en permanence par un observatoire ?", ["Le Piton de la Fournaise", "Le Vésuve", "L'Etna", "Le Puy de Dôme"], "Le Piton de la Fournaise", "Il connaît en moyenne une à deux éruptions par an."),
  Q("Quel document délimite les zones exposées à un risque et y règle les constructions ?", ["Le plan de prévention des risques (PPR)", "Le règlement intérieur", "Le cadastre", "Le Code de la route"], "Le plan de prévention des risques (PPR)", "Il est établi par l'État, à partir des cartes d'aléas."),
]),
# ── Le vivant et son évolution · Reproduction et dynamique des populations ──
notion('VE-2', 0, F, 'svt-reproduction-asexuee', [
  Q("Un fraisier produit de nouveaux pieds grâce à ses stolons. De quel type de reproduction s'agit-il ?", ["Une reproduction asexuée (multiplication végétative)", "Une reproduction sexuée", "Une pollinisation", "Une fécondation"], "Une reproduction asexuée (multiplication végétative)", "Aucun gamète n'intervient."),
  Q("Les individus issus d'une reproduction asexuée sont…", ["génétiquement identiques au parent (des clones)", "tous différents", "toujours stériles", "des hybrides"], "génétiquement identiques au parent (des clones)", "Seule la reproduction sexuée crée de la diversité génétique."),
  Q("Lequel de ces procédés est une reproduction asexuée utilisée par les jardiniers ?", ["Le bouturage", "La pollinisation", "La fécondation", "La germination d'une graine"], "Le bouturage", "Un fragment de tige replanté donne une nouvelle plante."),
]),
notion('VE-2', 0, I, 'svt-fecondation-animaux', [
  Q("Comment appelle-t-on une fécondation qui a lieu dans l'eau, hors du corps de la femelle ?", ["Une fécondation externe", "Une fécondation interne", "Une pollinisation", "Une mitose"], "Une fécondation externe", "C'est le cas de nombreux poissons et amphibiens."),
  Q("Lequel de ces animaux a une fécondation interne ?", ["Le chat", "La grenouille", "Le saumon", "L'oursin"], "Le chat", "Les mammifères, les oiseaux et les reptiles ont une fécondation interne."),
  Q("Pourquoi beaucoup de poissons pondent-ils un très grand nombre d'œufs ?", ["Parce que la plupart des œufs et des larves meurent avant l'âge adulte", "Parce que leurs œufs sont très gros", "Parce qu'ils protègent chaque œuf", "Parce qu'ils vivent longtemps"], "Parce que la plupart des œufs et des larves meurent avant l'âge adulte", "Le grand nombre compense les pertes et assure le maintien de la population."),
]),
# ── Le vivant et son évolution · Classification et parenté du vivant ──
notion('VE-3', 1, I, 'svt-homo-sapiens', [
  Q("À quel groupe d'êtres vivants appartient Homo sapiens ?", ["Aux primates (mammifères)", "Aux reptiles", "Aux insectes", "Aux amphibiens"], "Aux primates (mammifères)", "Nous partageons avec les autres primates des caractères comme le pouce opposable."),
  Q("Dans quel pays ont été découverts les plus anciens fossiles connus d'Homo sapiens, datés d'environ 300 000 ans ?", ["Au Maroc", "En France", "En Chine", "En Australie"], "Au Maroc", "Ils proviennent du site de Jebel Irhoud."),
  Q("L'être humain descend-il du chimpanzé ?", ["Non : ils partagent un ancêtre commun", "Oui, directement", "Oui, il y a 10 000 ans", "Ils n'ont aucun lien de parenté"], "Non : ils partagent un ancêtre commun", "Les deux lignées se sont séparées il y a environ 7 millions d'années."),
]),
# ── Le vivant et son évolution · L'évolution des espèces ──
notion('VE-5', 0, I, 'svt-premiers-vivants', [
  Q("Quels sont les plus anciens êtres vivants dont on a retrouvé des traces ?", ["Des bactéries", "Des dinosaures", "Des fougères", "Des poissons"], "Des bactéries", "Leurs traces remontent à environ 3,5 milliards d'années."),
  Q("Comment appelle-t-on les roches calcaires construites par des colonies de cyanobactéries, parmi les plus anciennes traces de vie ?", ["Des stromatolithes", "Des stalactites", "Des basaltes", "Des granites"], "Des stromatolithes", "Il en existe encore aujourd'hui, par exemple en Australie."),
  Q("Quel événement a probablement provoqué la disparition des dinosaures non aviens, il y a 66 millions d'années ?", ["La chute d'un astéroïde, associée à un volcanisme intense", "Une glaciation récente", "La chasse par les humains", "Une épidémie de grippe"], "La chute d'un astéroïde, associée à un volcanisme intense", "Les oiseaux sont les descendants actuels de dinosaures."),
]),
]

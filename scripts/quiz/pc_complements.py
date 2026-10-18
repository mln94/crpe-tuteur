# Physique-chimie : notions ajoutées pour couvrir chaque sous-thème du programme (au moins 15 questions)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── L'énergie · Rayonnement et transferts d'énergie ──
notion('EN-2', 0, F, 'pc-transferts-thermiques', [
  Q("Comment appelle-t-on le transfert d'énergie thermique à travers un matériau solide, comme le manche d'une casserole ?", ["La conduction", "La convection", "Le rayonnement", "L'évaporation"], "La conduction", "Les métaux sont de bons conducteurs thermiques, le bois et l'air de mauvais conducteurs."),
  Q("Quel mode de transfert fait monter l'air chaud vers le plafond d'une pièce ?", ["La convection", "La conduction", "Le rayonnement", "La fusion"], "La convection", "Le fluide chaud, moins dense, s'élève et le fluide froid descend."),
  Q("Quel mode de transfert permet de se réchauffer devant un feu, à distance ?", ["Le rayonnement", "La conduction", "La convection", "La condensation"], "Le rayonnement", "Le rayonnement n'a pas besoin de matière pour se propager."),
]),
notion('EN-2', 0, F, 'pc-rayonnement-absorption', [
  Q("Comment l'énergie du Soleil parvient-elle jusqu'à la Terre ?", ["Par rayonnement, à travers le vide spatial", "Par conduction", "Par convection", "Par le vent solaire uniquement"], "Par rayonnement, à travers le vide spatial", "Seul le rayonnement peut traverser le vide."),
  Q("Pourquoi un vêtement noir chauffe-t-il davantage au soleil qu'un vêtement blanc ?", ["Il absorbe davantage le rayonnement reçu", "Il est plus épais", "Il réfléchit plus de lumière", "Il produit de la chaleur"], "Il absorbe davantage le rayonnement reçu", "Une surface claire réfléchit une plus grande partie du rayonnement."),
  Q("Que se passe-t-il pour un objet qui absorbe un rayonnement ?", ["Il reçoit de l'énergie et sa température augmente", "Il perd de la masse", "Il devient transparent", "Rien du tout"], "Il reçoit de l'énergie et sa température augmente", "L'absorption d'un rayonnement est un transfert d'énergie."),
]),
notion('EN-2', 0, I, 'pc-infrarouge-thermographie', [
  Q("Quel rayonnement invisible tous les objets émettent-ils, d'autant plus qu'ils sont chauds ?", ["Le rayonnement infrarouge", "Les rayons X", "Les ultrasons", "Les ondes sonores"], "Le rayonnement infrarouge", "Notre corps en émet aussi en permanence."),
  Q("Que montre une caméra thermique ?", ["Les différences de température entre les objets", "Les objets à travers les murs", "Les sons émis", "La couleur réelle des objets"], "Les différences de température entre les objets", "Elle capte le rayonnement infrarouge émis par les objets."),
  Q("Pourquoi réalise-t-on des images thermographiques des maisons ?", ["Pour repérer les pertes de chaleur dues à une mauvaise isolation", "Pour mesurer la hauteur des murs", "Pour détecter l'humidité de l'air", "Pour choisir la couleur des façades"], "Pour repérer les pertes de chaleur dues à une mauvaise isolation", "Les zones qui laissent fuir la chaleur apparaissent plus chaudes."),
]),
notion('EN-2', 0, I, 'pc-effet-serre-physique', [
  Q("Sous quelle forme principalement la Terre réémet-elle vers l'espace l'énergie qu'elle reçoit ?", ["Un rayonnement infrarouge", "Un rayonnement ultraviolet", "Des ondes sonores", "Un courant électrique"], "Un rayonnement infrarouge", "La surface chauffée par le Soleil émet à son tour un rayonnement infrarouge."),
  Q("Quel est le rôle des gaz à effet de serre dans l'atmosphère ?", ["Ils absorbent une partie du rayonnement infrarouge émis par la Terre et en renvoient une partie vers le sol", "Ils bloquent toute la lumière du Soleil", "Ils refroidissent la Terre", "Ils produisent de l'énergie"], "Ils absorbent une partie du rayonnement infrarouge émis par la Terre et en renvoient une partie vers le sol", "Leur augmentation renforce l'effet de serre et réchauffe le climat."),
  Q("Sans effet de serre naturel, quelle serait environ la température moyenne à la surface de la Terre ?", ["Environ −18 °C", "Environ 15 °C", "Environ 50 °C", "Environ 100 °C"], "Environ −18 °C", "Grâce à l'effet de serre naturel, elle est d'environ 15 °C."),
]),
notion('EN-2', 0, D, 'pc-bilan-terre', [
  Q("Que se passe-t-il si la Terre reçoit durablement plus d'énergie qu'elle n'en renvoie vers l'espace ?", ["Sa température moyenne augmente", "Sa température moyenne baisse", "Rien ne change", "Elle s'éloigne du Soleil"], "Sa température moyenne augmente", "C'est le déséquilibre du bilan énergétique responsable du réchauffement actuel."),
  Q("Quelle part environ du rayonnement solaire reçu est directement réfléchie vers l'espace par la Terre (son albédo) ?", ["Environ 30 %", "Environ 1 %", "Environ 70 %", "La totalité"], "Environ 30 %", "Les nuages, les glaces et les déserts réfléchissent beaucoup."),
  Q("Laquelle de ces surfaces réfléchit le plus le rayonnement solaire ?", ["La neige fraîche", "L'océan", "Une forêt de conifères", "Une route goudronnée"], "La neige fraîche", "Elle a l'albédo le plus élevé ; l'océan, sombre, absorbe beaucoup."),
]),
# ── Des signaux pour observer et communiquer · Signaux et communication ──
notion('SI-3', 0, F, 'pc-ondes-radio', [
  Q("Quel type de signal utilisent la radio, le wifi et les téléphones portables ?", ["Des ondes électromagnétiques (ondes radio)", "Des ondes sonores", "Des ultrasons", "Un courant électrique dans l'air"], "Des ondes électromagnétiques (ondes radio)", "Comme la lumière, ce sont des ondes électromagnétiques, mais invisibles."),
  Q("Les ondes radio peuvent-elles se propager dans le vide ?", ["Oui, c'est ainsi que l'on communique avec les satellites et les sondes", "Non, elles ont besoin d'air", "Seulement la nuit", "Seulement sous l'eau"], "Oui, c'est ainsi que l'on communique avec les satellites et les sondes", "Le son, lui, ne se propage pas dans le vide."),
  Q("À quelle vitesse se propagent les ondes radio dans le vide ?", ["À la vitesse de la lumière, environ 300 000 km/s", "À la vitesse du son, environ 340 m/s", "À environ 100 km/h", "Instantanément, sans durée"], "À la vitesse de la lumière, environ 300 000 km/s", "Elles mettent pourtant plusieurs minutes pour atteindre Mars."),
]),
notion('SI-3', 0, I, 'pc-signal-numerique', [
  Q("Qu'est-ce qu'un signal numérique ?", ["Un signal codé par une suite de 0 et de 1", "Un signal qui varie de façon continue", "Un signal sonore très aigu", "Un signal lumineux coloré"], "Un signal codé par une suite de 0 et de 1", "Le signal analogique, lui, varie de façon continue."),
  Q("Quel appareil transforme un son en signal électrique ?", ["Un microphone", "Un haut-parleur", "Une lampe", "Une pile"], "Un microphone", "Le haut-parleur réalise la conversion inverse."),
  Q("Quel système utilise les signaux de satellites pour déterminer une position sur Terre ?", ["Le GPS (ou Galileo)", "Le sonar", "Le radar de vitesse", "La fibre optique"], "Le GPS (ou Galileo)", "Le récepteur calcule sa position à partir des durées de propagation des signaux."),
]),
]

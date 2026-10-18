# Arts plastiques : notions ajoutées pour couvrir chaque point du programme (au moins 12 questions par sous-thème)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ La représentation ; images, réalité et fiction ══
# L'autonomie de l'œuvre d'art
notion('AR-4', 0, F, 'art-abstraction-pionniers', [
  Q("Quel peintre est considéré comme l'un des pionniers de l'art abstrait, vers 1910 ?", ["Vassily Kandinsky", "Claude Monet", "Jean-François Millet", "Eugène Delacroix"], "Vassily Kandinsky", "Il cherche à exprimer des émotions par les seules couleurs et formes, comme la musique."),
  Q("Quel peintre néerlandais compose ses tableaux avec des lignes noires et des aplats de couleurs primaires ?", ["Piet Mondrian", "Rembrandt", "Vincent van Gogh", "Johannes Vermeer"], "Piet Mondrian", "Ses compositions illustrent une abstraction géométrique."),
  Q("Quel peintre russe a réalisé Carré blanc sur fond blanc (1918) ?", ["Kasimir Malevitch", "Marc Chagall", "Ilia Répine", "Pablo Picasso"], "Kasimir Malevitch", "Il est le fondateur du suprématisme."),
]),
notion('AR-4', 0, I, 'art-mise-en-abyme', [
  Q("Qu'est-ce qu'une mise en abyme en art ?", ["Une œuvre qui contient une représentation d'elle-même ou de sa propre fabrication", "Une œuvre peinte au fond d'un gouffre", "Une œuvre très sombre", "Une œuvre sans cadre"], "Une œuvre qui contient une représentation d'elle-même ou de sa propre fabrication", "L'œuvre parle alors de ses propres constituants."),
  Q("Dans Les Ménines (1656), que montre notamment Velázquez ?", ["Le peintre lui-même, en train de peindre une grande toile", "Une bataille navale", "Un paysage sans personnages", "Un objet du quotidien isolé"], "Le peintre lui-même, en train de peindre une grande toile", "Le tableau interroge le regard et la représentation."),
  Q("Quel tableau de Magritte porte l'inscription « Ceci n'est pas une pipe » ?", ["La Trahison des images", "Le Fils de l'homme", "L'Empire des lumières", "La Persistance de la mémoire"], "La Trahison des images", "Il rappelle qu'une image n'est pas l'objet qu'elle représente."),
]),
notion('AR-4', 0, D, 'art-informel-concret', [
  Q("Comment appelle-t-on, dans la France d'après-guerre, l'art abstrait fondé sur la spontanéité du geste et de la matière ?", ["L'art informel", "L'art concret", "Le pop art", "Le néoclassicisme"], "L'art informel", "Jean Fautrier et Jean Dubuffet en sont des figures majeures."),
  Q("Quel peintre français est célèbre pour ses toiles « outrenoires », jouant de la lumière sur le noir ?", ["Pierre Soulages", "Henri Matisse", "Georges Braque", "Paul Gauguin"], "Pierre Soulages", "Un musée lui est consacré à Rodez."),
  Q("Que revendique l'art concret, défini par Theo van Doesburg en 1930 ?", ["Une œuvre construite uniquement avec des éléments plastiques (lignes, plans, couleurs), sans référence au réel", "La copie fidèle de la nature", "L'usage d'objets du quotidien", "La peinture de scènes historiques"], "Une œuvre construite uniquement avec des éléments plastiques (lignes, plans, couleurs), sans référence au réel", "Pour lui, rien n'est plus concret qu'une ligne ou une couleur."),
]),
# La conception, la production et la diffusion de l'œuvre à l'ère du numérique
notion('AR-6', 0, F, 'art-image-pixels', [
  Q("De quoi est composée une image numérique matricielle, comme une photo ?", ["De pixels", "De vecteurs uniquement", "De pigments", "De fils"], "De pixels", "Chaque pixel est un petit point de couleur."),
  Q("Comment appelle-t-on la modification d'une photographie avec un logiciel ?", ["La retouche", "La gravure", "Le modelage", "Le tirage"], "La retouche", "Elle peut transformer profondément le sens d'une image."),
  Q("Qu'est-ce qu'un GIF animé ?", ["Une courte suite d'images qui s'enchaînent en boucle", "Une sculpture lumineuse", "Une affiche imprimée", "Un tableau abstrait"], "Une courte suite d'images qui s'enchaînent en boucle", "C'est une forme simple d'image animée numérique."),
]),
notion('AR-6', 0, I, 'art-diffusion-numerique', [
  Q("Pourquoi distingue-t-on une œuvre de son image, par exemple sur un écran ?", ["Parce que la reproduction ne restitue ni l'échelle, ni la matière, ni la présence de l'œuvre", "Parce que l'image est toujours plus belle", "Parce que l'œuvre n'existe pas vraiment", "Il n'y a aucune différence"], "Parce que la reproduction ne restitue ni l'échelle, ni la matière, ni la présence de l'œuvre", "Voir une œuvre en vrai reste une expérience différente."),
  Q("Qu'est-ce qu'une visite virtuelle de musée ?", ["Une découverte des salles et des œuvres en ligne, en images ou en 3D", "Une visite guidée de nuit", "Un musée sans œuvres", "Une exposition dans la rue"], "Une découverte des salles et des œuvres en ligne, en images ou en 3D", "Le numérique change la diffusion et l'analyse des œuvres."),
  Q("Peut-on diffuser librement en ligne l'image d'une œuvre d'un artiste vivant ?", ["Non, elle est protégée par le droit d'auteur", "Oui, toujours", "Oui, si l'image est en noir et blanc", "Oui, si on la recadre"], "Non, elle est protégée par le droit d'auteur", "En France, les œuvres entrent dans le domaine public 70 ans après la mort de l'auteur."),
]),
notion('AR-6', 0, D, 'art-ia-images', [
  Q("Qu'est-ce qu'une image générée par intelligence artificielle ?", ["Une image produite par un programme à partir d'une description ou d'exemples", "Une photographie prise par un robot", "Une peinture faite à la main", "Un dessin scanné"], "Une image produite par un programme à partir d'une description ou d'exemples", "Elle interroge les notions d'auteur et de création."),
  Q("Pourquoi les images générées par IA posent-elles des questions éthiques ?", ["Elles s'appuient sur des œuvres existantes et peuvent servir à fabriquer de fausses images", "Elles sont toujours en noir et blanc", "Elles coûtent trop cher à imprimer", "Elles ne peuvent pas être affichées"], "Elles s'appuient sur des œuvres existantes et peuvent servir à fabriquer de fausses images", "Le droit d'auteur et la désinformation sont en jeu."),
  Q("Comment appelle-t-on une vidéo truquée très réaliste produite par intelligence artificielle ?", ["Un hypertrucage (deepfake)", "Un storyboard", "Un travelling", "Un flip book"], "Un hypertrucage (deepfake)", "Il faut vérifier l'origine des images avant de les croire ou de les partager."),
]),
# ══ La matérialité de l'œuvre ; l'objet et l'œuvre ══
notion('AM-2', 0, I, 'art-fini-non-fini', [
  Q("Que désigne le « non finito » dans les sculptures de Michel-Ange ?", ["Des œuvres volontairement laissées inachevées, où le bloc de marbre reste visible", "Des statues en bronze poli", "Des sculptures peintes", "Des œuvres détruites"], "Des œuvres volontairement laissées inachevées, où le bloc de marbre reste visible", "Les figures semblent sortir de la matière brute."),
  Q("Quelle matière Joseph Beuys utilise-t-il souvent pour sa charge symbolique de protection et de chaleur ?", ["Le feutre (et la graisse)", "L'or", "Le marbre de Carrare", "Le verre soufflé"], "Le feutre (et la graisse)", "Le choix du matériau porte une signification."),
  Q("Pourquoi un sculpteur laisse-t-il parfois visibles les traces de ses outils ?", ["Pour montrer le processus de fabrication et la réalité de la matière", "Par manque de temps uniquement", "Pour que l'œuvre soit moins chère", "Pour cacher le matériau"], "Pour montrer le processus de fabrication et la réalité de la matière", "Le non-fini devient un choix expressif."),
]),
notion('AM-4', 0, F, 'art-detournement', [
  Q("Que signifie détourner un objet en art ?", ["Lui donner une autre fonction ou une autre signification", "Le réparer", "Le vendre", "Le jeter"], "Lui donner une autre fonction ou une autre signification", "L'objet, sorti de son usage, devient matériau artistique."),
  Q("Quel artiste a réalisé Tête de taureau (1942) avec une selle et un guidon de vélo ?", ["Pablo Picasso", "Auguste Rodin", "Claude Monet", "Henri Matisse"], "Pablo Picasso", "Deux objets ordinaires suffisent à évoquer un animal."),
  Q("Quel sculpteur français compresse des voitures pour en faire des œuvres ?", ["César", "Rodin", "Camille Claudel", "Maillol"], "César", "Ses « compressions » datent de la fin des années 1950."),
]),
notion('AM-4', 0, I, 'art-nouveau-realisme', [
  Q("Quel mouvement des années 1960, avec Arman, César et Tinguely, utilise les objets du quotidien ?", ["Le Nouveau Réalisme", "L'impressionnisme", "Le romantisme", "Le fauvisme"], "Le Nouveau Réalisme", "Il est fondé en 1960 autour du critique Pierre Restany."),
  Q("Quel artiste suisse crée des sculptures-machines animées à partir de ferraille ?", ["Jean Tinguely", "Alberto Giacometti", "Paul Klee", "Le Corbusier"], "Jean Tinguely", "Il réalise avec Niki de Saint Phalle la fontaine Stravinsky."),
  Q("Que sont les « tableaux-pièges » de Daniel Spoerri ?", ["Les restes d'un repas fixés sur la table, puis accrochés au mur", "Des toiles qui se déchirent seules", "Des tableaux cachés derrière d'autres", "Des peintures en trompe-l'œil"], "Les restes d'un repas fixés sur la table, puis accrochés au mur", "Un moment de vie réel devient œuvre."),
]),
notion('AM-5', 0, F, 'art-fontaine-duchamp', [
  Q("Quel objet Marcel Duchamp a-t-il présenté en 1917 sous le titre Fontaine ?", ["Un urinoir", "Une fontaine de jardin", "Un lavabo en marbre", "Un seau"], "Un urinoir", "L'objet, signé « R. Mutt », est refusé par l'exposition."),
  Q("Que montre le ready-made sur le statut de l'œuvre ?", ["Que le choix de l'artiste et le lieu d'exposition peuvent faire d'un objet une œuvre", "Qu'une œuvre doit être faite à la main", "Qu'une œuvre doit être belle", "Qu'un objet ne peut jamais être une œuvre"], "Que le choix de l'artiste et le lieu d'exposition peuvent faire d'un objet une œuvre", "Duchamp déplace la question de l'art vers l'idée."),
  Q("Quel ready-made de Duchamp (1913) associe une roue à un tabouret ?", ["Roue de bicyclette", "Porte-bouteilles", "Fontaine", "L.H.O.O.Q."], "Roue de bicyclette", "C'est souvent considéré comme son premier ready-made."),
]),
notion('AM-5', 0, I, 'art-objet-musee', [
  Q("Qu'est-ce que le design ?", ["La conception d'objets qui allient fonction et esthétique", "La restauration de tableaux anciens", "La peinture murale", "L'étude des pigments"], "La conception d'objets qui allient fonction et esthétique", "Des objets de design entrent dans les collections des musées."),
  Q("Quel fauteuil en tubes d'acier, conçu par Marcel Breuer en 1925, est une icône du design ?", ["Le fauteuil Wassily", "Le fauteuil Voltaire", "La chaise Louis XV", "Le pouf Chesterfield"], "Le fauteuil Wassily", "Il a été conçu au Bauhaus."),
  Q("Pourquoi un musée conserve-t-il des objets qui n'ont pas été créés comme des œuvres (outils, vêtements) ?", ["Comme témoins d'une culture : ils deviennent objets d'étude", "Pour les revendre", "Pour décorer les couloirs", "Parce qu'ils sont tous en or"], "Comme témoins d'une culture : ils deviennent objets d'étude", "Le statut d'un objet dépend du regard porté sur lui."),
]),
notion('AM-6', 0, F, 'art-outils-numeriques', [
  Q("Quel outil permet de dessiner directement sur un écran ou une surface sensible avec un stylet ?", ["Une tablette graphique", "Un scanner", "Une imprimante", "Un vidéoprojecteur"], "Une tablette graphique", "Elle reproduit le geste du dessin dans un logiciel."),
  Q("À quoi servent les calques dans un logiciel de dessin ?", ["À travailler séparément sur plusieurs couches d'une même image", "À imprimer en couleur", "À éteindre l'écran", "À envoyer l'image par courriel"], "À travailler séparément sur plusieurs couches d'une même image", "On peut modifier une couche sans toucher aux autres."),
  Q("Quelle possibilité du numérique n'existe pas en peinture traditionnelle ?", ["Annuler une action et revenir à un état antérieur de l'image", "Mélanger deux couleurs", "Tracer une ligne", "Choisir un format"], "Annuler une action et revenir à un état antérieur de l'image", "Le numérique garde en mémoire les différents états de l'œuvre."),
]),
notion('AM-6', 0, I, 'art-code-creatif', [
  Q("Comment appelle-t-on une œuvre produite à partir de règles programmées, souvent avec une part de hasard ?", ["De l'art génératif", "De l'art pariétal", "Du street art", "De l'art brut"], "De l'art génératif", "L'artiste écrit les règles, la machine produit les formes."),
  Q("Quel langage de programmation, créé pour les artistes et les designers, sert à produire des images ?", ["Processing", "Excel", "PowerPoint", "Word"], "Processing", "Il a été créé en 2001 pour enseigner la création par le code."),
  Q("Qu'est-ce qu'un « glitch » utilisé dans l'art numérique ?", ["Une erreur visuelle ou un bug volontairement exploité", "Un pinceau numérique", "Un format d'image", "Un écran tactile"], "Une erreur visuelle ou un bug volontairement exploité", "Le défaut technique devient matériau expressif."),
]),
notion('AM-6', 0, I, 'art-energie-numerique', [
  Q("Pourquoi porter un regard critique sur le coût énergétique des créations numériques ?", ["Parce que le calcul, le stockage et la diffusion des fichiers consomment de l'électricité", "Parce que le numérique ne consomme rien", "Parce que les écrans sont fragiles", "Parce que les logiciels sont gratuits"], "Parce que le calcul, le stockage et la diffusion des fichiers consomment de l'électricité", "Le programme invite à ce regard critique."),
  Q("Lequel de ces usages consomme particulièrement beaucoup d'énergie ?", ["La génération d'images par intelligence artificielle et la vidéo en haute définition", "Le dessin au crayon", "La lecture d'un livre papier", "La peinture à l'eau"], "La génération d'images par intelligence artificielle et la vidéo en haute définition", "Ces usages mobilisent d'importants serveurs."),
  Q("Quel choix réduit l'empreinte d'une création numérique ?", ["Éviter les fichiers inutilement lourds et les copies multiples", "Augmenter toujours la résolution au maximum", "Stocker chaque version en ligne", "Diffuser en boucle des vidéos 4K"], "Éviter les fichiers inutilement lourds et les copies multiples", "La sobriété numérique concerne aussi la création."),
]),
notion('AM-6', 0, D, 'art-traditionnel-numerique', [
  Q("Quel peintre britannique a réalisé des paysages sur iPad, exposés en très grand format ?", ["David Hockney", "William Turner", "Francis Bacon", "John Constable"], "David Hockney", "Il fait dialoguer peinture traditionnelle et outils numériques."),
  Q("Comment appelle-t-on la projection d'images sur une façade ou un objet, qui épouse ses reliefs ?", ["Le mapping vidéo", "Le pochoir", "La fresque", "Le vitrail"], "Le mapping vidéo", "On le voit lors des fêtes de la lumière, à Lyon par exemple."),
  Q("Qu'est-ce que la numérisation d'une œuvre ?", ["Sa reproduction en fichier numérique, par scanner ou photographie haute définition", "Sa destruction", "Sa vente aux enchères", "Sa restauration à la main"], "Sa reproduction en fichier numérique, par scanner ou photographie haute définition", "Elle facilite l'étude et la diffusion, sans remplacer l'œuvre."),
]),
# ══ L'œuvre, l'espace, l'auteur, le spectateur ══
notion('AE-1', 0, D, 'art-corps-artistes', [
  Q("Quelle artiste a réalisé la performance The Artist Is Present au MoMA de New York en 2010 ?", ["Marina Abramović", "Frida Kahlo", "Louise Bourgeois", "Yayoi Kusama"], "Marina Abramović", "Elle est restée assise des centaines d'heures face aux visiteurs."),
  Q("Quel artiste français utilisait des modèles enduites de peinture comme « pinceaux vivants » dans ses Anthropométries ?", ["Yves Klein", "Jean Dubuffet", "Henri Matisse", "Fernand Léger"], "Yves Klein", "Le corps laisse directement sa trace sur la toile."),
  Q("Quel peintre américain projetait la peinture sur une toile posée au sol (dripping) ?", ["Jackson Pollock", "Andy Warhol", "Edward Hopper", "Mark Rothko"], "Jackson Pollock", "Tout son corps participe au geste pictural."),
]),
notion('AE-4', 0, F, 'art-video', [
  Q("Quel artiste coréen est considéré comme le père de l'art vidéo ?", ["Nam June Paik", "Takashi Murakami", "Ai Weiwei", "Hokusai"], "Nam June Paik", "Il crée dès les années 1960 des œuvres avec des téléviseurs."),
  Q("Comment appelle-t-on une œuvre qui utilise des écrans et des images en mouvement dans l'espace ?", ["Une installation vidéo", "Une nature morte", "Un bas-relief", "Une gravure"], "Une installation vidéo", "Le spectateur la parcourt dans l'espace."),
  Q("Qu'est-ce qu'une œuvre en réalité virtuelle ?", ["Une œuvre que le spectateur explore avec un casque, dans un espace simulé", "Une peinture très réaliste", "Une sculpture en marbre", "Une photographie ancienne"], "Une œuvre que le spectateur explore avec un casque, dans un espace simulé", "Elle mêle présence virtuelle et expérience du corps."),
]),
notion('AE-4', 0, I, 'art-sciences-techniques', [
  Q("Quel artiste de la Renaissance mêlait art et sciences dans ses carnets (anatomie, machines volantes) ?", ["Léonard de Vinci", "Botticelli", "Le Caravage", "Raphaël"], "Léonard de Vinci", "Art et sciences se croisent depuis longtemps."),
  Q("Quel artiste américain a créé les « mobiles », sculptures suspendues mises en mouvement par l'air ?", ["Alexander Calder", "Jeff Koons", "Keith Haring", "Roy Lichtenstein"], "Alexander Calder", "C'est Marcel Duchamp qui leur a donné ce nom."),
  Q("Quel matériau lumineux Dan Flavin utilise-t-il pour ses installations ?", ["Des tubes fluorescents (néons)", "Des bougies", "Des miroirs", "Des vitraux"], "Des tubes fluorescents (néons)", "La lumière électrique devient matériau de l'œuvre."),
]),
notion('AE-4', 0, D, 'art-auteur-numerique', [
  Q("Quel collectif japonais est connu pour ses installations numériques immersives et interactives ?", ["teamLab", "Studio Ghibli", "Gutai", "Fluxus"], "teamLab", "Ses espaces réagissent à la présence et aux gestes des visiteurs."),
  Q("En quoi le numérique transforme-t-il la notion d'auteur ?", ["L'artiste conçoit souvent des règles ou des programmes plutôt qu'une forme définitive, parfois à plusieurs", "Il supprime toute intention artistique", "Il interdit le travail collectif", "Il impose de signer chaque pixel"], "L'artiste conçoit souvent des règles ou des programmes plutôt qu'une forme définitive, parfois à plusieurs", "Œuvres génératives, collaboratives ou interactives en sont des exemples."),
  Q("Qu'est-ce qu'un NFT sur le marché de l'art ?", ["Un certificat numérique d'authenticité et de propriété enregistré sur une chaîne de blocs", "Une nouvelle technique de peinture", "Un format d'impression", "Une école d'art"], "Un certificat numérique d'authenticité et de propriété enregistré sur une chaîne de blocs", "Il a fait évoluer, un temps, la vente d'œuvres numériques."),
]),
]

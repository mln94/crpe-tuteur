# Arts plastiques · La matérialité de l'œuvre ; l'objet et l'œuvre : 25 questions par niveau et par point du programme
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ AM-1 · La transformation de la matière ══
notion('AM-1', 0, F, 'artm-outils-peintre', [
  Q("Sur quoi le peintre mélange-t-il ses couleurs ?", ["Une palette", "Un chevalet", "Une toile", "Un cadre"], "Une palette", "Le chevalet tient la toile."),
  Q("Qu'est-ce qu'un chevalet ?", ["Un support qui maintient le tableau pendant qu'on peint", "Un petit cheval", "Un pinceau large", "Un pot de peinture"], "Un support qui maintient le tableau pendant qu'on peint", "Il permet de peindre debout."),
  Q("Qu'est-ce qu'une brosse en peinture ?", ["Un pinceau aux poils raides", "Une éponge", "Un couteau", "Un rouleau"], "Un pinceau aux poils raides", "Elle laisse des traces visibles."),
]),
notion('AM-1', 0, F, 'artm-gouache-pastel', [
  Q("Qu'est-ce que la gouache ?", ["Une peinture à l'eau opaque", "Une peinture à l'huile", "Une encre transparente", "Un crayon"], "Une peinture à l'eau opaque", "L'aquarelle est transparente."),
  Q("Qu'est-ce qu'un pastel ?", ["Un bâtonnet de pigment pressé, utilisé comme un crayon", "Une pâtisserie", "Un vernis", "Une toile"], "Un bâtonnet de pigment pressé, utilisé comme un crayon", "Degas l'utilisait beaucoup."),
  Q("Avec quoi peut-on estomper un trait de pastel ou de fusain ?", ["Avec le doigt ou une estompe", "Avec de l'eau", "Avec un marteau", "Avec du vernis"], "Avec le doigt ou une estompe", "On crée ainsi des dégradés."),
]),
notion('AM-1', 0, F, 'artm-modelage', [
  Q("Qu'est-ce que le modelage ?", ["Façonner une matière molle comme l'argile avec les mains", "Tailler la pierre", "Peindre un modèle", "Graver le bois"], "Façonner une matière molle comme l'argile avec les mains", "On ajoute et retire de la matière."),
  Q("Comment rend-on une sculpture en argile solide et durable ?", ["En la cuisant au four", "En la peignant", "En la mouillant", "En la congelant"], "En la cuisant au four", "Elle devient de la terre cuite."),
  Q("Comment appelle-t-on l'argile cuite ?", ["La terre cuite", "Le plâtre", "Le bronze", "Le marbre"], "La terre cuite", "Les Tanagras grecques sont en terre cuite."),
]),
notion('AM-1', 0, F, 'artm-encre', [
  Q("Qu'est-ce que le lavis ?", ["Une technique d'encre diluée à l'eau, en dégradés", "Un lavage de pinceaux", "Une peinture à l'huile", "Une gravure"], "Une technique d'encre diluée à l'eau, en dégradés", "L'encre de Chine s'y prête bien."),
  Q("Quel outil traditionnel sert à écrire et dessiner à l'encre ?", ["La plume", "Le burin", "La gouge", "Le ciseau"], "La plume", "On la trempe dans l'encre."),
  Q("Quelle encre noire, très utilisée en Asie et en Europe, est faite de noir de fumée ?", ["L'encre de Chine", "L'encre sympathique", "L'encre bleue", "L'encre d'imprimerie"], "L'encre de Chine", "Elle est très résistante."),
]),
notion('AM-1', 0, F, 'artm-taille-pierre', [
  Q("Quel outil le sculpteur utilise-t-il pour tailler la pierre ?", ["Un ciseau et un maillet", "Un pinceau", "Une éponge", "Un rouleau"], "Un ciseau et un maillet", "On frappe le ciseau avec le maillet."),
  Q("Quel marbre blanc italien a été utilisé par Michel-Ange ?", ["Le marbre de Carrare", "Le marbre noir", "Le granit", "Le grès"], "Le marbre de Carrare", "Le David y a été taillé."),
  Q("La taille est-elle une technique où l'on peut ajouter de la matière ?", ["Non, on ne peut qu'en enlever", "Oui, toujours", "Seulement en bois", "Seulement en argile"], "Non, on ne peut qu'en enlever", "Le modelage permet d'en ajouter."),
]),
notion('AM-1', 0, F, 'artm-traces-gestes', [
  Q("Qu'est-ce qu'une empreinte ?", ["La trace laissée par la pression d'un objet ou du corps sur une surface", "Une photo", "Un dessin au compas", "Une sculpture"], "La trace laissée par la pression d'un objet ou du corps sur une surface", "Les mains négatives préhistoriques en sont un exemple."),
  Q("Comment ont été réalisées les mains négatives des grottes préhistoriques ?", ["En soufflant du pigment autour d'une main posée sur la paroi", "En peignant au pinceau", "En gravant la pierre", "En collant du papier"], "En soufflant du pigment autour d'une main posée sur la paroi", "La grotte Cosquer en contient beaucoup."),
  Q("Que montre la touche d'un peintre ?", ["La trace visible de son pinceau, sa manière", "La signature", "Le prix du tableau", "Le cadre"], "La trace visible de son pinceau, sa manière", "Celle de Van Gogh est très reconnaissable."),
]),
notion('AM-1', 0, I, 'artm-huile-acrylique', [
  Q("Quel liant compose la peinture à l'huile ?", ["L'huile de lin", "L'eau", "L'œuf", "La colle"], "L'huile de lin", "Elle sèche lentement."),
  Q("Quelle peinture synthétique, apparue au XXe siècle, sèche vite et se dilue à l'eau ?", ["L'acrylique", "L'huile", "La tempera", "La fresque"], "L'acrylique", "Elle devient imperméable en séchant."),
  Q("Quel liant utilisait-on pour la tempera au Moyen Âge ?", ["Le jaune d'œuf", "L'huile de lin", "Le pétrole", "Le miel"], "Le jaune d'œuf", "Elle précède la peinture à l'huile."),
]),
notion('AM-1', 0, I, 'artm-empatement-glacis', [
  Q("Qu'est-ce qu'un empâtement ?", ["Une couche de peinture épaisse qui forme un relief", "Une couche très fine", "Une tache d'eau", "Un vernis"], "Une couche de peinture épaisse qui forme un relief", "Van Gogh en utilise beaucoup."),
  Q("Qu'est-ce qu'un glacis ?", ["Une couche de peinture fine et transparente", "Une couche épaisse", "Une sculpture de glace", "Un fond blanc"], "Une couche de peinture fine et transparente", "On superpose plusieurs glacis pour la profondeur."),
  Q("Qu'est-ce que le sfumato de Léonard de Vinci ?", ["Un modelé vaporeux aux contours adoucis", "Un contraste violent", "Une couleur vive", "Un collage"], "Un modelé vaporeux aux contours adoucis", "On le voit sur le visage de La Joconde."),
]),
notion('AM-1', 0, I, 'artm-fonte-bronze', [
  Q("Quelle technique de fonte utilise un modèle en cire qui disparaît ?", ["La fonte à la cire perdue", "Le moulage en plâtre", "La taille directe", "Le modelage"], "La fonte à la cire perdue", "Le métal prend la place de la cire."),
  Q("Pourquoi peut-il exister plusieurs exemplaires d'une sculpture en bronze ?", ["On peut couler plusieurs fois le même moule", "On copie à la main", "Le bronze se divise", "Ce n'est pas possible"], "On peut couler plusieurs fois le même moule", "En France, on limite à 12 exemplaires originaux."),
  Q("Qu'est-ce que la patine d'un bronze ?", ["La couleur de surface obtenue par oxydation ou traitement", "Le socle", "La signature", "Un défaut de fonte"], "La couleur de surface obtenue par oxydation ou traitement", "Elle peut être verte, brune ou noire."),
]),
notion('AM-1', 0, I, 'artm-dripping-gestes', [
  Q("Quelle technique laisse couler la peinture sur une toile au sol ?", ["Le dripping", "Le sfumato", "Le glacis", "La fresque"], "Le dripping", "Jackson Pollock l'a rendue célèbre."),
  Q("Comment appelle-t-on la technique de Max Ernst consistant à gratter la peinture sur une toile posée sur des objets ?", ["Le grattage", "Le frottage", "Le collage", "La décalcomanie"], "Le grattage", "Le frottage se fait au crayon sur papier."),
  Q("Qu'est-ce que la décalcomanie surréaliste ?", ["Presser une feuille sur de la peinture fraîche puis la décoller pour obtenir des formes", "Coller des autocollants", "Copier une image", "Graver un métal"], "Presser une feuille sur de la peinture fraîche puis la décoller pour obtenir des formes", "Oscar Domínguez l'a inventée."),
]),
notion('AM-1', 0, I, 'artm-ceramique', [
  Q("Qu'est-ce que la céramique ?", ["L'art de façonner et cuire l'argile", "La peinture sur toile", "La gravure sur bois", "La photographie"], "L'art de façonner et cuire l'argile", "Poterie, faïence, porcelaine…"),
  Q("Qu'est-ce qu'une émaillure (émail) sur une céramique ?", ["Un revêtement vitreux coloré cuit sur la pièce", "Une fissure", "Une signature", "Un socle"], "Un revêtement vitreux coloré cuit sur la pièce", "Il rend la pièce imperméable et brillante."),
  Q("Quelle ville chinoise est célèbre depuis des siècles pour sa porcelaine ?", ["Jingdezhen", "Pékin", "Shanghai", "Canton"], "Jingdezhen", "La porcelaine chinoise s'exportait dans le monde entier."),
]),
notion('AM-1', 0, D, 'artm-fresque-technique', [
  Q("Pourquoi faut-il peindre rapidement une fresque ?", ["Les pigments doivent pénétrer l'enduit avant qu'il sèche", "La peinture explose", "Le mur tombe", "La lumière s'en va"], "Les pigments doivent pénétrer l'enduit avant qu'il sèche", "On travaille par « journées »."),
  Q("Comment appelle-t-on la partie d'enduit préparée pour une journée de fresque ?", ["Une giornata", "Un carton", "Une esquisse", "Une sinopia"], "Une giornata", "On voit parfois les raccords."),
  Q("Qu'est-ce que la sinopia ?", ["Le dessin préparatoire à l'ocre rouge sous une fresque", "Un pigment bleu", "Un pinceau", "Une colle"], "Le dessin préparatoire à l'ocre rouge sous une fresque", "Le nom vient de Sinope, d'où venait le pigment."),
]),
notion('AM-1', 0, D, 'artm-taille-directe', [
  Q("Qu'est-ce que la taille directe ?", ["Tailler la matière sans modèle préalable, en suivant le matériau", "Copier une sculpture", "Mouler du plâtre", "Fondre du bronze"], "Tailler la matière sans modèle préalable, en suivant le matériau", "Brancusi la défendait."),
  Q("Quel sculpteur britannique a percé ses sculptures de grands trous, en dialogue avec le paysage ?", ["Henry Moore", "Antony Gormley", "Anish Kapoor", "Barbara Hepworth"], "Henry Moore", "Barbara Hepworth aussi."),
  Q("Qu'est-ce qu'une mise aux points en sculpture ?", ["Une méthode pour reporter les mesures d'un modèle sur un bloc", "Un réglage de lumière", "Une signature", "Un polissage"], "Une méthode pour reporter les mesures d'un modèle sur un bloc", "Les praticiens l'utilisaient pour Rodin."),
]),
notion('AM-1', 0, D, 'artm-matiere-picturale', [
  Q("Quel peintre a mélangé sable, plâtre et goudron à sa peinture (hautes pâtes) ?", ["Jean Dubuffet", "Claude Monet", "Raphaël", "Ingres"], "Jean Dubuffet", "Il valorise la matière brute."),
  Q("Quel artiste italien a utilisé des sacs de toile de jute rapiécés comme tableaux ?", ["Alberto Burri", "Lucio Fontana", "Piero Manzoni", "Giorgio Morandi"], "Alberto Burri", "Il a aussi brûlé du plastique."),
  Q("Quel artiste allemand intègre paille, plomb et cendres dans ses grandes toiles ?", ["Anselm Kiefer", "Gerhard Richter", "Joseph Beuys", "Georg Baselitz"], "Anselm Kiefer", "Ses œuvres évoquent l'histoire et la mémoire."),
]),
notion('AM-1', 0, D, 'artm-feu-fumee', [
  Q("Quel artiste a peint avec la fumée d'une bougie (fumage) ?", ["Wolfgang Paalen", "Claude Monet", "Henri Matisse", "Paul Klee"], "Wolfgang Paalen", "Technique surréaliste."),
  Q("Quel artiste a utilisé un lance-flammes pour ses « peintures de feu » ?", ["Yves Klein", "Pierre Soulages", "Jackson Pollock", "Andy Warhol"], "Yves Klein", "Il collabore avec Gaz de France en 1961."),
  Q("Quel artiste chinois crée des œuvres avec de la poudre à canon et des feux d'artifice ?", ["Cai Guo-Qiang", "Ai Weiwei", "Zao Wou-Ki", "Yue Minjun"], "Cai Guo-Qiang", "Il a conçu les feux d'artifice des JO de Pékin 2008."),
]),
notion('AM-1', 0, D, 'artm-geste-performance', [
  Q("Quel mouvement japonais des années 1950 explorait le geste et la matière, parfois avec le corps entier ?", ["Gutai", "Fluxus", "Mono-ha", "Supports/Surfaces"], "Gutai", "Kazuo Shiraga peignait avec ses pieds."),
  Q("Quel peintre français jetait de la peinture sur la toile avec une grande rapidité devant le public ?", ["Georges Mathieu", "Pierre Bonnard", "Henri Matisse", "Raoul Dufy"], "Georges Mathieu", "Il parle de « vitesse d'exécution »."),
  Q("Qu'est-ce que l'action painting ?", ["Une peinture où le geste et l'action de peindre sont essentiels", "Un film d'action", "Une peinture de batailles", "Une peinture de sport"], "Une peinture où le geste et l'action de peindre sont essentiels", "Le terme est du critique Harold Rosenberg."),
]),
notion('AM-1', 0, D, 'artm-restauration', [
  Q("Que fait un restaurateur d'œuvres d'art ?", ["Il conserve et répare les œuvres en respectant l'original", "Il repeint l'œuvre à sa façon", "Il vend les œuvres", "Il crée des copies"], "Il conserve et répare les œuvres en respectant l'original", "Ses interventions doivent être réversibles."),
  Q("Quel monument parisien a été restauré après l'incendie de 2019 ?", ["Notre-Dame de Paris", "La tour Eiffel", "Le Sacré-Cœur", "Le Panthéon"], "Notre-Dame de Paris", "Elle a rouvert en décembre 2024."),
  Q("Quel outil permet de voir les dessins cachés sous la couche de peinture d'un tableau ?", ["La réflectographie infrarouge", "Le microscope optique", "La loupe", "Le scanner de livres"], "La réflectographie infrarouge", "Elle révèle les repentirs."),
]),
notion('AM-1', 0, D, 'artm-repentirs', [
  Q("Qu'est-ce qu'un repentir en peinture ?", ["Une modification faite par l'artiste en cours de réalisation", "Une excuse publique", "Une copie", "Une restauration"], "Une modification faite par l'artiste en cours de réalisation", "Il devient parfois visible avec le temps."),
  Q("Comment appelle-t-on la couche de préparation blanche posée sur la toile avant de peindre ?", ["L'apprêt (enduit)", "Le vernis", "Le glacis", "Le fixatif"], "L'apprêt (enduit)", "On utilise souvent du gesso."),
  Q("À quoi sert le vernis final sur un tableau ?", ["À protéger la peinture et uniformiser la brillance", "À la colorer en jaune", "À la sécher", "À la signer"], "À protéger la peinture et uniformiser la brillance", "Il jaunit avec le temps."),
]),
notion('AM-1', 0, D, 'artm-gravure-taille-douce', [
  Q("Qu'est-ce que la taille-douce ?", ["Une gravure en creux sur métal, où l'encre se loge dans les sillons", "Une gravure sur bois en relief", "Une sculpture tendre", "Un dessin au crayon"], "Une gravure en creux sur métal, où l'encre se loge dans les sillons", "Burin, eau-forte, pointe sèche."),
  Q("Qu'est-ce que l'eau-forte ?", ["Une gravure où l'acide creuse le métal", "Une boisson", "Une aquarelle", "Un vernis"], "Une gravure où l'acide creuse le métal", "Rembrandt en était un maître."),
  Q("Qu'est-ce que la lithographie ?", ["Une impression à partir d'un dessin sur pierre calcaire", "Une gravure sur bois", "Une sculpture en pierre", "Une photo"], "Une impression à partir d'un dessin sur pierre calcaire", "Toulouse-Lautrec l'utilisait pour ses affiches."),
]),
notion('AM-1', 0, D, 'artm-moulage-tirage', [
  Q("Qu'est-ce qu'un tirage en sculpture ?", ["Un exemplaire obtenu à partir d'un moule", "Une loterie", "Un dessin", "Une gravure"], "Un exemplaire obtenu à partir d'un moule", "On parle de premier tirage, d'épreuve d'artiste…"),
  Q("Quel matériau utilise-t-on souvent pour les moules en atelier ?", ["Le plâtre ou l'élastomère", "Le verre", "Le papier", "Le marbre"], "Le plâtre ou l'élastomère", "Ils reproduisent fidèlement les détails."),
  Q("Quel sculpteur a coulé ses œuvres dans du bronze, et dont le musée parisien conserve aussi les plâtres ?", ["Auguste Rodin", "Michel-Ange", "Bernin", "Canova"], "Auguste Rodin", "Le musée Rodin est installé à l'hôtel Biron."),
]),
# ══ AM-2 · Les qualités physiques des matériaux ══
notion('AM-2', 0, F, 'artm-materiaux-durs-mous', [
  Q("Lequel de ces matériaux est souple ?", ["Le tissu", "La pierre", "Le métal", "Le verre"], "Le tissu", "On peut le plier et le coudre."),
  Q("Lequel de ces matériaux est transparent ?", ["Le verre", "Le bois", "Le carton", "La pierre"], "Le verre", "Il laisse passer la lumière."),
  Q("Quel matériau est opaque ?", ["Le bois", "Le verre", "Le calque", "L'eau claire"], "Le bois", "Il ne laisse pas passer la lumière."),
]),
notion('AM-2', 0, F, 'artm-bois', [
  Q("Quel outil sert à sculpter le bois en creusant ?", ["La gouge", "Le pinceau", "Le fusain", "La palette"], "La gouge", "On l'utilise aussi pour la gravure sur bois."),
  Q("Quelle œuvre célèbre est un totem sculpté dans le bois ?", ["Un mât totémique amérindien", "La Joconde", "Le Penseur", "La Vénus de Milo"], "Un mât totémique amérindien", "Les peuples de la côte nord-ouest en sculptent."),
  Q("Que signifie « le fil du bois » ?", ["Le sens des fibres du bois", "Une ficelle en bois", "Un outil", "Un type d'arbre"], "Le sens des fibres du bois", "Il faut en tenir compte pour tailler."),
]),
notion('AM-2', 0, F, 'artm-papier-carton', [
  Q("Qu'est-ce que le papier mâché ?", ["Du papier mélangé à de la colle et modelé", "Du papier coupé", "Du papier brûlé", "Du papier peint"], "Du papier mélangé à de la colle et modelé", "On peut faire des masques."),
  Q("Quelle technique japonaise consiste à plier le papier pour créer des formes ?", ["L'origami", "Le kirigami", "L'ikebana", "Le manga"], "L'origami", "Le kirigami ajoute des découpes."),
  Q("Quel matériau, à base de carton, est souvent utilisé en classe pour des maquettes ?", ["Le carton plume", "Le marbre", "Le bronze", "L'or"], "Le carton plume", "Il est léger et facile à découper."),
]),
notion('AM-2', 0, F, 'artm-metal', [
  Q("Quel métal, jaune et précieux, est utilisé en feuille pour dorer les œuvres ?", ["L'or", "Le fer", "Le plomb", "L'aluminium"], "L'or", "On parle de feuille d'or."),
  Q("Quel monument parisien est en fer puddlé ?", ["La tour Eiffel", "Notre-Dame", "L'Arc de triomphe", "Le Louvre"], "La tour Eiffel", "Elle pèse environ 10 000 tonnes."),
  Q("Quelle technique assemble deux pièces de métal en les faisant fondre localement ?", ["La soudure", "Le collage", "Le cousu", "Le tressage"], "La soudure", "Le sculpteur Julio González l'a utilisée."),
]),
notion('AM-2', 0, F, 'artm-textile', [
  Q("Qu'est-ce qu'une tapisserie ?", ["Un tissu décoratif tissé à la main, souvent mural", "Un papier peint", "Un tapis de sol", "Une peinture"], "Un tissu décoratif tissé à la main, souvent mural", "Les tapisseries d'Aubusson sont célèbres."),
  Q("Quelle série de tapisseries médiévales montre une dame et une licorne ?", ["La Dame à la licorne", "La tapisserie de Bayeux", "L'Apocalypse d'Angers", "Les Gobelins"], "La Dame à la licorne", "Elle est au musée de Cluny à Paris."),
  Q("Qu'est-ce que la broderie ?", ["Un décor cousu au fil sur un tissu", "Une peinture sur soie", "Une gravure", "Un tissage mécanique"], "Un décor cousu au fil sur un tissu", "La tapisserie de Bayeux est en réalité une broderie."),
]),
notion('AM-2', 0, F, 'artm-verre', [
  Q("Quelle île de Venise est célèbre pour son verre soufflé ?", ["Murano", "Burano", "Le Lido", "Torcello"], "Murano", "Les verriers y travaillent depuis le Moyen Âge."),
  Q("Comment façonne-t-on le verre soufflé ?", ["En soufflant dans une canne au bout de laquelle se trouve du verre en fusion", "En le taillant à froid", "En le coulant dans du sable mouillé", "En le collant"], "En soufflant dans une canne au bout de laquelle se trouve du verre en fusion", "Le verre est chauffé à plus de 1 000 °C."),
  Q("Quel artiste américain crée des sculptures en verre soufflé très colorées, comme des lustres géants ?", ["Dale Chihuly", "Jeff Koons", "Andy Warhol", "Alexander Calder"], "Dale Chihuly", "Ses œuvres ornent des plafonds et des jardins."),
]),
notion('AM-2', 0, F, 'artm-recup', [
  Q("Que signifie utiliser des matériaux de récupération en art ?", ["Réutiliser des objets ou déchets pour créer", "Acheter des matériaux neufs", "Voler des matériaux", "N'utiliser que de l'or"], "Réutiliser des objets ou déchets pour créer", "C'est aussi un geste écologique."),
  Q("Comment appelle-t-on la transformation de déchets en objets de plus grande valeur ?", ["L'upcycling (surcyclage)", "Le recyclage industriel", "Le compost", "L'incinération"], "L'upcycling (surcyclage)", "De nombreux artistes le pratiquent."),
  Q("Quel artiste ghanéen crée d'immenses tentures avec des capsules de bouteilles ?", ["El Anatsui", "Romuald Hazoumè", "Kehinde Wiley", "Chéri Samba"], "El Anatsui", "Elles brillent comme du tissu métallique."),
]),
notion('AM-2', 0, F, 'artm-sensations', [
  Q("Que ressent-on en touchant une surface rugueuse ?", ["Une surface râpeuse, irrégulière", "Une surface lisse", "Une surface mouillée", "Une surface chaude"], "Une surface râpeuse, irrégulière", "Le toucher fait partie de l'expérience des matériaux."),
  Q("Comment appelle-t-on l'aspect de surface d'un matériau (lisse, granuleux…) ?", ["La texture", "La couleur", "La forme", "La taille"], "La texture", "On peut aussi la représenter en dessin."),
  Q("Quel adjectif décrit un matériau qui renvoie fortement la lumière ?", ["Brillant", "Mat", "Opaque", "Rugueux"], "Brillant", "Mat = sans reflet."),
]),
notion('AM-2', 0, I, 'artm-arte-povera', [
  Q("Quel artiste de l'arte povera a associé une Vénus antique et un tas de vieux vêtements ?", ["Michelangelo Pistoletto", "Mario Merz", "Giuseppe Penone", "Jannis Kounellis"], "Michelangelo Pistoletto", "La Vénus aux chiffons (1967)."),
  Q("Quel artiste de l'arte povera a exposé des chevaux vivants dans une galerie (1969) ?", ["Jannis Kounellis", "Pistoletto", "Penone", "Beuys"], "Jannis Kounellis", "Le vivant devient matériau."),
  Q("Quel artiste italien travaille l'arbre, le souffle et l'empreinte dans la nature ?", ["Giuseppe Penone", "Mario Merz", "Lucio Fontana", "Piero Manzoni"], "Giuseppe Penone", "Il a exposé au château de Versailles en 2013."),
]),
notion('AM-2', 0, I, 'artm-matiere-legerete', [
  Q("Quelle artiste française a créé des sculptures géantes en forme d'araignée en bronze ?", ["Louise Bourgeois", "Niki de Saint Phalle", "Camille Claudel", "Annette Messager"], "Louise Bourgeois", "Maman (1999)."),
  Q("Quel matériau donne une impression de légèreté à une sculpture monumentale ?", ["Un matériau ajouré ou transparent", "Un bloc de granit", "Un plomb épais", "Un béton plein"], "Un matériau ajouré ou transparent", "Le vide joue un rôle important."),
  Q("Quel artiste a enveloppé de tissu le Pont-Neuf en 1985 et l'Arc de triomphe en 2021 ?", ["Christo (et Jeanne-Claude)", "Daniel Buren", "JR", "Jean Tinguely"], "Christo (et Jeanne-Claude)", "Le tissu révèle la forme des monuments."),
]),
notion('AM-2', 0, I, 'artm-lumiere-materiau', [
  Q("Quel artiste américain crée des espaces où la lumière elle-même est le matériau ?", ["James Turrell", "Jackson Pollock", "Andy Warhol", "Jeff Koons"], "James Turrell", "Ses « skyspaces » ouvrent sur le ciel."),
  Q("Quel matériau lumineux utilisent Dan Flavin ou François Morellet ?", ["Le néon", "Le marbre", "Le bronze", "Le bois"], "Le néon", "Le néon colore l'espace."),
  Q("Quel artiste danois-islandais a installé un immense soleil artificiel à la Tate Modern (2003) ?", ["Olafur Eliasson", "James Turrell", "Anish Kapoor", "Ai Weiwei"], "Olafur Eliasson", "The Weather Project."),
]),
notion('AM-2', 0, I, 'artm-sculpture-molle', [
  Q("Quel artiste américain a créé des objets géants et mous, comme des interrupteurs en tissu ?", ["Claes Oldenburg", "Jeff Koons", "Alexander Calder", "Donald Judd"], "Claes Oldenburg", "On parle de « soft sculptures »."),
  Q("Quelle artiste française a créé des « Nanas » colorées en polyester ?", ["Niki de Saint Phalle", "Louise Bourgeois", "Sophie Calle", "Annette Messager"], "Niki de Saint Phalle", "Formes rondes et joyeuses."),
  Q("Que crée le contraste entre un objet dur représenté en matière molle ?", ["Un effet de surprise et de décalage", "Une parfaite ressemblance", "Aucun effet", "Une confusion technique"], "Un effet de surprise et de décalage", "Le matériau change le sens de l'objet."),
]),
notion('AM-2', 0, I, 'artm-matiere-vivante', [
  Q("Quel artiste réalise des œuvres éphémères avec des feuilles, des pierres et de la glace dans la nature ?", ["Andy Goldsworthy", "Jeff Koons", "Damien Hirst", "Anish Kapoor"], "Andy Goldsworthy", "Il les photographie avant qu'elles disparaissent."),
  Q("Comment appelle-t-on l'art réalisé dans et avec la nature ?", ["Le land art", "Le pop art", "L'op art", "L'art déco"], "Le land art", "Il naît aux États-Unis vers 1968."),
  Q("Quelle œuvre de land art de Robert Smithson est une spirale de pierres dans un lac salé ?", ["Spiral Jetty", "Lightning Field", "Sun Tunnels", "Double Negative"], "Spiral Jetty", "Elle se trouve dans l'Utah."),
]),
notion('AM-2', 0, I, 'artm-plastique-resine', [
  Q("Quel matériau a permis de nouvelles formes de sculpture et de design au XXe siècle ?", ["Le plastique", "Le marbre", "Le bronze", "La pierre"], "Le plastique", "Il peut être moulé facilement."),
  Q("Qu'est-ce que la résine en sculpture ?", ["Une matière synthétique qu'on coule et qui durcit", "Une colle à papier", "Une peinture à l'eau", "Un tissu"], "Une matière synthétique qu'on coule et qui durcit", "Elle peut être transparente."),
  Q("Pourquoi les œuvres en plastique posent-elles des problèmes de conservation ?", ["Le plastique vieillit, jaunit et peut se dégrader", "Il est trop solide", "Il est trop lourd", "Il ne craint rien"], "Le plastique vieillit, jaunit et peut se dégrader", "Les restaurateurs étudient ces matériaux."),
]),
notion('AM-2', 0, I, 'artm-pierre-matiere', [
  Q("Quelle pierre volcanique noire et brillante était utilisée par les Aztèques pour leurs miroirs ?", ["L'obsidienne", "Le marbre", "Le calcaire", "Le grès"], "L'obsidienne", "Elle se taille en lames très coupantes."),
  Q("Quelle pierre tendre et facile à tailler a servi à construire de nombreuses cathédrales ?", ["Le calcaire", "Le granit", "Le diamant", "L'obsidienne"], "Le calcaire", "La pierre de Caen en est un exemple."),
  Q("Pourquoi le granit est-il plus difficile à sculpter que le calcaire ?", ["Il est beaucoup plus dur", "Il est plus mou", "Il est transparent", "Il est liquide"], "Il est beaucoup plus dur", "Les calvaires bretons sont en granit."),
]),
notion('AM-2', 0, D, 'artm-materiaux-symboliques', [
  Q("Pourquoi l'or est-il utilisé dans les icônes et les retables ?", ["Il évoque la lumière divine et la richesse", "Il est bon marché", "Il est facile à trouver", "Il est transparent"], "Il évoque la lumière divine et la richesse", "Le fond d'or crée un espace sacré."),
  Q("Quel artiste a exposé des tonnes de bonbons emballés que le public peut emporter, en hommage à son compagnon ?", ["Félix González-Torres", "Damien Hirst", "Jeff Koons", "Maurizio Cattelan"], "Félix González-Torres", "Le poids initial était celui de son compagnon."),
  Q("Pourquoi Wolfgang Laib utilise-t-il du pollen dans ses installations ?", ["Pour sa fragilité, sa lumière et sa dimension de vie", "Parce qu'il est solide", "Parce qu'il est noir", "Par hasard"], "Pour sa fragilité, sa lumière et sa dimension de vie", "Il le récolte lui-même."),
]),
notion('AM-2', 0, D, 'artm-ephemere', [
  Q("Qu'est-ce qu'une œuvre éphémère ?", ["Une œuvre qui n'est pas destinée à durer", "Une œuvre très ancienne", "Une œuvre en bronze", "Une œuvre volée"], "Une œuvre qui n'est pas destinée à durer", "Sculptures de sable, de glace, performances…"),
  Q("Comment conserve-t-on souvent le souvenir d'une œuvre éphémère ?", ["Par la photographie et la vidéo", "En la congelant", "En la peignant", "On ne la conserve pas"], "Par la photographie et la vidéo", "Le document prend alors une grande importance."),
  Q("Quel artiste a mis en scène sa propre merde en boîte de conserve (Merda d'artista, 1961) ?", ["Piero Manzoni", "Marcel Duchamp", "Andy Warhol", "Joseph Beuys"], "Piero Manzoni", "Il critique le marché de l'art."),
]),
notion('AM-2', 0, D, 'artm-acier-corten', [
  Q("Quel acier, qui rouille en surface pour se protéger, est utilisé par Richard Serra ?", ["L'acier Corten", "L'acier inoxydable", "L'aluminium", "Le titane"], "L'acier Corten", "Sa couleur orangée évolue avec le temps."),
  Q("Quel sculpteur américain a installé de grandes plaques d'acier courbes au musée Guggenheim de Bilbao ?", ["Richard Serra", "Alexander Calder", "Jeff Koons", "Donald Judd"], "Richard Serra", "The Matter of Time (2005)."),
  Q("De quel matériau est recouvert le musée Guggenheim de Bilbao ?", ["De titane", "De marbre", "De verre", "De bois"], "De titane", "Il est dessiné par Frank Gehry."),
]),
notion('AM-2', 0, D, 'artm-sculpture-poids', [
  Q("Quel sculpteur américain a posé au sol des plaques de métal sur lesquelles on peut marcher ?", ["Carl Andre", "Richard Serra", "Donald Judd", "Dan Flavin"], "Carl Andre", "La sculpture devient sol."),
  Q("Quelle œuvre de Carl Andre est composée de 120 briques alignées ?", ["Equivalent VIII", "Fountain", "Spiral Jetty", "Untitled (Cubes)"], "Equivalent VIII", "Son achat par la Tate en 1972 a fait scandale."),
  Q("Pourquoi certaines sculptures modernes n'ont-elles pas de socle ?", ["Pour partager l'espace du spectateur", "Par économie", "Parce qu'elles sont trop légères", "Par oubli"], "Pour partager l'espace du spectateur", "La sculpture descend de son piédestal."),
]),
notion('AM-2', 0, D, 'artm-sculpture-sonore', [
  Q("Quels frères français ont créé des sculptures sonores en métal et en verre ?", ["Les frères Baschet", "Les frères Lumière", "Les frères Goncourt", "Les frères Montgolfier"], "Les frères Baschet", "Le public peut en jouer."),
  Q("Qu'est-ce qu'une sculpture sonore ?", ["Une sculpture qui produit des sons", "Une sculpture d'instrument", "Une sculpture silencieuse", "Une sculpture d'oreille"], "Une sculpture qui produit des sons", "Le matériau vibre."),
  Q("Pourquoi certains matériaux comme le métal ou le verre sont-ils sonores ?", ["Ils vibrent facilement quand on les frappe", "Ils sont lourds", "Ils sont transparents", "Ils sont chauds"], "Ils vibrent facilement quand on les frappe", "La matière a des qualités physiques variées."),
]),
notion('AM-2', 0, D, 'artm-ceramique-contemporaine', [
  Q("Quel artiste britannique, lauréat du Turner Prize, crée des vases en céramique ornés de scènes contemporaines ?", ["Grayson Perry", "Damien Hirst", "Banksy", "David Hockney"], "Grayson Perry", "Il apparaît parfois sous les traits de son double, Claire."),
  Q("Quelle technique japonaise répare la céramique cassée avec de la laque saupoudrée d'or ?", ["Le kintsugi", "L'ikebana", "L'origami", "Le raku"], "Le kintsugi", "La cassure devient belle."),
  Q("Qu'est-ce que le raku ?", ["Une technique japonaise de cuisson rapide de la céramique", "Un pliage de papier", "Une danse", "Un type de pinceau"], "Une technique japonaise de cuisson rapide de la céramique", "Elle produit des effets imprévisibles."),
]),
notion('AM-2', 0, D, 'artm-materiau-corps', [
  Q("Quelle artiste serbe utilise son propre corps comme matériau dans ses performances ?", ["Marina Abramović", "Frida Kahlo", "Louise Bourgeois", "Yoko Ono"], "Marina Abramović", "The Artist Is Present (2010)."),
  Q("Quel artiste britannique a moulé son propre corps des dizaines de fois pour ses sculptures ?", ["Antony Gormley", "Henry Moore", "Damien Hirst", "Anish Kapoor"], "Antony Gormley", "Another Place, sur une plage près de Liverpool."),
  Q("Comment appelle-t-on l'art qui utilise le corps de l'artiste comme support ?", ["Le body art", "Le land art", "Le pop art", "L'op art"], "Le body art", "Il se développe dans les années 1960-1970."),
]),
notion('AM-2', 0, D, 'artm-eva-hesse', [
  Q("Quelle artiste américaine a utilisé latex et fibre de verre, matériaux qui se dégradent, dans les années 1960 ?", ["Eva Hesse", "Louise Bourgeois", "Georgia O'Keeffe", "Cindy Sherman"], "Eva Hesse", "Ses œuvres posent des problèmes de conservation."),
  Q("Pourquoi certains artistes choisissent-ils des matériaux qui vieillissent ?", ["Pour intégrer le temps et la fragilité dans l'œuvre", "Par économie uniquement", "Par erreur", "Pour qu'elles durent toujours"], "Pour intégrer le temps et la fragilité dans l'œuvre", "La dégradation fait partie du sens."),
  Q("Comment appelle-t-on l'art qui privilégie le processus et les matériaux souples, après le minimalisme ?", ["Le post-minimalisme (process art)", "Le pop art", "Le cubisme", "Le romantisme"], "Le post-minimalisme (process art)", "Richard Serra a lancé du plomb fondu contre un mur."),
]),
# ══ AM-3 · La matérialité et la qualité de la couleur ══
notion('AM-3', 0, F, 'artm-cercle-chromatique', [
  Q("Qu'est-ce qu'un cercle chromatique ?", ["Une roue qui organise les couleurs", "Un cadre rond", "Un pinceau rond", "Une palette en bois"], "Une roue qui organise les couleurs", "Les complémentaires y sont face à face."),
  Q("Quelle couleur obtient-on en mélangeant du rouge et du bleu ?", ["Le violet", "Le vert", "L'orange", "Le marron"], "Le violet", "C'est une couleur secondaire."),
  Q("Combien y a-t-il de couleurs secondaires traditionnelles ?", ["Trois : orange, vert, violet", "Deux", "Cinq", "Une"], "Trois : orange, vert, violet", "Elles naissent du mélange de deux primaires."),
]),
notion('AM-3', 0, F, 'artm-clair-fonce', [
  Q("Comment éclaircit-on une couleur en peinture ?", ["En ajoutant du blanc", "En ajoutant du noir", "En ajoutant du vert", "En ajoutant de l'eau uniquement en huile"], "En ajoutant du blanc", "On obtient une teinte plus claire."),
  Q("Comment fonce-t-on une couleur ?", ["En ajoutant du noir ou sa complémentaire", "En ajoutant du blanc", "En ajoutant de l'eau", "En la chauffant"], "En ajoutant du noir ou sa complémentaire", "La complémentaire la « casse »."),
  Q("Qu'est-ce qu'un dégradé ?", ["Un passage progressif d'une couleur ou d'une valeur à une autre", "Une couleur abîmée", "Une tache", "Un contour"], "Un passage progressif d'une couleur ou d'une valeur à une autre", "Il crée des effets de lumière."),
]),
notion('AM-3', 0, F, 'artm-couleurs-emotions', [
  Q("Quelle couleur est souvent associée au calme ?", ["Le bleu", "Le rouge", "Le jaune vif", "L'orange"], "Le bleu", "Les associations varient selon les cultures."),
  Q("Quelle couleur est souvent associée à la colère ou à la passion ?", ["Le rouge", "Le bleu", "Le vert pâle", "Le gris"], "Le rouge", "Elle attire l'œil."),
  Q("Quelle période de Picasso doit son nom à une couleur dominante froide et triste ?", ["La période bleue", "La période rose", "La période noire", "La période verte"], "La période bleue", "De 1901 à 1904."),
]),
notion('AM-3', 0, F, 'artm-pigments-naturels', [
  Q("D'où viennent les pigments naturels ?", ["De la terre, des minéraux, des plantes ou des animaux", "Uniquement des usines", "De l'eau", "De l'air"], "De la terre, des minéraux, des plantes ou des animaux", "Les ocres viennent de la terre."),
  Q("Quel pigment rouge était tiré d'un petit insecte, la cochenille ?", ["Le carmin", "L'ocre", "Le bleu de Prusse", "Le noir de fumée"], "Le carmin", "Il était très précieux."),
  Q("Quelle plante donnait la teinture bleue de pastel dans la région de Toulouse ?", ["La guède (le pastel)", "La rose", "L'ortie", "Le tournesol"], "La guède (le pastel)", "Toulouse s'est enrichie grâce à elle au XVIe siècle."),
]),
notion('AM-3', 0, F, 'artm-noir-blanc', [
  Q("Le noir et le blanc sont-ils considérés comme des couleurs en peinture ?", ["Oui, on les utilise comme des couleurs", "Non, jamais", "Seulement le blanc", "Seulement le noir"], "Oui, on les utilise comme des couleurs", "Les débats existent, mais les peintres les utilisent pleinement."),
  Q("Quel mélange donne du gris ?", ["Le noir et le blanc", "Le rouge et le bleu", "Le jaune et le vert", "Le violet et l'orange"], "Le noir et le blanc", "On obtient des valeurs de gris."),
  Q("Comment appelle-t-on une œuvre réalisée avec les nuances d'une seule couleur ?", ["Un camaïeu", "Un arc-en-ciel", "Un contraste", "Une mosaïque"], "Un camaïeu", "Par exemple, tout en bleus."),
]),
notion('AM-3', 0, F, 'artm-matisse-couleur', [
  Q("Quel mouvement de 1905 utilise des couleurs pures et violentes ?", ["Le fauvisme", "Le cubisme", "Le réalisme", "Le surréalisme"], "Le fauvisme", "Un critique a parlé de « cage aux fauves »."),
  Q("Quel peintre est la figure majeure du fauvisme ?", ["Henri Matisse", "Claude Monet", "Pablo Picasso", "Salvador Dalí"], "Henri Matisse", "Avec André Derain et Maurice de Vlaminck."),
  Q("Quel peintre fauve a peint Londres et la Tamise avec des couleurs inattendues ?", ["André Derain", "Claude Monet", "William Turner", "Henri Rousseau"], "André Derain", "Charing Cross Bridge (1906)."),
]),
notion('AM-3', 0, I, 'artm-synthese-additive', [
  Q("Quelles sont les trois couleurs primaires de la lumière (écrans) ?", ["Rouge, vert, bleu (RVB)", "Rouge, jaune, bleu", "Cyan, magenta, jaune", "Noir, blanc, gris"], "Rouge, vert, bleu (RVB)", "C'est la synthèse additive."),
  Q("Quelle couleur obtient-on en superposant toutes les lumières colorées ?", ["Le blanc", "Le noir", "Le marron", "Le gris foncé"], "Le blanc", "En peinture, mélanger toutes les couleurs donne un brun sombre."),
  Q("Quelles couleurs primaires utilise l'imprimerie (synthèse soustractive) ?", ["Cyan, magenta, jaune (et noir)", "Rouge, vert, bleu", "Orange, vert, violet", "Blanc et noir"], "Cyan, magenta, jaune (et noir)", "C'est le système CMJN."),
]),
notion('AM-3', 0, I, 'artm-valeur-saturation', [
  Q("Que désigne la valeur d'une couleur ?", ["Son degré de clarté ou d'obscurité", "Son prix", "Sa température", "Son nom"], "Son degré de clarté ou d'obscurité", "On l'observe en noir et blanc."),
  Q("Que désigne la saturation d'une couleur ?", ["Son intensité, sa pureté", "Sa clarté", "Son odeur", "Sa matière"], "Son intensité, sa pureté", "Une couleur peu saturée tire vers le gris."),
  Q("Que désigne le ton (la teinte) ?", ["La couleur elle-même (rouge, bleu…)", "La brillance", "L'épaisseur", "Le support"], "La couleur elle-même (rouge, bleu…)", "Ton, valeur, saturation décrivent une couleur."),
]),
notion('AM-3', 0, I, 'artm-liants', [
  Q("Qu'est-ce qu'un liant en peinture ?", ["La substance qui lie les pigments et les fait adhérer au support", "Le pinceau", "Le cadre", "Le solvant"], "La substance qui lie les pigments et les fait adhérer au support", "Huile, œuf, acrylique, gomme arabique…"),
  Q("Quel liant utilise l'aquarelle ?", ["La gomme arabique", "L'huile de lin", "L'œuf", "La cire"], "La gomme arabique", "Elle vient de l'acacia."),
  Q("Qu'est-ce que la peinture à l'encaustique ?", ["Une peinture à base de cire chaude", "Une peinture à l'eau", "Une encre", "Une sculpture"], "Une peinture à base de cire chaude", "Les portraits du Fayoum en Égypte romaine l'utilisent."),
]),
notion('AM-3', 0, I, 'artm-couleur-lumiere-vitrail', [
  Q("Comment la couleur d'un vitrail apparaît-elle ?", ["Par la lumière qui traverse le verre coloré", "Par la peinture posée sur le mur", "Par une lampe électrique", "Par le reflet du sol"], "Par la lumière qui traverse le verre coloré", "La couleur change selon l'heure."),
  Q("Quelle cathédrale est célèbre pour son « bleu de Chartres » ?", ["Notre-Dame de Chartres", "Notre-Dame de Paris", "La cathédrale de Reims", "La Sainte-Chapelle"], "Notre-Dame de Chartres", "Ses vitraux datent des XIIe-XIIIe siècles."),
  Q("Quel peintre a créé les vitraux de la chapelle du Rosaire à Vence ?", ["Henri Matisse", "Marc Chagall", "Pierre Soulages", "Fernand Léger"], "Henri Matisse", "Chagall a réalisé des vitraux à Reims et Metz."),
]),
notion('AM-3', 0, I, 'artm-couleur-histoire', [
  Q("Quel pigment bleu synthétique a été découvert par hasard à Berlin au début du XVIIIe siècle ?", ["Le bleu de Prusse", "Le bleu outremer", "Le bleu cobalt", "L'indigo"], "Le bleu de Prusse", "Hokusai l'a utilisé pour La Grande Vague."),
  Q("Quelle couleur était réservée aux empereurs romains, tirée d'un coquillage ?", ["La pourpre", "Le vert", "Le jaune", "Le gris"], "La pourpre", "Il fallait des milliers de murex."),
  Q("Quel historien français a écrit l'histoire des couleurs (Bleu, Noir, Vert, Rouge) ?", ["Michel Pastoureau", "Daniel Arasse", "Georges Duby", "Fernand Braudel"], "Michel Pastoureau", "Il montre que le sens des couleurs varie selon les époques."),
]),
notion('AM-3', 0, I, 'artm-tubes-impressionnistes', [
  Q("Quelle invention de 1841 a facilité la peinture en plein air ?", ["Le tube de peinture en métal", "L'appareil photo", "Le chevalet pliant", "La lampe à pétrole"], "Le tube de peinture en métal", "Inventé par John Goffe Rand."),
  Q("Pourquoi les impressionnistes évitent-ils le noir dans les ombres ?", ["Ils observent que les ombres sont colorées", "Le noir était interdit", "Le noir coûtait cher", "Ils n'avaient pas de noir"], "Ils observent que les ombres sont colorées", "Une ombre peut être bleue ou violette."),
  Q("Quelle loi de Chevreul ont exploité les peintres impressionnistes et néo-impressionnistes ?", ["La loi du contraste simultané des couleurs", "La loi de la gravitation", "La loi de la perspective", "La loi des proportions"], "La loi du contraste simultané des couleurs", "Une couleur change selon sa voisine."),
]),
notion('AM-3', 0, I, 'artm-albers', [
  Q("Quel artiste a peint des centaines de carrés emboîtés pour étudier l'interaction des couleurs ?", ["Josef Albers", "Mark Rothko", "Kasimir Malevitch", "Piet Mondrian"], "Josef Albers", "Série Hommage au carré."),
  Q("Quel ouvrage de Josef Albers (1963) étudie la perception des couleurs ?", ["L'Interaction des couleurs", "Du spirituel dans l'art", "Le Traité de la peinture", "De pictura"], "L'Interaction des couleurs", "Il montre que la couleur est relative."),
  Q("Quel professeur du Bauhaus a théorisé sept contrastes de couleurs ?", ["Johannes Itten", "Paul Klee", "Walter Gropius", "László Moholy-Nagy"], "Johannes Itten", "L'Art de la couleur (1961)."),
]),
notion('AM-3', 0, I, 'artm-couleurs-chaudes-froides', [
  Q("Quelle impression donne une couleur chaude dans un tableau ?", ["Elle semble avancer vers le spectateur", "Elle semble reculer", "Elle disparaît", "Elle devient grise"], "Elle semble avancer vers le spectateur", "Les couleurs froides semblent reculer."),
  Q("Quel peintre a joué sur les couleurs chaudes et froides dans ses Nymphéas ?", ["Claude Monet", "Jacques-Louis David", "Ingres", "Le Caravage"], "Claude Monet", "Ils sont exposés à l'Orangerie."),
  Q("Une couleur peut-elle paraître chaude ou froide selon ses voisines ?", ["Oui, la perception dépend du contexte", "Non, jamais", "Seulement le rouge", "Seulement le bleu"], "Oui, la perception dépend du contexte", "Un vert peut être chaud (tirant vers le jaune) ou froid (vers le bleu)."),
]),
notion('AM-3', 0, D, 'artm-goethe-newton', [
  Q("Quel savant a décomposé la lumière blanche en couleurs avec un prisme ?", ["Isaac Newton", "Galilée", "Goethe", "Léonard de Vinci"], "Isaac Newton", "Vers 1666."),
  Q("Quel écrivain allemand a publié en 1810 un Traité des couleurs fondé sur la perception ?", ["Goethe", "Schiller", "Kant", "Hegel"], "Goethe", "Il s'oppose à l'approche physique de Newton."),
  Q("Combien de couleurs Newton a-t-il retenues dans l'arc-en-ciel ?", ["Sept", "Trois", "Cinq", "Douze"], "Sept", "Par analogie avec les sept notes de musique."),
]),
notion('AM-3', 0, D, 'artm-noirs-soulages-vantablack', [
  Q("Quelle matière ultra-noire absorbe plus de 99,9 % de la lumière ?", ["Le Vantablack", "Le noir d'ivoire", "Le noir de fumée", "Le bitume"], "Le Vantablack", "Elle a été mise au point au Royaume-Uni."),
  Q("Quel artiste a obtenu l'exclusivité artistique du Vantablack, provoquant une polémique ?", ["Anish Kapoor", "Pierre Soulages", "Damien Hirst", "Banksy"], "Anish Kapoor", "D'autres artistes ont créé en réponse le « pinkest pink »."),
  Q("Quel pigment noir était fabriqué à partir d'os calcinés ?", ["Le noir d'ivoire (noir d'os)", "Le noir de vigne", "Le bleu de Prusse", "La sépia"], "Le noir d'ivoire (noir d'os)", "La sépia vient de l'encre de seiche."),
]),
notion('AM-3', 0, D, 'artm-couleur-architecture', [
  Q("Quel architecte a créé une palette de couleurs pour l'architecture (Polychromie architecturale) ?", ["Le Corbusier", "Gustave Eiffel", "Haussmann", "Mansart"], "Le Corbusier", "Ses claviers de couleurs datent de 1931 et 1959."),
  Q("Quel architecte mexicain est célèbre pour ses murs aux couleurs vives (rose, jaune, bleu) ?", ["Luis Barragán", "Oscar Niemeyer", "Frank Gehry", "Tadao Ando"], "Luis Barragán", "Il reçoit le prix Pritzker en 1980."),
  Q("Pourquoi les temples grecs antiques n'étaient-ils pas tout blancs à l'origine ?", ["Ils étaient peints de couleurs vives qui ont disparu", "Ils étaient en verre", "Ils étaient en or", "Ils étaient toujours blancs"], "Ils étaient peints de couleurs vives qui ont disparu", "C'est la polychromie antique."),
]),
notion('AM-3', 0, D, 'artm-couleur-numerique-codes', [
  Q("Comment s'écrit une couleur en code hexadécimal sur le web ?", ["Avec # suivi de six caractères, par exemple #FF0000", "Avec un nom en latin", "Avec un numéro de téléphone", "Avec des points"], "Avec # suivi de six caractères, par exemple #FF0000", "#FF0000 correspond au rouge."),
  Q("Pourquoi une couleur imprimée diffère-t-elle souvent de la même couleur à l'écran ?", ["L'écran utilise la lumière (RVB), l'imprimante l'encre (CMJN)", "L'imprimante est cassée", "Le papier est blanc", "Il n'y a pas de différence"], "L'écran utilise la lumière (RVB), l'imprimante l'encre (CMJN)", "Les graphistes calibrent leurs écrans."),
  Q("Quel nuancier sert de référence mondiale aux graphistes et designers ?", ["Le nuancier Pantone", "Le cercle de Newton", "Le dictionnaire Larousse", "Le code Morse"], "Le nuancier Pantone", "Chaque teinte a un numéro."),
]),
notion('AM-3', 0, D, 'artm-couleur-perception', [
  Q("Qu'est-ce qu'une image rémanente (persistance colorée) ?", ["La couleur complémentaire qu'on voit après avoir fixé une couleur", "Une photo ancienne", "Une couleur effacée", "Une tache sur l'œil"], "La couleur complémentaire qu'on voit après avoir fixé une couleur", "Fixez un rond rouge puis un mur blanc : il paraît vert."),
  Q("Qu'est-ce que le daltonisme ?", ["Une difficulté à distinguer certaines couleurs", "Une passion pour les couleurs", "Une technique de peinture", "Une maladie du pinceau"], "Une difficulté à distinguer certaines couleurs", "Il touche environ 8 % des hommes."),
  Q("Pourquoi une même robe a-t-elle été vue bleue et noire ou blanche et dorée en 2015 ?", ["Le cerveau interprète différemment l'éclairage supposé", "La robe changeait de couleur", "La photo était truquée", "C'était une erreur d'impression"], "Le cerveau interprète différemment l'éclairage supposé", "La perception de la couleur est une construction."),
]),
notion('AM-3', 0, D, 'artm-yves-klein-monochromes', [
  Q("Quels outils Yves Klein a-t-il utilisés pour ses Anthropométries ?", ["Des corps de modèles enduits de peinture bleue", "Des pinceaux fins", "Des pochoirs", "Des appareils photo"], "Des corps de modèles enduits de peinture bleue", "Les corps deviennent « pinceaux vivants »."),
  Q("Quelle couleur Klein associe-t-il à l'immatériel et à l'infini ?", ["Le bleu", "Le rouge", "Le vert", "Le noir"], "Le bleu", "Il a aussi utilisé l'or et le rose."),
  Q("Quelle exposition de Klein en 1958 présentait une galerie entièrement vide ?", ["Le Vide", "Le Plein", "La Couleur", "Le Bleu"], "Le Vide", "Arman lui répond en 1960 avec Le Plein."),
]),
notion('AM-3', 0, D, 'artm-couleur-symbolique-cultures', [
  Q("Quelle couleur est traditionnellement celle du deuil en Chine et au Japon ?", ["Le blanc", "Le noir", "Le rouge", "Le vert"], "Le blanc", "En Europe, c'est souvent le noir."),
  Q("Quelle couleur porte bonheur en Chine, notamment pour le Nouvel An ?", ["Le rouge", "Le blanc", "Le noir", "Le gris"], "Le rouge", "Les enveloppes rouges contiennent de l'argent."),
  Q("Pourquoi le sens des couleurs varie-t-il ?", ["Il dépend des cultures et des époques", "Il est fixé par la nature", "Il est décidé par les peintres", "Il ne varie pas"], "Il dépend des cultures et des époques", "Il faut se méfier des généralisations."),
]),
notion('AM-3', 0, D, 'artm-couleur-toxique', [
  Q("Quel pigment blanc, très utilisé autrefois, était toxique car à base de plomb ?", ["Le blanc de plomb (céruse)", "Le blanc de titane", "Le blanc de zinc", "Le blanc d'Espagne"], "Le blanc de plomb (céruse)", "Il a été remplacé par le blanc de titane."),
  Q("Quel pigment vert du XIXe siècle contenait de l'arsenic ?", ["Le vert de Paris (vert de Schweinfurt)", "Le vert émeraude moderne", "Le vert de chrome", "Le vert olive"], "Le vert de Paris (vert de Schweinfurt)", "On l'a soupçonné d'avoir empoisonné des papiers peints."),
  Q("Pourquoi les peintres d'aujourd'hui utilisent-ils des pigments synthétiques ?", ["Ils sont plus sûrs, stables et moins chers", "Ils sont plus toxiques", "Ils sont plus rares", "Ils n'existent pas"], "Ils sont plus sûrs, stables et moins chers", "La chimie a transformé la palette."),
]),
# ══ AM-4 · L'objet comme matériau en art ══
notion('AM-4', 0, F, 'artm-assemblage', [
  Q("Qu'est-ce qu'un assemblage en art ?", ["Une œuvre faite d'objets ou de morceaux réunis", "Une peinture lisse", "Un dessin au crayon", "Une photo"], "Une œuvre faite d'objets ou de morceaux réunis", "On peut coller, visser, attacher."),
  Q("Avec quoi Picasso a-t-il créé une guenon et son petit (1951) ?", ["Avec des petites voitures et des objets de récupération", "Avec de la pâte à modeler", "Avec du marbre", "Avec du verre"], "Avec des petites voitures et des objets de récupération", "La tête est faite de deux petites voitures."),
  Q("Qu'est-ce qu'un objet trouvé en art ?", ["Un objet ramassé et utilisé tel quel dans une œuvre", "Un objet perdu", "Un objet volé", "Un objet neuf acheté"], "Un objet ramassé et utilisé tel quel dans une œuvre", "Les surréalistes l'appréciaient."),
]),
notion('AM-4', 0, F, 'artm-arcimboldo', [
  Q("Quel peintre a composé des visages avec des fruits, des légumes ou des fleurs ?", ["Giuseppe Arcimboldo", "Léonard de Vinci", "Raphaël", "Titien"], "Giuseppe Arcimboldo", "Les Quatre Saisons (XVIe siècle)."),
  Q("Comment appelle-t-on une image qui change de sens selon la façon de la regarder ?", ["Une image double (ou ambiguë)", "Un monochrome", "Un trompe-l'œil classique", "Une nature morte"], "Une image double (ou ambiguë)", "Arcimboldo en a peint de célèbres."),
  Q("Quel objet du quotidien peut devenir un visage dans une œuvre ?", ["N'importe quel objet, selon l'imagination de l'artiste", "Aucun", "Seulement une assiette", "Seulement un miroir"], "N'importe quel objet, selon l'imagination de l'artiste", "On parle de paréidolie quand on voit des visages partout."),
]),
notion('AM-4', 0, F, 'artm-boites-cornell', [
  Q("Quel artiste américain a créé de petites boîtes vitrées remplies d'objets poétiques ?", ["Joseph Cornell", "Andy Warhol", "Jackson Pollock", "Alexander Calder"], "Joseph Cornell", "Ses boîtes ressemblent à des théâtres miniatures."),
  Q("Qu'est-ce qu'un cabinet de curiosités ?", ["Une collection d'objets rares et étranges, ancêtre du musée", "Un bureau", "Une salle de classe", "Un magasin"], "Une collection d'objets rares et étranges, ancêtre du musée", "Il était à la mode aux XVIe-XVIIe siècles."),
  Q("Quel objet peut devenir le contenant d'une œuvre-boîte ?", ["Une boîte, un tiroir, une valise…", "Uniquement un cadre doré", "Uniquement un vase", "Rien"], "Une boîte, un tiroir, une valise…", "Duchamp a créé une « Boîte-en-valise »."),
]),
notion('AM-4', 0, F, 'artm-jouets-art', [
  Q("Quel artiste fabrique ses œuvres avec des briques Lego ?", ["Nathan Sawaya (et Ai Weiwei)", "Claude Monet", "Auguste Rodin", "Henri Matisse"], "Nathan Sawaya (et Ai Weiwei)", "Ai Weiwei a fait des portraits en Lego."),
  Q("Quel artiste a créé un cirque miniature avec des fils de fer et des objets, qu'il animait lui-même ?", ["Alexander Calder", "Jean Tinguely", "Joan Miró", "Fernand Léger"], "Alexander Calder", "Le Cirque Calder (1926-1931)."),
  Q("Pourquoi des artistes utilisent-ils des jouets dans leurs œuvres ?", ["Pour jouer avec l'enfance, l'humour et la culture populaire", "Parce qu'ils sont gratuits", "Par manque d'idées", "Pour vendre des jouets"], "Pour jouer avec l'enfance, l'humour et la culture populaire", "Le jouet devient matériau."),
]),
notion('AM-4', 0, F, 'artm-accumulation', [
  Q("Que signifie accumuler en art ?", ["Rassembler un grand nombre d'objets semblables", "Peindre un seul objet", "Effacer une œuvre", "Vendre une œuvre"], "Rassembler un grand nombre d'objets semblables", "Arman a accumulé violons, cafetières, poupées…"),
  Q("Quel effet produit l'accumulation d'objets identiques ?", ["Elle évoque la production de masse et la société de consommation", "Elle rend l'objet unique", "Elle cache les objets", "Aucun effet"], "Elle évoque la production de masse et la société de consommation", "Le nombre change notre regard."),
  Q("Quelle œuvre d'Arman, à la gare Saint-Lazare, empile des horloges ?", ["L'Heure de tous", "Long Term Parking", "Le Plein", "Poubelles"], "L'Heure de tous", "Elle date de 1985."),
]),
notion('AM-4', 0, F, 'artm-objets-quotidiens', [
  Q("Quel artiste américain a peint des boîtes de soupe en série ?", ["Andy Warhol", "Jeff Koons", "Roy Lichtenstein", "Keith Haring"], "Andy Warhol", "Campbell's Soup Cans (1962)."),
  Q("Comment appelle-t-on la représentation d'objets inanimés posés sur une table ?", ["Une nature morte", "Un paysage", "Un portrait", "Une scène de genre"], "Une nature morte", "En anglais : still life."),
  Q("Quel peintre français a peint des pommes avec une grande attention aux volumes ?", ["Paul Cézanne", "Claude Monet", "Eugène Delacroix", "Jacques-Louis David"], "Paul Cézanne", "« Je veux étonner Paris avec une pomme »."),
]),
notion('AM-4', 0, F, 'artm-pliage-objet', [
  Q("Quel objet du quotidien devient sculpture chez Calder avec du fil de fer ?", ["Des portraits et animaux dessinés en fil de fer", "Des statues de marbre", "Des vitraux", "Des fresques"], "Des portraits et animaux dessinés en fil de fer", "Il « dessine dans l'espace »."),
  Q("Qu'est-ce qu'une sculpture en fil de fer ?", ["Une sculpture dont les lignes sont formées par du fil métallique plié", "Une sculpture en pierre", "Une peinture", "Un tissu"], "Une sculpture dont les lignes sont formées par du fil métallique plié", "On peut en faire en classe."),
  Q("Quel matériau du quotidien sert souvent à fabriquer des sculptures en classe ?", ["Le carton, les bouchons, les rouleaux", "Le marbre de Carrare", "L'or", "L'ivoire"], "Le carton, les bouchons, les rouleaux", "La récupération est un vrai matériau."),
]),
notion('AM-4', 0, I, 'artm-nouveau-realisme', [
  Q("Quel critique a fondé le nouveau réalisme en 1960 ?", ["Pierre Restany", "André Breton", "Guillaume Apollinaire", "Clement Greenberg"], "Pierre Restany", "Avec Yves Klein, Arman, César, Tinguely…"),
  Q("Quel nouveau réaliste a arraché des affiches publicitaires dans la rue pour en faire des œuvres ?", ["Raymond Hains (et Jacques Villeglé)", "Arman", "César", "Yves Klein"], "Raymond Hains (et Jacques Villeglé)", "Ce sont les affichistes."),
  Q("Que défend le nouveau réalisme ?", ["L'appropriation directe du réel et des objets de la société urbaine", "La peinture d'histoire", "L'abstraction pure", "Le retour à la Renaissance"], "L'appropriation directe du réel et des objets de la société urbaine", "Restany parle de « nouvelles approches perceptives du réel »."),
]),
notion('AM-4', 0, I, 'artm-rauschenberg', [
  Q("Quel artiste américain a créé des « combine paintings » mêlant peinture et objets ?", ["Robert Rauschenberg", "Jackson Pollock", "Mark Rothko", "Edward Hopper"], "Robert Rauschenberg", "Monogram associe une chèvre empaillée et un pneu."),
  Q("Quel objet entoure la chèvre empaillée de Monogram (1955-1959) ?", ["Un pneu", "Un cadre", "Une chaise", "Une cage"], "Un pneu", "L'œuvre est au Moderna Museet de Stockholm."),
  Q("Quel artiste a « effacé » un dessin de De Kooning en 1953 ?", ["Robert Rauschenberg", "Marcel Duchamp", "Andy Warhol", "Jasper Johns"], "Robert Rauschenberg", "Erased de Kooning Drawing."),
]),
notion('AM-4', 0, I, 'artm-surrealisme-objet', [
  Q("Quelle artiste surréaliste a recouvert une tasse, une soucoupe et une cuillère de fourrure ?", ["Meret Oppenheim", "Frida Kahlo", "Leonora Carrington", "Dora Maar"], "Meret Oppenheim", "Le Déjeuner en fourrure (1936)."),
  Q("Quel objet de Man Ray est un fer à repasser hérissé de clous ?", ["Cadeau", "Fontaine", "Roue de bicyclette", "Porte-bouteilles"], "Cadeau", "L'objet devient inutilisable et inquiétant."),
  Q("Quel objet surréaliste de Dalí associe un homard et un téléphone ?", ["Le Téléphone-homard", "La Persistance de la mémoire", "Le Grand Masturbateur", "Le Sofa lèvres"], "Le Téléphone-homard", "Il date de 1936."),
]),
notion('AM-4', 0, I, 'artm-compression-expansion', [
  Q("Quel sculpteur français a réalisé le trophée des César du cinéma ?", ["César Baldaccini", "Arman", "Jean Tinguely", "Niki de Saint Phalle"], "César Baldaccini", "C'est une petite compression."),
  Q("Qu'est-ce qu'une « expansion » chez César ?", ["Une sculpture en mousse de polyuréthane qui gonfle et se fige", "Une compression de voiture", "Une peinture", "Une photo agrandie"], "Une sculpture en mousse de polyuréthane qui gonfle et se fige", "Il les réalisait parfois en public."),
  Q("Quelle œuvre géante de César représente un pouce agrandi ?", ["Le Pouce", "Le Poing", "La Main", "Le Doigt d'honneur"], "Le Pouce", "Un exemplaire se trouve à La Défense."),
]),
notion('AM-4', 0, I, 'artm-art-recyclage', [
  Q("Quel artiste béninois crée des masques à partir de bidons d'essence en plastique ?", ["Romuald Hazoumè", "El Anatsui", "Chéri Samba", "Ousmane Sow"], "Romuald Hazoumè", "Il dénonce le trafic d'essence et la société de consommation."),
  Q("Quel artiste brésilien a créé des portraits avec des déchets d'une décharge de Rio ?", ["Vik Muniz", "Romero Britto", "Os Gêmeos", "Hélio Oiticica"], "Vik Muniz", "Le documentaire Waste Land raconte ce projet."),
  Q("Quel message porte souvent l'art réalisé avec des déchets ?", ["Une critique du gaspillage et de la pollution", "Un éloge de la consommation", "Aucun message", "Une publicité"], "Une critique du gaspillage et de la pollution", "L'objet jeté retrouve une valeur."),
]),
notion('AM-4', 0, I, 'artm-installation-objets', [
  Q("Qu'est-ce qu'une installation ?", ["Une œuvre qui occupe un espace et que le spectateur peut parcourir", "Un tableau accroché", "Un dessin", "Un livre"], "Une œuvre qui occupe un espace et que le spectateur peut parcourir", "Elle utilise souvent des objets."),
  Q("Quel artiste français a accumulé des vêtements usagés pour évoquer l'absence et la mémoire ?", ["Christian Boltanski", "Arman", "César", "Daniel Buren"], "Christian Boltanski", "Personnes (Grand Palais, 2010)."),
  Q("Quelle artiste française installe des peluches, des filets et des objets dans des mises en scène ?", ["Annette Messager", "Sophie Calle", "Niki de Saint Phalle", "ORLAN"], "Annette Messager", "Elle a reçu le Lion d'or à Venise en 2005."),
]),
notion('AM-4', 0, I, 'artm-objet-transformation-ecole', [
  Q("Que signifie « transformer un objet » en arts plastiques ?", ["Le modifier (couper, peindre, assembler) pour lui donner un autre sens", "Le jeter", "Le vendre", "Le copier à l'identique"], "Le modifier (couper, peindre, assembler) pour lui donner un autre sens", "C'est une pratique fréquente en classe."),
  Q("Quelle différence y a-t-il entre détourner et représenter un objet ?", ["Détourner, c'est utiliser l'objet réel ; représenter, c'est en faire une image", "Il n'y en a pas", "Représenter, c'est le casser", "Détourner, c'est le dessiner"], "Détourner, c'est utiliser l'objet réel ; représenter, c'est en faire une image", "Deux démarches artistiques différentes."),
  Q("Quel artiste a transformé un vieux vélo en Tête de taureau ?", ["Pablo Picasso", "Marcel Duchamp", "Arman", "César"], "Pablo Picasso", "Avec une selle et un guidon (1942)."),
]),
notion('AM-4', 0, D, 'artm-jeff-koons', [
  Q("Quel artiste américain a réalisé des chiens en ballons géants en acier inoxydable miroir ?", ["Jeff Koons", "Claes Oldenburg", "Takashi Murakami", "Damien Hirst"], "Jeff Koons", "Balloon Dog (1994-2000)."),
  Q("Quelle œuvre de Jeff Koons a été offerte à Paris en hommage aux victimes des attentats de 2015 ?", ["Bouquet of Tulips", "Balloon Dog", "Rabbit", "Puppy"], "Bouquet of Tulips", "Elle se trouve près du Petit Palais."),
  Q("Pourquoi les œuvres de Koons font-elles débat ?", ["Elles questionnent la frontière entre art, kitsch et marché", "Elles sont trop petites", "Elles sont anonymes", "Elles sont gratuites"], "Elles questionnent la frontière entre art, kitsch et marché", "Il fait produire ses œuvres en atelier."),
]),
notion('AM-4', 0, D, 'artm-louise-nevelson', [
  Q("Quelle sculptrice américaine a assemblé des morceaux de bois peints en noir dans de grands murs-sculptures ?", ["Louise Nevelson", "Louise Bourgeois", "Barbara Hepworth", "Eva Hesse"], "Louise Nevelson", "Elle récupérait des objets dans les rues de New York."),
  Q("Quel effet produit la peinture uniforme d'objets différents ?", ["Elle unifie l'ensemble et fait oublier leur fonction d'origine", "Elle les fait disparaître", "Elle les rend plus colorés", "Aucun effet"], "Elle unifie l'ensemble et fait oublier leur fonction d'origine", "Les objets deviennent formes."),
  Q("Quel sculpteur britannique assemble des fragments de plastique colorés en grandes formes ?", ["Tony Cragg", "Henry Moore", "Antony Gormley", "Anish Kapoor"], "Tony Cragg", "Britain Seen from the North (1981)."),
]),
notion('AM-4', 0, D, 'artm-tableaux-pieges', [
  Q("Que fixe Daniel Spoerri dans ses tableaux-pièges ?", ["Les restes d'un repas tels quels sur la table, accrochée au mur", "Des pièges à souris", "Des papillons", "Des photos"], "Les restes d'un repas tels quels sur la table, accrochée au mur", "Le hasard et le quotidien deviennent œuvre."),
  Q("Comment appelle-t-on l'art qui intègre le hasard dans sa création ?", ["L'art aléatoire (le hasard objectif chez les surréalistes)", "L'art académique", "L'art classique", "L'art officiel"], "L'art aléatoire (le hasard objectif chez les surréalistes)", "Duchamp utilisait des « stoppages-étalon »."),
  Q("Quelle œuvre de Duchamp a été fêlée par accident pendant un transport, ce qu'il a accepté ?", ["Le Grand Verre", "Fontaine", "L.H.O.O.Q.", "Roue de bicyclette"], "Le Grand Verre", "Il disait que l'œuvre était enfin terminée."),
]),
notion('AM-4', 0, D, 'artm-chaise-art', [
  Q("Quel artiste a exposé une chaise couverte d'un bloc de graisse (Fettstuhl, 1964) ?", ["Joseph Beuys", "Marcel Duchamp", "Andy Warhol", "Arman"], "Joseph Beuys", "La graisse évoque l'énergie et la chaleur."),
  Q("Quel artiste a fait d'une chaise électrique un motif de série (Electric Chair) ?", ["Andy Warhol", "Jeff Koons", "Robert Rauschenberg", "Roy Lichtenstein"], "Andy Warhol", "Il interroge la mort dans la société médiatique."),
  Q("Qu'interroge l'utilisation de la chaise dans l'art ?", ["Le rapport entre objet utilitaire et œuvre, présence et absence du corps", "La menuiserie", "La mode", "Rien"], "Le rapport entre objet utilitaire et œuvre, présence et absence du corps", "One and Three Chairs de Kosuth en est un autre exemple."),
]),
notion('AM-4', 0, D, 'artm-bertrand-lavier', [
  Q("Quel artiste français a posé un réfrigérateur sur un coffre-fort (Brandt/Haffner, 1984) ?", ["Bertrand Lavier", "César", "Arman", "Daniel Buren"], "Bertrand Lavier", "L'objet devient socle d'un autre objet."),
  Q("Que fait Bertrand Lavier quand il peint un piano avec une épaisse touche de peinture ?", ["Il brouille la frontière entre objet et peinture", "Il le répare", "Il le joue", "Il le vend"], "Il brouille la frontière entre objet et peinture", "On ne sait plus si c'est un piano ou un tableau."),
  Q("Qu'est-ce qu'un socle dans une exposition ?", ["Le support qui présente et met en valeur une œuvre", "Un mur", "Une étiquette", "Un gardien"], "Le support qui présente et met en valeur une œuvre", "Certains artistes en font une partie de l'œuvre."),
]),
notion('AM-4', 0, D, 'artm-objets-memoire', [
  Q("Pourquoi Christian Boltanski utilise-t-il des boîtes en fer et des photos anciennes ?", ["Pour évoquer la mémoire, la disparition et la Shoah", "Pour vendre des boîtes", "Pour décorer", "Pour faire rire"], "Pour évoquer la mémoire, la disparition et la Shoah", "Ses installations sont souvent sombres."),
  Q("Quelle artiste française a fait d'objets et de récits intimes le cœur de son œuvre (Prenez soin de vous) ?", ["Sophie Calle", "Annette Messager", "Louise Bourgeois", "Niki de Saint Phalle"], "Sophie Calle", "Elle mêle fiction et réalité."),
  Q("Qu'est-ce qu'un objet-souvenir dans une œuvre ?", ["Un objet chargé d'une histoire personnelle ou collective", "Un objet neuf", "Un objet décoratif sans histoire", "Un objet volé"], "Un objet chargé d'une histoire personnelle ou collective", "L'objet devient témoin."),
]),
notion('AM-4', 0, D, 'artm-ai-weiwei-objets', [
  Q("Quel artiste chinois a exposé 100 millions de graines de tournesol en porcelaine à la Tate Modern ?", ["Ai Weiwei", "Cai Guo-Qiang", "Yue Minjun", "Zhang Huan"], "Ai Weiwei", "Sunflower Seeds (2010)."),
  Q("Quel geste provocateur Ai Weiwei a-t-il photographié avec une urne de la dynastie Han ?", ["Il la laisse tomber et se briser", "Il la peint en or", "Il la vend", "Il la répare"], "Il la laisse tomber et se briser", "Il interroge la valeur du patrimoine."),
  Q("Avec quels objets Ai Weiwei a-t-il recouvert la façade d'un musée de Munich en hommage aux enfants victimes d'un séisme ?", ["Des sacs à dos d'écoliers", "Des chaussures", "Des livres", "Des téléphones"], "Des sacs à dos d'écoliers", "Remembering (2009)."),
]),
notion('AM-4', 0, D, 'artm-detournement-design', [
  Q("Quel designer a détourné un siège de tracteur en tabouret (Mezzadro) ?", ["Les frères Castiglioni", "Philippe Starck", "Charles Eames", "Le Corbusier"], "Les frères Castiglioni", "Le ready-made inspire le design."),
  Q("Quel collectif néerlandais a fait d'une lampe faite de vieux tiroirs une icône du design ?", ["Droog Design (Tejo Remy)", "Memphis", "Bauhaus", "De Stijl"], "Droog Design (Tejo Remy)", "Chest of Drawers (1991)."),
  Q("Pourquoi le détournement d'objet intéresse-t-il les designers ?", ["Il invente de nouveaux usages et questionne la consommation", "Il coûte plus cher", "Il est obligatoire", "Il supprime l'objet"], "Il invente de nouveaux usages et questionne la consommation", "L'objet change de fonction."),
]),
notion('AM-4', 0, D, 'artm-mark-dion', [
  Q("Quel artiste américain reconstitue des cabinets de curiosités avec des objets collectés ?", ["Mark Dion", "Jeff Koons", "Andy Warhol", "Donald Judd"], "Mark Dion", "Il interroge la science et la collection."),
  Q("Quelle artiste française a créé des « Collections » de petits objets et des « Mes vœux » faits de photos ?", ["Annette Messager", "Sophie Calle", "Louise Bourgeois", "Niki de Saint Phalle"], "Annette Messager", "Elle collectionne et classe."),
  Q("Qu'est-ce qu'une démarche de collection en art ?", ["Rassembler, classer et exposer des objets pour produire du sens", "Acheter des œuvres", "Vendre des objets", "Peindre un seul objet"], "Rassembler, classer et exposer des objets pour produire du sens", "L'inventaire devient œuvre."),
]),
# ══ AM-5 · Les représentations et statuts de l'objet en art ══
notion('AM-5', 0, F, 'artm-nature-morte-objets', [
  Q("Que représente souvent une nature morte flamande du XVIIe siècle ?", ["Des fruits, des fleurs, de la vaisselle et du gibier", "Des batailles", "Des rois", "Des paysages de montagne"], "Des fruits, des fleurs, de la vaisselle et du gibier", "Elle montre aussi la richesse des propriétaires."),
  Q("Quel peintre français du XVIIIe siècle a peint des objets simples de cuisine avec poésie ?", ["Jean Siméon Chardin", "Jacques-Louis David", "François Boucher", "Watteau"], "Jean Siméon Chardin", "La Raie (1728)."),
  Q("Quel peintre italien a peint des bouteilles et des pots tout au long de sa vie ?", ["Giorgio Morandi", "Caravage", "Amedeo Modigliani", "Giorgio de Chirico"], "Giorgio Morandi", "Ses natures mortes sont silencieuses."),
]),
notion('AM-5', 0, F, 'artm-objet-utile-beau', [
  Q("Un objet utile peut-il aussi être beau ?", ["Oui, c'est l'un des enjeux du design et des arts décoratifs", "Non, jamais", "Seulement s'il est cher", "Seulement s'il est ancien"], "Oui, c'est l'un des enjeux du design et des arts décoratifs", "Un vase, une chaise, une lampe…"),
  Q("Quel musée parisien conserve meubles, objets et bijoux ?", ["Le musée des Arts décoratifs", "Le musée d'Orsay", "Le musée Rodin", "Le Louvre-Lens"], "Le musée des Arts décoratifs", "Il est situé dans une aile du Louvre."),
  Q("Comment appelle-t-on un objet fabriqué à la main par un artisan ?", ["Un objet artisanal", "Un objet industriel", "Un ready-made", "Un multiple"], "Un objet artisanal", "L'industrie produit en série."),
]),
notion('AM-5', 0, F, 'artm-objet-geant', [
  Q("Quel artiste a créé des objets du quotidien géants, comme une cuillère avec une cerise ?", ["Claes Oldenburg (et Coosje van Bruggen)", "Andy Warhol", "Jeff Koons", "César"], "Claes Oldenburg (et Coosje van Bruggen)", "Spoonbridge and Cherry, à Minneapolis."),
  Q("Quel effet produit un objet agrandi de façon gigantesque ?", ["Il surprend et change notre regard sur l'objet", "Il disparaît", "Il devient invisible", "Aucun effet"], "Il surprend et change notre regard sur l'objet", "Le changement d'échelle est un levier artistique."),
  Q("Quel objet géant d'Oldenburg se trouve à la Villette, à Paris ?", ["Une bicyclette ensevelie", "Une cuillère", "Une pince à linge", "Un rouge à lèvres"], "Une bicyclette ensevelie", "Elle sort du sol par morceaux."),
]),
notion('AM-5', 0, F, 'artm-objet-sacre', [
  Q("Qu'est-ce qu'un reliquaire ?", ["Un objet précieux qui contient les reliques d'un saint", "Une boîte à bijoux ordinaire", "Un livre", "Un vitrail"], "Un objet précieux qui contient les reliques d'un saint", "Celui de sainte Foy à Conques est célèbre."),
  Q("Un objet religieux peut-il devenir une œuvre de musée ?", ["Oui, son statut change quand il entre au musée", "Non, jamais", "Seulement s'il est cassé", "Seulement s'il est neuf"], "Oui, son statut change quand il entre au musée", "Il passe du culte à la contemplation."),
  Q("Qu'est-ce qu'un masque rituel ?", ["Un masque utilisé lors de cérémonies religieuses ou sociales", "Un masque de carnaval moderne", "Un masque chirurgical", "Un masque de théâtre grec"], "Un masque utilisé lors de cérémonies religieuses ou sociales", "Les masques africains en sont des exemples."),
]),
notion('AM-5', 0, F, 'artm-objet-musee-statut', [
  Q("Qu'est-ce qui peut transformer un objet ordinaire en œuvre d'art ?", ["Le choix de l'artiste et son exposition dans un lieu d'art", "Son prix", "Sa couleur", "Son poids"], "Le choix de l'artiste et son exposition dans un lieu d'art", "Duchamp l'a montré avec ses ready-mades."),
  Q("Pourquoi certains musées exposent-ils des objets de la vie quotidienne d'autrefois ?", ["Pour témoigner de l'histoire et des modes de vie", "Pour les vendre", "Pour les jeter", "Par erreur"], "Pour témoigner de l'histoire et des modes de vie", "Ce sont des musées d'ethnographie ou de société."),
  Q("Quel musée marseillais est consacré aux civilisations de l'Europe et de la Méditerranée ?", ["Le Mucem", "Le Louvre", "Le musée d'Orsay", "Le musée Picasso"], "Le Mucem", "Il ouvre en 2013."),
]),
notion('AM-5', 0, F, 'artm-affiche-objet-pop', [
  Q("Quel artiste a représenté une boîte de lessive Brillo comme une sculpture ?", ["Andy Warhol", "Marcel Duchamp", "Claes Oldenburg", "Jasper Johns"], "Andy Warhol", "Brillo Boxes (1964)."),
  Q("Quel objet du quotidien le pop art a-t-il souvent représenté ?", ["Des produits de consommation (soupe, soda, hamburger)", "Des armures", "Des icônes religieuses", "Des épées"], "Des produits de consommation (soupe, soda, hamburger)", "Il célèbre et critique la consommation."),
  Q("Pourquoi les Brillo Boxes de Warhol posent-elles une question philosophique ?", ["Elles sont presque identiques aux vraies boîtes : qu'est-ce qui en fait une œuvre ?", "Elles sont en or", "Elles sont très petites", "Elles sont abstraites"], "Elles sont presque identiques aux vraies boîtes : qu'est-ce qui en fait une œuvre ?", "Le philosophe Arthur Danto en a fait un exemple célèbre."),
]),
notion('AM-5', 0, F, 'artm-objets-pouvoir', [
  Q("Quels objets symbolisent le pouvoir royal ?", ["La couronne, le sceptre, le trône", "Le balai, la casserole", "Le crayon, la gomme", "La bicyclette"], "La couronne, le sceptre, le trône", "On les appelle les regalia."),
  Q("Où sont conservés les joyaux de la Couronne britannique ?", ["À la tour de Londres", "Au British Museum", "À Buckingham", "À Westminster"], "À la tour de Londres", "Ils sont exposés au public."),
  Q("Pourquoi un objet peut-il devenir un symbole ?", ["Il représente une idée, une institution ou un pouvoir", "Il est très lourd", "Il est récent", "Il est petit"], "Il représente une idée, une institution ou un pouvoir", "La couronne symbolise la monarchie."),
]),
notion('AM-5', 0, I, 'artm-vanite-objets', [
  Q("Quels objets trouve-t-on souvent dans une vanité ?", ["Un crâne, une bougie, un sablier, des fleurs fanées", "Des jouets neufs", "Des drapeaux", "Des armes de guerre"], "Un crâne, une bougie, un sablier, des fleurs fanées", "Ils rappellent la mort et le temps qui passe."),
  Q("Que signifie l'expression latine « memento mori » ?", ["Souviens-toi que tu vas mourir", "Profite du jour", "Le temps s'enfuit", "La vie est belle"], "Souviens-toi que tu vas mourir", "Carpe diem = cueille le jour."),
  Q("Quel artiste contemporain a incrusté un crâne de diamants (For the Love of God, 2007) ?", ["Damien Hirst", "Jeff Koons", "Banksy", "Ai Weiwei"], "Damien Hirst", "C'est une vanité contemporaine."),
]),
notion('AM-5', 0, I, 'artm-design-icones', [
  Q("Quel designer a créé des fauteuils et chaises en contreplaqué moulé avec son épouse Ray ?", ["Charles Eames", "Philippe Starck", "Marcel Breuer", "Le Corbusier"], "Charles Eames", "Le Lounge Chair (1956)."),
  Q("Quel designer français a créé le presse-agrume Juicy Salif en forme d'araignée ?", ["Philippe Starck", "Charlotte Perriand", "Jean Prouvé", "Pierre Paulin"], "Philippe Starck", "Il date de 1990."),
  Q("Quelle designer française a collaboré avec Le Corbusier sur la chaise longue LC4 ?", ["Charlotte Perriand", "Eileen Gray", "Sonia Delaunay", "Coco Chanel"], "Charlotte Perriand", "Elle date de 1928."),
]),
notion('AM-5', 0, I, 'artm-objet-ethnographique', [
  Q("Quelle question pose aujourd'hui la présence d'objets africains dans les musées européens ?", ["Celle de leur acquisition pendant la colonisation et de leur restitution", "Celle de leur couleur", "Celle de leur poids", "Aucune"], "Celle de leur acquisition pendant la colonisation et de leur restitution", "Un rapport de 2018 a relancé le débat."),
  Q("Quels objets la France a-t-elle restitués au Bénin en 2021 ?", ["26 œuvres du trésor royal d'Abomey", "La Joconde", "Des tableaux impressionnistes", "Des vases grecs"], "26 œuvres du trésor royal d'Abomey", "Elles avaient été pillées en 1892."),
  Q("Quels bronzes africains, pillés par les Britanniques en 1897, sont réclamés par le Nigeria ?", ["Les bronzes du Bénin (royaume d'Edo)", "Les bronzes de Rodin", "Les bronzes grecs", "Les bronzes chinois"], "Les bronzes du Bénin (royaume d'Edo)", "Certains ont été restitués depuis 2022."),
]),
notion('AM-5', 0, I, 'artm-objet-precieux', [
  Q("Quel orfèvre italien de la Renaissance a créé une salière en or pour François Ier ?", ["Benvenuto Cellini", "Michel-Ange", "Donatello", "Ghiberti"], "Benvenuto Cellini", "Elle est conservée à Vienne."),
  Q("Quels œufs précieux le joaillier Fabergé créait-il pour les tsars de Russie ?", ["Des œufs de Pâques en métaux précieux et pierres", "Des œufs en chocolat", "Des œufs en céramique simple", "Des œufs en bois"], "Des œufs de Pâques en métaux précieux et pierres", "Chacun contenait une surprise."),
  Q("Qu'est-ce qui fait la valeur d'un objet d'art ?", ["Sa rareté, sa qualité, son histoire et son auteur", "Uniquement son poids", "Uniquement sa taille", "Uniquement son âge"], "Sa rareté, sa qualité, son histoire et son auteur", "La valeur est aussi symbolique."),
]),
notion('AM-5', 0, I, 'artm-objet-trompe-oeil', [
  Q("Quel peintre a représenté des objets si réalistes qu'on croit pouvoir les saisir (trompe-l'œil) ?", ["Cornelis Gijsbrechts", "Wassily Kandinsky", "Piet Mondrian", "Jackson Pollock"], "Cornelis Gijsbrechts", "Il a même peint le revers d'un tableau."),
  Q("Quel sculpteur hyperréaliste américain crée des personnages ordinaires si réels qu'on les confond avec des visiteurs ?", ["Duane Hanson", "Henry Moore", "Alberto Giacometti", "Auguste Rodin"], "Duane Hanson", "Tourists (1970)."),
  Q("Quel effet cherche un trompe-l'œil ?", ["Faire croire que l'objet peint est réel", "Montrer qu'il s'agit d'une peinture", "Abstraire l'objet", "Rendre l'objet flou"], "Faire croire que l'objet peint est réel", "Le spectateur est piégé."),
]),
notion('AM-5', 0, I, 'artm-bauhaus-objet', [
  Q("Quelle formule résume l'esprit du design moderne : la forme découle de l'usage ?", ["« Form follows function »", "« Less is more »", "« Art for art's sake »", "« Small is beautiful »"], "« Form follows function »", "Elle est attribuée à l'architecte Louis Sullivan."),
  Q("Quelle école allemande a réuni art, artisanat et industrie à partir de 1919 ?", ["Le Bauhaus", "L'École des beaux-arts", "La Sorbonne", "L'Académie royale"], "Le Bauhaus", "Fondée par Walter Gropius à Weimar."),
  Q("Quelle théière en métal aux formes géométriques est une icône du Bauhaus ?", ["La théière de Marianne Brandt", "La théière de Wedgwood", "La théière Alessi", "La théière de Sèvres"], "La théière de Marianne Brandt", "Elle date de 1924."),
]),
notion('AM-5', 0, I, 'artm-objet-photo-publicite', [
  Q("Comment la publicité met-elle en valeur un objet ?", ["Par la lumière, le cadrage, le décor et le slogan", "En le cachant", "En le salissant", "En le cassant"], "Par la lumière, le cadrage, le décor et le slogan", "Elle construit son désir."),
  Q("Qu'est-ce qu'un packshot ?", ["La photo d'un produit isolé sur fond neutre", "Une photo de famille", "Un tableau", "Une vidéo de voyage"], "La photo d'un produit isolé sur fond neutre", "On la voit dans les catalogues."),
  Q("Quel artiste a représenté de façon monumentale une bouteille de Coca-Cola ?", ["Andy Warhol", "Claude Monet", "Auguste Rodin", "Raphaël"], "Andy Warhol", "Green Coca-Cola Bottles (1962)."),
]),
notion('AM-5', 0, I, 'artm-objet-recit', [
  Q("Que peut raconter un objet dans une œuvre ?", ["Une histoire, une époque, une personne ou un souvenir", "Rien", "Seulement son prix", "Seulement sa couleur"], "Une histoire, une époque, une personne ou un souvenir", "L'objet est un témoin."),
  Q("Dans la peinture flamande, que suggère un chien aux pieds d'un couple ?", ["La fidélité", "La colère", "La richesse uniquement", "La maladie"], "La fidélité", "Les objets et animaux ont souvent une valeur symbolique."),
  Q("Quel musée raconte l'histoire du monde à travers des objets, dans un célèbre podcast de la BBC ?", ["Le British Museum (L'Histoire du monde en 100 objets)", "Le Louvre", "Le MoMA", "Le Prado"], "Le British Museum (L'Histoire du monde en 100 objets)", "Neil MacGregor l'a présenté en 2010."),
]),
notion('AM-5', 0, D, 'artm-danto-transfiguration', [
  Q("Quel philosophe américain a analysé la « transfiguration du banal » en art ?", ["Arthur Danto", "Clement Greenberg", "Walter Benjamin", "Theodor Adorno"], "Arthur Danto", "Il part des Brillo Boxes de Warhol."),
  Q("Qu'est-ce que le « monde de l'art » selon Danto ?", ["Le contexte de théories et d'institutions qui permet de reconnaître une œuvre", "Un musée précis", "Le marché de l'art", "Une galerie new-yorkaise"], "Le contexte de théories et d'institutions qui permet de reconnaître une œuvre", "Sans ce contexte, une boîte reste une boîte."),
  Q("Quel sociologue a étudié comment les institutions et les publics « font » la valeur de l'art ?", ["Pierre Bourdieu", "Émile Durkheim", "Max Weber", "Auguste Comte"], "Pierre Bourdieu", "La Distinction (1979)."),
]),
notion('AM-5', 0, D, 'artm-musee-patrimoine-industriel', [
  Q("Quel musée parisien est installé dans une ancienne gare ?", ["Le musée d'Orsay", "Le Centre Pompidou", "Le Louvre", "Le Grand Palais"], "Le musée d'Orsay", "Il ouvre en 1986."),
  Q("Quel ancien site industriel de la Ruhr, en Allemagne, est devenu un lieu culturel classé à l'Unesco ?", ["La mine de Zollverein", "Le Reichstag", "La Porte de Brandebourg", "Le château de Neuschwanstein"], "La mine de Zollverein", "Elle est à Essen."),
  Q("Pourquoi transforme-t-on d'anciens lieux industriels en musées ?", ["Pour préserver la mémoire et donner une nouvelle vie aux bâtiments", "Pour les détruire plus tard", "Parce qu'ils sont neufs", "Par obligation de l'Unesco"], "Pour préserver la mémoire et donner une nouvelle vie aux bâtiments", "La Tate Modern en est un exemple."),
]),
notion('AM-5', 0, D, 'artm-marche-art-objet', [
  Q("Quelle banane scotchée au mur de Maurizio Cattelan a été vendue plus de 6 millions de dollars en 2024 ?", ["Comedian", "Fountain", "Balloon Dog", "America"], "Comedian", "Son acheteur l'a mangée."),
  Q("Quelles grandes maisons de ventes aux enchères dominent le marché de l'art ?", ["Christie's et Sotheby's", "Amazon et eBay", "Ikea et Conforama", "Leroy Merlin et Castorama"], "Christie's et Sotheby's", "Elles sont nées à Londres au XVIIIe siècle."),
  Q("Qu'achète vraiment le collectionneur de Comedian ?", ["Un certificat d'authenticité et le droit de remplacer la banane", "Une banane unique et éternelle", "Une photo", "Rien"], "Un certificat d'authenticité et le droit de remplacer la banane", "L'idée prime sur l'objet."),
]),
notion('AM-5', 0, D, 'artm-objet-politique', [
  Q("Quel artiste a fondu des armes pour en faire des objets ou des sculptures pour la paix ?", ["Pedro Reyes (Palas por Pistolas)", "Jeff Koons", "Andy Warhol", "Claes Oldenburg"], "Pedro Reyes (Palas por Pistolas)", "Il a transformé des pistolets en pelles pour planter des arbres."),
  Q("Quelle sculpture devant le siège de l'ONU représente un revolver au canon noué ?", ["Non-Violence de Carl Fredrik Reuterswärd", "Le Penseur", "La Liberté", "Balloon Dog"], "Non-Violence de Carl Fredrik Reuterswärd", "Elle date de 1985."),
  Q("Comment un objet peut-il porter un message politique ?", ["Par sa transformation, son détournement ou le contexte où il est exposé", "Il ne le peut pas", "Seulement par son prix", "Seulement s'il parle"], "Par sa transformation, son détournement ou le contexte où il est exposé", "L'objet devient argument."),
]),
notion('AM-5', 0, D, 'artm-ikea-serie', [
  Q("Qu'est-ce qui distingue un objet de série d'une œuvre unique ?", ["Il est produit en grand nombre de façon identique", "Il est toujours plus beau", "Il est toujours plus cher", "Il est fait à la main"], "Il est produit en grand nombre de façon identique", "L'industrie a transformé notre rapport aux objets."),
  Q("Qu'est-ce qu'une édition limitée en design ?", ["Un objet produit en nombre restreint et numéroté", "Un objet unique", "Un objet gratuit", "Un objet défectueux"], "Un objet produit en nombre restreint et numéroté", "Elle augmente la rareté."),
  Q("Quel mouvement italien des années 1980 a créé des meubles colorés et ludiques ?", ["Le groupe Memphis", "Le Bauhaus", "De Stijl", "L'Art nouveau"], "Le groupe Memphis", "Fondé par Ettore Sottsass."),
]),
notion('AM-5', 0, D, 'artm-art-nouveau-objets', [
  Q("Quel mouvement de la fin du XIXe siècle s'inspire des formes végétales dans les objets et l'architecture ?", ["L'Art nouveau", "L'Art déco", "Le Bauhaus", "Le minimalisme"], "L'Art nouveau", "Les entrées du métro de Paris d'Hector Guimard en sont un exemple."),
  Q("Quel verrier de l'école de Nancy a créé des vases inspirés de la nature ?", ["Émile Gallé", "René Lalique", "Louis Comfort Tiffany", "Daum"], "Émile Gallé", "Daum et Lalique sont aussi célèbres."),
  Q("Quel mouvement des années 1920-1930 privilégie les formes géométriques et les matériaux luxueux ?", ["L'Art déco", "L'Art nouveau", "Le pop art", "L'art brut"], "L'Art déco", "Le Chrysler Building à New York en est un exemple."),
]),
notion('AM-5', 0, D, 'artm-objet-cinema-memoire', [
  Q("Quel musée parisien conserve des objets et costumes de l'histoire du cinéma ?", ["La Cinémathèque française", "Le musée Rodin", "Le musée de l'Orangerie", "Le Petit Palais"], "La Cinémathèque française", "Elle a été cofondée par Henri Langlois."),
  Q("Pourquoi les accessoires de films célèbres deviennent-ils des objets de collection ?", ["Ils sont chargés de mémoire et de célébrité", "Ils sont utiles", "Ils sont récents", "Ils sont faits en or"], "Ils sont chargés de mémoire et de célébrité", "Les souliers rouges du Magicien d'Oz valent des millions."),
  Q("Qu'est-ce qu'un « fétiche » dans le langage courant de l'art ?", ["Un objet auquel on attribue une valeur particulière, presque magique", "Un pinceau", "Un mur", "Une couleur"], "Un objet auquel on attribue une valeur particulière, presque magique", "Le mot a un sens anthropologique précis."),
]),
notion('AM-5', 0, D, 'artm-objet-sculpture-statue', [
  Q("Quelle différence y a-t-il entre une statue et un objet décoratif ?", ["La statue représente un être et a une fonction symbolique ou commémorative", "Aucune", "La statue est toujours petite", "L'objet décoratif est toujours ancien"], "La statue représente un être et a une fonction symbolique ou commémorative", "Mais les frontières sont mouvantes."),
  Q("Pourquoi certaines statues publiques ont-elles été déboulonnées ces dernières années ?", ["Elles honoraient des personnages liés à l'esclavage ou au colonialisme", "Elles étaient trop lourdes", "Elles étaient mal faites", "Pour les nettoyer"], "Elles honoraient des personnages liés à l'esclavage ou au colonialisme", "Comme celle d'Edward Colston à Bristol en 2020."),
  Q("Qu'est-ce qu'un monument commémoratif ?", ["Une œuvre publique qui rappelle un événement ou des personnes", "Un magasin", "Une maison privée", "Un tableau de musée"], "Une œuvre publique qui rappelle un événement ou des personnes", "Les monuments aux morts en sont des exemples."),
]),
# ══ AM-6 · Le numérique en tant que processus et matériau artistiques ══
notion('AM-6', 0, F, 'artm-tablette-dessin', [
  Q("Quel avantage offre le bouton « annuler » en dessin numérique ?", ["On peut revenir en arrière après une erreur", "On efface tout définitivement", "On imprime directement", "On ferme l'application"], "On peut revenir en arrière après une erreur", "Ce n'est pas possible en peinture traditionnelle."),
  Q("Quel outil numérique remplit une zone de couleur d'un seul clic ?", ["Le pot de peinture (remplissage)", "La gomme", "La loupe", "Le texte"], "Le pot de peinture (remplissage)", "Il colore une zone fermée."),
  Q("Quel outil numérique permet de sélectionner une couleur dans une image ?", ["La pipette", "Le pinceau", "Le crayon", "La gomme"], "La pipette", "Elle « prélève » la couleur."),
]),
notion('AM-6', 0, F, 'artm-formats-fichiers', [
  Q("Quel format d'image est le plus courant pour les photos ?", ["JPEG", "MP3", "DOCX", "MP4"], "JPEG", "MP3 est un format audio."),
  Q("Quel format d'image conserve la transparence ?", ["PNG", "JPEG", "TXT", "WAV"], "PNG", "Utile pour les logos."),
  Q("Quel format est utilisé pour les vidéos ?", ["MP4", "PNG", "JPEG", "PDF"], "MP4", "Il est très répandu."),
]),
notion('AM-6', 0, F, 'artm-photo-tablette', [
  Q("Que permet la fonction « recadrer » sur une photo numérique ?", ["Supprimer une partie de l'image pour changer le cadrage", "Agrandir le fichier", "Changer la couleur", "Envoyer la photo"], "Supprimer une partie de l'image pour changer le cadrage", "On choisit ce qu'on garde."),
  Q("Que fait le réglage de « luminosité » ?", ["Il éclaircit ou assombrit l'image", "Il change la forme", "Il ajoute du son", "Il supprime les couleurs"], "Il éclaircit ou assombrit l'image", "Le contraste règle l'écart entre clairs et sombres."),
  Q("Qu'est-ce qu'un panorama en photographie numérique ?", ["Une image large obtenue en assemblant plusieurs photos", "Une photo floue", "Une photo verticale", "Un portrait"], "Une image large obtenue en assemblant plusieurs photos", "Le téléphone le fait automatiquement."),
]),
notion('AM-6', 0, F, 'artm-animation-numerique', [
  Q("Combien d'images par seconde faut-il environ pour une animation fluide ?", ["Environ 24", "1", "100 au minimum", "3"], "Environ 24", "En dessous, le mouvement paraît saccadé."),
  Q("Qu'est-ce qu'une image clé (keyframe) en animation ?", ["Une image importante qui marque un moment du mouvement", "Une clé dessinée", "La dernière image", "Le titre"], "Une image importante qui marque un moment du mouvement", "Le logiciel calcule les images intermédiaires."),
  Q("Quelle application permet de réaliser un film d'animation image par image en classe ?", ["Une application de stop motion sur tablette", "Un tableur", "Un traitement de texte", "Une calculatrice"], "Une application de stop motion sur tablette", "Avec de la pâte à modeler ou des objets."),
]),
notion('AM-6', 0, F, 'artm-son-numerique', [
  Q("Peut-on créer de la musique avec un ordinateur ?", ["Oui, avec des logiciels de création musicale", "Non, jamais", "Seulement avec un micro", "Seulement au cinéma"], "Oui, avec des logiciels de création musicale", "On parle de MAO (musique assistée par ordinateur)."),
  Q("Qu'est-ce qu'un sample (échantillon) ?", ["Un extrait sonore réutilisé dans une nouvelle création", "Un instrument", "Une partition", "Un casque"], "Un extrait sonore réutilisé dans une nouvelle création", "Le hip-hop l'utilise beaucoup."),
  Q("Qu'est-ce qu'une boucle (loop) en musique numérique ?", ["Un motif sonore répété en continu", "Un nœud de câble", "Une erreur", "Un silence"], "Un motif sonore répété en continu", "Elle sert de base rythmique."),
]),
notion('AM-6', 0, F, 'artm-qr-code-art', [
  Q("Qu'est-ce qu'un QR code ?", ["Un code-barres en carré qu'on scanne avec un téléphone", "Une œuvre de Mondrian", "Une police d'écriture", "Une couleur"], "Un code-barres en carré qu'on scanne avec un téléphone", "Les musées en utilisent pour les audioguides."),
  Q("À quoi peut servir un QR code à côté d'une œuvre dans un musée ?", ["À accéder à des informations, du son ou une vidéo", "À acheter l'œuvre", "À éteindre la lumière", "À ouvrir la vitrine"], "À accéder à des informations, du son ou une vidéo", "Il enrichit la visite."),
  Q("Qu'est-ce qu'un audioguide ?", ["Un appareil ou une application qui commente les œuvres à l'oreille", "Un guide de musique", "Un casque de chantier", "Une radio"], "Un appareil ou une application qui commente les œuvres à l'oreille", "Il existe en plusieurs langues."),
]),
notion('AM-6', 0, F, 'artm-ecran-support', [
  Q("Un écran peut-il être un support d'œuvre d'art ?", ["Oui, comme la toile ou le papier", "Non, jamais", "Seulement au cinéma", "Seulement pour la publicité"], "Oui, comme la toile ou le papier", "L'art vidéo et numérique l'utilisent."),
  Q("Qu'est-ce qu'un fond d'écran ?", ["L'image affichée en arrière-plan d'un écran", "Un tableau ancien", "Un mur peint", "Un écran éteint"], "L'image affichée en arrière-plan d'un écran", "Certains artistes en ont créé."),
  Q("Pourquoi la taille de l'écran change-t-elle la perception d'une œuvre numérique ?", ["L'échelle modifie l'impression et les détails visibles", "Elle ne change rien", "Elle change la couleur", "Elle supprime le son"], "L'échelle modifie l'impression et les détails visibles", "Comme pour la peinture."),
]),
notion('AM-6', 0, F, 'artm-avatar', [
  Q("Qu'est-ce qu'un avatar ?", ["Une représentation de soi dans un univers numérique", "Un animal", "Un tableau ancien", "Un appareil photo"], "Une représentation de soi dans un univers numérique", "Le mot vient du sanskrit."),
  Q("Qu'est-ce qu'un émoji ?", ["Un petit pictogramme exprimant une émotion ou une idée", "Un mot anglais", "Une photo de profil", "Un virus"], "Un petit pictogramme exprimant une émotion ou une idée", "Ils sont nés au Japon."),
  Q("Quel musée a fait entrer les premiers émojis dans ses collections en 2016 ?", ["Le MoMA de New York", "Le Louvre", "Le Prado", "La Tate"], "Le MoMA de New York", "Les 176 émojis de Shigetaka Kurita."),
]),
notion('AM-6', 0, I, 'artm-code-creatif', [
  Q("Qu'est-ce que le « creative coding » ?", ["Programmer pour créer des images, des sons ou des animations", "Coder un mot de passe", "Réparer un ordinateur", "Écrire un roman"], "Programmer pour créer des images, des sons ou des animations", "L'artiste écrit des instructions."),
  Q("Quel langage visuel permet aux élèves de programmer des animations avec des blocs ?", ["Scratch", "Python", "Excel", "HTML"], "Scratch", "Il est utilisé au collège."),
  Q("Qu'apporte le hasard programmé (aléatoire) à une œuvre numérique ?", ["Des variations imprévisibles à chaque exécution", "Une image toujours identique", "Une erreur", "Rien"], "Des variations imprévisibles à chaque exécution", "L'œuvre peut être différente à chaque fois."),
]),
notion('AM-6', 0, I, 'artm-interactivite-capteurs', [
  Q("Qu'est-ce qu'un capteur dans une installation interactive ?", ["Un dispositif qui détecte le mouvement, le son ou la présence", "Un pinceau", "Un cadre", "Une lampe"], "Un dispositif qui détecte le mouvement, le son ou la présence", "L'œuvre réagit au visiteur."),
  Q("Quelle carte électronique est souvent utilisée par les artistes pour créer des objets interactifs ?", ["Arduino", "Une carte bancaire", "Une carte mère de télé", "Une carte postale"], "Arduino", "Elle est née en Italie en 2005."),
  Q("Que change l'interactivité dans le rôle du spectateur ?", ["Il devient acteur de l'œuvre", "Il devient spectateur passif", "Il doit payer plus", "Il doit se taire"], "Il devient acteur de l'œuvre", "Son geste modifie l'œuvre."),
]),
notion('AM-6', 0, I, 'artm-numerisation-patrimoine', [
  Q("Comment a-t-on numérisé Notre-Dame de Paris avant l'incendie ?", ["Grâce à un relevé laser 3D réalisé par un chercheur", "Avec des dessins à la main", "Avec des photos d'enfants", "On ne l'avait pas fait"], "Grâce à un relevé laser 3D réalisé par un chercheur", "Andrew Tallon avait scanné l'édifice."),
  Q("Pourquoi numérise-t-on les grottes ornées comme Lascaux ?", ["Pour les étudier et les montrer sans abîmer les originaux", "Pour les fermer définitivement", "Pour les vendre", "Pour les repeindre"], "Pour les étudier et les montrer sans abîmer les originaux", "Lascaux IV est une réplique."),
  Q("Qu'est-ce qu'une réplique (fac-similé) ?", ["Une copie fidèle d'une œuvre ou d'un lieu", "Une œuvre originale", "Une restauration", "Une signature"], "Une copie fidèle d'une œuvre ou d'un lieu", "Elle protège l'original."),
]),
notion('AM-6', 0, I, 'artm-photomontage-numerique', [
  Q("Quelle artiste allemande a réalisé des photomontages critiques dans les années 1920 ?", ["Hannah Höch", "Frida Kahlo", "Dora Maar", "Tamara de Lempicka"], "Hannah Höch", "Elle appartient au mouvement Dada."),
  Q("Quel artiste allemand a réalisé des photomontages contre Hitler dans les années 1930 ?", ["John Heartfield", "Max Ernst", "Kurt Schwitters", "George Grosz"], "John Heartfield", "Ses images paraissaient dans un magazine ouvrier."),
  Q("Comment le numérique a-t-il transformé le photomontage ?", ["Il le rend plus facile et plus difficile à détecter", "Il l'a fait disparaître", "Il l'a rendu illégal", "Il n'a rien changé"], "Il le rend plus facile et plus difficile à détecter", "D'où l'importance de l'esprit critique."),
]),
notion('AM-6', 0, I, 'artm-jeu-video-creation', [
  Q("Quel jeu vidéo de construction est utilisé comme outil créatif à l'école ?", ["Minecraft", "Tetris", "Pac-Man", "Pong"], "Minecraft", "Il existe une version éducation."),
  Q("Qu'est-ce qu'un « level design » ?", ["La conception des niveaux et des espaces d'un jeu", "Le choix de la musique", "La vente d'un jeu", "Le niveau de difficulté"], "La conception des niveaux et des espaces d'un jeu", "C'est un travail d'architecte virtuel."),
  Q("Quel jeu vidéo de 2012 (Journey) est souvent cité pour sa dimension artistique ?", ["Journey", "Fortnite", "FIFA", "Call of Duty"], "Journey", "Il ne contient presque aucun texte."),
]),
notion('AM-6', 0, I, 'artm-son-image-sync', [
  Q("Qu'est-ce qu'un clip vidéo musical ?", ["Un court film qui accompagne une chanson", "Un concert en direct", "Une affiche", "Un disque"], "Un court film qui accompagne une chanson", "MTV l'a popularisé dans les années 1980."),
  Q("Quel réalisateur français est célèbre pour ses clips inventifs (Daft Punk, Björk) ?", ["Michel Gondry", "Luc Besson", "François Truffaut", "Jean Renoir"], "Michel Gondry", "Il mélange bricolage et effets visuels."),
  Q("Qu'est-ce qu'un VJ ?", ["Un artiste qui mixe des images en direct, comme un DJ mixe des sons", "Un journaliste vidéo", "Un juge", "Un vendeur de jeux"], "Un artiste qui mixe des images en direct, comme un DJ mixe des sons", "Video jockey."),
]),
notion('AM-6', 0, I, 'artm-imprimante-laser-decoupe', [
  Q("Qu'est-ce qu'une découpeuse laser ?", ["Une machine qui découpe ou grave des matériaux à partir d'un fichier numérique", "Un pistolet", "Un projecteur", "Un ciseau"], "Une machine qui découpe ou grave des matériaux à partir d'un fichier numérique", "On en trouve dans les fab labs."),
  Q("Pourquoi dit-on que le numérique transforme le geste de l'artiste ?", ["La machine exécute ce que l'artiste conçoit à l'écran", "L'artiste ne dessine plus jamais", "La main est interdite", "Rien ne change"], "La machine exécute ce que l'artiste conçoit à l'écran", "Le geste se déplace vers la conception."),
  Q("Qu'est-ce que la fabrication numérique ?", ["Produire des objets réels à partir de fichiers numériques (impression 3D, laser)", "Faire des photos", "Écrire un e-mail", "Regarder un film"], "Produire des objets réels à partir de fichiers numériques (impression 3D, laser)", "Le virtuel devient matière."),
]),
notion('AM-6', 0, D, 'artm-ia-processus', [
  Q("Qu'est-ce qu'un « prompt » pour une IA génératrice d'images ?", ["La description textuelle donnée pour produire une image", "Un pinceau numérique", "Un format de fichier", "Un écran"], "La description textuelle donnée pour produire une image", "Le choix des mots influence le résultat."),
  Q("Sur quoi les IA génératrices d'images ont-elles été entraînées ?", ["Sur d'immenses quantités d'images et de textes existants", "Sur rien", "Uniquement sur des photos de chats", "Sur des sculptures"], "Sur d'immenses quantités d'images et de textes existants", "D'où les débats sur le droit d'auteur."),
  Q("Une image produite par IA peut-elle être protégée par le droit d'auteur en France ?", ["La question est débattue : il faut une intervention créative humaine", "Oui, toujours au nom de l'IA", "Oui, au nom de l'ordinateur", "Non, elle appartient à l'État"], "La question est débattue : il faut une intervention créative humaine", "Le droit d'auteur protège l'œuvre de l'esprit humain."),
]),
notion('AM-6', 0, D, 'artm-donnees-art', [
  Q("Qu'est-ce que la data visualisation ?", ["La mise en forme graphique de données", "La visite d'un data center", "Un logiciel de dessin", "Un film documentaire"], "La mise en forme graphique de données", "Certains artistes en font des œuvres."),
  Q("Quel artiste japonais transforme des flux de données en installations audiovisuelles massives ?", ["Ryoji Ikeda", "Takashi Murakami", "Yayoi Kusama", "Hokusai"], "Ryoji Ikeda", "Ses œuvres sont en noir et blanc, rythmées."),
  Q("Pourquoi des artistes utilisent-ils des données comme matériau ?", ["Pour rendre visible et sensible un monde invisible (climat, réseaux, flux)", "Pour vendre des données", "Par hasard", "Pour espionner"], "Pour rendre visible et sensible un monde invisible (climat, réseaux, flux)", "Les données deviennent formes."),
]),
notion('AM-6', 0, D, 'artm-cyborg-bioart', [
  Q("Quel artiste australien s'est fait greffer une oreille sur le bras ?", ["Stelarc", "ORLAN", "Marina Abramović", "Ron Mueck"], "Stelarc", "Il explore le corps augmenté."),
  Q("Qu'est-ce que le bio-art ?", ["Un art qui utilise des organismes vivants et des biotechnologies", "Un art de produits bio", "Un art de jardinage", "Un art de la cuisine"], "Un art qui utilise des organismes vivants et des biotechnologies", "Il soulève des questions éthiques."),
  Q("Quel artiste a créé un lapin vert fluorescent grâce à une protéine de méduse (GFP Bunny, 2000) ?", ["Eduardo Kac", "Damien Hirst", "Jeff Koons", "Stelarc"], "Eduardo Kac", "L'œuvre a suscité une vive polémique."),
]),
notion('AM-6', 0, D, 'artm-conservation-numerique', [
  Q("Pourquoi les œuvres numériques sont-elles difficiles à conserver ?", ["Les logiciels, formats et machines deviennent obsolètes", "Elles sont trop lourdes", "Elles prennent la poussière", "Elles sont en papier"], "Les logiciels, formats et machines deviennent obsolètes", "On parle d'obsolescence technologique."),
  Q("Qu'est-ce que l'émulation pour conserver une œuvre numérique ?", ["Faire fonctionner un ancien logiciel sur une machine récente", "Copier l'œuvre à la main", "Imprimer l'œuvre", "Détruire l'œuvre"], "Faire fonctionner un ancien logiciel sur une machine récente", "Elle permet de rejouer d'anciennes œuvres."),
  Q("Quelle institution française dépôt légal archive aussi le web ?", ["La Bibliothèque nationale de France (BnF)", "Le Louvre", "Le Sénat", "La Poste"], "La Bibliothèque nationale de France (BnF)", "Avec l'INA pour l'audiovisuel."),
]),
notion('AM-6', 0, D, 'artm-ecran-pixels-artistes', [
  Q("Quel peintre, par ses petits points de couleur pure, annonce la logique des pixels ?", ["Georges Seurat", "Claude Monet", "Raphaël", "Rembrandt"], "Georges Seurat", "Le mélange se fait dans l'œil, comme sur un écran."),
  Q("Quel jeu vidéo est entièrement construit en cubes, comme une sculpture de voxels ?", ["Minecraft", "Tetris", "Pac-Man", "Pong"], "Minecraft", "Chaque cube est un bloc de construction."),
  Q("Qu'est-ce qu'un voxel ?", ["L'équivalent d'un pixel en trois dimensions", "Un format audio", "Une couleur", "Un appareil photo"], "L'équivalent d'un pixel en trois dimensions", "Minecraft est construit en voxels."),
]),
notion('AM-6', 0, D, 'artm-blockchain-art', [
  Q("Qu'est-ce qu'une blockchain ?", ["Un registre numérique partagé et infalsifiable de transactions", "Une chaîne de blocs en bois", "Un logiciel de dessin", "Un jeu vidéo"], "Un registre numérique partagé et infalsifiable de transactions", "Les NFT l'utilisent."),
  Q("Quel problème les NFT veulent-ils résoudre pour l'art numérique ?", ["Prouver l'authenticité et la propriété d'un fichier copiable", "Rendre les images plus belles", "Imprimer les images", "Réduire la taille des fichiers"], "Prouver l'authenticité et la propriété d'un fichier copiable", "Le fichier lui-même reste copiable."),
  Q("Quelle critique est souvent faite aux NFT ?", ["La spéculation financière et l'impact énergétique", "Leur trop grande beauté", "Leur gratuité", "Leur absence de marché"], "La spéculation financière et l'impact énergétique", "Le marché s'est effondré après 2022."),
]),
notion('AM-6', 0, D, 'artm-ecritures-numeriques', [
  Q("Qu'est-ce qu'une œuvre transmédia ?", ["Une œuvre dont le récit se déploie sur plusieurs supports (film, jeu, web)", "Une œuvre en un seul format", "Une peinture murale", "Un livre de poche"], "Une œuvre dont le récit se déploie sur plusieurs supports (film, jeu, web)", "Le spectateur circule entre les médias."),
  Q("Qu'est-ce que la « poésie numérique » ?", ["Une poésie qui utilise l'animation, l'interactivité ou le code", "Une poésie imprimée", "Une poésie récitée", "Une chanson"], "Une poésie qui utilise l'animation, l'interactivité ou le code", "Le texte bouge, réagit, se transforme."),
  Q("Qu'est-ce qu'un « remix » en art numérique ?", ["Une nouvelle création à partir d'éléments existants recombinés", "Une copie exacte", "Une destruction", "Une restauration"], "Une nouvelle création à partir d'éléments existants recombinés", "Il pose la question des droits."),
]),
notion('AM-6', 0, D, 'artm-artiste-numerique-francais', [
  Q("Quel lieu parisien est consacré aux cultures numériques depuis 2011 ?", ["La Gaîté Lyrique", "Le Panthéon", "L'Opéra Garnier", "Le musée Rodin"], "La Gaîté Lyrique", "Il accueille expositions, concerts et ateliers."),
  Q("Quel lieu parisien est consacré aux expositions numériques immersives dans une ancienne fonderie ?", ["L'Atelier des Lumières", "Le Louvre", "Le musée d'Orsay", "Le Petit Palais"], "L'Atelier des Lumières", "Il a ouvert en 2018."),
  Q("Quel festival d'arts numériques a lieu chaque année à Enghien-les-Bains ?", ["Bains numériques", "Les Rencontres d'Arles", "Le Festival de Cannes", "Le Festival d'Avignon"], "Bains numériques", "Enghien est une « ville créative » de l'Unesco pour les arts numériques."),
]),
notion('AM-6', 0, D, 'artm-photo-computationnelle', [
  Q("Qu'est-ce que la photographie computationnelle des smartphones ?", ["Des images améliorées par des calculs automatiques (HDR, flou d'arrière-plan)", "Des photos sans calcul", "Des photos argentiques", "Des dessins"], "Des images améliorées par des calculs automatiques (HDR, flou d'arrière-plan)", "La photo n'est plus un simple enregistrement."),
  Q("Que signifie HDR en photographie ?", ["Grande plage dynamique : fusion de plusieurs expositions", "Haute définition rapide", "Une marque de téléphone", "Un format audio"], "Grande plage dynamique : fusion de plusieurs expositions", "On voit des détails dans les zones claires et sombres."),
  Q("Pourquoi peut-on dire qu'une photo de smartphone est déjà « interprétée » ?", ["Des algorithmes modifient l'image avant qu'on la voie", "Elle est en noir et blanc", "Elle est floue", "Elle est imprimée"], "Des algorithmes modifient l'image avant qu'on la voie", "Le regard critique est indispensable."),
]),
]

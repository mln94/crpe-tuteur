from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('A-1', 0, F, 'art-portrait', [
  Q("Comment appelle-t-on la représentation d'une personne réelle ?", ["Un paysage", "Un portrait", "Une nature morte", "Une marine"], "Un portrait", "L'autoportrait est le portrait de l'artiste par lui-même."),
  Q("Quel peintre a réalisé La Joconde ?", ["Michel-Ange", "Léonard de Vinci", "Raphaël", "Rembrandt"], "Léonard de Vinci", "Peinte au début du XVIe siècle, elle est conservée au musée du Louvre."),
  Q("Quel peintre néerlandais a réalisé de nombreux autoportraits, dont un avec l'oreille bandée (1889) ?", ["Vincent Van Gogh", "Claude Monet", "Pablo Picasso", "Paul Cézanne"], "Vincent Van Gogh", "Van Gogh a peint plus de 35 autoportraits."),
]),
notion('A-1', 0, F, 'art-genres', [
  Q("Comment appelle-t-on la représentation d'objets inanimés (fruits, vases, fleurs coupées) ?", ["Une nature morte", "Un portrait", "Un paysage", "Une scène de genre"], "Une nature morte", "Les vanités sont des natures mortes qui évoquent la fragilité de la vie."),
  Q("Comment appelle-t-on la représentation de la mer ?", ["Une marine", "Un portrait", "Une vanité", "Une fresque"], "Une marine", "La marine est un genre du paysage."),
  Q("Quel genre était considéré comme le plus prestigieux à l'Académie au XVIIe siècle ?", ["La nature morte", "La peinture d'histoire", "Le paysage", "La scène de genre"], "La peinture d'histoire", "La hiérarchie des genres plaçait l'histoire (religieuse, mythologique, historique) au sommet."),
]),
notion('A-1', 0, F, 'art-realisme-abstraction', [
  Q("Comment appelle-t-on un art qui ne représente pas la réalité visible ?", ["L'art figuratif", "L'art abstrait", "Le réalisme", "L'hyperréalisme"], "L'art abstrait", "Kandinsky est l'un des pionniers de l'abstraction vers 1910."),
  Q("Lequel de ces artistes est un pionnier de l'art abstrait ?", ["Vassily Kandinsky", "Ingres", "Courbet", "David"], "Vassily Kandinsky", "Mondrian et Malevitch sont d'autres pionniers de l'abstraction."),
  Q("Comment appelle-t-on un art qui représente des choses reconnaissables ?", ["L'art figuratif", "L'art abstrait", "L'art conceptuel", "L'art minimal"], "L'art figuratif", "La figuration peut être plus ou moins fidèle à la réalité."),
]),
notion('A-1', 1, F, 'art-perspective', [
  Q("Quelle technique donne l'illusion de la profondeur sur une surface plane ?", ["Le collage", "La perspective", "Le pochoir", "Le modelage"], "La perspective", "La perspective linéaire est théorisée à la Renaissance italienne."),
  Q("En perspective linéaire, comment appelle-t-on le point où convergent les lignes parallèles fuyantes ?", ["Le point de fuite", "Le point de vue", "Le centre", "Le point d'or"], "Le point de fuite", "Il est situé sur la ligne d'horizon."),
  Q("À quelle époque la perspective linéaire est-elle mise au point en Italie ?", ["Au Moyen Âge (XIIe siècle)", "À la Renaissance (XVe siècle)", "Au XIXe siècle", "Dans l'Antiquité grecque"], "À la Renaissance (XVe siècle)", "Brunelleschi et Alberti la théorisent à Florence."),
]),
notion('A-1', 1, F, 'art-plans-cadrage', [
  Q("Dans une image, comment appelle-t-on la partie la plus proche du spectateur ?", ["L'arrière-plan", "Le premier plan", "La ligne d'horizon", "Le hors-champ"], "Le premier plan", "On distingue premier plan, plan moyen et arrière-plan."),
  Q("Qu'est-ce que le hors-champ ?", ["Ce qui est visible au centre de l'image", "Ce qui n'est pas visible dans le cadre mais que le spectateur imagine", "Un champ de blé", "La signature"], "Ce qui n'est pas visible dans le cadre mais que le spectateur imagine", "Le hors-champ est très utilisé au cinéma et en photographie."),
  Q("Comment appelle-t-on une prise de vue de bas en haut, qui grandit le sujet ?", ["La plongée", "La contre-plongée", "Le plan large", "Le travelling"], "La contre-plongée", "La plongée (de haut en bas) tend au contraire à écraser le sujet."),
]),
notion('A-1', 1, F, 'art-composition', [
  Q("Qu'est-ce que la composition d'une œuvre ?", ["Son prix", "L'organisation des éléments dans l'espace de l'œuvre", "La signature", "Le cadre doré"], "L'organisation des éléments dans l'espace de l'œuvre", "Lignes de force, symétrie, équilibre des masses structurent la composition."),
  Q("Qu'est-ce qu'une composition symétrique ?", ["Une composition où les éléments sont répartis de façon équilibrée de part et d'autre d'un axe", "Une composition sans personnage", "Une composition en noir et blanc", "Une composition abstraite"], "Une composition où les éléments sont répartis de façon équilibrée de part et d'autre d'un axe", "Elle donne une impression de stabilité et de solennité."),
  Q("Qu'est-ce qu'une ligne de force dans une image ?", ["Une ligne tracée à la règle", "Une ligne, réelle ou suggérée, qui guide le regard", "Le bord du cadre", "La signature"], "Une ligne, réelle ou suggérée, qui guide le regard", "Les diagonales donnent souvent une impression de mouvement."),
]),
notion('A-1', 2, F, 'art-photographie', [
  Q("En quelle année l'invention de la photographie (daguerréotype) est-elle rendue publique en France ?", ["1789", "1839", "1900", "1950"], "1839", "Niépce réalise les premières images fixées dans les années 1820 ; Daguerre perfectionne le procédé."),
  Q("Qui a réalisé ce qu'on considère comme la plus ancienne photographie conservée, vers 1827 ?", ["Nicéphore Niépce", "Louis Lumière", "Claude Monet", "Gustave Eiffel"], "Nicéphore Niépce", "Point de vue du Gras, prise depuis sa fenêtre, a demandé une très longue exposition."),
  Q("Quel photographe français est célèbre pour la notion d'« instant décisif » ?", ["Henri Cartier-Bresson", "Nadar", "Robert Doisneau", "Man Ray"], "Henri Cartier-Bresson", "Il saisit le moment où forme et sens se rejoignent."),
]),
notion('A-1', 2, F, 'art-cinema', [
  Q("Qui a présenté la première projection publique et payante du cinématographe en 1895 ?", ["Les frères Lumière", "Georges Méliès", "Charlie Chaplin", "Thomas Edison"], "Les frères Lumière", "La projection a lieu le 28 décembre 1895 au Grand Café, à Paris."),
  Q("Quel pionnier du cinéma a réalisé Le Voyage dans la Lune (1902) ?", ["Georges Méliès", "Louis Lumière", "Jean Renoir", "François Truffaut"], "Georges Méliès", "Méliès invente de nombreux trucages."),
  Q("Qu'est-ce qu'un storyboard ?", ["Une affiche de film", "Une suite de dessins qui préparent les plans d'un film", "Le générique", "Un costume"], "Une suite de dessins qui préparent les plans d'un film", "Il ressemble à une bande dessinée du futur film."),
]),
notion('A-1', 2, F, 'art-bande-dessinee', [
  Q("Comment appelle-t-on chaque image d'une bande dessinée ?", ["Une vignette (case)", "Une bulle", "Une planche", "Un strip"], "Une vignette (case)", "Une planche est une page entière ; un strip, une bande de quelques cases."),
  Q("Comment appelle-t-on l'espace qui contient les paroles d'un personnage de BD ?", ["Le cartouche", "La bulle (phylactère)", "La case", "La gouttière"], "La bulle (phylactère)", "Le cartouche contient le texte du narrateur."),
  Q("Qui est le créateur de Tintin ?", ["Goscinny", "Hergé", "Uderzo", "Franquin"], "Hergé", "Tintin apparaît en 1929 ; Astérix est créé par Goscinny et Uderzo en 1959."),
]),
notion('A-1', 2, F, 'art-affiche-image', [
  Q("Quel artiste est célèbre pour ses affiches du Moulin Rouge à la fin du XIXe siècle ?", ["Henri de Toulouse-Lautrec", "Claude Monet", "Auguste Rodin", "Paul Gauguin"], "Henri de Toulouse-Lautrec", "Ses affiches lithographiées ont marqué l'art de l'affiche."),
  Q("Quel artiste du pop art a reproduit en série des images de Marilyn Monroe ?", ["Andy Warhol", "Picasso", "Matisse", "Dalí"], "Andy Warhol", "Warhol utilise la sérigraphie pour reproduire les images de la culture de masse."),
  Q("Quelle technique d'impression utilise un écran de soie ou de tissu ?", ["La gravure", "La sérigraphie", "La photographie", "La fresque"], "La sérigraphie", "L'encre passe à travers les zones non masquées de l'écran."),
]),
notion('A-2', 0, F, 'art-techniques-peinture', [
  Q("Quelle peinture se dilue à l'eau et sèche rapidement ?", ["La peinture à l'huile", "La gouache (ou l'acrylique)", "La cire", "L'émail"], "La gouache (ou l'acrylique)", "La peinture à l'huile sèche lentement et permet des glacis."),
  Q("Qu'est-ce qu'une fresque ?", ["Une peinture sur toile", "Une peinture réalisée sur un enduit frais de mur", "Un dessin au crayon", "Une sculpture"], "Une peinture réalisée sur un enduit frais de mur", "Michel-Ange a peint à fresque le plafond de la chapelle Sixtine."),
  Q("Qu'est-ce que l'aquarelle ?", ["Une peinture épaisse à l'huile", "Une peinture à l'eau, transparente, appliquée sur papier", "Une sculpture en argile", "Un collage"], "Une peinture à l'eau, transparente, appliquée sur papier", "Le blanc du papier sert de lumière."),
]),
notion('A-2', 0, F, 'art-sculpture', [
  Q("Quelle technique de sculpture consiste à enlever de la matière (pierre, bois) ?", ["Le modelage", "La taille", "Le moulage", "L'assemblage"], "La taille", "Le modelage, à l'inverse, ajoute ou façonne une matière malléable (argile)."),
  Q("Qui a sculpté Le Penseur ?", ["Auguste Rodin", "Camille Claudel", "Michel-Ange", "Giacometti"], "Auguste Rodin", "Le Penseur fait d'abord partie de La Porte de l'Enfer."),
  Q("Qu'est-ce qu'une sculpture en ronde-bosse ?", ["Une sculpture attachée à un mur", "Une sculpture dont on peut faire le tour", "Une sculpture plate", "Une peinture"], "Une sculpture dont on peut faire le tour", "Le bas-relief, lui, reste attaché à un fond."),
]),
notion('A-2', 2, F, 'art-couleurs-primaires', [
  Q("Quelles sont les trois couleurs primaires traditionnelles en peinture ?", ["Rouge, vert, bleu", "Rouge (magenta), jaune, bleu (cyan)", "Noir, blanc, gris", "Orange, violet, vert"], "Rouge (magenta), jaune, bleu (cyan)", "Leur mélange permet d'obtenir de nombreuses autres couleurs."),
  Q("Quelle couleur obtient-on en mélangeant du bleu et du jaune ?", ["Violet", "Vert", "Orange", "Marron"], "Vert", "Le vert est une couleur secondaire."),
  Q("Quelle couleur obtient-on en mélangeant du rouge et du jaune ?", ["Orange", "Vert", "Violet", "Rose"], "Orange", "Rouge + bleu donne violet."),
]),
notion('A-2', 2, F, 'art-couleurs-complementaires', [
  Q("Quelle est la couleur complémentaire du rouge ?", ["Le bleu", "Le vert", "Le jaune", "L'orange"], "Le vert", "Les couleurs complémentaires sont opposées sur le cercle chromatique."),
  Q("Quel effet produisent deux couleurs complémentaires juxtaposées ?", ["Elles s'éteignent", "Elles se renforcent mutuellement (contraste)", "Elles deviennent grises", "Aucun effet"], "Elles se renforcent mutuellement (contraste)", "Les impressionnistes et Van Gogh utilisent beaucoup ce contraste."),
  Q("Quelle est la couleur complémentaire du bleu ?", ["L'orange", "Le vert", "Le violet", "Le rouge"], "L'orange", "Jaune et violet sont aussi complémentaires."),
]),
notion('A-2', 2, F, 'art-couleurs-chaudes-froides', [
  Q("Laquelle de ces couleurs est dite « chaude » ?", ["Le bleu", "L'orange", "Le vert", "Le violet"], "L'orange", "Rouge, orange et jaune évoquent la chaleur ; bleu et vert, la fraîcheur."),
  Q("Quel effet produisent souvent les couleurs froides dans un paysage ?", ["Elles rapprochent les éléments", "Elles donnent une impression d'éloignement", "Elles réchauffent la scène", "Aucun"], "Elles donnent une impression d'éloignement", "C'est la perspective atmosphérique : les lointains paraissent bleutés."),
  Q("Comment appelle-t-on les variations d'une même couleur, plus claires ou plus foncées ?", ["Des camaïeux", "Des complémentaires", "Des primaires", "Des contrastes"], "Des camaïeux", "Un camaïeu utilise plusieurs tons d'une même couleur."),
]),
notion('A-2', 3, F, 'art-collage', [
  Q("Quels artistes introduisent le collage (papiers collés) en peinture vers 1912 ?", ["Picasso et Braque", "Monet et Renoir", "David et Ingres", "Rembrandt et Vermeer"], "Picasso et Braque", "Ils intègrent du papier peint, des journaux, une toile cirée."),
  Q("Qu'est-ce qu'un collage en arts plastiques ?", ["Un dessin", "Une œuvre réalisée en assemblant et en collant des matériaux divers", "Une sculpture en marbre", "Une photographie"], "Une œuvre réalisée en assemblant et en collant des matériaux divers", "Matisse réalise à la fin de sa vie des papiers gouachés découpés."),
  Q("Quel artiste réalise les célèbres « papiers découpés » de la série Jazz (1947) ?", ["Henri Matisse", "Salvador Dalí", "Jackson Pollock", "Andy Warhol"], "Henri Matisse", "Il « dessine avec des ciseaux »."),
]),
notion('A-2', 3, F, 'art-ready-made', [
  Q("Quel artiste expose en 1917 un urinoir intitulé Fontaine ?", ["Marcel Duchamp", "Pablo Picasso", "Claude Monet", "Auguste Rodin"], "Marcel Duchamp", "C'est le ready-made le plus célèbre."),
  Q("Qu'est-ce qu'un ready-made ?", ["Une œuvre peinte avec soin", "Un objet manufacturé choisi et présenté comme œuvre d'art", "Une sculpture en bronze", "Une photographie"], "Un objet manufacturé choisi et présenté comme œuvre d'art", "Le geste de l'artiste est le choix, pas la fabrication."),
  Q("Quel ready-made de Duchamp associe une roue de bicyclette et un tabouret (1913) ?", ["Roue de bicyclette", "Fontaine", "Porte-bouteilles", "L.H.O.O.Q."], "Roue de bicyclette", "C'est souvent considéré comme le premier ready-made."),
]),
notion('A-3', 0, F, 'art-trace-geste', [
  Q("Quel peintre américain pratique le « dripping », en faisant couler la peinture sur une toile posée au sol ?", ["Jackson Pollock", "Edward Hopper", "Andy Warhol", "Roy Lichtenstein"], "Jackson Pollock", "Le geste et le mouvement du corps deviennent essentiels."),
  Q("Comment appelle-t-on les mains négatives des grottes préhistoriques ?", ["Des empreintes réalisées en soufflant du pigment autour de la main posée sur la paroi", "Des sculptures", "Des gravures sur os", "Des mosaïques"], "Des empreintes réalisées en soufflant du pigment autour de la main posée sur la paroi", "On en trouve notamment dans la grotte Chauvet et la grotte Cosquer."),
  Q("Quel artiste français a utilisé des corps enduits de peinture bleue comme « pinceaux vivants » ?", ["Yves Klein", "Henri Matisse", "Paul Cézanne", "Georges Seurat"], "Yves Klein", "Ce sont les Anthropométries (1960), réalisées avec son bleu, l'IKB."),
]),
notion('A-3', 1, F, 'art-installation', [
  Q("Qu'est-ce qu'une installation en art contemporain ?", ["Un tableau accroché", "Une œuvre qui occupe un espace et que le spectateur peut parfois parcourir", "Un meuble", "Une affiche"], "Une œuvre qui occupe un espace et que le spectateur peut parfois parcourir", "Le spectateur fait l'expérience de l'œuvre avec son corps."),
  Q("Que signifie qu'une œuvre est créée « in situ » ?", ["Dans un atelier", "Pour un lieu précis, en tenant compte de ses caractéristiques", "En plein air seulement", "Dans un musée uniquement"], "Pour un lieu précis, en tenant compte de ses caractéristiques", "Les colonnes de Buren au Palais-Royal (1986) sont une œuvre in situ."),
  Q("Quel artiste a créé Les Deux Plateaux (colonnes rayées) au Palais-Royal à Paris ?", ["Daniel Buren", "Christo", "Niki de Saint Phalle", "Jean Tinguely"], "Daniel Buren", "Ses bandes verticales de 8,7 cm sont sa signature."),
]),
notion('A-3', 1, F, 'art-land-art', [
  Q("Qu'est-ce que le land art ?", ["Un art réalisé dans la nature, avec ses matériaux", "La peinture de paysages", "L'art des jardins à la française", "La photographie de paysages"], "Un art réalisé dans la nature, avec ses matériaux", "Il apparaît aux États-Unis à la fin des années 1960."),
  Q("Quel artiste britannique crée des œuvres éphémères avec des feuilles, des pierres ou de la glace ?", ["Andy Goldsworthy", "David Hockney", "Banksy", "Francis Bacon"], "Andy Goldsworthy", "Il photographie ses œuvres avant qu'elles ne disparaissent."),
  Q("Pourquoi beaucoup d'œuvres de land art sont-elles connues par des photographies ?", ["Parce qu'elles sont trop petites", "Parce qu'elles sont éphémères ou situées dans des lieux éloignés", "Parce qu'elles sont interdites", "Parce qu'elles sont toutes détruites volontairement"], "Parce qu'elles sont éphémères ou situées dans des lieux éloignés", "La photographie devient alors un témoignage de l'œuvre."),
]),
notion('A-3', 2, F, 'art-musees', [
  Q("Quel est le musée le plus visité au monde, situé à Paris ?", ["Le musée d'Orsay", "Le Louvre", "Le Centre Pompidou", "Le musée Rodin"], "Le Louvre", "Il accueille près de 9 millions de visiteurs par an."),
  Q("Quel musée parisien, installé dans une ancienne gare, présente l'art du XIXe siècle (dont l'impressionnisme) ?", ["Le musée d'Orsay", "Le Louvre", "Le Centre Pompidou", "Le musée Guimet"], "Le musée d'Orsay", "Il a ouvert en 1986."),
  Q("Quel musée parisien est consacré à l'art moderne et contemporain ?", ["Le Centre Pompidou", "Le Louvre", "Le musée Carnavalet", "Le musée de Cluny"], "Le Centre Pompidou", "Il a ouvert en 1977 ; son architecture expose les tuyaux en façade."),
]),
notion('A-3', 2, F, 'art-patrimoine', [
  Q("Quelle grotte ornée, découverte en 1940, est surnommée « la chapelle Sixtine de la préhistoire » ?", ["La grotte de Lascaux", "La grotte de Niaux", "Le gouffre de Padirac", "La grotte de Gargas"], "La grotte de Lascaux", "Ses peintures datent d’environ 18 000 ans."),
  Q("Quelle grotte ornée d'Ardèche possède des peintures datées d'environ 36 000 ans ?", ["La grotte Chauvet", "La grotte de Lascaux", "La grotte Cosquer", "La grotte d'Altamira"], "La grotte Chauvet", "Découverte en 1994, elle est inscrite au patrimoine mondial de l'UNESCO."),
  Q("Quel organisme international inscrit des sites au patrimoine mondial ?", ["L'UNESCO", "L'OMS", "L'ONU Femmes", "Le FMI"], "L'UNESCO", "La France compte plus de 50 sites inscrits."),
]),
notion('A-1', 0, F, 'art-impressionnisme', [
  Q("Quel tableau de Claude Monet a donné son nom à l'impressionnisme ?", ["Les Nymphéas", "Impression, soleil levant", "La Cathédrale de Rouen", "Le Déjeuner sur l'herbe"], "Impression, soleil levant", "Peint en 1872, il est exposé en 1874 lors de la première exposition des impressionnistes."),
  Q("Que cherchent à saisir les peintres impressionnistes ?", ["Des scènes mythologiques", "Les effets changeants de la lumière, souvent en plein air", "Des portraits officiels", "Des formes géométriques"], "Les effets changeants de la lumière, souvent en plein air", "Les tubes de peinture facilitent le travail en extérieur."),
  Q("Lequel de ces peintres est impressionniste ?", ["Auguste Renoir", "Jacques-Louis David", "Pablo Picasso", "Salvador Dalí"], "Auguste Renoir", "Monet, Renoir, Pissarro, Sisley, Degas, Berthe Morisot font partie du groupe."),
]),
notion('A-1', 0, F, 'art-cubisme', [
  Q("Quels artistes fondent le cubisme au début du XXe siècle ?", ["Picasso et Braque", "Monet et Manet", "Dalí et Magritte", "Warhol et Lichtenstein"], "Picasso et Braque", "Le cubisme représente un objet selon plusieurs points de vue à la fois."),
  Q("Quel tableau de Picasso (1907) est considéré comme annonçant le cubisme ?", ["Guernica", "Les Demoiselles d'Avignon", "La Joconde", "Le Cri"], "Les Demoiselles d'Avignon", "Les visages s'inspirent notamment de masques africains et ibériques."),
  Q("Que montre souvent une œuvre cubiste ?", ["Un seul point de vue réaliste", "Un objet décomposé en facettes et vu sous plusieurs angles", "Uniquement des paysages", "Des taches de couleur sans forme"], "Un objet décomposé en facettes et vu sous plusieurs angles", "C'est une rupture avec la perspective traditionnelle."),
]),
notion('A-1', 0, F, 'art-surrealisme', [
  Q("Quel mouvement artistique explore le rêve et l'inconscient dans les années 1920-1930 ?", ["L'impressionnisme", "Le surréalisme", "Le classicisme", "Le réalisme"], "Le surréalisme", "André Breton publie le Manifeste du surréalisme en 1924."),
  Q("Quel peintre surréaliste a peint des montres molles dans La Persistance de la mémoire ?", ["Salvador Dalí", "René Magritte", "Joan Miró", "Max Ernst"], "Salvador Dalí", "Le tableau date de 1931."),
  Q("Quel peintre belge a écrit « Ceci n'est pas une pipe » sous l'image d'une pipe ?", ["René Magritte", "Salvador Dalí", "Paul Delvaux", "Marcel Duchamp"], "René Magritte", "La Trahison des images (1929) rappelle qu'une image n'est pas l'objet qu'elle représente."),
]),
notion('A-3', 0, F, 'art-street-art', [
  Q("Comment appelle-t-on l'art réalisé dans l'espace public (murs, rues) ?", ["L'art urbain (street art)", "L'art pariétal", "L'art roman", "L'art déco"], "L'art urbain (street art)", "Il comprend graffitis, pochoirs, collages, fresques murales."),
  Q("Quel artiste britannique anonyme est célèbre pour ses pochoirs engagés ?", ["Banksy", "Keith Haring", "Invader", "JR"], "Banksy", "Son identité reste officiellement inconnue."),
  Q("Quel artiste français colle des mosaïques inspirées des jeux vidéo des années 1970-1980 dans les villes ?", ["Invader", "Banksy", "Jean-Michel Basquiat", "Christo"], "Invader", "Ses « Space Invaders » sont présents dans des dizaines de villes."),
]),
notion('A-2', 1, F, 'art-materiaux', [
  Q("Quel matériau un sculpteur peut-il modeler ?", ["Le marbre", "L'argile (terre)", "Le granite", "L'acier"], "L'argile (terre)", "L'argile se modèle à la main avant d'être éventuellement cuite."),
  Q("Quelle technique permet de reproduire une sculpture en bronze ?", ["La taille directe", "La fonte à partir d'un moule", "Le modelage", "Le collage"], "La fonte à partir d'un moule", "Le bronze en fusion est coulé dans un moule."),
  Q("Quel artiste réalise des sculptures très allongées et filiformes, comme L'Homme qui marche ?", ["Alberto Giacometti", "Auguste Rodin", "Henry Moore", "Niki de Saint Phalle"], "Alberto Giacometti", "L'Homme qui marche I (1960) est l'une des sculptures les plus chères vendues aux enchères."),
]),
notion('A-2', 0, F, 'art-gravure', [
  Q("Qu'est-ce qu'une gravure ?", ["Une peinture à l'huile", "Une image imprimée à partir d'une matrice (bois, métal, linoléum) creusée ou incisée", "Une photographie", "Une sculpture"], "Une image imprimée à partir d'une matrice (bois, métal, linoléum) creusée ou incisée", "La gravure permet de reproduire une image en plusieurs exemplaires."),
  Q("Quelle technique de gravure est souvent pratiquée à l'école ?", ["La gravure sur linoléum (linogravure)", "La gravure sur diamant", "L'eau-forte à l'acide", "La lithographie sur pierre"], "La gravure sur linoléum (linogravure)", "Le linoléum est facile à creuser avec des gouges."),
  Q("Dans une gravure en relief, quelle partie reçoit l'encre ?", ["Les parties creusées", "Les parties restées en relief", "Toute la plaque", "Aucune"], "Les parties restées en relief", "Les creux restent blancs à l'impression ; l'image est inversée."),
]),
notion('A-3', 2, F, 'art-spectateur', [
  Q("Qu'est-ce qu'une œuvre interactive ?", ["Une œuvre qu'on ne peut que regarder", "Une œuvre qui réagit à la présence ou aux actions du spectateur", "Une œuvre en noir et blanc", "Une œuvre volée"], "Une œuvre qui réagit à la présence ou aux actions du spectateur", "Le spectateur devient acteur de l'œuvre."),
  Q("Quelle artiste française a créé les sculptures colorées des « Nanas » ?", ["Niki de Saint Phalle", "Camille Claudel", "Louise Bourgeois", "Sophie Calle"], "Niki de Saint Phalle", "Elle a aussi créé la fontaine Stravinsky à Paris avec Jean Tinguely."),
  Q("Quelle artiste a réalisé l'araignée géante Maman (1999) ?", ["Louise Bourgeois", "Frida Kahlo", "Yayoi Kusama", "Berthe Morisot"], "Louise Bourgeois", "L'œuvre mesure environ 9 mètres de haut."),
]),
notion('A-1', 0, F, 'art-renaissance', [
  Q("Qui a peint le plafond de la chapelle Sixtine au Vatican ?", ["Léonard de Vinci", "Michel-Ange", "Raphaël", "Botticelli"], "Michel-Ange", "Il l'a peint entre 1508 et 1512."),
  Q("Quel peintre florentin a peint La Naissance de Vénus ?", ["Botticelli", "Titien", "Caravage", "Vermeer"], "Botticelli", "L'œuvre date des années 1480 environ et est conservée aux Offices de Florence."),
  Q("Qu'est-ce qui caractérise l'art de la Renaissance italienne ?", ["L'abstraction", "La redécouverte de l'Antiquité, la perspective et l'étude du corps humain", "Le ready-made", "L'art numérique"], "La redécouverte de l'Antiquité, la perspective et l'étude du corps humain", "L'humanisme place l'être humain au centre."),
]),
notion('A-1', 0, F, 'art-peintres-celebres', [
  Q("Quel peintre a réalisé La Nuit étoilée (1889) ?", ["Vincent Van Gogh", "Claude Monet", "Paul Gauguin", "Edgar Degas"], "Vincent Van Gogh", "Il l'a peinte depuis sa chambre de l'asile de Saint-Rémy-de-Provence."),
  Q("Quel peintre norvégien a peint Le Cri ?", ["Edvard Munch", "Gustav Klimt", "Egon Schiele", "Paul Klee"], "Edvard Munch", "C'est une œuvre emblématique de l'expressionnisme naissant."),
  Q("Quel peintre a réalisé Guernica (1937) pour dénoncer le bombardement d'une ville espagnole ?", ["Pablo Picasso", "Salvador Dalí", "Joan Miró", "Francisco Goya"], "Pablo Picasso", "Guernica est conservé au musée Reina Sofía de Madrid."),
]),
notion('A-4', 2, F, 'mus-familles-instruments', [
  Q("À quelle famille appartient le violon ?", ["Les vents", "Les cordes", "Les percussions", "Les claviers"], "Les cordes", "Violon, alto, violoncelle et contrebasse sont des cordes frottées."),
  Q("À quelle famille appartient la trompette ?", ["Les cuivres", "Les bois", "Les cordes", "Les percussions"], "Les cuivres", "Trompette, cor, trombone et tuba sont des cuivres."),
  Q("À quelle famille appartient la flûte traversière, bien qu'elle soit en métal ?", ["Les cuivres", "Les bois", "Les percussions", "Les cordes"], "Les bois", "La famille dépend du mode de production du son, pas de la matière : la flûte n'utilise pas les lèvres en vibration comme les cuivres."),
]),
notion('A-4', 2, F, 'mus-percussions', [
  Q("Lequel de ces instruments est une percussion ?", ["La harpe", "Les timbales", "Le hautbois", "Le cor"], "Les timbales", "Les percussions se frappent, se secouent ou se grattent."),
  Q("Le xylophone est un instrument…", ["à cordes", "à percussion qui peut jouer des mélodies", "à vent", "électronique uniquement"], "à percussion qui peut jouer des mélodies", "Ses lames de bois produisent des notes de hauteurs différentes."),
  Q("À quelle famille appartient le piano selon son mode de production du son ?", ["Cordes frappées", "Vents", "Cuivres", "Cordes pincées"], "Cordes frappées", "Des marteaux frappent les cordes ; le clavecin, lui, pince les cordes."),
]),
notion('A-4', 2, F, 'mus-orchestre', [
  Q("Comment appelle-t-on la personne qui dirige un orchestre ?", ["Le soliste", "Le chef d'orchestre", "Le compositeur", "Le luthier"], "Le chef d'orchestre", "Il donne le tempo, les départs et les nuances."),
  Q("Quel ensemble réunit cordes, bois, cuivres et percussions ?", ["Un quatuor à cordes", "Un orchestre symphonique", "Une fanfare", "Un trio jazz"], "Un orchestre symphonique", "Il peut compter près d'une centaine de musiciens."),
  Q("Combien de musiciens compte un quatuor à cordes ?", ["Deux", "Quatre", "Six", "Huit"], "Quatre", "Deux violons, un alto et un violoncelle."),
]),
notion('A-4', 2, F, 'mus-voix', [
  Q("Quelle est la voix de femme la plus aiguë ?", ["L'alto", "La soprano", "Le ténor", "La basse"], "La soprano", "Voix de femmes : soprano, mezzo-soprano, alto (contralto)."),
  Q("Quelle est la voix d'homme la plus grave ?", ["Le ténor", "La basse", "Le baryton", "La soprano"], "La basse", "Voix d'hommes : ténor, baryton, basse."),
  Q("Comment appelle-t-on un ensemble de chanteurs ?", ["Un orchestre", "Un chœur (chorale)", "Une fanfare", "Un quatuor à cordes"], "Un chœur (chorale)", "Un chœur peut chanter à l'unisson ou à plusieurs voix."),
]),
notion('A-4', 0, F, 'mus-parametres-son', [
  Q("Qu'est-ce que le tempo ?", ["La hauteur d'un son", "La vitesse d'exécution d'un morceau", "Le volume", "Le timbre"], "La vitesse d'exécution d'un morceau", "Lento est lent, allegro est rapide."),
  Q("Qu'est-ce que le timbre d'un son ?", ["Son volume", "Sa « couleur », qui permet de reconnaître l'instrument ou la voix", "Sa durée", "Sa hauteur"], "Sa « couleur », qui permet de reconnaître l'instrument ou la voix", "Un même la joué au violon ou à la flûte n'a pas le même timbre."),
  Q("Que désignent les nuances en musique ?", ["Les variations de volume (intensité)", "Les variations de vitesse", "Les instruments", "Les notes"], "Les variations de volume (intensité)", "Piano (p) signifie doux, forte (f) signifie fort."),
]),
notion('A-4', 0, F, 'mus-nuances-tempo', [
  Q("Que signifie l'indication « crescendo » ?", ["En ralentissant", "En augmentant progressivement le volume", "En diminuant le volume", "En accélérant"], "En augmentant progressivement le volume", "Decrescendo (ou diminuendo) signifie en diminuant."),
  Q("Que signifie « pianissimo » (pp) ?", ["Très fort", "Très doux", "Très vite", "Très lent"], "Très doux", "Fortissimo (ff) signifie très fort."),
  Q("Que signifie l'indication de tempo « allegro » ?", ["Lent", "Rapide et joyeux", "Très lent", "Modéré"], "Rapide et joyeux", "Adagio et lento sont des tempos lents ; andante est modéré."),
]),
notion('A-4', 1, F, 'mus-compositeurs-classiques', [
  Q("Quel compositeur a écrit La Flûte enchantée ?", ["Mozart", "Bach", "Beethoven", "Debussy"], "Mozart", "Mozart (1756-1791) a composé plus de 600 œuvres."),
  Q("Quel compositeur, devenu sourd, a écrit la Neuvième Symphonie et son « Hymne à la joie » ?", ["Beethoven", "Mozart", "Vivaldi", "Chopin"], "Beethoven", "L'« Hymne à la joie » est l'hymne de l'Union européenne."),
  Q("Quel compositeur italien a écrit Les Quatre Saisons ?", ["Vivaldi", "Verdi", "Rossini", "Puccini"], "Vivaldi", "Ce sont quatre concertos pour violon composés au début du XVIIIe siècle."),
]),
notion('A-4', 1, F, 'mus-oeuvres-jeunesse', [
  Q("Quel compositeur a écrit Pierre et le Loup (1936), où chaque personnage est associé à un instrument ?", ["Prokofiev", "Saint-Saëns", "Ravel", "Tchaïkovski"], "Prokofiev", "Le loup est joué par les cors, l'oiseau par la flûte, le canard par le hautbois."),
  Q("Quel compositeur français a écrit Le Carnaval des animaux ?", ["Camille Saint-Saëns", "Claude Debussy", "Maurice Ravel", "Georges Bizet"], "Camille Saint-Saëns", "Le Cygne est l'une de ses pièces les plus connues."),
  Q("Dans Pierre et le Loup, quel instrument représente le grand-père ?", ["Le basson", "La flûte", "Le violon", "La clarinette"], "Le basson", "La clarinette représente le chat ; les cordes, Pierre."),
]),
notion('A-4', 1, F, 'mus-styles', [
  Q("Dans quel pays le jazz naît-il au début du XXe siècle ?", ["La France", "Les États-Unis", "Le Brésil", "Le Royaume-Uni"], "Les États-Unis", "Il naît à La Nouvelle-Orléans, dans les communautés afro-américaines."),
  Q("Qu'est-ce qui caractérise le jazz ?", ["L'absence de rythme", "L'improvisation et le swing", "L'utilisation exclusive de violons", "Le chant grégorien"], "L'improvisation et le swing", "Louis Armstrong, Duke Ellington, Miles Davis en sont des figures majeures."),
  Q("Quel style musical né en Jamaïque est popularisé par Bob Marley ?", ["Le reggae", "Le rap", "Le blues", "Le tango"], "Le reggae", "Le reggae se développe à la fin des années 1960."),
]),
notion('A-5', 0, F, 'mus-notes', [
  N("Combien de notes différentes compte la gamme de do majeur (sans répéter le do aigu) ?", 7, "Do, ré, mi, fa, sol, la, si."),
  Q("Sur quoi écrit-on les notes de musique ?", ["Sur une portée de cinq lignes", "Sur une ligne unique", "Sur une grille de mots croisés", "Sur un cercle"], "Sur une portée de cinq lignes", "La position sur la portée indique la hauteur de la note."),
  Q("Quel symbole placé au début d'une portée permet de lire le nom des notes ?", ["Une clé (clé de sol, clé de fa…)", "Un dièse", "Une barre de mesure", "Un point d'orgue"], "Une clé (clé de sol, clé de fa…)", "La clé de sol est la plus courante pour les voix aiguës et la flûte."),
]),
notion('A-5', 0, F, 'mus-durees', [
  Q("Laquelle de ces figures de note dure le plus longtemps ?", ["La croche", "La ronde", "La noire", "La blanche"], "La ronde", "Ronde = 2 blanches = 4 noires = 8 croches."),
  N("Combien de noires valent une blanche ?", 2, "Une blanche vaut deux noires."),
  N("Combien de croches valent une noire ?", 2, "Une noire vaut deux croches."),
]),
notion('A-5', 0, F, 'mus-rythme-pulsation', [
  Q("Qu'est-ce que la pulsation en musique ?", ["Le battement régulier qui sert de repère au rythme", "Une note aiguë", "Un instrument", "Le titre d'un morceau"], "Le battement régulier qui sert de repère au rythme", "C'est ce qu'on frappe naturellement du pied en écoutant."),
  Q("Qu'est-ce qu'un ostinato ?", ["Une note tenue", "Un motif rythmique ou mélodique répété obstinément", "Un silence", "Un chef d'orchestre"], "Un motif rythmique ou mélodique répété obstinément", "Le Boléro de Ravel repose sur un ostinato de caisse claire."),
  Q("Qu'est-ce qu'un silence en musique ?", ["Une pause sans son, de durée mesurée", "Une fin de morceau", "Une erreur", "Un instrument"], "Une pause sans son, de durée mesurée", "Pause, demi-pause, soupir et demi-soupir sont des silences."),
]),
notion('A-5', 1, F, 'mus-chant-choral', [
  Q("Que signifie chanter « à l'unisson » ?", ["Chanter seul", "Chanter tous la même mélodie en même temps", "Chanter à plusieurs voix différentes", "Chanter sans musique"], "Chanter tous la même mélodie en même temps", "Chanter à plusieurs voix, c'est la polyphonie."),
  Q("Qu'est-ce qu'un canon ?", ["Une arme", "Une même mélodie chantée par plusieurs groupes qui commencent les uns après les autres", "Un chant sans paroles", "Une chanson très courte"], "Une même mélodie chantée par plusieurs groupes qui commencent les uns après les autres", "« Frère Jacques » se chante souvent en canon."),
  Q("Pourquoi s'échauffer la voix avant de chanter ?", ["Ce n'est pas utile", "Pour préparer le souffle, le corps et les cordes vocales et éviter de les abîmer", "Pour chanter plus faux", "Pour aller plus vite"], "Pour préparer le souffle, le corps et les cordes vocales et éviter de les abîmer", "Posture, respiration et articulation sont travaillées."),
]),
notion('A-4', 1, F, 'mus-hymne', [
  Q("Qui a composé La Marseillaise en 1792 ?", ["Rouget de Lisle", "Berlioz", "Mozart", "Lully"], "Rouget de Lisle", "Elle devient l'hymne national français en 1795, puis définitivement en 1879."),
  Q("Pour quelle armée La Marseillaise est-elle d'abord écrite ?", ["L'armée du Rhin", "L'armée d'Italie", "L'armée de Napoléon en Égypte", "La garde royale"], "L'armée du Rhin", "Elle s'appelait le « Chant de guerre pour l'armée du Rhin » ; les fédérés marseillais la popularisent."),
  Q("Quelle œuvre sert d'hymne à l'Union européenne ?", ["L'« Hymne à la joie » de Beethoven", "La Marseillaise", "Les Quatre Saisons", "Le Boléro"], "L'« Hymne à la joie » de Beethoven", "Il est issu du dernier mouvement de la Neuvième Symphonie."),
]),
notion('A-4', 0, F, 'mus-forme', [
  Q("Comment appelle-t-on la partie qui revient plusieurs fois dans une chanson ?", ["Le couplet", "Le refrain", "L'introduction", "La coda"], "Le refrain", "Les couplets changent de paroles, le refrain revient à l'identique."),
  Q("Qu'est-ce qu'une forme ABA en musique ?", ["Trois parties différentes", "Une partie A, une partie contrastante B, puis le retour de A", "Un morceau sans structure", "Une seule partie répétée"], "Une partie A, une partie contrastante B, puis le retour de A", "C'est une forme ternaire très courante."),
  Q("Qu'est-ce qu'une coda ?", ["Le début d'un morceau", "La partie qui conclut un morceau", "Un instrument", "Une nuance"], "La partie qui conclut un morceau", "Coda signifie « queue » en italien."),
]),
notion('A-4', 1, F, 'mus-musiques-monde', [
  Q("De quel pays vient le flamenco ?", ["L'Espagne (Andalousie)", "L'Argentine", "Le Portugal", "Cuba"], "L'Espagne (Andalousie)", "Chant, guitare et danse en sont les composantes."),
  Q("De quel pays vient la samba ?", ["Le Brésil", "Le Mexique", "Le Pérou", "L'Espagne"], "Le Brésil", "Elle est au cœur du carnaval de Rio."),
  Q("Quel instrument est emblématique de la musique d'Afrique de l'Ouest, avec sa calebasse et ses 21 cordes ?", ["La kora", "Le sitar", "Le banjo", "Le koto"], "La kora", "Le sitar est indien et le koto japonais."),
]),
notion('A-5', 1, F, 'mus-instruments-ecole', [
  Q("Quel instrument à vent est souvent utilisé à l'école ?", ["La flûte à bec", "Le basson", "Le tuba", "Le cor anglais"], "La flûte à bec", "C'est un instrument de la famille des bois."),
  Q("Qu'est-ce qu'une percussion corporelle ?", ["Un instrument en bois", "Un son produit avec son propre corps (claquements de mains, frappes sur les cuisses)", "Un tambour", "Un mouvement de danse sans son"], "Un son produit avec son propre corps (claquements de mains, frappes sur les cuisses)", "Les percussions corporelles permettent de travailler le rythme sans matériel."),
  Q("À quoi sert un métronome ?", ["À accorder un instrument", "À donner un tempo régulier", "À mesurer le volume", "À enregistrer"], "À donner un tempo régulier", "Le tempo s'indique en battements par minute (BPM)."),
]),
notion('A-1', 2, F, 'art-images-numeriques', [
  Q("Qu'est-ce qu'un photomontage ?", ["Une photo prise en montagne", "Une image composée en assemblant plusieurs photographies", "Une photo en noir et blanc", "Un appareil photo"], "Une image composée en assemblant plusieurs photographies", "Le numérique facilite ces montages, d'où la nécessité de vérifier les images."),
  Q("Pourquoi faut-il rester critique face aux images diffusées sur Internet ?", ["Elles sont toujours vraies", "Elles peuvent être retouchées, détournées ou sorties de leur contexte", "Elles sont toujours floues", "Elles sont interdites"], "Elles peuvent être retouchées, détournées ou sorties de leur contexte", "La recherche d'image inversée aide à retrouver l'origine d'une photo."),
  Q("Qu'est-ce que le droit à l'image ?", ["Le droit de photographier n'importe qui", "Le droit de chaque personne de s'opposer à la diffusion de son image sans son accord", "Le droit de copier une œuvre", "Un droit réservé aux artistes"], "Le droit de chaque personne de s'opposer à la diffusion de son image sans son accord", "À l'école, une autorisation des responsables légaux est demandée pour diffuser des photos d'élèves."),
]),
notion('A-3', 2, F, 'art-exposition', [
  Q("Comment appelle-t-on la personne qui conçoit et organise une exposition ?", ["Le commissaire d'exposition", "Le gardien", "Le restaurateur", "Le collectionneur"], "Le commissaire d'exposition", "Il choisit les œuvres et leur accrochage."),
  Q("Qu'est-ce qu'un cartel dans un musée ?", ["Un plan du musée", "La petite étiquette qui indique l'artiste, le titre, la date et la technique d'une œuvre", "Un billet d'entrée", "Une vitrine"], "La petite étiquette qui indique l'artiste, le titre, la date et la technique d'une œuvre", "Lire le cartel aide à situer l'œuvre."),
  Q("Pourquoi interdit-on souvent le flash devant les œuvres anciennes ?", ["Pour vendre des cartes postales", "Parce que la lumière intense peut abîmer certains pigments fragiles", "Pour éviter le bruit", "Par habitude"], "Parce que la lumière intense peut abîmer certains pigments fragiles", "La conservation préventive limite l'exposition à la lumière."),
]),
]

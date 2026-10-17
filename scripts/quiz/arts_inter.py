from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('A-1', 0, I, 'art-ressemblance-vraisemblance', [
  Q("Quelle est la différence entre ressemblance et vraisemblance ?", ["Aucune", "La ressemblance imite le réel ; la vraisemblance rend crédible une image, même inventée", "La vraisemblance concerne seulement la sculpture", "La ressemblance concerne seulement la photographie"], "La ressemblance imite le réel ; la vraisemblance rend crédible une image, même inventée", "Une scène mythologique peut être vraisemblable sans ressembler à rien de réel."),
  Q("Qu'est-ce qu'un trompe-l'œil ?", ["Une peinture abstraite", "Une représentation si réaliste qu'elle donne l'illusion de la réalité", "Une sculpture cassée", "Un dessin d'enfant"], "Une représentation si réaliste qu'elle donne l'illusion de la réalité", "On en trouve sur des façades d'immeubles ou des plafonds."),
  Q("Quel mouvement des années 1960-1970 reproduit la réalité avec une précision photographique ?", ["L'hyperréalisme", "Le fauvisme", "Le cubisme", "Le dadaïsme"], "L'hyperréalisme", "Il prend souvent pour modèle des photographies."),
]),
notion('A-1', 0, I, 'art-ecart-expressif', [
  Q("Quel mouvement, autour de Matisse vers 1905, utilise des couleurs pures et arbitraires ?", ["Le fauvisme", "L'impressionnisme", "Le réalisme", "Le classicisme"], "Le fauvisme", "Un critique les compare à des « fauves » au Salon d'automne de 1905."),
  Q("Que cherche à exprimer l'expressionnisme ?", ["Une copie fidèle du réel", "Les émotions de l'artiste, quitte à déformer la réalité", "Uniquement la lumière", "Des formes géométriques pures"], "Les émotions de l'artiste, quitte à déformer la réalité", "Munch, Kirchner, Schiele sont des figures de l'expressionnisme."),
  Q("Pourquoi un artiste peut-il volontairement s'écarter de la ressemblance ?", ["Par maladresse uniquement", "Pour exprimer une émotion, une idée ou un point de vue", "Parce que c'est interdit de copier", "Pour aller plus vite"], "Pour exprimer une émotion, une idée ou un point de vue", "C'est la « valeur expressive de l'écart » du programme d'arts plastiques."),
]),
notion('A-1', 1, I, 'art-perspective-types', [
  Q("Quelle perspective représente les lointains plus flous et bleutés ?", ["La perspective linéaire", "La perspective atmosphérique", "La perspective cavalière", "La perspective inversée"], "La perspective atmosphérique", "Léonard de Vinci l'utilise avec le sfumato."),
  Q("Quelle perspective, sans point de fuite, est souvent utilisée en dessin technique et en mathématiques ?", ["La perspective cavalière", "La perspective atmosphérique", "La perspective à deux points de fuite", "La perspective aérienne"], "La perspective cavalière", "Les arêtes fuyantes y restent parallèles."),
  Q("Dans l'art médiéval, comment indique-t-on souvent l'importance d'un personnage ?", ["Par la perspective linéaire", "Par sa taille (perspective hiérarchique)", "Par l'ombre", "Par la couleur noire"], "Par sa taille (perspective hiérarchique)", "Le personnage le plus important est représenté le plus grand."),
]),
notion('A-1', 1, I, 'art-point-de-vue', [
  Q("Quel effet produit une vue en plongée sur un personnage ?", ["Il paraît plus grand et puissant", "Il paraît plus petit, écrasé ou vulnérable", "Il disparaît", "Aucun effet"], "Il paraît plus petit, écrasé ou vulnérable", "La contre-plongée produit l'effet inverse."),
  Q("Qu'est-ce qu'une anamorphose ?", ["Une sculpture en bronze", "Une image déformée qui ne se lit correctement que d'un point de vue précis", "Un collage", "Une gravure"], "Une image déformée qui ne se lit correctement que d'un point de vue précis", "Le crâne des Ambassadeurs de Holbein (1533) en est un exemple célèbre."),
  Q("Quel artiste contemporain crée des anamorphoses géométriques dans l'espace ?", ["Felice Varini", "Claude Monet", "Jean Dubuffet", "Pierre Soulages"], "Felice Varini", "Artiste suisse vivant à Paris, il peint des formes qui ne se reconstituent que d'un point de vue."),
]),
notion('A-1', 2, I, 'art-plans-cinema', [
  Q("Quel plan cadre un personnage de la tête à la taille ?", ["Le plan d'ensemble", "Le plan américain", "Le plan rapproché (taille)", "Le très gros plan"], "Le plan rapproché (taille)", "Le plan américain coupe à mi-cuisses ; le gros plan montre le visage."),
  Q("Qu'est-ce qu'un travelling ?", ["Un plan fixe", "Un déplacement de la caméra pendant la prise de vue", "Un montage rapide", "Un effet sonore"], "Un déplacement de la caméra pendant la prise de vue", "Le panoramique, lui, fait pivoter la caméra sur place."),
  Q("Qu'est-ce que le montage au cinéma ?", ["Le tournage", "L'assemblage des plans dans un ordre choisi pour construire le récit", "Le décor", "La musique"], "L'assemblage des plans dans un ordre choisi pour construire le récit", "Le montage crée le rythme et le sens du film."),
]),
notion('A-1', 2, I, 'art-cinema-animation', [
  Q("Sur quel principe repose le cinéma d'animation ?", ["L'enregistrement en continu", "La succession rapide d'images fixes qui donne l'illusion du mouvement", "La projection d'une seule image", "La photographie en couleur"], "La succession rapide d'images fixes qui donne l'illusion du mouvement", "C'est la persistance rétinienne et l'effet phi."),
  N("Combien d'images par seconde utilise traditionnellement le cinéma ?", 24, "24 images par seconde est la norme depuis le cinéma parlant."),
  Q("Qu'est-ce que le stop motion (animation image par image) ?", ["Un film en accéléré", "Une technique où l'on photographie des objets déplacés légèrement entre chaque prise", "Un dessin animé numérique", "Un film muet"], "Une technique où l'on photographie des objets déplacés légèrement entre chaque prise", "Wallace et Gromit ou Ma vie de Courgette utilisent cette technique."),
]),
notion('A-1', 2, I, 'art-reproductibilite', [
  Q("Quel changement majeur la photographie et l'imprimerie apportent-elles à la diffusion des images ?", ["Elles rendent les images uniques", "Elles permettent la reproduction en grand nombre des images", "Elles interdisent la peinture", "Elles suppriment les musées"], "Elles permettent la reproduction en grand nombre des images", "Walter Benjamin analyse « l'œuvre d'art à l'époque de sa reproductibilité technique » (1935)."),
  Q("Quel artiste du pop art imite les trames et les bulles de la bande dessinée dans ses tableaux ?", ["Roy Lichtenstein", "Mark Rothko", "Jackson Pollock", "Francis Bacon"], "Roy Lichtenstein", "Il reproduit en peinture les points Benday de l'impression."),
  Q("Que critique ou célèbre le pop art ?", ["La nature sauvage", "La société de consommation et la culture de masse", "L'art religieux", "La préhistoire"], "La société de consommation et la culture de masse", "Boîtes de soupe Campbell, stars, publicités deviennent des sujets."),
]),
notion('A-2', 0, I, 'art-outils-gestes', [
  Q("Quel outil le peintre utilise-t-il pour appliquer une peinture épaisse en pâte ?", ["Le couteau à peindre", "La plume", "Le fusain", "La gouge"], "Le couteau à peindre", "Il permet des empâtements visibles."),
  Q("Qu'est-ce que le fusain ?", ["Une peinture", "Un bâton de charbon de bois utilisé pour dessiner", "Un pinceau", "Une encre"], "Un bâton de charbon de bois utilisé pour dessiner", "Il permet des noirs profonds et des estompages."),
  Q("Quel peintre français contemporain a consacré son œuvre au noir et à la lumière qu'il reflète (« outrenoir ») ?", ["Pierre Soulages", "Yves Klein", "Henri Matisse", "Jean Dubuffet"], "Pierre Soulages", "Le musée Soulages se trouve à Rodez."),
]),
notion('A-2', 1, I, 'art-materiaux-sens', [
  Q("Quel artiste a revendiqué un « art brut », produit hors des circuits artistiques officiels ?", ["Jean Dubuffet", "Claude Monet", "Ingres", "Delacroix"], "Jean Dubuffet", "Il collectionne des œuvres de personnes internées ou autodidactes."),
  Q("Quel mouvement italien des années 1960 utilise des matériaux « pauvres » (terre, chiffons, bois) ?", ["L'arte povera", "Le futurisme", "Le baroque", "Le maniérisme"], "L'arte povera", "Le choix de matériaux humbles porte un sens critique."),
  Q("Pourquoi un artiste choisit-il un matériau particulier ?", ["Uniquement pour son prix", "Parce que ses qualités physiques (texture, couleur, fragilité) participent au sens de l'œuvre", "Au hasard", "Parce que c'est imposé"], "Parce que ses qualités physiques (texture, couleur, fragilité) participent au sens de l'œuvre", "Le matériau n'est pas neutre : il signifie."),
]),
notion('A-2', 2, I, 'art-couleur-theorie', [
  Q("Quel peintre français pratique le pointillisme, avec Un dimanche après-midi à l'île de la Grande Jatte ?", ["Georges Seurat", "Paul Cézanne", "Édouard Manet", "Eugène Delacroix"], "Georges Seurat", "Le mélange optique se fait dans l'œil du spectateur."),
  Q("Quel chimiste a formulé au XIXe siècle la loi du contraste simultané des couleurs ?", ["Michel-Eugène Chevreul", "Antoine Lavoisier", "Louis Pasteur", "Marie Curie"], "Michel-Eugène Chevreul", "Ses travaux influencent les impressionnistes et les néo-impressionnistes."),
  Q("Qu'est-ce que le monochrome ?", ["Une œuvre très colorée", "Une œuvre d'une seule couleur", "Une photographie", "Une sculpture"], "Une œuvre d'une seule couleur", "Yves Klein réalise des monochromes bleus (IKB)."),
]),
notion('A-2', 3, I, 'art-assemblage', [
  Q("Quel artiste compresse des voitures pour en faire des sculptures ?", ["César", "Arman", "Rodin", "Calder"], "César", "Ses « compressions » datent de la fin des années 1950."),
  Q("Quel artiste accumule des objets identiques dans des boîtes (« accumulations ») ?", ["Arman", "César", "Monet", "Seurat"], "Arman", "César et Arman font partie des Nouveaux Réalistes."),
  Q("Quel artiste américain invente le mobile, sculpture suspendue en mouvement ?", ["Alexander Calder", "Andy Warhol", "Jeff Koons", "Mark Rothko"], "Alexander Calder", "C'est Marcel Duchamp qui donne le nom de « mobile » à ces œuvres."),
]),
notion('A-3', 0, I, 'art-performance', [
  Q("Qu'est-ce qu'une performance artistique ?", ["Un concours sportif", "Une action réalisée par l'artiste devant un public, en temps réel", "Une sculpture monumentale", "Une exposition de photos"], "Une action réalisée par l'artiste devant un public, en temps réel", "Le corps de l'artiste devient le matériau de l'œuvre."),
  Q("Quelle artiste serbe est célèbre pour ses performances, comme The Artist Is Present (2010) ?", ["Marina Abramović", "Frida Kahlo", "Louise Bourgeois", "Yayoi Kusama"], "Marina Abramović", "Elle reste assise face à des visiteurs pendant plus de 700 heures au MoMA."),
  Q("Comment appelle-t-on les événements artistiques spontanés des années 1960 associant le public ?", ["Les happenings", "Les vernissages", "Les salons", "Les rétrospectives"], "Les happenings", "Allan Kaprow en est l'initiateur."),
]),
notion('A-3', 1, I, 'art-architecture', [
  Q("Quel architecte a conçu la villa Savoye et défini les « cinq points d'une architecture nouvelle » ?", ["Le Corbusier", "Gustave Eiffel", "Jean Nouvel", "Haussmann"], "Le Corbusier", "Pilotis, toit-terrasse, plan libre, fenêtre en bandeau, façade libre."),
  Q("Quel architecte sino-américain a conçu la pyramide du Louvre ?", ["Ieoh Ming Pei", "Renzo Piano", "Frank Gehry", "Zaha Hadid"], "Ieoh Ming Pei", "Elle est inaugurée en 1989."),
  Q("Quels architectes ont conçu le Centre Pompidou ?", ["Renzo Piano et Richard Rogers", "Le Corbusier et Jeanneret", "Jean Nouvel et Philippe Starck", "Pei et Gehry"], "Renzo Piano et Richard Rogers", "Ses tuyaux colorés en façade codent les fonctions (bleu pour l'air, vert pour l'eau…)."),
]),
notion('A-3', 1, I, 'art-emballages-christo', [
  Q("Quels artistes ont emballé le Pont-Neuf en 1985 ?", ["Christo et Jeanne-Claude", "Buren et Varini", "Niki de Saint Phalle et Tinguely", "Gilbert et George"], "Christo et Jeanne-Claude", "L'emballage modifie temporairement le regard sur un monument."),
  Q("Quel monument parisien a été emballé en 2021, d'après un projet de Christo et Jeanne-Claude ?", ["La tour Eiffel", "L'Arc de triomphe", "Notre-Dame", "Le Panthéon"], "L'Arc de triomphe", "Le projet a été réalisé après la mort de Christo, en 2020."),
  Q("Pourquoi l'emballage d'un monument est-il une démarche artistique ?", ["Pour le protéger de la pluie", "Pour révéler autrement sa forme et renouveler le regard du public", "Pour le restaurer", "Pour le cacher définitivement"], "Pour révéler autrement sa forme et renouveler le regard du public", "L'œuvre est éphémère et in situ."),
]),
notion('A-3', 2, I, 'art-art-numerique', [
  Q("Qu'est-ce qu'une œuvre immersive ?", ["Une œuvre sous l'eau", "Une œuvre qui enveloppe le spectateur (projections, sons, réalité virtuelle)", "Une petite peinture", "Une sculpture en bronze"], "Une œuvre qui enveloppe le spectateur (projections, sons, réalité virtuelle)", "Le spectateur est plongé à l'intérieur de l'œuvre."),
  Q("Quel lieu parisien, installé dans une ancienne fonderie, propose des expositions numériques immersives ?", ["L'Atelier des Lumières", "Le Louvre", "Le musée Rodin", "Le Grand Palais uniquement"], "L'Atelier des Lumières", "Il a ouvert en 2018 dans le 11e arrondissement."),
  Q("Quelle artiste japonaise crée des « Infinity Rooms » couvertes de miroirs et de points ?", ["Yayoi Kusama", "Marina Abramović", "Sophie Calle", "Annette Messager"], "Yayoi Kusama", "Les pois sont devenus sa signature."),
]),
notion('A-1', 0, I, 'art-romantisme-realisme', [
  Q("Quel peintre romantique a peint La Liberté guidant le peuple (1830) ?", ["Eugène Delacroix", "Gustave Courbet", "Jacques-Louis David", "Théodore Géricault"], "Eugène Delacroix", "Elle célèbre les Trois Glorieuses de juillet 1830."),
  Q("Quel peintre a réalisé Le Radeau de la Méduse (1819) ?", ["Théodore Géricault", "Eugène Delacroix", "Ingres", "Courbet"], "Théodore Géricault", "Il s'inspire d'un naufrage réel de 1816."),
  Q("Quel peintre est le chef de file du réalisme, avec Un enterrement à Ornans ?", ["Gustave Courbet", "Claude Monet", "Édouard Manet", "Paul Cézanne"], "Gustave Courbet", "Il représente des gens ordinaires sur une toile de très grand format."),
]),
notion('A-1', 0, I, 'art-classicisme-baroque', [
  Q("Quel peintre italien est célèbre pour ses contrastes violents d'ombre et de lumière (clair-obscur) ?", ["Le Caravage", "Botticelli", "Fra Angelico", "Giotto"], "Le Caravage", "On parle de « ténébrisme » pour ses fonds très sombres."),
  Q("Quel peintre hollandais du XVIIe siècle a peint La Jeune Fille à la perle ?", ["Johannes Vermeer", "Rembrandt", "Rubens", "Van Eyck"], "Johannes Vermeer", "Vermeer est célèbre pour sa lumière douce venant d'une fenêtre."),
  Q("Quel peintre néoclassique a peint Le Serment des Horaces et Le Sacre de Napoléon ?", ["Jacques-Louis David", "Eugène Delacroix", "Claude Monet", "Nicolas Poussin"], "Jacques-Louis David", "Le néoclassicisme s'inspire de l'Antiquité."),
]),
notion('A-4', 0, I, 'mus-vocabulaire-analyse', [
  Q("Qu'est-ce que la texture musicale ?", ["Le volume", "La manière dont les voix ou instruments se superposent (monodie, polyphonie…)", "La vitesse", "Le titre"], "La manière dont les voix ou instruments se superposent (monodie, polyphonie…)", "Une monodie est une seule ligne mélodique ; la polyphonie en superpose plusieurs."),
  Q("Qu'est-ce que l'harmonie en musique ?", ["Une seule note", "La combinaison de sons joués simultanément (accords)", "Le rythme", "Le silence"], "La combinaison de sons joués simultanément (accords)", "La mélodie est horizontale ; l'harmonie, verticale."),
  Q("Qu'est-ce qu'une mélodie ?", ["Une suite de sons de hauteurs différentes formant une phrase musicale", "Un battement régulier", "Un accord", "Un instrument"], "Une suite de sons de hauteurs différentes formant une phrase musicale", "C'est l'« air » que l'on fredonne."),
]),
notion('A-4', 0, I, 'mus-formes-classiques', [
  Q("Qu'est-ce qu'un concerto ?", ["Une œuvre pour chœur seul", "Une œuvre pour soliste et orchestre", "Une chanson populaire", "Une œuvre pour piano seul"], "Une œuvre pour soliste et orchestre", "Le soliste dialogue avec l'orchestre."),
  Q("Qu'est-ce qu'une symphonie ?", ["Une œuvre pour orchestre, généralement en plusieurs mouvements", "Une pièce pour voix seule", "Un opéra", "Une danse"], "Une œuvre pour orchestre, généralement en plusieurs mouvements", "Haydn, considéré comme le « père de la symphonie », en a composé plus de cent."),
  Q("Qu'est-ce qu'un opéra ?", ["Une symphonie sans voix", "Une œuvre théâtrale entièrement ou majoritairement chantée, avec orchestre", "Un morceau de jazz", "Une chanson"], "Une œuvre théâtrale entièrement ou majoritairement chantée, avec orchestre", "Carmen de Bizet (1875) est l'un des opéras les plus joués au monde."),
]),
notion('A-4', 1, I, 'mus-periodes', [
  Q("À quelle période appartient Jean-Sébastien Bach ?", ["Le Moyen Âge", "La période baroque", "Le romantisme", "Le XXe siècle"], "La période baroque", "Période baroque : environ 1600-1750."),
  Q("À quelle période appartiennent Chopin et Liszt ?", ["La période baroque", "Le romantisme", "La Renaissance", "Le classicisme"], "Le romantisme", "Le romantisme musical couvre principalement le XIXe siècle."),
  Q("Quel compositeur est un représentant majeur du classicisme viennois ?", ["Haydn", "Debussy", "Bach", "Stravinsky"], "Haydn", "Haydn, Mozart et le jeune Beethoven incarnent le classicisme viennois."),
]),
notion('A-4', 1, I, 'mus-xxe', [
  Q("Quel compositeur français est associé à l'impressionnisme musical, avec Prélude à l'après-midi d'un faune ?", ["Claude Debussy", "Hector Berlioz", "Georges Bizet", "Jean-Baptiste Lully"], "Claude Debussy", "L'œuvre date de 1894."),
  Q("Quel ballet de Stravinsky provoque un scandale lors de sa création à Paris en 1913 ?", ["Le Sacre du printemps", "Le Lac des cygnes", "Casse-Noisette", "Giselle"], "Le Sacre du printemps", "Ses rythmes et ses dissonances bousculent le public."),
  Q("Quelle œuvre de Ravel (1928) répète une même mélodie avec un crescendo continu ?", ["Le Boléro", "La Mer", "Carmen", "Les Planètes"], "Le Boléro", "Ravel lui-même le décrivait comme une expérience d'orchestration."),
]),
notion('A-4', 1, I, 'mus-musiques-actuelles', [
  Q("Dans quel quartier de New York le hip-hop naît-il dans les années 1970 ?", ["Le Bronx", "Manhattan", "Brooklyn Heights", "Queens"], "Le Bronx", "Le hip-hop réunit rap, DJing, breakdance et graffiti."),
  Q("Quel style musical, né chez les Afro-Américains du sud des États-Unis, est à l'origine du rock et du jazz ?", ["Le blues", "La valse", "Le tango", "Le menuet"], "Le blues", "Le blues utilise souvent une grille de douze mesures."),
  Q("Qu'est-ce que la musique électro ?", ["Une musique jouée uniquement au violon", "Une musique produite principalement avec des instruments et outils électroniques", "Une musique médiévale", "Une musique sans rythme"], "Une musique produite principalement avec des instruments et outils électroniques", "La « French touch » (Daft Punk, Air) a marqué les années 1990."),
]),
notion('A-4', 2, I, 'mus-formations', [
  Q("Quel ensemble est composé uniquement de vents et de percussions et défile souvent en plein air ?", ["La fanfare (ou harmonie)", "Le quatuor à cordes", "L'orchestre de chambre", "Le trio avec piano"], "La fanfare (ou harmonie)", "La fanfare comprend surtout des cuivres."),
  Q("Qu'est-ce qu'un big band ?", ["Un orchestre symphonique", "Un grand orchestre de jazz avec sections de cuivres, saxophones et rythmique", "Un groupe de rock de trois musiciens", "Un chœur d'enfants"], "Un grand orchestre de jazz avec sections de cuivres, saxophones et rythmique", "Duke Ellington et Count Basie dirigent de célèbres big bands."),
  Q("Qu'est-ce qu'une chorale a cappella ?", ["Une chorale accompagnée d'un orchestre", "Une chorale qui chante sans accompagnement instrumental", "Une chorale d'église uniquement", "Une chorale qui chante faux"], "Une chorale qui chante sans accompagnement instrumental", "A cappella signifie « comme à la chapelle »."),
]),
notion('A-5', 0, I, 'mus-mesures', [
  Q("Que signifie une mesure à 3/4 ?", ["Trois noires par mesure", "Quatre noires par mesure", "Trois croches par mesure", "Trois blanches par mesure"], "Trois noires par mesure", "C'est la mesure de la valse."),
  N("Dans une mesure à 4/4, combien de croches peut-on placer ?", 8, "4 noires × 2 croches = 8 croches."),
  Q("Quelle danse est associée à une mesure à trois temps ?", ["La valse", "La marche", "Le rock", "Le tango"], "La valse", "La marche est à deux temps."),
]),
notion('A-5', 0, I, 'mus-alterations', [
  Q("Que fait un dièse (♯) placé devant une note ?", ["Il baisse la note d'un demi-ton", "Il hausse la note d'un demi-ton", "Il double sa durée", "Il la rend muette"], "Il hausse la note d'un demi-ton", "Le bémol (♭) la baisse d'un demi-ton ; le bécarre annule l'altération."),
  N("Combien de demi-tons compte une octave ?", 12, "Une octave compte 12 demi-tons, comme les 12 touches (blanches et noires) d'une octave du piano."),
  Q("Qu'est-ce qu'une octave ?", ["Un intervalle de huit notes, d'un do au do suivant", "Un instrument", "Un tempo", "Un silence"], "Un intervalle de huit notes, d'un do au do suivant", "Deux notes à l'octave portent le même nom."),
]),
notion('A-5', 1, I, 'mus-interpretation', [
  Q("Qu'est-ce qu'une partition ?", ["Un instrument", "Le support écrit d'une œuvre musicale", "Un enregistrement", "Une salle de concert"], "Le support écrit d'une œuvre musicale", "Elle indique notes, rythmes, nuances, tempo."),
  Q("Que signifie le point d'orgue (𝄐) au-dessus d'une note ?", ["Jouer la note plus courte", "Prolonger la note à volonté", "Jouer plus fort", "Supprimer la note"], "Prolonger la note à volonté", "La durée est laissée à l'appréciation du chef ou de l'interprète."),
  Q("Pourquoi suit-on les gestes du chef de chœur en interprétation collective ?", ["Par politesse uniquement", "Pour démarrer ensemble, respecter le tempo, les nuances et terminer ensemble", "Pour éviter de chanter", "Ce n'est pas utile"], "Pour démarrer ensemble, respecter le tempo, les nuances et terminer ensemble", "Le chef coordonne l'ensemble des interprètes."),
]),
notion('A-5', 0, I, 'mus-creation', [
  Q("Qu'est-ce que l'improvisation en musique ?", ["Jouer une partition à la lettre", "Créer de la musique spontanément en la jouant", "Écouter un enregistrement", "Accorder un instrument"], "Créer de la musique spontanément en la jouant", "Elle est centrale dans le jazz et dans de nombreuses musiques du monde."),
  Q("Qu'est-ce qu'un paysage sonore ?", ["Une peinture de paysage", "Une création composée de sons enregistrés ou imités d'un environnement", "Un concert en plein air", "Une chanson sur la nature"], "Une création composée de sons enregistrés ou imités d'un environnement", "C'est une activité fréquente à l'école primaire et au collège."),
  Q("Quel compositeur français est un pionnier de la musique concrète, faite de sons enregistrés ?", ["Pierre Schaeffer", "Claude Debussy", "Gabriel Fauré", "Maurice Ravel"], "Pierre Schaeffer", "Il crée la musique concrète en 1948."),
]),
notion('A-4', 2, I, 'mus-ecoute-reconnaitre', [
  Q("Quel instrument à anche double a un son nasillard et donne le la à l'orchestre ?", ["Le hautbois", "La flûte", "La trompette", "Le violon"], "Le hautbois", "C'est traditionnellement le hautbois qui donne le la pour accorder l'orchestre."),
  Q("Quel instrument à cordes est le plus grave de l'orchestre ?", ["La contrebasse", "L'alto", "Le violon", "Le violoncelle"], "La contrebasse", "Plus l'instrument est grand, plus il est grave en général."),
  Q("Quel instrument est à la fois un bois et à anche simple ?", ["La clarinette", "Le hautbois", "Le basson", "La flûte traversière"], "La clarinette", "Le saxophone, en métal, est aussi un bois à anche simple."),
]),
notion('A-2', 0, I, 'art-gestes-techniques', [
  Q("Qu'est-ce que le frottage, utilisé par Max Ernst ?", ["Une technique de sculpture", "Une technique qui consiste à frotter un crayon sur un papier posé sur une surface texturée", "Un type de peinture à l'huile", "Une gravure à l'acide"], "Une technique qui consiste à frotter un crayon sur un papier posé sur une surface texturée", "Elle révèle les textures du bois, des feuilles…"),
  Q("Qu'est-ce que le pochoir ?", ["Une technique où l'on applique la couleur à travers une forme découpée", "Une sculpture", "Une photographie", "Une mosaïque"], "Une technique où l'on applique la couleur à travers une forme découpée", "Très utilisé dans le street art."),
  Q("Qu'est-ce qu'une mosaïque ?", ["Une peinture à l'eau", "Une image composée de petits fragments (tesselles) assemblés", "Un collage de journaux", "Une gravure"], "Une image composée de petits fragments (tesselles) assemblés", "Les Romains et les Byzantins en ont réalisé de remarquables."),
  Q("Qu'est-ce que la technique du sgraffite (grattage) ?", ["Gratter une couche de couleur pour faire apparaître la couche inférieure", "Coller des papiers", "Mouler du plâtre", "Souffler de la peinture"], "Gratter une couche de couleur pour faire apparaître la couche inférieure", "À l'école, on recouvre souvent des pastels de couleur avec de l'encre noire, puis on gratte."),
]),
notion('A-1', 0, I, 'art-art-moyen-age', [
  Q("Qu'est-ce qu'un vitrail ?", ["Une peinture sur toile", "Une composition de morceaux de verre colorés assemblés par des plombs", "Une sculpture en bois", "Une tapisserie"], "Une composition de morceaux de verre colorés assemblés par des plombs", "Les vitraux de la cathédrale de Chartres sont célèbres."),
  Q("Quelle broderie du XIe siècle raconte la conquête de l'Angleterre par Guillaume le Conquérant ?", ["La tapisserie de Bayeux", "La Dame à la licorne", "L'Apocalypse d'Angers", "Les Très Riches Heures"], "La tapisserie de Bayeux", "C'est en réalité une broderie de près de 70 mètres de long."),
  Q("Qu'est-ce qu'une enluminure ?", ["Une sculpture de façade", "Une peinture ornant un manuscrit", "Un vitrail", "Une fresque"], "Une peinture ornant un manuscrit", "Les Très Riches Heures du duc de Berry sont un chef-d'œuvre de l'enluminure."),
]),
notion('A-3', 0, I, 'art-corps-oeuvre', [
  Q("Quelle peintre mexicaine a réalisé de nombreux autoportraits exprimant sa souffrance physique ?", ["Frida Kahlo", "Tamara de Lempicka", "Berthe Morisot", "Artemisia Gentileschi"], "Frida Kahlo", "Victime d'un grave accident, elle peint souvent depuis son lit."),
  Q("Quel peintre impressionniste représente souvent des danseuses de l'Opéra ?", ["Edgar Degas", "Claude Monet", "Alfred Sisley", "Camille Pissarro"], "Edgar Degas", "Il sculpte aussi La Petite Danseuse de quatorze ans."),
  Q("Qu'est-ce que l'action painting ?", ["Une peinture de scènes d'action", "Une peinture où le geste et le mouvement du corps de l'artiste sont essentiels", "Un dessin animé", "Une peinture réalisée par une machine"], "Une peinture où le geste et le mouvement du corps de l'artiste sont essentiels", "Jackson Pollock en est la figure majeure."),
]),
notion('A-4', 1, I, 'mus-chanson-francaise', [
  Q("Quelle chanteuse française est célèbre pour La Vie en rose et Non, je ne regrette rien ?", ["Édith Piaf", "Barbara", "Dalida", "Juliette Gréco"], "Édith Piaf", "Elle est une figure majeure de la chanson française du XXe siècle."),
  Q("Quel auteur-compositeur-interprète a écrit Les Copains d'abord ?", ["Georges Brassens", "Jacques Brel", "Serge Gainsbourg", "Charles Aznavour"], "Georges Brassens", "La chanson, de 1964, accompagne le film Les Copains d'Yves Robert."),
  Q("Quel chanteur belge a écrit Ne me quitte pas ?", ["Jacques Brel", "Léo Ferré", "Georges Brassens", "Boris Vian"], "Jacques Brel", "La chanson date de 1959."),
]),
notion('A-4', 1, I, 'mus-musique-baroque', [
  Q("Quel instrument à clavier, aux cordes pincées, est typique de la musique baroque ?", ["Le clavecin", "Le piano", "Le synthétiseur", "L'accordéon"], "Le clavecin", "Le piano le remplace progressivement au XVIIIe siècle."),
  Q("Quel compositeur de la cour de Louis XIV a écrit de nombreuses musiques pour les ballets et les comédies de Molière ?", ["Jean-Baptiste Lully", "Hector Berlioz", "Claude Debussy", "Maurice Ravel"], "Jean-Baptiste Lully", "Lully est surintendant de la musique du roi."),
  Q("Quel compositeur allemand a écrit le Messie, dont le célèbre « Alléluia » ?", ["Haendel", "Bach", "Mozart", "Beethoven"], "Haendel", "Le Messie est créé à Dublin en 1742."),
]),
]

from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('A-1', 0, D, 'art-manet-modernite', [
  Q("Quel tableau d'Édouard Manet fait scandale au Salon des refusés de 1863 ?", ["Le Déjeuner sur l'herbe", "Olympia", "Le Fifre", "Un bar aux Folies Bergère"], "Le Déjeuner sur l'herbe", "Une femme nue, contemporaine, au milieu d'hommes habillés choque le public."),
  Q("Pourquoi Olympia (1863, exposée en 1865) de Manet choque-t-elle ?", ["Parce qu'elle est abstraite", "Parce qu'elle représente une femme nue contemporaine qui regarde le spectateur sans idéalisation mythologique", "Parce qu'elle est en noir et blanc", "Parce qu'elle est très petite"], "Parce qu'elle représente une femme nue contemporaine qui regarde le spectateur sans idéalisation mythologique", "Manet reprend la Vénus d'Urbin de Titien en la modernisant."),
  Q("Qu'est-ce que le Salon des refusés de 1863 ?", ["Une exposition d'œuvres rejetées par le jury du Salon officiel, autorisée par Napoléon III", "Un musée d'art moderne", "Un concours de sculpture", "Une galerie privée"], "Une exposition d'œuvres rejetées par le jury du Salon officiel, autorisée par Napoléon III", "Il marque une étape dans l'émergence de l'art moderne."),
]),
notion('A-1', 0, D, 'art-cezanne', [
  Q("Quel peintre est souvent considéré comme le « père de l'art moderne », notamment par Picasso ?", ["Paul Cézanne", "Claude Monet", "Ingres", "Gustave Courbet"], "Paul Cézanne", "Il cherche à traiter la nature « par le cylindre, la sphère, le cône »."),
  Q("Quelle montagne Cézanne a-t-il peinte de nombreuses fois ?", ["La montagne Sainte-Victoire", "Le mont Blanc", "Le mont Ventoux", "Le Puy de Dôme"], "La montagne Sainte-Victoire", "Elle domine la région d'Aix-en-Provence, sa ville natale."),
  Q("En quoi Cézanne prépare-t-il le cubisme ?", ["Il peint des scènes religieuses", "Il simplifie les formes en volumes géométriques et multiplie les points de vue", "Il invente la photographie", "Il abandonne la couleur"], "Il simplifie les formes en volumes géométriques et multiplie les points de vue", "Ses natures mortes juxtaposent des angles de vue différents."),
]),
notion('A-1', 2, D, 'art-avant-gardes', [
  Q("Quel mouvement italien, lancé par Marinetti en 1909, célèbre la vitesse, la machine et la modernité ?", ["Le futurisme", "Le surréalisme", "Le dadaïsme", "L'impressionnisme"], "Le futurisme", "Le manifeste est publié dans Le Figaro en 1909."),
  Q("Quel mouvement né à Zurich en 1916 rejette les valeurs artistiques traditionnelles par la provocation et l'absurde ?", ["Dada", "Le Bauhaus", "Le cubisme", "Le fauvisme"], "Dada", "Il naît au Cabaret Voltaire, en réaction à la Première Guerre mondiale."),
  Q("Quelle école allemande, fondée par Gropius en 1919, réunit arts, artisanat et industrie ?", ["Le Bauhaus", "L'École de Paris", "Der Blaue Reiter", "Die Brücke"], "Le Bauhaus", "Elle influence durablement le design et l'architecture moderne."),
]),
notion('A-1', 1, D, 'art-nombre-or-composition', [
  Q("Qu'est-ce que le nombre d'or ?", ["Un prix décerné aux artistes", "Une proportion d'environ 1,618, réputée harmonieuse", "Le nombre de couleurs primaires", "La date de la Renaissance"], "Une proportion d'environ 1,618, réputée harmonieuse", "Son usage réel par les artistes est souvent surestimé."),
  Q("Qu'est-ce que la « règle des tiers » en photographie ?", ["Prendre trois photos", "Placer les éléments importants sur les lignes qui divisent l'image en tiers", "Utiliser trois couleurs", "Photographier trois personnes"], "Placer les éléments importants sur les lignes qui divisent l'image en tiers", "Elle dynamise la composition par rapport au centrage."),
  Q("Quel peintre a théorisé la perspective dans De pictura (1435) ?", ["Leon Battista Alberti", "Giotto", "Michel-Ange", "Vasari"], "Leon Battista Alberti", "Il compare le tableau à une « fenêtre ouverte »."),
]),
notion('A-2', 1, D, 'art-matieres-contemporaines', [
  Q("Quel artiste allemand utilise le feutre et la graisse, matériaux liés à son récit personnel ?", ["Joseph Beuys", "Gerhard Richter", "Anselm Kiefer", "Kurt Schwitters"], "Joseph Beuys", "Il raconte avoir été soigné avec ces matériaux après un accident d'avion."),
  Q("Quel artiste britannique a présenté un requin dans du formol (1991) ?", ["Damien Hirst", "Banksy", "David Hockney", "Anish Kapoor"], "Damien Hirst", "L'œuvre s'intitule The Physical Impossibility of Death in the Mind of Someone Living."),
  Q("Pourquoi certains artistes utilisent-ils des matériaux périssables (aliments, fleurs, glace) ?", ["Par économie uniquement", "Pour intégrer le temps, la transformation ou la disparition au sens de l'œuvre", "Parce qu'ils sont plus solides", "Par erreur"], "Pour intégrer le temps, la transformation ou la disparition au sens de l'œuvre", "Cela pose aussi des questions de conservation pour les musées."),
]),
notion('A-2', 2, D, 'art-pigments', [
  Q("D'où vient historiquement le bleu outremer, très précieux à la Renaissance ?", ["Du lapis-lazuli broyé", "Du ciel", "Du cuivre", "Du charbon"], "Du lapis-lazuli broyé", "Importé d'Afghanistan, il coûtait plus cher que l'or."),
  Q("Quels pigments les hommes préhistoriques utilisaient-ils principalement ?", ["Des ocres (terres) et du charbon de bois ou des oxydes de manganèse", "Des pigments synthétiques", "Du bleu outremer", "Des encres industrielles"], "Des ocres (terres) et du charbon de bois ou des oxydes de manganèse", "Les ocres donnent des rouges et des jaunes."),
  Q("Quel bleu Yves Klein a-t-il fait déposer en 1960 ?", ["L'IKB (International Klein Blue)", "Le bleu de Prusse", "Le bleu cobalt", "Le bleu ciel"], "L'IKB (International Klein Blue)", "Il dépose une enveloppe Soleau pour protéger sa formule de liant."),
]),
notion('A-3', 2, D, 'art-institution', [
  Q("Que dénonce la critique institutionnelle en art contemporain ?", ["Les techniques de peinture", "Le rôle des musées, des galeries et du marché dans la définition de l'art", "Les couleurs vives", "Le dessin d'observation"], "Le rôle des musées, des galeries et du marché dans la définition de l'art", "Hans Haacke ou Daniel Buren interrogent les lieux d'exposition."),
  Q("Qu'est-ce que l'art conceptuel ?", ["Un art où l'idée prime sur la réalisation matérielle", "Un art purement décoratif", "Un art uniquement religieux", "Un art de la sculpture en marbre"], "Un art où l'idée prime sur la réalisation matérielle", "Joseph Kosuth présente One and Three Chairs en 1965."),
  Q("Que présente l'œuvre One and Three Chairs de Joseph Kosuth ?", ["Trois chaises identiques", "Une chaise réelle, sa photographie et sa définition du dictionnaire", "Un tableau de chaise", "Une chaise cassée"], "Une chaise réelle, sa photographie et sa définition du dictionnaire", "Elle interroge le rapport entre objet, image et langage."),
]),
notion('A-3', 1, D, 'art-oeuvre-espace-public', [
  Q("Quel dispositif français impose de consacrer environ 1 % du coût de construction d'un bâtiment public à une œuvre d'art ?", ["Le 1 % artistique", "La loi Malraux", "Le Pass Culture", "Le label Patrimoine"], "Le 1 % artistique", "Il existe depuis 1951 pour les bâtiments scolaires notamment."),
  Q("Quel artiste a réalisé La Fontaine Stravinsky à Paris avec Niki de Saint Phalle ?", ["Jean Tinguely", "Alexander Calder", "César", "Arman"], "Jean Tinguely", "Ses sculptures mécaniques en mouvement côtoient les sculptures colorées de Niki de Saint Phalle."),
  Q("Quelle question pose souvent une œuvre dans l'espace public ?", ["Sa valeur marchande uniquement", "Son rapport aux habitants, au lieu et à son usage", "Sa taille exacte", "La couleur de son socle"], "Son rapport aux habitants, au lieu et à son usage", "Les colonnes de Buren ont suscité une vive polémique en 1986."),
]),
notion('A-4', 0, D, 'mus-analyse-avancee', [
  Q("Qu'est-ce qu'un leitmotiv, notamment chez Wagner ?", ["Une danse", "Un motif musical associé à un personnage, une idée ou un objet", "Un instrument", "Un silence"], "Un motif musical associé à un personnage, une idée ou un objet", "John Williams l'utilise aussi dans la musique de Star Wars."),
  Q("Qu'est-ce qu'une fugue ?", ["Un morceau improvisé", "Une forme contrapuntique où un thème est repris successivement par plusieurs voix", "Un opéra", "Une marche militaire"], "Une forme contrapuntique où un thème est repris successivement par plusieurs voix", "Bach en est le maître (L'Art de la fugue)."),
  Q("Qu'est-ce que le contrepoint ?", ["Un instrument", "L'art de superposer plusieurs lignes mélodiques indépendantes", "Un tempo", "Une nuance"], "L'art de superposer plusieurs lignes mélodiques indépendantes", "Il est au cœur de la musique baroque."),
]),
notion('A-4', 1, D, 'mus-histoire-repere', [
  Q("Comment appelle-t-on le chant liturgique monodique de l'Église catholique au Moyen Âge ?", ["Le chant grégorien", "Le gospel", "Le madrigal", "L'opéra"], "Le chant grégorien", "Il est chanté a cappella, à l'unisson, en latin."),
  Q("Quel moine du XIe siècle invente un système de notation qui donne leur nom à certaines notes (ut, ré, mi…) ?", ["Guido d'Arezzo", "Saint Benoît", "Pérotin", "Josquin des Prés"], "Guido d'Arezzo", "Les noms viennent des premières syllabes de l'hymne à saint Jean-Baptiste."),
  Q("Quelle note s'appelait « ut » avant d'être renommée dans la plupart des pays latins ?", ["Do", "Ré", "Sol", "Si"], "Do", "« Ut » a été remplacé par « do », plus facile à chanter."),
]),
notion('A-4', 1, D, 'mus-comparer-epoques', [
  Q("Quelle caractéristique distingue souvent la musique romantique de la musique classique ?", ["Moins d'instruments", "L'expression plus intense des émotions et des formes plus libres", "L'absence de mélodie", "L'usage exclusif du clavecin"], "L'expression plus intense des émotions et des formes plus libres", "L'orchestre romantique s'agrandit aussi."),
  Q("Quel compositeur de la Symphonie fantastique (1830) est une figure du romantisme français ?", ["Hector Berlioz", "Jean-Philippe Rameau", "Camille Saint-Saëns", "Érik Satie"], "Hector Berlioz", "La symphonie raconte une histoire : c'est de la musique à programme."),
  Q("Qu'est-ce que la musique à programme ?", ["Une musique de télévision", "Une musique instrumentale qui évoque une histoire, une image ou un texte", "Une musique d'ordinateur", "Une musique sans titre"], "Une musique instrumentale qui évoque une histoire, une image ou un texte", "La Moldau de Smetana décrit le cours d'une rivière."),
]),
notion('A-5', 0, D, 'mus-gammes-intervalles', [
  Q("Quelle suite de tons et demi-tons forme une gamme majeure ?", ["Ton, ton, demi-ton, ton, ton, ton, demi-ton", "Ton, demi-ton, ton, ton, demi-ton, ton, ton", "Demi-ton partout", "Ton partout"], "Ton, ton, demi-ton, ton, ton, ton, demi-ton", "Do majeur : do-ré-mi (ton, ton), mi-fa (demi-ton)…"),
  N("Combien de demi-tons y a-t-il entre do et sol (quinte juste) ?", 7, "do-do♯-ré-ré♯-mi-fa-fa♯-sol : 7 demi-tons."),
  Q("Quel caractère est souvent associé au mode mineur dans la musique occidentale ?", ["Joyeux et brillant", "Plus sombre ou mélancolique", "Toujours rapide", "Sans émotion"], "Plus sombre ou mélancolique", "Cette association est culturelle et non absolue."),
]),
notion('A-5', 0, D, 'mus-rythme-calcul', [
  N("Une noire pointée vaut combien de croches ?", 3, "Le point ajoute la moitié de la durée : 2 + 1 = 3 croches."),
  N("À un tempo de 120 noires par minute, combien de secondes dure une noire ?", 0.5, "60 / 120 = 0,5 s."),
  N("Un morceau à 4/4 dure 32 mesures à 120 noires par minute. Combien de secondes dure-t-il ?", 64, "32 × 4 = 128 noires ; 128 × 0,5 s = 64 s."),
]),
notion('A-4', 2, D, 'mus-orchestration', [
  Q("Dans un orchestre symphonique, où sont généralement placés les cordes ?", ["Au fond", "Devant, au plus près du chef", "Sur les côtés uniquement", "Dans la fosse sous la scène"], "Devant, au plus près du chef", "Les bois sont derrière, puis les cuivres et les percussions au fond."),
  Q("Quelle œuvre de Benjamin Britten présente un à un les instruments de l'orchestre ?", ["The Young Person's Guide to the Orchestra", "Pierre et le Loup", "Le Carnaval des animaux", "Les Planètes"], "The Young Person's Guide to the Orchestra", "Composée en 1945 sur un thème de Purcell."),
  Q("Qu'est-ce qu'un tutti ?", ["Un passage joué par tout l'orchestre", "Un solo", "Un silence", "Un instrument italien"], "Un passage joué par tout l'orchestre", "Il s'oppose au solo."),
]),
notion('A-3', 0, D, 'art-photographie-art', [
  Q("Quel photographe américain a capturé les effets de la Grande Dépression, avec Migrant Mother (1936) ?", ["Dorothea Lange", "Ansel Adams", "Diane Arbus", "Cindy Sherman"], "Dorothea Lange", "La photographie documentaire devient un témoignage social."),
  Q("Quelle artiste américaine se met en scène dans ses photographies pour interroger les stéréotypes, notamment avec ses Untitled Film Stills ?", ["Cindy Sherman", "Annie Leibovitz", "Diane Arbus", "Nan Goldin"], "Cindy Sherman", "Elle joue des rôles inspirés des films de série B."),
  Q("Quelle artiste française mêle photographie et récit autobiographique, comme dans Suite vénitienne ?", ["Sophie Calle", "Annette Messager", "Orlan", "Agnès Varda"], "Sophie Calle", "Elle a suivi un inconnu jusqu'à Venise en 1980."),
  Q("Quel artiste français colle d'immenses portraits photographiques dans l'espace public ?", ["JR", "Invader", "Banksy", "Keith Haring"], "JR", "Il a notamment réalisé des collages sur la pyramide du Louvre."),
]),
notion('A-1', 0, D, 'art-femmes-artistes', [
  Q("Quelle peintre baroque italienne a peint Judith décapitant Holopherne ?", ["Artemisia Gentileschi", "Élisabeth Vigée Le Brun", "Rosa Bonheur", "Sofonisba Anguissola"], "Artemisia Gentileschi", "Elle est l'une des rares femmes reconnues de son époque."),
  Q("Quelle peintre a été la portraitiste officielle de Marie-Antoinette ?", ["Élisabeth Vigée Le Brun", "Berthe Morisot", "Camille Claudel", "Suzanne Valadon"], "Élisabeth Vigée Le Brun", "Elle a peint plus de 30 portraits de la reine."),
  Q("Quelle sculptrice, élève puis compagne de Rodin, a réalisé La Valse et L'Âge mûr ?", ["Camille Claudel", "Niki de Saint Phalle", "Louise Bourgeois", "Germaine Richier"], "Camille Claudel", "Un musée lui est consacré à Nogent-sur-Seine."),
  Q("Quelle impressionniste a exposé à presque toutes les expositions du groupe ?", ["Berthe Morisot", "Frida Kahlo", "Tamara de Lempicka", "Sonia Delaunay"], "Berthe Morisot", "Elle participe à sept des huit expositions impressionnistes."),
]),
]

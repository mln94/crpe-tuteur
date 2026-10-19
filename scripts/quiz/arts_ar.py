# Arts plastiques · La représentation ; images, réalité et fiction : 25 questions par niveau et par point du programme
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ AR-1 · La ressemblance ══
notion('AR-1', 0, F, 'artr-genres-picturaux', [
  Q("Comment appelle-t-on la représentation de la nature, de la campagne ou de la montagne ?", ["Un paysage", "Une nature morte", "Un portrait", "Une scène de genre"], "Un paysage", "Le paysage devient un genre autonome au XVIIe siècle."),
  Q("Comment appelle-t-on la représentation de scènes de la vie quotidienne ?", ["La scène de genre", "La peinture d'histoire", "La marine", "Le paysage"], "La scène de genre", "Vermeer en est un maître."),
  Q("Comment appelle-t-on un portrait qu'un artiste fait de lui-même ?", ["Un autoportrait", "Un selfie peint", "Une caricature", "Un profil"], "Un autoportrait", "Rembrandt en a peint plus de 80."),
]),
notion('AR-1', 0, F, 'artr-croquis-esquisse', [
  Q("Comment appelle-t-on un dessin rapide qui saisit l'essentiel d'un sujet ?", ["Un croquis", "Une fresque", "Une gravure", "Une mosaïque"], "Un croquis", "On le réalise souvent sur le motif."),
  Q("Qu'est-ce qu'une esquisse ?", ["Un premier état, préparatoire, d'une œuvre", "Une œuvre achevée", "Un cadre", "Un vernis"], "Un premier état, préparatoire, d'une œuvre", "Elle permet de chercher la composition."),
  Q("Que signifie « dessiner d'après nature » ?", ["Dessiner en observant directement le modèle réel", "Dessiner des plantes", "Dessiner de mémoire", "Recopier une photo"], "Dessiner en observant directement le modèle réel", "On dit aussi « sur le motif »."),
]),
notion('AR-1', 0, F, 'artr-caricature', [
  Q("Qu'est-ce qu'une caricature ?", ["Un portrait qui exagère les traits pour faire rire ou critiquer", "Un portrait très fidèle", "Une photo officielle", "Un paysage"], "Un portrait qui exagère les traits pour faire rire ou critiquer", "Daumier en est un maître au XIXe siècle."),
  Q("Quel artiste français du XIXe siècle a caricaturé le roi Louis-Philippe en poire ?", ["Honoré Daumier (et Philipon)", "Claude Monet", "Edgar Degas", "Jean-Louis David"], "Honoré Daumier (et Philipon)", "La poire devient un symbole de la satire."),
  Q("Pourquoi la caricature s'écarte-t-elle de la ressemblance ?", ["Pour souligner un trait de caractère ou critiquer", "Par maladresse", "Pour imiter la photographie", "Pour cacher le modèle"], "Pour souligner un trait de caractère ou critiquer", "L'écart a une valeur expressive."),
]),
notion('AR-1', 0, F, 'artr-photo-realisme', [
  Q("Comment appelle-t-on un dessin ou une peinture qui imite la précision d'une photographie ?", ["Hyperréaliste", "Abstrait", "Cubiste", "Fauve"], "Hyperréaliste", "On a parfois du mal à croire que ce n'est pas une photo."),
  Q("Quel sculpteur hyperréaliste australien crée des figures humaines géantes ou minuscules ?", ["Ron Mueck", "Alberto Giacometti", "Auguste Rodin", "Henry Moore"], "Ron Mueck", "Ses sculptures jouent sur l'échelle."),
  Q("L'œuvre la plus ressemblante est-elle forcément la plus réussie ?", ["Non, l'écart peut être un choix expressif", "Oui, toujours", "Seulement pour les portraits", "Seulement en sculpture"], "Non, l'écart peut être un choix expressif", "Matisse ou Picasso s'éloignent volontairement du réel."),
]),
notion('AR-1', 0, I, 'artr-ecart-expressif', [
  Q("Pourquoi Giacometti étire-t-il ses sculptures de personnages ?", ["Pour exprimer la fragilité et la solitude de l'être humain", "Par manque de matière", "Pour les rendre plus réalistes", "Pour les faire tenir debout"], "Pour exprimer la fragilité et la solitude de l'être humain", "L'Homme qui marche (1960) en est un exemple."),
  Q("Quel peintre a représenté sa chambre à Arles avec des couleurs vives et une perspective déformée ?", ["Vincent van Gogh", "Paul Cézanne", "Claude Monet", "Georges Seurat"], "Vincent van Gogh", "La Chambre (1888)."),
  Q("Que cherche Matisse en peignant un visage avec une bande verte (La Raie verte, 1905) ?", ["Exprimer par la couleur plutôt qu'imiter le réel", "Représenter une maladie", "Copier exactement son modèle", "Faire un trompe-l'œil"], "Exprimer par la couleur plutôt qu'imiter le réel", "C'est un manifeste fauve."),
]),
notion('AR-1', 0, I, 'artr-mimesis', [
  Q("Comment appelle-t-on, depuis l'Antiquité, l'imitation de la nature par l'art ?", ["La mimésis", "La catharsis", "L'abstraction", "La perspective"], "La mimésis", "Le mot est grec."),
  Q("Selon la légende antique, quel peintre peignait des raisins si réalistes que des oiseaux venaient les picorer ?", ["Zeuxis", "Apelle", "Phidias", "Praxitèle"], "Zeuxis", "Son rival Parrhasios peignit un rideau qui trompa Zeuxis lui-même."),
  Q("Quel philosophe grec se méfiait de l'art, simple copie d'une copie ?", ["Platon", "Aristote", "Socrate", "Épicure"], "Platon", "Aristote valorisait au contraire l'imitation."),
]),
notion('AR-1', 0, I, 'artr-portraits-officiels', [
  Q("Quel peintre a réalisé le portrait officiel de Louis XIV en costume de sacre (1701) ?", ["Hyacinthe Rigaud", "Jacques-Louis David", "Ingres", "Le Brun"], "Hyacinthe Rigaud", "Le tableau est au Louvre."),
  Q("Qu'est-ce qu'un portrait d'apparat ?", ["Un portrait qui met en scène le rang et le pouvoir du modèle", "Un portrait intime", "Un autoportrait", "Une caricature"], "Un portrait qui met en scène le rang et le pouvoir du modèle", "Les attributs (couronne, sceptre) comptent autant que le visage."),
  Q("Qu'est-ce qu'un attribut dans un portrait ?", ["Un objet qui renseigne sur l'identité ou le rôle du modèle", "Le cadre", "La signature", "La couleur du fond"], "Un objet qui renseigne sur l'identité ou le rôle du modèle", "La balance de la Justice, le livre du savant…"),
]),
notion('AR-1', 0, I, 'artr-impressionnisme-2', [
  Q("Quel peintre impressionniste est célèbre pour ses danseuses de l'Opéra ?", ["Edgar Degas", "Claude Monet", "Camille Pissarro", "Alfred Sisley"], "Edgar Degas", "Il utilise beaucoup le pastel."),
  Q("Quelle série de Monet représente la même cathédrale à différentes heures ?", ["Les Cathédrales de Rouen", "Les Nymphéas", "Les Meules", "La Gare Saint-Lazare"], "Les Cathédrales de Rouen", "Il étudie les variations de la lumière."),
  Q("Pourquoi les impressionnistes peignent-ils souvent en plein air ?", ["Pour saisir directement les effets changeants de la lumière", "Parce que les ateliers étaient interdits", "Pour aller plus vite", "Parce qu'ils n'avaient pas d'atelier"], "Pour saisir directement les effets changeants de la lumière", "Les tubes de peinture leur facilitent la tâche."),
]),
notion('AR-1', 0, I, 'artr-pointillisme', [
  Q("Quel peintre a inventé le pointillisme avec Un dimanche après-midi à l'île de la Grande Jatte ?", ["Georges Seurat", "Paul Signac", "Claude Monet", "Paul Gauguin"], "Georges Seurat", "Paul Signac poursuit cette voie."),
  Q("Sur quel principe repose le pointillisme ?", ["Des touches de couleurs pures juxtaposées qui se mélangent dans l'œil", "Des aplats de couleur", "Des lignes noires", "Des collages"], "Des touches de couleurs pures juxtaposées qui se mélangent dans l'œil", "On parle de mélange optique."),
  Q("Comment appelle-t-on aussi le pointillisme ?", ["Le divisionnisme (néo-impressionnisme)", "Le fauvisme", "Le cubisme analytique", "Le tachisme"], "Le divisionnisme (néo-impressionnisme)", "Il s'appuie sur les théories de la couleur."),
]),
notion('AR-1', 0, D, 'artr-ingres-deformation', [
  Q("Pourquoi La Grande Odalisque d'Ingres (1814) a-t-elle été critiquée ?", ["Son dos est anatomiquement trop long", "Elle est trop petite", "Elle est inachevée", "Elle est abstraite"], "Son dos est anatomiquement trop long", "Ingres privilégie la beauté de la ligne."),
  Q("Quel courant du XVIe siècle allonge les corps et complique les poses, comme chez Parmesan ?", ["Le maniérisme", "Le réalisme", "L'impressionnisme", "Le néoclassicisme"], "Le maniérisme", "La Madone au long cou en est un exemple."),
  Q("Quel peintre crétois installé à Tolède est célèbre pour ses figures étirées ?", ["Le Greco", "Vélasquez", "Goya", "Zurbarán"], "Le Greco", "L'Enterrement du comte d'Orgaz (1586)."),
]),
notion('AR-1', 0, D, 'artr-modigliani-bacon', [
  Q("Quel peintre italien est connu pour ses portraits aux visages allongés et aux yeux en amande ?", ["Amedeo Modigliani", "Giorgio de Chirico", "Caravage", "Botticelli"], "Amedeo Modigliani", "Il travaille à Montparnasse."),
  Q("Quel peintre britannique a déformé des portraits pour exprimer l'angoisse, d'après Vélasquez ?", ["Francis Bacon", "David Hockney", "Lucian Freud", "William Turner"], "Francis Bacon", "Étude d'après le portrait du pape Innocent X (1953)."),
  Q("Quel peintre autrichien a peint des corps tourmentés et anguleux au début du XXe siècle ?", ["Egon Schiele", "Gustav Klimt", "Oskar Kokoschka", "Paul Klee"], "Egon Schiele", "Il est proche de l'expressionnisme."),
]),
notion('AR-1', 0, D, 'artr-ressemblance-photo', [
  Q("Quel peintre français déclara, selon la légende, « À partir d'aujourd'hui, la peinture est morte » en découvrant la photographie ?", ["Paul Delaroche", "Ingres", "Delacroix", "Courbet"], "Paul Delaroche", "La photographie bouscule la fonction de ressemblance de la peinture."),
  Q("Comment la photographie a-t-elle influencé la peinture au XIXe siècle ?", ["Elle a libéré les peintres de l'obligation d'imiter fidèlement", "Elle a fait disparaître la peinture", "Elle a imposé le noir et blanc", "Aucune influence"], "Elle a libéré les peintres de l'obligation d'imiter fidèlement", "La peinture explore alors la couleur et la forme."),
  Q("Quel peintre a utilisé des photographies de chevaux au galop pour corriger ses tableaux ?", ["Edgar Degas", "Paul Cézanne", "Henri Matisse", "Claude Monet"], "Edgar Degas", "Grâce aux photos de Muybridge."),
]),
notion('AR-1', 0, D, 'artr-portrait-identite', [
  Q("Quel artiste a peint des portraits presque monochromes, aux visages effacés, à partir de photos (Gerhard Richter) ?", ["Gerhard Richter", "Andy Warhol", "Cindy Sherman", "Chuck Close"], "Gerhard Richter", "Ses toiles floues interrogent la mémoire."),
  Q("Quel peintre américain réalisait des portraits géants à partir de grilles de petits carrés ?", ["Chuck Close", "Roy Lichtenstein", "Edward Hopper", "Jasper Johns"], "Chuck Close", "De près, on voit des cellules ; de loin, un visage."),
  Q("Quelle artiste française a réalisé des autoportraits en transformant son propre corps ?", ["ORLAN", "Sophie Calle", "Annette Messager", "Niki de Saint Phalle"], "ORLAN", "Elle utilise son propre corps comme matériau."),
]),
notion('AR-1', 0, D, 'artr-courbet-realisme', [
  Q("Quel tableau de Courbet représente des ouvriers cassant des pierres sur une route ?", ["Les Casseurs de pierres", "L'Origine du monde", "Bonjour Monsieur Courbet", "L'Angélus"], "Les Casseurs de pierres", "Le réalisme montre le monde du travail."),
  Q("Quel peintre réaliste a peint L'Angélus et Les Glaneuses ?", ["Jean-François Millet", "Gustave Courbet", "Honoré Daumier", "Jules Breton"], "Jean-François Millet", "Il représente la vie paysanne."),
  Q("Quel principe guide le réalisme selon Courbet ?", ["Peindre ce que l'on voit, y compris le banal et les gens ordinaires", "Peindre les dieux et les héros", "Peindre le rêve", "Peindre des formes géométriques"], "Peindre ce que l'on voit, y compris le banal et les gens ordinaires", "« Montrez-moi un ange et j'en peindrai un »."),
]),
notion('AR-1', 0, D, 'artr-art-premier', [
  Q("Quel peintre s'est inspiré des masques africains pour Les Demoiselles d'Avignon ?", ["Picasso", "Monet", "Renoir", "Degas"], "Picasso", "L'art africain bouscule la représentation occidentale."),
  Q("Quel musée parisien expose les arts d'Afrique, d'Asie, d'Océanie et des Amériques ?", ["Le musée du quai Branly – Jacques-Chirac", "Le musée d'Orsay", "Le Centre Pompidou", "Le musée Rodin"], "Le musée du quai Branly – Jacques-Chirac", "Il ouvre en 2006."),
  Q("Quel peintre français est parti à Tahiti pour peindre un monde jugé plus « primitif » ?", ["Paul Gauguin", "Paul Cézanne", "Henri Rousseau", "Claude Monet"], "Paul Gauguin", "Ce regard est aujourd'hui interrogé."),
]),
notion('AR-1', 0, D, 'artr-douanier-rousseau', [
  Q("Quel peintre autodidacte, surnommé « le Douanier », a peint des jungles imaginaires ?", ["Henri Rousseau", "Paul Gauguin", "Henri Matisse", "Raoul Dufy"], "Henri Rousseau", "Il n'a jamais quitté la France."),
  Q("Comment appelle-t-on l'art d'artistes autodidactes au style simple et minutieux ?", ["L'art naïf", "L'art brut", "L'art conceptuel", "L'art cinétique"], "L'art naïf", "Séraphine de Senlis en est un exemple."),
  Q("Comment Jean Dubuffet appelle-t-il l'art créé hors de toute culture artistique, par des marginaux ?", ["L'art brut", "L'art naïf", "Le pop art", "L'art déco"], "L'art brut", "Il en rassemble une collection à Lausanne."),
]),
notion('AR-1', 0, D, 'artr-vraisemblance-sculpture', [
  Q("Quelle sculpture de Rodin a été accusée d'être un moulage sur nature tant elle était réaliste ?", ["L'Âge d'airain", "Le Penseur", "Le Baiser", "Balzac"], "L'Âge d'airain", "Rodin a dû prouver qu'il l'avait modelée."),
  Q("Pourquoi le Balzac de Rodin (1898) a-t-il choqué ?", ["Il s'éloigne de la ressemblance pour exprimer le génie de l'écrivain", "Il était trop petit", "Il était en or", "Il était trop réaliste"], "Il s'éloigne de la ressemblance pour exprimer le génie de l'écrivain", "La Société des gens de lettres l'a refusé."),
  Q("Qu'est-ce qu'un moulage ?", ["La reproduction d'une forme à l'aide d'un moule", "Une gravure", "Une peinture", "Une photo"], "La reproduction d'une forme à l'aide d'un moule", "On peut mouler sur un modèle vivant."),
]),
# ══ AR-2 · Le dispositif de représentation ══
notion('AR-2', 0, F, 'artr-cadrages', [
  Q("Comment appelle-t-on un plan qui montre un visage de très près ?", ["Un gros plan", "Un plan d'ensemble", "Un plan moyen", "Un plan large"], "Un gros plan", "Il met en valeur les émotions."),
  Q("Comment appelle-t-on un plan qui montre un vaste paysage ?", ["Un plan d'ensemble (plan large)", "Un gros plan", "Un insert", "Un très gros plan"], "Un plan d'ensemble (plan large)", "Il situe l'action."),
  Q("Qu'est-ce que le cadrage ?", ["Le choix de ce qui est montré dans l'image et de ce qui en est exclu", "La pose d'un cadre en bois", "La signature de l'artiste", "Le vernissage"], "Le choix de ce qui est montré dans l'image et de ce qui en est exclu", "Il oriente le regard."),
]),
notion('AR-2', 0, F, 'artr-plongee-contre', [
  Q("Comment appelle-t-on une prise de vue d'en haut vers le bas ?", ["Une plongée", "Une contre-plongée", "Un panoramique", "Un zoom"], "Une plongée", "Elle peut écraser ou rapetisser le sujet."),
  Q("Quel effet donne souvent une contre-plongée ?", ["Le sujet paraît plus grand, plus puissant", "Le sujet paraît plus petit", "Le sujet disparaît", "Aucun effet"], "Le sujet paraît plus grand, plus puissant", "On l'utilise pour les héros ou les monuments."),
  Q("Comment appelle-t-on une prise de vue à hauteur d'yeux ?", ["Un plan frontal (à hauteur d'homme)", "Une plongée totale", "Une vue aérienne", "Un zoom"], "Un plan frontal (à hauteur d'homme)", "Il paraît neutre et naturel."),
]),
notion('AR-2', 0, F, 'artr-formats', [
  Q("Comment appelle-t-on un support plus haut que large ?", ["Un format portrait (vertical)", "Un format paysage", "Un format carré", "Un format rond"], "Un format portrait (vertical)", "Format paysage = horizontal."),
  Q("Comment appelle-t-on une œuvre de forme ronde ?", ["Un tondo", "Un triptyque", "Un retable", "Un diptyque"], "Un tondo", "Il était apprécié à la Renaissance."),
  Q("Comment appelle-t-on une œuvre en trois panneaux ?", ["Un triptyque", "Un diptyque", "Un polyptyque à deux volets", "Un tondo"], "Un triptyque", "Diptyque = deux panneaux."),
]),
notion('AR-2', 0, F, 'artr-plans-image', [
  Q("Comment appelle-t-on la partie de l'image la plus éloignée du spectateur ?", ["L'arrière-plan", "Le premier plan", "Le hors-champ", "Le cadre"], "L'arrière-plan", "Entre les deux : le plan intermédiaire."),
  Q("Qu'est-ce que la ligne d'horizon dans un dessin en perspective ?", ["La ligne à hauteur des yeux du spectateur", "Le bord du cadre", "Le sol", "La signature"], "La ligne à hauteur des yeux du spectateur", "Le point de fuite s'y trouve."),
  Q("Comment donner l'impression qu'un objet est loin dans un dessin ?", ["Le dessiner plus petit et plus haut sur la feuille", "Le dessiner plus grand", "Le dessiner en rouge vif", "Le dessiner au premier plan"], "Le dessiner plus petit et plus haut sur la feuille", "C'est la diminution des tailles."),
]),
notion('AR-2', 0, F, 'artr-cadre-fenetre', [
  Q("Quel théoricien de la Renaissance comparait le tableau à une « fenêtre ouverte » sur le monde ?", ["Alberti", "Vasari", "Léonard de Vinci", "Michel-Ange"], "Alberti", "Dans De pictura (1435)."),
  Q("Qu'est-ce que le champ dans une image ?", ["L'espace visible délimité par le cadre", "Un pré", "La toile entière avec son châssis", "Le titre"], "L'espace visible délimité par le cadre", "Le hors-champ est ce qu'on ne voit pas."),
  Q("Comment appelle-t-on une image placée à l'intérieur d'une autre (tableau dans le tableau) ?", ["Une mise en abyme", "Un trompe-l'œil", "Un collage", "Une anamorphose"], "Une mise en abyme", "Le reflet d'un miroir peut aussi la créer."),
]),
notion('AR-2', 0, F, 'artr-lumiere-ombre', [
  Q("Comment appelle-t-on le contraste fort entre zones claires et zones sombres ?", ["Le clair-obscur", "Le sfumato", "Le camaïeu", "Le glacis"], "Le clair-obscur", "Caravage et Rembrandt en sont des maîtres."),
  Q("Comment appelle-t-on l'ombre qu'un objet projette sur le sol ?", ["L'ombre portée", "L'ombre propre", "La silhouette", "Le contre-jour"], "L'ombre portée", "L'ombre propre est sur l'objet lui-même."),
  Q("Qu'est-ce qu'un contre-jour en photographie ?", ["Une prise de vue face à la lumière, le sujet apparaît sombre", "Une photo de nuit", "Une photo floue", "Une photo en couleur"], "Une prise de vue face à la lumière, le sujet apparaît sombre", "Le sujet devient une silhouette."),
]),
notion('AR-2', 0, I, 'artr-perspective-inversee', [
  Q("Comment appelle-t-on la perspective des icônes byzantines, où les lignes s'écartent vers le fond ?", ["La perspective inversée", "La perspective atmosphérique", "La perspective cavalière", "La perspective linéaire"], "La perspective inversée", "Le monde sacré semble venir vers le fidèle."),
  Q("Comment est souvent représenté l'espace dans l'art égyptien antique ?", ["Les corps de profil avec l'œil et les épaules de face", "En perspective linéaire", "En trompe-l'œil", "En vue aérienne"], "Les corps de profil avec l'œil et les épaules de face", "On montre chaque partie sous son meilleur angle."),
  Q("Comment les estampes japonaises représentent-elles souvent la profondeur ?", ["Par l'étagement des plans et des vues plongeantes", "Par un point de fuite unique", "Par le clair-obscur", "Elles ne la représentent jamais"], "Par l'étagement des plans et des vues plongeantes", "Elles ont fasciné les impressionnistes."),
]),
notion('AR-2', 0, I, 'artr-cadrage-photo-degas', [
  Q("Quel peintre impressionniste coupe audacieusement ses personnages par le bord du tableau, comme une photo ?", ["Edgar Degas", "Claude Monet", "Alfred Sisley", "Camille Pissarro"], "Edgar Degas", "Il s'inspire des estampes japonaises et de la photographie."),
  Q("Qu'apporte un cadrage décentré ?", ["Du dynamisme et une impression d'instantané", "De la symétrie", "Une image plus classique", "Rien"], "Du dynamisme et une impression d'instantané", "Le regard circule davantage."),
  Q("Quel graveur japonais a réalisé La Grande Vague de Kanagawa ?", ["Hokusai", "Hiroshige", "Utamaro", "Sharaku"], "Hokusai", "Le mont Fuji apparaît minuscule au fond."),
]),
notion('AR-2', 0, I, 'artr-espace-litteral-suggere', [
  Q("Que désigne l'espace littéral d'une œuvre en deux dimensions ?", ["La surface plane réelle du support", "L'espace imaginaire représenté", "La salle d'exposition", "Le cadre doré"], "La surface plane réelle du support", "L'espace suggéré est l'illusion de profondeur."),
  Q("Quels artistes ont affirmé la planéité du tableau au XXe siècle ?", ["Les peintres abstraits comme Mondrian ou Matisse dans ses papiers découpés", "Les peintres de la Renaissance", "Les peintres de trompe-l'œil", "Les photographes"], "Les peintres abstraits comme Mondrian ou Matisse dans ses papiers découpés", "Ils refusent l'illusion de profondeur."),
  Q("Quelle technique crée l'illusion de profondeur par la dégradation des couleurs avec la distance ?", ["La perspective atmosphérique (aérienne)", "La perspective cavalière", "L'aplat", "Le collage"], "La perspective atmosphérique (aérienne)", "Léonard de Vinci l'utilise beaucoup."),
]),
notion('AR-2', 0, I, 'artr-polyptyque', [
  Q("Comment appelle-t-on une œuvre composée de plusieurs panneaux, souvent articulés ?", ["Un polyptyque", "Un tondo", "Un cartel", "Un vitrail"], "Un polyptyque", "Le retable de l'Agneau mystique des frères Van Eyck en est un exemple."),
  Q("Où se trouvait souvent un retable ?", ["Au-dessus de l'autel d'une église", "Dans une salle de bains", "Sur la façade d'une mairie", "Au plafond d'un théâtre"], "Au-dessus de l'autel d'une église", "Ses volets pouvaient s'ouvrir les jours de fête."),
  Q("Quel grand retable de Matthias Grünewald est conservé à Colmar ?", ["Le retable d'Issenheim", "Le retable de Gand", "Le Jardin des délices", "La Cène"], "Le retable d'Issenheim", "Il est exposé au musée Unterlinden."),
]),
notion('AR-2', 0, I, 'artr-points-de-vue-multiples', [
  Q("Quel mouvement montre un objet sous plusieurs angles à la fois sur la même toile ?", ["Le cubisme", "L'impressionnisme", "Le réalisme", "Le romantisme"], "Le cubisme", "La perspective classique est abandonnée."),
  Q("Quel artiste britannique a assemblé des dizaines de photos pour créer des « joiners » ?", ["David Hockney", "Francis Bacon", "Banksy", "Damien Hirst"], "David Hockney", "Pearblossom Highway (1986)."),
  Q("Pourquoi multiplier les points de vue dans une même image ?", ["Pour montrer davantage la réalité d'un objet que ce que voit un œil fixe", "Pour tromper le spectateur", "Par erreur", "Pour respecter la perspective classique"], "Pour montrer davantage la réalité d'un objet que ce que voit un œil fixe", "C'est une autre façon de représenter."),
]),
notion('AR-2', 0, I, 'artr-camera-obscura', [
  Q("Quel dispositif optique projette une image inversée de l'extérieur dans une boîte noire ?", ["La camera obscura (chambre noire)", "Le stéréoscope", "Le zootrope", "Le kaléidoscope"], "La camera obscura (chambre noire)", "C'est l'ancêtre de l'appareil photo."),
  Q("Pourquoi certains peintres ont-ils utilisé la chambre noire ?", ["Pour les aider à reproduire exactement la perspective et les proportions", "Pour peindre dans le noir", "Pour sécher leurs toiles", "Pour faire des ombres chinoises"], "Pour les aider à reproduire exactement la perspective et les proportions", "On soupçonne Vermeer de l'avoir utilisée."),
  Q("Qu'est-ce qu'un sténopé ?", ["Un appareil photo très simple, sans objectif, avec un petit trou", "Un pinceau fin", "Un cadre de tableau", "Un type de crayon"], "Un appareil photo très simple, sans objectif, avec un petit trou", "On peut en fabriquer un en classe."),
]),
notion('AR-2', 0, D, 'artr-ambassadeurs', [
  Q("Quel tableau de Holbein (1533) contient une anamorphose de crâne au premier plan ?", ["Les Ambassadeurs", "La Joconde", "Les Ménines", "Les Époux Arnolfini"], "Les Ambassadeurs", "Il faut se placer de biais pour voir le crâne."),
  Q("Que symbolise le crâne caché dans Les Ambassadeurs ?", ["La mort et la vanité des richesses (memento mori)", "La victoire", "La science", "La joie"], "La mort et la vanité des richesses (memento mori)", "C'est un thème de la vanité."),
  Q("Qu'est-ce qu'une vanité en peinture ?", ["Une nature morte qui rappelle la brièveté de la vie", "Un autoportrait orgueilleux", "Un paysage", "Un portrait de cour"], "Une nature morte qui rappelle la brièveté de la vie", "Crânes, bougies éteintes, fleurs fanées…"),
]),
notion('AR-2', 0, D, 'artr-arnolfini', [
  Q("Quel tableau de Jan van Eyck (1434) montre un miroir convexe reflétant la scène ?", ["Les Époux Arnolfini", "Les Ambassadeurs", "La Joconde", "Les Ménines"], "Les Époux Arnolfini", "On y voit le peintre lui-même dans le reflet."),
  Q("Quelle technique les peintres flamands ont-ils perfectionnée au XVe siècle ?", ["La peinture à l'huile", "La fresque", "L'acrylique", "La tempera sur verre"], "La peinture à l'huile", "Elle permet des transparences et des détails précis."),
  Q("Que permet le miroir dans un tableau ?", ["De montrer un espace hors du cadre et d'élargir le champ", "De décorer seulement", "De cacher le peintre", "D'aplatir l'image"], "De montrer un espace hors du cadre et d'élargir le champ", "On le retrouve dans Les Ménines."),
]),
notion('AR-2', 0, D, 'artr-masaccio-brunelleschi', [
  Q("Quel architecte florentin a démontré la perspective linéaire vers 1415 ?", ["Filippo Brunelleschi", "Alberti", "Giotto", "Michel-Ange"], "Filippo Brunelleschi", "Il a aussi construit la coupole de Florence."),
  Q("Quelle fresque de Masaccio est l'une des premières à appliquer la perspective linéaire ?", ["La Trinité (Santa Maria Novella)", "La Cène", "Le Jugement dernier", "Le Printemps"], "La Trinité (Santa Maria Novella)", "Elle date d'environ 1427."),
  Q("Quel peintre du XIVe siècle, avant la perspective, a déjà donné du volume aux corps ?", ["Giotto", "Raphaël", "Titien", "Caravage"], "Giotto", "Fresques de la chapelle Scrovegni à Padoue."),
]),
notion('AR-2', 0, D, 'artr-grille-composition', [
  Q("Qu'est-ce qu'une composition pyramidale ?", ["Une organisation des personnages en triangle", "Un tableau représentant une pyramide", "Une perspective cavalière", "Une image abstraite"], "Une organisation des personnages en triangle", "Raphaël l'utilise pour ses Vierges."),
  Q("Quel tableau célèbre est construit en pyramide avec un radeau ?", ["Le Radeau de la Méduse", "La Joconde", "Les Nymphéas", "Guernica"], "Le Radeau de la Méduse", "La pyramide culmine avec un homme agitant un tissu."),
  Q("Que crée une composition en diagonale ?", ["Du mouvement et du dynamisme", "Du calme et de la stabilité", "Une symétrie parfaite", "Aucun effet"], "Du mouvement et du dynamisme", "L'horizontale évoque le repos."),
]),
notion('AR-2', 0, D, 'artr-installation-dispositif', [
  Q("Quel artiste a créé des « chambres de miroirs infinis » où le spectateur se perd ?", ["Yayoi Kusama", "Marina Abramović", "Louise Bourgeois", "Annette Messager"], "Yayoi Kusama", "Infinity Mirror Rooms."),
  Q("Quel artiste joue avec des miroirs et des points de vue pour déformer l'espace du spectateur ?", ["Anish Kapoor (Cloud Gate)", "Henri Matisse", "Claude Monet", "Auguste Rodin"], "Anish Kapoor (Cloud Gate)", "Sa sculpture miroir est à Chicago."),
  Q("Pourquoi certains artistes font-ils entrer le spectateur dans l'œuvre ?", ["Pour qu'il fasse partie du dispositif de représentation", "Pour le punir", "Par manque de place", "Pour protéger l'œuvre"], "Pour qu'il fasse partie du dispositif de représentation", "Le point de vue devient mobile."),
]),
notion('AR-2', 0, D, 'artr-ecran-dispositif', [
  Q("Quel artiste coréen est un pionnier de l'art vidéo avec des téléviseurs ?", ["Nam June Paik", "Bill Viola", "Pierre Huyghe", "Ai Weiwei"], "Nam June Paik", "TV Buddha (1974)."),
  Q("Quel artiste américain filme des scènes au ralenti aux allures de peintures religieuses ?", ["Bill Viola", "Andy Warhol", "Nam June Paik", "Christian Boltanski"], "Bill Viola", "Il interroge la vie, la mort et l'eau."),
  Q("Qu'est-ce qu'une installation vidéo ?", ["Une œuvre qui dispose des écrans et des images dans un espace", "Un film au cinéma", "Une émission de télévision", "Un jeu vidéo"], "Une œuvre qui dispose des écrans et des images dans un espace", "Le spectateur circule parmi les images."),
]),
notion('AR-2', 0, D, 'artr-perspective-curviligne', [
  Q("Quel effet produit un objectif « fish-eye » en photographie ?", ["Une forte déformation courbe de l'image", "Une image en noir et blanc", "Un zoom sans déformation", "Une image floue"], "Une forte déformation courbe de l'image", "Les lignes droites deviennent courbes."),
  Q("Quel graveur néerlandais a créé des espaces impossibles et des perspectives paradoxales ?", ["M. C. Escher", "Rembrandt", "Bosch", "Mondrian"], "M. C. Escher", "Relativité (1953) en est un exemple."),
  Q("Qu'est-ce qu'une figure impossible, comme le triangle de Penrose ?", ["Un dessin cohérent en apparence mais irréalisable en trois dimensions", "Une figure géométrique simple", "Une sculpture réelle", "Un dessin d'enfant"], "Un dessin cohérent en apparence mais irréalisable en trois dimensions", "Elle joue sur les conventions de la perspective."),
]),
notion('AR-2', 0, I, 'artr-hors-champ-suggere', [
  Q("Comment un artiste peut-il suggérer ce qui se trouve hors du cadre ?", ["Par des regards, des ombres ou des objets coupés par le bord", "Il ne peut pas", "En écrivant le texte", "En agrandissant le cadre"], "Par des regards, des ombres ou des objets coupés par le bord", "Le spectateur imagine la suite."),
  Q("Que crée un personnage qui regarde hors du tableau ?", ["Un espace imaginaire au-delà du cadre", "Une erreur", "Un trompe-l'œil", "Une symétrie"], "Un espace imaginaire au-delà du cadre", "Le cadre n'enferme pas tout."),
  Q("Quel photographe américain a cadré la vie urbaine avec des reflets et des cadres dans le cadre, comme Saul Leiter ?", ["Saul Leiter", "Ansel Adams", "Robert Capa", "Nadar"], "Saul Leiter", "Ses photos en couleur jouent sur les vitres et les reflets."),
]),
notion('AR-2', 0, D, 'artr-perspective-architecture', [
  Q("Quelle ville idéale peinte à la Renaissance montre une perspective parfaite sans personnages ?", ["La Cité idéale (Urbino)", "Le Jardin des délices", "La Tour de Babel", "Venise vue du Grand Canal"], "La Cité idéale (Urbino)", "Elle illustre la maîtrise de la perspective."),
  Q("Quel peintre vénitien a peint des vues précises de Venise (vedute) au XVIIIe siècle ?", ["Canaletto", "Titien", "Tintoret", "Véronèse"], "Canaletto", "Il aurait utilisé une chambre noire."),
  Q("Comment appelle-t-on une vue détaillée et fidèle d'une ville ?", ["Une veduta", "Une marine", "Une nature morte", "Une vanité"], "Une veduta", "Le pluriel est vedute."),
]),
# ══ AR-3 · La narration visuelle ══
notion('AR-3', 0, F, 'artr-bd-codes', [
  Q("Comment appelle-t-on une suite d'images de bande dessinée sur une ligne horizontale ?", ["Une bande (un strip)", "Un phylactère", "Une planche", "Un cadre"], "Une bande (un strip)", "Une planche est une page entière."),
  Q("Comment appelle-t-on une page complète de bande dessinée ?", ["Une planche", "Une vignette", "Une bulle", "Une case vide"], "Une planche", "Elle contient plusieurs bandes."),
  Q("Que sont les onomatopées dans une BD ?", ["Des mots qui imitent des bruits (Boum ! Paf !)", "Les noms des personnages", "Les titres", "Les dialogues"], "Des mots qui imitent des bruits (Boum ! Paf !)", "Elles rendent le son visible."),
]),
notion('AR-3', 0, F, 'artr-bd-celebres', [
  Q("Qui a créé Astérix avec René Goscinny ?", ["Albert Uderzo", "Hergé", "Morris", "Franquin"], "Albert Uderzo", "Le premier album paraît en 1961."),
  Q("Quel cow-boy de bande dessinée tire plus vite que son ombre ?", ["Lucky Luke", "Tintin", "Spirou", "Blueberry"], "Lucky Luke", "Créé par Morris en 1946."),
  Q("Quel petit garçon de BD a pour chien Milou ?", ["Tintin", "Spirou", "Boule", "Titeuf"], "Tintin", "Hergé l'a créé en 1929."),
]),
notion('AR-3', 0, F, 'artr-mouvement-image', [
  Q("Comment suggère-t-on le mouvement dans un dessin ?", ["Avec des traits de vitesse et des postures en déséquilibre", "Avec des aplats immobiles", "Avec un cadre doré", "On ne peut pas le suggérer"], "Avec des traits de vitesse et des postures en déséquilibre", "La BD utilise beaucoup ces codes."),
  Q("Qu'est-ce qu'un flip book (folioscope) ?", ["Un petit livre dont les images s'animent quand on fait défiler les pages", "Un livre de cuisine", "Un livre pliant", "Un album photo"], "Un petit livre dont les images s'animent quand on fait défiler les pages", "C'est l'ancêtre du dessin animé."),
  Q("Quel jouet optique du XIXe siècle fait tourner des images dans un cylindre ?", ["Le zootrope", "Le kaléidoscope", "Le télescope", "Le stéthoscope"], "Le zootrope", "On regarde par des fentes."),
]),
notion('AR-3', 0, F, 'artr-recit-sequence', [
  Q("Comment appelle-t-on une suite d'images qui raconte une histoire ?", ["Une séquence narrative", "Un portrait", "Une nature morte", "Un monochrome"], "Une séquence narrative", "La BD, le roman-photo, le cinéma…"),
  Q("Qu'est-ce qu'un roman-photo ?", ["Une histoire racontée avec des photographies et des bulles", "Un roman sans images", "Un album de vacances", "Un documentaire"], "Une histoire racontée avec des photographies et des bulles", "Il a été très populaire dans les années 1950-1970."),
  Q("Comment appelle-t-on l'espace blanc entre deux cases de BD ?", ["La gouttière (ou inter-case)", "La bulle", "Le récitatif", "Le phylactère"], "La gouttière (ou inter-case)", "Le lecteur imagine ce qui s'y passe."),
]),
notion('AR-3', 0, F, 'artr-tapisserie-bayeux', [
  Q("Quelle broderie de 70 mètres raconte la conquête de l'Angleterre en 1066 ?", ["La tapisserie de Bayeux", "La tapisserie de la Dame à la licorne", "Le retable de Gand", "La tapisserie de l'Apocalypse"], "La tapisserie de Bayeux", "On la compare à une bande dessinée."),
  Q("Pourquoi la tapisserie de Bayeux est-elle comparée à une BD ?", ["Elle raconte une histoire en scènes successives, avec du texte", "Elle a des bulles", "Elle est en couleur", "Elle est récente"], "Elle raconte une histoire en scènes successives, avec du texte", "Le texte est en latin."),
  Q("Quelle colonne romaine raconte en spirale les guerres de l'empereur Trajan ?", ["La colonne Trajane", "La colonne Vendôme", "L'obélisque", "La colonne de Juillet"], "La colonne Trajane", "Elle est à Rome."),
]),
notion('AR-3', 0, F, 'artr-cinema-anim', [
  Q("Quel studio américain a réalisé Blanche-Neige et les Sept Nains (1937) ?", ["Disney", "Pixar", "DreamWorks", "Ghibli"], "Disney", "C'est le premier long métrage d'animation en couleurs de Disney."),
  Q("Quel studio japonais a réalisé Le Voyage de Chihiro ?", ["Le studio Ghibli", "Disney", "Pixar", "Aardman"], "Le studio Ghibli", "Réalisé par Hayao Miyazaki en 2001."),
  Q("Quel personnage de pâte à modeler est le compagnon du chien Gromit ?", ["Wallace", "Shaun", "Mr Bean", "Pingu"], "Wallace", "Studio Aardman, en Angleterre."),
]),
notion('AR-3', 0, F, 'artr-photo-sequence', [
  Q("Quel photographe a décomposé le galop d'un cheval en une série de photos (1878) ?", ["Eadweard Muybridge", "Nadar", "Niépce", "Cartier-Bresson"], "Eadweard Muybridge", "Il prouve que le cheval décolle ses quatre sabots."),
  Q("Quel scientifique français a inventé la chronophotographie ?", ["Étienne-Jules Marey", "Louis Lumière", "Nicéphore Niépce", "Georges Méliès"], "Étienne-Jules Marey", "Il étudie le mouvement des corps."),
  Q("Qu'est-ce qu'une chronophotographie ?", ["Une série de photos décomposant un mouvement", "Une photo de montre", "Une photo très ancienne", "Une photo floue"], "Une série de photos décomposant un mouvement", "Elle annonce le cinéma."),
]),
notion('AR-3', 0, I, 'artr-futurisme-mouvement', [
  Q("Quel tableau de Marcel Duchamp (1912) décompose une figure qui descend des marches ?", ["Nu descendant un escalier n° 2", "La Fontaine", "Le Grand Verre", "La Roue de bicyclette"], "Nu descendant un escalier n° 2", "Il mêle cubisme et chronophotographie."),
  Q("Quel futuriste italien a peint Dynamisme d'un chien en laisse (1912) ?", ["Giacomo Balla", "Umberto Boccioni", "Marinetti", "Gino Severini"], "Giacomo Balla", "Les pattes du chien se multiplient."),
  Q("Quel sculpteur futuriste a réalisé Formes uniques de la continuité dans l'espace ?", ["Umberto Boccioni", "Giacometti", "Rodin", "Brancusi"], "Umberto Boccioni", "Elle figure sur la pièce italienne de 20 centimes."),
]),
notion('AR-3', 0, I, 'artr-temps-montage', [
  Q("Qu'est-ce qu'une ellipse dans un récit en images ?", ["Un saut dans le temps : on omet une partie de l'action", "Une forme ovale", "Un gros plan", "Un retour en arrière"], "Un saut dans le temps : on omet une partie de l'action", "Le lecteur reconstitue ce qui manque."),
  Q("Comment appelle-t-on un retour en arrière dans un récit ?", ["Un flash-back (analepse)", "Une ellipse", "Un travelling", "Un raccord"], "Un flash-back (analepse)", "Le flash-forward anticipe."),
  Q("Qu'est-ce que le ralenti ?", ["Une image où le temps semble s'écouler plus lentement", "Une panne de projecteur", "Un arrêt sur image", "Un fondu au noir"], "Une image où le temps semble s'écouler plus lentement", "Il dramatise l'action."),
]),
notion('AR-3', 0, I, 'artr-mangas', [
  Q("Dans quel sens se lit traditionnellement un manga japonais ?", ["De droite à gauche", "De gauche à droite", "De bas en haut", "En diagonale"], "De droite à gauche", "Les éditions françaises respectent souvent ce sens."),
  Q("Quel mangaka a créé Astro Boy et est surnommé « le dieu du manga » ?", ["Osamu Tezuka", "Akira Toriyama", "Hayao Miyazaki", "Eiichiro Oda"], "Osamu Tezuka", "Il a révolutionné le manga après 1945."),
  Q("Quel manga d'Akira Toriyama raconte les aventures de Son Goku ?", ["Dragon Ball", "One Piece", "Naruto", "Akira"], "Dragon Ball", "Il paraît à partir de 1984."),
]),
notion('AR-3', 0, I, 'artr-cinema-pionniers', [
  Q("Quel est le titre du célèbre premier film des frères Lumière montrant des ouvriers ?", ["La Sortie de l'usine Lumière à Lyon", "Le Voyage dans la Lune", "L'Arroseur arrosé", "Metropolis"], "La Sortie de l'usine Lumière à Lyon", "Projeté en 1895."),
  Q("Quel effet spécial Méliès a-t-il inventé par hasard ?", ["L'arrêt de caméra (substitution)", "Le numérique", "La 3D", "Le fond vert"], "L'arrêt de caméra (substitution)", "Un objet semble apparaître ou disparaître."),
  Q("Quel film muet de Fritz Lang (1927) imagine une ville futuriste ?", ["Metropolis", "Nosferatu", "Le Cabinet du docteur Caligari", "Les Temps modernes"], "Metropolis", "C'est un chef-d'œuvre de l'expressionnisme allemand."),
]),
notion('AR-3', 0, I, 'artr-hiroshige-sequence', [
  Q("Quelle série de Hiroshige représente les étapes d'une route japonaise ?", ["Les Cinquante-trois Stations du Tōkaidō", "Les Trente-six Vues du mont Fuji", "La Grande Vague", "Les Nymphéas"], "Les Cinquante-trois Stations du Tōkaidō", "C'est un récit de voyage en images."),
  Q("Qu'est-ce qu'une série en arts plastiques ?", ["Un ensemble d'œuvres liées par un même sujet ou principe", "Une seule œuvre", "Un feuilleton télévisé", "Un catalogue"], "Un ensemble d'œuvres liées par un même sujet ou principe", "Les Meules de Monet en sont une."),
  Q("Comment appelle-t-on le genre des estampes japonaises de l'époque d'Edo ?", ["L'ukiyo-e (images du monde flottant)", "Le manga", "Le haïku", "Le kabuki"], "L'ukiyo-e (images du monde flottant)", "Il a influencé le japonisme en Europe."),
]),
notion('AR-3', 0, I, 'artr-dessin-anime-techniques', [
  Q("Comment appelle-t-on les feuilles transparentes peintes utilisées autrefois pour les dessins animés ?", ["Les celluloïds (cellos)", "Les calques de couture", "Les vitraux", "Les pochoirs"], "Les celluloïds (cellos)", "On superposait personnages et décors."),
  Q("Qu'est-ce que la rotoscopie ?", ["Dessiner par-dessus des images filmées pour animer", "Faire tourner une caméra", "Coloriser un film", "Filmer en 3D"], "Dessiner par-dessus des images filmées pour animer", "Elle rend les mouvements très réalistes."),
  Q("Quel film d'animation de 1995 est le premier entièrement en images de synthèse ?", ["Toy Story", "Le Roi lion", "Shrek", "Wall-E"], "Toy Story", "Réalisé par Pixar."),
]),
notion('AR-3', 0, I, 'artr-narration-peinture-histoire', [
  Q("Comment raconter une histoire en une seule image, selon la peinture d'histoire ?", ["En choisissant le moment le plus significatif de l'action", "En peignant tout le récit", "En écrivant le texte", "En multipliant les cadres"], "En choisissant le moment le plus significatif de l'action", "On parle d'« instant prégnant »."),
  Q("Quel tableau de David représente le moment d'un serment prêté par trois frères ?", ["Le Serment des Horaces", "Le Sacre de Napoléon", "La Mort de Marat", "Les Sabines"], "Le Serment des Horaces", "Il date de 1784."),
  Q("Qu'est-ce qu'une représentation simultanée (narration continue) dans un tableau ?", ["Le même personnage apparaît plusieurs fois à différents moments", "Plusieurs tableaux côte à côte", "Un film", "Une BD"], "Le même personnage apparaît plusieurs fois à différents moments", "Fréquent dans l'art médiéval."),
]),
notion('AR-3', 0, D, 'artr-eisenstein-montage', [
  Q("Quel cinéaste soviétique a théorisé le montage dans Le Cuirassé Potemkine (1925) ?", ["Sergueï Eisenstein", "Fritz Lang", "Charlie Chaplin", "Jean Renoir"], "Sergueï Eisenstein", "La scène de l'escalier d'Odessa est célèbre."),
  Q("Qu'est-ce que l'« effet Koulechov » ?", ["Le sens d'une image change selon l'image qui la précède ou la suit", "Un effet spécial pyrotechnique", "Un ralenti", "Un type de caméra"], "Le sens d'une image change selon l'image qui la précède ou la suit", "Le montage crée du sens."),
  Q("Qu'est-ce qu'un plan-séquence ?", ["Une scène filmée en un seul plan, sans coupe", "Une série de photos", "Un montage rapide", "Un gros plan"], "Une scène filmée en un seul plan, sans coupe", "Il demande une grande préparation."),
]),
notion('AR-3', 0, D, 'artr-roman-graphique', [
  Q("Quel roman graphique d'Art Spiegelman raconte la Shoah avec des souris et des chats ?", ["Maus", "Persepolis", "Watchmen", "L'Arabe du futur"], "Maus", "Il reçoit le prix Pulitzer en 1992."),
  Q("Quelle autrice franco-iranienne a raconté son enfance en Iran dans un roman graphique ?", ["Marjane Satrapi (Persepolis)", "Riad Sattouf", "Claire Bretécher", "Pénélope Bagieu"], "Marjane Satrapi (Persepolis)", "Il a été adapté au cinéma en 2007."),
  Q("Qu'est-ce qu'un roman graphique ?", ["Une bande dessinée longue, souvent destinée aux adultes, au récit ambitieux", "Un roman sans images", "Un livre de coloriage", "Un manuel de dessin"], "Une bande dessinée longue, souvent destinée aux adultes, au récit ambitieux", "Le terme se répand dans les années 1980."),
]),
notion('AR-3', 0, D, 'artr-hogarth-narration', [
  Q("Quel peintre anglais du XVIIIe siècle a raconté des histoires morales en séries de tableaux et gravures ?", ["William Hogarth", "William Turner", "John Constable", "Thomas Gainsborough"], "William Hogarth", "La Carrière d'un roué (A Rake's Progress)."),
  Q("Quel dessinateur suisse est considéré comme l'inventeur de la bande dessinée vers 1830 ?", ["Rodolphe Töpffer", "Hergé", "Winsor McCay", "Christophe"], "Rodolphe Töpffer", "Il publie des « histoires en estampes »."),
  Q("Quel dessinateur américain a créé Little Nemo in Slumberland, aux mises en page inventives ?", ["Winsor McCay", "Walt Disney", "Charles Schulz", "Bill Watterson"], "Winsor McCay", "Il débute en 1905."),
]),
notion('AR-3', 0, D, 'artr-temps-reel-oeuvre', [
  Q("Quel artiste a filmé un homme dormant pendant plus de cinq heures (Sleep, 1963) ?", ["Andy Warhol", "Bill Viola", "Nam June Paik", "Christian Marclay"], "Andy Warhol", "La durée devient matériau."),
  Q("Quelle œuvre vidéo de Christian Marclay (2010) dure 24 heures et donne l'heure réelle ?", ["The Clock", "Empire", "Sleep", "TV Buddha"], "The Clock", "Elle assemble des milliers d'extraits de films."),
  Q("Quel artiste a peint des séries de nombres croissants pendant toute sa vie (Opalka) ?", ["Roman Opalka", "On Kawara", "Pierre Soulages", "Daniel Buren"], "Roman Opalka", "Il note le temps qui passe : 1 → ∞."),
]),
notion('AR-3', 0, D, 'artr-cinematographe-dispositifs', [
  Q("Quel inventeur américain a mis au point le kinétoscope, appareil de vision individuelle ?", ["Thomas Edison", "Louis Lumière", "Georges Méliès", "Émile Reynaud"], "Thomas Edison", "Le cinématographe Lumière permet, lui, la projection collective."),
  Q("Quel Français a présenté des « pantomimes lumineuses », ancêtres du dessin animé, en 1892 ?", ["Émile Reynaud", "Georges Méliès", "Étienne-Jules Marey", "Louis Daguerre"], "Émile Reynaud", "Avec son théâtre optique."),
  Q("Qu'est-ce que la persistance rétinienne, longtemps invoquée pour expliquer le cinéma ?", ["L'impression qu'une image reste un instant sur la rétine", "Une maladie de l'œil", "Un type de pellicule", "Un réglage de caméra"], "L'impression qu'une image reste un instant sur la rétine", "Les scientifiques parlent aujourd'hui plutôt d'effet phi."),
]),
notion('AR-3', 0, D, 'artr-street-art-recit', [
  Q("Quelle fresque monumentale de Diego Rivera raconte l'histoire du Mexique ?", ["Les fresques du Palais national de Mexico", "Guernica", "La Cène", "Les Nymphéas"], "Les fresques du Palais national de Mexico", "Le muralisme mexicain raconte l'histoire au peuple."),
  Q("Comment appelle-t-on le mouvement mexicain de grandes peintures murales politiques ?", ["Le muralisme", "Le surréalisme", "Le futurisme", "Le minimalisme"], "Le muralisme", "Avec Rivera, Orozco et Siqueiros."),
  Q("Quel artiste français colle des portraits géants sur les murs du monde entier ?", ["JR", "Banksy", "Invader", "Keith Haring"], "JR", "Il a fait « disparaître » la pyramide du Louvre en 2016."),
]),
notion('AR-3', 0, D, 'artr-jeux-video-narration', [
  Q("Comment appelle-t-on un récit dont le joueur fait les choix ?", ["Un récit interactif", "Un récit linéaire", "Une BD muette", "Un film muet"], "Un récit interactif", "Les jeux vidéo l'ont popularisé."),
  Q("Qu'est-ce qu'une cinématique dans un jeu vidéo ?", ["Une séquence non jouable qui fait avancer l'histoire", "Un niveau difficile", "Un bug", "Un menu"], "Une séquence non jouable qui fait avancer l'histoire", "On parle aussi de cut-scene."),
  Q("Quel musée de New York a intégré des jeux vidéo à ses collections en 2012 ?", ["Le MoMA", "Le Louvre", "La Tate Modern", "Le Prado"], "Le MoMA", "Pac-Man, Tetris…"),
]),
notion('AR-3', 0, D, 'artr-bayeux-trajane-comparaison', [
  Q("Quelle frise antique raconte la procession des Panathénées à Athènes ?", ["La frise du Parthénon", "La colonne Trajane", "La tapisserie de Bayeux", "L'arc de Titus"], "La frise du Parthénon", "Une partie est au British Museum."),
  Q("Quel peintre a raconté la vie de saint François en une série de fresques à Assise ?", ["Giotto", "Raphaël", "Michel-Ange", "Fra Angelico"], "Giotto", "Le récit se lit scène après scène."),
  Q("Comment appelle-t-on une bande décorative horizontale qui peut raconter une histoire ?", ["Une frise", "Une rosace", "Une colonne", "Un fronton vide"], "Une frise", "On la lit de gauche à droite."),
]),
# ══ AR-4 · L'autonomie de l'œuvre d'art ══
notion('AR-4', 0, F, 'artr-abstrait-formes', [
  Q("Qu'est-ce qu'une œuvre abstraite ?", ["Une œuvre qui ne représente pas d'objet reconnaissable", "Une œuvre très réaliste", "Un portrait", "Un paysage précis"], "Une œuvre qui ne représente pas d'objet reconnaissable", "Elle joue avec les formes, couleurs et matières."),
  Q("Qu'est-ce qu'un monochrome ?", ["Une œuvre d'une seule couleur", "Une œuvre en noir et blanc", "Une œuvre très colorée", "Un dessin au crayon"], "Une œuvre d'une seule couleur", "Yves Klein en a fait de célèbres en bleu."),
  Q("Quel artiste a breveté un bleu outremer intense qui porte son nom ?", ["Yves Klein", "Pierre Soulages", "Henri Matisse", "Piet Mondrian"], "Yves Klein", "L'IKB (International Klein Blue)."),
]),
notion('AR-4', 0, F, 'artr-pollock', [
  Q("Quel artiste américain projetait de la peinture sur des toiles posées au sol ?", ["Jackson Pollock", "Andy Warhol", "Mark Rothko", "Roy Lichtenstein"], "Jackson Pollock", "On parle de dripping."),
  Q("Comment appelle-t-on la technique de Pollock consistant à laisser couler la peinture ?", ["Le dripping", "Le pointillisme", "Le sfumato", "Le collage"], "Le dripping", "Drip = goutter."),
  Q("À quel mouvement appartient Jackson Pollock ?", ["L'expressionnisme abstrait", "Le pop art", "L'impressionnisme", "Le cubisme"], "L'expressionnisme abstrait", "Né à New York après 1945."),
]),
notion('AR-4', 0, F, 'artr-rothko', [
  Q("Quel peintre américain a peint de grands rectangles de couleur flottants ?", ["Mark Rothko", "Jackson Pollock", "Keith Haring", "Edward Hopper"], "Mark Rothko", "Il veut provoquer une émotion profonde."),
  Q("Que recherchait Rothko avec ses grandes surfaces colorées ?", ["Une expérience émotionnelle, presque spirituelle", "La ressemblance avec le réel", "Un effet comique", "Une illustration de livre"], "Une expérience émotionnelle, presque spirituelle", "La chapelle Rothko à Houston en témoigne."),
  Q("Comment appelle-t-on la peinture abstraite de grands champs de couleur ?", ["Le Color Field painting", "Le pointillisme", "Le cubisme", "Le réalisme"], "Le Color Field painting", "Rothko et Barnett Newman."),
]),
notion('AR-4', 0, F, 'artr-calder-mobiles', [
  Q("Quel artiste américain a inventé les mobiles, sculptures suspendues qui bougent ?", ["Alexander Calder", "Jean Tinguely", "Henry Moore", "Constantin Brancusi"], "Alexander Calder", "Marcel Duchamp leur a donné ce nom."),
  Q("Qu'est-ce qu'un stabile chez Calder ?", ["Une sculpture fixe, posée au sol", "Un mobile suspendu", "Un tableau", "Une installation sonore"], "Une sculpture fixe, posée au sol", "Le nom a été trouvé par Jean Arp."),
  Q("Qu'est-ce qui fait bouger un mobile de Calder ?", ["Les courants d'air", "Un moteur électrique toujours", "L'eau", "Un ressort"], "Les courants d'air", "Le mouvement est imprévisible."),
]),
notion('AR-4', 0, F, 'artr-art-cinetique', [
  Q("Comment appelle-t-on l'art fondé sur le mouvement réel ou l'illusion de mouvement ?", ["L'art cinétique", "L'art brut", "L'art naïf", "L'art conceptuel"], "L'art cinétique", "Vasarely en est une figure."),
  Q("Quel artiste franco-hongrois a créé des illusions d'optique géométriques (op art) ?", ["Victor Vasarely", "Pablo Picasso", "Joan Miró", "Fernand Léger"], "Victor Vasarely", "Il est le père de l'op art."),
  Q("Quel artiste suisse a construit des machines sculptures absurdes et bruyantes ?", ["Jean Tinguely", "Alberto Giacometti", "Paul Klee", "Le Corbusier"], "Jean Tinguely", "Il réalise la fontaine Stravinsky à Paris avec Niki de Saint Phalle."),
]),
notion('AR-4', 0, F, 'artr-titre-oeuvre', [
  Q("Que signifie « Sans titre » pour une œuvre ?", ["L'artiste laisse le spectateur libre de l'interpréter", "L'œuvre est perdue", "L'œuvre est inachevée", "L'œuvre est volée"], "L'artiste laisse le spectateur libre de l'interpréter", "C'est fréquent dans l'art abstrait."),
  Q("Comment appelle-t-on l'étiquette placée à côté d'une œuvre dans un musée ?", ["Le cartel", "Le cadre", "Le socle", "Le catalogue"], "Le cartel", "Il indique l'artiste, le titre, la date, la technique."),
  Q("Pourquoi Kandinsky intitule-t-il certaines œuvres « Composition » ou « Improvisation » ?", ["Pour rapprocher la peinture de la musique", "Parce qu'il n'avait pas d'idées", "Pour faire rire", "Pour indiquer leur prix"], "Pour rapprocher la peinture de la musique", "Les couleurs sont pour lui comme des sons."),
]),
notion('AR-4', 0, F, 'artr-miro-klee', [
  Q("Quel peintre catalan a créé un univers de signes colorés, d'étoiles et de lunes ?", ["Joan Miró", "Salvador Dalí", "Pablo Picasso", "Antoni Gaudí"], "Joan Miró", "Il est proche du surréalisme."),
  Q("Quel peintre suisse-allemand, professeur au Bauhaus, a peint des petits tableaux poétiques et colorés ?", ["Paul Klee", "Wassily Kandinsky", "Piet Mondrian", "Kasimir Malevitch"], "Paul Klee", "« L'art ne reproduit pas le visible, il rend visible »."),
  Q("Quel artiste a réalisé des papiers gouachés et découpés comme La Gerbe ou Icare ?", ["Henri Matisse", "Paul Klee", "Joan Miró", "Fernand Léger"], "Henri Matisse", "Il « dessine dans la couleur » avec des ciseaux."),
]),
notion('AR-4', 0, I, 'artr-musique-peinture', [
  Q("Quel peintre a affirmé que « la couleur est une touche, l'œil le marteau, l'âme le piano » ?", ["Wassily Kandinsky", "Claude Monet", "Pablo Picasso", "Paul Cézanne"], "Wassily Kandinsky", "Dans Du spirituel dans l'art (1911)."),
  Q("Qu'est-ce que la synesthésie, invoquée par Kandinsky ?", ["L'association de sensations différentes, comme voir des couleurs en entendant des sons", "Une technique de gravure", "Une maladie des yeux", "Un type de perspective"], "L'association de sensations différentes, comme voir des couleurs en entendant des sons", "Elle relie peinture et musique."),
  Q("Quel tableau de Mondrian s'inspire de la musique jazz de New York ?", ["Broadway Boogie-Woogie", "Composition en rouge, jaune et bleu", "L'Arbre gris", "Victory Boogie-Woogie"], "Broadway Boogie-Woogie", "Il date de 1942-1943."),
]),
notion('AR-4', 0, I, 'artr-geometrique-abstraction', [
  Q("Comment appelle-t-on l'abstraction fondée sur des formes géométriques et des aplats ?", ["L'abstraction géométrique", "L'abstraction lyrique", "Le tachisme", "L'informel"], "L'abstraction géométrique", "Mondrian et Malevitch en sont des représentants."),
  Q("Comment appelle-t-on l'abstraction fondée sur le geste et l'émotion ?", ["L'abstraction lyrique", "L'abstraction géométrique", "Le constructivisme", "Le minimalisme"], "L'abstraction lyrique", "Hans Hartung ou Georges Mathieu en France."),
  Q("Quel mouvement russe fondé par Malevitch réduit la peinture à des formes simples ?", ["Le suprématisme", "Le constructivisme", "Le futurisme", "Le fauvisme"], "Le suprématisme", "Le Carré noir (1915) en est l'icône."),
]),
notion('AR-4', 0, I, 'artr-de-stijl', [
  Q("Comment s'appelle le mouvement néerlandais de Mondrian, fondé en 1917 ?", ["De Stijl (le néoplasticisme)", "Le Bauhaus", "Le cubisme", "Le surréalisme"], "De Stijl (le néoplasticisme)", "Il influence l'architecture et le design."),
  Q("Quelles couleurs utilise principalement Mondrian ?", ["Les couleurs primaires, avec le noir, le blanc et le gris", "Toutes les couleurs de l'arc-en-ciel", "Uniquement le vert", "Des couleurs pastel"], "Les couleurs primaires, avec le noir, le blanc et le gris", "Rouge, jaune, bleu."),
  Q("Quel meuble de Gerrit Rietveld applique les principes de De Stijl ?", ["La chaise rouge et bleue", "La chaise Louis XV", "Le fauteuil club", "Le tabouret Tam Tam"], "La chaise rouge et bleue", "Elle date de 1918-1923."),
]),
notion('AR-4', 0, I, 'artr-sonia-delaunay', [
  Q("Quelle artiste a créé l'orphisme avec Robert Delaunay, jouant des contrastes de couleurs en cercles ?", ["Sonia Delaunay", "Frida Kahlo", "Niki de Saint Phalle", "Louise Bourgeois"], "Sonia Delaunay", "Elle applique aussi ses motifs à la mode et aux tissus."),
  Q("Quelle peintre suédoise, redécouverte récemment, a peint des toiles abstraites avant Kandinsky ?", ["Hilma af Klint", "Sonia Delaunay", "Georgia O'Keeffe", "Tamara de Lempicka"], "Hilma af Klint", "Dès 1906."),
  Q("Comment appelle-t-on le contraste entre deux couleurs opposées sur le cercle chromatique ?", ["Le contraste de complémentaires", "Le camaïeu", "La monochromie", "Le dégradé"], "Le contraste de complémentaires", "Rouge/vert, bleu/orange, jaune/violet."),
]),
notion('AR-4', 0, I, 'artr-hors-du-cadre', [
  Q("Quel artiste italien a lacéré ses toiles monochromes pour ouvrir l'espace ?", ["Lucio Fontana", "Alberto Burri", "Piero Manzoni", "Giorgio Morandi"], "Lucio Fontana", "Ce sont les Concetti spaziali (concepts spatiaux)."),
  Q("Quel mouvement français des années 1960 questionne le châssis et la toile, avec Claude Viallat ?", ["Supports/Surfaces", "Le nouveau réalisme", "La figuration libre", "Le cubisme"], "Supports/Surfaces", "La toile est libérée du châssis."),
  Q("Pourquoi certains artistes sortent-ils la peinture du cadre ?", ["Pour interroger ce qui fait une œuvre et son rapport à l'espace", "Par manque de cadres", "Pour la vendre plus cher", "Pour la protéger"], "Pour interroger ce qui fait une œuvre et son rapport à l'espace", "La toile devient un objet."),
]),
notion('AR-4', 0, I, 'artr-noir-soulages', [
  Q("Dans quelle ville se trouve le musée Soulages ?", ["Rodez", "Paris", "Lyon", "Montpellier"], "Rodez", "Le peintre y est né en 1919."),
  Q("Qu'est-ce que l'« outrenoir » pour Soulages ?", ["Une lumière reflétée par la matière noire travaillée", "Un noir très profond sans relief", "Un bleu nuit", "Une absence de peinture"], "Une lumière reflétée par la matière noire travaillée", "Le noir y devient lumière."),
  Q("Pour quel monument Soulages a-t-il créé des vitraux ?", ["L'abbatiale de Conques", "Notre-Dame de Paris", "La Sainte-Chapelle", "La cathédrale de Chartres"], "L'abbatiale de Conques", "104 vitraux, posés entre 1987 et 1994."),
]),
notion('AR-4', 0, I, 'artr-arbre-mondrian', [
  Q("Comment Mondrian est-il passé de la figuration à l'abstraction ?", ["En simplifiant progressivement un même motif, comme un arbre", "Du jour au lendemain", "En copiant Picasso", "En arrêtant de peindre"], "En simplifiant progressivement un même motif, comme un arbre", "La série des Arbres le montre (1908-1913)."),
  Q("Comment appelle-t-on le fait de réduire une forme à l'essentiel ?", ["La simplification (stylisation)", "La complication", "Le trompe-l'œil", "L'agrandissement"], "La simplification (stylisation)", "Elle mène parfois à l'abstraction."),
  Q("Quel artiste a simplifié la forme d'un oiseau dans L'Oiseau dans l'espace ?", ["Constantin Brancusi", "Auguste Rodin", "Alberto Giacometti", "Henry Moore"], "Constantin Brancusi", "Une sculpture lisse et élancée."),
]),
notion('AR-4', 0, D, 'artr-greenberg-modernisme', [
  Q("Quel critique américain a défendu une peinture qui affirme sa planéité et ses propres moyens ?", ["Clement Greenberg", "Harold Rosenberg", "Leo Steinberg", "Arthur Danto"], "Clement Greenberg", "Il soutient l'expressionnisme abstrait."),
  Q("Que signifie « l'art pour l'art » ?", ["L'art n'a pas d'autre but que lui-même", "L'art doit servir la politique", "L'art doit enseigner la morale", "L'art doit être utile"], "L'art n'a pas d'autre but que lui-même", "La formule est associée à Théophile Gautier."),
  Q("Quel peintre déclara en 1890 qu'un tableau est « une surface plane recouverte de couleurs en un certain ordre assemblées » ?", ["Maurice Denis", "Paul Gauguin", "Claude Monet", "Paul Cézanne"], "Maurice Denis", "Une phrase fondatrice de la modernité."),
]),
notion('AR-4', 0, D, 'artr-minimalisme', [
  Q("Quel mouvement américain des années 1960 réduit l'œuvre à des formes simples et industrielles ?", ["L'art minimal", "Le pop art", "L'expressionnisme abstrait", "Le surréalisme"], "L'art minimal", "Donald Judd, Carl Andre, Dan Flavin."),
  Q("Quel artiste minimaliste utilise des tubes de néon fluorescents ?", ["Dan Flavin", "Donald Judd", "Carl Andre", "Sol LeWitt"], "Dan Flavin", "La lumière devient matériau."),
  Q("Quelle formule résume l'esprit minimaliste ?", ["« Less is more »", "« Plus c'est mieux »", "« Art is life »", "« Just do it »"], "« Less is more »", "Elle est attribuée à l'architecte Mies van der Rohe."),
]),
notion('AR-4', 0, D, 'artr-art-conceptuel', [
  Q("Quel mouvement affirme que l'idée de l'œuvre compte plus que sa réalisation ?", ["L'art conceptuel", "L'art naïf", "L'impressionnisme", "Le baroque"], "L'art conceptuel", "Il se développe dans les années 1960."),
  Q("Quelle œuvre de Joseph Kosuth présente une chaise, sa photo et sa définition ?", ["One and Three Chairs", "Fountain", "Le Grand Verre", "Les Demoiselles d'Avignon"], "One and Three Chairs", "Elle date de 1965."),
  Q("Quel artiste américain a créé des « wall drawings » réalisés par d'autres selon ses instructions ?", ["Sol LeWitt", "Jackson Pollock", "Andy Warhol", "Keith Haring"], "Sol LeWitt", "L'idée devient « une machine qui fabrique l'art »."),
]),
notion('AR-4', 0, D, 'artr-malevitch-icone', [
  Q("Comment Malevitch a-t-il accroché son Carré noir lors de l'exposition 0,10 en 1915 ?", ["Dans l'angle supérieur de la pièce, à la place traditionnelle des icônes", "Au sol", "Au plafond au centre", "Dans un coffre"], "Dans l'angle supérieur de la pièce, à la place traditionnelle des icônes", "Il en fait une icône moderne."),
  Q("Que signifie « suprématisme » pour Malevitch ?", ["La suprématie de la sensation pure dans l'art", "La supériorité d'un peuple", "La domination d'un style ancien", "Une technique de sculpture"], "La suprématie de la sensation pure dans l'art", "L'art est libéré de l'objet."),
  Q("Quel mouvement russe veut mettre l'art au service de la société et de l'industrie ?", ["Le constructivisme", "Le suprématisme", "L'impressionnisme", "Le fauvisme"], "Le constructivisme", "Avec Tatline et Rodtchenko."),
]),
notion('AR-4', 0, D, 'artr-informel-matiere', [
  Q("Quel mouvement français d'après-guerre privilégie la matière et le geste sans forme définie ?", ["L'art informel", "L'art minimal", "Le néoplasticisme", "Le pop art"], "L'art informel", "Jean Fautrier et Wols en sont des figures."),
  Q("Comment appelle-t-on la peinture par taches spontanées de l'après-guerre en France ?", ["Le tachisme", "Le pointillisme", "Le cubisme", "Le réalisme"], "Le tachisme", "Proche de l'abstraction lyrique."),
  Q("Quel peintre français est célèbre pour ses performances de peinture rapide devant le public ?", ["Georges Mathieu", "Pierre Soulages", "Jean Dubuffet", "Yves Klein"], "Georges Mathieu", "Il a aussi dessiné une pièce de 10 francs."),
]),
notion('AR-4', 0, D, 'artr-ready-made-autonomie', [
  Q("Quelle œuvre de Duchamp (1917) est un urinoir signé « R. Mutt » ?", ["Fontaine", "La Roue de bicyclette", "L.H.O.O.Q.", "Le Grand Verre"], "Fontaine", "Elle a été refusée à une exposition."),
  Q("Qu'est-ce qu'un ready-made ?", ["Un objet manufacturé choisi et exposé comme œuvre d'art", "Une sculpture en bronze", "Une peinture inachevée", "Un dessin préparatoire"], "Un objet manufacturé choisi et exposé comme œuvre d'art", "C'est le choix de l'artiste qui fait l'œuvre."),
  Q("Que conteste Duchamp avec ses ready-mades ?", ["L'idée que l'art doit être fait de la main de l'artiste et être beau", "La photographie", "La couleur", "Les musées gratuits"], "L'idée que l'art doit être fait de la main de l'artiste et être beau", "Il ouvre la voie à l'art conceptuel."),
]),
notion('AR-4', 0, D, 'artr-art-concret-fr', [
  Q("Quel artiste a peint en noir et blanc des toiles cinétiques jouant sur des bandes ?", ["Bridget Riley", "Sonia Delaunay", "Mark Rothko", "Frank Stella"], "Bridget Riley", "Une figure britannique de l'op art."),
  Q("Quel artiste français installe des bandes verticales alternées de 8,7 cm in situ ?", ["Daniel Buren", "François Morellet", "Pierre Soulages", "Yves Klein"], "Daniel Buren", "Les Deux Plateaux au Palais-Royal (1986)."),
  Q("Quel artiste français utilise néons et règles mathématiques pour composer ses œuvres ?", ["François Morellet", "Daniel Buren", "Christian Boltanski", "Jean Dubuffet"], "François Morellet", "Il aime l'humour et le hasard."),
]),
notion('AR-4', 0, D, 'artr-frank-stella-shaped', [
  Q("Quel peintre américain a fait sortir la toile du rectangle avec des « shaped canvases » ?", ["Frank Stella", "Mark Rothko", "Jasper Johns", "Robert Rauschenberg"], "Frank Stella", "Le format suit le motif."),
  Q("Quelle phrase de Frank Stella résume l'autonomie de la peinture ?", ["« What you see is what you see »", "« Less is more »", "« Art is life »", "« Ceci n'est pas une pipe »"], "« What you see is what you see »", "Il refuse toute illusion."),
  Q("Quel peintre américain a peint des drapeaux et des cibles, entre objet et image ?", ["Jasper Johns", "Andy Warhol", "Roy Lichtenstein", "Mark Rothko"], "Jasper Johns", "Flag (1954-1955)."),
]),
notion('AR-4', 0, I, 'artr-collage-papier', [
  Q("Quels artistes ont introduit le papier collé dans la peinture en 1912 ?", ["Braque et Picasso", "Monet et Renoir", "Matisse et Derain", "Kandinsky et Klee"], "Braque et Picasso", "Le réel entre dans le tableau."),
  Q("Qu'est-ce qu'un collage ?", ["Une œuvre faite d'éléments découpés et assemblés sur un support", "Une sculpture fondue", "Une peinture à l'huile", "Un dessin au fusain"], "Une œuvre faite d'éléments découpés et assemblés sur un support", "Journaux, papiers peints, photos…"),
  Q("Quel artiste dadaïste allemand a créé des collages avec des déchets, appelés « Merz » ?", ["Kurt Schwitters", "Max Ernst", "Hans Arp", "Hannah Höch"], "Kurt Schwitters", "Il construit aussi des installations."),
]),
# ══ AR-5 · La création, la matérialité, le statut, la signification des images ══
notion('AR-5', 0, F, 'artr-affiche', [
  Q("Quel artiste tchèque est célèbre pour ses affiches Art nouveau, notamment pour Sarah Bernhardt ?", ["Alfons Mucha", "Toulouse-Lautrec", "Andy Warhol", "Cassandre"], "Alfons Mucha", "Arabesques et femmes aux longs cheveux."),
  Q("À quoi sert une affiche ?", ["À transmettre rapidement un message visible de loin", "À décorer un musée", "À illustrer un roman", "À remplacer un tableau"], "À transmettre rapidement un message visible de loin", "Image et texte s'y combinent."),
  Q("Qu'est-ce qu'un logo ?", ["Un signe graphique qui représente une marque ou une institution", "Une photo de famille", "Un paysage", "Un tableau ancien"], "Un signe graphique qui représente une marque ou une institution", "Il doit être simple et reconnaissable."),
]),
notion('AR-5', 0, F, 'artr-pictogrammes', [
  Q("Qu'est-ce qu'un pictogramme ?", ["Un dessin simplifié qui transmet une information sans mots", "Un tableau abstrait", "Une photographie", "Une signature"], "Un dessin simplifié qui transmet une information sans mots", "Les panneaux de signalisation en utilisent."),
  Q("Quel avantage présentent les pictogrammes dans les aéroports ?", ["Ils sont compris quelle que soit la langue", "Ils sont plus jolis", "Ils sont plus grands", "Ils sont moins chers"], "Ils sont compris quelle que soit la langue", "Ils sont universels."),
  Q("Quelle écriture ancienne utilisait des signes-images ?", ["Les hiéroglyphes égyptiens", "L'alphabet latin", "Le braille", "Le morse"], "Les hiéroglyphes égyptiens", "Champollion les a déchiffrés en 1822."),
]),
notion('AR-5', 0, F, 'artr-image-fixe-animee', [
  Q("Quelle différence y a-t-il entre une image fixe et une image animée ?", ["L'image animée montre un mouvement dans le temps", "L'image fixe est toujours en couleur", "L'image animée est toujours une photo", "Il n'y en a pas"], "L'image animée montre un mouvement dans le temps", "Cinéma, vidéo, animation…"),
  Q("Laquelle de ces images est une image fixe ?", ["Une photographie", "Un film", "Un GIF animé", "Un dessin animé"], "Une photographie", "Comme un tableau ou une affiche."),
  Q("Qu'est-ce qu'une image d'illustration ?", ["Une image qui accompagne et éclaire un texte", "Une image abstraite", "Une image en mouvement", "Une image floue"], "Une image qui accompagne et éclaire un texte", "Dans un livre ou un journal."),
]),
notion('AR-5', 0, F, 'artr-gravure', [
  Q("Qu'est-ce qu'une estampe ?", ["Une image imprimée à partir d'une matrice gravée", "Une peinture à l'huile", "Une photo", "Une sculpture"], "Une image imprimée à partir d'une matrice gravée", "Elle peut être tirée en plusieurs exemplaires."),
  Q("Comment appelle-t-on la gravure sur bois ?", ["La xylogravure", "La lithographie", "La sérigraphie", "La photogravure"], "La xylogravure", "Du grec xylon, le bois."),
  Q("Quel peintre allemand de la Renaissance est célèbre pour ses gravures, comme Melencolia I ?", ["Albrecht Dürer", "Hans Holbein", "Lucas Cranach", "Rembrandt"], "Albrecht Dürer", "Il a aussi gravé un rhinocéros célèbre."),
]),
notion('AR-5', 0, F, 'artr-image-propagande', [
  Q("Qu'est-ce qu'une image de propagande ?", ["Une image qui cherche à influencer l'opinion au service d'un pouvoir", "Une image de vacances", "Une image scientifique", "Un dessin d'enfant"], "Une image qui cherche à influencer l'opinion au service d'un pouvoir", "Les régimes totalitaires en ont beaucoup produit."),
  Q("Pourquoi faut-il analyser les images qui nous entourent ?", ["Pour comprendre leurs intentions et ne pas être manipulé", "Pour les collectionner", "Pour les effacer", "Ce n'est pas utile"], "Pour comprendre leurs intentions et ne pas être manipulé", "C'est l'éducation aux médias."),
  Q("Qu'est-ce qu'une image publicitaire ?", ["Une image conçue pour donner envie d'acheter", "Une image d'archive", "Une œuvre de musée", "Un dessin technique"], "Une image conçue pour donner envie d'acheter", "Elle utilise des codes précis."),
]),
notion('AR-5', 0, I, 'artr-statut-image', [
  Q("Une même image peut-elle avoir plusieurs statuts (œuvre, document, publicité) ?", ["Oui, selon le contexte et l'usage", "Non, jamais", "Seulement les photos", "Seulement les peintures"], "Oui, selon le contexte et l'usage", "La Joconde est une œuvre, mais aussi une image publicitaire."),
  Q("Quel artiste a détourné La Joconde en lui ajoutant moustache et barbiche (L.H.O.O.Q.) ?", ["Marcel Duchamp", "Andy Warhol", "Salvador Dalí", "Banksy"], "Marcel Duchamp", "C'est un détournement de 1919."),
  Q("Qu'est-ce qu'un détournement d'image ?", ["La modification d'une image connue pour lui donner un autre sens", "La destruction d'une image", "La copie exacte", "Le vol d'une image"], "La modification d'une image connue pour lui donner un autre sens", "Il est souvent humoristique ou critique."),
]),
notion('AR-5', 0, I, 'artr-icones-religieuses', [
  Q("Qu'est-ce qu'une icône dans l'art orthodoxe ?", ["Une image sacrée peinte sur bois, objet de vénération", "Un logo informatique", "Une sculpture", "Un vitrail"], "Une image sacrée peinte sur bois, objet de vénération", "Elle suit des règles très codifiées."),
  Q("Quel conflit au VIIIe siècle a opposé partisans et adversaires des images religieuses à Byzance ?", ["La querelle des images (iconoclasme)", "La guerre de Cent Ans", "La Réforme", "Les croisades"], "La querelle des images (iconoclasme)", "Iconoclaste = briseur d'images."),
  Q("Quel peintre russe est célèbre pour son icône de la Trinité (vers 1411) ?", ["Andreï Roublev", "Kasimir Malevitch", "Wassily Kandinsky", "Ilia Répine"], "Andreï Roublev", "Elle est conservée à Moscou."),
]),
notion('AR-5', 0, I, 'artr-photo-documentaire', [
  Q("Quel photographe américain a documenté la Grande Dépression, dont Migrant Mother ?", ["Dorothea Lange", "Robert Capa", "Ansel Adams", "Man Ray"], "Dorothea Lange", "La photo est prise en 1936."),
  Q("Quel photographe a documenté les conditions de vie à Paris, comme Robert Doisneau ?", ["Robert Doisneau (Le Baiser de l'Hôtel de Ville)", "Man Ray", "Nadar", "Atget"], "Robert Doisneau (Le Baiser de l'Hôtel de Ville)", "La photo date de 1950 et était mise en scène."),
  Q("Une photographie est-elle toujours une preuve objective du réel ?", ["Non, elle résulte de choix (cadrage, moment, mise en scène)", "Oui, toujours", "Seulement en noir et blanc", "Seulement si elle est floue"], "Non, elle résulte de choix (cadrage, moment, mise en scène)", "Il faut l'analyser."),
]),
notion('AR-5', 0, I, 'artr-man-ray-photo-art', [
  Q("Quel photographe surréaliste a inventé les « rayographies », images sans appareil ?", ["Man Ray", "Henri Cartier-Bresson", "Brassaï", "Robert Doisneau"], "Man Ray", "Il pose des objets directement sur le papier photo."),
  Q("Qu'est-ce qu'un photogramme ?", ["Une image obtenue en posant des objets sur du papier sensible exposé à la lumière", "Une photo numérique", "Un cadre photo", "Une pellicule de cinéma"], "Une image obtenue en posant des objets sur du papier sensible exposé à la lumière", "On peut en faire en classe avec du papier cyanotype."),
  Q("Quel photographe portraitiste du XIXe siècle a photographié Victor Hugo et Baudelaire ?", ["Nadar", "Daguerre", "Niépce", "Atget"], "Nadar", "Il a aussi photographié Paris en ballon."),
]),
notion('AR-5', 0, I, 'artr-pop-art-images', [
  Q("Quel artiste britannique est considéré comme l'un des pionniers du pop art avec un collage de 1956 ?", ["Richard Hamilton", "David Hockney", "Banksy", "Francis Bacon"], "Richard Hamilton", "Just what is it that makes today's homes so different, so appealing?"),
  Q("D'où viennent souvent les images utilisées par le pop art ?", ["De la publicité, des magazines, des BD et de la télévision", "Des musées anciens", "De la Bible", "Des rêves"], "De la publicité, des magazines, des BD et de la télévision", "La culture populaire entre au musée."),
  Q("Pourquoi Warhol répète-t-il les mêmes images en série ?", ["Pour évoquer la production de masse et la société de consommation", "Par manque d'idées", "Pour économiser la peinture", "Pour tromper les collectionneurs"], "Pour évoquer la production de masse et la société de consommation", "Son atelier s'appelait la Factory."),
]),
notion('AR-5', 0, I, 'artr-images-scientifiques', [
  Q("Quel naturaliste a peint avec précision les oiseaux d'Amérique au XIXe siècle ?", ["John James Audubon", "Charles Darwin", "Albrecht Dürer", "Buffon"], "John James Audubon", "The Birds of America."),
  Q("Quel artiste de la Renaissance a réalisé des planches anatomiques à partir de dissections ?", ["Léonard de Vinci", "Raphaël", "Botticelli", "Michel-Ange"], "Léonard de Vinci", "Elles sont restées longtemps inconnues."),
  Q("Une image scientifique peut-elle devenir une œuvre d'art ?", ["Oui, selon son regard et son contexte d'exposition", "Non, jamais", "Seulement si elle est peinte", "Seulement si elle est floue"], "Oui, selon son regard et son contexte d'exposition", "Le statut de l'image peut changer."),
]),
notion('AR-5', 0, I, 'artr-serigraphie-multiple', [
  Q("Qu'est-ce qu'un multiple en art ?", ["Une œuvre produite en plusieurs exemplaires identiques", "Une œuvre unique", "Un tableau en plusieurs couleurs", "Une sculpture géante"], "Une œuvre produite en plusieurs exemplaires identiques", "Gravures, sérigraphies, photographies…"),
  Q("Quel penseur allemand a analysé l'œuvre d'art « à l'époque de sa reproductibilité technique » (1935) ?", ["Walter Benjamin", "Karl Marx", "Friedrich Nietzsche", "Theodor Adorno"], "Walter Benjamin", "Selon lui, l'œuvre reproduite perd son « aura »."),
  Q("Qu'est-ce que l'« aura » d'une œuvre selon Walter Benjamin ?", ["Son caractère unique, ici et maintenant", "Son cadre doré", "Sa couleur dominante", "Son prix"], "Son caractère unique, ici et maintenant", "La reproduction la transforme."),
]),
notion('AR-5', 0, D, 'artr-iconographie', [
  Q("Qu'est-ce que l'iconographie ?", ["L'étude des sujets, symboles et attributs représentés dans les images", "La fabrication d'icônes", "La restauration des tableaux", "Un style de peinture"], "L'étude des sujets, symboles et attributs représentés dans les images", "Elle aide à identifier un saint, un dieu, une allégorie."),
  Q("Quel historien de l'art a théorisé l'iconologie, lecture en plusieurs niveaux du sens d'une image ?", ["Erwin Panofsky", "Giorgio Vasari", "Ernst Gombrich", "Daniel Arasse"], "Erwin Panofsky", "Essais d'iconologie (1939)."),
  Q("Quel attribut permet d'identifier saint Pierre dans une œuvre ?", ["Les clés", "Une roue", "Une flèche", "Un agneau"], "Les clés", "Les clés du Paradis."),
]),
notion('AR-5', 0, D, 'artr-allegorie', [
  Q("Qu'est-ce qu'une allégorie ?", ["La représentation d'une idée abstraite sous une forme concrète", "Un portrait réaliste", "Une nature morte", "Une caricature"], "La représentation d'une idée abstraite sous une forme concrète", "La Justice avec sa balance et son glaive."),
  Q("Quelle allégorie représente la République française ?", ["Marianne", "Britannia", "Germania", "Columbia"], "Marianne", "Britannia représente le Royaume-Uni."),
  Q("Que symbolise le bandeau sur les yeux de la Justice ?", ["L'impartialité", "La cécité", "La tristesse", "Le sommeil"], "L'impartialité", "Elle juge sans regarder qui est jugé."),
]),
notion('AR-5', 0, D, 'artr-image-sacre-politique', [
  Q("Quel tableau de David met en scène le couronnement de Joséphine par Napoléon ?", ["Le Sacre de Napoléon", "Bonaparte franchissant le Grand-Saint-Bernard", "La Mort de Marat", "Le Serment des Horaces"], "Le Sacre de Napoléon", "Il est immense : près de 10 m de large."),
  Q("Pourquoi David a-t-il peint Bonaparte calme sur un cheval cabré au col du Grand-Saint-Bernard ?", ["Pour construire une image héroïque, alors qu'il avait traversé à dos de mulet", "Parce que c'était la réalité exacte", "Pour se moquer de lui", "Par erreur"], "Pour construire une image héroïque, alors qu'il avait traversé à dos de mulet", "C'est une image de propagande."),
  Q("Quel peintre a représenté Bonaparte sur un mulet, de manière plus réaliste, en 1850 ?", ["Paul Delaroche", "Jacques-Louis David", "Ingres", "Gros"], "Paul Delaroche", "La comparaison des deux tableaux est éclairante."),
]),
notion('AR-5', 0, D, 'artr-photo-manipulation-histoire', [
  Q("Quel dirigeant soviétique faisait effacer de certaines photos les opposants disgraciés ?", ["Staline", "Lénine", "Gorbatchev", "Khrouchtchev"], "Staline", "La retouche existait bien avant le numérique."),
  Q("Quelle célèbre photo de la guerre d'Espagne de Robert Capa fait l'objet de débats sur sa mise en scène ?", ["Mort d'un soldat républicain", "Le Baiser de l'Hôtel de Ville", "Migrant Mother", "La Petite Fille au napalm"], "Mort d'un soldat républicain", "Sa spontanéité est contestée."),
  Q("Quelle photo de 1945 montre des soldats américains plantant un drapeau à Iwo Jima ?", ["Raising the Flag on Iwo Jima (Joe Rosenthal)", "Le Baiser à Times Square", "Migrant Mother", "Tank Man"], "Raising the Flag on Iwo Jima (Joe Rosenthal)", "La scène a été rejouée pour une meilleure photo."),
]),
notion('AR-5', 0, D, 'artr-images-mediatiques', [
  Q("Quelle photo de 1989 montre un homme seul face à une colonne de chars à Pékin ?", ["Tank Man (place Tian'anmen)", "Migrant Mother", "Le Baiser de l'Hôtel de Ville", "Earthrise"], "Tank Man (place Tian'anmen)", "L'homme n'a jamais été identifié."),
  Q("Quelle photo de la NASA (1968) montre la Terre se levant au-dessus de la Lune ?", ["Earthrise", "Pale Blue Dot", "The Blue Marble", "Pillars of Creation"], "Earthrise", "Elle a influencé le mouvement écologiste."),
  Q("Pourquoi certaines photos deviennent-elles des « icônes » médiatiques ?", ["Elles résument un événement et sont reproduites massivement", "Elles sont peintes", "Elles sont très anciennes", "Elles sont en couleur"], "Elles résument un événement et sont reproduites massivement", "Elles deviennent des symboles."),
]),
notion('AR-5', 0, D, 'artr-image-texte', [
  Q("Quel artiste américaine projette ou affiche des phrases provocantes (Truisms) dans l'espace public ?", ["Jenny Holzer", "Barbara Kruger", "Cindy Sherman", "Kara Walker"], "Jenny Holzer", "Le texte devient image."),
  Q("Quelle artiste américaine associe photos en noir et blanc et slogans en lettres blanches sur fond rouge ?", ["Barbara Kruger", "Jenny Holzer", "Annie Leibovitz", "Louise Bourgeois"], "Barbara Kruger", "« I shop therefore I am »."),
  Q("Qu'est-ce qu'un calligramme ?", ["Un poème dont les mots dessinent une forme", "Une écriture chinoise", "Un graffiti", "Une enluminure"], "Un poème dont les mots dessinent une forme", "Apollinaire en a écrit de célèbres."),
]),
notion('AR-5', 0, I, 'artr-enluminure', [
  Q("Qu'est-ce qu'une enluminure ?", ["Une peinture décorant un manuscrit", "Une lampe", "Un vitrail", "Une sculpture"], "Une peinture décorant un manuscrit", "Elle peut être rehaussée d'or."),
  Q("Quel manuscrit enluminé du XVe siècle représente les travaux des mois ?", ["Les Très Riches Heures du duc de Berry", "Le Livre de Kells", "La Bible de Gutenberg", "Le Codex Mendoza"], "Les Très Riches Heures du duc de Berry", "Il est conservé à Chantilly."),
  Q("Comment appelle-t-on une grande lettre décorée au début d'un texte ?", ["Une lettrine", "Une majuscule simple", "Un logo", "Un calligramme"], "Une lettrine", "Elle est fréquente dans les manuscrits médiévaux."),
]),
# ══ AR-6 · L'œuvre à l'ère du numérique ══
notion('AR-6', 0, F, 'artr-pixel', [
  Q("Qu'est-ce qu'un pixel ?", ["Le plus petit point d'une image numérique", "Un logiciel", "Un appareil photo", "Une couleur"], "Le plus petit point d'une image numérique", "Picture element."),
  Q("Que se passe-t-il quand on agrandit beaucoup une image numérique de basse résolution ?", ["Elle devient pixelisée (on voit les carrés)", "Elle devient plus nette", "Elle change de couleur", "Elle disparaît"], "Elle devient pixelisée (on voit les carrés)", "La résolution compte."),
  Q("Quel artiste français colle des mosaïques inspirées des jeux vidéo dans les villes ?", ["Invader", "JR", "Banksy", "Miss Tic"], "Invader", "Il s'inspire de Space Invaders."),
]),
notion('AR-6', 0, F, 'artr-outils-numeriques', [
  Q("Quel outil permet de dessiner directement sur un écran ou une tablette ?", ["Un stylet", "Un pinceau à huile", "Un burin", "Une craie grasse"], "Un stylet", "On dessine avec une tablette graphique."),
  Q("Que permet un logiciel de retouche d'image ?", ["Modifier couleurs, cadrage et éléments d'une image", "Imprimer en 3D", "Envoyer un e-mail", "Écouter de la musique"], "Modifier couleurs, cadrage et éléments d'une image", "Photoshop ou GIMP par exemple."),
  Q("Qu'est-ce qu'un calque dans un logiciel de dessin ?", ["Une couche indépendante qu'on peut superposer et modifier", "Un papier transparent réel", "Une erreur", "Un fichier son"], "Une couche indépendante qu'on peut superposer et modifier", "On travaille comme avec des feuilles transparentes."),
]),
notion('AR-6', 0, F, 'artr-photo-numerique', [
  Q("Quelle différence principale y a-t-il entre la photo argentique et la photo numérique ?", ["L'argentique utilise une pellicule, le numérique un capteur électronique", "Le numérique est toujours en noir et blanc", "L'argentique est plus récente", "Il n'y en a pas"], "L'argentique utilise une pellicule, le numérique un capteur électronique", "Le numérique s'impose dans les années 2000."),
  Q("Qu'est-ce qu'un filtre sur un réseau social ?", ["Un effet appliqué automatiquement à une photo", "Un mot de passe", "Un virus", "Un appareil photo"], "Un effet appliqué automatiquement à une photo", "Il modifie l'apparence de la réalité."),
  Q("Pourquoi les filtres peuvent-ils poser problème ?", ["Ils diffusent des images idéalisées et irréalistes du corps", "Ils effacent les photos", "Ils sont payants", "Ils abîment le téléphone"], "Ils diffusent des images idéalisées et irréalistes du corps", "Il faut garder un regard critique."),
]),
notion('AR-6', 0, F, 'artr-diffusion-numerique', [
  Q("Comment les artistes diffusent-ils aujourd'hui souvent leurs œuvres ?", ["Sur Internet et les réseaux sociaux", "Uniquement par la poste", "Uniquement dans les églises", "Jamais"], "Sur Internet et les réseaux sociaux", "La diffusion est mondiale et instantanée."),
  Q("Qu'est-ce qu'un musée virtuel ?", ["Un musée consultable en ligne, avec des images numérisées", "Un musée sans œuvres", "Un musée fermé", "Un musée imaginaire de roman"], "Un musée consultable en ligne, avec des images numérisées", "Google Arts & Culture en propose."),
  Q("Pourquoi les musées numérisent-ils leurs collections ?", ["Pour les rendre accessibles à tous et les conserver", "Pour les vendre", "Pour les détruire", "Pour les cacher"], "Pour les rendre accessibles à tous et les conserver", "Les bases Joconde ou Navigart en sont des exemples."),
]),
notion('AR-6', 0, F, 'artr-licences', [
  Q("Peut-on utiliser librement n'importe quelle image trouvée sur Internet ?", ["Non, elle peut être protégée par le droit d'auteur", "Oui, toujours", "Oui, si elle est jolie", "Oui, si on la modifie un peu"], "Non, elle peut être protégée par le droit d'auteur", "Il faut vérifier la licence."),
  Q("Que permettent les licences Creative Commons ?", ["De réutiliser une œuvre selon des conditions choisies par l'auteur", "De voler une œuvre", "De vendre une œuvre sans accord", "Rien"], "De réutiliser une œuvre selon des conditions choisies par l'auteur", "Par exemple en citant l'auteur."),
  Q("Combien de temps après la mort de l'auteur une œuvre entre-t-elle dans le domaine public en France ?", ["70 ans", "10 ans", "200 ans", "Jamais"], "70 ans", "Elle peut alors être utilisée librement."),
]),
notion('AR-6', 0, F, 'artr-art-jeu-video', [
  Q("Peut-on considérer certains jeux vidéo comme des œuvres d'art ?", ["Oui, ils mêlent image, son, récit et interaction", "Non, jamais", "Seulement les jeux d'échecs", "Seulement les jeux de cartes"], "Oui, ils mêlent image, son, récit et interaction", "Des musées les exposent."),
  Q("Qu'est-ce que le « pixel art » ?", ["Un style graphique fait de pixels visibles, inspiré des premiers jeux vidéo", "Une peinture à l'huile", "Une sculpture", "Un style de photo"], "Un style graphique fait de pixels visibles, inspiré des premiers jeux vidéo", "Il joue sur la nostalgie."),
  Q("Qu'est-ce qu'un « game designer » ?", ["Le concepteur d'un jeu", "Un joueur professionnel", "Un vendeur de jeux", "Un testeur"], "Le concepteur d'un jeu", "Il imagine les règles et l'univers."),
]),
notion('AR-6', 0, F, 'artr-video-art', [
  Q("Qu'est-ce que l'art vidéo ?", ["Une pratique artistique qui utilise la vidéo comme matériau", "Un film de cinéma commercial", "Une émission de télévision", "Une publicité"], "Une pratique artistique qui utilise la vidéo comme matériau", "Il apparaît dans les années 1960."),
  Q("Qu'est-ce qu'un mapping vidéo ?", ["La projection d'images animées sur un bâtiment ou un objet", "Une carte routière", "Un plan de musée", "Un dessin au feutre"], "La projection d'images animées sur un bâtiment ou un objet", "La Fête des lumières de Lyon en est célèbre."),
  Q("Quelle fête lyonnaise célèbre la lumière chaque mois de décembre ?", ["La Fête des lumières", "La Nuit blanche", "Le Festival d'Avignon", "La Fête de la musique"], "La Fête des lumières", "Autour du 8 décembre."),
]),
notion('AR-6', 0, I, 'artr-art-numerique-immersif', [
  Q("Qu'est-ce qu'une exposition immersive ?", ["Une exposition où des projections enveloppent le visiteur", "Une exposition sous l'eau", "Une exposition fermée", "Une exposition de sculptures"], "Une exposition où des projections enveloppent le visiteur", "L'Atelier des Lumières à Paris en propose."),
  Q("Quel collectif japonais crée des installations numériques interactives géantes ?", ["teamLab", "Daft Punk", "Ghibli", "Gutai"], "teamLab", "Ses musées à Tokyo attirent des millions de visiteurs."),
  Q("Quelle critique est parfois faite aux expositions immersives de peintures ?", ["Elles transforment l'œuvre en spectacle et éloignent de l'original", "Elles sont trop silencieuses", "Elles montrent les originaux", "Elles sont gratuites"], "Elles transforment l'œuvre en spectacle et éloignent de l'original", "L'expérience diffère de la rencontre avec l'œuvre."),
]),
notion('AR-6', 0, I, 'artr-net-art', [
  Q("Qu'est-ce que le net art ?", ["Un art créé pour Internet et qui utilise ses spécificités", "Un art réalisé avec des filets", "Un art de la pêche", "Un art du tennis"], "Un art créé pour Internet et qui utilise ses spécificités", "Il apparaît dans les années 1990."),
  Q("Qu'est-ce qu'une œuvre interactive ?", ["Une œuvre qui réagit aux actions du spectateur", "Une œuvre qu'on ne peut pas toucher", "Une œuvre en noir et blanc", "Une œuvre ancienne"], "Une œuvre qui réagit aux actions du spectateur", "Le spectateur devient acteur."),
  Q("Qu'est-ce qu'un « mème » sur Internet ?", ["Une image ou une idée détournée et partagée massivement", "Une œuvre de musée", "Un virus informatique", "Une photo de famille"], "Une image ou une idée détournée et partagée massivement", "Il circule et se transforme."),
]),
notion('AR-6', 0, I, 'artr-impression-3d', [
  Q("Que permet une imprimante 3D en art ?", ["Fabriquer des sculptures à partir d'un fichier numérique", "Imprimer des photos", "Peindre des tableaux", "Projeter des films"], "Fabriquer des sculptures à partir d'un fichier numérique", "Elle dépose la matière couche par couche."),
  Q("Qu'est-ce que la modélisation 3D ?", ["La création d'un objet en trois dimensions sur ordinateur", "Le moulage en plâtre", "La gravure", "Le dessin en perspective"], "La création d'un objet en trois dimensions sur ordinateur", "Elle sert au cinéma, aux jeux et au design."),
  Q("Qu'est-ce que la numérisation 3D d'une sculpture ?", ["Sa reproduction numérique en volume grâce à un scanner", "Sa destruction", "Sa photo de face", "Sa peinture"], "Sa reproduction numérique en volume grâce à un scanner", "Elle aide à la conservation et à la restauration."),
]),
notion('AR-6', 0, I, 'artr-realite-virtuelle', [
  Q("Qu'est-ce que la réalité virtuelle ?", ["Une immersion dans un monde numérique grâce à un casque", "Un rêve", "Un film en noir et blanc", "Une photo retouchée"], "Une immersion dans un monde numérique grâce à un casque", "Le visiteur se déplace dans l'œuvre."),
  Q("Qu'est-ce que la réalité augmentée ?", ["L'ajout d'éléments numériques à la vision du monde réel", "Une réalité agrandie au microscope", "Un film 3D", "Un tableau très grand"], "L'ajout d'éléments numériques à la vision du monde réel", "Par l'écran d'un téléphone."),
  Q("Comment certains musées utilisent-ils la réalité augmentée ?", ["Pour faire apparaître des informations ou des reconstitutions sur les œuvres", "Pour cacher les œuvres", "Pour vendre des billets", "Pour éteindre les lumières"], "Pour faire apparaître des informations ou des reconstitutions sur les œuvres", "Elle enrichit la visite."),
]),
notion('AR-6', 0, I, 'artr-photographie-retouche', [
  Q("La retouche d'image est-elle une invention du numérique ?", ["Non, elle existait déjà en photographie argentique", "Oui, elle date de 2000", "Oui, elle date d'Internet", "Elle n'existe pas"], "Non, elle existait déjà en photographie argentique", "On grattait et recomposait les négatifs."),
  Q("Quelle mention est obligatoire en France sur les photos publicitaires où un corps a été retouché ?", ["« Photographie retouchée »", "« Image interdite »", "« Photo d'art »", "Aucune"], "« Photographie retouchée »", "Depuis 2017."),
  Q("Pourquoi cette mention a-t-elle été rendue obligatoire ?", ["Pour lutter contre des modèles de beauté irréalistes", "Pour aider les photographes", "Pour vendre plus", "Pour protéger les logiciels"], "Pour lutter contre des modèles de beauté irréalistes", "Elle vise notamment les troubles alimentaires."),
]),
notion('AR-6', 0, I, 'artr-artistes-numeriques', [
  Q("Quel artiste britannique crée des œuvres numériques sur iPad et les expose dans les musées ?", ["David Hockney", "Francis Bacon", "Lucian Freud", "Damien Hirst"], "David Hockney", "Ses dessins sur iPad ont été exposés à Paris."),
  Q("Quel artiste installé en France crée depuis les années 1980 des jardins virtuels génératifs ?", ["Miguel Chevalier", "Pierre Soulages", "Daniel Buren", "Yves Klein"], "Miguel Chevalier", "Il crée des jardins virtuels génératifs."),
  Q("Qu'est-ce qu'une œuvre générative ?", ["Une œuvre produite par un programme qui la fait évoluer", "Une œuvre réalisée par plusieurs générations", "Une œuvre ancienne", "Une sculpture en bronze"], "Une œuvre produite par un programme qui la fait évoluer", "L'artiste écrit les règles."),
]),
notion('AR-6', 0, I, 'artr-copie-original', [
  Q("À l'ère du numérique, une copie peut-elle être identique à l'original ?", ["Oui, un fichier numérique peut être copié à l'identique", "Non, jamais", "Seulement sur papier", "Seulement pour la musique"], "Oui, un fichier numérique peut être copié à l'identique", "Cela pose la question de l'original."),
  Q("Qu'est-ce qu'un NFT dans le monde de l'art ?", ["Un certificat numérique d'authenticité et de propriété d'une œuvre", "Une copie gratuite", "Un logiciel de dessin", "Un format d'image"], "Un certificat numérique d'authenticité et de propriété d'une œuvre", "Le phénomène a explosé en 2021."),
  Q("Quel artiste a vendu une œuvre numérique 69 millions de dollars en 2021 ?", ["Beeple", "Banksy", "Jeff Koons", "Damien Hirst"], "Beeple", "Everydays: The First 5000 Days."),
]),
notion('AR-6', 0, I, 'artr-montage-numerique', [
  Q("Qu'est-ce qu'un logiciel de montage vidéo ?", ["Un outil qui permet d'assembler et couper des séquences", "Un appareil photo", "Un pinceau", "Un scanner"], "Un outil qui permet d'assembler et couper des séquences", "On peut ajouter son et effets."),
  Q("Qu'est-ce qu'un fond vert (incrustation) ?", ["Un fond uni remplacé ensuite par une autre image", "Un fond de jardin", "Une peinture verte", "Un écran éteint"], "Un fond uni remplacé ensuite par une autre image", "Il est très utilisé au cinéma et à la météo."),
  Q("Qu'est-ce qu'un « stop motion » numérique ?", ["Une animation image par image réalisée avec un appareil numérique", "Une vidéo en direct", "Une photo floue", "Un arrêt de la caméra"], "Une animation image par image réalisée avec un appareil numérique", "On peut le faire en classe avec une tablette."),
]),
notion('AR-6', 0, D, 'artr-ia-creation', [
  Q("Quelle question pose une image générée par une intelligence artificielle ?", ["Qui en est l'auteur : la machine, le programmeur ou l'utilisateur ?", "Sa couleur", "Son prix", "Aucune"], "Qui en est l'auteur : la machine, le programmeur ou l'utilisateur ?", "Le droit d'auteur est en débat."),
  Q("Quel portrait généré par une IA a été vendu aux enchères chez Christie's en 2018 ?", ["Le Portrait d'Edmond de Belamy (collectif Obvious)", "La Joconde numérique", "Le Cri numérique", "Girl with Balloon"], "Le Portrait d'Edmond de Belamy (collectif Obvious)", "Il a atteint 432 500 dollars."),
  Q("Pourquoi des artistes protestent-ils contre certaines IA génératrices d'images ?", ["Elles ont été entraînées sur leurs œuvres sans autorisation", "Elles sont trop lentes", "Elles ne font que du noir et blanc", "Elles sont gratuites"], "Elles ont été entraînées sur leurs œuvres sans autorisation", "La question du droit d'auteur est posée."),
]),
notion('AR-6', 0, D, 'artr-glitch-art', [
  Q("Qu'est-ce que le glitch art ?", ["Un art qui exploite les erreurs et les bugs numériques", "Un art de la poterie", "Un art du vitrail", "Un art du bois"], "Un art qui exploite les erreurs et les bugs numériques", "L'accident devient esthétique."),
  Q("Quelle différence y a-t-il entre une image vectorielle et une image matricielle ?", ["La vectorielle est définie par des formes mathématiques et s'agrandit sans perte", "Elles sont identiques", "La matricielle s'agrandit sans perte", "La vectorielle est une photo"], "La vectorielle est définie par des formes mathématiques et s'agrandit sans perte", "Les logos sont souvent vectoriels."),
  Q("Qu'est-ce que la compression d'une image numérique ?", ["La réduction de la taille du fichier, parfois avec perte de qualité", "Le recadrage", "L'impression", "L'agrandissement"], "La réduction de la taille du fichier, parfois avec perte de qualité", "Le format JPEG compresse avec perte."),
]),
notion('AR-6', 0, D, 'artr-art-algorithmique', [
  Q("Quelle artiste hongroise pionnière a créé des œuvres par ordinateur dès les années 1960 ?", ["Vera Molnár", "Sonia Delaunay", "Hilma af Klint", "Bridget Riley"], "Vera Molnár", "Elle a travaillé en France."),
  Q("Qu'est-ce qu'un algorithme en art numérique ?", ["Une suite d'instructions que l'ordinateur exécute pour produire l'œuvre", "Un pinceau numérique", "Un écran", "Une imprimante"], "Une suite d'instructions que l'ordinateur exécute pour produire l'œuvre", "On parle d'art algorithmique."),
  Q("Quel langage de programmation est souvent utilisé par les artistes pour créer des images ?", ["Processing", "Excel", "Word", "PowerPoint"], "Processing", "Il est conçu pour l'art et le design."),
]),
notion('AR-6', 0, D, 'artr-musee-numerique-acces', [
  Q("Quel grand musée a mis en ligne gratuitement l'ensemble de ses collections en 2021 ?", ["Le Louvre", "Le Prado", "Le MoMA", "Aucun"], "Le Louvre", "Plus de 480 000 œuvres."),
  Q("Qu'est-ce que l'« open content » dans les musées ?", ["La mise à disposition libre d'images d'œuvres du domaine public", "L'ouverture des musées la nuit", "La gratuité des billets", "Un musée sans gardien"], "La mise à disposition libre d'images d'œuvres du domaine public", "Le Rijksmuseum d'Amsterdam en est un pionnier."),
  Q("Pourquoi voir une œuvre en vrai reste-t-il important malgré le numérique ?", ["Pour percevoir sa taille, sa matière et sa présence réelle", "Ce n'est plus important", "Parce que les écrans sont interdits", "Pour prendre des selfies"], "Pour percevoir sa taille, sa matière et sa présence réelle", "L'écran ne remplace pas l'expérience."),
]),
notion('AR-6', 0, D, 'artr-surveillance-image', [
  Q("Quel artiste chinois critique la surveillance et la censure, notamment avec des caméras en marbre ?", ["Ai Weiwei", "Cai Guo-Qiang", "Yayoi Kusama", "Takashi Murakami"], "Ai Weiwei", "Il a été emprisonné en 2011."),
  Q("Quelle question pose la reconnaissance faciale aux artistes ?", ["Celle de la surveillance et de la vie privée", "Celle de la perspective", "Celle de la couleur", "Aucune"], "Celle de la surveillance et de la vie privée", "Certains créent des maquillages anti-reconnaissance."),
  Q("Qu'est-ce que l'« image opérationnelle » selon l'artiste Harun Farocki ?", ["Une image produite par des machines pour des machines (surveillance, guidage)", "Un tableau de bloc opératoire", "Une photo de famille", "Un dessin d'architecte"], "Une image produite par des machines pour des machines (surveillance, guidage)", "Elle n'est pas faite pour être regardée par des humains."),
]),
notion('AR-6', 0, D, 'artr-ecologie-numerique', [
  Q("Le numérique a-t-il un coût environnemental ?", ["Oui, serveurs, écrans et réseaux consomment énergie et ressources", "Non, il est immatériel", "Seulement l'impression", "Seulement la musique"], "Oui, serveurs, écrans et réseaux consomment énergie et ressources", "On parle de sobriété numérique."),
  Q("Pourquoi les NFT ont-ils été critiqués sur le plan écologique ?", ["Certaines blockchains consomment beaucoup d'électricité", "Ils utilisent du papier", "Ils polluent les rivières", "Ils sont imprimés en 3D"], "Certaines blockchains consomment beaucoup d'électricité", "Des solutions moins énergivores existent."),
  Q("Quel geste réduit l'empreinte numérique d'une classe ?", ["Limiter le stockage et l'envoi de fichiers lourds inutiles", "Tout imprimer", "Laisser les écrans allumés", "Multiplier les vidéos en haute définition"], "Limiter le stockage et l'envoi de fichiers lourds inutiles", "Chaque fichier stocké a un coût."),
]),
notion('AR-6', 0, D, 'artr-photographie-numerique-art', [
  Q("Quel photographe allemand crée de très grandes photos retouchées numériquement, comme Rhein II ?", ["Andreas Gursky", "Gerhard Richter", "Thomas Ruff", "August Sander"], "Andreas Gursky", "Elle a été l'une des photos les plus chères du monde."),
  Q("Quel photographe canadien compose ses images comme des tableaux, avec de grands caissons lumineux ?", ["Jeff Wall", "Andreas Gursky", "Robert Frank", "Ansel Adams"], "Jeff Wall", "Il mêle photographie et peinture d'histoire."),
  Q("Qu'est-ce qu'un caisson lumineux en art ?", ["Une boîte éclairée de l'intérieur qui présente une image transparente", "Un projecteur de cinéma", "Une lampe de bureau", "Un écran de téléphone"], "Une boîte éclairée de l'intérieur qui présente une image transparente", "Il donne une forte présence à l'image."),
]),
notion('AR-6', 0, D, 'artr-video-artistes', [
  Q("Quel artiste français crée des œuvres vivantes, comme un chien à la patte rose dans un jardin en friche (Untilled, 2012) ?", ["Pierre Huyghe", "Daniel Buren", "Yves Klein", "Christian Boltanski"], "Pierre Huyghe", "Il mêle vidéo, êtres vivants et fiction."),
  Q("Quelle artiste suisse crée des installations vidéo colorées et oniriques ?", ["Pipilotti Rist", "Sophie Calle", "Annette Messager", "Louise Bourgeois"], "Pipilotti Rist", "Elle projette ses vidéos sur les murs et les plafonds."),
  Q("Quel mouvement des années 1960, avec Nam June Paik, mêlait art, musique et happening ?", ["Fluxus", "Le cubisme", "Le Bauhaus", "Le fauvisme"], "Fluxus", "Il refuse les frontières entre les arts."),
]),
]

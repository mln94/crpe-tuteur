# Arts plastiques · L'œuvre, l'espace, l'auteur, le spectateur : 25 questions par niveau et par point du programme
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ AE-1 · La relation du corps à la production artistique ══
notion('AE-1', 0, F, 'arte-geste-trace', [
  Q("Quelle partie du corps l'artiste utilise-t-il le plus souvent pour peindre ?", ["La main et le bras", "Le pied", "La tête", "Le genou"], "La main et le bras", "Mais certains peignent avec tout le corps."),
  Q("Qu'est-ce qu'un geste ample en peinture ?", ["Un grand mouvement du bras qui laisse une trace large", "Un tout petit trait", "Un point minuscule", "Une signature"], "Un grand mouvement du bras qui laisse une trace large", "Il donne de l'énergie à l'œuvre."),
  Q("Comment appelle-t-on la marque laissée par un outil sur une surface ?", ["Une trace", "Un cadre", "Un socle", "Un cartel"], "Une trace", "Chaque outil laisse une trace différente."),
]),
notion('AE-1', 0, F, 'arte-calligraphie', [
  Q("Qu'est-ce que la calligraphie ?", ["L'art de bien former les lettres et les signes", "L'art de la danse", "L'art de la sculpture", "L'art du jardin"], "L'art de bien former les lettres et les signes", "Elle est très importante en Chine, au Japon et dans le monde arabe."),
  Q("Quel outil utilise traditionnellement le calligraphe chinois ?", ["Un pinceau et de l'encre", "Un stylo à bille", "Un burin", "Un rouleau"], "Un pinceau et de l'encre", "Le geste doit être maîtrisé et souple."),
  Q("Pourquoi la respiration compte-t-elle en calligraphie ?", ["Le geste suit le souffle et doit être continu", "Pour sentir l'encre", "Elle ne compte pas", "Pour souffler sur la feuille"], "Le geste suit le souffle et doit être continu", "Le corps entier participe."),
]),
notion('AE-1', 0, F, 'arte-dessin-lumiere', [
  Q("Quel artiste a été photographié en train de « dessiner avec la lumière » d'une lampe en 1949 ?", ["Pablo Picasso", "Claude Monet", "Henri Matisse", "Auguste Rodin"], "Pablo Picasso", "Le photographe Gjon Mili a utilisé une pose longue."),
  Q("Qu'est-ce que le light painting ?", ["Une photo en pose longue où l'on dessine avec une source lumineuse", "Une peinture sur ampoule", "Un vitrail", "Un dessin phosphorescent"], "Une photo en pose longue où l'on dessine avec une source lumineuse", "On peut en faire en classe."),
  Q("Que garde le light painting du geste de l'artiste ?", ["Sa trajectoire lumineuse dans l'espace", "Son empreinte digitale", "Sa voix", "Rien"], "Sa trajectoire lumineuse dans l'espace", "Le mouvement devient image."),
]),
notion('AE-1', 0, F, 'arte-matisse-baton', [
  Q("Comment Matisse dessinait-il sur les murs quand il était alité à la fin de sa vie ?", ["Avec un fusain fixé au bout d'un long bâton", "Avec un pistolet à peinture", "Avec ses pieds", "Il ne dessinait plus"], "Avec un fusain fixé au bout d'un long bâton", "Le corps s'adapte à la maladie."),
  Q("Quelle technique Matisse a-t-il développée en découpant du papier coloré ?", ["Les papiers gouachés découpés", "Le dripping", "La fresque", "La gravure"], "Les papiers gouachés découpés", "Il « dessine dans la couleur »."),
  Q("Que signifie « dessiner avec des ciseaux » pour Matisse ?", ["Découper directement la forme dans la couleur, sans dessin préalable", "Couper un dessin raté", "Utiliser une règle", "Faire du collage de journaux"], "Découper directement la forme dans la couleur, sans dessin préalable", "Le geste est direct."),
]),
notion('AE-1', 0, F, 'arte-mains-sculpteur', [
  Q("Avec quoi le sculpteur modèle-t-il l'argile ?", ["Avec ses mains et des ébauchoirs", "Avec un pinceau", "Avec un appareil photo", "Avec de l'encre"], "Avec ses mains et des ébauchoirs", "Les traces de doigts restent parfois visibles."),
  Q("Quel sculpteur a représenté de nombreuses mains, comme La Cathédrale (deux mains droites) ?", ["Auguste Rodin", "Constantin Brancusi", "Alberto Giacometti", "Henry Moore"], "Auguste Rodin", "La main est pour lui très expressive."),
  Q("Que montrent les empreintes de doigts laissées dans une sculpture ?", ["La présence et le geste de l'artiste", "Une erreur à corriger", "La signature officielle", "Le prix"], "La présence et le geste de l'artiste", "On parle de trace de la main."),
]),
notion('AE-1', 0, F, 'arte-danse-peinture', [
  Q("Quel art utilise principalement le corps en mouvement ?", ["La danse", "La peinture murale", "La photographie", "L'architecture"], "La danse", "Le corps y est l'instrument de l'œuvre."),
  Q("Quel peintre a représenté des danseurs en ronde dans La Danse (1910) ?", ["Henri Matisse", "Edgar Degas", "Claude Monet", "Paul Cézanne"], "Henri Matisse", "Cinq personnages rouges sur fond bleu et vert."),
  Q("Quelle danseuse américaine a révolutionné la danse moderne en dansant pieds nus ?", ["Isadora Duncan", "Anna Pavlova", "Pina Bausch", "Martha Graham"], "Isadora Duncan", "Elle refuse les pointes et le corset."),
]),
notion('AE-1', 0, F, 'arte-autoportrait-corps', [
  Q("Que représente un autoportrait ?", ["L'artiste lui-même", "Un ami de l'artiste", "Un paysage", "Un objet"], "L'artiste lui-même", "Il se peint souvent grâce à un miroir."),
  Q("De quel outil le peintre a-t-il besoin pour faire son autoportrait ?", ["Un miroir (ou une photo)", "Une boussole", "Un microscope", "Une règle"], "Un miroir (ou une photo)", "D'où des autoportraits parfois inversés."),
  Q("Quel peintre autrichien s'est représenté nu et tourmenté dans de nombreux autoportraits ?", ["Egon Schiele", "Gustav Klimt", "Claude Monet", "Raphaël"], "Egon Schiele", "Le corps exprime l'angoisse."),
]),
notion('AE-1', 0, F, 'arte-proportions-corps', [
  Q("Quel dessin de Léonard de Vinci montre un homme inscrit dans un cercle et un carré ?", ["L'Homme de Vitruve", "La Joconde", "La Cène", "L'Annonciation"], "L'Homme de Vitruve", "Il étudie les proportions idéales du corps."),
  Q("Combien de fois la hauteur de la tête est-elle souvent contenue dans un corps adulte en dessin ?", ["Environ 7 à 8 fois", "2 fois", "15 fois", "1 fois"], "Environ 7 à 8 fois", "On parle de canon."),
  Q("Qu'est-ce qu'un canon en sculpture grecque ?", ["Un système de proportions idéales du corps", "Une arme", "Une chanson", "Un socle"], "Un système de proportions idéales du corps", "Celui de Polyclète est célèbre."),
]),
notion('AE-1', 0, I, 'arte-niki-tirs', [
  Q("Comment Niki de Saint Phalle a-t-elle réalisé ses « Tirs » en 1961 ?", ["En tirant à la carabine sur des poches de peinture cachées dans du plâtre", "En peignant au pinceau", "En sculptant du marbre", "En photographiant"], "En tirant à la carabine sur des poches de peinture cachées dans du plâtre", "La peinture coule comme du sang."),
  Q("Quel jardin de sculptures géantes Niki de Saint Phalle a-t-elle créé en Toscane ?", ["Le Jardin des Tarots", "Le Jardin du Luxembourg", "Les Jardins de Monet", "Le Jardin des Plantes"], "Le Jardin des Tarots", "Elle y a travaillé près de vingt ans."),
  Q("Quel sens donne Niki de Saint Phalle à ses Tirs ?", ["Une révolte contre la violence et l'autorité", "Une fête foraine", "Un exercice militaire", "Une décoration"], "Une révolte contre la violence et l'autorité", "Le geste est cathartique."),
]),
notion('AE-1', 0, I, 'arte-performance-corps', [
  Q("Quelle artiste française s'est blessée volontairement dans ses performances des années 1970 ?", ["Gina Pane", "Niki de Saint Phalle", "Sophie Calle", "Annette Messager"], "Gina Pane", "Elle interroge la douleur et la société."),
  Q("Quelle artiste cubano-américaine a imprimé la silhouette de son corps dans la terre et la nature ?", ["Ana Mendieta", "Frida Kahlo", "Louise Bourgeois", "Cindy Sherman"], "Ana Mendieta", "Série Siluetas."),
  Q("Qu'est-ce qui caractérise une performance ?", ["Une action réalisée en direct par l'artiste devant un public", "Un tableau accroché", "Un livre", "Une sculpture fixe"], "Une action réalisée en direct par l'artiste devant un public", "Elle est souvent éphémère."),
]),
notion('AE-1', 0, I, 'arte-hartung-outils', [
  Q("Quel peintre franco-allemand a inventé ses propres outils (balais, rameaux, pistolets) pour peindre ?", ["Hans Hartung", "Pierre Soulages", "Georges Mathieu", "Jean Dubuffet"], "Hans Hartung", "Il a perdu une jambe à la guerre."),
  Q("Pourquoi un artiste invente-t-il de nouveaux outils ?", ["Pour obtenir des traces et des gestes nouveaux", "Par économie", "Pour aller plus lentement", "Par obligation"], "Pour obtenir des traces et des gestes nouveaux", "L'outil prolonge le corps."),
  Q("Quels outils Soulages fabriquait-il pour travailler le noir ?", ["Des raclettes, lames et brosses de peintre en bâtiment", "Des pinceaux fins", "Des crayons", "Des feutres"], "Des raclettes, lames et brosses de peintre en bâtiment", "Il creuse et sillonne la peinture."),
]),
notion('AE-1', 0, I, 'arte-mystere-picasso', [
  Q("Quel film d'Henri-Georges Clouzot (1956) filme Picasso en train de peindre ?", ["Le Mystère Picasso", "La Belle Noiseuse", "Guernica", "Les Demoiselles"], "Le Mystère Picasso", "On voit l'œuvre naître et se transformer."),
  Q("Quel photographe a pris en 1950 des photos et un film de Pollock au travail ?", ["Hans Namuth", "Robert Capa", "Man Ray", "Cartier-Bresson"], "Hans Namuth", "Ils ont rendu célèbre le dripping."),
  Q("Pourquoi filmer un artiste au travail ?", ["Pour montrer le processus et le geste de création", "Pour le surveiller", "Pour vendre une caméra", "Pour remplacer l'œuvre"], "Pour montrer le processus et le geste de création", "Le geste devient visible."),
]),
notion('AE-1', 0, I, 'arte-corps-mesure', [
  Q("Pourquoi les anciennes unités de mesure s'appelaient-elles pied, pouce ou coudée ?", ["Elles étaient tirées des dimensions du corps humain", "Par hasard", "En hommage à des rois", "Elles venaient de la mer"], "Elles étaient tirées des dimensions du corps humain", "Le corps a longtemps servi d'étalon."),
  Q("Quel système de proportions Le Corbusier a-t-il fondé sur le corps humain ?", ["Le Modulor", "Le nombre d'or", "Le mètre", "Le canon de Polyclète"], "Le Modulor", "Il a servi à concevoir la Cité radieuse."),
  Q("Quelle taille d'homme Le Corbusier a-t-il retenue pour le Modulor (1,83 m le bras levé à 2,26 m) ?", ["1,83 m", "1,50 m", "2 m", "1,70 m"], "1,83 m", "Il s'inspire d'un policier anglais."),
]),
notion('AE-1', 0, I, 'arte-dessin-aveugle', [
  Q("Qu'est-ce que le dessin « à l'aveugle » ?", ["Dessiner en regardant le modèle sans regarder sa feuille", "Dessiner dans le noir total", "Dessiner les yeux fermés", "Copier un dessin"], "Dessiner en regardant le modèle sans regarder sa feuille", "Il libère le geste."),
  Q("Qu'est-ce qu'un dessin automatique chez les surréalistes ?", ["Un dessin fait sans contrôle de la raison, au fil de la main", "Un dessin fait par une machine", "Un dessin très précis", "Un dessin copié"], "Un dessin fait sans contrôle de la raison, au fil de la main", "André Masson en est un pionnier."),
  Q("Quel poète-peintre belge a dessiné sous l'effet de la mescaline pour explorer l'esprit ?", ["Henri Michaux", "René Magritte", "Paul Delvaux", "Jacques Brel"], "Henri Michaux", "Ses dessins sont faits de lignes vibrantes."),
]),
notion('AE-1', 0, I, 'arte-instrument-musique-geste', [
  Q("Qu'est-ce qui relie le geste du musicien et celui du peintre ?", ["Le corps et l'instrument produisent une trace (sonore ou visuelle) dans le temps", "Rien", "Ils utilisent les mêmes outils", "Ils travaillent tous les deux assis"], "Le corps et l'instrument produisent une trace (sonore ou visuelle) dans le temps", "Kandinsky comparait la peinture à la musique."),
  Q("Quel outil prolonge le bras du peintre comme l'archet celui du violoniste ?", ["Le pinceau", "La palette", "Le cadre", "Le chevalet"], "Le pinceau", "L'outil est une extension du corps."),
  Q("Quel artiste dessinait en musique, en suivant le rythme avec son crayon (dessin musical) ?", ["Paul Klee, lui-même violoniste", "Pablo Picasso", "Claude Monet", "Auguste Rodin"], "Paul Klee, lui-même violoniste", "Il cherchait des équivalences entre rythme et ligne."),
]),
notion('AE-1', 0, D, 'arte-pinceau-vivant', [
  Q("Quel artiste japonais du groupe Gutai peignait avec ses pieds, suspendu à une corde ?", ["Kazuo Shiraga", "Hokusai", "Takashi Murakami", "Yayoi Kusama"], "Kazuo Shiraga", "Il glissait sur la toile posée au sol."),
  Q("Quelle chorégraphe américaine a dessiné sur de grandes feuilles avec son corps entier (It's a Draw) ?", ["Trisha Brown", "Martha Graham", "Pina Bausch", "Isadora Duncan"], "Trisha Brown", "Elle tient des fusains dans les mains et les pieds."),
  Q("Que montrent ces pratiques sur le corps de l'artiste ?", ["Le corps tout entier peut devenir outil et sujet de l'œuvre", "Le corps n'a aucun rôle", "Seules les mains comptent", "Le corps doit rester immobile"], "Le corps tout entier peut devenir outil et sujet de l'œuvre", "La frontière entre danse et dessin s'efface."),
]),
notion('AE-1', 0, D, 'arte-twombly-ecriture', [
  Q("Quel peintre américain couvre ses toiles de gribouillis et d'écritures proches de graffitis ?", ["Cy Twombly", "Jackson Pollock", "Mark Rothko", "Jasper Johns"], "Cy Twombly", "Il a peint un plafond du Louvre en 2010."),
  Q("Que montrent les tracés de Twombly ?", ["La vitesse et la spontanéité du geste, entre dessin et écriture", "Des paysages réalistes", "Des portraits", "Des objets"], "La vitesse et la spontanéité du geste, entre dessin et écriture", "Le geste rappelle l'enfance et l'Antiquité."),
  Q("Quel peintre chinois naturalisé français a mêlé calligraphie et abstraction ?", ["Zao Wou-Ki", "Ai Weiwei", "Cai Guo-Qiang", "Yue Minjun"], "Zao Wou-Ki", "Il est mort en 2013."),
]),
notion('AE-1', 0, D, 'arte-yves-klein-saut', [
  Q("Quelle photographie célèbre montre Yves Klein se jetant d'un mur (1960) ?", ["Le Saut dans le vide", "La Chute d'Icare", "L'Envol", "Le Plongeon"], "Le Saut dans le vide", "C'est un photomontage."),
  Q("Comment le Saut dans le vide a-t-il été réalisé ?", ["Par un photomontage : des judokas tenaient une bâche invisible sur l'image finale", "Klein a vraiment sauté sans protection", "C'est une peinture", "C'est une image numérique"], "Par un photomontage : des judokas tenaient une bâche invisible sur l'image finale", "Klein était judoka."),
  Q("Qu'exprime cette image pour Klein ?", ["Le désir d'aller dans le vide, l'immatériel", "La peur du sport", "Une publicité", "Une blague sans sens"], "Le désir d'aller dans le vide, l'immatériel", "Il parle de « peintre de l'espace »."),
]),
notion('AE-1', 0, D, 'arte-artiste-vieillesse-maladie', [
  Q("Quel peintre impressionniste, atteint de rhumatismes, peignait avec le pinceau attaché à la main ?", ["Auguste Renoir", "Claude Monet", "Edgar Degas", "Paul Cézanne"], "Auguste Renoir", "Il a continué à peindre jusqu'à sa mort."),
  Q("Quel peintre, atteint de cataracte, a vu les couleurs de ses Nymphéas changer ?", ["Claude Monet", "Edgar Degas", "Henri Matisse", "Vincent van Gogh"], "Claude Monet", "Ses dernières toiles sont plus rouges et brunes."),
  Q("Quel peintre, devenu presque aveugle, s'est tourné vers la sculpture et le pastel ?", ["Edgar Degas", "Claude Monet", "Paul Gauguin", "Henri Rousseau"], "Edgar Degas", "Il a modelé des danseuses en cire."),
]),
notion('AE-1', 0, D, 'arte-voix-son-corps', [
  Q("Quelle artiste japonaise de Fluxus a créé Cut Piece, où le public découpe ses vêtements ?", ["Yoko Ono", "Yayoi Kusama", "Marina Abramović", "Mariko Mori"], "Yoko Ono", "La performance date de 1964."),
  Q("Quel artiste a enregistré le son de sa propre fabrication d'une boîte (Box with the Sound of Its Own Making) ?", ["Robert Morris", "Marcel Duchamp", "John Cage", "Andy Warhol"], "Robert Morris", "Le processus devient l'œuvre."),
  Q("Quelle œuvre musicale de John Cage consiste en 4 minutes 33 secondes de silence de l'interprète ?", ["4'33\"", "Le Boléro", "Clapping Music", "In C"], "4'33\"", "Les bruits de la salle deviennent la musique."),
]),
notion('AE-1', 0, D, 'arte-mime-masque', [
  Q("Quel mime français a créé le personnage de Bip ?", ["Marcel Marceau", "Jacques Tati", "Charlie Chaplin", "Louis de Funès"], "Marcel Marceau", "Le corps raconte sans mots."),
  Q("Que permet le masque au théâtre ?", ["De transformer le corps et l'identité de l'acteur", "De mieux entendre", "De cacher le décor", "De parler plus fort"], "De transformer le corps et l'identité de l'acteur", "La commedia dell'arte en utilise."),
  Q("Dans quel théâtre traditionnel japonais les acteurs portent-ils des masques de bois ?", ["Le nô", "Le kabuki", "Le bunraku", "Le butō"], "Le nô", "Il existe depuis le XIVe siècle."),
]),
notion('AE-1', 0, D, 'arte-corps-photographie', [
  Q("Quel photographe a photographié des danseurs en suspension, « saut » des célébrités (Jumpology) ?", ["Philippe Halsman", "Ansel Adams", "Robert Doisneau", "Nadar"], "Philippe Halsman", "Il a aussi photographié Dalí en l'air."),
  Q("Quelle photo de Philippe Halsman montre Dalí, des chats et de l'eau en suspension ?", ["Dalí Atomicus", "Le Baiser", "Migrant Mother", "Earthrise"], "Dalí Atomicus", "Il a fallu 28 essais en 1948."),
  Q("Quel photographe a figé le saut d'un homme au-dessus d'une flaque derrière la gare Saint-Lazare ?", ["Henri Cartier-Bresson", "Robert Doisneau", "Brassaï", "Man Ray"], "Henri Cartier-Bresson", "Photo de 1932, symbole de l'instant décisif."),
]),
notion('AE-1', 0, D, 'arte-geste-machine', [
  Q("Quel artiste suisse a construit des machines à dessiner, les Méta-Matics ?", ["Jean Tinguely", "Paul Klee", "Alexander Calder", "Le Corbusier"], "Jean Tinguely", "Elles produisent des dessins abstraits automatiques."),
  Q("Quel programme informatique créé par Harold Cohen dessinait de façon autonome dès les années 1970 ?", ["AARON", "Photoshop", "Scratch", "Minecraft"], "AARON", "C'est un pionnier de l'art génératif."),
  Q("Que questionnent les machines à peindre ?", ["La place du geste et de l'auteur dans la création", "Le prix de la peinture", "La couleur du papier", "Rien"], "La place du geste et de l'auteur dans la création", "Qui est l'artiste : la machine ou son créateur ?"),
]),
notion('AE-1', 0, D, 'arte-corps-genre-art', [
  Q("Quel groupe d'artistes féministes masquées dénonce l'absence des femmes dans les musées ?", ["Les Guerrilla Girls", "Les Pussy Riot", "Les Suffragettes", "Les Nanas"], "Les Guerrilla Girls", "Elles portent des masques de gorille."),
  Q("Quelle affiche des Guerrilla Girls (1989) demande si les femmes doivent être nues pour entrer au Met ?", ["« Do women have to be naked to get into the Met. Museum? »", "« Keep Calm »", "« We Can Do It! »", "« I want YOU »"], "« Do women have to be naked to get into the Met. Museum? »", "Elle compare nus féminins et artistes femmes."),
  Q("Quelle installation de Judy Chicago rend hommage à 39 femmes célèbres autour d'une table ?", ["The Dinner Party", "La Cène", "Le Déjeuner sur l'herbe", "The Artist Is Present"], "The Dinner Party", "Elle date de 1979."),
]),
# ══ AE-2 · La présence matérielle de l'œuvre dans l'espace ══
notion('AE-2', 0, F, 'arte-echelle-oeuvre', [
  Q("Qu'est-ce qu'une œuvre monumentale ?", ["Une œuvre de très grande taille", "Une œuvre très ancienne", "Une œuvre en bois", "Une œuvre minuscule"], "Une œuvre de très grande taille", "Elle domine le spectateur."),
  Q("Qu'est-ce qu'une miniature en art ?", ["Une œuvre de très petite taille, souvent très détaillée", "Une œuvre géante", "Une œuvre floue", "Une œuvre en mouvement"], "Une œuvre de très petite taille, souvent très détaillée", "Les miniatures persanes sont célèbres."),
  Q("Quelle statue géante domine la baie de Rio de Janeiro ?", ["Le Christ Rédempteur", "La statue de la Liberté", "Le Bouddha de Leshan", "Le Colosse de Rhodes"], "Le Christ Rédempteur", "Elle mesure environ 30 mètres."),
]),
notion('AE-2', 0, F, 'arte-accrochage', [
  Q("Qu'est-ce que l'accrochage d'une exposition ?", ["La façon de disposer les œuvres sur les murs", "La vente des œuvres", "Le transport des œuvres", "Le nettoyage du musée"], "La façon de disposer les œuvres sur les murs", "Il influence le regard du visiteur."),
  Q("Comment appelle-t-on la surface murale où l'on accroche les tableaux ?", ["La cimaise", "Le socle", "Le cartel", "La vitrine"], "La cimaise", "On dit qu'un artiste est « sur les cimaises »."),
  Q("À quoi sert une vitrine dans un musée ?", ["À protéger et présenter des objets fragiles", "À vendre des billets", "À éclairer la salle", "À ranger les balais"], "À protéger et présenter des objets fragiles", "Elle contrôle aussi l'humidité."),
]),
notion('AE-2', 0, F, 'arte-street-art-2', [
  Q("Quelle artiste française écrit des poèmes au pochoir sur les murs de Paris depuis 1985 ?", ["Miss.Tic", "Niki de Saint Phalle", "Louise Bourgeois", "Sophie Calle"], "Miss.Tic", "Elle accompagne ses phrases d'autoportraits."),
  Q("Qu'est-ce qu'une fresque murale (mural) contemporaine ?", ["Une grande peinture sur un mur, souvent dans l'espace public", "Une affiche publicitaire", "Un tableau de musée", "Un graffiti illisible"], "Une grande peinture sur un mur, souvent dans l'espace public", "Les villes en commandent de plus en plus."),
  Q("Le street art est-il toujours autorisé ?", ["Non, il est parfois illégal sans autorisation", "Oui, toujours", "Seulement le dimanche", "Seulement en été"], "Non, il est parfois illégal sans autorisation", "Il pose la question de l'espace public."),
]),
notion('AE-2', 0, F, 'arte-sculptures-jardins', [
  Q("Quel jardin parisien expose des sculptures de Maillol en plein air ?", ["Le jardin des Tuileries", "Le Jardin d'acclimatation", "Le parc Astérix", "Le bois de Vincennes"], "Le jardin des Tuileries", "Près du Louvre."),
  Q("Qu'est-ce qu'un parc de sculptures ?", ["Un espace en plein air où des sculptures sont exposées", "Un musée fermé", "Une carrière", "Une usine"], "Un espace en plein air où des sculptures sont exposées", "La nature dialogue avec les œuvres."),
  Q("Quel château propose chaque année des installations d'art contemporain dans ses jardins depuis 2008 ?", ["Le château de Versailles", "Le château de Chambord", "Le château de Vincennes", "Le château d'If"], "Le château de Versailles", "Koons, Murakami, Kapoor y ont exposé."),
]),
notion('AE-2', 0, F, 'arte-oeuvre-socle', [
  Q("À quoi sert traditionnellement un socle ?", ["À surélever et isoler une sculpture", "À peindre", "À éclairer", "À accrocher un tableau"], "À surélever et isoler une sculpture", "Il sépare l'œuvre du monde ordinaire."),
  Q("Quel sculpteur a fait du socle une partie de ses œuvres, notamment avec des bases taillées ?", ["Constantin Brancusi", "Auguste Rodin", "Michel-Ange", "Donatello"], "Constantin Brancusi", "Socle et sculpture se confondent."),
  Q("Pourquoi certaines sculptures contemporaines sont-elles posées à même le sol ?", ["Pour partager l'espace du spectateur", "Par manque d'argent", "Par oubli", "Pour qu'on les enjambe"], "Pour partager l'espace du spectateur", "Le socle disparaît."),
]),
notion('AE-2', 0, F, 'arte-oeuvre-dehors-dedans', [
  Q("Qu'est-ce que l'art public ?", ["Des œuvres installées dans l'espace public, accessibles à tous", "Des œuvres vendues aux enchères", "Des œuvres privées", "Des œuvres en ligne"], "Des œuvres installées dans l'espace public, accessibles à tous", "Places, gares, parcs…"),
  Q("Quelle sculpture géante de pouce de César se trouve dans un quartier d'affaires de Paris ?", ["Le Pouce, à La Défense", "Le Penseur", "La Liberté", "Le Génie de la Bastille"], "Le Pouce, à La Défense", "Elle mesure 12 mètres."),
  Q("Quelle colonne surmontée d'un ange doré se trouve place de la Bastille ?", ["La colonne de Juillet", "La colonne Vendôme", "La colonne Trajane", "La colonne Morris"], "La colonne de Juillet", "Elle commémore la révolution de 1830."),
]),
notion('AE-2', 0, I, 'arte-white-cube', [
  Q("Comment appelle-t-on l'espace d'exposition aux murs blancs et neutres typique de l'art moderne ?", ["Le white cube (cube blanc)", "Le salon de peinture", "La chapelle", "Le cabinet"], "Le white cube (cube blanc)", "L'expression vient du critique Brian O'Doherty."),
  Q("Pourquoi les musées d'art moderne ont-ils des murs blancs ?", ["Pour isoler l'œuvre et concentrer le regard", "Par économie de peinture", "Pour mieux nettoyer", "Par tradition religieuse"], "Pour isoler l'œuvre et concentrer le regard", "L'espace se veut neutre."),
  Q("Comment étaient accrochés les tableaux dans les Salons du XIXe siècle ?", ["Serrés les uns contre les autres jusqu'au plafond", "Un par mur", "Au sol", "Dans des boîtes"], "Serrés les uns contre les autres jusqu'au plafond", "On parle d'accrochage « à touche-touche »."),
]),
notion('AE-2', 0, I, 'arte-scenographie', [
  Q("Qu'est-ce que la scénographie d'une exposition ?", ["La mise en espace des œuvres, des lumières et du parcours", "Le prix d'entrée", "La vente du catalogue", "Le gardiennage"], "La mise en espace des œuvres, des lumières et du parcours", "Elle guide le visiteur."),
  Q("Pourquoi la lumière est-elle essentielle dans une exposition ?", ["Elle révèle les œuvres mais peut aussi les abîmer", "Elle n'a aucune importance", "Elle sert seulement à la sécurité", "Elle remplace les cartels"], "Elle révèle les œuvres mais peut aussi les abîmer", "Les dessins anciens sont exposés en lumière faible."),
  Q("Qu'est-ce qu'un parcours d'exposition ?", ["L'ordre et le cheminement proposés au visiteur", "Une course à pied", "Une liste de prix", "Un plan de métro"], "L'ordre et le cheminement proposés au visiteur", "Il peut être chronologique ou thématique."),
]),
notion('AE-2', 0, I, 'arte-cabanes-kawamata', [
  Q("Quel artiste japonais construit des cabanes en bois accrochées aux bâtiments et aux arbres ?", ["Tadashi Kawamata", "Takashi Murakami", "Tadao Ando", "Hokusai"], "Tadashi Kawamata", "Il a installé des cabanes au Centre Pompidou."),
  Q("Quel artiste américain tresse des branches pour créer d'immenses huttes ?", ["Patrick Dougherty", "Richard Serra", "Donald Judd", "Jeff Koons"], "Patrick Dougherty", "Ses œuvres se dégradent naturellement."),
  Q("Qu'ont en commun ces œuvres en bois et en branches ?", ["Elles dialoguent avec un lieu et sont souvent éphémères", "Elles sont toujours en musée", "Elles sont en bronze", "Elles sont minuscules"], "Elles dialoguent avec un lieu et sont souvent éphémères", "Ce sont des œuvres in situ."),
]),
notion('AE-2', 0, I, 'arte-biennales', [
  Q("Quelle grande exposition internationale d'art se tient tous les deux ans en Italie ?", ["La Biennale de Venise", "La Documenta", "La FIAC", "Art Basel"], "La Biennale de Venise", "Elle est créée en 1895."),
  Q("Quelle grande exposition d'art contemporain a lieu tous les cinq ans à Kassel, en Allemagne ?", ["La Documenta", "La Biennale de Venise", "Monumenta", "La Nuit blanche"], "La Documenta", "Elle est née en 1955."),
  Q("Quelle manifestation propose chaque automne à Paris des œuvres dans la ville toute la nuit ?", ["La Nuit blanche", "La Fête de la musique", "Les Journées du patrimoine", "La Fête des lumières"], "La Nuit blanche", "Elle existe depuis 2002."),
]),
notion('AE-2', 0, I, 'arte-pignon-ernest', [
  Q("Quel artiste français colle sur les murs des dessins grandeur nature, comme des fantômes dans la ville ?", ["Ernest Pignon-Ernest", "Daniel Buren", "Yves Klein", "Bernar Venet"], "Ernest Pignon-Ernest", "Il est un pionnier de l'art urbain."),
  Q("Pourquoi Ernest Pignon-Ernest choisit-il soigneusement le lieu de ses collages ?", ["Le lieu, son histoire et sa mémoire font partie de l'œuvre", "Par hasard", "Pour trouver des murs lisses", "Pour vendre ses dessins"], "Le lieu, son histoire et sa mémoire font partie de l'œuvre", "Il a collé des images de Rimbaud ou de Pasolini."),
  Q("Quel artiste portugais sculpte des portraits en creusant les murs des immeubles ?", ["Vhils", "JR", "Invader", "Banksy"], "Vhils", "Il utilise burins et explosifs."),
]),
notion('AE-2', 0, I, 'arte-maquette', [
  Q("Qu'est-ce qu'une maquette ?", ["Une représentation en réduction d'un projet ou d'un bâtiment", "Un dessin au crayon", "Une photo", "Un tableau"], "Une représentation en réduction d'un projet ou d'un bâtiment", "Les architectes l'utilisent beaucoup."),
  Q("Qu'est-ce que l'échelle 1 ?", ["La taille réelle", "La moitié de la taille", "Un dixième", "Le double"], "La taille réelle", "Une maquette au 1/100e est cent fois plus petite."),
  Q("Quel artiste américain construit des villages miniatures en argile dans les recoins des villes ?", ["Charles Simonds", "Richard Serra", "Claes Oldenburg", "Ron Mueck"], "Charles Simonds", "Ils sont habités par un « petit peuple » imaginaire."),
]),
notion('AE-2', 0, I, 'arte-presentation-oeuvre', [
  Q("Pourquoi un même tableau peut-il produire un effet différent selon le lieu d'exposition ?", ["La lumière, la hauteur, les murs et les œuvres voisines changent la perception", "Il ne change jamais", "Il change de couleur réellement", "Le cadre disparaît"], "La lumière, la hauteur, les murs et les œuvres voisines changent la perception", "Le dispositif de présentation compte."),
  Q("Qu'est-ce qu'un cadre pour un tableau ?", ["Un encadrement qui protège, isole et met en valeur l'œuvre", "Une partie de la toile", "Une signature", "Un socle"], "Un encadrement qui protège, isole et met en valeur l'œuvre", "Certains artistes le peignent eux-mêmes, comme Seurat."),
  Q("À quelle hauteur accroche-t-on souvent le centre d'un tableau dans un musée ?", ["Environ à hauteur des yeux (1,50 m)", "Au ras du sol", "Au plafond", "À 3 mètres"], "Environ à hauteur des yeux (1,50 m)", "C'est une convention d'accrochage."),
]),
notion('AE-2', 0, D, 'arte-in-situ-buren', [
  Q("Que signifie « in situ » pour Daniel Buren ?", ["L'œuvre est conçue pour un lieu précis et ne peut être déplacée sans perdre son sens", "L'œuvre peut aller n'importe où", "L'œuvre est en atelier", "L'œuvre est sur Internet"], "L'œuvre est conçue pour un lieu précis et ne peut être déplacée sans perdre son sens", "Le lieu fait partie de l'œuvre."),
  Q("Quelle largeur mesurent les bandes de Daniel Buren ?", ["8,7 cm", "1 cm", "50 cm", "1 m"], "8,7 cm", "C'est son « outil visuel »."),
  Q("Quel monument Buren a-t-il recouvert de couleurs pour la Fondation Louis Vuitton en 2016 ?", ["Les verrières du bâtiment de Frank Gehry", "La tour Eiffel", "L'Arc de triomphe", "Notre-Dame"], "Les verrières du bâtiment de Frank Gehry", "L'Observatoire de la lumière."),
]),
notion('AE-2', 0, D, 'arte-monumenta', [
  Q("Quelle manifestation invitait un artiste à occuper seul la nef du Grand Palais ?", ["Monumenta", "La FIAC", "La Biennale", "La Documenta"], "Monumenta", "Kiefer, Serra, Boltanski, Kapoor y ont exposé."),
  Q("Quelle œuvre gonflable géante Anish Kapoor a-t-il installée au Grand Palais en 2011 ?", ["Leviathan", "Cloud Gate", "Descension", "Dirty Corner"], "Leviathan", "Le visiteur pouvait y entrer."),
  Q("Quel défi pose une nef immense comme celle du Grand Palais à un artiste ?", ["Créer une œuvre à l'échelle de l'architecture", "Trouver une petite toile", "Faire du bruit", "Rien"], "Créer une œuvre à l'échelle de l'architecture", "Le rapport d'échelle est central."),
]),
notion('AE-2', 0, D, 'arte-un-pour-cent', [
  Q("Que finance le « 1 % artistique » ?", ["Une œuvre d'art lors de la construction d'un bâtiment public", "Un impôt sur les artistes", "La rénovation des musées", "Les billets d'entrée"], "Une œuvre d'art lors de la construction d'un bâtiment public", "Il existe depuis 1951."),
  Q("Dans quels bâtiments trouve-t-on souvent des œuvres du 1 % ?", ["Les écoles, collèges, lycées et universités", "Les maisons privées", "Les supermarchés", "Les usines privées"], "Les écoles, collèges, lycées et universités", "Votre collège en a peut-être une."),
  Q("Pourquoi ce dispositif est-il important ?", ["Il met l'art contemporain au contact de tous au quotidien", "Il enrichit les architectes", "Il remplace les musées", "Il est obligatoire pour les maisons"], "Il met l'art contemporain au contact de tous au quotidien", "C'est une politique de démocratisation."),
]),
notion('AE-2', 0, D, 'arte-oeuvre-deplacee', [
  Q("Quelle sculpture de Richard Serra (Tilted Arc) a été retirée d'une place de New York après une polémique ?", ["Tilted Arc", "Cloud Gate", "Balloon Dog", "Spiral Jetty"], "Tilted Arc", "Elle a été démontée en 1989."),
  Q("Pourquoi Serra a-t-il refusé que Tilted Arc soit installée ailleurs ?", ["Elle était conçue pour ce lieu précis : la déplacer revenait à la détruire", "Elle était trop lourde", "Elle était cassée", "Il voulait la vendre"], "Elle était conçue pour ce lieu précis : la déplacer revenait à la détruire", "C'est le principe du site-specific."),
  Q("Que montre cette polémique sur l'art public ?", ["L'œuvre peut entrer en conflit avec les usages des habitants", "L'art public plaît toujours", "Les artistes n'ont aucun droit", "L'art public est interdit"], "L'œuvre peut entrer en conflit avec les usages des habitants", "Le débat démocratique fait partie de l'art public."),
]),
notion('AE-2', 0, D, 'arte-ephemere-espace', [
  Q("Quelle installation de Christo et Jeanne-Claude permettait de marcher sur l'eau d'un lac italien en 2016 ?", ["The Floating Piers", "The Gates", "Running Fence", "Surrounded Islands"], "The Floating Piers", "Sur le lac d'Iseo, pendant 16 jours."),
  Q("Comment Christo et Jeanne-Claude finançaient-ils leurs projets ?", ["Par la vente de leurs dessins et maquettes préparatoires", "Par des subventions publiques", "Par des billets d'entrée", "Par des sponsors publicitaires"], "Par la vente de leurs dessins et maquettes préparatoires", "Ils refusaient le mécénat."),
  Q("Pourquoi le caractère éphémère renforce-t-il ces œuvres ?", ["Leur disparition rend l'expérience unique et précieuse", "Il les rend inutiles", "Il les rend moins chères", "Il n'a pas d'effet"], "Leur disparition rend l'expérience unique et précieuse", "Il reste la mémoire et les images."),
]),
notion('AE-2', 0, D, 'arte-architecture-musee', [
  Q("Quel architecte a conçu le musée Guggenheim de New York, en forme de spirale ?", ["Frank Lloyd Wright", "Frank Gehry", "Le Corbusier", "Renzo Piano"], "Frank Lloyd Wright", "Il ouvre en 1959."),
  Q("Quel musée de Lyon, en forme de nuage de verre et d'acier, ouvre en 2014 ?", ["Le musée des Confluences", "Le musée des Beaux-Arts de Lyon", "Le Mucem", "Le Louvre-Lens"], "Le musée des Confluences", "Il est conçu par l'agence Coop Himmelb(l)au."),
  Q("Pourquoi l'architecture d'un musée peut-elle concurrencer les œuvres ?", ["Elle peut devenir elle-même une œuvre spectaculaire", "Elle cache les œuvres", "Elle est toujours neutre", "Elle n'a pas d'importance"], "Elle peut devenir elle-même une œuvre spectaculaire", "On parle d'« effet Bilbao »."),
]),
# ══ AE-3 · L'expérience sensible de l'espace de l'œuvre ══
notion('AE-3', 0, F, 'arte-cathedrale-lumiere', [
  Q("Quel monument parisien, chapelle royale, est presque entièrement fait de vitraux ?", ["La Sainte-Chapelle", "Notre-Dame", "Le Panthéon", "Les Invalides"], "La Sainte-Chapelle", "Saint Louis la fait construire au XIIIe siècle."),
  Q("Quelle impression donne l'intérieur d'une cathédrale gothique ?", ["Une élévation et une lumière colorée qui saisissent le visiteur", "Une sensation d'étroitesse sombre", "Une impression de cave", "Aucune"], "Une élévation et une lumière colorée qui saisissent le visiteur", "L'architecture crée une expérience."),
  Q("Qu'est-ce qu'une rosace dans une église ?", ["Un grand vitrail rond", "Une fleur sculptée", "Un autel", "Une cloche"], "Un grand vitrail rond", "Celles de Notre-Dame sont célèbres."),
]),
notion('AE-3', 0, F, 'arte-jardins', [
  Q("Quel jardinier a dessiné les jardins à la française de Versailles ?", ["André Le Nôtre", "Claude Monet", "Le Corbusier", "Haussmann"], "André Le Nôtre", "Symétrie, perspectives et bassins."),
  Q("Quel jardin célèbre Claude Monet a-t-il créé à Giverny ?", ["Un jardin avec un bassin aux nymphéas et un pont japonais", "Un jardin à la française", "Un jardin zen", "Un potager"], "Un jardin avec un bassin aux nymphéas et un pont japonais", "Il a peint ce jardin pendant des années."),
  Q("Qu'est-ce qu'un jardin zen japonais ?", ["Un jardin sec de pierres et de sable ratissé, propice à la méditation", "Un jardin de légumes", "Un parc d'attractions", "Une forêt"], "Un jardin sec de pierres et de sable ratissé, propice à la méditation", "Celui du Ryōan-ji à Kyoto est célèbre."),
]),
notion('AE-3', 0, F, 'arte-espace-ressenti', [
  Q("Que ressent-on dans un espace très haut et vaste ?", ["Une impression de petitesse ou d'élévation", "Une impression d'étouffement", "Aucune impression", "Une envie de dormir"], "Une impression de petitesse ou d'élévation", "L'espace agit sur le corps."),
  Q("Quels sens peuvent être sollicités par une œuvre dans l'espace ?", ["La vue, l'ouïe, le toucher, parfois l'odorat", "Uniquement la vue", "Uniquement l'ouïe", "Aucun"], "La vue, l'ouïe, le toucher, parfois l'odorat", "L'expérience est globale."),
  Q("Qu'est-ce qu'un labyrinthe en art ?", ["Un parcours complexe qui fait perdre ses repères", "Un tableau abstrait", "Un tunnel droit", "Une salle vide"], "Un parcours complexe qui fait perdre ses repères", "Celui de la cathédrale de Chartres est au sol."),
]),
notion('AE-3', 0, F, 'arte-pantheon-coupole', [
  Q("Quel temple romain possède une immense coupole percée d'une ouverture au sommet ?", ["Le Panthéon de Rome", "Le Colisée", "Le Parthénon", "La basilique Saint-Pierre"], "Le Panthéon de Rome", "L'ouverture s'appelle l'oculus."),
  Q("Qu'est-ce qu'un oculus ?", ["Une ouverture ronde dans un mur ou une coupole", "Un œil peint", "Une lunette", "Une colonne"], "Une ouverture ronde dans un mur ou une coupole", "La lumière tourne avec le soleil."),
  Q("Quel effet produit la lumière de l'oculus dans le Panthéon ?", ["Un rond lumineux qui se déplace au fil de la journée", "Une pièce toujours sombre", "Une lumière artificielle", "Aucun effet"], "Un rond lumineux qui se déplace au fil de la journée", "Le temps devient visible."),
]),
notion('AE-3', 0, F, 'arte-visite-musee', [
  Q("Pourquoi faut-il garder une certaine distance devant une œuvre ?", ["Pour la protéger et mieux la voir dans son ensemble", "Parce qu'elle est dangereuse", "Pour ne pas la sentir", "Par superstition"], "Pour la protéger et mieux la voir dans son ensemble", "Certains détails demandent aussi de s'approcher."),
  Q("Qu'est-ce qu'une médiation au musée ?", ["Un accompagnement qui aide le public à découvrir les œuvres", "Une dispute", "Une vente", "Une restauration"], "Un accompagnement qui aide le public à découvrir les œuvres", "Les médiateurs animent des visites et ateliers."),
  Q("Pourquoi certains musées proposent-ils des visites tactiles ?", ["Pour rendre les œuvres accessibles aux personnes aveugles ou malvoyantes", "Pour salir les œuvres", "Pour gagner du temps", "Par erreur"], "Pour rendre les œuvres accessibles aux personnes aveugles ou malvoyantes", "On touche des reproductions ou certaines sculptures."),
]),
notion('AE-3', 0, I, 'arte-orangerie-nympheas', [
  Q("Dans quel musée parisien les Nymphéas de Monet sont-ils exposés dans deux salles ovales ?", ["Le musée de l'Orangerie", "Le musée d'Orsay", "Le Louvre", "Le musée Marmottan"], "Le musée de l'Orangerie", "Monet a conçu leur présentation."),
  Q("Quel effet produit la disposition des Nymphéas en anneau ?", ["Le spectateur est enveloppé par le paysage d'eau", "Le spectateur ne voit rien", "Les tableaux sont petits", "Un effet de perspective linéaire"], "Le spectateur est enveloppé par le paysage d'eau", "C'est une œuvre immersive avant l'heure."),
  Q("Qu'est-ce qu'un panorama au XIXe siècle ?", ["Une immense peinture circulaire qui entoure le spectateur", "Une photo large", "Un balcon", "Une carte"], "Une immense peinture circulaire qui entoure le spectateur", "Il donnait l'illusion d'être sur place."),
]),
notion('AE-3', 0, I, 'arte-ando-lumiere', [
  Q("Quel architecte japonais a créé l'église de la Lumière, où une croix est découpée dans le béton ?", ["Tadao Ando", "Kenzo Tange", "Toyo Ito", "Kengo Kuma"], "Tadao Ando", "La lumière dessine la croix."),
  Q("Quel matériau Tadao Ando utilise-t-il le plus souvent ?", ["Le béton brut lissé", "Le marbre rose", "Le bois peint", "Le plastique"], "Le béton brut lissé", "Il le travaille avec une grande précision."),
  Q("Quel architecte a conçu la chapelle de Ronchamp, aux murs percés de petites fenêtres colorées ?", ["Le Corbusier", "Tadao Ando", "Jean Nouvel", "Renzo Piano"], "Le Corbusier", "Elle est achevée en 1955."),
]),
notion('AE-3', 0, I, 'arte-son-espace', [
  Q("Qu'est-ce qu'une installation sonore ?", ["Une œuvre qui utilise le son pour transformer la perception d'un espace", "Un concert classique", "Un disque", "Une radio"], "Une œuvre qui utilise le son pour transformer la perception d'un espace", "Le son devient matériau."),
  Q("Quelle artiste canadienne propose des promenades sonores avec casque qui mêlent réel et fiction ?", ["Janet Cardiff", "Laurie Anderson", "Yoko Ono", "Björk"], "Janet Cardiff", "Ses « audio walks » guident le visiteur."),
  Q("Quelle œuvre de Janet Cardiff diffuse un chant à 40 voix par 40 haut-parleurs en cercle ?", ["The Forty Part Motet", "4'33\"", "Clapping Music", "Music for Airports"], "The Forty Part Motet", "On peut circuler entre les voix."),
]),
notion('AE-3', 0, I, 'arte-chapelle-rothko', [
  Q("Dans quelle ville américaine se trouve la chapelle ornée de grandes toiles sombres de Rothko ?", ["Houston", "New York", "Chicago", "Los Angeles"], "Houston", "Elle ouvre en 1971."),
  Q("Quel type d'expérience la chapelle Rothko propose-t-elle ?", ["Une expérience de silence et de méditation", "Une fête", "Un spectacle sonore", "Un parcours sportif"], "Une expérience de silence et de méditation", "Elle accueille toutes les religions."),
  Q("Quel peintre français a réalisé les vitraux et le décor de la chapelle du Rosaire de Vence ?", ["Henri Matisse", "Pierre Soulages", "Marc Chagall", "Fernand Léger"], "Henri Matisse", "Il la considérait comme son chef-d'œuvre."),
]),
notion('AE-3', 0, I, 'arte-temps-oeuvre', [
  Q("Comment le temps peut-il être un matériau de l'œuvre ?", ["Par la durée, le changement, la disparition ou l'attente", "Il ne peut pas l'être", "Uniquement par une horloge", "Uniquement par la date de création"], "Par la durée, le changement, la disparition ou l'attente", "Performance, vidéo, œuvres éphémères…"),
  Q("Quel artiste japonais a peint chaque jour la date du jour sur une toile (Today series) ?", ["On Kawara", "Hokusai", "Yayoi Kusama", "Takashi Murakami"], "On Kawara", "Il a commencé en 1966."),
  Q("Que montre une œuvre qui se transforme avec le temps, comme une sculpture de glace ?", ["Le passage du temps et la fragilité", "Une erreur", "Une œuvre ratée", "Rien"], "Le passage du temps et la fragilité", "Le spectateur assiste à la transformation."),
]),
notion('AE-3', 0, I, 'arte-grottes-experience', [
  Q("Pourquoi les peintures des grottes semblent-elles bouger à la lumière d'une torche ?", ["La flamme vacille et les reliefs de la paroi créent des ombres mouvantes", "Elles sont animées", "Elles sont projetées", "Elles sont en relief métallique"], "La flamme vacille et les reliefs de la paroi créent des ombres mouvantes", "Les artistes utilisaient les reliefs naturels."),
  Q("Pourquoi la grotte de Lascaux a-t-elle été fermée au public en 1963 ?", ["La respiration des visiteurs et les micro-organismes abîmaient les peintures", "Elle était trop dangereuse", "Elle a été inondée", "Elle a été vendue"], "La respiration des visiteurs et les micro-organismes abîmaient les peintures", "On visite des répliques."),
  Q("Comment s'appelle la réplique intégrale de Lascaux ouverte en 2016 ?", ["Lascaux IV", "Lascaux II", "Lascaux Bis", "Chauvet 2"], "Lascaux IV", "Elle se trouve à Montignac."),
]),
notion('AE-3', 0, I, 'arte-parcours-oeuvre', [
  Q("Que signifie « déambuler » dans une œuvre ?", ["Se promener à l'intérieur, la découvrir en se déplaçant", "Rester immobile", "La regarder en photo", "La toucher"], "Se promener à l'intérieur, la découvrir en se déplaçant", "Le corps du visiteur participe."),
  Q("Pourquoi une sculpture en ronde-bosse invite-t-elle à tourner autour ?", ["Elle se découvre sous tous ses angles", "Elle est plate", "Elle est accrochée au mur", "Elle est cachée"], "Elle se découvre sous tous ses angles", "Le bas-relief ne se voit que de face."),
  Q("Quelle œuvre de Serra à Bilbao fait marcher le visiteur entre de hautes parois d'acier courbes ?", ["The Matter of Time", "Tilted Arc", "Spiral Jetty", "Cloud Gate"], "The Matter of Time", "On ressent physiquement l'espace."),
]),
notion('AE-3', 0, I, 'arte-ville-experience', [
  Q("Quelle architecture de Gaudí, à Barcelone, offre des façades ondulantes et un parc coloré ?", ["Le parc Güell et la Casa Batlló", "La tour Eiffel", "Le Louvre", "Le Colisée"], "Le parc Güell et la Casa Batlló", "La Sagrada Família est toujours en construction."),
  Q("Qu'est-ce qu'une dérive selon les situationnistes ?", ["Une promenade sans but pour éprouver la ville autrement", "Un bateau perdu", "Une erreur de carte", "Une course"], "Une promenade sans but pour éprouver la ville autrement", "Guy Debord la théorise en 1956."),
  Q("Quelle promenade plantée parisienne a inspiré la High Line de New York ?", ["La Coulée verte René-Dumont", "Les Champs-Élysées", "Le jardin du Luxembourg", "Les Buttes-Chaumont"], "La Coulée verte René-Dumont", "Elle suit une ancienne voie ferrée."),
]),
notion('AE-3', 0, I, 'arte-miroirs-espace', [
  Q("Quelle salle du château de Versailles multiplie l'espace grâce à 357 miroirs ?", ["La galerie des Glaces", "La chapelle royale", "L'Opéra", "La chambre du roi"], "La galerie des Glaces", "Elle est achevée en 1684."),
  Q("Quel effet produisent des miroirs face à face ?", ["Une impression d'espace infini", "Une pièce plus sombre", "Une pièce plus petite", "Aucun effet"], "Une impression d'espace infini", "Kusama l'utilise dans ses Infinity Rooms."),
  Q("Pourquoi les miroirs étaient-ils un luxe au XVIIe siècle ?", ["Leur fabrication était difficile et venait surtout de Venise", "Ils étaient interdits", "Ils étaient en or", "Ils n'existaient pas"], "Leur fabrication était difficile et venait surtout de Venise", "Colbert crée une manufacture française pour concurrencer Venise."),
]),
notion('AE-3', 0, D, 'arte-turrell-roden', [
  Q("Quel projet colossal James Turrell transforme-t-il en observatoire de lumière dans un volcan d'Arizona ?", ["Le Roden Crater", "Spiral Jetty", "Lightning Field", "Sun Tunnels"], "Le Roden Crater", "Le chantier dure depuis les années 1970."),
  Q("Qu'est-ce qu'un « Ganzfeld » chez Turrell ?", ["Un espace où l'on perd tout repère visuel dans une lumière uniforme", "Un champ de blé", "Une photo", "Un tableau abstrait"], "Un espace où l'on perd tout repère visuel dans une lumière uniforme", "Le visiteur ne voit plus les murs."),
  Q("Que cherche à faire percevoir James Turrell ?", ["La lumière elle-même et l'acte de voir", "Des objets précis", "Des portraits", "Des paysages peints"], "La lumière elle-même et l'acte de voir", "Il dit : « Mon œuvre, c'est votre perception »."),
]),
notion('AE-3', 0, D, 'arte-merleau-ponty', [
  Q("Quel philosophe français a écrit sur la peinture et la perception dans L'Œil et l'Esprit (1961) ?", ["Maurice Merleau-Ponty", "Jean-Paul Sartre", "Albert Camus", "Michel Foucault"], "Maurice Merleau-Ponty", "Il s'intéresse beaucoup à Cézanne."),
  Q("Qu'est-ce que la phénoménologie appliquée à l'art ?", ["L'étude de l'expérience vécue de l'œuvre par le corps et les sens", "L'étude des prix", "L'histoire des artistes", "La chimie des couleurs"], "L'étude de l'expérience vécue de l'œuvre par le corps et les sens", "Elle a influencé l'art minimal."),
  Q("Quel philosophe allemand a analysé l'œuvre d'art et le lieu dans L'Origine de l'œuvre d'art ?", ["Martin Heidegger", "Emmanuel Kant", "Hegel", "Nietzsche"], "Martin Heidegger", "Il prend l'exemple d'un temple grec."),
]),
notion('AE-3', 0, D, 'arte-memoriaux', [
  Q("Quel mémorial de Berlin est composé de 2 711 stèles de béton de hauteurs différentes ?", ["Le Mémorial aux Juifs assassinés d'Europe", "La porte de Brandebourg", "Le Reichstag", "Le mur de Berlin"], "Le Mémorial aux Juifs assassinés d'Europe", "Conçu par Peter Eisenman, il ouvre en 2005."),
  Q("Quel mémorial de Washington, conçu par Maya Lin, est un long mur noir gravé de noms ?", ["Le Vietnam Veterans Memorial", "Le Lincoln Memorial", "Le Washington Monument", "Le Capitole"], "Le Vietnam Veterans Memorial", "Le visiteur voit son reflet dans le granit."),
  Q("Quelle expérience proposent ces mémoriaux ?", ["Une expérience physique du deuil, du vide et de la mémoire", "Un divertissement", "Une visite commerciale", "Aucune expérience"], "Une expérience physique du deuil, du vide et de la mémoire", "Le corps du visiteur est engagé."),
]),
notion('AE-3', 0, D, 'arte-installation-totale', [
  Q("Quel artiste russe a créé des « installations totales », comme des appartements soviétiques reconstitués ?", ["Ilya Kabakov", "Kasimir Malevitch", "Marc Chagall", "Wassily Kandinsky"], "Ilya Kabakov", "Le visiteur entre dans une fiction."),
  Q("Quelle œuvre de Kabakov montre un homme qui s'est envolé de sa chambre ?", ["L'Homme qui s'est envolé dans l'espace", "Le Saut dans le vide", "Icare", "Le Voyageur"], "L'Homme qui s'est envolé dans l'espace", "Elle est au Centre Pompidou."),
  Q("Qu'est-ce qu'une installation « totale » ?", ["Un environnement complet qui englobe le visiteur dans un monde", "Un tableau accroché", "Une petite sculpture", "Une photo"], "Un environnement complet qui englobe le visiteur dans un monde", "Tous les éléments contribuent à l'expérience."),
]),
notion('AE-3', 0, D, 'arte-boltanski-memoire-espace', [
  Q("Quelle installation de Boltanski au Grand Palais (2010) présentait des tonnes de vêtements et une grue ?", ["Personnes", "Leviathan", "Monumenta Kiefer", "Les Archives du cœur"], "Personnes", "La grue saisissait des vêtements au hasard."),
  Q("Quel projet de Boltanski enregistre les battements de cœur de milliers de personnes sur une île japonaise ?", ["Les Archives du cœur", "Personnes", "Animitas", "Monuments"], "Les Archives du cœur", "Sur l'île de Teshima."),
  Q("Quel sentiment cherche souvent à provoquer Boltanski ?", ["Une émotion liée à la mémoire, à l'absence et à la mort", "Le rire", "La colère", "L'ennui"], "Une émotion liée à la mémoire, à l'absence et à la mort", "Il parle d'« art du souvenir »."),
]),
notion('AE-3', 0, D, 'arte-paysage-sublime', [
  Q("Quel peintre romantique allemand a peint Le Voyageur contemplant une mer de nuages ?", ["Caspar David Friedrich", "William Turner", "Eugène Delacroix", "John Constable"], "Caspar David Friedrich", "Il date de 1818 environ."),
  Q("Qu'est-ce que le sublime en art selon les romantiques ?", ["Une émotion mêlée d'effroi face à la grandeur de la nature", "Une beauté calme et douce", "Un style géométrique", "Une couleur"], "Une émotion mêlée d'effroi face à la grandeur de la nature", "Burke et Kant l'ont théorisé."),
  Q("Pourquoi Friedrich peint-il souvent ses personnages de dos ?", ["Pour que le spectateur s'identifie à eux face au paysage", "Parce qu'il ne savait pas peindre les visages", "Par hasard", "Pour cacher ses modèles"], "Pour que le spectateur s'identifie à eux face au paysage", "On parle de Rückenfigur."),
]),
notion('AE-3', 0, D, 'arte-odorat-art', [
  Q("Une œuvre peut-elle solliciter l'odorat ?", ["Oui, certains artistes utilisent des odeurs", "Non, jamais", "Seulement en cuisine", "Seulement en parfumerie"], "Oui, certains artistes utilisent des odeurs", "Wolfgang Laib utilise du pollen et de la cire d'abeille."),
  Q("Quel artiste brésilien crée des sculptures souples remplies d'épices odorantes ?", ["Ernesto Neto", "Vik Muniz", "Romero Britto", "Oscar Niemeyer"], "Ernesto Neto", "Le visiteur peut parfois y entrer."),
  Q("Pourquoi certains artistes sollicitent-ils plusieurs sens ?", ["Pour créer une expérience plus complète et intime", "Pour faire peur", "Pour vendre des parfums", "Par erreur"], "Pour créer une expérience plus complète et intime", "On parle d'art multisensoriel."),
]),
notion('AE-3', 0, D, 'arte-espace-represente', [
  Q("Quel peintre de la Renaissance a représenté un espace architectural parfait dans L'École d'Athènes ?", ["Raphaël", "Léonard de Vinci", "Botticelli", "Titien"], "Raphaël", "La perspective converge vers Platon et Aristote."),
  Q("Quelle différence y a-t-il entre l'espace représenté et l'espace réel de l'œuvre ?", ["L'un est une illusion dans l'image, l'autre est le lieu physique où se trouve l'œuvre", "Ils sont identiques", "L'espace réel est imaginaire", "L'espace représenté est toujours en 3D"], "L'un est une illusion dans l'image, l'autre est le lieu physique où se trouve l'œuvre", "Le programme distingue espace perçu, ressenti et représenté."),
  Q("Quel peintre a peint des plafonds en trompe-l'œil donnant l'illusion que le ciel s'ouvre (quadratura) ?", ["Andrea Pozzo", "Vermeer", "Monet", "Seurat"], "Andrea Pozzo", "Plafond de l'église Saint-Ignace à Rome."),
]),
notion('AE-3', 0, D, 'arte-skyspace-lumiere-naturelle', [
  Q("Qu'est-ce qu'un « skyspace » de James Turrell ?", ["Une pièce ouverte sur le ciel par une ouverture découpée dans le plafond", "Un avion", "Un planétarium", "Un écran de cinéma"], "Une pièce ouverte sur le ciel par une ouverture découpée dans le plafond", "Le ciel devient tableau."),
  Q("Quel moment de la journée est privilégié pour vivre un skyspace ?", ["Le lever ou le coucher du soleil", "Midi uniquement", "La nuit noire", "N'importe quand sans différence"], "Le lever ou le coucher du soleil", "Les couleurs du ciel changent avec la lumière intérieure."),
  Q("Que montre cette œuvre sur la couleur du ciel ?", ["Elle dépend de la lumière qui l'entoure et de notre perception", "Elle est toujours bleue", "Elle est peinte", "Elle ne change jamais"], "Elle dépend de la lumière qui l'entoure et de notre perception", "Comme le montrait Albers avec la couleur."),
]),
# ══ AE-4 · Les métissages entre arts plastiques et technologies numériques ══
notion('AE-4', 0, F, 'arte-art-et-sciences', [
  Q("Les artistes ont-ils toujours utilisé les nouvelles technologies de leur époque ?", ["Oui, de la perspective à la photo et au numérique", "Non, jamais", "Seulement aujourd'hui", "Seulement au Moyen Âge"], "Oui, de la perspective à la photo et au numérique", "L'art et la technique avancent ensemble."),
  Q("Quel inventeur-artiste a imaginé des machines volantes à la Renaissance ?", ["Léonard de Vinci", "Raphaël", "Michel-Ange", "Botticelli"], "Léonard de Vinci", "Ses carnets en sont remplis."),
  Q("Qu'est-ce qu'un artiste-ingénieur ?", ["Un artiste qui associe création et invention technique", "Un ingénieur sans imagination", "Un vendeur d'outils", "Un architecte"], "Un artiste qui associe création et invention technique", "Tinguely ou Calder en sont des exemples."),
]),
notion('AE-4', 0, F, 'arte-public-participe', [
  Q("Que signifie une œuvre « participative » ?", ["Le public contribue à créer ou transformer l'œuvre", "Le public paie plus", "Le public ne peut pas entrer", "Le public la regarde de loin"], "Le public contribue à créer ou transformer l'œuvre", "Le spectateur devient co-auteur."),
  Q("Quelle œuvre de Yayoi Kusama invite les visiteurs à coller des gommettes dans une pièce blanche ?", ["The Obliteration Room", "Infinity Mirror Room", "Pumpkin", "Narcissus Garden"], "The Obliteration Room", "La pièce se couvre peu à peu de points colorés."),
  Q("Quelle place le numérique donne-t-il souvent au public ?", ["Il peut interagir, partager et créer à partir des œuvres", "Aucune", "Il doit rester silencieux", "Il ne peut que regarder"], "Il peut interagir, partager et créer à partir des œuvres", "Les frontières entre créateur et public bougent."),
]),
notion('AE-4', 0, F, 'arte-drones-spectacle', [
  Q("Quelle technologie remplace parfois les feux d'artifice par des centaines de lumières volantes ?", ["Les spectacles de drones", "Les ballons", "Les lasers fixes", "Les lampions"], "Les spectacles de drones", "Ils dessinent des formes dans le ciel."),
  Q("Pourquoi certains préfèrent-ils les drones aux feux d'artifice ?", ["Ils ne font pas de bruit ni de fumée polluante", "Ils sont plus anciens", "Ils explosent", "Ils sont gratuits"], "Ils ne font pas de bruit ni de fumée polluante", "Ils sont réutilisables."),
  Q("Quel studio néerlandais crée des installations poétiques avec des drones et de la lumière ?", ["Studio Drift", "teamLab", "Ghibli", "Pixar"], "Studio Drift", "Franchise Freedom évoque un vol d'étourneaux."),
]),
notion('AE-4', 0, F, 'arte-oeuvre-a-distance', [
  Q("Peut-on aujourd'hui découvrir une œuvre à distance ?", ["Oui, grâce aux images, vidéos et visites virtuelles", "Non, jamais", "Seulement par lettre", "Seulement à la radio"], "Oui, grâce aux images, vidéos et visites virtuelles", "Mais l'expérience n'est pas la même."),
  Q("Que perd-on en regardant une œuvre sur un écran plutôt qu'en vrai ?", ["La taille réelle, la matière et la présence physique", "Rien", "La couleur exacte", "Le titre"], "La taille réelle, la matière et la présence physique", "L'écran uniformise les œuvres."),
  Q("Que gagne-t-on parfois grâce aux images numériques en haute définition ?", ["La possibilité de voir des détails invisibles à l'œil nu", "Le toucher", "L'odeur", "Le poids de l'œuvre"], "La possibilité de voir des détails invisibles à l'œil nu", "Le projet Gigapixel permet de zoomer très loin."),
]),
notion('AE-4', 0, F, 'arte-robots-artistes', [
  Q("Un robot peut-il peindre ?", ["Oui, s'il est programmé pour cela", "Non, jamais", "Seulement des murs", "Seulement en noir"], "Oui, s'il est programmé pour cela", "Mais qui est alors l'auteur ?"),
  Q("Quel robot humanoïde a exposé des tableaux en 2019 et été présenté comme « artiste » ?", ["Ai-Da", "R2-D2", "WALL-E", "Nao"], "Ai-Da", "Il a été créé au Royaume-Uni."),
  Q("Quelle question posent les robots artistes ?", ["Qu'est-ce qu'un artiste et qu'est-ce que la création ?", "Combien coûte un robot ?", "Quelle est la couleur du robot ?", "Aucune"], "Qu'est-ce qu'un artiste et qu'est-ce que la création ?", "C'est un débat philosophique."),
]),
notion('AE-4', 0, F, 'arte-tech-musique-image', [
  Q("Quel musicien français est un pionnier de la musique électronique avec Oxygène (1976) ?", ["Jean-Michel Jarre", "Daft Punk", "Serge Gainsbourg", "Johnny Hallyday"], "Jean-Michel Jarre", "Il a aussi donné des concerts géants avec lasers."),
  Q("Quel duo français de musique électronique portait des casques de robots ?", ["Daft Punk", "Justice", "Air", "Cassius"], "Daft Punk", "Il s'est séparé en 2021."),
  Q("Pourquoi les concerts électroniques sont-ils souvent aussi des spectacles visuels ?", ["Ils associent musique, lumière, vidéo et scénographie", "Ils n'ont pas de musique", "Ils sont silencieux", "Ils sont interdits"], "Ils associent musique, lumière, vidéo et scénographie", "C'est un art total."),
]),
notion('AE-4', 0, F, 'arte-videoprojection', [
  Q("Qu'est-ce qu'un vidéoprojecteur ?", ["Un appareil qui projette des images sur une surface", "Un appareil photo", "Une télévision portable", "Un ordinateur"], "Un appareil qui projette des images sur une surface", "Les artistes s'en servent pour transformer les lieux."),
  Q("Quelle surface peut recevoir une projection artistique ?", ["Un mur, un bâtiment, un objet, l'eau ou même de la fumée", "Uniquement un écran blanc", "Uniquement une toile", "Aucune"], "Un mur, un bâtiment, un objet, l'eau ou même de la fumée", "Le support transforme l'image."),
  Q("Qu'est-ce qu'une boucle vidéo dans une installation ?", ["Une vidéo qui se répète sans fin", "Une vidéo arrêtée", "Une vidéo en noir", "Un film long"], "Une vidéo qui se répète sans fin", "Le visiteur peut entrer à tout moment."),
]),
notion('AE-4', 0, F, 'arte-art-et-jeu', [
  Q("Qu'est-ce qu'un « serious game » ?", ["Un jeu vidéo conçu pour apprendre ou sensibiliser", "Un jeu de société sérieux", "Un concours", "Un jeu interdit"], "Un jeu vidéo conçu pour apprendre ou sensibiliser", "Des musées en proposent."),
  Q("Quel musée parisien a consacré une grande exposition aux jeux vidéo en 2011 ?", ["Le Grand Palais (Game Story)", "Le Louvre", "Le musée Rodin", "Le musée de Cluny"], "Le Grand Palais (Game Story)", "Le jeu vidéo entre dans les institutions."),
  Q("Pourquoi le jeu vidéo est-il parfois appelé « dixième art » ?", ["Il mêle image, son, récit, architecture et interaction", "Il est le plus ancien", "Il est le plus cher", "Il est le plus simple"], "Il mêle image, son, récit, architecture et interaction", "Le cinéma est le septième art."),
]),
notion('AE-4', 0, I, 'arte-rafael-lozano', [
  Q("Quel artiste mexicano-canadien crée des installations interactives géantes réagissant au public ?", ["Rafael Lozano-Hemmer", "Diego Rivera", "Frida Kahlo", "Gabriel Orozco"], "Rafael Lozano-Hemmer", "Pulse Room capte les battements de cœur."),
  Q("Que fait l'installation Pulse Room de Lozano-Hemmer ?", ["Elle fait clignoter des ampoules au rythme des cœurs des visiteurs", "Elle diffuse de la musique", "Elle projette un film", "Elle mesure la taille"], "Elle fait clignoter des ampoules au rythme des cœurs des visiteurs", "Le corps devient lumière."),
  Q("Quelle est la place du public dans ces œuvres ?", ["Sans lui, l'œuvre ne fonctionne pas", "Il est inutile", "Il doit rester dehors", "Il paie seulement"], "Sans lui, l'œuvre ne fonctionne pas", "Il est le moteur de l'œuvre."),
]),
notion('AE-4', 0, I, 'arte-rain-room', [
  Q("Quelle installation permet de marcher sous une pluie artificielle sans être mouillé ?", ["Rain Room (Random International)", "The Weather Project", "Cloud Gate", "Infinity Room"], "Rain Room (Random International)", "Des capteurs arrêtent la pluie au-dessus des visiteurs."),
  Q("Quelle technologie rend possible la Rain Room ?", ["Des caméras 3D qui détectent les mouvements", "Des parapluies", "Un toit", "Des ventilateurs"], "Des caméras 3D qui détectent les mouvements", "L'œuvre réagit en temps réel."),
  Q("Quelle sensation crée la Rain Room ?", ["Une impression de pouvoir sur la nature, entre émerveillement et inquiétude", "La peur de l'eau", "L'ennui", "La faim"], "Une impression de pouvoir sur la nature, entre émerveillement et inquiétude", "Elle a été exposée au MoMA en 2013."),
]),
notion('AE-4', 0, I, 'arte-anadol-donnees', [
  Q("Quel artiste turco-américain transforme des données en peintures numériques mouvantes ?", ["Refik Anadol", "Ai Weiwei", "Banksy", "Jeff Koons"], "Refik Anadol", "Il utilise l'intelligence artificielle."),
  Q("Quelle œuvre d'Anadol au MoMA (2022) s'appuyait sur les données de la collection du musée ?", ["Unsupervised", "Starry Night", "Infinity", "Data Wall"], "Unsupervised", "Une IA « rêve » à partir des œuvres."),
  Q("Pourquoi ces œuvres font-elles débat ?", ["On se demande si elles sont de l'art ou du simple spectacle technologique", "Elles sont trop petites", "Elles sont en noir et blanc", "Elles n'ont pas de public"], "On se demande si elles sont de l'art ou du simple spectacle technologique", "Le débat est ouvert."),
]),
notion('AE-4', 0, I, 'arte-musee-numerique-mediation', [
  Q("Comment les musées utilisent-ils les tablettes et applications ?", ["Pour proposer des jeux, des commentaires et des zooms sur les œuvres", "Pour remplacer les œuvres", "Pour fermer les salles", "Pour vendre des tablettes"], "Pour proposer des jeux, des commentaires et des zooms sur les œuvres", "La médiation numérique se développe."),
  Q("Qu'est-ce qu'une Micro-Folie ?", ["Un musée numérique installé dans une petite ville ou un quartier", "Une petite folie architecturale", "Un jeu vidéo", "Une chanson"], "Un musée numérique installé dans une petite ville ou un quartier", "Le dispositif est coordonné par La Villette."),
  Q("Quel est l'objectif des Micro-Folies ?", ["Rendre les chefs-d'œuvre des musées accessibles partout", "Remplacer les musées", "Vendre des œuvres", "Former des informaticiens"], "Rendre les chefs-d'œuvre des musées accessibles partout", "Il en existe des centaines en France."),
]),
notion('AE-4', 0, I, 'arte-strandbeest', [
  Q("Quel artiste néerlandais construit des « animaux de plage » mus par le vent ?", ["Theo Jansen", "Piet Mondrian", "Rembrandt", "Escher"], "Theo Jansen", "Les Strandbeests marchent sur le sable."),
  Q("En quel matériau sont faits les Strandbeests ?", ["En tubes de plastique jaunes", "En marbre", "En bois massif", "En acier rouillé"], "En tubes de plastique jaunes", "Ils sont conçus grâce à des calculs informatiques."),
  Q("Pourquoi les Strandbeests mêlent-ils art et science ?", ["Ils combinent ingénierie, mécanique, informatique et poésie", "Ce sont des robots militaires", "Ce sont des jouets d'enfants", "Ce sont des voitures"], "Ils combinent ingénierie, mécanique, informatique et poésie", "Jansen parle de « nouvelles formes de vie »."),
]),
notion('AE-4', 0, I, 'arte-bjork-biophilia', [
  Q("Quelle chanteuse islandaise a sorti un album sous forme d'applications interactives (Biophilia, 2011) ?", ["Björk", "Adele", "Madonna", "Beyoncé"], "Björk", "Chaque chanson est une application."),
  Q("Quelle artiste américaine mêle musique, performance et technologie depuis les années 1980 ?", ["Laurie Anderson", "Taylor Swift", "Patti Smith", "Joan Baez"], "Laurie Anderson", "Elle a été artiste en résidence à la NASA."),
  Q("Qu'est-ce qu'une œuvre multimédia ?", ["Une œuvre qui combine plusieurs médias (image, son, texte, interaction)", "Une œuvre en un seul matériau", "Une peinture à l'huile", "Une sculpture en bronze"], "Une œuvre qui combine plusieurs médias (image, son, texte, interaction)", "Le numérique favorise ces mélanges."),
]),
notion('AE-4', 0, I, 'arte-co-creation-internet', [
  Q("Quel projet de l'artiste Aaron Koblin a fait dessiner des milliers de moutons par des internautes ?", ["The Sheep Market", "Minecraft", "Wikipedia", "Second Life"], "The Sheep Market", "Chaque internaute était payé 2 centimes."),
  Q("Qu'est-ce que le crowdsourcing en art ?", ["Faire participer un grand nombre d'internautes à une œuvre", "Vendre aux enchères", "Peindre", "Copier une œuvre"], "Faire participer un grand nombre d'internautes à une œuvre", "L'auteur devient collectif."),
  Q("Quelle question pose une œuvre créée par des milliers d'anonymes ?", ["Qui en est l'auteur ?", "Quelle est sa couleur ?", "Combien pèse-t-elle ?", "Aucune"], "Qui en est l'auteur ?", "La notion d'artiste évolue."),
]),
notion('AE-4', 0, D, 'arte-auteur-numerique', [
  Q("Qu'est-ce qu'une œuvre open source ?", ["Une œuvre dont le code ou les fichiers sont partagés librement", "Une œuvre secrète", "Une œuvre vendue très cher", "Une œuvre détruite"], "Une œuvre dont le code ou les fichiers sont partagés librement", "Chacun peut la modifier."),
  Q("Quel théoricien a parlé de la « mort de l'auteur » en 1967 ?", ["Roland Barthes", "Jean-Paul Sartre", "Albert Camus", "Claude Lévi-Strauss"], "Roland Barthes", "Le sens de l'œuvre naît aussi chez le lecteur."),
  Q("Pourquoi le numérique remet-il en question la notion d'œuvre unique ?", ["Les fichiers se copient, se modifient et circulent à l'infini", "Il interdit les copies", "Il rend les œuvres plus lourdes", "Il n'a aucun effet"], "Les fichiers se copient, se modifient et circulent à l'infini", "L'original devient difficile à définir."),
]),
notion('AE-4', 0, D, 'arte-esthetique-relationnelle', [
  Q("Quel critique français a théorisé l'« esthétique relationnelle » en 1998 ?", ["Nicolas Bourriaud", "Pierre Restany", "André Malraux", "Daniel Arasse"], "Nicolas Bourriaud", "L'œuvre crée des relations entre les gens."),
  Q("Quel artiste thaïlandais cuisinait et servait des repas dans les galeries ?", ["Rirkrit Tiravanija", "Ai Weiwei", "Yayoi Kusama", "Takashi Murakami"], "Rirkrit Tiravanija", "Le partage devient l'œuvre."),
  Q("Que devient le spectateur dans l'esthétique relationnelle ?", ["Un participant à une situation sociale créée par l'artiste", "Un simple regardeur", "Un acheteur", "Un gardien"], "Un participant à une situation sociale créée par l'artiste", "Les réseaux numériques prolongent cette idée."),
]),
notion('AE-4', 0, D, 'arte-art-genetique-vivant', [
  Q("Qu'est-ce que l'« art transgénique » ?", ["Un art qui utilise la modification génétique d'êtres vivants", "Un art de la peinture classique", "Un art du jardin", "Un art de la cuisine"], "Un art qui utilise la modification génétique d'êtres vivants", "Eduardo Kac en est un pionnier."),
  Q("Pourquoi ces pratiques posent-elles des questions éthiques ?", ["Elles touchent au vivant et aux limites de la manipulation", "Elles sont trop colorées", "Elles sont trop petites", "Elles sont gratuites"], "Elles touchent au vivant et aux limites de la manipulation", "Le débat dépasse l'art."),
  Q("Quel laboratoire-atelier australien, SymbioticA, accueille des artistes ?", ["Un laboratoire de biologie de l'université d'Australie-Occidentale", "Un musée de peinture", "Un studio de cinéma", "Une école de danse"], "Un laboratoire de biologie de l'université d'Australie-Occidentale", "Artistes et scientifiques y collaborent."),
]),
notion('AE-4', 0, D, 'arte-paik-robot', [
  Q("Quel artiste a assemblé des téléviseurs pour créer des « robots » sculptures ?", ["Nam June Paik", "Bill Viola", "Andy Warhol", "Jean Tinguely"], "Nam June Paik", "Family of Robot (1986)."),
  Q("Quelle expression Nam June Paik a-t-il employée dès 1974, annonçant Internet ?", ["« Electronic super highway »", "« World Wide Web »", "« Cyberspace »", "« Metaverse »"], "« Electronic super highway »", "Il imaginait un réseau mondial de communication."),
  Q("Pourquoi Paik est-il considéré comme un précurseur ?", ["Il a fait de la télévision et de la vidéo un matériau artistique avant tout le monde", "Il a inventé la télévision", "Il a créé Internet", "Il a fondé YouTube"], "Il a fait de la télévision et de la vidéo un matériau artistique avant tout le monde", "Il appartenait aussi à Fluxus."),
]),
notion('AE-4', 0, D, 'arte-metavers', [
  Q("Qu'est-ce qu'un métavers ?", ["Un univers virtuel partagé où l'on évolue avec un avatar", "Un poème", "Un musée réel", "Un vers de poésie"], "Un univers virtuel partagé où l'on évolue avec un avatar", "Le mot vient du roman Snow Crash (1992)."),
  Q("Pourquoi des artistes exposent-ils dans des mondes virtuels ?", ["Pour toucher un nouveau public et inventer d'autres formes d'expositions", "Parce que les musées sont fermés", "Par obligation", "Pour cacher leurs œuvres"], "Pour toucher un nouveau public et inventer d'autres formes d'expositions", "Des galeries existent dans des jeux en ligne."),
  Q("Quel concert virtuel d'un rappeur américain dans Fortnite a réuni plus de 12 millions de joueurs en 2020 ?", ["Travis Scott", "Eminem", "Jay-Z", "Kanye West"], "Travis Scott", "La frontière entre concert, jeu et art s'efface."),
]),
notion('AE-4', 0, D, 'arte-ia-statut-artiste', [
  Q("Une œuvre générée par IA a remporté un concours d'art dans le Colorado en 2022. Quel débat cela a-t-il suscité ?", ["Celui de la place de l'artiste et de la légitimité de ces images", "Celui du prix des pinceaux", "Celui de la taille des toiles", "Aucun"], "Celui de la place de l'artiste et de la légitimité de ces images", "L'œuvre s'appelait Théâtre d'opéra spatial."),
  Q("Qu'est-ce qu'un « artiste augmenté » ?", ["Un artiste qui intègre les outils numériques et l'IA à sa pratique", "Un artiste plus grand", "Un artiste célèbre", "Un artiste-robot"], "Un artiste qui intègre les outils numériques et l'IA à sa pratique", "L'outil ne remplace pas l'intention."),
  Q("Qu'est-ce qui distingue encore l'artiste de l'outil numérique selon beaucoup de théoriciens ?", ["L'intention, le choix et le sens qu'il donne à l'œuvre", "La vitesse", "Le prix", "La couleur"], "L'intention, le choix et le sens qu'il donne à l'œuvre", "La question reste ouverte."),
]),
notion('AE-4', 0, D, 'arte-oeuvre-processus', [
  Q("Qu'est-ce qu'une œuvre « processuelle » ?", ["Une œuvre dont le processus de fabrication ou d'évolution est montré", "Une œuvre achevée et fixe", "Une œuvre ancienne", "Une œuvre secrète"], "Une œuvre dont le processus de fabrication ou d'évolution est montré", "Le temps et le changement font l'œuvre."),
  Q("Quel avantage le numérique offre-t-il pour garder la trace d'un processus ?", ["L'enregistrement et l'historique de chaque étape", "Il efface tout", "Il interdit les essais", "Il rend tout aléatoire"], "L'enregistrement et l'historique de chaque étape", "On peut rejouer la création."),
  Q("Quel peintre britannique montre en vidéo, trait par trait, la naissance de ses dessins sur iPad ?", ["David Hockney", "Francis Bacon", "William Turner", "Lucian Freud"], "David Hockney", "Le spectateur voit le dessin naître."),
]),
notion('AE-4', 0, D, 'arte-musee-ia-conservation', [
  Q("Comment l'IA aide-t-elle aujourd'hui les musées ?", ["À analyser, attribuer et restaurer virtuellement des œuvres", "À remplacer les gardiens", "À vendre les tableaux", "À peindre de nouvelles Joconde"], "À analyser, attribuer et restaurer virtuellement des œuvres", "Elle a reconstitué les bords coupés de La Ronde de nuit de Rembrandt."),
  Q("Quel tableau de Rembrandt a été complété virtuellement par IA en 2021 au Rijksmuseum ?", ["La Ronde de nuit", "La Leçon d'anatomie", "La Fiancée juive", "Les Syndics"], "La Ronde de nuit", "Ses bords avaient été coupés au XVIIIe siècle."),
  Q("Quelle limite présente cette restauration virtuelle ?", ["C'est une hypothèse et non l'œuvre originale", "Elle est fausse à 100 %", "Elle détruit l'œuvre", "Elle n'a aucune limite"], "C'est une hypothèse et non l'œuvre originale", "Les ajouts sont présentés à part."),
]),
]

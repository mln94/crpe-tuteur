# Anglais · Repères culturels, 5e : Portrait, autoportrait ; Le quotidien : lieux, rythmes, saisons ; Le réel et l'imaginaire (25 questions par niveau)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ C5-1 · Portrait, autoportrait ══
notion('C5-1', 0, F, 'ang5-selfie', [
  Q("Comment appelle-t-on une photo de soi prise avec son téléphone ?", ["Un selfie", "Un portrait officiel", "Un paysage", "Un poster"], "Un selfie", "Le mot entre dans le dictionnaire Oxford en 2013."),
  Q("Que signifie « to take a picture » ?", ["Prendre une photo", "Peindre un tableau", "Acheter un cadre", "Regarder un film"], "Prendre une photo", "Picture = image, photo."),
  Q("Que signifie « smile! » quand on prend une photo ?", ["Souriez !", "Bougez !", "Fermez les yeux !", "Partez !"], "Souriez !", "On dit aussi « Say cheese! »."),
]),
notion('C5-1', 0, F, 'ang5-visage', [
  Q("Comment dit-on « le nez » en anglais ?", ["The nose", "The mouth", "The ear", "The chin"], "The nose", "Mouth = bouche, ear = oreille, chin = menton."),
  Q("Que signifie « cheeks » ?", ["Les joues", "Les sourcils", "Les lèvres", "Le front"], "Les joues", "Eyebrows = sourcils, lips = lèvres."),
  Q("Comment dit-on « une barbe » ?", ["A beard", "A moustache", "A fringe", "A bun"], "A beard", "Fringe = frange, bun = chignon."),
]),
notion('C5-1', 0, F, 'ang5-vetements', [
  Q("Que signifie « hoodie » ?", ["Un sweat à capuche", "Un manteau long", "Une cravate", "Un pantalon"], "Un sweat à capuche", "Hood = capuche."),
  Q("Comment dit-on « une jupe » ?", ["A skirt", "A shirt", "A dress", "A coat"], "A skirt", "Shirt = chemise, dress = robe."),
  Q("Que signifie « She is wearing a hat » ?", ["Elle porte un chapeau.", "Elle achète un chapeau.", "Elle a perdu son chapeau.", "Elle fabrique un chapeau."], "Elle porte un chapeau.", "Be + wearing : ce qu'elle porte en ce moment."),
]),
notion('C5-1', 0, F, 'ang5-portrait-musee', [
  Q("Quel tableau de Léonard de Vinci est le portrait le plus célèbre du monde ?", ["La Joconde (Mona Lisa)", "La Jeune Fille à la perle", "Les Ménines", "Le Cri"], "La Joconde (Mona Lisa)", "En anglais, on l'appelle Mona Lisa."),
  Q("Que signifie « self-portrait » ?", ["Un autoportrait", "Un portrait de groupe", "Un paysage", "Une caricature"], "Un autoportrait", "Self = soi-même."),
  Q("Que signifie « frame » à propos d'un tableau ?", ["Le cadre", "La toile", "Le pinceau", "Le musée"], "Le cadre", "Canvas = toile."),
]),
notion('C5-1', 0, F, 'ang5-adjectifs-personnalite', [
  Q("Que signifie « shy » ?", ["Timide", "Bavard", "Courageux", "Malin"], "Timide", "Talkative = bavard."),
  Q("Comment dit-on « intelligent, malin » ?", ["Clever (smart)", "Lazy", "Rude", "Selfish"], "Clever (smart)", "Selfish = égoïste."),
  Q("Que signifie « hard-working » ?", ["Travailleur", "Paresseux", "Dur", "Fatigué"], "Travailleur", "Lazy = paresseux."),
]),
notion('C5-1', 0, F, 'ang5-profil-reseaux', [
  Q("Que signifie « profile picture » ?", ["La photo de profil", "Un tableau de profil", "Une carte d'identité", "Un dessin animé"], "La photo de profil", "C'est l'image qui nous représente en ligne."),
  Q("Que signifie « to post » sur les réseaux sociaux ?", ["Publier", "Supprimer", "Envoyer une lettre", "Bloquer"], "Publier", "A post = une publication."),
  Q("Comment dit-on « un abonné » sur les réseaux sociaux ?", ["A follower", "A leader", "A fan club", "A member"], "A follower", "To follow = suivre."),
]),
notion('C5-1', 0, F, 'ang5-se-decrire', [
  Q("Comment dit-on « J'ai les cheveux courts et blonds » ?", ["I've got short blond hair.", "I have hairs short blond.", "I am short blond hair.", "My hair are short and blond."], "I've got short blond hair.", "Hair est indénombrable et singulier."),
  Q("Que signifie « I'm quite tall » ?", ["Je suis assez grand.", "Je suis très petit.", "Je suis trop grand.", "Je suis grand comme mon père."], "Je suis assez grand.", "Quite = assez, very = très."),
  Q("Que signifie « I look like my mother » ?", ["Je ressemble à ma mère.", "Je regarde ma mère.", "J'aime ma mère.", "Je cherche ma mère."], "Je ressemble à ma mère.", "To look like = ressembler à."),
]),
notion('C5-1', 0, F, 'ang5-photo-famille', [
  Q("Comment dit-on « une photo de famille » ?", ["A family photo", "A photo family", "A familial picture", "A family's photograph of"], "A family photo", "Le nom complément se place devant."),
  Q("Que signifie « on the left » dans la description d'une photo ?", ["À gauche", "À droite", "Au centre", "En bas"], "À gauche", "On the right = à droite, in the middle = au milieu."),
  Q("Que signifie « in the background » ?", ["À l'arrière-plan", "Au premier plan", "Au centre", "Dans le cadre"], "À l'arrière-plan", "In the foreground = au premier plan."),
]),
notion('C5-1', 0, I, 'ang5i-portraits-royaux', [
  Q("Sur quels objets du quotidien figure le portrait du souverain britannique ?", ["Les billets, les pièces et les timbres", "Les plaques d'immatriculation", "Les cartes d'identité", "Les panneaux routiers"], "Les billets, les pièces et les timbres", "Les billets à l'effigie de Charles III circulent depuis 2024."),
  Q("Quel portrait de la reine Élisabeth Ire montre sa main posée sur un globe ?", ["Le portrait de l'Armada", "Le portrait d'Arnolfini", "La Joconde", "Les Ménines"], "Le portrait de l'Armada", "Il célèbre la victoire de 1588 contre l'Espagne."),
  Q("Quel artiste a réalisé une série de portraits colorés de la reine Élisabeth II en 1985 ?", ["Andy Warhol", "Pablo Picasso", "Claude Monet", "Banksy"], "Andy Warhol", "La série s'appelle Reigning Queens."),
]),
notion('C5-1', 0, I, 'ang5i-mount-rushmore', [
  Q("Quel monument américain représente quatre présidents sculptés dans la montagne ?", ["Le mont Rushmore", "Le Lincoln Memorial", "La statue de la Liberté", "Le Capitole"], "Le mont Rushmore", "Il se trouve dans le Dakota du Sud."),
  Q("Quels présidents figurent sur le mont Rushmore ?", ["Washington, Jefferson, Theodore Roosevelt et Lincoln", "Kennedy, Obama, Reagan et Nixon", "Washington, Adams, Madison et Monroe", "Lincoln, Grant, Lee et Davis"], "Washington, Jefferson, Theodore Roosevelt et Lincoln", "Ils symbolisent la naissance et l'expansion du pays."),
  Q("Le site du mont Rushmore est-il sacré pour un peuple amérindien ?", ["Oui, pour les Lakotas (Sioux)", "Non, il était désert", "Oui, pour les Inuits", "Oui, pour les Maoris"], "Oui, pour les Lakotas (Sioux)", "Ils l'appellent les Six Grands-Pères."),
]),
notion('C5-1', 0, I, 'ang5i-vermeer-rembrandt', [
  Q("Quel tableau de Vermeer est surnommé « la Joconde du Nord » ?", ["La Jeune Fille à la perle", "La Ronde de nuit", "La Laitière", "Le Cri"], "La Jeune Fille à la perle", "En anglais : Girl with a Pearl Earring."),
  Q("Quel peintre néerlandais a réalisé plus de 80 autoportraits au XVIIe siècle ?", ["Rembrandt", "Vermeer", "Van Eyck", "Rubens"], "Rembrandt", "On peut y suivre son vieillissement."),
  Q("Quel peintre a réalisé de nombreux autoportraits, dont un avec l'oreille bandée ?", ["Vincent van Gogh", "Picasso", "Monet", "Dalí"], "Vincent van Gogh", "Plusieurs sont exposés à Londres et à New York."),
]),
notion('C5-1', 0, I, 'ang5i-frida-kahlo', [
  Q("Quelle artiste mexicaine est célèbre pour ses autoportraits aux sourcils épais ?", ["Frida Kahlo", "Georgia O'Keeffe", "Tamara de Lempicka", "Yayoi Kusama"], "Frida Kahlo", "Elle peint plus de 50 autoportraits."),
  Q("Pourquoi Frida Kahlo peint-elle souvent son propre visage ?", ["Immobilisée après un accident, elle se peint dans un miroir", "Parce qu'elle n'a pas de modèle à payer, sans autre raison", "Par obligation d'école", "Elle ne peint jamais son visage"], "Immobilisée après un accident, elle se peint dans un miroir", "« Je me peins parce que je suis le sujet que je connais le mieux »."),
  Q("Quelle peintre américaine est célèbre pour ses grandes fleurs et ses paysages du Nouveau-Mexique ?", ["Georgia O'Keeffe", "Frida Kahlo", "Mary Cassatt", "Louise Bourgeois"], "Georgia O'Keeffe", "Elle est une figure du modernisme américain."),
]),
notion('C5-1', 0, I, 'ang5i-describe-picture', [
  Q("Comment commencer la description d'une image en anglais ?", ["This picture shows…", "This picture is showing me that…", "In this picture we are…", "The picture says to me…"], "This picture shows…", "On peut aussi dire : In this picture, I can see…"),
  Q("Que signifie « at the top » ?", ["En haut", "En bas", "Au fond", "À côté"], "En haut", "At the bottom = en bas."),
  Q("Que signifie « It seems that… » ?", ["Il semble que…", "Il faut que…", "Il est sûr que…", "Il dit que…"], "Il semble que…", "Pour faire des hypothèses."),
]),
notion('C5-1', 0, I, 'ang5i-modal-may-might', [
  Q("Que signifie « He may be sad » ?", ["Il est peut-être triste.", "Il doit être triste.", "Il veut être triste.", "Il a été triste."], "Il est peut-être triste.", "May / might expriment une éventualité."),
  Q("Complétez : « She ___ be his sister, they look alike. » (déduction forte)", ["must", "can't", "mustn't", "should"], "must", "Must = sûrement, dans une déduction."),
  Q("Que signifie « He can't be the thief » ?", ["Ce ne peut pas être lui le voleur.", "Il ne sait pas voler.", "Il n'a pas le droit de voler.", "Il ne peut pas être volé."], "Ce ne peut pas être lui le voleur.", "Can't = c'est impossible."),
]),
notion('C5-1', 0, I, 'ang5i-caricature', [
  Q("Qu'est-ce qu'une caricature ?", ["Un portrait qui exagère les traits pour faire rire ou critiquer", "Un autoportrait sérieux", "Une photo officielle", "Une statue"], "Un portrait qui exagère les traits pour faire rire ou critiquer", "La presse britannique en publie beaucoup."),
  Q("Comment dit-on « dessin animé » en anglais ?", ["A cartoon", "A drawing", "A comic", "A sketch"], "A cartoon", "Un cartoonist dessine des caricatures."),
  Q("Quel magazine satirique britannique, créé en 1841, était célèbre pour ses caricatures ?", ["Punch", "Time", "The Economist", "Vogue"], "Punch", "Il a cessé de paraître en 2002."),
]),
notion('C5-1', 0, I, 'ang5i-identite-numerique', [
  Q("Que signifie « privacy settings » ?", ["Les paramètres de confidentialité", "Les réglages de l'écran", "Les mots de passe", "Les abonnements"], "Les paramètres de confidentialité", "Ils décident qui voit nos publications."),
  Q("Que signifie « fake profile » ?", ["Un faux profil", "Un profil privé", "Un profil vérifié", "Un profil oublié"], "Un faux profil", "Fake = faux."),
  Q("Que signifie « to share » une photo ?", ["La partager", "La supprimer", "La modifier", "L'imprimer"], "La partager", "Il faut l'accord des personnes photographiées."),
]),
notion('C5-1', 0, D, 'ang5d-portraits-presidentiels', [
  Q("Quelle artiste a peint le portrait officiel de Michelle Obama en 2018 ?", ["Amy Sherald", "Frida Kahlo", "Annie Leibovitz", "Yayoi Kusama"], "Amy Sherald", "Kehinde Wiley a peint celui de Barack Obama."),
  Q("Dans quel musée de Washington sont exposés les portraits officiels des présidents ?", ["La National Portrait Gallery (Smithsonian)", "Le MoMA", "Le Louvre", "La Tate Britain"], "La National Portrait Gallery (Smithsonian)", "Il existe aussi une National Portrait Gallery à Londres."),
  Q("Quelle photographe américaine est célèbre pour ses portraits de stars dans Vanity Fair ?", ["Annie Leibovitz", "Dorothea Lange", "Vivian Maier", "Cindy Sherman"], "Annie Leibovitz", "Elle a photographié Élisabeth II en 2007."),
]),
notion('C5-1', 0, D, 'ang5d-cindy-sherman', [
  Q("Quelle artiste américaine se photographie déguisée en différents personnages ?", ["Cindy Sherman", "Annie Leibovitz", "Frida Kahlo", "Georgia O'Keeffe"], "Cindy Sherman", "Elle interroge l'identité et les stéréotypes."),
  Q("Quelle photographe américaine a pris Migrant Mother pendant la Grande Dépression ?", ["Dorothea Lange", "Diane Arbus", "Cindy Sherman", "Annie Leibovitz"], "Dorothea Lange", "La photo date de 1936."),
  Q("Quelle nourrice américaine a pris des milliers de photos de rue, découvertes après sa mort ?", ["Vivian Maier", "Dorothea Lange", "Berenice Abbott", "Lee Miller"], "Vivian Maier", "Ses négatifs ont été retrouvés en 2007."),
]),
notion('C5-1', 0, D, 'ang5d-dorian-gray', [
  Q("Dans quel roman d'Oscar Wilde un portrait vieillit-il à la place de son modèle ?", ["Le Portrait de Dorian Gray", "Frankenstein", "Dracula", "Jane Eyre"], "Le Portrait de Dorian Gray", "Il paraît en 1890."),
  Q("De quel pays Oscar Wilde est-il originaire ?", ["L'Irlande", "L'Écosse", "Les États-Unis", "Le pays de Galles"], "L'Irlande", "Il est né à Dublin en 1854."),
  Q("Quelle comédie d'Oscar Wilde joue sur le prénom « Ernest » ?", ["The Importance of Being Earnest", "Hamlet", "Pygmalion", "Mrs Dalloway"], "The Importance of Being Earnest", "Earnest = sérieux."),
]),
notion('C5-1', 0, D, 'ang5d-present-perfect-experience', [
  Q("Complétez : « Have you ever ___ a self-portrait? » (paint)", ["painted", "paint", "painting", "paints"], "painted", "Present perfect : have + participe passé."),
  Q("Que signifie « I have never been to London » ?", ["Je ne suis jamais allé à Londres.", "Je ne vais jamais à Londres.", "Je n'irai jamais à Londres.", "Je n'étais pas à Londres."], "Je ne suis jamais allé à Londres.", "Le present perfect exprime l'expérience."),
  Q("Quel est le participe passé de « take » ?", ["taken", "took", "taked", "take"], "taken", "Take, took, taken."),
]),
notion('C5-1', 0, D, 'ang5d-national-portrait-gallery', [
  Q("Près de quelle place de Londres se trouve la National Portrait Gallery ?", ["Trafalgar Square", "Piccadilly Circus", "Leicester Square", "Times Square"], "Trafalgar Square", "Elle ouvre en 1856."),
  Q("Quel peintre a réalisé le portrait d'Henri VIII le plus célèbre ?", ["Hans Holbein le Jeune", "Rembrandt", "Turner", "Gainsborough"], "Hans Holbein le Jeune", "Il était peintre de la cour d'Angleterre."),
  Q("Quel peintre anglais du XVIIIe siècle est célèbre pour The Blue Boy ?", ["Thomas Gainsborough", "William Turner", "John Constable", "David Hockney"], "Thomas Gainsborough", "Le tableau est aujourd'hui en Californie."),
]),
notion('C5-1', 0, D, 'ang5d-jane-eyre-autobio', [
  Q("Quel roman de Charlotte Brontë, raconté à la première personne, suit une orpheline devenue gouvernante ?", ["Jane Eyre", "Les Hauts de Hurlevent", "Orgueil et Préjugés", "Emma"], "Jane Eyre", "Il paraît en 1847."),
  Q("Comment appelle-t-on le récit de sa propre vie ?", ["Une autobiographie", "Une biographie", "Une fable", "Un roman policier"], "Une autobiographie", "Une biographie raconte la vie d'un autre."),
  Q("Quel journal intime d'une adolescente a été traduit en anglais sous le titre The Diary of a Young Girl ?", ["Le Journal d'Anne Frank", "Le Journal de Bridget Jones", "Les Mémoires de Churchill", "Le Journal de Samuel Pepys"], "Le Journal d'Anne Frank", "Il paraît en néerlandais en 1947."),
]),
notion('C5-1', 0, D, 'ang5d-phrasal-verbs-look', [
  Q("Que signifie « to look after » ?", ["S'occuper de", "Chercher", "Ressembler à", "Admirer"], "S'occuper de", "She looks after her little brother."),
  Q("Que signifie « to look up to someone » ?", ["Admirer quelqu'un", "Regarder en haut", "Chercher quelqu'un", "Mépriser quelqu'un"], "Admirer quelqu'un", "To look down on = mépriser."),
  Q("Que signifie « to look for » ?", ["Chercher", "Regarder", "Trouver", "Garder"], "Chercher", "I'm looking for my keys."),
]),
notion('C5-1', 0, D, 'ang5d-hockney-ipad', [
  Q("Quel peintre britannique crée depuis les années 2010 des portraits et paysages sur iPad ?", ["David Hockney", "Banksy", "Damien Hirst", "Lucian Freud"], "David Hockney", "Il montre que le portrait se renouvelle avec le numérique."),
  Q("Quel peintre britannique, petit-fils de Sigmund Freud, a peint des portraits très réalistes ?", ["Lucian Freud", "Francis Bacon", "David Hockney", "Henry Moore"], "Lucian Freud", "Il a peint un portrait d'Élisabeth II en 2001."),
  Q("Quel peintre irlandais est célèbre pour ses portraits déformés et tourmentés ?", ["Francis Bacon", "Lucian Freud", "Jack Yeats", "Turner"], "Francis Bacon", "Il est né à Dublin en 1909."),
]),
# ══ C5-2 · Le quotidien : lieux, rythmes, saisons ══
notion('C5-2', 0, F, 'ang5-lieux-ville', [
  Q("Comment dit-on « la gare » en anglais ?", ["The train station", "The bus stop", "The airport", "The harbour"], "The train station", "Bus stop = arrêt de bus."),
  Q("Que signifie « library » ?", ["Bibliothèque", "Librairie", "Laboratoire", "Liberté"], "Bibliothèque", "Faux ami : librairie = bookshop."),
  Q("Comment dit-on « la boulangerie » ?", ["The bakery", "The butcher's", "The chemist's", "The grocery"], "The bakery", "Chemist's = pharmacie (GB)."),
]),
notion('C5-2', 0, F, 'ang5-moments-journee', [
  Q("Que signifie « in the evening » ?", ["Le soir", "Le matin", "L'après-midi", "La nuit"], "Le soir", "In the morning, in the afternoon, at night."),
  Q("Comment dit-on « la nuit » avec la bonne préposition ?", ["At night", "In night", "On night", "By night only"], "At night", "On dit in the morning mais at night."),
  Q("Que signifie « at noon » ?", ["À midi", "À minuit", "Le matin", "Le soir"], "À midi", "Midnight = minuit."),
]),
notion('C5-2', 0, F, 'ang5-saisons-activites', [
  Q("Que fait-on souvent en hiver au Canada ?", ["Du hockey sur glace et du ski", "Du surf", "De la plongée", "Des barbecues sur la plage"], "Du hockey sur glace et du ski", "Le hockey est le sport national d'hiver."),
  Q("Que signifie « spring » ?", ["Le printemps", "L'été", "L'automne", "L'hiver"], "Le printemps", "Spring signifie aussi « ressort » et « source »."),
  Q("Que signifie « snowman » ?", ["Un bonhomme de neige", "Un skieur", "Un flocon", "Un ours polaire"], "Un bonhomme de neige", "Snow = neige."),
]),
notion('C5-2', 0, F, 'ang5-dates', [
  Q("Comment dit-on « le 1er mai » en anglais ?", ["May the first (1st May)", "May one", "The one of May", "First of the May month"], "May the first (1st May)", "On utilise les nombres ordinaux pour les dates."),
  Q("Comment lit-on « 1066 » en anglais ?", ["Ten sixty-six", "One thousand sixty-six only", "One zero six six", "Ten six six"], "Ten sixty-six", "On lit souvent les années par paires."),
  Q("Complétez : « My birthday is ___ July. »", ["in", "on", "at", "of"], "in", "In + mois ; on + date précise (on 4th July)."),
]),
notion('C5-2', 0, F, 'ang5-transports-quotidien', [
  Q("Comment dit-on « Je vais à l'école à pied » ?", ["I walk to school.", "I go to school by feet.", "I foot to school.", "I go at school walking."], "I walk to school.", "On dit aussi : I go to school on foot."),
  Q("Complétez : « I go to school ___ bus. »", ["by", "with", "in", "on the"], "by", "By bus, by car, by train."),
  Q("Que signifie « school bus » ?", ["Le car scolaire", "Le bus de nuit", "Le tramway", "Le taxi"], "Le car scolaire", "Les cars scolaires jaunes sont un symbole des États-Unis."),
]),
notion('C5-2', 0, F, 'ang5-repas-us', [
  Q("Qu'est-ce qu'un « hot dog » ?", ["Une saucisse dans un petit pain", "Un chien malade", "Un hamburger", "Une soupe"], "Une saucisse dans un petit pain", "C'est un classique américain."),
  Q("Que mangent souvent les Américains au petit-déjeuner avec du sirop d'érable ?", ["Des pancakes", "Des croissants", "Du riz", "Des frites"], "Des pancakes", "Les pancakes américains sont épais."),
  Q("Que signifie « dessert » ?", ["Le dessert", "Le désert", "Le dîner", "Le déjeuner"], "Le dessert", "Attention : desert (un seul s) = désert."),
]),
notion('C5-2', 0, I, 'ang5i-fuseaux-horaires', [
  Q("Combien de fuseaux horaires couvrent les États-Unis continentaux ?", ["Quatre", "Un", "Deux", "Dix"], "Quatre", "Eastern, Central, Mountain et Pacific."),
  Q("Quelle heure est-il à Londres quand il est midi à Paris (en hiver) ?", ["11 heures", "13 heures", "Midi", "6 heures"], "11 heures", "Le Royaume-Uni a une heure de moins que la France."),
  Q("Quel méridien, référence des fuseaux horaires, passe par un quartier de Londres ?", ["Le méridien de Greenwich", "Le méridien de Paris", "L'équateur", "Le tropique du Cancer"], "Le méridien de Greenwich", "On parle d'heure GMT."),
]),
notion('C5-2', 0, I, 'ang5i-noel-traditions', [
  Q("Que trouvent les enfants britanniques au pied de leur lit le matin de Noël ?", ["Un bas (stocking) rempli de cadeaux", "Des œufs en chocolat", "Une citrouille", "Un feu d'artifice"], "Un bas (stocking) rempli de cadeaux", "On l'accroche à la cheminée."),
  Q("Quel dessert traditionnel britannique est servi flambé à Noël ?", ["Le Christmas pudding", "Le cheesecake", "L'apple pie", "Le brownie"], "Le Christmas pudding", "Il est préparé des semaines à l'avance."),
  Q("Que sont les « crackers » de Noël britanniques ?", ["Des papillotes qui claquent et contiennent une couronne en papier et une blague", "Des biscuits salés", "Des pétards de rue", "Des cadeaux de grande valeur"], "Des papillotes qui claquent et contiennent une couronne en papier et une blague", "On les ouvre à deux en tirant."),
]),
notion('C5-2', 0, I, 'ang5i-preferences-routines', [
  Q("Complétez : « She usually ___ her homework after dinner. » (do)", ["does", "do", "is doing", "did"], "does", "Usually + présent simple pour une habitude."),
  Q("Que signifie « once a week » ?", ["Une fois par semaine", "Une fois dans la semaine dernière", "Chaque jour", "Deux fois par semaine"], "Une fois par semaine", "Twice a week = deux fois par semaine."),
  Q("Comment demande-t-on à quelle fréquence quelqu'un fait du sport ?", ["How often do you do sport?", "How many do you do sport?", "When often you do sport?", "How much time sport?"], "How often do you do sport?", "How often… ? = à quelle fréquence ?"),
]),
notion('C5-2', 0, I, 'ang5i-vivre-campagne', [
  Q("Que signifie « countryside » ?", ["La campagne", "Le pays", "La ville", "La banlieue"], "La campagne", "Country = pays (ou campagne)."),
  Q("Comment dit-on « une ferme » ?", ["A farm", "A firm", "A field", "A barn"], "A farm", "Firm = entreprise, field = champ, barn = grange."),
  Q("Quelle région anglaise est célèbre pour ses villages de pierre dorée et ses collines ?", ["Les Cotswolds", "Les Highlands", "Le Lake District", "Les Midlands industriels"], "Les Cotswolds", "Elles sont classées « zone de beauté naturelle »."),
]),
notion('C5-2', 0, I, 'ang5i-vacances-ecole', [
  Q("Comment appelle-t-on les vacances d'été aux États-Unis ?", ["Summer vacation (ou summer break)", "Summer holiday camp", "Half-term", "Spring break only"], "Summer vacation (ou summer break)", "Au Royaume-Uni, on dit summer holidays."),
  Q("Qu'est-ce que le « half-term » au Royaume-Uni ?", ["Une semaine de vacances au milieu d'un trimestre", "Un examen de mi-année", "La moitié d'une journée de cours", "Un demi-tarif"], "Une semaine de vacances au milieu d'un trimestre", "L'année est divisée en trois trimestres (terms)."),
  Q("Qu'est-ce qu'un « summer camp » aux États-Unis ?", ["Une colonie de vacances", "Un camping familial", "Un camp militaire", "Une école d'été obligatoire"], "Une colonie de vacances", "Beaucoup d'enfants américains y partent l'été."),
]),
notion('C5-2', 0, I, 'ang5i-maisons-gb', [
  Q("Comment appelle-t-on une maison accolée à d'autres en rangée au Royaume-Uni ?", ["A terraced house", "A detached house", "A bungalow", "A cottage"], "A terraced house", "Detached = individuelle, semi-detached = jumelée."),
  Q("Qu'est-ce qu'un « cottage » ?", ["Une petite maison de campagne", "Un immeuble", "Un château", "Une cabane d'arbre"], "Une petite maison de campagne", "Souvent avec un toit de chaume."),
  Q("Qu'est-ce qu'un « bungalow » ?", ["Une maison de plain-pied", "Une maison de trois étages", "Un appartement", "Une tente"], "Une maison de plain-pied", "Le mot vient de l'hindi."),
]),
notion('C5-2', 0, I, 'ang5i-rythmes-usa', [
  Q("Que signifie « rush hour » ?", ["L'heure de pointe", "L'heure du déjeuner", "L'heure du coucher", "L'heure d'été"], "L'heure de pointe", "Les transports sont bondés."),
  Q("Que signifie « daylight saving time » ?", ["L'heure d'été", "Le lever du soleil", "La journée de travail", "Les congés payés"], "L'heure d'été", "Les montres avancent d'une heure au printemps."),
  Q("Que signifie « 24/7 » (twenty-four seven) ?", ["Tout le temps, jour et nuit", "Le 24 juillet", "24 heures par semaine", "De 7 heures à 24 heures"], "Tout le temps, jour et nuit", "24 heures sur 24, 7 jours sur 7."),
]),
notion('C5-2', 0, I, 'ang5i-prepositions-temps', [
  Q("Complétez : « See you ___ Monday! »", ["on", "in", "at", "by"], "on", "On + jour."),
  Q("Complétez : « The film starts ___ 8 o'clock. »", ["at", "in", "on", "for"], "at", "At + heure."),
  Q("Complétez : « I was born ___ 2013. »", ["in", "on", "at", "since"], "in", "In + année, mois, saison."),
]),
notion('C5-2', 0, I, 'ang5i-fetes-religieuses', [
  Q("Quelle fête chrétienne de printemps est célébrée avec des œufs en chocolat ?", ["Easter (Pâques)", "Christmas", "Halloween", "Thanksgiving"], "Easter (Pâques)", "On organise des chasses aux œufs (egg hunts)."),
  Q("Quelle fête hindoue des lumières est très célébrée à Londres et à Leicester ?", ["Diwali", "Hanoukka", "Ramadan", "Holi"], "Diwali", "Le Royaume-Uni compte une importante communauté d'origine indienne."),
  Q("Quel animal apporte les œufs de Pâques dans les pays anglophones ?", ["Le lapin (Easter Bunny)", "Les cloches", "Le père Noël", "Une poule rouge"], "Le lapin (Easter Bunny)", "En France, ce sont souvent les cloches."),
]),
notion('C5-2', 0, D, 'ang5d-seasons-australia', [
  Q("En quelle saison fête-t-on Noël en Australie ?", ["En été", "En hiver", "Au printemps", "En automne"], "En été", "Beaucoup d'Australiens font un barbecue sur la plage."),
  Q("Qu'est-ce que l'« Australia Day » ?", ["La fête nationale australienne, le 26 janvier", "Le jour de l'indépendance en juillet", "Un festival de surf", "Le jour de Noël"], "La fête nationale australienne, le 26 janvier", "Elle est contestée par des Aborigènes, qui y voient un jour d'invasion."),
  Q("Pourquoi les saisons sont-elles inversées entre l'hémisphère Nord et l'hémisphère Sud ?", ["À cause de l'inclinaison de l'axe de la Terre", "À cause de la distance au Soleil", "À cause des océans", "À cause de la Lune"], "À cause de l'inclinaison de l'axe de la Terre", "Ce n'est pas la distance au Soleil."),
]),
notion('C5-2', 0, D, 'ang5d-used-to', [
  Q("Que signifie « I used to live in London » ?", ["J'habitais à Londres autrefois (mais plus maintenant).", "J'ai l'habitude de vivre à Londres.", "J'utilise Londres.", "J'habiterai à Londres."], "J'habitais à Londres autrefois (mais plus maintenant).", "Used to + base verbale : une habitude passée révolue."),
  Q("Quelle est la forme négative de « He used to play rugby » ?", ["He didn't use to play rugby.", "He usedn't to play rugby.", "He didn't used play rugby.", "He not used to play rugby."], "He didn't use to play rugby.", "Didn't + use to."),
  Q("Que signifie « I'm used to getting up early » ?", ["J'ai l'habitude de me lever tôt.", "Je me levais tôt autrefois.", "Je me lèverai tôt.", "J'utilise le réveil tôt."], "J'ai l'habitude de me lever tôt.", "Be used to + V-ing = être habitué à."),
]),
notion('C5-2', 0, D, 'ang5d-heure-gb-us', [
  Q("Comment les Américains écrivent-ils souvent la date du 4 juillet 2026 ?", ["7/4/2026", "4/7/2026", "2026/4/7", "4-VII-2026"], "7/4/2026", "Mois / jour / année aux États-Unis ; jour / mois / année au Royaume-Uni."),
  Q("Que signifie « a fortnight » en anglais britannique ?", ["Quinze jours", "Quatre nuits", "Un mois", "Une semaine"], "Quinze jours", "Fourteen nights."),
  Q("Que signifie « the day after tomorrow » ?", ["Après-demain", "Avant-hier", "Demain", "La semaine prochaine"], "Après-demain", "The day before yesterday = avant-hier."),
]),
notion('C5-2', 0, D, 'ang5d-vie-rurale-us', [
  Q("Qu'est-ce qu'un « ranch » aux États-Unis ?", ["Une grande exploitation d'élevage", "Une petite maison de ville", "Un champ de coton uniquement", "Une forêt"], "Une grande exploitation d'élevage", "Les cow-boys y gardent le bétail."),
  Q("Quelle communauté religieuse de Pennsylvanie vit sans électricité ni voiture ?", ["Les Amish", "Les Mormons", "Les Quakers", "Les Puritains"], "Les Amish", "Ils se déplacent en carriole à cheval."),
  Q("Qu'est-ce que le « Midwest » ?", ["Une région agricole du centre-nord des États-Unis", "Une région du Royaume-Uni", "Une côte de l'Australie", "Une province canadienne"], "Une région agricole du centre-nord des États-Unis", "On l'appelle le « grenier » de l'Amérique."),
]),
notion('C5-2', 0, D, 'ang5d-calendrier-gb', [
  Q("Qu'est-ce qu'un « bank holiday » au Royaume-Uni ?", ["Un jour férié", "Un jour où seules les banques ouvrent", "Un congé payé de cinq semaines", "Un jour de grève"], "Un jour férié", "Le nom vient de la fermeture des banques."),
  Q("Quelle fête écossaise célèbre le Nouvel An ?", ["Hogmanay", "Burns Night", "St Andrew's Day", "Halloween"], "Hogmanay", "Édimbourg organise de grandes festivités."),
  Q("Quel jour fête-t-on la Saint-Georges, patron de l'Angleterre ?", ["Le 23 avril", "Le 17 mars", "Le 30 novembre", "Le 1er mars"], "Le 23 avril", "C'est aussi l'anniversaire présumé de Shakespeare."),
]),
notion('C5-2', 0, D, 'ang5d-meteo-extremes', [
  Q("Comment appelle-t-on les violentes tornades fréquentes dans les plaines du centre des États-Unis ?", ["Tornadoes (la Tornado Alley)", "Typhoons", "Monsoons", "Blizzards uniquement"], "Tornadoes (la Tornado Alley)", "Le Kansas et l'Oklahoma sont très touchés."),
  Q("Que signifie « heatwave » ?", ["Une vague de chaleur", "Une vague de froid", "Une tempête de sable", "Un tsunami"], "Une vague de chaleur", "Cold snap = coup de froid."),
  Q("Qu'est-ce qu'un « blizzard » ?", ["Une violente tempête de neige", "Un orage d'été", "Un vent chaud", "Une sécheresse"], "Une violente tempête de neige", "Il touche le Canada et le nord des États-Unis."),
]),
notion('C5-2', 0, D, 'ang5d-futur-projets', [
  Q("Complétez : « Next summer, we ___ visit Scotland. » (projet décidé)", ["are going to", "will to", "going", "are go to"], "are going to", "Be going to : un projet, une intention."),
  Q("Complétez : « Look at the clouds! It ___ rain. »", ["is going to", "will to", "goes", "rains"], "is going to", "Be going to : une prévision fondée sur un indice présent."),
  Q("Complétez : « I think it ___ be sunny tomorrow. »", ["will", "is going", "goes to", "shall to"], "will", "Will pour une prédiction."),
]),
notion('C5-2', 0, D, 'ang5d-pub-culture', [
  Q("Qu'est-ce qu'un « pub » au Royaume-Uni ?", ["Un lieu de convivialité où l'on boit et parfois mange", "Une publicité", "Un club de sport", "Une école"], "Un lieu de convivialité où l'on boit et parfois mange", "Public house."),
  Q("Qu'est-ce que le « Sunday roast » ?", ["Le rôti du dimanche, avec légumes et Yorkshire pudding", "Un barbecue d'été", "Un petit-déjeuner du dimanche", "Une pâtisserie"], "Le rôti du dimanche, avec légumes et Yorkshire pudding", "C'est un repas familial traditionnel."),
  Q("Qu'est-ce qu'un « diner » aux États-Unis ?", ["Un petit restaurant populaire", "Le repas du soir uniquement", "Un dîner de gala", "Une cantine scolaire"], "Un petit restaurant populaire", "Souvent avec banquettes et comptoir."),
]),
notion('C5-2', 0, D, 'ang5d-greenwich-big-ben', [
  Q("Pourquoi le méridien d'origine passe-t-il par Greenwich ?", ["Une conférence internationale l'a choisi en 1884", "C'est le centre de la Terre", "Par hasard", "Parce que Londres est la capitale de l'Europe"], "Une conférence internationale l'a choisi en 1884", "La puissance maritime britannique l'explique."),
  Q("Que signifie GMT ?", ["Greenwich Mean Time", "Great Map Time", "Global Meridian Tool", "Greenwich Main Tower"], "Greenwich Mean Time", "C'est l'heure de référence au Royaume-Uni en hiver."),
  Q("Comment appelle-t-on l'heure d'été britannique ?", ["British Summer Time (BST)", "GMT +2", "London Time", "Daylight Time Zone"], "British Summer Time (BST)", "Elle a une heure d'avance sur GMT."),
]),
# ══ C5-3 · Le réel et l'imaginaire ══
notion('C5-3', 0, F, 'ang5-reve-cauchemar', [
  Q("Que signifie « dream » ?", ["Un rêve", "Un cauchemar", "Un sommeil", "Un réveil"], "Un rêve", "Nightmare = cauchemar."),
  Q("Comment dit-on « imaginer » ?", ["To imagine", "To image", "To magic", "To dream up only"], "To imagine", "Imagination = imagination."),
  Q("Que signifie « real » ?", ["Réel, vrai", "Royal", "Rare", "Rêveur"], "Réel, vrai", "Reality = réalité."),
]),
notion('C5-3', 0, F, 'ang5-super-pouvoirs', [
  Q("Que signifie « to fly » ?", ["Voler (dans les airs)", "Voler (dérober)", "Fuir", "Flotter"], "Voler (dans les airs)", "To steal = voler (dérober)."),
  Q("Comment dit-on « invisible » en anglais ?", ["Invisible", "Unseen-able", "Unvisible", "Nonvisible"], "Invisible", "Le mot est identique."),
  Q("Que signifie « superpower » ?", ["Un super-pouvoir", "Une grande puissance électrique", "Un super-héros", "Un supermarché"], "Un super-pouvoir", "Superpower désigne aussi une superpuissance (pays)."),
]),
notion('C5-3', 0, F, 'ang5-science-fiction', [
  Q("Que signifie « spaceship » ?", ["Un vaisseau spatial", "Une planète", "Une étoile", "Un astronaute"], "Un vaisseau spatial", "Space = espace, ship = navire."),
  Q("Comment dit-on « extraterrestre » en anglais ?", ["An alien", "A ghost", "A robot", "A stranger"], "An alien", "E.T. est le plus célèbre."),
  Q("Quel film de Steven Spielberg met en scène un petit extraterrestre qui veut « téléphoner maison » ?", ["E.T.", "Star Wars", "Jurassic Park", "Avatar"], "E.T.", "« E.T. phone home »."),
]),
notion('C5-3', 0, F, 'ang5-star-wars', [
  Q("Comment s'appelle le chevalier qui devient Dark Vador dans Star Wars ?", ["Anakin Skywalker", "Luke Skywalker", "Han Solo", "Obi-Wan Kenobi"], "Anakin Skywalker", "« Luke, I am your father » est une citation déformée."),
  Q("Quelle formule souhaitent les héros de Star Wars ?", ["« May the Force be with you »", "« To infinity and beyond »", "« Live long and prosper »", "« I'll be back »"], "« May the Force be with you »", "« Que la Force soit avec toi »."),
  Q("Comment s'appellent les chevaliers à sabre laser de Star Wars ?", ["Les Jedi", "Les Hobbits", "Les Avengers", "Les Klingons"], "Les Jedi", "Leurs ennemis sont les Sith."),
]),
notion('C5-3', 0, F, 'ang5-robots', [
  Q("Que signifie « robot » ?", ["Un robot", "Une robe", "Un voleur", "Un rocher"], "Un robot", "Le mot vient du tchèque."),
  Q("Quel petit robot de Pixar nettoie la Terre abandonnée ?", ["WALL-E", "R2-D2", "Baymax", "C-3PO"], "WALL-E", "Le film sort en 2008."),
  Q("Que signifie « AI » en anglais ?", ["Artificial intelligence (intelligence artificielle)", "Automatic internet", "American idea", "Art and image"], "Artificial intelligence (intelligence artificielle)", "En français, on dit IA."),
]),
notion('C5-3', 0, F, 'ang5-vrai-faux', [
  Q("Que signifie « true » ?", ["Vrai", "Faux", "Peut-être", "Rarement"], "Vrai", "False = faux."),
  Q("Que signifie « fake news » ?", ["Des fausses informations", "Des nouvelles récentes", "Un journal du soir", "Une émission de télé"], "Des fausses informations", "Il faut vérifier ses sources."),
  Q("Comment dit-on « mentir » en anglais ?", ["To lie", "To lay", "To laugh", "To leave"], "To lie", "A lie = un mensonge, a liar = un menteur."),
]),
notion('C5-3', 0, F, 'ang5-mondes-imaginaires', [
  Q("Dans quel monde imaginaire vit Alice après être tombée dans un terrier ?", ["Wonderland (le pays des merveilles)", "Narnia", "Neverland", "Oz"], "Wonderland (le pays des merveilles)", "Lewis Carroll l'invente en 1865."),
  Q("Quel petit être aux pieds poilus est le héros du Hobbit ?", ["Bilbo Baggins", "Frodo", "Gandalf", "Gollum"], "Bilbo Baggins", "Frodon est son neveu dans Le Seigneur des anneaux."),
  Q("Quel jouet en bois s'anime la nuit dans Toy Story, avec ses amis ?", ["Woody le cow-boy", "Pinocchio", "Casse-noisette", "Barbie"], "Woody le cow-boy", "Les jouets s'animent quand les humains ne regardent pas."),
]),
notion('C5-3', 0, F, 'ang5-dessins-animes-classiques', [
  Q("Quel lapin gris de la Warner dit « What's up, Doc? » ?", ["Bugs Bunny", "Roger Rabbit", "Peter Rabbit", "Thumper"], "Bugs Bunny", "Il apparaît en 1940."),
  Q("Quelle famille jaune de dessin animé vit à Springfield ?", ["Les Simpson", "Les Griffin", "Les Flintstones", "Les Jetson"], "Les Simpson", "La série commence en 1989."),
  Q("Quel chat et quelle souris se poursuivent sans cesse dans un dessin animé célèbre ?", ["Tom et Jerry", "Sylvestre et Titi", "Garfield et Odie", "Mickey et Minnie"], "Tom et Jerry", "Ils sont créés en 1940."),
]),
notion('C5-3', 0, I, 'ang5i-if-imaginaire', [
  Q("Complétez : « If I ___ a superpower, I would fly. » (have)", ["had", "have", "will have", "would have"], "had", "Hypothèse : if + prétérit, would + base verbale."),
  Q("Que signifie « I wish I could fly » ?", ["J'aimerais savoir voler.", "Je sais voler.", "Je vais voler.", "J'ai volé."], "J'aimerais savoir voler.", "I wish + prétérit exprime un souhait irréel."),
  Q("Complétez : « If it rains, we ___ stay at home. » (réel)", ["will", "would", "had", "are"], "will", "Condition réaliste : if + présent, will + base verbale."),
]),
notion('C5-3', 0, I, 'ang5i-jules-verne-wells', [
  Q("Quel auteur britannique a écrit La Guerre des mondes (1898), une invasion martienne ?", ["H. G. Wells", "Jules Verne", "Isaac Asimov", "George Orwell"], "H. G. Wells", "Une adaptation radio a provoqué la panique aux États-Unis en 1938."),
  Q("Quel roman de H. G. Wells imagine un voyage dans le temps ?", ["La Machine à explorer le temps", "1984", "Frankenstein", "Dracula"], "La Machine à explorer le temps", "The Time Machine (1895)."),
  Q("Quel écrivain américain d'origine russe a imaginé les trois lois de la robotique ?", ["Isaac Asimov", "Ray Bradbury", "Philip K. Dick", "Arthur C. Clarke"], "Isaac Asimov", "Elles apparaissent en 1942."),
]),
notion('C5-3', 0, I, 'ang5i-super-heros-marvel', [
  Q("Quel super-héros est milliardaire et porte une armure de haute technologie ?", ["Iron Man (Tony Stark)", "Batman", "Superman", "Hulk"], "Iron Man (Tony Stark)", "Batman est aussi milliardaire, mais sans armure volante."),
  Q("Comment s'appelle l'équipe de super-héros de Marvel réunissant Iron Man, Thor et Captain America ?", ["Les Avengers", "La Justice League", "Les X-Men", "Les Gardiens de la Galaxie"], "Les Avengers", "La Justice League est l'équipe de DC Comics."),
  Q("Quel scénariste a cocréé Spider-Man, les X-Men et les Quatre Fantastiques ?", ["Stan Lee", "Walt Disney", "Steven Spielberg", "George Lucas"], "Stan Lee", "Il apparaissait dans de nombreux films Marvel."),
]),
notion('C5-3', 0, I, 'ang5i-stereotypes', [
  Q("Quel cliché associe souvent les Britanniques à une boisson ?", ["Ils boivent du thé à toute heure", "Ils ne boivent que du café", "Ils boivent du vin rouge à chaque repas", "Ils ne boivent que de l'eau"], "Ils boivent du thé à toute heure", "C'est un stéréotype en partie fondé."),
  Q("Quel cliché sur les Américains concerne la taille des portions ?", ["Tout y serait plus grand (« super-size »)", "Ils mangent très peu", "Ils ne mangent que des légumes", "Ils ne mangent jamais au restaurant"], "Tout y serait plus grand (« super-size »)", "Les stéréotypes simplifient la réalité."),
  Q("Pourquoi faut-il se méfier des stéréotypes ?", ["Ils généralisent et ne correspondent pas à tous les individus", "Ils sont toujours vrais", "Ils sont interdits par la loi", "Ils sont scientifiques"], "Ils généralisent et ne correspondent pas à tous les individus", "La rencontre réelle les nuance."),
]),
notion('C5-3', 0, I, 'ang5i-gulliver', [
  Q("Dans quel pays de minuscules habitants Gulliver arrive-t-il ?", ["Lilliput", "Brobdingnag", "Narnia", "Wonderland"], "Lilliput", "Les Voyages de Gulliver (1726), de Jonathan Swift."),
  Q("De quel pays est originaire Jonathan Swift ?", ["L'Irlande", "L'Écosse", "Les États-Unis", "L'Australie"], "L'Irlande", "Il était doyen de la cathédrale Saint-Patrick de Dublin."),
  Q("Que critique Swift à travers les voyages imaginaires de Gulliver ?", ["La société et la politique de son époque", "Les animaux", "Rien, c'est un livre pour enfants", "La météo"], "La société et la politique de son époque", "C'est une satire."),
]),
notion('C5-3', 0, I, 'ang5i-theme-parks', [
  Q("Dans quelle ville de Floride se trouve Walt Disney World ?", ["Orlando", "Miami", "Tampa", "Jacksonville"], "Orlando", "Le premier parc Disney a ouvert en Californie en 1955."),
  Q("Quel parc d'attractions de Californie a été le premier créé par Walt Disney ?", ["Disneyland, à Anaheim", "Disney World", "Universal Studios", "Six Flags"], "Disneyland, à Anaheim", "Il ouvre en 1955."),
  Q("Dans quel parc londonien peut-on visiter les studios de tournage de Harry Potter ?", ["Les studios Warner Bros. de Leavesden", "Hyde Park", "Kew Gardens", "Regent's Park"], "Les studios Warner Bros. de Leavesden", "On y voit les décors originaux."),
]),
notion('C5-3', 0, I, 'ang5i-temps-recit-imaginaire', [
  Q("Complétez : « The dragon ___ fire and the knight ran away. » (breathe, au passé)", ["breathed", "breath", "breathes", "was breath"], "breathed", "Le prétérit fait avancer le récit."),
  Q("Quel est le prétérit de « fly » ?", ["flew", "flied", "flown", "flyed"], "flew", "Fly, flew, flown."),
  Q("Quel est le prétérit de « see » ?", ["saw", "seed", "seen", "sees"], "saw", "See, saw, seen."),
]),
notion('C5-3', 0, I, 'ang5i-loch-ness-mythes', [
  Q("Quel monstre légendaire vivrait dans un lac d'Écosse ?", ["Nessie", "Bigfoot", "Le Yéti", "Le Kraken"], "Nessie", "La photo célèbre de 1934 était un trucage."),
  Q("Que signifie « legend » en anglais ?", ["Une légende", "Une leçon", "Une liste", "Une lettre"], "Une légende", "Legendary = légendaire."),
  Q("Quelle créature à cornes unique est l'animal national de l'Écosse ?", ["La licorne", "Le dragon", "Le lion", "Le griffon"], "La licorne", "Elle figure sur les armoiries royales avec le lion."),
]),
notion('C5-3', 0, D, 'ang5d-dystopies', [
  Q("Quel roman de George Orwell imagine une société surveillée par « Big Brother » ?", ["1984", "La Ferme des animaux", "Le Meilleur des mondes", "Fahrenheit 451"], "1984", "Il paraît en 1949."),
  Q("Comment appelle-t-on un récit qui décrit une société imaginaire cauchemardesque ?", ["Une dystopie", "Une utopie", "Une biographie", "Une fable"], "Une dystopie", "Une utopie décrit une société idéale."),
  Q("Quelle série de romans de Suzanne Collins met en scène des jeux mortels télévisés ?", ["Hunger Games", "Divergent", "Le Labyrinthe", "Twilight"], "Hunger Games", "L'héroïne s'appelle Katniss Everdeen."),
]),
notion('C5-3', 0, D, 'ang5d-utopie-more', [
  Q("Quel humaniste anglais a inventé le mot « Utopie » en 1516 ?", ["Thomas More", "Shakespeare", "Francis Bacon", "Thomas Hobbes"], "Thomas More", "Le mot signifie « nulle part »."),
  Q("Quel roman d'Aldous Huxley imagine une société où le bonheur est fabriqué ?", ["Le Meilleur des mondes (Brave New World)", "1984", "Fahrenheit 451", "La Servante écarlate"], "Le Meilleur des mondes (Brave New World)", "Il paraît en 1932."),
  Q("Quelle autrice canadienne a écrit La Servante écarlate ?", ["Margaret Atwood", "Alice Munro", "J. K. Rowling", "Toni Morrison"], "Margaret Atwood", "The Handmaid's Tale (1985)."),
]),
notion('C5-3', 0, D, 'ang5d-surrealisme-magritte', [
  Q("Quel mouvement artistique explore le rêve et l'inconscient, avec Dalí et Magritte ?", ["Le surréalisme", "L'impressionnisme", "Le pop art", "Le cubisme"], "Le surréalisme", "Il naît dans les années 1920."),
  Q("Quel tableau de Magritte porte l'inscription « Ceci n'est pas une pipe » ?", ["La Trahison des images", "La Persistance de la mémoire", "Le Fils de l'homme", "Golconde"], "La Trahison des images", "Il interroge la différence entre l'objet et sa représentation."),
  Q("Quel peintre a représenté des montres molles dans La Persistance de la mémoire ?", ["Salvador Dalí", "René Magritte", "Max Ernst", "Joan Miró"], "Salvador Dalí", "Le tableau est au MoMA de New York."),
]),
notion('C5-3', 0, D, 'ang5d-tolkien-monde', [
  Q("Comment s'appelle le monde imaginaire du Seigneur des anneaux ?", ["La Terre du Milieu (Middle-earth)", "Narnia", "Westeros", "Hogwarts"], "La Terre du Milieu (Middle-earth)", "Tolkien y a inventé des langues complètes."),
  Q("Dans quel pays les films du Seigneur des anneaux ont-ils été tournés ?", ["La Nouvelle-Zélande", "L'Écosse", "Le Canada", "L'Islande"], "La Nouvelle-Zélande", "Le réalisateur Peter Jackson est néo-zélandais."),
  Q("Quelle créature obsédée par l'anneau appelle celui-ci « my precious » ?", ["Gollum", "Gandalf", "Sauron", "Legolas"], "Gollum", "« Mon précieux »."),
]),
notion('C5-3', 0, D, 'ang5d-reported-speech', [
  Q("Transformez au discours indirect : « I am tired », she said.", ["She said she was tired.", "She said I am tired.", "She said she is tiring.", "She told she was tired."], "She said she was tired.", "Le temps recule d'un cran au discours indirect."),
  Q("Quelle différence y a-t-il entre « say » et « tell » ?", ["Tell est suivi d'un complément de personne : tell someone", "Ils sont identiques", "Say est suivi d'un complément de personne", "Tell ne s'utilise qu'au passé"], "Tell est suivi d'un complément de personne : tell someone", "He told me… / He said that…"),
  Q("Transformez : « Open the door! », he said to me.", ["He told me to open the door.", "He said me open the door.", "He told to me open the door.", "He said I open the door."], "He told me to open the door.", "Ordre : tell + personne + to + verbe."),
]),
notion('C5-3', 0, D, 'ang5d-realisme-magique-us', [
  Q("Quel auteur américain a écrit Fahrenheit 451, où les livres sont brûlés ?", ["Ray Bradbury", "Isaac Asimov", "Stephen King", "Philip K. Dick"], "Ray Bradbury", "451 °F est la température à laquelle le papier brûle."),
  Q("Quel auteur américain est le maître du roman d'horreur, avec Ça (It) ?", ["Stephen King", "Edgar Allan Poe", "Mark Twain", "John Steinbeck"], "Stephen King", "Il vit dans le Maine."),
  Q("Quelle série de Netflix met en scène des enfants affrontant des créatures dans les années 1980 ?", ["Stranger Things", "The Crown", "Sherlock", "Friends"], "Stranger Things", "Elle se déroule dans l'Indiana."),
]),
notion('C5-3', 0, D, 'ang5d-doctor-who', [
  Q("Quelle série britannique met en scène un voyageur du temps dans une cabine de police bleue ?", ["Doctor Who", "Sherlock", "Black Mirror", "The Crown"], "Doctor Who", "Elle existe depuis 1963."),
  Q("Comment s'appelle la cabine de Doctor Who, plus grande à l'intérieur qu'à l'extérieur ?", ["Le TARDIS", "Le DeLorean", "L'Enterprise", "Le Faucon Millenium"], "Le TARDIS", "Time And Relative Dimension In Space."),
  Q("Quelle série britannique explore les dérives des technologies numériques ?", ["Black Mirror", "Downton Abbey", "Doctor Who", "Peaky Blinders"], "Black Mirror", "Chaque épisode est indépendant."),
]),
notion('C5-3', 0, D, 'ang5d-would-conditionnel', [
  Q("Complétez : « If I were invisible, I ___ visit the White House. »", ["would", "will", "am", "had"], "would", "If I were… : on utilise were pour toutes les personnes dans l'irréel."),
  Q("Que signifie « What would you do if you met an alien? » ?", ["Que ferais-tu si tu rencontrais un extraterrestre ?", "Qu'as-tu fait quand tu as rencontré un extraterrestre ?", "Que feras-tu demain ?", "Où est l'extraterrestre ?"], "Que ferais-tu si tu rencontrais un extraterrestre ?", "Conditionnel de l'imaginaire."),
  Q("Complétez : « If I ___ you, I would read this book. »", ["were", "am", "was being", "will be"], "were", "« If I were you » = à ta place."),
]),
]

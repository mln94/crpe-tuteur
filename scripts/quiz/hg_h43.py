# Histoire 4e · Société, culture et politique dans la France du XIXe siècle : au moins 50 questions par niveau
# (plus une notion avancée pour compléter H4-2)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ H4-2 : complément avancé ══
notion('H4-2', 0, D, 'hg4d-deuxieme-industrialisation', [
  Q("Quelle entreprise allemande de chimie, fondée en 1865, illustre la deuxième industrialisation ?", ["BASF", "Renault", "Michelin", "Peugeot"], "BASF", "La chimie et l'électricité sont les industries nouvelles."),
  Q("Quel ingénieur américain organise le travail en tâches simples et chronométrées ?", ["Frederick Taylor", "Henry Ford", "Thomas Edison", "Alexander Bell"], "Frederick Taylor", "On parle de taylorisme ou d'organisation scientifique du travail."),
  Q("Comment appelle-t-on de grandes entreprises qui contrôlent tout un secteur, comme la Standard Oil de Rockefeller ?", ["Des trusts", "Des corporations médiévales", "Des coopératives", "Des manufactures royales"], "Des trusts", "Les États-Unis votent une loi antitrust en 1890."),
]),
# ══ Facile ══
notion('H4-3', 0, F, 'hg4-restauration', [
  Q("Quel régime revient en France après la chute de Napoléon en 1815 ?", ["La monarchie (la Restauration)", "La République", "L'Empire", "La dictature militaire"], "La monarchie (la Restauration)", "Les frères de Louis XVI règnent."),
  Q("Quel roi, frère de Louis XVI, règne de 1814 à 1824 ?", ["Louis XVIII", "Charles X", "Louis-Philippe", "Louis XVII"], "Louis XVIII", "Il accorde une Charte constitutionnelle."),
  Q("Quel drapeau la Restauration rétablit-elle ?", ["Le drapeau blanc", "Le drapeau tricolore", "Le drapeau rouge", "Le drapeau noir"], "Le drapeau blanc", "C'est la couleur de la monarchie des Bourbons."),
]),
notion('H4-3', 0, F, 'hg4-trois-glorieuses', [
  Q("Comment appelle-t-on les trois journées révolutionnaires de juillet 1830 ?", ["Les Trois Glorieuses", "Les Cent-Jours", "La Semaine sanglante", "Les journées de Juin"], "Les Trois Glorieuses", "Elles renversent Charles X."),
  Q("Quel roi devient « roi des Français » après la révolution de 1830 ?", ["Louis-Philippe", "Charles X", "Louis XVIII", "Napoléon III"], "Louis-Philippe", "C'est la monarchie de Juillet."),
  Q("Quel tableau d'Eugène Delacroix célèbre la révolution de 1830 ?", ["La Liberté guidant le peuple", "Le Radeau de la Méduse", "Le Sacre de Napoléon", "Le Serment des Horaces"], "La Liberté guidant le peuple", "Il est exposé au Louvre."),
]),
notion('H4-3', 0, F, 'hg4-1848', [
  Q("Quelle République est proclamée en février 1848 ?", ["La IIe République", "La Ire République", "La IIIe République", "La Ve République"], "La IIe République", "Elle dure jusqu'en 1852."),
  Q("Qui est élu président de la République en décembre 1848 ?", ["Louis-Napoléon Bonaparte", "Lamartine", "Victor Hugo", "Adolphe Thiers"], "Louis-Napoléon Bonaparte", "C'est le neveu de Napoléon Ier."),
  Q("Quel poète, membre du gouvernement provisoire, défend le drapeau tricolore en 1848 ?", ["Lamartine", "Baudelaire", "Rimbaud", "Musset"], "Lamartine", "Il refuse le drapeau rouge."),
]),
notion('H4-3', 0, F, 'hg4-voter', [
  Q("Où dépose-t-on son bulletin de vote ?", ["Dans une urne", "Dans une boîte aux lettres", "Chez le maire", "À l'église"], "Dans une urne", "L'urne garantit le secret du vote."),
  Q("Qu'est-ce que le suffrage universel masculin ?", ["Le droit de vote pour tous les hommes adultes", "Le droit de vote pour les riches", "Le droit de vote pour tous, hommes et femmes", "Le vote des nobles"], "Le droit de vote pour tous les hommes adultes", "Il existe durablement en France à partir de 1848."),
  Q("Qu'est-ce qu'un député ?", ["Un élu qui vote les lois à l'Assemblée", "Un juge", "Un préfet", "Un ministre du culte"], "Un élu qui vote les lois à l'Assemblée", "Il représente les électeurs."),
]),
notion('H4-3', 1, F, 'hg4-ecole-ferry', [
  Q("Qui est le ministre à l'origine des lois scolaires de 1881-1882 ?", ["Jules Ferry", "Jean Jaurès", "Victor Hugo", "Gambetta"], "Jules Ferry", "Il est ministre de l'Instruction publique."),
  Q("Comment appelle-t-on les instituteurs de la IIIe République, chargés de former de bons républicains ?", ["Les « hussards noirs » de la République", "Les gardes rouges", "Les sans-culottes", "Les grognards"], "Les « hussards noirs » de la République", "L'expression est de Charles Péguy."),
  Q("Quel livre de lecture raconte le voyage de deux enfants à travers la France ?", ["Le Tour de la France par deux enfants", "Les Misérables", "Le Petit Prince", "Germinal"], "Le Tour de la France par deux enfants", "Il apprend aux élèves à aimer la patrie."),
]),
notion('H4-3', 1, F, 'hg4-symboles-republique', [
  Q("Quelle est la devise de la République française ?", ["Liberté, Égalité, Fraternité", "Travail, Famille, Patrie", "Dieu et mon droit", "Unité, Progrès, Ordre"], "Liberté, Égalité, Fraternité", "Elle est inscrite au fronton des mairies et des écoles."),
  Q("Quel bâtiment de chaque commune affiche la devise républicaine et accueille les mariages civils ?", ["La mairie", "L'église", "La gare", "Le château"], "La mairie", "La IIIe République construit de nombreuses mairies-écoles."),
  Q("Quel monument parisien accueille les grands personnages de la nation ?", ["Le Panthéon", "La tour Eiffel", "L'Arc de triomphe", "Le Louvre"], "Le Panthéon", "Victor Hugo y entre en 1885."),
]),
notion('H4-3', 1, F, 'hg4-victor-hugo', [
  Q("Quel grand écrivain s'exile pendant tout le Second Empire pour s'opposer à Napoléon III ?", ["Victor Hugo", "Émile Zola", "Balzac", "Flaubert"], "Victor Hugo", "Il vit à Jersey puis à Guernesey."),
  Q("Quel roman de Victor Hugo raconte la vie de Jean Valjean ?", ["Les Misérables", "Notre-Dame de Paris", "Germinal", "Le Comte de Monte-Cristo"], "Les Misérables", "Il paraît en 1862."),
  N("En quelle année ont lieu les funérailles nationales de Victor Hugo ?", 1885, "Deux millions de personnes suivent le cortège."),
]),
notion('H4-3', 1, F, 'hg4-loi-1905', [
  Q("Que signifie la séparation des Églises et de l'État en 1905 ?", ["L'État ne reconnaît ni ne finance aucun culte", "L'État interdit les religions", "L'État choisit une religion officielle", "Les prêtres deviennent fonctionnaires"], "L'État ne reconnaît ni ne finance aucun culte", "Il garantit la liberté de conscience."),
  Q("Quelle liberté la loi de 1905 garantit-elle ?", ["La liberté de conscience et de culte", "La liberté de la presse", "Le droit de grève", "Le droit de vote des femmes"], "La liberté de conscience et de culte", "Chacun peut croire ou ne pas croire."),
  Q("Quel député socialiste rapporte la loi de séparation de 1905 ?", ["Aristide Briand", "Jules Ferry", "Clemenceau", "Gambetta"], "Aristide Briand", "Jean Jaurès la soutient."),
]),
notion('H4-3', 1, F, 'hg4-jaures', [
  Q("Quel homme politique socialiste défend la paix et les ouvriers à la fin du XIXe siècle ?", ["Jean Jaurès", "Adolphe Thiers", "Napoléon III", "Mac Mahon"], "Jean Jaurès", "Il est député du Tarn (Carmaux)."),
  N("En quelle année Jean Jaurès est-il assassiné ?", 1914, "Il est tué le 31 juillet, quelques jours avant la guerre."),
  Q("Quel journal Jaurès fonde-t-il en 1904 ?", ["L'Humanité", "Le Monde", "Le Figaro", "L'Aurore"], "L'Humanité", "Il existe toujours."),
]),
notion('H4-3', 2, F, 'hg4-femmes-travail', [
  Q("Dans quels secteurs travaillent beaucoup de femmes au XIXe siècle ?", ["Le textile, la domesticité et l'agriculture", "L'armée", "La politique", "La justice"], "Le textile, la domesticité et l'agriculture", "Elles sont moins payées que les hommes."),
  Q("Comment appelle-t-on une jeune ouvrière de la couture à Paris ?", ["Une midinette (ou grisette)", "Une bourgeoise", "Une suffragette", "Une religieuse"], "Une midinette (ou grisette)", "Le nom vient du repas pris à midi."),
  Q("Quel métier exercent de nombreuses jeunes femmes venues de la campagne en ville ?", ["Domestique (bonne)", "Médecin", "Avocate", "Députée"], "Domestique (bonne)", "Elles logent souvent sous les toits."),
]),
notion('H4-3', 2, F, 'hg4-femmes-modeles', [
  Q("Quel rôle la société bourgeoise du XIXe siècle attribue-t-elle surtout aux femmes ?", ["S'occuper du foyer et des enfants", "Diriger les entreprises", "Commander l'armée", "Voter les lois"], "S'occuper du foyer et des enfants", "On parle de « fée du logis »."),
  Q("Quelle romancière prend un nom d'homme et porte parfois des vêtements masculins ?", ["George Sand", "Colette", "Marie Curie", "Louise Michel"], "George Sand", "Son vrai nom est Aurore Dupin."),
  Q("Quelle femme scientifique reçoit deux prix Nobel, en 1903 et 1911 ?", ["Marie Curie", "George Sand", "Simone Veil", "Hubertine Auclert"], "Marie Curie", "Elle étudie la radioactivité."),
]),
notion('H4-3', 0, F, 'hg4-napoleon-iii', [
  Q("Quel régime Napoléon III dirige-t-il de 1852 à 1870 ?", ["Le Second Empire", "Le Premier Empire", "La IIe République", "La monarchie de Juillet"], "Le Second Empire", "Il est rétabli par plébiscite."),
  Q("Comment appelle-t-on un vote où le peuple répond par oui ou par non à une question du chef de l'État ?", ["Un plébiscite", "Une élection législative", "Une pétition", "Un sacre"], "Un plébiscite", "Napoléon III l'utilise à plusieurs reprises."),
  Q("Quelle impératrice est l'épouse de Napoléon III ?", ["Eugénie", "Joséphine", "Marie-Louise", "Hortense"], "Eugénie", "Elle est d'origine espagnole."),
]),
notion('H4-3', 1, F, 'hg4-service-militaire', [
  Q("Que doivent faire les jeunes hommes sous la IIIe République ?", ["Le service militaire", "Le service civique volontaire", "Un pèlerinage", "Rien de particulier"], "Le service militaire", "Il devient universel en 1905, pour deux ans."),
  Q("Pourquoi la IIIe République développe-t-elle un fort patriotisme ?", ["Pour préparer la revanche après la perte de l'Alsace-Moselle", "Pour conquérir l'Angleterre", "Pour rétablir la monarchie", "Pour plaire au pape"], "Pour préparer la revanche après la perte de l'Alsace-Moselle", "La carte de France montre les « provinces perdues »."),
  Q("De quelle couleur la carte de l'Alsace-Moselle est-elle souvent coloriée dans les écoles après 1871 ?", ["En noir ou violet, en signe de deuil", "En bleu", "En vert", "En or"], "En noir ou violet, en signe de deuil", "Le souvenir est entretenu chez les élèves."),
]),
# ══ Intermédiaire ══
notion('H4-3', 0, I, 'hg4i-suffrage-censitaire', [
  Q("Sous la Restauration, quelle condition faut-il remplir pour voter ?", ["Payer un impôt élevé (le cens)", "Savoir lire", "Être noble", "Avoir 18 ans"], "Payer un impôt élevé (le cens)", "Moins de 100 000 électeurs sous Louis XVIII."),
  Q("Quel ministre de Louis-Philippe aurait répondu « Enrichissez-vous » à ceux qui réclamaient le droit de vote ?", ["Guizot", "Thiers", "Polignac", "Villèle"], "Guizot", "Son refus de réforme provoque la révolution de 1848."),
  Q("Comment appelle-t-on les banquets organisés en 1847 pour réclamer l'élargissement du droit de vote ?", ["La campagne des banquets", "Les salons", "Les clubs jacobins", "Les états généraux"], "La campagne des banquets", "L'interdiction d'un banquet déclenche la révolution de Février."),
]),
notion('H4-3', 0, I, 'hg4i-journees-juin', [
  Q("Quel atelier, créé en 1848 pour donner du travail aux chômeurs, est fermé en juin ?", ["Les Ateliers nationaux", "Les manufactures royales", "Les bourses du travail", "Les ateliers de charité"], "Les Ateliers nationaux", "Leur fermeture provoque l'insurrection ouvrière."),
  Q("Comment est réprimée l'insurrection ouvrière de juin 1848 ?", ["Par l'armée, très violemment", "Par une loi sociale", "Par le roi", "Elle réussit"], "Par l'armée, très violemment", "Le général Cavaignac commande la répression."),
  Q("Quel vote de 1848 surprend les républicains ?", ["Les campagnes élisent une Assemblée conservatrice", "Paris élit un roi", "Les femmes votent", "Les ouvriers gagnent tous les sièges"], "Les campagnes élisent une Assemblée conservatrice", "Les paysans votent pour les notables."),
]),
notion('H4-3', 0, I, 'hg4i-coup-etat-1851', [
  Q("Pourquoi Louis-Napoléon Bonaparte fait-il un coup d'État le 2 décembre 1851 ?", ["Il ne peut pas se représenter et veut garder le pouvoir", "Il veut rétablir la monarchie des Bourbons", "Il veut donner le vote aux femmes", "Pour déclarer la guerre à l'Angleterre"], "Il ne peut pas se représenter et veut garder le pouvoir", "La Constitution interdit sa réélection."),
  Q("Pourquoi la date du 2 décembre est-elle symbolique ?", ["C'est l'anniversaire du sacre de Napoléon Ier et d'Austerlitz", "C'est Noël", "C'est la prise de la Bastille", "C'est la naissance de Louis-Napoléon"], "C'est l'anniversaire du sacre de Napoléon Ier et d'Austerlitz", "Il joue sur la légende napoléonienne."),
  Q("Quel député est tué sur une barricade en résistant au coup d'État ?", ["Alphonse Baudin", "Victor Hugo", "Gambetta", "Ledru-Rollin"], "Alphonse Baudin", "Il serait mort « pour 25 francs par jour »."),
]),
notion('H4-3', 0, I, 'hg4i-empire-liberal', [
  Q("Comment évolue le Second Empire dans les années 1860 ?", ["Il devient plus libéral", "Il devient plus autoritaire", "Il devient une République", "Il disparaît"], "Il devient plus libéral", "Le droit de grève est accordé en 1864."),
  Q("Quel pays déclare la guerre en 1870 et provoque la chute de l'Empire ?", ["La France déclare la guerre à la Prusse", "La Prusse déclare la guerre à l'Angleterre", "L'Italie déclare la guerre à la France", "La Russie déclare la guerre à la France"], "La France déclare la guerre à la Prusse", "La défaite de Sedan est rapide."),
  Q("Quelle expédition militaire au Mexique échoue sous Napoléon III ?", ["L'expédition du Mexique (1861-1867)", "La guerre de Crimée", "La campagne d'Italie", "La conquête de l'Algérie"], "L'expédition du Mexique (1861-1867)", "Maximilien, installé empereur, est fusillé."),
]),
notion('H4-3', 1, I, 'hg4i-installation-republique', [
  Q("Quel régime les élections de 1871 semblent-elles d'abord favoriser ?", ["Une restauration monarchique", "Une république socialiste", "Le retour de l'Empire", "Une dictature"], "Une restauration monarchique", "La majorité de l'Assemblée est royaliste."),
  Q("Quel amendement de 1875 inscrit le mot « République » dans les lois constitutionnelles, à une voix de majorité ?", ["L'amendement Wallon", "L'amendement Ferry", "L'amendement Thiers", "L'amendement Gambetta"], "L'amendement Wallon", "La République s'installe presque par hasard."),
  Q("Quel républicain prononce le célèbre discours « Le cléricalisme, voilà l'ennemi ! » ?", ["Gambetta", "Jules Ferry", "Thiers", "Jaurès"], "Gambetta", "Il le prononce en 1877."),
]),
notion('H4-3', 1, I, 'hg4i-libertes-1880', [
  N("En quelle année est votée la grande loi sur la liberté de la presse ?", 1881, "Elle est toujours en vigueur."),
  N("En quelle année la loi sur la liberté d'association est-elle votée ?", 1901, "Elle permet de créer des associations librement."),
  Q("Quelle liberté la loi de 1884 accorde-t-elle aux communes ?", ["Elles élisent leur conseil municipal, qui élit le maire", "Elles choisissent leur préfet", "Elles battent monnaie", "Elles votent les lois"], "Elles élisent leur conseil municipal, qui élit le maire", "Seul Paris garde un statut particulier."),
]),
notion('H4-3', 1, I, 'hg4i-boulangisme', [
  Q("Quel général menace la République par sa popularité à la fin des années 1880 ?", ["Le général Boulanger", "Le général de Gaulle", "Le général Mac Mahon", "Le général Cavaignac"], "Le général Boulanger", "On le surnomme « le général Revanche »."),
  Q("Quel président monarchiste démissionne en 1879 après la victoire des républicains ?", ["Mac Mahon", "Thiers", "Grévy", "Carnot"], "Mac Mahon", "Les républicains contrôlent désormais toutes les institutions."),
  Q("Quel président de la République est assassiné par un anarchiste en 1894 ?", ["Sadi Carnot", "Jules Grévy", "Félix Faure", "Paul Doumer"], "Sadi Carnot", "Il est poignardé à Lyon."),
]),
notion('H4-3', 1, I, 'hg4i-dreyfusards', [
  Q("Comment appelle-t-on ceux qui défendent l'innocence de Dreyfus ?", ["Les dreyfusards", "Les antidreyfusards", "Les boulangistes", "Les communards"], "Les dreyfusards", "Ils fondent la Ligue des droits de l'homme en 1898."),
  Q("Quel officier est le vrai coupable de la trahison dans l'affaire Dreyfus ?", ["Esterhazy", "Picquart", "Henry", "Mercier"], "Esterhazy", "Il est pourtant acquitté en 1898."),
  N("En quelle année Dreyfus est-il réhabilité ?", 1906, "Il est réintégré dans l'armée."),
]),
notion('H4-3', 2, I, 'hg4i-education-filles', [
  Q("Quelle loi de 1867 oblige les communes de plus de 500 habitants à ouvrir une école de filles ?", ["La loi Duruy", "La loi Falloux", "La loi Ferry", "La loi Guizot"], "La loi Duruy", "Victor Duruy est ministre de Napoléon III."),
  Q("Quelle école normale supérieure de jeunes filles est créée en 1881 ?", ["L'École normale de Sèvres", "L'École polytechnique", "Saint-Cyr", "L'ENA"], "L'École normale de Sèvres", "Elle forme les professeures des lycées de filles."),
  Q("Quelle femme est l'une des premières avocates à plaider en France, en 1907 ?", ["Jeanne Chauvin", "Simone Veil", "Marie Curie", "Louise Weiss"], "Jeanne Chauvin", "Une loi de 1900 ouvre le barreau aux femmes."),
]),
notion('H4-3', 2, I, 'hg4i-suffragettes', [
  Q("Comment appelle-t-on les militantes britanniques qui réclament le droit de vote au début du XXe siècle ?", ["Les suffragettes", "Les midinettes", "Les pétroleuses", "Les précieuses"], "Les suffragettes", "Emmeline Pankhurst les dirige."),
  Q("Quelle militante française renverse une urne en 1908 pour réclamer le vote des femmes ?", ["Hubertine Auclert", "George Sand", "Louise Michel", "Olympe de Gouges"], "Hubertine Auclert", "Elle mène ce combat depuis 1876."),
  Q("Quel pays accorde le premier le droit de vote aux femmes, en 1893 ?", ["La Nouvelle-Zélande", "La France", "Les États-Unis", "Le Royaume-Uni"], "La Nouvelle-Zélande", "La France ne le fera qu'en 1944."),
]),
notion('H4-3', 1, I, 'hg4i-courants-artistiques', [
  Q("Quel mouvement artistique tire son nom d'un tableau de Monet, Impression, soleil levant ?", ["L'impressionnisme", "Le romantisme", "Le cubisme", "Le réalisme"], "L'impressionnisme", "Le tableau est exposé en 1874."),
  Q("Quel mouvement littéraire et artistique, au début du XIXe siècle, exalte les sentiments et la nature ?", ["Le romantisme", "Le classicisme", "Le naturalisme", "Le surréalisme"], "Le romantisme", "Hugo, Lamartine et Delacroix en font partie."),
  Q("Quel écrivain est le chef de file du naturalisme, avec Les Rougon-Macquart ?", ["Émile Zola", "Victor Hugo", "Stendhal", "Chateaubriand"], "Émile Zola", "Il décrit la société de manière quasi scientifique."),
]),
notion('H4-3', 1, I, 'hg4i-loisirs-belle-epoque', [
  Q("Comment appelle-t-on la période d'optimisme et de progrès qui précède 1914 ?", ["La Belle Époque", "Les Années folles", "Les Trente Glorieuses", "La Renaissance"], "La Belle Époque", "Le nom est donné après la guerre."),
  N("En quelle année a lieu le premier Tour de France cycliste ?", 1903, "Il est créé par le journal L'Auto."),
  Q("Quel Français rénove les Jeux olympiques en 1894 ?", ["Pierre de Coubertin", "Jules Ferry", "Gustave Eiffel", "Louis Lumière"], "Pierre de Coubertin", "Les premiers Jeux modernes ont lieu à Athènes en 1896."),
]),
notion('H4-3', 0, I, 'hg4i-presse-opinion', [
  Q("Quel journal populaire vendu un sou se développe à partir de 1863 ?", ["Le Petit Journal", "Le Monde", "Libération", "Le Canard enchaîné"], "Le Petit Journal", "Il tire à un million d'exemplaires vers 1890."),
  Q("Pourquoi la presse se développe-t-elle fortement à la fin du XIXe siècle ?", ["Grâce à l'alphabétisation, la rotative et la liberté de la presse", "Grâce à la radio", "Grâce à la censure", "Grâce à Internet"], "Grâce à l'alphabétisation, la rotative et la liberté de la presse", "Le journal devient un objet quotidien."),
  Q("Dans quel journal paraît « J'accuse… ! » de Zola ?", ["L'Aurore", "Le Figaro", "L'Humanité", "Le Petit Journal"], "L'Aurore", "Le journal est dirigé par Clemenceau."),
]),
# ══ Avancé ══
notion('H4-3', 0, D, 'hg4d-charte-1814', [
  Q("Comment s'appelle le texte constitutionnel accordé par Louis XVIII en 1814 ?", ["La Charte", "La Déclaration des droits", "Le Code civil", "Le Concordat"], "La Charte", "Le roi la présente comme une concession."),
  Q("Quel roi, sacré à Reims en 1825, veut revenir à l'Ancien Régime ?", ["Charles X", "Louis XVIII", "Louis-Philippe", "Louis XVI"], "Charles X", "Il est renversé en 1830."),
  Q("Quelles ordonnances de juillet 1830, qui suspendent la liberté de la presse, déclenchent la révolution ?", ["Les ordonnances de Saint-Cloud", "Les ordonnances de Villers-Cotterêts", "Les ordonnances de Fontainebleau", "Les ordonnances de Moulins"], "Les ordonnances de Saint-Cloud", "Elles dissolvent aussi la Chambre."),
]),
notion('H4-3', 0, D, 'hg4d-1848-acquis', [
  Q("Quel homme politique fait voter l'abolition de l'esclavage le 27 avril 1848 ?", ["Victor Schœlcher", "Lamartine", "Ledru-Rollin", "Louis Blanc"], "Victor Schœlcher", "Il est sous-secrétaire d'État à la Marine."),
  Q("Quelle peine la IIe République abolit-elle en matière politique ?", ["La peine de mort", "Les amendes", "Le bannissement", "La prison"], "La peine de mort", "Elle restera en vigueur pour les crimes de droit commun."),
  Q("Quelle loi de 1850 restreint le suffrage universel en exigeant trois ans de domicile ?", ["La loi du 31 mai 1850", "La loi Falloux", "La loi Le Chapelier", "La loi Guizot"], "La loi du 31 mai 1850", "Près de trois millions d'électeurs sont exclus."),
]),
notion('H4-3', 0, D, 'hg4d-candidature-officielle', [
  Q("Comment appelle-t-on la pratique du Second Empire où le préfet soutient le candidat choisi par le pouvoir ?", ["La candidature officielle", "Le scrutin de liste", "La proportionnelle", "Le vote secret"], "La candidature officielle", "L'opposition a peu de chances."),
  Q("Combien de députés républicains, « les Cinq », siègent au Corps législatif en 1857 ?", ["Cinq", "Cent", "Deux cents", "Aucun"], "Cinq", "Émile Ollivier en fait partie."),
  N("En quelle année a lieu le dernier plébiscite du Second Empire, largement gagné par Napoléon III ?", 1870, "Quelques mois avant la chute de l'Empire."),
]),
notion('H4-3', 0, D, 'hg4d-apprentissage-vote', [
  Q("Comment appelle-t-on le passage, après 1848, d'un vote dicté par les notables à un vote plus libre ?", ["L'apprentissage du suffrage universel", "La Restauration", "Le despotisme", "La cohabitation"], "L'apprentissage du suffrage universel", "Les historiens parlent de « politisation » des campagnes."),
  Q("Quel dispositif, adopté en 1913, protège le secret du vote ?", ["L'isoloir et l'enveloppe", "Le vote à main levée", "Le vote par correspondance", "Le vote électronique"], "L'isoloir et l'enveloppe", "Avant, on pouvait voir le bulletin de chacun."),
  Q("Quel âge faut-il avoir pour voter sous la IIIe République ?", ["21 ans", "18 ans", "25 ans", "30 ans"], "21 ans", "La majorité passe à 18 ans en 1974."),
]),
notion('H4-3', 1, D, 'hg4d-lois-constitutionnelles-1875', [
  Q("Qui élit le président de la République sous la IIIe République ?", ["Les députés et les sénateurs réunis", "Le peuple au suffrage direct", "Le Sénat seul", "Le gouvernement"], "Les députés et les sénateurs réunis", "Ils forment l'Assemblée nationale réunie à Versailles."),
  Q("Pour combien d'années le président de la IIIe République est-il élu ?", ["Sept ans", "Cinq ans", "Quatre ans", "À vie"], "Sept ans", "Le septennat dure jusqu'en 2000."),
  Q("Quelle crise de 1877 affaiblit durablement le pouvoir présidentiel ?", ["La crise du 16 mai", "La crise de Fachoda", "L'affaire Dreyfus", "Le boulangisme"], "La crise du 16 mai", "Mac Mahon dissout la Chambre, mais les républicains l'emportent."),
]),
notion('H4-3', 1, D, 'hg4d-laicisation', [
  Q("Quelle loi de 1886 confie l'enseignement des écoles publiques à des laïcs uniquement ?", ["La loi Goblet", "La loi Falloux", "La loi Combes", "La loi Camille Sée"], "La loi Goblet", "Les religieux ne peuvent plus enseigner à l'école publique."),
  Q("Quel président du Conseil anticlérical interdit l'enseignement aux congrégations en 1904 ?", ["Émile Combes", "Jules Ferry", "Waldeck-Rousseau", "Clemenceau"], "Émile Combes", "Des milliers d'écoles religieuses ferment."),
  Q("Comment appelle-t-on les conflits lors des inventaires des biens d'Église en 1906 ?", ["La querelle des inventaires", "La querelle des Investitures", "La Fronde", "La guerre scolaire de 1984"], "La querelle des inventaires", "Des fidèles s'opposent aux fonctionnaires."),
]),
notion('H4-3', 1, D, 'hg4d-panama-anarchistes', [
  Q("Quel attentat anarchiste vise la Chambre des députés en 1893 ?", ["Une bombe lancée par Auguste Vaillant", "L'incendie du Palais-Bourbon", "L'assassinat de Jaurès", "L'attentat de la rue Saint-Nicaise"], "Une bombe lancée par Auguste Vaillant", "Des « lois scélérates » répriment ensuite les anarchistes."),
  Q("Comment appelle-t-on les lois de 1893-1894 contre les anarchistes ?", ["Les lois scélérates", "Les lois Ferry", "Les lois constitutionnelles", "Les lois d'exception de Vichy"], "Les lois scélérates", "Leurs opposants dénoncent des atteintes à la liberté."),
  Q("Quel mouvement nationaliste et antisémite se développe autour de Charles Maurras ?", ["L'Action française", "La Ligue des droits de l'homme", "Le Parti radical", "La SFIO"], "L'Action française", "Il est royaliste."),
]),
notion('H4-3', 1, D, 'hg4d-partis-politiques', [
  N("En quelle année est fondé le Parti radical, premier parti politique organisé en France ?", 1901, "Il domine la vie politique jusqu'en 1914."),
  Q("Quel parti socialiste unifié est fondé en 1905 ?", ["La SFIO", "Le PCF", "Le PS", "La CGT"], "La SFIO", "Section française de l'Internationale ouvrière."),
  Q("Quel parti est issu de la scission du congrès de Tours en 1920 ?", ["Le Parti communiste", "Le Parti radical", "Le Front national", "Les Républicains"], "Le Parti communiste", "La majorité de la SFIO rejoint l'Internationale communiste."),
]),
notion('H4-3', 1, D, 'hg4d-memoire-republicaine', [
  Q("Quel sculpteur réalise le monument du Triomphe de la République, place de la Nation ?", ["Jules Dalou", "Rodin", "Bartholdi", "Carpeaux"], "Jules Dalou", "Il est inauguré en 1899."),
  Q("Quel sculpteur conçoit la statue de la Liberté offerte aux États-Unis ?", ["Auguste Bartholdi", "Rodin", "Dalou", "Rude"], "Auguste Bartholdi", "Gustave Eiffel en conçoit la structure."),
  Q("Pourquoi la IIIe République multiplie-t-elle statues de Marianne et monuments ?", ["Pour enraciner les valeurs républicaines dans tout le pays", "Pour honorer les rois", "Pour célébrer l'Empire", "Pour décorer les églises"], "Pour enraciner les valeurs républicaines dans tout le pays", "On parle de « statuomanie »."),
]),
notion('H4-3', 2, D, 'hg4d-divorce-naquet', [
  N("En quelle année la loi Naquet rétablit-elle le divorce ?", 1884, "Il avait été supprimé en 1816."),
  Q("Pour quelles raisons le divorce est-il possible avec la loi Naquet ?", ["Uniquement pour faute (adultère, violences, condamnation)", "Par consentement mutuel", "Sans aucune raison", "Seulement à la demande du mari"], "Uniquement pour faute (adultère, violences, condamnation)", "Le divorce par consentement mutuel arrive en 1975."),
  Q("Quelle loi de 1938 supprime l'incapacité juridique de la femme mariée ?", ["La loi du 18 février 1938", "La loi Naquet", "La loi Veil", "La loi Neuwirth"], "La loi du 18 février 1938", "La femme reste cependant soumise à certains pouvoirs du mari."),
]),
notion('H4-3', 2, D, 'hg4d-feminisme-xixe', [
  Q("Quelle journaliste fonde en 1897 La Fronde, journal entièrement réalisé par des femmes ?", ["Marguerite Durand", "Hubertine Auclert", "Louise Michel", "Séverine"], "Marguerite Durand", "Une bibliothèque parisienne porte son nom."),
  Q("Quelle femme de lettres et socialiste réclame dès 1849 de se présenter aux élections ?", ["Jeanne Deroin", "George Sand", "Flora Tristan", "Madame de Staël"], "Jeanne Deroin", "Sa candidature est refusée."),
  Q("Quelle militante, autrice de L'Union ouvrière (1843), lie la cause des femmes et celle des ouvriers ?", ["Flora Tristan", "Marie Curie", "Colette", "Séverine"], "Flora Tristan", "Elle est la grand-mère de Paul Gauguin."),
]),
notion('H4-3', 2, D, 'hg4d-femmes-sante-travail', [
  Q("Quelle loi de 1892 interdit le travail de nuit des femmes dans l'industrie ?", ["La loi du 2 novembre 1892", "La loi Ferry", "La loi Naquet", "La loi Falloux"], "La loi du 2 novembre 1892", "Elle limite aussi leur journée à 11 heures."),
  Q("Quelle loi de 1909 crée un congé de maternité de huit semaines sans rupture de contrat ?", ["La loi Engerand", "La loi Veil", "La loi Roussel", "La loi Camille Sée"], "La loi Engerand", "Il n'est pas encore rémunéré."),
  Q("Quel est le salaire moyen d'une ouvrière par rapport à celui d'un ouvrier vers 1900 ?", ["Environ la moitié", "Le même", "Le double", "Un dixième"], "Environ la moitié", "L'inégalité salariale est très forte."),
]),
notion('H4-3', 2, D, 'hg4d-femmes-instruction-sup', [
  Q("Quelle femme devient la première docteure en médecine en France, en 1875 ?", ["Madeleine Brès", "Marie Curie", "Julie-Victoire Daubié", "Jeanne Chauvin"], "Madeleine Brès", "Elle se spécialise en pédiatrie."),
  Q("Quelle femme entre la première à l'Académie française, en 1980 ?", ["Marguerite Yourcenar", "Simone de Beauvoir", "George Sand", "Colette"], "Marguerite Yourcenar", "Ce sera bien après le XIXe siècle."),
  Q("Pourquoi les lycées de filles créés en 1880 ne préparent-ils pas au baccalauréat ?", ["On veut former de bonnes épouses et mères plutôt que des diplômées", "Parce que le bac n'existe pas", "Parce que les filles sont trop jeunes", "Parce que l'Église l'interdit"], "On veut former de bonnes épouses et mères plutôt que des diplômées", "L'égalité des programmes arrive en 1924."),
]),
notion('H4-3', 1, D, 'hg4d-ecole-republique', [
  Q("Quelle loi de 1833 oblige chaque commune à entretenir une école de garçons ?", ["La loi Guizot", "La loi Ferry", "La loi Duruy", "La loi Falloux"], "La loi Guizot", "L'école n'est pas encore gratuite ni obligatoire."),
  Q("Quelle loi de 1850 favorise l'enseignement catholique ?", ["La loi Falloux", "La loi Goblet", "La loi Guizot", "La loi de 1905"], "La loi Falloux", "Elle permet aux congrégations d'ouvrir des écoles."),
  Q("Quel diplôme sanctionne la fin de l'école primaire sous la IIIe République ?", ["Le certificat d'études primaires", "Le baccalauréat", "Le brevet des collèges", "La licence"], "Le certificat d'études primaires", "Il est créé en 1866 et supprimé en 1989."),
]),
notion('H4-3', 0, D, 'hg4d-thiers', [
  Q("Quel homme politique dirige la répression de la Commune en 1871 ?", ["Adolphe Thiers", "Gambetta", "Jules Ferry", "Mac Mahon seul"], "Adolphe Thiers", "Il est chef du pouvoir exécutif puis président."),
  Q("Comment Gambetta quitte-t-il Paris assiégé en 1870 pour organiser la défense ?", ["En ballon", "En train", "À cheval", "En bateau"], "En ballon", "Il rejoint Tours."),
  Q("Quel traité de 1871 met fin à la guerre franco-prussienne ?", ["Le traité de Francfort", "Le traité de Versailles", "Le traité de Vienne", "Le traité de Paris"], "Le traité de Francfort", "La France perd l'Alsace et une partie de la Lorraine."),
]),
]

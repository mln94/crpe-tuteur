# Histoire 4e · Le XVIIIe siècle. Expansions, Lumières et révolutions : au moins 50 questions par niveau
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Facile ══
notion('H4-1', 0, F, 'hg4-negoce-ports', [
  Q("Quel produit des Antilles, surnommé « l'or blanc », enrichit les négociants au XVIIIe siècle ?", ["Le sucre", "Le sel", "Le coton", "Le riz"], "Le sucre", "Le café et le tabac sont aussi très recherchés."),
  Q("Quel port français, célèbre pour ses quais et ses façades de pierre, prospère grâce au commerce avec les Antilles ?", ["Bordeaux", "Brest", "Calais", "Dunkerque"], "Bordeaux", "C'est le premier port colonial du royaume au XVIIIe siècle."),
  Q("Comment appelle-t-on un riche marchand qui fait du commerce à grande échelle ?", ["Un négociant", "Un colporteur", "Un artisan", "Un fermier"], "Un négociant", "Les négociants forment une bourgeoisie marchande puissante."),
]),
notion('H4-1', 0, F, 'hg4-plantations', [
  Q("Qu'est-ce qu'une plantation dans les colonies au XVIIIe siècle ?", ["Une grande exploitation agricole tournée vers l'exportation", "Un jardin public", "Une forêt protégée", "Une petite ferme familiale"], "Une grande exploitation agricole tournée vers l'exportation", "On y cultive la canne à sucre, le café ou l'indigo."),
  Q("Qui travaille de force dans les plantations des Antilles ?", ["Des esclaves africains", "Des paysans français libres", "Des soldats", "Des moines"], "Des esclaves africains", "Ils sont plusieurs centaines de milliers à Saint-Domingue."),
  Q("Comment appelle-t-on un esclave qui s'enfuit de la plantation ?", ["Un esclave marron", "Un affranchi", "Un colon", "Un engagé"], "Un esclave marron", "Le marronnage est une forme de résistance."),
]),
notion('H4-1', 1, F, 'hg4-valeurs-lumieres', [
  Q("Contre quoi les philosophes des Lumières luttent-ils ?", ["L'intolérance et l'arbitraire du pouvoir", "La science", "L'éducation", "Le commerce"], "L'intolérance et l'arbitraire du pouvoir", "Ils défendent la liberté et la raison."),
  Q("Que signifie être tolérant ?", ["Accepter les croyances et les opinions des autres", "Imposer sa religion", "Refuser de discuter", "Obéir sans réfléchir"], "Accepter les croyances et les opinions des autres", "Voltaire a écrit un Traité sur la tolérance."),
  Q("Pourquoi parle-t-on de « Lumières » pour désigner ces philosophes ?", ["Ils veulent éclairer les esprits par la raison", "Ils inventent l'électricité", "Ils travaillent la nuit", "Ils aiment le soleil"], "Ils veulent éclairer les esprits par la raison", "Ils s'opposent à l'ignorance et aux préjugés."),
]),
notion('H4-1', 2, F, 'hg4-louis-xvi', [
  Q("Qui devient roi de France en 1774 ?", ["Louis XVI", "Louis XV", "Louis XIV", "Napoléon"], "Louis XVI", "Il est le petit-fils de Louis XV."),
  Q("Quelle reine, d'origine autrichienne, est l'épouse de Louis XVI ?", ["Marie-Antoinette", "Catherine de Médicis", "Joséphine", "Anne d'Autriche"], "Marie-Antoinette", "Elle est très impopulaire à la veille de la Révolution."),
  N("En quelle année Marie-Antoinette est-elle guillotinée ?", 1793, "Elle est exécutée en octobre, neuf mois après Louis XVI."),
]),
notion('H4-1', 2, F, 'hg4-symboles-revolution', [
  Q("Qui compose La Marseillaise en 1792 ?", ["Rouget de Lisle", "Robespierre", "Danton", "Mozart"], "Rouget de Lisle", "Elle devient le chant des soldats marseillais montant à Paris."),
  Q("Quelle fête célèbre l'unité de la nation le 14 juillet 1790 ?", ["La fête de la Fédération", "La fête de l'Être suprême", "La prise de la Bastille", "Le sacre du roi"], "La fête de la Fédération", "Le 14 juillet, fête nationale, commémore les deux événements."),
  Q("Quelles sont les couleurs de la cocarde révolutionnaire ?", ["Bleu, blanc, rouge", "Vert, blanc, rouge", "Noir, rouge, or", "Bleu et or"], "Bleu, blanc, rouge", "Le bleu et le rouge de Paris encadrent le blanc de la royauté."),
]),
notion('H4-1', 2, F, 'hg4-sans-culottes', [
  Q("Comment appelle-t-on les révolutionnaires parisiens des milieux populaires ?", ["Les sans-culottes", "Les émigrés", "Les chouans", "Les feuillants"], "Les sans-culottes", "Ils portent un pantalon et non la culotte des nobles."),
  Q("Quel bonnet est le symbole de la liberté pendant la Révolution ?", ["Le bonnet phrygien", "Le tricorne", "Le bicorne", "Le chapeau haut-de-forme"], "Le bonnet phrygien", "Marianne le porte souvent."),
  Q("Comment se tutoient et s'appellent les révolutionnaires à partir de 1793 ?", ["« Citoyen » et « citoyenne »", "« Monsieur » et « Madame »", "« Sire » et « Majesté »", "« Frère » et « Sœur »"], "« Citoyen » et « citoyenne »", "C'est un signe d'égalité."),
]),
notion('H4-1', 2, F, 'hg4-bonaparte', [
  Q("Dans quelle île Napoléon Bonaparte est-il né en 1769 ?", ["La Corse", "La Sardaigne", "L'île d'Elbe", "Sainte-Hélène"], "La Corse", "Il naît à Ajaccio."),
  Q("Quel titre prend Bonaparte après son coup d'État de 1799 ?", ["Premier consul", "Roi", "Président", "Doge"], "Premier consul", "Il devient empereur en 1804."),
  Q("Sur quelle île Napoléon meurt-il en exil en 1821 ?", ["Sainte-Hélène", "L'île d'Elbe", "La Corse", "La Réunion"], "Sainte-Hélène", "C'est une île isolée de l'Atlantique sud."),
]),
notion('H4-1', 2, F, 'hg4-france-nouvelle', [
  Q("Quelle division administrative est créée en 1790 et existe toujours ?", ["Le département", "La province", "Le canton seulement", "La région"], "Le département", "Chaque chef-lieu doit être accessible en une journée de cheval."),
  N("Combien de départements la France compte-t-elle lors de leur création en 1790 ?", 83, "Ils portent souvent le nom d'un fleuve ou d'une montagne."),
  Q("Quel système d'unités de mesure la Révolution crée-t-elle ?", ["Le système métrique", "Le système impérial", "Les pieds et les pouces", "Le système sexagésimal"], "Le système métrique", "Le mètre et le kilogramme unifient les mesures."),
]),
notion('H4-1', 2, F, 'hg4-ancien-regime', [
  Q("Comment appelle-t-on la société et le régime politique d'avant 1789 ?", ["L'Ancien Régime", "Le Moyen Âge", "La République", "L'Empire"], "L'Ancien Régime", "Le nom est donné par les révolutionnaires."),
  Q("Quel ordre de la société paie l'essentiel des impôts sous l'Ancien Régime ?", ["Le tiers état", "La noblesse", "Le clergé", "La famille royale"], "Le tiers état", "Il rassemble plus de 95 % de la population."),
  Q("Comment appelle-t-on les avantages réservés au clergé et à la noblesse ?", ["Les privilèges", "Les droits de l'homme", "Les libertés publiques", "Les assignats"], "Les privilèges", "Ils sont abolis la nuit du 4 août 1789."),
]),
notion('H4-1', 1, F, 'hg4-salons-cafes', [
  Q("Dans quels lieux mondains, tenus souvent par des femmes, les philosophes discutent-ils ?", ["Les salons", "Les monastères", "Les casernes", "Les tribunaux"], "Les salons", "Madame Geoffrin tient un salon célèbre à Paris."),
  Q("Quel café parisien, toujours ouvert, est fréquenté par les philosophes au XVIIIe siècle ?", ["Le Procope", "Le Café de Flore", "Les Deux Magots", "Le Fouquet's"], "Le Procope", "On y lit les gazettes et on y débat."),
  Q("Par quels moyens les idées des Lumières se diffusent-elles ?", ["Livres, journaux, salons, cafés et académies", "Uniquement par la télévision", "Par les sermons des curés", "Par les ordres du roi"], "Livres, journaux, salons, cafés et académies", "Une opinion publique naît."),
]),
notion('H4-1', 0, F, 'hg4-grands-voyages', [
  Q("Quel navigateur français réalise un tour du monde de 1766 à 1769 ?", ["Bougainville", "La Pérouse", "Jacques Cartier", "Champlain"], "Bougainville", "Il fait connaître Tahiti en Europe."),
  Q("Quel navigateur britannique explore le Pacifique et l'Australie au XVIIIe siècle ?", ["James Cook", "Vasco de Gama", "Magellan", "Francis Drake"], "James Cook", "Il réalise trois grands voyages."),
  Q("Quelle île du Pacifique devient le symbole d'un paradis lointain pour les Européens du XVIIIe siècle ?", ["Tahiti", "Madagascar", "Cuba", "Ceylan"], "Tahiti", "Diderot écrit un Supplément au voyage de Bougainville."),
]),
notion('H4-1', 2, F, 'hg4-guerres-revolution-empire', [
  Q("Quelle victoire de septembre 1792 sauve la Révolution face aux Prussiens ?", ["Valmy", "Austerlitz", "Waterloo", "Trafalgar"], "Valmy", "Le lendemain, la République est proclamée."),
  Q("Quelle victoire de Napoléon, en 1805, est restée la plus célèbre ?", ["Austerlitz", "Waterloo", "Leipzig", "Trafalgar"], "Austerlitz", "On l'appelle la « bataille des Trois Empereurs »."),
  Q("Contre quels pays la France révolutionnaire entre-t-elle en guerre en 1792 ?", ["L'Autriche et la Prusse", "L'Espagne et le Portugal", "La Russie et la Suède", "Les États-Unis"], "L'Autriche et la Prusse", "Les monarchies européennes craignent la Révolution."),
]),
# ══ Intermédiaire ══
notion('H4-1', 0, I, 'hg4i-traite-atlantique', [
  Q("Combien d'Africains environ ont été déportés par la traite atlantique du XVIe au XIXe siècle ?", ["Environ 12 millions", "Environ 120 000", "Environ 1 million", "Environ 100 millions"], "Environ 12 millions", "Beaucoup meurent avant même d'arriver."),
  Q("Comment appelle-t-on la traversée de l'Atlantique par les navires négriers ?", ["Le « passage du milieu »", "La route des Indes", "Le grand tour", "Le cap Horn"], "Le « passage du milieu »", "C'est la deuxième étape du commerce triangulaire."),
  Q("Quelle proportion des captifs meurt en moyenne pendant la traversée ?", ["Environ un sur huit", "Presque aucun", "La moitié", "Les trois quarts"], "Environ un sur huit", "Les conditions à bord sont effroyables."),
]),
notion('H4-1', 0, I, 'hg4i-compagnie-indes', [
  Q("Quelle compagnie commerciale Colbert crée-t-il en 1664 pour commercer avec l'Asie ?", ["La Compagnie des Indes orientales", "La Hanse", "La Compagnie de Jésus", "La Banque de France"], "La Compagnie des Indes orientales", "Elle a le monopole du commerce vers l'Asie."),
  Q("Quel port breton est fondé pour la Compagnie des Indes et lui doit son nom ?", ["Lorient", "Saint-Malo", "Brest", "Quimper"], "Lorient", "Le nom vient de « L'Orient »."),
  Q("Quel comptoir français de l'Inde est le centre de la présence française au XVIIIe siècle ?", ["Pondichéry", "Goa", "Calcutta", "Madras"], "Pondichéry", "Il reste français jusqu'en 1954."),
]),
notion('H4-1', 0, I, 'hg4i-empire-colonial-francais', [
  Q("Quel traité de 1763 fait perdre le Canada à la France ?", ["Le traité de Paris", "Le traité d'Utrecht", "Le traité de Versailles", "Le traité de Vienne"], "Le traité de Paris", "Il conclut la guerre de Sept Ans."),
  Q("Comment appelle-t-on la colonie française du Canada avant 1763 ?", ["La Nouvelle-France", "La Louisiane", "Le Québec libre", "L'Acadie seulement"], "La Nouvelle-France", "Québec en est la principale ville."),
  N("En quelle année Napoléon vend-il la Louisiane aux États-Unis ?", 1803, "Le territoire double la superficie des États-Unis."),
]),
notion('H4-1', 1, I, 'hg4i-voltaire', [
  Q("Dans quel ouvrage de 1734 Voltaire fait-il l'éloge des libertés anglaises ?", ["Les Lettres philosophiques", "Candide", "Le Contrat social", "L'Esprit des lois"], "Les Lettres philosophiques", "Le livre est condamné et brûlé."),
  Q("Près de quelle frontière Voltaire s'installe-t-il à Ferney pour échapper à la censure ?", ["La frontière suisse, près de Genève", "La frontière espagnole", "La frontière belge", "La frontière italienne"], "La frontière suisse, près de Genève", "Il y passe les vingt dernières années de sa vie."),
  Q("Quelle formule Voltaire utilise-t-il pour combattre le fanatisme religieux ?", ["« Écrasez l'infâme »", "« L'État, c'est moi »", "« Liberté, égalité, fraternité »", "« Je pense donc je suis »"], "« Écrasez l'infâme »", "L'« infâme » désigne le fanatisme et la superstition."),
]),
notion('H4-1', 2, I, 'hg4i-revolution-americaine', [
  N("En quelle année les colonies américaines proclament-elles leur indépendance ?", 1776, "La Déclaration est adoptée le 4 juillet."),
  Q("Quel jeune noble français combat aux côtés des insurgés américains ?", ["La Fayette", "Robespierre", "Mirabeau", "Danton"], "La Fayette", "Il devient un héros des deux côtés de l'Atlantique."),
  N("En quelle année est rédigée la Constitution des États-Unis ?", 1787, "Elle est toujours en vigueur."),
]),
notion('H4-1', 2, I, 'hg4i-crise-1789', [
  Q("Quelle difficulté financière pousse Louis XVI à convoquer les états généraux ?", ["La dette énorme du royaume", "Un excès d'or dans les caisses", "La baisse des prix", "La fin des guerres"], "La dette énorme du royaume", "La guerre d'Amérique l'a encore aggravée."),
  Q("Pourquoi le prix du pain flambe-t-il au printemps 1789 ?", ["Après la mauvaise récolte de 1788", "À cause d'une taxe sur le pain", "Parce que le roi interdit le blé", "À cause de la peste"], "Après la mauvaise récolte de 1788", "La misère alimente la colère populaire."),
  Q("Quel ministre populaire Louis XVI renvoie-t-il le 11 juillet 1789, provoquant l'émeute à Paris ?", ["Necker", "Colbert", "Turgot", "Calonne"], "Necker", "Trois jours plus tard, la Bastille est prise."),
]),
notion('H4-1', 2, I, 'hg4i-ete-1789', [
  Q("Comment appelle-t-on la panique qui gagne les campagnes pendant l'été 1789 ?", ["La Grande Peur", "La Terreur", "La Jacquerie", "La Fronde"], "La Grande Peur", "Les paysans craignent un « complot aristocratique »."),
  Q("Que détruisent les paysans en attaquant les châteaux pendant l'été 1789 ?", ["Les registres des droits seigneuriaux", "Les églises", "Les récoltes", "Les routes"], "Les registres des droits seigneuriaux", "Ces documents fixent ce qu'ils doivent au seigneur."),
  Q("Pourquoi des femmes de Paris marchent-elles sur Versailles les 5 et 6 octobre 1789 ?", ["Pour réclamer du pain et ramener le roi à Paris", "Pour soutenir la reine", "Pour fuir la capitale", "Pour assister au sacre"], "Pour réclamer du pain et ramener le roi à Paris", "La famille royale s'installe aux Tuileries."),
]),
notion('H4-1', 2, I, 'hg4i-revolution-eglise', [
  Q("Que décide l'Assemblée en novembre 1789 à propos des biens de l'Église ?", ["Elle les met à la disposition de la nation", "Elle les augmente", "Elle les donne au pape", "Elle les laisse aux évêques"], "Elle les met à la disposition de la nation", "Ils deviennent des biens nationaux."),
  N("En quelle année est votée la Constitution civile du clergé ?", 1790, "Les prêtres deviennent des fonctionnaires élus."),
  Q("Comment appelle-t-on les prêtres qui refusent de prêter serment à la Constitution civile du clergé ?", ["Les prêtres réfractaires", "Les prêtres jureurs", "Les jésuites", "Les jansénistes"], "Les prêtres réfractaires", "Ceux qui l'acceptent sont appelés « jureurs » ou « constitutionnels »."),
]),
notion('H4-1', 2, I, 'hg4i-convention-factions', [
  Q("Quel député montagnard incarne la Terreur en 1793-1794 ?", ["Robespierre", "La Fayette", "Mirabeau", "Necker"], "Robespierre", "Il est surnommé « l'Incorruptible »."),
  Q("Quels députés, modérés, sont éliminés par les Montagnards en juin 1793 ?", ["Les Girondins", "Les Feuillants", "Les Jacobins", "Les Chouans"], "Les Girondins", "Beaucoup sont ensuite guillotinés."),
  Q("Quel tribun révolutionnaire, ministre de la Justice en 1792, est guillotiné en 1794 ?", ["Danton", "Marat", "Saint-Just", "Sieyès"], "Danton", "Il demandait la fin de la Terreur."),
]),
notion('H4-1', 2, I, 'hg4i-vendee', [
  N("En quelle année éclate l'insurrection de la Vendée contre la République ?", 1793, "Elle commence au printemps, après la levée de 300 000 hommes."),
  Q("Quelles causes poussent les Vendéens à se soulever ?", ["La levée de soldats et la défense de leurs prêtres", "La hausse du prix du sel", "La mort de Napoléon", "La perte du Canada"], "La levée de soldats et la défense de leurs prêtres", "Ils combattent sous l'emblème du Sacré-Cœur."),
  Q("Comment appelle-t-on les insurgés royalistes de Bretagne et du Maine ?", ["Les chouans", "Les sans-culottes", "Les girondins", "Les grognards"], "Les chouans", "Le nom viendrait du cri de la chouette."),
]),
notion('H4-1', 2, I, 'hg4i-directoire-consulat', [
  Q("Quel régime gouverne la France de 1795 à 1799 ?", ["Le Directoire", "Le Consulat", "La Convention montagnarde", "L'Empire"], "Le Directoire", "Le pouvoir exécutif est confié à cinq directeurs."),
  Q("Comment appelle-t-on le coup d'État de Bonaparte du 9 novembre 1799 ?", ["Le 18 Brumaire", "Le 9 Thermidor", "Le 10 Août", "Le 14 Juillet"], "Le 18 Brumaire", "Le nom vient du calendrier révolutionnaire."),
  Q("Quel régime Bonaparte installe-t-il après son coup d'État ?", ["Le Consulat", "La monarchie constitutionnelle", "Le Directoire", "La IIe République"], "Le Consulat", "Il en est le Premier consul."),
]),
notion('H4-1', 2, I, 'hg4i-napoleon-reformes', [
  Q("Quels fonctionnaires Bonaparte place-t-il à la tête des départements en 1800 ?", ["Les préfets", "Les intendants", "Les maires élus", "Les baillis"], "Les préfets", "Ils sont nommés par le pouvoir central."),
  Q("Quelle institution financière est créée en 1800 sous le Consulat ?", ["La Banque de France", "La Bourse de Paris", "La Caisse d'épargne", "Le Trésor royal"], "La Banque de France", "Elle émet les billets."),
  Q("Quelle décoration Bonaparte crée-t-il en 1802 pour récompenser les mérites ?", ["La Légion d'honneur", "L'ordre du Saint-Esprit", "La croix de guerre", "La médaille militaire"], "La Légion d'honneur", "Les lycées sont aussi créés en 1802."),
]),
notion('H4-1', 2, I, 'hg4i-empire-europe', [
  Q("Quelle défaite navale de 1805 assure à l'Angleterre la maîtrise des mers ?", ["Trafalgar", "Austerlitz", "Iéna", "Aboukir"], "Trafalgar", "L'amiral Nelson y meurt."),
  Q("Quelle mesure de 1806 interdit tout commerce entre l'Europe dominée par Napoléon et l'Angleterre ?", ["Le Blocus continental", "Le Code civil", "Le Concordat", "La levée en masse"], "Le Blocus continental", "Il vise à ruiner l'économie anglaise."),
  N("En quelle année la Grande Armée mène-t-elle la désastreuse campagne de Russie ?", 1812, "La retraite dans le froid décime l'armée."),
]),
notion('H4-1', 2, I, 'hg4i-femmes-revolution', [
  Q("Les femmes obtiennent-elles le droit de vote pendant la Révolution ?", ["Non", "Oui, dès 1789", "Oui, en 1792", "Seulement les femmes nobles"], "Non", "Elles participent pourtant activement aux événements."),
  N("En quelle année le divorce est-il autorisé en France pour la première fois ?", 1792, "Il sera restreint par le Code civil puis supprimé en 1816."),
  Q("Que décide la Convention à propos des clubs de femmes en octobre 1793 ?", ["Elle les interdit", "Elle les rend obligatoires", "Elle leur donne le droit de voter les lois", "Elle les finance"], "Elle les interdit", "Olympe de Gouges est guillotinée en novembre 1793."),
]),
# ══ Avancé ══
notion('H4-1', 0, D, 'hg4d-abolition-1794', [
  N("En quelle année la Convention abolit-elle l'esclavage dans les colonies françaises ?", 1794, "Le décret date du 4 février 1794 (16 pluviôse an II)."),
  Q("Qui rétablit l'esclavage dans les colonies françaises en 1802 ?", ["Napoléon Bonaparte", "Louis XVIII", "Robespierre", "Louis XVI"], "Napoléon Bonaparte", "Il faudra attendre 1848 pour l'abolition définitive."),
  Q("Quelle société, fondée en 1788, milite pour l'abolition de la traite et de l'esclavage ?", ["La Société des amis des Noirs", "Le club des Jacobins", "La Compagnie des Indes", "L'Académie française"], "La Société des amis des Noirs", "Brissot et Condorcet en sont membres."),
]),
notion('H4-1', 0, D, 'hg4d-toussaint', [
  N("En quelle année éclate la grande insurrection des esclaves de Saint-Domingue ?", 1791, "Elle commence dans la nuit du 22 au 23 août."),
  Q("Quel ancien esclave devient le principal chef de la révolution de Saint-Domingue ?", ["Toussaint Louverture", "Victor Schœlcher", "Jean-Jacques Dessalines seulement", "Simón Bolívar"], "Toussaint Louverture", "Il gouverne l'île avant d'être arrêté sur ordre de Bonaparte."),
  Q("Où Toussaint Louverture meurt-il en 1803 ?", ["Au fort de Joux, dans le Jura", "À Port-au-Prince", "À Sainte-Hélène", "À Paris"], "Au fort de Joux, dans le Jura", "Haïti proclame son indépendance l'année suivante."),
]),
notion('H4-1', 1, D, 'hg4d-economie-lumieres', [
  Q("Quel courant économique français du XVIIIe siècle considère la terre comme la seule source de richesse ?", ["Les physiocrates", "Les mercantilistes", "Les socialistes", "Les luddites"], "Les physiocrates", "François Quesnay en est la figure principale."),
  Q("Quel économiste écossais publie en 1776 Recherches sur la nature et les causes de la richesse des nations ?", ["Adam Smith", "John Locke", "David Hume", "Karl Marx"], "Adam Smith", "Il défend la liberté du commerce."),
  Q("Quelle formule résume l'idée de liberté économique défendue par les physiocrates ?", ["« Laissez faire, laissez passer »", "« Diviser pour régner »", "« Écrasez l'infâme »", "« Du pain et des jeux »"], "« Laissez faire, laissez passer »", "Ils s'opposent aux règlements et aux douanes intérieures."),
]),
notion('H4-1', 1, D, 'hg4d-despotes-eclaires', [
  Q("Quel roi de Prusse accueille Voltaire dans son palais de Sans-Souci ?", ["Frédéric II", "Guillaume Ier", "Frédéric-Guillaume IV", "Bismarck"], "Frédéric II", "Il se veut un « roi philosophe »."),
  Q("Quel empereur d'Autriche abolit le servage et accorde la tolérance religieuse dans les années 1780 ?", ["Joseph II", "Charles VI", "François-Joseph", "Léopold Ier"], "Joseph II", "Il est le fils de Marie-Thérèse."),
  Q("Quelle limite présente le « despotisme éclairé » ?", ["Les réformes viennent du souverain, qui garde un pouvoir absolu", "Il donne le pouvoir au peuple", "Il supprime la monarchie", "Il est inspiré par le pape"], "Les réformes viennent du souverain, qui garde un pouvoir absolu", "Les philosophes y voient un compromis."),
]),
notion('H4-1', 1, D, 'hg4d-censure', [
  Q("Que décide le pouvoir royal en 1759 à propos de l'Encyclopédie ?", ["Il retire son autorisation de publier", "Il la finance", "Il la rend obligatoire dans les écoles", "Il la traduit"], "Il retire son autorisation de publier", "La publication se poursuit clandestinement."),
  Q("Quel philosophe est emprisonné au donjon de Vincennes en 1749 ?", ["Diderot", "Voltaire", "Montesquieu", "Rousseau"], "Diderot", "Il est inquiété pour ses écrits."),
  Q("Quel ouvrage de Rousseau sur l'éducation est condamné et brûlé en 1762 ?", ["Émile", "Candide", "Les Lettres persanes", "L'Encyclopédie"], "Émile", "Rousseau doit fuir la France."),
]),
notion('H4-1', 2, D, 'hg4d-champ-de-mars', [
  Q("Que se passe-t-il au Champ-de-Mars le 17 juillet 1791 ?", ["La garde nationale tire sur des manifestants qui réclament la déchéance du roi", "Le roi est couronné", "La Bastille est prise", "La République est proclamée"], "La garde nationale tire sur des manifestants qui réclament la déchéance du roi", "C'est la première fracture entre révolutionnaires."),
  Q("Qui commande la garde nationale lors de la fusillade du Champ-de-Mars ?", ["La Fayette", "Robespierre", "Bonaparte", "Danton"], "La Fayette", "Sa popularité s'effondre."),
  Q("Quel événement de juin 1791 est à l'origine de cette crise ?", ["La fuite du roi, arrêté à Varennes", "La mort de Mirabeau", "La déclaration de guerre", "La nuit du 4 août"], "La fuite du roi, arrêté à Varennes", "La confiance envers Louis XVI est perdue."),
]),
notion('H4-1', 2, D, 'hg4d-10-aout-1792', [
  Q("Que se passe-t-il à Paris le 10 août 1792 ?", ["Le palais des Tuileries est pris et le roi est suspendu", "Le roi est sacré", "La Bastille est prise", "Napoléon est sacré"], "Le palais des Tuileries est pris et le roi est suspendu", "C'est la chute de la monarchie."),
  Q("Comment appelle-t-on les tueries de prisonniers dans les prisons parisiennes en septembre 1792 ?", ["Les massacres de Septembre", "La Saint-Barthélemy", "La Grande Peur", "La Terreur blanche"], "Les massacres de Septembre", "On craint alors une trahison des prisonniers."),
  Q("Comment la Convention est-elle élue en 1792 ?", ["Au suffrage universel masculin", "Au suffrage censitaire", "Par le roi", "Par tirage au sort"], "Au suffrage universel masculin", "C'est une première en France, même si peu votent."),
]),
notion('H4-1', 2, D, 'hg4d-terreur', [
  Q("Quel comité de la Convention dirige en fait le gouvernement pendant la Terreur ?", ["Le Comité de salut public", "Le Comité de sûreté générale seulement", "Le Directoire", "Le Conseil d'État"], "Le Comité de salut public", "Robespierre en est le membre le plus influent."),
  Q("Quelle loi de septembre 1793 permet d'arrêter toute personne soupçonnée d'hostilité à la Révolution ?", ["La loi des suspects", "La loi Le Chapelier", "La loi du maximum", "La loi sur les émigrés"], "La loi des suspects", "Les prisons se remplissent."),
  Q("Quel tribunal juge les ennemis de la Révolution à Paris ?", ["Le Tribunal révolutionnaire", "Le Parlement de Paris", "La Cour de cassation", "Le Conseil du roi"], "Le Tribunal révolutionnaire", "Ses jugements sont sans appel."),
]),
notion('H4-1', 2, D, 'hg4d-thermidor', [
  Q("Comment appelle-t-on la chute de Robespierre le 27 juillet 1794 ?", ["Le 9 Thermidor", "Le 18 Brumaire", "Le 10 Août", "Le 14 Juillet"], "Le 9 Thermidor", "Il est guillotiné le lendemain."),
  Q("Que se passe-t-il après la chute de Robespierre ?", ["La Terreur prend fin et une réaction contre les Jacobins s'installe", "La monarchie est rétablie", "Napoléon devient empereur", "La guerre s'arrête"], "La Terreur prend fin et une réaction contre les Jacobins s'installe", "On parle de « réaction thermidorienne »."),
  Q("Quel jeune député, proche de Robespierre, est guillotiné avec lui ?", ["Saint-Just", "Danton", "Desmoulins", "Marat"], "Saint-Just", "Danton et Desmoulins avaient été exécutés en avril 1794."),
]),
notion('H4-1', 2, D, 'hg4d-calendrier', [
  Q("À quelle année correspond l'an I du calendrier révolutionnaire ?", ["1792", "1789", "1793", "1799"], "1792", "Il commence le 22 septembre 1792, avec la République."),
  Q("Comment appelle-t-on le jour de repos qui remplace le dimanche dans le calendrier républicain ?", ["Le décadi", "Le primidi", "Le sabbat", "Le samedi"], "Le décadi", "La semaine est remplacée par une décade de dix jours."),
  Q("Quel mois du calendrier républicain correspond à la fin de l'été et aux vendanges ?", ["Vendémiaire", "Germinal", "Thermidor", "Nivôse"], "Vendémiaire", "Les noms évoquent les saisons et les travaux agricoles."),
]),
notion('H4-1', 2, D, 'hg4d-assignats', [
  Q("Qu'est-ce qu'un assignat pendant la Révolution ?", ["Un papier-monnaie garanti par la vente des biens nationaux", "Un impôt sur le sel", "Un titre de noblesse", "Un passeport"], "Un papier-monnaie garanti par la vente des biens nationaux", "Il est créé en 1789-1790."),
  Q("Quelle conséquence a l'émission massive d'assignats ?", ["Une très forte inflation", "Une baisse des prix", "La fin de la dette", "L'enrichissement de tous"], "Une très forte inflation", "Ils perdent presque toute leur valeur."),
  Q("Qui achète surtout les biens nationaux ?", ["Des bourgeois et des paysans aisés", "Les nobles émigrés", "Le clergé", "Les pauvres des villes"], "Des bourgeois et des paysans aisés", "Ils s'attachent alors à la Révolution."),
]),
notion('H4-1', 2, D, 'hg4d-concordat', [
  N("En quelle année Bonaparte signe-t-il le Concordat avec le pape ?", 1801, "Il met fin au conflit religieux né de la Révolution."),
  Q("Avec quel pape le Concordat est-il signé ?", ["Pie VII", "Pie IX", "Jean XXIII", "Grégoire VII"], "Pie VII", "Il assiste aussi au sacre de 1804."),
  Q("Comment le Concordat définit-il le catholicisme ?", ["Comme la religion de la majorité des Français", "Comme religion d'État obligatoire", "Comme une religion interdite", "Comme une religion étrangère"], "Comme la religion de la majorité des Français", "Les évêques sont nommés par le gouvernement."),
]),
notion('H4-1', 2, D, 'hg4d-code-civil', [
  N("Combien d'articles compte le Code civil de 1804 ?", 2281, "Il est encore en partie en vigueur."),
  Q("Quel principe hérité de la Révolution le Code civil confirme-t-il ?", ["L'égalité devant la loi et le droit de propriété", "Le droit d'aînesse", "Les privilèges de la noblesse", "Le vote des femmes"], "L'égalité devant la loi et le droit de propriété", "Il garantit aussi la liberté individuelle."),
  Q("Quelle place le Code civil donne-t-il à la femme mariée ?", ["Elle est soumise à l'autorité de son mari", "Elle est l'égale de son mari", "Elle dirige la famille", "Elle peut voter"], "Elle est soumise à l'autorité de son mari", "Elle ne peut ni travailler ni gérer ses biens sans son accord."),
]),
notion('H4-1', 2, D, 'hg4d-revolutions-atlantiques', [
  Q("Comment les historiens appellent-ils l'ensemble des révolutions de la fin du XVIIIe siècle, en Amérique et en Europe ?", ["Les révolutions atlantiques", "Les révolutions industrielles", "Les révolutions orientales", "Le printemps des peuples"], "Les révolutions atlantiques", "Elles partagent des idées de liberté et de souveraineté."),
  Q("Quel général libère une grande partie de l'Amérique du Sud de la domination espagnole ?", ["Simón Bolívar", "George Washington", "Toussaint Louverture", "Hernán Cortés"], "Simón Bolívar", "Il est surnommé « le Libertador »."),
  Q("Quelle révolution précède et inspire en partie la Révolution française ?", ["La révolution américaine", "La révolution russe", "La révolution industrielle", "La révolution de 1848"], "La révolution américaine", "Beaucoup d'officiers français y ont participé."),
]),
notion('H4-1', 2, D, 'hg4d-fin-empire', [
  Q("Sur quelle île Napoléon est-il exilé après sa première abdication en 1814 ?", ["L'île d'Elbe", "Sainte-Hélène", "La Corse", "Malte"], "L'île d'Elbe", "Il en revient en mars 1815."),
  Q("Comment appelle-t-on le retour de Napoléon au pouvoir en 1815 ?", ["Les Cent-Jours", "La Restauration", "Les Trois Glorieuses", "Le Consulat"], "Les Cent-Jours", "Il prend fin avec la défaite de Waterloo."),
  Q("Quel congrès réorganise l'Europe après la chute de Napoléon ?", ["Le congrès de Vienne", "Le congrès de Berlin", "Le congrès de Paris", "La conférence de Yalta"], "Le congrès de Vienne", "Il réunit les vainqueurs en 1814-1815."),
]),
]

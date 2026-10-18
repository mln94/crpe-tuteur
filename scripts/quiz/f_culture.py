# Thème « Culture littéraire et artistique » (français) : les perspectives annuelles du cycle 4
# 5e → facile, 4e → intermédiaire, 3e → avancé (40 questions)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ── 5e : Éprouver, expérimenter : la découverte de soi, d'autrui et du monde ──
notion('F13', 0, F, 'f-cla-heros', [
  Q("Quel héros de la mythologie grecque accomplit douze travaux ?", ["Hercule (Héraclès)", "Ulysse", "Persée", "Jason"], "Hercule (Héraclès)", "Parmi ses travaux : tuer le lion de Némée et l'hydre de Lerne."),
  Q("Dans la Bible, quel jeune berger affronte le géant Goliath ?", ["David", "Moïse", "Noé", "Samson"], "David", "David abat Goliath d'un simple jet de fronde."),
  Q("Quel chevalier de la Table ronde est le héros du « Chevalier de la charrette » de Chrétien de Troyes ?", ["Lancelot", "Perceval", "Gauvain", "Tristan"], "Lancelot", "Chrétien de Troyes (XIIe siècle) est l'un des premiers romanciers en langue française."),
]),
notion('F13', 0, F, 'f-cla-aventure', [
  Q("Quel personnage de Daniel Defoe survit des années sur une île déserte ?", ["Robinson Crusoé", "Gulliver", "Phileas Fogg", "Long John Silver"], "Robinson Crusoé", "Le roman paraît en 1719 ; il inspire de nombreuses « robinsonnades »."),
  Q("Quel jeune Gascon rejoint Athos, Porthos et Aramis dans « Les Trois Mousquetaires » d'Alexandre Dumas ?", ["D'Artagnan", "Cyrano", "Jean Valjean", "Edmond Dantès"], "D'Artagnan", "« Un pour tous, tous pour un ! » est la devise des mousquetaires."),
  Q("Qui a écrit « L'Île au trésor » ?", ["Robert Louis Stevenson", "Jules Verne", "Mark Twain", "Jack London"], "Robert Louis Stevenson", "Le roman met en scène le jeune Jim Hawkins et le pirate Long John Silver."),
]),
notion('F13', 1, F, 'f-cla-voyage-poesie', [
  Q("« Heureux qui, comme Ulysse, a fait un beau voyage » : de quel poète de la Renaissance est ce vers ?", ["Joachim du Bellay", "Pierre de Ronsard", "Victor Hugo", "Paul Verlaine"], "Joachim du Bellay", "Le sonnet, extrait des « Regrets », dit la nostalgie de son village natal."),
  Q("Quel poète a écrit « L'Invitation au voyage » (« Mon enfant, ma sœur, / Songe à la douceur… ») ?", ["Charles Baudelaire", "Jean de La Fontaine", "Pierre de Ronsard", "Jacques Prévert"], "Charles Baudelaire", "Le poème figure dans « Les Fleurs du mal »."),
  Q("Quel poète a écrit « Le Bateau ivre » à 17 ans ?", ["Arthur Rimbaud", "Paul Éluard", "Alfred de Musset", "Guillaume Apollinaire"], "Arthur Rimbaud", "Le poème raconte le voyage halluciné d'un bateau livré aux flots."),
]),
notion('F13', 2, F, 'f-cla-valets', [
  Q("Dans « Les Fourberies de Scapin » de Molière, qui est Scapin ?", ["Un valet rusé", "Un roi", "Un médecin", "Un juge"], "Un valet rusé", "Scapin multiplie les ruses pour aider les jeunes maîtres face à leurs pères."),
  Q("De quel théâtre populaire italien viennent des personnages comme Arlequin ?", ["La commedia dell'arte", "La tragédie grecque", "Le nô", "L'opéra"], "La commedia dell'arte", "Ses personnages types masqués ont inspiré Molière et Marivaux."),
  Q("Dans « Ruy Blas » de Victor Hugo, de qui le laquais Ruy Blas est-il amoureux ?", ["De la reine d'Espagne", "D'une servante", "D'une paysanne", "D'une actrice"], "De la reine d'Espagne", "L'amour d'un valet pour une reine illustre une société « sens dessus dessous »."),
]),
notion('F13', 3, F, 'f-cla-fables', [
  Q("Quelle fable de La Fontaine se termine par la morale « La raison du plus fort est toujours la meilleure » ?", ["« Le Loup et l'Agneau »", "« Le Corbeau et le Renard »", "« La Cigale et la Fourmi »", "« Le Lion et le Rat »"], "« Le Loup et l'Agneau »", "La morale est placée ici au début de la fable."),
  Q("« Rien ne sert de courir ; il faut partir à point. » De quelle fable vient cette morale ?", ["« Le Lièvre et la Tortue »", "« Le Loup et le Chien »", "« La Grenouille et le Bœuf »", "« Le Chêne et le Roseau »"], "« Le Lièvre et la Tortue »", "La Fontaine veut « plaire et instruire » à la fois."),
  Q("Quel fabuliste grec de l'Antiquité a inspiré La Fontaine ?", ["Ésope", "Homère", "Sophocle", "Platon"], "Ésope", "La Fontaine s'inspire aussi du fabuliste latin Phèdre."),
]),
# ── 4e : Rêver, délibérer, développer son jugement : en quête de valeurs et de vérité ──
notion('F14', 0, I, 'f-cla-anticipation', [
  Q("Qui a écrit « De la Terre à la Lune » (1865) ?", ["Jules Verne", "H. G. Wells", "Isaac Asimov", "Victor Hugo"], "Jules Verne", "Jules Verne imagine le voyage vers la Lune un siècle avant Apollo 11."),
  Q("Dans quel roman de George Orwell la société est-elle surveillée par « Big Brother » ?", ["« 1984 »", "« Le Meilleur des mondes »", "« Fahrenheit 451 »", "« La Ferme des animaux »"], "« 1984 »", "Ce roman d'anticipation dénonce les régimes totalitaires."),
  Q("Qui a écrit « Frankenstein ou le Prométhée moderne » (1818) ?", ["Mary Shelley", "Bram Stoker", "Edgar Allan Poe", "Jules Verne"], "Mary Shelley", "Le savant Victor Frankenstein donne vie à une créature qui lui échappe."),
]),
notion('F14', 1, I, 'f-cla-poete-terre', [
  Q("Quel poète de la mythologie grecque charme les animaux et les pierres par son chant et descend aux Enfers chercher Eurydice ?", ["Orphée", "Homère", "Apollon", "Hermès"], "Orphée", "Il est la figure fondatrice du poète dans la tradition occidentale."),
  Q("« Demain, dès l'aube, à l'heure où blanchit la campagne » : quel poète l'a écrit, en pensant à sa fille morte ?", ["Victor Hugo", "Alphonse de Lamartine", "Paul Verlaine", "Charles Baudelaire"], "Victor Hugo", "Le poème, extrait des « Contemplations », évoque sa fille Léopoldine."),
  Q("Quel poète romantique a écrit « Le Lac » (« Ô temps ! suspends ton vol ») ?", ["Alphonse de Lamartine", "Arthur Rimbaud", "Jean de La Fontaine", "Paul Éluard"], "Alphonse de Lamartine", "Le poème paraît dans les « Méditations poétiques » (1820)."),
]),
notion('F14', 2, I, 'f-cla-conflits-valeurs', [
  Q("Dans la tragédie de Sophocle, pourquoi Antigone désobéit-elle au roi Créon ?", ["Pour enterrer son frère Polynice malgré l'interdiction", "Pour prendre le trône", "Pour épouser un étranger", "Pour fuir Thèbes"], "Pour enterrer son frère Polynice malgré l'interdiction", "Elle oppose les lois divines et familiales à la loi du roi."),
  Q("Dans « Le Cid » de Corneille, entre quelles valeurs Rodrigue doit-il choisir ?", ["Son amour pour Chimène et l'honneur de sa famille", "La richesse et la gloire", "La guerre et la paix", "La ville et la campagne"], "Son amour pour Chimène et l'honneur de sa famille", "Venger son père, c'est tuer le père de celle qu'il aime."),
  Q("Comment appelle-t-on un choix impossible entre deux valeurs aussi fortes l'une que l'autre, comme celui de Rodrigue ?", ["Un dilemme cornélien", "Un quiproquo", "Un coup de théâtre", "Une catharsis"], "Un dilemme cornélien", "L'expression vient de Corneille, auteur du « Cid » (1637)."),
]),
notion('F14', 3, I, 'f-cla-lumieres-heritage', [
  Q("Quelle affaire judiciaire pousse Voltaire à écrire son « Traité sur la tolérance » (1763) ?", ["L'affaire Calas", "L'affaire Dreyfus", "L'affaire du collier", "Le procès de Louis XVI"], "L'affaire Calas", "Jean Calas, protestant, avait été injustement exécuté ; Voltaire obtient sa réhabilitation."),
  Q("Qui a rédigé la « Déclaration des droits de la femme et de la citoyenne » (1791) ?", ["Olympe de Gouges", "Madame de Staël", "George Sand", "Simone de Beauvoir"], "Olympe de Gouges", "Elle réclame pour les femmes les droits proclamés en 1789."),
  Q("Dans « De l'esclavage des nègres » (« De l'esprit des lois »), quel procédé Montesquieu utilise-t-il pour dénoncer l'esclavage ?", ["L'ironie", "Le lyrisme", "Le merveilleux", "L'épopée"], "L'ironie", "Il feint de justifier l'esclavage avec des arguments absurdes pour mieux le condamner."),
  Q("Quel philosophe des Lumières a écrit « Du contrat social » (1762) ?", ["Jean-Jacques Rousseau", "Voltaire", "Diderot", "Montesquieu"], "Jean-Jacques Rousseau", "Il y fonde la légitimité du pouvoir sur la volonté générale du peuple."),
]),
# ── 3e : S'affirmer, s'émanciper : l'engagement humaniste ──
notion('F15', 0, D, 'f-cla-temoigner', [
  Q("Quel écrivain italien témoigne de sa déportation à Auschwitz dans « Si c'est un homme » ?", ["Primo Levi", "Italo Calvino", "Umberto Eco", "Dante"], "Primo Levi", "Le livre paraît en 1947 : témoigner devient un devoir de mémoire."),
  Q("Quel événement Pablo Picasso dénonce-t-il dans « Guernica » (1937) ?", ["Le bombardement d'une ville basque pendant la guerre d'Espagne", "La prise de la Bastille", "La bataille de Verdun", "Le débarquement en Normandie"], "Le bombardement d'une ville basque pendant la guerre d'Espagne", "Le tableau, en noir et blanc, est devenu un symbole universel contre la guerre."),
  Q("Dans « Germinal », Émile Zola raconte la vie et la grève…", ["des mineurs du Nord", "des marins bretons", "des soldats de Napoléon", "des paysans de Provence"], "des mineurs du Nord", "Zola s'est documenté sur place pour peindre la condition ouvrière."),
]),
notion('F15', 1, D, 'f-cla-amour-poesie', [
  Q("« Mignonne, allons voir si la rose / Qui ce matin avait déclose… » : quel poète de la Renaissance l'a écrit ?", ["Pierre de Ronsard", "Joachim du Bellay", "Louise Labé", "Clément Marot"], "Pierre de Ronsard", "Le poème développe le thème du « carpe diem » : profiter de la jeunesse."),
  Q("Quel poète du XXe siècle a célébré Elsa Triolet, notamment dans « Les Yeux d'Elsa » ?", ["Louis Aragon", "Paul Éluard", "Jacques Prévert", "Robert Desnos"], "Louis Aragon", "Elsa est la muse de nombreux recueils d'Aragon."),
  Q("« Sous le pont Mirabeau coule la Seine / Et nos amours » : de quel poète est ce vers ?", ["Guillaume Apollinaire", "Paul Verlaine", "Arthur Rimbaud", "Charles Baudelaire"], "Guillaume Apollinaire", "Le poème, dans « Alcools » (1913), chante l'amour qui passe comme l'eau."),
]),
notion('F15', 2, D, 'f-cla-scene-cite', [
  Q("Lors de quelles fêtes religieuses les tragédies étaient-elles jouées dans l'Athènes antique ?", ["Les Dionysies, en l'honneur de Dionysos", "Les jeux Olympiques", "Les Saturnales", "Les fêtes de Pâques"], "Les Dionysies, en l'honneur de Dionysos", "Le théâtre était un événement civique qui réunissait toute la Cité."),
  Q("Dans « Rhinocéros » d'Eugène Ionesco (1959), que dénonce la transformation des habitants en rhinocéros ?", ["La montée des totalitarismes et le conformisme", "La pollution des villes", "La maltraitance animale", "Le progrès technique"], "La montée des totalitarismes et le conformisme", "Seul Bérenger résiste à la « rhinocérite »."),
  Q("Quelle comédie de Beaumarchais (1784), où un valet tient tête à son maître, critique les privilèges de la noblesse ?", ["« Le Mariage de Figaro »", "« Le Misanthrope »", "« Les Fourberies de Scapin »", "« Le Jeu de l'amour et du hasard »"], "« Le Mariage de Figaro »", "Figaro reproche au comte de s'être « donné la peine de naître, et rien de plus »."),
]),
notion('F15', 3, D, 'f-cla-ecrivains-engages', [
  Q("Dans quelle affaire Émile Zola publie-t-il « J'accuse…! » dans « L'Aurore » en 1898 ?", ["L'affaire Dreyfus", "L'affaire Calas", "Le scandale de Panama", "La Commune de Paris"], "L'affaire Dreyfus", "Zola y défend le capitaine Dreyfus, condamné à tort."),
  Q("Pourquoi Victor Hugo vit-il en exil à Jersey et Guernesey à partir de 1851 ?", ["Il s'oppose au coup d'État de Louis-Napoléon Bonaparte", "Il fuit une épidémie", "Il est nommé ambassadeur", "Il veut écrire au calme"], "Il s'oppose au coup d'État de Louis-Napoléon Bonaparte", "Il y écrit « Les Châtiments » contre Napoléon III."),
  Q("Quel peintre a représenté la révolution de juillet 1830 dans « La Liberté guidant le peuple » ?", ["Eugène Delacroix", "Jacques-Louis David", "Gustave Courbet", "Claude Monet"], "Eugène Delacroix", "Le tableau fait de la Liberté une figure allégorique du peuple en armes."),
]),
]

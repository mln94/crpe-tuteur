# EMC · Construire une culture civique : au moins 20 questions par niveau et par section
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ CC-1 · Le vote, un droit fondamental ══
notion('CC-1', 2, F, 'emc-bureau-vote', [
  Q("Où vote-t-on lors d'une élection ?", ["Dans un bureau de vote", "À l'école en classe", "Au supermarché", "Chez soi par téléphone"], "Dans un bureau de vote", "Il est souvent installé dans une école ou une mairie."),
  Q("Pourquoi passe-t-on par l'isoloir avant de voter ?", ["Pour garantir le secret du vote", "Pour se reposer", "Pour remplir sa déclaration d'impôts", "Pour se changer"], "Pour garantir le secret du vote", "Personne ne doit savoir pour qui l'on vote."),
  Q("Que fait l'électeur après avoir glissé son enveloppe dans l'urne ?", ["Il signe la liste d'émargement", "Il repart sans rien faire", "Il compte les voix", "Il choisit un autre candidat"], "Il signe la liste d'émargement", "Cela évite qu'une personne vote deux fois."),
]),
notion('CC-1', 1, F, 'emc-carte-electeur', [
  Q("Quel document reçoit-on après s'être inscrit sur les listes électorales ?", ["La carte électorale", "Le permis de conduire", "Le passeport", "La carte Vitale"], "La carte électorale", "Elle indique le bureau de vote."),
  Q("À 18 ans, les jeunes sont-ils inscrits automatiquement sur les listes électorales ?", ["Oui, s'ils ont fait le recensement citoyen à 16 ans", "Non, jamais", "Seulement s'ils le demandent au président", "Seulement à 21 ans"], "Oui, s'ils ont fait le recensement citoyen à 16 ans", "L'inscription d'office existe depuis 1997."),
  Q("Que peut faire un électeur absent le jour du vote ?", ["Donner une procuration à un autre électeur", "Voter par SMS", "Voter le lendemain", "Rien du tout"], "Donner une procuration à un autre électeur", "La procuration se fait au commissariat, à la gendarmerie ou en ligne."),
]),
notion('CC-1', 0, F, 'emc-vote-feminin-date', [
  Q("Qui pouvait voter en France avant 1944 ?", ["Seulement les hommes", "Tout le monde", "Seulement les femmes", "Personne"], "Seulement les hommes", "Le suffrage était universel masculin depuis 1848."),
  N("En quelle année la majorité électorale passe-t-elle de 21 à 18 ans ?", 1974, "Sous la présidence de Valéry Giscard d'Estaing."),
  Q("Pourquoi parle-t-on d'une « conquête progressive » du droit de vote ?", ["Le droit de vote a été étendu par étapes à de nouvelles catégories", "Il a été conquis par la guerre", "Il a toujours existé pour tous", "Il a été réduit au fil du temps"], "Le droit de vote a été étendu par étapes à de nouvelles catégories", "Hommes en 1848, femmes en 1944, jeunes de 18 ans en 1974…"),
]),
notion('CC-1', 0, I, 'emc-suffrage-censitaire-cc', [
  Q("Qu'est-ce que le suffrage censitaire ?", ["Un droit de vote réservé à ceux qui paient un certain montant d'impôt", "Le vote de tous les citoyens", "Le vote des femmes", "Le vote par Internet"], "Un droit de vote réservé à ceux qui paient un certain montant d'impôt", "Il existe en France avant 1848."),
  N("En quelle année le suffrage universel masculin est-il établi durablement en France ?", 1848, "Sous la IIe République."),
  Q("Quel pays européen accorde le droit de vote aux femmes dès 1906 ?", ["La Finlande", "La France", "La Suisse", "L'Italie"], "La Finlande", "La Suisse ne le fait au niveau fédéral qu'en 1971."),
]),
notion('CC-1', 1, I, 'emc-devoirs-citoyen', [
  Q("Lequel de ces éléments est un devoir du citoyen ?", ["Respecter les lois et payer ses impôts", "Voter obligatoirement à chaque élection", "Adhérer à un parti", "Faire du bénévolat"], "Respecter les lois et payer ses impôts", "En France, le vote est un droit et un devoir civique, mais pas une obligation légale."),
  Q("Quel devoir peut être demandé à un citoyen tiré au sort ?", ["Être juré d'assises", "Être député", "Être maire", "Être préfet"], "Être juré d'assises", "Refuser sans motif est puni d'une amende."),
  Q("Le recensement citoyen à 16 ans est…", ["obligatoire pour tous les jeunes Français", "facultatif", "réservé aux garçons", "réservé aux étrangers"], "obligatoire pour tous les jeunes Français", "Il permet d'être convoqué à la JDC."),
]),
notion('CC-1', 2, I, 'emc-presidentielle', [
  Q("Combien de signatures (parrainages) d'élus faut-il pour être candidat à l'élection présidentielle ?", ["500", "50", "5 000", "100 000"], "500", "Elles doivent venir d'au moins 30 départements."),
  Q("Que se passe-t-il si aucun candidat n'obtient la majorité absolue au premier tour de la présidentielle ?", ["Un second tour oppose les deux candidats arrivés en tête", "Le plus âgé est élu", "Le Sénat choisit", "On tire au sort"], "Un second tour oppose les deux candidats arrivés en tête", "Le second tour a lieu deux semaines plus tard."),
  Q("Quelle institution proclame les résultats de l'élection présidentielle ?", ["Le Conseil constitutionnel", "Le ministère de l'Intérieur seul", "L'Assemblée nationale", "Le Sénat"], "Le Conseil constitutionnel", "Il contrôle aussi la régularité du scrutin."),
]),
notion('CC-1', 2, I, 'emc-vote-blanc', [
  Q("Qu'est-ce qu'un vote blanc ?", ["Un bulletin vide ou une enveloppe vide, exprimant le refus de choisir parmi les candidats", "Un vote pour le candidat le plus âgé", "Un vote annulé pour fraude", "Un vote par procuration"], "Un bulletin vide ou une enveloppe vide, exprimant le refus de choisir parmi les candidats", "Depuis 2014, les votes blancs sont décomptés à part."),
  Q("Les votes blancs sont-ils pris en compte dans les suffrages exprimés ?", ["Non", "Oui", "Seulement à la présidentielle", "Seulement aux municipales"], "Non", "Ils sont comptés séparément mais n'influent pas sur le résultat."),
  Q("Qu'est-ce qu'un bulletin nul ?", ["Un bulletin raturé, déchiré ou portant des inscriptions", "Un bulletin pour un candidat élu", "Un bulletin blanc", "Une procuration"], "Un bulletin raturé, déchiré ou portant des inscriptions", "Il n'est pas compté comme suffrage exprimé."),
]),
notion('CC-1', 2, I, 'emc-elections-calendrier', [
  Q("Pour combien d'années sont élus les députés ?", ["5 ans", "6 ans", "7 ans", "4 ans"], "5 ans", "Sauf dissolution de l'Assemblée."),
  Q("Pour combien d'années sont élus les conseillers municipaux ?", ["6 ans", "5 ans", "3 ans", "9 ans"], "6 ans", "Les dernières élections municipales ont eu lieu en mars 2026."),
  Q("Pour combien d'années sont élus les députés européens ?", ["5 ans", "6 ans", "4 ans", "7 ans"], "5 ans", "Les dernières élections ont eu lieu en juin 2024."),
]),
notion('CC-1', 0, D, 'emc-vote-etrangers', [
  Q("Les étrangers non européens résidant en France peuvent-ils voter aux élections municipales ?", ["Non", "Oui, depuis 1981", "Oui, après 5 ans de résidence", "Oui, s'ils parlent français"], "Non", "Seuls les citoyens de l'UE le peuvent, depuis 1992."),
  N("En quelle année les citoyens européens votent-ils pour la première fois aux municipales en France ?", 2001, "Le traité de Maastricht a ouvert ce droit."),
  Q("Les citoyens européens peuvent-ils devenir maires en France ?", ["Non, ni maires ni adjoints", "Oui, sans restriction", "Oui, seulement dans les grandes villes", "Oui, après 10 ans"], "Non, ni maires ni adjoints", "Ils peuvent être conseillers municipaux."),
]),
notion('CC-1', 1, D, 'emc-privation-droits', [
  Q("Un tribunal peut-il priver une personne condamnée de son droit de vote ?", ["Oui, à titre de peine complémentaire", "Non, jamais", "Oui, automatiquement pour toute amende", "Oui, à vie pour une contravention"], "Oui, à titre de peine complémentaire", "Elle est limitée dans le temps."),
  Q("Les majeurs sous tutelle peuvent-ils voter depuis 2019 ?", ["Oui, tous", "Non, jamais", "Seulement avec l'accord du juge", "Seulement aux municipales"], "Oui, tous", "La loi de 2019 leur a rendu le droit de vote."),
  Q("Les détenus peuvent-ils voter ?", ["Oui, s'ils n'ont pas été privés de leurs droits civiques ; ils peuvent voter par correspondance depuis 2022", "Non, jamais", "Seulement les femmes détenues", "Seulement aux élections européennes"], "Oui, s'ils n'ont pas été privés de leurs droits civiques ; ils peuvent voter par correspondance depuis 2022", "Le vote par correspondance a été ouvert pour eux."),
]),
notion('CC-1', 2, D, 'emc-abstention-analyse', [
  Q("Quel record d'abstention est atteint aux élections régionales de 2021 au premier tour ?", ["Environ 67 %", "Environ 10 %", "Environ 30 %", "Environ 95 %"], "Environ 67 %", "Deux électeurs sur trois ne votent pas."),
  Q("Quels électeurs s'abstiennent le plus souvent ?", ["Les jeunes et les catégories populaires", "Les retraités", "Les cadres supérieurs", "Les élus"], "Les jeunes et les catégories populaires", "L'abstention est socialement différenciée."),
  Q("Quel pays européen rend le vote obligatoire ?", ["La Belgique", "La France", "L'Allemagne", "Le Royaume-Uni"], "La Belgique", "L'Australie aussi."),
]),
notion('CC-1', 2, D, 'emc-contentieux-electoral', [
  Q("Qui juge les contestations d'élections municipales ?", ["Le tribunal administratif", "La cour d'assises", "Le Conseil constitutionnel", "Le maire sortant"], "Le tribunal administratif", "Le Conseil d'État en appel."),
  Q("Qui juge les contestations d'élections législatives ?", ["Le Conseil constitutionnel", "Le tribunal administratif", "Le Sénat", "La Cour de cassation"], "Le Conseil constitutionnel", "Il peut annuler une élection."),
  Q("Quelle commission contrôle les comptes de campagne des candidats ?", ["La CNCCFP", "La CNIL", "L'Arcom", "La Cour de cassation"], "La CNCCFP", "Commission nationale des comptes de campagne et des financements politiques."),
]),
notion('CC-1', 2, D, 'emc-referendum-local', [
  Q("Qu'est-ce qu'un référendum local ?", ["Une consultation des électeurs d'une collectivité sur une affaire de sa compétence, à valeur décisionnelle", "Une élection présidentielle", "Un vote du Parlement", "Un sondage d'opinion"], "Une consultation des électeurs d'une collectivité sur une affaire de sa compétence, à valeur décisionnelle", "Il existe depuis 2003."),
  Q("Quelle condition doit remplir un référendum local pour être adopté ?", ["La moitié au moins des électeurs inscrits doit voter et la majorité des suffrages être favorable", "Un seul vote suffit", "Les deux tiers des inscrits doivent voter oui", "L'accord du préfet suffit"], "La moitié au moins des électeurs inscrits doit voter et la majorité des suffrages être favorable", "Sinon, il ne vaut qu'avis."),
  Q("Quelle consultation de 2016 portait sur le projet d'aéroport de Notre-Dame-des-Landes ?", ["Une consultation locale en Loire-Atlantique", "Un référendum national", "Une élection présidentielle", "Un vote du Sénat"], "Une consultation locale en Loire-Atlantique", "Le projet est finalement abandonné en 2018."),
]),
notion('CC-1', 1, D, 'emc-droits-civiques', [
  Q("Que recouvrent les droits civiques ?", ["Le droit de vote, d'éligibilité, d'être juré, d'exercer une fonction publique", "Le droit au logement", "Le droit à la santé", "Le droit au travail"], "Le droit de vote, d'éligibilité, d'être juré, d'exercer une fonction publique", "Ils sont liés à la citoyenneté."),
  Q("À partir de quel âge peut-on être candidat à l'élection présidentielle ?", ["18 ans", "23 ans", "35 ans", "21 ans"], "18 ans", "C'est aussi l'âge d'éligibilité de député depuis 2011."),
  Q("À partir de quel âge peut-on être élu sénateur ?", ["24 ans", "18 ans", "30 ans", "40 ans"], "24 ans", "Depuis la loi de 2011."),
]),
# ══ CC-2 · L'élection, la représentation citoyenne ══
notion('CC-2', 0, F, 'emc-democratie-definition', [
  Q("Que signifie le mot « démocratie » ?", ["Le pouvoir du peuple", "Le pouvoir d'un roi", "Le pouvoir des riches", "Le pouvoir de l'armée"], "Le pouvoir du peuple", "Du grec dêmos (peuple) et kratos (pouvoir)."),
  Q("Quelle formule de Lincoln définit la démocratie, reprise dans la Constitution française ?", ["« Gouvernement du peuple, par le peuple et pour le peuple »", "« L'État, c'est moi »", "« Diviser pour régner »", "« Ordre et progrès »"], "« Gouvernement du peuple, par le peuple et pour le peuple »", "C'est l'article 2 de la Constitution."),
  Q("Dans une démocratie représentative, qui vote les lois ?", ["Des représentants élus par les citoyens", "Le roi", "Les juges", "Les militaires"], "Des représentants élus par les citoyens", "En France, les députés et les sénateurs."),
]),
notion('CC-2', 0, F, 'emc-depute', [
  N("Combien de députés siègent à l'Assemblée nationale ?", 577, "Chacun représente une circonscription."),
  Q("Un député représente-t-il seulement sa circonscription ?", ["Non, il représente la Nation tout entière", "Oui, uniquement", "Il représente son parti seulement", "Il représente le président"], "Non, il représente la Nation tout entière", "Son mandat n'est pas impératif."),
  Q("Dans quel palais siège l'Assemblée nationale ?", ["Le palais Bourbon", "Le palais du Luxembourg", "Le palais de l'Élysée", "L'hôtel Matignon"], "Le palais Bourbon", "Le Sénat siège au palais du Luxembourg."),
]),
notion('CC-2', 1, F, 'emc-majorite-absolue', [
  Q("Qu'est-ce que la majorité absolue ?", ["Plus de la moitié des suffrages exprimés", "Le plus grand nombre de voix, même sans la moitié", "Tous les votes", "Un tiers des votes"], "Plus de la moitié des suffrages exprimés", "La majorité relative, c'est simplement arriver en tête."),
  Q("Dans la classe, l'élection des délégués se fait…", ["au scrutin uninominal à deux tours", "par tirage au sort", "par nomination du professeur", "à la proportionnelle"], "au scrutin uninominal à deux tours", "La majorité absolue est exigée au premier tour."),
  Q("Qu'est-ce qu'un scrutin uninominal ?", ["On vote pour une seule personne", "On vote pour une liste", "On vote pour un parti sans nom", "On ne vote pas"], "On vote pour une seule personne", "Plurinominal : on vote pour plusieurs."),
]),
notion('CC-2', 2, F, 'emc-sondage', [
  Q("Qu'est-ce qu'un sondage d'opinion ?", ["Une enquête auprès d'un échantillon pour connaître l'avis de la population", "Une élection officielle", "Un référendum", "Une loi"], "Une enquête auprès d'un échantillon pour connaître l'avis de la population", "Il donne une estimation, pas un résultat."),
  Q("Peut-on publier des sondages électoraux la veille et le jour d'une élection ?", ["Non, c'est interdit", "Oui, sans limite", "Oui, seulement le matin", "Seulement à la télévision"], "Non, c'est interdit", "Pour ne pas influencer les électeurs au dernier moment."),
  Q("Quelle commission contrôle les sondages électoraux ?", ["La Commission des sondages", "La CNIL", "Le Conseil d'État", "L'Arcom"], "La Commission des sondages", "Elle peut faire publier des mises au point."),
]),
notion('CC-2', 2, F, 'emc-opinion-publique', [
  Q("Qu'appelle-t-on l'opinion publique ?", ["L'ensemble des avis partagés par une population sur un sujet", "L'opinion du président", "Une loi", "Un parti politique"], "L'ensemble des avis partagés par une population sur un sujet", "Elle peut soutenir ou freiner une réforme."),
  Q("Quel moyen permet aux citoyens d'exprimer collectivement leur désaccord avec une réforme ?", ["La manifestation", "La dissolution", "Le décret", "La censure"], "La manifestation", "Elle est encadrée par la loi."),
  Q("Pourquoi la presse libre est-elle importante pour l'opinion publique ?", ["Elle informe les citoyens et leur permet de se forger un avis", "Elle décide des lois", "Elle élit le président", "Elle remplace les juges"], "Elle informe les citoyens et leur permet de se forger un avis", "On la surnomme le « quatrième pouvoir »."),
]),
notion('CC-2', 0, I, 'emc-souverainete-article3', [
  Q("Selon l'article 3 de la Constitution, à qui appartient la souveraineté nationale ?", ["Au peuple, qui l'exerce par ses représentants et par le référendum", "Au président", "Au Parlement seul", "Au gouvernement"], "Au peuple, qui l'exerce par ses représentants et par le référendum", "« Aucune section du peuple ni aucun individu ne peut s'en attribuer l'exercice »."),
  Q("Qu'est-ce que le mandat impératif, interdit en France ?", ["Une obligation pour l'élu de suivre les ordres de ses électeurs", "Un mandat de 5 ans", "Le cumul des mandats", "Le vote obligatoire"], "Une obligation pour l'élu de suivre les ordres de ses électeurs", "L'élu vote selon sa conscience."),
  Q("Quelle est la différence entre démocratie directe et représentative ?", ["Dans la directe, les citoyens décident eux-mêmes ; dans la représentative, ils élisent des représentants", "Aucune", "La directe est réservée aux rois", "La représentative supprime le vote"], "Dans la directe, les citoyens décident eux-mêmes ; dans la représentative, ils élisent des représentants", "La France combine les deux grâce au référendum."),
]),
notion('CC-2', 1, I, 'emc-scrutins-elections', [
  Q("Quel mode de scrutin est utilisé pour les élections européennes en France ?", ["La proportionnelle à un tour sur listes nationales", "Le scrutin majoritaire uninominal", "Le tirage au sort", "Le suffrage indirect"], "La proportionnelle à un tour sur listes nationales", "Une liste doit obtenir au moins 5 % pour avoir des élus."),
  Q("Quel mode de scrutin est utilisé pour les élections législatives ?", ["Le scrutin uninominal majoritaire à deux tours", "La proportionnelle intégrale", "Le scrutin de liste à un tour", "Le suffrage indirect"], "Le scrutin uninominal majoritaire à deux tours", "Un député par circonscription."),
  Q("Comment sont élus les sénateurs ?", ["Au suffrage universel indirect, par des grands électeurs", "Au suffrage universel direct", "Par le président", "Par tirage au sort"], "Au suffrage universel indirect, par des grands électeurs", "Surtout des délégués des conseils municipaux."),
]),
notion('CC-2', 1, I, 'emc-avantages-scrutins', [
  Q("Quel est l'avantage principal du scrutin majoritaire ?", ["Il dégage des majorités stables", "Il représente parfaitement toutes les opinions", "Il supprime les partis", "Il évite les élections"], "Il dégage des majorités stables", "Mais il sous-représente les petits partis."),
  Q("Quel est l'avantage principal de la proportionnelle ?", ["Elle représente fidèlement la diversité des opinions", "Elle garantit toujours une majorité", "Elle supprime le second tour et les partis", "Elle élit le président"], "Elle représente fidèlement la diversité des opinions", "Mais elle peut rendre les majorités difficiles."),
  Q("Quelle législature a été élue à la proportionnelle sous la Ve République ?", ["Celle de 1986", "Celle de 1958", "Celle de 2017", "Celle de 2024"], "Celle de 1986", "Le scrutin majoritaire est rétabli ensuite."),
]),
notion('CC-2', 2, I, 'emc-hatvp', [
  Q("Quelle autorité contrôle le patrimoine et les intérêts des élus depuis 2013 ?", ["La Haute Autorité pour la transparence de la vie publique (HATVP)", "La CNIL", "Le Conseil d'État", "L'Arcom"], "La Haute Autorité pour la transparence de la vie publique (HATVP)", "Elle est créée après l'affaire Cahuzac."),
  Q("Que doivent déclarer les ministres et les parlementaires à la HATVP ?", ["Leur patrimoine et leurs intérêts", "Leurs opinions religieuses", "Leurs notes scolaires", "Leurs loisirs"], "Leur patrimoine et leurs intérêts", "Les déclarations d'intérêts sont publiques."),
  Q("Depuis 2017, un parlementaire peut-il employer un membre de sa famille comme collaborateur ?", ["Non, c'est interdit", "Oui, sans limite", "Oui, s'il le paie lui-même", "Seulement ses enfants"], "Non, c'est interdit", "C'est la loi pour la confiance dans la vie politique."),
]),
notion('CC-2', 0, I, 'emc-cumul-mandats', [
  Q("Depuis 2017, un député peut-il être maire en même temps ?", ["Non", "Oui", "Oui, d'une petite commune seulement", "Oui, s'il le souhaite"], "Non", "La loi interdit le cumul avec une fonction exécutive locale."),
  Q("Pourquoi limiter le cumul des mandats ?", ["Pour que les élus se consacrent pleinement à leur mandat et renouveler la vie politique", "Pour réduire le nombre d'élections", "Pour donner plus de pouvoir au président", "Pour supprimer les maires"], "Pour que les élus se consacrent pleinement à leur mandat et renouveler la vie politique", "La mesure est appliquée depuis 2017."),
  Q("Un député peut-il rester conseiller municipal ?", ["Oui, sans fonction exécutive", "Non, jamais", "Oui, et maire aussi", "Seulement à Paris"], "Oui, sans fonction exécutive", "Il ne peut pas être maire ni adjoint."),
]),
notion('CC-2', 0, D, 'emc-representation-theorie', [
  Q("Quel penseur affirme que « la souveraineté ne peut être représentée » ?", ["Rousseau", "Montesquieu", "Sieyès", "Tocqueville"], "Rousseau", "Dans Du contrat social (1762)."),
  Q("Quel révolutionnaire défend en 1789 la représentation de la Nation par des élus ?", ["Sieyès", "Robespierre", "Marat", "Danton"], "Sieyès", "Auteur de Qu'est-ce que le tiers état ?"),
  Q("Quel penseur du XIXe siècle met en garde contre la « tyrannie de la majorité » ?", ["Alexis de Tocqueville", "Karl Marx", "Auguste Comte", "Victor Hugo"], "Alexis de Tocqueville", "Dans De la démocratie en Amérique."),
]),
notion('CC-2', 1, D, 'emc-scrutin-municipal', [
  Q("Quel mode de scrutin s'applique aux municipales dans les communes de 1 000 habitants et plus ?", ["Un scrutin de liste à deux tours avec prime majoritaire", "Le scrutin uninominal", "Le tirage au sort", "Le suffrage indirect"], "Un scrutin de liste à deux tours avec prime majoritaire", "La liste arrivée en tête obtient la moitié des sièges."),
  Q("Quelle réforme de 2025 étend le scrutin de liste paritaire à toutes les communes ?", ["La loi supprimant le panachage dans les communes de moins de 1 000 habitants", "La loi Defferre", "La loi de 1884", "La loi NOTRe"], "La loi supprimant le panachage dans les communes de moins de 1 000 habitants", "Elle s'applique à partir des municipales de 2026."),
  Q("Comment le maire est-il élu ?", ["Par le conseil municipal", "Directement par les habitants", "Par le préfet", "Par le président de la République"], "Par le conseil municipal", "Lors de la première réunion du conseil."),
]),
notion('CC-2', 1, D, 'emc-seuils-proportionnelle', [
  Q("Quel seuil une liste doit-elle atteindre aux élections européennes pour obtenir des sièges en France ?", ["5 %", "10 %", "1 %", "25 %"], "5 %", "C'est un seuil d'accès à la répartition."),
  Q("Quelle méthode répartit les sièges à la plus forte moyenne ?", ["La méthode d'Hondt", "La méthode de Condorcet", "La méthode de Borda", "La méthode de Pythagore"], "La méthode d'Hondt", "Elle favorise légèrement les grandes listes."),
  Q("Quel seuil faut-il atteindre aux législatives pour se maintenir au second tour ?", ["12,5 % des électeurs inscrits", "5 % des votants", "50 % des exprimés", "25 % des inscrits"], "12,5 % des électeurs inscrits", "Les deux premiers sont qualifiés de toute façon."),
]),
notion('CC-2', 2, D, 'emc-lobbying', [
  Q("Comment appelle-t-on l'action de groupes d'intérêts cherchant à influencer les décisions publiques ?", ["Le lobbying", "Le militantisme syndical seulement", "La désobéissance civile", "Le référendum"], "Le lobbying", "Les représentants d'intérêts doivent s'inscrire au répertoire de la HATVP."),
  Q("Quel principe oblige les administrations à communiquer leurs documents aux citoyens qui le demandent ?", ["Le droit d'accès aux documents administratifs (CADA)", "Le secret défense", "Le secret médical", "Le droit d'auteur"], "Le droit d'accès aux documents administratifs (CADA)", "Il découle de la loi de 1978."),
  Q("Quel article de la DDHC permet à la société de « demander compte à tout agent public de son administration » ?", ["L'article 15", "L'article 1er", "L'article 10", "L'article 17"], "L'article 15", "C'est le fondement de la transparence."),
]),
notion('CC-2', 2, D, 'emc-corruption', [
  Q("Quel organisme français est chargé de prévenir la corruption ?", ["L'Agence française anticorruption (AFA)", "La CNIL", "Le CESE", "L'Arcom"], "L'Agence française anticorruption (AFA)", "Elle est créée par la loi Sapin II de 2016."),
  Q("Quel parquet spécialisé, créé en 2013, poursuit la grande délinquance financière ?", ["Le parquet national financier (PNF)", "Le parquet antiterroriste", "La Cour des comptes", "Le Conseil d'État"], "Le parquet national financier (PNF)", "Il traite les affaires de corruption et de fraude fiscale."),
  Q("Quelle peine complémentaire est obligatoire pour les élus condamnés pour corruption depuis 2017 ?", ["L'inéligibilité", "Le bannissement", "La déchéance de nationalité", "L'exil"], "L'inéligibilité", "Le juge peut l'écarter par une décision motivée."),
]),
notion('CC-2', 1, D, 'emc-parite-scrutins', [
  Q("Comment la parité est-elle assurée dans les élections départementales depuis 2015 ?", ["Par des binômes femme-homme dans chaque canton", "Par des quotas de 10 %", "Par tirage au sort", "Elle n'est pas assurée"], "Par des binômes femme-homme dans chaque canton", "Les assemblées départementales sont strictement paritaires."),
  Q("Que risque un parti qui ne présente pas autant de femmes que d'hommes aux législatives ?", ["Une baisse de son financement public", "Sa dissolution", "La prison pour ses dirigeants", "Rien"], "Une baisse de son financement public", "Certains partis préfèrent payer."),
  Q("Comment s'appelle l'alternance femme-homme sur une liste électorale ?", ["Le système « chabadabada » (alternance stricte)", "Le panachage", "Le cumul", "Le ballottage"], "Le système « chabadabada » (alternance stricte)", "Il s'applique aux scrutins de liste."),
]),
# ══ CC-3 · La Défense et la sécurité ══
notion('CC-3', 0, F, 'emc-onu-paix', [
  Q("Quelle organisation internationale a pour mission principale de maintenir la paix ?", ["L'ONU", "L'OMC", "Le FMI", "L'Unesco"], "L'ONU", "Elle est créée en 1945."),
  Q("Comment appelle-t-on les soldats de l'ONU chargés de maintenir la paix ?", ["Les Casques bleus", "Les légionnaires", "Les gendarmes", "Les marines"], "Les Casques bleus", "Ils reçoivent le prix Nobel de la paix en 1988."),
  Q("Combien de membres permanents compte le Conseil de sécurité de l'ONU ?", ["Cinq", "Dix", "Quinze", "Trois"], "Cinq", "États-Unis, Russie, Chine, Royaume-Uni et France."),
]),
notion('CC-3', 3, F, 'emc-jdc', [
  Q("Que signifie JDC ?", ["Journée défense et citoyenneté", "Jeunesse du centre", "Journal de classe", "Journée des citoyens"], "Journée défense et citoyenneté", "Tous les jeunes Français y participent."),
  Q("Entre quels âges doit-on effectuer sa JDC ?", ["Entre 16 et 25 ans", "Entre 6 et 10 ans", "Après 30 ans", "Avant 12 ans"], "Entre 16 et 25 ans", "Le certificat est demandé pour s'inscrire aux examens et concours publics avant 25 ans."),
  Q("Le service militaire obligatoire existe-t-il encore en France ?", ["Non, il est suspendu depuis 1997", "Oui, pour tous", "Oui, pour les garçons", "Oui, pour les filles"], "Non, il est suspendu depuis 1997", "Décision de Jacques Chirac en 1996."),
]),
notion('CC-3', 0, I, 'emc-causes-conflits', [
  Q("Quelle ressource est souvent à l'origine de tensions dans le monde ?", ["L'eau, le pétrole ou les minerais", "Le sable du désert seulement", "La neige", "L'air"], "L'eau, le pétrole ou les minerais", "Le contrôle des ressources attise les conflits."),
  Q("Comment appelle-t-on un conflit qui oppose des groupes à l'intérieur d'un même État ?", ["Une guerre civile", "Une guerre mondiale", "Une guerre froide", "Une guerre commerciale"], "Une guerre civile", "Les civils en sont souvent les premières victimes."),
  Q("Qu'est-ce qu'un réfugié selon la convention de Genève ?", ["Une personne qui fuit son pays par crainte de persécutions", "Un touriste", "Un étudiant étranger", "Un travailleur saisonnier"], "Une personne qui fuit son pays par crainte de persécutions", "L'Ofpra examine les demandes en France."),
]),
notion('CC-3', 1, I, 'emc-europe-defense', [
  Q("Quelle clause du traité de l'Union européenne prévoit l'assistance mutuelle en cas d'agression d'un État membre ?", ["L'article 42-7", "L'article 49-3", "L'article 16", "L'article 5 du traité de Rome"], "L'article 42-7", "La France l'a invoquée après les attentats de 2015."),
  Q("Quel article du traité de l'OTAN prévoit la défense collective ?", ["L'article 5", "L'article 1er", "L'article 42-7", "L'article 89"], "L'article 5", "Une attaque contre un membre est une attaque contre tous."),
  Q("Quelle est la dissuasion nucléaire française ?", ["La capacité de répondre à une agression par des armes nucléaires pour l'empêcher", "Une attaque préventive", "Le désarmement total", "Une alliance avec la Russie"], "La capacité de répondre à une agression par des armes nucléaires pour l'empêcher", "Elle repose sur les sous-marins et les avions."),
]),
notion('CC-3', 2, I, 'emc-vigipirate', [
  Q("Quel plan protège la population contre la menace terroriste en France ?", ["Le plan Vigipirate", "Le plan ORSEC", "Le plan Marshall", "Le plan canicule"], "Le plan Vigipirate", "Il est créé en 1978."),
  Q("Quelle opération militaire déploie des soldats sur le territoire national depuis 2015 ?", ["L'opération Sentinelle", "L'opération Barkhane", "L'opération Serval", "L'opération Overlord"], "L'opération Sentinelle", "Elle protège les lieux sensibles."),
  Q("Quel exercice est organisé dans les écoles pour se préparer à une intrusion ou un attentat ?", ["L'exercice PPMS « attentat-intrusion »", "L'exercice d'incendie seulement", "Le cross du collège", "La JDC"], "L'exercice PPMS « attentat-intrusion »", "PPMS : plan particulier de mise en sûreté."),
]),
notion('CC-3', 3, I, 'emc-snu-armee-jeunesse', [
  Q("Quel dispositif lancé en 2019 propose un séjour de cohésion aux jeunes de 15 à 17 ans ?", ["Le Service national universel (SNU)", "La JDC", "Le service civique", "L'école"], "Le Service national universel (SNU)", "Il repose sur le volontariat."),
  Q("Quel dispositif permet aux jeunes de 16 à 25 ans de s'engager au service de l'intérêt général, avec une indemnité ?", ["Le service civique", "Le SNU", "La JDC", "Le recensement"], "Le service civique", "Il dure de 6 à 12 mois."),
  Q("Quel dispositif permet d'accueillir des collégiens dans les unités militaires (classes défense) ?", ["Les classes de défense et de sécurité globales", "Les classes vertes", "Les classes européennes", "Les classes prépa"], "Les classes de défense et de sécurité globales", "Elles relèvent des dispositifs Armée-jeunesse."),
]),
notion('CC-3', 0, D, 'emc-droit-guerre', [
  Q("Quel ensemble de règles protège les civils et les prisonniers en temps de guerre ?", ["Le droit international humanitaire (conventions de Genève)", "Le Code civil", "Le droit commercial", "Le règlement intérieur"], "Le droit international humanitaire (conventions de Genève)", "Les conventions de 1949 sont ratifiées par tous les États."),
  Q("Quelle organisation est la gardienne des conventions de Genève ?", ["Le Comité international de la Croix-Rouge (CICR)", "L'OTAN", "Le FMI", "L'Unesco"], "Le Comité international de la Croix-Rouge (CICR)", "Fondé par Henry Dunant en 1863."),
  Q("Que signifie le principe de distinction en droit de la guerre ?", ["Il faut distinguer combattants et civils, et ne viser que les objectifs militaires", "On peut viser tout le monde", "Les civils doivent combattre", "Les soldats ne peuvent pas se défendre"], "Il faut distinguer combattants et civils, et ne viser que les objectifs militaires", "Viser des civils est un crime de guerre."),
]),
notion('CC-3', 1, D, 'emc-chef-armees', [
  Q("Qui est le chef des armées en France ?", ["Le président de la République", "Le Premier ministre", "Le ministre des Armées", "Le chef d'état-major"], "Le président de la République", "C'est l'article 15 de la Constitution."),
  Q("Qui autorise la prolongation d'une intervention militaire à l'étranger au-delà de 4 mois ?", ["Le Parlement", "Le Conseil constitutionnel", "L'ONU", "Le Sénat seul"], "Le Parlement", "Depuis la révision constitutionnelle de 2008 (article 35)."),
  Q("Qui déclare la guerre selon la Constitution ?", ["Le Parlement l'autorise", "Le président seul", "Le ministre des Armées", "Le peuple par référendum"], "Le Parlement l'autorise", "Article 35 de la Constitution."),
]),
notion('CC-3', 2, D, 'emc-continuum-securite', [
  Q("Quelle différence y a-t-il entre la police nationale et la gendarmerie nationale ?", ["La police est civile et surtout en ville ; la gendarmerie est militaire et surtout en zone rurale et périurbaine", "Elles sont identiques", "La gendarmerie dépend de l'ONU", "La police est militaire"], "La police est civile et surtout en ville ; la gendarmerie est militaire et surtout en zone rurale et périurbaine", "Les deux dépendent du ministère de l'Intérieur."),
  Q("Quel service de renseignement intérieur lutte contre le terrorisme en France ?", ["La DGSI", "La DGSE", "La CIA", "Le GIGN"], "La DGSI", "La DGSE agit à l'extérieur."),
  Q("Quelle unité d'élite de la gendarmerie intervient lors de prises d'otages ?", ["Le GIGN", "Le RAID", "La BAC", "Les CRS"], "Le GIGN", "Le RAID est l'équivalent pour la police."),
]),
notion('CC-3', 1, D, 'emc-operations-france', [
  Q("Quelle opération française au Sahel (2014-2022) lutte contre les groupes jihadistes ?", ["L'opération Barkhane", "L'opération Sentinelle", "L'opération Turquoise", "L'opération Daguet"], "L'opération Barkhane", "Elle succède à l'opération Serval au Mali (2013)."),
  Q("Dans quel pays la France déploie-t-elle des troupes au sein de l'OTAN depuis 2022 pour rassurer ses alliés de l'Est ?", ["La Roumanie", "L'Espagne", "Le Portugal", "L'Irlande"], "La Roumanie", "C'est la mission Aigle."),
  Q("Quel est le budget de défense visé par les pays de l'OTAN en 2014 ?", ["2 % du PIB", "10 % du PIB", "0,5 % du PIB", "50 % du PIB"], "2 % du PIB", "L'objectif est relevé à 5 % lors du sommet de La Haye en 2025."),
]),
notion('CC-3', 3, D, 'emc-reserve', [
  Q("Qu'est-ce que la réserve opérationnelle ?", ["Des citoyens volontaires qui renforcent les armées quelques jours par an", "Un stock d'armes", "Une réserve naturelle", "Un fonds d'argent"], "Des citoyens volontaires qui renforcent les armées quelques jours par an", "On peut s'engager dès 17 ans."),
  Q("Quelle garde réunit depuis 2016 les réservistes des armées, de la gendarmerie et de la police ?", ["La Garde nationale", "La Garde républicaine", "La Légion étrangère", "La Garde suisse"], "La Garde nationale", "Elle est créée après les attentats de 2015."),
  Q("Quel document atteste de la participation à la JDC ?", ["Un certificat individuel de participation", "Le livret de famille", "La carte Vitale", "Le diplôme du brevet"], "Un certificat individuel de participation", "Il est exigé pour les examens et concours avant 25 ans."),
]),
notion('CC-3', 0, D, 'emc-cybermenace-etat', [
  Q("Quelle agence française protège les systèmes d'information de l'État contre les cyberattaques ?", ["L'ANSSI", "La CNIL", "L'Arcom", "La DGSE seulement"], "L'ANSSI", "Agence nationale de la sécurité des systèmes d'information."),
  Q("Quel service de l'État détecte les ingérences numériques étrangères depuis 2021 ?", ["Viginum", "Pharos", "Tracfin", "Interpol"], "Viginum", "Il lutte contre les manipulations de l'information venant de l'étranger."),
  Q("Qu'est-ce qu'une « guerre hybride » ?", ["Un conflit mêlant moyens militaires, cyberattaques et désinformation", "Une guerre entre robots", "Une guerre commerciale seulement", "Un jeu vidéo"], "Un conflit mêlant moyens militaires, cyberattaques et désinformation", "Elle brouille la frontière entre paix et guerre."),
]),
# ══ CC-4 · L'engagement ══
notion('CC-4', 2, F, 'emc-consommateur-responsable', [
  Q("Que signifie être un consommateur responsable ?", ["Acheter en pensant aux conséquences sociales et environnementales", "Acheter toujours plus", "Choisir le moins cher sans réfléchir", "Ne jamais acheter"], "Acheter en pensant aux conséquences sociales et environnementales", "Réduire, réutiliser, recycler."),
  Q("Que garantit le label « commerce équitable » ?", ["Un prix juste versé aux producteurs", "Un produit gratuit", "Un produit fabriqué en France", "Un produit sans emballage"], "Un prix juste versé aux producteurs", "Il soutient les petits producteurs."),
  Q("Quel geste aide à réduire les déchets ?", ["Trier et éviter le suremballage", "Jeter dans la nature", "Tout brûler", "Acheter des objets jetables"], "Trier et éviter le suremballage", "Le meilleur déchet est celui qu'on ne produit pas."),
]),
notion('CC-4', 4, F, 'emc-femmes-droits-reperes', [
  Q("Quelle journée internationale est consacrée aux droits des femmes ?", ["Le 8 mars", "Le 1er mai", "Le 14 juillet", "Le 25 décembre"], "Le 8 mars", "Elle est officialisée par l'ONU en 1977."),
  Q("Quel numéro gratuit écoute les femmes victimes de violences ?", ["Le 3919", "Le 3018", "Le 15", "Le 112"], "Le 3919", "Il est anonyme et disponible 24 h/24."),
  Q("Quelle militante pakistanaise reçoit le prix Nobel de la paix en 2014 pour l'éducation des filles ?", ["Malala Yousafzai", "Greta Thunberg", "Rosa Parks", "Simone Veil"], "Malala Yousafzai", "Elle a été victime d'un attentat des talibans."),
]),
notion('CC-4', 0, I, 'emc-delegue', [
  Q("Quel est le rôle d'un délégué de classe ?", ["Représenter les élèves et porter leur parole", "Punir ses camarades", "Remplacer le professeur", "Noter les copies"], "Représenter les élèves et porter leur parole", "Il participe au conseil de classe."),
  Q("Quelle instance permet aux collégiens de débattre de la vie du collège ?", ["Le conseil de la vie collégienne (CVC)", "Le Sénat", "Le conseil municipal", "Le conseil de discipline"], "Le conseil de la vie collégienne (CVC)", "Il fait des propositions."),
  Q("Quel engagement local permet à des jeunes de donner leur avis sur la vie de la commune ?", ["Le conseil municipal des jeunes", "La cour d'assises", "La garde nationale", "Le Parlement européen"], "Le conseil municipal des jeunes", "Il existe dans de nombreuses communes."),
]),
notion('CC-4', 1, I, 'emc-risques-majeurs', [
  Q("Quel signal d'alerte retentit le premier mercredi de chaque mois à midi ?", ["La sirène du réseau national d'alerte", "Une cloche d'église", "Un SMS du maire", "Un feu d'artifice"], "La sirène du réseau national d'alerte", "C'est un essai mensuel."),
  Q("Quel système envoie depuis 2022 des alertes sur les téléphones portables en cas de danger ?", ["FR-Alert", "Pronote", "Pharos", "Vigicrues seulement"], "FR-Alert", "Il prévient sans inscription préalable."),
  Q("En cas d'alerte à un nuage toxique, quel réflexe faut-il adopter ?", ["Se mettre à l'abri dans un bâtiment fermé", "Aller voir dehors", "Chercher ses enfants à l'école", "Ouvrir les fenêtres"], "Se mettre à l'abri dans un bâtiment fermé", "On ne va pas chercher les enfants : l'école les protège."),
]),
notion('CC-4', 3, I, 'emc-fake-news-verifier', [
  Q("Quel réflexe adopter avant de partager une information choquante ?", ["Vérifier la source et croiser avec d'autres médias", "La partager immédiatement", "La modifier", "La croire si elle a beaucoup de « likes »"], "Vérifier la source et croiser avec d'autres médias", "Les fausses informations circulent plus vite que les vraies."),
  Q("Qu'est-ce qu'un « fact-checker » ?", ["Un journaliste qui vérifie les faits", "Un pirate informatique", "Un influenceur", "Un algorithme publicitaire"], "Un journaliste qui vérifie les faits", "AFP Factuel ou Les Décodeurs en sont des exemples."),
  Q("Qu'est-ce qu'une « bulle de filtre » ?", ["L'enfermement de l'utilisateur dans des contenus proches de ses opinions par les algorithmes", "Une bulle de savon", "Un filtre photo", "Un antivirus"], "L'enfermement de l'utilisateur dans des contenus proches de ses opinions par les algorithmes", "Elle réduit la diversité des points de vue."),
]),
notion('CC-4', 5, I, 'emc-engagement-environnement', [
  Q("Quel accord international de 2015 vise à limiter le réchauffement climatique bien en dessous de 2 °C ?", ["L'accord de Paris", "Le protocole de Kyoto", "Le traité de Rome", "L'accord de Schengen"], "L'accord de Paris", "Il est adopté lors de la COP21."),
  Q("Quelle jeune militante suédoise lance en 2018 les grèves scolaires pour le climat ?", ["Greta Thunberg", "Malala Yousafzai", "Wangari Maathai", "Rachel Carson"], "Greta Thunberg", "Le mouvement « Fridays for Future » se répand dans le monde."),
  Q("Qu'est-ce qu'un éco-délégué au collège ?", ["Un élève élu pour mener des actions en faveur du développement durable", "Un professeur de SVT", "Un agent d'entretien", "Un élu municipal"], "Un élève élu pour mener des actions en faveur du développement durable", "Ils sont obligatoires dans chaque classe de collège depuis 2020."),
]),
notion('CC-4', 4, I, 'emc-violences-femmes-lutte', [
  Q("Comment appelle-t-on le meurtre d'une femme en raison de son genre, souvent par son conjoint ?", ["Un féminicide", "Un homicide involontaire", "Un accident", "Un fait divers banal"], "Un féminicide", "Plus d'une centaine de femmes en sont victimes chaque année en France."),
  Q("Quel dispositif permet à une victime de violences conjugales d'alerter les forces de l'ordre en urgence ?", ["Le téléphone grave danger", "Pronote", "La carte Vitale", "Le 3018"], "Le téléphone grave danger", "Il est attribué par le procureur."),
  Q("Quel mouvement de 2017 libère la parole des femmes victimes de violences sexuelles ?", ["#MeToo", "Fridays for Future", "Les Gilets jaunes", "Nuit debout"], "#MeToo", "En France, il prend aussi le nom de #BalanceTonPorc."),
]),
notion('CC-4', 0, I, 'emc-associations-loi1901', [
  Q("Combien de personnes faut-il au minimum pour créer une association loi 1901 ?", ["Deux", "Dix", "Cent", "Une seule"], "Deux", "Elle doit avoir un but non lucratif."),
  Q("Où déclare-t-on la création d'une association ?", ["À la préfecture (ou en ligne)", "Au tribunal", "À l'école", "À la banque"], "À la préfecture (ou en ligne)", "Elle est publiée au Journal officiel."),
  Q("Un mineur de 16 ans peut-il créer une association ?", ["Oui, librement, depuis 2017", "Non, jamais", "Seulement s'il est délégué", "Seulement à 18 ans"], "Oui, librement, depuis 2017", "La loi Égalité et citoyenneté l'a permis ; certains actes demandent l'accord écrit de ses parents."),
]),
notion('CC-4', 0, D, 'emc-syndicalisme', [
  Q("Quelle part environ des salariés français est syndiquée ?", ["Environ 10 %", "Environ 50 %", "Environ 90 %", "Moins de 1 %"], "Environ 10 %", "C'est l'un des taux les plus bas d'Europe."),
  Q("Comment est mesurée la représentativité des syndicats depuis 2008 ?", ["Par leurs résultats aux élections professionnelles", "Par leur ancienneté", "Par le nombre de grèves", "Par décision du président"], "Par leurs résultats aux élections professionnelles", "Il faut au moins 8 % au niveau national."),
  Q("Quel syndicat est le premier en voix aux élections professionnelles dans le secteur privé depuis 2017 ?", ["La CFDT", "La CGT", "FO", "La CFTC"], "La CFDT", "Elle devance la CGT."),
]),
notion('CC-4', 1, D, 'emc-dicrim-pcs', [
  Q("Quel document informe les habitants d'une commune sur les risques majeurs ?", ["Le DICRIM (document d'information communal sur les risques majeurs)", "Le PLU", "Le cadastre", "Le budget communal"], "Le DICRIM (document d'information communal sur les risques majeurs)", "Il est établi par le maire."),
  Q("Quel plan organise la réponse de la commune en cas de catastrophe ?", ["Le plan communal de sauvegarde (PCS)", "Le plan Vigipirate", "Le plan Marshall", "Le plan de relance"], "Le plan communal de sauvegarde (PCS)", "Il est obligatoire dans les communes exposées."),
  Q("Quel dispositif organise les secours à l'échelle du département en cas de catastrophe ?", ["Le plan ORSEC", "Le plan Sentinelle", "Le PPMS", "Le plan canicule seulement"], "Le plan ORSEC", "Il est déclenché par le préfet."),
]),
notion('CC-4', 2, D, 'emc-droit-consommation', [
  Q("Quel délai de rétractation un consommateur a-t-il pour un achat sur Internet ?", ["14 jours", "48 heures", "1 an", "Aucun"], "14 jours", "Sans avoir à se justifier."),
  Q("Quelle loi de 2020 lutte contre le gaspillage et pour l'économie circulaire ?", ["La loi AGEC", "La loi Evin", "La loi Veil", "La loi NOTRe"], "La loi AGEC", "Elle interdit notamment la destruction des invendus non alimentaires."),
  Q("Qu'est-ce que l'obsolescence programmée, devenue un délit en France en 2015 ?", ["Réduire volontairement la durée de vie d'un produit pour pousser à le remplacer", "Le recyclage", "La garantie légale", "Le commerce équitable"], "Réduire volontairement la durée de vie d'un produit pour pousser à le remplacer", "L'indice de réparabilité informe les consommateurs."),
]),
notion('CC-4', 3, D, 'emc-lanceurs-protection', [
  Q("Quelle loi de 2016 crée un statut protecteur des lanceurs d'alerte en France ?", ["La loi Sapin II", "La loi Pleven", "La loi Gayssot", "La loi Debré"], "La loi Sapin II", "Elle est renforcée par la loi Waserman de 2022."),
  Q("Quel lanceur d'alerte révèle en 2013 la surveillance de masse de la NSA ?", ["Edward Snowden", "Julian Assange", "Irène Frachon", "Antoine Deltour"], "Edward Snowden", "Il vit depuis en Russie."),
  Q("Quelle pneumologue française révèle le scandale du Mediator ?", ["Irène Frachon", "Simone Veil", "Marie Curie", "Agnès Buzyn"], "Irène Frachon", "Le médicament est retiré en 2009."),
]),
notion('CC-4', 4, D, 'emc-droits-femmes-monde-avance', [
  Q("Quelle convention de l'ONU de 1979 vise l'élimination de toutes les discriminations envers les femmes ?", ["La CEDAW", "La CIDE", "La DUDH", "La convention de Genève"], "La CEDAW", "Elle est ratifiée par la France en 1983."),
  Q("Quelle convention du Conseil de l'Europe de 2011 lutte contre les violences faites aux femmes ?", ["La convention d'Istanbul", "La convention de Genève", "Le traité de Lisbonne", "La convention de Vienne"], "La convention d'Istanbul", "La Turquie s'en est retirée en 2021."),
  Q("Dans quel pays les femmes sont-elles exclues de l'enseignement secondaire et supérieur depuis le retour des talibans ?", ["L'Afghanistan", "La Tunisie", "Le Maroc", "Le Sénégal"], "L'Afghanistan", "C'est une situation unique au monde."),
]),
notion('CC-4', 5, D, 'emc-aide-developpement', [
  Q("Quel objectif d'aide publique au développement l'ONU fixe-t-elle aux pays riches ?", ["0,7 % du revenu national brut", "10 % du PIB", "0,01 % du PIB", "50 % du budget"], "0,7 % du revenu national brut", "Peu de pays l'atteignent."),
  Q("Quelle agence publique française finance des projets de développement dans le monde ?", ["L'Agence française de développement (AFD)", "Pôle emploi", "La Banque de France", "L'ANSSI"], "L'Agence française de développement (AFD)", "Elle intervient dans plus de 150 pays."),
  Q("Combien d'Objectifs de développement durable l'ONU a-t-elle adoptés en 2015 ?", ["17", "8", "50", "3"], "17", "À atteindre d'ici 2030."),
]),
notion('CC-4', 0, D, 'emc-engagement-politique', [
  Q("À partir de quel âge peut-on adhérer à un parti politique ?", ["Il n'y a pas d'âge légal fixé ; les partis ont souvent des mouvements de jeunes", "21 ans", "30 ans", "Uniquement après avoir voté"], "Il n'y a pas d'âge légal fixé ; les partis ont souvent des mouvements de jeunes", "Ils fixent leurs propres règles."),
  Q("Quel article de la Constitution reconnaît le rôle des partis politiques ?", ["L'article 4", "L'article 1er", "L'article 16", "L'article 89"], "L'article 4", "« Les partis et groupements politiques concourent à l'expression du suffrage »."),
  Q("Comment sont financés en partie les partis politiques en France ?", ["Par une aide publique selon leurs résultats électoraux et leur nombre d'élus", "Par les entreprises sans limite", "Par des États étrangers", "Par la vente de produits"], "Par une aide publique selon leurs résultats électoraux et leur nombre d'élus", "Les dons des entreprises sont interdits depuis 1995."),
]),
]

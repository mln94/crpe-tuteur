# EMC : notions ajoutées pour couvrir chaque section du programme en trois domaines (BO n°31 du 30 juillet 2020)
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ Respecter autrui · Construire le respect de soi ══
notion('RA-1', 0, F, 'emc-respect', [
  Q("Que signifie respecter quelqu'un ?", ["Reconnaître sa dignité et ses droits, quelles que soient nos différences", "Être toujours d'accord avec lui", "Lui obéir en toutes circonstances", "L'éviter pour ne pas le gêner"], "Reconnaître sa dignité et ses droits, quelles que soient nos différences", "Le respect repose sur l'égale dignité de chaque personne."),
  Q("Le respect de soi passe notamment par…", ["prendre soin de sa santé et refuser ce qui nous met en danger", "faire tout ce que le groupe demande", "ne jamais exprimer ses émotions", "se moquer des autres"], "prendre soin de sa santé et refuser ce qui nous met en danger", "Se respecter, c'est aussi savoir dire non."),
  Q("Respecter autrui, c'est notamment…", ["accepter ses différences d'opinion, de culture ou d'apparence", "exiger qu'il pense comme nous", "ignorer ses droits", "le juger sur son apparence"], "accepter ses différences d'opinion, de culture ou d'apparence", "Ma liberté suppose de reconnaître celle des autres."),
]),
notion('RA-1', 1, I, 'emc-addictions', [
  Q("Comment appelle-t-on la dépendance à une substance ou à un comportement (jeux, écrans…) ?", ["Une addiction", "Une allergie", "Une habitude saine", "Une vocation"], "Une addiction", "Le parcours éducatif de santé aborde la prévention des addictions."),
  Q("Qu'appelle-t-on la pression du groupe ?", ["L'influence d'un groupe qui pousse quelqu'un à adopter un comportement", "Une règle de l'établissement", "Une loi votée par le Parlement", "Un exercice de sécurité"], "L'influence d'un groupe qui pousse quelqu'un à adopter un comportement", "Savoir prendre une décision face au groupe est un objectif du programme."),
  Q("La vente d'alcool et de tabac aux mineurs est-elle autorisée en France ?", ["Non, elle est interdite", "Oui, à partir de 14 ans", "Oui, avec l'accord des parents", "Oui, le week-end"], "Non, elle est interdite", "La loi protège les mineurs contre ces produits."),
]),
notion('RA-1', 2, F, 'emc-identite-legale', [
  Q("Quels éléments composent l'identité légale d'une personne ?", ["Son nom, ses prénoms, sa date et son lieu de naissance, sa nationalité", "Ses goûts et ses loisirs", "Son pseudonyme sur les réseaux sociaux", "Son métier"], "Son nom, ses prénoms, sa date et son lieu de naissance, sa nationalité", "Elle est enregistrée à l'état civil."),
  Q("Où est enregistrée la naissance d'un enfant en France ?", ["À l'état civil de la mairie", "Au commissariat", "À l'école", "À la préfecture uniquement"], "À l'état civil de la mairie", "L'acte de naissance est le premier document d'identité légale."),
  Q("Quel document officiel permet de prouver son identité ?", ["La carte nationale d'identité ou le passeport", "La carte de cantine", "Un relevé de notes", "Un abonnement de transport"], "La carte nationale d'identité ou le passeport", "L'identité légale se distingue de l'identité personnelle, construite par chacun."),
]),
notion('RA-1', 2, I, 'emc-identite-numerique', [
  Q("Qu'appelle-t-on l'identité numérique ?", ["L'ensemble des traces et informations qui nous concernent en ligne", "Le numéro de la carte d'identité", "Le mot de passe de sa messagerie", "L'adresse de son domicile"], "L'ensemble des traces et informations qui nous concernent en ligne", "Publications, photos, commentaires et données personnelles la composent."),
  Q("Au nom du « droit à l'oubli », que peut-on demander à un moteur de recherche ?", ["Le déréférencement de certaines informations nous concernant", "La suppression d'Internet", "Le remboursement de ses achats", "L'accès aux données des autres"], "Le déréférencement de certaines informations nous concernant", "Ce droit est reconnu par le règlement européen sur la protection des données (RGPD)."),
  Q("Quel réflexe protège le mieux sa vie privée sur un réseau social ?", ["Paramétrer son compte en privé et limiter les informations publiques", "Accepter tous les inconnus comme amis", "Publier son adresse et son numéro de téléphone", "Partager son mot de passe avec ses amis"], "Paramétrer son compte en privé et limiter les informations publiques", "Ce qui est publié en ligne peut rester visible longtemps."),
]),
notion('RA-1', 3, D, 'emc-responsabilite', [
  N("En dessous de quel âge un mineur est-il présumé ne pas avoir de discernement devant la justice pénale ?", 13, "Le Code de la justice pénale des mineurs (2021) fixe cette présomption simple à 13 ans."),
  Q("Qui est civilement responsable des dommages causés par un enfant mineur ?", ["Ses parents", "Son école dans tous les cas", "Personne", "La mairie"], "Ses parents", "Ils doivent réparer le dommage, souvent grâce à leur assurance."),
  Q("Quelle est la différence entre responsabilité civile et responsabilité pénale ?", ["La civile oblige à réparer un dommage ; la pénale fait répondre d'une infraction et peut entraîner une peine", "Il n'y en a aucune", "La civile concerne les adultes, la pénale les enfants", "La pénale concerne seulement les entreprises"], "La civile oblige à réparer un dommage ; la pénale fait répondre d'une infraction et peut entraîner une peine", "Un même acte peut engager les deux responsabilités."),
]),
# ══ Respecter autrui · La morale et l'éthique ══
notion('RA-3', 0, F, 'emc-temoin', [
  Q("Face à un harcèlement, que doit faire un témoin ?", ["Ne pas rester spectateur et alerter un adulte", "Filmer la scène et la diffuser", "Rire avec les autres", "Faire comme s'il n'avait rien vu"], "Ne pas rester spectateur et alerter un adulte", "Le témoin qui se tait laisse le harcèlement continuer."),
  Q("Comment devient-on complice d'un harcèlement, même sans y participer directement ?", ["En l'encourageant ou en relayant des messages blessants", "En prévenant un professeur", "En soutenant la victime", "En appelant le 3018"], "En l'encourageant ou en relayant des messages blessants", "Partager ou « liker » participe au harcèlement en ligne."),
  Q("Que commet une personne qui ne porte pas secours à quelqu'un en danger alors qu'elle pouvait le faire sans risque ?", ["Le délit de non-assistance à personne en danger", "Rien d'interdit", "Une simple impolitesse", "Une contravention de stationnement"], "Le délit de non-assistance à personne en danger", "Le Code pénal impose d'agir ou au moins d'alerter les secours."),
]),
notion('RA-3', 0, D, 'emc-non-assistance', [
  N("Quelle peine maximale de prison le Code pénal prévoit-il pour la non-assistance à personne en danger (en années) ?", 5, "L'article 223-6 prévoit jusqu'à 5 ans d'emprisonnement et 75 000 € d'amende."),
  Q("L'obligation de porter secours s'applique-t-elle si intervenir mettait le témoin lui-même en danger ?", ["Non, l'aide doit être possible sans risque pour soi ou pour les autres", "Oui, dans tous les cas", "Seulement pour les adultes", "Seulement la nuit"], "Non, l'aide doit être possible sans risque pour soi ou pour les autres", "Dans ce cas, il faut au moins alerter les secours."),
  Q("Que doit faire au minimum un témoin qui ne peut pas intervenir lui-même ?", ["Alerter les secours (15, 17, 18 ou 112)", "Partir", "Prendre une photo", "Attendre que quelqu'un d'autre agisse"], "Alerter les secours (15, 17, 18 ou 112)", "Prévenir les secours, c'est déjà porter assistance."),
]),
notion('RA-3', 1, I, 'emc-decision-juge-medecin', [
  Q("Sur quoi un juge doit-il fonder sa décision ?", ["Sur la loi et les faits établis, de façon impartiale", "Sur son opinion personnelle", "Sur la réputation de l'accusé", "Sur l'avis des réseaux sociaux"], "Sur la loi et les faits établis, de façon impartiale", "L'impartialité du juge est une garantie de l'État de droit."),
  Q("Quelle obligation impose au médecin de garder pour lui ce qu'il apprend de ses patients ?", ["Le secret médical", "Le devoir de réserve des élèves", "La neutralité religieuse", "Le droit de grève"], "Le secret médical", "Il protège la vie privée du patient."),
  Q("Avant un soin, que doit obtenir le médecin du patient, sauf urgence ?", ["Son consentement libre et éclairé", "Une autorisation du maire", "L'accord de ses voisins", "Une décision de justice"], "Son consentement libre et éclairé", "Le patient doit être informé pour pouvoir décider."),
]),
notion('RA-3', 2, F, 'emc-sentiments-moraux', [
  Q("Comment appelle-t-on la capacité à se mettre à la place d'autrui et à comprendre ce qu'il ressent ?", ["L'empathie", "L'indifférence", "L'égoïsme", "La jalousie"], "L'empathie", "L'empathie favorise l'écoute et le respect d'autrui."),
  Q("Quel sentiment moral éprouve-t-on face à une injustice grave ?", ["L'indignation", "L'ennui", "La fierté", "La gourmandise"], "L'indignation", "L'indignation peut conduire à s'engager contre l'injustice."),
  Q("Comment appelle-t-on le sentiment d'avoir mal agi envers quelqu'un ?", ["La culpabilité (ou le remords)", "La joie", "La curiosité", "La surprise"], "La culpabilité (ou le remords)", "Nommer ses sentiments moraux aide à expliquer ses choix et ses actes."),
]),
notion('RA-3', 2, D, 'emc-deontologie', [
  Q("Qu'est-ce que la déontologie ?", ["L'ensemble des règles et des devoirs propres à une profession", "La science des dents", "Un régime politique", "Une branche des mathématiques"], "L'ensemble des règles et des devoirs propres à une profession", "Médecins, avocats, journalistes ou enseignants ont leur déontologie."),
  Q("Quelle obligation impose à un agent public de ne pas manifester ses opinions religieuses ou politiques dans l'exercice de ses fonctions ?", ["Le devoir de neutralité", "Le droit de grève", "La liberté d'expression", "Le secret des sources"], "Le devoir de neutralité", "Il découle du principe de laïcité et d'égalité des usagers."),
  Q("Quelle distinction fait-on souvent entre morale et éthique ?", ["La morale énonce des règles du bien et du mal ; l'éthique réfléchit à leur application dans des situations précises", "Ce sont deux lois votées par le Parlement", "La morale concerne les animaux, l'éthique les humains", "Il n'existe aucune différence"], "La morale énonce des règles du bien et du mal ; l'éthique réfléchit à leur application dans des situations précises", "Les comités d'éthique examinent par exemple les questions de bioéthique."),
]),
# ══ Respecter autrui · Le rôle de la loi dans une société ══
notion('RA-4', 3, F, 'emc-propriete-reglement', [
  Q("Quel texte fixe les droits et les devoirs des élèves dans un collège ?", ["Le règlement intérieur", "Le Code de la route", "La Constitution", "Le Code civil"], "Le règlement intérieur", "Il est adopté par le conseil d'administration et s'appuie sur les valeurs de la République."),
  Q("Le droit de propriété est-il protégé par la Déclaration des droits de l'homme et du citoyen de 1789 ?", ["Oui, elle le qualifie de « droit inviolable et sacré »", "Non", "Seulement pour les entreprises", "Seulement depuis 2000"], "Oui, elle le qualifie de « droit inviolable et sacré »", "C'est l'article 17 de la Déclaration."),
  Q("Que commet une personne qui détruit volontairement le bien d'autrui ?", ["Une infraction (dégradation), punie par la loi", "Un acte autorisé", "Une simple maladresse sans conséquence", "Un acte de solidarité"], "Une infraction (dégradation), punie par la loi", "Elle doit aussi réparer le dommage causé."),
]),
# ══ Acquérir et partager les valeurs de la République ══
notion('VR-1', 2, F, 'emc-symboles-europe', [
  Q("Quel est l'hymne européen ?", ["L'« Ode à la joie » de Beethoven", "La Marseillaise", "Le Chant des partisans", "Le Boléro de Ravel"], "L'« Ode à la joie » de Beethoven", "Il est joué sans paroles, pour ne privilégier aucune langue."),
  Q("Pourquoi le 9 mai est-il la Journée de l'Europe ?", ["C'est l'anniversaire de la déclaration Schuman de 1950", "C'est la date de l'entrée de la France dans l'UE", "C'est la fin de la Première Guerre mondiale", "C'est la naissance de Beethoven"], "C'est l'anniversaire de la déclaration Schuman de 1950", "Robert Schuman y propose la mise en commun du charbon et de l'acier."),
  N("Combien d'étoiles compte le drapeau européen ?", 12, "Le nombre 12 symbolise la perfection et l'unité, pas le nombre d'États membres."),
]),
notion('VR-3', 4, F, 'emc-regalien', [
  Q("Laquelle de ces fonctions est une fonction régalienne de l'État ?", ["La justice", "La vente de vêtements", "L'organisation d'un concert privé", "La fabrication de voitures"], "La justice", "Les fonctions régaliennes sont la défense, la diplomatie, la justice, la police et la fiscalité."),
  Q("Quel ministère conduit la diplomatie de la France ?", ["Le ministère de l'Europe et des Affaires étrangères", "Le ministère de l'Agriculture", "Le ministère des Sports", "Le ministère de la Culture"], "Le ministère de l'Europe et des Affaires étrangères", "Les ambassades représentent la France à l'étranger."),
  Q("Que signifie la déconcentration ?", ["L'État confie des pouvoirs à ses représentants locaux, comme les préfets", "L'État transfère des compétences à des collectivités élues", "L'État supprime ses services", "Les citoyens votent les lois"], "L'État confie des pouvoirs à ses représentants locaux, comme les préfets", "La décentralisation, elle, transfère des compétences aux collectivités territoriales."),
]),
notion('VR-3', 6, I, 'emc-journees-memoire', [
  Q("Que commémore-t-on le 8 mai ?", ["La victoire des Alliés sur l'Allemagne nazie en 1945", "La prise de la Bastille", "L'armistice de 1918", "L'abolition de l'esclavage"], "La victoire des Alliés sur l'Allemagne nazie en 1945", "Le 11 novembre commémore l'armistice de 1918."),
  Q("Que commémore la journée du 27 janvier ?", ["La libération du camp d'Auschwitz et la mémoire de la Shoah", "La fête du travail", "La naissance de la Ve République", "La Journée de l'Europe"], "La libération du camp d'Auschwitz et la mémoire de la Shoah", "C'est la Journée internationale dédiée à la mémoire des victimes de la Shoah."),
  Q("Que commémore la journée nationale du 10 mai en France ?", ["Les mémoires de la traite, de l'esclavage et de leurs abolitions", "La fin de la guerre d'Algérie", "La Libération de Paris", "La fête des mères"], "Les mémoires de la traite, de l'esclavage et de leurs abolitions", "La loi Taubira de 2001 a reconnu la traite et l'esclavage comme crimes contre l'humanité."),
]),
# ══ Construire une culture civique ══
notion('CC-1', 0, F, 'emc-conquete-vote', [
  Q("Le suffrage universel instauré en 1848 concerne-t-il les femmes ?", ["Non, c'est un suffrage universel masculin", "Oui, toutes les femmes", "Seulement les femmes mariées", "Seulement les femmes de plus de 30 ans"], "Non, c'est un suffrage universel masculin", "Les femmes n'obtiennent le droit de vote qu'en 1944."),
  N("En 1974, l'âge du droit de vote passe de 21 ans à combien d'années ?", 18, "La majorité civile et électorale est abaissée à 18 ans."),
  N("Depuis quelle année les citoyens européens résidant en France peuvent-ils voter aux élections municipales ?", 2001, "Ce droit, prévu par le traité de Maastricht (1992), s'applique pour la première fois aux municipales de 2001."),
]),
notion('CC-1', 1, I, 'emc-droits-devoirs-citoyen', [
  Q("Le vote est-il obligatoire en France ?", ["Non : c'est un droit et un devoir civique, mais pas une obligation légale", "Oui, sous peine d'amende", "Oui, seulement pour l'élection présidentielle", "Non, il est réservé aux élus"], "Non : c'est un droit et un devoir civique, mais pas une obligation légale", "Dans d'autres pays, comme la Belgique, le vote est obligatoire."),
  Q("Que faut-il pour pouvoir voter ?", ["Être inscrit sur les listes électorales", "Avoir un emploi", "Être propriétaire", "Avoir le baccalauréat"], "Être inscrit sur les listes électorales", "Les jeunes recensés à 16 ans sont inscrits automatiquement à 18 ans."),
  Q("Lequel de ces éléments est un devoir du citoyen ?", ["Respecter la loi et contribuer aux dépenses publiques par l'impôt", "Voter pour un parti imposé", "Adhérer à un syndicat", "Être membre d'une association"], "Respecter la loi et contribuer aux dépenses publiques par l'impôt", "La citoyenneté associe des droits et des devoirs."),
]),
notion('CC-2', 0, I, 'emc-representation', [
  Q("Dans une démocratie représentative, qui vote les lois ?", ["Les représentants élus par les citoyens", "Chaque citoyen directement, pour chaque loi", "Le président seul", "Les juges"], "Les représentants élus par les citoyens", "Le référendum permet aussi au peuple de décider directement."),
  Q("Qu'est-ce qu'un mandat électif ?", ["La mission confiée par les électeurs à un élu pour une durée limitée", "Un ordre de la police", "Un document d'identité", "Un contrat de travail"], "La mission confiée par les électeurs à un élu pour une durée limitée", "Le mandat se termine par une nouvelle élection."),
  Q("Pourquoi la Constitution interdit-elle le « mandat impératif » ?", ["Parce que chaque député représente la nation entière, et non seulement ses électeurs", "Parce que les élus doivent obéir aux sondages", "Parce que les élus sont nommés par le président", "Parce que le vote est secret"], "Parce que chaque député représente la nation entière, et non seulement ses électeurs", "C'est l'article 27 de la Constitution de 1958."),
]),
notion('CC-2', 2, D, 'emc-transparence', [
  Q("Quelle autorité contrôle les déclarations de patrimoine et d'intérêts des élus depuis 2013 ?", ["La Haute Autorité pour la transparence de la vie publique (HATVP)", "La Cour de cassation", "L'Arcom", "Le Conseil économique, social et environnemental"], "La Haute Autorité pour la transparence de la vie publique (HATVP)", "Elle a été créée après l'affaire Cahuzac."),
  Q("Quand est-il interdit de publier des sondages électoraux en France ?", ["La veille et le jour du scrutin", "Pendant toute la campagne", "Jamais", "Seulement le mois précédent"], "La veille et le jour du scrutin", "Il s'agit d'éviter d'influencer les électeurs au dernier moment."),
  Q("Quelle commission contrôle les comptes de campagne des candidats ?", ["La Commission nationale des comptes de campagne et des financements politiques (CNCCFP)", "La CNIL", "Le Défenseur des droits", "Le Conseil d'État uniquement"], "La Commission nationale des comptes de campagne et des financements politiques (CNCCFP)", "Les dépenses de campagne sont plafonnées par la loi."),
]),
notion('CC-3', 3, I, 'emc-jdc-dissuasion', [
  N("À quel âge les jeunes Français doivent-ils se faire recenser ?", 16, "Le recensement est obligatoire et ouvre la convocation à la Journée défense et citoyenneté."),
  Q("Que permet l'attestation de participation à la Journée défense et citoyenneté ?", ["De s'inscrire aux examens et concours publics, comme le permis ou le baccalauréat, jusqu'à 25 ans", "De voter dès 16 ans", "D'entrer dans l'armée sans autre condition", "De ne pas payer d'impôts"], "De s'inscrire aux examens et concours publics, comme le permis ou le baccalauréat, jusqu'à 25 ans", "La JDC présente les enjeux de la défense et les formes d'engagement."),
  Q("Qu'est-ce que la dissuasion nucléaire ?", ["Posséder l'arme nucléaire pour dissuader tout adversaire de s'en prendre aux intérêts vitaux du pays", "Interdire toute centrale nucléaire", "Attaquer en premier un pays voisin", "Fabriquer de l'électricité"], "Posséder l'arme nucléaire pour dissuader tout adversaire de s'en prendre aux intérêts vitaux du pays", "Le président de la République en est le seul décideur."),
]),
notion('CC-4', 2, F, 'emc-eco-citoyen', [
  Q("Qui sont les éco-délégués au collège ?", ["Des élèves élus pour mener des actions en faveur du développement durable", "Des agents d'entretien", "Des inspecteurs de l'environnement", "Des parents d'élèves"], "Des élèves élus pour mener des actions en faveur du développement durable", "Leur élection est obligatoire dans chaque classe de collège depuis 2020."),
  Q("Que signifie consommer de manière responsable ?", ["Tenir compte des effets sociaux et environnementaux de ses achats", "Acheter toujours le moins cher", "Acheter le plus possible", "N'acheter que des produits importés"], "Tenir compte des effets sociaux et environnementaux de ses achats", "Le consommateur a aussi une responsabilité de citoyen."),
  Q("Que garantit le label « commerce équitable » ?", ["Une rémunération plus juste pour les producteurs", "Un prix toujours plus bas", "Une livraison plus rapide", "Un produit fabriqué en France"], "Une rémunération plus juste pour les producteurs", "Il concerne souvent le café, le cacao ou le coton."),
]),
notion('CC-4', 3, D, 'emc-lanceurs-alerte', [
  Q("Qu'est-ce qu'un lanceur d'alerte ?", ["Une personne qui signale, de bonne foi, une menace ou un préjudice pour l'intérêt général", "Un pompier", "Un journaliste sportif", "Un agent de sécurité routière"], "Une personne qui signale, de bonne foi, une menace ou un préjudice pour l'intérêt général", "Elle révèle par exemple un scandale sanitaire ou une fraude."),
  Q("Quelle loi de 2016 a créé en France un statut protecteur pour les lanceurs d'alerte ?", ["La loi Sapin 2", "La loi Veil", "La loi Ferry", "La loi Pleven"], "La loi Sapin 2", "La protection a été renforcée en 2022."),
  Q("Quel lanceur d'alerte a révélé en 2013 la surveillance de masse des communications par l'agence américaine NSA ?", ["Edward Snowden", "Julian Assange", "Irène Frachon", "Mark Zuckerberg"], "Edward Snowden", "Irène Frachon a, elle, révélé le scandale du Mediator en France."),
]),
notion('CC-4', 4, I, 'emc-droits-femmes-monde', [
  Q("Quel pays a été le premier à accorder le droit de vote aux femmes, en 1893 ?", ["La Nouvelle-Zélande", "La France", "Les États-Unis", "Le Royaume-Uni"], "La Nouvelle-Zélande", "La France ne l'accorde qu'en 1944."),
  Q("Quelle militante britannique a mené le combat des « suffragettes » pour le droit de vote des femmes ?", ["Emmeline Pankhurst", "Simone Veil", "Marie Curie", "Rosa Parks"], "Emmeline Pankhurst", "Les Britanniques obtiennent le vote en 1918, puis à égalité avec les hommes en 1928."),
  N("En quelle année une loi française pose-t-elle le principe « à travail égal, salaire égal » entre femmes et hommes ?", 1972, "Malgré ce principe, des écarts de salaire persistent encore."),
]),
]

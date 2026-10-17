from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('E5-1', 0, F, 'emc-egalite-constitution', [
  Q("Quel texte de valeur constitutionnelle affirme : « La loi garantit à la femme, dans tous les domaines, des droits égaux à ceux de l'homme » ?", ["La DDHC de 1789", "Le préambule de la Constitution de 1946", "Le Code civil de 1804", "La loi de 1905"], "Le préambule de la Constitution de 1946", "Le préambule de 1946, auquel renvoie la Constitution de 1958, garantit l'égalité entre femmes et hommes."),
  Q("L'égalité entre les femmes et les hommes est en France…", ["une simple recommandation", "un principe fondamental garanti par la Constitution", "un principe propre à l'école", "une règle seulement européenne"], "un principe fondamental garanti par la Constitution", "C'est un principe constitutionnel ; c'est aussi un objectif de développement durable de l'ONU (ODD 5)."),
  Q("Pourquoi dit-on que l'égalité des droits entre femmes et hommes est le résultat de combats ?", ["Elle a toujours existé", "Elle a été obtenue progressivement par des luttes et des lois (vote, travail, contraception…)", "Elle date de la Révolution de 1789", "Elle a été imposée par l'Europe"], "Elle a été obtenue progressivement par des luttes et des lois (vote, travail, contraception…)", "Droit de vote (1944), droit de travailler sans autorisation du mari (1965), IVG (1975), parité (2000)… sont des conquêtes successives."),
]),
notion('E5-1', 0, F, 'emc-lois-egalite', [
  N("En quelle année les femmes mariées peuvent-elles exercer une profession sans l'autorisation de leur mari ?", 1965, "La loi du 13 juillet 1965 réforme les régimes matrimoniaux : la femme peut travailler et ouvrir un compte sans l'accord du mari."),
  Q("Que vise la loi sur la parité de 2000 ?", ["L'égalité des salaires", "Favoriser l'égal accès des femmes et des hommes aux mandats électoraux", "Le droit de vote des femmes", "L'égalité à l'école"], "Favoriser l'égal accès des femmes et des hommes aux mandats électoraux", "Elle impose notamment des listes alternant femmes et hommes pour certaines élections."),
  N("En quelle année est adoptée la loi sur la parité en politique ?", 2000, "La loi du 6 juin 2000 met en œuvre la parité, inscrite dans la Constitution en 1999."),
]),
notion('E5-1', 1, F, 'emc-discrimination-definition', [
  Q("Qu'est-ce qu'une discrimination ?", ["Une simple différence d'opinion", "Un traitement défavorable fondé sur un critère interdit par la loi (origine, sexe, handicap…)", "Une sanction scolaire", "Un choix personnel"], "Un traitement défavorable fondé sur un critère interdit par la loi (origine, sexe, handicap…)", "La discrimination est un délit puni par la loi, par exemple dans l'accès à l'emploi ou au logement."),
  Q("Lequel de ces critères est un motif de discrimination interdit par la loi ?", ["L'adresse e-mail", "Le handicap", "La couleur préférée", "Le prénom d'un animal"], "Le handicap", "La loi interdit plus de 25 critères de discrimination, dont l'origine, le sexe, le handicap, la religion ou l'orientation sexuelle."),
  Q("Refuser un logement à quelqu'un en raison de son origine est…", ["autorisé si le propriétaire le souhaite", "une discrimination punie par la loi", "une simple impolitesse", "une liberté du propriétaire"], "une discrimination punie par la loi", "Le Code pénal punit la discrimination, notamment dans l'accès au logement ou à l'emploi."),
]),
notion('E5-1', 1, F, 'emc-stereotypes-prejuges', [
  Q("Qu'est-ce qu'un stéréotype ?", ["Une connaissance scientifique", "Une idée toute faite et simplificatrice sur un groupe de personnes", "Une loi", "Un droit fondamental"], "Une idée toute faite et simplificatrice sur un groupe de personnes", "« Les filles sont moins bonnes en maths » est un stéréotype : il peut conduire à des discriminations."),
  Q("Qu'est-ce qu'un préjugé ?", ["Un jugement porté sans connaître réellement la personne ou le groupe", "Une décision de justice", "Une preuve", "Une règle de politesse"], "Un jugement porté sans connaître réellement la personne ou le groupe", "Le préjugé est une opinion préconçue, souvent négative, qui peut nourrir le rejet de l'autre."),
  Q("Quel exemple illustre un stéréotype de genre ?", ["« Ce métier demande de la formation »", "« Le football, c'est pour les garçons »", "« Il pleut aujourd'hui »", "« L'école est obligatoire »"], "« Le football, c'est pour les garçons »", "Attribuer des goûts ou des capacités selon le sexe est un stéréotype de genre."),
]),
notion('E5-1', 1, F, 'emc-defenseur-des-droits', [
  Q("Quelle autorité indépendante peut être saisie par une victime de discrimination ?", ["Le Défenseur des droits", "Le maire", "Le Conseil d'État", "Le Sénat"], "Le Défenseur des droits", "Créé en 2011, le Défenseur des droits lutte contre les discriminations et défend les droits des enfants."),
  Q("Le Défenseur des droits défend notamment…", ["les droits de l'enfant", "les intérêts des entreprises", "les partis politiques", "les syndicats uniquement"], "les droits de l'enfant", "L'une de ses missions est la défense et la promotion des droits de l'enfant."),
  N("En quelle année est créé le Défenseur des droits ?", 2011, "Inscrit dans la Constitution en 2008, le Défenseur des droits est institué en 2011."),
]),
notion('E5-1', 1, F, 'emc-harcelement', [
  N("Quel est le numéro national gratuit contre le harcèlement et le cyberharcèlement ?", 3018, "Le 3018 aide les victimes de harcèlement et de cyberharcèlement (écoute, signalement, suppression de contenus)."),
  Q("Le harcèlement scolaire se caractérise par…", ["une dispute isolée", "des violences répétées, avec une volonté de nuire et un isolement de la victime", "une mauvaise note", "une punition"], "des violences répétées, avec une volonté de nuire et un isolement de la victime", "La répétition et le rapport de domination distinguent le harcèlement d'un simple conflit."),
  Q("Depuis la loi de 2022, le harcèlement scolaire est…", ["autorisé hors de l'école", "un délit pénal", "une simple faute de règlement", "réservé au collège"], "un délit pénal", "La loi du 2 mars 2022 fait du harcèlement scolaire un délit, puni de peines pouvant aller jusqu'à 10 ans de prison dans les cas les plus graves."),
]),
notion('E5-2', 0, F, 'emc-fraternite', [
  Q("Quelle est la devise de la République française ?", ["Unité, Progrès, Justice", "Liberté, Égalité, Fraternité", "Travail, Famille, Patrie", "Paix et Liberté"], "Liberté, Égalité, Fraternité", "Elle est inscrite à l'article 2 de la Constitution."),
  Q("En 2018, le Conseil constitutionnel reconnaît la fraternité comme…", ["une simple valeur morale", "un principe à valeur constitutionnelle", "une loi ordinaire", "un symbole sans portée"], "un principe à valeur constitutionnelle", "La décision du 6 juillet 2018 en déduit la liberté d'aider autrui dans un but humanitaire."),
  Q("Que signifie la fraternité ?", ["Seulement les liens entre frères et sœurs", "Considérer l'autre comme son égal et lui venir en aide", "Obéir aux lois", "Payer ses impôts"], "Considérer l'autre comme son égal et lui venir en aide", "La fraternité fonde la solidarité entre citoyens."),
]),
notion('E5-2', 0, F, 'emc-solidarite', [
  Q("Qu'est-ce que la solidarité ?", ["L'indifférence aux autres", "L'entraide entre les membres d'une société", "La compétition", "La concurrence économique"], "L'entraide entre les membres d'une société", "La solidarité peut être individuelle, associative ou organisée par l'État."),
  Q("Quel dispositif public est un exemple de solidarité nationale ?", ["La Sécurité sociale", "La publicité", "Le marché boursier", "Le tourisme"], "La Sécurité sociale", "Chacun cotise selon ses moyens et reçoit selon ses besoins (maladie, retraite, famille)."),
  Q("Les impôts participent à la solidarité car ils…", ["financent uniquement l'armée", "financent les services publics accessibles à tous", "sont reversés aux entreprises", "ne servent à rien"], "financent les services publics accessibles à tous", "École, hôpitaux, routes ou aides sociales sont financés par l'impôt."),
]),
notion('E5-2', 1, F, 'emc-securite-sociale', [
  N("En quelle année est créée la Sécurité sociale en France ?", 1945, "Les ordonnances d'octobre 1945 créent la Sécurité sociale."),
  Q("Quelle branche de la Sécurité sociale rembourse les soins médicaux ?", ["La branche famille", "L'assurance maladie", "La branche retraite", "La branche chômage"], "L'assurance maladie", "L'Assurance maladie rembourse une partie des frais de santé."),
  Q("Sur quel principe repose la Sécurité sociale ?", ["Chacun paie selon ses moyens et reçoit selon ses besoins", "Seuls les riches sont soignés", "Chacun paie le même montant", "L'aide est réservée aux fonctionnaires"], "Chacun paie selon ses moyens et reçoit selon ses besoins", "C'est un système de solidarité nationale."),
]),
notion('E5-2', 1, F, 'emc-numeros-urgence', [
  N("Quel numéro appelle-t-on pour joindre le SAMU ?", 15, "Le 15 joint le SAMU (urgences médicales) ; le 17 la police, le 18 les pompiers, le 112 les secours dans toute l'Europe."),
  N("Quel est le numéro d'appel d'urgence européen, valable dans tous les pays de l'Union européenne ?", 112, "Le 112 est le numéro d'urgence européen, gratuit, accessible depuis tous les téléphones."),
  N("Quel numéro appelle-t-on pour joindre les sapeurs-pompiers ?", 18, "Les pompiers (18) interviennent pour les incendies, les accidents et le secours aux personnes."),
]),
notion('E5-2', 1, F, 'emc-associations', [
  N("En quelle année est votée la loi sur la liberté d'association ?", 1901, "La loi du 1er juillet 1901 permet de créer librement une association à but non lucratif."),
  Q("Quel est le but d'une association « loi 1901 » ?", ["Faire des bénéfices pour ses membres", "Poursuivre un but non lucratif (culture, sport, solidarité…)", "Gouverner une commune", "Rendre la justice"], "Poursuivre un but non lucratif (culture, sport, solidarité…)", "Une association réunit des personnes autour d'un projet commun sans partage des bénéfices."),
  Q("Laquelle de ces organisations est une association de solidarité ?", ["Les Restos du cœur", "L'Assemblée nationale", "La Banque de France", "La SNCF"], "Les Restos du cœur", "Fondés par Coluche en 1985, les Restos du cœur distribuent des repas aux personnes démunies."),
]),
notion('E4-1', 0, F, 'emc-separation-pouvoirs', [
  Q("Quels sont les trois pouvoirs distingués par Montesquieu ?", ["Législatif, exécutif, judiciaire", "Militaire, religieux, civil", "Local, national, européen", "Économique, social, culturel"], "Législatif, exécutif, judiciaire", "Leur séparation empêche la concentration du pouvoir et protège les libertés."),
  Q("Quelle institution détient le pouvoir législatif en France ?", ["Le Gouvernement", "Le Parlement", "Le Conseil constitutionnel", "Le président seul"], "Le Parlement", "Le Parlement (Assemblée nationale et Sénat) vote les lois."),
  Q("Qui exerce le pouvoir judiciaire ?", ["Les députés", "Les juges et les tribunaux", "Les préfets", "Les maires"], "Les juges et les tribunaux", "Les juges appliquent la loi pour trancher les litiges et sanctionner les infractions."),
]),
notion('E4-1', 0, F, 'emc-etat-de-droit', [
  Q("Qu'est-ce qu'un État de droit ?", ["Un État où le chef décide seul", "Un État où tous, y compris les dirigeants, sont soumis au droit", "Un État sans lois", "Un État religieux"], "Un État où tous, y compris les dirigeants, sont soumis au droit", "Dans un État de droit, les pouvoirs publics respectent les règles de droit et les libertés sont garanties par des juges indépendants."),
  Q("Quel texte est placé au sommet de la hiérarchie des normes en France ?", ["Un décret", "La Constitution", "Un arrêté municipal", "Un règlement intérieur"], "La Constitution", "La Constitution est au sommet ; les lois et les règlements doivent la respecter."),
  Q("Quelle institution vérifie que les lois respectent la Constitution ?", ["Le Conseil d'État", "Le Conseil constitutionnel", "La Cour des comptes", "Le Sénat"], "Le Conseil constitutionnel", "Le Conseil constitutionnel contrôle la conformité des lois à la Constitution."),
]),
notion('E4-1', 0, F, 'emc-presomption-innocence', [
  Q("Que signifie la présomption d'innocence ?", ["Toute personne accusée est coupable", "Toute personne est considérée innocente tant que sa culpabilité n'a pas été établie par un jugement", "Les juges sont toujours innocents", "On ne peut jamais être condamné"], "Toute personne est considérée innocente tant que sa culpabilité n'a pas été établie par un jugement", "Ce principe est affirmé à l'article 9 de la DDHC."),
  Q("Quel droit est garanti à toute personne jugée ?", ["Le droit à une défense, notamment par un avocat", "Le droit de choisir son juge", "Le droit de ne pas être jugée", "Le droit de fixer sa peine"], "Le droit à une défense, notamment par un avocat", "Le droit à un procès équitable comprend le droit d'être défendu."),
  Q("À partir de quel âge un mineur peut-il faire l'objet d'une sanction pénale en principe, selon le code de la justice pénale des mineurs (2021) ?", ["10 ans", "13 ans", "16 ans", "18 ans"], "13 ans", "Il existe une présomption simple de non-discernement avant 13 ans ; la justice des mineurs privilégie l'éducatif."),
]),
notion('E4-1', 1, F, 'emc-libertes-fondamentales', [
  Q("Quel article de la DDHC proclame : « Les hommes naissent et demeurent libres et égaux en droits » ?", ["L'article 1", "L'article 10", "L'article 17", "L'article 6"], "L'article 1", "C'est le premier article de la Déclaration des droits de l'homme et du citoyen de 1789."),
  Q("Selon la DDHC, la liberté consiste à…", ["faire tout ce que l'on veut", "pouvoir faire tout ce qui ne nuit pas à autrui", "obéir au roi", "ne jamais respecter de règles"], "pouvoir faire tout ce qui ne nuit pas à autrui", "L'article 4 de la DDHC fixe cette limite : la liberté s'arrête là où elle nuit à autrui."),
  Q("La liberté d'expression permet-elle d'insulter ou d'appeler à la haine ?", ["Oui, sans limite", "Non, la loi punit l'injure, la diffamation et l'incitation à la haine", "Oui, sur Internet uniquement", "Oui, si l'on est majeur"], "Non, la loi punit l'injure, la diffamation et l'incitation à la haine", "La liberté d'expression a des limites fixées par la loi pour protéger les personnes."),
]),
notion('E4-1', 1, F, 'emc-liberte-presse', [
  N("En quelle année est votée la grande loi sur la liberté de la presse ?", 1881, "La loi du 29 juillet 1881 garantit la liberté de la presse ; elle encadre aussi l'injure et la diffamation."),
  Q("Pourquoi la liberté de la presse est-elle essentielle en démocratie ?", ["Elle permet d'informer les citoyens et de critiquer les pouvoirs", "Elle permet de diffuser des fausses informations", "Elle remplace les élections", "Elle protège seulement les journalistes"], "Elle permet d'informer les citoyens et de critiquer les pouvoirs", "Une presse libre est un contre-pouvoir indispensable au débat démocratique."),
  Q("Qu'est-ce que la diffamation ?", ["Une critique artistique", "L'affirmation d'un fait précis qui porte atteinte à l'honneur d'une personne", "Une opinion politique", "Une information vérifiée"], "L'affirmation d'un fait précis qui porte atteinte à l'honneur d'une personne", "La diffamation est punie par la loi de 1881 ; l'injure est une expression outrageante sans fait précis."),
]),
notion('E4-1', 1, F, 'emc-laicite', [
  N("En quelle année est votée la loi de séparation des Églises et de l'État ?", 1905, "La loi du 9 décembre 1905 fonde la laïcité de l'État."),
  Q("Qu'implique la laïcité pour l'État ?", ["Il favorise une religion", "Il est neutre et garantit la liberté de conscience de tous", "Il interdit toutes les religions", "Il finance les cultes"], "Il est neutre et garantit la liberté de conscience de tous", "La République ne reconnaît, ne salarie ni ne subventionne aucun culte, et garantit le libre exercice des cultes."),
  Q("La laïcité garantit-elle le droit de ne pas avoir de religion ?", ["Non", "Oui, c'est la liberté de conscience", "Seulement pour les adultes", "Seulement à l'école"], "Oui, c'est la liberté de conscience", "Chacun est libre de croire ou de ne pas croire, et de changer de religion."),
]),
notion('E4-1', 1, F, 'emc-laicite-ecole', [
  N("En quelle année est publiée la Charte de la laïcité à l'École ?", 2013, "La Charte de la laïcité à l'École (15 articles) est affichée dans les établissements publics depuis 2013."),
  Q("Que prévoit la loi du 15 mars 2004 pour les élèves des écoles, collèges et lycées publics ?", ["L'obligation de porter un uniforme", "L'interdiction des signes et tenues manifestant ostensiblement une appartenance religieuse", "L'interdiction de toute croyance", "L'enseignement obligatoire d'une religion"], "L'interdiction des signes et tenues manifestant ostensiblement une appartenance religieuse", "Elle protège les élèves de toute pression et préserve la neutralité de l'école publique."),
  Q("Le professeur d'une école publique est-il tenu à la neutralité religieuse ?", ["Non, il est libre de manifester sa religion en classe", "Oui, comme tout agent public", "Seulement en primaire", "Seulement pendant les examens"], "Oui, comme tout agent public", "Les agents publics ont un devoir strict de neutralité dans l'exercice de leurs fonctions."),
]),
notion('E4-2', 0, F, 'emc-defense-nationale', [
  Q("Qui est le chef des armées en France ?", ["Le Premier ministre", "Le président de la République", "Le ministre des Armées", "Le chef d'état-major"], "Le président de la République", "L'article 15 de la Constitution fait du président le chef des armées."),
  Q("Quelle journée tous les jeunes Français doivent-ils effectuer, après leur recensement ?", ["La journée du patrimoine", "La journée défense et citoyenneté (JDC)", "La journée de solidarité", "La journée du 14 Juillet"], "La journée défense et citoyenneté (JDC)", "La JDC présente les enjeux de la défense ; elle suit le recensement obligatoire à 16 ans."),
  N("En quelle année est décidée la suspension du service militaire obligatoire en France ?", 1997, "La loi de 1997 suspend le service national ; l'armée devient professionnelle."),
]),
notion('E4-2', 0, F, 'emc-forces-securite', [
  Q("Quelle force de sécurité, à statut militaire, assure la sécurité surtout dans les zones rurales et périurbaines ?", ["La police nationale", "La gendarmerie nationale", "La police municipale", "L'armée de l'air"], "La gendarmerie nationale", "La gendarmerie est militaire ; la police nationale, civile, agit surtout en zone urbaine."),
  Q("Quel plan de vigilance contre le terrorisme est appliqué en France ?", ["Le plan Orsec", "Le plan Vigipirate", "Le plan Marshall", "Le plan Blanc"], "Le plan Vigipirate", "Vigipirate associe l'État, les collectivités et les citoyens à la vigilance face à la menace terroriste."),
  N("À quel âge doit-on se faire recenser en France ?", 16, "Le recensement est obligatoire à 16 ans ; il permet l'inscription sur les listes électorales et la convocation à la JDC."),
]),
notion('E4-2', 1, F, 'emc-cybermenaces', [
  Q("Qu'est-ce qu'une « fake news » ?", ["Une information vérifiée", "Une information fausse diffusée volontairement ou non", "Un article de presse ancien", "Une publicité"], "Une information fausse diffusée volontairement ou non", "Les fausses informations circulent vite sur les réseaux sociaux : il faut vérifier les sources."),
  Q("Quel réflexe adopter avant de partager une information sur les réseaux sociaux ?", ["La partager vite", "Vérifier la source et croiser avec d'autres médias fiables", "Ajouter un commentaire", "Ne lire que le titre"], "Vérifier la source et croiser avec d'autres médias fiables", "Identifier l'auteur, la date et la source, puis comparer avec d'autres sources permet de repérer les fausses informations."),
  Q("Comment appelle-t-on une tentative de vol d'identifiants par un faux message imitant un organisme connu ?", ["L'hameçonnage (phishing)", "Le streaming", "Le cookie", "Le spam publicitaire"], "L'hameçonnage (phishing)", "Le phishing pousse la victime à donner ses mots de passe ou ses coordonnées bancaires."),
]),
notion('E3-1', 0, F, 'emc-president', [
  Q("Pour combien d'années le président de la République est-il élu ?", ["4 ans", "5 ans", "6 ans", "7 ans"], "5 ans", "Le quinquennat est en vigueur depuis 2002 (référendum de 2000)."),
  Q("Comment le président de la République est-il élu ?", ["Par les députés", "Au suffrage universel direct", "Par les sénateurs", "Par les maires"], "Au suffrage universel direct", "Les citoyens élisent directement le président, au scrutin majoritaire à deux tours."),
  Q("Combien de mandats consécutifs un président peut-il exercer au maximum ?", ["Un", "Deux", "Trois", "Sans limite"], "Deux", "Depuis la révision de 2008, nul ne peut exercer plus de deux mandats consécutifs."),
]),
notion('E3-1', 0, F, 'emc-parlement', [
  N("Combien de députés siègent à l'Assemblée nationale ?", 577, "577 députés sont élus au suffrage universel direct pour 5 ans."),
  Q("Comment sont élus les sénateurs ?", ["Au suffrage universel direct", "Au suffrage universel indirect, par des grands électeurs", "Par le président", "Par tirage au sort"], "Au suffrage universel indirect, par des grands électeurs", "Les sénateurs sont élus pour 6 ans par des élus locaux (grands électeurs)."),
  Q("Quelle assemblée peut renverser le gouvernement par une motion de censure ?", ["Le Sénat", "L'Assemblée nationale", "Le Conseil constitutionnel", "Le Conseil économique, social et environnemental"], "L'Assemblée nationale", "Le gouvernement est responsable devant l'Assemblée nationale."),
]),
notion('E3-1', 0, F, 'emc-droit-de-vote', [
  N("À partir de quel âge peut-on voter en France ?", 18, "Le droit de vote est accordé à 18 ans depuis 1974."),
  Q("Quelles conditions faut-il remplir pour voter aux élections présidentielles ?", ["Être majeur, de nationalité française et inscrit sur les listes électorales", "Avoir un emploi", "Payer un impôt", "Être propriétaire"], "Être majeur, de nationalité française et inscrit sur les listes électorales", "Les citoyens de l'Union européenne peuvent aussi voter aux élections municipales et européennes."),
  Q("Le vote en France est…", ["obligatoire", "un droit, personnel et secret", "public", "réservé aux hommes"], "un droit, personnel et secret", "Le vote est secret (isoloir) et personnel ; il n'est pas obligatoire en France."),
]),
notion('E3-1', 0, F, 'emc-referendum', [
  Q("Qu'est-ce qu'un référendum ?", ["Une élection de députés", "Un vote par lequel les citoyens répondent directement par oui ou par non à une question", "Une réunion du gouvernement", "Un jugement"], "Un vote par lequel les citoyens répondent directement par oui ou par non à une question", "Le référendum est une forme de démocratie directe."),
  N("En quelle année est adoptée par référendum la Constitution de la Ve République ?", 1958, "Le référendum du 28 septembre 1958 approuve la nouvelle Constitution."),
  Q("Comment appelle-t-on le régime où les citoyens élisent des représentants qui décident en leur nom ?", ["La démocratie directe", "La démocratie représentative", "La monarchie", "La dictature"], "La démocratie représentative", "En France, la démocratie est surtout représentative, avec quelques outils de démocratie directe comme le référendum."),
]),
notion('E3-1', 1, F, 'emc-article-1-constitution', [
  Q("Selon l'article 1er de la Constitution, la France est une République…", ["fédérale, laïque et sociale", "indivisible, laïque, démocratique et sociale", "religieuse et démocratique", "monarchique et sociale"], "indivisible, laïque, démocratique et sociale", "Ce sont les quatre caractères de la République française."),
  Q("Que signifie le caractère « indivisible » de la République ?", ["Le territoire et la souveraineté ne peuvent être partagés ; la loi est la même pour tous", "Les régions sont indépendantes", "La République ne peut pas être modifiée", "Il n'y a qu'un seul parti"], "Le territoire et la souveraineté ne peuvent être partagés ; la loi est la même pour tous", "L'indivisibilité garantit l'unité de la nation et l'égalité devant la loi."),
  Q("Que signifie le caractère « social » de la République ?", ["Elle organise des fêtes", "Elle garantit des droits sociaux et une solidarité (santé, éducation, protection)", "Elle interdit les entreprises", "Elle est gouvernée par les syndicats"], "Elle garantit des droits sociaux et une solidarité (santé, éducation, protection)", "La République sociale cherche à réduire les inégalités et à protéger chacun."),
]),
notion('E3-1', 1, F, 'emc-symboles', [
  Q("Quelles sont les couleurs du drapeau français ?", ["Bleu, blanc, rouge", "Bleu, blanc, vert", "Rouge, blanc, noir", "Bleu, jaune, rouge"], "Bleu, blanc, rouge", "Le drapeau tricolore est l'emblème national (article 2 de la Constitution)."),
  Q("Quelle est la fête nationale française ?", ["Le 8 mai", "Le 14 juillet", "Le 11 novembre", "Le 1er mai"], "Le 14 juillet", "Elle commémore la prise de la Bastille (1789) et la fête de la Fédération (1790)."),
  Q("Qui a composé La Marseillaise ?", ["Victor Hugo", "Rouget de Lisle", "Hector Berlioz", "Napoléon"], "Rouget de Lisle", "Rouget de Lisle la compose en 1792 ; elle devient hymne national en 1795, puis définitivement en 1879."),
]),
notion('E3-2', 0, F, 'emc-medias', [
  Q("Quel rôle jouent les médias dans une démocratie ?", ["Imposer une opinion unique", "Informer les citoyens et permettre le débat", "Remplacer le Parlement", "Voter les lois"], "Informer les citoyens et permettre le débat", "Des médias libres et pluralistes sont indispensables à la formation de l'opinion."),
  Q("Qu'est-ce que le pluralisme des médias ?", ["L'existence d'un seul média public", "L'existence de médias variés exprimant des opinions différentes", "L'interdiction de la presse", "La publicité dans les médias"], "L'existence de médias variés exprimant des opinions différentes", "Le pluralisme permet aux citoyens de confronter les points de vue."),
  Q("Comment appelle-t-on l'ensemble des opinions partagées par une partie importante de la population à un moment donné ?", ["L'opinion publique", "La loi", "La constitution", "La propagande"], "L'opinion publique", "Les sondages, les médias et les réseaux sociaux participent à sa formation et à sa mesure."),
]),
notion('E3-2', 1, F, 'emc-esprit-critique', [
  Q("Quelle question se poser en premier face à une information trouvée sur Internet ?", ["Qui en est l'auteur et quelle est la source ?", "Combien de « j'aime » a-t-elle ?", "Est-elle drôle ?", "Est-elle récente sur mon fil ?"], "Qui en est l'auteur et quelle est la source ?", "Identifier la source permet d'évaluer la fiabilité d'une information."),
  Q("Qu'est-ce qu'une théorie du complot ?", ["Une enquête journalistique vérifiée", "Une explication qui attribue un événement à l'action secrète d'un groupe, sans preuve fiable", "Une décision de justice", "Une loi"], "Une explication qui attribue un événement à l'action secrète d'un groupe, sans preuve fiable", "Le complotisme rejette les explications établies au profit d'un récit invérifiable."),
  Q("Comment appelle-t-on les algorithmes des réseaux sociaux qui nous montrent surtout des contenus proches de nos opinions ?", ["Des bulles de filtres", "Des moteurs de recherche neutres", "Des pare-feu", "Des antivirus"], "Des bulles de filtres", "Les bulles de filtres enferment l'utilisateur dans des contenus qui confirment ce qu'il pense déjà."),
]),
notion('E3-3', 0, F, 'emc-partis-syndicats', [
  Q("Quel est le rôle d'un parti politique ?", ["Défendre les intérêts d'une profession", "Rassembler des citoyens autour d'idées et présenter des candidats aux élections", "Rendre la justice", "Gérer une entreprise"], "Rassembler des citoyens autour d'idées et présenter des candidats aux élections", "L'article 4 de la Constitution reconnaît le rôle des partis dans l'expression du suffrage."),
  Q("Quel est le rôle d'un syndicat ?", ["Présenter un candidat à la présidentielle", "Défendre les intérêts des salariés ou d'une profession", "Voter les lois", "Diriger l'armée"], "Défendre les intérêts des salariés ou d'une profession", "Les syndicats négocient avec les employeurs et peuvent appeler à la grève."),
  Q("Le droit de grève est-il reconnu en France ?", ["Non", "Oui, par le préambule de la Constitution de 1946", "Seulement pour les fonctionnaires", "Seulement dans l'industrie"], "Oui, par le préambule de la Constitution de 1946", "Le droit de grève s'exerce dans le cadre des lois qui le réglementent."),
]),
notion('E3-3', 1, F, 'emc-engagement', [
  Q("Laquelle de ces actions est une forme d'engagement citoyen ?", ["Faire du bénévolat dans une association", "Regarder un film", "Faire ses courses", "Dormir"], "Faire du bénévolat dans une association", "S'engager, c'est agir pour une cause collective : bénévolat, vote, délégué de classe…"),
  Q("Qu'est-ce que le service civique ?", ["Un service militaire obligatoire", "Un engagement volontaire de 6 à 12 mois au service de l'intérêt général, pour les 16-25 ans", "Un emploi dans une entreprise privée", "Un stage scolaire obligatoire"], "Un engagement volontaire de 6 à 12 mois au service de l'intérêt général, pour les 16-25 ans", "Le service civique est indemnisé ; il s'ouvre jusqu'à 30 ans pour les jeunes en situation de handicap."),
  Q("Au collège, comment les élèves participent-ils à la vie démocratique de l'établissement ?", ["En élisant des délégués de classe", "En choisissant les programmes", "En recrutant les professeurs", "En fixant les notes"], "En élisant des délégués de classe", "Les délégués représentent leurs camarades, notamment au conseil de classe."),
]),
notion('E5-1', 0, F, 'emc-violences-sexistes', [
  Q("Quel numéro national gratuit et anonyme écoute les femmes victimes de violences ?", ["Le 3919", "Le 3018", "Le 119", "Le 15"], "Le 3919", "Le 3919 « Violences Femmes Info » écoute, informe et oriente les victimes, 24 h/24."),
  N("Quel numéro national gratuit est dédié à l'enfance en danger ?", 119, "Le 119 « Allô Enfance en danger » est joignable gratuitement 24 h/24, y compris par les enfants eux-mêmes."),
  Q("Les violences sexistes et sexuelles sont…", ["tolérées dans le cadre privé", "punies par la loi, y compris au sein du couple", "une affaire uniquement familiale", "autorisées entre mineurs"], "punies par la loi, y compris au sein du couple", "La loi punit ces violences et protège les victimes, quel que soit le cadre."),
]),
notion('E4-1', 0, F, 'emc-justice', [
  Q("Quelle juridiction juge les crimes les plus graves (meurtre, viol…) ?", ["Le tribunal de police", "La cour d'assises (ou la cour criminelle départementale)", "Le conseil de prud'hommes", "Le tribunal administratif"], "La cour d'assises (ou la cour criminelle départementale)", "Les crimes sont jugés par la cour d'assises, avec des jurés citoyens, ou par la cour criminelle départementale pour certains crimes."),
  Q("Quelle juridiction règle les conflits entre salariés et employeurs ?", ["Le conseil de prud'hommes", "La cour d'assises", "Le Conseil constitutionnel", "Le tribunal de commerce"], "Le conseil de prud'hommes", "Les prud'hommes jugent les litiges liés au contrat de travail."),
  Q("Comment appelle-t-on les citoyens tirés au sort pour juger à la cour d'assises ?", ["Les avocats", "Les jurés", "Les greffiers", "Les huissiers"], "Les jurés", "Les jurés participent au jugement des crimes avec des magistrats professionnels."),
]),
notion('E3-1', 0, F, 'emc-gouvernement', [
  Q("Qui nomme le Premier ministre ?", ["L'Assemblée nationale", "Le président de la République", "Le Sénat", "Les citoyens"], "Le président de la République", "Le président nomme le Premier ministre (article 8), en tenant compte de la majorité à l'Assemblée."),
  Q("Quel est le rôle du Gouvernement ?", ["Juger les délits", "Déterminer et conduire la politique de la nation", "Contrôler la constitutionnalité des lois", "Élire le président"], "Déterminer et conduire la politique de la nation", "Le Gouvernement exerce le pouvoir exécutif avec le président (article 20)."),
  Q("Qui dirige l'action du Gouvernement ?", ["Le président du Sénat", "Le Premier ministre", "Le ministre de l'Intérieur", "Le maire de Paris"], "Le Premier ministre", "Le Premier ministre dirige l'action du Gouvernement (article 21)."),
]),
notion('E3-1', 0, F, 'emc-collectivites', [
  Q("Qui élit le maire d'une commune ?", ["Directement les habitants", "Le conseil municipal", "Le préfet", "Le président de la République"], "Le conseil municipal", "Les habitants élisent les conseillers municipaux, qui élisent ensuite le maire parmi eux."),
  Q("Quelle collectivité territoriale gère les collèges ?", ["La commune", "Le département", "La région", "L'État seul"], "Le département", "Les départements construisent et entretiennent les collèges ; les régions, les lycées ; les communes, les écoles."),
  Q("Quelle collectivité gère les écoles maternelles et élémentaires (bâtiments, cantine) ?", ["La commune", "La région", "Le département", "L'Union européenne"], "La commune", "La commune construit et entretient les écoles ; l'État rémunère les professeurs et fixe les programmes."),
]),
notion('E5-2', 1, F, 'emc-securite-civile', [
  Q("Quel plan organise les secours en cas de catastrophe de grande ampleur en France ?", ["Le plan Orsec", "Le plan Vigipirate", "Le plan Marshall", "Le plan local d'urbanisme"], "Le plan Orsec", "Le plan Orsec (Organisation de la réponse de sécurité civile) coordonne les moyens de secours."),
  Q("Quelle est la mission principale des sapeurs-pompiers ?", ["Rendre la justice", "Protéger les personnes et les biens et porter secours", "Percevoir les impôts", "Enseigner"], "Protéger les personnes et les biens et porter secours", "La grande majorité des sapeurs-pompiers en France sont des volontaires."),
  Q("Qui coordonne les secours dans un département lors d'une catastrophe ?", ["Le maire seul", "Le préfet", "Le président de région", "Le député"], "Le préfet", "Le préfet, représentant de l'État dans le département, dirige les opérations de secours de grande ampleur."),
]),
notion('E4-1', 1, F, 'emc-droits-enfant', [
  N("En quelle année l'ONU adopte-t-elle la Convention internationale des droits de l'enfant ?", 1989, "Adoptée le 20 novembre 1989, elle est ratifiée par la France en 1990."),
  Q("Lequel de ces droits est garanti par la Convention internationale des droits de l'enfant ?", ["Le droit de voter", "Le droit à l'éducation", "Le droit de travailler dès 10 ans", "Le droit de conduire"], "Le droit à l'éducation", "La Convention garantit notamment le droit à l'éducation, à la santé, à la protection et à être entendu."),
  N("Quel jour de novembre est la Journée internationale des droits de l'enfant ?", 20, "Le 20 novembre commémore l'adoption de la Convention en 1989."),
]),
notion('E5-1', 0, F, 'emc-egalite-ecole', [
  Q("Depuis quand l'instruction est-elle obligatoire en France dès 3 ans ?", ["1882", "1959", "2019", "1989"], "2019", "La loi pour une école de la confiance (2019) abaisse l'âge de l'instruction obligatoire à 3 ans."),
  Q("Jusqu'à quel âge la formation est-elle obligatoire en France ?", ["14 ans", "16 ans", "18 ans", "21 ans"], "18 ans", "L'instruction est obligatoire de 3 à 16 ans, et la formation jusqu'à 18 ans depuis 2020."),
  Q("La mixité filles-garçons dans les écoles publiques est généralisée à partir…", ["de 1882", "des années 1960-1970 (loi Haby de 1975)", "de 2004", "de 1789"], "des années 1960-1970 (loi Haby de 1975)", "La mixité se généralise dans les années 1960 et devient obligatoire avec la loi Haby (1975)."),
]),
notion('E3-1', 1, F, 'emc-souverainete', [
  Q("Selon l'article 3 de la Constitution, à qui appartient la souveraineté nationale ?", ["Au président", "Au peuple", "Au Parlement", "Aux juges"], "Au peuple", "« La souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum. »"),
  Q("Le suffrage universel signifie que…", ["seuls les riches votent", "tous les citoyens majeurs ont le droit de vote, sans condition de fortune", "le vote est obligatoire", "seuls les hommes votent"], "tous les citoyens majeurs ont le droit de vote, sans condition de fortune", "Il s'oppose au suffrage censitaire, réservé aux plus riches."),
  Q("Quelle est la formule qui résume le principe de la République, selon l'article 2 de la Constitution ?", ["« Gouvernement du peuple, par le peuple et pour le peuple »", "« L'État, c'est moi »", "« Liberté, ordre, progrès »", "« Un pour tous, tous pour un »"], "« Gouvernement du peuple, par le peuple et pour le peuple »", "Cette formule, empruntée à Abraham Lincoln, figure à l'article 2 de la Constitution."),
]),
notion('E3-3', 0, F, 'emc-europe-citoyennete', [
  Q("Tous les citoyens d'un pays de l'Union européenne sont aussi…", ["citoyens européens", "citoyens américains", "sans droits en Europe", "fonctionnaires européens"], "citoyens européens", "La citoyenneté européenne (traité de Maastricht, 1992) s'ajoute à la citoyenneté nationale."),
  Q("Quel droit donne la citoyenneté européenne ?", ["Voter aux élections municipales et européennes dans le pays de résidence", "Voter à l'élection présidentielle de tous les pays", "Ne pas payer d'impôts", "Être fonctionnaire partout"], "Voter aux élections municipales et européennes dans le pays de résidence", "Un citoyen européen peut aussi circuler et s'installer librement dans l'Union."),
  N("Tous les combien d'années les députés européens sont-ils élus ?", 5, "Les députés européens sont élus pour 5 ans au suffrage universel direct ; la dernière élection a eu lieu en 2024."),
]),
notion('E4-1', 0, F, 'emc-loi-decret', [
  Q("Qui vote la loi en France ?", ["Le président", "Le Parlement", "Le Conseil d'État", "Le Premier ministre seul"], "Le Parlement", "La loi est votée par le Parlement ; le Gouvernement peut proposer des projets de loi."),
  Q("Comment appelle-t-on un texte de loi proposé par le Gouvernement ?", ["Une proposition de loi", "Un projet de loi", "Un décret", "Une ordonnance de juge"], "Un projet de loi", "Un projet de loi vient du Gouvernement ; une proposition de loi vient d'un parlementaire."),
  Q("Qui promulgue la loi, c'est-à-dire la rend applicable ?", ["Le président de la République", "Le président de l'Assemblée", "Le Conseil constitutionnel", "Le maire"], "Le président de la République", "Le président promulgue la loi dans les 15 jours suivant son adoption (article 10)."),
]),
notion('E5-2', 0, F, 'emc-handicap-inclusion', [
  N("En quelle année est votée la loi pour l'égalité des droits et des chances des personnes handicapées ?", 2005, "La loi du 11 février 2005 affirme le droit à la scolarisation et à l'accessibilité des personnes handicapées."),
  Q("Qui accompagne en classe des élèves en situation de handicap ?", ["Les AESH (accompagnants d'élèves en situation de handicap)", "Les inspecteurs", "Les délégués de classe", "Les gendarmes"], "Les AESH (accompagnants d'élèves en situation de handicap)", "Les AESH favorisent l'autonomie et la scolarisation des élèves en situation de handicap."),
  Q("Qu'est-ce que l'école inclusive ?", ["Une école réservée aux élèves en situation de handicap", "Une école qui accueille tous les élèves en adaptant l'enseignement à leurs besoins", "Une école privée", "Une école sans programme"], "Une école qui accueille tous les élèves en adaptant l'enseignement à leurs besoins", "L'école inclusive scolarise chaque élève, avec des aménagements si nécessaire."),
]),
notion('E4-2', 1, F, 'emc-terrorisme-memoire', [
  Q("Quel journal satirique est visé par un attentat terroriste en janvier 2015 ?", ["Le Monde", "Charlie Hebdo", "Le Figaro", "Libération"], "Charlie Hebdo", "L'attentat du 7 janvier 2015 tue 12 personnes, dont plusieurs dessinateurs."),
  Q("Quel professeur d'histoire-géographie est assassiné en octobre 2020 pour avoir enseigné la liberté d'expression ?", ["Samuel Paty", "Dominique Bernard", "Jean Zay", "Lucien Herr"], "Samuel Paty", "Samuel Paty est assassiné le 16 octobre 2020 à Conflans-Sainte-Honorine."),
  Q("Quel professeur de lettres est tué en octobre 2023 dans son lycée à Arras ?", ["Samuel Paty", "Dominique Bernard", "Jean Moulin", "Jules Ferry"], "Dominique Bernard", "Dominique Bernard est tué le 13 octobre 2023 au lycée Gambetta d'Arras."),
]),
notion('E3-2', 0, F, 'emc-sondages-reseaux', [
  Q("Qu'est-ce qu'un sondage d'opinion ?", ["Un vote officiel", "Une enquête auprès d'un échantillon représentatif pour mesurer l'opinion", "Une loi", "Un débat télévisé"], "Une enquête auprès d'un échantillon représentatif pour mesurer l'opinion", "Un sondage donne une estimation, avec une marge d'erreur."),
  Q("Quelle autorité régule les médias audiovisuels et numériques en France ?", ["L'Arcom", "La CNIL", "L'Insee", "L'AMF"], "L'Arcom", "L'Arcom (ex-CSA) veille notamment au pluralisme et à la protection des publics."),
  Q("Quelle autorité protège les données personnelles en France ?", ["La CNIL", "L'Arcom", "La Cour des comptes", "Le Défenseur des droits"], "La CNIL", "La Commission nationale de l'informatique et des libertés veille au respect de la vie privée et du RGPD."),
]),
notion('E5-1', 1, F, 'emc-racisme-antisemitisme', [
  Q("Qu'est-ce que le racisme ?", ["Une opinion autorisée", "L'idée fausse d'une hiérarchie entre groupes humains et l'hostilité qui en découle", "Une science", "Une religion"], "L'idée fausse d'une hiérarchie entre groupes humains et l'hostilité qui en découle", "Le racisme est un délit lorsqu'il s'exprime par des injures, des discriminations ou des violences."),
  Q("Qu'est-ce que l'antisémitisme ?", ["L'hostilité envers les Juifs", "Une religion", "Un courant artistique", "Une forme de laïcité"], "L'hostilité envers les Juifs", "L'antisémitisme a conduit au pire avec la Shoah ; il est puni par la loi."),
  Q("Quelle loi de 1990 réprime la négation des crimes contre l'humanité ?", ["La loi Gayssot", "La loi Veil", "La loi Falloux", "La loi Neuwirth"], "La loi Gayssot", "La loi Gayssot (13 juillet 1990) punit notamment la contestation de la Shoah."),
]),
notion('E3-1', 0, F, 'emc-elections-locales', [
  Q("Quelle élection permet de désigner les conseillers municipaux ?", ["Les élections législatives", "Les élections municipales", "Les élections européennes", "L'élection présidentielle"], "Les élections municipales", "Les élections municipales ont lieu tous les 6 ans ; les dernières se sont tenues en mars 2026."),
  Q("Quelle élection permet d'élire les députés ?", ["Les élections municipales", "Les élections législatives", "Les élections sénatoriales", "Les élections régionales"], "Les élections législatives", "Les législatives désignent les 577 députés de l'Assemblée nationale."),
  N("Pour combien d'années les conseillers municipaux sont-ils élus ?", 6, "Le mandat municipal dure 6 ans."),
]),
notion('E3-3', 1, F, 'emc-benevolat', [
  Q("Qu'est-ce que le bénévolat ?", ["Un travail rémunéré", "Un engagement librement choisi et non rémunéré au service des autres", "Une obligation légale", "Un emploi public"], "Un engagement librement choisi et non rémunéré au service des autres", "Des millions de Français sont bénévoles dans des associations."),
  Q("Quel est le principal moyen pour un citoyen de participer au choix de ses représentants ?", ["Le vote", "La grève", "La pétition seulement", "La manifestation seulement"], "Le vote", "Le vote est l'acte fondamental de la citoyenneté démocratique."),
  Q("Qu'est-ce qu'une pétition ?", ["Une loi", "Un texte signé par des citoyens pour soutenir une demande auprès d'une autorité", "Une élection", "Un jugement"], "Un texte signé par des citoyens pour soutenir une demande auprès d'une autorité", "Une pétition citoyenne peut être déposée auprès des assemblées, notamment en ligne."),
]),
notion('E4-2', 0, F, 'emc-defense-alliances', [
  Q("De quelle alliance militaire la France est-elle membre ?", ["Le pacte de Varsovie", "L'OTAN", "L'ASEAN", "Le Mercosur"], "L'OTAN", "La France est membre fondateur de l'OTAN (1949) ; elle a réintégré son commandement intégré en 2009."),
  Q("Comment appelle-t-on les soldats de l'ONU chargés de missions de maintien de la paix ?", ["Les légionnaires", "Les casques bleus", "Les marines", "Les gardes républicains"], "Les casques bleus", "Les casques bleus sont fournis par les États membres, dont la France, pour des opérations de maintien de la paix."),
  Q("Sur quoi repose la stratégie de dissuasion de la France ?", ["Sur l'arme nucléaire", "Sur la neutralité", "Sur l'absence d'armée", "Sur le service militaire obligatoire"], "Sur l'arme nucléaire", "La dissuasion nucléaire vise à décourager toute agression contre les intérêts vitaux de la France."),
]),
notion('E5-2', 1, F, 'emc-protection-sociale', [
  Q("Quel organisme verse les allocations familiales ?", ["La CAF (Caisse d'allocations familiales)", "La mairie", "Pôle emploi uniquement", "La Banque de France"], "La CAF (Caisse d'allocations familiales)", "La CAF verse les prestations familiales et certaines aides au logement."),
  Q("Quel dispositif assure un revenu minimum aux personnes sans ressources ?", ["Le RSA (revenu de solidarité active)", "Le SMIC", "Le PEL", "La TVA"], "Le RSA (revenu de solidarité active)", "Le RSA, versé par les départements, garantit un revenu minimum aux personnes aux ressources faibles ou nulles."),
  Q("Le système de retraite français est principalement fondé sur…", ["la capitalisation individuelle", "la répartition : les cotisations des actifs financent les pensions des retraités", "les dons", "l'épargne obligatoire en banque"], "la répartition : les cotisations des actifs financent les pensions des retraités", "La retraite par répartition repose sur la solidarité entre générations."),
]),
notion('E3-2', 1, F, 'emc-education-medias', [
  Q("Quel organisme public est chargé de l'éducation aux médias et à l'information à l'école ?", ["Le CLEMI", "L'Insee", "La CNIL", "L'Arcom"], "Le CLEMI", "Le CLEMI organise notamment chaque année la Semaine de la presse et des médias dans l'École."),
  Q("Comment appelle-t-on le travail des journalistes qui vérifient les déclarations et les informations qui circulent ?", ["Le fact-checking (vérification des faits)", "La publicité", "Le community management", "La censure"], "Le fact-checking (vérification des faits)", "Des rubriques de vérification des faits existent dans de nombreux médias."),
  Q("Peut-on publier la photo d'une personne sans son accord ?", ["Oui, toujours", "Non, en principe : chacun a droit à son image", "Oui, si elle est sur Internet", "Oui, si la photo est floue"], "Non, en principe : chacun a droit à son image", "Le droit à l'image protège la vie privée ; publier la photo d'autrui suppose en principe son autorisation."),
]),
]

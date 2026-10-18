# EMC · Respecter autrui et Acquérir et partager les valeurs de la République : au moins 20 questions par niveau et par section
from qlib import Q, N, C, notion
F, I, D = 'facile', 'intermediaire', 'difficile'
NOTIONS = [
# ══ RA-1 · Construire le respect de soi ══
notion('RA-1', 0, F, 'emc-politesse', [
  Q("Quelle attitude montre le respect envers un camarade ?", ["L'écouter sans l'interrompre ni se moquer", "Lui couper la parole", "Rire de ses erreurs", "L'ignorer"], "L'écouter sans l'interrompre ni se moquer", "L'écoute est une marque de respect."),
  Q("Dire « bonjour », « merci » et « s'il te plaît », c'est…", ["faire preuve de politesse", "une obligation inscrite dans la Constitution", "inutile", "réservé aux adultes"], "faire preuve de politesse", "La politesse facilite la vie en commun."),
  Q("Respecter le matériel commun de la classe, c'est…", ["respecter le travail des autres et le bien collectif", "une perte de temps", "l'affaire du concierge seulement", "facultatif"], "respecter le travail des autres et le bien collectif", "Le respect concerne aussi les biens partagés."),
]),
notion('RA-1', 1, F, 'emc-dire-non', [
  Q("Un camarade te propose de fumer pour « faire comme les grands ». Que peux-tu faire ?", ["Refuser et expliquer que tu n'en as pas envie", "Accepter pour ne pas paraître différent", "Accepter puis le dénoncer", "Te taire et suivre"], "Refuser et expliquer que tu n'en as pas envie", "Savoir dire non, c'est se respecter."),
  Q("Pourquoi est-il parfois difficile de dire non dans un groupe ?", ["Par peur d'être rejeté ou moqué", "Parce que c'est interdit", "Parce que le groupe a toujours raison", "Parce que la loi l'impose"], "Par peur d'être rejeté ou moqué", "C'est la pression du groupe."),
  Q("À qui un élève peut-il parler s'il se sent poussé à se mettre en danger ?", ["À un adulte de confiance : parent, professeur, CPE, infirmière", "À personne", "Seulement à un inconnu sur Internet", "Uniquement au groupe qui le pousse"], "À un adulte de confiance : parent, professeur, CPE, infirmière", "Demander de l'aide est une bonne décision."),
]),
notion('RA-1', 1, F, 'emc-mise-en-danger', [
  Q("Qu'est-ce qu'un « défi » dangereux diffusé sur les réseaux sociaux ?", ["Un jeu qui pousse à prendre des risques pour sa santé", "Un concours scolaire", "Un exercice de sécurité", "Un jeu de société"], "Un jeu qui pousse à prendre des risques pour sa santé", "Certains ont causé des blessures graves ou des décès."),
  Q("Pourquoi faut-il porter un casque à vélo ?", ["Pour protéger sa tête en cas de chute", "Pour être à la mode", "Parce que c'est joli", "Pour aller plus vite"], "Pour protéger sa tête en cas de chute", "Il est obligatoire pour les moins de 12 ans."),
  Q("Le jeu du foulard (étouffement volontaire) est…", ["très dangereux et peut être mortel", "un jeu sans risque", "un sport olympique", "recommandé par les médecins"], "très dangereux et peut être mortel", "Il faut en parler à un adulte si on en entend parler."),
]),
notion('RA-1', 2, F, 'emc-etat-civil', [
  Q("Dans quel délai faut-il déclarer la naissance d'un enfant à la mairie ?", ["Dans les 5 jours", "Dans l'année", "Dans les 10 ans", "Ce n'est pas obligatoire"], "Dans les 5 jours", "L'acte de naissance établit l'identité légale."),
  Q("Quel document prouve officiellement l'identité d'une personne ?", ["La carte nationale d'identité ou le passeport", "La carte de cantine", "Le carnet de correspondance", "Un abonnement de bus"], "La carte nationale d'identité ou le passeport", "Ce sont des documents délivrés par l'État."),
  Q("Quels éléments forment l'identité légale d'une personne ?", ["Nom, prénom, date et lieu de naissance, nationalité", "Ses goûts et ses loisirs", "Son pseudo sur Internet", "Sa couleur préférée"], "Nom, prénom, date et lieu de naissance, nationalité", "Ils figurent dans l'état civil."),
]),
notion('RA-1', 2, F, 'emc-mot-de-passe', [
  Q("Que faut-il faire de son mot de passe ?", ["Le garder secret", "Le partager avec tous ses amis", "L'écrire sur son cahier de classe", "Le publier sur les réseaux"], "Le garder secret", "Il protège ton identité numérique."),
  Q("Qu'est-ce qu'un bon mot de passe ?", ["Un mot long, mélangeant lettres, chiffres et symboles", "Sa date de naissance", "« 123456 »", "Son prénom"], "Un mot long, mélangeant lettres, chiffres et symboles", "Il doit être difficile à deviner."),
  Q("Avant de publier une photo d'un camarade, il faut…", ["lui demander son accord", "la publier rapidement", "la modifier pour le faire rire", "demander à un inconnu"], "lui demander son accord", "Chacun a droit à son image."),
]),
notion('RA-1', 0, I, 'emc-estime-de-soi', [
  Q("Qu'appelle-t-on l'estime de soi ?", ["La valeur que l'on s'accorde à soi-même", "L'opinion des autres sur nous", "Une note scolaire", "Un droit constitutionnel"], "La valeur que l'on s'accorde à soi-même", "Elle aide à résister aux pressions."),
  Q("Quel lien existe entre respect de soi et respect d'autrui ?", ["Se respecter aide à respecter les autres, et réciproquement", "Aucun lien", "On ne peut respecter que soi", "Respecter les autres empêche de se respecter"], "Se respecter aide à respecter les autres, et réciproquement", "Les deux vont ensemble."),
  Q("Quel comportement porte atteinte à la dignité d'une personne ?", ["L'humilier publiquement", "La féliciter", "Lui demander son avis", "L'aider"], "L'humilier publiquement", "La dignité est le fondement du respect."),
]),
notion('RA-1', 2, I, 'emc-majorite-numerique', [
  Q("À partir de quel âge un mineur peut-il consentir seul au traitement de ses données par un réseau social en France ?", ["15 ans", "10 ans", "18 ans", "13 ans"], "15 ans", "En dessous, l'accord d'un parent est nécessaire."),
  Q("Quel organisme français protège les données personnelles ?", ["La CNIL", "L'Arcom", "Le CSA", "La SNCF"], "La CNIL", "Commission nationale de l'informatique et des libertés."),
  Q("Quel règlement européen de 2018 protège les données personnelles ?", ["Le RGPD", "Le traité de Rome", "La Charte de la laïcité", "Le code de la route"], "Le RGPD", "Règlement général sur la protection des données."),
]),
notion('RA-1', 2, I, 'emc-droit-oubli', [
  Q("Que permet le « droit à l'oubli » sur Internet ?", ["Demander l'effacement de certaines données personnelles", "Effacer ses notes scolaires", "Oublier ses mots de passe", "Supprimer les lois"], "Demander l'effacement de certaines données personnelles", "Il est prévu par le RGPD."),
  Q("Pourquoi faut-il réfléchir avant de publier en ligne ?", ["Ce qui est publié peut rester visible longtemps et être copié", "Tout disparaît au bout d'une heure", "Personne ne lit Internet", "C'est interdit de publier"], "Ce qui est publié peut rester visible longtemps et être copié", "On parle d'empreinte numérique."),
  Q("Comment appelle-t-on l'ensemble des traces qu'on laisse sur Internet ?", ["L'empreinte (ou identité) numérique", "Le casier judiciaire", "L'état civil", "Le livret de famille"], "L'empreinte (ou identité) numérique", "Elle peut être consultée par d'autres."),
]),
notion('RA-1', 3, I, 'emc-responsabilite-civile', [
  Q("Un élève casse volontairement la vitre d'un voisin. Qui doit payer les réparations s'il est mineur ?", ["Ses parents, civilement responsables", "Personne", "L'école", "L'État"], "Ses parents, civilement responsables", "Les parents répondent des dommages causés par leur enfant mineur."),
  Q("Quelle différence existe entre responsabilité civile et pénale ?", ["La civile oblige à réparer un dommage, la pénale sanctionne une infraction", "Elles sont identiques", "La civile concerne les militaires", "La pénale concerne les contrats"], "La civile oblige à réparer un dommage, la pénale sanctionne une infraction", "Une même action peut engager les deux."),
  Q("Pourquoi souscrit-on une assurance « responsabilité civile » ?", ["Pour couvrir les dommages causés involontairement à autrui", "Pour éviter la prison", "Pour avoir de bonnes notes", "Pour voter"], "Pour couvrir les dommages causés involontairement à autrui", "Elle est souvent demandée pour les sorties scolaires."),
]),
notion('RA-1', 1, I, 'emc-ecrans-sante', [
  Q("Quel trouble l'usage excessif des écrans le soir peut-il provoquer ?", ["Des troubles du sommeil", "Une meilleure vue", "Plus de concentration", "Aucun effet"], "Des troubles du sommeil", "La lumière bleue retarde l'endormissement."),
  Q("Qu'est-ce que la « nomophobie » ?", ["La peur d'être séparé de son téléphone", "La peur des chiens", "La peur de l'eau", "La peur de l'école"], "La peur d'être séparé de son téléphone", "C'est un signe de dépendance."),
  Q("Depuis 2018, l'usage du téléphone portable au collège est…", ["interdit, sauf usage pédagogique ou exceptions prévues", "obligatoire", "autorisé en classe", "réservé aux professeurs uniquement en récréation"], "interdit, sauf usage pédagogique ou exceptions prévues", "La loi du 3 août 2018 l'encadre."),
]),
notion('RA-1', 3, D, 'emc-majorite-penale', [
  Q("À partir de quel âge un mineur est-il présumé capable de discernement devant la justice pénale ?", ["13 ans", "7 ans", "16 ans", "18 ans"], "13 ans", "C'est une présomption simple du Code de la justice pénale des mineurs (2021)."),
  Q("Quel code régit la justice des mineurs depuis 2021 ?", ["Le Code de la justice pénale des mineurs", "L'ordonnance de 1945 toujours en vigueur", "Le Code civil", "Le Code de la route"], "Le Code de la justice pénale des mineurs", "Il remplace l'ordonnance du 2 février 1945."),
  Q("Quel principe guide la justice des mineurs ?", ["La primauté de l'éducatif sur le répressif", "La sévérité maximale", "L'absence de sanction", "Les mêmes peines que les adultes"], "La primauté de l'éducatif sur le répressif", "Les peines sont atténuées pour les mineurs."),
]),
notion('RA-1', 3, D, 'emc-cyberharcelement-penal', [
  Q("Quelle peine maximale encourt l'auteur majeur d'un cyberharcèlement ayant causé une incapacité de plus de 8 jours ?", ["3 ans de prison et 45 000 € d'amende", "Une simple remarque", "1 € d'amende", "La perpétuité"], "3 ans de prison et 45 000 € d'amende", "Le harcèlement en ligne est une circonstance aggravante."),
  Q("Le fait de partager une vidéo humiliante d'un camarade peut-il être sanctionné ?", ["Oui, même si on n'est pas l'auteur de la vidéo", "Non, seul l'auteur est responsable", "Non, si on la partage à peu de gens", "Seulement si on est majeur"], "Oui, même si on n'est pas l'auteur de la vidéo", "Le partage participe au harcèlement."),
  Q("Quelle loi de 2022 crée un délit spécifique de harcèlement scolaire ?", ["La loi Balanant", "La loi Veil", "La loi Gayssot", "La loi Pleven"], "La loi Balanant", "Il est puni jusqu'à 10 ans de prison en cas de suicide de la victime."),
]),
notion('RA-1', 2, D, 'emc-usurpation-identite', [
  Q("Créer un faux compte au nom d'un camarade pour se moquer de lui, c'est…", ["une usurpation d'identité, punie par la loi", "une simple blague", "autorisé avant 18 ans", "un droit d'expression"], "une usurpation d'identité, punie par la loi", "Elle est punie d'un an de prison et de 15 000 € d'amende."),
  Q("Quel texte protège le droit à l'image et à la vie privée ?", ["L'article 9 du Code civil", "L'article 49-3 de la Constitution", "La loi de 1905", "Le traité de Maastricht"], "L'article 9 du Code civil", "« Chacun a droit au respect de sa vie privée »."),
  Q("Quelle plateforme publique permet de signaler un contenu illicite en ligne ?", ["Pharos", "Parcoursup", "Pronote", "Doctolib"], "Pharos", "Elle est gérée par la police et la gendarmerie."),
]),
notion('RA-1', 1, D, 'emc-prevention-risques', [
  Q("Quel numéro gratuit et anonyme aide les jeunes face aux drogues, à l'alcool ou aux écrans ?", ["Drogues info service (0 800 23 13 13)", "Le 17", "Le 112", "Le 3919"], "Drogues info service (0 800 23 13 13)", "Il est joignable 7 jours sur 7."),
  Q("Quel parcours éducatif aborde à l'école la prévention des conduites à risque ?", ["Le parcours éducatif de santé", "Le parcours Avenir", "Le parcours d'éducation artistique", "Le parcours citoyen seulement"], "Le parcours éducatif de santé", "Il existe de la maternelle au lycée."),
  Q("Pourquoi les adolescents sont-ils particulièrement exposés aux conduites à risque ?", ["Recherche de sensations, besoin d'appartenance et cerveau encore en maturation", "Ils sont moins intelligents", "La loi les y pousse", "Ils n'ont aucune règle"], "Recherche de sensations, besoin d'appartenance et cerveau encore en maturation", "Le cortex préfrontal mûrit jusqu'à environ 25 ans."),
]),
notion('RA-1', 0, D, 'emc-respect-philosophie', [
  Q("Quel philosophe affirme qu'il faut traiter l'humanité « toujours en même temps comme une fin, et jamais simplement comme un moyen » ?", ["Kant", "Rousseau", "Voltaire", "Montesquieu"], "Kant", "C'est le fondement de la dignité humaine."),
  Q("Quelle différence y a-t-il entre la tolérance et le respect ?", ["Tolérer, c'est supporter ; respecter, c'est reconnaître la valeur de l'autre", "Aucune différence", "Le respect est interdit par la loi", "La tolérance exige d'être d'accord"], "Tolérer, c'est supporter ; respecter, c'est reconnaître la valeur de l'autre", "Le respect va plus loin que la tolérance."),
  Q("Le respect d'autrui oblige-t-il à accepter tous ses comportements ?", ["Non, on peut refuser des actes contraires à la loi ou à la dignité", "Oui, toujours", "Oui, s'il est majeur", "Oui, s'il est plus âgé"], "Non, on peut refuser des actes contraires à la loi ou à la dignité", "Respecter une personne n'est pas tout accepter."),
]),
notion('RA-1', 2, D, 'emc-identite-genre-nom', [
  Q("Depuis 2022, un majeur peut-il changer de nom de famille par simple déclaration en mairie, une fois dans sa vie ?", ["Oui, pour prendre ou ajouter le nom de l'autre parent", "Non, jamais", "Oui, autant de fois qu'il veut", "Seulement avec l'accord du préfet"], "Oui, pour prendre ou ajouter le nom de l'autre parent", "C'est la loi du 2 mars 2022."),
  Q("Qui décide d'un changement de prénom ?", ["L'officier d'état civil de la mairie, sous contrôle du procureur", "Le directeur de l'école", "Le président de la République", "N'importe qui"], "L'officier d'état civil de la mairie, sous contrôle du procureur", "Il faut un intérêt légitime."),
  Q("Quel texte international garantit le droit de l'enfant à une identité ?", ["La Convention internationale des droits de l'enfant", "Le traité de Rome", "Le Code de la route", "La loi de 1905"], "La Convention internationale des droits de l'enfant", "Son article 8 protège l'identité de l'enfant."),
]),
# ══ RA-2 · Respect d'autrui ══
notion('RA-2', 5, I, 'emc-valeurs-tension', [
  Q("La liberté d'expression peut-elle entrer en tension avec le respect d'autrui ?", ["Oui, elle est limitée par l'interdiction de l'injure, de la diffamation et de l'incitation à la haine", "Non, jamais", "Oui, elle est donc supprimée", "Non, car elle est absolue"], "Oui, elle est limitée par l'interdiction de l'injure, de la diffamation et de l'incitation à la haine", "La loi fixe ses limites."),
  Q("Le blasphème est-il un délit en France ?", ["Non", "Oui, depuis 1905", "Oui, puni de prison", "Oui, puni d'une amende"], "Non", "On peut critiquer une religion, pas inciter à la haine contre des personnes."),
  Q("Comment résoudre une tension entre deux valeurs, comme liberté et sécurité ?", ["Par le débat démocratique et la loi, sous le contrôle du juge", "Par la force", "En supprimant l'une des deux", "Par tirage au sort"], "Par le débat démocratique et la loi, sous le contrôle du juge", "Le juge vérifie que la mesure est proportionnée."),
]),
notion('RA-2', 2, I, 'emc-harcelement-reperes', [
  Q("Quels sont les trois critères du harcèlement ?", ["La violence, la répétition et l'isolement de la victime", "Une dispute unique", "Un désaccord entre amis", "Une mauvaise note"], "La violence, la répétition et l'isolement de la victime", "Le harcèlement s'installe dans la durée."),
  Q("Quel numéro gratuit permet de signaler un harcèlement scolaire ?", ["Le 3018", "Le 15", "Le 18", "Le 3646"], "Le 3018", "Il traite aussi le cyberharcèlement."),
  Q("Quel programme de lutte contre le harcèlement est généralisé dans les collèges ?", ["Le programme pHARe", "Le plan Vigipirate", "Le programme Erasmus", "Le SNU"], "Le programme pHARe", "Il forme des élèves ambassadeurs."),
]),
notion('RA-2', 0, I, 'emc-dignite', [
  Q("Quel article de la Déclaration universelle des droits de l'homme affirme l'égale dignité de tous ?", ["L'article 1er", "L'article 49", "L'article 16", "L'article 89"], "L'article 1er", "« Tous les êtres humains naissent libres et égaux en dignité et en droits »."),
  N("En quelle année la Déclaration universelle des droits de l'homme est-elle adoptée ?", 1948, "Elle est adoptée à Paris par l'ONU."),
  Q("Quelle pratique porte atteinte à la dignité humaine et est interdite en toutes circonstances ?", ["La torture", "Le débat", "La grève", "Le vote"], "La torture", "Aucune exception n'est admise."),
]),
notion('RA-2', 1, D, 'emc-lois-memorielles-haine', [
  Q("Quelle loi de 1972 punit la provocation à la haine raciale ?", ["La loi Pleven", "La loi Gayssot", "La loi Veil", "La loi Taubira"], "La loi Pleven", "Elle complète la loi de 1881 sur la presse."),
  Q("Quelle loi de 1990 punit la négation des crimes contre l'humanité ?", ["La loi Gayssot", "La loi Pleven", "La loi Neuwirth", "La loi Badinter"], "La loi Gayssot", "Elle vise notamment le négationnisme de la Shoah."),
  Q("Quelle loi de 2001 reconnaît la traite et l'esclavage comme crimes contre l'humanité ?", ["La loi Taubira", "La loi Gayssot", "La loi Pleven", "La loi Schœlcher"], "La loi Taubira", "Le 10 mai est la journée de mémoire."),
]),
notion('RA-2', 1, D, 'emc-criteres-discrimination', [
  Q("Combien de critères de discrimination la loi française reconnaît-elle environ ?", ["Plus de 25", "3", "10", "100"], "Plus de 25", "Origine, sexe, âge, handicap, orientation sexuelle, lieu de résidence…"),
  Q("Refuser un logement à quelqu'un à cause de son nom est…", ["une discrimination punie par la loi", "un droit du propriétaire", "autorisé si le propriétaire est âgé", "une simple préférence"], "une discrimination punie par la loi", "Elle est punie de 3 ans de prison et 45 000 € d'amende."),
  Q("Qu'est-ce qu'un « testing » ?", ["Une méthode pour prouver une discrimination en comparant deux candidats identiques sauf un critère", "Un examen scolaire", "Un test médical", "Un sondage d'opinion"], "Une méthode pour prouver une discrimination en comparant deux candidats identiques sauf un critère", "Il est admis comme preuve par la justice."),
]),
notion('RA-2', 3, D, 'emc-integrite-corps', [
  Q("Quel principe interdit de vendre son corps ou ses organes en France ?", ["La non-patrimonialité du corps humain", "La liberté du commerce", "La laïcité", "La séparation des pouvoirs"], "La non-patrimonialité du corps humain", "Le don d'organes est gratuit et anonyme."),
  N("En quelle année la loi interdit-elle les « violences éducatives ordinaires » (fessées, gifles) ?", 2019, "« L'autorité parentale s'exerce sans violences physiques ou psychologiques »."),
  Q("Quelle pratique est interdite comme atteinte à l'intégrité des filles et punie en France ?", ["L'excision", "La vaccination", "Le sport", "La scolarisation"], "L'excision", "Elle est poursuivie même si commise à l'étranger sur une mineure résidant en France."),
]),
notion('RA-2', 4, D, 'emc-laicite-espace-public', [
  Q("Un usager d'un service public (à la mairie, à l'hôpital) peut-il porter un signe religieux ?", ["Oui, la neutralité s'impose aux agents, pas aux usagers", "Non, jamais", "Seulement le dimanche", "Seulement s'il est majeur"], "Oui, la neutralité s'impose aux agents, pas aux usagers", "Sous réserve de l'ordre public."),
  Q("Quelle loi de 2010 interdit la dissimulation du visage dans l'espace public ?", ["La loi du 11 octobre 2010", "La loi de 1905", "La loi de 2004", "La loi Ferry"], "La loi du 11 octobre 2010", "Elle repose sur la sécurité et les exigences de la vie en société."),
  Q("Quelle fête religieuse est un jour férié en France pour des raisons historiques ?", ["Noël", "L'Aïd el-Kébir", "Yom Kippour", "Le Nouvel An chinois"], "Noël", "Les jours fériés chrétiens sont un héritage historique."),
]),
notion('RA-2', 5, D, 'emc-arbitrage-juge', [
  Q("Quelle institution tranche les conflits entre liberté religieuse et ordre public dans les services publics ?", ["Le Conseil d'État et les tribunaux administratifs", "Le Sénat", "L'Église", "Le Président seul"], "Le Conseil d'État et les tribunaux administratifs", "Il a jugé en 2016 que les arrêtés « anti-burkini » étaient illégaux."),
  Q("Qu'appelle-t-on le contrôle de proportionnalité ?", ["Vérifier qu'une restriction de liberté est nécessaire et adaptée au but recherché", "Compter les voix", "Calculer un impôt", "Mesurer un terrain"], "Vérifier qu'une restriction de liberté est nécessaire et adaptée au but recherché", "C'est un outil central des juges."),
  Q("Quel droit peut entrer en tension avec la liberté de manifester ?", ["La sécurité et la liberté de circuler", "Le droit de vote", "Le droit à l'éducation", "La liberté religieuse"], "La sécurité et la liberté de circuler", "Une manifestation peut être interdite en cas de trouble grave."),
]),
# ══ RA-3 · La morale et l'éthique ══
notion('RA-3', 0, F, 'emc-alerter', [
  Q("Tu vois un camarade se faire frapper dans la cour. Que fais-tu ?", ["Je préviens immédiatement un adulte", "Je filme la scène", "Je m'éloigne sans rien dire", "J'encourage la bagarre"], "Je préviens immédiatement un adulte", "Alerter, ce n'est pas dénoncer : c'est protéger."),
  Q("Quelle différence y a-t-il entre alerter et « balancer » ?", ["Alerter protège une victime, ce n'est pas trahir", "Il n'y en a aucune", "Alerter est interdit", "Balancer est obligatoire"], "Alerter protège une victime, ce n'est pas trahir", "Le silence protège le harceleur."),
  Q("Qui sont les témoins d'une situation de harcèlement ?", ["Les personnes qui voient ou savent sans être victimes ni auteurs", "Les juges", "Les policiers seulement", "Les parents de la victime"], "Les personnes qui voient ou savent sans être victimes ni auteurs", "Leur réaction peut tout changer."),
]),
notion('RA-3', 0, F, 'emc-gestes-secours', [
  Q("Quel numéro appeler pour le SAMU ?", ["Le 15", "Le 17", "Le 18", "Le 119"], "Le 15", "Le 18 est celui des pompiers, le 17 celui de la police."),
  Q("Quelle est la première chose à faire face à un accident ?", ["Protéger, puis alerter, puis secourir", "Partir", "Prendre une photo", "Déplacer la victime sans réfléchir"], "Protéger, puis alerter, puis secourir", "Ce sont les trois gestes de base."),
  Q("Quelle formation aux premiers secours les collégiens peuvent-ils suivre ?", ["PSC1 (Prévention et secours civiques)", "Le permis B", "Le BAFA", "Le brevet de pilote"], "PSC1 (Prévention et secours civiques)", "L'école sensibilise aux gestes qui sauvent."),
]),
notion('RA-3', 1, F, 'emc-juge-impartial', [
  Q("Quelle qualité doit avoir un juge ?", ["L'impartialité", "La partialité", "La rapidité avant tout", "L'amitié avec l'accusé"], "L'impartialité", "Il ne doit favoriser aucune partie."),
  Q("Sur quoi un juge fonde-t-il sa décision ?", ["Sur la loi et les preuves", "Sur son humeur", "Sur les réseaux sociaux", "Sur l'avis de ses amis"], "Sur la loi et les preuves", "Il doit motiver ses jugements."),
  Q("Quel symbole représente la justice ?", ["Une balance", "Une épée seule", "Un coq", "Une étoile"], "Une balance", "Elle évoque l'équilibre et l'équité."),
]),
notion('RA-3', 1, F, 'emc-medecin-secret', [
  Q("Quel serment prêtent les médecins ?", ["Le serment d'Hippocrate", "Le serment du Jeu de paume", "Le serment de Strasbourg", "Le serment olympique"], "Le serment d'Hippocrate", "Il engage à soigner sans discrimination."),
  Q("Qu'est-ce que le secret médical ?", ["L'obligation pour le médecin de ne pas révéler ce qu'il sait de son patient", "Un médicament secret", "Une maladie rare", "Un code d'accès à l'hôpital"], "L'obligation pour le médecin de ne pas révéler ce qu'il sait de son patient", "Il protège la confiance entre patient et médecin."),
  Q("Un médecin doit-il soigner toute personne, quelles que soient ses origines ou opinions ?", ["Oui", "Non, il choisit ses patients selon leurs opinions", "Seulement les Français", "Seulement les adultes"], "Oui", "C'est un principe déontologique fondamental."),
]),
notion('RA-3', 2, F, 'emc-empathie', [
  Q("Qu'est-ce que l'empathie ?", ["La capacité à se mettre à la place de l'autre et à comprendre ses émotions", "La colère", "L'indifférence", "La jalousie"], "La capacité à se mettre à la place de l'autre et à comprendre ses émotions", "Elle aide à prévenir les violences."),
  Q("Quel sentiment moral ressent-on quand on a mal agi ?", ["La culpabilité ou le remords", "La fierté", "L'indifférence", "La joie"], "La culpabilité ou le remords", "Elle peut pousser à réparer."),
  Q("Qu'appelle-t-on l'indignation ?", ["Une colère face à une injustice", "La joie d'une victoire", "La peur de l'orage", "L'ennui"], "Une colère face à une injustice", "Elle peut conduire à l'engagement."),
]),
notion('RA-3', 0, I, 'emc-effet-spectateur', [
  Q("Qu'est-ce que « l'effet spectateur » ?", ["Plus il y a de témoins, moins chacun se sent obligé d'intervenir", "Le plaisir de regarder un film", "Un effet spécial au cinéma", "L'obligation de filmer"], "Plus il y a de témoins, moins chacun se sent obligé d'intervenir", "Chacun attend que l'autre agisse."),
  Q("Comment un témoin peut-il aider sans se mettre en danger ?", ["Alerter un adulte, soutenir la victime, ne pas relayer", "Frapper l'agresseur", "Rire avec les autres", "Partager la vidéo"], "Alerter un adulte, soutenir la victime, ne pas relayer", "Il n'est jamais demandé de prendre des risques."),
  Q("Pourquoi rire d'une moquerie fait-il de toi un acteur du harcèlement ?", ["Parce que cela encourage l'agresseur et isole la victime", "Ce n'est pas le cas", "Parce que le rire est interdit", "Parce que la loi l'exige"], "Parce que cela encourage l'agresseur et isole la victime", "Le public renforce le harceleur."),
]),
notion('RA-3', 1, I, 'emc-consentement-medical', [
  Q("Un médecin peut-il soigner un patient adulte conscient sans son accord ?", ["Non, il faut son consentement libre et éclairé", "Oui, toujours", "Oui, si la famille le demande", "Oui, s'il est pressé"], "Non, il faut son consentement libre et éclairé", "C'est la loi Kouchner de 2002."),
  Q("Quelle loi de 2016 renforce les droits des patients en fin de vie ?", ["La loi Claeys-Leonetti", "La loi Veil", "La loi Evin", "La loi Ferry"], "La loi Claeys-Leonetti", "Elle permet la sédation profonde et continue."),
  Q("Que sont les « directives anticipées » ?", ["Des volontés écrites sur sa fin de vie, si l'on ne peut plus s'exprimer", "Des ordres militaires", "Un règlement intérieur", "Un testament financier"], "Des volontés écrites sur sa fin de vie, si l'on ne peut plus s'exprimer", "Le médecin doit en tenir compte."),
]),
notion('RA-3', 1, I, 'emc-jury-assises', [
  Q("Qui peut être juré dans une cour d'assises ?", ["Des citoyens tirés au sort sur les listes électorales", "Uniquement des juges", "Des policiers", "Des avocats"], "Des citoyens tirés au sort sur les listes électorales", "Ils participent au jugement des crimes."),
  Q("Quelle formule rappelle que le doute profite à l'accusé ?", ["« In dubio pro reo »", "« Dura lex, sed lex »", "« Veni, vidi, vici »", "« Carpe diem »"], "« In dubio pro reo »", "Le doute doit bénéficier à l'accusé."),
  Q("Sur quoi les jurés fondent-ils leur décision ?", ["Leur « intime conviction » après examen des preuves", "Les rumeurs", "Les réseaux sociaux", "L'avis de la presse"], "Leur « intime conviction » après examen des preuves", "Ils prêtent serment d'impartialité."),
]),
notion('RA-3', 2, I, 'emc-deontologie-metiers', [
  Q("Quel principe déontologique s'impose aux journalistes ?", ["Vérifier ses informations et protéger ses sources", "Publier les rumeurs", "Inventer des citations", "Révéler toutes ses sources"], "Vérifier ses informations et protéger ses sources", "La Charte de Munich (1971) les rassemble."),
  Q("Quelle obligation déontologique s'impose aux enseignants ?", ["La neutralité politique et religieuse", "Faire de la publicité", "Donner leur opinion politique en classe", "Noter selon leurs préférences"], "La neutralité politique et religieuse", "Ils sont agents du service public."),
  Q("Qu'est-ce qu'un conflit d'intérêts ?", ["Une situation où un intérêt personnel peut influencer une décision professionnelle", "Une dispute entre élèves", "Une guerre entre pays", "Une grève"], "Une situation où un intérêt personnel peut influencer une décision professionnelle", "Il doit être déclaré et évité."),
]),
notion('RA-3', 2, I, 'emc-morale-loi', [
  Q("Tout ce qui est légal est-il forcément moral ?", ["Non, la loi et la morale ne se confondent pas", "Oui, toujours", "Oui, depuis 1789", "Non, car la loi est toujours immorale"], "Non, la loi et la morale ne se confondent pas", "Mentir à un ami n'est pas puni par la loi, mais c'est moralement discutable."),
  Q("Comment appelle-t-on le refus d'obéir à une loi jugée injuste, de façon publique et non violente ?", ["La désobéissance civile", "La délinquance", "La guerre civile", "Le terrorisme"], "La désobéissance civile", "Gandhi et Martin Luther King l'ont pratiquée."),
  Q("Quelle héroïne grecque désobéit au roi Créon pour enterrer son frère ?", ["Antigone", "Pénélope", "Hélène", "Médée"], "Antigone", "Elle oppose la loi morale à la loi du roi."),
]),
notion('RA-3', 0, I, 'emc-justes', [
  Q("Comment appelle-t-on les personnes qui ont sauvé des Juifs au péril de leur vie pendant la Shoah ?", ["Les Justes parmi les nations", "Les résistants armés seulement", "Les collaborateurs", "Les déportés"], "Les Justes parmi les nations", "Ce titre est décerné par Yad Vashem."),
  Q("Quel village de Haute-Loire a protégé des milliers de réfugiés, dont de nombreux enfants juifs ?", ["Le Chambon-sur-Lignon", "Oradour-sur-Glane", "Vichy", "Drancy"], "Le Chambon-sur-Lignon", "Il a été honoré collectivement comme Juste."),
  Q("Qu'enseigne l'exemple des Justes ?", ["Qu'il est possible de refuser l'injustice même quand elle est imposée", "Qu'il faut toujours obéir", "Qu'il vaut mieux se taire", "Que la loi a toujours raison"], "Qu'il est possible de refuser l'injustice même quand elle est imposée", "Ils illustrent le rôle du témoin qui agit."),
]),
notion('RA-3', 0, D, 'emc-non-denonciation', [
  Q("Que risque une personne qui ne signale pas les mauvais traitements infligés à un mineur dont elle a connaissance ?", ["Jusqu'à 3 ans de prison et 45 000 € d'amende", "Rien du tout", "Une simple remarque", "Une amende de 1 €"], "Jusqu'à 3 ans de prison et 45 000 € d'amende", "C'est le délit de non-dénonciation de mauvais traitements."),
  Q("Quel article du Code de procédure pénale oblige les fonctionnaires à signaler les crimes et délits dont ils ont connaissance ?", ["L'article 40", "L'article 49-3", "L'article 16", "L'article 1er"], "L'article 40", "Les enseignants y sont soumis."),
  Q("Quel document l'école transmet-elle à la cellule départementale quand un enfant est peut-être en danger ?", ["Une information préoccupante", "Un bulletin scolaire", "Un certificat de scolarité", "Une carte d'électeur"], "Une information préoccupante", "La CRIP l'évalue."),
]),
notion('RA-3', 1, D, 'emc-bioethique', [
  Q("Quel comité donne des avis sur les questions de bioéthique en France ?", ["Le Comité consultatif national d'éthique (CCNE)", "Le Conseil constitutionnel", "Le CSA", "La CNIL"], "Le Comité consultatif national d'éthique (CCNE)", "Il est créé en 1983."),
  N("En quelle année la loi de bioéthique ouvre-t-elle la PMA à toutes les femmes ?", 2021, "Elle concerne les couples de femmes et les femmes seules."),
  Q("Quelle pratique reste interdite en France par la loi de bioéthique ?", ["La gestation pour autrui (GPA)", "Le don du sang", "La greffe d'organes", "La vaccination"], "La gestation pour autrui (GPA)", "Au nom de la non-patrimonialité du corps."),
]),
notion('RA-3', 2, D, 'emc-ethique-ia', [
  Q("Quel règlement européen de 2024 encadre l'intelligence artificielle ?", ["L'AI Act (règlement sur l'IA)", "Le RGPD", "Le traité de Lisbonne", "Le DSA seulement"], "L'AI Act (règlement sur l'IA)", "Il classe les usages selon leur niveau de risque."),
  Q("Quel risque éthique les algorithmes peuvent-ils présenter ?", ["Reproduire ou amplifier des discriminations", "Être toujours neutres", "Supprimer toutes les erreurs", "Aucun risque"], "Reproduire ou amplifier des discriminations", "On parle de biais algorithmiques."),
  Q("Qu'est-ce qu'un « deepfake » ?", ["Une vidéo ou image truquée par IA faisant dire ou faire des choses à quelqu'un", "Un jeu vidéo", "Un réseau social", "Un logiciel antivirus"], "Une vidéo ou image truquée par IA faisant dire ou faire des choses à quelqu'un", "Il peut servir à désinformer ou harceler."),
]),
notion('RA-3', 2, D, 'emc-ethique-philosophes', [
  Q("Quelle philosophe a analysé la « banalité du mal » à propos du procès Eichmann ?", ["Hannah Arendt", "Simone de Beauvoir", "Simone Weil", "Élisabeth Badinter"], "Hannah Arendt", "Elle montre que des individus ordinaires peuvent commettre le pire en obéissant."),
  Q("Quelle expérience des années 1960 étudie la soumission à l'autorité ?", ["L'expérience de Milgram", "L'expérience de Pavlov", "L'expérience de Pasteur", "L'expérience de Galilée"], "L'expérience de Milgram", "Beaucoup de participants obéissent jusqu'à infliger de prétendus chocs mortels."),
  Q("Qu'appelle-t-on une éthique de la responsabilité ?", ["Juger une action d'après ses conséquences prévisibles", "Agir sans réfléchir", "Obéir aveuglément", "Ignorer les autres"], "Juger une action d'après ses conséquences prévisibles", "Max Weber l'oppose à l'éthique de conviction."),
]),
# ══ RA-4 · Le rôle de la loi ══
notion('RA-4', 1, F, 'emc-reglement-interieur', [
  Q("Quel document fixe les droits et les devoirs des élèves au collège ?", ["Le règlement intérieur", "La Constitution", "Le Code civil", "Le carnet de santé"], "Le règlement intérieur", "Il est voté par le conseil d'administration."),
  Q("Qui vote le règlement intérieur d'un collège ?", ["Le conseil d'administration", "Le maire", "Le président de la République", "Les parents seuls"], "Le conseil d'administration", "Les élèves y sont représentés par leurs délégués."),
  Q("Une sanction au collège doit être…", ["proportionnée à la faute et expliquée", "collective", "humiliante", "décidée sans entendre l'élève"], "proportionnée à la faute et expliquée", "Les punitions collectives sont interdites."),
]),
notion('RA-4', 0, D, 'emc-ddhc-liberte', [
  Q("Quel article de la DDHC définit la liberté comme « pouvoir faire tout ce qui ne nuit pas à autrui » ?", ["L'article 4", "L'article 1er", "L'article 10", "L'article 17"], "L'article 4", "Ses bornes sont fixées par la loi."),
  Q("Selon l'article 5 de la DDHC, que peut-on faire de ce qui n'est pas défendu par la loi ?", ["Le faire librement : nul ne peut être empêché", "Rien sans autorisation", "Seulement avec l'accord du roi", "Le faire en payant une taxe"], "Le faire librement : nul ne peut être empêché", "La liberté est le principe, l'interdiction l'exception."),
  Q("Selon la DDHC, la loi est « l'expression de la volonté générale ». De quel article s'agit-il ?", ["L'article 6", "L'article 2", "L'article 12", "L'article 16"], "L'article 6", "Tous les citoyens peuvent concourir à sa formation."),
]),
notion('RA-4', 3, D, 'emc-propriete', [
  Q("Comment la DDHC qualifie-t-elle le droit de propriété dans son article 17 ?", ["« Inviolable et sacré »", "Facultatif", "Réservé aux nobles", "Provisoire"], "« Inviolable et sacré »", "Nul ne peut en être privé sauf nécessité publique et juste indemnité."),
  Q("Comment appelle-t-on la procédure par laquelle l'État prend un bien privé pour un projet d'intérêt général, contre indemnisation ?", ["L'expropriation", "La confiscation", "Le vol", "La nationalisation forcée sans indemnité"], "L'expropriation", "Elle doit être déclarée d'utilité publique."),
  Q("Quel droit protège les créations de l'esprit (livres, musiques) ?", ["La propriété intellectuelle (droit d'auteur)", "Le droit de grève", "Le droit de vote", "Le droit d'asile"], "La propriété intellectuelle (droit d'auteur)", "Télécharger illégalement porte atteinte à ce droit."),
]),
notion('RA-4', 4, D, 'emc-droit-greve', [
  Q("Depuis quelle Constitution le droit de grève a-t-il une valeur constitutionnelle ?", ["Le préambule de 1946", "La Constitution de 1791", "La Charte de 1814", "La Constitution de 1875"], "Le préambule de 1946", "Il s'exerce « dans le cadre des lois qui le réglementent »."),
  Q("Qu'est-ce qu'un service minimum ?", ["Une continuité minimale du service public pendant une grève", "Un salaire minimum", "Une durée minimale de travail", "Une retraite minimale"], "Une continuité minimale du service public pendant une grève", "Il existe dans les transports et les écoles (accueil)."),
  Q("Quel document doit déposer un syndicat avant une grève dans un service public ?", ["Un préavis de grève, au moins 5 jours avant", "Une pétition", "Une lettre au président", "Rien du tout"], "Un préavis de grève, au moins 5 jours avant", "Il permet d'ouvrir des négociations."),
]),
notion('RA-4', 6, D, 'emc-traites-hierarchie', [
  Q("Selon l'article 55 de la Constitution, les traités régulièrement ratifiés ont une autorité…", ["supérieure à celle des lois", "inférieure à celle des décrets", "égale à celle des arrêtés", "nulle"], "supérieure à celle des lois", "Mais ils restent inférieurs à la Constitution."),
  Q("Quel traité international protège les réfugiés depuis 1951 ?", ["La Convention de Genève", "Le traité de Rome", "Le traité de Versailles", "Le traité de Maastricht"], "La Convention de Genève", "Elle définit le statut de réfugié."),
  Q("Quelle juridiction de l'ONU règle les différends entre États ?", ["La Cour internationale de justice", "La Cour pénale internationale", "La CEDH", "La Cour de cassation"], "La Cour internationale de justice", "Elle siège à La Haye."),
]),
# ══ VR-1 · Principes, valeurs et symboles ══
notion('VR-1', 1, I, 'emc-marseillaise-histoire', [
  Q("Pour quelle armée Rouget de Lisle compose-t-il La Marseillaise en 1792 ?", ["L'armée du Rhin, à Strasbourg", "L'armée d'Italie", "La garde nationale de Paris", "La marine"], "L'armée du Rhin, à Strasbourg", "Les fédérés marseillais la popularisent à Paris."),
  N("En quelle année La Marseillaise devient-elle hymne national pour la première fois ?", 1795, "Elle est interdite sous l'Empire et la Restauration, puis rétablie en 1879."),
  Q("Quel texte de 1958 fait de La Marseillaise l'hymne national ?", ["L'article 2 de la Constitution", "La loi de 1905", "La DDHC", "Le Code civil"], "L'article 2 de la Constitution", "Il cite aussi l'emblème, la devise et la langue."),
]),
notion('VR-1', 3, I, 'emc-liberte-expression-limites', [
  Q("Quel article de la DDHC garantit la libre communication des pensées et des opinions ?", ["L'article 11", "L'article 1er", "L'article 17", "L'article 4"], "L'article 11", "Sauf à répondre de l'abus de cette liberté."),
  Q("Qu'est-ce que la diffamation ?", ["Accuser publiquement quelqu'un d'un fait précis qui porte atteinte à son honneur", "Donner son avis", "Critiquer un film", "Faire une caricature d'un ministre"], "Accuser publiquement quelqu'un d'un fait précis qui porte atteinte à son honneur", "Elle est punie par la loi de 1881."),
  Q("Une caricature d'un responsable politique est-elle permise ?", ["Oui, la satire fait partie de la liberté d'expression", "Non, jamais", "Seulement avec son accord", "Seulement à l'étranger"], "Oui, la satire fait partie de la liberté d'expression", "Elle reste soumise aux limites de la loi."),
]),
notion('VR-1', 5, I, 'emc-laicite-principes', [
  Q("Quelles sont les deux garanties de la laïcité selon l'article 1er de la loi de 1905 ?", ["La liberté de conscience et le libre exercice des cultes", "La religion obligatoire et le culte d'État", "L'interdiction des religions", "Le financement des cultes"], "La liberté de conscience et le libre exercice des cultes", "Dans les limites de l'ordre public."),
  Q("La laïcité signifie-t-elle que l'État est hostile aux religions ?", ["Non, il est neutre et garantit la liberté de croire ou de ne pas croire", "Oui, il combat les religions", "Oui, il interdit les fêtes religieuses", "Non, il favorise une religion"], "Non, il est neutre et garantit la liberté de croire ou de ne pas croire", "La laïcité protège toutes les convictions."),
  Q("Quel jour est célébrée la Journée de la laïcité à l'école ?", ["Le 9 décembre", "Le 14 juillet", "Le 8 mai", "Le 1er septembre"], "Le 9 décembre", "En souvenir de la loi du 9 décembre 1905."),
]),
notion('VR-1', 0, I, 'emc-nationalite', [
  Q("Comment devient-on français à la naissance ?", ["Si au moins un de ses parents est français (droit du sang)", "En naissant n'importe où dans le monde", "En apprenant le français", "En payant une taxe"], "Si au moins un de ses parents est français (droit du sang)", "Le droit du sol joue aussi dans certains cas."),
  Q("Comment appelle-t-on l'acquisition de la nationalité française par décision de l'État ?", ["La naturalisation", "L'adoption", "L'élection", "La conscription"], "La naturalisation", "Elle suppose notamment une bonne connaissance du français."),
  Q("Un enfant né en France de parents étrangers peut-il devenir français ?", ["Oui, à sa majorité s'il réside en France depuis au moins 5 ans", "Non, jamais", "Oui, dès sa naissance automatiquement", "Seulement s'il est adopté"], "Oui, à sa majorité s'il réside en France depuis au moins 5 ans", "C'est le droit du sol différé."),
]),
notion('VR-1', 6, I, 'emc-loi-2004', [
  Q("Que prévoit la loi du 15 mars 2004 ?", ["L'interdiction des signes religieux ostensibles pour les élèves des écoles, collèges et lycées publics", "La séparation des Églises et de l'État", "L'école gratuite", "Le droit de vote à 18 ans"], "L'interdiction des signes religieux ostensibles pour les élèves des écoles, collèges et lycées publics", "Les signes discrets restent autorisés."),
  Q("La loi de 2004 s'applique-t-elle aux étudiants des universités ?", ["Non, seulement aux élèves des écoles, collèges et lycées publics", "Oui, à tous", "Oui, aux étudiants étrangers", "Seulement aux professeurs"], "Non, seulement aux élèves des écoles, collèges et lycées publics", "Les étudiants sont des adultes usagers."),
  Q("Quelle loi de 1882 laïcise les programmes de l'école publique ?", ["La loi Ferry du 28 mars 1882", "La loi Falloux", "La loi Debré", "La loi Guizot"], "La loi Ferry du 28 mars 1882", "L'instruction morale et civique remplace l'instruction religieuse."),
]),
notion('VR-1', 0, D, 'emc-citoyennete-europeenne-droits', [
  Q("Depuis quel traité existe la citoyenneté européenne ?", ["Le traité de Maastricht (1992)", "Le traité de Rome (1957)", "Le traité de Lisbonne (2007)", "Le traité de l'Élysée (1963)"], "Le traité de Maastricht (1992)", "Elle s'ajoute à la citoyenneté nationale."),
  Q("Un citoyen européen résidant en France peut voter à quelles élections ?", ["Municipales et européennes", "Présidentielle", "Législatives", "Toutes"], "Municipales et européennes", "Il ne peut pas voter aux élections nationales."),
  Q("Quel texte de 2000 rassemble les droits fondamentaux des citoyens de l'Union ?", ["La Charte des droits fondamentaux de l'UE", "La DDHC", "La Convention de Genève", "Le Code civil"], "La Charte des droits fondamentaux de l'UE", "Elle est contraignante depuis le traité de Lisbonne."),
]),
notion('VR-1', 1, D, 'emc-marianne-symboles', [
  Q("Quel symbole républicain est reconnu par la Constitution comme emblème national ?", ["Le drapeau tricolore", "Le coq", "Marianne", "Le bonnet phrygien"], "Le drapeau tricolore", "Marianne et le coq ne sont pas cités dans la Constitution."),
  Q("Quel est le sceau officiel de la République, utilisé pour sceller la Constitution ?", ["Le Grand Sceau de France", "La médaille de la Légion d'honneur", "La couronne royale", "La croix de Lorraine"], "Le Grand Sceau de France", "Il représente la Liberté assise."),
  Q("Pourquoi le 14 juillet est-il fête nationale ?", ["Il rappelle la prise de la Bastille (1789) et la fête de la Fédération (1790)", "C'est l'anniversaire de Napoléon", "C'est la fin de la Seconde Guerre mondiale", "C'est la naissance de la Ve République"], "Il rappelle la prise de la Bastille (1789) et la fête de la Fédération (1790)", "La loi de 1880 l'a institué."),
]),
notion('VR-1', 4, D, 'emc-egalite-femmes-hommes-lois', [
  Q("Depuis 1946, quel texte affirme que « la loi garantit à la femme, dans tous les domaines, des droits égaux à ceux de l'homme » ?", ["Le préambule de la Constitution de 1946", "La DDHC de 1789", "Le Code civil de 1804", "La loi de 1905"], "Le préambule de la Constitution de 1946", "Il fait partie du bloc de constitutionnalité."),
  Q("Quel index les entreprises d'au moins 50 salariés doivent-elles publier depuis 2019 ?", ["L'index de l'égalité professionnelle femmes-hommes", "L'index des prix", "L'index boursier", "L'index de pollution"], "L'index de l'égalité professionnelle femmes-hommes", "Il mesure notamment les écarts de salaire."),
  Q("Quelle loi de 2011 impose des quotas de femmes dans les conseils d'administration des grandes entreprises ?", ["La loi Copé-Zimmermann", "La loi Veil", "La loi Roudy", "La loi Neuwirth"], "La loi Copé-Zimmermann", "L'objectif est de 40 %."),
]),
notion('VR-1', 6, D, 'emc-laicite-alsace-outre-mer', [
  Q("Pourquoi la loi de 1905 ne s'applique-t-elle pas en Alsace-Moselle ?", ["Ce territoire était allemand en 1905 et a gardé le régime concordataire", "Par erreur", "Parce que la population l'a refusé en 2005", "Parce qu'il n'y a pas de religion"], "Ce territoire était allemand en 1905 et a gardé le régime concordataire", "Les prêtres, pasteurs et rabbins y sont rémunérés par l'État."),
  Q("Le Conseil constitutionnel a-t-il validé ce régime particulier en 2013 ?", ["Oui, au nom de la tradition républicaine de dispositions locales", "Non, il l'a abrogé", "Il ne s'est jamais prononcé", "Oui, et l'a étendu à toute la France"], "Oui, au nom de la tradition républicaine de dispositions locales", "Décision du Conseil constitutionnel du 21 février 2013."),
  Q("Quelle loi de 1959 permet à l'État de financer les écoles privées sous contrat ?", ["La loi Debré", "La loi Ferry", "La loi Falloux", "La loi Savary"], "La loi Debré", "Les écoles sous contrat suivent les programmes nationaux."),
]),
# ══ VR-2 · Les grands principes des sociétés démocratiques ══
notion('VR-2', 0, F, 'emc-ddhc-1789', [
  N("En quelle année est adoptée la Déclaration des droits de l'homme et du citoyen ?", 1789, "Elle est adoptée le 26 août 1789."),
  Q("Que proclame l'article 1er de la DDHC ?", ["« Les hommes naissent et demeurent libres et égaux en droits »", "« La France est une République indivisible »", "« L'État, c'est moi »", "« Liberté, Égalité, Fraternité »"], "« Les hommes naissent et demeurent libres et égaux en droits »", "C'est un texte fondateur de la démocratie française."),
  Q("Quelle place a la DDHC dans le droit français aujourd'hui ?", ["Elle a valeur constitutionnelle", "Elle n'a aucune valeur", "C'est un simple règlement scolaire", "Elle a été abrogée"], "Elle a valeur constitutionnelle", "Le préambule de 1958 y renvoie."),
]),
notion('VR-2', 0, I, 'emc-declarations-comparees', [
  Q("Quel texte de 1776 proclame que tous les hommes ont des droits inaliénables, dont « la vie, la liberté et la recherche du bonheur » ?", ["La Déclaration d'indépendance des États-Unis", "La DDHC", "La Magna Carta", "Le Bill of Rights anglais"], "La Déclaration d'indépendance des États-Unis", "Elle inspire les révolutionnaires français."),
  Q("Quel texte anglais de 1689 limite les pouvoirs du roi face au Parlement ?", ["Le Bill of Rights", "La Magna Carta", "L'Habeas Corpus de 1215", "La Déclaration d'indépendance"], "Le Bill of Rights", "Il fonde la monarchie parlementaire."),
  Q("Quelle différence majeure distingue la DUDH de 1948 de la DDHC de 1789 ?", ["Elle a une portée universelle et ajoute des droits économiques et sociaux", "Elle ne concerne que la France", "Elle supprime les libertés", "Elle ne concerne que les hommes"], "Elle a une portée universelle et ajoute des droits économiques et sociaux", "Droit au travail, à l'éducation, à la santé…"),
]),
notion('VR-2', 1, I, 'emc-statut-enfant', [
  Q("En France, à quel âge devient-on majeur ?", ["18 ans", "16 ans", "21 ans", "15 ans"], "18 ans", "Depuis la loi de 1974."),
  Q("Qui exerce l'autorité parentale sur un enfant mineur ?", ["Ses deux parents, en principe ensemble", "L'école", "Le maire", "Le juge seul"], "Ses deux parents, en principe ensemble", "Elle vise à protéger l'enfant."),
  Q("Un enfant peut-il être entendu par un juge dans une procédure qui le concerne ?", ["Oui, s'il est capable de discernement", "Non, jamais", "Seulement après 18 ans", "Seulement avec l'accord du maire"], "Oui, s'il est capable de discernement", "C'est un droit prévu par la CIDE."),
]),
notion('VR-2', 2, I, 'emc-pluralisme-medias', [
  Q("Quelle autorité veille au pluralisme et à la régulation de l'audiovisuel et du numérique ?", ["L'Arcom", "La CNIL", "Le Conseil d'État", "L'Assemblée nationale"], "L'Arcom", "Elle remplace le CSA et l'Hadopi depuis 2022."),
  Q("Pourquoi la diversité des médias est-elle importante en démocratie ?", ["Elle permet l'expression de différents points de vue", "Elle est inutile", "Elle crée la censure", "Elle empêche de s'informer"], "Elle permet l'expression de différents points de vue", "Le pluralisme est un objectif à valeur constitutionnelle."),
  Q("Qu'est-ce que la concentration des médias ?", ["La possession de nombreux médias par un petit nombre de groupes", "Un média très concentré sur l'actualité", "Une réunion de journalistes", "Une émission spéciale"], "La possession de nombreux médias par un petit nombre de groupes", "Elle peut menacer le pluralisme."),
]),
notion('VR-2', 3, I, 'emc-petition', [
  Q("Qu'est-ce qu'une pétition ?", ["Une demande collective signée adressée aux autorités", "Une loi", "Un jugement", "Un impôt"], "Une demande collective signée adressée aux autorités", "C'est une forme d'expression citoyenne."),
  Q("À partir de combien de signatures une pétition sur le site de l'Assemblée nationale peut-elle donner lieu à un débat en séance ?", ["500 000", "1 000", "10 millions", "50"], "500 000", "Si elles proviennent d'au moins 30 départements."),
  Q("Quelle assemblée consultative peut être saisie par une pétition de 150 000 personnes ?", ["Le Conseil économique, social et environnemental (CESE)", "Le Sénat", "Le Conseil constitutionnel", "La Cour de cassation"], "Le Conseil économique, social et environnemental (CESE)", "Depuis 2021, le seuil est de 150 000 signataires."),
]),
notion('VR-2', 0, D, 'emc-droits-generations', [
  Q("Comment appelle-t-on les droits de la DDHC de 1789 (liberté, sûreté, propriété) ?", ["Des droits-libertés (droits de première génération)", "Des droits sociaux", "Des droits environnementaux", "Des droits numériques"], "Des droits-libertés (droits de première génération)", "Ils protègent l'individu face à l'État."),
  Q("Quel texte constitutionnel français ajoute en 1946 des droits sociaux, comme le droit à l'emploi ?", ["Le préambule de 1946", "La DDHC", "La Charte de l'environnement", "Le Code du travail"], "Le préambule de 1946", "On parle de droits-créances."),
  N("En quelle année la Charte de l'environnement est-elle intégrée à la Constitution ?", 2005, "Elle affirme le droit de vivre dans un environnement équilibré."),
]),
notion('VR-2', 0, D, 'emc-olympe-gouges', [
  Q("Quel texte Olympe de Gouges écrit-elle en 1791 en réponse à la DDHC ?", ["La Déclaration des droits de la femme et de la citoyenne", "Le Contrat social", "Le Deuxième Sexe", "La Charte des droits fondamentaux"], "La Déclaration des droits de la femme et de la citoyenne", "Elle dénonce l'exclusion des femmes."),
  Q("Quelle phrase célèbre figure dans ce texte ?", ["« La femme a le droit de monter sur l'échafaud ; elle doit avoir également celui de monter à la tribune »", "« Je pense donc je suis »", "« L'homme est né libre »", "« Liberté, Égalité, Fraternité »"], "« La femme a le droit de monter sur l'échafaud ; elle doit avoir également celui de monter à la tribune »", "Elle est guillotinée en 1793."),
  Q("Quel texte de 1948 a été rédigé avec la participation de René Cassin ?", ["La Déclaration universelle des droits de l'homme", "La DDHC", "La Constitution de 1958", "Le traité de Rome"], "La Déclaration universelle des droits de l'homme", "Il reçoit le prix Nobel de la paix en 1968."),
]),
notion('VR-2', 1, D, 'emc-cide', [
  N("En quelle année la Convention internationale des droits de l'enfant est-elle adoptée par l'ONU ?", 1989, "Le 20 novembre, journée internationale des droits de l'enfant."),
  Q("Quel principe guide toute décision concernant un enfant selon la CIDE ?", ["L'intérêt supérieur de l'enfant", "L'intérêt des parents", "L'intérêt de l'État", "La volonté du juge"], "L'intérêt supérieur de l'enfant", "C'est l'article 3 de la Convention."),
  Q("Quel pays n'a jamais ratifié la CIDE ?", ["Les États-Unis", "La France", "Le Canada", "Le Japon"], "Les États-Unis", "Ils l'ont signée mais pas ratifiée."),
]),
notion('VR-2', 2, D, 'emc-loi-1881', [
  Q("Quelle loi de 1881 fonde la liberté de la presse en France ?", ["La loi du 29 juillet 1881", "La loi de 1905", "La loi Ferry", "La loi Le Chapelier"], "La loi du 29 juillet 1881", "Son article 1er : « L'imprimerie et la librairie sont libres »."),
  Q("Qu'est-ce que le droit de réponse ?", ["Le droit d'une personne mise en cause de faire publier sa réponse dans le même média", "Le droit de répondre en classe", "Le droit de vote", "Le droit de grève"], "Le droit d'une personne mise en cause de faire publier sa réponse dans le même média", "Il est prévu par la loi de 1881."),
  Q("Quelle loi de 2018 permet de faire cesser rapidement la diffusion de fausses informations en période électorale ?", ["La loi relative à la lutte contre la manipulation de l'information", "La loi Gayssot", "La loi Avia, entièrement validée", "La loi de 1905"], "La loi relative à la lutte contre la manipulation de l'information", "Un juge des référés peut être saisi."),
]),
notion('VR-2', 2, D, 'emc-dsa', [
  Q("Quel règlement européen de 2022 oblige les grandes plateformes à lutter contre les contenus illicites ?", ["Le Digital Services Act (DSA)", "Le RGPD", "Le traité de Lisbonne", "L'AI Act"], "Le Digital Services Act (DSA)", "Les amendes peuvent atteindre 6 % du chiffre d'affaires mondial."),
  Q("Quel classement annuel mesure la liberté de la presse dans le monde ?", ["Le classement de Reporters sans frontières", "Le classement de Shanghai", "Le classement FIFA", "Le classement PISA"], "Le classement de Reporters sans frontières", "Il est publié chaque année."),
  Q("Qu'est-ce que le secret des sources des journalistes ?", ["Le droit de ne pas révéler l'identité de ses informateurs", "L'obligation de tout révéler", "Un secret médical", "Un secret défense"], "Le droit de ne pas révéler l'identité de ses informateurs", "Il est protégé par la loi de 2010."),
]),
notion('VR-2', 3, D, 'emc-convention-citoyenne', [
  Q("Combien de citoyens tirés au sort composent la Convention citoyenne pour le climat (2019-2020) ?", ["150", "15", "1 500", "577"], "150", "Elle formule 149 propositions."),
  Q("Quel sujet traite la Convention citoyenne de 2022-2023 ?", ["La fin de vie", "Le climat", "Les retraites", "L'école"], "La fin de vie", "Elle se prononce majoritairement pour une « aide active à mourir » encadrée."),
  Q("Qu'est-ce que la démocratie participative ?", ["L'association des citoyens aux décisions, au-delà du vote", "La suppression des élections", "Le vote obligatoire", "Le pouvoir d'un seul"], "L'association des citoyens aux décisions, au-delà du vote", "Budgets participatifs, consultations, conventions citoyennes…"),
]),
# ══ VR-3 · Les grandes caractéristiques d'un État démocratique ══
notion('VR-3', 4, D, 'emc-fiscalite', [
  Q("Quel article de la DDHC fonde la contribution commune « également répartie entre tous les citoyens, en raison de leurs facultés » ?", ["L'article 13", "L'article 1er", "L'article 4", "L'article 17"], "L'article 13", "C'est le fondement de l'impôt."),
  Q("Qui vote chaque année le budget de l'État ?", ["Le Parlement, par la loi de finances", "Le Président seul", "Le Conseil constitutionnel", "Les maires"], "Le Parlement, par la loi de finances", "C'est l'origine historique des parlements."),
  Q("Qu'est-ce qu'un impôt progressif ?", ["Un impôt dont le taux augmente avec le revenu", "Un impôt identique pour tous", "Un impôt qui diminue chaque année", "Un impôt payé uniquement par les entreprises"], "Un impôt dont le taux augmente avec le revenu", "L'impôt sur le revenu est progressif ; la TVA ne l'est pas."),
]),
notion('VR-3', 5, D, 'emc-deconcentration', [
  Q("Quelle différence y a-t-il entre décentralisation et déconcentration ?", ["Décentraliser, c'est confier des compétences à des collectivités élues ; déconcentrer, c'est confier des pouvoirs à des agents de l'État sur le territoire", "Elles sont identiques", "La déconcentration supprime l'État", "La décentralisation renforce Paris"], "Décentraliser, c'est confier des compétences à des collectivités élues ; déconcentrer, c'est confier des pouvoirs à des agents de l'État sur le territoire", "Le préfet est l'agent de la déconcentration."),
  Q("Qui représente l'État dans chaque département ?", ["Le préfet", "Le maire", "Le président du conseil départemental", "Le député"], "Le préfet", "Il est nommé en Conseil des ministres."),
  Q("Quel article de la Constitution affirme que l'organisation de la République est décentralisée ?", ["L'article 1er, depuis 2003", "L'article 49", "L'article 16", "L'article 89"], "L'article 1er, depuis 2003", "C'est la révision constitutionnelle du 28 mars 2003."),
]),
notion('VR-3', 6, D, 'emc-francophonie', [
  Q("Quelle organisation regroupe les États et gouvernements ayant le français en partage ?", ["L'Organisation internationale de la Francophonie (OIF)", "L'ONU", "L'Union européenne", "Le Commonwealth"], "L'Organisation internationale de la Francophonie (OIF)", "Elle compte plus de 80 membres et observateurs."),
  Q("Combien de personnes parlent le français dans le monde environ ?", ["Plus de 320 millions", "Environ 30 millions", "Environ 3 milliards", "Environ 70 millions"], "Plus de 320 millions", "La majorité vit en Afrique."),
  Q("Quel jour est célébrée la Journée internationale de la Francophonie ?", ["Le 20 mars", "Le 14 juillet", "Le 9 mai", "Le 11 novembre"], "Le 20 mars", "Elle rappelle la création de l'ACCT à Niamey en 1970."),
]),
]

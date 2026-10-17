from qlib import Q, N, C, notion
I = 'intermediaire'
NOTIONS = [
notion('F50', 1, I, 'f-principale-subordonnee', [
  C("Cliquez sur tous les mots de la proposition subordonnée.", "Je pense [qu'il viendra demain].", "La subordonnée « qu'il viendra demain » dépend du verbe « pense » de la principale ; elle est introduite par le subordonnant « que »."),
  C("Cliquez sur tous les mots de la proposition principale.", "[Nous partirons] dès que la pluie cessera.", "La principale « nous partirons » a un sens par elle-même ; « dès que la pluie cessera » en dépend."),
  Q("Dans « L'élève qui a gagné sourit », combien y a-t-il de propositions ?", ["Une", "Deux", "Trois", "Quatre"], "Deux", "Deux verbes conjugués : « sourit » (principale) et « a gagné » (subordonnée relative enchâssée dans le sujet)."),
]),
notion('F53', 0, I, 'f-pronom-relatif', [
  C("Cliquez sur le pronom relatif.", "Le livre [que] tu m'as prêté est passionnant.", "« Que » reprend l'antécédent « le livre » et introduit la subordonnée relative : c'est un pronom relatif."),
  C("Cliquez sur le pronom relatif.", "La ville [où] je suis né est au bord de la mer.", "« Où » reprend « la ville » et introduit une relative : ici, c'est un pronom relatif."),
  C("Cliquez sur le pronom relatif.", "C'est un ami [dont] je suis fier.", "« Dont » reprend « un ami » (être fier de quelqu'un) : c'est un pronom relatif."),
]),
notion('F53', 0, I, 'f-conjonction-subordination', [
  C("Cliquez sur la conjonction de subordination.", "Je reste à la maison [parce qu'] il pleut.", "La locution conjonctive « parce que » introduit une subordonnée de cause. Contrairement au pronom relatif, elle ne reprend aucun nom."),
  C("Cliquez sur la conjonction de subordination.", "Il faut [que] tu viennes.", "Ici « que » ne reprend aucun antécédent : c'est une conjonction de subordination qui introduit une complétive."),
  C("Cliquez sur la conjonction de subordination.", "[Quand] le chat dort, les souris dansent.", "« Quand » introduit une subordonnée de temps : c'est une conjonction de subordination."),
]),
notion('F53', 1, I, 'f-subordonnee-relative', [
  C("Cliquez sur tous les mots de la proposition subordonnée relative.", "La maison [qui se trouve au bout de la rue] est à vendre.", "La relative commence par le pronom « qui » et complète l'antécédent « la maison »."),
  C("Cliquez sur tous les mots de la proposition subordonnée relative.", "J'ai retrouvé la photo [que tu cherchais].", "« Que tu cherchais » complète le nom « photo » : c'est une subordonnée relative."),
  Q("Quelle est la fonction de la subordonnée relative dans « Le chien qui aboie est nerveux » ?", ["Sujet", "Complément de l'antécédent « chien »", "COD", "Complément circonstanciel"], "Complément de l'antécédent « chien »", "La relative « qui aboie » complète le nom « chien », comme le ferait un adjectif (le chien aboyeur)."),
]),
notion('F53', 2, I, 'f-cc-cause-but-consequence', [
  Q("Dans « Il travaille pour réussir », quelle circonstance exprime « pour réussir » ?", ["La cause", "Le but", "La conséquence", "Le temps"], "Le but", "« Pour » + infinitif exprime le but : l'objectif visé."),
  Q("Dans « Il est absent à cause de la grève », quelle circonstance exprime le complément ?", ["La cause", "Le but", "L'opposition", "La condition"], "La cause", "« À cause de » introduit la raison de l'absence : c'est la cause."),
  Q("Dans « Il a tant couru qu'il est épuisé », que exprime la subordonnée ?", ["La cause", "La conséquence", "Le but", "La comparaison"], "La conséquence", "« Tant… que » introduit le résultat de l'action : la conséquence."),
]),
notion('F53', 2, I, 'f-apposition', [
  C("Cliquez sur tous les mots en apposition.", "Paris, [capitale de la France], attire les touristes.", "L'apposition, séparée par des virgules, apporte une précision sur le nom « Paris » ; on peut la supprimer."),
  C("Cliquez sur tous les mots en apposition.", "[Épuisé par sa course], le coureur s'assit.", "Le groupe détaché en tête de phrase se rapporte au sujet « le coureur » : il est en apposition."),
  Q("Dans « Victor Hugo, poète engagé, s'exila », quelle est la fonction de « poète engagé » ?", ["Sujet", "Attribut du sujet", "Apposition", "Complément du nom"], "Apposition", "Détaché par des virgules et sans verbe, ce groupe précise le nom « Victor Hugo » : c'est une apposition."),
]),
notion('F49', 5, I, 'f-juxtaposition-coordination', [
  Q("« Il pleuvait ; nous sommes restés. » Les propositions sont…", ["coordonnées", "juxtaposées", "subordonnées", "enchâssées"], "juxtaposées", "Elles sont reliées par un signe de ponctuation (point-virgule), sans mot de liaison : juxtaposées."),
  Q("« Il pleuvait, donc nous sommes restés. » Les propositions sont…", ["juxtaposées", "coordonnées", "subordonnées", "indépendantes sans lien"], "coordonnées", "Elles sont reliées par « donc », un mot de coordination : elles sont coordonnées."),
  Q("Dans « Je suis venu, j'ai vu, j'ai vaincu », quel effet produit la juxtaposition ?", ["Un effet de lenteur", "Un effet de rapidité et d'enchaînement", "Une opposition", "Une hypothèse"], "Un effet de rapidité et d'enchaînement", "Sans mots de liaison, les actions s'enchaînent sèchement : la juxtaposition crée un rythme rapide."),
]),
notion('F62', 0, I, 'f-plus-que-parfait', [
  Q("À quel temps est « ils avaient fini » ?", ["Passé composé", "Plus-que-parfait", "Passé antérieur", "Conditionnel passé"], "Plus-que-parfait", "Auxiliaire à l'imparfait (avaient) + participe passé : plus-que-parfait."),
  Q("Quelle forme est au plus-que-parfait ?", ["Elle était partie", "Elle est partie", "Elle fut partie", "Elle serait partie"], "Elle était partie", "Être à l'imparfait + participe : plus-que-parfait."),
  Q("Quelle valeur a souvent le plus-que-parfait dans un récit au passé ?", ["Une action postérieure", "Une action antérieure à une autre action passée", "Une action future", "Un ordre"], "Une action antérieure à une autre action passée", "« Quand il arriva, elle était déjà partie » : le départ a eu lieu avant l'arrivée."),
]),
notion('F62', 0, I, 'f-futur-anterieur', [
  Q("À quel temps est « nous aurons terminé » ?", ["Futur simple", "Futur antérieur", "Conditionnel passé", "Passé composé"], "Futur antérieur", "Auxiliaire au futur (aurons) + participe passé : futur antérieur."),
  Q("Dans « Quand tu auras fini, tu sortiras », quelle action se passe en premier ?", ["Sortir", "Finir", "Les deux en même temps", "Aucune"], "Finir", "Le futur antérieur (auras fini) marque une action future antérieure à une autre action future (sortiras)."),
  Q("Quelle forme est au futur antérieur ?", ["Il sera venu", "Il serait venu", "Il était venu", "Il viendra"], "Il sera venu", "Être au futur (sera) + participe passé : futur antérieur."),
]),
notion('F62', 0, I, 'f-conditionnel-passe', [
  Q("À quel temps est « j'aurais aimé » ?", ["Futur antérieur", "Conditionnel passé", "Plus-que-parfait", "Subjonctif passé"], "Conditionnel passé", "Auxiliaire au conditionnel présent (aurais) + participe passé : conditionnel passé."),
  Q("Quelle forme est au conditionnel passé ?", ["Tu serais venu", "Tu seras venu", "Tu étais venu", "Tu fus venu"], "Tu serais venu", "Être au conditionnel (serais) + participe : conditionnel passé."),
  Q("Dans « Si j'avais su, je serais venu », quelle valeur a le conditionnel passé ?", ["Un fait certain", "Un fait irréel dans le passé", "Un ordre", "Un futur proche"], "Un fait irréel dans le passé", "La condition ne s'est pas réalisée : je ne suis pas venu. C'est l'irréel du passé."),
]),
notion('F62', 3, I, 'f-voix-passive', [
  Q("Quelle phrase est à la voix passive ?", ["Le chat mange la souris.", "La souris est mangée par le chat.", "Le chat est affamé.", "La souris s'enfuit."], "La souris est mangée par le chat.", "Être + participe passé, avec un complément d'agent (par le chat) : voix passive."),
  Q("Transformez à la voix passive : « Le vent a renversé l'arbre. »", ["L'arbre a renversé le vent.", "L'arbre a été renversé par le vent.", "L'arbre est renversant.", "Le vent est renversé par l'arbre."], "L'arbre a été renversé par le vent.", "Le COD devient sujet, le sujet devient complément d'agent, et le verbe passe à être (au même temps : a été) + participe."),
  Q("Dans « Le gâteau a été préparé par Léa », quelle est la fonction de « par Léa » ?", ["COD", "COI", "Complément d'agent", "Complément circonstanciel de manière"], "Complément d'agent", "À la voix passive, le complément d'agent désigne celui qui fait l'action."),
]),
notion('F65', 0, I, 'f-valeurs-conditionnel', [
  Q("Dans « Il m'a dit qu'il viendrait », quelle valeur a le conditionnel ?", ["Une hypothèse", "Le futur dans le passé", "Une demande polie", "Un souhait"], "Le futur dans le passé", "Le conditionnel exprime ici une action future vue depuis un moment passé : c'est une valeur temporelle."),
  Q("Dans « Pourriez-vous m'aider ? », quelle valeur a le conditionnel ?", ["La politesse", "Le futur dans le passé", "L'irréel du passé", "Un fait certain"], "La politesse", "Le conditionnel atténue la demande : c'est une valeur modale de politesse."),
  Q("Dans « Selon la presse, le ministre démissionnerait », quelle valeur a le conditionnel ?", ["Un ordre", "Une information non confirmée", "Un futur certain", "Une politesse"], "Une information non confirmée", "Le conditionnel journalistique présente un fait incertain, non vérifié."),
]),
notion('F65', 2, I, 'f-subjonctif', [
  Q("Quelle forme est au subjonctif présent ?", ["Qu'il fait", "Qu'il fasse", "Qu'il ferait", "Qu'il fera"], "Qu'il fasse", "Le subjonctif présent de « faire » est « que je fasse, qu'il fasse »."),
  Q("Après quelle expression emploie-t-on le subjonctif ?", ["Je pense que", "Il est certain que", "Je veux que", "J'espère que"], "Je veux que", "La volonté (vouloir que, exiger que) entraîne le subjonctif. « Penser que » et « espérer que » sont suivis de l'indicatif."),
  Q("Quelle phrase est correcte ?", ["Il faut que tu viens.", "Il faut que tu viennes.", "Il faut que tu viendras.", "Il faut que tu venais."], "Il faut que tu viennes.", "« Il faut que » exprime la nécessité et commande le subjonctif."),
]),
notion('F64', 0, I, 'f-valeurs-present', [
  Q("Dans « La Terre tourne autour du Soleil », quelle est la valeur du présent ?", ["Présent d'énonciation", "Présent de vérité générale", "Présent de narration", "Futur proche"], "Présent de vérité générale", "Le fait est toujours vrai, quel que soit le moment : présent de vérité générale."),
  Q("Dans « En 1789, le peuple prend la Bastille », quelle est la valeur du présent ?", ["Présent de narration", "Présent d'habitude", "Présent de vérité générale", "Présent d'énonciation"], "Présent de narration", "Le présent raconte un fait passé pour le rendre plus vivant : présent de narration (ou historique)."),
  Q("Dans « Je pars dans cinq minutes », quelle est la valeur du présent ?", ["Passé récent", "Futur proche", "Vérité générale", "Habitude"], "Futur proche", "L'action aura lieu bientôt : le présent exprime un futur proche."),
]),
notion('F64', 0, I, 'f-imparfait-passe-simple', [
  Q("Dans un récit, quel temps exprime le plus souvent les actions de premier plan, ponctuelles et successives ?", ["L'imparfait", "Le passé simple", "Le plus-que-parfait", "Le présent de vérité générale"], "Le passé simple", "Le passé simple présente des actions délimitées qui font avancer le récit ; l'imparfait décrit l'arrière-plan."),
  Q("Dans « Il lisait quand le téléphone sonna », quel verbe exprime l'action d'arrière-plan ?", ["Sonna", "Lisait", "Les deux", "Aucun"], "Lisait", "L'imparfait (lisait) décrit une action en cours, interrompue par une action ponctuelle au passé simple (sonna)."),
  Q("Dans « Chaque matin, il se levait à six heures », quelle valeur a l'imparfait ?", ["Action ponctuelle", "Habitude dans le passé", "Futur dans le passé", "Ordre"], "Habitude dans le passé", "Avec « chaque matin », l'imparfait exprime une action répétée, une habitude."),
]),
notion('F67', 3, I, 'f-pp-avoir', [
  Q("Quelle phrase est correcte ?", ["Les lettres que j'ai écrit sont parties.", "Les lettres que j'ai écrites sont parties.", "Les lettres que j'ai écrits sont parties.", "Les lettres que j'ai écrite sont parties."], "Les lettres que j'ai écrites sont parties.", "Avec avoir, le participe s'accorde avec le COD placé avant : « que », mis pour « les lettres » (féminin pluriel)."),
  Q("Quelle phrase est correcte ?", ["Elle a mangée une pomme.", "Elle a mangé une pomme.", "Elle a mangés une pomme.", "Elle a manger une pomme."], "Elle a mangé une pomme.", "Avec avoir, on n'accorde pas avec le sujet ; le COD « une pomme » est placé après le verbe : pas d'accord."),
  Q("Quelle phrase est correcte ?", ["Ces fleurs, je les ai cueilli.", "Ces fleurs, je les ai cueillies.", "Ces fleurs, je les ai cueillis.", "Ces fleurs, je les ai cueillit."], "Ces fleurs, je les ai cueillies.", "Le COD « les » (ces fleurs) est placé avant le verbe : accord au féminin pluriel."),
]),
notion('F68', 1, I, 'f-accord-qui', [
  Q("Quelle phrase est correcte ?", ["C'est moi qui a raison.", "C'est moi qui ai raison.", "C'est moi qui as raison.", "C'est moi qui ont raison."], "C'est moi qui ai raison.", "Le pronom relatif « qui » a pour antécédent « moi » : le verbe se met à la 1re personne du singulier."),
  Q("Quelle phrase est correcte ?", ["C'est toi qui viendra.", "C'est toi qui viendras.", "C'est toi qui viendrai.", "C'est toi qui viendront."], "C'est toi qui viendras.", "« Qui » reprend « toi » : 2e personne du singulier."),
  Q("Quelle phrase est correcte ?", ["Les élèves qui travaille réussiront.", "Les élèves qui travaillent réussiront.", "Les élèves qui travailles réussiront.", "Les élèves qui travaillons réussiront."], "Les élèves qui travaillent réussiront.", "« Qui » reprend « les élèves » : le verbe s'accorde à la 3e personne du pluriel."),
]),
notion('F68', 0, I, 'f-determinants-indefinis', [
  Q("Quelle forme est correcte ?", ["Aucuns élèves n'est venu.", "Aucun élève n'est venu.", "Aucun élèves n'est venus.", "Aucune élève n'est venu."], "Aucun élève n'est venu.", "« Aucun » s'emploie au singulier (sauf avec des noms toujours pluriels) et le verbe aussi."),
  Q("Quelle forme est correcte ?", ["Chaque enfants a un livre.", "Chaque enfant a un livre.", "Chaque enfant ont un livre.", "Chaques enfants ont un livre."], "Chaque enfant a un livre.", "« Chaque » est toujours singulier : le nom et le verbe aussi."),
  Q("Quelle forme est correcte ?", ["Quelque amis sont venus.", "Quelques amis sont venus.", "Quelques ami sont venus.", "Quelques amis est venu."], "Quelques amis sont venus.", "« Quelques » (un petit nombre de) prend un -s devant un nom pluriel."),
]),
notion('F59', 0, I, 'f-transposition-indirect', [
  Q("Transformez au discours indirect : Elle dit : « Je suis contente. »", ["Elle dit qu'elle est contente.", "Elle dit que je suis contente.", "Elle dit : elle est contente.", "Elle dit qu'elle était contente demain."], "Elle dit qu'elle est contente.", "Au discours indirect, le pronom change (je → elle) ; le verbe introducteur étant au présent, le temps ne change pas."),
  Q("Transformez au discours indirect : Il a demandé : « Viens-tu ? »", ["Il a demandé si je venais.", "Il a demandé que je viens.", "Il a demandé viens-tu.", "Il a demandé si je viendrai."], "Il a demandé si je venais.", "Une question totale devient une subordonnée introduite par « si » ; après un verbe au passé, le présent devient imparfait."),
  Q("Transformez au discours indirect : Elle a affirmé : « J'ai réussi hier. »", ["Elle a affirmé qu'elle a réussi hier.", "Elle a affirmé qu'elle avait réussi la veille.", "Elle a affirmé qu'elle réussira la veille.", "Elle a affirmé que j'ai réussi hier."], "Elle a affirmé qu'elle avait réussi la veille.", "Après un verbe au passé : le passé composé devient plus-que-parfait, et « hier » devient « la veille »."),
]),
notion('F41', 0, I, 'f-polysemie-homonymie', [
  Q("Le mot « feuille » (d'arbre, de papier) est un exemple de…", ["polysémie", "homonymie", "antonymie", "paronymie"], "polysémie", "Un même mot a plusieurs sens liés entre eux (une surface mince et plate) : c'est un mot polysémique."),
  Q("« Verre », « vert », « ver » et « vers » sont…", ["des synonymes", "des homonymes", "des antonymes", "des mots de la même famille"], "des homonymes", "Ils se prononcent de la même façon mais ont des sens et des orthographes différents."),
  Q("« Éminent » et « imminent » sont…", ["des homonymes", "des paronymes", "des synonymes", "des antonymes"], "des paronymes", "Des paronymes se ressemblent par la forme mais ont des sens différents : éminent (remarquable), imminent (sur le point d'arriver)."),
]),
notion('F42', 0, I, 'f-denotation-connotation', [
  Q("Quelle est la connotation du mot « rouge » dans « Il voit rouge » ?", ["La couleur du sang au sens propre", "La colère", "Le calme", "La tristesse"], "La colère", "La dénotation est le sens premier (une couleur) ; la connotation est le sens suggéré, ici la colère."),
  Q("Qu'est-ce que la dénotation d'un mot ?", ["Son sens premier, objectif", "Les idées qu'il évoque", "Son étymologie", "Sa prononciation"], "Son sens premier, objectif", "La dénotation est le sens littéral, celui du dictionnaire ; la connotation ajoute des valeurs subjectives ou culturelles."),
  Q("Quel mot a une connotation péjorative ?", ["Maison", "Taudis", "Logement", "Demeure"], "Taudis", "« Taudis » désigne un logement en suggérant la misère et la saleté : sa connotation est péjorative."),
]),
notion('F38', 1, I, 'f-composition', [
  Q("Comment est formé le mot « porte-monnaie » ?", ["Par dérivation", "Par composition", "Par abréviation", "Par emprunt"], "Par composition", "Il associe deux mots existants (porte + monnaie) : c'est un mot composé."),
  Q("Comment est formé le mot « bibliothèque » ?", ["Composition savante à partir du grec", "Dérivation avec suffixe", "Abréviation", "Mot-valise"], "Composition savante à partir du grec", "Biblio (livre) + thèque (coffre, lieu de rangement) : deux éléments grecs."),
  Q("Quel mot est formé par dérivation ?", ["Chou-fleur", "Arc-en-ciel", "Impoli", "Pomme de terre"], "Impoli", "Impoli = préfixe im- + poli : c'est une dérivation. Les autres sont des mots composés."),
]),
notion('F38', 3, I, 'f-degre-intensite', [
  Q("Quel est le classement du moins intense au plus intense ?", ["Peur, effroi, crainte", "Crainte, peur, effroi", "Effroi, crainte, peur", "Peur, crainte, effroi"], "Crainte, peur, effroi", "La crainte est une légère appréhension, la peur un sentiment net, l'effroi une peur intense."),
  Q("Quel mot exprime le plus haut degré de chaleur ?", ["Tiède", "Chaud", "Brûlant", "Doux"], "Brûlant", "Tiède < chaud < brûlant."),
  Q("Quel classement va du plus général au plus particulier ?", ["Animal, mammifère, chien, caniche", "Caniche, chien, mammifère, animal", "Chien, animal, caniche, mammifère", "Mammifère, animal, chien, caniche"], "Animal, mammifère, chien, caniche", "Du terme générique (animal) au terme le plus spécifique (caniche)."),
]),
notion('F39', 1, I, 'f-connecteurs', [
  Q("Quel connecteur exprime l'opposition ?", ["Donc", "Pourtant", "Car", "Ainsi"], "Pourtant", "« Pourtant » introduit une idée contraire à ce qu'on attendait : opposition (concession)."),
  Q("Quel connecteur introduit une conséquence ?", ["Cependant", "Par conséquent", "En effet", "Néanmoins"], "Par conséquent", "« Par conséquent » introduit le résultat de ce qui précède."),
  Q("Quel connecteur introduit une explication ou une justification ?", ["En effet", "Toutefois", "Donc", "Enfin"], "En effet", "« En effet » annonce la justification de ce qui vient d'être affirmé."),
]),
notion('F36', 1, I, 'f-hyperbole-litote', [
  Q("« Je meurs de faim. » Quelle figure de style est utilisée ?", ["Une litote", "Une hyperbole", "Un euphémisme", "Une antithèse"], "Une hyperbole", "L'exagération (mourir de faim) pour exprimer une grande faim : c'est une hyperbole."),
  Q("« Va, je ne te hais point » (Corneille) signifie « je t'aime ». Quelle figure de style est utilisée ?", ["Une hyperbole", "Une litote", "Une métaphore", "Une anaphore"], "Une litote", "La litote dit moins pour suggérer plus, souvent par la négation du contraire."),
  Q("« Il nous a quittés » pour dire « il est mort ». Quelle figure de style est utilisée ?", ["Une hyperbole", "Un euphémisme", "Une litote", "Une comparaison"], "Un euphémisme", "L'euphémisme atténue une réalité pénible ou choquante."),
]),
notion('F36', 1, I, 'f-anaphore-gradation', [
  Q("« Paris ! Paris outragé ! Paris brisé ! Paris martyrisé ! » Quelle figure repose sur la reprise de « Paris » en début de groupe ?", ["Une anaphore", "Une litote", "Une métonymie", "Un oxymore"], "Une anaphore", "L'anaphore répète un même mot en tête de phrases ou de vers pour insister."),
  Q("« Va, cours, vole, et nous venge ! » (Corneille) Quelle figure de style est utilisée ?", ["Une gradation", "Une litote", "Un euphémisme", "Une antithèse"], "Une gradation", "Les verbes sont rangés par intensité croissante (va, cours, vole) : c'est une gradation."),
  Q("Quel est l'effet le plus fréquent d'une anaphore ?", ["Atténuer", "Insister et créer un rythme", "Ridiculiser", "Rendre le texte plus court"], "Insister et créer un rythme", "La répétition martèle une idée et donne du rythme, notamment dans les discours et la poésie engagée."),
]),
notion('F12', 2, I, 'f-mouvements-litteraires', [
  Q("Quel mouvement littéraire du XIXe siècle met en avant l'expression des sentiments et du moi ?", ["Le classicisme", "Le romantisme", "Le naturalisme", "L'humanisme"], "Le romantisme", "Le romantisme (Hugo, Lamartine, Musset) privilégie le lyrisme, les émotions et la nature."),
  Q("À quel mouvement appartient Émile Zola ?", ["Le romantisme", "Le naturalisme", "Le surréalisme", "Le classicisme"], "Le naturalisme", "Zola, avec la série des Rougon-Macquart, est le chef de file du naturalisme, qui veut décrire la société de façon quasi scientifique."),
  Q("À quel siècle appartient le mouvement des Lumières ?", ["XVIe", "XVIIe", "XVIIIe", "XIXe"], "XVIIIe", "Les Lumières (Voltaire, Diderot, Rousseau, Montesquieu) dominent le XVIIIe siècle et défendent la raison et la tolérance."),
]),
notion('F11', 2, I, 'f-auteurs-siecles', [
  Q("Molière a vécu au…", ["XVIe siècle", "XVIIe siècle", "XVIIIe siècle", "XIXe siècle"], "XVIIe siècle", "Molière (1622-1673) est l'auteur de comédies comme Le Malade imaginaire ou L'Avare, sous Louis XIV."),
  Q("Quel auteur appartient au XVIe siècle ?", ["Rabelais", "Racine", "Voltaire", "Baudelaire"], "Rabelais", "Rabelais (Gargantua, Pantagruel) est un auteur humaniste de la Renaissance, au XVIe siècle."),
  Q("Qui a écrit « Les Fleurs du mal » (1857) ?", ["Victor Hugo", "Charles Baudelaire", "Arthur Rimbaud", "Paul Verlaine"], "Charles Baudelaire", "Baudelaire publie Les Fleurs du mal en 1857 ; le recueil est condamné pour atteinte aux bonnes mœurs."),
]),
notion('F35', 0, I, 'f-lexique-roman', [
  Q("Comment appelle-t-on un récit dont le narrateur est aussi un personnage de l'histoire ?", ["Un récit à la 3e personne", "Un récit à la 1re personne", "Un récit omniscient", "Un récit théâtral"], "Un récit à la 1re personne", "Le narrateur-personnage raconte avec « je » ; dans une autobiographie, il se confond même avec l'auteur."),
  Q("Quand le narrateur sait tout des personnages, de leurs pensées et de leur passé, on parle de focalisation…", ["interne", "externe", "zéro (omnisciente)", "réduite"], "zéro (omnisciente)", "En focalisation zéro, le narrateur omniscient connaît tout. En focalisation interne, on suit le point de vue d'un personnage."),
  Q("Comment appelle-t-on le personnage principal d'un roman ?", ["L'antagoniste", "Le protagoniste", "Le narrataire", "Le figurant"], "Le protagoniste", "Le protagoniste est le personnage central ; l'antagoniste s'oppose à lui."),
]),
notion('F56', 0, I, 'f-registres-langue', [
  Q("Quelle phrase relève du registre soutenu ?", ["J'ai pas compris.", "Je n'ai pas compris.", "Je n'ai point saisi votre propos.", "J'ai rien capté."], "Je n'ai point saisi votre propos.", "Vocabulaire recherché et tournure littéraire (« point ») : registre soutenu."),
  Q("Quelle marque est caractéristique du registre familier à l'oral ?", ["L'inversion du sujet dans les questions", "La suppression du « ne » de la négation", "L'usage du passé simple", "Le vocabulaire technique"], "La suppression du « ne » de la négation", "« J'sais pas » au lieu de « je ne sais pas » : l'omission du « ne » est typique du registre familier."),
  Q("Quelle question est formulée dans un registre soutenu ?", ["Tu viens ?", "Est-ce que tu viens ?", "Viendras-tu ?", "Tu viens ou quoi ?"], "Viendras-tu ?", "L'inversion du sujet est la tournure la plus soutenue ; « est-ce que » est courant, l'intonation seule est familière."),
]),
notion('F48', 1, I, 'f-orthographe-radicaux', [
  Q("Quelle forme du conditionnel présent est correcte ?", ["Je courirais", "Je courrais", "Je courais", "Je courerais"], "Je courrais", "Au conditionnel, « courir » prend deux r (courr-) : je courrais. « Je courais » est l'imparfait."),
  Q("Quelle forme est correcte au subjonctif présent ?", ["Que nous voyons", "Que nous voyions", "Que nous voyons-nous", "Que nous voierons"], "Que nous voyions", "Au subjonctif comme à l'imparfait, on écrit -yions : que nous voyions."),
  Q("Quelle forme du futur est correcte ?", ["Il enverra", "Il envoiera", "Il envoyera", "Il enverrera"], "Il enverra", "« Envoyer » a un futur irrégulier : j'enverrai, il enverra."),
]),
notion('F52', 1, I, 'f-distinguer-fonctions', [
  Q("Dans « Il ressemble à son père », quelle est la fonction de « à son père » ?", ["COD", "COI", "Complément circonstanciel de lieu", "Attribut du sujet"], "COI", "« Ressembler à quelqu'un » : le complément, introduit par « à » et non supprimable, est un COI."),
  Q("Dans « Il travaille à Lyon depuis un an », quelle est la fonction de « à Lyon » ?", ["COI", "Complément circonstanciel de lieu", "COD", "Complément du nom"], "Complément circonstanciel de lieu", "« À Lyon » indique le lieu et peut être supprimé ou déplacé (« À Lyon, il travaille… ») : c'est un complément circonstanciel, pas un COI malgré la préposition."),
  C("Cliquez sur tous les mots du COD.", "Le directeur a nommé [Julie] responsable du projet.", "« A nommé qui ? Julie » : COD. « Responsable du projet » est attribut du COD : il caractérise Julie."),
  Q("Dans « Elle est devenue médecin », quelle est la fonction de « médecin » ?", ["COD", "Attribut du sujet", "Complément du nom", "Apposition"], "Attribut du sujet", "Après le verbe d'état « devenir », « médecin » caractérise le sujet : c'est un attribut, pas un COD."),
]),
notion('F44', 1, I, 'f-suffixation', [
  Q("Quel nom est formé à partir de l'adjectif « rapide » ?", ["Rapidité", "Rapidement", "Rapider", "Rapidesse"], "Rapidité", "Le suffixe -ité forme des noms de qualité à partir d'adjectifs : rapide → rapidité. « Rapidement » est un adverbe."),
  Q("Quel suffixe permet de former un nom d'action à partir du verbe « arroser » ?", ["-age", "-able", "-ette", "-iste"], "-age", "Arroser → arrosage : le suffixe -age forme des noms d'action (lavage, nettoyage)."),
  Q("Quel adverbe est correctement formé à partir de « prudent » ?", ["Prudentement", "Prudemment", "Prudament", "Prudement"], "Prudemment", "Les adjectifs en -ent donnent des adverbes en -emment (prudent → prudemment) ; ceux en -ant donnent -amment (savant → savamment)."),
]),
]

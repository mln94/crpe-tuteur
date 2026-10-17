from qlib import Q, N, C, notion
F = 'facile'
NOTIONS = [
notion('F52', 1, F, 'f-sujet', [
  C("Cliquez sur le sujet du verbe « aboie ».", "Chaque soir, [le chien du voisin] aboie.", "Le sujet répond à « Qui est-ce qui aboie ? » : le chien du voisin. On peut l'encadrer par « c'est… qui »."),
  C("Cliquez sur le sujet du verbe « arrivent ».", "Au printemps arrivent [les hirondelles].", "Le sujet est ici inversé, placé après le verbe : « Qui est-ce qui arrive ? Les hirondelles. » Le verbe s'accorde avec lui."),
  C("Cliquez sur le sujet du verbe « jouent ».", "[Mes cousins] jouent dans le jardin.", "« C'est mes cousins qui jouent » : le groupe nominal « mes cousins » est sujet."),
]),
notion('F52', 1, F, 'f-cod', [
  C("Cliquez sur tous les mots du complément d'objet direct (COD).", "Le facteur apporte [une lettre] chaque matin.", "Le COD complète le verbe sans préposition : « apporte quoi ? une lettre ». Il ne peut ni être supprimé ni déplacé."),
  C("Cliquez sur tous les mots du COD.", "Les élèves lisent [un roman de Jules Verne].", "« Lisent quoi ? un roman de Jules Verne » : tout le groupe nominal est COD."),
  C("Cliquez sur le COD.", "Le jardinier [les] arrose tous les jours.", "Le pronom « les » est COD du verbe « arrose » : il remplace un groupe nominal (les plantes) et se place avant le verbe."),
]),
notion('F52', 1, F, 'f-coi', [
  C("Cliquez sur tous les mots du complément d'objet indirect (COI).", "Elle pense souvent [à son enfance].", "Le COI complète le verbe et est introduit par une préposition : « penser à quelque chose »."),
  C("Cliquez sur tous les mots du COI.", "Ce livre appartient [à ma sœur].", "« Appartenir à quelqu'un » : le groupe introduit par la préposition « à » est complément d'objet indirect."),
  C("Cliquez sur tous les mots du COI.", "Nous parlons [de nos vacances].", "« Parler de quelque chose » : le COI est introduit par la préposition « de »."),
]),
notion('F52', 1, F, 'f-attribut-sujet', [
  C("Cliquez sur l'attribut du sujet.", "Ce gâteau semble [délicieux].", "Après un verbe d'état (sembler), l'attribut donne une caractéristique du sujet et s'accorde avec lui."),
  C("Cliquez sur tous les mots de l'attribut du sujet.", "Mon frère deviendra [un grand musicien].", "« Devenir » est un verbe attributif : « un grand musicien » caractérise le sujet « mon frère »."),
  C("Cliquez sur l'attribut du sujet.", "Les rues étaient [désertes].", "Après le verbe être, « désertes » qualifie le sujet « les rues » : c'est un attribut du sujet."),
]),
notion('F52', 1, F, 'f-cc-lieu', [
  C("Cliquez sur tous les mots du complément circonstanciel de lieu.", "Les enfants jouent [dans la cour].", "« Où jouent-ils ? Dans la cour. » Ce complément peut être déplacé ou supprimé : c'est un complément circonstanciel."),
  C("Cliquez sur tous les mots du complément circonstanciel de lieu.", "[Sous le pont], un pêcheur attendait.", "Le groupe « sous le pont » indique le lieu et peut être déplacé en fin de phrase."),
  C("Cliquez sur le complément circonstanciel de lieu.", "Nous dînerons [ici] ce soir.", "L'adverbe « ici » indique le lieu : il est complément circonstanciel de lieu."),
]),
notion('F52', 1, F, 'f-cc-temps', [
  C("Cliquez sur tous les mots du complément circonstanciel de temps.", "[Le lendemain], ils partirent en voiture.", "« Quand partirent-ils ? Le lendemain. » Ce groupe, déplaçable et supprimable, indique le temps."),
  C("Cliquez sur tous les mots du complément circonstanciel de temps.", "Le magasin ferme [à dix-neuf heures].", "« Quand ferme-t-il ? À dix-neuf heures. »"),
  C("Cliquez sur le complément circonstanciel de temps.", "Elle viendra [demain].", "L'adverbe « demain » indique le moment de l'action."),
]),
notion('F52', 4, F, 'f-determinant-pronom', [
  Q("Dans « Je le vois », quelle est la nature de « le » ?", ["Déterminant", "Pronom", "Préposition", "Adverbe"], "Pronom", "« Le » est placé devant un verbe et remplace un nom : c'est un pronom personnel. Devant un nom (« le livre »), ce serait un déterminant."),
  Q("Dans « Leur maison est grande », quelle est la nature de « leur » ?", ["Pronom personnel", "Déterminant possessif", "Adverbe", "Préposition"], "Déterminant possessif", "« Leur » précède le nom « maison » : c'est un déterminant possessif (il prend un -s au pluriel : leurs maisons)."),
  Q("Dans « Je leur ai écrit », quelle est la nature de « leur » ?", ["Déterminant possessif", "Pronom personnel", "Nom", "Conjonction"], "Pronom personnel", "Placé devant le verbe, « leur » remplace « à eux » : c'est un pronom personnel, toujours invariable."),
]),
notion('F52', 3, F, 'f-adverbe', [
  C("Cliquez sur l'adverbe.", "Le train roule [lentement].", "« Lentement » modifie le verbe « roule » et est invariable : c'est un adverbe (souvent formé avec le suffixe -ment)."),
  C("Cliquez sur l'adverbe.", "Ce film est [très] long.", "« Très » modifie l'adjectif « long » et est invariable : c'est un adverbe d'intensité."),
  C("Cliquez sur l'adverbe.", "Il est [déjà] parti.", "« Déjà » est un adverbe de temps : il est invariable et modifie le verbe."),
]),
notion('F52', 3, F, 'f-preposition', [
  C("Cliquez sur la préposition.", "Le chat dort [sur] le canapé.", "« Sur » relie le verbe à son complément « le canapé » : c'est une préposition, mot invariable."),
  C("Cliquez sur la préposition.", "Elle est partie [sans] son manteau.", "« Sans » introduit le groupe « son manteau » : c'est une préposition."),
  C("Cliquez sur la préposition.", "Il travaille [pour] gagner sa vie.", "« Pour » introduit ici un infinitif : c'est une préposition."),
]),
notion('F52', 6, F, 'f-coordination', [
  Q("Quel mot est une conjonction de coordination ?", ["Quand", "Mais", "Parce que", "Très"], "Mais", "Les conjonctions de coordination sont mais, ou, et, donc, or, ni, car. « Quand » et « parce que » sont des subordonnants."),
  Q("Dans « Il pleut, donc je reste », quel lien logique exprime « donc » ?", ["La cause", "La conséquence", "L'opposition", "Le temps"], "La conséquence", "« Donc » introduit la conséquence de la pluie : je reste."),
  Q("Dans « Je reste, car il pleut », quel lien logique exprime « car » ?", ["La cause", "La conséquence", "Le but", "La condition"], "La cause", "« Car » introduit l'explication, la cause : il pleut."),
]),
notion('F49', 1, F, 'f-types-phrases', [
  Q("« Ferme la porte. » Quel est le type de cette phrase ?", ["Déclaratif", "Interrogatif", "Injonctif", "Exclamatif"], "Injonctif", "Elle donne un ordre, avec un verbe à l'impératif : c'est une phrase injonctive (ou impérative)."),
  Q("« Viendras-tu demain ? » Quel est le type de cette phrase ?", ["Déclaratif", "Interrogatif", "Injonctif", "Négatif"], "Interrogatif", "Elle pose une question (inversion du sujet et point d'interrogation) : c'est une phrase interrogative."),
  Q("Combien existe-t-il de types de phrases ?", ["Deux", "Trois", "Quatre", "Cinq"], "Trois", "Il y a trois types : déclaratif, interrogatif, injonctif. L'exclamation, comme la négation, est une forme de phrase."),
]),
notion('F49', 2, F, 'f-formes-phrases', [
  Q("« Je ne mange jamais de viande. » Quelle est la forme de cette phrase ?", ["Affirmative", "Négative", "Exclamative", "Interrogative"], "Négative", "La négation « ne… jamais » encadre le verbe : la phrase est à la forme négative."),
  Q("« Quelle belle journée ! » Cette phrase est…", ["de forme exclamative", "de type interrogatif", "de forme négative", "de type injonctif"], "de forme exclamative", "Elle exprime une émotion et se termine par un point d'exclamation : c'est la forme exclamative."),
  Q("Quelle phrase est à la forme négative ?", ["Il part toujours tôt.", "Personne n'est venu.", "Quel temps !", "Viens ici."], "Personne n'est venu.", "« Personne… ne » forme une négation, même sans « pas »."),
]),
notion('F49', 3, F, 'f-phrase-simple-complexe', [
  Q("« Le soleil brille et les oiseaux chantent. » Cette phrase est…", ["simple", "complexe", "non verbale", "nominale"], "complexe", "Elle contient deux verbes conjugués (brille, chantent), donc deux propositions : c'est une phrase complexe."),
  Q("« Silence ! » Cette phrase est…", ["simple", "complexe", "non verbale", "interrogative"], "non verbale", "Elle ne contient aucun verbe conjugué : c'est une phrase non verbale (ou nominale)."),
  Q("Combien de propositions y a-t-il dans « Quand il pleut, je prends mon parapluie » ?", ["Une", "Deux", "Trois", "Aucune"], "Deux", "Il y a deux verbes conjugués (pleut, prends) : deux propositions, une subordonnée et une principale."),
]),
notion('F52', 2, F, 'f-nom-noyau', [
  C("Cliquez sur le nom noyau du groupe nominal.", "La petite [maison] de pierre", "Le nom principal, que les autres mots complètent, est « maison » : « petite » et « de pierre » sont ses expansions."),
  C("Cliquez sur le nom noyau du groupe nominal.", "Un vieux [pêcheur] aux mains calleuses", "« Pêcheur » est le nom principal ; « vieux » et « aux mains calleuses » sont ses expansions."),
  C("Cliquez sur le nom noyau du groupe nominal.", "Les [feuilles] mortes du jardin", "Le noyau est « feuilles » : « mortes » (adjectif) et « du jardin » (complément du nom) l'enrichissent."),
]),
notion('F52', 2, F, 'f-epithete', [
  C("Cliquez sur l'adjectif épithète.", "Elle porte une robe [rouge].", "« Rouge » est placé à côté du nom « robe » sans verbe intermédiaire : il est épithète."),
  C("Cliquez sur l'adjectif épithète.", "Un [immense] nuage couvrait la vallée.", "« Immense » qualifie directement le nom « nuage » : c'est un adjectif épithète."),
  C("Cliquez sur l'adjectif épithète.", "Le chien est content de son os [énorme].", "« Énorme » est directement lié au nom « os ». « Content », lui, est attribut du sujet, car il suit le verbe être."),
]),
notion('F37', 0, F, 'f-synonymes', [
  Q("Quel mot est un synonyme de « rapide » ?", ["Lent", "Véloce", "Lourd", "Calme"], "Véloce", "Des synonymes ont un sens proche : véloce signifie rapide. « Lent » est un antonyme."),
  Q("Quel mot est un synonyme de « effrayé » ?", ["Apeuré", "Rassuré", "Joyeux", "Fatigué"], "Apeuré", "Apeuré et effrayé désignent tous deux le fait d'avoir peur."),
  Q("Dans « Il a ôté son chapeau », par quel mot peut-on remplacer « ôté » ?", ["Mis", "Retiré", "Acheté", "Porté"], "Retiré", "Ôter signifie enlever, retirer."),
]),
notion('F37', 0, F, 'f-antonymes', [
  Q("Quel est l'antonyme de « généreux » ?", ["Avare", "Gentil", "Prodigue", "Riche"], "Avare", "Un antonyme a un sens contraire : l'avare garde son argent, le généreux le donne."),
  Q("Quel est l'antonyme de « augmenter » ?", ["Accroître", "Diminuer", "Ajouter", "Multiplier"], "Diminuer", "Augmenter et diminuer ont des sens contraires."),
  Q("Quel préfixe permet de former l'antonyme de « possible » ?", ["re-", "im-", "pré-", "sur-"], "im-", "Le préfixe négatif in- devient im- devant p, b ou m : impossible."),
]),
notion('F37', 1, F, 'f-famille-mots', [
  Q("Quel mot n'appartient pas à la famille de « terre » ?", ["Terrain", "Enterrer", "Terrible", "Terrestre"], "Terrible", "« Terrible » vient du latin terror (la peur) et non de terra : il ressemble aux autres mais n'est pas de la même famille."),
  Q("Quel mot appartient à la famille de « dent » ?", ["Dentiste", "Danse", "Dense", "Ardent"], "Dentiste", "Dentiste est formé sur le radical dent-. Les autres mots n'ont qu'une ressemblance de forme."),
  Q("Quels mots forment une famille ?", ["Chanter, chanson, chanteur", "Chanter, champ, chance", "Chant, chat, chaud", "Chanteur, chandail, chantier"], "Chanter, chanson, chanteur", "Une famille de mots partage le même radical et un sens commun : ici, l'idée de chanter."),
]),
notion('F43', 1, F, 'f-prefixes', [
  Q("Quel est le sens du préfixe « re- » dans « relire » ?", ["Le contraire", "La répétition", "L'avant", "L'excès"], "La répétition", "Relire, c'est lire de nouveau : re- marque la répétition."),
  Q("Quel est le sens du préfixe « pré- » dans « préhistoire » ?", ["Après", "Avant", "Contre", "Avec"], "Avant", "La préhistoire est la période qui précède l'histoire : pré- signifie avant."),
  Q("Quel est le sens du préfixe « anti- » dans « antivol » ?", ["Contre", "Avant", "À nouveau", "Très"], "Contre", "Un antivol protège contre le vol : anti- signifie contre."),
]),
notion('F43', 1, F, 'f-suffixes', [
  Q("Quel sens apporte le suffixe « -able » dans « lavable » ?", ["Qui lave", "Qui peut être lavé", "Qui a été lavé", "Le fait de laver"], "Qui peut être lavé", "Le suffixe -able exprime la possibilité : lavable, buvable, mangeable."),
  Q("Quel sens apporte le suffixe « -ette » dans « maisonnette » ?", ["La grandeur", "La petitesse", "La profession", "Le lieu"], "La petitesse", "-ette est un suffixe diminutif : une maisonnette est une petite maison."),
  Q("Quel suffixe désigne souvent une profession ?", ["-ier", "-able", "-ment", "-ette"], "-ier", "Boulanger, pâtissier, menuisier : -ier (et -er) désigne souvent un métier."),
]),
notion('F34', 0, F, 'f-sens-contexte', [
  Q("Dans « Il a une mémoire d'éléphant », que signifie l'expression ?", ["Il est lourd", "Il a une très bonne mémoire", "Il oublie tout", "Il aime les animaux"], "Il a une très bonne mémoire", "L'éléphant est réputé ne rien oublier : l'expression signifie avoir une excellente mémoire."),
  Q("Dans « La séance est levée », que signifie « levée » ?", ["Soulevée", "Terminée", "Commencée", "Annulée à l'avance"], "Terminée", "Lever une séance, c'est y mettre fin : le contexte donne le sens du mot."),
  Q("Dans « Le chef a donné le feu vert », que signifie « le feu vert » ?", ["Un incendie", "Une autorisation", "Un signal routier uniquement", "Un refus"], "Une autorisation", "Au sens figuré, donner le feu vert, c'est autoriser."),
]),
notion('F40', 1, F, 'f-registres', [
  Q("À quel registre appartient le mot « bagnole » ?", ["Soutenu", "Courant", "Familier", "Littéraire"], "Familier", "« Bagnole » est familier ; « voiture » est courant ; « automobile » ou « véhicule » sont plus soutenus."),
  Q("Quel mot appartient au registre soutenu ?", ["Bouquin", "Livre", "Ouvrage", "Truc"], "Ouvrage", "« Ouvrage » est soutenu, « livre » courant, « bouquin » familier."),
  Q("Quelle phrase est au registre courant ?", ["J'ai la flemme.", "Je suis fatigué.", "Je suis las.", "Je suis crevé."], "Je suis fatigué.", "« Fatigué » est courant, « las » soutenu, « crevé » et « avoir la flemme » familiers."),
]),
notion('F47', 2, F, 'f-homophones-a', [
  Q("Complétez : « Il … faim. »", ["a", "à"], "a", "On peut remplacer par « avait » : c'est le verbe avoir, sans accent."),
  Q("Complétez : « Je vais … la piscine. »", ["a", "à"], "à", "On ne peut pas dire « je vais avait la piscine » : c'est la préposition « à »."),
  Q("Complétez : « Elle … oublié son sac … la maison. »", ["a / à", "à / a", "a / a", "à / à"], "a / à", "« Elle avait oublié » : verbe avoir (a) ; « à la maison » : préposition (à)."),
]),
notion('F47', 2, F, 'f-homophones-et-est', [
  Q("Complétez : « Le ciel … bleu. »", ["et", "est"], "est", "On peut remplacer par « était » : c'est le verbe être."),
  Q("Complétez : « Paul … Marie sont amis. »", ["et", "est"], "et", "On peut remplacer par « et puis » : c'est la conjonction de coordination."),
  Q("Complétez : « Ce film … long … ennuyeux. »", ["est / et", "et / est", "est / est", "et / et"], "est / et", "« Ce film était long » (verbe être), puis « et ennuyeux » (conjonction)."),
]),
notion('F47', 2, F, 'f-homophones-son-sont', [
  Q("Complétez : « Ils … partis tôt. »", ["son", "sont"], "sont", "On peut remplacer par « étaient » : c'est le verbe être."),
  Q("Complétez : « Il a perdu … cartable. »", ["son", "sont"], "son", "On peut remplacer par « mon » : c'est le déterminant possessif."),
  Q("Complétez : « Ses amis … venus avec … chien. »", ["sont / son", "son / sont", "sont / sont", "son / son"], "sont / son", "« Ses amis étaient venus » (verbe être) ; « avec mon chien » (déterminant possessif)."),
]),
notion('F48', 2, F, 'f-homophones-ces-ses', [
  Q("Complétez : « Il range … affaires. » (les siennes)", ["ses", "ces", "c'est", "s'est"], "ses", "On peut dire « ses affaires à lui » : c'est le déterminant possessif."),
  Q("Complétez : « … arbres sont centenaires. » (ceux-là)", ["Ses", "Ces", "C'est", "S'est"], "Ces", "On peut dire « ces arbres-là » : c'est le déterminant démonstratif."),
  Q("Complétez : « Il … blessé en tombant. »", ["ses", "ces", "c'est", "s'est"], "s'est", "C'est le verbe pronominal « se blesser » au passé composé : il s'est blessé (on peut dire « je me suis blessé »)."),
]),
notion('F47', 2, F, 'f-homophones-ou-ou', [
  Q("Complétez : « … habites-tu ? »", ["Ou", "Où"], "Où", "Il s'agit du lieu : « où » prend un accent. On ne peut pas le remplacer par « ou bien »."),
  Q("Complétez : « Tu préfères le thé … le café ? »", ["ou", "où"], "ou", "On peut dire « ou bien » : c'est la conjonction de coordination, sans accent."),
  Q("Complétez : « Le jour … il est né, il neigeait. »", ["ou", "où"], "où", "« Où » est ici un pronom relatif qui reprend « le jour » (sens temporel) : il prend un accent."),
]),
notion('F61', 1, F, 'f-temps-imparfait', [
  Q("À quel temps est conjugué « nous chantions » ?", ["Présent", "Imparfait", "Passé simple", "Futur"], "Imparfait", "Les terminaisons -ions, -iez, -ais, -ait, -aient marquent l'imparfait de l'indicatif."),
  Q("Quelle est la forme de « finir » à l'imparfait, 3e personne du pluriel ?", ["Ils finissent", "Ils finissaient", "Ils finirent", "Ils finiront"], "Ils finissaient", "Imparfait : radical finiss- + terminaison -aient."),
  Q("À quel temps est « tu voyais » ?", ["Présent", "Futur", "Imparfait", "Conditionnel présent"], "Imparfait", "Radical voy- + terminaison -ais : imparfait. Au conditionnel, on aurait « tu verrais »."),
]),
notion('F61', 1, F, 'f-temps-futur', [
  Q("À quel temps est conjugué « ils viendront » ?", ["Futur simple", "Conditionnel présent", "Passé simple", "Présent"], "Futur simple", "Radical viendr- + terminaison -ont : futur simple de l'indicatif."),
  Q("Quelle est la forme de « aller » au futur simple, 1re personne du singulier ?", ["J'allerai", "J'irai", "J'irais", "J'allais"], "J'irai", "« Aller » a un radical irrégulier au futur : j'irai. « J'irais » est le conditionnel."),
  Q("Quelle forme est au futur simple ?", ["Nous serions", "Nous serons", "Nous étions", "Nous fûmes"], "Nous serons", "Terminaison -ons sans -i- : futur. « Nous serions » est au conditionnel présent."),
]),
notion('F61', 1, F, 'f-temps-passe-simple', [
  Q("À quel temps est conjugué « il chanta » ?", ["Imparfait", "Passé simple", "Futur", "Passé composé"], "Passé simple", "Terminaison -a à la 3e personne des verbes en -er : passé simple."),
  Q("Quelle est la forme de « prendre » au passé simple, 3e personne du singulier ?", ["Il prenait", "Il prit", "Il prendra", "Il a pris"], "Il prit", "Passé simple de prendre : il prit."),
  Q("Quelle forme est au passé simple ?", ["Ils finirent", "Ils finissaient", "Ils finiront", "Ils finissent"], "Ils finirent", "Terminaison -irent : passé simple des verbes du 2e groupe."),
]),
notion('F61', 1, F, 'f-temps-passe-compose', [
  Q("À quel temps est « nous avons mangé » ?", ["Plus-que-parfait", "Passé composé", "Passé simple", "Futur antérieur"], "Passé composé", "Auxiliaire au présent (avons) + participe passé : passé composé."),
  Q("Quel auxiliaire utilise-t-on pour « partir » au passé composé ?", ["Avoir", "Être", "Les deux selon le sens", "Aucun"], "Être", "« Je suis parti » : partir, comme la plupart des verbes de mouvement, se conjugue avec être."),
  Q("Quelle forme est au passé composé ?", ["Elle était venue", "Elle est venue", "Elle vint", "Elle viendrait"], "Elle est venue", "Être au présent + participe : passé composé. « Était venue » est au plus-que-parfait."),
]),
notion('F61', 3, F, 'f-conjugaison-present', [
  Q("Quelle est la forme correcte de « faire » au présent, 2e personne du pluriel ?", ["Vous faisez", "Vous faites", "Vous fesez", "Vous faitez"], "Vous faites", "« Faire » est irrégulier : vous faites (comme vous êtes, vous dites)."),
  Q("Quelle est la forme correcte de « prendre » au présent, 3e personne du pluriel ?", ["Ils prendent", "Ils prennent", "Ils prenent", "Ils prendrent"], "Ils prennent", "Le radical change au pluriel : nous prenons, ils prennent (deux n)."),
  Q("Quelle est la forme correcte de « appeler » au présent, 1re personne du singulier ?", ["J'appele", "J'appelle", "J'apelle", "J'appelles"], "J'appelle", "Devant un e muet, appeler double le l : j'appelle, mais nous appelons."),
]),
notion('F61', 0, F, 'f-groupes-verbes', [
  Q("À quel groupe appartient le verbe « finir » ?", ["1er groupe", "2e groupe", "3e groupe", "Aucun"], "2e groupe", "Les verbes du 2e groupe se terminent par -ir et font -issons au présent : nous finissons."),
  Q("À quel groupe appartient le verbe « partir » ?", ["1er groupe", "2e groupe", "3e groupe", "Auxiliaire"], "3e groupe", "Nous partons (et non partissons) : partir est du 3e groupe."),
  Q("Quel verbe appartient au 1er groupe ?", ["Aller", "Chanter", "Venir", "Courir"], "Chanter", "Le 1er groupe réunit les verbes en -er, sauf « aller », qui est du 3e groupe."),
]),
notion('F64', 1, F, 'f-imperatif', [
  Q("Quelle est la forme correcte de « manger » à l'impératif, 2e personne du singulier ?", ["Manges ta soupe", "Mange ta soupe", "Mangez ta soupe", "Mangeas ta soupe"], "Mange ta soupe", "À l'impératif, les verbes en -er ne prennent pas de -s à la 2e personne du singulier (sauf devant en et y)."),
  Q("Combien de personnes compte l'impératif ?", ["Une", "Deux", "Trois", "Six"], "Trois", "L'impératif se conjugue à trois personnes, sans sujet exprimé : mange, mangeons, mangez."),
  Q("Quelle est la forme correcte ?", ["Vas-y !", "Va-y !", "Vas y !", "Va y !"], "Vas-y !", "Devant « y » ou « en », on ajoute un -s pour la liaison : vas-y, manges-en."),
]),
notion('F67', 0, F, 'f-accord-gn', [
  Q("Quelle est la forme correcte ?", ["des fleurs blanche", "des fleurs blanches", "des fleur blanches", "des fleurs blanchent"], "des fleurs blanches", "Dans le groupe nominal, le déterminant, le nom et l'adjectif s'accordent en genre et en nombre."),
  Q("Quelle est la forme correcte ?", ["de beaux jours ensoleillé", "de beaux jours ensoleillés", "de beau jours ensoleillés", "de beaus jours ensoleillés"], "de beaux jours ensoleillés", "Masculin pluriel : beaux (pluriel en -x) et ensoleillés (-s)."),
  Q("Quelle est la forme correcte ?", ["une veste et un pantalon noir", "une veste et un pantalon noirs", "une veste et un pantalon noires", "une veste et un pantalons noirs"], "une veste et un pantalon noirs", "Si l'adjectif qualifie les deux noms, il se met au pluriel ; avec un nom masculin et un féminin, il est au masculin."),
]),
notion('F67', 2, F, 'f-accord-sujet-verbe', [
  Q("Quelle phrase est correcte ?", ["Les enfants du village joue.", "Les enfants du village jouent.", "Les enfants du village jouet.", "Les enfants du village joues."], "Les enfants du village jouent.", "Le sujet est « les enfants » (pluriel), et non « village » : le verbe s'accorde avec le noyau du sujet."),
  Q("Quelle phrase est correcte ?", ["Toi et moi partirons.", "Toi et moi partiront.", "Toi et moi partira.", "Toi et moi partirez."], "Toi et moi partirons.", "« Toi et moi » équivaut à « nous » : le verbe se met à la 1re personne du pluriel."),
  Q("Quelle phrase est correcte ?", ["Le bruit des voitures me gênent.", "Le bruit des voitures me gêne.", "Le bruit des voitures me gênes.", "Le bruit des voitures me gêner."], "Le bruit des voitures me gêne.", "Le sujet est « le bruit » (singulier) ; « des voitures » n'est qu'un complément du nom."),
]),
notion('F67', 3, F, 'f-pp-etre', [
  Q("Quelle phrase est correcte ?", ["Elles sont arrivé hier.", "Elles sont arrivées hier.", "Elles sont arrivés hier.", "Elles sont arriver hier."], "Elles sont arrivées hier.", "Avec l'auxiliaire être, le participe passé s'accorde avec le sujet : elles (féminin pluriel) → arrivées."),
  Q("Quelle phrase est correcte ?", ["La porte a été fermé.", "La porte a été fermée.", "La porte a été fermer.", "La porte a été fermés."], "La porte a été fermée.", "À la voix passive, le participe s'accorde avec le sujet « la porte »."),
  Q("Quelle phrase est correcte ?", ["Nous sommes partis tôt, mes frères et moi.", "Nous sommes parti tôt, mes frères et moi.", "Nous sommes partie tôt, mes frères et moi.", "Nous sommes partit tôt, mes frères et moi."], "Nous sommes partis tôt, mes frères et moi.", "« Nous » désigne ici plusieurs garçons : participe au masculin pluriel."),
]),
notion('F67', 4, F, 'f-verbes-attributifs', [
  Q("Lequel de ces verbes est un verbe attributif (verbe d'état) ?", ["Manger", "Sembler", "Courir", "Donner"], "Sembler", "Les verbes d'état (être, sembler, paraître, devenir, demeurer, rester…) introduisent un attribut du sujet."),
  Q("Dans « Il reste calme », quelle est la fonction de « calme » ?", ["COD", "Attribut du sujet", "Complément circonstanciel", "Épithète"], "Attribut du sujet", "« Rester » est ici un verbe d'état : « calme » caractérise le sujet."),
  Q("Dans quelle phrase « paraître » est-il un verbe d'état ?", ["Le livre paraîtra en mai.", "Elle paraît fatiguée.", "Le soleil paraît à l'horizon.", "Ce journal paraît chaque jour."], "Elle paraît fatiguée.", "« Paraître fatiguée » : on peut remplacer par « être fatiguée ». Dans les autres phrases, paraître signifie être publié ou apparaître."),
]),
notion('F58', 0, F, 'f-discours-direct-indirect', [
  Q("« Il a dit : « Je suis fatigué. » » Ces paroles sont rapportées…", ["au discours direct", "au discours indirect", "au discours indirect libre", "sans paroles rapportées"], "au discours direct", "Les paroles sont citées telles quelles, entre guillemets, après deux-points : c'est le discours direct."),
  Q("« Il a dit qu'il était fatigué. » Ces paroles sont rapportées…", ["au discours direct", "au discours indirect", "au style télégraphique", "au discours libre"], "au discours indirect", "Les paroles sont intégrées dans une subordonnée introduite par « que », sans guillemets : discours indirect."),
  Q("Quel signe de ponctuation introduit le plus souvent le discours direct ?", ["Le point-virgule", "Les deux-points", "Les points de suspension", "La virgule"], "Les deux-points", "Le discours direct est annoncé par les deux-points et encadré de guillemets (ou introduit par un tiret dans un dialogue)."),
]),
notion('F49', 0, F, 'f-ponctuation', [
  Q("Quel signe de ponctuation sépare les éléments d'une énumération ?", ["La virgule", "Le point", "Le point d'interrogation", "Les guillemets"], "La virgule", "Dans « des pommes, des poires, des prunes », les virgules séparent les éléments énumérés."),
  Q("À quoi servent les guillemets ?", ["À poser une question", "À encadrer des paroles rapportées ou une citation", "À finir une phrase", "À marquer une pause longue"], "À encadrer des paroles rapportées ou une citation", "Les guillemets signalent les paroles prononcées ou les mots empruntés à quelqu'un d'autre."),
  Q("Quelle phrase est correctement ponctuée ?", ["Le chat, dort.", "Le matin, le chat dort.", "Le, chat dort le matin.", "Le chat dort, le matin, le."], "Le matin, le chat dort.", "On ne sépare pas le sujet du verbe par une virgule ; en revanche, un complément placé en tête est souvent suivi d'une virgule."),
]),
notion('F52', 5, F, 'f-pronom-personnel', [
  C("Cliquez sur le pronom personnel.", "Le professeur [nous] explique la leçon.", "« Nous » remplace les personnes qui parlent et est complément du verbe « explique »."),
  C("Cliquez sur le pronom personnel sujet.", "Demain, [ils] partiront en voyage.", "« Ils » est un pronom personnel sujet de « partiront »."),
  C("Cliquez sur le pronom personnel.", "Cette histoire, je [la] connais par cœur.", "« La » remplace « cette histoire » : c'est un pronom personnel COD."),
]),
notion('F43', 2, F, 'f-etymologie', [
  Q("Que signifie la racine grecque « graphie » (dans orthographe, calligraphie) ?", ["Parler", "Écrire", "Voir", "Entendre"], "Écrire", "Graphein signifie écrire en grec : l'orthographe est l'art d'écrire correctement."),
  Q("Que signifie la racine grecque « bio » (dans biologie) ?", ["La terre", "La vie", "L'eau", "Le temps"], "La vie", "Bios signifie la vie : la biologie est la science du vivant."),
  Q("Que signifie la racine latine « aqua » (dans aquarium) ?", ["Le feu", "L'eau", "L'air", "La pierre"], "L'eau", "Aqua signifie l'eau en latin : aquatique, aquarium, aqueduc."),
]),
notion('F36', 1, F, 'f-comparaison', [
  Q("« Ses yeux brillent comme des étoiles. » Quelle figure de style est utilisée ?", ["Une métaphore", "Une comparaison", "Une personnification", "Une hyperbole"], "Une comparaison", "Le rapprochement entre les yeux et les étoiles est fait avec un outil de comparaison : « comme »."),
  Q("Quel mot est un outil de comparaison ?", ["Donc", "Tel", "Car", "Mais"], "Tel", "Comme, tel, pareil à, semblable à, ressembler à… sont des outils de comparaison."),
  Q("Quels sont les éléments d'une comparaison ?", ["Le comparé, l'outil, le comparant", "Le sujet, le verbe, le complément", "La cause, la conséquence", "Le thème et le propos"], "Le comparé, l'outil, le comparant", "Dans « ses yeux brillent comme des étoiles », ses yeux = comparé, comme = outil, des étoiles = comparant."),
]),
notion('F36', 1, F, 'f-metaphore', [
  Q("« Cet homme est un lion. » Quelle figure de style est utilisée ?", ["Une comparaison", "Une métaphore", "Une litote", "Une antithèse"], "Une métaphore", "Le rapprochement entre l'homme et le lion se fait sans outil de comparaison : c'est une métaphore."),
  Q("Qu'est-ce qui distingue la métaphore de la comparaison ?", ["La métaphore n'a pas d'outil de comparaison", "La métaphore n'a pas de comparé", "La métaphore est toujours exagérée", "Rien"], "La métaphore n'a pas d'outil de comparaison", "La métaphore rapproche deux réalités directement, sans « comme » ni « tel »."),
  Q("Quelle phrase contient une métaphore ?", ["Il est fort comme un bœuf.", "La vie est un long fleuve.", "Il court vite.", "Il ressemble à son père."], "La vie est un long fleuve.", "La vie est assimilée à un fleuve sans outil de comparaison : c'est une métaphore."),
]),
notion('F36', 1, F, 'f-personnification', [
  Q("« Le vent hurlait dans la nuit. » Quelle figure de style est utilisée ?", ["Une comparaison", "Une personnification", "Une litote", "Une énumération"], "Une personnification", "Le vent se voit attribuer une action humaine (hurler) : c'est une personnification."),
  Q("Qu'est-ce qu'une personnification ?", ["Attribuer des caractéristiques humaines à une chose ou un animal", "Exagérer une idée", "Dire moins pour suggérer plus", "Répéter un mot en début de vers"], "Attribuer des caractéristiques humaines à une chose ou un animal", "La personnification donne à un objet, un animal ou une idée des traits humains."),
  Q("Quelle phrase contient une personnification ?", ["La ville dort encore.", "La ville est grande.", "Il habite en ville.", "La ville compte un million d'habitants."], "La ville dort encore.", "Dormir est une action humaine attribuée à la ville."),
]),
notion('F35', 0, F, 'f-lexique-theatre', [
  Q("Au théâtre, comment appelle-t-on les indications de l'auteur sur les gestes, le ton ou le décor ?", ["Les répliques", "Les didascalies", "Les tirades", "Les apartés"], "Les didascalies", "Les didascalies, souvent en italique, ne sont pas prononcées par les comédiens."),
  Q("Comment appelle-t-on une longue réplique d'un personnage ?", ["Un aparté", "Une tirade", "Une stichomythie", "Une didascalie"], "Une tirade", "La tirade est une longue réplique ; le monologue, lui, est prononcé par un personnage seul en scène."),
  Q("Comment appelle-t-on les paroles qu'un personnage prononce pour lui-même, sans être entendu des autres personnages ?", ["Un aparté", "Un dialogue", "Une tirade", "Un prologue"], "Un aparté", "L'aparté est entendu du public mais pas des autres personnages présents."),
]),
notion('F36', 1, F, 'f-versification', [
  Q("Combien de syllabes compte un alexandrin ?", ["8", "10", "12", "14"], "12", "L'alexandrin est le vers de 12 syllabes, très utilisé dans la poésie et le théâtre classiques."),
  Q("Comment appelle-t-on une strophe de quatre vers ?", ["Un tercet", "Un quatrain", "Un distique", "Un sizain"], "Un quatrain", "Distique (2), tercet (3), quatrain (4), quintil (5), sizain (6)."),
  Q("Quelle est la forme d'un sonnet ?", ["Trois quatrains", "Deux quatrains et deux tercets", "Quatre tercets", "Un seul long paragraphe"], "Deux quatrains et deux tercets", "Le sonnet compte 14 vers : deux quatrains suivis de deux tercets."),
]),
notion('F10', 2, F, 'f-auteurs-oeuvres', [
  Q("Qui a écrit « Les Fables » mettant en scène des animaux, au XVIIe siècle ?", ["Molière", "Jean de La Fontaine", "Victor Hugo", "Charles Perrault"], "Jean de La Fontaine", "Jean de La Fontaine publie ses Fables entre 1668 et 1694."),
  Q("Qui a écrit « Les Misérables » ?", ["Émile Zola", "Victor Hugo", "Honoré de Balzac", "Gustave Flaubert"], "Victor Hugo", "Victor Hugo publie Les Misérables en 1862."),
  Q("Qui a écrit « Le Petit Prince » ?", ["Antoine de Saint-Exupéry", "Jules Verne", "Albert Camus", "Marcel Pagnol"], "Antoine de Saint-Exupéry", "Le Petit Prince d'Antoine de Saint-Exupéry paraît en 1943."),
]),
notion('F46', 0, F, 'f-orthographe-lexicale', [
  Q("Quelle orthographe est correcte ?", ["Un abri", "Un abrit", "Un abris", "Un habri"], "Un abri", "« Abri » s'écrit sans consonne finale, même si on pense à « abriter »."),
  Q("Quelle orthographe est correcte ?", ["Un apartement", "Un appartement", "Un appartemment", "Un apartemment"], "Un appartement", "Appartement prend deux p et un seul m."),
  Q("Quelle orthographe est correcte ?", ["Malgrè", "Malgré", "Malgrés", "Malgrais"], "Malgré", "« Malgré » se termine par un é accent aigu, sans s."),
]),
notion('F62', 2, F, 'f-participes-finales', [
  Q("Quelle est la forme correcte du participe passé de « prendre » au masculin singulier ?", ["Pri", "Pris", "Prit", "Prie"], "Pris", "Pensez au féminin : prise. La consonne finale muette est donc un -s : pris."),
  Q("Quelle est la forme correcte du participe passé de « faire » au masculin singulier ?", ["Fai", "Fais", "Fait", "Fé"], "Fait", "Au féminin on dit « faite » : le participe se termine donc par -t."),
  Q("Quelle est la forme correcte du participe passé de « finir » au masculin singulier ?", ["Fini", "Finit", "Finis", "Finie"], "Fini", "Au féminin, « finie » : pas de consonne muette, le masculin est « fini »."),
]),
]

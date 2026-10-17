from qlib import Q, N, C, notion
D = 'difficile'
NOTIONS = [
notion('F54', 0, D, 'f-completive', [
  Q("Dans « Je crois que tu as raison », quelle est la fonction de la subordonnée « que tu as raison » ?", ["Complément circonstanciel", "COD du verbe « crois »", "Complément de l'antécédent", "Sujet"], "COD du verbe « crois »", "Cette subordonnée conjonctive complétive complète le verbe « croire » : on peut la remplacer par « cela » (je crois cela). Elle est COD."),
  C("Cliquez sur tous les mots de la subordonnée complétive.", "Il est probable [qu'il pleuve ce soir].", "La complétive est introduite par la conjonction « que » ; elle complète l'expression « il est probable »."),
  Q("Comment distinguer « que » conjonction de « que » pronom relatif ?", ["Le pronom relatif a un antécédent qu'il reprend", "La conjonction est toujours en début de phrase", "Le pronom relatif est toujours sujet", "Il n'y a aucune différence"], "Le pronom relatif a un antécédent qu'il reprend", "Dans « le livre que je lis », « que » reprend « le livre » (relatif) ; dans « je sais que tu lis », il ne reprend rien (conjonction)."),
]),
notion('F51', 2, D, 'f-circonstancielle', [
  Q("Dans « Bien qu'il soit fatigué, il continue », quelle est la valeur de la subordonnée ?", ["Cause", "Concession (opposition)", "Condition", "But"], "Concession (opposition)", "« Bien que » + subjonctif introduit une concession : un fait qui aurait dû empêcher l'action principale."),
  Q("Dans « S'il fait beau, nous sortirons », quelle est la valeur de la subordonnée ?", ["Temps", "Condition (hypothèse)", "Cause", "Conséquence"], "Condition (hypothèse)", "« Si » introduit ici la condition de réalisation de l'action principale."),
  Q("Dans « Il parle fort pour qu'on l'entende », quelle est la valeur de la subordonnée ?", ["But", "Cause", "Conséquence", "Concession"], "But", "« Pour que » + subjonctif exprime le but, l'objectif visé."),
]),
notion('F50', 4, D, 'f-interrogative-indirecte', [
  Q("Quelle phrase contient une subordonnée interrogative indirecte ?", ["Je me demande s'il viendra.", "S'il vient, je partirai.", "Viendra-t-il ?", "Il viendra si tu l'invites."], "Je me demande s'il viendra.", "La subordonnée « s'il viendra » rapporte une question (interrogation totale) et est COD de « se demander »."),
  Q("Transformez en interrogative indirecte : « Où vas-tu ? » demande-t-il.", ["Il demande où vas-tu.", "Il demande où tu vas.", "Il demande si où tu vas.", "Il demande que tu vas où."], "Il demande où tu vas.", "Dans l'interrogative indirecte, il n'y a plus d'inversion du sujet ni de point d'interrogation."),
  Q("Dans « Dis-moi ce que tu penses », que introduit « ce que » ?", ["Une relative sans antécédent", "Une interrogative indirecte partielle", "Une circonstancielle", "Une complétive en que"], "Une interrogative indirecte partielle", "« Ce que » correspond à la question « Que penses-tu ? » rapportée : c'est une interrogative indirecte partielle."),
]),
notion('F51', 3, D, 'f-fonction-relatif', [
  Q("Dans « Le film dont tu m'as parlé est sorti », quelle est la fonction de « dont » dans la relative ?", ["Sujet", "COD", "COI du verbe « parler »", "Complément de lieu"], "COI du verbe « parler »", "On parle de quelque chose : « dont » remplace « de ce film » et est COI de « as parlé »."),
  Q("Dans « La maison que j'ai achetée est ancienne », quelle est la fonction de « que » dans la relative ?", ["Sujet", "COD de « ai achetée »", "Attribut", "COI"], "COD de « ai achetée »", "J'ai acheté quoi ? la maison, reprise par « que » : COD, ce qui explique l'accord « achetée »."),
  Q("Dans « Voici l'ami avec qui je voyage », quelle est la fonction de « avec qui » ?", ["Sujet", "COD", "Complément circonstanciel d'accompagnement", "Attribut"], "Complément circonstanciel d'accompagnement", "Je voyage avec cet ami : le groupe prépositionnel relatif exprime l'accompagnement."),
]),
notion('F51', 1, D, 'f-emphase', [
  Q("Quelle phrase est de forme emphatique ?", ["Pierre a cassé le vase.", "C'est Pierre qui a cassé le vase.", "Le vase a été cassé.", "Pierre n'a pas cassé le vase."], "C'est Pierre qui a cassé le vase.", "L'extraction « c'est… qui » met en relief un élément de la phrase : c'est la forme emphatique."),
  Q("« Ce livre, je l'ai adoré. » Par quel procédé l'emphase est-elle obtenue ?", ["Extraction par « c'est… que »", "Détachement avec reprise par un pronom", "Passivation", "Négation"], "Détachement avec reprise par un pronom", "« Ce livre » est détaché en tête et repris par le pronom « l' » : c'est une dislocation (détachement)."),
  Q("Quel est l'effet principal de la forme emphatique ?", ["Nier une information", "Mettre un élément en relief", "Poser une question", "Atténuer le propos"], "Mettre un élément en relief", "L'emphase insiste sur un constituant, souvent pour l'opposer à un autre ou le souligner."),
]),
notion('F69', 2, D, 'f-pp-cas-complexes', [
  Q("Quelle phrase est correcte ?", ["Les efforts qu'il a fallus étaient immenses.", "Les efforts qu'il a fallu étaient immenses.", "Les efforts qu'il a fallue étaient immenses.", "Les efforts qu'il a fallut étaient immenses."], "Les efforts qu'il a fallu étaient immenses.", "Le participe passé des verbes impersonnels (falloir) reste toujours invariable."),
  Q("Quelle phrase est correcte ?", ["Des pommes, j'en ai mangées.", "Des pommes, j'en ai mangé.", "Des pommes, j'en ai mangés.", "Des pommes, j'en ai mangée."], "Des pommes, j'en ai mangé.", "Avec le pronom « en » placé avant, le participe passé reste en général invariable."),
  Q("Quelle phrase est correcte ?", ["Les chanteurs que j'ai entendus chanter étaient bons.", "Les chanteurs que j'ai entendu chanter étaient bons.", "Les chanteurs que j'ai entendue chanter étaient bons.", "Les chanteurs que j'ai entendus chantés étaient bons."], "Les chanteurs que j'ai entendus chanter étaient bons.", "Ce sont les chanteurs qui chantent : le COD « que » fait l'action de l'infinitif, on accorde le participe."),
  Q("Quelle phrase est correcte ?", ["Les trois heures qu'il a dormies l'ont reposé.", "Les trois heures qu'il a dormi l'ont reposé.", "Les trois heures qu'il a dormie l'ont reposé.", "Les trois heures qu'il a dormis l'ont reposé."], "Les trois heures qu'il a dormi l'ont reposé.", "« Que » est ici un complément de durée, pas un COD (on ne dort pas « quelque chose ») : pas d'accord."),
]),
notion('F68', 2, D, 'f-pp-pronominaux', [
  Q("Quelle phrase est correcte ?", ["Elles se sont lavées les mains.", "Elles se sont lavé les mains.", "Elles se sont lavés les mains.", "Elles se sont laver les mains."], "Elles se sont lavé les mains.", "Le COD est « les mains », placé après le verbe ; « se » est COI (laver les mains à soi) : pas d'accord."),
  Q("Quelle phrase est correcte ?", ["Elles se sont lavé.", "Elles se sont lavées.", "Elles se sont lavés.", "Elles se sont lavée."], "Elles se sont lavées.", "Ici « se » est COD (elles ont lavé elles-mêmes) et placé avant : accord au féminin pluriel."),
  Q("Quelle phrase est correcte ?", ["Ils se sont parlés longtemps.", "Ils se sont parlé longtemps.", "Ils se sont parlées longtemps.", "Ils se sont parler longtemps."], "Ils se sont parlé longtemps.", "On parle à quelqu'un : « se » est COI, le participe reste invariable."),
]),
notion('F69', 3, D, 'f-accord-sujet-complexe', [
  Q("Quelle phrase est correcte selon la règle la plus courante ?", ["La plupart des élèves est venue.", "La plupart des élèves sont venus.", "La plupart des élèves est venu.", "La plupart des élèves sont venue."], "La plupart des élèves sont venus.", "Après « la plupart », le verbe s'accorde avec le complément (les élèves) : pluriel."),
  Q("Quelle phrase est correcte ?", ["Chacun des invités ont apporté un plat.", "Chacun des invités a apporté un plat.", "Chacun des invités avons apporté un plat.", "Chacuns des invités ont apporté un plat."], "Chacun des invités a apporté un plat.", "« Chacun » est un pronom distributif singulier : le verbe est au singulier."),
  Q("Avec un sujet coordonné par « ni… ni » (« Ni Paul ni Marie ne … »), quel accord est le plus courant ?", ["Le pluriel : « ne viendront »", "La 1re personne du pluriel : « ne viendrons »", "Le singulier obligatoire : « ne viendra »", "L'infinitif : « ne venir »"], "Le pluriel : « ne viendront »", "Quand les deux sujets peuvent faire l'action, l'usage le plus courant est le pluriel ; le singulier est admis quand l'action ne peut concerner qu'un seul des deux."),
]),
notion('F69', 1, D, 'f-accord-adjectif-complexe', [
  Q("Quelle forme est correcte ?", ["Des chemises bleu clair", "Des chemises bleues claires", "Des chemises bleus clairs", "Des chemises bleue claire"], "Des chemises bleu clair", "Un adjectif de couleur composé reste invariable : bleu clair, vert foncé."),
  Q("Quelle forme est correcte ?", ["Des rubans orange", "Des rubans oranges", "Des rubans orangés et oranges", "Des rubans orangent"], "Des rubans orange", "Les adjectifs de couleur issus d'un nom (orange, marron, crème) restent invariables, sauf rose, mauve, pourpre, fauve…"),
  Q("Quelle forme est correcte ?", ["Elles sont arrivées nu-pieds.", "Elles sont arrivées nues-pieds.", "Elles sont arrivées nus-pieds.", "Elles sont arrivées nue-pieds."], "Elles sont arrivées nu-pieds.", "« Nu » placé devant le nom et lié par un trait d'union reste invariable ; on écrirait en revanche « pieds nus »."),
]),
notion('F66', 0, D, 'f-subjonctif-conjonctions', [
  Q("Quelle phrase est correcte ?", ["Après qu'il soit parti, nous avons dîné.", "Après qu'il est parti, nous avons dîné.", "Après qu'il parte, nous avons dîné.", "Après qu'il partirait, nous avons dîné."], "Après qu'il est parti, nous avons dîné.", "« Après que » introduit un fait réalisé : il se construit avec l'indicatif, contrairement à « avant que »."),
  Q("Quelle phrase est correcte ?", ["Avant qu'il part, dis-lui au revoir.", "Avant qu'il parte, dis-lui au revoir.", "Avant qu'il partira, dis-lui au revoir.", "Avant qu'il est parti, dis-lui au revoir."], "Avant qu'il parte, dis-lui au revoir.", "« Avant que » introduit un fait non encore réalisé : subjonctif."),
  Q("Quelle conjonction entraîne le subjonctif ?", ["Parce que", "Pendant que", "Bien que", "Puisque"], "Bien que", "« Bien que » (concession) entraîne le subjonctif ; les autres conjonctions citées introduisent des faits réels, à l'indicatif."),
]),
notion('F66', 1, D, 'f-conditionnel-modal-temporel', [
  Q("Dans « Il savait qu'elle réussirait », le conditionnel est…", ["un temps de l'indicatif à valeur de futur dans le passé", "un mode exprimant une hypothèse", "un subjonctif", "un impératif"], "un temps de l'indicatif à valeur de futur dans le passé", "La grammaire actuelle range le conditionnel parmi les temps de l'indicatif ; ici, il situe une action future par rapport à un moment passé."),
  Q("Dans « Si tu venais, je serais heureux », quelle valeur a le conditionnel ?", ["Le futur dans le passé", "Le potentiel ou l'irréel du présent", "La politesse", "L'ordre"], "Le potentiel ou l'irréel du présent", "Le système « si + imparfait, conditionnel présent » exprime une hypothèse sur le présent ou l'avenir."),
  Q("Selon la terminologie grammaticale actuelle (Eduscol), le conditionnel est…", ["un mode à part entière", "un temps de l'indicatif", "une forme du subjonctif", "une voix"], "un temps de l'indicatif", "La « Grammaire du français » d'Eduscol présente le conditionnel comme un temps de l'indicatif, aux valeurs temporelles et modales."),
]),
notion('F60', 0, D, 'f-discours-indirect-libre', [
  Q("« Elle hésitait. Partirait-elle demain ? Rien n'était sûr. » Comment sont rapportées les pensées du personnage ?", ["Au discours direct", "Au discours indirect", "Au discours indirect libre", "Au discours narrativisé"], "Au discours indirect libre", "Les pensées gardent la tournure interrogative mais sans guillemets ni verbe introducteur, avec les temps et pronoms du récit."),
  Q("Quelle est la caractéristique du discours indirect libre ?", ["Il utilise des guillemets", "Il n'a ni verbe introducteur ni subordination, mais adopte les temps du récit", "Il est toujours au présent", "Il utilise un tiret de dialogue"], "Il n'a ni verbe introducteur ni subordination, mais adopte les temps du récit", "Il mêle la voix du narrateur et celle du personnage, sans marques explicites."),
  Q("Quel effet produit souvent le discours indirect libre ?", ["Un effet de distance", "Une plongée dans la conscience du personnage", "Un effet théâtral", "Une accélération de l'action"], "Une plongée dans la conscience du personnage", "Le lecteur entend la pensée du personnage de l'intérieur, sans interruption du récit."),
]),
notion('F63', 1, D, 'f-subjonctif-passe', [
  Q("Quelle forme est au subjonctif passé ?", ["Qu'il ait fini", "Qu'il avait fini", "Qu'il aurait fini", "Qu'il aura fini"], "Qu'il ait fini", "Auxiliaire au subjonctif présent (ait) + participe passé : subjonctif passé."),
  Q("Complétez : « Je suis content que tu … (venir) hier. »", ["viennes", "sois venu", "étais venu", "serais venu"], "sois venu", "L'action est passée et la principale exige le subjonctif : subjonctif passé (que tu sois venu)."),
  Q("Quelle forme est correcte ?", ["Bien qu'elle ait réussi", "Bien qu'elle a réussi", "Bien qu'elle avait réussi", "Bien qu'elle aurait réussi"], "Bien qu'elle ait réussi", "« Bien que » exige le subjonctif ; l'action étant achevée, on emploie le subjonctif passé."),
]),
notion('F45', 1, D, 'f-doublets', [
  Q("« Hôtel » et « hôpital » viennent du même mot latin hospitalis. Comment appelle-t-on de tels mots ?", ["Des homonymes", "Des doublets", "Des paronymes", "Des antonymes"], "Des doublets", "Des doublets sont issus du même étymon : l'un par évolution populaire (hôtel), l'autre par emprunt savant (hôpital)."),
  Q("Quel mot est la forme savante correspondant à « frêle » ?", ["Fragile", "Faible", "Fréle", "Frisson"], "Fragile", "Frêle (formation populaire) et fragile (formation savante) viennent tous deux du latin fragilis."),
  Q("Quel adjectif savant correspond au nom « eau » ?", ["Aquatique", "Eaueux", "Ondin", "Liquide"], "Aquatique", "L'adjectif est formé sur la racine latine aqua, alors que le nom « eau » est issu de l'évolution populaire du même mot."),
]),
notion('F12', 2, D, 'f-courants-caracteristiques', [
  Q("Quel mouvement, au XVIIe siècle, recherche l'ordre, la mesure et le respect de règles comme celle des trois unités au théâtre ?", ["Le baroque", "Le classicisme", "Le romantisme", "Le symbolisme"], "Le classicisme", "Le classicisme (Racine, Molière, La Fontaine) valorise la raison, la clarté et les règles héritées de l'Antiquité."),
  Q("Quel mouvement du XXe siècle, mené par André Breton, explore l'inconscient et le rêve ?", ["Le réalisme", "Le surréalisme", "Le naturalisme", "Le Parnasse"], "Le surréalisme", "Le surréalisme (Breton, Éluard, Aragon) s'appuie sur l'écriture automatique et l'imaginaire."),
  Q("Quelle œuvre appartient au réalisme ?", ["Madame Bovary de Flaubert", "Phèdre de Racine", "Les Contemplations de Hugo", "Alcools d'Apollinaire"], "Madame Bovary de Flaubert", "Madame Bovary (1857) décrit avec précision la vie provinciale et les illusions d'Emma : c'est un roman réaliste."),
  Q("Quel mouvement de la Renaissance place l'être humain et le savoir antique au centre de la réflexion ?", ["L'humanisme", "Le classicisme", "Les Lumières", "Le romantisme"], "L'humanisme", "L'humanisme du XVIe siècle (Érasme, Rabelais, Montaigne) redécouvre les textes antiques et croit en l'éducation de l'homme."),
]),
notion('F54', 2, D, 'f-gn-etendu', [
  C("Cliquez sur tous les mots du complément du nom « souvenir ».", "Le souvenir [de ses vacances en Bretagne] la faisait sourire.", "Le groupe prépositionnel introduit par « de » complète le nom « souvenir » : c'est un complément du nom, expansion du groupe nominal."),
  C("Cliquez sur tous les mots des expansions du nom « château ».", "Un château [ancien] [qui domine la vallée] attire les visiteurs.", "Le nom « château » est complété par un adjectif épithète (ancien) et par une subordonnée relative (qui domine la vallée)."),
  Q("Dans « une tasse à café », quelle est la fonction de « à café » ?", ["COI", "Complément du nom « tasse »", "Complément circonstanciel", "Attribut"], "Complément du nom « tasse »", "« À café » précise le type de tasse : c'est un complément du nom, introduit par la préposition « à »."),
]),
]

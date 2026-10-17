#!/usr/bin/env python3
"""Génère la page de l'application « Quiz CRPE » : /quizzapp.

Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Sortie  : landing/quizzapp.html
Données : table Supabase quiz_questions, servie par /api/quiz/catalogue et /api/quiz/reponse (app.js)
Usage   : python3 scripts/generate_quiz.py

Fonctionnement (tout dans le navigateur, sans compte) :
- séries de 20 questions, note sur 20 à la fin ;
- chaque notion est posée sous plusieurs formulations : 3 bonnes réponses (formulations différentes) = notion maîtrisée ;
- révision espacée : après une bonne réponse, la formulation suivante revient 1 jour puis 3 jours plus tard ;
  après une erreur, l'explication est affichée et une question similaire revient le lendemain ;
- progression gardée dans le navigateur (localStorage), par matière et par thème.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, 'landing', 'crpe-bac3-structure-premiere-epreuve-admissibilite.html')
SITE = 'https://www.passcrpe.fr'

# (clé dans la table, libellé, icône)
MATIERES = [
    ('francais', 'Français', '✍️'),
    ('mathematiques', 'Mathématiques', '🔢'),
    ('histoire_geographie', 'Histoire-géographie', '🌍'),
    ('emc', 'Enseignement moral et civique', '⚖️'),
    ('svt', 'Sciences de la vie et de la Terre', '🌱'),
    ('physique_chimie', 'Physique-chimie', '⚗️'),
    ('technologie', 'Technologie', '⚙️'),
    ('arts', 'Arts', '🎨'),
    ('anglais', 'Anglais', '🇬🇧'),
]
TAILLE_SERIE = 20
BONNES_POUR_MAITRISER = 3
INTERVALLES_JOURS = [1, 3]   # après la 1re puis la 2e bonne réponse
APRES_ERREUR_JOURS = 1

# ── Gabarit commun ───────────────────────────────────────────────────────────
tpl = open(TEMPLATE, encoding='utf-8').read()
HEAD_START = tpl[:tpl.index('  <title>')]
css_start = tpl.index('  <link rel="preconnect"')
css_end = tpl.index('  </style>', css_start)
CSS_BASE = tpl[css_start:css_end]
BODY_START = tpl[css_end:tpl.index('<div class="article-wrap">')]
TAIL = tpl[tpl.index('<footer>'):]
NAV_BLOG = '<li><a href="/blog" class="active">Blog</a></li>'
assert BODY_START.count(NAV_BLOG) == 1
BODY_NAV = BODY_START.replace(NAV_BLOG, '<li><a href="/blog">Blog</a></li>')

CSS = """
    /* QUIZ */
    .quiz-wrap { max-width: 780px; margin: 0 auto; padding: 32px 20px 72px; color: var(--gray-700); }
    .quiz-wrap h1 { font-size: clamp(28px, 4.5vw, 38px); font-weight: 900; color: var(--gray-900); line-height: 1.15; letter-spacing: -.5px; margin-bottom: 10px; }
    .quiz-lead { font-size: 16px; line-height: 1.6; margin-bottom: 26px; }
    .quiz-filtres { display: grid; gap: 18px; }
    .quiz-filtre label, .quiz-filtre .lbl { display: block; font-size: 13px; font-weight: 800; color: var(--gray-700); margin-bottom: 8px; }
    .quiz-select { width: 100%; padding: 13px 14px; font: inherit; font-size: 16px; font-weight: 600; color: var(--gray-900); border: 1.5px solid var(--gray-200); border-radius: 12px; background: #fff; cursor: pointer; }
    .quiz-select:focus { outline: none; border-color: #fb923c; }
    .quiz-niveaux { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .quiz-niveau { padding: 12px 8px; border-radius: 12px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 15px; font-weight: 700; color: var(--gray-700); cursor: pointer; transition: border-color .15s, background .15s; }
    .quiz-niveau:hover { border-color: #fb923c; }
    .quiz-niveau[aria-pressed="true"] { border-color: #f97316; background: #fff7ed; color: #c2410c; }
    .quiz-resume { font-size: 14px; color: var(--gray-600); background: var(--gray-50); border-radius: 12px; padding: 12px 14px; min-height: 46px; }
    .quiz-resume b { color: var(--gray-900); }
    .quiz-card { background: #fff; border: 1.5px solid var(--gray-200); border-radius: 20px; padding: 28px; box-shadow: 0 8px 30px rgba(0,0,0,.04); }
    .quiz-top { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 10px; font-size: 13px; font-weight: 700; color: var(--gray-500); }
    .quiz-top .mat { color: #c2410c; }
    .quiz-bar { height: 6px; border-radius: 6px; background: var(--gray-100); overflow: hidden; margin-bottom: 16px; }
    .quiz-bar span { display: block; height: 100%; background: linear-gradient(90deg, #f97316, #fb923c); transition: width .3s; }
    .quiz-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
    .chip { font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 100px; background: var(--gray-100); color: var(--gray-600); }
    .chip.facile { background: #dcfce7; color: #166534; }
    .chip.intermediaire { background: #fef3c7; color: #92400e; }
    .chip.difficile { background: #fee2e2; color: #991b1b; }
    .chip.theme { background: #ede9fe; color: #5b21b6; }
    .quiz-objectif { font-size: 12.5px; color: var(--gray-500); line-height: 1.5; margin-bottom: 18px; }
    .quiz-objectif strong { color: var(--gray-600); }
    .quiz-q { font-size: 19px; font-weight: 800; color: var(--gray-900); line-height: 1.45; margin-bottom: 18px; }
    .quiz-choices { display: grid; gap: 10px; }
    .quiz-choice { text-align: left; padding: 14px 16px; border-radius: 12px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 15px; color: var(--gray-800); cursor: pointer; transition: border-color .15s, background .15s; }
    .quiz-choice:hover:not(:disabled) { border-color: #fb923c; background: #fff7ed; }
    .quiz-choice:disabled { cursor: default; }
    .quiz-choice.good, .quiz-choice.bad, .tok.good, .tok.bad { transition: none; }
    .quiz-choice.good { border-color: #16a34a; background: #f0fdf4; color: #14532d; font-weight: 700; }
    .quiz-choice.bad { border-color: #dc2626; background: #fef2f2; color: #7f1d1d; }
    .quiz-num { display: flex; gap: 10px; flex-wrap: wrap; }
    .quiz-num input { flex: 1; min-width: 160px; padding: 13px 14px; font: inherit; font-size: 17px; border: 1.5px solid var(--gray-200); border-radius: 12px; }
    .quiz-num input:focus { outline: none; border-color: #fb923c; }
    .quiz-num input.good { border-color: #16a34a; background: #f0fdf4; }
    .quiz-num input.bad { border-color: #dc2626; background: #fef2f2; }
    .quiz-phrase { font-size: 19px; line-height: 2.3; padding: 14px 16px; border-radius: 14px; background: var(--gray-50); border: 1px solid var(--gray-200); margin-bottom: 14px; }
    .tok { display: inline-block; font: inherit; padding: 0 6px; margin: 0 1px; border-radius: 8px; border: 1.5px solid transparent; background: none; cursor: pointer; color: var(--gray-900); line-height: 1.7; }
    .tok:hover:not(:disabled) { background: #ffedd5; }
    .tok.sel { background: #fed7aa; border-color: #fb923c; }
    .tok.good { background: #dcfce7; border-color: #16a34a; }
    .tok.bad { background: #fee2e2; border-color: #dc2626; }
    .tok:disabled { cursor: default; }
    .punct { color: var(--gray-700); }
    .quiz-hint { font-size: 13px; color: var(--gray-500); margin-bottom: 4px; }
    .quiz-feedback { margin-top: 18px; padding: 16px 18px; border-radius: 14px; font-size: 15px; line-height: 1.6; }
    .quiz-feedback.ok { background: #f0fdf4; border: 1px solid #bbf7d0; }
    .quiz-feedback.ko { background: #fef2f2; border: 1px solid #fecaca; }
    .quiz-feedback strong { display: block; margin-bottom: 4px; color: var(--gray-900); }
    .quiz-feedback .suite { display: block; margin-top: 8px; font-size: 13px; color: var(--gray-600); }
    .quiz-actions { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 20px; }
    .quiz-btn { display: inline-flex; align-items: center; justify-content: center; padding: 12px 22px; border-radius: 10px; border: 0; font: inherit; font-size: 15px; font-weight: 800; cursor: pointer; background: #f97316; color: #fff; text-decoration: none; }
    .quiz-btn:hover { background: #ea580c; }
    .quiz-btn:disabled { background: #fdba74; cursor: not-allowed; }
    .quiz-btn.ghost { background: #fff; color: var(--gray-700); border: 1.5px solid var(--gray-200); }
    .quiz-btn.ghost:hover { background: var(--gray-50); }
    .quiz-score { text-align: center; }
    .quiz-score .big { font-size: 56px; font-weight: 900; color: var(--gray-900); letter-spacing: -1px; line-height: 1; margin: 6px 0 8px; }
    .quiz-score p { font-size: 16px; margin-bottom: 6px; }
    .quiz-score .quiz-actions { justify-content: center; }
    .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 18px 0 4px; }
    .stat { background: var(--gray-50); border-radius: 12px; padding: 12px 8px; text-align: center; }
    .stat b { display: block; font-size: 22px; font-weight: 900; color: var(--gray-900); }
    .stat span { font-size: 12px; color: var(--gray-500); }
    .quiz-recap { text-align: left; margin-top: 22px; display: grid; gap: 8px; }
    .quiz-recap div { font-size: 14px; padding: 10px 12px; border-radius: 10px; background: var(--gray-50); line-height: 1.5; }
    .quiz-recap .r-ok::before { content: "✓ "; color: #16a34a; font-weight: 900; }
    .quiz-recap .r-ko::before { content: "✗ "; color: #dc2626; font-weight: 900; }
    .prog-theme { margin-top: 16px; }
    .prog-theme h3 { font-size: 15px; font-weight: 800; color: var(--gray-900); margin-bottom: 6px; display: flex; justify-content: space-between; gap: 10px; }
    .prog-theme h3 span { font-size: 13px; font-weight: 600; color: var(--gray-500); }
    .prog-bar { height: 10px; border-radius: 10px; background: var(--gray-100); overflow: hidden; display: flex; }
    .prog-bar .m { background: #16a34a; }
    .prog-bar .c { background: #fbbf24; }
    .prog-legend { display: flex; gap: 14px; flex-wrap: wrap; font-size: 12px; color: var(--gray-500); margin-top: 14px; }
    .prog-legend i { display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 5px; vertical-align: -1px; }
    .quiz-msg { padding: 14px 16px; border-radius: 12px; background: #fef2f2; color: #7f1d1d; font-size: 15px; }
    .quiz-link { background: none; border: 0; font: inherit; font-size: 13px; color: var(--gray-500); text-decoration: underline; cursor: pointer; padding: 0; }
    @media (max-width: 600px) { .quiz-card { padding: 20px 16px; } .quiz-q { font-size: 17px; } .quiz-phrase { font-size: 17px; } .stat b { font-size: 19px; } }
  .quiz-confirm { background: #dcfce7; color: #166534; font-weight: 600; border-radius: 12px; padding: 12px 16px; margin: 0 0 16px; }
"""

JS = """<script>
(function () {
  var MATIERES = __MATIERES__, SERIE = __SERIE__, MAITRISE = __MAITRISE__, INTERVALLES = __INTERVALLES__, APRES_ERREUR = __APRES_ERREUR__;
  var JOUR = 86400000, CLE = 'passcrpe-quiz-v1';
  var NIVEAUX = { facile: 'Facile', intermediaire: 'Intermédiaire', difficile: 'Avancé' };
  var CLE_CHOIX = 'passcrpe-quiz-choix';
  var root = document.getElementById('quiz-app');
  var catalogues = {}, st = null, choix = lireChoix();

  // ── Progression (navigateur uniquement) ──
  function lire() { try { return JSON.parse(localStorage.getItem(CLE)) || {}; } catch (e) { return {}; } }
  function ecrire(p) { try { localStorage.setItem(CLE, JSON.stringify(p)); } catch (e) {} }
  // Dernier choix de matière et de niveau, retrouvé à la prochaine visite
  function lireChoix() { var c = {}; try { c = JSON.parse(localStorage.getItem(CLE_CHOIX)) || {}; } catch (e) {}
    return { mat: MATIERES.some(function (m) { return m[0] === c.mat; }) ? c.mat : MATIERES[0][0], niveau: NIVEAUX[c.niveau] ? c.niveau : 'facile' }; }
  function garderChoix() { try { localStorage.setItem(CLE_CHOIX, JSON.stringify(choix)); } catch (e) {} }
  function prog(mat) { var p = lire(); return (p[mat] && p[mat].notions) ? p[mat] : { notions: {}, series: 0 }; }
  function sauver(mat, pm) { var p = lire(); p[mat] = pm; ecrire(p); }

  function esc(v) { return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function label(k) { for (var i = 0; i < MATIERES.length; i++) if (MATIERES[i][0] === k) return MATIERES[i][1]; return k; }
  function top() { window.scrollTo({ top: root.offsetTop - 90, behavior: 'smooth' }); }
  function melange(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function jours(n) { return n <= 1 ? 'demain' : 'dans ' + n + ' jours'; }
  function dateFr(ts) { return new Date(ts).toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' }); }

  function grouper(qs) {
    var notions = {}, ordre = [];
    qs.forEach(function (q) { if (!notions[q.notion]) { notions[q.notion] = { cle: q.notion, niveau: q.niveau, theme: q.theme, questions: [] }; ordre.push(q.notion); } notions[q.notion].questions.push(q); });
    return { notions: notions, ordre: ordre };
  }
  function charger(mat) {
    if (catalogues[mat]) return Promise.resolve(catalogues[mat]);
    return fetch('/api/quiz/catalogue?matiere=' + encodeURIComponent(mat)).then(function (r) { return r.json(); }).then(function (d) {
      if (!d.questions || !d.questions.length) throw new Error(d.error || 'vide');
      catalogues[mat] = grouper(d.questions); return catalogues[mat];
    });
  }

  // ── Composition d'une série du niveau choisi : révisions dues, puis nouvelles notions, puis révisions anticipées ──
  function composer(cat, pm, niveau) {
    var now = Date.now(), dues = [], neuves = [], attente = [], rang = { facile: 0, intermediaire: 1, difficile: 2 };
    cat.ordre.forEach(function (k) {
      if (niveau && cat.notions[k].niveau !== niveau) return;
      var s = pm.notions[k];
      if (!s) neuves.push(k);
      else if (s.maitrise) return;
      else if ((s.due || 0) <= now) dues.push(k);
      else attente.push(k);
    });
    dues.sort(function (a, b) { return (pm.notions[a].due || 0) - (pm.notions[b].due || 0); });
    neuves = melange(neuves).sort(function (a, b) { return rang[cat.notions[a].niveau] - rang[cat.notions[b].niveau]; });
    attente.sort(function (a, b) { return pm.notions[a].due - pm.notions[b].due; });
    var choisies = dues.concat(neuves, attente).slice(0, SERIE);
    return melange(choisies.map(function (k) {
      var s = pm.notions[k] || { ok: [], vus: [] }, qs = cat.notions[k].questions;
      var restantes = qs.filter(function (q) { return s.ok.indexOf(q.id) < 0; });
      if (!restantes.length) restantes = qs;
      var jamais = restantes.filter(function (q) { return s.vus.indexOf(q.id) < 0; });
      var pool = jamais.length ? jamais : restantes;
      return pool[Math.floor(Math.random() * pool.length)];
    }));
  }

  function bilan(mat, cat, niveau) {
    var pm = prog(mat), m = 0, c = 0, n = 0, now = Date.now(), prochaine = null, dues = 0;
    cat.ordre.forEach(function (k) {
      if (niveau && cat.notions[k].niveau !== niveau) return;
      n++;
      var s = pm.notions[k]; if (!s) return;
      if (s.maitrise) m++; else { c++; if ((s.due || 0) <= now) dues++; else if (!prochaine || s.due < prochaine) prochaine = s.due; }
    });
    return { maitrisees: m, encours: c, total: n, dues: dues, prochaine: prochaine };
  }

  // ── Écrans ──
  function accueil() {
    st = null;
    root.innerHTML = '<div class="quiz-card quiz-filtres">' +
      '<div class="quiz-filtre"><label for="quiz-mat">Matière</label><select id="quiz-mat" class="quiz-select">' +
      MATIERES.map(function (m) { return '<option value="' + m[0] + '"' + (m[0] === choix.mat ? ' selected' : '') + '>' + esc(m[1]) + '</option>'; }).join('') + '</select></div>' +
      '<div class="quiz-filtre"><span class="lbl" id="quiz-niv-lbl">Niveau</span><div class="quiz-niveaux" role="group" aria-labelledby="quiz-niv-lbl">' +
      Object.keys(NIVEAUX).map(function (n) { return '<button type="button" class="quiz-niveau" data-niv="' + n + '" aria-pressed="' + (n === choix.niveau) + '">' + NIVEAUX[n] + '</button>'; }).join('') + '</div></div>' +
      '<div class="quiz-resume" id="quiz-resume">…</div>' +
      '<div class="quiz-actions" style="margin-top:0"><button type="button" class="quiz-btn" data-act="start">Lancer une série</button><button type="button" class="quiz-btn ghost" data-act="prog-choix">Ma progression</button></div>' +
      '</div>';
    resume();
  }

  // Résumé du choix en cours : notions du niveau, maîtrisées, à réviser
  function resume() {
    var el = document.getElementById('quiz-resume'); if (!el) return;
    var mat = choix.mat, niveau = choix.niveau;
    el.textContent = 'Chargement…';
    charger(mat).then(function (cat) {
      if (!document.getElementById('quiz-resume') || choix.mat !== mat || choix.niveau !== niveau) return;
      var b = bilan(mat, cat, niveau);
      el.innerHTML = '<b>' + esc(label(mat)) + ' · ' + NIVEAUX[niveau] + '</b> : ' + b.total + ' notions, ' + b.maitrisees + ' maîtrisée' + (b.maitrisees > 1 ? 's' : '') +
        (b.dues ? ', <b>' + b.dues + ' à réviser aujourd\\'hui</b>' : '') + '.';
    }).catch(function () { el.textContent = 'Le quiz n\\'a pas pu être chargé. Réessaie dans quelques instants.'; });
  }

  function demarrer(mat, niveau) {
    root.innerHTML = '<div class="quiz-card"><p>Chargement des questions…</p></div>';
    charger(mat).then(function (cat) {
      var serie = composer(cat, prog(mat), niveau);
      if (!serie.length) return progression(mat, 'Toutes les notions de niveau ' + NIVEAUX[niveau].toLowerCase() + ' sont maîtrisées dans cette matière. Bravo ! Essayez un autre niveau.');
      st = { mat: mat, niveau: niveau, cat: cat, serie: serie, i: 0, score: 0, recap: [], sel: [], repondu: false };
      question(); top();
    }).catch(function () {
      root.innerHTML = '<div class="quiz-msg">Le quiz n\\'a pas pu être chargé. Réessaie dans quelques instants.</div><div class="quiz-actions"><button type="button" class="quiz-btn ghost" data-act="home">Changer de matière ou de niveau</button></div>';
    });
  }

  function entete(q) {
    var n = st.serie.length;
    return '<div class="quiz-top"><span class="mat">' + esc(label(st.mat)) + ' · ' + NIVEAUX[st.niveau] + '</span><span>Question ' + (st.i + 1) + ' / ' + n + '</span></div>' +
      '<div class="quiz-bar"><span style="width:' + Math.round(st.i / n * 100) + '%"></span></div>' +
      '<div class="quiz-meta"><span class="chip ' + q.niveau + '">' + (NIVEAUX[q.niveau] || '') + '</span>' +
      (q.theme ? '<span class="chip theme">' + esc(q.theme) + (q.sous_theme ? ' › ' + esc(q.sous_theme) : '') + '</span>' : '') +
      (q.classe ? '<span class="chip">Programme de ' + esc(q.classe) + '</span>' : '') + '</div>' +
      (q.objectif ? '<p class="quiz-objectif"><strong>Objectif du programme :</strong> ' + esc(q.objectif) + '</p>' : '');
  }

  function question() {
    var q = st.serie[st.i], corps = '';
    st.repondu = false; st.sel = [];
    if (q.type === 'numerique') {
      corps = '<form class="quiz-num" data-form="num"><input type="text" inputmode="decimal" autocomplete="off" placeholder="Votre réponse (nombre)" aria-label="Votre réponse"><button type="submit" class="quiz-btn">Valider</button></form>';
    } else if (q.type === 'cliquer_mot') {
      corps = '<p class="quiz-hint">Cliquez sur le ou les mots, puis validez.</p><div class="quiz-phrase">' + q.choix.map(function (t, k) {
        return /[\\wÀ-ÿ]/.test(t) ? '<button type="button" class="tok" data-tok="' + k + '">' + esc(t) + '</button>' : '<span class="punct">' + esc(t) + '</span>';
      }).join(' ') + '</div><button type="button" class="quiz-btn" data-act="valider" disabled>Valider</button>';
    } else {
      corps = '<div class="quiz-choices">' + q.choix.map(function (c, k) { return '<button type="button" class="quiz-choice" data-k="' + k + '">' + esc(c) + '</button>'; }).join('') + '</div>';
    }
    root.innerHTML = '<div class="quiz-card">' + entete(q) + '<p class="quiz-q">' + esc(q.question) + '</p>' + corps + '<div id="quiz-fb"></div></div>';
    var inp = root.querySelector('.quiz-num input'); if (inp) inp.focus();
  }

  function envoyer(reponse, afficher) {
    if (st.repondu) return; st.repondu = true;
    var q = st.serie[st.i];
    fetch('/api/quiz/reponse', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ id: q.id, reponse: reponse }) })
      .then(function (r) { return r.json(); }).then(function (d) {
        if (d.error) throw new Error(d.error);
        afficher(d);
        var suite = enregistrer(q, d.correct);
        if (d.correct) st.score++;
        st.recap.push({ q: q.question, ok: d.correct, attendu: d.attendu });
        var last = st.i === st.serie.length - 1;
        document.getElementById('quiz-fb').innerHTML =
          '<div class="quiz-feedback ' + (d.correct ? 'ok' : 'ko') + '"><strong>' + (d.correct ? 'Bonne réponse !' : 'Ce n\\'est pas la bonne réponse. Réponse attendue : ' + esc(d.attendu)) + '</strong>' + esc(d.explication) +
          '<span class="suite">' + suite + '</span></div>' +
          '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="next">' + (last ? 'Voir ma note' : 'Question suivante →') + '</button></div>';
      }).catch(function () {
        st.repondu = false;
        document.getElementById('quiz-fb').innerHTML = '<div class="quiz-msg" style="margin-top:16px">La correction n\\'a pas pu être chargée. Réessaie.</div>';
      });
  }

  // Révision espacée : met à jour la notion et renvoie le message affiché sous l'explication
  function enregistrer(q, correct) {
    var pm = prog(st.mat), s = pm.notions[q.notion] || { ok: [], vus: [], erreurs: 0, due: 0, maitrise: false };
    var now = Date.now(), msg;
    if (s.vus.indexOf(q.id) < 0) s.vus.push(q.id);
    if (correct) {
      if (s.ok.indexOf(q.id) < 0) s.ok.push(q.id);
      if (s.ok.length >= MAITRISE) { s.maitrise = true; msg = '🎉 Notion maîtrisée : ' + MAITRISE + ' bonnes réponses à des questions différentes.'; }
      else { var j = INTERVALLES[Math.min(s.ok.length - 1, INTERVALLES.length - 1)]; s.due = now + j * JOUR; msg = 'Bonne réponse ' + s.ok.length + ' / ' + MAITRISE + ' pour cette notion : une autre formulation vous sera posée ' + jours(j) + '.'; }
    } else {
      s.erreurs = (s.erreurs || 0) + 1; s.due = now + APRES_ERREUR * JOUR;
      msg = 'Une question similaire vous sera reposée ' + jours(APRES_ERREUR) + ', pour ancrer la notion.';
    }
    pm.notions[q.notion] = s; sauver(st.mat, pm);
    return msg;
  }

  function fin() {
    var pm = prog(st.mat); pm.series = (pm.series || 0) + 1; sauver(st.mat, pm);
    var n = st.serie.length, s = st.score, b = bilan(st.mat, st.cat, st.niveau);
    var note = Math.round(s / n * 20 * 2) / 2;
    var msg = note >= 16 ? 'Excellent travail !' : note >= 12 ? 'Bon travail, continuez comme ça.' : note >= 8 ? 'C\\'est un début : les notions ratées reviendront pour être retravaillées.' : 'Ces notions sont à retravailler : elles reviendront dans vos prochaines séries.';
    root.innerHTML = '<div class="quiz-card quiz-score">' +
      '<div class="quiz-top" style="justify-content:center"><span class="mat">' + esc(label(st.mat)) + ' · ' + NIVEAUX[st.niveau] + ' · série ' + pm.series + '</span></div>' +
      '<div class="big">' + String(note).replace('.', ',') + ' / 20</div><p>' + s + ' bonne' + (s > 1 ? 's' : '') + ' réponse' + (s > 1 ? 's' : '') + ' sur ' + n + '. ' + msg + '</p>' +
      '<div class="stats"><div class="stat"><b>' + b.maitrisees + '</b><span>notions maîtrisées</span></div><div class="stat"><b>' + b.encours + '</b><span>en cours</span></div><div class="stat"><b>' + (b.total - b.maitrisees - b.encours) + '</b><span>à découvrir</span></div></div>' +
      (b.prochaine && !b.dues ? '<p style="font-size:13px;color:var(--gray-500)">Prochaines révisions à partir du ' + dateFr(b.prochaine) + '.</p>' : '') +
      '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="again">Nouvelle série de ' + SERIE + '</button><button type="button" class="quiz-btn ghost" data-act="prog">Ma progression</button><button type="button" class="quiz-btn ghost" data-act="home">Changer de matière ou de niveau</button></div>' +
      '<div class="quiz-recap">' + st.recap.map(function (r) {
        return '<div class="' + (r.ok ? 'r-ok' : 'r-ko') + '">' + esc(r.q) + (r.ok ? '' : ' <em>Réponse : ' + esc(r.attendu) + '</em>') + '</div>';
      }).join('') + '</div></div>';
    top();
  }

  function progression(mat, message) {
    charger(mat).then(function (cat) {
      var pm = prog(mat), b = bilan(mat, cat), themes = {}, ordre = [];
      cat.ordre.forEach(function (k) {
        var t = cat.notions[k].theme || 'Notions';
        if (!themes[t]) { themes[t] = { m: 0, c: 0, n: 0 }; ordre.push(t); }
        var s = pm.notions[k]; themes[t].n++;
        if (s && s.maitrise) themes[t].m++; else if (s) themes[t].c++;
      });
      var niveau = (st && st.niveau) || choix.niveau;
      st = { mat: mat, niveau: niveau, cat: cat };
      var parNiveau = Object.keys(NIVEAUX).map(function (n) { var x = bilan(mat, cat, n); return '<div class="stat"><b>' + x.maitrisees + ' / ' + x.total + '</b><span>' + NIVEAUX[n] + '</span></div>'; }).join('');
      root.innerHTML = '<div class="quiz-card">' +
        '<div class="quiz-top"><span class="mat">' + esc(label(mat)) + ' · ma progression</span><span>' + (pm.series || 0) + ' série' + ((pm.series || 0) > 1 ? 's' : '') + '</span></div>' +
        (message ? '<p style="font-weight:700;color:#166534">' + esc(message) + '</p>' : '') +
        '<div class="stats"><div class="stat"><b>' + b.maitrisees + ' / ' + b.total + '</b><span>notions maîtrisées</span></div><div class="stat"><b>' + b.encours + '</b><span>en cours</span></div><div class="stat"><b>' + b.dues + '</b><span>à réviser aujourd\\'hui</span></div></div>' +
        '<p style="font-size:13px;font-weight:800;color:var(--gray-700);margin-top:14px">Notions maîtrisées par niveau</p><div class="stats" style="margin-top:6px">' + parNiveau + '</div>' +
        ordre.map(function (t) {
          var x = themes[t];
          return '<div class="prog-theme"><h3>' + esc(t) + '<span>' + x.m + ' / ' + x.n + ' maîtrisées</span></h3><div class="prog-bar"><span class="m" style="width:' + (x.m / x.n * 100) + '%"></span><span class="c" style="width:' + (x.c / x.n * 100) + '%"></span></div></div>';
        }).join('') +
        '<div class="prog-legend"><span><i style="background:#16a34a"></i>Maîtrisées (' + MAITRISE + ' bonnes réponses)</span><span><i style="background:#fbbf24"></i>En cours</span><span><i style="background:var(--gray-100)"></i>À découvrir</span></div>' +
        '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="again">Lancer une série · ' + NIVEAUX[niveau] + '</button><button type="button" class="quiz-btn ghost" data-act="home">Changer de matière ou de niveau</button></div>' +
        '<p style="margin-top:18px"><button type="button" class="quiz-link" data-act="reset">Réinitialiser ma progression dans cette matière</button></p></div>';
      top();
    }).catch(function () { root.innerHTML = '<div class="quiz-msg">La progression n\\'a pas pu être chargée.</div>'; });
  }

  // ── Interactions ──
  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b || b.type === 'submit') return;
    if (b.dataset.niv) { choix.niveau = b.dataset.niv; garderChoix(); root.querySelectorAll('.quiz-niveau').forEach(function (x) { x.setAttribute('aria-pressed', x === b); }); resume(); return; }
    if (b.dataset.k !== undefined && st && !st.repondu) {
      var q = st.serie[st.i], k = +b.dataset.k, btns = root.querySelectorAll('.quiz-choice');
      btns.forEach(function (x) { x.disabled = true; });
      envoyer(q.choix[k], function (d) { btns.forEach(function (x, j) { if (q.choix[j] === d.reponse) x.classList.add('good'); else if (j === k) x.classList.add('bad'); }); });
      return;
    }
    if (b.dataset.tok !== undefined && st && !st.repondu) {
      var t = +b.dataset.tok, i = st.sel.indexOf(t);
      if (i < 0) st.sel.push(t); else st.sel.splice(i, 1);
      b.classList.toggle('sel');
      root.querySelector('[data-act="valider"]').disabled = !st.sel.length;
      return;
    }
    var act = b.dataset.act;
    if (act === 'valider' && st && !st.repondu) {
      var toks = root.querySelectorAll('.tok'); toks.forEach(function (x) { x.disabled = true; }); b.disabled = true;
      envoyer(st.sel.slice().sort(function (x, y) { return x - y; }).join(','), function (d) {
        var att = d.reponse.split(',').map(Number);
        toks.forEach(function (x) { var k = +x.dataset.tok; x.classList.remove('sel'); if (att.indexOf(k) >= 0) x.classList.add('good'); else if (st.sel.indexOf(k) >= 0) x.classList.add('bad'); });
      });
    }
    else if (act === 'next') { if (st.i < st.serie.length - 1) { st.i++; question(); top(); } else fin(); }
    else if (act === 'start') demarrer(choix.mat, choix.niveau);
    else if (act === 'prog-choix') { st = null; progression(choix.mat); }
    else if (act === 'again') demarrer(st.mat, st.niveau);
    else if (act === 'prog') progression(st.mat);
    else if (act === 'home') { accueil(); top(); }
    else if (act === 'reset' && confirm('Effacer votre progression dans cette matière ?')) { var p = lire(); delete p[st.mat]; ecrire(p); progression(st.mat); }
  });
  root.addEventListener('change', function (e) {
    if (e.target.id === 'quiz-mat') { choix.mat = e.target.value; garderChoix(); resume(); }
  });
  root.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!st || st.repondu) return;
    var inp = root.querySelector('.quiz-num input'), v = inp.value.trim(); if (!v) return;
    inp.disabled = true; root.querySelector('.quiz-num button').disabled = true;
    envoyer(v, function (d) { inp.classList.add(d.correct ? 'good' : 'bad'); });
  });
  accueil();
})();
</script>
<script>
  // Arrivée depuis l'e-mail de confirmation d'un compte du quiz (projet « quizzcrpe ») :
  // message de bienvenue et mise à jour de email_verified dans Klaviyo
  (function () {
    var h = new URLSearchParams(location.hash.slice(1));
    if (h.get('type') !== 'signup' || !h.get('access_token')) return;
    document.getElementById('quiz-confirm').hidden = false;
    window.dataLayer = window.dataLayer || []; window.dataLayer.push({ event: 'inscription_confirmee', parcours: 'quizcrpe' });
    fetch('/api/klaviyo/email-verified', { method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ access_token: h.get('access_token'), projet: 'quizzcrpe' }) }).catch(function () {});
    history.replaceState(null, '', location.pathname + location.search);
  })();
</script>
"""


def page():
    title = 'Quiz CRPE : testez vos connaissances'
    desc = "Quiz CRPE : séries de 20 questions en français, mathématiques, histoire-géographie, EMC, sciences, arts et anglais, corrigées, expliquées et rattachées au programme."
    body = f'''<main class="quiz-wrap">
  <h1>Quiz CRPE</h1>
  <p class="quiz-confirm" id="quiz-confirm" hidden>✓ Votre adresse e-mail est confirmée : bienvenue sur le Quiz CRPE !</p>
  <p class="quiz-lead">Choisissez une matière et un niveau, puis répondez à des séries de {TAILLE_SERIE} questions rattachées au programme du concours. Chaque notion est posée sous plusieurs formes : avec {BONNES_POUR_MAITRISER} bonnes réponses, elle est maîtrisée. En cas d'erreur, vous voyez l'explication et une question similaire revient plus tard. Votre progression est gardée sur cet appareil.</p>
  <div id="quiz-app"></div>
</main>
'''
    head = (HEAD_START
            + f'  <title>{title} | PassCRPE</title>\n'
            + f'  <meta name="description" content="{desc}" />\n'
            + '  <meta name="robots" content="noindex, nofollow" />\n'
            + f'  <link rel="canonical" href="{SITE}/quizzapp" />\n'
            + CSS_BASE + CSS)
    js = (JS.replace('__MATIERES__', json.dumps(MATIERES, ensure_ascii=False))
            .replace('__SERIE__', str(TAILLE_SERIE)).replace('__MAITRISE__', str(BONNES_POUR_MAITRISER))
            .replace('__INTERVALLES__', json.dumps(INTERVALLES_JOURS)).replace('__APRES_ERREUR__', str(APRES_ERREUR_JOURS)))
    return head + BODY_NAV + body + js + TAIL


open(os.path.join(ROOT, 'landing', 'quizzapp.html'), 'w', encoding='utf-8').write(page())
print('landing/quizzapp.html')

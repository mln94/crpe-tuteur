#!/usr/bin/env python3
"""Génère la page de l'application « Quiz CRPE » : /quiz.

Gabarit : landing/crpe-bac3-structure-premiere-epreuve-admissibilite.html (menu, pied de page, suivi)
Sortie  : landing/quiz.html
Données : table Supabase quiz_questions, servie par /api/quiz/questions et /api/quiz/reponse (app.js)
Usage   : python3 scripts/generate_quiz.py
"""
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
    .quiz-wrap { max-width: 760px; margin: 0 auto; padding: 32px 20px 72px; color: var(--gray-700); }
    .quiz-wrap h1 { font-size: clamp(28px, 4.5vw, 38px); font-weight: 900; color: var(--gray-900); line-height: 1.15; letter-spacing: -.5px; margin-bottom: 10px; }
    .quiz-lead { font-size: 16px; line-height: 1.6; margin-bottom: 26px; }
    .quiz-subjects { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 12px; }
    .quiz-subject { display: flex; align-items: center; gap: 12px; text-align: left; padding: 16px; border-radius: 14px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 15px; font-weight: 700; color: var(--gray-900); cursor: pointer; transition: border-color .15s, box-shadow .15s, transform .15s; }
    .quiz-subject:hover { border-color: #fb923c; box-shadow: 0 6px 20px rgba(249,115,22,.12); transform: translateY(-1px); }
    .quiz-subject .ico { width: 40px; height: 40px; border-radius: 12px; background: #ffedd5; display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; }
    .quiz-subject small { display: block; font-size: 12px; font-weight: 500; color: var(--gray-500); }
    .quiz-card { background: #fff; border: 1.5px solid var(--gray-200); border-radius: 20px; padding: 28px; box-shadow: 0 8px 30px rgba(0,0,0,.04); }
    .quiz-top { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 10px; font-size: 13px; font-weight: 700; color: var(--gray-500); }
    .quiz-top .mat { color: #c2410c; }
    .quiz-bar { height: 6px; border-radius: 6px; background: var(--gray-100); overflow: hidden; margin-bottom: 22px; }
    .quiz-bar span { display: block; height: 100%; background: linear-gradient(90deg, #f97316, #fb923c); transition: width .3s; }
    .quiz-q { font-size: 19px; font-weight: 800; color: var(--gray-900); line-height: 1.45; margin-bottom: 20px; }
    .quiz-choices { display: grid; gap: 10px; }
    .quiz-choice { text-align: left; padding: 14px 16px; border-radius: 12px; border: 1.5px solid var(--gray-200); background: #fff; font: inherit; font-size: 15px; color: var(--gray-800); cursor: pointer; transition: border-color .15s, background .15s; }
    .quiz-choice:hover:not(:disabled) { border-color: #fb923c; background: #fff7ed; }
    .quiz-choice:disabled { cursor: default; }
    .quiz-choice.good, .quiz-choice.bad { transition: none; }
    .quiz-choice.good { border-color: #16a34a; background: #f0fdf4; color: #14532d; font-weight: 700; }
    .quiz-choice.bad { border-color: #dc2626; background: #fef2f2; color: #7f1d1d; }
    .quiz-feedback { margin-top: 18px; padding: 16px 18px; border-radius: 14px; font-size: 15px; line-height: 1.6; }
    .quiz-feedback.ok { background: #f0fdf4; border: 1px solid #bbf7d0; }
    .quiz-feedback.ko { background: #fef2f2; border: 1px solid #fecaca; }
    .quiz-feedback strong { display: block; margin-bottom: 4px; color: var(--gray-900); }
    .quiz-actions { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 20px; }
    .quiz-btn { display: inline-flex; align-items: center; justify-content: center; padding: 12px 22px; border-radius: 10px; border: 0; font: inherit; font-size: 15px; font-weight: 800; cursor: pointer; background: #f97316; color: #fff; text-decoration: none; }
    .quiz-btn:hover { background: #ea580c; }
    .quiz-btn.ghost { background: #fff; color: var(--gray-700); border: 1.5px solid var(--gray-200); }
    .quiz-btn.ghost:hover { background: var(--gray-50); }
    .quiz-score { text-align: center; }
    .quiz-score .big { font-size: 56px; font-weight: 900; color: var(--gray-900); letter-spacing: -1px; line-height: 1; margin: 6px 0 8px; }
    .quiz-score p { font-size: 16px; margin-bottom: 6px; }
    .quiz-score .quiz-actions { justify-content: center; }
    .quiz-recap { text-align: left; margin-top: 24px; display: grid; gap: 8px; }
    .quiz-recap div { font-size: 14px; padding: 10px 12px; border-radius: 10px; background: var(--gray-50); }
    .quiz-recap .r-ok::before { content: "✓ "; color: #16a34a; font-weight: 900; }
    .quiz-recap .r-ko::before { content: "✗ "; color: #dc2626; font-weight: 900; }
    .quiz-msg { padding: 14px 16px; border-radius: 12px; background: #fef2f2; color: #7f1d1d; font-size: 15px; }
    @media (max-width: 600px) { .quiz-card { padding: 20px 16px; } .quiz-q { font-size: 17px; } }
"""

JS = """<script>
(function () {
  var MATIERES = __MATIERES__;
  var root = document.getElementById('quiz-app');
  var st = { mat: null, qs: [], i: 0, score: 0, answered: false, recap: [] };
  function esc(v) { return String(v == null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function label(k) { for (var i = 0; i < MATIERES.length; i++) if (MATIERES[i][0] === k) return MATIERES[i][1]; return k; }
  function top() { window.scrollTo({ top: root.offsetTop - 90, behavior: 'smooth' }); }

  function choose() {
    root.innerHTML = '<div class="quiz-subjects">' + MATIERES.map(function (m) {
      return '<button type="button" class="quiz-subject" data-mat="' + m[0] + '"><span class="ico">' + m[2] + '</span><span>' + esc(m[1]) + '<small>10 questions</small></span></button>';
    }).join('') + '</div>';
  }

  function start(mat) {
    st = { mat: mat, qs: [], i: 0, score: 0, answered: false, recap: [] };
    root.innerHTML = '<div class="quiz-card"><p>Chargement des questions…</p></div>';
    fetch('/api/quiz/questions?matiere=' + encodeURIComponent(mat)).then(function (r) { return r.json(); }).then(function (d) {
      if (!d.questions || !d.questions.length) throw new Error(d.error || 'vide');
      st.qs = d.questions; question(); top();
    }).catch(function () {
      root.innerHTML = '<div class="quiz-msg">Le quiz n\\'a pas pu être chargé. Réessaie dans quelques instants.</div><div class="quiz-actions"><button type="button" class="quiz-btn ghost" data-act="home">Choisir une matière</button></div>';
    });
  }

  function question() {
    var q = st.qs[st.i], n = st.qs.length;
    st.answered = false;
    root.innerHTML = '<div class="quiz-card">' +
      '<div class="quiz-top"><span class="mat">' + esc(label(st.mat)) + '</span><span>Question ' + (st.i + 1) + ' / ' + n + '</span></div>' +
      '<div class="quiz-bar"><span style="width:' + Math.round(st.i / n * 100) + '%"></span></div>' +
      '<p class="quiz-q">' + esc(q.question) + '</p>' +
      '<div class="quiz-choices">' + q.choix.map(function (c, k) { return '<button type="button" class="quiz-choice" data-k="' + k + '">' + esc(c) + '</button>'; }).join('') + '</div>' +
      '<div id="quiz-fb"></div></div>';
  }

  function answer(k) {
    if (st.answered) return; st.answered = true;
    var q = st.qs[st.i], pick = q.choix[k];
    var btns = root.querySelectorAll('.quiz-choice');
    btns.forEach(function (b) { b.disabled = true; });
    fetch('/api/quiz/reponse', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ id: q.id, choix: pick }) })
      .then(function (r) { return r.json(); }).then(function (d) {
        if (d.error) throw new Error(d.error);
        btns.forEach(function (b, j) {
          if (q.choix[j] === d.reponse) b.classList.add('good');
          else if (j === k) b.classList.add('bad');
        });
        if (d.correct) st.score++;
        st.recap.push({ q: q.question, ok: d.correct, rep: d.reponse });
        var last = st.i === st.qs.length - 1;
        document.getElementById('quiz-fb').innerHTML =
          '<div class="quiz-feedback ' + (d.correct ? 'ok' : 'ko') + '"><strong>' + (d.correct ? 'Bonne réponse !' : 'Ce n\\'est pas la bonne réponse. Réponse attendue : ' + esc(d.reponse)) + '</strong>' + esc(d.explication) + '</div>' +
          '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="next">' + (last ? 'Voir mon score' : 'Question suivante →') + '</button></div>';
      }).catch(function () {
        st.answered = false; btns.forEach(function (b) { b.disabled = false; });
        document.getElementById('quiz-fb').innerHTML = '<div class="quiz-msg" style="margin-top:16px">La correction n\\'a pas pu être chargée. Réessaie.</div>';
      });
  }

  function end() {
    var n = st.qs.length, s = st.score;
    var msg = s === n ? 'Parfait, rien à redire !' : s >= n * 0.7 ? 'Très bien, continue comme ça.' : s >= n * 0.5 ? 'C\\'est un bon début : revois les notions manquées.' : 'Ces notions sont à retravailler avant le concours.';
    root.innerHTML = '<div class="quiz-card quiz-score">' +
      '<div class="quiz-top" style="justify-content:center"><span class="mat">' + esc(label(st.mat)) + '</span></div>' +
      '<div class="big">' + s + ' / ' + n + '</div><p>' + msg + '</p>' +
      '<div class="quiz-actions"><button type="button" class="quiz-btn" data-act="again">Recommencer</button><button type="button" class="quiz-btn ghost" data-act="home">Changer de matière</button></div>' +
      '<div class="quiz-recap">' + st.recap.map(function (r) {
        return '<div class="' + (r.ok ? 'r-ok' : 'r-ko') + '">' + esc(r.q) + (r.ok ? '' : ' <em>Réponse : ' + esc(r.rep) + '</em>') + '</div>';
      }).join('') + '</div></div>';
    top();
  }

  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.dataset.mat) start(b.dataset.mat);
    else if (b.dataset.k !== undefined) answer(+b.dataset.k);
    else if (b.dataset.act === 'next') { if (st.i < st.qs.length - 1) { st.i++; question(); top(); } else end(); }
    else if (b.dataset.act === 'again') start(st.mat);
    else if (b.dataset.act === 'home') { choose(); top(); }
  });
  choose();
})();
</script>
"""


def page():
    import json
    title = 'Quiz CRPE : testez vos connaissances'
    desc = "Quiz CRPE : questions à choix multiples en français, mathématiques, histoire-géographie, EMC, sciences, arts et anglais, corrigées et expliquées."
    body = f'''<main class="quiz-wrap">
  <h1>Quiz CRPE</h1>
  <p class="quiz-lead">Choisissez une matière et répondez à 10 questions adaptées au CRPE. Après chaque réponse, vous voyez la bonne réponse et une brève explication.</p>
  <div id="quiz-app"></div>
</main>
'''
    head = (HEAD_START
            + f'  <title>{title} | PassCRPE</title>\n'
            + f'  <meta name="description" content="{desc}" />\n'
            + '  <meta name="robots" content="noindex, nofollow" />\n'
            + f'  <link rel="canonical" href="{SITE}/quiz" />\n'
            + CSS_BASE + CSS)
    return head + BODY_NAV + body + JS.replace('__MATIERES__', json.dumps(MATIERES, ensure_ascii=False)) + TAIL


open(os.path.join(ROOT, 'landing', 'quiz.html'), 'w', encoding='utf-8').write(page())
print('landing/quiz.html')

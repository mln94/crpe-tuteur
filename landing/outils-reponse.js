// Outils de réponse pour les questions de maths qui ne se résolvent pas seulement par du texte :
// droite graduée, repère et tableau à compléter. Partagé par l'application (import) et l'Entraîneur (balise script).
//
// Usage : OutilsReponse.mount(conteneur, outils, onInsert) → { destroy }
//   outils   : tableau de réglages lu dans exercices_maths.outil_reponse
//   onInsert : reçoit le texte à ajouter à la réponse (ex. « Sur la droite graduée : D = 1,5 ; E = −0,5. »)
//
// Réglages :
//   { type: 'droite',  titre?, min, max, pas, pas_placement?, etiquettes?, points: ['D','E'], deja?: [{ nom, x }] }
//   { type: 'repere',  titre?, xmin, xmax, ymin, ymax, pasx?, pasy?, etiquettesx?, etiquettesy?, points: ['D'], deja?: [{ nom, x, y }] }
//   { type: 'tableau', titre?, lignes: [[...]], entete_ligne?, entete_colonne?, choix?: ['Vrai', 'Faux'] }   (null = case à remplir)
(function (global) {
  'use strict';
  var SVG = 'http://www.w3.org/2000/svg';
  var INDIGO = '#4f46e5', GRIS = '#9ca3af', TEXTE = '#374151';

  // ── Utilitaires ──
  function fmt(v) {
    var r = Math.round(v * 100) / 100;
    return String(r).replace('.', ',').replace('-', '−');
  }
  function el(tag, attrs, parent) {
    var e = document.createElement(tag);
    for (var k in attrs || {}) {
      if (k === 'text') e.textContent = attrs[k];
      else if (k === 'class') e.className = attrs[k];
      else e.setAttribute(k, attrs[k]);
    }
    if (parent) parent.appendChild(e);
    return e;
  }
  function svgEl(tag, attrs, parent) {
    var e = document.createElementNS(SVG, tag);
    for (var k in attrs || {}) {
      if (k === 'text') e.textContent = attrs[k];
      else e.setAttribute(k, attrs[k]);
    }
    if (parent) parent.appendChild(e);
    return e;
  }
  // Position du clic dans le repère du viewBox de l'SVG
  function svgPoint(svg, evt) {
    var r = svg.getBoundingClientRect();
    var vb = svg.viewBox.baseVal;
    return { x: (evt.clientX - r.left) * vb.width / r.width, y: (evt.clientY - r.top) * vb.height / r.height };
  }
  function snap(v, pas, min, max) {
    var s = Math.round((v - min) / pas) * pas + min;
    s = Math.round(s * 1000) / 1000;
    return Math.min(max, Math.max(min, s));
  }

  var STYLE = '' +
    '.orx{border:1px solid #e5e7eb;border-radius:12px;padding:12px;margin:0 0 10px;background:#f9fafb;font-family:inherit}' +
    '.orx-titre{font-size:12px;font-weight:700;color:#6b7280;margin:0 0 6px}' +
    '.orx-aide{font-size:12px;color:#6b7280;margin:6px 0 0}' +
    '.orx-points{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}' +
    '.orx-pt{border:1.5px solid #e5e7eb;background:#fff;border-radius:999px;padding:4px 10px;font-size:13px;font-weight:700;color:#374151;cursor:pointer;font-family:inherit}' +
    '.orx-pt.on{border-color:' + INDIGO + ';background:#eef2ff;color:' + INDIGO + '}' +
    '.orx-pt.ok:not(.on){border-color:#a7f3d0;background:#ecfdf5;color:#065f46}' +
    '.orx svg{display:block;width:100%;height:auto;touch-action:manipulation;user-select:none;-webkit-user-select:none;cursor:crosshair;background:#fff;border-radius:8px}' +
    '.orx-bas{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px;margin-top:8px}' +
    '.orx-res{font-size:12px;color:#374151}' +
    '.orx-btn{border:0;border-radius:8px;padding:7px 12px;font-size:13px;font-weight:700;color:#fff;background:' + INDIGO + ';cursor:pointer;font-family:inherit}' +
    '.orx-btn:disabled{opacity:.4;cursor:not-allowed}' +
    '.orx-lien{border:0;background:none;color:#6b7280;font-size:12px;text-decoration:underline;cursor:pointer;padding:0;font-family:inherit}' +
    '.orx-tab{overflow-x:auto}' +
    '.orx table{border-collapse:collapse;background:#fff;font-size:13px}' +
    '.orx td,.orx th{border:1px solid #e5e7eb;padding:4px 6px;text-align:center;white-space:nowrap}' +
    '.orx th{background:#f3f4f6;font-weight:700;color:#374151}' +
    '.orx td input,.orx td select{width:64px;min-width:48px;border:1.5px solid #c7d2fe;border-radius:6px;padding:4px;font-size:13px;text-align:center;font-family:inherit}' +
    '.orx td input.large{width:150px}';
  function injectStyle() {
    if (document.getElementById('orx-style')) return;
    var s = document.createElement('style');
    s.id = 'orx-style';
    s.textContent = STYLE;
    document.head.appendChild(s);
  }

  // Bloc commun : titre, contenu, résumé et bouton « Insérer dans ma réponse »
  function bloc(container, titre) {
    var box = el('div', { class: 'orx' }, container);
    el('p', { class: 'orx-titre', text: titre }, box);
    return box;
  }
  function pied(box, onInsert, getTexte, reset) {
    var bas = el('div', { class: 'orx-bas' }, box);
    var res = el('span', { class: 'orx-res' }, bas);
    var actions = el('span', {}, bas);
    if (reset) {
      var eff = el('button', { type: 'button', class: 'orx-lien', text: 'Tout effacer' }, actions);
      eff.style.marginRight = '10px';
      eff.addEventListener('click', reset);
    }
    var btn = el('button', { type: 'button', class: 'orx-btn', text: 'Insérer dans ma réponse' }, actions);
    btn.addEventListener('click', function () { var t = getTexte(); if (t) onInsert(t); });
    return function maj(resume) { res.textContent = resume || ''; btn.disabled = !getTexte(); };
  }
  // Boutons de choix du point à placer
  function choixPoints(box, noms, etat) {
    var wrap = el('div', { class: 'orx-points' }, box);
    var btns = {};
    noms.forEach(function (n) {
      var b = el('button', { type: 'button', class: 'orx-pt', text: n }, wrap);
      b.addEventListener('click', function () { etat.actif = n; etat.render(); });
      btns[n] = b;
    });
    return function maj() {
      noms.forEach(function (n) {
        btns[n].className = 'orx-pt' + (etat.actif === n ? ' on' : '') + (etat.pos[n] !== undefined ? ' ok' : '');
        btns[n].textContent = etat.pos[n] !== undefined ? n + ' ✓' : n;
      });
    };
  }

  // ── Droite graduée ──
  function droite(container, o, onInsert) {
    var box = bloc(container, o.titre || 'Place les points sur la droite graduée');
    var noms = o.points || [];
    var etat = { actif: noms[0], pos: {} };
    var pas = o.pas || 1, pasP = o.pas_placement || pas, etiq = o.etiquettes || pas;
    // Largeur de dessin adaptée à l'écran : le texte garde une taille lisible sur téléphone
    var W = Math.max(330, Math.min(640, (container.clientWidth || 640) - 26)), H = 110, PAD = 22, Y = 62;
    var X = function (v) { return PAD + (v - o.min) / (o.max - o.min) * (W - 2 * PAD); };
    var majPts = choixPoints(box, noms, etat);
    var svg = svgEl('svg', { viewBox: '0 0 ' + W + ' ' + H, role: 'img', 'aria-label': 'Droite graduée' }, box);
    var aide = el('p', { class: 'orx-aide', text: 'Choisis un point ci-dessus, puis touche la droite pour le placer. Touche à nouveau pour le déplacer.' }, box);

    svg.addEventListener('click', function (e) {
      if (!etat.actif) return;
      var p = svgPoint(svg, e);
      var v = o.min + (p.x - PAD) / (W - 2 * PAD) * (o.max - o.min);
      etat.pos[etat.actif] = snap(v, pasP, o.min, o.max);
      var reste = noms.filter(function (n) { return etat.pos[n] === undefined; });
      if (reste.length) etat.actif = reste[0];
      etat.render();
    });

    function texte() {
      var places = noms.filter(function (n) { return etat.pos[n] !== undefined; });
      if (!places.length) return '';
      var t = 'Sur la droite graduée : ' + places.map(function (n) { return n + ' = ' + fmt(etat.pos[n]); }).join(' ; ');
      var manquants = noms.filter(function (n) { return etat.pos[n] === undefined; });
      return t + (manquants.length ? ' (non placé : ' + manquants.join(', ') + ')' : '') + '.';
    }
    var majPied = pied(box, onInsert, texte, function () { etat.pos = {}; etat.actif = noms[0]; etat.render(); });

    etat.render = function () {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      svgEl('line', { x1: PAD - 8, y1: Y, x2: W - PAD + 14, y2: Y, stroke: GRIS, 'stroke-width': 2 }, svg);
      svgEl('path', { d: 'M' + (W - PAD + 14) + ',' + Y + ' l-9,-5 v10 z', fill: GRIS }, svg);
      var n = Math.round((o.max - o.min) / pas);
      for (var i = 0; i <= n; i++) {
        var v = Math.round((o.min + i * pas) * 1000) / 1000, x = X(v);
        var grand = Math.abs((v / etiq) - Math.round(v / etiq)) < 1e-6;
        svgEl('line', { x1: x, y1: Y - (grand ? 8 : 5), x2: x, y2: Y + (grand ? 8 : 5), stroke: GRIS, 'stroke-width': grand ? 2 : 1 }, svg);
        if (grand) svgEl('text', { x: x, y: Y + 26, 'font-size': 14, 'text-anchor': 'middle', fill: '#6b7280', text: fmt(v) }, svg);
      }
      (o.deja || []).forEach(function (d) {
        var x = X(d.x);
        svgEl('circle', { cx: x, cy: Y, r: 5, fill: GRIS }, svg);
        svgEl('text', { x: x, y: Y - 16, 'font-size': 14, 'font-weight': 700, 'text-anchor': 'middle', fill: GRIS, text: d.nom }, svg);
      });
      noms.forEach(function (nom) {
        if (etat.pos[nom] === undefined) return;
        var x = X(etat.pos[nom]);
        svgEl('circle', { cx: x, cy: Y, r: 6, fill: INDIGO }, svg);
        svgEl('text', { x: x, y: Y - 16, 'font-size': 15, 'font-weight': 800, 'text-anchor': 'middle', fill: INDIGO, text: nom }, svg);
      });
      majPts();
      majPied(texte());
    };
    etat.render();
  }

  // ── Repère ──
  function repere(container, o, onInsert) {
    var box = bloc(container, o.titre || 'Place les points dans le repère');
    var noms = o.points || [];
    var etat = { actif: noms[0], pos: {} };
    var px = o.pasx || 1, py = o.pasy || 1, ex = o.etiquettesx || px, ey = o.etiquettesy || py;
    var nx = (o.xmax - o.xmin), ny = (o.ymax - o.ymin);
    var PAD = 26;
    var L = Math.max(300, Math.min(380, (container.clientWidth || 432) - 78));
    var W = PAD * 2 + L, H = PAD * 2 + Math.max(160, Math.min(420, L * ny / nx));
    var sx = (W - 2 * PAD) / nx, sy = (H - 2 * PAD) / ny;
    var X = function (v) { return PAD + (v - o.xmin) * sx; };
    var Yf = function (v) { return H - PAD - (v - o.ymin) * sy; };
    var majPts = choixPoints(box, noms, etat);
    var svg = svgEl('svg', { viewBox: '0 0 ' + W + ' ' + H, role: 'img', 'aria-label': 'Repère' }, box);
    el('p', { class: 'orx-aide', text: 'Choisis un point ci-dessus, puis touche le repère à l\'endroit voulu (le point s\'aligne sur le quadrillage).' }, box);

    svg.addEventListener('click', function (e) {
      if (!etat.actif) return;
      var p = svgPoint(svg, e);
      var x = snap(o.xmin + (p.x - PAD) / sx, px, o.xmin, o.xmax);
      var y = snap(o.ymin + (H - PAD - p.y) / sy, py, o.ymin, o.ymax);
      etat.pos[etat.actif] = [x, y];
      var reste = noms.filter(function (n) { return etat.pos[n] === undefined; });
      if (reste.length) etat.actif = reste[0];
      etat.render();
    });

    function texte() {
      var places = noms.filter(function (n) { return etat.pos[n] !== undefined; });
      if (!places.length) return '';
      var t = 'Dans le repère : ' + places.map(function (n) { return n + '(' + fmt(etat.pos[n][0]) + ' ; ' + fmt(etat.pos[n][1]) + ')'; }).join(' ; ');
      var manquants = noms.filter(function (n) { return etat.pos[n] === undefined; });
      return t + (manquants.length ? ' (non placé : ' + manquants.join(', ') + ')' : '') + '.';
    }
    var majPied = pied(box, onInsert, texte, function () { etat.pos = {}; etat.actif = noms[0]; etat.render(); });

    etat.render = function () {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      var i, v;
      for (i = 0; i <= Math.round(nx / px); i++) { v = o.xmin + i * px; svgEl('line', { x1: X(v), y1: Yf(o.ymin), x2: X(v), y2: Yf(o.ymax), stroke: '#eef0f3', 'stroke-width': 1 }, svg); }
      for (i = 0; i <= Math.round(ny / py); i++) { v = o.ymin + i * py; svgEl('line', { x1: X(o.xmin), y1: Yf(v), x2: X(o.xmax), y2: Yf(v), stroke: '#eef0f3', 'stroke-width': 1 }, svg); }
      var x0 = Math.min(Math.max(0, o.xmin), o.xmax), y0 = Math.min(Math.max(0, o.ymin), o.ymax);
      svgEl('line', { x1: X(o.xmin), y1: Yf(y0), x2: X(o.xmax), y2: Yf(y0), stroke: GRIS, 'stroke-width': 2 }, svg);
      svgEl('line', { x1: X(x0), y1: Yf(o.ymin), x2: X(x0), y2: Yf(o.ymax), stroke: GRIS, 'stroke-width': 2 }, svg);
      for (i = 0; i <= Math.round(nx / px); i++) {
        v = Math.round((o.xmin + i * px) * 1000) / 1000;
        if (v !== 0 && Math.abs(v / ex - Math.round(v / ex)) < 1e-6) svgEl('text', { x: X(v), y: Yf(y0) + 15, 'font-size': 13, 'text-anchor': 'middle', fill: '#6b7280', text: fmt(v) }, svg);
      }
      for (i = 0; i <= Math.round(ny / py); i++) {
        v = Math.round((o.ymin + i * py) * 1000) / 1000;
        if (v !== 0 && Math.abs(v / ey - Math.round(v / ey)) < 1e-6) svgEl('text', { x: X(x0) - 6, y: Yf(v) + 4, 'font-size': 13, 'text-anchor': 'end', fill: '#6b7280', text: fmt(v) }, svg);
      }
      svgEl('text', { x: X(x0) - 6, y: Yf(y0) + 15, 'font-size': 13, 'text-anchor': 'end', fill: '#6b7280', text: '0' }, svg);
      (o.deja || []).forEach(function (d) {
        svgEl('circle', { cx: X(d.x), cy: Yf(d.y), r: 4.5, fill: GRIS }, svg);
        svgEl('text', { x: X(d.x) + 7, y: Yf(d.y) - 7, 'font-size': 15, 'font-weight': 700, fill: GRIS, text: d.nom }, svg);
      });
      noms.forEach(function (nom) {
        if (etat.pos[nom] === undefined) return;
        var p = etat.pos[nom];
        svgEl('circle', { cx: X(p[0]), cy: Yf(p[1]), r: 5.5, fill: INDIGO }, svg);
        svgEl('text', { x: X(p[0]) + 8, y: Yf(p[1]) - 8, 'font-size': 16, 'font-weight': 800, fill: INDIGO, text: nom }, svg);
      });
      majPts();
      majPied(texte());
    };
    etat.render();
  }

  // ── Tableau à compléter ──
  function tableau(container, o, onInsert) {
    var box = bloc(container, o.titre || 'Complète le tableau');
    var wrap = el('div', { class: 'orx-tab' }, box);
    var table = el('table', {}, wrap);
    var champs = [];
    var enteteL = o.entete_ligne !== false, enteteC = o.entete_colonne !== false;
    var large = (o.lignes[0] || []).length <= 4;
    o.lignes.forEach(function (ligne, i) {
      var tr = el('tr', {}, table);
      ligne.forEach(function (cell, j) {
        var isHead = (enteteL && i === 0) || (enteteC && j === 0);
        var td = el(isHead ? 'th' : 'td', {}, tr);
        if (cell === null) {
          var input;
          if (o.choix) {
            input = el('select', { 'aria-label': 'Case ' + (i + 1) + '-' + (j + 1) }, td);
            el('option', { value: '', text: '…' }, input);
            o.choix.forEach(function (c) { el('option', { value: c, text: c }, input); });
          } else {
            input = el('input', { type: 'text', inputmode: 'text', 'aria-label': 'Case ' + (i + 1) + '-' + (j + 1), class: large ? 'large' : '' }, td);
          }
          input.addEventListener('input', majTout);
          input.addEventListener('change', majTout);
          champs.push(input);
          td._input = input;
        } else {
          td.textContent = typeof cell === 'number' ? fmt(cell) : cell;
        }
      });
    });
    function texte() {
      if (!champs.some(function (c) { return c.value.trim(); })) return '';
      var lignes = Array.prototype.map.call(table.rows, function (tr) {
        return '| ' + Array.prototype.map.call(tr.cells, function (td) { return td._input ? (td._input.value.trim() || '…') : td.textContent; }).join(' | ') + ' |';
      });
      return 'Tableau complété :\n' + lignes.join('\n');
    }
    var majPied = pied(box, onInsert, texte, function () { champs.forEach(function (c) { c.value = ''; }); majTout(); });
    function majTout() {
      var rempli = champs.filter(function (c) { return c.value.trim(); }).length;
      majPied(rempli + ' case' + (rempli > 1 ? 's' : '') + ' remplie' + (rempli > 1 ? 's' : '') + ' sur ' + champs.length);
    }
    majTout();
  }

  var OUTILS = { droite: droite, repere: repere, tableau: tableau };

  function mount(container, outils, onInsert) {
    if (!container || !Array.isArray(outils) || !outils.length) return { destroy: function () {} };
    injectStyle();
    var root = el('div', { class: 'orx-root' }, container);
    outils.forEach(function (o) { if (OUTILS[o.type]) OUTILS[o.type](root, o, onInsert); });
    return { destroy: function () { if (root.parentNode) root.parentNode.removeChild(root); } };
  }

  global.OutilsReponse = { mount: mount, fmt: fmt };
})(typeof window !== 'undefined' ? window : globalThis);

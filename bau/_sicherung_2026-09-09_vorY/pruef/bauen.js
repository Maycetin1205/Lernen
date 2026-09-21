#!/usr/bin/env node
// Setzt die Kapitel-Fragmente zur fertigen Datei zusammen, erzeugt Glossar (91) und
// Quellenverzeichnis (92) aus den Kapiteln und ruft danach check.js auf.
// Aufruf:  node bau/pruef/bauen.js          (aus dem Ordner Lernen/)
'use strict';
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const root = path.resolve(__dirname, '..', '..');        // Lernen/
const kapDir = path.join(root, 'bau', 'kapitel');
const ziel = path.join(root, 'AP1_Lerndatei.html');

const dateien = fs.readdirSync(kapDir).filter(f => /^\d{2}-.+\.html$/.test(f)).sort();
const teile = {};
for (const f of dateien) teile[f] = fs.readFileSync(path.join(kapDir, f), 'utf8');

const strip = x => (x || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
const esc = x => x.replace(/&(?![a-zA-Z#0-9]+;)/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const istKapitel = f => /^(1\d|2\d|30)-/.test(f);

// Glossar aus Begriffskarten
const eintraege = [];
for (const f of dateien) {
  if (!istKapitel(f)) continue;
  const t = teile[f];
  const kapId = (t.match(/<section class="kapitel" id="([^"]+)"/) || [])[1] || '?';
  const re = /<dl class="begriff" id="([^"]+)">\s*<dt>([\s\S]*?)<\/dt>/g;
  let m;
  while ((m = re.exec(t))) eintraege.push({ id: m[1], begriff: strip(m[2].replace(/<span class="en">[\s\S]*?<\/span>/, '')), kapId });
}
eintraege.sort((a, b) => a.begriff.localeCompare(b.begriff, 'de'));
const glossar =
`<section class="teil" id="glossar">
<p class="kapitel-nr">Teil 4</p>
<h2>Glossar</h2>
<p class="unter">Jeder Begriff führt zu seiner Begriffskarte. Die Kennung dahinter ist das Kapitel.</p>
<ul class="glossar">
${eintraege.map(e => `<li><a href="#${e.id}">${esc(e.begriff)}</a><span class="wo">${e.kapId.toUpperCase()}</span></li>`).join('\n')}
</ul>
</section>
`;

// Quellenverzeichnis aus den Kapitelquellen, zusammengeführt über data-src
const quellen = {};
for (const f of dateien) {
  if (!istKapitel(f) && !/^0[23]-/.test(f)) continue;
  const re = /<li id="([^"]+)" data-src="([^"]+)"[^>]*>([\s\S]*?)<\/li>/g;
  let m;
  while ((m = re.exec(teile[f]))) {
    if (!quellen[m[2]]) quellen[m[2]] = { html: m[3].trim(), wo: [] };
    quellen[m[2]].wo.push(m[1]);
  }
}
const typRang = { Gesetz: 0, Norm: 1, RFC: 2, 'Behörde': 3, Hersteller: 4, Fachbuch: 5, 'IHK-Prüfung': 6, 'IHK-Konvention': 7 };
const typVon = h => (h.match(/<span class="typ">([^<]+)<\/span>/) || [, ''])[1];
const schluessel = Object.keys(quellen).sort((a, b) => {
  const ta = typRang[typVon(quellen[a].html)] ?? 9, tb = typRang[typVon(quellen[b].html)] ?? 9;
  if (ta !== tb) return ta - tb;
  return strip(quellen[a].html).localeCompare(strip(quellen[b].html), 'de');
});
const verzeichnis =
`<section class="teil" id="quellen">
<p class="kapitel-nr">Teil 5</p>
<h2>Quellenverzeichnis</h2>
<p class="unter">Alle Quellen der Kapitel, nach Typ geordnet. Die Kennungen dahinter führen zur Verwendung im jeweiligen Kapitel.</p>
<ol class="quellenliste">
${schluessel.map(k => `<li>${quellen[k].html}<span class="wo">${quellen[k].wo.map(w => `<a href="#${w}">${w.split('-q')[0].toUpperCase()}</a>`).join(' ')}</span></li>`).join('\n')}
</ol>
</section>
`;

fs.writeFileSync(path.join(kapDir, '91-glossar.html'), glossar);
fs.writeFileSync(path.join(kapDir, '92-quellen.html'), verzeichnis);
teile['91-glossar.html'] = glossar;
teile['92-quellen.html'] = verzeichnis;

const reihenfolge = Object.keys(teile).sort();
const fehlend = ['00-kopf.html', '01-benutzung.html', '02-pruefung.html', '03-matrix.html', '90-verfahrensblatt.html', '99-fuss.html'].filter(f => !teile[f]);
if (fehlend.length) console.log('Achtung, es fehlen: ' + fehlend.join(', '));

const out = reihenfolge.map(f => teile[f].replace(/\s+$/, '')).join('\n\n');
fs.writeFileSync(ziel, out, 'utf8');
console.log(`Zusammengesetzt: ${reihenfolge.length} Teile, ${(Buffer.byteLength(out, 'utf8') / 1024).toFixed(0)} KB, ${eintraege.length} Glossareinträge, ${schluessel.length} Quellen → ${ziel}`);

try {
  execFileSync(process.execPath, [path.join(__dirname, 'check.js'), ziel], { stdio: 'inherit' });
} catch (e) {
  process.exit(1);
}

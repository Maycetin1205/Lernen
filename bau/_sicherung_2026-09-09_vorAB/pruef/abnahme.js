// Deterministische Abnahmepruefung nach BAUPLAN §12 Punkt 3 und 4 ueber alle vorhandenen Fragmente.
const fs = require('fs'), path = require('path');
const BAU = 'C:/Users/mu.aycetin/Desktop/Lernen/bau';
const K = path.join(BAU, 'kapitel');
const CR = new RegExp(String.fromCharCode(13), 'g');
const lies = p => fs.readFileSync(path.join(BAU, p), 'utf8').replace(CR, '');
const fehler = [], ok = [];

// ---------- MATRIX Tabelle 2: je Kapitel die Teilaufgabenliste ----------
const matrix = lies('notizen/MATRIX.md');
const soll = {};
for (const m of matrix.matchAll(/^### (A\d|B\d{1,2}) [^\n]*\n\s*\n([^\n]+)/gm)) {
  const map = new Map();
  for (const t of m[2].matchAll(/\b([FH]2\d)\s+(\d+\.\d+)\s+\((\d+)\s*P\)/g)) map.set(t[1] + ' ' + t[2], Number(t[3]));
  if (map.size) soll[m[1].toLowerCase()] = map;
}

// ---------- Quellenlisten ----------
const qkeys = new Map();
for (const f of ['notizen/QUELLEN-A.md', 'notizen/QUELLEN-B.md']) {
  for (const z of lies(f).split('\n')) {
    const s = z.split('|').map(x => x.trim());
    if (s.length >= 9 && /^[a-z0-9][a-z0-9.-]*$/.test(s[1]) && s[1] !== 'Schlüssel') {
      qkeys.set(s[1], { typ: s[3], url: s[5], status: s[6], datum: s[7] });
    }
  }
}

const kurz = (saison, jahr) => (saison === 'Herbst' ? 'H' : 'F') + jahr.slice(2);
const alleIds = new Map();
const dateien = fs.readdirSync(K).filter(f => /^\d\d-[ab]\d+\.html$/.test(f)).sort();

for (const datei of dateien) {
  const s = fs.readFileSync(path.join(K, datei), 'utf8').replace(CR, '');
  const kap = (s.match(/<section class="kapitel" id="([^"]+)"/) || [])[1];
  if (!kap) { fehler.push(datei + ': keine Kapitel-section'); continue; }
  if (!soll[kap]) { fehler.push(kap + ': kein Abschnitt in MATRIX.md Tabelle 2 gefunden'); continue; }

  // §12.3 kam-dran gegen MATRIX
  const kd = (s.match(/<p class="kam-dran">([\s\S]*?)<\/p>/) || [])[1] || '';
  const ist = new Set();
  let kapSummeIst = 0;
  for (const sp of kd.matchAll(/<span>AP1 (Frühjahr|Herbst) (20\d\d), ([^(]+)\((\d+)\s*P\)<\/span>/g)) {
    const pre = kurz(sp[1], sp[2]);
    const nummern = [];
    for (const teil of sp[3].split(',').map(x => x.trim()).filter(Boolean)) {
      const sp2 = teil.match(/^(\d+)\.(\d+)\s+bis\s+(?:(\d+)\.)?(\d+)$/);
      if (sp2) { for (let i = +sp2[2]; i <= +sp2[4]; i++) nummern.push(sp2[1] + '.' + i); }
      else if (/^\d+\.\d+$/.test(teil)) nummern.push(teil);
      else fehler.push(kap + ': kam-dran, unlesbarer Eintrag "' + teil + '"');
    }
    let summe = 0;
    for (const n of nummern) {
      const key = pre + ' ' + n;
      if (ist.has(key)) fehler.push(kap + ': ' + key + ' steht doppelt in der kam-dran-Zeile');
      ist.add(key);
      const p = soll[kap].get(key);
      if (p === undefined) fehler.push(kap + ': kam-dran nennt ' + key + ', in MATRIX.md nicht diesem Kapitel zugeordnet');
      else summe += p;
    }
    if (summe !== Number(sp[4])) fehler.push(kap + ': kam-dran ' + pre + ' nennt ' + sp[4] + ' P, MATRIX ergibt ' + summe + ' P');
    kapSummeIst += Number(sp[4]);
  }
  for (const key of soll[kap].keys()) if (!ist.has(key)) fehler.push(kap + ': MATRIX-Teilaufgabe ' + key + ' fehlt in der kam-dran-Zeile');
  const sollSumme = [...soll[kap].values()].reduce((a, b) => a + b, 0);
  ok.push(kap.toUpperCase().padEnd(4) + String(ist.size).padStart(3) + '/' + String(soll[kap].size).padStart(2) + ' Teilaufgaben   ' +
          String(kapSummeIst).padStart(3) + '/' + String(sollSumme).padStart(3) + ' P   ' + (ist.size === soll[kap].size && kapSummeIst === sollSumme ? 'ok' : 'ABWEICHUNG'));

  // §12.4 URLs
  for (const a of s.matchAll(/<a href="(https?:\/\/[^"]+)"/g)) {
    const url = a[1];
    let treffer = null;
    for (const [k, v] of qkeys) {
      if (!v.url || v.url === '–') continue;
      const a1 = v.url.replace(/\.txt$/, ''), a2 = url.replace(/\.txt$/, '');
      if (v.url === url || a1 === a2) { treffer = [k, v]; break; }
    }
    if (!treffer) fehler.push(kap + ': URL steht in keiner Quellenliste: ' + url);
    else if (!/geprüft/.test(treffer[1].status)) fehler.push(kap + ': URL verlinkt, Status ist aber "' + treffer[1].status + '": ' + url);
  }
  for (const d of s.matchAll(/data-src="([^"]+)"/g)) if (!qkeys.has(d[1])) fehler.push(kap + ': data-src="' + d[1] + '" steht in keiner Quellenliste');
  for (const li of s.matchAll(/<li id="[^"]+" data-src="([^"]+)">([\s\S]*?)<\/li>/g)) {
    const v = qkeys.get(li[1]);
    if (v && !/geprüft/.test(v.status) && /<a href="http/.test(li[2])) fehler.push(kap + ': Quelle ' + li[1] + ' hat Status "' + v.status + '", traegt aber einen Link');
  }
  for (const i of s.matchAll(/\sid="([^"]+)"/g)) {
    if (alleIds.has(i[1])) fehler.push('doppelte id "' + i[1] + '" in ' + datei + ' und ' + alleIds.get(i[1]));
    else alleIds.set(i[1], datei);
  }
}

console.log('Geprueft: ' + dateien.length + ' Fragmente, ' + alleIds.size + ' ids, ' + qkeys.size + ' Quellenschluessel, ' + Object.keys(soll).length + ' Kapitel in MATRIX.\n');
console.log('KAP  Teilaufgaben      Punkte   Abgleich MATRIX');
console.log(ok.join('\n'));
console.log('\n' + (fehler.length ? 'BEFUNDE (' + fehler.length + '):\n- ' + fehler.join('\n- ') : 'Keine Befunde.'));

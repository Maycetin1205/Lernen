const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const chapterDir = path.join(root, 'kapitel');
const files = fs.readdirSync(chapterDir)
  .filter((name) => /^(1[0-8]-a[1-9]|2\d-b\d+|30-b11)\.html$/.test(name) && name !== '15-a6.html')
  .sort();

function topLevelParts(html) {
  const bodyStart = html.indexOf('>') + 1;
  const bodyEnd = html.lastIndexOf('</section>');
  const body = html.slice(bodyStart, bodyEnd);
  const parts = [];
  const tag = /<\/?(header|section)\b[^>]*>/gi;
  let depth = 0;
  let start = -1;
  let kind = '';
  let match;
  while ((match = tag.exec(body))) {
    const closing = match[0].startsWith('</');
    if (!closing) {
      if (depth === 0) {
        start = match.index;
        kind = match[1].toLowerCase();
      }
      depth += 1;
    } else {
      depth -= 1;
      if (depth === 0 && start >= 0) {
        parts.push({ kind, html: body.slice(start, tag.lastIndex) });
        start = -1;
      }
    }
  }
  return { open: html.slice(0, bodyStart), close: html.slice(bodyEnd), parts };
}

for (const name of files) {
  const file = path.join(chapterDir, name);
  const source = fs.readFileSync(file, 'utf8');
  const id = source.match(/<section class="kapitel" id="([ab]\d+)"/)?.[1];
  if (!id) throw new Error(`Kapitel-id fehlt: ${name}`);
  const groupA = id.startsWith('a');
  const parsed = topLevelParts(source);
  const byId = new Map();
  let header = '';
  for (const part of parsed.parts) {
    if (part.kind === 'header') header = part.html;
    else {
      const sectionId = part.html.match(/^<section id="([^"]+)"/)?.[1];
      if (sectionId) byId.set(sectionId, part.html);
    }
  }
  const nav = `<nav class="kapitel-wege" aria-label="Abschnitte dieses Kapitels"><a href="#${id}-worum">Worum es geht</a><a href="#${id}-kern">${groupA ? 'Das Verfahren' : 'Die Sache'}</a><a href="#${id}-original">So hat die IHK gefragt</a><a href="#${id}-variante">Jetzt du</a><a href="#${id}-selbstcheck">Selbstcheck</a><a href="#${id}-begriffe">Begriffe</a><a href="#${id}-quellen">Quellen</a></nav>`;
  header = header.replace(/<nav class="kapitel-wege"[\s\S]*?<\/nav>/, nav);
  let terms = byId.get(`${id}-begriffe`);
  if (!terms) throw new Error(`Begriffe fehlen: ${name}`);
  terms = terms.replace(/<h3>Begriffe(?: zum Nachschlagen)?<\/h3>/, '<h3>Begriffe zum Nachschlagen</h3>');
  if (!terms.includes('<p class="unter">')) {
    const helper = groupA
      ? 'Nicht durchlesen. Wenn dir im Verfahren oder in einer Aufgabe ein Wort fehlt, schlag es hier nach.'
      : 'Nicht durchlesen. Wenn dir in der Sache oder in einer Aufgabe ein Wort fehlt, schlag es hier nach.';
    terms = terms.replace('</h3>', `</h3>\n  <p class="unter">${helper}</p>`);
  }
  byId.set(`${id}-begriffe`, terms);
  const order = ['worum', 'kern', 'original', 'variante', 'selbstcheck', 'begriffe', 'quellen'];
  const missing = order.filter((part) => !byId.has(`${id}-${part}`));
  if (missing.length) throw new Error(`${name}: Abschnitte fehlen: ${missing.join(', ')}`);
  const rebuilt = `${parsed.open}\n\n${header}\n\n${order.map((part) => byId.get(`${id}-${part}`)).join('\n\n')}\n\n${parsed.close}`;
  fs.writeFileSync(file, rebuilt, 'utf8');
}

console.log(`${files.length} Kapitel in die verbindliche Abschnittsfolge gebracht.`);

const a1File = path.join(chapterDir, '10-a1.html');
const a1Source = fs.readFileSync(a1File, 'utf8');
const a1Parsed = topLevelParts(a1Source);
const replacements = new Map([
  ['a1-kern', fs.readFileSync(path.join(root, 'notizen', '_a1-kern-neu.html'), 'utf8').trim()],
  ['a1-begriffe', fs.readFileSync(path.join(root, 'notizen', '_a1-begriffe-neu.html'), 'utf8').trim()],
]);
const a1Parts = a1Parsed.parts.map((part) => {
  if (part.kind !== 'section') return part.html;
  const sectionId = part.html.match(/^<section id="([^"]+)"/)?.[1];
  return replacements.get(sectionId) || part.html;
});
fs.writeFileSync(a1File, `${a1Parsed.open}\n\n${a1Parts.join('\n\n')}\n\n${a1Parsed.close}`, 'utf8');
console.log('A1 nach dem Lehrer-Entwurf aufgebaut.');

const problemTitles = {
  a2: 'Angebote, Raten und Mengen vergleichbar machen',
  a3: 'Mehrere Angebote fair bewerten',
  a4: 'Bit, Byte und Übertragungszeit zusammenrechnen',
  a5: 'Verbrauch und Kosten ausrechnen',
  a7: 'Programmabläufe ohne Raten verfolgen',
  a8: 'Anforderungen als Diagramm zeigen',
  a9: 'Daten ohne Doppelungen ordnen',
  b1: 'Eine Bedrohung der richtigen Schutzmaßnahme zuordnen',
  b2: 'Daten und Identitäten schützen',
  b3: 'Personendaten rechtmäßig behandeln',
  b4: 'Passende Hardware erkennen und auswählen',
  b5: 'Einen Netzwerkfehler von unten nach oben finden',
  b6: 'Software, Lizenz und Webtechnik passend auswählen',
  b7: 'Datenverlust und Ausfall vermeiden',
  b8: 'Einen sicheren, zugänglichen Arbeitsplatz einrichten',
  b9: 'Aus einem Auftrag einen planbaren Projektweg machen',
  b10: 'Bedarf verstehen und Veränderungen erklären',
  b11: 'Verträge und wirtschaftliche Entscheidungen einordnen',
};

for (const name of files.filter((value) => value !== '10-a1.html')) {
  const file = path.join(chapterDir, name);
  let html = fs.readFileSync(file, 'utf8');
  const id = html.match(/<section class="kapitel" id="([ab]\d+)"/)?.[1];
  const parsed = topLevelParts(html);
  const updatedParts = parsed.parts.map((part) => {
    if (part.kind !== 'section' || !part.html.startsWith(`<section id="${id}-kern">`)) return part.html;
    let core = part.html;
    const overviewMatch = core.match(/\s*<div class="merke" data-art="Auf einen Blick">[\s\S]*?<\/div>/);
    const overview = overviewMatch?.[0].trim();
    if (overview) core = core.replace(overviewMatch[0], '\n');
    if (!core.includes('<h4>Das Problem:')) {
      const heading = `<h4>Das Problem: ${problemTitles[id]}</h4>`;
      if (id.startsWith('a')) core = core.replace(/(<h3>Das Verfahren<\/h3>\s*)/, `$1\n  ${heading}\n`);
      else core = core.replace(/<h4>(.*?)<\/h4>/, `<h4>Das Problem: $1</h4>`);
    }
    if (overview) core = core.replace(/\s*<\/section>$/, `\n\n  ${overview}\n\n</section>`);
    return core;
  });
  html = `${parsed.open}\n\n${updatedParts.join('\n\n')}\n\n${parsed.close}`;
  html = html.replace(/\bklein\b/g, 't2').replace(/\bt2\s+t2\b/g, 't2');
  html = html.replace(/<(line|polyline|path)([^>]*)>/g, (tag, element, attrs) => {
    if (/class="a"/.test(attrs) && /marker-end="url\(#pfeil\)"/.test(attrs)) {
      return tag.replace('url(#pfeil)', 'url(#pfeil-a)');
    }
    return tag;
  });
  fs.writeFileSync(file, html, 'utf8');
}
console.log('Problem-Einstieg und Schlusszusammenfassung in allen übrigen Kapiteln gesetzt.');

// Ersetzt einen Abschnitt eines Kapitels durch eine neue Fassung.
// Aufruf: node pruef/_lehrer_ersetzen.js kapitel/16-a7.html a7-kern notizen/_a7-kern-neu.html
const fs = require('fs');
const path = require('path');

const [chapterArg, sectionId, replacementArg] = process.argv.slice(2);
if (!chapterArg || !sectionId || !replacementArg) {
  console.error('Aufruf: node pruef/_lehrer_ersetzen.js <kapitel> <abschnitt-id> <ersatzdatei>');
  process.exit(1);
}

const root = path.resolve(__dirname, '..');
const chapterFile = path.resolve(root, chapterArg);
const replacementFile = path.resolve(root, replacementArg);

const source = fs.readFileSync(chapterFile, 'utf8');
const bodyStart = source.indexOf('>') + 1;
const bodyEnd = source.lastIndexOf('</section>');
const body = source.slice(bodyStart, bodyEnd);

const tag = /<\/?(header|section)\b[^>]*>/gi;
let depth = 0;
let start = -1;
let found = null;
let match;
while ((match = tag.exec(body))) {
  const closing = match[0].startsWith('</');
  if (!closing) {
    if (depth === 0) start = match.index;
    depth += 1;
  } else {
    depth -= 1;
    if (depth === 0 && start >= 0) {
      const part = body.slice(start, tag.lastIndex);
      if (part.startsWith(`<section id="${sectionId}"`)) {
        found = { start, end: tag.lastIndex, alt: part };
      }
      start = -1;
    }
  }
}

if (!found) {
  console.error(`Abschnitt ${sectionId} nicht gefunden in ${chapterArg}`);
  process.exit(1);
}

const replacement = fs.readFileSync(replacementFile, 'utf8').trim();
if (!replacement.startsWith(`<section id="${sectionId}"`)) {
  console.error(`Ersatzdatei beginnt nicht mit <section id="${sectionId}">`);
  process.exit(1);
}

// Alle ids des alten Abschnitts muessen im neuen wieder vorkommen.
const idsAlt = [...found.alt.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]);
const idsNeu = new Set([...replacement.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]));
const fehlend = idsAlt.filter((id) => !idsNeu.has(id) && !/-abb\d+-t$/.test(id));
if (fehlend.length) {
  console.error(`Fehlende ids im neuen Abschnitt: ${fehlend.join(', ')}`);
  process.exit(1);
}

const neu = source.slice(0, bodyStart) + body.slice(0, found.start) + replacement + body.slice(found.end) + source.slice(bodyEnd);
fs.writeFileSync(chapterFile, neu, 'utf8');
console.log(`${sectionId} ersetzt (${found.alt.length} -> ${replacement.length} Zeichen).`);

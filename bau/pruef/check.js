#!/usr/bin/env node
// Prüft ein Kapitel-Fragment (--fragment) oder die zusammengesetzte Datei.
// Aufruf:  node bau/pruef/check.js <datei.html> [--fragment]
// Exit 0 = keine Fehler. Exit 1 = Fehler (Liste auf stdout). Hinweise sind keine Fehler.
'use strict';
const fs = require('fs');

const file = process.argv[2];
const fragment = process.argv.includes('--fragment');
if (!file) { console.error('Aufruf: node check.js <datei.html> [--fragment]'); process.exit(2); }
const s = fs.readFileSync(file, 'utf8');
const errs = [], warn = [];

// 1) Verbotene Gestaltung, externe Ressourcen, Platzhalter
const verboten = [
  ['linear-gradient', 'Farbverlauf'], ['radial-gradient', 'Farbverlauf'], ['box-shadow', 'Schatten'],
  ['backdrop-filter', 'Blur'], ['@import', 'CSS-Import'], ['fonts.googleapis', 'Webfont'], ['fonts.gstatic', 'Webfont'],
  ['cdn.', 'CDN'], ['<img ', 'img-Element (nur inline SVG erlaubt)'], ['<iframe', 'iframe'],
  ['VORLAGE', 'Vorlagen-Kommentar nicht entfernt'], ['PLATZHALTER', 'Platzhalter nicht ersetzt'],
  ['TODO', 'offener TODO'], ['lorem ipsum', 'Fülltext'], ['<script src', 'externes Skript'],
];
for (const [k, n] of verboten) {
  if (s.toLowerCase().includes(k.toLowerCase())) errs.push(`verboten: ${n} ("${k}")`);
}

// 2) Emoji
if (/\p{Extended_Pictographic}/u.test(s)) errs.push('Emoji gefunden');

// 3) Tag-Balance (script-, style-Inhalt und Kommentare ausgeblendet)
const ohne = s
  .replace(/<script[\s\S]*?<\/script>/gi, '<script></script>')
  .replace(/<style[\s\S]*?<\/style>/gi, '<style></style>')
  .replace(/<!--[\s\S]*?-->/g, '');
const VOID = new Set(['br','hr','img','input','meta','link','col','wbr','source','track','area','base','embed','param','!doctype']);
const stack = [];
const re = /<(\/?)([a-zA-Z!][\w:-]*)((?:"[^"]*"|'[^']*'|[^'"<>])*?)(\/?)>/g;
let m, line = 1, last = 0;
while ((m = re.exec(ohne))) {
  for (let i = last; i < m.index; i++) if (ohne.charCodeAt(i) === 10) line++;
  last = m.index;
  const closing = m[1] === '/', tag = m[2].toLowerCase(), self = m[4] === '/';
  if (VOID.has(tag) || self) continue;
  if (!closing) { stack.push([tag, line]); continue; }
  if (stack.length && stack[stack.length - 1][0] === tag) { stack.pop(); continue; }
  const idx = stack.map(x => x[0]).lastIndexOf(tag);
  if (idx >= 0) {
    errs.push(`Tag-Fehler: </${tag}> in Zeile ${line} schließt, aber noch offen: ${stack.slice(idx + 1).map(x => `<${x[0]}> (Zeile ${x[1]})`).join(', ')}`);
    stack.length = idx;
  } else {
    errs.push(`unerwartetes </${tag}> in Zeile ${line}`);
  }
}
for (const x of stack) errs.push(`nicht geschlossen: <${x[0]}> aus Zeile ${x[1]}`);

// 4) Kapitelstruktur
const kaps = [...s.matchAll(/<section class="kapitel" id="([^"]+)"/g)].map(x => x[1]);
const TEILE = ['worum', 'begriffe', 'kern', 'original', 'variante', 'selbstcheck', 'quellen'];
function kapText(k) {
  const i = s.indexOf(`<section class="kapitel" id="${k}"`);
  const enden = [s.indexOf('<section class="kapitel" id=', i + 10), s.indexOf('<section class="teil" id=', i + 10), s.indexOf('</main>', i + 10)].filter(x => x >= 0);
  const j = enden.length ? Math.min(...enden) : -1;
  return s.slice(i, j < 0 ? undefined : j);
}
function woerter(t) {
  // Nur Lesestoff wird gezählt. Nicht mitgezählt werden Abbildungen, die Sprunglink-Zeilen
  // (nav) und die immer gleichen Beschriftungen der Begriffskarten: das sind Wegweiser
  // und Aufschriften, kein Text, den man liest.
  return t.replace(/<svg[\s\S]*?<\/svg>/g, ' ')
    .replace(/<details class="wegweiser">[\s\S]*?<\/details>/g, ' ')
    .replace(/<nav\b[\s\S]*?<\/nav>/g, ' ')
    .replace(/<span class="label">[^<]*<\/span>/g, ' ')
    .replace(/<[^>]+>/g, ' ').replace(/&[a-z#0-9]+;/g, ' ').split(/\s+/).filter(Boolean).length;
}
for (const k of kaps) {
  const t = kapText(k);
  for (const teil of TEILE) if (!t.includes(`id="${k}-${teil}"`)) errs.push(`${k}: Abschnitt "${teil}" fehlt`);
  const abb = (t.match(/<figure class="abb">/g) || []).length;
  if (abb < 2) errs.push(`${k}: nur ${abb} Abbildung(en), Plan §9 verlangt mindestens 2`);
  if (t.startsWith('<section class="kapitel" id="a') && abb < 3) warn.push(`${k}: nur ${abb} Abbildungen, in Gruppe A sind 3 bis 5 der Richtwert`);
  for (const fig of t.match(/<figure class="abb">[\s\S]*?<\/figure>/g) || []) {
    if (!/<svg[^>]*\brole="img"/.test(fig)) errs.push(`${k}: Abbildung ohne role="img"`);
    if (!/<title id="/.test(fig)) errs.push(`${k}: Abbildung ohne <title>`);
    if (!/<figcaption>Abb\. [AB]\d+-\d+:/.test(fig)) errs.push(`${k}: Bildunterschrift nicht im Format "Abb. <Kapitel>-<Nr>: …"`);
    if (!/viewBox="0 0 640 \d+"/.test(fig)) errs.push(`${k}: Abbildung ohne viewBox="0 0 640 H"`);
  }
  if (!/class="kam-dran"/.test(t)) errs.push(`${k}: Zeile "Kam dran" fehlt`);
  const karten = (t.match(/<dl class="begriff" id="/g) || []).length;
  if (karten < 5) errs.push(`${k}: nur ${karten} Begriffskarten (mindestens 5)`);
  if (karten > 12) warn.push(`${k}: ${karten} Begriffskarten (Richtwert höchstens 10)`);
  // Jede Karte: genau vier dd mit den vier Labels
  for (const karte of t.match(/<dl class="begriff"[\s\S]*?<\/dl>/g) || []) {
    const labels = [...karte.matchAll(/<span class="label">([^<]+)<\/span>/g)].map(x => x[1].trim());
    const soll = ['Was es ist', 'Wo es dir begegnet', 'Nicht verwechseln mit', 'So fragt die IHK'];
    if (labels.join('|') !== soll.join('|')) {
      const dt = (karte.match(/<dt>([\s\S]*?)<\/dt>/) || [, '?'])[1].replace(/<[^>]+>/g, '');
      errs.push(`${k}: Begriffskarte "${dt.trim()}" hat nicht die vier Zeilen ${soll.join('/')}`);
    }
    if (!/<span class="label">Was es ist<\/span>[\s\S]*?<sup class="q">/.test(karte.split('<span class="label">Wo es dir begegnet')[0])) {
      const dt = (karte.match(/<dt>([\s\S]*?)<\/dt>/) || [, '?'])[1].replace(/<[^>]+>/g, '');
      errs.push(`${k}: Begriffskarte "${dt.trim()}": Zeile "Was es ist" ohne Quellenverweis`);
    }
  }
  const originale = (t.match(/class="aufgabe" id="[^"]*-original-\d+"/g) || []).length;
  const varianten = (t.match(/class="aufgabe" id="[^"]*-variante-\d+"/g) || []).length;
  if (originale < 1) errs.push(`${k}: keine Original-Aufgabe`);
  if (originale > 3) warn.push(`${k}: ${originale} Original-Aufgaben (höchstens 3)`);
  if (varianten !== originale) errs.push(`${k}: ${originale} Original-Aufgaben, aber ${varianten} Varianten (muss gleich sein)`);
  const herk = (t.match(/<p class="herkunft">AP1 (Frühjahr|Herbst) 20\d\d, Aufgabe [^,<]+, \d+ Punkte?, sinngemäß wiedergegeben/g) || []).length;
  if (herk < originale) errs.push(`${k}: Herkunftszeile nicht im Format "AP1 <Saison> <Jahr>, Aufgabe <Nr>, <n> Punkte, sinngemäß wiedergegeben"`);
  const checks = (t.match(/<ol class="selbstcheck">[\s\S]*?<\/ol>/) || [''])[0];
  const fragen = (checks.match(/<li>/g) || []).length;
  if (fragen < 3) errs.push(`${k}: Selbstcheck hat ${fragen} Fragen (mindestens 3)`);
  const quellen = (t.match(/<li id="[^"]+" data-src="/g) || []).length;
  if (quellen < 3) errs.push(`${k}: nur ${quellen} Quellen (mindestens 3)`);
  const sup = (t.match(/<sup class="q">/g) || []).length;
  if (sup < 6) warn.push(`${k}: nur ${sup} Quellenverweise im Text`);
  const merke = (t.match(/class="merke" data-art="([^"]+)"/g) || []);
  if (merke.length > 6) warn.push(`${k}: ${merke.length} Merke-Blöcke (höchstens 6)`);
  for (const b of merke) if (!/data-art="(Auf einen Blick|Merke|Typischer Fehler|Prüfungsnotiz|Für die Prüfung reicht)"/.test(b)) errs.push(`${k}: unerlaubter Merke-Typ ${b}`);
  const w = woerter(t);
  // Obergrenze 4500, Ausnahme a7 mit 4700: A7 lehrt Programmlogik von null und traegt seit
  // 2026-09-11 zusaetzlich das Struktogramm (DIN 66261) und den Programmablaufplan (DIN 66001).
  // Die beiden Formen werden in zwei Pruefungsaufgaben verlangt und standen vorher nirgends.
  // Begruendung in ENTSCHEIDUNGEN.md, Abschnitt AF. Alle anderen Kapitel bleiben bei 4500.
  const grenze = k === 'a7' ? 4700 : 4500;
  if (w > grenze) errs.push(`${k}: ${w} Wörter, Obergrenze ${grenze}`);
  else if (w > 3500) warn.push(`${k}: ${w} Wörter, Richtwert 3500`);
  if (w < 900) warn.push(`${k}: nur ${w} Wörter, wirkt unvollständig`);
  if (/style="/.test(t.replace(/<svg[\s\S]*?<\/svg>/g, ''))) warn.push(`${k}: style-Attribut außerhalb von SVG`);
  if (/<h4>/.test(t) && !/<h3>/.test(t)) warn.push(`${k}: h4 ohne h3`);
  // Klassen außerhalb des Systems
  const erlaubt = new Set(['kapitel','kapitel-kopf','kapitel-nr','kam-dran','begriff','label','en','abb','l','f','w','a','fa','d','g','t2','tb','ta','mono','mitte','rechts','tabelle','z','summe','hervor','rechenweg','merke','aufgabe','herkunft','text','inhalt','q','quellenliste','typ','abruf','wo','selbstcheck','teil','unter','klein','glossar','kapitel-wege','begriffsliste','wegweiser']);
  for (const cm of t.matchAll(/class="([^"]+)"/g)) for (const c of cm[1].split(/\s+/)) if (c && !erlaubt.has(c)) errs.push(`${k}: unbekannte Klasse "${c}"`);
}

// 5) Anker und ids
const idListe = [...s.matchAll(/\sid="([^"]+)"/g)].map(x => x[1]);
const ids = new Set(idListe);
const doppelt = [...new Set(idListe.filter((v, i, a) => a.indexOf(v) !== i))];
for (const d of doppelt) errs.push(`doppelte id: ${d}`);
if (!fragment) {
  for (const x of s.matchAll(/href="#([^"]+)"/g)) if (!ids.has(x[1])) errs.push(`toter Anker: #${x[1]}`);
  for (const x of s.matchAll(/url\(#([^)]+)\)/g)) if (!ids.has(x[1])) errs.push(`SVG-Marker fehlt: #${x[1]}`);
} else {
  const abschnitte = [...kaps, ...[...s.matchAll(/<section class="teil" id="([^"]+)"/g)].map(x => x[1])];
  for (const x of s.matchAll(/<sup class="q"><a href="#([^"]+)"/g)) if (!ids.has(x[1])) errs.push(`Quellenverweis ohne Ziel im Fragment: #${x[1]}`);
  for (const x of s.matchAll(/<sup class="q"><a href="#([^"]+)"/g)) {
    const kap = x[1].split('-q')[0];
    if (!s.includes(`<li id="${x[1]}" data-src=`)) errs.push(`Quellenverweis #${x[1]} zeigt auf keine Quelle mit data-src`);
    if (!abschnitte.includes(kap)) errs.push(`Quellenverweis #${x[1]} gehört zu keinem Abschnitt dieses Fragments`);
  }
}

// 6) Sprachregeln (nur Fließtext, ohne SVG, pre, code)
const fliess = s.replace(/<svg[\s\S]*?<\/svg>|<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>|<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/g, '');
const sprach = [
  [/\bIn diesem Kapitel\b/, 'Füllphrase "In diesem Kapitel"'],
  [/\blernst du\b/i, 'Füllphrase "lernst du"'],
  [/[a-zäöüß]![\s<]/, 'Ausrufezeichen im Fließtext'],
  [/\bLesezeit\b/i, 'Lesezeit-Angabe (verboten)'],
  [/\b\d+\s?(Minuten|Min\.)\s+(pro|am|täglich|je)\b/i, 'Zeitvorgabe für den Lernenden (verboten)'],
  [/\b(Tag|Woche)\s+\d+\b/, 'Tages-/Wochenplan (verboten)'],
  [/\bKI\b.*\bgeneriert\b/i, 'Selbstbezug auf KI'],
  [/—/, 'Geviertstrich (Gedankenstrich als „ – “ setzen)'],
];
for (const [r, n] of sprach) if (r.test(fliess)) warn.push(`${n} gefunden`);
if (/<(b|i|u|font|center)[\s>]/.test(fliess)) warn.push('veraltete Tags b/i/u/font/center (strong/em verwenden)');

// 7) Datei-Ebene
if (!fragment) {
  if (!/<!doctype html>/i.test(s)) errs.push('doctype fehlt');
  if ((s.match(/<main/g) || []).length !== 1) errs.push('main fehlt oder mehrfach');
  const soll = ['benutzung','pruefung','matrix','a1','a2','a3','a4','a5','a6','a7','a8','a9','b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','verfahrensblatt','glossar','quellen'];
  for (const id of soll) if (!ids.has(id)) errs.push(`Abschnitt fehlt: #${id}`);
  const kb = Buffer.byteLength(s, 'utf8') / 1024;
  if (kb > 3072) errs.push(`Datei ${kb.toFixed(0)} KB, Obergrenze 3072 KB`);
}

console.log(errs.length ? `FEHLER (${errs.length}):\n- ${errs.join('\n- ')}` : 'Keine Fehler.');
if (warn.length) console.log(`HINWEISE (${warn.length}):\n- ${warn.join('\n- ')}`);
process.exit(errs.length ? 1 : 0);

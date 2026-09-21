'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..');
const append=(f,s)=>fs.appendFileSync(path.join(root,f),s);
const text=f=>fs.readFileSync(path.join(root,f),'utf8');
const notes=`
## Abschlussprüfung K-2, 2026-09-03

Die vorhandenen Fragmente A5–A9 wurden fachlich korrigiert. Ausführung der erneuten
Rechnungen: node bau/pruef/k2-abschluss-check.js; Eingaben und Ergebnisse stehen in
k2-pruefung/NACHRECHNUNG.txt. Die bisherigen Abschnitte dokumentieren den Vorzustand.
Maßgeblich ist das korrigierte Kapitel; umsortierte Originale und Varianten sind über
ihre Prüfungsherkunft zuzuordnen, nicht über die frühere laufende Nummer.
`;
for(const k of ['a5','a6','a7','a8','a9'])append(`notizen/RECHNUNGEN-${k}.md`,notes);
append('notizen/RECHNUNGEN-a8.md',`
Korrektur der Klassenvariante: Notebook 12 × 5 = 60 EUR; Beamer 25 × 5 + 10 = 135 EUR.
Die zusätzliche Einrichtungspauschale begründet ein tatsächlich anderes Verfahren.
Der alte Wert 125 EUR und die Begründung allein mit unterschiedlichen Tagessätzen sind ersetzt.
include und extend sind UML-Beziehungsarten, keine zusätzlichen Stereotype.
Alternative Kontrollflüsse werden vor einer gemeinsamen Aktion per Merge vereinigt.
`);
append('notizen/RECHNUNGEN-a6.md',`
Quellenpräzisierung F25: Die Antwortdatei ist ein ausgefülltes Aufgabenheft, keine amtliche
Musterlösung. Die erneute Rechnung bestätigt die Zahlen unabhängig; eine amtliche
Feinverteilung der neun Punkte ist dadurch nicht belegt.
`);
append('notizen/RECHNUNGEN-a7.md',`
Quellenpräzisierung: Vier Punkte je F25-Aufruf beziehungsweise je H21-Fehler sind nur
abgeleitete Übungsgewichtungen. Die jeweiligen Gesamtpunkte sind belegt.
`);
const stats=[];
for(const[n,k]of [['14-a5','a5'],['15-a6','a6'],['16-a7','a7'],['17-a8','a8'],['18-a9','a9']]){
 const s=text('kapitel/'+n+'.html');
 const w=s.replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/&[a-z#0-9]+;/g,' ').split(/\s+/).filter(Boolean).length;
 stats.push(`${n}.html: ${w} Wörter, ${(s.match(/<figure /g)||[]).length} SVG-Abbildungen, ${(s.match(/<dl class="begriff"/g)||[]).length} Begriffskarten.`);
 const matrix=text('notizen/MATRIX.md').split(`### ${k.toUpperCase()} ·`)[1].split('\n### ')[0];
 const expected=[...matrix.matchAll(/([HF])(\d{2}) (\d+\.\d+) \((\d+) P\)/g)].map(m=>({exam:m[1]+m[2],task:m[3],points:+m[4]}));
 const head=s.match(/<p class="kam-dran">([\s\S]*?)<\/p>/)[1];const actual=[];
 for(const m of head.matchAll(/AP1 (Herbst|Frühjahr) 20(\d{2}), ([^<]+?) \((\d+) P\)/g)){
  const exam=(m[1]==='Herbst'?'H':'F')+m[2];const list=[];
  for(const piece of m[3].split(', ')){const range=piece.match(/(\d+)\.(\d+) bis \d+\.(\d+)/);if(range){for(let i=+range[2];i<=+range[3];i++)list.push(range[1]+'.'+i);}else list.push(piece);}
  assert.equal(expected.filter(v=>v.exam===exam).reduce((a,v)=>a+v.points,0),+m[4],k+' Punktesumme');
  actual.push(...list.map(task=>exam+' '+task));
 }
 assert.deepEqual(actual,expected.map(v=>v.exam+' '+v.task),k+' Kam dran');
}
for(const x of JSON.parse(text('notizen/FESTE-BAUTEILE-SHA256.json'))){assert.equal(crypto.createHash('sha256').update(fs.readFileSync(x.Path)).digest('hex').toUpperCase(),x.Hash,'Fester Bauteil verändert');}
const decision=`
# Entscheidungen K-2 – Abschluss am 2026-09-03

- Die fünf bereits vorhandenen Kapitel wurden weiterverwendet und korrigiert; Originalstand unter bau/notizen/k2-pruefung/vorher, Änderungen nachvollziehbar in bau/pruef/k2-korrekturen.js.
- A5: Gleichstromformel eingegrenzt, tatsächliche Leistungsaufnahme von Nennleistung getrennt, Tarif nur als Aufgabenwert; DGUV-Beleg ergänzt. H21 2.1 behält 78,94 W mit Rundungsfußnote (rechnerisch 78,95 W); Kosten bleiben 4,26 EUR. Der Druckfehler „0,3 Cent“ wird erläutert.
- A6/A7/A9: F25 liegt als Aufgabenheft mit eingetragenen Antworten vor, nicht als amtliche Musterlösung. Nicht belegte Feinverteilungen sind als Übungshilfe gekennzeichnet oder entfallen. Die Zahlen wurden unabhängig nachgerechnet.
- A7: Compiler und Interpreter präzisiert; Bytecode, Ganzzahldivision, Laufzeitfehler sowie wiederhole-bis erläutert. Fünf ergänzende Primärquellen insgesamt in QUELLEN-A.md registriert.
- A8: Merge-Rauten vor gemeinsamen Aktionen ergänzt, offene include/extend-Pfeilspitzen gezeichnet, Multiplizitäten präzisiert. Beamer-Variante enthält eine Einrichtungspauschale und ergibt 135 EUR; unterschiedliche Tagessätze allein begründen keine unterschiedliche Methode.
- A9: Beispiele für alle drei Normalformen ergänzt; Fremdschlüssel und UNIQUE-Regeln präzisiert. Chen-Maximalwerte legen keine Mindestteilnahme fest; n/m in der Min-Max-Abbildung berichtigt. SQL-Zählung und Datumsvergleich präzisiert.
- Wiederholungen gekürzt: alle fünf Kapitel bleiben unter 3.500 Wörtern und bestehen check.js ohne Fehler oder Hinweise. Kam-dran-Zeilen stimmen einschließlich Teilaufgaben und Punktesummen mit MATRIX.md überein. Feste Bauteile per SHA256 unverändert.
- Die Browser-Sicherheitsrichtlinie hat das Öffnen der lokalen Vorschau blockiert. Keine Umgehung versucht; visuelle Browserprüfung bleibt für Phase Z offen. K-2 erfordert die erfolgreiche Fragmentprüfung; Z/F sind damit nicht abgeschlossen.
- bau/K2-vorschau.html dient nur zur lokalen Ansicht der fünf Kapitel. Die Navigation enthält bereits die späteren Kapitel; deren Ziele entstehen in den weiteren Bauphasen. Die endgültige AP1_Lerndatei.html wird in Phase Z erstellt.
`;
append('ENTSCHEIDUNGEN.md',decision);
fs.writeFileSync(path.join(root,'notizen/k2-pruefung/ABSCHLUSS.md'),'# Abschlussprüfung K-2\n\n'+stats.join('\n')+'\n\nKam-dran-Zeilen: vollständig gegen MATRIX.md geprüft.\nQuellen-URLs: registriert und geprüft.\nFeste Bauteile: SHA256 unverändert.\nSichtprüfung: durch Browser-URL-Sicherheitsrichtlinie blockiert; für Phase Z offen.\n');
fs.writeFileSync(path.join(root,'status/K2.done'),'Phase K-2 abgeschlossen am 2026-09-03.\n'+stats.join('\n')+'\nAlle fünf Fragmente: check.js --fragment, keine Fehler und keine Hinweise.\nRechnungen und Quellenprüfung: bau/notizen/k2-pruefung/.\nKam-dran-Zeilen stimmen mit MATRIX.md überein; feste Bauteile unverändert.\nBrowser-Sichtprüfung durch Sicherheitsrichtlinie blockiert; in Phase Z nachholen.\nEntscheidungen: bau/ENTSCHEIDUNGEN.md, Abschnitt K-2.\nNächste Kapitelphase: K-3, B1 bis B4.\n');
fs.writeFileSync(path.join(root,'STATUS.md'),text('STATUS.md').replace('| K2.done | offen |','| K2.done | abgeschlossen: Kapitel A5 bis A9 korrigiert und validiert, 0 Fehler / 0 Hinweise; Sichtprüfung in Z offen |'));
console.log(stats.join('\n'));console.log('K2.done, STATUS.md und ENTSCHEIDUNGEN.md aktualisiert.');

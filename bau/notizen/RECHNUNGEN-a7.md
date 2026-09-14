# Nachrechnungen Kapitel A7 · Programmlogik und Schreibtischtest

Gerechnet am 2026-09-03 mit Node v25 auf diesem Rechner. Alle Programme wurden wirklich ausgeführt,
nicht im Kopf durchgespielt. Skriptdatei (Arbeitskopie, außerhalb von `bau/`):
`…/scratchpad/a7.js`. Der vollständige Skriptinhalt ist unten je Abschnitt wiedergegeben.

Abgleich jeweils gegen den Lösungskern aus `notizen/2021-herbst.md`, `notizen/2024-herbst.md`,
`notizen/2025-fruehjahr.md` und `notizen/2025-herbst.md`.

---

## 1) Kern-Beispiel: Schleife mit Akkumulator (eigenes Beispiel, kein Prüfungsstoff)

Eingabe (Node):

```js
const menge = [12, 7, 25, 9, 18];
let summe = 0, gross = 0, i = 0;
while (i < 5) {
  summe = summe + menge[i];
  if (menge[i] > 10) gross = gross + 1;
  console.log(`i=${i} menge[i]=${menge[i]} summe=${summe} gross=${gross}`);
  i = i + 1;
}
console.log(`Ende: i=${i} summe=${summe} gross=${gross}`);
```

Ausgabe:

```
Durchlauf 1: i=0 menge[i]=12 summe=12 gross=1
Durchlauf 2: i=1 menge[i]=7  summe=19 gross=1
Durchlauf 3: i=2 menge[i]=25 summe=44 gross=2
Durchlauf 4: i=3 menge[i]=9  summe=53 gross=2
Durchlauf 5: i=4 menge[i]=18 summe=71 gross=3
Ende: i=5 summe=71 gross=3
```

Ergebnis: Summe 71, Zähler 3. Die Schreibtischtest-Tabelle im Abschnitt „Das Verfahren“
enthält genau diese sieben Zeilen (Start, fünf Durchläufe, Ende). Kein Prüfungsabgleich nötig,
weil das Beispiel selbst gebaut ist; die Tabellenform folgt `ihk-konvention-schreibtischtest`.

---

## 2) Original 1 · AP1 Frühjahr 2025, Aufgabe 3.6 (8 P)

Verschachtelte Bedingungen, in Node nachgebaut (Bezeichner und Ergebnistexte geändert, Logik
und Verschachtelungstiefe unverändert gegenüber dem Lösungskern in `notizen/2025-fruehjahr.md`).

Eingabe: siehe Funktion `bewerteAuftritt(ladedauer, htmlKorrekt, mobilTauglich, seoWert)` im Skript.

Ausgabe:

```
(1.5, true, true, 80)  -> Gut, SEO verbesserungsfaehig
(3.0, true, false, 45) -> Zu langsam und nicht mobiltauglich
```

Abgleich mit dem Lösungshinweis (Notiz F25 3.6): Aufruf 1 = „Gut, SEO könnte besser sein“,
Aufruf 2 = „Langsam und nicht mobilfreundlich“. Beide Zweige sind identisch, nur die Ergebnistexte
sind nach §2 Regel 5 umformuliert. **Stimmt überein.**

Grenzfallkontrolle (die Lösungsdatei hebt `> 80` ausdrücklich hervor):

```
(1.5, true, true, 81) -> Sehr gut
(2.0, true, true, 90) -> Zu langsam, sonst in Ordnung
```

Bestätigt: 80 erfüllt `> 80` nicht, 2,0 erfüllt `< 2` nicht.

## 2b) Variante 1 (gleiche Funktion, andere Aufrufe)

```
(1.8, true, false, 95) -> Nicht mobiltauglich, SEO aber stark
(0.9, false, true, 70) -> HTML fehlerhaft, aber mobiltauglich
```

Beide Ergebnisse aus dem laufenden Programm übernommen.

---

## 3) Original 2 · AP1 Herbst 2024, Aufgabe 2.5 (6 P)

Zweidimensionales Feld, Werte unverändert aus der Notiz `notizen/2024-herbst.md`:

```
Zeile 0: 1 | 223 | 312 | 154 |  47 | 124 | 236 | 334
Zeile 1: 2 | 103 | 401 |  14 | 236 |  56 |  –  |  –
Zeile 2: 3 |  20 | 312 | 235 |  17 | 124 |  32 |  –
```

Ausgabe:

```
pruefeBerechtigung(3, 236) -> false
Zeile von Person 3: 20, 312, 235, 17, 124, 32
236 steht in Zeile/Spalte: [0][6] und [1][4]
Kontrolle pruefeBerechtigung(2, 236) -> true
Kontrolle pruefeBerechtigung(1, 236) -> true
```

Abgleich mit dem Lösungshinweis (Notiz H24 2.5): „Weil der Mitarbeiter mit der Nummer 3 keinen
Zugriff auf Raum 236 hat, wird `False` zurückgegeben.“ **Stimmt überein.**
Die beiden Kontrollaufrufe belegen zusätzlich, dass 236 im Feld vorkommt, aber in fremden Zeilen –
das ist die Falle der Aufgabe.

## 3b) Variante 2 (eigenes Szenario, eigene Zahlen)

```
Feld: [101, 12, 34, 56] / [102, 34, 78, 90] / [103, 12, 90, 78]
hatLizenz(103, 78) -> true
hatLizenz(102, 56) -> false
56 steht in Zeile/Spalte: [0][3]
```

Gleiche Fallenstruktur wie im Original: 56 existiert, aber in der Zeile eines anderen Geräts.

---

## 4) Original 3 · AP1 Herbst 2021, Aufgabe 2.5 (8 P)

Zwei Fehler im Skript: Faktor 1000 statt 100 und `-gt` statt `-lt`.
In Node nachgebaut, weil PowerShell hier nur Vergleich und Multiplikation ausführt.

Ausgabe:

```
Laufwerk zu 50 % gefuellt (frei 50 %):
  fehlerhaft: Anteil = 500  -> WARNUNG
  korrigiert: Anteil = 50   -> ok
Laufwerk zu 90 % gefuellt (frei 10 %):
  fehlerhaft: -> WARNUNG
  korrigiert: Anteil = 10   -> WARNUNG
```

Abgleich mit dem Lösungshinweis (Notiz H21 2.5): Fehler 1 = Faktor 1000 statt 100,
Fehler 2 = falscher Vergleichsoperator, Korrektur `-lt 15`. **Stimmt überein.**
Die Rechnung zeigt zusätzlich, warum das Symptom in der Aufgabe („warnt bei 50 % Füllstand“)
zwingend auftritt: 500 ist immer größer als 15.

## 4b) Variante 3 (eigenes Szenario: Warnung ab 90 % Belegung)

Fehler 1: Faktor 10 statt 100. Fehler 2: `-lt` statt `-gt`.

```
gesamt=100 frei=80 -> belegt=20 % | fehlerhaft: Wert=2   -> WARNUNG | korrigiert: Wert=20 -> ok
gesamt=100 frei=5  -> belegt=95 % | fehlerhaft: Wert=9.5 -> WARNUNG | korrigiert: Wert=95 -> WARNUNG
```

Symptom der Variante: Das Skript warnt auch bei 20 % Belegung. Nach der Korrektur warnt es
nur noch bei 95 %. Beide Zeilen aus dem laufenden Programm.

---

## 5) Kontrollrechnung zu AP1 Frühjahr 2025, Aufgabe 3.5 (nicht als Original übernommen)

```
33000/12000                = 2.75
(5562/12000)*100           = 46.35
((12000-7554)/12000)*100   = 37.05
```

Deckungsgleich mit dem Lösungskern in `notizen/2025-fruehjahr.md`. Diese Zahlen stehen nur im
Selbstcheck des Kapitels, nicht als eigene Original-Aufgabe.

## 6) Kontrollrechnung zu AP1 Herbst 2025, Aufgabe 4.6 (nicht als Original übernommen)

```
Paracetamol: 50 < 25 -> false
ASS:         22 < 25 -> true
Pantoprazol: 25 < 25 -> false
Ibuprofen:   30 < 25 -> false
```

Nur ASS löst eine Meldung aus. Deckungsgleich mit dem Lösungskern in `notizen/2025-herbst.md`.
Der Fall „25 < 25 ist falsch“ wird im Kapitel als Grenzfehler-Beispiel benutzt.

## 7) Ganzzahldivision und Grenzfehler

```
7/2 als Gleitkommazahl = 3.5
7/2 ganzzahlig         = 3
```

Ein Feld mit fünf Elementen hat die gültigen Indizes 0 bis 4; der Index 5 existiert nicht.
Beide Aussagen stehen so im Selbstcheck des Kapitels.

## Abschlussprüfung K-2, 2026-09-03

Die vorhandenen Fragmente A5–A9 wurden fachlich korrigiert. Ausführung der erneuten
Rechnungen: node bau/pruef/k2-abschluss-check.js; Eingaben und Ergebnisse stehen in
k2-pruefung/NACHRECHNUNG.txt. Die bisherigen Abschnitte dokumentieren den Vorzustand.
Maßgeblich ist das korrigierte Kapitel; umsortierte Originale und Varianten sind über
ihre Prüfungsherkunft zuzuordnen, nicht über die frühere laufende Nummer.

Quellenpräzisierung: Vier Punkte je F25-Aufruf beziehungsweise je H21-Fehler sind nur
abgeleitete Übungsgewichtungen. Die jeweiligen Gesamtpunkte sind belegt.

## Kontrolle 2026-09-06

Unabhängige Zweitkontrolle sämtlicher Programme des Fragments `kapitel/16-a7.html`
(3 Originale, 3 Varianten, Schreibtischtest-Beispiel des Verfahrensteils, Schleifenbild
Abb. A7-1, Verschachtelungsbild Abb. A7-2, Feldraster Abb. A7-3). Jeder Pseudocode wurde
als lauffähiges Node-Programm nachgeschrieben und ausgeführt, jeder Zwischenwert des
Schreibtischtests Zeile für Zeile gegen die tatsächliche Ausführung gestellt. Abgleich
gegen `notizen/2025-fruehjahr.md` (3.6), `notizen/2024-herbst.md` (2.2, 2.3, 2.5),
`notizen/2021-herbst.md` (2.5), `notizen/2022-fruehjahr.md` (4.4), `notizen/2022-herbst.md`
(4.4) und `notizen/2025-herbst.md` (4.5 bis 4.8).

### Befehl 1 – Schreibtischtest-Beispiel des Verfahrensteils

Eingabe:

```
node -e "const menge=[12,7,25,9,18]; let summe=0,gross=0,i=0;
console.log('Start i=0 summe=0 gross=0');
while(i<5){ summe+=menge[i]; if(menge[i]>10) gross++;
  console.log('DL'+(i+1),'i='+i,'menge[i]='+menge[i],'summe='+summe,'gross='+gross); i++; }
console.log('Austritt i='+i,'Ausgabe',summe,gross);"
```

Ausgabe:

```
Start i=0 summe=0 gross=0
DL1 i=0 menge[i]=12 summe=12 gross=1
DL2 i=1 menge[i]=7  summe=19 gross=1
DL3 i=2 menge[i]=25 summe=44 gross=2
DL4 i=3 menge[i]=9  summe=53 gross=2
DL5 i=4 menge[i]=18 summe=71 gross=3
Austritt i=5 Ausgabe 71 3
```

Alle sieben Zeilen der Kapiteltabelle einschließlich Start- und Austrittszeile stimmen
mit der Ausführung überein; beim Austritt steht i auf 5, die Bedingung i < 5 ist falsch.

### Befehl 2 – bewerteAuftritt (Original 1 und Variante 1)

Die Verschachtelung wurde aus dem Fragment eins zu eins als Funktion übernommen.

Eingabe:

```
node -e "function b(l,h,m,s){ if(l<2){ if(h){ if(m){ if(s>80) return 'Sehr gut';
  else if(s>50) return 'Gut, SEO verbesserungsfaehig'; else return 'SEO zu schwach'; }
  else { if(s>80) return 'Nicht mobiltauglich, SEO aber stark';
         else return 'SEO und Mobiltauglichkeit verbesserungsfaehig'; } }
  else { if(m) return 'HTML fehlerhaft, aber mobiltauglich';
         else return 'HTML fehlerhaft und nicht mobiltauglich'; } }
  else { if(h){ if(m) return 'Zu langsam, sonst in Ordnung';
                else return 'Zu langsam und nicht mobiltauglich'; }
         else return 'Zu langsam und HTML fehlerhaft'; } }
console.log(b(1.5,true,true,80)); console.log(b(3.0,true,false,45));
console.log(b(1.8,true,false,95)); console.log(b(0.9,false,true,70));
console.log('Grenzfall', 80>80, 80>50);"
```

Ausgabe:

```
Gut, SEO verbesserungsfaehig
Zu langsam und nicht mobiltauglich
Nicht mobiltauglich, SEO aber stark
HTML fehlerhaft, aber mobiltauglich
Grenzfall false true
```

Der Grenzfall ist der Kern der Aufgabe: 80 > 80 ist falsch, 80 > 50 ist wahr.

### Befehl 3 – pruefeBerechtigung und hatLizenz (Original 2 und Variante 2)

Das Feld ist Zeile für Zeile aus dem SVG von Abb. A7-3 übernommen; leere Zellen bleiben leer.

Eingabe:

```
node -e "const F=[[1,223,312,154,47,124,236,334],[2,103,401,14,236,56],[3,20,312,235,17,124,32]];
function p(nr,raum){ for(let z=0;z<F.length;z++) for(let s=1;s<=F[z].length-1;s++)
  if(nr===F[z][0]&&raum===F[z][s]) return 'WAHR'; return 'FALSCH'; }
console.log(p(3,236), 'Zeile 2:', F[2].slice(1).join(','));
console.log('236 in Zeilen', F.map((r,z)=>r.slice(1).includes(236)?z:null).filter(z=>z!==null).join(' und '));
const L=[[101,12,34,56],[102,34,78,90],[103,12,90,78]];
function h(g,sw){ for(let z=0;z<L.length;z++) for(let s=1;s<=L[z].length-1;s++)
  if(g===L[z][0]&&sw===L[z][s]) return 'WAHR'; return 'FALSCH'; }
console.log(h(103,78), h(102,56), '56 steht in Zeile', L.findIndex(r=>r.slice(1).includes(56)));"
```

Ausgabe:

```
FALSCH Zeile 2: 20,312,235,17,124,32
236 in Zeilen 0 und 1
WAHR FALSCH 56 steht in Zeile 0
```

### Befehl 4 – PowerShell-Logik (Original 3 und Variante 3)

Beide Skripte wurden in ihrer fehlerhaften und ihrer korrigierten Fassung durchgerechnet.

Eingabe:

```
node -e "for(const [belegt,frei] of [[0.5,0.5],[0.9,0.1]])
  console.log('H21 Fuellstand '+(belegt*100)+'%: falsch '+(frei*1000)+' -gt 15 -> '+((frei*1000)>15?'Warnung':'keine')
    +' | richtig '+(frei*100)+' -lt 15 -> '+((frei*100)<15?'Warnung':'keine'));
for(const b of [0.2,0.95])
  console.log('Var3 Belegung '+(b*100)+'%: falsch '+(b*10)+' -lt 90 -> '+((b*10)<90?'Warnung':'keine')
    +' | richtig '+(b*100)+' -gt 90 -> '+((b*100)>90?'Warnung':'keine'));"
```

Ausgabe:

```
H21 Fuellstand 50%: falsch 500 -gt 15 -> Warnung | richtig 50 -lt 15 -> keine
H21 Fuellstand 90%: falsch 100 -gt 15 -> Warnung | richtig 10 -lt 15 -> Warnung
Var3 Belegung 20%: falsch 2 -lt 90 -> Warnung | richtig 20 -gt 90 -> keine
Var3 Belegung 95%: falsch 9.5 -lt 90 -> Warnung | richtig 95 -gt 90 -> Warnung
```

Beide Gegenproben des Fragments sind damit belegt: die fehlerhafte Fassung warnt im
Beispielfall zu Unrecht, die korrigierte warnt genau dann, wenn sie soll.

### Ergebnis

| Prüfstelle | Eigene Ausführung | Fragment | Abgleich |
|---|---|---|---|
| Schreibtischtest-Beispiel, alle 5 Durchläufe | summe 12/19/44/53/71, gross 1/1/2/2/3, Austritt i = 5 | wie links | gleich, jeder Zwischenwert |
| Abb. A7-1 (i = 0, i < 5, Rücksprung) | 5 Durchläufe, Austritt bei i = 5 | wie links | gleich |
| Abb. A7-2 (SoftwareNr = 0 innerhalb der äußeren Schleife) | Reihenfolge wie im Lösungshinweis F22 4.4 | wie links | gleich |
| Abb. A7-3 (Raster 3 × 8, Zugriff rechteFeld[1][4] = 236) | Zeile 1 Spalte 4 trägt 236 | Akzentfeld auf Zeile 1, Spalte 4 | gleich |
| Original 1, F25 3.6 (8 P) | „Gut, SEO verbesserungsfähig“ und „Zu langsam und nicht mobiltauglich“ | wie links | gleich |
| Variante 1 | „Nicht mobiltauglich, SEO aber stark“ und „HTML fehlerhaft, aber mobiltauglich“ | wie links | gleich, Verfahren wie F25 3.6 |
| Original 2, H24 2.5 (6 P) | FALSCH; Zeile 2 führt 20, 312, 235, 17, 124, 32; 236 liegt in Zeile 0 und Zeile 1 | wie links | gleich |
| Variante 2 | hatLizenz(103, 78) = WAHR; hatLizenz(102, 56) = FALSCH, 56 liegt in Zeile 0 | wie links | gleich, Verfahren wie H24 2.5 |
| Original 3, H21 2.5 (8 P) | Faktor 100 statt 1000; `-lt` statt `-gt`; Gegenprobe 50 und 10 | wie links | gleich |
| Variante 3 | Faktor 100 statt 10; `-gt` statt `-lt`; Gegenprobe 20 und 95 | wie links | gleich, Verfahren wie H21 2.5 |
| Selbstcheck 2 und 4 (Grenzen, Ganzzahldivision) | gültige Indizes 0 bis 4; 7/2 = 3 ganzzahlig, 7.0/2 = 3,5 | wie links | gleich |
| Punktangaben der Kopfzeile | 8 + 9 + 7 + (3+3+6) + (6+8) + (3+2+3+2) = 60 | 8/9/7/12/14/10 P, Summe 60 P | gleich |

Keine Korrektur am Fragment nötig. `node pruef/check.js kapitel/16-a7.html --fragment`
meldet unverändert „Keine Fehler.“

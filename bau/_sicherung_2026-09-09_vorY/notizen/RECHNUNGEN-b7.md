# K-4 · B7 · Datensicherung und Verfügbarkeit · Nachrechnung 2026-09-05

Werkzeug: Node v25, Skript `b7.js` im Sitzungs-Scratchpad (Wegwerfdatei, nicht im Projekt).
Alle Zahlen unten stehen so oder umgerechnet im Fragment `kapitel/26-b7.html`.

## R1 · Speicherbedarf der drei Sicherungsarten über eine Woche

Annahme (eigenes Lehrbeispiel, keine IHK-Aufgabe): Datenbestand 500 GB, Vollsicherung Sonntag,
Montag bis Samstag je 20 GB neu geänderte Daten.

Eingabe (Node):
```
const voll=500, tag=20, tage=6;
let diffSum=0, diffTag=[];
for(let i=1;i<=tage;i++){diffTag.push(i*tag); diffSum+=i*tag;}
console.log(diffTag.join(', '), diffSum, voll+diffSum, tage*tag, voll+tage*tag, 7*voll);
```
Ausgabe:
```
diff je Tag Mo..Sa GB: 20, 40, 60, 80, 100, 120 | Summe 420 | Woche gesamt 920
inkr je Tag GB: 20 x6 | Summe 120 | Woche gesamt 620
taeglich voll: 7 x 500 = 3500
```
Abgleich: kein IHK-Lösungshinweis vorhanden, weil keine der sieben B7-Teilaufgaben diese Rechnung stellt.
Die Formeln folgen der Definition der Sicherungsarten aus BSI CON.3 (differenziell: alles seit der letzten
Vollsicherung; inkrementell: alles seit der letzten Sicherung gleich welcher Art). Ersparnis differenziell
gegenüber inkrementell über die Woche: 920 − 620 = 300 GB.

## R2 · Wiederherstellung auf den Stand von Donnerstagabend

Eingabe/Ausgabe:
```
diff bis Do: 500 + 200 = 700 | Baender: 2
inkr bis Do: 500 + 80 = 580 | Baender: 5
```
Bänderzahl: differenziell Vollsicherung Sonntag plus differenzielle Sicherung Donnerstag = 2.
Inkrementell Vollsicherung Sonntag plus Montag, Dienstag, Mittwoch, Donnerstag = 5.
Diese Zahlen stehen in Abbildung B7-1 und im Rechenschema.

## R3 · RAID-Nutzkapazität, 8 Platten zu je 4 TB

Eingabe (Node): `n=8, k=4` mit den Formeln n·k, (n/2)·k, (n−1)·k, (n/2)·k.
Ausgabe:
```
RAID0 32 TB | RAID1 (4 Paare) 16 TB | RAID5 28 TB | RAID10 16 TB
RAID1 klassisch 2 Platten: 4 TB
RAID5 Nutzanteil: 87,50 % | RAID10/RAID1 Nutzanteil: 50 %
RAID5 bei 3 Platten Nutzanteil: 66,67 % Verlust 33,33 %
```
Abgleich: Die Zeile „RAID 5 bei drei Platten, etwa 33 % Verlust" deckt sich mit dem Lösungshinweis
zu H21 3.6 („Verringerung der Nutzkapazität bei zum Beispiel drei Festplatten auf etwa 33 % Verlust")
und mit der Aussage zu RAID 1 („anteilig reduziert, zum Beispiel um 50 %").

## R4 · Original H22 2.4: RAID 5 aus ungleichen Platten

Gegeben: zwei Platten zu 3 TB, sieben Platten zu 2 TB, alle neun im Verbund.
Eingabe/Ausgabe: `(9-1)*2 = 16` TB.
Abgleich mit dem Lösungshinweis: kleinste gemeinsam nutzbare Kapazität 2 TB (2 Punkte),
(9 − 1) × 2 TB = 16 TB (2 Punkte). Übereinstimmung.

## R5 · Original H22 2.5: JBOD aus denselben Platten

Eingabe/Ausgabe: `2*3 + 7*2 = 20` TB. `20e12/2**40 = 18.189894035458565`.
Abgleich: Der Lösungshinweis nennt 20 und beschriftet das Feld mit TiB, während der Aufgabentext TB
verlangt. Die Summe 20 stimmt; die Einheit TiB ist im Lösungshinweis falsch, denn 20 TB sind
18,19 TiB. Im Fragment wird deshalb 20 TB geschrieben und der Einheitenwiderspruch als Prüfungsnotiz
benannt. Siehe auch notizen/2022-herbst.md, Teilaufgabe 2.5.
Diese Teilaufgabe erscheint nicht als eigene Original-Aufgabe, sondern in der Variante zu H22 2.4.

## R6 · Variante zu H22 2.4

Gegeben: drei Platten zu 4 TB, fünf Platten zu 3 TB, alle acht im Verbund.
Eingabe/Ausgabe: `(8-1)*3 = 21` TB; JBOD `3*4 + 5*3 = 27` TB.

## R7 · Verfügbarkeit in Prozent, Ausfallzeit je Jahr

Jahr mit 365 Tagen: 365 × 24 = 8 760 h.
Eingabe: `(1-p/100)*8760` für p = 99; 99,5; 99,9; 99,99; 99,999.
Ausgabe:
```
99 %     -> 87,600 h = 5.256,00 min = 3,650 Tage
99,5 %   -> 43,800 h = 2.628,00 min = 1,825 Tage
99,9 %   ->  8,760 h =   525,60 min = 0,365 Tage
99,99 %  ->  0,876 h =    52,56 min
99,999 % ->  0,088 h =     5,26 min
```
Abgleich mit der Auftragsvorgabe (99,9 % = 8,76 h; 99,99 % = 52,6 min): bestätigt.
52,56 min wird im Fragment als 52,56 min geschrieben, nicht gerundet auf 52,6.

## R8 · MTBF, MTTR und Verfügbarkeit

Formel A = MTBF / (MTBF + MTTR).
Eingabe/Ausgabe: `50000/50005 = 0.99990001` → 99,990 %; Ausfallzeit 52,55 min/Jahr.
Kontrollbeispiel: `1000/1004 = 99,60 %`.
Im Fragment wird der Wert als „rund 99,99 %" geschrieben, weil 99,990 % auf zwei Nachkommastellen
99,99 % ergibt. Die kleine Abweichung zu R7 (52,55 statt 52,56 min) stammt aus der Rundung von A
und wird im Fragment nicht behauptet.

## R9 · Variante zum Rechenschema (Speicherbedarf)

Gegeben: 800 GB Bestand, 30 GB Änderung je Tag, Vollsicherung Sonntag, Mo bis Sa gesichert.
Ausgabe:
```
diff Woche: 800 + 630 = 1430 GB | inkr Woche: 800 + 180 = 980 GB
Stand Do:   diff 1100 GB, 2 Baender | inkr 920 GB, 5 Baender
```

## R10 · Variante zu H21 3.6 und Selbstcheck

Variante: vier Platten zu je 6 TB.
```
RAID 0  4 x 6 = 24 TB | RAID 1 als zwei Spiegelpaare 2 x 6 = 12 TB
RAID 5  (4-1) x 6 = 18 TB | RAID 10 (4/2) x 6 = 12 TB
```
Selbstcheck: sechs Platten zu je 2 TB im RAID 5.
```
(6-1) x 2 = 10 TB nutzbar von 12 TB brutto, Anteil 83,33 %
```

## Nicht gerechnet

Aufbewahrungsfristen (10, 8, 6 Jahre) sind Rechtsangaben aus HGB § 257 Abs. 4 und AO § 147 Abs. 3,
keine Rechnung. Sie wurden am 2026-09-05 über die in QUELLEN-B.md als geprüft geführten URLs
gegengelesen. Ergebnis: 10 Jahre für Handelsbücher, Inventare, Eröffnungsbilanzen und Jahresabschlüsse;
8 Jahre für Buchungsbelege; 6 Jahre für Handelsbriefe und sonstige Unterlagen; Fristbeginn mit Schluss
des Kalenderjahrs. Die Fundstellenspalte in QUELLEN-B.md nennt nur „10 bzw. 6 Jahre" und ist damit
unvollständig; die Liste wird von diesem Bauer nicht geändert (§2 Regel: nur drei Dateien anfassen).

## Kontrolle 2026-09-06

Kontrolleur K-5. Werkzeug: Node v25, Wegwerfskript `b7chk.js` im Sitzungs-Scratchpad.
Geprüft: H21 3.6, H22 2.4, F24 4.3 und die drei Varianten gegen `notizen/2021-herbst.md` 3.6,
`notizen/2022-herbst.md` 2.4 und `notizen/2024-fruehjahr.md` 4.3.

Eingabe und Befehl:

```
node -e "
const voll=500,tag=20; let d=[],s=0; for(let i=1;i<=6;i++){d.push(i*tag);s+=i*tag;}
console.log('diff', d.join(','), s, voll+s, '| inkr', voll+6*tag, '| voll', 7*voll);
console.log('n=8 k=4:', 8*4, 4, (8-1)*4, (8/2)*4);
console.log('H22 2.4:', (9-1)*2, '| JBOD H22 2.5:', 2*3+7*2);
console.log('Var1 4x6:', 4*6, 2*6, (4-1)*6, (4/2)*6, 'Diff', (4-1)*6-(4/2)*6);
console.log('Var2:', (8-1)*3, 3*4+5*3);
console.log('Selbstcheck 6x2:', (6-1)*2, 6*2, ((2/12)*100).toFixed(2));
const h=365*24; for(const p of [99,99.5,99.9,99.99,99.999]){const a=(1-p/100)*h;
  console.log(p+' %', a.toFixed(3)+' h', (a*60).toFixed(2)+' min', (a/24).toFixed(3)+' Tage');}
console.log('MTBF:', (50000/50005*100).toFixed(5), '| RAID5 3 Platten Verlust', ((1/3)*100).toFixed(2));
"
```

Ausgabe:

```
diff 20,40,60,80,100,120 420 920 | inkr 620 | voll 3500
n=8 k=4: 32 4 28 16
H22 2.4: 16 | JBOD H22 2.5: 20
Var1 4x6: 24 12 18 12 Diff 6
Var2: 21 27
Selbstcheck 6x2: 10 12 16.67
99 %     87.600 h  5256.00 min  3.650 Tage
99,5 %   43.800 h  2628.00 min  1.825 Tage
99,9 %    8.760 h   525.60 min  0.365 Tage
99,99 %   0.876 h    52.56 min  0.037 Tage
99,999 %  0.088 h     5.26 min  0.004 Tage
MTBF: 99.99000 | RAID5 3 Platten Verlust 33.33
```

Abgleich:

| Stelle im Fragment | Wert im Fragment | Nachrechnung | Abgleich |
|---|---|---|---|
| Original H22 2.4 | (9 − 1) × 2 TB = 16 TB, kleinste Kapazität 2 TB | 16 | stimmt, Lösungskern nennt beide Teilschritte zu je 2 P |
| Original H21 3.6 | RAID 5, bei drei Platten etwa 33 % Verlust, RAID 1 50 % | 33,33 / 50 | stimmt mit dem Lösungshinweis |
| Original F24 4.3 | 3 P, ein Punkt je Aspekt, keine feinere Aufteilung | – | stimmt, Notiz nennt keine weitere Aufteilung; keine Datenträgerzahl ergänzt |
| Variante 1 | 24 / 12 / 18 / 12 TB, Wahl RAID 5 | identisch | stimmt, RAID 0 scheidet mangels Ausfalltoleranz aus |
| Variante 2 | RAID 5 21 TB, JBOD 27 TB | identisch | stimmt |
| Variante 3 | drei Aspekte, kein Zahlenwert | – | trainiert dasselbe Verfahren wie F24 4.3 |
| Rechenschema Woche | 3.500 / 920 / 620 GB | identisch | stimmt |
| Medien für Stand Donnerstag | differenziell 2, inkrementell 5 | 2 / 5 | stimmt |
| Verfügbarkeitstabelle | 87,60 h / 8,76 h / 52,56 min / 5,26 min | identisch | stimmt, Jahr mit 365 × 24 = 8.760 h |
| MTBF 50.000 h, MTTR 5 h | „rund 99,99 %" | 99,99000 % | stimmt |

Aufbewahrungsfristen (keine Rechnung, Rechtsangabe): § 257 Abs. 4 HGB und § 147 Abs. 3 AO in
der seit dem 1. Januar 2025 geltenden Fassung nennen zehn Jahre für Handelsbücher, Inventare,
Eröffnungsbilanzen und Jahresabschlüsse, acht Jahre für Buchungsbelege und sechs Jahre für
Handelsbriefe und sonstige Unterlagen; Fristbeginn mit Schluss des Kalenderjahrs
(§ 257 Abs. 5 HGB, § 147 Abs. 4 AO). Die Tabelle im Fragment gibt genau diese drei Fristen an.

Ergebnis: keine Abweichung, keine Korrektur am Fragment nötig.
`node pruef/check.js kapitel/26-b7.html --fragment` meldet unverändert „Keine Fehler."

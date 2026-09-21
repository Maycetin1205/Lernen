# Nachrechnungen Kapitel A5 · Strom und Energiekosten

Stand: 2026-09-03. Phase K-2. Alle Rechnungen mit `node -e` auf demselben Rechner geprüft.
Abgleich jeweils gegen den Lösungskern in `notizen/2021-herbst.md`, `notizen/2024-fruehjahr.md`
und `notizen/2025-herbst.md`.

Rundung: kaufmännisch auf zwei Nachkommastellen, sofern nicht anders vermerkt.
Hilfsfunktion in allen Läufen: `const r2 = x => Math.round(x*100)/100;`

---

## 1. Original 1 · H21 2.1 (6 P) · Wirkungsgrad und Energiekosten zweier Netzteile

Eingabe:

```
node -e "const r2=x=>Math.round(x*100)/100;
console.log(20*9);
console.log(60/0.43, r2(60/0.43));
console.log(60/0.76, r2(60/0.76));
console.log(180*0.13953*0.30, r2(180*0.13953*0.30));
console.log(180*0.07894*0.30, r2(180*0.07894*0.30));
console.log(r2(180*(60/0.76/1000)*0.30));"
```

Ausgabe:

```
180
139.53488372093022  139.53
78.94736842105263   78.95
7.5346199999999985  7.53
4.262759999999999   4.26
4.26
```

| Größe | Eigene Rechnung | Lösungshinweis | Abgleich |
|---|---|---|---|
| Betriebsstunden je Monat | 20 · 9 = 180 h | 180 h | gleich |
| PC-A, aufgenommene Leistung | 60 / 0,43 = 139,53 W | 139,53 W (im Heft vorgegeben) | gleich |
| PC-B, aufgenommene Leistung | 60 / 0,76 = 78,9474 W, kaufmännisch 78,95 W | 78,94 W | **Abweichung**, siehe unten |
| PC-A, Energiekosten je Monat | 180 · 0,13953 kW · 0,30 EUR = 7,53 EUR | 7,53 EUR | gleich |
| PC-B, Energiekosten je Monat | 180 · 0,07894 kW · 0,30 EUR = 4,26 EUR | 4,26 EUR | gleich |

Abweichung PC-B: Der Lösungshinweis schneidet 78,9473… bei 78,94 ab, kaufmännisch gerundet wären es
78,95 W. Nach §2 Regel 6 wird die IHK-Zahl 78,94 W verwendet und im Kapitel als Rundungshinweis
kenntlich gemacht. Auf das Kostenergebnis wirkt sich das nicht aus: mit 78,9474 W ergeben sich
ebenfalls 4,26 EUR (Kontrollzeile oben).

Preisfalle: Der Lösungshinweis schreibt in beiden Kostenzeilen „0,3 Cent/kWh“. Gerechnet wurde dort
mit 0,30 EUR/kWh (30 Cent), sonst käme 7,53 EUR nicht heraus. Kontrolle: mit 0,003 EUR/kWh wären es
0,075 EUR statt 7,53 EUR. Die Aufgabenstellung selbst nennt „eine Kilowattstunde kostet 30 Cent“.

## 2. Original 2 · H21 2.2 (4 P) · Amortisationszeit

Eingabe:

```
node -e "const r2=x=>Math.round(x*100)/100;
console.log(r2(7.53-4.26));
console.log(100/3.27, Math.ceil(100/3.27));
console.log(r2(6.83-4.78), 100/2.05, Math.ceil(100/2.05));"
```

Ausgabe:

```
3.27
30.581039755351682  31
2.05  48.78048780487805  49
```

| Größe | Eigene Rechnung | Lösungshinweis | Abgleich |
|---|---|---|---|
| Einsparung je Monat | 7,53 − 4,26 = 3,27 EUR | 3,27 EUR | gleich |
| Amortisationszeit | 100 / 3,27 = 30,58 Monate, aufgerundet 31 | 30,58, also nach 31 Monaten | gleich |
| Ersatzwertlösung des Hefts | 6,83 − 4,78 = 2,05; 100 / 2,05 = 48,78 → 49 | 48,78, also nach 49 Monaten | gleich |

Aufgerundet wird, weil der Mehrpreis erst nach Ablauf des angebrochenen Monats gedeckt ist.
Weitergerechnet wird mit den in 2.1 eingetragenen gerundeten Beträgen (Deckblattregel).

## 3. Original 3 · F24 3.7 (4 P) · Netzteil aus Komponentenleistung und Reserve

Eingabe:

```
node -e "const k=20+172+12+4*5+310+2*5+2*8;
console.log(k, k*1.10);
for(let p=400;p<=1200;p+=50) if(p>=k*1.10){console.log(p);break;}"
```

Ausgabe:

```
560  616.0000000000001
650
```

| Größe | Eigene Rechnung | Lösungshinweis | Abgleich |
|---|---|---|---|
| Summe der Komponenten | 20 + 172 + 12 + 4·5 + 310 + 2·5 + 2·8 = 560 W | 560 W | gleich |
| Mit 10 % Reserve | 560 · 1,10 = 616 W | 616 W | gleich |
| Gewähltes Netzteil | nächste 50-W-Stufe ≥ 616 W → 650 W | 650 W | gleich |

Die Fließkomma-Ausgabe 616.0000000000001 ist ein Darstellungsartefakt; exakt sind es 616 W.

## 4. Variante 1 (zu H21 2.1)

Eingabe:

```
node -e "const r2=x=>Math.round(x*100)/100; const h=22*8;
console.log(h, 80/0.50, 80/0.85, r2(80/0.85));
console.log(h*0.160*0.32, r2(h*0.160*0.32));
console.log(h*0.09412*0.32, r2(h*0.09412*0.32));"
```

Ausgabe:

```
176  160  94.11764705882354  94.12
9.0112   9.01
5.3008384  5.3
```

Ergebnis: 176 h je Monat; Variante A 160,00 W; Variante B 94,12 W; Kosten 9,01 EUR und 5,30 EUR.
Kein Lösungshinweis vorhanden (eigene Variante), Verfahren identisch mit H21 2.1.

## 5. Variante 2 (zu H21 2.2)

Eingabe:

```
node -e "const r2=x=>Math.round(x*100)/100;
console.log(r2(9.01-5.30), 80/3.71, Math.ceil(80/3.71));"
```

Ausgabe:

```
3.71  21.5633423180593  22
```

Ergebnis: Einsparung 3,71 EUR je Monat; 80 / 3,71 = 21,56 Monate, aufgerundet 22 Monate.

## 6. Variante 3 (zu F24 3.7)

Eingabe:

```
node -e "const s=25+145+10+4*4+260+2*6+3*7;
console.log(s, s*1.15);
for(let p=400;p<=1200;p+=50) if(p>=s*1.15){console.log(p);break;}"
```

Ausgabe:

```
489  562.3499999999999
600
```

Ergebnis: Summe 489 W (25 + 145 + 10 + 16 + 260 + 12 + 21); mit 15 % Reserve 562,35 W;
nächste 50-W-Stufe 600 W.

## 7. Rechenweg-Schema im Abschnitt „Das Verfahren“

Eingabe:

```
node -e "const r2=x=>Math.round(x*100)/100;
console.log(65/0.87, r2(65/0.87));
console.log(8*220, 16*220);
console.log(0.07471*1760, r2(0.07471*1760));
console.log(0.003*3520);
console.log(r2(0.07471*1760)+10.56);
console.log((r2(0.07471*1760)+10.56)*0.32, r2((r2(0.07471*1760)+10.56)*0.32));"
```

Ausgabe:

```
74.71264367816092  74.71
1760  3520
131.4896  131.49
10.56
142.05
45.456  45.46
```

Ergebnis: P_auf = 74,71 W; E_Betrieb = 131,49 kWh; E_Standby = 10,56 kWh; E = 142,05 kWh;
Kosten = 45,46 EUR je Jahr. Frei erfundenes Übungsbeispiel, kein IHK-Bezug.

## 8. Zahlen in Abbildungen und Merke-Blöcken

Eingabe:

```
node -e "console.log(500*0.85, 500-425);
console.log(16*230, 3*180+400+1200+2000);
console.log(24*0.5, 12/5);
console.log(900/300);
console.log(139.53-60);"
```

Ausgabe:

```
425  75
3680  4140
12  2.4
3
79.53000000000001
```

| Verwendung | Rechnung | Ergebnis |
|---|---|---|
| Abb. A5-3, Verlustwärme PC-A | 139,53 W − 60 W | 79,53 W |
| Merke „Belastbarkeit“ | 16 A · 230 V | 3.680 W |
| Merke „Belastbarkeit“ (H21 2.4) | 3 · 180 + 400 + 1.200 + 2.000 | 4.140 W, also zu viel |
| Begriffskarte USV / Selbstcheck | 900 Wh / 300 W | 3 h |
| Begriffskarte USB (H25 3.5) | 24 V · 0,5 A = 12 W; 12 W / 5 V | 2,4 A |
| Beispiel Wirkungsgrad in Abb. A5-3 (Text) | 500 W · 0,85; 500 − 425 | 425 W; 75 W Verlust |

Die Werte zu H21 2.4 (3.680 W gegen 4.140 W) und H25 3.5 (12 W, 2,4 A) stimmen mit den
Lösungskernen in den Extraktionsnotizen überein.

## 9. Amortisations-Abbildung (Abb. A5-4)

Maßstab der Zeichnung, geprüft:

```
node -e "const x=m=>60+m*13.5, y=E=>200-E*1.143;
console.log(x(0), x(10), x(20), x(30), x(40));
console.log(y(0), y(100), y(130.8));
const m=100/3.27; console.log(m, x(m), y(m*3.27));"
```

Ausgabe:

```
60  195  330  465  600
200  85.7  50.28560000000001
30.581039755351682  472.84403669724767  85.70000000000002
```

Die Schnittstelle der Einsparungsgeraden mit der 100-EUR-Linie liegt bei x ≈ 473, y ≈ 86;
so ist sie in der Abbildung gesetzt.

## Abschlussprüfung K-2, 2026-09-03

Die vorhandenen Fragmente A5–A9 wurden fachlich korrigiert. Ausführung der erneuten
Rechnungen: node bau/pruef/k2-abschluss-check.js; Eingaben und Ergebnisse stehen in
k2-pruefung/NACHRECHNUNG.txt. Die bisherigen Abschnitte dokumentieren den Vorzustand.
Maßgeblich ist das korrigierte Kapitel; umsortierte Originale und Varianten sind über
ihre Prüfungsherkunft zuzuordnen, nicht über die frühere laufende Nummer.

## Kontrolle 2026-09-06

Unabhängige Zweitkontrolle sämtlicher Lösungen des Fragments `kapitel/14-a5.html`
(3 Originale, 3 Varianten, alle Abbildungs-, Merke- und Selbstcheckwerte).
Abgleich gegen `notizen/2021-herbst.md` (2.1, 2.2, 2.4), `notizen/2024-fruehjahr.md` (3.7)
und `notizen/2025-herbst.md` (3.5, 3.6). Jede Zahl mit Node nachgerechnet, nichts im Kopf.

### Befehl 1 – Originale, Varianten, Rechenweg-Schema, Abbildungen

Eingabe:

```
node -e "const r2=x=>Math.round(x*100)/100;
console.log('Schema', 65/0.87, r2(65/0.87), 8*220, 16*220, 0.07471*1760, 0.003*3520, (131.49+10.56), r2((131.49+10.56)*0.32));
console.log('Abb3', 60/0.43, 139.53-60);
console.log('O1', 20+172+12+4*5+310+2*5+2*8, (20+172+12+4*5+310+2*5+2*8)*1.1, Math.ceil(616/50)*50);
console.log('O2', 20*9, 60/0.76, r2(0.13953*180*0.30), r2(0.07894*180*0.30));
console.log('O3', 7.53-4.26, 100/3.27, Math.ceil(100/3.27), 6.83-4.78, Math.ceil(100/2.05));
console.log('V1', 25+145+10+4*4+260+2*6+3*7, 489*1.15, Math.ceil(562.35/50)*50);
console.log('V2', 22*8, 80/0.50, r2(0.160*176), r2(0.160*176*0.32), 80/0.85, r2(0.09412*176), r2(16.57*0.32), 9.01-5.30);
console.log('V3', 80/3.71, Math.ceil(80/3.71));"
```

Ausgabe:

```
Schema 74.71264367816092 74.71 1760 3520 131.4896 10.56 142.05 45.46
Abb3 139.53488372093022 79.53
O1 560 616.0000000000001 650
O2 180 78.94736842105263 7.53 4.26
O3 3.2700000000000005 30.581039755351682 31 2.05 49
V1 489 562.3499999999999 600
V2 176 160 28.16 9.01 94.11764705882354 16.57 5.3 3.71
V3 21.5633423180593 22
```

### Befehl 2 – Selbstcheck, Begriffskarten, Merke-Blöcke

Eingabe:

```
node -e "console.log(24*0.5, 12/5);
console.log(8*250, 0.090*2000, 0.090*2000*0.35);
console.log(120/0.80, 150-120);
console.log(16*230, 3*180+400+1200+2000, 1200+2000);
console.log(900/300);
console.log('Punktesummen', 6+4+4, 4+3, 2+3);"
```

Ausgabe:

```
12 2.4
2000 180 62.99999999999999
150 30
3680 4140 3200
3
Punktesummen 14 7 5
```

### Ergebnis

| Prüfstelle | Eigene Rechnung | Fragment | Abgleich |
|---|---|---|---|
| Rechenweg-Schema (74,71 W / 131,49 / 10,56 / 142,05 / 45,46 EUR) | wie links | wie links | gleich |
| Abb. A5-3 (139,53 W; Verlust 79,53 W) | 60/0,43 = 139,5349; 139,53 − 60 = 79,53 | wie links | gleich |
| Abb. A5-4 (Schnittpunkt 30,58 → 31 Monate) | 100/3,27 = 30,581 | wie links | gleich |
| Original 1, F24 3.7 (4 P: 3 + 1) | 560 W; 616 W; 650 W | wie links | gleich, auch Punkteverteilung |
| Original 2, H21 2.1 (6 P: 3 × 2) | 180 h; 78,9474 W; 7,53 EUR; 4,26 EUR | 78,94 W (IHK) | gleich; Abschneidefehler des Hefts bleibt mit Fußnote stehen |
| Original 3, H21 2.2 (4 P) | 3,27 EUR; 30,58 → 31 Monate; Ersatzweg 2,05 → 49 | wie links | gleich |
| Variante 1 (Reserve 15 %) | 489 W; 562,35 W; 600 W | wie links | gleich, Verfahren wie F24 3.7 |
| Variante 2 (Wirkungsgrad, Kosten) | 176 h; 160,00 W; 94,12 W; 9,01 EUR; 5,30 EUR | wie links | gleich, Verfahren wie H21 2.1 |
| Variante 3 (Amortisation) | 3,71 EUR; 21,56 → 22 Monate | wie links | gleich, Verfahren wie H21 2.2 |
| Selbstcheck 1 bis 4 | 12 W / 2,4 A; 180 kWh / 63,00 EUR; 150 W / 30 W; 3.680 W gegen 4.140 W | wie links | gleich |
| Punktangaben der Kopfzeile | 6+4+4 = 14; 4+3 = 7; 2+3 = 5 | 14 P / 7 P / 5 P | gleich |

Zusätzlich wurden alle Gleichungen des Fragments maschinell aus dem HTML gelöst und
gegen den gedruckten Wert gestellt. Einziger Treffer: `60 W / 0,76 = 78,94 W`. Das ist
die bekannte Abweichung des IHK-Hefts (kaufmännisch 78,95 W); sie bleibt nach Vorgabe
mit dem vorhandenen Rundungshinweis erhalten und wirkt sich auf die Kosten nicht aus.

Keine Korrektur am Fragment nötig. `node pruef/check.js kapitel/14-a5.html --fragment`
meldet unverändert „Keine Fehler.“

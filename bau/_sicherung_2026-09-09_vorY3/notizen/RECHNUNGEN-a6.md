# Nachrechnungen Kapitel A6 · Netzplan und Gantt

Gerechnet am 2026-09-03 mit Node v25 (Bauplan §2 Regel 6).
Werkzeug: eigenes Skript `cpm.js` (Vorgangsknoten, Ende-Anfang-Beziehung, Zeitzählung ab 0).

## 0. Verwendetes Skript

```js
// Vorwaerts: FAZ = max(FEZ der Vorgaenger) bzw. 0; FEZ = FAZ + Dauer
// Projektdauer T = max(FEZ)
// Rueckwaerts: SEZ = min(SAZ der Nachfolger) bzw. T; SAZ = SEZ - Dauer
// GP = SAZ - FAZ  (Gegenprobe GP = SEZ - FEZ)
// FP = min(FAZ der Nachfolger) - FEZ  (Endvorgang: T - FEZ)
```

Das Skript gibt zu jedem Plan zusätzlich aus: Projektdauer, alle Vorgänge mit GP = 0
(kritischer Pfad), die Summe der Dauern auf diesem Pfad und die Gegenprobe
`SAZ − FAZ == SEZ − FEZ` für jeden Vorgang.

---

## 1. Beispielnetzplan des Kapitels (Abb. A6-2, Abb. A6-3, Tabelle im Kern)

Eingabe (eigenes Szenario, Umzug eines Steuerbüros, Dauern in Arbeitstagen):

| Vorgang | Beschreibung | Dauer | Vorgänger |
|---|---|---|---|
| A | Bestandsaufnahme | 3 | – |
| B | Hardware bestellen und liefern lassen | 6 | A |
| C | Netzwerkdosen setzen | 2 | A |
| D | Patchfeld auflegen | 2 | C |
| E | Rechner aufbauen und einrichten | 6 | B, D |
| F | Abnahme mit dem Kunden | 2 | E |

Ausgabe von `node run1.js`:

```
=== Kapitelbeispiel A6 (6 Vorgaenge) === Projektdauer: 17
V | Dauer | FAZ | FEZ | SAZ | SEZ | GP | GP(Gegenprobe SEZ-FEZ) | FP
A | 3 | 0 | 3 | 0 | 3 | 0 | 0 | 0
B | 6 | 3 | 9 | 3 | 9 | 0 | 0 | 0
C | 2 | 3 | 5 | 5 | 7 | 2 | 2 | 0
D | 2 | 5 | 7 | 7 | 9 | 2 | 2 | 2
E | 6 | 9 | 15 | 9 | 15 | 0 | 0 | 0
F | 2 | 15 | 17 | 15 | 17 | 0 | 0 | 0
Kritisch (GP=0): A - B - E - F
Summe Dauern kritisch: 17
Gegenprobe GP (SAZ-FAZ == SEZ-FEZ): true
```

Ergebnis: Projektdauer 17 Arbeitstage. Kritischer Pfad A – B – E – F,
Summe der Dauern 3 + 6 + 6 + 2 = 17, also deckungsgleich mit der Vorwärtsrechnung.
Gegenprobe SAZ − FAZ = SEZ − FEZ bei allen sechs Vorgängen erfüllt.
Auf dem kritischen Pfad ist GP überall 0.

Didaktisch tragende Stelle: C hat GP 2, aber FP 0, weil der Nachfolger D
unmittelbar am FEZ von C beginnt (FAZ D = 5 = FEZ C). D hat GP 2 und FP 2.

Balkenlagen für Abb. A6-3 (Zeitachse ab 0, Balken von FAZ bis FEZ):
A 0–3, B 3–9, C 3–5, D 5–7, E 9–15, F 15–17.
Puffer sichtbar als Strecke von FEZ bis SEZ: C 5–7, D 7–9.

Verzögerungsprobe (dieselbe Rechnung mit veränderter Dauer von C):

```
C dauert 2 -> Projektdauer 17, GP(C)=2, FP(C)=0
C dauert 3 -> Projektdauer 17, GP(C)=1, FP(C)=0   (D verschiebt sich auf 6..8)
C dauert 4 -> Projektdauer 17, GP(C)=0, FP(C)=0   (zweiter kritischer Pfad)
C dauert 5 -> Projektdauer 18                      (Endtermin kippt)
```

Abgleich: passt zur Definition. Solange die Verzögerung den Gesamtpuffer nicht
überschreitet, hält der Endtermin; ab Überschreitung wächst die Projektdauer
genau um die Differenz.

---

## 2. Original H21 1.3 (14 P) · Netzplan vervollständigen

Eingabe aus `notizen/2021-herbst.md`, Abschnitt „1.3“ (Dauern in Stunden):
A 2 (–), B 4 (A), C 3 (B), D 8 (B), E 2 (B), F 5 (B), G 4 (C, D), H 1 (E),
I 3 (G, H), J 1 (I), K 2 (F, J).

Ausgabe:

```
=== H21 1.3 Original === Projektdauer: 24
V | Dauer | FAZ | FEZ | SAZ | SEZ | GP | GP(Gegenprobe) | FP
A | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 0
B | 4 | 2 | 6 | 2 | 6 | 0 | 0 | 0
C | 3 | 6 | 9 | 11 | 14 | 5 | 5 | 5
D | 8 | 6 | 14 | 6 | 14 | 0 | 0 | 0
E | 2 | 6 | 8 | 15 | 17 | 9 | 9 | 0
F | 5 | 6 | 11 | 17 | 22 | 11 | 11 | 11
G | 4 | 14 | 18 | 14 | 18 | 0 | 0 | 0
H | 1 | 8 | 9 | 17 | 18 | 9 | 9 | 9
I | 3 | 18 | 21 | 18 | 21 | 0 | 0 | 0
J | 1 | 21 | 22 | 21 | 22 | 0 | 0 | 0
K | 2 | 22 | 24 | 22 | 24 | 0 | 0 | 0
Kritisch (GP=0): A - B - D - G - I - J - K
Summe Dauern kritisch: 24
Gegenprobe GP (SAZ-FAZ == SEZ-FEZ): true
```

Abgleich mit dem Lösungshinweis (Tabelle in `2021-herbst.md`, Abschnitt 1.3):
alle 11 Zeilen und alle sechs Werte je Zeile stimmen zeichengenau überein.
Projektdauer 24 Stunden wie im Lösungshinweis.

H21 1.4 (kritischer Pfad): Lösungshinweis nennt A – B – D – G – I – J – K.
Eigene Rechnung liefert exakt diese Menge (alle Vorgänge mit GP = 0). Summe
2 + 4 + 8 + 4 + 3 + 1 + 2 = 24 = Projektdauer. Übereinstimmung.

H21 1.5 (Verzögerung von H um 4 Stunden): Nachrechnung mit H-Dauer 1 + 4 = 5:

```
=== H21 mit H-Dauer 5 === Projektdauer: 24
H | 5 | 8 | 13 | 13 | 18 | 5 | 5 | 5
Kritisch: A - B - D - G - I - J - K
```

Projektende bleibt bei 24 Stunden, der Puffer von H sinkt von 9 auf 5 Stunden.
Der Lösungshinweis („keine Auswirkung, Puffer 9 Stunden fängt die 4 Stunden auf“)
ist damit bestätigt. Kontrollrechnung: erst ab einer Verlängerung von H um mehr
als 9 Stunden kippt der Endtermin (H-Dauer 11 ergibt Projektdauer 25 und einen
neuen kritischen Pfad A – B – E – H – I – J – K).

---

## 3. Variante 1 (zu H21 1.3) · gleiche Struktur, neue Dauern

Eingabe: A 3 (–), B 5 (A), C 4 (B), D 9 (B), E 3 (B), F 6 (B), G 5 (C, D),
H 2 (E), I 4 (G, H), J 2 (I), K 3 (F, J).

```
=== Variante 1 (zu H21 1.3) === Projektdauer: 31
A | 3 | 0 | 3 | 0 | 3 | 0 | 0 | 0
B | 5 | 3 | 8 | 3 | 8 | 0 | 0 | 0
C | 4 | 8 | 12 | 13 | 17 | 5 | 5 | 5
D | 9 | 8 | 17 | 8 | 17 | 0 | 0 | 0
E | 3 | 8 | 11 | 17 | 20 | 9 | 9 | 0
F | 6 | 8 | 14 | 22 | 28 | 14 | 14 | 14
G | 5 | 17 | 22 | 17 | 22 | 0 | 0 | 0
H | 2 | 11 | 13 | 20 | 22 | 9 | 9 | 9
I | 4 | 22 | 26 | 22 | 26 | 0 | 0 | 0
J | 2 | 26 | 28 | 26 | 28 | 0 | 0 | 0
K | 3 | 28 | 31 | 28 | 31 | 0 | 0 | 0
Kritisch (GP=0): A - B - D - G - I - J - K
Summe Dauern kritisch: 31
Gegenprobe GP (SAZ-FAZ == SEZ-FEZ): true
```

Gegenprobe: 3 + 5 + 9 + 5 + 4 + 2 + 3 = 31 = Projektdauer. Die Variante behält
die lehrreiche Stelle des Originals: E hat GP 9, aber FP 0.

---

## 4. Original F25 3.1 (9 P) · Netzplan vervollständigen

Eingabe aus `notizen/2025-fruehjahr.md`, Abschnitt „3.1“ (Dauern in Stunden):
A 2 (–), B 25 (A), C 32 (B), D 40 (B), E 70 (C, D), F 15 (E), G 8 (B),
H 2 (G), I 16 (E), J 4 (F, I, H).

```
=== F25 3.1 Original === Projektdauer: 157
A | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 0
B | 25 | 2 | 27 | 2 | 27 | 0 | 0 | 0
C | 32 | 27 | 59 | 35 | 67 | 8 | 8 | 8
D | 40 | 27 | 67 | 27 | 67 | 0 | 0 | 0
E | 70 | 67 | 137 | 67 | 137 | 0 | 0 | 0
F | 15 | 137 | 152 | 138 | 153 | 1 | 1 | 1
G | 8 | 27 | 35 | 143 | 151 | 116 | 116 | 0
H | 2 | 35 | 37 | 151 | 153 | 116 | 116 | 116
I | 16 | 137 | 153 | 137 | 153 | 0 | 0 | 0
J | 4 | 153 | 157 | 153 | 157 | 0 | 0 | 0
Kritisch (GP=0): A - B - D - E - I - J
Summe Dauern kritisch: 157
Gegenprobe GP (SAZ-FAZ == SEZ-FEZ): true
```

Abgleich mit dem Lösungsplan aus `2025-fruehjahr.md`: alle zehn Zeilen
deckungsgleich, Projektdauer 157 Stunden. F25 3.2 (kritischer Pfad
A – B – D – E – I – J) bestätigt: 2 + 25 + 40 + 70 + 16 + 4 = 157.

---

## 5. Variante 2 (zu F25 3.1) · gleiche Struktur, neue Dauern

Eingabe: A 3 (–), B 20 (A), C 25 (B), D 35 (B), E 60 (C, D), F 12 (E),
G 6 (B), H 3 (G), I 18 (E), J 5 (F, I, H).

```
=== Variante 2 (zu F25 3.1) === Projektdauer: 141
A | 3 | 0 | 3 | 0 | 3 | 0 | 0 | 0
B | 20 | 3 | 23 | 3 | 23 | 0 | 0 | 0
C | 25 | 23 | 48 | 33 | 58 | 10 | 10 | 10
D | 35 | 23 | 58 | 23 | 58 | 0 | 0 | 0
E | 60 | 58 | 118 | 58 | 118 | 0 | 0 | 0
F | 12 | 118 | 130 | 124 | 136 | 6 | 6 | 6
G | 6 | 23 | 29 | 127 | 133 | 104 | 104 | 0
H | 3 | 29 | 32 | 133 | 136 | 104 | 104 | 104
I | 18 | 118 | 136 | 118 | 136 | 0 | 0 | 0
J | 5 | 136 | 141 | 136 | 141 | 0 | 0 | 0
Kritisch (GP=0): A - B - D - E - I - J
Summe Dauern kritisch: 141
Gegenprobe GP (SAZ-FAZ == SEZ-FEZ): true
```

Gegenprobe: 3 + 20 + 35 + 60 + 18 + 5 = 141 = Projektdauer. Auch hier bleibt
G mit GP 104 und FP 0 der Beleg für den Unterschied der beiden Pufferarten.

---

## 6. Original H23 4.3 bis 4.5 (6 + 1 + 1 = 8 P) · Gantt, Endtermin, größter Puffer

Eingabe aus `notizen/2023-herbst.md`, Abschnitte 4.3 bis 4.5 (Dauern in Tagen):
A 3 (–), B 6 (A), C 4 (B), D 8 (A), E 5 (A), F 3 (C, D, E), G 2 (F).

```
=== H23 4.3 bis 4.5 Original === Projektdauer: 18
A | 3 | 0 | 3 | 0 | 3 | 0 | 0 | 0
B | 6 | 3 | 9 | 3 | 9 | 0 | 0 | 0
C | 4 | 9 | 13 | 9 | 13 | 0 | 0 | 0
D | 8 | 3 | 11 | 5 | 13 | 2 | 2 | 2
E | 5 | 3 | 8 | 8 | 13 | 5 | 5 | 5
F | 3 | 13 | 16 | 13 | 16 | 0 | 0 | 0
G | 2 | 16 | 18 | 16 | 18 | 0 | 0 | 0
Kritisch (GP=0): A - B - C - F - G
Summe Dauern kritisch: 18
Gegenprobe GP (SAZ-FAZ == SEZ-FEZ): true
```

Umrechnung in die Balkenlage des Aufgabenrasters (die IHK zählt hier ab 1,
ein Balken belegt die Nummern FAZ + 1 bis FEZ):
A 1–3 (Vorgabe im Heft), B 4–9, C 10–13, D 4–11, E 4–8, F 14–16, G 17–18.
Das ist zeichengenau die Balkentabelle aus dem Lösungshinweis.

H23 4.4 (frühestes Projektende): Lösungshinweis „nach 18 Tagen“; eigene
Rechnung 18. Übereinstimmung.

H23 4.5 (größter Puffer): Lösungshinweis nennt zuerst „Vorgang C“, dieser Eintrag
ist durchgestrichen, daneben steht handschriftlich „Vorgang E ist richtig“.
Eigene Rechnung: C liegt auf dem kritischen Pfad und hat GP 0; D hat GP 2;
E hat GP 5 und damit den größten Puffer. Die handschriftliche Korrektur ist
rechnerisch bestätigt, der ursprünglich gedruckte Wert war falsch.

---

## 7. Variante 3 (zu H23 4.3 bis 4.5) · gleiche Struktur, neue Dauern

Eingabe: A 2 (–), B 7 (A), C 3 (B), D 9 (A), E 4 (A), F 4 (C, D, E), G 3 (F).

```
=== Variante 3 (zu H23 4.3 bis 4.5) === Projektdauer: 19
A | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 0
B | 7 | 2 | 9 | 2 | 9 | 0 | 0 | 0
C | 3 | 9 | 12 | 9 | 12 | 0 | 0 | 0
D | 9 | 2 | 11 | 3 | 12 | 1 | 1 | 1
E | 4 | 2 | 6 | 8 | 12 | 6 | 6 | 6
F | 4 | 12 | 16 | 12 | 16 | 0 | 0 | 0
G | 3 | 16 | 19 | 16 | 19 | 0 | 0 | 0
Kritisch (GP=0): A - B - C - F - G
Summe Dauern kritisch: 19
Gegenprobe GP (SAZ-FAZ == SEZ-FEZ): true
```

Balkenlage bei Zählung ab 1: A 1–2, B 3–9, C 10–12, D 3–11, E 3–6, F 13–16,
G 17–19. Gegenprobe 2 + 7 + 3 + 4 + 3 = 19 = Projektdauer.
Größter Puffer: E mit 6 Tagen (D hat nur 1 Tag).

---

## 8. Zusammenfassung der Abgleiche

| Rechnung | Quelle des Sollwerts | Ergebnis |
|---|---|---|
| Kapitelbeispiel (6 Vorgänge) | eigene Konstruktion | in sich schlüssig, Gegenproben erfüllt |
| H21 1.3 (11 Knoten, 66 Werte) | Lösungshinweis H21 | vollständig deckungsgleich |
| H21 1.4 kritischer Pfad | Lösungshinweis H21 | deckungsgleich |
| H21 1.5 Verzögerung H um 4 h | Lösungshinweis H21 | deckungsgleich (Endtermin hält) |
| F25 3.1 (10 Knoten, 60 Werte) | Lösungshinweis F25 | vollständig deckungsgleich |
| F25 3.2 kritischer Pfad | Lösungshinweis F25 | deckungsgleich |
| H23 4.3 Balkenlage | Lösungshinweis H23 | deckungsgleich |
| H23 4.4 Projektende 18 | Lösungshinweis H23 | deckungsgleich |
| H23 4.5 größter Puffer | Lösungshinweis H23 (korrigiert) | bestätigt die Korrektur „Vorgang E“ |
| Varianten 1 bis 3 | eigene Konstruktion | Gegenproben erfüllt |

Keine Abweichung zwischen eigener Rechnung und Lösungshinweisen. Ein einziger
Konflikt liegt in den Lösungshinweisen selbst (H23 4.5, gedruckt „C“, korrigiert
auf „E“); dort folgt das Kapitel der Korrektur und der eigenen Rechnung.

## Abschlussprüfung K-2, 2026-09-03

Die vorhandenen Fragmente A5–A9 wurden fachlich korrigiert. Ausführung der erneuten
Rechnungen: node bau/pruef/k2-abschluss-check.js; Eingaben und Ergebnisse stehen in
k2-pruefung/NACHRECHNUNG.txt. Die bisherigen Abschnitte dokumentieren den Vorzustand.
Maßgeblich ist das korrigierte Kapitel; umsortierte Originale und Varianten sind über
ihre Prüfungsherkunft zuzuordnen, nicht über die frühere laufende Nummer.

Quellenpräzisierung F25: Die Antwortdatei ist ein ausgefülltes Aufgabenheft, keine amtliche
Musterlösung. Die erneute Rechnung bestätigt die Zahlen unabhängig; eine amtliche
Feinverteilung der neun Punkte ist dadurch nicht belegt.

## Kontrolle 2026-09-06

Unabhängige Zweitkontrolle sämtlicher Netzpläne des Fragments `kapitel/15-a6.html`
(2 Originale, 2 Varianten, 1 Beispielplan in Abb. A6-2 samt Tabelle, Balkenplan Abb. A6-3,
Detailbild Abb. A6-4, Selbstcheck 4 mit dem H23-Plan). Abgleich gegen
`notizen/2021-herbst.md` (1.3 bis 1.5), `notizen/2025-fruehjahr.md` (3.1, 3.2) und
`notizen/2023-herbst.md` (4.1, 4.3 bis 4.5).

### Befehl – vollständige Vorwärts- und Rückwärtsrechnung je Plan

Jeder Plan wurde nicht abgelesen, sondern aus Dauern und Vorgängerliste neu gerechnet:
FAZ = Maximum der Vorgänger-FEZ, FEZ = FAZ + Dauer, T = größter FEZ, SEZ = Minimum der
Nachfolger-SAZ (beim Endvorgang T), SAZ = SEZ − Dauer, GP = SAZ − FAZ mit Gegenprobe
SEZ − FEZ, FP = kleinster Nachfolger-FAZ − FEZ (ohne Nachfolger T − FEZ).

Eingabe (Wegwerf-Skript im Scratchpad der Sitzung, Kern):

```
function rechne(vg){ /* Vorwaerts, Rueckwaerts, GP mit Gegenprobe, FP */ }
zeig('Beispielplan', {A:{d:3,pred:[]},B:{d:6,pred:['A']},C:{d:2,pred:['A']},
                      D:{d:2,pred:['C']},E:{d:6,pred:['B','D']},F:{d:2,pred:['E']}});
zeig('F25 3.1',      {A:{d:2,pred:[]},B:{d:25,pred:['A']},C:{d:32,pred:['B']},D:{d:40,pred:['B']},
                      E:{d:70,pred:['C','D']},F:{d:15,pred:['E']},G:{d:8,pred:['B']},
                      H:{d:2,pred:['G']},I:{d:16,pred:['E']},J:{d:4,pred:['F','I','H']}});
zeig('H21 1.3',      {A:{d:2,pred:[]},B:{d:4,pred:['A']},C:{d:3,pred:['B']},D:{d:8,pred:['B']},
                      E:{d:2,pred:['B']},F:{d:5,pred:['B']},G:{d:4,pred:['C','D']},H:{d:1,pred:['E']},
                      I:{d:3,pred:['G','H']},J:{d:1,pred:['I']},K:{d:2,pred:['F','J']}});
zeig('Variante 1',   {A:{d:3,pred:[]},B:{d:20,pred:['A']},C:{d:25,pred:['B']},D:{d:35,pred:['B']},
                      E:{d:60,pred:['C','D']},F:{d:12,pred:['E']},G:{d:6,pred:['B']},
                      H:{d:3,pred:['G']},I:{d:18,pred:['E']},J:{d:5,pred:['F','I','H']}});
zeig('Variante 2',   {A:{d:3,pred:[]},B:{d:5,pred:['A']},C:{d:4,pred:['B']},D:{d:9,pred:['B']},
                      E:{d:3,pred:['B']},F:{d:6,pred:['B']},G:{d:5,pred:['C','D']},H:{d:2,pred:['E']},
                      I:{d:4,pred:['G','H']},J:{d:2,pred:['I']},K:{d:3,pred:['F','J']}});
zeig('H23 4.3-4.5',  {A:{d:3,pred:[]},B:{d:6,pred:['A']},C:{d:4,pred:['B']},D:{d:8,pred:['A']},
                      E:{d:5,pred:['A']},F:{d:3,pred:['C','D','E']},G:{d:2,pred:['F']}});
```

Ausgabe (Vorgang · Dauer · FAZ · FEZ · SAZ · SEZ · GP · FP):

```
Beispielplan (Abb. A6-2 und Tabelle)
A 3 0 3 0 3 0 0 | B 6 3 9 3 9 0 0 | C 2 3 5 5 7 2 0
D 2 5 7 7 9 2 2 | E 6 9 15 9 15 0 0 | F 2 15 17 15 17 0 0
T = 17 | kritisch A,B,E,F | Summe Dauern 17

F25 3.1 (Original 1)
A 2 0 2 0 2 0 0 | B 25 2 27 2 27 0 0 | C 32 27 59 35 67 8 8
D 40 27 67 27 67 0 0 | E 70 67 137 67 137 0 0 | F 15 137 152 138 153 1 1
G 8 27 35 143 151 116 0 | H 2 35 37 151 153 116 116
I 16 137 153 137 153 0 0 | J 4 153 157 153 157 0 0
T = 157 | kritisch A,B,D,E,I,J | Summe Dauern 157

H21 1.3 (Original 2)
A 2 0 2 0 2 0 0 | B 4 2 6 2 6 0 0 | C 3 6 9 11 14 5 5
D 8 6 14 6 14 0 0 | E 2 6 8 15 17 9 0 | F 5 6 11 17 22 11 11
G 4 14 18 14 18 0 0 | H 1 8 9 17 18 9 9 | I 3 18 21 18 21 0 0
J 1 21 22 21 22 0 0 | K 2 22 24 22 24 0 0
T = 24 | kritisch A,B,D,G,I,J,K | Summe Dauern 24

Variante 1 (Onlineshop)
A 3 0 3 0 3 0 0 | B 20 3 23 3 23 0 0 | C 25 23 48 33 58 10 10
D 35 23 58 23 58 0 0 | E 60 58 118 58 118 0 0 | F 12 118 130 124 136 6 6
G 6 23 29 127 133 104 0 | H 3 29 32 133 136 104 104
I 18 118 136 118 136 0 0 | J 5 136 141 136 141 0 0
T = 141 | kritisch A,B,D,E,I,J | Summe Dauern 141

Variante 2 (Autohaus)
A 3 0 3 0 3 0 0 | B 5 3 8 3 8 0 0 | C 4 8 12 13 17 5 5
D 9 8 17 8 17 0 0 | E 3 8 11 17 20 9 0 | F 6 8 14 22 28 14 14
G 5 17 22 17 22 0 0 | H 2 11 13 20 22 9 9 | I 4 22 26 22 26 0 0
J 2 26 28 26 28 0 0 | K 3 28 31 28 31 0 0
T = 31 | kritisch A,B,D,G,I,J,K | Summe Dauern 31

H23 4.3 bis 4.5 (Selbstcheck 4, Raster ab Tag 1: Balken FAZ+1 bis FEZ)
A Tag 1-3 GP 0 | B Tag 4-9 GP 0 | C Tag 10-13 GP 0 | D Tag 4-11 GP 2
E Tag 4-8 GP 5 | F Tag 14-16 GP 0 | G Tag 17-18 GP 0
T = 18 | kritisch A,B,C,F,G | größter Puffer E mit 5 Tagen
```

Die GP-Gegenprobe (SAZ − FAZ gegen SEZ − FEZ) stimmt in jedem der 55 gerechneten Knoten
(6 + 10 + 11 + 10 + 11 + 7);
auf jedem kritischen Pfad ist GP durchweg 0, und die Summe der Dauern des Pfades ist
jeweils gleich der Projektdauer.

### Ergebnis

| Prüfstelle | Zählweise | Eigene Rechnung | Fragment | Abgleich |
|---|---|---|---|---|
| Beispielplan Abb. A6-2, Tabelle und Fließtext | ab 0 | T = 17, kritisch A,B,E,F | wie links | gleich |
| Abb. A6-3 Balkenplan (Maßstab 27 px je Tag, Nullpunkt x = 160) | ab 0 | A 0-3, B 3-9, C 3-5, D 5-7, E 9-15, F 15-17 | Balken 160/241/241/295/403/565 | gleich |
| Abb. A6-4 (E und H aus H21) | ab 0 | E 6-8, H 8-9, SEZ von E = 17, GP 9, FP 0 | wie links | gleich |
| Original 1, F25 3.1 (9 P) und kritischer Pfad (1 P) | ab 0 | fünf ergänzte Knoten F,G,H,I,J wie oben; T = 157 | wie links | gleich |
| Original 2, H21 1.3 (14 P = 4 × 1 + 5 × 2) | ab 0 | alle 11 Knoten wie oben; T = 24 | wie links | gleich, auch Punkteregel |
| H21 1.4 / 1.5 (1 P / 2 P) | ab 0 | Pfad A,B,D,G,I,J,K; H mit GP 9 trägt 4 h | wie links | gleich |
| Variante 1 | ab 0 | T = 141, Pfad A,B,D,E,I,J, G mit GP 104 und FP 0 | wie links | gleich, Verfahren wie F25 3.1 |
| Variante 2 | ab 0 | T = 31, Pfad A,B,D,G,I,J,K, H mit GP 9 trägt 6 h | wie links | gleich, Verfahren wie H21 1.3 |
| Selbstcheck 4 (H23) | ab 1 | Balken 1-3/4-9/10-13/4-11/4-8/14-16/17-18; Ende Tag 18; größter Puffer E = 5, D = 2 | wie links | gleich |
| Punktangaben der Kopfzeile | – | 14+1+2 = 17; 4+6+1+1 = 12; 9+1 = 10; Summe 39 | 17 P / 12 P / 10 P / 39 P | gleich |

Keine Korrektur am Fragment nötig. `node pruef/check.js kapitel/15-a6.html --fragment`
meldet unverändert „Keine Fehler.“

# Nachrechnungen Kapitel A8 · UML-Diagramme

Erstellt in Phase K-2 gemäß BAUPLAN.md §2 Regel 6. Werkzeug: Node v25.
Datum der Prüfung: 2026-09-03.

A8 ist ein Zeichenkapitel. Es gibt keine Sachrechnungen. Nachgerechnet werden deshalb
alle Zahlen, die im Fragment stehen: die Punktesummen der Original-Aufgaben (Abgleich mit
der amtlichen Punkteverteilung aus den Lösungshinweisen laut Extraktionsnotizen), die
Summe der Kam-dran-Zeile sowie alle Zahlen, die in Aufgabentexten und Varianten als
Schwellenwert oder Rechenbeispiel auftauchen.

## 1. Punktesummen der Original-Aufgaben

Ein Aufruf, alle Zeilen:

```
node -e "
console.log('H25 2.2 Punkte:', 2+2+1+1+1+1+1);
console.log('F23 4.4 Punkte:', 3*2+2);
console.log('H24 2.4 Punkte:', 1+1+3*0.5+3*0.5);
console.log('H23 1.1 Punkte:', 4+2);
console.log('Kam dran Summe:', 8+6+5+9);
console.log('Variante Urlaub Resturlaub:', 30-12);
console.log('Grenzfall 1000 EUR manuell?', 1000>=1000, ' 999,99:', 999.99>=1000);
console.log('Grenzfall 12 Tage > 10?', 12>10, ' 10 Tage > 10?', 10>10);
console.log('Notebook 5 Tage:', 12*5, 'Beamer 5 Tage:', 25*5);
console.log('Variante Kasse Punkte:', 1+1+3*0.5+3*0.5);
console.log('Variante Klassen Punkte:', 3*2+2);
console.log('Variante Aktivitaet Punkte:', 2+2+1+1+1+1+1);
"
```

Ausgabe:

```
H25 2.2 Punkte: 9
F23 4.4 Punkte: 8
H24 2.4 Punkte: 5
H23 1.1 Punkte: 6
Kam dran Summe: 28
Variante Urlaub Resturlaub: 18
Grenzfall 1000 EUR manuell? true  999,99: false
Grenzfall 12 Tage > 10? true  10 Tage > 10? false
Notebook 5 Tage: 60 Beamer 5 Tage: 125
Variante Kasse Punkte: 5
Variante Klassen Punkte: 8
Variante Aktivitaet Punkte: 9
```

### Abgleich mit den Lösungshinweisen (aus den Extraktionsnotizen)

| Zeile | Eingabe | Ausgabe | Lösungshinweis laut Notizen | Abgleich |
|---|---|---|---|---|
| H25 2.2 | 2+2+1+1+1+1+1 | 9 | notizen/2025-herbst.md, 2.2: „automatische Prüfung samt Entscheidung 2 P; manuelle Prüfung samt Entscheidung 2 P; Bezahlung, Archivierung, Parallelisierung, Ablehnung und Endknoten jeweils 1 P" | stimmt, 9 P |
| F23 4.4 | 3*2+2 | 8 | notizen/2023-fruehjahr.md, 4.4: „Je Klasse 2 Punkte, 2 Punkte für die Vererbung"; drei Klassen (Versicherungsobjekt, KFZ, Immobilie) | stimmt, 8 P |
| H24 2.4 | 1+1+3*0.5+3*0.5 | 5 | notizen/2024-herbst.md, 2.4: 1 P Akteur Administrator, 1 P Vererbung, 3 × 0,5 P Anwendungsfälle, 3 × 0,5 P include-Beziehungen | stimmt, 5 P |
| H23 1.1 | 4+2 | 6 | notizen/2023-herbst.md, 1.1: „1 Punkt je ergänztem Akteur und Anwendungsfall", 4 Anwendungsfälle + 2 Akteure | stimmt, 6 P |
| Kam dran | 8+6+5+9 | 28 | notizen/MATRIX.md Zeile A8: Summe 28, 4 Teilaufgaben | stimmt, 28 P |

Die vier Herkunftszeilen im Fragment nennen damit genau die Punktzahlen der Matrix:
F23 4.4 = 8 P, H23 1.1 = 6 P, H24 2.4 = 5 P, H25 2.2 = 9 P.
H23 1.1 wird im Fragment nicht als Original-Aufgabe ausgeschrieben (Budget, §10:
höchstens drei Aufgaben), sondern nur in einer Prüfungsnotiz erwähnt.

## 2. Zahlen in den Aufgabentexten

| Zahl | Herkunft | Prüfung | Ergebnis |
|---|---|---|---|
| 1.000 EUR | H25 2.2, Schwelle für die manuelle Prüfung, „ab 1.000 EUR einschließlich" | `1000>=1000` und `999.99>=1000` | `true` / `false` – der Betrag 1.000,00 € gehört in den manuellen Zweig, 999,99 € nicht. Guard im Diagramm deshalb `[Betrag >= 1.000 EUR]` und `[Betrag < 1.000 EUR]`. |

## 3. Zahlen in den Varianten

| Zahl | Ort | Prüfung | Ergebnis |
|---|---|---|---|
| 18 Tage | Variante zu 2.2, Beispielwert Resturlaub | `30-12` | 18 – ein Antrag über 12 Tage ist durch 30 Tage Resturlaub gedeckt |
| Schwelle 10 Tage | Variante zu 2.2, Guard | `12>10` = `true`, `10>10` = `false` | Guard `[mehr als 10 Arbeitstage]` schließt genau 10 Tage aus; die Gegenbedingung lautet `[10 Arbeitstage oder weniger]` |
| 9 P | Variante zu 2.2, Punkteschlüssel analog zum Original | `2+2+1+1+1+1+1` | 9 |
| 60,00 € | Variante zu 4.4, Notebook 12,00 €/Tag über 5 Tage | `12*5` | 60 |
| 125,00 € | Variante zu 4.4, Beamer 25,00 €/Tag über 5 Tage | `25*5` | 125 |
| 8 P | Variante zu 4.4, Punkteschlüssel analog zum Original | `3*2+2` | 8 |
| 5 P | Variante zu 2.4, Punkteschlüssel analog zum Original | `1+1+3*0.5+3*0.5` | 5 |

Die beiden Tagessätze belegen im Klassendiagramm, warum `mietpreisBerechnen()` in beiden
Unterklassen bleibt: die Rechnung ist dieselbe Formel, aber der Satz steht je Gerätetyp
in einem eigenen Attribut. Beide Beträge erscheinen nur im Lösungstext der Variante,
nicht im Diagramm.

## 4. Nicht gerechnet

Sichtbarkeiten (+, -, #), Multiplizitäten (1, 0..1, 1..*, 0..*) und Stereotype
(«include», «extend») sind Symbole, keine Zahlen. Sie wurden gegen OMG UML 2.5.1
(Clause 9, 15, 18) und die Lösungsdiagramme in den Extraktionsnotizen geprüft, nicht
gerechnet.

## Abschlussprüfung K-2, 2026-09-03

Die vorhandenen Fragmente A5–A9 wurden fachlich korrigiert. Ausführung der erneuten
Rechnungen: node bau/pruef/k2-abschluss-check.js; Eingaben und Ergebnisse stehen in
k2-pruefung/NACHRECHNUNG.txt. Die bisherigen Abschnitte dokumentieren den Vorzustand.
Maßgeblich ist das korrigierte Kapitel; umsortierte Originale und Varianten sind über
ihre Prüfungsherkunft zuzuordnen, nicht über die frühere laufende Nummer.

Korrektur der Klassenvariante: Notebook 12 × 5 = 60 EUR; Beamer 25 × 5 + 10 = 135 EUR.
Die zusätzliche Einrichtungspauschale begründet ein tatsächlich anderes Verfahren.
Der alte Wert 125 EUR und die Begründung allein mit unterschiedlichen Tagessätzen sind ersetzt.
include und extend sind UML-Beziehungsarten, keine zusätzlichen Stereotype.
Alternative Kontrollflüsse werden vor einer gemeinsamen Aktion per Merge vereinigt.

## Kontrolle 2026-09-06

Kontrolleur K-5. Werkzeug: Node v25, Wegwerfskript `a8chk.js` im Sitzungs-Scratchpad.
Geprüft: drei Original-Aufgaben (H25 2.2, F23 4.4, H24 2.4) und drei Varianten gegen
`notizen/2025-herbst.md` 2.2, `notizen/2023-fruehjahr.md` 4.4 und `notizen/2024-herbst.md` 2.4.

Eingabe und Befehl:

```
node -e "
console.log('H25 2.2:', 2+2+1+1+1+1+1);
console.log('F23 4.4:', 3*2+2);
console.log('H24 2.4:', 1+1+3*0.5+3*0.5);
console.log('Grenze 1000:', 1000>=1000, 999.99>=1000);
console.log('Grenze 10 Tage:', 12>10, 10>10, 'Rest:', 30-12);
console.log('Notebook:', 12*5, 'Beamer:', 25*5+10);
"
```

Ausgabe:

```
H25 2.2: 9
F23 4.4: 8
H24 2.4: 5
Grenze 1000: true false
Grenze 10 Tage: true false Rest: 18
Notebook: 60 Beamer: 135
```

Abgleich der Punktzahlen: Herkunftszeilen nennen 9, 8 und 5 Punkte; die Lösungskerne der
Notizen nennen dieselben Werte mit derselben Aufteilung. Die drei Varianten übernehmen sie
unverändert (9, 8, 5). Keine Abweichung.

Diagrammprüfung (Symbole, nicht gerechnet; Maßstab OMG UML 2.5.1 Clause 9, 15, 18):

| Prüfpunkt | Abb. A8-5 (H25 2.2) | Abb. A8-6 (F23 4.4) | Abb. A8-7 (H24 2.4) |
|---|---|---|---|
| Guards in eckigen Klammern an jeder Kante der Entscheidung | drei Rauten, sechs Guards vollständig | entfällt | entfällt |
| Gabelung mit zugehöriger Synchronisation | Balken y=470 und y=580, beide vorhanden | entfällt | entfällt |
| Zusammenführung vor gemeinsamer Aktion | zwei Merge-Rauten (vor Gabelung, vor Ablehnung) | entfällt | entfällt |
| Endknoten für jeden Pfad | Aktivitätsendknoten, beide Pfade münden hinein | entfällt | entfällt |
| Vererbungspfeil mit hohler Spitze zur Oberklasse | entfällt | Spitze an Unterkante Versicherungsobjekt | Spitze am Akteur Mitarbeiter |
| include-Richtung Basis → eingebundener Fall | entfällt | entfällt | drei Pfeile auf Berechtigungsprüfung |
| Attributverteilung wie im Lösungshinweis | entfällt | Neupreis, Baujahr, Schadenshöhe, auszahlen() oben; restwertBerechnen() unten | entfällt |

Ergebnis: keine Abweichung. Grenzwert 1.000,00 EUR liegt im manuellen Zweig
(`[ab 1.000 EUR]`), genau 10 Arbeitstage in der Variante im Zweig ohne Freigabe.
Der Beamer-Mietpreis 135,00 EUR entspricht 25 × 5 + 10 und begründet die eigene Methode.
Keine Korrektur am Fragment nötig; `node pruef/check.js kapitel/17-a8.html --fragment`
meldet unverändert „Keine Fehler."

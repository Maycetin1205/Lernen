# K-5 · B9 · Rechenprüfung 2026-09-06

Das Kapitel enthält keine Sachrechnungen: Alle dreizehn Teilaufgaben sind Nenn-, Erklär- und Zuordnungsaufgaben (Projektmerkmale, SMART, Lastenheft gegen Pflichtenheft, Projektschritte, Stakeholder, Bedarfsanalyse, Phasenreihenfolge). Weder Original-Lösungen noch Varianten enthalten eine Größe, die aus anderen Größen berechnet wird. Geprüft wurde deshalb nur die Punktelogik der Lösungshinweise und die Summe der Kam-dran-Zeile, dazu die Textbreiten der SVG-Beschriftungen nach §9.

Vor dem Schreiben mit Node ausgeführt (Skript im Scratchpad der Sitzung, `rechnungen-b9.js`):

```js
console.log('H24 4.1: Zweck 2+2, Beispiel 1+1 =', 2+2+1+1);
console.log('H22 1.3: 6 Schritte x 1 P =', 6*1);
console.log('F22 1.4: 3 Zeilen x 2 P =', 3*2);
console.log('H21 1.1: 4 Merkmale x 1 P =', 4*1);
console.log('H21 1.2: 4 Buchstaben x 1 P =', 4*1);
console.log('H21 3.1: 5 Aspekte x 1 P =', 5*1);
console.log('H22 1.5: 5 Vor-/Nachteile x 1 P =', 5*1);
console.log('H23 4.2: 6 Felder x 0,5 P =', 6*0.5);
console.log('F23 4.2: 2 Unterschiede x 2 P =', 2*2);
console.log('Kam dran H21 4+4+5 =', 4+4+5);
console.log('Kam dran F22 6+1 =', 6+1);
console.log('Kam dran H22 6+3+5 =', 6+3+5);
console.log('Kam dran F23 4+2 =', 4+2);
console.log('Kam dran H23 3+3 =', 3+3);
console.log('Kam dran H24 6 =', 6);
console.log('Summe Kapitel =', 13+7+14+6+6+6);
console.log('Tuckman-Kurve: Phasenspalten 5 x 116 =', 5*116, ' ab x=40 bis', 40+5*116);
console.log('Textbreite 13px: "Lösungsweg, Technik, Abnahmekriterien" =', 'Lösungsweg, Technik, Abnahmekriterien'.length*6.5);
console.log('Textbreite t2: "Rückmeldung fließt in den nächsten Zyklus" =', 'Rückmeldung fließt in den nächsten Zyklus'.length*5.8);
console.log('Textbreite t2: "Scrum Master: verantwortlich dafür, dass Scrum gelebt wird" =', 'Scrum Master: verantwortlich dafür, dass Scrum gelebt wird'.length*5.8);
```

Ausgabe:

```text
H24 4.1: Zweck 2+2, Beispiel 1+1 = 6
H22 1.3: 6 Schritte x 1 P = 6
F22 1.4: 3 Zeilen x 2 P = 6
H21 1.1: 4 Merkmale x 1 P = 4
H21 1.2: 4 Buchstaben x 1 P = 4
H21 3.1: 5 Aspekte x 1 P = 5
H22 1.5: 5 Vor-/Nachteile x 1 P = 5
H23 4.2: 6 Felder x 0,5 P = 3
F23 4.2: 2 Unterschiede x 2 P = 4
Kam dran H21 4+4+5 = 13
Kam dran F22 6+1 = 7
Kam dran H22 6+3+5 = 14
Kam dran F23 4+2 = 6
Kam dran H23 3+3 = 6
Kam dran H24 6 = 6
Summe Kapitel = 52
Tuckman-Kurve: Phasenspalten 5 x 116 = 580  ab x=40 bis 620
Textbreite 13px: "Lösungsweg, Technik, Abnahmekriterien" = 240.5
Textbreite t2: "Rückmeldung fließt in den nächsten Zyklus" = 237.8
Textbreite t2: "Scrum Master: verantwortlich dafür, dass Scrum gelebt wird" = 336.4
```

Abgleich mit den Lösungshinweisen (aus den Extraktionsnotizen):

| Aufgabe | Lösungshinweis | Eigene Rechnung | Ergebnis |
|---|---|---|---|
| H24 4.1 | „Inhalt jeweils 2 Punkte; Beispiel jeweils 1 Punkt“, 6 P | 2 + 2 + 1 + 1 = 6 | stimmt |
| H22 1.3 | 6 P, sechs offene Zeilen, keine Teilpunktzeile | 6 × 1 = 6 | stimmt (Verteilung „je Zeile 1 P“ ist eigene Ableitung) |
| F22 1.4 | 6 P für drei Erläuterungen | 3 × 2 = 6 | stimmt |
| H21 1.1 | 4 P, je Merkmal 1 P | 4 × 1 = 4 | stimmt |
| H21 1.2 | 4 P, je Buchstabe 1 P | 4 × 1 = 4 | stimmt |
| H21 3.1 | 5 P, je Aspekt 1 P | 5 × 1 = 5 | stimmt |
| H22 1.5 | 5 P, fünf Angaben | 5 × 1 = 5 | stimmt |
| H23 4.2 | „je richtigem Feld 0,5 Punkte“, 3 P | 6 × 0,5 = 3 | stimmt |
| F23 4.2 | 4 P, zwei Unterschiede, keine Aufteilung angegeben | 2 × 2 = 4 | stimmt (Aufteilung ist Ableitung der Notiz) |
| Kam dran | MATRIX.md: 13 Teilaufgaben, 52 P | 13 + 7 + 14 + 6 + 6 + 6 = 52 | stimmt |

Varianten: Die Variante zu F22 1.4 nennt „18 Arbeitsplätze“ als Szenariogröße; damit wird nicht gerechnet. Keine weiteren Zahlen.

SVG-Textbreiten: Alle Beschriftungen wurden mit 6,5 Einheiten je Zeichen (13 px), 5,8 (t2) und 7,6 (mono) überschlagen; die drei knappsten Fälle stehen oben. Die Tuckman-Kurve nutzt fünf Spalten zu 116 Einheiten von x = 40 bis x = 620.

## Kontrolle 2026-09-06

Geprüft: die drei Original-Aufgaben `b9-original-1` bis `b9-original-3` und die drei Varianten
`b9-variante-1` bis `b9-variante-3`.

Geprüfte Angaben je Original: Szenario gegen die Extraktionsnotiz, Vollständigkeit der Lösung
gegen den Lösungskern, Punktzahl in `p.herkunft`, Absatz „Punkte" gegen die amtliche Verteilung,
fachliche Richtigkeit jeder Aussage.

- `b9-original-1` (H24 4.1, 6 P): Szenario Identify OHG (elektronische Schließsysteme und
  Ausweise) stimmt. Die Tabelle nennt Zweck und Beispiel je Heft; die Beispiele stehen auf der
  richtigen Seite (Teilleistungen, Rahmenbedingung, Datenschutz links; Ansprechpartner,
  Zeitrahmen, Testszenarien und Abnahmekriterien rechts). Punkteaufteilung 2 + 1 je Spalte stimmt
  mit „Inhalt jeweils 2 Punkte; Beispiel jeweils 1 Punkt". Ohne Befund.
- `b9-original-2` (H22 1.3, 6 P): Szenario Package AG (Verpackungshersteller, Automatisierung
  wegen gestiegener Nachfrage) stimmt. Alle sechs offenen Schritte sind mit einem passenden
  Aspekt belegt, je Schritt 1 Punkt, der vorgegebene erste Schritt zählt nicht mit. Ohne Befund.
- `b9-original-3` (F22 1.4, 6 P): Szenario und das vorgegebene Beispiel „Räumliche Gegebenheiten"
  stimmen. Alle drei Zeilen nennen Inhalt und Wirkung auf das Angebot, 2 Punkte je Zeile.
  Ohne Befund.
- `b9-variante-1` bis `b9-variante-3`: unabhängig selbst beantwortet und verglichen. Jede Variante
  fragt dieselbe Sache wie ihr Original (Zweck und Beispielinhalt der beiden Hefte; sechs
  Projektschritte mit Inhalt; drei Informationen für die Angebotserstellung), jede Lösung liefert
  die geforderte Anzahl und je Aspekt beide Punkteteile. Ohne Befund.

Geprüfte Fachangaben: Scrum-Rollen (Product Owner, Scrum Master, Developers), drei Artefakte,
fünf Ereignisse mit Sprint als Container, Sprint höchstens ein Monat, Daily Scrum höchstens
15 Minuten (`scrum-guide-2020`); Tuckman-Phasen Forming, Storming, Norming, Performing plus
Adjourning 1977 (`tuckman-1965`, `tuckman-jensen-1977`); SMART nach Doran; RFC 2119 für Muss,
Soll, Kann; § 640 BGB zur Abnahme; Phasenreihenfolge des Datenbankentwurfs gegen H23 4.2.
Alle stimmen.

Korrigiert wurden zwei Angaben außerhalb der Aufgabenblöcke, die eine Musterlösung falsch stützen:

1. Abschnitt „Die Sache", Absatz „Vom Bedarf zum Auftrag". Alt: „Das Systemhaus antwortet mit dem
   Pflichtenheft: Lösungsweg, eingesetzte Technik, Teilleistungen, Ansprechpartner, Zeitrahmen,
   Testszenarien und Abnahmekriterien." Der Fußnotenverweis nennt die Lösungshinweise zu H24 4.1;
   dort steht „Festlegung von Teilleistungen" aber in der Spalte Lastenheft, so wie auch die
   Tabelle in `b9-original-1`. Neu: „Teilleistungen" gestrichen.
2. Derselbe Absatz, Methoden der Bedarfsanalyse. Alt: „Interview, schriftlicher Befragung,
   Beobachtung am Arbeitsplatz, Fokusgruppe oder Auswertung von Beschwerden." Die Lösungshinweise
   zu H23 1.4 nennen Interviews, schriftliche Befragungen, Fokusgruppe, Beschwerden auswerten und
   Medien analysieren; die Beobachtung steht nicht darunter, die Medienanalyse fehlte. Neu:
   „Interview, schriftlicher Befragung, Fokusgruppe, Auswertung von Beschwerden oder
   Medienanalyse." Selbstcheck 3 entsprechend angepasst: die drei sicheren Antworten sind jetzt
   Interview, schriftliche Befragung und Fokusgruppe, ergänzt um Beschwerden und Medienanalyse.

Ergebnis: `node pruef/check.js kapitel/28-b9.html --fragment` meldet nach beiden Änderungen
„Keine Fehler."; der Wortzahl-Hinweis bleibt unverändert bestehen, die Wortzahl sank von 3981
auf 3976 und liegt damit weiter deutlich unter der Obergrenze von 4500.

# RECHNUNGEN B10 · Kunde, Kommunikation und Veränderung

Geprüft am 2026-09-06 mit Node v25 (ein Aufruf, alle Zeilen zusammen).

Kapitel B10 ist ein Erklärkapitel. Es enthält keine Sachrechnung in Beispiel, Original-Lösung oder Variante: Alle sechzehn Teilaufgaben sind vom Typ Nennen oder Erklären, die Lösungen bestehen aus Begriff, Erklärung und Szenariobezug. Die einzige Rechenaufgabe im Umfeld (H23 2.5, Hotline-Minutensatz; F25 4.3, Chatbot-Jahreskosten) liegt in A2 und wird dort protokolliert.

Nachgerechnet wurden deshalb nur die Zahlen, die im Fragment als Punkteangaben oder Prüfungsfakten erscheinen.

| Nr. | Eingabe (Node) | Ausgabe | Abgleich |
|---|---|---|---|
| 1 | `[4,6,6,3,9,4,4,2,4,4,6,2,4,2,4,4].reduce((a,b)=>a+b,0)` | `68` aus 16 Teilaufgaben | MATRIX.md Tabelle 2: 68 Punkte, 16 Teilaufgaben. Stimmt. |
| 2 | `10+18+4+14+12+10` | `68` | MATRIX.md Tabelle 1, Zeile B10 (H21 10, F22 18, F23 4, H23 14, F25 12, H25 10). Stimmt; Kam-dran-Zeile daraus abgeleitet. |
| 3 | `2022-1985` | `37` | F22 1.1: Heft und Lösungshinweis sprechen von „über 35 Jahre Marktpräsenz". 37 ≥ 35, Formulierung übernommen. |
| 4 | `3*2+3*1` | `9` | F22 1.1 (6 P) und 1.2 (3 P) zusammen 9 P: Lösungshinweis „3 x 2 Punkte Botschaft, 3 x 1 Punkt Stichpunkt". Stimmt. |
| 5 | `3*(2+1)` | `9` | F22 1.3: „jeweils 2 Punkte Inhalt, 1 Punkt Sprache", drei Leistungsangebote. Stimmt. |
| 6 | `8*0.5` und `4*1` | `4` und `4` | F23 4.1: Lösungshinweis 0,5 P je Antwort (acht Antworten), Heft ein Argument je Feld (vier Felder). Beide Lesarten ergeben 4 P; im Fragment als Konvention benannt: je Feld zwei Argumente schreiben. |
| 7 | `3*2` | `6` | F25 4.1: drei Stellen zu je 2 P (Stelle plus Nutzen). Stimmt. |
| 8 | `2*2` | `4` | F25 4.4: Vorteil 2 P, Nachteil 2 P (Aussage plus Wirkung). Stimmt. |
| 9 | `2*2` und `2*1` | `4` und `2` | H25 1.8: zwei Maßnahmen zu je 2 P; H25 1.7: zwei Ursachen zu je 1 P. Stimmt. |
| 10 | `4*1` | `4` | H23 1.8: vier Ebenen des Vier-Seiten-Modells, der Sache nach 1 P je Ebene (keine ausdrückliche Aufteilung im Lösungshinweis). |
| 11 | `2*2` | `4` | H23 2.6: „2 x 2 Punkte" für zwei Argumente in ganzen Sätzen. Stimmt. |
| 12 | `3*2` und `4*1` | `6` und `4` | H21 3.5: drei Beschreibungen zu je 2 P; H21 3.4: zwei Vorteile, zwei Nachteile zu je 1 P. Stimmt. |

Abweichungen zu den Lösungshinweisen: keine. Die Doppellesart in Zeile 6 wird im Fragment offen benannt, nicht aufgelöst (Bauplan §2 Regel 3).

## Kontrolle 2026-09-06

Geprüft: die drei Original-Aufgaben `b10-original-1` bis `b10-original-3` und die drei Varianten
`b10-variante-1` bis `b10-variante-3`.

Geprüfte Angaben je Original: Szenario gegen die Extraktionsnotiz, Vollständigkeit der Lösung
gegen den Lösungskern, Punktzahl in `p.herkunft`, Absatz „Punkte" gegen die amtliche Verteilung,
fachliche Richtigkeit jeder Aussage.

- `b10-original-1` (F25 4.1, 6 P): Szenario (drei Rechtsanwälte, IT-Beratungsunternehmen,
  fünfschrittiger Ablauf, Beispiel in Schritt 1 vorgegeben) stimmt. Die Lösung wählt drei Stellen
  und nennt je Stelle Tätigkeit der KI und Nutzen; sie deckt die Beispiele der Lösungsdatei zu den
  Schritten 2, 3 und 4 ab und weist auf Schritt 5 als zulässige Alternative hin. 2 Punkte je
  Stelle stimmen. Ohne Befund.
- `b10-original-2` (H25 1.8, 4 P): Szenario Apothekengruppe Curatia stimmt. Zwei Maßnahmen
  (informieren; schulen und begleiten mit Key-Usern) mit je einer Wirkung auf die Beschäftigten;
  die weiteren Punkte der Liste (Beteiligung, verständliche Anleitungen, neue anspruchsvollere
  Tätigkeiten) sind ergänzt. Hinweis auf 1.7 mit zwei Ursachen zu je 1 Punkt stimmt. Ohne Befund.
- `b10-original-3` (H23 1.8, 4 P): Szenario OptiSoft-XXL GmbH nach der Preiserhöhung stimmt. Alle
  vier Ebenen sind gefüllt, die Ebenen 2 bis 4 in der Ich-Form des Kunden wie im Lösungshinweis,
  die Sachebene als Wiedergabe der Aussage. 1 Punkt je Ebene stimmt. Ohne Befund.
- `b10-variante-1` bis `b10-variante-3`: unabhängig selbst beantwortet und verglichen. Jede
  Variante fragt dieselbe Sache wie ihr Original (drei KI-Einsatzstellen in einem fünfschrittigen
  Ablauf; zwei Maßnahmen des Veränderungsmanagements mit Wirkung; Zerlegung einer Kundenaussage in
  vier Seiten), jede Lösung liefert die geforderte Anzahl und beide Punkteteile. In Variante 1 ist
  zusätzlich die menschliche Bestätigung genannt, in Variante 3 der Anschluss an Sach- und
  Appellseite. Ohne Befund.

Geprüfte Fachangaben: Lewin-Phasen Auftauen, Bewegen, Einfrieren (`lewin-1947`); Kotter mit acht
Stufen und frühen Erfolgen (`kotter-1996`); die vier Seiten nach Schulz von Thun und die
IHK-Bezeichnungen 4-Ohren-Modell und Selbstaussage; Art. 50 KI-Verordnung (Transparenzpflicht bei
Interaktion) und Art. 22 DSGVO (automatisierte Einzelfallentscheidung); die vier Vermittlungsformen
gegen H21 3.5; die drei Schwächen der Störungsannahme gegen H23 1.2; die Hotline-Argumente gegen
H23 2.6; 0,5 Punkte je Argument gegen F23 4.1. Alle stimmen.

Korrigiert wurde eine Angabe außerhalb der Aufgabenblöcke:

1. Abschnitt „Die Sache", Absatz „Veränderung führen". Alt: „Die Ursachen sind Gewohnheit, Angst
   vor Kontroll- oder Arbeitsplatzverlust, fehlende Information, befürchteter Mehraufwand und
   fehlende Beteiligung." Der Fußnotenverweis nennt H25 1.7; dort steht als zweite von fünf
   Ursachen ausdrücklich die Überforderung gegenüber neuen technischen Systemen, die auch die
   Lösung von `b10-original-2` als Beispiel anführt. Neu: „Überforderung" in die Aufzählung
   eingefügt (ein Wort).

Ergebnis: `node pruef/check.js kapitel/29-b10.html --fragment` meldet nach der Änderung
„Keine Fehler."; der Wortzahl-Hinweis bleibt bestehen, die Wortzahl stieg von 3802 auf 3803 und
liegt weiter deutlich unter der Obergrenze von 4500.

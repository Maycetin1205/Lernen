# Entscheidungen Bauer K-2, Kapitel A7 (Programmlogik und Schreibtischtest)

Nur echte Entscheidungen an Stellen, an denen der Bauplan schweigt oder zwei Wege offen ließ.

1. **Neun Begriffskarten statt fünfzehn Pflichtbegriffen.** §6 nennt 15 Pflichtbegriffe, §10 erlaubt
   höchstens 10 Karten. Zusammengefasst wurden: Variable + Datentyp + Zuweisung; Bedingung +
   boolescher Ausdruck; Array + Index; Compiler + Interpreter; logischer Fehler + Laufzeitfehler.
   Grund: Diese Paare werden in den Prüfungen immer gemeinsam abgefragt und lassen sich nur
   gegeneinander erklären.

2. **Drei Original-Aufgaben: F25 3.6, H24 2.5, H21 2.5.** Der Auftrag ließ die Wahl zwischen
   F25 3.6 und F22 4.4 als punktreichster Aufgabe. Gewählt wurde F25 3.6, weil sie die
   Verschachtelung und den Grenzfall „größer als 80“ zugleich prüft und als Text abbildbar ist.
   F22 4.4 und H22 4.4 sind Struktogramm-Zeichenaufgaben; ihr Kern (Platzierung des inneren
   Zählers, Schleifenbedingung) steckt in Abb. A7-2 und in zwei Begriffskarten, die
   Darstellungsform gehört zu A8. Mehr als drei Originale erlaubt §10 nicht.

3. **Variante 1 verwendet dieselbe Funktion mit anderen Aufrufwerten** statt eines neu erfundenen
   Pseudocodes. Grund: Das Heft selbst gibt zu einem Code zwei Aufrufe; die Prüfungsleistung ist
   der Pfad, nicht das Lesen eines zweiten Programms. Zusätzlicher Nutzen: Das Wortbudget bleibt
   für die beiden anderen Varianten frei, die wirklich neue Szenarien brauchen.

4. **Vier Abbildungen statt der drei geforderten.** Die vierte (Compiler gegen Interpreter am
   Zeitpunkt des Programmstarts) kam dazu, weil H24 2.3 (3 Punkte) sonst nur in einer
   Begriffskarte vorkäme und der Unterschied genau ein zeichenbarer Zeitpunkt ist (§9 Fall 3).

5. **Dezimalpunkt im Code, Komma im Fließtext.** Die Lösungsdatei zu F25 3.5/3.6 schreibt
   Python-Ausgaben mit Punkt, §8 verlangt für den Fließtext das deutsche Komma. Beides steht so
   im Kapitel, mit einem Satz Erklärung im ersten Absatz des Verfahrens, damit der Widerspruch
   nicht als Fehler gelesen wird.

6. **Ausgabetexte der PowerShell-Skripte in ASCII** („genuegend“, „verfuegbar“). Das entspricht der
   Vorlage im Heft und ist in Skripten üblich; es ist kein Rechtschreibfehler des Kapitels und wird
   deshalb nicht „korrigiert“.

7. **Nicht belegbare Zahl gestrichen.** Ein Merke-Block enthielt im Entwurf den Satz „Drei von vier
   Fehlern in Prüfungsaufgaben zu diesem Kapitel sitzen an genau solchen Grenzen“. Diese Quote ist
   aus den Notizen nicht belegbar und wurde entfernt (§2 Regel 2).

8. **Quelle q5 ohne Verweis-Element.** `ihk-konvention-schreibtischtest` hat in QUELLEN-A.md den
   Status „geprüft“, aber keine URL (Spalte „–“). Nach §7 Regel 3 kommt ohne geprüfte URL kein
   `a`-Element in die Datei; ausgewiesen wird deshalb `(nicht online geprüft)`, genauso wie bei den
   Prüfungsheften. Dasselbe gilt für `aho-compilers`.

9. **Wortzahl 3440 statt der im Auftrag genannten 3400.** Der Prüfer zählt den Inhalt der drei
   `pre`-Blöcke mit; allein der Pseudocode der Original-Aufgabe 1 sind rund 120 Wörter. Weiteres
   Kürzen hätte Prüfungslogik entfernt (Ergebnistexte, Zweige). Der Wert liegt unter dem
   Prüferschwellwert 3500 und weit unter der Obergrenze 4500 aus §10.

10. **Temporäre Dateien.** Das Rechenskript und die beiden Kürzungsskripte liegen im
    Sitzungs-Scratchpad des Harness, nicht unter `Lernen/`. Im Projekt sind nur die drei
    beauftragten Dateien entstanden: `kapitel/16-a7.html`, `notizen/RECHNUNGEN-a7.md`,
    `notizen/ENTSCHEIDUNGEN-K2-a7.md`.

11. **Sichtprüfung im Browser nicht möglich.** Die Vorschaudatei liegt außerhalb des Projektordners
    und wird vom Browser-Werkzeug nur als statischer Schnappschuss geöffnet, ohne Bildschirmfoto.
    Ersatzweise wurden alle SVG-Beschriftungen rechnerisch auf Überlauf geprüft (6,5 Einheiten je
    Zeichen bei 13&nbsp;px, 5,8 bei `t2`, 7,6 bei `mono`): kein Text verlässt seine Box oder den
    Rand bei x&nbsp;=&nbsp;640. Die endgültige Sichtprüfung bleibt Phase Z.

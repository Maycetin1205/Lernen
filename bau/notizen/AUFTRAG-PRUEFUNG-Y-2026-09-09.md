# Auftrag – Gegenprüfung der Einheiten 3 bis 8 (Stand 2026-09-09, 13:45 Uhr)

Du bist der Prüfer, nicht der Autor. Ein anderer Opus-Chat hat heute die Einheiten 3 bis 8 aus
`notizen/AUFTRAG-CODEX-2026-09-09.md` umgesetzt und meldet alles grün. Deine Aufgabe: nachsehen, ob das stimmt,
klare Fehler beheben, Geschmacksfragen nur aufschreiben.

Lies zuerst: `notizen/AUFTRAG-CODEX-2026-09-09.md` (Abschnitte 1, 2, 3 mit den Einheiten 3–8, Abschnitt 4
Abschlussroutine) und in `ENTSCHEIDUNGEN.md` den Abschnitt „Entscheidungen Y“ (Einträge zu Einheit 3 bis 8).
Arbeitsordner: `C:\Users\mu.aycetin\Desktop\Lernen\bau`.

## Womit du vergleichst

`_sicherung_2026-09-09_vorY/fertig-Y<n>/` enthält die Kapiteldateien nach Abschluss von Einheit n.
`fertig-Y3` = Stand vor Einheit 4, `fertig-Y4` = Stand vor Einheit 5 usw. Ein Diff `fertig-Y<n-1>` gegen
`fertig-Y<n>` zeigt genau, was Einheit n geändert hat. Kapitel, die in einem Ordner fehlen, wurden in dieser
Einheit nicht angefasst; nimm dann den jüngsten älteren Stand. Verlass dich auf die Diffs, nicht auf das Protokoll.

## Schritt 0: grüner Start

`node pruef/bauen-in-bau.js` → „Keine Fehler.“, `node pruef/abnahme.js` → „Keine Befunde.“
Koffer `C:/Users/mu.aycetin/Desktop/iCloudDrive/AP1/AP1-Koffer/` hat genau drei Dateien, Lerndatei byte-identisch
mit `bau/AP1_Lerndatei.html`. Dann eigenen Sicherungsordner anlegen: `_sicherung_2026-09-09_vorY/pruefung/` mit
Kopie aller 20 Kapiteldateien, bevor du etwas änderst.

## Was du je Einheit prüfst

**Einheit 4 (Fragekette).** Für jede neue „Frage vorab“: Kann der Leser sie mit dem beantworten, was im Kapitel
davor steht? Stimmt die zugeklappte Antwort fachlich? Steht keine Frage vor „Das Problem“ oder „Rechenweg-Schema“?
Stichprobe: alle Fragen in A2 und A9 (je 7 und 8, die meisten), dazu je zwei in den übrigen Kapiteln.

**Einheit 5 (Vergleichsbilder).** Die fünf Bilder B7-1, B2-2, B1-8, B5-8, A6-8 ansehen:
`python pruef/vorschau.py <id>` und die PNG-Streifen in `notizen/vorschau/` öffnen. Prüfen: genau ein Akzent,
drei Zeilen untereinander, Zahlen im Bild = Zahlen im Text daneben. Fachlich nachrechnen: Sonntag Vollsicherung
plus Mo–Do, Rückspielen für Donnerstagabend = 1 Datenträger (täglich voll), 2 (differenziell), 5 (inkrementell).
Hub Schicht 1, Switch Schicht 2, Router Schicht 3. Bei Abb. B2-2: Ist der Angreifer-Akzent tatsächlich nur beim
offen mitgeschickten Schlüssel? Text im SVG lesbar bei normaler Bildschirmgröße?

**Einheit 6 (Zuordnungstabellen).** Tabelle Schutzziele in B1 gegen `notizen/2021-herbst.md` Aufgabe 4.1,
Tabelle Open Source in B6 gegen `notizen/2025-fruehjahr.md` Aufgabe 2.6. Jede Zeile muss den Lösungshinweisen
entsprechen. Doppelt der Typischer-Fehler-Kasten etwas, was die Begriffskarte schon sagt?

**Einheit 7 (Alltagswort zuerst).** Zwei Richtungen:
a) Die 18 geänderten Stellen: Ist das Alltagswort fachlich richtig? Ist das Fachwort noch da (IHK fragt es ab)?
   Steht die Erklärung beim ersten Auftreten im Kapitel, nicht erst beim zweiten?
b) Was übersehen wurde: 18 Stellen in 12 Kapiteln sind wenig für 20 Kapitel. Suche in allen 20 Kapiteln nach
   Fachwörtern ohne Alltagswort beim ersten Auftreten. Die Liste aus dem Auftrag ist der Anfang (Nennleistung,
   Weisungsbindung, Rechenschaftspflicht, Latenz, Multiplizität, Kardinalität, abnahmefähig, Gewährleistungsfrist),
   danach eigene Funde. Maßstab: Umschüler ohne Vorwissen. Bis zu zehn klare Fälle selbst beheben, den Rest
   als Liste ins Protokoll. Vorher Wortzahl prüfen: A7 4488, B11 4478, B7 4467, B9 4466 (Grenze 4500). Dort
   nur ändern, wenn du an anderer Stelle im selben Kapitel gleich viel kürzt.

**Einheit 8 (Beispielzahlen).** B7 Parität mit 7 + 12 = 19 nachrechnen, in Text, Tabelle und Bild. A3 Rangfolge
und A2 Gewinnschwelle: Rechnung nachrechnen, Einheiten überall gleich (nicht einmal „Stück“, einmal ohne).
Dann selbst suchen: Gibt es in A1 bis A9 und B7 weitere Rechenbeispiele, deren Zahlen wie Prüfungswerte wirken
oder ohne Einheit dastehen? Aufschreiben, nur beheben, wenn eindeutig.

**Einheit 3 (Kasten „Für die Prüfung reicht“).** Nur Stichprobe: drei der dreizehn Kästen lesen (B7 RAID,
A1 Subnetting, A6 Puffer). Steht darin wirklich nur, was aufs Papier muss, und stimmt es mit den gelösten
Originalaufgaben im Abschnitt `-original` überein?

## Kollateralschäden (für alle Einheiten, per Diff und Skript)

- Keine `id` geändert: alle `h4 id="<kap>-k<n>"` und alle `<kap>-abb<n>-t` von `fertig-Y3`
  bis heute identisch. Wegweiser-Ziele (`WEGWEISER-*.json`, `lektion`-Felder) zeigen noch auf passende Abschnitte.
- Nichts doppelt: gleiche Frage zweimal, gleicher Kasten zweimal, Tabelle sagt dasselbe wie der Absatz davor.
- Merke-Kästen höchstens 6 je Kapitel, Begriffskarten 5–12, Wortzahlen unter 4500.
- Ton: Lehrer, kurze Sätze, kein Fachchinesisch. Wenn dir eine neue Passage wie ein Fachbuch klingt, aufschreiben.
- Ersetztes prüfen: Bei Abb. B7-1 und B2-2 wurden alte Bilder ersetzt. Ging dabei ein Inhalt verloren, auf den der
  Text noch verweist?

## Regeln für Korrekturen

- Klarer Fehler (falsche Zahl, falsche Zuordnung, falsches Alltagswort, Frage nicht beantwortbar): beheben.
- Geschmack, Stil, „hätte man anders machen können“: nur aufschreiben, nicht ändern.
- Keine neue Idee umsetzen, keine Regel in `check.js` ändern.
- Nach jeder Änderung Abschlussroutine aus Abschnitt 4 des Codex-Auftrags: Fragmentcheck, ggf. wegweiser-bauen.py,
  ggf. vorschau.py, bauen-in-bau.js, abnahme.js, Koffer, Protokoll, STATUS-Zeile.
- Protokoll in `ENTSCHEIDUNGEN.md` unter Abschnitt Y anhängen: „Gegenprüfung Einheiten 3–8 (2026-09-09, Opus)“.
  Drei Teile: was geprüft, was behoben (mit Kapitel und Stelle), was offen bleibt (Liste mit Einschätzung wichtig /
  unwichtig). Nur anhängen, nie löschen.

## Bericht an den Nutzer

Am Ende eine kurze Nachricht in Klartext, höchstens 15 Zeilen: Was war falsch, was ist behoben, was bleibt offen
und ob er sich darum kümmern muss. Kein Fachchinesisch, keine Prüfprotokolle im Chattext, Zahlen nur, wenn sie
eine Entscheidung ändern. Wenn alles in Ordnung war, genügt ein Satz plus die offene Liste.

## Wenn dein Kontingent knapp wird

Kein angefangenes Kapitel halbfertig lassen. Letzter Protokolleintrag „Reststand Gegenprüfung“: welche Einheiten
geprüft, welche nicht, welche Korrekturen fertig, was noch anzusehen wäre. Halbfertige Datei aus
`_sicherung_2026-09-09_vorY/pruefung/` zurückholen, dann bauen, abnahme, Koffer.

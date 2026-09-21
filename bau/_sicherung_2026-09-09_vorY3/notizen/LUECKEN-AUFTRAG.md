# LÜCKEN-AUFTRAG · Inhaltslücken schließen und Begriffskarten in Klartext (2026-09-08)

Du bearbeitest genau ein Kapitel: `bau/kapitel/<NN>-<id>.html`. Arbeitsverzeichnis `C:\Users\mu.aycetin\Desktop\Lernen\bau`. Lies zuerst `bau/notizen/LEHRER-VORLAGE.md` (Ton, Bildregeln, Sprache) und `bau/notizen/WEGWEISER-<id>.md` sowie `bau/notizen/WEGWEISER-<id>.json` (dort stehen die Lücken deines Kapitels und die Zuordnung Aufgabe → Absatz). Dann deine Kapiteldatei vollständig.

## Teil 1: Lücken schließen

Eine Lücke ist eine Prüfungsteilaufgabe, zu der das Kapitel nichts oder zu wenig sagt (Feld `hinweis` im JSON, Abschnitt „Lücken“ im MD). Für jede Lücke:

1. Lies die Aufgabe im Original: `bau/notizen/<jahr>-<saison>.md` (z. B. `2022-herbst.md`), Abschnitt `### <nr> | …`, samt Lösungshinweis dort. Die Lösung sagt dir, was die IHK hören will.
2. Ergänze im Kern (`<section id="<id>-kern">`) das Fehlende an der logisch richtigen Stelle: entweder ein Absatz unter der passenden vorhandenen Zwischenüberschrift oder eine neue Zwischenüberschrift `<h4 id="<id>-k<n>">` mit der **nächsten freien Nummer** (vorhandene ids nie ändern, nie neu nummerieren). Erklären wie ein Lehrer für Leser ohne Vorwissen: erst wozu, dann was, dann wie; ein Beispiel mit den Zahlen der Aufgabe, wenn gerechnet wird. Ein Bild nur, wenn es einen Mechanismus zeigt (Bildregeln in LEHRER-VORLAGE.md §6).
3. Jede fachliche Aussage braucht einen Quellenverweis `<sup class="q"><a href="#<id>-q<n>" title="…">n</a></sup>`. Passt eine vorhandene Quelle, nimm sie. Sonst darfst du **eine Quelle ohne URL** in `ol.quellenliste` ergänzen, im Format der vorhandenen Einträge, mit `<span class="abruf">(nicht online geprüft)</span>` und eindeutiger `data-src`; niemals eine URL erfinden. Norm, RFC, Gesetz oder Herstellerdokumentation mit Nummer, Titel, Jahr. Findest du keine belastbare Quelle, schreibe nur, was aus den IHK-Lösungshinweisen folgt, und zitiere die Prüfungsquelle des Kapitels (`IHK-Prüfung`).
4. Rechnungen (JBOD-Kapazität, Anzahl Teilnetze, Ratenrechnung) mit `python -c` nachrechnen und in `bau/notizen/RECHNUNGEN-<id>.md` anhängen (Eingabe, Ausgabe).
5. Aktualisiere `bau/notizen/WEGWEISER-<id>.json`: Die Lücken-Aufgaben zeigen jetzt auf die neue oder ergänzte Zwischenüberschrift, `hinweis` wird leer. Nichts anderes darin ändern. Gültiges JSON.

Was **keine** Lücke ist: Aufgaben, die nur eine andere Zahl oder ein anderes Szenario haben als das Kapitelbeispiel, das Verfahren aber identisch ist. Dort nichts ergänzen.

## Teil 2: Begriffskarten in Klartext

Der Begriffe-Abschnitt liegt am Kapitelende in `<details><summary>Begriffe aufklappen (n Karten)</summary><div class="inhalt"> … </div></details>`. Diese Hülle bleibt exakt so. Jede Karte (`dl.begriff`, id unverändert, genau die vier Zeilen mit den Labels „Was es ist“, „Wo es dir begegnet“, „Nicht verwechseln mit“, „So fragt die IHK“) wird umgeschrieben nach LEHRER-VORLAGE.md §5:

- **Was es ist:** erster Satz in Alltagsworten, wie man es einem Kollegen ohne Vorwissen sagt. Dann höchstens ein Satz fachlicher Kern. Der vorhandene Quellenverweis bleibt in dieser Zeile (Pflicht, sonst meldet der Prüfer einen Fehler).
- **Wo es dir begegnet:** ein konkretes Beispiel aus dem Kapitelfall oder einer Prüfungsaufgabe. Keine zweite Definition.
- **Nicht verwechseln mit:** beginnt mit dem Ding, mit dem es verwechselt wird, dann woran man beide auseinanderhält. Gibt es keine echte Verwechslung, nenne die eine wichtigste Abgrenzung in einem Satz.
- **So fragt die IHK:** kürzen auf das, was der Leser beim Antworten wissen muss (Operator, was die Lösungshinweise erwarten). Quellenverweise behalten.
- 40 bis 80 Wörter je Karte. Normsprache raus („logische Netzwerkadresse zur Adressierung von Knoten“ wird „die Hausnummer eines Geräts im Netz“). Keine Zahl, kein Fachbegriff, der im Kern nicht vorkommt, es sei denn, die Karte erklärt genau ihn.
- Begriffe im Glossar A–Z verlinken auf diese Karten; deshalb bleiben ids und Anzahl der Karten gleich. Nur der Text ändert sich.

## Grenzen

- Kapitel höchstens 4 400 Wörter (Prüfer zählt; die Wegweiser-Tabelle zählt nicht). Wenn Teil 1 Platz braucht, holst du ihn in Teil 2 (kürzere Karten) oder bei Wiederholungen, nie bei Originalen, Varianten, Selbstcheck.
- Nichts außer deiner Kapiteldatei, `WEGWEISER-<id>.json` und `RECHNUNGEN-<id>.md` verändern. Kein Zusammenbau, kein Koffer, kein `00-kopf.html`, kein `check.js`.
- Die Wegweiser-Tabelle am Ende von „Worum es geht“ (`<nav aria-label="Prüfungsaufgaben dieses Kapitels">`) nicht anfassen; sie wird nach deiner Arbeit aus dem JSON neu erzeugt.
- Sprache: Du-Form, kurze Sätze, kein Ausrufezeichen, kein Geviertstrich, keine Emojis, kein `style`, nur Klassen aus dem System.

## Abnahme

1. `node pruef/check.js kapitel/<NN>-<id>.html --fragment` meldet „Keine Fehler.“
2. `python pruef/vorschau.py <id>` meldet keine Befunde; wenn du ein Bild ergänzt hast, sieh dir den zugehörigen Streifen mit dem Read-Werkzeug an.
3. `python -c "import json;json.load(open(r'notizen/WEGWEISER-<id>.json',encoding='utf-8'))"` läuft ohne Fehler.
4. Bericht `bau/notizen/LUECKEN-<id>.md`, höchstens acht Zeilen: welche Lücken geschlossen, welche nicht und warum, neue Quellen, Wörter vorher/nachher, Karten umgeschrieben (Anzahl).

Antworte am Ende mit höchstens fünf Zeilen Klartext.

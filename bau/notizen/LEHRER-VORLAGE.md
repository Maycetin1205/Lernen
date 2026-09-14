# LEHRER-VORLAGE · Umbau der Kapitel in den Lehrer-Stil (2026-09-08)

Diese Datei ist der verbindliche Auftrag für den Umbau eines Kapitels. Das fertige Muster ist `bau/kapitel/15-a6.html` (Netzplan). Lies es vollständig, bevor du anfängst, und baue dein Kapitel nach demselben Prinzip. Alle Regeln aus `Lernen/BAUPLAN.md` §2, §7, §8, §9 gelten weiter; diese Vorlage präzisiert und übersteuert nur die Punkte, die hier genannt sind.

## 1. Für wen und warum

Der Leser hat zu dem Thema **kein Vorwissen**, kann nicht programmieren, lernt am Bild und am durchgerechneten Beispiel, hat kurze Konzentrationsfenster. Sein Auftrag wörtlich: „Du bist ein Lehrer. Deine Schüler haben überhaupt keine Ahnung. Die Lerndatei soll ihnen alles von Grund auf in einer logischen Reihenfolge erklären, die Logik, den Sinn dahinter.“ Und: „Nicht übertreiben.“

Das heißt konkret:
- Erst das Problem, dann die Lösung. Nie eine Definition, bevor der Leser weiß, wozu das Ding gut ist.
- Ein durchgehendes Beispiel mit echten Zahlen, das von Anfang bis Ende durchgezogen wird.
- Jeder Schritt bekommt ein Bild, wenn es etwas zu zeigen gibt (Ablauf, Aufbau, Gegenüberstellung, Rechenkette, Zuordnung im Raum). Ein Bild pro Schritt, mit genau den Zahlen dieses Schritts.
- Die Regel in einem Satz, direkt nach dem Schritt, in dem sie gebraucht wird.
- Zusammenfassung am Ende, nicht am Anfang.
- Begriffe erst am Kapitelende, zum Nachschlagen.

## 2. Was unverändert bleibt

- Die Kapitel-id, alle vorhandenen `id`-Attribute (Glossar und Navigation verlinken darauf), die Zeile „Kam dran“ wörtlich.
- Die Abschnitte „So hat die IHK gefragt“, „Jetzt du“, „Selbstcheck“ und „Quellen“ inhaltlich. Sprachliche Glättung erlaubt, keine neuen Zahlen, keine neuen Aufgaben.
- Alle Zahlen, Formeln, Ergebnisse. Neue Rechenbeispiele nur, wenn das Kapitel ohne durchgehendes Beispiel nicht erklärbar ist; dann jede Zahl mit `python -c` nachrechnen und in `bau/notizen/RECHNUNGEN-<id>.md` anhängen (Eingabe, Ausgabe).
- Die Quellen. Keine neuen Quellen, keine neuen URLs. Eine Aussage ohne Quelle im Kapitel wird weggelassen, nicht erfunden. Fachliche Aussagen behalten ihren `<sup class="q">`-Verweis.
- Das Gestaltungssystem: nur die Klassen aus `00-kopf.html` (siehe §6), kein CSS, kein `style` außerhalb von SVG, keine neuen Klassen.
- Andere Dateien: nicht anfassen. Kein `00-kopf.html`, kein `check.js`, kein `bauen.js`, keine anderen Kapitel, nichts im Koffer.

## 3. Neue Reihenfolge der Abschnitte

1. `<header class="kapitel-kopf">` wie bisher, aber die Sprungleiste `nav.kapitel-wege` in dieser Reihenfolge: Worum es geht · Das Verfahren (bzw. Die Sache) · So hat die IHK gefragt · Jetzt du · Selbstcheck · Begriffe · Quellen.
2. `<section id="<id>-worum">` Worum es geht: der konkrete Fall aus dem Systemhaus (bleibt), plus ein Satz, **warum es dieses Verfahren oder diese Sache überhaupt gibt** (welches Problem sie löst). 80 bis 150 Wörter.
3. `<section id="<id>-kern">` Das Verfahren / Die Sache: die Lektion, siehe §4.
4. `<section id="<id>-original">` So hat die IHK gefragt (unverändert).
5. `<section id="<id>-variante">` Jetzt du (unverändert).
6. `<section id="<id>-selbstcheck">` Selbstcheck (unverändert).
7. `<section id="<id>-begriffe">` mit `<h3>Begriffe zum Nachschlagen</h3>` und direkt darunter `<p class="unter">Nicht durchlesen. Wenn dir im Verfahren oder in einer Aufgabe ein Wort fehlt, schlag es hier nach.</p>` (bei B-Kapiteln „in der Sache“ statt „im Verfahren“), dann `nav.begriffsliste` und die Karten, siehe §5.
8. `<section id="<id>-quellen">` Quellen (unverändert).

`check.js` prüft nur, dass alle Abschnitte vorhanden sind, nicht ihre Reihenfolge. Die ids der Abschnitte bleiben exakt so.

## 4. Der Kern als Lektion

Aufbau, jeweils mit `<h4>`-Zwischenüberschriften, die die Wörter aus den Prüfungsaufgaben tragen (aus `kapitel/03-matrix.html`, Abschnitt „Die neun Prüfungen im Einzelnen“; Strg+F von der Papieraufgabe muss in den richtigen Absatz führen):

1. **Das Problem.** Ein bis zwei Absätze: Was will der Kunde oder die Prüfung wissen, warum reicht der naive Weg nicht. Bei A6: „Einfach zusammenzählen ergibt 21 Tage, und das ist falsch.“ Wenn es zum Thema gehört, hier die Ausgangsdaten als Tabelle (Vorgangsliste, Angebotstabelle, Adressvorgabe).
2. **Die Bausteine.** Was der Leser kennen muss, bevor gerechnet oder gezeichnet wird, mit Bild: der Kasten und seine Felder, die 32 Bit und der Schnitt, die Symbole des Diagramms, die Schichten des Modells. Jeder Fachbegriff wird in dem Satz erklärt, in dem er zum ersten Mal vorkommt, und zwar in Alltagswörtern („Puffer, also die Luft, die der Vorgang hat“). Abkürzung beim ersten Auftreten ausschreiben.
3. **Die Schritte.** Ein Schritt je `<h4>`. Jeder Schritt: was passiert, warum, am Beispiel mit Zahlen, dann die Regel in einem Satz. Wo der Schritt einen Zustand erzeugt, den man zeichnen kann, bekommt er ein Bild mit genau dem Stand nach diesem Schritt (A6: erst nur obere Felder gefüllt, dann auch untere, dann Puffer). Dieselbe Geometrie in allen Schrittbildern, damit der Leser das Bild wiedererkennt und nur die neuen Zahlen sieht.
4. **Die Falle.** Wo Lernende typischerweise scheitern: ein `div.merke` mit `data-art="Typischer Fehler"`, so nah wie möglich an der Stelle, an der der Fehler passiert.
5. **Vom Verfahren zur Prüfung.** Was die IHK genau verlangt (Operator, Format der Antwort, Punktelogik), `data-art="Prüfungsnotiz"`.
6. **Rechenweg-Schema** (`pre.rechenweg`, nur Gruppe A): das, was der Leser in der Prüfung hinschreibt. Bleibt, wenn vorhanden.
7. **Auf einen Blick** (`div.merke data-art="Auf einen Blick"`): drei bis fünf Merksätze, jeder beginnt mit dem Begriff in `<strong>`. Steht am **Ende** des Kerns, nicht am Anfang.

Für Gruppe B („Die Sache“) gilt dasselbe Prinzip ohne Rechenschema: Problem (welche Frage des Kunden oder welche Bedrohung) → Bausteine mit Bild → Zusammenhang Schritt für Schritt oder Gegenüberstellung als Tabelle → Falle → Prüfungsnotiz → Auf einen Blick. Wo die IHK „Nennen Sie drei …“ fragt, steht die Antwort als nummerierte Liste mit genau so vielen Punkten.

Höchstens fünf `merke`-Blöcke je Kapitel (einschließlich Auf einen Blick), erlaubte `data-art`: Auf einen Blick, Merke, Typischer Fehler, Prüfungsnotiz.

**Nicht übertreiben.** Nicht jeder Absatz wird ein Bild. Ein Bild kommt, wo es einen Mechanismus zeigt (BAUPLAN §9, fünf Fälle). Ein Bild, das nur wiederholt, was der Absatz sagt, wird gestrichen. Wo ein Bild den Text ersetzt, wird der beschreibende Satz gelöscht und der faktentragende behalten. Richtwert: Gruppe A vier bis sieben Abbildungen, Gruppe B drei bis sechs. Vorhandene gute Abbildungen behalten und in die Schrittfolge einordnen, Nummern (`Abb. <Kapitel>-<n>`) fortlaufend neu vergeben, jede Abbildung wird im Text genannt.

## 5. Begriffskarten am Kapitelende

Fünf bis zehn Karten, ids unverändert, genau die vier Zeilen mit den Labels „Was es ist“, „Wo es dir begegnet“, „Nicht verwechseln mit“, „So fragt die IHK“. Neu ist der Ton:
- **Was es ist:** erster Satz in Klartext, wie man es einem Kollegen ohne Vorwissen sagt („Die Luft eines Vorgangs: so viele Tage darf er rutschen, ohne dass das Projektende wandert“). Danach, wenn nötig, der fachliche Kern in einem Satz. Quellenverweis bleibt Pflicht.
- **Wo es dir begegnet:** ein konkretes Beispiel aus dem Kapitelfall oder aus einer Prüfungsaufgabe. Keine zweite Definition.
- **Nicht verwechseln mit:** beginnt mit dem Ding, mit dem verwechselt wird („dem freien Puffer. Der Gesamtpuffer schont …“), dann woran man beide auseinanderhält. Steht dort keine echte Verwechslung, sondern nur eine weitere Regel, wird die Zeile umgeschrieben oder auf die wichtigste Abgrenzung reduziert.
- **So fragt die IHK:** bleibt, wenn sie gut ist.
Jede Karte 40 bis 90 Wörter. Was im Kern schon erklärt ist, wird hier nicht wiederholt, sondern kurz gefasst.

## 6. Bilder (SVG)

- `<figure class="abb">` mit `<svg viewBox="0 0 640 H" role="img" aria-labelledby="<id>-abb<n>-t">`, `<title id="<id>-abb<n>-t">`, `<figcaption>Abb. <KAP>-<n>: …</figcaption>`. Die Bildunterschrift sagt, was man sehen soll.
- Klassen ausschließlich: `l` (Linie, 2 Einheiten), `f` (gefüllte Form, hell), `w` (weiße Form), `a` (Akzentlinie, 3 Einheiten), `fa` (Akzentfläche, sparsam), `d` (gestrichelt grau), `g` (Gitter), Text: `t2` (klein, grau, 11,5 px), `tb` (fett), `ta` (Akzent, fett), `mono`, `mitte` (text-anchor middle), `rechts` (text-anchor end). Pfeile: `marker-end="url(#pfeil)"`, `url(#pfeil-a)`, `url(#pfeil-g)`. Nichts anderes, keine eigenen Farben, keine Filter, kein `style`.
- Schrift nie kleiner als 11 im viewBox-Maß. Textbreite abschätzen: 13-px-Text rund 6,5 Einheiten je Zeichen, `t2` rund 5,8, fette Schrift rund 6,8. Kein Text über den Rand (640) und kein Text über einem anderen Text oder über einer Linie, die er nicht beschriftet.
- Der Akzent markiert je Bild genau eine Sache: die Stelle, um die es in diesem Schritt geht. Vorwärtsbild: die Stelle, wo zwei Wege zusammenlaufen. Rückwärtsbild: die Gabelung.
- Beschriftung an das Ding, nicht in eine Legende. Erklärende Sätze unter dem Bild im Bild als `t2` sind erlaubt (zwei Zeilen), wenn sie das Lesen des Bildes anleiten.
- Schrittbilder: gleiche Geometrie, nur der Füllstand ändert sich. Leere Felder bleiben sichtbar leer.

## 7. Sprache

Du-Form, kurze Sätze, ein Gedanke je Satz. Alltagswörter zuerst, Fachwort in Klammern oder im selben Satz. Keine Ausrufezeichen, kein Geviertstrich (nur „ – “), kein „In diesem Kapitel“, kein „lernst du“, keine Motivationssprache, keine Zeitangaben für den Lernenden. Absätze im Kern beginnen mit dem Begriff, um den es geht, in `<strong>` (höchstens ein `<strong>` je Absatz). HTML-Sonderzeichen maskieren (`&lt;`, `&gt;`, `&amp;`), geschütztes Leerzeichen zwischen Zahl und Einheit.

## 8. Umfang

Richtwert 2 500 bis 4 000 Wörter ohne SVG (check.js zählt), Obergrenze 4 500 ist ein Fehler. Wenn die Lektion Platz braucht, kürze die Begriffskarten und Wiederholungen, nie die Originale und Varianten.

## 9. Besondere Hinweise je Kapitel

- **A1** (macht der Auftraggeber selbst) – nicht bearbeiten.
- **A2 Kaufmännisch rechnen** (kommt in jeder Prüfung): jede Rechenart als Rechenkette oder Treppe (Listenpreis → Rabatt → Skonto → Bezugspreis), ein Bild je Kette, die Zahlen aus dem Kapitelbeispiel. Erst erklären, was Skonto überhaupt ist (Belohnung fürs schnelle Zahlen), dann rechnen.
- **A7 Programmlogik**: Der Leser kann nicht programmieren. Von null: Was ist eine Variable (ein beschriftetes Kästchen mit einem Wert), was eine Bedingung, was eine Schleife, was ein Akkumulator (ein Kästchen, in das man immer wieder dazuzählt). Der Schreibtischtest als Tabelle mit einer Zeile je Durchlauf, in zwei oder drei Bildern oder Tabellen schrittweise gefüllt. Struktogramm-Symbole einmal als Legende mit Alltagsworten.
- **A8 UML**: Symbole einmal als Legende (Alltagswort daneben), dann ein Diagramm in zwei oder drei Schritten aufbauen.
- **A9 Datenmodell und SQL**: Von null: Was ist eine Tabelle, eine Zeile, ein Schlüssel, warum braucht man Beziehungen (Problem: doppelte Daten). Chen und Krähenfuß nebeneinander am selben Beispiel. SQL-Abfrage Wort für Wort übersetzt („SELECT = zeig mir, FROM = aus der Tabelle, WHERE = aber nur die Zeilen, bei denen …“).
- **A3, A4, A5**: Rechenketten als Bild; A4 die Leiter Bit → Byte → KiB → MiB mit Faktor 1024 gegen 1000.
- **B1, B2**: Angriff oder Schutz als Ablaufbild mit Rollen (Angreifer, Nutzer, Server). B2: symmetrisch gegen asymmetrisch nebeneinander mit denselben zwei Personen; Signatur als Ablauf in Schritten.
- **B5**: OSI-Schichten als Stapel, neben jeder Schicht in Alltagsworten, was sie tut und welches Gerät dort arbeitet; Fehlersuche von unten nach oben als Schrittfolge. Dieses Kapitel ist Grundlage für A1, also besonders sorgfältig von null.
- **B9**: SMART als fünf Kästen mit je einem Wort und einem Beispielsatz, nicht als Absatz. Lasten- gegen Pflichtenheft nebeneinander (wer schreibt, was steht drin, wann). Scrum als Kreislauf.
- **B7**: Sicherungsarten auf einem Zeitstrahl (was wird jeweils gesichert), RAID als Plattenbilder.
- **B3, B6, B8, B10, B11**: Gegenüberstellungen als Tabelle, Abläufe als Bild (Meldeweg, Vertragsarten als Entscheidungsbaum), Aufzählungen ab vier Punkten abzählbar.

## 10. Arbeitsablauf und Abnahme

1. `bau/kapitel/15-a6.html` lesen (Muster). Dann das eigene Kapitel vollständig lesen. Dann `kapitel/03-matrix.html` nach den Prüfungsformulierungen des Kapitels durchsuchen.
2. Lektion planen: Welches Beispiel zieht sich durch, welche Schritte, welches Bild je Schritt. Dann schreiben.
3. Prüfen: `node pruef/check.js kapitel/<NN>-<id>.html --fragment` muss „Keine Fehler.“ melden. Hinweise lesen; der Wörter-Hinweis über 3 500 ist erlaubt, Fehler nicht.
4. Ansehen: `python pruef/vorschau.py <id>` erzeugt Bildstreifen in `bau/notizen/vorschau/` und meldet Textüberlappungen in den Abbildungen. Jeden Streifen mit dem Read-Werkzeug ansehen. Beheben, was nicht sitzt (Text über Linien, zu enge Kästen, unlogische Reihenfolge), dann Schritt 3 und 4 wiederholen, bis es stimmt.
5. Bericht: `bau/notizen/LEHRER-<id>.md`, höchstens zehn Zeilen: Was ist die Lektion (Beispiel, Schritte), Abbildungen vorher/nachher, Wörter, was du bewusst nicht gemacht hast und warum. Kein Lob, keine Wiederholung dieser Vorlage.
6. Nichts anderes anfassen, keinen Zusammenbau starten. Die Sicherung des Ausgangsstands liegt in `bau/_sicherung_2026-09-08_kapitel/`.

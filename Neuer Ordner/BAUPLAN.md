# BAUPLAN · AP1-Lerndatei

Stand: 2026-09-02. Verfasst von Claude (Fable) als verbindliche Bauanweisung. Ausführung durch Claude Opus in Claude Code, in Phasen (§5), jede Phase als eigener Agent. Der Plan ist so geschrieben, dass kein Bauer Rückfragen stellen muss. Wo der Plan schweigt, gilt §2 Regel 7.

## 0. Auftrag in einem Absatz

Baue **eine** Datei `C:\Users\mu.aycetin\Desktop\Lernen\AP1_Lerndatei.html`, aus der ein Auszubildender (Fachinformatiker Systemintegration, Umschulung, Vorwissen pro Thema: null) die IHK-Abschlussprüfung Teil 1 „Einrichten eines IT-gestützten Arbeitsplatzes“ lernt. Die Datei erklärt jedes prüfungsrelevante Thema von Grund auf (theoretisch, praktisch, didaktisch), belegt jede Aussage mit einer Quelle, zeigt an sinngemäß wiedergegebenen Original-Aufgaben, wie die IHK fragt und Punkte vergibt, und lässt den Lernenden jedes Verfahren an einer Variante selbst anwenden. Die Datei wird in einem Durchlauf gebaut, in Kapitel-Fragmenten unter `Lernen/bau/kapitel/`, und mit `node bau/pruef/bauen.js` zusammengesetzt. Danach ist sie fertig. Sie wird benutzt, nicht weiterentwickelt.

## 1. Für wen

Quelle dieser Angaben: Gespräch mit dem Lernenden am 2026-09-02 und `Desktop/Projekt/AP1/PRODUCT.md`.

- Fachinformatiker Systemintegration in Umschulung, arbeitet in einem IT-Systemhaus. Vorwissen zum jeweiligen Thema: null annehmen.
- Hat Angst, an umformulierten Aufgaben zu scheitern, weil er Musterlösungen statt der Sache gelernt hat. Deshalb: Verfahren erklären, dann Original, dann Variante.
- Wurde von KI-generiertem Material schon einmal „durch schiere Menge erschlagen“. Deshalb: feste Wortbudgets (§10), keine Füllsätze, keine Wiederholungen zwischen Kapiteln (stattdessen Querverweis).
- Konzentrationsfenster gering (ADHS). Deshalb: immer derselbe Kapitelaufbau, sichtbare Abschnitte, ein Verfahren pro Kapitel, Lösungen zugeklappt.
- Will Begriffe **theoretisch, praktisch und didaktisch** erklärt. Deshalb: Begriffskarten mit genau vier Zeilen (§10).
- Will **immer Quellenangaben**. Deshalb: §7.
- Will **keine Zeitangaben** (keine Lesezeiten, keine Tages- oder Wochenpläne, keine Minutenvorgaben). Einzige erlaubte Zeitangabe: die Prüfungsdauer selbst als Prüfungsfakt.
- Will ein Design, das ein „Meisterwerk“ ist, hell, ohne „KI-Design“. Deshalb: das Gestaltungssystem in `00-kopf.html` ist fertig und wird nicht verändert (§9).
- Ziel: mindestens 90 Prozent. Deshalb: Rechen- und Zeichenverfahren fehlerfrei, Erklärthemen im Antwortformat der IHK.

## 2. Eiserne Regeln

Diese Regeln stehen über allem anderen im Plan.

1. **Eine Ausgabedatei.** Reines HTML, CSS und das kleine Skript aus `99-fuss.html`. Kein Framework, kein npm-Paket, kein Build-Tool, kein Markdown-Renderer, keine externen Ressourcen (keine Webfonts, kein CDN, keine externen Bilder). Alle Abbildungen sind inline SVG. Die Datei muss von `file://` aus offline funktionieren und drucken.
2. **Jede fachliche Aussage hat eine Quelle.** Ohne Quelle keine Aussage. Wenn keine Primärquelle auffindbar ist: Aussage weglassen oder, wenn sie aus IHK-Lösungshinweisen stammt, als `IHK-Konvention` kennzeichnen.
3. **Keine erfundenen Quellen.** Eine URL kommt nur in die Datei, wenn sie in `bau/notizen/QUELLEN-A.md` oder `QUELLEN-B.md` als „geprüft“ mit Abrufdatum steht (Phase Q, §5). Sonst nur Titel, Nummer, Jahr, ohne URL, mit Vermerk „nicht online geprüft“.
4. **Keine Zeitangaben für den Lernenden.** Siehe §1.
5. **Original-Aufgaben nie wörtlich.** Sinngemäß wiedergeben: gleiche Zahlen, gleiche Struktur, eigene Worte. Code und Pseudocode: Logik beibehalten, Variablennamen und Formulierung ändern. Herkunft immer angeben: „AP1 Herbst 2024, Aufgabe 3b, 4 Punkte, sinngemäß wiedergegeben“. Grund: Urheberrecht der IHK-Aufgabenstelle und Didaktik (Wiedererkennen in anderer Formulierung).
6. **Rechnen wird nachgerechnet.** Jede Zahl in Beispiel, Original-Lösung und Variante wird mit einem Python- oder Node-Einzeiler geprüft, bevor sie in das Fragment kommt. Die Prüfung wird in `bau/notizen/RECHNUNGEN-<kapitel>.md` protokolliert (Eingabe, Ausgabe). Original-Lösungen werden gegen die IHK-Lösungshinweise abgeglichen. Abweichung zwischen eigener Rechnung und Lösungshinweisen: in `bau/ENTSCHEIDUNGEN.md` notieren und die IHK-Zahl mit Fußnote verwenden.
7. **Keine Rückfragen an den Nutzer.** Wo der Plan schweigt: die einfachste Variante wählen, Entscheidung mit einem Satz Begründung in `bau/ENTSCHEIDUNGEN.md` anhängen, weitermachen.
8. **grundlast nicht anfassen.** Weder `Desktop/grundlast` noch `Desktop/Projekte/Porjekte/AP1/grundlast` verändern, starten oder importieren. Lesen einzelner Inhaltsdateien als Rohmaterial ist erlaubt (§3), jede daraus übernommene Aussage wird gegen Primärquellen geprüft.
9. **Gestaltung nur aus dem System.** Nur die Klassen aus `00-kopf.html` und der Vorlage. Verboten: Emojis, Icon-Fonts, Farbverläufe, Glas- und Blur-Effekte, Schatten, Karten-Raster, bunte Info-Boxen, Dunkelmodus, `style`-Attribute außerhalb von SVG, Fettdruck als Betonungsersatz, `<img>`.
10. **Ein Durchlauf.** Kein Redesign, keine zweite Architektur, keine Version 2. Fertig ist, wenn §12 erfüllt ist. Fehler werden im betroffenen Fragment behoben und die Datei neu zusammengesetzt. Mehr nicht.
11. **Nichts außerhalb von `Lernen/bau/` und `Lernen/AP1_Lerndatei.html` schreiben.** Quellmaterial wird nur gelesen.
12. **Prüfer ist Pflicht.** Kein Fragment gilt als fertig, bevor `node bau/pruef/check.js <fragment> --fragment` „Keine Fehler.“ meldet. Hinweise des Prüfers werden gelesen und, wenn berechtigt, umgesetzt.

## 3. Eingaben

Alle Pfade unter `C:/Users/mu.aycetin/Desktop/`. Ordner- und Dateinamen enthalten Umlaute, Leerzeichen, `&` und Klammern; einige Dateinamen verwenden zerlegte Unicode-Umlaute. Immer mit Glob suchen und Pfade in Anführungszeichen setzen. Nur lesen.

### 3.1 Aufgabenhefte (OCR-Fassungen, Text extrahierbar)

Ordner: `Projekte/Porjekte/AP1/PrüfungenOCR/`

| Prüfung | Datei (Glob-Muster) |
|---|---|
| Herbst 2021 | `Herbst 2021 Teil 1*OCR*.pdf` |
| Frühjahr 2022 | `Fr*her 22 Teil 1*OCR*.pdf` |
| Herbst 2022 | `Herbst 22 Teil 1*OCR*.pdf` |
| Frühjahr 2023 | `AP1Fr2023*OCR*.pdf` |
| Herbst 2023 | `AP1_Herbst_2023*OCR*.pdf` |
| Frühjahr 2024 | `1. AP1 Fr*hjahr 2024 Fi*OCR*.pdf` |
| Herbst 2024 | `AP1_Herbst_2024*OCR*.pdf` |
| Frühjahr 2025 | `ap1_fr*hjahr_2025*OCR*.pdf` |
| Herbst 2025 | `2025 Herbst - FiAE*OCR*.pdf` (die AP1 ist für alle IT-Berufe identisch) |

Die Datei `Frühjahr2021*` ist die **alte Zwischenprüfung** (Ankreuzformat) und wird nicht ausgewertet.

**PDF lesen: so, nicht anders.** Das Read-Tool kann PDFs auf diesem Rechner nicht rendern (`pdftoppm` fehlt). Geprüft am 2026-09-02 funktionieren diese zwei Wege:

1. **Text** (immer zuerst): `pdftotext -layout -enc UTF-8 "<pfad>" -` in Bash. `-layout` erhält Spalten und Tabellen, was für Punktezeilen und Wertetabellen nötig ist. Ausgabe in eine Datei unter dem Scratchpad-Ordner umleiten und dann in Abschnitten lesen, wenn sie lang ist. Ein Aufgabenheft ergibt rund 15 000 bis 25 000 Zeichen.
2. **Seitenbild** (nur für Abbildungen, Netzpläne, ER-Modelle, UML, Anschlussbilder, Formulare und für Seiten ohne Textebene): mit PyMuPDF rendern, dann die PNG-Datei mit dem Read-Tool ansehen.
   ```
   python -c "import fitz,sys; d=fitz.open(sys.argv[1]); d[int(sys.argv[2])].get_pixmap(dpi=150).save(sys.argv[3])" "<pfad>" <seite-ab-0> "<ziel.png>"
   ```
   PNGs in den Scratchpad-Ordner schreiben, nicht nach `Lernen/`.

`pypdf` (6.7.5) und PyMuPDF (1.27.2.3) sind installiert, `pdftotext` liegt in `/mingw64/bin`. `pypdf` schreibt Warnungen auf stderr, die nichts bedeuten. Hat eine Lösungsdatei keine Textebene (bekannt für `Ap1_Lösung (1).pdf`, Herbst 2025), führt nur Weg 2 zum Ziel. Bleibt eine Seite unlesbar: als „nicht lesbar“ in den Notizen vermerken und weitermachen.

**Urheberrecht.** Auf dem Deckblatt der Hefte steht, dass Vervielfältigung, Verbreitung und öffentliche Wiedergabe der Prüfungsaufgaben und Lösungen nicht gestattet sind (ZPA Nord-West, mit Verweis auf §§ 97 ff., 106 ff. UrhG). Die Lerndatei ist ein privates Lernmittel für eine Person und gibt Aufgaben deshalb ausschließlich sinngemäß wieder (§2 Regel 5). Diese Regel ist nicht verhandelbar: kein Aufgabentext, kein Lösungstext und keine Formulierung aus den Heften wird wörtlich übernommen.

### 3.2 Lösungshinweise (Punkteverteilung)

Ordner: `Projekte/Porjekte/AP1/Lerndateien/Informationen/FISI AP1 & AP2/Prüfungen/Prüfungen AP1/AP1 und Zwischenprüfungen/AP1 (Neue Prüfungsordnung)/`

| Prüfung | Unterordner | Lösungsdatei |
|---|---|---|
| Herbst 2021 | `AP1 2021/IHK_Prüfung_AP1_Herbst_2021/` | `Herbst 2021 Lösungen Teil 1.pdf` |
| Frühjahr 2022 | `AP1 2022/IHK_Prüfung_AP1_Frühjahr_2022/` | `Früher 22 Lösung Teil 1.pdf` |
| Herbst 2022 | `AP1 2022/IHK_Prüfung_AP1_Herbst_2022/` | `Herbst 22 Lösung Teil 1.pdf` |
| Frühjahr 2023 | `AP1 2023/IHK_Prüfung_AP1_Frühjahr_2023/` | `2023_Fruhjahr_Losung_1.pdf` |
| Herbst 2023 | `AP1 2023/IHK_Prüfung_AP1_Herbst_2023/` | `AP1_Herbst_2023_Loesung.pdf` |
| Frühjahr 2024 | `Ap1 2024/IHK_Prüfung_AP1_Frühjahr_2024/` | `2. AP1 Frühjahr 2024 Fi Lösungen.pdf` |
| Herbst 2024 | `Ap1 2024/IHK_Prüfung_AP1_Herbst_2024/` | `AP1_Herbst_2024_Loeser.pdf` |
| Frühjahr 2025 | `Ap1 2025/IHK_Prüfung_AP1_Frühjahr_2025/` | `ap1_frühjahr_2025_lösungen.pdf` |
| Herbst 2025 | `Ap1 2025/IHK_Prüfung_AP1_Herbst_2025/` | `Ap1_Lösung (1).pdf` |

In denselben Unterordnern liegen die nicht-OCR-Aufgabenhefte.

### 3.3 Bereits aufbereitetes Material (Rohmaterial, spart Lesezeit, ersetzt keine Primärquelle)

- `Projekt/AP1/Fruehjahr_2022_Teil1_Aufgaben_mit_Loesungen.md`: Aufgaben und Lösungen Frühjahr 2022 als Markdown.
- Im Ordner aus §3.2: `AP1_Fruehjahr_2024_Lernkurs.md`, `AP1_Herbst_2024_Lernkurs.md`, `AP1_Fruehjahr_2025_Lernkurs.md`, `AP1_Herbst_2025_Lernkurs.md`. Von ChatGPT/Codex erzeugte Lernkurse mit „Punkteübersicht“ je Aufgabe und Transferaufgaben. Fachlich nicht geprüft. Nutzen: Punkteübersichten, Aufgabenstruktur, Ideen für Varianten. Jede fachliche Aussage daraus ist gegen Primärquellen zu prüfen.
- `Projekte/Porjekte/AP1/LERNPLAN.md` (Juli 2026): Themenliste mit Prioritäten, Rechen-Checkliste, Prüfungstag-Strategie, Hinweis auf einen geänderten AKA-Prüfungskatalog ab 2025. Sekundärquelle.
- `Projekt/AP1/PRODUCT.md`: Leserbeschreibung und Gestaltungsverbote des Lernenden.
- `Projekte/Porjekte/AP1/grundlast/src/content/` und `grundlast/src/content/`: MDX-Lerntexte zu vielen Themen. Optionales Rohmaterial, wenn Lernkurse zu einem Kapitel nichts hergeben (z. B. Netzplan, Backup, Ergonomie). Nicht importieren, nur lesen.
- SVG-Vorlagen im Ordner aus §3.2, Unterordner `assets/` (Anschlüsse, Netzwerk, ER-Modell, UML, Ratendarlehen): dürfen angesehen und im Stil des Systems **neu gezeichnet** werden. Nicht einbetten.

### 3.4 Feste Bauteile (fertig, nicht verändern)

- `Lernen/bau/kapitel/00-kopf.html`: Dokumentkopf, komplettes CSS, Navigation, SVG-Marker, Titelblock.
- `Lernen/bau/kapitel/01-benutzung.html`: Teil 0.
- `Lernen/bau/kapitel/99-fuss.html`: Skript (Häkchen, Druck, Navigation) und Dokumentende.
- `Lernen/bau/vorlage/kapitel-vorlage.html`: verbindliche Kapitelvorlage.
- `Lernen/bau/pruef/check.js`: Prüfer. `Lernen/bau/pruef/bauen.js`: Zusammenbau.
- Werkzeuge vorhanden: Node v25, Python 3.14.

## 4. Ausgabe und Ordnerstruktur

```
Lernen/
  AP1_Lerndatei.html            ← Ergebnis (erzeugt von bauen.js)
  BAUPLAN.md                    ← dieser Plan
  bau/
    STATUS.md                   ← Übersicht der Phasen
    ENTSCHEIDUNGEN.md           ← alle Entscheidungen der Bauer (anhängen, nie löschen)
    status/<Phase>.done         ← Marker je abgeschlossener Phase mit Kurzbericht
    notizen/
      2021-herbst.md … 2025-herbst.md   ← Extraktion je Prüfung (Format §5.1)
      MATRIX.md                  ← Cluster × Prüfung, Punkte
      QUELLEN-A.md, QUELLEN-B.md ← geprüfte Quellen (Format §5.2)
      RECHNUNGEN-<kapitel>.md    ← Nachrechnungsprotokolle
    kapitel/
      00-kopf.html, 01-benutzung.html, 02-pruefung.html, 03-matrix.html,
      10-a1.html … 18-a9.html, 20-b1.html … 30-b11.html,
      90-verfahrensblatt.html, 91-glossar.html (erzeugt), 92-quellen.html (erzeugt), 99-fuss.html
    pruef/  check.js, bauen.js
    vorlage/ kapitel-vorlage.html
```

Dateinummern sind fest: A1 = 10 … A9 = 18, B1 = 20 … B11 = 30.

## 5. Arbeitsablauf in Phasen

Jede Phase ist ein eigener Agent mit eigenem Kontext. Ergebnisse liegen ausschließlich auf der Platte. Ein Agent, der neu startet, liest zuerst `bau/status/` und macht beim ersten fehlenden Marker weiter. Abschluss einer Phase: Marker-Datei `bau/status/<Phase>.done` mit fünf bis zehn Zeilen Kurzbericht (was erzeugt, was unklar).

| Phase | Aufgabe | Eingaben | Ausgaben | Abhängig von |
|---|---|---|---|---|
| E1, E2, E3 | Extraktion je drei Prüfungen | §3.1, §3.2, §3.3 | `notizen/<jahr>-<saison>.md` | – |
| Q-A | Quellen prüfen: Prüfung, A1 bis A9 | §6, §7 | `notizen/QUELLEN-A.md` | – |
| Q-B | Quellen prüfen: B1 bis B11 | §6, §7 | `notizen/QUELLEN-B.md` | – |
| M | Matrix, Teil 1, Teil 2 | alle Notizen, QUELLEN-A | `notizen/MATRIX.md`, `02-pruefung.html`, `03-matrix.html` | E1 bis E3, Q-A |
| K-1 … K-5 | Kapitel schreiben | MATRIX, Notizen, QUELLEN, Vorlage | `10-a1.html` … `30-b11.html` | M, Q-A, Q-B |
| V | Verfahrensblatt | Kapitel A1 bis A9 | `90-verfahrensblatt.html` | K-1, K-2 |
| Z | Zusammenbau und Sichtprüfung | alle Fragmente | `AP1_Lerndatei.html` | alle K, V |
| F | Fachliche Gegenprüfung | fertige Datei, Notizen | Korrekturen in Fragmenten, neuer Zusammenbau | Z |

### 5.1 Format der Extraktionsnotizen (`notizen/<jahr>-<saison>.md`)

```
# AP1 <Saison> <Jahr>

Aufgabenheft: <Pfad>
Lösungshinweise: <Pfad>
Gelesen am: <JJJJ-MM-TT>

## Deckblatt
- Aufgaben: <n>
- Punkte je Aufgabe: <z. B. 25 / 25 / 25 / 25>
- Gesamtpunkte: <n>
- Bearbeitungszeit: <Minuten>
- Alle Aufgaben Pflicht: <ja/nein, Wortlaut der Regel auf dem Deckblatt>
- Hilfsmittel: <Wortlaut>
- Sonstiges vom Deckblatt: <…>

## Szenario
<Drei bis sechs Sätze in eigenen Worten: Unternehmen, Rolle des Prüflings, Auftrag.>

## Teilaufgaben
### <Nr> | <Thema in 3 bis 8 Wörtern> | <Punkte> P | <Typ> | <Kapitel-id>
Aufgabe (eigene Worte, vollständig, alle Zahlen; Tabellen als Markdown-Tabelle):
<…>
Material (Abbildungen beschreiben; Code oder Pseudocode wörtlich, weil Code keine Prosa ist):
<…>
Lösungskern (aus den Lösungshinweisen; Stichworte; Punkteverteilung genau wie dort):
<…>
Bemerkung (Unklarheiten, OCR-Lücken, Zweitzuordnung zu anderem Kapitel):
<…>
```

Typ ist genau einer von: `Rechnen`, `Zeichnen`, `Erklären`, `Nennen`, `Zuordnen`, `Fachtext`. Ein Schreibtischtest am Pseudocode gilt als `Rechnen`, weil dort wie bei einer Rechnung ein Verfahren schrittweise zu einem Ergebnis führt.

Kapitel-id ist genau eine aus `a1` bis `b11` (§6); passt eine Teilaufgabe zu zwei Kapiteln, entscheidet der Kern der Aufgabe, das zweite Kapitel steht in der Bemerkung. Punkte kommen aus dem Aufgabenheft oder den Lösungshinweisen; nicht lesbar heißt `?`, niemals raten. Jede Teilaufgabe wird direkt nach dem Lesen der Prüfung geschrieben, nicht am Ende gesammelt.

**Nummerierung der Teilaufgaben (verbindlich für alle Phasen).** Die Hefte bezeichnen Teilaufgaben mit Buchstaben (`a`, `b`, `da`, `db` …), die Matrix und die Kapitel brauchen Zahlen (Form `H24 1.4`). Deshalb wird je Hauptaufgabe fortlaufend `<Hauptaufgabe>.<n>` in Heftreihenfolge numeriert, beginnend bei 1. Die Bezeichnung aus dem Heft steht als erste Zeile der Bemerkung, damit sie auffindbar bleibt. Die Herkunftszeile in den Kapiteln (§10) nennt die Nummer dieses Schemas.

### 5.2 Format der Quellenlisten (`notizen/QUELLEN-A.md`, `QUELLEN-B.md`)

Eine Markdown-Tabelle:

```
| Schlüssel | Kapitel | Typ | Zitat | URL | Status | Abrufdatum | Fundstellen |
```

- `Schlüssel`: stabil, kleingeschrieben, Bindestriche, z. B. `rfc-4632`, `dsgvo-2016-679`, `bgb`, `arbstaettv`, `bsi-grundschutz-2023`, `omg-uml-2-5-1`, `ihk-ap1-h2024`. Er wird in den Kapiteln als `data-src` verwendet; das Quellenverzeichnis führt darüber zusammen.
- `Typ`: genau einer von `Gesetz`, `Norm`, `RFC`, `Behörde`, `Hersteller`, `Fachbuch`, `IHK-Prüfung`, `IHK-Konvention`.
- `Zitat`: so, wie es in der Quellenliste des Kapitels erscheint (Urheber, Titel, Nummer, Herausgeber, Jahr; bei Gesetzen Kurztitel und Fassung).
- `Status`: `geprüft` (WebFetch erfolgreich, Inhalt passt zum Zitat), `nicht erreichbar`, `kostenpflichtig` (Norm hinter Bezahlschranke; Zitat ohne URL zulässig), `verworfen` (mit Grund).
- `Abrufdatum`: `JJJJ-MM-TT` des erfolgreichen WebFetch (Datum per `date +%F` ermitteln).
- `Fundstellen`: Artikel, Paragraf, Abschnitt oder Seite für die Kernaussagen des Kapitels, z. B. `Art. 4 Nr. 1 (personenbezogene Daten); Art. 33 (72 Stunden)`.

Nur Quellen der Typen oben. Keine Blogs, keine Foren, keine Lernplattformen, keine Wikipedia als Beleg (Wikipedia darf zum Auffinden der Primärquelle benutzt werden). Sekundär-Lesehilfen wie `dsgvo-gesetz.de` dürfen zusätzlich verlinkt werden, wenn der amtliche Text (eur-lex, gesetze-im-internet) die Hauptquelle ist.

### 5.3 Kapitelphase (K-1 bis K-5), Vorgehen je Kapitel

1. Lesen: §2, §6 (eigene Kapitel), §7 bis §10 dieses Plans; `bau/vorlage/kapitel-vorlage.html`; den CSS-Teil von `00-kopf.html` (Klassen); `notizen/MATRIX.md`; aus allen Notizen die Teilaufgaben mit der eigenen Kapitel-id (mit Grep über `| a1` usw.); die eigenen Zeilen aus `QUELLEN-A.md` bzw. `QUELLEN-B.md`. Optional: passende Abschnitte der Lernkurse (§3.3) per Stichwortsuche.
2. Schreiben: Fragment `bau/kapitel/NN-<id>.html` nach Vorlage und §10. Reihenfolge innerhalb des Kapitels wie in der Vorlage. Vor dem Schreiben der Lösungen: Rechnungen nach §2 Regel 6 prüfen und in `notizen/RECHNUNGEN-<id>.md` protokollieren.
3. Prüfen: `node bau/pruef/check.js bau/kapitel/NN-<id>.html --fragment`. So lange korrigieren, bis „Keine Fehler.“ erscheint. Hinweise lesen und umsetzen, sofern sie zutreffen.
4. Weiter mit dem nächsten Kapitel der Phase. Am Ende: `bau/status/K<n>.done` schreiben.

### 5.4 Phase M (Matrix, Teil 1, Teil 2)

- `notizen/MATRIX.md`: Tabelle 1: Zeilen = Kapitel a1 bis b11, Spalten = H21, F22, H22, F23, H23, F24, H24, F25, H25, Zellen = Punktsumme der Teilaufgaben dieses Kapitels in dieser Prüfung (leer, wenn keine), dann `Summe`, `in n von 9`, `Ø je Prüfung`. Tabelle 2: je Kapitel die Liste der Teilaufgaben in der Form `H24 1.4 (3 P)`, chronologisch. Danach je Kapitel ein Satz: was genau immer wieder gefragt wird. Danach: Trend (was seit 2024 zunimmt, was seit 2023 nicht mehr vorkam). Alles aus den Notizen, nichts aus dem Gedächtnis.
- `02-pruefung.html` (Teil 1 „Die Prüfung“, `<section class="teil" id="pruefung">`): Prüfungsbereich, Dauer, Punkte, Gewichtung (Quelle: FIAusbV, Paragraf per WebFetch von gesetze-im-internet.de prüfen); Aufgabenstruktur über die neun Prüfungen als Tabelle aus den Deckblättern; Pflicht oder Wahl; Hilfsmittel (Wortlaut Deckblatt). Dann „Wie Punkte entstehen“: Lösungshinweise, Anzahl Aspekte gleich Punkte, Teilpunkte für Rechenweg, Folgefehler; jede dieser Aussagen mit Beleg aus einer konkreten Lösungshinweis-Datei (Kennzeichnung `IHK-Konvention`). Dann Operatoren (nennen, beschreiben, erläutern, begründen, berechnen, zeichnen, vergleichen, beurteilen, zuordnen) mit erwarteter Tiefe; Quelle: eine IHK-Operatorenliste, wenn per WebFetch auffindbar, sonst `IHK-Konvention`. Dann Antwortformat: Begriff, Erklärung, Bezug zum Szenario; Tabellenantworten; Rechenweg mit Einheiten. Dann Prüfungstag-Regeln aus `LERNPLAN.md` §7, gekennzeichnet als Konvention. Dann ein Absatz zum AKA-Prüfungskatalog: der Hinweis aus `LERNPLAN.md` §2 (geänderter Katalog ab 2025) wird per WebFetch bei IHK-AkA oder U-Form zu verifizieren versucht; Ergebnis mit Status angeben; gestrichene Themen werden in der Datei trotzdem kurz behandelt (kostet wenig, schadet nicht). Keine Kapitelstruktur mit sieben Abschnitten nötig, aber Quellenliste am Ende mit `data-src`-Einträgen wie in Kapiteln.
- `03-matrix.html` (Teil 2 „Was wie oft drankam“, `<section class="teil" id="matrix">`): die beiden Tabellen aus MATRIX.md als HTML-Tabellen (Klassen `tabelle`, `z`, `summe`), Kapitelnamen als Links zu den Kapiteln, dann die Trendsätze. Kein weiterer Text.

### 5.5 Phase V (Verfahrensblatt)

`90-verfahrensblatt.html` (Teil 3, `<section class="teil" id="verfahrensblatt">`): alle `pre.rechenweg`-Schemata und Umrechnungstabellen aus A1 bis A9, je mit Überschrift `h3` und Link zum Kapitel. Kein neuer Inhalt, keine Erklärungen, nur die Schemata. Ziel: eine Übersicht zum Ausdrucken. Wenn ein A-Kapitel kein Schema hat, wird das dort nachgetragen, nicht hier erfunden.

### 5.6 Phase Z (Zusammenbau)

1. `node bau/pruef/bauen.js` aus dem Ordner `Lernen/`. Erzeugt 91, 92 und die Datei, startet den Prüfer.
2. Fehler im betroffenen Fragment beheben, erneut bauen. Nicht die fertige Datei editieren.
3. Sichtprüfung: Wenn ein Browser-Werkzeug verfügbar ist, `file:///C:/Users/mu.aycetin/Desktop/Lernen/AP1_Lerndatei.html` bei 1440 px und bei 900 px Breite öffnen, drei Kapitel vollständig durchscrollen, eine Abbildung je Kapitelgruppe prüfen (Beschriftungen lesbar, nichts abgeschnitten), Druckvorschau öffnen. Layoutfehler im Fragment beheben. Wenn kein Browser verfügbar ist: vermerken.
4. `bau/status/Z.done`.

### 5.7 Phase F (Fachliche Gegenprüfung)

Ein Agent, der nichts geschrieben hat, prüft adversarial: je Kapitel zwei Begriffskarten und eine Original-Lösung gegen die Quelle bzw. die Lösungshinweise; alle Rechnungen aus `RECHNUNGEN-*.md` stichprobenartig neu rechnen; jede „Kam dran“-Zeile gegen MATRIX.md; jede URL-Angabe gegen QUELLEN-*.md. Befunde in `bau/notizen/PRUEFBEFUNDE.md` (Kapitel, Stelle, Befund, Korrektur). Korrekturen direkt im Fragment, neuer Zusammenbau, `bau/status/F.done`. Danach ist die Datei fertig.

## 6. Kapitelplan

20 Kapitel in fester Reihenfolge. Titel exakt wie in der Navigation von `00-kopf.html`. Zu jedem Kapitel: Lernziele („Der Leser kann …“), Pflichtbegriffe (Begriffskarten), Pflichtabbildung, Prüfungsbelege (Stand meiner Sichtung am 2026-09-02; die vollständige Liste kommt aus MATRIX.md), Startquellen (in Phase Q zu prüfen). Lernziele sind Mindestumfang. Was hier nicht steht, kommt nur hinein, wenn eine Teilaufgabe in den Notizen es verlangt.

Gruppe A: Überschrift des Kerns „Das Verfahren“, Pflicht: `pre.rechenweg`-Schema (bei A8 und A9: Zeichenschritte als Schema). Gruppe B: Überschrift des Kerns „Die Sache“.

### A1 · IPv4, Subnetting und Netzkonfiguration

Lernziele:
- IPv4-Adresse und Netzmaske als 32-Bit-Muster lesen; Präfix `/n` in Maske umrechnen und zurück; Oktett dual ↔ dezimal.
- Netzadresse, Broadcast, erste und letzte Hostadresse, Anzahl nutzbarer Hosts (2^(32−n) − 2) für `/16` bis `/30` berechnen; Subnetze eines Netzes aufzählen.
- Prüfen, ob zwei Adressen im selben Netz liegen; Adresskonflikt erkennen; eine statische Konfiguration (Adresse, Maske, Gateway, DNS) fehlerfrei ausfüllen und begründen.
- Private Bereiche (RFC 1918), APIPA 169.254.0.0/16 deuten (kein DHCP erreichbar), Loopback 127.0.0.1.
- MAC-Adresse erkennen, korrekt schreiben (6 Byte hexadezimal), von der IP-Adresse abgrenzen; Hersteller-Teil (OUI).
- IPv6: Aufbau (128 Bit, acht Blöcke hexadezimal), Kürzungsregeln, Link-Local `fe80::/10`, Global Unicast, Präfix `/64`, Gründe für IPv6.
- DHCP-Ablauf (Discover, Offer, Request, Acknowledge) in je einem Satz; Aufgabe von DNS in einem Satz.

Pflichtbegriffe: IP-Adresse, Netzmaske/Präfix (CIDR), Netzadresse, Broadcastadresse, Netzanteil/Hostanteil, Standardgateway, DHCP, DNS, APIPA, private Adresse, MAC-Adresse, Link-Local, Global Unicast.

Pflichtabbildungen: (1) 32-Bit-Balken einer Adresse mit Maske `/26`, Netz- und Hostanteil, darunter die Dezimaloktette; (2) Tabelle Präfix → Maske → Adressen → Hosts für `/24` bis `/30`; (3) Aufbau einer IPv6-Adresse mit Kürzung.

Prüfungsbelege (gesichtet): F2025 1.5 (`/26`); H2025 3.5 (`/24`, letzte Hostadresse); H2024 1.4 (169.254), 1.5 (statische Konfiguration ohne Konflikt), 1.7 (MAC). Rest aus MATRIX.md.

Startquellen: RFC 791; RFC 4632 (CIDR); RFC 1918; RFC 3927 (Link-Local IPv4); RFC 2131 (DHCP); RFC 1034/1035 (DNS); RFC 826 (ARP); RFC 8200 (IPv6); RFC 4291 (IPv6-Adressarchitektur); RFC 5952 (IPv6-Schreibweise); IEEE Registration Authority, „Guidelines for Use of EUI, OUI“ (MAC-Aufbau); Microsoft Learn: `ipconfig`.

### A2 · Kaufmännisch rechnen

Lernziele:
- Bezugspreis: Listenpreis − Rabatt − Skonto + Bezugskosten; zwei Angebote quantitativ vergleichen und qualitativ ergänzen (Lieferzeit, Garantie, Service, Zahlungsziel).
- Rabatt und Skonto unterscheiden (Skonto: Zahlungsziel, Prozentsatz, Frist); Skontobetrag und Zahlbetrag berechnen.
- Kosten über Laufzeit: einmalige plus laufende Kosten über n Jahre; monatliche Gesamtkosten; Paketpreise vergleichen; Grundidee Gesamtbetriebskosten (TCO).
- Kauf gegen Leasing rechnerisch (Leasingrate × Monate + Restwert gegen Kaufpreis) und Miete.
- Ratendarlehen mit konstanter Tilgung: Tilgung = Kredit / Laufzeit, Zins auf Restschuld, Tabelle je Periode, Gesamtzins; Abgrenzung zur Annuität in einem Satz.
- Break-even: Fixkosten / (Preis − variable Stückkosten); Deckungsbeitrag; Grafik lesen.
- Lineare Abschreibung: Anschaffungskosten / Nutzungsdauer; AfA-Tabelle (PC, Notebook); Sonderregel Computerhardware und Software (BMF 2021/2022, Nutzungsdauer ein Jahr).
- Entgangener Umsatz und Ausfallkosten (F2025 4.3); jährliche Gesamtkosten.
- Für jede Rechnung ein Schema mit Einheiten, Rundungsregel (kaufmännisch, zwei Nachkommastellen) und deutschem Zahlenformat.

Pflichtbegriffe: Listenpreis, Rabatt, Skonto, Zahlungsziel, Bezugskosten, Bezugspreis, einmalige und laufende Kosten, fixe und variable Kosten, Deckungsbeitrag, Break-even-Punkt, Leasingrate, Restwert, Tilgung, Zins, Restschuld, Abschreibung (AfA), Nutzungsdauer, Gesamtbetriebskosten (TCO).

Pflichtabbildungen: Kalkulationsschema Listenpreis → Bezugspreis als Treppe; Break-even-Grafik (Umsatz- und Kostengerade, Schnittpunkt); Ratendarlehen als Balken je Jahr (Tilgung konstant, Zins fallend).

Prüfungsbelege (gesichtet): F2025 1.2 (Monatskosten), 4.3 (Jahreskosten, entgangener Umsatz); H2024 2.6 (Kosten über fünf Jahre), 3.1 (Ratendarlehen); H2025 1.3 (Skonto, Rabatt), 2.5 (Paketpreise über Jahre).

Startquellen: BGB § 433 (Kaufvertrag), § 488 (Darlehen), §§ 535 ff. (Miete); UStG § 14 Abs. 4 Nr. 7 (Entgeltminderung auf der Rechnung); EStG § 7 (AfA); BMF, AfA-Tabelle für allgemein verwendbare Anlagegüter (2000); BMF-Schreiben vom 22.02.2022 (Nutzungsdauer Computerhardware und Software); Wöhe/Döring/Brösel, „Einführung in die Allgemeine Betriebswirtschaftslehre“ (Kalkulation, Break-even, Leasing); IHK-Lösungshinweise der genannten Prüfungen (`IHK-Konvention` für Rechenwege und Rundung).

### A3 · Nutzwertanalyse

Lernziele:
- Kriterien aufstellen (monetär und nicht-monetär trennen), gewichten (Summe 100 % oder Punkte), Erfüllungsgrad je Alternative bewerten (Skala festlegen), gewichtete Punkte, Summe, Rangfolge.
- Entscheidung begründen und Grenzen benennen (Subjektivität von Gewichtung und Bewertung, Scheingenauigkeit).
- Kombination mit Kostenvergleich (Kosten-Nutzen); Entscheidungsmatrix mit K.-o.-Kriterium.
- Sensitivität in einem Satz: was passiert, wenn eine Gewichtung sich ändert.

Pflichtbegriffe: Kriterium, Gewichtung, Erfüllungsgrad (Punktwert), Teilnutzwert, Gesamtnutzwert, K.-o.-Kriterium, monetär/nicht-monetär, Sensitivität.

Pflichtabbildungen: (1) der Ablauf in vier Schritten als Kette (Kriterien, Gewichten, Bewerten, Summieren); (2) die Gewichtung als Balken, die zusammen 100 Prozent ergeben, mit dem Teilnutzwert einer Alternative daneben, damit sichtbar wird, wie aus Gewicht mal Punktwert der Beitrag entsteht. Dazu die vollständig ausgefüllte Tabelle mit ausgeschriebenem Rechenweg in einer Zelle.

Prüfungsbelege (gesichtet): F2025 1.1. Rest aus MATRIX.md.

Startquellen: Zangemeister, Christof: „Nutzwertanalyse in der Systemtechnik“ (1970); Wöhe/Döring/Brösel; IHK-Lösungshinweise (`IHK-Konvention` für Tabellenform und Bewertungsskala).

### A4 · Einheiten, Speicher und Datenrate

Lernziele:
- Bit und Byte (Faktor 8); SI-Präfixe (k, M, G, T als Zehnerpotenzen) und Binärpräfixe (Ki, Mi, Gi, Ti als Zweierpotenzen); warum eine „1-TB-Platte“ im Betriebssystem kleiner wirkt.
- Speicherbedarf berechnen: Bild (Breite × Höhe × Farbtiefe / 8), Scan (DPI, Fläche), Text (Zeichen × Byte je Zeichen; ASCII, UTF-8), Audio (Abtastrate × Bittiefe × Kanäle × Dauer), Video grob (Bild × Bildrate × Dauer); Kompression als Angabe verwenden.
- Datenrate und Übertragungszeit: Zeit = Datenmenge / Datenrate, mit Umrechnung Byte ↔ Bit; Brutto/Netto mit angegebenem Nutzanteil; Ergebnis in sinnvolle Einheit (s, min, h) umrechnen.
- Zahlensysteme dual, dezimal, hexadezimal umrechnen (Grundlage für A1, MAC, Farbwerte).
- Rundung und Einheitenkontrolle als letzter Schritt jeder Rechnung.

Pflichtbegriffe: Bit, Byte, SI-Präfix, Binärpräfix, Farbtiefe, Auflösung, DPI, Abtastrate, Bittiefe, Datenrate (Bandbreite), Übertragungszeit, Overhead/Nutzdatenrate, Dualsystem, Hexadezimalsystem.

Pflichtabbildungen: Umrechnungsleiter Bit → Byte → KiB → MiB → GiB mit Faktoren neben der SI-Leiter; Pixelraster mit Farbtiefe; Rechenkette Datenmenge → Bit → Zeit.

Prüfungsbelege (gesichtet): H2025 2.4 (Speichergrößen). Rest aus MATRIX.md.

Startquellen: IEC 80000-13 (Binärpräfixe); BIPM, SI-Broschüre (9. Auflage); NIST SP 811 (SI-Präfixe); RFC 3629 (UTF-8); Tanenbaum/Wetherall, „Computer Networks“ (Datenrate, Übertragungszeit); IHK-Lösungshinweise (`IHK-Konvention`: ob 1 000 oder 1 024 erwartet wird, je Aufgabe belegen).

### A5 · Strom und Energiekosten

Lernziele:
- Spannung U (V), Stromstärke I (A), Leistung P (W); P = U · I; aus zwei Größen die dritte berechnen.
- Energie E = P · t in Wh und kWh; Stromkosten = P[kW] × Stunden × Tage × Preis je kWh; mehrere Geräte summieren; Betrieb und Standby getrennt rechnen.
- Einsparung berechnen und Amortisationszeit = Mehrpreis / jährliche Einsparung.
- Netzteil dimensionieren: Summe der Verbraucher plus Reserve; Wirkungsgrad = Pab / Pauf; 80-PLUS-Stufen als Angabe lesen.
- USV: Zweck, Überbrückungszeit grob aus Kapazität (Wh) / Last (W).
- Gefahren des elektrischen Stroms und Schutzmaßnahmen am Arbeitsplatz in drei Sätzen (nur so tief, wie eine Teilaufgabe es verlangt).

Pflichtbegriffe: Spannung, Stromstärke, Leistung, elektrische Arbeit/Energie, Kilowattstunde, Wirkungsgrad, Standby, Amortisationszeit, Netzteil, unterbrechungsfreie Stromversorgung (USV).

Pflichtabbildungen: Formeldreieck U, I, P; Rechenkette Watt → kWh → Euro als Ablauf.

Prüfungsbelege (gesichtet): H2025 3.4 (Spannung, Strom, Leistung). Rest aus MATRIX.md.

Startquellen: Hering/Martin/Stohrer, „Physik für Ingenieure“ oder ein Tabellenbuch Informations- und Kommunikationstechnik (Europa-Lehrmittel) für P = U · I und E = P · t; BIPM SI-Broschüre (Einheiten); Bundesnetzagentur, Monitoringbericht (Strompreis für Haushalte/Gewerbe, aktuelles Jahr); CLEAResult, 80 PLUS Programm (Wirkungsgradstufen); IEC 62040-3 (USV-Klassifikation); DGUV Information 203-xxx zu elektrischen Gefährdungen (nur wenn eine Teilaufgabe es verlangt).

### A6 · Netzplan und Gantt

Lernziele:
- Vorgangsknoten lesen und ausfüllen: Dauer, frühester Anfang und Ende (FAZ, FEZ), spätester Anfang und Ende (SAZ, SEZ), Gesamtpuffer, freier Puffer.
- Vorwärtsrechnung, Rückwärtsrechnung, kritischer Pfad, Projektdauer.
- Netzplan aus einer Vorgangsliste mit Vorgängern zeichnen (fünf bis acht Vorgänge).
- Gantt-Diagramm aus dem Netzplan ableiten und lesen; Meilenstein; Auswirkung einer Verzögerung auf Puffer und Endtermin beurteilen.

Pflichtbegriffe: Vorgang, Anordnungsbeziehung (Vorgänger/Nachfolger), FAZ, FEZ, SAZ, SEZ, Gesamtpuffer, freier Puffer, kritischer Pfad, Meilenstein, Balkenplan (Gantt).

Pflichtabbildungen: Legende eines Vorgangsknotens; ein vollständig gerechneter Netzplan mit sechs Vorgängen und markiertem kritischem Pfad (Klasse `a`); das zugehörige Gantt-Diagramm.

Prüfungsbelege (gesichtet): F2025 3.1 (Netzplan). Rest aus MATRIX.md.

Startquellen: DIN 69900:2009-01 (Netzplantechnik, Begriffe); DIN 69901-5 (Projektmanagement, Begriffe); Kuster u. a., „Handbuch Projektmanagement“ (Springer) oder Litke, „Projektmanagement“; IHK-Lösungshinweise (`IHK-Konvention`: Knotendarstellung, ob Tag 0 oder Tag 1 als Start gilt, je Aufgabe belegen).

### A7 · Programmlogik und Schreibtischtest

Lernziele:
- Pseudocode und einfache Programmtexte lesen: Zuweisung, Vergleich, Bedingung (wenn/sonst), Schleifen (solange, für, wiederhole-bis), Verschachtelung, Funktionsaufruf mit Rückgabe.
- Schreibtischtest als Tabelle: eine Spalte je Variable, eine Zeile je Durchlauf, Ausgabe festhalten; Abbruchbedingung korrekt anwenden (Zählung ab 0 oder 1 je Aufgabe).
- Arrays ein- und zweidimensional lesen (Index, Zeile/Spalte); Akkumulator (Summe, Produkt, Zähler, Maximum); Kennzahlen aus einem Programm ableiten (F2025 3.4).
- Boolesche Ausdrücke auswerten (UND, ODER, NICHT, Vergleiche), Wahrheitstabelle für zwei Eingänge.
- Logische Fehler finden und korrigieren (falscher Operator, Grenzfehler, falsche Initialisierung); Laufzeitfehler von logischem Fehler abgrenzen.
- Datentypen (ganze Zahl, Gleitkommazahl, Wahrheitswert, Zeichenkette, Zeichen) und typische Fehler (Ganzzahldivision, Rundung).
- Compiler und Interpreter unterscheiden (Übersetzung vorab gegen Ausführung zur Laufzeit, Folgen für Fehlerzeitpunkt und Portabilität); Kriterien für die Wahl einer Programmiersprache (H2024 2.2).

Pflichtbegriffe: Variable, Datentyp, Zuweisung, Bedingung, Schleife, Array, Index, Akkumulator, boolescher Ausdruck, Schreibtischtest, Pseudocode, Compiler, Interpreter, logischer Fehler, Laufzeitfehler.

Pflichtabbildungen: Schreibtischtest-Tabelle für eine Schleife mit Akkumulator (als HTML-Tabelle) plus SVG: Ablauf einer Schleife als Aktivitätsdiagramm-Ausschnitt (Bedingung, Rücksprung); Verschachtelung als eingerückte Blöcke.

Prüfungsbelege (gesichtet): F2025 3.4, 3.5; H2024 2.2, 2.3, 2.5 (zweidimensionales Array); H2025 4.3, 4.4 (Akkumulator). Rest aus MATRIX.md.

Startquellen: Python-Dokumentation, Tutorial Abschnitt „More Control Flow Tools“ (F2025 verwendete Python); Aho/Lam/Sethi/Ullman, „Compilers: Principles, Techniques, and Tools“ (Compiler/Interpreter); Java Language Specification oder Microsoft C#-Dokumentation (Datentypen); IHK-Lösungshinweise (`IHK-Konvention`: Tabellenform des Schreibtischtests).

### A8 · UML-Diagramme

Lernziele:
- Anwendungsfalldiagramm: Akteur, Anwendungsfall, Systemgrenze, Assoziation, `include`, `extend`, Generalisierung; aus einer Beschreibung vervollständigen (H2024 2.4).
- Aktivitätsdiagramm: Startknoten, Aktion, Entscheidungsknoten mit Bedingungen in eckigen Klammern, Zusammenführung, Gabelung und Synchronisation, Endknoten, Schwimmbahnen; aus einem Prozess­text zeichnen (H2025 2.2).
- Klassendiagramm: Klasse, Attribute mit Typ, Methoden, Sichtbarkeit (`+`, `−`, `#`), Assoziation mit Multiplizität; lesen und ergänzen.
- Typische Fehler: fehlende Bedingung an einer Verzweigung, kein Endknoten, Akteur innerhalb der Systemgrenze, Multiplizität vertauscht.
- Zeichenschema: in welcher Reihenfolge man ein Diagramm in der Prüfung aufbaut.

Pflichtbegriffe: Akteur, Anwendungsfall, Systemgrenze, `include`/`extend`, Aktion, Entscheidungsknoten, Bedingung (Guard), Gabelung/Synchronisation, Klasse, Attribut, Methode, Sichtbarkeit, Multiplizität, Assoziation.

Pflichtabbildungen: je Diagrammart ein kleines vollständiges Beispiel als SVG mit Symbolerklärung; alle drei im selben Stil.

Prüfungsbelege (gesichtet): H2024 2.4 (Anwendungsfall); H2025 2.2 (Aktivität). Rest aus MATRIX.md.

Startquellen: OMG, „Unified Modeling Language (UML) 2.5.1“, formal/2017-12-05 (Abschnitte zu Use Cases, Activities, Classes); Rupp/Queins, „UML 2 glasklar“ (Hanser) oder Oestereich/Scheithauer, „Analyse und Design mit der UML 2.5“.

### A9 · Datenmodell und ER-Diagramm

Lernziele:
- Entität, Attribut, Beziehung; Kardinalitäten 1:1, 1:n, n:m in Chen-Notation und in Krähenfuß- bzw. Min-Max-Notation lesen und schreiben (H2025 4.2).
- Primärschlüssel und Fremdschlüssel; Umsetzung einer Beziehung in Tabellen; n:m durch Beziehungstabelle auflösen.
- Redundanz erkennen (dieselbe Information mehrfach), Anomalien (Änderung, Einfügen, Löschen) benennen, Redundanz durch Auslagern in eigene Entität beseitigen (H2024 4.2, F2025 4.6).
- Normalisierung 1. bis 3. Normalform als Grundidee mit je einem Satz und einem Beispiel.
- SQL nur lesen: `SELECT … FROM … WHERE …` in einem Absatz (ausreichend, mehr nur wenn eine Teilaufgabe es verlangt).

Pflichtbegriffe: Entität, Attribut, Beziehung, Kardinalität, Primärschlüssel, Fremdschlüssel, Redundanz, Anomalie, Normalform, Beziehungstabelle, Chen-Notation, Krähenfußnotation.

Pflichtabbildungen: ein ER-Modell mit drei Entitäten in Chen-Notation und dieselbe Sache als Tabellen mit Pfeilen Fremdschlüssel → Primärschlüssel; Krähenfuß-Symbole neben Chen-Symbolen.

Prüfungsbelege (gesichtet): H2024 4.2; H2025 4.1, 4.2; F2025 4.6 (Redundanz). Rest aus MATRIX.md.

Startquellen: Chen, P. P.-S.: „The Entity-Relationship Model – Toward a Unified View of Data“, ACM Transactions on Database Systems 1 (1976); Codd, E. F.: „A Relational Model of Data for Large Shared Data Banks“, Communications of the ACM 13 (1970); Kemper/Eickler, „Datenbanksysteme. Eine Einführung“ (De Gruyter Oldenbourg); ISO/IEC 9075 (SQL, nur nennen, kostenpflichtig).

### B1 · IT-Sicherheit I: Schutzziele, Zugang, Angriffe

Lernziele:
- Schutzziele Vertraulichkeit, Integrität, Verfügbarkeit (dazu Authentizität, Nichtabstreitbarkeit) definieren, an Beispielen erkennen, Maßnahmen zuordnen.
- Authentifizierungsfaktoren Wissen, Besitz, Biometrie; Zwei- und Mehrfaktor-Authentifizierung; Authentifizierung gegen Autorisierung.
- Least Privilege und Umgang mit Administratorrechten (F2025 1.7); Rollen und Berechtigungen.
- Passwortregeln nach BSI (Länge vor Komplexität, kein erzwungener regelmäßiger Wechsel, Passwortmanager); sichere Speicherung wird in B2 behandelt (Querverweis).
- Updates und Patch-Management; sichere Lieferkette (signierte Updates, vertrauenswürdige Quellen, Geräte mit Herstellersupport) (H2025 3.3).
- Härtung: Minimalkonfiguration, nicht benötigte Dienste abschalten, Netztrennung und Segmentierung, Gast-WLAN (H2024 1.3).
- Zutritts-, Zugangs- und Zugriffskontrolle unterscheiden; automatische Zutrittskontrolle (H2024 1.1).
- Sicherheitsrisiko als Ursache-Wirkungs-Kette formulieren (H2024 1.2).
- Malware-Arten (Virus, Wurm, Trojaner, Ransomware, Spyware) und Social Engineering; Phishing: Anzeichen einer Phishing-Mail, Gefahren, Maßnahmen auf Unternehmensebene (technisch und organisatorisch), Verhaltensregeln für Mitarbeitende (H2024 3.5 bis 3.8).
- Sicherheitsmaßnahmen aus einem englischen Fachtext entnehmen und auf Deutsch wiedergeben (F2025 1.6): Vorgehen in drei Schritten.

Pflichtbegriffe: Vertraulichkeit, Integrität, Verfügbarkeit, Authentizität, Authentifizierung, Autorisierung, Authentifizierungsfaktor, Zwei-Faktor-Authentifizierung, Least Privilege, Berechtigung/Rolle, Patch, Härtung, Segmentierung, Zutritt/Zugang/Zugriff, Malware, Ransomware, Phishing, Social Engineering.

Pflichtabbildungen: Schutzziel-Dreieck mit je zwei Maßnahmen; drei Türen für Zutritt, Zugang, Zugriff; eine schematische Phishing-Mail als SVG mit fünf markierten Anzeichen.

Prüfungsbelege (gesichtet): F2025 1.6, 1.7, 2.2; H2024 1.1 bis 1.3, 3.5 bis 3.8; H2025 3.2, 3.3. Rest aus MATRIX.md.

Startquellen: BSI, IT-Grundschutz-Kompendium (aktuelle Edition), Glossar und Bausteine ORP.4 (Identitäts- und Berechtigungsmanagement), SYS.2.1 (Allgemeiner Client), NET.1.1 (Netzarchitektur); BSI-Standard 200-2; BSI, „Sichere Passwörter erstellen“ (bsi.bund.de); NIST SP 800-63B (Authentifizierungsfaktoren); Saltzer/Schroeder, „The Protection of Information in Computer Systems“ (1975, Least Privilege); BSI, „Die Lage der IT-Sicherheit in Deutschland“ (aktueller Bericht, Phishing/Ransomware); Verordnung (EU) 2024/2847 (Cyber Resilience Act, Updates und Lieferkette); ENISA Threat Landscape (aktuell).

### B2 · IT-Sicherheit II: Kryptografie und sichere Verbindungen

Lernziele:
- Symmetrische Verschlüsselung (ein Schlüssel, schnell, Schlüsselverteilung als Problem; AES), asymmetrische Verschlüsselung (öffentlicher und privater Schlüssel; RSA, elliptische Kurven; langsam), hybrides Verfahren (Schlüsselaustausch asymmetrisch, Daten symmetrisch); je Vor- und Nachteile (F2025 2.3, 2.4).
- Hashfunktion: Einwegfunktion, feste Länge, kollisionsresistent; SHA-256; Integritätsprüfung von Downloads; Passwortspeicherung mit Salt (F2025 2.6).
- Digitale Signatur: Hash mit privatem Schlüssel signieren, mit öffentlichem prüfen; Signatur (Authentizität, Integrität, Nichtabstreitbarkeit) gegen Verschlüsselung (Vertraulichkeit) abgrenzen (H2025 3.7); qualifizierte elektronische Signatur nach eIDAS in einem Satz.
- Zertifikat, Zertifizierungsstelle, Public-Key-Infrastruktur; was das Schloss im Browser bedeutet; TLS/HTTPS grob.
- VPN: Tunnel, Standort-zu-Standort gegen Fernzugriff, Zweck.
- SSH gegen Telnet; Schlüsselpaar-Anmeldung; Port 22; einen Cloud-Server sicher administrieren (F2025 4.5).
- WLAN-Sicherheit: WPA2, WPA3; Pre-Shared Key gegen Enterprise (RADIUS, 802.1X); Anmeldung an WPA-Personal (F2022 3a, 3b).
- E-Mail: Transportverschlüsselung gegen Ende-zu-Ende (S/MIME, PGP) in einem Absatz.

Pflichtbegriffe: symmetrische Verschlüsselung, asymmetrische Verschlüsselung, öffentlicher Schlüssel, privater Schlüssel, hybrides Verfahren, Hashwert, Kollision, Salt, digitale Signatur, Zertifikat, Zertifizierungsstelle (CA), PKI, TLS/HTTPS, VPN, SSH, WPA2/WPA3, Pre-Shared Key, RADIUS.

Pflichtabbildungen: Schlüsselfluss symmetrisch gegen asymmetrisch (zwei Personen, Schlüsselsymbole); Signaturablauf (Dokument → Hash → signieren → übertragen → prüfen); TLS-Verbindungsaufbau in vier Schritten.

Prüfungsbelege (gesichtet): F2025 2.3, 2.4, 2.6, 4.5; H2025 3.7; F2022 3a, 3b. Rest aus MATRIX.md.

Startquellen: BSI TR-02102-1, „Kryptographische Verfahren: Empfehlungen und Schlüssellängen“ (aktuelle Fassung); NIST FIPS 197 (AES); NIST FIPS 180-4 (SHA); NIST FIPS 186-5 (Digitale Signaturen); RFC 8017 (RSA PKCS #1); RFC 5280 (X.509-Zertifikate); RFC 8446 (TLS 1.3); RFC 4251 (SSH-Architektur); RFC 4301 (IPsec); Verordnung (EU) Nr. 910/2014 (eIDAS); Wi-Fi Alliance, WPA3 Specification; RFC 2865 (RADIUS); IEEE 802.1X.

### B3 · Datenschutz: DSGVO und BDSG

Lernziele:
- Personenbezogene Daten (Art. 4 Nr. 1) mit Beispielen; besondere Kategorien (Art. 9: Gesundheit, Religion, …) und warum sie erhöhten Schutz brauchen (H2025 3.1); Pseudonymisierung und Anonymisierung unterscheiden (Art. 4 Nr. 5).
- Grundsätze (Art. 5): Rechtmäßigkeit, Zweckbindung, Datenminimierung, Richtigkeit, Speicherbegrenzung, Integrität und Vertraulichkeit, Rechenschaftspflicht; je ein Beispiel aus dem IT-Alltag.
- Rechtsgrundlagen (Art. 6): Einwilligung, Vertrag, rechtliche Verpflichtung, berechtigtes Interesse; Anforderungen an eine Einwilligung (Art. 7).
- Betroffenenrechte (Art. 12 bis 22): Information, Auskunft, Berichtigung, Löschung, Einschränkung, Übertragbarkeit, Widerspruch; Frist einen Monat (Art. 12 Abs. 3).
- Verantwortlicher gegen Auftragsverarbeiter (Art. 4 Nr. 7, 8; Art. 28, Vertrag zur Auftragsverarbeitung) mit IT-Systemhaus-Beispiel; technische und organisatorische Maßnahmen (Art. 32) mit je drei Beispielen; Datenschutz durch Technikgestaltung und Voreinstellungen (Art. 25).
- Datenschutzbeauftragter (Art. 37; BDSG § 38: ab 20 ständig mit automatisierter Verarbeitung beschäftigten Personen); Meldung von Verletzungen binnen 72 Stunden (Art. 33), Benachrichtigung Betroffener (Art. 34); Bußgeldrahmen (Art. 83).
- Datenschutz gegen Datensicherheit abgrenzen; Datenschutz bei KI-Diensten und Drittlandübermittlung in einem Absatz (Querverweis B10).

Pflichtbegriffe: personenbezogene Daten, besondere Kategorien, Verarbeitung, Verantwortlicher, Auftragsverarbeiter, Einwilligung, Zweckbindung, Datenminimierung, Betroffenenrechte, technische und organisatorische Maßnahmen (TOM), Datenschutzbeauftragter, Datenschutzverletzung (Meldepflicht), Anonymisierung, Pseudonymisierung, Datenschutz gegen Datensicherheit.

Pflichtabbildungen: Rollenbild Betroffener, Verantwortlicher, Auftragsverarbeiter, Aufsichtsbehörde mit Pfeilen (Vertrag, Auskunft, Meldung); die sieben Grundsätze als Reihe.

Prüfungsbelege (gesichtet): F2025 2.1; H2025 3.1. Rest aus MATRIX.md.

Startquellen: Verordnung (EU) 2016/679 (DSGVO), amtlicher Text auf EUR-Lex; BDSG § 38 (gesetze-im-internet.de); BfDI, Informationsmaterial zu Betroffenenrechten; Datenschutzkonferenz (DSK), Kurzpapiere (Auftragsverarbeitung, TOM); Lesehilfe: dsgvo-gesetz.de (nur zusätzlich).

### B4 · Hardware und Anschlüsse

Lernziele:
- Komponenten und Auswahlkriterien: Prozessor (Kerne, Threads, Takt, Cache, Leistungsaufnahme), Arbeitsspeicher (DDR4/DDR5, Takt, Kapazität, Dual Channel, DIMM gegen SO-DIMM, Kompatibilität zu Mainboard und CPU; H2024 3.2, 3.3), Massenspeicher (HDD gegen SSD; SATA gegen NVMe/M.2; Kennwerte Durchsatz, Zugriffszeit, Preis je GB, Lebensdauer; H2024 3.4, F2022 2d), Mainboard (Sockel, Chipsatz, Steckplätze), Netzteil, Grafikkarte und ihre Anschlüsse (F2022 2e).
- Einbau und Pflege: CPU einsetzen (Sockel, Markierung, Hebel), Wärmeleitpaste (Zweck, Menge), Kühlung (F2022 2a, 2b).
- Kennzahlen aus dem Task-Manager deuten (F2022 2g).
- Anschlüsse und Symbole erkennen: USB-A, USB-B, USB-C (Stecker) gegen USB-Versionen (Datenraten: USB 2.0 480 Mbit/s, USB 3.2 Gen 1 5 Gbit/s, Gen 2 10 Gbit/s, Gen 2x2 20 Gbit/s, USB4 40 Gbit/s); HDMI, DisplayPort, Thunderbolt, RJ45, Klinke; Funk-Symbole WLAN und Bluetooth (F2025 1.3, 1.4; F2022 2f).
- Monitor (Auflösung, Bildwiederholrate, Paneltyp), Peripherie (Drucker Laser gegen Tinte, Scanner), Beamer-Anschluss; Gerätearten (Desktop, Notebook, Thin Client, Tablet, Docking-Station) und Einsatz.
- BIOS/UEFI, Treiber, Firmware in je zwei Sätzen.

Pflichtbegriffe: CPU (Kern, Thread, Takt), RAM (DDR, Dual Channel, DIMM), SSD, HDD, NVMe, M.2, SATA, Mainboard (Sockel, Chipsatz), Netzteil, Grafikkarte, USB (Steckertyp gegen Version), HDMI, DisplayPort, Thunderbolt, RJ45, Thin Client, Docking-Station, BIOS/UEFI, Treiber, Firmware.

Pflichtabbildungen: Anschluss-Silhouetten (USB-A, USB-C, HDMI, DisplayPort, RJ45, Klinke) schematisch als SVG mit Beschriftung; Tabelle SSD gegen HDD; Checkliste RAM-Kompatibilität als Tabelle. Die vorhandenen SVGs im `assets/`-Ordner (§3.3) dürfen als Vorlage angesehen werden.

Prüfungsbelege (gesichtet): F2025 1.3, 1.4; H2024 3.2 bis 3.4; F2022 2a bis 2g. Rest aus MATRIX.md.

Startquellen: USB Implementers Forum, USB-Spezifikationen und Namensschema (usb.org); JEDEC JESD79-4 (DDR4) und JESD79-5 (DDR5); HDMI Licensing Administrator (hdmi.org); VESA DisplayPort (vesa.org); Intel, Thunderbolt-Technologieübersicht; NVM Express Base Specification (nvmexpress.org); SATA-IO; Intel ARK und AMD Produktseiten (Beispiel-CPUs); Microsoft Learn, Task-Manager; Noctua oder Arctic, FAQ Wärmeleitpaste (Hersteller); Tanenbaum/Austin, „Structured Computer Organization“ (Fachbuch).

### B5 · Netzwerk-Grundlagen

Lernziele:
- OSI-Modell: sieben Schichten mit Aufgabe, Beispielprotokollen, Geräten und Adressart je Schicht; TCP/IP-Modell daneben; Fehlersuche schichtweise (F2022 3c, 3d).
- Geräte: Switch, Router, Access Point, Firewall, Modem; welche Schicht, welche Aufgabe.
- TCP gegen UDP (Verbindung, Zuverlässigkeit, Einsatz); Ports und die wichtigsten Portnummern (HTTP 80, HTTPS 443, DNS 53, DHCP 67/68, SMTP 25/587, IMAP 143/993, POP3 110/995, SSH 22, RDP 3389, FTP 21, SMB 445).
- DHCP (Ablauf, Lease), DNS (Auflösung, Rekursion in einem Satz), ARP (IP zu MAC).
- E-Mail: IMAP gegen POP3 gegen SMTP, wer holt, wer schickt, wo liegen die Mails (F2025 2.7).
- Verkabelung: Kategorien Cat 5e, 6, 6A, 7 und Datenraten; Netzwerkdose, Patchfeld, Patchkabel, Switch; Glasfaser gegen Kupfer; PoE (H2025 3.6); den richtigen Switch-Port systematisch finden (H2024 1.6).
- WLAN: Standards Wi-Fi 5/6/6E/7, Frequenzbänder 2,4 GHz gegen 5 GHz (Reichweite gegen Durchsatz), SSID, Kanäle; Bluetooth-Einsatz (F2025 1.4).
- Diagnosebefehle `ping`, `ipconfig`, `tracert`, `nslookup`: was sie zeigen.
- VLAN Grundidee; Client-Server gegen Peer-to-Peer; Cloud-Dienstmodelle IaaS, PaaS, SaaS und Bereitstellungsmodelle Public, Private, Hybrid; Virtualisierung: Hypervisor Typ 1 gegen Typ 2, virtuelle Maschine gegen Container.

Pflichtbegriffe: OSI-Schicht, Protokoll, Port, TCP, UDP, Switch, Router, Access Point, Firewall, DHCP, DNS, ARP, IMAP/POP3/SMTP, Patchfeld, Kategorie (Cat), PoE, SSID, Frequenzband, VLAN, IaaS/PaaS/SaaS, Hypervisor, Container.

Pflichtabbildungen: OSI-Stapel mit Beispielen je Schicht; Weg eines Pakets Client → Switch → Router → Internet mit Adressen je Station; Verkabelung Arbeitsplatzdose → Patchfeld → Switch; Cloud-Verantwortung als Treppe (wer betreibt was bei IaaS, PaaS, SaaS).

Prüfungsbelege (gesichtet): F2025 1.4, 2.7; H2024 1.6; H2025 3.6; F2022 3c, 3d. Rest aus MATRIX.md.

Startquellen: ITU-T X.200 (OSI-Referenzmodell); RFC 9293 (TCP); RFC 768 (UDP); IANA, Service Name and Transport Protocol Port Number Registry; RFC 2131 (DHCP); RFC 1035 (DNS); RFC 826 (ARP); RFC 5321 (SMTP); RFC 9051 (IMAP4rev2); RFC 1939 (POP3); ISO/IEC 11801 bzw. DIN EN 50173 (strukturierte Verkabelung, kostenpflichtig); IEEE 802.3 (Ethernet, PoE-Klauseln), IEEE 802.11 (WLAN), IEEE 802.1Q (VLAN); Wi-Fi Alliance, Generationen-Bezeichnungen; NIST SP 800-145 (Cloud-Definition); Popek/Goldberg, „Formal Requirements for Virtualizable Third Generation Architectures“ (1974); Microsoft Learn, Hyper-V-Übersicht; Tanenbaum/Wetherall, „Computer Networks“; Microsoft Learn: `ping`, `tracert`, `nslookup`.

### B6 · Software, Lizenzen und Web

Lernziele:
- Softwarearten: System- gegen Anwendungssoftware, Firmware, Treiber; Standard- gegen Individual- gegen Branchensoftware mit Vor- und Nachteilen; Eigenentwicklung gegen Fremdvergabe mit Argumenten (H2024 2.1); Programmiersprache nach einem Kriterium wählen (H2024 2.2, Querverweis A7).
- Aufgaben eines Betriebssystems (Prozess-, Speicher-, Geräte-, Datei-, Benutzerverwaltung); Prozess gegen Thread in zwei Sätzen.
- Dateisysteme NTFS, FAT32, exFAT, ext4, APFS: Grenzen, Rechte, Einsatz; Partitionierung.
- Lizenzmodelle: proprietär gegen Open Source (Open-Source-Definition; GPL mit Copyleft gegen MIT permissiv), Freeware, Shareware, EULA, OEM, Volumenlizenz, benannter gegen gleichzeitiger Nutzer, Abonnement/SaaS; Vor- und Nachteile von Open Source für ein Unternehmen (F2025 2.5); Lizenzverstöße und Audit.
- Web: statische gegen dynamische Website (F2025 3.2); Rollen von HTML, CSS, JavaScript, Backend, Datenbank, Webserver (F2025 3.3); Ablauf einer Anfrage; Content-Management-System.
- ERP, CRM, DMS: was, wofür, je ein Beispiel.
- Software auswählen (Kriterien), einführen (Rollout, Schulung, Querverweis B10), aktualisieren.

Pflichtbegriffe: Systemsoftware, Anwendungssoftware, Firmware, Treiber, Standardsoftware, Individualsoftware, Branchensoftware, Betriebssystem, Prozess/Thread, Dateisystem, Partition, Lizenz, Open Source, Copyleft, EULA, OEM, Volumenlizenz, SaaS, statische/dynamische Website, Frontend/Backend, CMS, ERP, CRM, DMS.

Pflichtabbildungen: Anfrage statisch gegen dynamisch (Browser → Webserver → Anwendung → Datenbank); Lizenz-Landkarte als Matrix (Quellcode offen/geschlossen gegen kostenlos/kostenpflichtig) mit Beispielen.

Prüfungsbelege (gesichtet): F2025 2.5, 3.2, 3.3; H2024 2.1, 2.2. Rest aus MATRIX.md.

Startquellen: Open Source Initiative, „The Open Source Definition“; Free Software Foundation, GNU GPL v3 (Text); MIT License (opensource.org); UrhG §§ 69a bis 69g (Computerprogramme); MDN Web Docs (HTTP, HTML, CSS, JavaScript, „Dynamic websites“); Microsoft Learn: NTFS, FAT32, exFAT, Volumenlizenzierung; Linux-Kernel-Dokumentation ext4; Apple, „Apple File System Reference“; Tanenbaum/Bos, „Modern Operating Systems“; Gronau, „Enterprise Resource Planning“ (Fachbuch).

### B7 · Datensicherung und Verfügbarkeit

Lernziele:
- Sicherungsarten Vollsicherung, differenziell, inkrementell: Ablauf über eine Woche, Speicherbedarf und Wiederherstellungsaufwand berechnen und vergleichen (Rechenschema).
- Generationenprinzip (Großvater, Vater, Sohn), 3-2-1-Regel, Offline- und Offsite-Kopie, unveränderliche Sicherung gegen Ransomware, Wiederherstellungstest, Aufbewahrung der Medien; RPO und RTO als Grundidee.
- Aufbewahrungsfristen für Geschäftsunterlagen (HGB § 257, AO § 147; aktuelle Fristen prüfen, Änderung durch Bürokratieentlastungsgesetz 2024 beachten).
- RAID 0, 1, 5, 10: Prinzip, Nutzkapazität, Ausfalltoleranz; RAID ist kein Backup; Hot Spare in einem Satz.
- USV: Zweck, Typen (Offline, Line-Interactive, Online) grob; Verfügbarkeit in Prozent und Ausfallzeit je Jahr; MTBF in einem Satz.
- Datenträger sicher löschen und vernichten (Überschreiben, DIN 66399) in einem Absatz.

Pflichtbegriffe: Vollsicherung, differenzielle Sicherung, inkrementelle Sicherung, Generationenprinzip, 3-2-1-Regel, Wiederherstellung, RPO, RTO, RAID-Level, Nutzkapazität, Hot Spare, USV, Verfügbarkeit, MTBF, Aufbewahrungsfrist.

Pflichtabbildungen: Zeitstrahl Montag bis Sonntag mit Blöcken für Voll/Diff/Inkr und der Wiederherstellungskette am Donnerstag; RAID-1- und RAID-5-Plattenschema mit Nutzkapazität.

Prüfungsbelege: aus MATRIX.md (erwartet in 2021 bis 2023).

Startquellen: BSI IT-Grundschutz-Kompendium, Baustein CON.3 (Datensicherungskonzept); Krogh, „The DAM Book“ (Ursprung der 3-2-1-Regel); Patterson/Gibson/Katz, „A Case for Redundant Arrays of Inexpensive Disks (RAID)“ (1988); IEC 62040-3 (USV); HGB § 257 und AO § 147 (aktuelle Fassung, gesetze-im-internet.de); DIN 66399 (Vernichtung von Datenträgern, kostenpflichtig, nur nennen); IEC 60050-192 (Zuverlässigkeitsbegriffe).

### B8 · Arbeitsplatz: Ergonomie, Barrierefreiheit, Nachhaltigkeit

Lernziele:
- Bildschirmarbeitsplatz nach ArbStättV Anhang Nr. 6: Bildschirm (Höhe, Abstand, entspiegelt, Blickrichtung parallel zum Fenster), Tastatur und Maus, Stuhl, Tisch, Beleuchtung (Richtwert 500 lx nach DIN EN 12464-1), Lärm, Raumklima, Tätigkeitswechsel und Pausen, Unterweisung; Telearbeit und Homeoffice: Pflichten des Arbeitgebers.
- Softwareergonomie: Grundsätze der Dialoggestaltung (DIN EN ISO 9241-110) mit je einem Beispiel.
- Barrierefreiheit: vier Prinzipien der WCAG (wahrnehmbar, bedienbar, verständlich, robust), konkrete Maßnahmen (Kontrastverhältnis 4,5:1, Alternativtexte, Tastaturbedienung, Screenreader-Kompatibilität, Untertitel, skalierbare Schrift), Hilfsmittel am Arbeitsplatz; Rechtsrahmen BGG, BITV 2.0, BFSG (gilt seit 28.06.2025), EN 301 549.
- Nachhaltigkeit und Green IT: Energieeffizienz (Labels Blauer Engel, ENERGY STAR, TCO Certified, EPEAT), Lebensdauer verlängern, Refurbished, Reparierbarkeit, Entsorgung und Rücknahme (ElektroG), Ökodesign; ökologische Aspekte einer Neuinvestition (H2024 4.5); Nachhaltigkeit ökonomisch, ökologisch, sozial.

Pflichtbegriffe: Bildschirmarbeitsplatz, Ergonomie, Softwareergonomie, Blendung/Reflexion, Beleuchtungsstärke (Lux), Barrierefreiheit, WCAG, Screenreader, Alternativtext, Kontrastverhältnis, BFSG, Green IT, Energieeffizienzlabel, Lebenszyklus, Refurbished, ElektroG.

Pflichtabbildungen: Arbeitsplatz in Seitenansicht mit Maßen (Bildschirmoberkante, Abstand, Winkel) als SVG; vier WCAG-Prinzipien mit je einer Maßnahme.

Prüfungsbelege (gesichtet): H2024 4.5 (ökologische Aspekte). Rest aus MATRIX.md (Ergonomie und Barrierefreiheit werden erwartet).

Startquellen: Arbeitsstättenverordnung, Anhang Nr. 6 (gesetze-im-internet.de); Arbeitsschutzgesetz; DGUV Information 215-410, „Bildschirm- und Büroarbeitsplätze“; DIN EN ISO 9241-110 und 9241-303 (kostenpflichtig, nur nennen); DIN EN 12464-1 (Beleuchtung, kostenpflichtig, Richtwert per DGUV belegen); W3C, WCAG 2.2; BITV 2.0; BGG; BFSG; ETSI EN 301 549; ElektroG; Blauer Engel (Umweltbundesamt/RAL), ENERGY STAR, TCO Certified, EPEAT (Herstellerkonsortien); Verordnung (EU) 2024/1781 (Ökodesign); Umweltbundesamt, Green IT.

### B9 · Projekt, Anforderungen und Vorgehen

Lernziele:
- Projektmerkmale (DIN 69901), magisches Dreieck (Zeit, Kosten, Qualität/Umfang), Projektphasen, Meilenstein, Stakeholder, Risiko.
- Anforderungen ermitteln: Interview, Beobachtung, Fragebogen; funktionale gegen nicht-funktionale Anforderungen; Muss-, Soll-, Kann-Kriterien; Zielgruppe und Nutzungsprofil; Kundenbedarf zielgruppengerecht klären; welche Informationen ein Angebot braucht (F2022 1c).
- Lastenheft (Auftraggeber: was und wofür) gegen Pflichtenheft (Auftragnehmer: wie und womit), Inhalte je Heft, Reihenfolge (H2024 4.1).
- SMART-Ziele mit Beispiel; Kick-off (Inhalte, Teilnehmer).
- Vorgehensmodelle: Wasserfall, V-Modell, Scrum (Rollen, Artefakte, Ereignisse, Sprint), Kanban (Board, WIP-Limit); Vor- und Nachteile, Auswahl nach Situation.
- Teamphasen nach Tuckman mit je einem Merkmal.
- Dokumentation (System-, Benutzer-, Projektdokumentation), Übergabe und Abnahme; Qualitätssicherung als Grundidee (PDCA, Testarten: Blackbox, Whitebox, Unit-, Integrations-, System-, Abnahmetest in je einem Satz).

Pflichtbegriffe: Projekt, magisches Dreieck, Lastenheft, Pflichtenheft, funktionale Anforderung, nicht-funktionale Anforderung, Muss-/Soll-/Kann-Kriterium, SMART, Stakeholder, Meilenstein, Wasserfallmodell, V-Modell, Scrum (Product Owner, Scrum Master, Entwicklungsteam, Product Backlog, Sprint, Review, Retrospektive), Kanban, Teamphasen, Kick-off, Abnahme, PDCA.

Pflichtabbildungen: Lastenheft → Pflichtenheft als zwei Spalten (wer, was, wann); Scrum-Zyklus; Tuckman-Kurve.

Prüfungsbelege (gesichtet): H2024 4.1; F2022 1c. Rest aus MATRIX.md.

Startquellen: DIN 69901-5 (Projektmanagement, Begriffe); VDI 2519 Blatt 1 (Lastenheft/Pflichtenheft); Schwaber/Sutherland, „The Scrum Guide“ (2020, scrumguides.org); Doran, „There's a S.M.A.R.T. way to write management's goals and objectives“, Management Review (1981); Tuckman, „Developmental sequence in small groups“, Psychological Bulletin (1965); Royce, „Managing the development of large software systems“ (1970); V-Modell XT (Bund); Anderson, „Kanban“ (2010); ISO 9001 (PDCA, kostenpflichtig, nur nennen); ISTQB, Glossar (Testarten).

### B10 · Kunde, Kommunikation und Veränderung

Lernziele:
- Kundengespräch strukturieren: Bedarf klären, offene gegen geschlossene Fragen, aktives Zuhören, Zusammenfassen, zielgruppengerecht erklären (Laie gegen Fachkraft).
- Vier-Seiten-Modell (Schulz von Thun) an einem Satz aus dem IT-Alltag anwenden; Sender-Empfänger-Modell und Störungen; Feedbackregeln.
- Unternehmensdarstellung und Leistungsangebot überzeugend erläutern; Aufbau einer Präsentationsfolie (F2022 1a, 1b).
- Schulung, Einweisung, Key-User-Konzept, Übergabe; Dokumentation für Anwender.
- Veränderungsmanagement: warum Menschen neue Prozesse ablehnen (Gewohnheit, Angst vor Kontroll- oder Arbeitsplatzverlust, fehlende Information, Mehraufwand, fehlende Beteiligung) (H2025 1.5); Gegenmaßnahmen (informieren, beteiligen, schulen, Pilotphase, Vorbild, Nutzen zeigen); Lewin drei Phasen, Kotter acht Stufen kurz; Vorteile einer Neuerung für Beschäftigte argumentieren (F2025 4.2).
- KI im Betrieb: sinnvolle Einsatzstelle in einem Prozess finden und begründen (F2025 4.1, H2025 2.3); Chancen und Risiken; Chatbot Vor- und Nachteil (F2025 4.4); Grenzen (Halluzination, Datenschutz, Haftung, Nachvollziehbarkeit); KI-Verordnung der EU in einem Absatz (Querverweis B3).
- Serviceanfragen: Störungsannahme, Ticket, Priorisierung, Support-Level 1 bis 3, Service-Level-Vereinbarung in je einem Satz.

Pflichtbegriffe: aktives Zuhören, offene/geschlossene Frage, Vier-Seiten-Modell (Sach-, Selbstoffenbarungs-, Beziehungs-, Appellseite), Feedback, Zielgruppe, Key-User, Einweisung/Schulung, Widerstand gegen Veränderung, Veränderungsmanagement, Pilotphase, Chatbot, generative KI, Halluzination, Support-Level, Ticket, SLA.

Pflichtabbildungen: Vier-Seiten-Modell als Quadrat mit Beispielsatz; Lewin-Phasen; ein Geschäftsprozess als Ablauf mit markierter KI-Einsatzstelle.

Prüfungsbelege (gesichtet): F2025 4.1, 4.2, 4.4; H2025 1.5, 2.1, 2.3; F2022 1a bis 1c. Rest aus MATRIX.md.

Startquellen: Schulz von Thun, „Miteinander reden 1“ (1981); Shannon/Weaver, „The Mathematical Theory of Communication“ (1949); Rogers/Farson, „Active Listening“ (1957); Lewin, „Frontiers in Group Dynamics“ (1947); Kotter, „Leading Change“ (1996); Verordnung (EU) 2024/1689 (KI-Verordnung); BSI, „Generative KI-Modelle – Chancen und Risiken für Industrie und Behörden“; DSGVO Art. 22; Axelos/PeopleCert, ITIL 4 Foundation (Support-Level, SLA; Fachbuch).

### B11 · Wirtschaft und Recht

Lernziele:
- Vertragsarten Kauf-, Werk-, Dienstvertrag mit IT-Beispielen (Hardwarekauf, Individualsoftware, Wartung); Vertragsschluss (Angebot, Annahme, „freibleibend“); zweiseitiger Handelskauf.
- Gewährleistung (gesetzlich, zwei Jahre, Beweislastumkehr zwölf Monate bei Verbrauchern) gegen Garantie (freiwillig, Hersteller); Sachmangel; Rechte bei Mängeln (Nacherfüllung, Rücktritt, Minderung, Schadensersatz); Mängelrüge im Handelskauf (HGB § 377, unverzüglich); Lieferverzug und Zahlungsverzug (30 Tage nach Rechnung, BGB § 286 Abs. 3).
- Rechnung: Pflichtangaben (UStG § 14), Rechnungsdatum, Lieferdatum, Fälligkeit, Zahlungsziel, Skontofrist auf einem Zeitstrahl (H2025 1.1); Rechnungspositionen prüfen (H2025 1.2); E-Rechnung im B2B (Pflicht ab 2025, XRechnung, ZUGFeRD); GiroCode/QR-Zahlung (EPC-QR) (H2025 1.4); Aufbewahrungsfristen (Querverweis B7).
- Digitalisierung eines Rechnungsprozesses: Nutzen und Risiko (H2025 2.1).
- Beschaffung: Kauf, Leasing, Miete qualitativ (Liquidität, Eigentum, Bilanz, Flexibilität, Wartung), Vorteile von Leasing (H2024 4.3), Möglichkeiten nach Ablauf der Leasingdauer (Rückgabe, Verlängerung, Kauf zum Restwert, Neuleasing) (H2024 4.4); Make-or-Buy.
- Unternehmen: Unternehmensziele (ökonomisch, ökologisch, sozial), Marktformen kurz, Rechtsformen kurz (e. K., GbR, GmbH, UG, AG), Vollmachten (Prokura, Handlungsvollmacht) kurz, Aufbauorganisation (Organigramm, Linie, Stab) kurz.

Pflichtbegriffe: Kaufvertrag, Werkvertrag, Dienstvertrag, Angebot/Annahme, Gewährleistung, Garantie, Sachmangel, Nacherfüllung, Mängelrüge, Verzug, Rechnung (Pflichtangaben), Fälligkeit, Zahlungsziel, E-Rechnung, GiroCode, Leasing, Miete, Restwert, Make-or-Buy, Liquidität, Rechtsform, Prokura, Handlungsvollmacht, Organigramm.

Pflichtabbildungen: Rechnung als annotiertes Schema mit markierten Pflichtangaben; Zeitstrahl Rechnungsdatum → Skontofrist → Zahlungsziel → Verzug.

Prüfungsbelege (gesichtet): H2025 1.1 bis 1.4, 2.1; H2024 4.3, 4.4. Rest aus MATRIX.md.

Startquellen: BGB §§ 145 ff. (Vertragsschluss), 433, 434, 437, 438, 439, 443, 286, 611, 631; HGB §§ 48 bis 58 (Prokura, Handlungsvollmacht), 257, 377; UStG § 14 (Rechnung, E-Rechnung); AO § 147; BMF-Schreiben vom 15.10.2024 (E-Rechnung); European Payments Council, „Quick Response Code: Guidelines to Enable Data Capture for the Initiation of a SEPA Credit Transfer“ (EPC069-12); Deutsche Kreditwirtschaft, GiroCode; GmbHG, AktG; Wöhe/Döring/Brösel; IHK-Lösungshinweise (`IHK-Konvention` für Leasing-Argumente).

## 7. Quellenregeln

1. Zulässige Typen: `Gesetz`, `Norm`, `RFC`, `Behörde`, `Hersteller`, `Fachbuch`, `IHK-Prüfung`, `IHK-Konvention`. Sonst nichts.
2. Harte gegen weiche Aussagen trennen. Gesetz, Norm, RFC sind hart. Was die IHK in Lösungshinweisen erwartet, ist Konvention und wird so gekennzeichnet. Wo beides auseinandergeht (Beispiel: 1 000 gegen 1 024), steht beides da, und die Prüfungsnotiz sagt, was in der Prüfung zählt und warum.
3. Zitierweise in der Kapitel-Quellenliste: `<li id="<kapitel>-q<n>" data-src="<schlüssel>"><span class="typ">Typ</span> Urheber: Titel, Nummer/Fassung, Herausgeber Jahr, Fundstelle. <a href="URL">kurz lesbare URL</a> <span class="abruf">(abgerufen JJJJ-MM-TT)</span></li>`. Ohne geprüfte URL: kein `<a>`, stattdessen `<span class="abruf">(nicht online geprüft)</span>`.
4. Im Text: `<sup class="q"><a href="#<kapitel>-q<n>" title="Kurzname">n</a></sup>` direkt hinter der Aussage, vor dem Satzzeichen oder danach, einheitlich pro Kapitel. Mehrere Quellen: mehrere `sup`.
5. Jede Begriffskarte trägt in der Theorie-Zeile mindestens einen Verweis. Jede Rechenformel trägt einen Verweis. Jede Rechts- oder Normaussage trägt den Verweis mit Fundstelle (Artikel, Paragraf, Abschnitt) im `title`.
6. Prüfungsaufgaben werden mit `data-src="ihk-ap1-<f|h><jahr>"` zitiert, Typ `IHK-Prüfung`, ohne URL (lokale Datei).
7. Sekundärquellen (Lernkurse, LERNPLAN, grundlast, Blogs) werden nie zitiert. Sie sind Rohmaterial.

## 8. Text- und Sprachregeln

- Deutsch, Du-Form, neue Rechtschreibung. Kurze Sätze. Ein Gedanke je Satz.
- Jedes Kapitel beginnt in „Worum es geht“ mit einem konkreten Fall aus dem Alltag eines IT-Systemhauses (ein Kunde, ein Gerät, ein Problem). Kein „In diesem Kapitel lernst du“.
- Fachbegriff beim ersten Auftreten deutsch, englische Form in Klammern, wenn Prüfungen sie verwenden (`Least Privilege`, `Broadcast`). Danach durchgängig eine Form.
- Abkürzungen beim ersten Auftreten ausschreiben.
- Zahlen im deutschen Format: `1.234,56 €`, `12 GB`, `5 Gbit/s`, `2,4 GHz`; zwischen Zahl und Einheit ein geschütztes Leerzeichen (`&nbsp;`).
- Fettdruck nur in `<dt>` und in Tabellenköpfen. Kursiv nur für englische Termini und Titel. Keine Ausrufezeichen. Keine Emojis. Keine Motivationssprache. Kein Selbstbezug auf KI oder auf diesen Bauplan.
- Keine Zeitangaben für den Lernenden (§1). Einzige Ausnahme: Prüfungsdauer und Fristen, die Prüfungsinhalt sind (72 Stunden, 30 Tage, zwei Jahre).
- Keine Wiederholung eines Themas in zwei Kapiteln. Stattdessen ein Satz mit Link: `siehe <a href="#b2">B2</a>`.
- Verwechslungen ausdrücklich benennen („wird verwechselt mit …, unterscheidet sich durch …“).
- Bei jeder Original-Aufgabe erklärt der Absatz „Punkte“ die Punktelogik aus den Lösungshinweisen („je ein Punkt für Maßnahme mit Begründung, insgesamt drei“).
- Gedankenstrich als Halbgeviertstrich mit Leerzeichen ( – ), kein Geviertstrich.
- HTML-Sonderzeichen im Text maskieren: `&lt;`, `&gt;`, `&amp;`.

## 9. Gestaltung

Das Gestaltungssystem ist fertig und liegt als CSS-Block in `00-kopf.html`. Es wird nicht verändert und nicht ergänzt. Der Lernende hat es am 2026-09-03 aus drei Entwürfen ausgewählt („Stil B, Werkstatt“) und dazu gesagt: „immer viel visuell grafisches wo es sinn macht“. Beides ist verbindlich.

Der Stil in einem Satz: weiße Seite, Groteske in großem Schriftbild, sehr kräftige Überschriften, dicke schwarze Linien als Gliederung, ein einziger warmer Akzent (`--akzent`, ein gebranntes Orange) für das, worauf es ankommt. Keine Serifenschrift, kein beiger Grund, keine Kartenraster, keine Verläufe, keine Schatten, keine Emojis, kein Dunkelmodus.

**Grafik ist Pflicht, nicht Zierde.** Ein Sachverhalt, den man zeichnen kann, wird gezeichnet. Der Text stützt das Bild, nicht umgekehrt. Wer das Bild im Kopf hat, kann die Aufgabe rekonstruieren. Konkret: mindestens zwei Abbildungen je Kapitel, in Gruppe A eher drei bis fünf. Eine Abbildung gehört überall dorthin, wo es um einen dieser fünf Fälle geht:

1. **Ablauf oder Reihenfolge.** Wer macht was in welcher Folge (DHCP-Ablauf, Signaturprüfung, TLS-Aufbau, Rechnungslauf, Netzplanrechnung vorwärts und rückwärts).
2. **Aufbau oder Zerlegung.** Woraus besteht etwas und wo liegt die Grenze (32-Bit-Adresse mit Präfixschnitt, Rechnung mit Pflichtangaben, OSI-Stapel, Vorgangsknoten, Arbeitsplatz in Seitenansicht mit Maßen).
3. **Gegenüberstellung.** Zwei Dinge, die man verwechselt, nebeneinander im Bild (symmetrisch gegen asymmetrisch, Voll- gegen Differenz- gegen Inkrementalsicherung auf einem Zeitstrahl, Chen- gegen Krähenfußnotation, HDD gegen SSD).
4. **Rechenkette.** Der Weg von der gegebenen Größe zum Ergebnis mit den Umrechnungsschritten als Kette (Watt zu Kilowattstunde zu Euro, Datenmenge zu Bit zu Zeit, Listenpreis zu Bezugspreis als Treppe).
5. **Zuordnung im Raum.** Etwas, das man in der Prüfung selbst zeichnen oder ergänzen muss (UML, ER-Modell, Netzplan, Verkabelung von der Dose zum Patchfeld zum Switch, Anschlusssilhouetten).

Tabellen sind keine Abbildungen und ersetzen keine. Eine Abbildung, die nur wiederholt, was der Absatz daneben sagt, wird gestrichen.

Erlaubte Bausteine (Klassen siehe Vorlage): Kapitelkopf, Abschnitte mit `h3`, Zwischenüberschrift `h4`, Absatz, Listen, Begriffskarte `dl.begriff`, Abbildung `figure.abb` mit inline SVG, Tabelle in `div.tabelle`, Rechenweg `pre.rechenweg`, Hinweisblock `div.merke` mit `data-art` aus genau drei Werten (`Merke`, `Typischer Fehler`, `Prüfungsnotiz`; höchstens vier je Kapitel), Aufgabe `article.aufgabe`, Aufklappbares `details` mit `summary` und `div.inhalt`, Quellenverweis `sup.q`, Quellenliste `ol.quellenliste`, Hervorhebung `mark` (nur für die Zahl oder das Wort, auf das die Aufgabe hinausläuft, höchstens dreimal je Kapitel).

Abbildungen (SVG):
- `viewBox="0 0 640 H"`, Höhe nach Bedarf, `role="img"`, `<title id="…">` mit Kurzbeschreibung, `figcaption` beginnt mit „Abb. A1-1:“ (Kapitel-Nummer). Die Bildunterschrift sagt, was man sehen soll, nicht was das Bild heißt.
- Linien in diesem Stil sind kräftig: `l`, `f` und `w` zeichnen mit 2 Einheiten, `a` mit 3. Kleinteilige Diagramme mit vielen dünnen Linien passen nicht; lieber wenige große Formen mit klaren Beschriftungen.
- Beschriftung gehört an das Ding, das sie benennt, nicht in eine Legende. Wo eine Legende unvermeidlich ist, steht sie im Bild, nicht in der Bildunterschrift.
- Der Akzent (`a`, `fa`, `ta`) markiert genau eine Sache je Abbildung: die Stelle, um die es geht. Wird alles betont, ist nichts betont.
- Gegebene und gesuchte Größen einer Aufgabe im Bild unterscheiden: gegeben in Tinte, gesucht im Akzent.
- Nur die Klassen `l` (Linie), `f` (gefüllte Form, Akzenttint), `w` (weiße Form), `a` (Akzentlinie, für das, worum es geht), `fa` (Akzentfläche, sparsam), `d` (gestrichelt), `g` (Gitter/Hilfslinie), Text mit `t2` (klein, grau), `tb` (fett), `ta` (Akzent), `mono`, `mitte`, `rechts`. Pfeile über `marker-end="url(#pfeil)"`, `url(#pfeil-a)`, `url(#pfeil-g)`.
- Keine eigenen Farben, keine Filter, keine Verläufe, keine Schrift kleiner als 11 im viewBox-Maß, kein Text, der über den Rand läuft (Textlänge vorher abschätzen: 13-px-Sans braucht rund 6,5 Einheiten je Zeichen).
- Eine Abbildung zeigt einen Mechanismus, nicht eine Dekoration. Wer die Abbildung im Kopf hat, kann die Aufgabe rekonstruieren.

Tabellen: Kopfzeile mit `th`, Zahlen rechtsbündig mit `class="z"`, Summenzeile `tr.summe`, hervorgehobene Zeile `tr.hervor` (höchstens eine je Tabelle), `caption` immer.

## 10. Kapitelvorlage und Budgets

Die Vorlage `bau/vorlage/kapitel-vorlage.html` ist verbindlich: Reihenfolge, ids, Klassen, Herkunftszeilen. Alle `VORLAGE:`-Kommentare werden entfernt, alle `PLATZHALTER` ersetzt. Der Prüfer erzwingt beides.

| Teil | Inhalt | Budget |
|---|---|---|
| Kopf | Nummer, Titel, „Kam dran“ (alle Teilaufgaben des Kapitels aus MATRIX.md, chronologisch, mit Punkten), Häkchen | – |
| Worum es geht | konkreter Fall, dann was man können muss, dann warum es geprüft wird | 80 bis 150 Wörter |
| Begriffe | 5 bis 10 Begriffskarten, jede mit genau den vier Zeilen Theorie (mit Quelle), Praxis, Merkhilfe und Verwechslung, In der Prüfung | 60 bis 120 Wörter je Karte |
| Das Verfahren / Die Sache | Schritt für Schritt; Gruppe A mit `pre.rechenweg`-Schema; **mindestens zwei Abbildungen** nach §9, in Gruppe A eher drei bis fünf; höchstens vier `merke`-Blöcke | 500 bis 1 000 Wörter |
| So hat die IHK gefragt | 1 bis 3 Original-Aufgaben (jüngste und punktreichste zuerst), sinngemäß, mit Herkunftszeile im festen Format; Lösung in `details` mit Absatz „Punkte“ | je Aufgabe bis 150 Wörter, Lösung bis 250 |
| Jetzt du | genau eine Variante je Original-Aufgabe (andere Zahlen oder anderes Szenario, gleiches Verfahren), Lösung in `details`, rechnerisch geprüft | wie Original |
| Selbstcheck | 3 bis 5 Fragen, Antwort je in `details` | je Antwort bis 60 Wörter |
| Quellen | alle im Kapitel verwendeten Quellen, Format §7 | – |

Kapitel insgesamt: Richtwert 2 000 bis 3 500 Wörter ohne SVG, Obergrenze 4 500 (Prüfer bricht ab). Kapitel mit vielen Prüfungsbelegen (B1, B4, B5, A2) nutzen das Budget aus, kleine Kapitel (A3, A5) bleiben kurz. Nie auffüllen.

Begriffskarte, Zeile für Zeile:
- **Theorie**: die Definition, fachlich exakt, ein bis zwei Sätze, mit Quellenverweis (bei Rechtsbegriffen Artikel oder Paragraf im `title`).
- **Praxis**: wo dem Leser das im Systemhaus oder beim Kunden konkret begegnet; ein Beispiel, kein Allgemeinsatz.
- **Merkhilfe und Verwechslung**: womit der Begriff verwechselt wird, woran man ihn auseinanderhält, eine sachliche Merkhilfe (Eselsbrücke nur, wenn sie trägt).
- **In der Prüfung**: wie die IHK danach fragt (Operator, typische Formulierung), was die Lösungshinweise erwarten, wie viele Aspekte je Punkt.

## 11. Prüfung und Zusammenbau

- Fragment prüfen: `node bau/pruef/check.js bau/kapitel/10-a1.html --fragment`
- Alles zusammensetzen und prüfen: `cd C:/Users/mu.aycetin/Desktop/Lernen && node bau/pruef/bauen.js`
- Rechnung prüfen (Beispiel): `python -c "print(2**(32-26)-2)"` oder `node -e "console.log(1500*0.97)"`; Eingabe und Ausgabe nach `bau/notizen/RECHNUNGEN-<kapitel>.md` kopieren.
- Der Prüfer meldet Fehler (müssen behoben werden) und Hinweise (lesen, abwägen, in `ENTSCHEIDUNGEN.md` begründen, wenn nicht umgesetzt).

## 12. Abnahme (Definition of done)

Die Datei ist fertig, wenn alles Folgende zutrifft:

1. `node bau/pruef/bauen.js` endet mit „Keine Fehler.“
2. Alle 20 Kapitel, Teil 0 bis 5 vorhanden; Navigation trifft jedes Ziel.
3. Jede Teilaufgabe aus MATRIX.md ist in genau einer „Kam dran“-Zeile aufgeführt; jede Kam-dran-Zeile stimmt mit MATRIX.md überein.
4. Jede URL in der Datei steht in QUELLEN-A.md oder QUELLEN-B.md als „geprüft“ mit demselben Abrufdatum.
5. Jede Rechnung in Original-Lösungen und Varianten ist in einer RECHNUNGEN-Datei protokolliert.
6. Kein Wort aus der Liste: Emoji, Verlauf, Schatten, Lesezeit, Wochenplan, „In diesem Kapitel“.
7. Sichtprüfung im Browser bei 1440 px und 900 px durchgeführt oder als „kein Browser verfügbar“ vermerkt.
8. Phase F hat mindestens 40 Stichproben geprüft und alle Befunde behoben; PRUEFBEFUNDE.md liegt vor.
9. Marker Z.done und F.done vorhanden.

## 13. Abschlussbericht jeder Phase

Höchstens 15 Zeilen in `bau/status/<Phase>.done`: erzeugte Dateien mit Pfad; Anzahl (Teilaufgaben, Quellen, Kapitel, Wörter); was unklar blieb oder nach §2 Regel 7 entschieden wurde (Verweis auf ENTSCHEIDUNGEN.md); Ergebnis des Prüfers. Kein Lob, keine Zusammenfassung des Plans.

## 14. Startprompts für die Phasen

Jeder Prompt beginnt mit: „Lies `C:\Users\mu.aycetin\Desktop\Lernen\BAUPLAN.md` vollständig. Du bist Bauer für Phase <X>. Stelle keine Rückfragen (§2 Regel 7). Schreibe nur unter `Lernen/bau/` (§2 Regel 11). Schließe mit `bau/status/<X>.done` nach §13.“ Danach die Phasenangabe:

- **E1**: „Extraktion nach §5.1 für Herbst 2021, Frühjahr 2022, Herbst 2022. Dateien §3.1, §3.2; Rohmaterial §3.3 (Frühjahr 2022 als Markdown vorhanden).“
- **E2**: „Extraktion nach §5.1 für Frühjahr 2023, Herbst 2023, Frühjahr 2024. Rohmaterial: Lernkurs Frühjahr 2024.“
- **E3**: „Extraktion nach §5.1 für Herbst 2024, Frühjahr 2025, Herbst 2025. Rohmaterial: die drei Lernkurse.“
- **Q-A**: „Quellenprüfung nach §5.2 und §7 für Teil 1 (FIAusbV, IHK-Operatorenliste, AKA-Prüfungskatalog-Hinweis) und die Startquellen von A1 bis A9 (§6). Ergebnis `notizen/QUELLEN-A.md`.“
- **Q-B**: „Quellenprüfung nach §5.2 und §7 für die Startquellen von B1 bis B11 (§6). Ergebnis `notizen/QUELLEN-B.md`.“
- **M**: „Phase M nach §5.4. Voraussetzung: E1.done, E2.done, E3.done, QA.done vorhanden.“
- **K-1** bis **K-5**: „Kapitelphase nach §5.3 für <Kapitel>. Voraussetzung: M.done, QA.done, QB.done.“ Zuteilung: K-1 = A1, A2, A3, A4; K-2 = A5, A6, A7, A8, A9; K-3 = B1, B2, B3, B4; K-4 = B5, B6, B7, B8; K-5 = B9, B10, B11.
- **V**: „Phase V nach §5.5. Voraussetzung: K1.done, K2.done.“
- **Z**: „Phase Z nach §5.6. Voraussetzung: alle K*.done und V.done.“
- **F**: „Phase F nach §5.7. Voraussetzung: Z.done.“

## 15. Herkunft der Vorgaben dieses Plans

- Leser, Ziel, Verbote: Gespräch am 2026-09-02; `Desktop/Projekt/AP1/PRODUCT.md`.
- Kapitelliste und Lernziele: Sichtung der Lernkurse H2024, F2025, H2025 (Überschriften und Punkteübersichten), der Markdown-Fassung F2022, des alten Zwischenprüfungsformats F2021, von `LERNPLAN.md` (Juli 2026) und des grundlast-Katalogs (`AP1_STATUS.md`, `CURRICULUM_MAPPING.md`). Die Zuordnung „kam dran“ ist Sichtung, keine Zählung; die Zählung liefert Phase M aus den Notizen.
- Startquellen: aus Kenntnis der Normen, Gesetze und RFCs zusammengestellt; jede wird in Phase Q geprüft, ungeprüfte werden nicht zitiert.
- Gestaltungssystem: eigene Setzung nach Butterick, „Practical Typography“, und den Verboten aus PRODUCT.md.
- Prüfer und Zusammenbau: eigene Skripte, Node v25 und Python 3.14 sind auf dem Rechner vorhanden (geprüft am 2026-09-02).

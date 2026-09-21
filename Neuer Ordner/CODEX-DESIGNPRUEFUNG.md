## A. Typografie und Lesbarkeit

- **Schwere:** blockierend  
  **Stelle:** `C:/Users/mu.aycetin/Desktop/Lernen/DESIGN-VORSCHAU.html` (am angegebenen Pfad nicht vorhanden)  
  **Beobachtung:** Die Vorschau fehlte bei vier Existenzprüfungen. Damit sind tatsächliche Text- und Hintergrundfarben, Schriftgrößen, Zeilenhöhen, Zeilenlängen und die vollständigen `font-family`-Deklarationen nicht belegbar. Insbesondere dürfen keine Kontrastwerte geschätzt werden; ohne Farbwerte lässt sich die WCAG-2.2-Quote `(L_hell + 0,05) / (L_dunkel + 0,05)` nicht berechnen und nicht gegen 4,5:1 beziehungsweise 3:1 prüfen. Auch die metrische Eignung der Fallbacks ist ohne die tatsächlich deklarierte Reihenfolge nicht beurteilbar. Annahme zum allgemeinen Browserverhalten unter Windows 11: Fehlt eine benannte Schrift, wird die nächste Familie der Liste versucht und zuletzt gegebenenfalls der generische Fallback des Systems benutzt; welche Schrift das konkret ist und wie stark Laufweite, x-Höhe und Umbruch abweichen, hängt vom vollständigen Stack und vom Rechner ab.  
  **Empfohlene Korrektur:** Die Vorschau am exakt genannten Pfad erzeugen und A vollständig wiederholen. Alle effektiven Farbpaare sind mit der WCAG-Relativluminanz exakt zu berechnen; die vollständigen Stacks sind auf einem unveränderten Windows-11-System mit fehlender Erstwahl auf Umbruch- und Höhenänderungen zu testen.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeile 639; Vorgabe des Prüfauftrags zu `Sitka Text`  
  **Beobachtung:** Der Bauplan verbietet Serifenschrift, während der Prüfauftrag ausdrücklich einen Serifenstapel mit `Sitka Text` als erster Wahl nennt. Ohne das CSS bleibt offen, ob der Stapel nur ungenutzt deklariert oder tatsächlich angewandt wird. Die beiden Vorgaben sind in ihrer gegenwärtigen Form nicht gleichzeitig normativ erfüllbar, sobald der Serifenstapel verwendet wird.  
  **Empfohlene Korrektur:** Festlegen, welche Vorgabe Vorrang hat. Bei Fortgeltung von Zeile 639 darf der Serifenstapel nirgends wirksam werden; andernfalls muss der Bauplan den eng begrenzten Einsatzzweck ausdrücklich zulassen.

## B. Robustheit des CSS

- **Schwere:** blockierend  
  **Stelle:** fehlende Selektoren in `DESIGN-VORSCHAU.html`: `body`, Navigation, `details`, `summary`, Tabellen-Wrapper, Glossarliste und die Regel mit `scroll-padding-top`  
  **Beobachtung:** Ohne die Vorschau sind Spaltenbreite und Mindestbreite des Body-Grids, Sticky-/Overflow-Vorfahren, der negative obere Rand aufeinanderfolgender `details`, Ankerabstände, horizontales Tabellen-Scrolling und das Verhalten der mehrspaltigen Glossarliste nicht anhand tatsächlicher Deklarationen prüfbar. Konkrete Bruchstellen bei 20 Kapiteln wären ohne Quelltext Spekulation.  
  **Empfohlene Korrektur:** Nach Bereitstellung der Vorschau die genannten Selektoren samt Cascade und Media Queries bei schmalem Viewport, 200-%-Zoom, sehr langen Tabellen/SVGs, aufeinanderfolgenden offenen und geschlossenen `details` sowie einer langen Glossarliste prüfen.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeile 637  
  **Beobachtung:** Der Bauplan erklärt den CSS-Block für unveränderlich und verbietet sogar Ergänzungen. Damit fehlt ein zulässiger Korrekturweg, falls die verlangte Robustheitsprüfung einen reproduzierbaren Layoutfehler im gemeinsamen CSS nachweist.  
  **Empfohlene Korrektur:** Einen eng begrenzten, versionierten Fehlerkorrekturweg für den gemeinsamen CSS-Block definieren und danach Prüfsumme sowie Prüferwartung aktualisieren.

## C. Druck

- **Schwere:** blockierend  
  **Stelle:** nicht zugänglicher `@media print`-Block und nicht zugängliches Fußskript in der fehlenden `DESIGN-VORSCHAU.html`  
  **Beobachtung:** Es ist nicht belegbar, ob jedes Kapitel auf einer neuen Seite beginnt, ob Abbildungen, Tabellen, Rechenwege und Begriffskarten gegen ungünstige Umbrüche geschützt sind, ob Tabellenköpfe wiederholt werden oder ob `beforeprint` alle Lösungen sichtbar macht. Ebenso lässt sich nicht feststellen, ob `afterprint` den vorherigen Zustand wiederherstellt und ob Seitenzahlen beziehungsweise laufende Seitentitel vorgesehen sind.  
  **Empfohlene Korrektur:** Nach Bereitstellung der Vorschau eine echte Druckvorschau mit mehrseitigen Grenzfällen prüfen: Kapitelanfang, große SVGs, mehrseitige Tabellen, lange Rechenwege, Begriffskarten, offene und geschlossene Lösungen sowie Abbruch des Druckdialogs.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 697–706  
  **Beobachtung:** Die Abnahmeliste verlangt eine Browser-Sichtprüfung bei 1.440 px und 900 px, aber keine Druckprüfung. Damit kann der formale Bauabschluss einen unbrauchbaren Ausdruck übersehen.  
  **Empfohlene Korrektur:** Die Abnahme um Druckkriterien ergänzen: Kapitel-Seitenbeginn, sichtbare Lösungen, sinnvolle `break-inside`-Regeln, wiederholtes `thead`, lesbare Link-/URL-Behandlung und, soweit die Zielbrowser es unterstützen, Seitenzahl und Seitentitel.

## D. Das Skript am Dateiende

- **Schwere:** blockierend  
  **Stelle:** fehlendes Endskript in `DESIGN-VORSCHAU.html`  
  **Beobachtung:** Storage-Zugriffe, Navigation-Spiegelung, Observer-Konfiguration und Druckzustandsverwaltung sind nicht lesbar. Deshalb sind Fehlerbehandlung bei blockiertem `localStorage`, Aufwand bei 20 Kapiteln, Umschaltpunkte der tatsächlichen `rootMargin`-Werte, Wiederherstellung verschachtelter `details` sowie die Funktion unter `file://` nicht belegbar. Annahme: `localStorage` für `file:`-Dokumente ist browserabhängig und darf ohne Test im Zielbrowser nicht als dauerhaft verfügbar behandelt werden.  
  **Empfohlene Korrektur:** Nach Bereitstellung unter `file://` testen: blockierter oder eine Ausnahme werfender Storage, fehlender `IntersectionObserver`, 20 Kapitel mit sehr kurzen und sehr langen Abschnitten, mehrere Druckdialoge, abgebrochener Druck und manuell geänderte `details` während des Druckvorgangs. Storage-Lesen und -Schreiben muss in einem fehlertoleranten Fallback gekapselt sein.

## E. Zugänglichkeit

- **Schwere:** blockierend  
  **Stelle:** fehlendes DOM und fehlendes CSS in `DESIGN-VORSCHAU.html`  
  **Beobachtung:** Überschriftenhierarchie, Landmarks, zugänglicher SVG-Name, Struktur der Definitionslisten, Tastaturbedienbarkeit von `details` und Checkbox, Fokus-Sichtbarkeit und Linktexte der Quellenliste sind nicht am tatsächlichen Dokument prüfbar. Insbesondere kann kein Selektor für `:focus` oder `:focus-visible` belegt werden.  
  **Empfohlene Korrektur:** Nach Bereitstellung die Seite vollständig per Tastatur und im Accessibility Tree prüfen; dabei Fokusreihenfolge und Fokusindikator, Überschriftenebenen, Landmark-Namen, Checkbox-Beschriftung, `summary`-Namen, SVG-Namensberechnung sowie Linktexte kontrollieren.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 651–660  
  **Beobachtung:** Der Bauplan fordert für SVG zwar `role="img"` und ein `title`, verlangt aber weder eine eindeutige Zuordnung über `aria-labelledby` noch einen sichtbaren Fokusstil, einen Sprunglink oder eigenständig verständliche Quellenlinktexte. Das ist eine Lücke der Sollvorgaben; daraus folgt ohne Vorschau noch kein konkreter DOM-Fehler.  
  **Empfohlene Korrektur:** Bauplan und Abnahme um überprüfbare Kriterien für sichtbaren Tastaturfokus, Landmark-/Sprungnavigation, eindeutige zugängliche SVG-Namen und kontextfrei verständliche Linktexte ergänzen.

## F. Das Prüfskript `check.js`

- **Schwere:** blockierend  
  **Stelle:** `BAUPLAN.md`, Zeilen 637–660; `check.js`, Zeilen 14–24 und 118–122  
  **Beobachtung:** Die Unveränderlichkeit des CSS aus `00-kopf.html` wird nicht geprüft. Zusätzliches CSS oder geänderte Farben bestehen, solange keines der wenigen gesuchten Teilwörter vorkommt. Die Ressourcenprüfung lässt unter anderem `<script defer src="x.js">`, ein `img` mit Zeilenumbruch vor `src`, externe Stylesheets, CSS-`url(https://…)`, SVG-`image`, `object`, Audio und Video passieren. Damit können Offlinebetrieb und Gestaltungsbindung verletzt werden.  
  **Empfohlene Korrektur:** In Fragmenten `style` und ressourcenladende Elemente beziehungsweise Attribute verbieten; im Gesamtdokument genau den erwarteten CSS-Block per Prüfsumme oder strukturellem Vergleich zulassen. Externe Ressourcen kontextbezogen mit einem HTML-Parser prüfen, normale Quellenlinks aber erlauben.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 627 und 667; `check.js`, Zeilen 15–27  
  **Beobachtung:** Globale Teilzeichen-Suchen erzeugen falsche Fehler. Schon das Wort „Rechnungsvorlage“ enthält `VORLAGE`; ein fachlicher Codeausschnitt mit `box-shadow` oder `@import` wird wie wirksames CSS behandelt. `\p{Extended_Pictographic}` erfasst außerdem sachlich mögliche Zeichen wie `©`, `®`, `™` und `↔`, obwohl sie nicht zwingend als Emoji verwendet werden.  
  **Empfohlene Korrektur:** `VORLAGE:` nur in Vorlagenkommentaren und echte Platzhaltermarker strukturell prüfen. CSS-Verbote nur im Style-Kontext anwenden; für Emoji Präsentationsform, Variationsselektoren und ZWJ-Sequenzen berücksichtigen oder erlaubte sachliche Symbole ausnehmen.

- **Schwere:** blockierend  
  **Stelle:** `check.js`, Zeilen 55–70  
  **Beobachtung:** Kapitel werden nur bei der exakten Zeichenfolge `<section class="kapitel" id="…">` erkannt. `<section class="kapitel" aria-labelledby="titel-a1" id="a1">` oder `<section id="a1" class="kapitel">` ergibt keine Kapitelmenge; damit entfallen sämtliche Kapitelprüfungen. Im Gesamtdokument kann die allgemeine ID-Suche die erwarteten IDs dennoch finden. Umgekehrt kann ein bloßer Kommentar mit `id="a1-worum"` die per `includes()` ausgeführte Abschnittsprüfung erfüllen.  
  **Empfohlene Korrektur:** HTML parsen, Kapitel über `section.kapitel[id]` ermitteln und die sieben Abschnitte als reale Elemente im zulässigen DOM-Bereich prüfen. Kommentare und Skripttext dürfen nicht zählen.

- **Schwere:** wichtig  
  **Stelle:** `check.js`, Zeilen 71–78, 81–85, 97–108 und 125–139  
  **Beobachtung:** Viele Regeln hängen von Attributreihenfolge, doppelten Anführungszeichen und einem unmittelbar folgenden `>` ab. Beispielsweise zählen `<figure class="abb" id="a1-f1">`, `<title lang="de" id="a1-t1">`, `<p id="h1" class="herkunft">` und `<li data-src="x" id="a1-q1">` nicht. Valides, besonders um ARIA-Attribute ergänztes HTML kann daher scheitern oder Prüfungen umgehen. IDs und Links in einfachen Anführungszeichen werden übersehen.  
  **Empfohlene Korrektur:** Elemente und Attribute ausschließlich über einen HTML-DOM-Parser selektieren; Reihenfolge und Quote-Stil dürfen keine Bedeutung haben.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 622–633; `check.js`, Zeilen 143–156 und 168–170  
  **Beobachtung:** Wesentliche Regeln aus §8 fehlen: Deutsch und Du-Form, kurzer Satzbau, konkreter Systemhausfall, Erstnennung von Fachbegriffen, ausgeschriebene Abkürzungen, deutsches Zahlenformat, `&nbsp;` vor Einheiten, zulässige Orte für Fett- und Kursivdruck, Motivationssprache, Themenwiederholungen, Verwechslungssätze, Punktelogik und maskierte Sonderzeichen. `<strong>` außerhalb von `dt` und `th`, `2.5 GHz`, ein normales Leerzeichen in `2,4 GHz` oder rohes `AT&T` passieren. Selbst erkannte Sprachverstöße sind nur Hinweise und ändern den Exit-Code nicht.  
  **Empfohlene Korrektur:** Strukturell prüfbare Regeln als Fehler implementieren, insbesondere Hervorhebungskontext, Zahlen/Einheiten, Sonderzeichen und Pflichtabsätze. Semantische Regeln als verbindliche manuelle Prüfliste ausgeben.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 627–632; `check.js`, Zeilen 146–155  
  **Beobachtung:** Die vorhandenen Sprachregex sind zugleich lückenhaft und zu breit. `20&nbsp;Minuten pro Tag`, `OK!`, ein Ausrufezeichen vor einem Schlussanführungszeichen sowie „Dieser Text wurde von ChatGPT erstellt“ werden nicht erkannt. Dagegen wird „30 Minuten je Prüfungsteil“ trotz der erlaubten Prüfungsdauer gemeldet. Beim Gedankenstrich wird nur das Geviertstrich-Zeichen gesucht; fehlende Leerzeichen um `–` und ein ersatzweise benutzter Bindestrich bleiben unentdeckt.  
  **Empfohlene Korrektur:** Sichtbaren, entity-dekodierten DOM-Text prüfen, Satzzeichenfälle vollständig erfassen, Prüfungsdauer über klaren Kontext oder Markup ausnehmen und Halbgeviertstriche einschließlich beider Leerzeichen validieren.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 641–663; `check.js`, Zeilen 71–79 und 111–122  
  **Beobachtung:** Von den SVG-Regeln werden nur Teilstrings für `role`, `title`, `figcaption` und `viewBox` geprüft. Eine Bildnummer aus dem falschen Kapitel besteht; `title` und `viewBox` müssen nicht demselben SVG zugeordnet sein. Linienbreiten, erlaubte Farben/Klassen, genau ein Akzent, Mindestschriftgröße 11, Textüberlauf, gegebene/gesuchte Größen und Filterverbot fehlen. Für Tabellen fehlen alle Prüfungen auf `div.tabelle`, `caption`, Kopfzellen, `.z`, `.summe` und höchstens eine `.hervor`-Zeile.  
  **Empfohlene Korrektur:** Jede `figure.abb` als DOM-Unterbaum prüfen, Kapitelkennung und laufende Nummer abgleichen, SVG-Attribute/-Klassen per Positivliste validieren und sämtliche Tabellenregeln ergänzen.

- **Schwere:** blockierend  
  **Stelle:** `BAUPLAN.md`, Zeilen 667–678; `check.js`, Zeilen 55–70 und 119  
  **Beobachtung:** Die verbindliche Kapitelvorlage wird weder auf Reihenfolge noch auf Elementtypen oder Überschriften geprüft. Die sieben IDs dürfen auf beliebigen Elementen in beliebiger Reihenfolge stehen. Kapitelnummer, Titel, vollständige chronologische „Kam dran“-Zeile und echte Checkbox werden nicht validiert; irgendein `data-key="a1"` genügt. Die vorgeschriebenen `h3` sowie `details > summary + div.inhalt` fehlen in der Prüfung.  
  **Empfohlene Korrektur:** Eine DOM-basierte Strukturspezifikation pro Kapitel durchsetzen: Kopfbestandteile, `input[type="checkbox"][data-key]`, Abschnittsreihenfolge, Überschriften und Details-Struktur.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 673 und 682–686; `check.js`, Zeilen 81–95  
  **Beobachtung:** Entgegen dem Kommentar „genau vier dd“ zählt der Code nur vier `span.label` in passender Textreihenfolge. Eine Karte ohne `dt`, mit allen Labels in einem einzigen `dd` und mit zusätzlichen unbeschrifteten `dd` kann bestehen. Die 60–120 Wörter, ein bis zwei Theorie-Sätze und die inhaltlichen Anforderungen werden nicht geprüft. Ein Quellenverweis muss lediglich irgendwo vor dem Praxis-Label stehen.  
  **Empfohlene Korrektur:** Genau ein direktes `dt` und vier direkte `dd` verlangen; jedes `dd` muss genau das erwartete Label enthalten. Budget separat zählen und den Quellenverweis innerhalb des Theorie-`dd` fordern.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 675–677; `check.js`, Zeilen 97–106  
  **Beobachtung:** Aufgaben werden nur kapitelweit gezählt. Herkunftszeilen sind keiner Original-Aufgabe zugeordnet und können gesammelt anderswo stehen. Ein `div.aufgabe` genügt statt `article.aufgabe`. Varianten brauchen nur dieselbe Gesamtzahl; Zuordnung und Nummer bleiben offen. Lösungen in `details`, der Absatz „Punkte“, Reihenfolge nach Aktualität/Punktzahl, Herkunft pro Aufgabe und rechnerische Prüfung fehlen. Drei leere `li` erfüllen den Selbstcheck.  
  **Empfohlene Korrektur:** Jede Aufgabe als eigenes `article.aufgabe` prüfen, Herkunft, Lösung und Punkteabsatz innerhalb des Artikels verlangen und Original/Variante über Kapitelkennung und laufende Nummer paaren. Jedes Selbstcheck-`li` muss Frage und genau ein Antwort-`details` enthalten.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 651 und 673–677; `check.js`, Zeilen 82–83 und 99–113  
  **Beobachtung:** Verbindliche Obergrenzen sind falsch oder nur Hinweise. Der Plan erlaubt 5–10 Begriffskarten; 11 und 12 bleiben ohne Meldung, ab 13 folgt nur ein Hinweis. Mehr als drei Original-Aufgaben und mehr als vier Merke-Blöcke erzeugen ebenfalls nur Hinweise. Die Obergrenze von fünf Selbstcheckfragen und höchstens drei `mark` je Kapitel wird gar nicht geprüft. Eine andere Attributreihenfolge umgeht auch die `data-art`-Erkennung.  
  **Empfohlene Korrektur:** Verbindliche Bereiche als Fehler behandeln: Karten 5–10, Originale 1–3, Merke höchstens 4, Selbstcheck 3–5 und `mark` höchstens 3; DOM-basiert zählen.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeile 678; `check.js`, Zeilen 107–110  
  **Beobachtung:** Mindestens drei Quellen und mindestens sechs Quellenverweise stehen nicht in §10. Die erfundene Dreiergrenze kann ein fachlich vollständiges Kapitel mit ein oder zwei maßgeblichen Primärquellen blockieren. Gleichzeitig wird weder geprüft, ob alle verwendeten Quellen vollständig formatiert sind, noch ob unbenutzte Einträge verbleiben.  
  **Empfohlene Korrektur:** Die unbelegte Mengenuntergrenze entfernen. Stattdessen jeden `sup.q` auf genau ein eindeutiges Ziel beziehen, unbenutzte Quellen melden und das vorgeschriebene Quellenformat prüfen.

- **Schwere:** wichtig  
  **Stelle:** `BAUPLAN.md`, Zeilen 672–680; `check.js`, Zeilen 64–65 und 114–117  
  **Beobachtung:** Sämtliche Teilbudgets fehlen. Für das Gesamtkapitel warnt der Prüfer erst unter 900 Wörtern, obwohl 2.000–3.500 der Richtwert ist; 900–1.999 Wörter bleiben unauffällig. Der regexbasierte Zähler arbeitet nicht mit sichtbarem DOM-Text und kann etwa großgeschriebenes `SVG`, Skriptinhalt oder ungewöhnliches Markup falsch zählen.  
  **Empfohlene Korrektur:** Sichtbaren, entity-dekodierten Text je Abschnitt DOM-basiert zählen. Unter 2.000 und über 3.500 als Hinweis, über 4.500 als Fehler behandeln; alle speziellen Teilbudgets separat melden.

- **Schwere:** blockierend  
  **Stelle:** `check.js`, Zeilen 29–53  
  **Beobachtung:** Der selbstgeschriebene Tag-Parser urteilt bei konkreten Eingaben falsch. Falsch positiv sind das gültige HTML `<ul><li>Eins<li>Zwei</ul>` mit optionalen `li`-End-Tags, `<textarea><b></textarea>` mit RCDATA und gültiger SVG-Fremdinhalt `<svg><![CDATA[<g>]]></svg>`. Falsch negativ sind `<div` am Dateiende, `<div/>Text` (der Slash schließt ein HTML-`div` im Browser nicht), `<p><div>Block</div></p>` mit abweichender Browser-DOM-Struktur und `<scripture><div></script>`, das wegen der fehlenden Wortgrenze der Script-Ausblendung vollständig maskiert wird. Außerdem löschen die Ersetzungen Zeilenumbrüche: Bei `<script>\nx\n</script>\n<div></span>` liegt der Fehler im Original in Zeile 4, gemeldet wird Zeile 2.  
  **Empfohlene Korrektur:** Einen standardkonformen HTML5-Parser mit Quellpositionen einsetzen. Falls explizite End-Tags gewollt sind, dies nach dem Parsen als eigene Serialisierungsregel prüfen. Bis dahin Raw-/RCDATA, Foreign Content, Wortgrenzen, unvollständige Tags und der Erhalt aller Zeilenumbrüche korrigieren.

- **Schwere:** blockierend  
  **Stelle:** `bauen.js`, Zeilen 14–16 und 78–87; `check.js`, Zeilen 158–166  
  **Beobachtung:** Der Zusammenbau nimmt jede Datei passend zu `^\\d{2}-.+\\.html$`; eine alte `98-alt.html` gelangt in die Ausgabe. Weder Bau- noch Prüfskript verlangen exakt 20 Kapitel oder einen exakten Fragmentbestand. Fehlende Pflichtdateien erzeugen in `bauen.js` nur „Achtung“, der Bau läuft weiter, und das Ziel wird vor erfolgreicher Prüfung geschrieben. IDs aus einer falschen Datei können die Dateiebene des Prüfers zufriedenstellen.  
  **Empfohlene Korrektur:** Einen festen Manifest-Satz verwenden, bei fehlenden oder zusätzlichen Dateien vor dem Schreiben abbrechen und exakt 20 erwartete Kapitel-IDs prüfen. Zunächst in eine temporäre Zieldatei bauen, prüfen und erst danach atomar als Enddatei übernehmen.

- **Schwere:** wichtig  
  **Stelle:** `bauen.js`, Zeilen 22–32, 44–60 und 73–83; `check.js`, Zeilen 81–95 und 107–108  
  **Beobachtung:** Glossar- und Quellenextraktion wiederholen die starren Regexannahmen. Zusätzliche Attribute am `dl`, Attribute am `dt`, Kommentare oder umgestellte Quellenattribute können Einträge aus der generierten Ausgabe entfernen. Haben zwei Einträge dasselbe `data-src`, aber abweichende bibliografische Angaben, übernimmt `bauen.js` stillschweigend nur die erste Fassung.  
  **Empfohlene Korrektur:** Prüfer und Zusammenbau müssen denselben DOM-basierten Extraktor verwenden. Widersprüchliche Metadaten für identisches `data-src` als Fehler melden und Glossar-/Quellenbestand nach der Generierung mit den Kapiteln abgleichen.

## G. Das Musterkapitel gegen den Bauplan

- **Schwere:** blockierend  
  **Stelle:** `DESIGN-VORSCHAU.html` (nicht vorhanden); Soll: `BAUPLAN.md`, Zeilen 620–633 und 665–687  
  **Beobachtung:** Ein Soll-Ist-Vergleich ist nicht möglich. Deshalb lassen sich weder die sieben Abschnitte, genau vier `dd` je Begriffskarte, Herkunftszeile und Variante je Original-Aufgabe noch Verstöße gegen Zeitangaben, Geviertstrich, Ausrufezeichen und die Beschränkung von Fettdruck belastbar feststellen. Eine Aufzählung vermuteter Abweichungen wäre nicht quellengestützt.  
  **Empfohlene Korrektur:** Die Vorschau unter dem angegebenen Pfad bereitstellen und G vollständig zeilengenau wiederholen; bis dahin darf das Musterkapitel nicht als gegen §8 und §10 geprüft gelten.

## H. Fachliche Stichprobe

- **Schwere:** blockierend  
  **Stelle:** `DESIGN-VORSCHAU.html` (nicht vorhanden; Rechenweg, Aufgaben und Präfixtabelle ohne Ist-Zeilenreferenz)  
  **Beobachtung:** Abweichungen der Vorschau können nicht festgestellt werden. Die zweimal unabhängig nachgerechneten Sollwerte lauten:

  - `192.168.10.75/26`: IP binär `11000000.10101000.00001010.01001011`; Maske `255.255.255.192`, binär `11111111.11111111.11111111.11000000`; Netz `192.168.10.64`, binär `11000000.10101000.00001010.01000000`; Broadcast `192.168.10.127`, binär `11000000.10101000.00001010.01111111`; Hostbereich `192.168.10.65` bis `192.168.10.126` mit Endoktetten `01000001` und `01111110`; `2^6 - 2 = 62` nutzbare Hosts.
  - `192.168.20.128/26`: IP und Netz binär `11000000.10101000.00010100.10000000`; Maske `255.255.255.192`, binär `11111111.11111111.11111111.11000000`; Netz `192.168.20.128`; Broadcast `192.168.20.191`, binär `11000000.10101000.00010100.10111111`; Hostbereich `192.168.20.129` bis `192.168.20.190` mit Endoktetten `10000001` und `10111110`; 62 nutzbare Hosts.
  - `10.14.7.96/27`: IP und Netz binär `00001010.00001110.00000111.01100000`; Maske `255.255.255.224`, binär `11111111.11111111.11111111.11100000`; Netz `10.14.7.96`; Broadcast `10.14.7.127`, binär `00001010.00001110.00000111.01111111`; Hostbereich `10.14.7.97` bis `10.14.7.126` mit Endoktetten `01100001` und `01111110`; `2^5 - 2 = 30` nutzbare Hosts.

  | Präfix | Maske | Binäres letztes Maskenoktett | Hostbits | Adressen | Nutzbare Hosts | Blockgröße |
  |---:|---|---|---:|---:|---:|---:|
  | `/24` | `255.255.255.0` | `00000000` | 8 | 256 | 254 | 256 |
  | `/25` | `255.255.255.128` | `10000000` | 7 | 128 | 126 | 128 |
  | `/26` | `255.255.255.192` | `11000000` | 6 | 64 | 62 | 64 |
  | `/27` | `255.255.255.224` | `11100000` | 5 | 32 | 30 | 32 |
  | `/28` | `255.255.255.240` | `11110000` | 4 | 16 | 14 | 16 |
  | `/29` | `255.255.255.248` | `11111000` | 3 | 8 | 6 | 8 |
  | `/30` | `255.255.255.252` | `11111100` | 2 | 4 | 2 | 4 |

  **Empfohlene Korrektur:** Nach Bereitstellung jede dargestellte Dezimalzahl, Binärgruppe und Tabellenzelle gegen diese Referenzwerte vergleichen und jede Abweichung mit der tatsächlichen Vorschau-Zeile dokumentieren.

## Die fuenf wichtigsten Aenderungen in Reihenfolge

1. `DESIGN-VORSCHAU.html` am vorgegebenen Pfad bereitstellen und A–E, G und den Ist-Vergleich in H vor jeder Abnahme vollständig wiederholen.
2. Den regexbasierten HTML- und Tag-Parser in `check.js` durch einen standardkonformen HTML5-DOM-Parser mit Quellpositionen ersetzen.
3. Kapitelstruktur, Aufgaben-/Variantenpaare, Begriffskarten, Tabellen, SVG-Regeln und Budgets DOM-basiert und entsprechend den verbindlichen Grenzen aus §9–§10 prüfen.
4. Die harten Sprachregeln aus §8 als Fehler durchsetzen und semantisch nicht automatisierbare Regeln als verpflichtende manuelle Prüfliste ausgeben.
5. Den Zusammenbau auf ein exaktes Dateimanifest und genau 20 Kapitel begrenzen, externe Ressourcen kontextbezogen ausschließen und erst nach erfolgreicher Prüfung atomar die Zieldatei schreiben.

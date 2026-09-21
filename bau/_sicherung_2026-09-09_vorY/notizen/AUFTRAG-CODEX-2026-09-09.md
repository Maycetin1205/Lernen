# Auftrag an Codex – Lerndatei weiter verbessern (Stand 2026-09-09)

Du arbeitest allein und so lange, bis dein Kontingent aufgebraucht ist. Nach jeder abgeschlossenen
Einheit ist der Stand konsistent gesichert (siehe Abschnitt 4). Brichst du mitten in einer Einheit ab,
darf nichts Halbfertiges im Koffer oder im Bau liegen: entweder die Einheit fertig durchziehen oder
die Kapiteldatei aus der Sicherung zurückholen (siehe Schritt 0 in Abschnitt 3).

## 1. Was das Projekt ist

- Arbeitsordner: `C:\Users\mu.aycetin\Desktop\Lernen\bau` (kein Git; Sicherungen sind Ordnerkopien `_sicherung_<datum>_*`).
- Kapitel liegen in `kapitel/NN-<id>.html` (A1–A9 = 10-a1 … 18-a9, B1–B11 = 20-b1 … 30-b11).
  Jedes Kapitel ist ein HTML-Fragment mit festen Abschnitten:
  `header` → `<section id="<id>-worum">` (Fall + Wegweiser-Tabelle) → `<section id="<id>-kern">` (die Lektion,
  h4 mit `id="<id>-k<n>"`) → `-original` (gelöste IHK-Aufgaben) → `-variante` (Übungen, gleiche Anzahl wie
  Originale) → `-selbstcheck` → `-begriffe` (Karten, zugeklappt) → `-quellen`.
- Zielgruppe: ein Umschüler ohne Vorwissen, der auf Papier Prüfungsaufgaben löst und dann im Kapitel
  nachschlägt. Ton: Lehrer, Alltagswort zuerst, kurze Sätze, kein Fachchinesisch, „Nicht übertreiben“.
- Bauen: `node pruef/bauen-in-bau.js` → `bau/AP1_Lerndatei.html`. Muss „Keine Fehler.“ sagen.
- Endprodukt: `C:\Users\mu.aycetin\Desktop\iCloudDrive\AP1\AP1-Koffer\AP1_Lerndatei.html`.
  Im Koffer liegen genau drei Dateien (Lerndatei, `AP1_Pruefungen_2021-2025.pdf`,
  `AP1_Loesungen_2021-2025.pdf`). Nichts anderes dort ablegen, die PDFs nicht anfassen.
- Regeln stehen in `BAUPLAN.md`; Entscheidungen werden in `ENTSCHEIDUNGEN.md` nur angehängt, nie gelöscht.
  Der bisherige Verlauf steht dort in den Abschnitten W und X. Lies beide, bevor du anfängst.

## 2. Harte Regeln (Prüfskripte erzwingen sie)

- `node pruef/check.js kapitel/<datei> --fragment` muss „Keine Fehler.“ melden. Hinweise sind erlaubt.
  Wichtige Regeln daraus: höchstens 4500 Wörter je Kapitel (Fehler), Richtwert 3500 (Hinweis);
  5–12 Begriffskarten mit genau den Labels „Was es ist / Wo es dir begegnet / Nicht verwechseln mit /
  So fragt die IHK“, in „Was es ist“ ein `<sup class="q">`; Merke-Kästen `<div class="merke" data-art="…">`
  nur mit `Auf einen Blick`, `Merke`, `Typischer Fehler`, `Prüfungsnotiz`, höchstens 5 je Kapitel;
  Klassen-Whitelist; Abbildungen brauchen `role="img"`, `<title id>`, `viewBox="0 0 640 H"`,
  `<figcaption>Abb. <KAP>-<n>: …</figcaption>` fortlaufend im Kapitel.
- Kein Fakt ohne Quelle (`<sup class="q"><a href="#<id>-q<n>">`). Neue Quellen ohne URL sind erlaubt mit
  `<span class="abruf">(nicht online geprüft)</span>`, aber der `data-src`-Schlüssel muss als Zeile in
  `notizen/QUELLEN-A.md` (A-Kapitel) oder `notizen/QUELLEN-B.md` (B-Kapitel) stehen. Zeilenformat dort:
  `| schluessel | kapitel | Typ | Titel | – | nicht online geprüft | 2026-09-09 | Fundstelle |`.
- `node pruef/abnahme.js` muss „Keine Befunde.“ melden (Kam-dran-Zeilen, Quellen-Schlüssel, URLs).
- `python pruef/vorschau.py <id>` rendert ein Kapitel als PNG-Streifen nach `notizen/vorschau/` und prüft
  Textüberlappungen in allen SVGs des Kapitels. Pflicht nach jeder Bildänderung; Ergebnis muss
  „Befunde: Keine Befunde.“ sein.
- `python pruef/wegweiser-bauen.py` nach jeder Änderung an h4-ids, Überschriften oder
  `notizen/WEGWEISER-<id>.json` laufen lassen. Es baut die Wegweiser-Tabellen und die Deep-Links in
  Teil 2 neu und bricht ab, wenn ein Ziel-id nicht existiert.
- Ids (`<id>-k<n>`, `<id>-original-<n>`, `<id>-begriff-…`, `<id>-abb<n>-t`) niemals löschen oder umbenennen.
  Neue Abschnitte bekommen die nächste freie Nummer.
- Das Wort „Sitzt“ (alte Häkchen-Funktion) darf nirgends wieder auftauchen.
- Keine parallelen Agenten, kein Massenlauf über alle Kapitel gleichzeitig. Ein Kapitel nach dem anderen.
- Prüfungsdaten nur aus `notizen/TIPPS-ZUORDNUNG.json` und den Prüfungsnotizen `notizen/20NN-fruehjahr.md`
  bzw. `20NN-herbst.md` (dort steht je Teilaufgabe der Lösungskern der IHK). Nichts erfinden.

SVG-Konventionen (siehe `kapitel/00-kopf.html` ab Zeile 100): nur die Klassen `l` (Linie), `f` (graue Fläche),
`w` (weiße Fläche), `a` (Akzent-Kontur ohne Füllung), `fa` (Akzent-Füllung, kein Text darauf), `d` (gestrichelt),
`g` (Gitter), Text `t2` (klein grau), `tb` (fett), `ta` (Akzent), `mono`, `mitte`, `rechts`;
Pfeilmarker `#pfeil`, `#pfeil-a`, `#pfeil-g`. Breite immer 640. Faustregel Textbreite: 13-px-Text
≈ 6,5 Einheiten je Zeichen, `t2` ≈ 5,8, fett ≈ 6,8. Akzent markiert je Bild genau eine Sache.

Werkzeug-Fallen: Bash-Heredocs mit typografischen Anführungszeichen („“) brechen ab; Skripte deshalb als
Datei schreiben (Python, UTF-8) und ausführen. Umbauten pro Kapitel als ein Python-Skript mit exakten
Ankern (`s.count(anker) == 1` prüfen, sonst abbrechen).

## 3. Die Arbeitsliste, in dieser Reihenfolge

Schritt 0, bevor du irgendetwas änderst: `bau` ist kein Git-Repository. Lege eine Sicherung des
heutigen Stands an, so wie es die früheren Ordner `_sicherung_2026-09-08_*` vormachen:
`mkdir _sicherung_2026-09-09_vorY` und dorthin `kapitel/`, `notizen/`, `pruef/`, `ENTSCHEIDUNGEN.md`,
`STATUS.md` und `AP1_Lerndatei.html` kopieren. Einzelne Dateien holst du bei Bedarf von dort zurück
(`cp _sicherung_2026-09-09_vorY/kapitel/<datei> kapitel/`). Den Sicherungsordner nicht in den Koffer legen.

Jede Nummer ist eine Einheit. Fertig heißt: Abschnitt 4 komplett durchlaufen. Erst dann die nächste.

### Einheit 1 – Überschriften im Kern nach der Sache benennen
In allen 20 Kapiteln jede h4 im Kern prüfen. Überschriften, die wörtlich eine Prüfungsfrage sind
(„Drei Vorteile einer SSD gegenüber einer HDD“, „RAID 0, 1 und 5 erklären und auswählen“,
„Aufgabe der Wärmeleitpaste“), umbenennen in den Namen der Sache („HDD oder SSD“, „RAID: drei Grundideen“,
„Wärmeleitpaste: Luft leitet schlecht“). Nummerierung „1. … 2. …“ beibehalten, wo sie da ist.
Nur den Text der h4 ändern, ids unangetastet. Danach `wegweiser-bauen.py` (die Tabellen übernehmen den
neuen Text automatisch). Abnahme: kein h4 im Kern enthält mehr Operatoren wie „nennen“, „erklären“,
„berechnen“, „begründen“, „zuordnen“ oder Zahlwörter wie „Drei Vorteile“, „Zwei Maßnahmen“.

### Einheit 2 – Wegweiser: erst lernen, dann Lösung
Heute zeigen viele Zeilen der Wegweiser-Tabelle direkt auf „Gelöste Originalaufgabe mit Lösung“.
Ziel: in solchen Zeilen zuerst der Lektionsabschnitt, dann die Lösung.
1. `pruef/wegweiser-bauen.py` erweitern: Jeder Eintrag in `WEGWEISER-<id>.json` darf ein Feld
   `"lektion": "<id>-k<n>"` haben. Steht es, rendert die Zelle „Hier steht es“ zwei Links:
   `Erst lernen: <h4-Text>` und darunter `Dann prüfen: Gelöste Originalaufgabe mit Lösung`.
   Die Deep-Links in Teil 2 (Matrix) zeigen weiterhin auf `ziel`. Skript bleibt idempotent und
   prüft auch `lektion`-ids.
2. Für alle Einträge, deren `ziel` mit `-original-` beginnt (alle 20 JSON-Dateien), das passende
   `lektion` eintragen: der Kern-Abschnitt, der das Verfahren oder die Sache lehrt. Dafür das Kapitel lesen,
   nicht raten.
3. `wegweiser-bauen.py` laufen lassen, ein Kapitel mit `vorschau.py` ansehen (Tabelle darf nicht
   umbrechen bis zur Unlesbarkeit), bauen, abnahme.

### Einheit 3 – „Für die Prüfung reicht“ und Vertiefung zugeklappt
Neue Kastenart einführen: `data-art="Für die Prüfung reicht"`.
1. `pruef/check.js`: die Art in die Whitelist aufnehmen, Obergrenze der Merke-Kästen von 5 auf 6 heben.
   `kapitel/00-kopf.html`: falls die Kästen ihr Etikett aus `data-art` per CSS ziehen, ist nichts weiter
   nötig; sonst Etikett analog zu „Prüfungsnotiz“ ergänzen. Änderung in ENTSCHEIDUNGEN begründen.
2. In jeder Mechanik-Lektion (Reihenfolge: B7 RAID/Sicherungsarten, A1 Subnetting und IPv6,
   A6 Netzplan, A5 Strom, A7 Schreibtischtest, A3 Nutzwert, A4 Einheiten, A2 Kalkulation, A9 ER, A8 UML,
   B2 Verschlüsselung) direkt nach dem Verfahren einen Kasten mit genau drei Sätzen: was man in der
   Prüfung hinschreiben muss, nicht mehr.
3. Mechanik, die über die Prüfung hinausgeht (Parität ausrechnen, Binärrechnung im Detail,
   Formelherleitungen), aus dem Hauptweg in `<details><summary>Vertiefung: …</summary><div class="inhalt">…</div></details>`
   verschieben. Nichts löschen, nur verschieben. Wortzahl beachten (Grenze 4500; B9 4494, B11 4479,
   A7 4476, B4 4470 sind fast voll: dort zuerst bei den Karten „Wo es dir begegnet“ und „So fragt die IHK“
   auf einen Satz kürzen).

### Einheit 4 – Fragekette vor jedem Mechanik-Abschnitt
Vor jeden Verfahrensschritt in den Kapiteln aus Einheit 3 eine Einstiegsfrage, die der Leser mit dem
bisher Gelesenen selbst beantworten kann, Antwort zugeklappt darunter. Muster (ist bereits im Selbstcheck
üblich, keine neuen Klassen nötig):
```
<p><strong>Frage vorab:</strong> Der Chef gibt dir eine zweite Platte. Was machst du damit?</p>
<details><summary>Antwort</summary><div class="inhalt"><p>Spiegeln (RAID 1) oder …</p></div></details>
```
Eine Frage je Abschnitt, ein bis zwei Sätze Antwort. Nicht bei „Das Problem“ und nicht bei
„Rechenweg-Schema“.

### Einheit 5 – Vergleichsbild als Standard
Muster: eine Lage, drei Antworten untereinander, der Schaden eingezeichnet. Beispiel RAID: je Zeile vier
Platten, eine davon mit Akzent „kaputt“, rechts ein Satz, was übrig bleibt. Je Bild eine Zeile pro
Alternative, gleiche Geometrie in jeder Zeile, der Unterschied springt ins Auge.
Kandidaten, in dieser Reihenfolge: B7 Sicherungsarten (Voll/differenziell/inkrementell: was muss ich
zurückspielen, wenn Mittwoch kaputt ist), B2 Verschlüsselung (symmetrisch/asymmetrisch/hybrid: wer hat
welchen Schlüssel, was sieht der Angreifer), B1 Passwortschutz (kurz/lang/lang+2. Faktor: was der Angreifer
schafft), B5 Hub/Switch/Router (ein Paket, drei Geräte, wohin geht es), A6 Verzögerung mit und ohne Puffer
(kritischer Pfad verschiebt sich oder nicht).
Je Bild: neue Abbildung mit nächster freier Nummer (Nummern der folgenden Bilder im Kapitel prüfen!),
`<title>`, Bildunterschrift „Abb. X-n: …“, Text im Kern verweist darauf, `vorschau.py` ohne Befund.
Bestehende Bilder nur ersetzen, wenn sie dasselbe zeigen wollten.

### Einheit 6 – Zuordnen/Nennen-Themen als Tabelle
In B1 (Schutzziele, Malwarearten, BSI-Maßnahmen) und wo sonst reine Zuordnungsthemen als Lektion
geschrieben sind: Tabelle `Maßnahme → Ziel → Warum` und darunter ein Kasten „Typischer Fehler“ mit den
Stolperfallen (Backup ist Verfügbarkeit, nicht Integrität; Verschlüsselung ist Vertraulichkeit, nicht
Verfügbarkeit; Hash ist Integrität). Die IHK-Lösungen aus den Prüfungsnotizen als Zeilen übernehmen,
Quelle je Zeile ist die jeweilige IHK-Prüfung. Bestehende Absätze kürzen statt verdoppeln (B1 hat 3983 Wörter).

### Einheit 7 – Alltagswort zuerst, Fachwort danach
Alle 20 Kapitel durchgehen. Muster gut: „Prüfsumme, heißt Parität“. Muster schlecht:
„Paritätsinformation je Streifen“. Suche nach Substantivketten und Fachwörtern ohne Erklärung beim ersten
Auftreten (Beispiele: Nennleistung, Weisungsbindung, Rechenschaftspflicht, Latenz, Multiplizität,
Kardinalität, Abnahmefähig, Gewährleistungsfrist). Beim ersten Auftreten Alltagswort davor, Fachwort in
Klammern oder mit „heißt“ dahinter. Karten „Was es ist“ ebenso. Nicht die Fachwörter streichen, die IHK
fragt sie ab.

### Einheit 8 – Beispielzahlen entzerren
In Rechenbeispielen Zahlen prüfen, die wie Einheiten oder Aufgabenwerte der Prüfung aussehen (in B7 wurden
„3, 5, 4“ für Terabyte gehalten). Beispiele so wählen, dass sie erkennbar Spielzahlen sind (z. B. 7, 12, 20)
oder die Einheit dazuschreiben. Rechenwege nachrechnen, wenn du Zahlen änderst; Ergebnisse in Bildern und
Text müssen übereinstimmen.

## 4. So schließt du jede Einheit ab (Pflicht, in dieser Reihenfolge)

1. `node pruef/check.js kapitel/<datei> --fragment` für jedes geänderte Kapitel → „Keine Fehler.“
2. `python pruef/wegweiser-bauen.py` (immer, wenn ids, h4-Texte oder JSON berührt wurden).
3. `python pruef/vorschau.py <id>` für jedes Kapitel mit Bildänderung → „Befunde: Keine Befunde.“
   Die PNG-Streifen in `notizen/vorschau/` kurz ansehen: Ist das Bild lesbar, stimmt die Nummer?
4. `node pruef/bauen-in-bau.js` → „Keine Fehler.“; `node pruef/abnahme.js` → „Keine Befunde.“
5. `cp AP1_Lerndatei.html "C:/Users/mu.aycetin/Desktop/iCloudDrive/AP1/AP1-Koffer/AP1_Lerndatei.html"`
   und prüfen, dass der Koffer genau drei Dateien enthält.
6. In `ENTSCHEIDUNGEN.md` unter einer neuen Überschrift
   `# Entscheidungen Y – Lernsitzungs-Ideen umgesetzt (2026-09-09, Codex)` einen Eintrag anhängen:
   was geändert, welche Kapitel, Wortzahlen, was offen blieb. Nur anhängen.
7. In `STATUS.md` eine Zeile `| Y | 2026-09-09 | Einheit <n> fertig: … |` anhängen.
8. Nach jeder fertigen Einheit die geänderten Kapiteldateien zusätzlich nach
   `_sicherung_2026-09-09_vorY/fertig-Y<n>/` kopieren, damit ein Rückweg je Einheit existiert.

Wenn eine Prüfung rot ist: beheben, nicht umgehen. Keine Regel in `check.js` lockern außer der in
Einheit 3 beschriebenen und begründeten.

## 5. Wenn dein Kontingent knapp wird

- Keine neue Einheit anfangen, wenn du sie nicht mehr komplett durch Abschnitt 4 bringst.
- Letzter Eintrag in ENTSCHEIDUNGEN Y: „Reststand“ mit der Liste, welche Einheiten fertig sind,
  welche Kapitel innerhalb einer Einheit noch fehlen, und welche Stolpersteine du gesehen hast.
- Halbfertige Kapiteldatei zurücksetzen: aus dem jüngsten passenden Sicherungsordner zurückkopieren
  (`_sicherung_2026-09-09_vorY/kapitel/<datei>` oder `.../fertig-Y<n>/<datei>`), dann `wegweiser-bauen.py`,
  bauen, abnahme, Koffer.

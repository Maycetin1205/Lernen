# ÜBERGABE · AP1-Lerndatei fertigstellen (Stand 2026-09-08)

Du übernimmst eine laufende Arbeit. Lies diese Datei ganz, dann `bau/notizen/LEHRER-VORLAGE.md` (der verbindliche Auftrag je Kapitel), dann `bau/kapitel/15-a6.html` (das fertige Muster). Arbeitsverzeichnis: `C:\Users\mu.aycetin\Desktop\Lernen\bau`. Alle Pfade unten sind relativ dazu.

## 1. Worum es geht

Der Nutzer ist FISI-Umschüler kurz vor der IHK-Abschlussprüfung Teil 1, Vorwissen null, kann nicht programmieren, ADHS, lernt am Bild und am durchgerechneten Beispiel. Die Datei `AP1_Lerndatei.html` (eine HTML-Datei, 20 Kapitel A1–A9 und B1–B11) soll jedes Thema **wie ein Lehrer von null erklären**: erst das Problem, dann Bausteine, dann Schritt für Schritt mit einem Bild je Schritt, die Regel in einem Satz, Zusammenfassung am Ende, Begriffe erst ganz hinten zum Nachschlagen. „Nicht übertreiben.“ Besonders wichtig sind ihm **Netzplan (A6, fertig)** und **Subnetting (A1, offen)**; schwer fallen ihm außerdem A7 Programmlogik und A9 Datenbanken.

Mit dem Nutzer wird in Klartext gesprochen: kurze Sätze, kein Fachchinesisch, keine Statusprotokolle, keine Werkzeugnamen. Erst sagen, was er davon hat, dann höchstens drei Sätze zum Wie. Zeigen statt behaupten (Render-PNG schicken).

## 2. Was fertig ist

- **Prüfungs-PDF** im Koffer (`Desktop/iCloudDrive/AP1/AP1-Koffer/AP1_Pruefungen_2021-2025.pdf`, 105 Seiten) mit Tipp-Kästen im Korrekturrand. Nicht mehr anfassen.
- **Kapitel A6** (`kapitel/15-a6.html`) im Lehrer-Stil: das Muster. `node pruef/check.js kapitel/15-a6.html --fragment` sagt „Keine Fehler.“, `python pruef/vorschau.py a6` ohne Befund.
- **Werkzeuge:** `pruef/check.js` (Regelprüfer), `pruef/vorschau.py <id>` (rendert ein Kapitel als PNG-Streifen nach `notizen/vorschau/` und misst Textüberlappungen in den Bildern), `pruef/svgcheck.py` (alle Bilder), `pruef/abnahme.js` (Kam-dran gegen MATRIX, URLs, doppelte ids), `pruef/bauen-in-bau.js` (Zusammenbau nach `bau/AP1_Lerndatei.html`).
- **Sicherungen:** alle Kapitel vor dem Umbau in `_sicherung_2026-09-08_kapitel/`. Wenn ein Kapitel halb fertig oder kaputt ist: von dort zurückkopieren und neu machen.

## 3. Was gerade läuft (Stand beim Schreiben dieser Datei)

Neun Opus-Agenten bauen parallel je ein Kapitel um: **A2, A3, A7, A8, A9, B1, B5, B9, B10**. Jeder schreibt am Ende einen Bericht `notizen/LEHRER-<id>.md`. So erkennst du den Zustand:

```
ls notizen/LEHRER-*.md
for f in kapitel/1[1-8]-a*.html kapitel/2*-b*.html kapitel/30-b11.html; do node pruef/check.js "$f" --fragment | head -1; done
```

- Bericht vorhanden und Prüfer sagt „Keine Fehler.“ → Kapitel fertig, nur noch ansehen (`python pruef/vorschau.py <id>`, PNGs anschauen).
- Kein Bericht, Datei aber verändert (Vergleich mit `_sicherung_2026-09-08_kapitel/`) → Agent wurde abgebrochen. Datei zurückkopieren und das Kapitel selbst nach LEHRER-VORLAGE.md umbauen.
- Datei unverändert → Kapitel noch offen.

## 4. Was noch fehlt, in dieser Reihenfolge

1. **A1 Subnetting selbst bauen** (`kapitel/10-a1.html`), nach LEHRER-VORLAGE.md und mit dem Entwurf in Abschnitt 6 unten. Das ist das wichtigste offene Kapitel.
2. **Welle 2:** A4, A5, B2, B3, B4, B6, B7, B8, B11 nach LEHRER-VORLAGE.md umbauen (Hinweise je Kapitel stehen dort in §9). Je Kapitel: Datei lesen, Lektion planen, schreiben, `check.js --fragment` bis „Keine Fehler.“, `vorschau.py` bis ohne Befund, PNGs ansehen, Bericht `notizen/LEHRER-<id>.md`.
3. **Lernpfad** in `kapitel/01-benutzung.html`: ein kurzer Abschnitt „Wenn du bei null anfängst“ mit einer Lesereihenfolge, Grundlagen vor Verfahren: B5 → A1 → B9 → A6 → A2 → A3 → A4 → A5 → A7 → A8 → A9 → B1 → B2 → B3 → B4 → B6 → B7 → B8 → B10 → B11. Nur Links auf vorhandene ids (`#b5` usw.), Klassen nur aus dem System, keine Zeitangaben.
4. **Zusammenbau und Abnahme:**
   ```
   node pruef/bauen-in-bau.js        # muss „Keine Fehler.“ melden (Hinweise zu Wörtern sind erlaubt)
   python pruef/svgcheck.py          # muss „Befunde: 0“ melden
   node pruef/abnahme.js             # darf keine Fehler melden
   ```
   Fehler beheben im betroffenen Kapitel, dann neu bauen.
5. **Sichtprüfung:** drei bis vier Kapitel mit `vorschau.py` rendern und die PNGs ansehen (Bilder sitzen, nichts läuft über Ränder, Reihenfolge ist logisch, Begriffe stehen hinten).
6. **In den Koffer kopieren:** nur `bau/AP1_Lerndatei.html` nach `C:\Users\mu.aycetin\Desktop\iCloudDrive\AP1\AP1-Koffer\AP1_Lerndatei.html`. Im Koffer liegen genau drei Dateien (Lerndatei, Prüfungs-PDF, Lösungs-PDF); nichts anderes dort ablegen, keine Sicherungen.
7. **Protokoll:** in `ENTSCHEIDUNGEN.md` unten einen Abschnitt „Entscheidungen V2 – Lehrer-Umbau alle Kapitel (Datum)“ anhängen (nie etwas löschen): welche Kapitel, Abweichungen, offene Punkte. `STATUS.md` Zeile U auf „abgeschlossen“ setzen.
8. **Dem Nutzer berichten**, in Klartext, höchstens zehn Zeilen, mit zwei oder drei Render-PNGs als Beleg.

## 5. Eiserne Regeln (Kurzfassung, Details in Lernen/BAUPLAN.md §2, §8, §9)

- Keine Aussage ohne Quelle, keine neuen Quellen, keine neuen URLs. Fehlt eine Quelle: Aussage weglassen.
- Alle Zahlen bleiben. Neue Rechenbeispiele nur mit `python -c` nachgerechnet und in `notizen/RECHNUNGEN-<id>.md` protokolliert.
- Alle `id`-Attribute bleiben (Glossar und Navigation verlinken darauf). Die Zeile „Kam dran“ bleibt wörtlich.
- Nur Klassen aus `kapitel/00-kopf.html` (Liste in `check.js`, Variable `erlaubt`). Kein CSS, kein `style` außerhalb von SVG, keine Emojis, kein `<img>`, nichts Externes.
- `00-kopf.html`, `check.js`, `bauen.js`, `MATRIX.md` nicht ändern.
- Kein Ausrufezeichen, kein Geviertstrich (nur „ – “), kein „In diesem Kapitel“, kein „lernst du“, keine Zeitangaben für den Lernenden.
- Kapitel höchstens 4 500 Wörter (Prüferfehler), Richtwert unter 4 000.
- Stolperfalle Shell: Heredocs mit typografischen Anführungszeichen („ “) scheitern in der Bash-Umgebung; längere Skripte als Datei schreiben und ausführen. Mehrere Headless-Edge-Aufrufe gleichzeitig brauchen eigene `--user-data-dir` (vorschau.py macht das schon).

## 6. Entwurf für A1 (Subnetting), fertig geplant, nur noch bauen

Neue Abschnittsfolge wie in A6: Worum es geht → Das Verfahren → So hat die IHK gefragt → Jetzt du → Selbstcheck → Begriffe zum Nachschlagen → Quellen. Originale, Varianten, Selbstcheck, Quellen unverändert übernehmen. Durchgehendes Beispiel: PC mit 192.168.10.75 im Netz /26 (steht schon im Rechenweg-Schema).

Der Kern, jeweils `<h4>` und ein Bild (viewBox 640 breit, Klassen wie in A6):

1. **Das Problem: Wer gehört zu wem?** 45 Rechner, Drucker, Server. Ein PC muss wissen: Ist der Drucker in meinem Netz (direkt hin) oder woanders (über den Router)? Das entscheidet die Maske. Falsche Maske oder falsches Gateway: kein Druck, kein Internet.
2. **Baustein 1: Eine IPv4-Adresse sind 32 Schalter.** Vier Zahlen 0–255, jede 8 Bit. Bild: 192.168.10.75 als vier Kästen, darunter die 32 Bit; die letzte Zahl vergrößert mit den Stellenwerten 128 64 32 16 8 4 2 1 und der Summe 64 + 8 + 2 + 1 = 75. Bits mit 1 gefüllt (Klasse `f`), mit 0 weiß (`w`).
3. **Baustein 2: Die Maske teilt in Netz und Gerät.** Bild: 32 Zellen, die ersten 26 gefüllt (Netzanteil, „die Straße“), 6 weiß (Gerät, „die Hausnummer“), Akzentlinie am Schnitt „/26“; darunter dieselben 32 Zellen als Maske (26 Einsen, 6 Nullen) und die Dezimalform 255.255.255.192 (192 = 128 + 64).
4. **Schritt 1: Hostbits und Blockgröße.** 32 − 26 = 6 Hostbits, 2^6 = 64 Adressen je Netz, Schrittweite 64. Bild: Zahlenstrahl .0 bis .255 in vier Blöcke (.0–.63, .64–.127, .128–.191, .192–.255), Akzentmarke bei .75 „liegt im Block .64 bis .127“.
5. **Schritt 2: Netz-, Host- und Broadcastadresse angeben.** Bild: der Block .64–.127 als Streifen: .64 Netzadresse (alle Gerätebits 0) | .65 bis .126 = 62 nutzbare Geräte | .127 Broadcast (Rundruf, alle Gerätebits 1); Akzentmarke „unser PC .75“. Merke: erste Adresse gehört dem Netz, letzte dem Rundruf, Router bekommt meist die erste nutzbare.
6. **Schritt 3: Maske dezimal schreiben.** Regel 256 − Blockgröße, dann die vorhandene Tabelle /24 bis /30.
7. **Schritt 4: Statische IP-Konfiguration: IP-Adresse, Subnetzmaske, Standardgateway.** Bild: PC und Drucker am Switch, Router mit Innenadresse 192.168.10.65 (= Gateway, „die Tür nach draußen“, Akzent) und Außenadresse vom Provider, Pfeil ins Internet. Regel: gleicher Netzanteil → direkt über den Switch; anderes Netz → ans Gateway. Typischer Fehler: WAN-Adresse des Routers oder Adresse aus einem anderen Netz als Gateway eintragen. Hier auch „letzte nutzbare Adresse“ (Herbst 2025) und „vorletzte nutzbare“ (Frühjahr 2025) als Rechenbeispiel im Text.
8. **Wenn es automatisch geht: DHCP und die Adresse 169.254.122.115 erklären.** Vorhandenes DORA-Bild behalten (Discover, Offer, Request, Acknowledge in Alltagsworten: Wer hat eine Adresse für mich? Hier ist ein Angebot. Das nehme ich. Bestätigt, gilt so lange). Prüfungsnotiz: 169.254.x.x heißt „ich habe keinen DHCP-Server gefunden“ (APIPA), kein Adresskonflikt.
9. **IPv6-Adresse ausschreiben und kürzen.** 128 Bit, acht Blöcke hexadezimal. Zwei Regeln (führende Nullen weg; einmal `::` für Nullblöcke). Vorhandenes Kürzungsbild behalten. Link-Local `fe80::` gibt sich jeder Rechner selbst, gilt nur im eigenen Netz (Prüfungsfrage „Herkunft einer Link-Local-Adresse“).
10. **MAC-Adresse: die Hardware-Nummer.** 48 Bit, sechs Hexpaare, die ersten drei = Hersteller (OUI), `ipconfig /all` zeigt sie. Nur Text, kein eigenes Bild.
11. **Rechenweg-Schema** (vorhanden, behalten). Danach die Merke-Blöcke und zuletzt **Auf einen Blick** (vorhandener Kasten, an das Ende verschoben, plus eine Zeile zum Gateway).

Begriffskarten (acht, ids unverändert) ans Ende, „Was es ist“ in einem Satz Klartext, „Nicht verwechseln mit“ nur echte Verwechslungen (IP gegen MAC, Netzadresse gegen Broadcast, Gateway gegen DNS, private gegen öffentliche Adresse, APIPA gegen statischer Konflikt, Präfix gegen Maske, IPv6-Kürzung: `::` nur einmal).

In den vorhandenen SVGs von A1 die Klasse `klein` durch `t2` ersetzen und bei Akzentlinien (`class="a"`) den Pfeil `url(#pfeil-a)` statt `url(#pfeil)` verwenden. Prüfen mit `node pruef/check.js kapitel/10-a1.html --fragment` und `python pruef/vorschau.py a1`.

## 7. Wenn etwas unklar ist

Die einfachste Variante wählen, in `ENTSCHEIDUNGEN.md` mit einem Satz begründen, weitermachen (BAUPLAN §2 Regel 7). Den Nutzer nur fragen, wenn eine Entscheidung das Ergebnis grundlegend ändert.

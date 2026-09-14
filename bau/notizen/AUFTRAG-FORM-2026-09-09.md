# Auftrag – Textwände in Tabellen und Listen umbauen (Stand 2026-09-09, 15:00 Uhr)

Du arbeitest allein in `Desktop/Lernen/bau`. Kein zweiter Chat schreibt gleichzeitig. Kurze Meldungen, keine Agentenschwärme, wenige Bild-Kontrollen. Der Lernende hat Vorwissen null und lernt am Bild und an der Tabelle, nicht am Absatz.

## Ausgangslage

- Alle 20 Kapitel sind Lektionen von null, jede beginnt mit „Worum es geht“ (Fall) und im Kern mit „Das Problem“ (das Wieso). Das ist fertig und bleibt so.
- Die Wegweiser-Tabelle liegt seit heute in jedem Kapitel zugeklappt in `<details class="wegweiser">` (Skript `pruef/wegweiser-bauen.py`, idempotent). Nicht anfassen.
- **Prototyp ist fertig und abgenommen:** Kapitel B7 (`kapitel/26-b7.html`). Dort sind
  1. der Vergleich JBOD gegen RAID 0 eine Tabelle (Spalten „Frage | JBOD | RAID 0“, letzte Zeile `class="hervor"` für den Schaden),
  2. die drei „Erstens, Zweitens, Drittens“-Absätze (Kern „Externe Sicherungsmedien“, Originallösung, Variantenlösung) nummerierte Listen `<ol>` mit einem Satz davor und dem Restsatz danach.
  Das ist das Muster. Genau so weitermachen.

## Regeln

- Tabellen-Markup wie im Bestand: `<div class="tabelle"><table><caption>…</caption><thead><tr><th>…</th></tr></thead><tbody>…</tbody></table></div>`. Keine neuen Klassen (check.js kennt nur die Liste in Zeile 126). `class="hervor"` für die eine Zeile, auf die es ankommt.
- Ein Vergleich (Vorteil/Nachteil, X gegenüber Y, drei Wege, drei Modelle) wird eine Tabelle: eine Zeile je Frage, eine Spalte je Sache. Ein Ablauf oder eine Aufzählung („Erstens … Zweitens … Drittens“) wird `<ol>`. Ein Satz Einleitung davor bleibt, Quellen-`<sup class="q">` behalten.
- Kein Inhalt geht verloren. Fachwörter, die die IHK abfragt, bleiben stehen (Beispiel: „abnahmefähig“).
- Wortgrenze 4500 je Kapitel (check.js). Eng: B4 4463, B9 4466, A7 4488, B11 4480. Dort Tabellen so knapp wie möglich, Sätze, die die Tabelle ersetzt, ganz löschen. Wortzahl nach jedem Kapitel prüfen.
- h4-ids nicht ändern (Wegweiser und Teil 2 zeigen darauf). Abbildungsnummern nicht ändern.
- Pro Kapitel ein Python-Skript im Scratchpad (Write-Tool, wegen Anführungszeichen), das mit `assert t.count(alt) == 1` ersetzt. Keine globalen Ersetzungen.

## Die Stellen (aus maschineller Suche, alle Absätze geprüft)

Tabellen:
1. **B2** Kern „WPA-PSK gegen WPA-Enterprise“ (zwei Absätze): Tabelle „Frage | WPA-Personal (PSK) | WPA-Enterprise“ mit Zeilen: Nachweis (ein Passwort für alle / eigene Anmeldung je Nutzer, Passwort oder Zertifikat), Wer prüft (Access Point / RADIUS-Server über 802.1X), Mitarbeiter geht (Passwort für alle ändern / nur sein Konto sperren), Reicht für (Gästenetz / Firmennetz). SAE-Satz und Zertifikat-prüfen-Satz als Prosa darunter behalten.
2. **B3** Kern „1. DSGVO und BDSG“, erster Absatz: Tabelle „ | DSGVO | BDSG“ mit Zeilen: Was (EU-Verordnung / deutsches Gesetz), Gilt (seit 25. Mai 2018 unmittelbar in jedem EU-Land / füllt die Stellen mit nationalem Spielraum), Beispiel (Hauptgesetz / ab wie vielen Beschäftigten ein Datenschutzbeauftragter nötig ist, Beschäftigtendaten). Absätze 2 und 3 bleiben.
3. **B4** Kern „8. SATA, M.2 und NVMe“: Absatz 1 → Tabelle „Wort | Was es ist | Bild“ (SATA: Laufwerksanschluss mit Kabel / Landstraße; NVMe: Verfahren über PCIe zum Prozessor / Autobahn; M.2: nur die Bauform, Steckmodul ohne Kabel / kann SATA oder NVMe führen). Absatz 2 (F22 2.5 Vor-/Nachteil) → zweizeilige Tabelle „ | M.2-SSD gegenüber SATA-SSD“. Wortgrenze beachten!
4. **B6** Kern „Eigenentwicklung, Kauf oder Fremdvergabe“: Tabelle „Weg | Vorteil | Nachteil“ (drei Zeilen aus dem Absatz). Letzter Satz („Die IHK will je Weg …“) bleibt als Prosa.
5. **B6** Originallösung Open Source / proprietär (zwei Absätze „Erstens … Zweitens …“): eine Tabelle „ | Open Source | Proprietär“ mit zwei Zeilen „Vorteil 1 / Vorteil 2“.
6. **B9** Kern „Wasserfall, V-Modell, iterativ“: Tabelle „Modell | Passt, wenn | Schwäche / Antwort darauf“ (drei Zeilen). Verweis auf Abb. B9-4 behalten.
7. **B9** Kern „Stakeholder und das Team“, Absatz „Ein externer Projektberater“: zweispaltige Tabelle „Vorteile | Nachteile“ (4 gegen 6 Nennungen, leere Zellen erlaubt). Satz „Fünf Punkte für fünf Nennungen …“ bleibt. Wortgrenze beachten!

Listen (`<ol>`):
8. **B2** Originallösung „Erstens erhält der Anwalt … Viertens …“ → vier Schritte, letzter Satz als Prosa danach.
9. **B4** Kern „Das Problem“, Absatz „Passen heißt dreierlei“ → drei Punkte (Form, Verfahren, Verbund), fett das Stichwort.
10. **B4** Originallösung SSD gegenüber HDD „Erstens … Drittens …“ → drei Punkte.
11. **B5** Originallösung „Erstens den Rechner … Fünftens …“ → fünf Schritte (`<code>ping 192.168.20.1</code>` behalten).
12. **B8** Originallösungen: drei Absätze mit „Erstens … Zweitens …“ (Energie/Material; Ergonomie/Anschlüsse; Bildschirm/Tastatur) → je `<ol>` mit zwei Punkten, der Satz „Weitere anerkannte …“ / „Die Lösungshinweise nennen …“ / „Ebenfalls anerkannt …“ als Prosa danach.
13. **B8** Variantenlösungen: zwei Absätze ebenso.

Zwei offene Punkte aus der Gegenprüfung (ENTSCHEIDUNGEN Y, „Was offen bleibt“), jetzt entschieden:
14. **A2** Begriffskarten, Feld „Was es ist“ (7 Karten): in Klartext umschreiben, ein Satz, Alltagswort zuerst, Fachwort danach, Paragraphen weg. Beispiel: Abschreibung → „Ein Gerät verliert jedes Jahr an Wert; die Abschreibung verteilt den Kaufpreis als Kosten über die Jahre, in denen es genutzt wird.“ Quellen-`<sup>` behalten. A2 hat Platz.
15. **B5** Abb. B5-8: Der Text davor sagt „stellt die drei an dasselbe Paket“, das Bild zeigt beim Router aber ein Ziel im anderen Netz (Port 4). Fix: den Satz davor ändern in „Abb. B5-8 zeigt die drei nebeneinander; beim Router liegt das Ziel in einem anderen Netz, sonst hätte er nichts zu tun.“ und die figcaption in „Abb. B5-8: Drei Geräte, je ein Paket an Port 1. Beim Hub und Switch sitzt das Ziel im eigenen Netz (Port 3), beim Router in einem anderen Netz (Port 4). Der Akzent zeigt, was der Hub zu viel tut.“ Das SVG selbst nicht ändern.

## Ablauf je Kapitel

`node pruef/check.js kapitel/<datei> --fragment` (muss „Keine Fehler.“ sagen, Wortzahl lesen) → nur bei Bildänderung `python pruef/vorschau.py <id>` → nach allen Kapiteln `node pruef/bauen-in-bau.js` („Keine Fehler.“; die Hinweise „a8: 4 Original-Aufgaben“ und „Tages-/Wochenplan“ sind alt und bleiben) → `node pruef/abnahme.js` („Keine Befunde.“) → `AP1_Lerndatei.html` nach `Desktop/iCloudDrive/AP1/AP1-Koffer/` kopieren (dort genau drei Dateien, nichts anderes ablegen).

Vorher Sicherung: `kapitel/` nach `_sicherung_2026-09-09_vorAA/` kopieren. Protokoll in `ENTSCHEIDUNGEN.md` als neuer Abschnitt „# Entscheidungen AA – Textwände zu Tabellen und Listen (2026-09-09, Opus)“, eine Zeile je Stelle, plus eine Zeile in `STATUS.md`. Kein Kapitel halbfertig lassen; wenn das Kontingent knapp wird, letzten Eintrag „Reststand“ mit den offenen Nummern schreiben.

Am Ende dem Nutzer in fünf Sätzen sagen: was umgebaut wurde, welche Nummern offen sind, Wortzahlen der engen Kapitel, ob Bau, Abnahme und Koffer grün sind.

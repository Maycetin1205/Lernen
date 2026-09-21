# Abarbeitungsplan: alle Kapitel wirklich von null (ab 2026-09-16)

Regeln stehen in `AUFTRAG-OPUS-2026-09-16.md`. Diese Datei ist die Liste, die abgehakt wird.
Der Lernende hat entschieden: **kein Zwischenurteil, keine Rückfrage.** Alle Kapitel nacheinander abarbeiten, bis jede Zeile `fertig` ist.

## So wird gearbeitet

1. Diese Datei lesen. Das erste Kapitel mit Stand `offen` ist das nächste. Nie zwei gleichzeitig.
2. Vorher Sicherung: Kapiteldatei nach `bau/_sicherung_2026-09-16_vonnull/` kopieren (Ordner anlegen, falls er fehlt).
3. Kapitel nach den neun Regeln des Auftrags neu bauen. Muster: `kapitel/10-a1.html` (Abschnitt AI in ENTSCHEIDUNGEN.md beschreibt, was dort warum geändert wurde).
4. Selbsttest: jede Aufgabe aus `notizen/WEGWEISER-<kap>.json` allein mit dem Kapiteltext lösen. Lücke gefunden = Absatz ergänzen, nicht notieren und weitergehen.
5. Prüfen und bauen, in dieser Reihenfolge, jede Stufe muss grün sein, sonst reparieren:
   `node pruef/check.js kapitel/<datei> --fragment` → `python pruef/wegweiser-bauen.py` → `python pruef/vorschau.py <kap>` (nur Bilder mit Befund ansehen) → `node pruef/bauen-in-bau.js` (muss "Keine Fehler." sagen) → `node pruef/abnahme.js`.
   Schlägt die Wortgrenze an: in `pruef/check.js` (`const grenze`) für dieses Kapitel anheben, Begründung in den ENTSCHEIDUNGEN-Eintrag.
6. Kopieren: `bau/AP1_Lerndatei.html` nach `Desktop/Lernen/AP1_Lerndatei.html` und `Desktop/iCloudDrive/AP1/AP1-Koffer/AP1_Lerndatei.html`. Hash vergleichen.
7. Eintragen: ENTSCHEIDUNGEN.md (Abschnitt AI fortschreiben, je Kapitel ein Absatz: Befund vorher, was neu ist, verschobene ids, Selbsttest-Lücken), STATUS.md eine Zeile, und **hier den Stand auf `fertig` setzen** mit Datum.
8. Dem Lernenden drei Sätze melden (was neu, wo, was er tun soll). Nicht auf Antwort warten, direkt mit dem nächsten Kapitel weitermachen.
9. Nach einer Zusammenfassung der Sitzung: zuerst diese Datei lesen, nicht aus dem Gedächtnis weiterarbeiten.

## Was ein Kapitel "von null" mindestens braucht

- Erste Abschnitte erklären die Welt, in der das Thema spielt (Was ist ein Netz, was ist eine Datenbank, was ist ein Programm, was ist ein Angebot), bevor ein einziges Fachwort ohne Erklärung fällt.
- Rechenwege als `pre.rechenweg` mit Einheiten in jeder Zeile, Zwischenergebnis sichtbar.
- Grundlagen, die mehrere Kapitel brauchen, gehören dorthin, wo sie zuerst gebraucht werden, mit einem Satz Verweis aus den anderen Kapiteln (Beispiel: Binär und Hexadezimal stehen in A1; Zweierpotenzen und 1.024 in A4; Prozentrechnung in A2).
- Begriffskarten am Ende: für jedes neu eingeführte Wort eine Karte, höchstens 12.

## Reihenfolge und Stand

| Nr | Kapitel | Datei | Thema | Aufgaben | Stand |
|---|---|---|---|---|---|
| 1 | A1 | kapitel/10-a1.html | Netz, IPv4, Binär, Hex, Subnetting, IPv6, MAC | 18 | fertig 2026-09-16 (Abschnitt AI) |
| 2 | A4 | kapitel/13-a4.html | Datenmengen, Einheiten, Übertragungszeit, Speicherbedarf | 12 | fertig 2026-09-16 (Abschnitt AI.2) |
| 3 | A2 | kapitel/11-a2.html | Kosten, Angebote, Prozent, Gewinnschwelle | 16 | fertig 2026-09-16 (Abschnitt AI.3) |
| 4 | A9 | kapitel/18-a9.html | Datenbank, Tabellen, Schlüssel, SQL | 17 | fertig 2026-09-16 (Abschnitt AI.4) |
| 5 | A7 | kapitel/16-a7.html | Programmlogik, Pseudocode, Struktogramm, PAP | 12 | fertig 2026-09-16 (Abschnitt AI.5) |
| 6 | A3 | kapitel/12-a3.html | Nutzwertanalyse | 8 | fertig 2026-09-16 (Abschnitt AI.6) |
| 7 | A5 | kapitel/14-a5.html | Strom und Energiekosten | 7 | fertig 2026-09-16 (AI.7, geprueft ohne Aenderung) |
| 8 | A6 | kapitel/15-a6.html | Netzplan, Gantt | 9 | fertig 2026-09-16 (Abschnitt AI.8) |
| 9 | A8 | kapitel/17-a8.html | UML-Diagramme | 4 | fertig 2026-09-16 (AI.9, geprueft ohne Aenderung) |
| 10 | B5 | kapitel/24-b5.html | Netzbetrieb, Dienste, Cloud | 13 | fertig 2026-09-16 (Abschnitt AI.10) |
| 11 | B1 | kapitel/20-b1.html | Schutzziele, IT-Sicherheit | 30 | fertig 2026-09-16 (AI.11, geprueft ohne Aenderung) |
| 12 | B9 | kapitel/28-b9.html | Projekt | 13 | fertig 2026-09-16 (AI.12, geprueft ohne Aenderung) |
| 13 | B7 | kapitel/26-b7.html | Datensicherung, RAID | 7 | fertig 2026-09-16 (AI.13, geprueft ohne Aenderung) |
| 14 | B2 | kapitel/21-b2.html | Verschluesselung und sichere Verbindungen | 13 | fertig 2026-09-16 (AI.14, geprueft ohne Aenderung) |
| 15 | B3 | kapitel/22-b3.html | Datenschutz | 6 | fertig 2026-09-16 (AI.15, geprueft ohne Aenderung) |
| 16 | B4 | kapitel/23-b4.html | Hardware, Schnittstellen | 17 | fertig 2026-09-16 (AI.16, geprueft ohne Aenderung) |
| 17 | B6 | kapitel/25-b6.html | Software, Lizenzen | 8 | fertig 2026-09-16 (AI.17, geprueft ohne Aenderung) |
| 18 | B8 | kapitel/27-b8.html | Ergonomie, Nachhaltigkeit | 6 | fertig 2026-09-16 (AI.18, geprueft ohne Aenderung) |
| 19 | B10 | kapitel/29-b10.html | Kommunikation, Service | 16 | fertig 2026-09-16 (AI.19, geprueft ohne Aenderung) |
| 20 | B11 | kapitel/30-b11.html | Vertraege, Kaufmaennisches | 20 | fertig 2026-09-16 (AI.20, geprueft ohne Aenderung) |

Zeilen mit "(Thema laut Kapitelkopf)": Thema aus der h2 der Datei nehmen und hier eintragen, wenn das Kapitel drankommt.

## Wenn etwas hakt

- Ein Prüfskript bricht: Ursache im Skript oder Kapitel beheben, nicht das Skript umgehen. Ausnahme Wortgrenze, siehe Schritt 5.
- Ein Bild überlappt (svgcheck-Befund): Bild korrigieren, Vorschau erneut, dann weiter.
- Etwas ist unklar und nicht aus Auftrag, Kapitel oder ENTSCHEIDUNGEN zu klären: die sinnvollste Lesart wählen, im ENTSCHEIDUNGEN-Eintrag als Annahme benennen, weitermachen. Nicht fragen.

## Nachtrag AJ, 2026-09-16 abends: Aufgaben im Lernabschnitt anbinden

Messung mit dem Skript im Scratchpad (Kennung wie "H22 3.7" im Text des Lernabschnitts):
vorher 76 von 252, jetzt 252 von 252. Damit ist auch der Nachtrag abgeschlossen.

| Bereich | Aufgaben | angebunden | Stand |
|---|---|---|---|
| A1 bis A9 | 103 | 103 | fertig 2026-09-16 |
| B1 bis B11 | 149 | 149 | fertig 2026-09-16 |


So wird angebunden: bei Rechenaufgaben ein pre.rechenweg mit den Zahlen der Aufgabe, bei
Erklaeraufgaben ein Absatz mit der geforderten Antwortform und Punktzahl, bei Zeichenaufgaben
der Weg in Schritten plus Verweis auf die geloeste Originalaufgabe. Nicht die Kennung allein
einstreuen; das waere Zaehlerkosmetik ohne Nutzen.

Achtung bei B4, B7, B9 und B11: alle dicht an der Wortgrenze 4500, dort vor dem Ergaenzen
die Grenze anheben und in ENTSCHEIDUNGEN begruenden.


# Auftrag an Opus, 2026-09-16: Kapitel wirklich von null

## Wer liest das Ergebnis

Ein FISI-Umschüler kurz vor der AP1. Vorwissen: keins. Er kennt weder Bit, Router, Switch, Datenbank noch Pseudocode. Er lernt auf Papier, mit Bild und einem durchgerechneten Beispiel. Definitionen vor der Erklärung sind für ihn wertlos. Er springt bei Textwänden ab (ADHS). Er ist dünnhäutig und hat wenig Token-Kontingent: kurz antworten, liefern, keine Berichte, keine Agentenschwärme.

## Was er will (wörtlich sinngemäß)

"Ich muss das wirklich von 0 auf verstehen. Kapitel, die nicht gezielt auf die Aufgabe sind, sondern so gut, dass ich einfach die jeweiligen Aufgaben lösen kann."

Also: nicht 252 Musterlösungen (die stehen schon drin, Abschnitt `<kap>-geloest`), sondern Kapitel, nach deren Lektüre er eine unbekannte Aufgabe zum Thema selbst löst.

## Woran die bisherigen drei Umbauten gescheitert sind

Die Kapitel heißen "Lektion von null", setzen aber Wörter voraus, die er nicht hat (Präfix, Oktett, Gateway, Datensatz, Variable, Schleife), springen nach zwei Bausteinen ins Rechnen und erklären das Warum in einem Halbsatz. Er hat F22 4.5 mit dem Kapitel nicht lösen können, weil drei Zwischenschritte fehlten (Upload statt Download, MiByte = 1.024 · 1.024, Mbit/s · 1.000.000). Dieser Fehler steckt vermutlich in jedem Kapitel: Der Autor kannte das Thema und hat Schritte übersprungen, die für ihn selbstverständlich waren.

## Regeln für jedes Kapitel

1. **Nullpunkt prüfen.** Vor dem Schreiben: Liste jedes Fachwort im Kapitel. Jedes Wort wird an seiner ersten Stelle mit einem Alltagsvergleich eingeführt, bevor es benutzt wird. Kein Wort darf früher vorkommen als seine Erklärung. Begriffskarten am Ende bleiben als Nachschlagteil.
2. **Ein durchgehendes Beispiel** von vorn bis hinten (ein Netz, eine Firma, eine Tabelle, ein Programm). Keine wechselnden Zahlen.
3. **Jeder Schritt ein Bild** mit genau den Zahlen dieses Schritts, plus der Satz, was man tut und warum. Erst das Bild, dann die Regel in einem Satz.
4. **Kein Schritt übersprungen.** Testfrage an jeder Rechenzeile: "Weiß jemand, der das Wort gerade zum ersten Mal gelesen hat, woher diese Zahl kommt?" Wenn nein, eine Zeile einfügen.
5. **Warum vor Wie.** Erst, welches Problem der Mechanismus löst (Wer gehört zu wem? Warum trennt man Netze? Warum eine zweite Tabelle?), dann das Verfahren.
6. **Fallen benennen**, jeweils an der Stelle, an der sie passieren (Download statt Upload, 1.024 statt 1.000, Broadcast als Host gezählt, JOIN ohne Bedingung).
7. **Abschluss-Test durch dich selbst:** Nimm jede Prüfungsaufgabe des Kapitels aus dem Wegweiser (`notizen/WEGWEISER-<kap>.json`) und löse sie allein mit dem Kapiteltext, so als hättest du nur das Kapitel. Fehlt dir eine Information, gehört sie ins Kapitel. Notiere je Aufgabe in einer Zeile, welcher Absatz sie trägt. Erst wenn alle Aufgaben durchgehen, ist das Kapitel fertig.
8. **Länge ist zweitrangig.** Wenn `pruef/check.js` (Zeile 130, `const grenze`) wegen der Wortzahl anschlägt, Grenze für dieses Kapitel anheben und in ENTSCHEIDUNGEN.md begründen. Der Lernende hat Verständlichkeit vor Kürze gestellt. Textwände vermeiden trotzdem: kurze Absätze, Bild, Absatz, Bild.
9. Alten Katalogtext ("So hat die IHK gefragt") verschieben, nicht löschen. Abschnitt `<kap>-geloest`, Wegweiser-Tabelle und Selbstcheck bleiben; ids `<kap>-k<n>` erhalten oder in `notizen/WEGWEISER-<kap>.json` nachziehen.

## Reihenfolge

A1 ist fertig (2026-09-16, Abschnitt AI). **Entscheidung des Lernenden vom selben Tag: kein Zwischenurteil, alle Kapitel ohne Rückfrage nacheinander abarbeiten.** Liste und Stand: `notizen/PLAN-ABARBEITEN.md`. Reihenfolge: A4 (Übertragung, Speicher), A2 (Kosten, Angebote), A9 (SQL, Datenbank), A7 (Pseudocode, Struktogramm), dann A3, A5, A6, A8, dann B5, B1, B9, B7, B2, B3, B4, B6, B8, B10, B11. Ein Kapitel pro Durchgang, kein Kapitel parallel.

## Arbeitsweise, die funktioniert hat

- Pro Kapitel ein Python-Skript im Scratchpad, **per Write-Tool ablegen** (das Bash-Werkzeug frisst Backslashes und scheitert an Heredocs mit Sonderzeichen). Zeilenenden der Kapiteldatei beibehalten (LF, nicht CRLF).
- Reihenfolge je Kapitel: Sicherungskopie → schreiben → `node pruef/check.js` → `python pruef/wegweiser-bauen.py` → `python pruef/vorschau.py <kap>` (Bilder ansehen, wenige) → `node pruef/bauen-in-bau.js` (muss "Keine Fehler." sagen) → `node pruef/abnahme.js` → Kopien: `Desktop/Lernen/AP1_Lerndatei.html` (die öffnet er) und `Desktop/iCloudDrive/AP1/AP1-Koffer/AP1_Lerndatei.html` (dort nur drei Dateien, nichts anderes ablegen) → Eintrag in ENTSCHEIDUNGEN.md (neuer Abschnitt AI) und STATUS.md.
- Globale Ersetzungen nie ohne Abgrenzung gegen `class=` (ein Skript hat mal `klein` → `t2` im Fließtext ersetzt).
- Abbildungsnummern kollidieren mit den Bildern in den Aufgabenteilen: nach Umnummerierung alle Verweise im Kapitel prüfen. `pruef/svgcheck.py` prüft Textüberlappung in den Bildern.
- Muster für einen gelungenen Abschnitt: `kapitel/13-a4.html`, Abschnitt `a4-k5` (fünf Schritte, Rechenweg mit Einheiten, Falle, Bild A4-4).

## Meldungen an den Lernenden

Klartext, keine Fachbegriffe ohne Erklärung, kein Bericht. Drei Sätze: was neu ist, wo er es findet, was er tun soll (lesen, sagen ob es sitzt). Bei "versteh ich nicht": eine Frage tiefer nachfragen, nicht neu erklären.

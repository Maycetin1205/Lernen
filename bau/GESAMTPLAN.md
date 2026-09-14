# Gesamtplan AP1-Lerndatei (Stand 2026-09-09)

Eine Seite für jeden, der einsteigt: Ziel, was fertig ist, was als Nächstes kommt, was geparkt ist, wo die Regeln stehen.

## Ziel

Eine einzige HTML-Datei (`AP1_Lerndatei.html`), mit der ein Umschüler ohne Vorwissen die AP1 „Einrichten eines
IT-gestützten Arbeitsplatzes“ lernen kann: 20 Kapitel (A1–A9 Verfahren, B1–B11 Erklären), jedes eine Lektion von
null, jede Aussage mit Quelle, jede Prüfungsaufgabe 2021–2025 einem Absatz zugeordnet. Dazu die Prüfungs-PDF mit
Tipp-Kästen und die Lösungs-PDF. Alles drei liegt im Koffer `Desktop/iCloudDrive/AP1/AP1-Koffer` (genau drei Dateien).

## Fertig (Reihenfolge der Phasen, Details in STATUS.md und ENTSCHEIDUNGEN.md)

| Phase | Was | Wann |
|---|---|---|
| E1–E3 | Alle 9 Prüfungen extrahiert: 252 Teilaufgaben mit IHK-Lösungskern (`notizen/20NN-*.md`) | bis 2026-09-03 |
| Q-A, Q-B | 133 Quellen geprüft (`notizen/QUELLEN-A.md`, `QUELLEN-B.md`) | 2026-09-03 |
| M, K-1…K-5, V, Z, F | Matrix, 20 Kapitel, Verfahrensblatt, Zusammenbau, fachliche Gegenprüfung | bis 2026-09-07 |
| L | Grafiken statt Textwüste (123 SVG-Abbildungen, svgcheck) | 2026-09-07 |
| T | Tipp-Kästen in der Prüfungs-PDF, leere Seiten raus | 2026-09-08 |
| U, V2 | Lehrer-Stil: Lektion von null, Begriffskarten ans Ende | 2026-09-08 |
| W | Begriffe zugeklappt, Wegweiser Aufgabe → Absatz (alle 252 Aufgaben), „Sitzt“ entfernt | 2026-09-08 |
| X | 14 schwache Kapitel von Hand als Lektion nachgezogen, alle Inhaltslücken geschlossen | 2026-09-09 |

## Als Nächstes: Phase Y (Auftrag für Codex)

Acht Verbesserungen aus der Lernsitzung RAID, als Einheiten 1–8 in `notizen/AUFTRAG-CODEX-2026-09-09.md`:
1 Überschriften nach der Sache · 2 Wegweiser erst Lektion, dann Lösung · 3 Kasten „Für die Prüfung reicht“ +
Vertiefung zugeklappt · 4 Fragekette · 5 Vergleichsbilder (B7, B2, B1, B5, A6) · 6 Zuordnen-Themen als Tabelle ·
7 Alltagswort zuerst · 8 Beispielzahlen entzerren. Protokoll in ENTSCHEIDUNGEN unter „Y“.

## Geparkt (nur auf Zuruf)

- Kontrastanhebung blasser Scan-Seiten in der Prüfungs-PDF (S. 24, 29, 74).
- Abgleich mit der Fremd-Zusammenfassung unter `Desktop/Projekte/Porjekte/AP1/Lerndateien/Informationen`.
- Altlasten in `bau/` (`pruef/k2-*.js`, `k3-*.js`, `pruef/erstelle-a5.py`, `K2-/K3-vorschau.html`): nicht löschen ohne Freigabe.
- Wortgrenze 4500 fast erreicht bei B9 (4494), B11 (4479), A7 (4476), B4 (4470): vor Ergänzungen dort Karten kürzen.

## Wo was steht

- Regeln: `BAUPLAN.md`. Prüfskripte: `pruef/check.js`, `pruef/abnahme.js`, `pruef/vorschau.py`, `pruef/svgcheck.py`,
  `pruef/wegweiser-bauen.py`. Bauen: `node pruef/bauen-in-bau.js`.
- Verlauf und Begründungen: `ENTSCHEIDUNGEN.md` (nur anhängen). Phasenübersicht: `STATUS.md`.
- Aufgaben → Kapitel: `notizen/TIPPS-ZUORDNUNG.json`; Aufgabe → Absatz: `notizen/WEGWEISER-<id>.json`.
- Sicherungen: Ordner `_sicherung_<datum>_*` (kein Git).

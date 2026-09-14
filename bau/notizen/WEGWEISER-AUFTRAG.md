# WEGWEISER-AUFTRAG · Von der Prüfungsaufgabe zum richtigen Absatz (2026-09-08)

## Warum

Der Lernende löst eine Originalprüfung auf Papier. Am Rand der Prüfungs-PDF steht bei jeder Aufgabe, in welchem Kapitel die Antwort steht, zum Beispiel „c) » B7 Datensicherung/RAID“. Er springt ins Kapitel und findet dann nichts, weil er nicht weiß, in welchem Absatz die Sache steht. Er soll künftig von jeder Teilaufgabe mit einem Klick genau in den Absatz kommen, der sie beantwortet.

## Was du lieferst

Eine Datei `bau/notizen/WEGWEISER-<id>.json` (id klein, z. B. `b7`) mit einer Liste. Je Teilaufgabe des Kapitels ein Eintrag:

```json
[
  {"pruefung": "H21", "nr": "3.6", "ziel": "b7-original-1", "hinweis": ""},
  {"pruefung": "H22", "nr": "2.4", "ziel": "b7-k3", "hinweis": ""},
  {"pruefung": "H22", "nr": "2.5", "ziel": "b7-k3", "hinweis": "JBOD wird im Absatz nur in einem Satz erwähnt"}
]
```

Dazu drei Zeilen Klartext in `bau/notizen/WEGWEISER-<id>.md`: Anzahl der Aufgaben, wie viele auf eine gelöste Originalaufgabe zeigen, welche Lücken du gefunden hast (Aufgaben, zu denen im Kapitel nichts oder zu wenig steht).

## Woher die Aufgaben kommen

`bau/notizen/TIPPS-ZUORDNUNG.json` enthält alle 252 Teilaufgaben mit den Feldern `pruefung` (H21, F22, H22, F23, H23, F24, H24, F25, H25), `nr` (z. B. 3.6), `titel` (Kurzfassung der Aufgabe) und `kapitel` (z. B. B7). Nimm genau die Einträge mit deinem Kapitel. Die vollständige Aufgabenbeschreibung steht in `bau/notizen/<jahr>-<saison>.md` (z. B. `2021-herbst.md`) unter `### 3.6 | …`. Lies sie, wenn der Kurztitel nicht reicht.

## Wohin die Ziele zeigen dürfen

Nur auf ids, die in deiner Kapiteldatei `bau/kapitel/<NN>-<id>.html` existieren:

1. **Bevorzugt:** die gelöste Originalaufgabe, wenn die Teilaufgabe dort sinngemäß wiedergegeben ist. Die Artikel heißen `<id>-original-1`, `-2`, `-3`; die Zeile `<p class="herkunft">AP1 Herbst 2021, Aufgabe 3.6, …</p>` sagt dir, welche Prüfung und Nummer gemeint ist. Achtung: Die Herkunftszeile nennt die Nummer der Lerndatei (z. B. 3.6), dieselbe wie in TIPPS-ZUORDNUNG.json.
2. **Sonst:** die Zwischenüberschrift im Kern, unter der die Antwort steht. Jede Zwischenüberschrift hat eine id `<id>-k1`, `<id>-k2`, … (`<h4 id="b7-k3">RAID 0, 1 und 5 erklären und auswählen</h4>`). Wähle den Absatz, der die Frage tatsächlich beantwortet, nicht den, der nur das Wort enthält.
3. Passt nichts: nimm die am nächsten liegende Zwischenüberschrift und schreib in `hinweis`, was fehlt. Erfinde keine ids.

## Regeln

- Du veränderst **keine** Kapiteldatei und keine andere Datei. Du schreibst nur die zwei Dateien `WEGWEISER-<id>.json` und `WEGWEISER-<id>.md`.
- Jede Teilaufgabe deines Kapitels bekommt genau einen Eintrag. Vollständigkeit prüfen: Anzahl der Einträge = Anzahl der Einträge mit deinem Kapitel in TIPPS-ZUORDNUNG.json.
- `ziel` muss wörtlich als `id="…"` in der Kapiteldatei vorkommen. Prüfe das mit grep, bevor du abgibst.
- Gültiges JSON, UTF-8, keine Kommentare.

## Abgabe

Antworte mit höchstens fünf Zeilen: Kapitel, Anzahl Einträge, davon auf Originale, Lücken.

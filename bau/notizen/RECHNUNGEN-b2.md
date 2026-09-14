# K-3 · B2 · Rechenprüfung 2026-09-03

Vor dem Schreiben der Lösungen mit Node ausgeführt:

```js
console.log('SHA-256: 64 * 4 =',64*4);
```

Ausgabe: `SHA-256: 64 * 4 = 256`.

Die 64 Hexadezimalstellen entsprechen 256 Bit. Der aus F25 2.7 übernommene Referenzhash hat 64 Stellen. Ohne die damalige ausführbare Datei wird kein tatsächlicher Downloadhash behauptet. Originalaufgaben und Varianten prüfen Abläufe; weitere Sachrechnungen fallen nicht an.

## Kontrolle 2026-09-06

Geprüft: 3 Originalaufgaben (H25 3.9, F25 2.3, F25 2.7) und 3 Varianten.

- Punktzahlen 4 P, 4 P, 4 P gegen `notizen/2025-herbst.md` und `notizen/2025-fruehjahr.md` bestätigt; die Punkteabsätze geben die Aufteilung so wieder wie die Notizen (H25 3.9 ohne amtliche Teilaufteilung, F25 2.3 je Schritt ein abgeleiteter Punkt, F25 2.7 drei bis vier Aussagen).
- Zahlen geprüft: der Referenzhash aus F25 2.7 Zeichen für Zeichen gegen die Notiz abgeglichen, 33 + 31 = 64 Hexstellen über den `<wbr>`-Umbruch hinweg, also 64 × 4 = 256 Bit; SSH-Standardport 22 gegen `rfc-4251` beziehungsweise die Porttabelle aus F25 4.5.

### Gefundener Fehler und Korrektur

b2-original-1 (H25 3.9): Der Lösungskern der Notiz ordnet die geprüfte Signatur ausdrücklich der Herkunftsprüfung beziehungsweise Authentizität **und** der Erkennung einer Änderung beziehungsweise Integrität zu. Im Fragment war nur die Änderungserkennung benannt, das Schutzziel Authentizität fehlte.

- alt: „Eine passende Signatur belegt die Bindung an diesen Schlüssel und macht Änderungen erkennbar.“
- neu: „Eine passende Signatur belegt die Bindung an diesen Schlüssel, damit die Herkunft der Daten (Authentizität), und macht nachträgliche Änderungen erkennbar (Integrität).“
- Danach `node pruef/check.js kapitel/21-b2.html --fragment`: „Keine Fehler.“

### Übrige Prüfpunkte

- H25 3.9 sonst vollständig: Hashbildung, Signieren mit dem privaten Schlüssel der Apotheke, Übertragung, Prüfung mit dem öffentlichen Schlüssel der Apotheke. Die Warnung der Notiz, nicht den öffentlichen Schlüssel des Rechenzentrums zu wählen, ist durch die Formulierung eingehalten.
- F25 2.3: alle vier Schritte des Lösungskerns vorhanden, jeder Schlüssel mit Besitzer benannt.
- F25 2.7: Zweck, eigene Berechnung, vollständiger Vergleich und Umgang mit einer Abweichung – vier Aussagen wie im Lösungskern.
- Varianten unabhängig beantwortet und verglichen: signiertes Herstellerupdate, vier Schritte Bewerberin und Personalabteilung, abweichender Hash bei `backup-agent.msi` – fachlich richtig und jeweils dieselbe Sache wie das Original.

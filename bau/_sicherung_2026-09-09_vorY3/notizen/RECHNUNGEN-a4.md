# A4 · Einheiten, Speicherbedarf und Datenrate · Nachrechnung

Datei war zuvor nicht vorhanden und wurde bei der Lösungskontrolle angelegt.

## Kontrolle 2026-09-06

Werkzeug: Node v25, Wegwerfskripte `rechnung.js` und `varianten.js` im Sitzungs-Scratchpad (nicht im Projekt).
Geprüft: `kapitel/13-a4.html`, Abschnitte `a4-original-1`, `a4-original-2`, `a4-variante-1`, `a4-variante-2`.
Amtliche Grundlage: `notizen/2025-herbst.md` Abschnitt 2.4 und `notizen/2024-fruehjahr.md` Abschnitt 4.7.
Konvention: 1 kB = 1.000 Byte, 1 KiB = 1.024 Byte, 1 MiB = 1.024 KiB, 1 GiB = 1.024 MiB.

### Eingabe und Befehl

```
console.log('H25 2.4 Rechnungen/Tag', 24*14);
console.log('H25 2.4 Byte', 336*124*1000);
console.log('H25 2.4 KiB', 336*124*1000/1024, Math.round(336*124*1000/1024));

console.log('F24 4.7 Byte', 2**30, 'Bit', 2**30*8, 'Rate', 50.02*1e6);
console.log('F24 4.7 Dauer', 2**30*8/(50.02*1e6), Math.ceil(2**30*8/(50.02*1e6)));
console.log('F24 4.7 min:s', Math.floor(172/60)+':'+(172%60));

console.log('Var1 Vorgaenge', 24*18, 'Byte', 24*18*86*1000);
console.log('Var1 KiB', 24*18*86*1000/1024, Math.round(24*18*86*1000/1024));
console.log('Var1 30 Tage MiB', 36281*30/1024, Math.round(36281*30/1024*100)/100);
console.log('Var1 ungerundet   ', 36281.25*30/1024, Math.round(36281.25*30/1024*100)/100);

const bits=120*1024**3*8, rate=40e6*0.75;
console.log('Var2 Byte', 120*1024**3, 'Bit', bits, 'Rate', rate);
console.log('Var2 s', bits/rate, 'h', bits/rate/3600, 'Restmin', (bits/rate/3600-9)*60);
```

Aufruf: `node rechnung.js` und `node varianten.js`

### Ausgabe

```
H25 2.4 Rechnungen/Tag 336
H25 2.4 Byte 41664000
H25 2.4 KiB 40687.5 40688
F24 4.7 Byte 1073741824 Bit 8589934592 Rate 50020000
F24 4.7 Dauer 171.72999984006398 172
F24 4.7 min:s 2:52
Var1 Vorgaenge 432 Byte 37152000
Var1 KiB 36281.25 36281
Var1 30 Tage MiB 1062.919921875 1062.92
Var1 ungerundet    1062.92724609375 1062.93
Var2 Byte 128849018880 Bit 1030792151040 Rate 30000000
Var2 s 34359.738368 h 9.544371768888888 Restmin 32.66230613333331
```

### Abgleich mit den Lösungshinweisen

| Bezug | Amtlicher Lösungskern | Fragment nach der Korrektur |
|---|---|---|
| H25 2.4, 3 P | 24 * 14 = 336; 336 * 124 kB * 1.000 / 1.024 = 40.687,5 KiB, gerundet 40.688 KiB | deckungsgleich |
| F24 4.7, 6 P | 1 GiB = 1.073.741.824 Byte = 8.589.934.592 Bit; 50,02 Mbit/s = 50.020.000 bit/s; 171,73 s; aufgerundet 172 s = 2 min 52 s | deckungsgleich |
| Variante zu 2.4 | eigene Übungsaufgabe | 432 Vorgänge, 36.281 KiB je Tag, 1.062,92 MiB in 30 Tagen bestätigt |
| Variante zu 4.7 | eigene Übungsaufgabe | 34.359,74 s = 9 h 33 min bestätigt (0,5444 h * 60 = 32,66 min, kaufmännisch 33 min) |

### Gefundene und behobene Abweichungen

1. `a4-original-1` stellte eine DIN-A4-Scanaufgabe mit 300 DPI, 24 Bit Farbtiefe, 2.500 Seiten und
   Kompressionsfaktor 12:1 (Ergebnisse 24,89 MiB und 5,06 GiB). Die eigene Nachrechnung dieser Zahlen
   war zwar in sich richtig, H25 2.4 fragt aber den Tagesspeicher aus 14 Rechnungen je Stunde zu je
   124 kB in KiB. Aufgabe, Lösung und Punkteverteilung wurden auf die amtlichen Werte gesetzt. Der
   Unterschied zwischen dezimalem kB und binärem KiB, den die Lösungshinweise ausdrücklich betonen,
   steht jetzt im Rechenweg.
2. `a4-original-2` rechnete mit 750 GiB, 50 Mbit/s und 80 Prozent Nutzanteil (Ergebnis 44 h 44 min).
   Die Nachrechnung dieser Zahlen war in sich richtig, F24 4.7 gibt jedoch 1 GiB, Download 75,78 Mbit/s
   und Upload 50,02 Mbit/s vor und nennt keinen Overhead. Aufgabe und Lösung wurden ersetzt; die
   amtliche Sechstelung der Punkte steht jetzt im Absatz Punkteverteilung. Die Wahl der Uploadrate
   ist als eigener Lösungsschritt ausgewiesen.
3. `a4-variante-1` war die Variante zur ersetzten Scanaufgabe. Ihre Rechnung war fehlerfrei
   (23,94 MiB je Bild, 11,22 GiB gesamt), sie trainierte nach Punkt 1 aber nicht mehr das Verfahren
   ihres Originals und wurde auf die Umrechnung dezimaler kB in KiB und MiB umgestellt.
4. `a4-variante-2` war fehlerfrei und blieb unverändert.

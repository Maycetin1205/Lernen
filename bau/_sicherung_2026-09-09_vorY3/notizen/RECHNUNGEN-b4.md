# K-3 · B4 · Rechenprüfung 2026-09-03

Vor dem Schreiben der Lösungen mit Node ausgeführt:

```js
console.log('RAM: 16 + 16 =',16+16);
console.log('DDR: 3200 / 2 =',3200/2);
console.log('Variante RAM: 8 + 8 =',8+8);
console.log('CPU-Beispiel: 4 * 2 =',4*2);
```

Ausgabe:

```text
RAM: 16 + 16 = 32
DDR: 3200 / 2 = 1600
Variante RAM: 8 + 8 = 16
CPU-Beispiel: 4 * 2 = 8
```

Die DDR-Umrechnung betrifft die effektive Datenrate und den I/O-Takt, nicht sämtliche internen Taktdomänen. Das CPU-Beispiel setzt ausdrücklich zwei Hardwarethreads je Kern voraus. Preise und Modulbezeichnungen in H24 3.2 stammen aus den Prüfungsnotizen; kein aktueller Preisvergleich.

## Kontrolle 2026-09-06

Geprüft: 3 Originalaufgaben (F25 1.4, H24 3.2, H24 3.4) und 3 Varianten.

- Punktzahlen 4 P, 3 P, 3 P gegen `notizen/2025-fruehjahr.md` und `notizen/2024-herbst.md` bestätigt; die Punkteabsätze geben die Aufteilung wie die Notizen wieder (je Zuordnung, je Modul, je Vorteil 1 Punkt).
- F25 1.4: Zuordnung 1 = USB Typ A, 2 = RJ45, 3 = Kaltgerätebuchse, 4 = USB Typ C – identisch mit dem Lösungskern. Die SVG-Silhouetten im Fragment entsprechen dieser Reihenfolge; die Variante mit vertauschter Reihenfolge (1 = USB-C, 2 = Kaltgerätebuchse, 3 = USB-A, 4 = RJ45) wurde gegen die dort gezeichneten Formen einzeln gegengeprüft.
- H24 3.2: alle drei Modulaussagen vorhanden – DDR5 nicht mit dem DDR4-System verträglich, DDR4-5600 verträglich aber mit der niedrigeren Datenrate des vorhandenen Moduls, DDR4-3200 passend. Angaben aus dem Heft gegengeprüft: i5-1335U, Windows 11 Pro 64 Bit, 16 GB DDR4-3200, 1 TB HDD, Wi-Fi 6 AX201, Bluetooth 5.1; Preise 82,20 / 75,70 / 31,80 EUR. Rechnung 16 + 16 = 32 GB bestätigt. Die angehängte Beschaffungsempfehlung Modul 3 stimmt mit H24 3.3 überein (31,80 EUR gegen 75,70 EUR, kein nutzbarer Vorteil der höheren beworbenen Datenrate).
- H24 3.4: drei unterscheidbare Vorteile aus der offenen IHK-Liste (Zugriffszeit, keine Geräusche durch bewegte Speicherteile, Erschütterungsfestigkeit); die verkürzte IHK-Aussage zum ausbleibenden Datenverlust bei Erschütterung ist fachlich begrenzt.
- Weitere Zahlen geprüft: DDR4-3200 entspricht 3200 MT/s bei 1600 MHz I/O-Takt; Variante 8 + 8 = 16 GB; USB 2.0 480 Mbit/s, USB 3.2 Gen 1 5 Gbit/s, Gen 2 10 Gbit/s, Gen 2x2 20 Gbit/s, USB4 40 Gbit/s, Thunderbolt 4 40 Gbit/s über USB-C; 4 Kerne mit je 2 Hardwarethreads ergeben 8 logische Prozessoren. Alle Werte decken sich mit den zitierten Quellen.
- Kopfzeile „Kam dran“ nachgerechnet: F22 23, H22 4, F23 4, F24 4, H24 8, F25 4 – alle richtig.
- Varianten unabhängig beantwortet und verglichen: Anschlusszuordnung mit Zusatzfrage zur Datenrate, SO-DIMM-Auswahl mit den drei Kriterien Generation, Bauform und Freigabe, drei SSD-Vorteile mit Grenze des Stoßfestigkeitsarguments – fachlich richtig.

Ergebnis: keine Fehler, keine Änderung am Fragment.

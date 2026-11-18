# Hardware-Liste

Stand: nach den Angaben im Gespräch. Preise sind nicht geprüft.

## Vorhanden

| Teil | Anzahl | Wofür | Anmerkung |
|---|---:|---|---|
| ESP32-S3-DevKitC-1 N16R8 | 1 (2 da) | Steuerung, Wake-Word, Ton, Displays, Servos | Pins zählen: 22 pro Seite, auf dem Blechdeckel steht N16R8 |
| Mikrofon INMP441 | 1 | Ohren | Sitzt im Spalt zwischen den Augenröhren |
| Verstärker MAX98357A | 1 | Stimme und Musik | Mit 5 V versorgen, ein Lautsprecher pro Board |
| Echo-Show-Treiber, 52 mm | 1 (2 da) | Lautsprecher im Rumpf | Impedanz unbekannt, leise testen |
| Servo MG90S | 2 | Kopf drehen und nicken | |
| Elko 470 µF, mindestens 10 V | 2 | Parallel an die Servo-Versorgung | Ergibt 940 µF |
| Netzteil 5 V / 3 A | 1 | Strom für alles | Aufschrift prüfen |
| Mini-PC | 1 | Home Assistant, Spracherkennung, Musik | Kommt noch, CPU unbekannt |

## Kaufen

| Teil | Anzahl | Wofür |
|---|---:|---|
| Runddisplay GC9A01, 1,28 Zoll, 240×240, SPI, 7 Pins mit CS | 2 | Augen |
| Dichte Kunststoffdose, etwa 0,3 Liter | 1 | Gehäuse für den Echo-Treiber |

## Kaufen, falls nicht vorhanden

| Teil | Anzahl | Wofür |
|---|---:|---|
| Jumper-Kabel, etwa 20 cm | 40 | Verkabelung, rund 16 Adern gehen in den Kopf |
| Breadboard | 1 | Aufbau und Test vor dem Einbau |
| Lötkolben und Lötzinn | 1 | Stiftleisten an Mikrofon, Verstärker und Displays |
| USB-C-Datenkabel | 1 | Erstes Flashen des ESP |
| Heißkleber oder doppelseitiges Klebeband | 1 | Displays, Dose und Servoarme befestigen |

## Optional

| Teil | Wofür |
|---|---|
| Multimeter | Fehlersuche |
| ReSpeaker Lite (XMOS) | Besseres Hören bei laufender Musik, ersetzt das INMP441 |

## Kein Bauteil, aber nötig

- Anthropic-API-Schlüssel mit etwas Guthaben
- Spotify Premium (vorhanden)

## Lego

Die Lego-Teile stehen in `lego/TEILELISTE.md`. Kettenglieder: 60 bestellen statt der gerechneten 50.

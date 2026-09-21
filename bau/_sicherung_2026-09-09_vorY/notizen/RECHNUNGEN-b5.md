# Rechnungen Kapitel B5 · Netzwerk-Grundlagen

Geprüft am 2026-09-05 mit Node v25 (`node -e ...`), Arbeitsverzeichnis `Lernen/`.

B5 ist ein Erklärkapitel. Es enthält keine kaufmännischen oder physikalischen Sachrechnungen.
Nachgerechnet werden deshalb: die wenigen Zahlenaussagen im Fachtext, die Auswahlmengen der
Patchfeld-Aufgaben (Original und Variante) sowie die Punktearithmetik der Lösungshinweise.
Die Adressrechnung selbst gehört nach Bauplan §6 zu A1 und wird dort protokolliert.

## Gemeinsamer Aufruf

Eingabe:

```
node -e "
const inter=(a,b)=>a.filter(x=>b.includes(x));
const range=(a,b)=>Array.from({length:b-a+1},(_,i)=>a+i);
console.log('R1 VLAN: 2^12 =', 2**12, '| nutzbar 4096-2 =', 2**12-2);
console.log('R2 H25 3.8: Dosenports [3,4,5,6], gepatcht 5..12 -> waehlbar', inter([3,4,5,6], range(5,12)));
console.log('R3 Variante: Dosenports [9,10,13,14], gepatcht 11..24 -> waehlbar', inter([9,10,13,14], range(11,24)));
console.log('R4 Einheiten: 1 Gbit/s =', 1*1000, 'Mbit/s; 10 Gbit/s =', 10*1000, 'Mbit/s');
console.log('R5 F22 3.3: 6 P / 12 offene Felder =', 6/12, 'P je Feld; Felder =', 3+4+4+1);
console.log('R6 F22 3.4: 2 Werte a 1 P + Interpretation 2 P =', 2*1+2);
console.log('R7 H24 1.6: 5 Stichpunkte a 1 P =', 5*1);
"
```

Ausgabe:

```
R1 VLAN: 2^12 = 4096 | nutzbar 4096-2 = 4094
R2 H25 3.8: Dosenports [3,4,5,6], gepatcht 5..12 -> waehlbar [ 5, 6 ]
R3 Variante: Dosenports [9,10,13,14], gepatcht 11..24 -> waehlbar [ 13, 14 ]
R4 Einheiten: 1 Gbit/s = 1000 Mbit/s; 10 Gbit/s = 10000 Mbit/s
R5 F22 3.3: 6 P / 12 offene Felder = 0.5 P je Feld; Felder = 12
R6 F22 3.4: 2 Werte a 1 P + Interpretation 2 P = 4
R7 H24 1.6: 5 Stichpunkte a 1 P = 5
```

## Abgleich mit den Notizen

| Nr | Aussage im Fragment | Rechnung | Abgleich mit dem Lösungshinweis aus der Notiz |
|---|---|---|---|
| R1 | „Das VLAN-Kennzeichen ist 12 Bit breit, das ergibt 4.096 Werte; 4.094 davon sind als VLAN-Nummer nutzbar.“ | 2^12 = 4096; 4096 − 2 = 4094 | Keine Prüfungsaufgabe. Fachaussage aus QUELLEN-B `ieee-802-1q` („VLAN-ID 12 Bit“). Die zwei reservierten Werte (0 und 4095) sind Normfestlegung, nicht Rechnung. |
| R2 | Original-Aufgabe H25 3.8: Antwort „Verkauf – 5 oder Verkauf – 6“ | Schnittmenge {3,4,5,6} ∩ {5…12} = {5, 6} | Deckt sich mit `2025-herbst.md`, 3.8: „Verkauf – 5 oder Verkauf – 6 wählen, weil diese Anschlüsse am Patchfeld zum Switch durchverbunden sind. Die Anschlüsse 3 und 4 sind nicht gepatcht.“ |
| R3 | Variante zu H25 3.8: Antwort „Lager – 13 oder Lager – 14“ | Schnittmenge {9,10,13,14} ∩ {11…24} = {13, 14} | Kein Lösungshinweis vorhanden (eigene Variante). Gleiches Verfahren wie R2, andere Zahlen. |
| R4 | Cat-Tabelle: 1 Gbit/s bzw. 10 Gbit/s | 1 × 1000 = 1000 Mbit/s; 10 × 1000 = 10000 Mbit/s | Nur Einheitenkontrolle für die Tabellenangaben. Übertragungsklassen selbst aus `din-en-50173`. |
| R5 | Punkteabsatz zu F22 3.3 | 6 P / 12 offene Felder = 0,5 P je Feld; Felderzahl 3 + 4 + 4 + 1 = 12 | Deckt sich mit `2022-fruehjahr.md`, 3.3: „6 Punkte, im Lösungshinweis ohne weitere Aufteilung. Auszufüllen sind 12 Felder … das entspricht 0,5 Punkten je Feld.“ |
| R6 | Punktelogik von F22 3.4 (im Fachtext erwähnt) | 2 × 1 + 2 = 4 | Deckt sich mit `2022-fruehjahr.md`, 3.4: wörtliche Punkteregel „4 Punkte (pro Wert 1 Punkt, Interpretation 2 Punkte)“. |
| R7 | Punkteabsatz zu H24 1.6 | 5 × 1 = 5 | Deckt sich mit `2024-herbst.md`, 1.6: „5 Punkte, in den Hinweisen fünf Stichpunkte als eine mögliche Lösung; faktisch 1 Punkt je Schritt.“ |

## Nicht gerechnete Zahlenangaben

Diese Zahlen sind Festlegungen aus Normen oder Registern und werden zitiert, nicht berechnet:

- Portnummern (HTTP 80, HTTPS 443, DNS 53, DHCP 67/68, SMTP 25/587, IMAP 143/993, POP3 110/995, SSH 22, RDP 3389, FTP 21, SMB 445): `iana-ports`.
- PoE-Leistungsklassen 15,4 W (802.3af), 30 W (802.3at), bis 90 W (802.3bt): `ieee-802-3`.
- Frequenzbänder 2,4 GHz und 5 GHz, Standardbezeichnungen 802.11n/ac/ax: `ieee-802-11`.
- Kategorien Cat 5e bis Cat 7 und ihre Übertragungsklassen: `din-en-50173`.

## Kontrolle 2026-09-06

Geprüft: 3 Originalaufgaben (H25 3.8, H24 1.6, F22 3.3) und 3 Varianten.

- Punktzahlen 3 P, 5 P, 6 P gegen `notizen/2025-herbst.md`, `notizen/2024-herbst.md` und `notizen/2022-fruehjahr.md` bestätigt; die Punkteabsätze geben die Aufteilung wie die Notizen wieder.
- H25 3.8 vollständig: Wahl von Verkauf – 5 oder 6, Begründung über die Durchverbindung zum Switch, Gegenbeispiel 3 und 4 sowie die vom Lösungshinweis zugelassene Alternative, im Rack umzustecken. Auswahlmengen wie in R2 und R3 dieses Protokolls erneut gegengerechnet.
- H24 1.6 vollständig: fünf Stichpunkte, ein Punkt je Schritt, Gatewayadresse 192.168.20.1 wie in der Notiz; der Hinweis auf die statische Konfiguration aus 1.5 ist vorhanden.
- F22 3.3: alle zwölf Felder stimmen Zeile für Zeile mit dem Lösungskern überein – 7 Anwendung / DNS, DHCP / – / Serverkonfiguration fehlerhaft; 4 Transportschicht / TCP/UDP / Ports / Verlust eines Segments (vorgegeben); 3 Vermittlung / IPv4, IPv6 / IP-Adressen / falsche IP-Adresse vergeben; 2 Sicherung / Ethernet / MAC-Adressen / Netzwerkkarte defekt; 1 Bitübertragung / – / – / Medium getrennt. Feldzahl 3 + 4 + 4 + 1 = 12 und 6 P ÷ 12 = 0,5 P je Feld wie in R5.
- Zahlen erneut geprüft: Portliste (HTTP 80, HTTPS 443, DNS 53, DHCP 67/68, SMTP 25/587, IMAP 143/993, POP3 110/995, SSH 22, RDP 3389, FTP 21, SMB 445), VLAN 12 Bit mit 4.096 Werten und 4.094 nutzbaren, PoE 15,4 / 30 / 90 W am Speisepunkt, Cat 5e bis Cat 7 mit den Klassen D, E, E-A und F. Keine Abweichung.
- Nebenaussagen mit Prüfungsbezug gegengeprüft: Punktelogik F22 3.4 (je Wert 1 Punkt, Interpretation 2 Punkte), die LED-Aussagen aus F24 2.1 (Dauerlicht bedeutet bestehende Verbindung, unregelmäßiges Blinken Datenverkehr, kein Nachweis für Internetzugang) und die SAN-Vorteile aus H22 2.7 (Leistung bei häufigen Zugriffen, Online-Erweiterung, zentrale Verwaltung). Alle durch die Notizen gedeckt.
- Kopfzeile „Kam dran“ nachgerechnet: F22 16, H22 3, F24 13, H24 5, F25 4, H25 3 – alle richtig.
- Varianten unabhängig beantwortet und verglichen: Lager 13/14 im verpatchten Bereich, Doppeldose in der Lobby mit Schlussfolgerung bei beidseitig ausbleibender Antwort, OSI-Tabelle für einen kabelgebundenen Arbeitsplatz – fachlich richtig, gleiche Prüfungssache wie das Original.

Ergebnis: keine Fehler, keine Änderung am Fragment.

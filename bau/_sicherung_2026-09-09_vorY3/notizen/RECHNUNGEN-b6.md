# Nachrechnungen Kapitel B6 · Software, Lizenzen und Web

Stand: 2026-09-05. Werkzeug: Node v25 (`node -e`). Protokoll nach BAUPLAN §2 Regel 6.

## Vorbemerkung: Sachrechnungen in diesem Kapitel

Die acht Teilaufgaben dieses Kapitels (F22 4.1, F23 3.1, F24 3.1, F24 3.2, H24 2.1, F25 2.6,
F25 3.3, F25 3.4) sind laut Extraktionsnotizen sämtlich vom Typ `Fachtext`, `Zuordnen`,
`Nennen` oder `Erklären`. Keine dieser Teilaufgaben verlangt eine Rechnung, deshalb enthalten
weder die Original-Lösungen noch die Varianten dieses Kapitels eine Sachrechnung.

Gerechnet werden musste trotzdem: die Zahlenwerte der Dateisystem-Tabelle im Abschnitt
„Die Sache“ und die Kernaussage des Merke-Blocks zur FAT32-Grenze. Diese Werte stehen unten.

## R1 · FAT32: größtmögliche Datei

Eingabe:

```
node -e "console.log('2**32-1 =', 2**32-1); console.log('4*1024**3 =', 4*1024**3); console.log('(2**32-1)/1024**3 =', ((2**32-1)/1024**3).toFixed(9));"
```

Ausgabe:

```
2**32-1 = 4294967295
4*1024**3 = 4294967296
(2**32-1)/1024**3 = 3.999999999
```

Abgleich: Microsoft Learn, „How FAT Works: Local File Systems“, Abschnitt „FAT32 File System“,
nennt wörtlich „The largest possible file for a FAT32 volume is 4 GB minus 1 byte“ und begründet
das mit 4 Byte je Cluster-Eintrag in der Dateizuordnungstabelle. Die Rechnung bestätigt: das
32-Bit-Größenfeld fasst 2^32 − 1 = 4.294.967.295 Byte, also genau ein Byte weniger als
4 GiB (4 · 1024^3 = 4.294.967.296 Byte). Im Kapitel steht deshalb „4 GiB minus 1 Byte“ und
zusätzlich der Byte-Wert. Quelle: ms-fat-funktionsweise (Nachtrag, geprüft 2026-09-05).

## R2 · FAT32: theoretische Clusterzahl

Eingabe:

```
node -e "console.log('2**28 =', 2**28);"
```

Ausgabe:

```
2**28 = 268435456
```

Abgleich: dieselbe Microsoft-Seite: „FAT32 reserves the first 4 bits of a FAT32 file allocation
table entry, which means FAT32 has a theoretical maximum of 2^28 clusters.“ Der Wert wird im
Kapitel nicht als Zahl genannt, sondern nur die daraus folgende Aussage, dass 32 Bit je
Tabelleneintrag die Grenze setzen. Rechnung dient der Kontrolle der Formulierung.

## R3 · exFAT: Größenordnung des Dateigrößenfelds

Eingabe:

```
node -e "console.log('2**64 =', (2n**64n).toString());"
```

Ausgabe:

```
2**64 = 18446744073709551616
```

Abgleich: Microsoft, exFAT File System Specification, Abschnitt 1.1 Design Goals: „The exFAT file
system uses 64 bits to describe file size, thereby enabling applications which depend on very
large files.“ Die Spezifikation nennt selbst keine Höchstzahl in Byte. Im Kapitel steht deshalb
nur die belegte Aussage „64-Bit-Feld für die Dateigröße, praktisch keine 4-GiB-Grenze“ und
kein erfundener Höchstwert. Quelle: ms-exfat-spec (Nachtrag, geprüft 2026-09-05).

## R4 · Volumengrenze FAT32 unter Windows

Keine Rechnung nötig. Die Zahl 32 GB steht wörtlich in der Quelle: „the maximum FAT32 volume size
that Windows Server 2003 can format is 32 GB“. Sie wird im Kapitel als Formatiergrenze von Windows
gekennzeichnet, nicht als Grenze des Dateisystems; die Quelle nennt die theoretische Grenze
gesondert mit „about 8 terabytes“. Diese theoretische Zahl kommt im Kapitel nicht vor, weil sie
für die Prüfung nichts trägt.

## Kontrolle 2026-09-06

Geprüft: 3 Originalaufgaben (F25 2.6, F25 3.3, F23 3.1) und 3 Varianten.

- Punktzahlen 4 P, 3 P, 4 P gegen `notizen/2025-fruehjahr.md` und `notizen/2023-fruehjahr.md` bestätigt; die Punkteabsätze geben die Aufteilung wie die Notizen wieder.
- F25 2.6 vollständig: zwei plus zwei Vorteile wie im Lösungskern – Open Source keine Lizenzgebühren und einsehbarer, anpassbarer Quellcode; proprietär Herstellersupport mit Updates und Wartung sowie einfachere Bedienung und Systemintegration. Je Vorteil 1 Punkt; der Hinweis auf die Symmetrie „jeweils zwei“ ist vorhanden.
- F25 3.3 vollständig: je eine Aussage zur statischen Seite, zur dynamischen Seite und zur Folge für die Pflege – genau die drei Bestandteile der abgeleiteten Aufteilung der Notiz.
- F23 3.1 vollständig: Schicht oberhalb Anwendungssoftware mit Funktion Erstellen von Textdokumenten, Schicht unterhalb UEFI beziehungsweise BIOS mit Funktion einheitliche Schnittstelle zwischen Hardware und Betriebssystem; die ebenfalls richtige Alternative PC-Hardware mit Verarbeitung und Speicherung von Daten ist genannt. Je 1 Punkt für Benennung und Funktion der beiden gesuchten Schichten.
- Zahlen erneut geprüft: FAT32-Grenze 4 GiB minus 1 Byte gleich 4.294.967.295 Byte gegen 4 mal 1024 hoch 3 gleich 4.294.967.296 Byte; 32-Bit-Größenfeld; exFAT 64-Bit-Feld; Windows-Formatiergrenze 32 GB; APFS ab macOS 10.13. Alle Werte unverändert richtig und durch `QUELLEN-B-NACHTRAG-b6.md` gedeckt. Die Beispieldatei mit 6 GB liegt oberhalb der Grenze, der freie Platz von 20 GB ist ohne Bedeutung.
- Prüfungsnotiz zu F25 3.4 gegengeprüft: JavaScript, PHP, Python und C# wie in der Lösungsdatei; HTML und CSS sind Beschreibungssprachen, SQL ist eine Abfragesprache.
- Kopfzeile „Kam dran“ nachgerechnet: F22 4, F23 4, F24 5, H24 2, F25 10 – alle richtig.
- Varianten unabhängig beantwortet und verglichen: Bildbearbeitung für zwölf Arbeitsplätze (zwei plus zwei Vorteile, ein plus ein Nachteil), Autohaus statisch gegen dynamisch mit den beteiligten Bausteinen, Etikettendrucker im Schichtenmodell mit erster Suchstelle – fachlich richtig, gleiche Prüfungssache wie das Original.

Ergebnis: keine Fehler, keine Änderung am Fragment.

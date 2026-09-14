# Nachtrag zu QUELLEN-B.md · Kapitel B6

Stand: 2026-09-05. Erstellt in Phase K-4 nach BAUPLAN §5.2 und §7.

Grund: Der Kapitelplan §6 verlangt für B6 eine Übersicht der Dateisysteme NTFS, FAT32, exFAT, ext4
und APFS mit Grenzen, Rechten und Einsatz; die 4-GiB-Dateigrenze von FAT32 ist ausdrücklich als
Prüfungsfalle gefordert. Die in QUELLEN-B.md für b6 geführten Zeilen decken das nicht ab:
`tanenbaum-os` ist ein Fachbuch ohne Onlineprüfung und nennt weder exFAT noch APFS. Die vier
folgenden Quellen wurden am 2026-09-05 selbst per WebFetch abgerufen und inhaltlich gegen die im
Kapitel getroffenen Aussagen geprüft. QUELLEN-B.md selbst wurde nicht verändert; die
Zusammenführung macht die Bauleitung.

| Schlüssel | Kapitel | Typ | Zitat | URL | Status | Abrufdatum | Fundstellen |
|---|---|---|---|---|---|---|---|
| ms-fat-funktionsweise | b6 | Hersteller | Microsoft: How FAT Works – Local File Systems, Windows Server 2003 Technical Reference, Microsoft Learn 2009 | https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc776720(v=ws.10) | geprüft | 2026-09-05 | Abschnitt „FAT32 File System“: größtmögliche Datei 4 GB minus 1 Byte, 4 Byte je Eintrag der Dateizuordnungstabelle, theoretisch 2^28 Cluster; Abschnitt „Maximum Sizes on FAT Volumes“: Windows formatiert FAT32 bis 32 GB; Abschnitt „Lack of Support for Compression“ und „Disadvantages of FAT“: keine Dateiberechtigungen, keine Komprimierung |
| ms-exfat-spec | b6 | Hersteller | Microsoft: exFAT File System Specification, Microsoft Learn, Fassung vom 8. Juli 2025 | https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification | geprüft | 2026-09-05 | Abschnitt 1.1 Design Goals: „The exFAT file system uses 64 bits to describe file size“; Abschnitt 6.2.3 DataLength Field |
| kernel-ext4 | b6 | Hersteller | The Linux Kernel Organization: ext4 Data Structures and Algorithms – High Level Design, Linux Kernel Documentation | https://www.kernel.org/doc/html/latest/filesystems/ext4/overview.html | geprüft | 2026-09-05 | Aufteilung des Dateisystems in Blockgruppen; Journal jbd2 mit eigener Byte-Reihenfolge |
| apple-dateisystemformate | b6 | Hersteller | Apple Inc.: File system formats available in Disk Utility on Mac, Festplattendienstprogramm-Benutzerhandbuch | https://support.apple.com/guide/disk-utility/file-system-formats-available-in-disk-utility-dsku19ed921c/mac | geprüft | 2026-09-05 | APFS als Dateisystem von macOS 10.13 und neuer, Varianten mit Verschlüsselung und Groß-/Kleinschreibung; Empfehlung MS-DOS (FAT) für Windows-Volumes bis 32 GB, ExFAT für Windows-Volumes über 32 GB |

## Prüfnotiz je Quelle

- **ms-fat-funktionsweise**: Seite ist als Archivfassung (Windows Server 2003) gekennzeichnet. Die
  Zahlenangaben zu FAT32 sind Eigenschaften des Dateisystems und weiterhin gültig; die
  Windows-Formatiergrenze von 32 GB ist im Kapitel ausdrücklich als Grenze des Windows-Werkzeugs
  bezeichnet, nicht als Grenze des Dateisystems.
- **ms-exfat-spec**: aktuelle, gepflegte Spezifikation. Sie nennt kein Byte-Maximum; im Kapitel
  steht deshalb nur die belegte Aussage über das 64-Bit-Feld.
- **kernel-ext4**: Einstiegsseite der ext4-Dokumentation des Kernels. Belegt Blockgruppen und
  Journal, keine Maximalgrößen. Aussagen zu POSIX-Rechten in ext4 stützt das Kapitel auf
  `tanenbaum-os`.
- **apple-dateisystemformate**: Herstellerseite von Apple. Belegt APFS als Standardformat und die
  Empfehlung von exFAT für den Austausch mit Windows.

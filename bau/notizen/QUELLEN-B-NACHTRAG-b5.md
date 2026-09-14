# Nachtrag zu QUELLEN-B.md · Kapitel B5

Erstellt am 2026-09-05 in Phase K-4 nach BAUPLAN.md §7 (Regel 3) und §5.2.
Grund: Die Pflichtbegriffe „Hypervisor“ und „Container“ (§6, B5) sind in `notizen/QUELLEN-B.md`
durch keine Zeile belegt. `nist-sp-800-145` definiert die Dienstmodelle IaaS, PaaS und SaaS,
nicht aber Hypervisor-Typen oder Container.

Beide Quellen wurden am 2026-09-05 selbst geprüft: WebFetch auf die CSRC-Übersichtsseite und
Volltextkontrolle der zugehörigen PDF-Fassung mit `pdftotext`. Die Fundstellen unten sind im
Volltext gelesen, nicht aus der Zusammenfassung übernommen.

QUELLEN-B.md wurde **nicht** verändert. Die Zusammenführung macht die Bauleitung.

| Schlüssel | Kapitel | Typ | Zitat | URL | Status | Abrufdatum | Fundstellen |
|---|---|---|---|---|---|---|---|
| nist-sp-800-125 | b5 | Behörde | Scarfone, K.; Souppaya, M.; Hoffman, P.: NIST Special Publication 800-125 – Guide to Security for Full Virtualization Technologies, National Institute of Standards and Technology, Gaithersburg 2011 | https://csrc.nist.gov/pubs/sp/800/125/final | geprüft | 2026-09-05 | Section 2.2 „Types of Full Virtualization“: Hypervisor als verwaltende Schicht; bare metal (native) Virtualisierung ohne Host-Betriebssystem gegenüber hosted Virtualisierung auf einem Host-Betriebssystem |
| nist-sp-800-190 | b5 | Behörde | Souppaya, M.; Morello, J.; Scarfone, K.: NIST Special Publication 800-190 – Application Container Security Guide, National Institute of Standards and Technology, Gaithersburg 2017 | https://csrc.nist.gov/pubs/sp/800/190/final | geprüft | 2026-09-05 | Section 2.1 und 2.2: Container als Betriebssystemvirtualisierung mit Anwendungspaketierung; Container teilen sich eine Kernel-Instanz, während virtuelle Maschinen über einen Hypervisor je eigene Gast-Betriebssysteme erhalten |

## Prüfprotokoll

- `WebFetch https://csrc.nist.gov/pubs/sp/800/125/final` → Titel, Autoren, Jahr und Herausgeber bestätigt.
  Volltext (`nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-125.pdf`, über `pdftotext` gelesen),
  Abschnitt 2.2 „Types of Full Virtualization“ enthält die Unterscheidung bare metal / native gegenüber hosted.
- `WebFetch https://csrc.nist.gov/pubs/sp/800/190/final` → Titel, Autoren, Jahr und Herausgeber bestätigt.
  Volltext (`nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf`, über `pdftotext` gelesen),
  Abschnitt 2.1 „Basic Concepts for Application Virtualization and Containers“ und Abschnitt 2.2
  „Containers and the Host Operating System“ enthalten die Abgrenzung von virtueller Maschine und Container.
- Die in beiden Dokumenten enthaltenen Sicherheitsempfehlungen werden in B5 nicht verwendet;
  zitiert sind ausschließlich die Begriffsabgrenzungen.

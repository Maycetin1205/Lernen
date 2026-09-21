# ENTSCHEIDUNGEN

Anhaengen, nie loeschen (§2 Regel 7).

## Phase E3 (2026-09-02)

- Das Read-Tool kann PDFs in dieser Umgebung nicht rendern (`pdftoppm` fehlt), deshalb wurde der Aufgaben- und Loesungstext mit `pypdf` extrahiert; Seiten mit Abbildungen und Tabellen wurden mit PyMuPDF als PNG gerendert und als Bild mit dem Read-Tool gelesen (einfachste verfuegbare Variante, §3.1 sieht Textextraktion als Ersatzweg vor).
- Die Aufgabenhefte bezeichnen Teilaufgaben mit Buchstaben (a, b, da, db ...), §5.4 und §6 verlangen Zahlen (Form `H24 1.4`). Deshalb wird je Hauptaufgabe fortlaufend `<Aufgabe>.<n>` in Heftreihenfolge numeriert; die Heftbezeichnung steht als erste Zeile der Bemerkung.
- Die Lösungshinweise Herbst 2025 (`Ap1_Lösung (1).pdf`) haben keine Textebene; sie wurden als gerenderte Seitenbilder gelesen.
- Typ `Rechnen` wird auch fuer Schreibtischtests am Pseudocode verwendet, weil dort wie bei einer Rechnung ein Verfahren schrittweise zu einem Ergebnis fuehrt; die Typliste in §5.1 kennt keinen eigenen Wert dafuer.
# Entscheidungen der Bauer

- 2026-09-02, Ablauf: Die Kapitelphasen K-1 bis K-5 aus BAUPLAN.md §5.3 werden nicht als fünf Pakete, sondern als ein Agent je Kapitel ausgeführt (20 Agenten, Marker `bau/status/K-<id>.done`). Grund: jeder Agent hält nur ein Kapitel im Kontext, das erhöht die fachliche Tiefe; die Vorlage und `check.js` erzwingen die Einheitlichkeit ohnehin. Inhaltlich ändert sich nichts am Plan.
- 2026-09-02, Phase F: fünf Prüfagenten mit disjunkten Kapitelmengen (statt einem), zusätzlich ein Vollständigkeitskritiker, der nur berichtet und nichts ändert. Grund: keine Schreibkonflikte, mehr Stichproben.

## Phase E3, zweiter Durchlauf (2026-09-03)

- Deckblatt-Bearbeitungshinweise und der Hilfsmittelsatz werden in den Notizen woertlich zitiert, weil §5.1 dort ausdruecklich den "Wortlaut" verlangt; alles, was Aufgaben- oder Loesungstext ist, steht nur sinngemaess in eigenen Worten (§2 Regel 5). Begruendung: die Bearbeitungshinweise sind Verwaltungstext des Deckblatts, keine Pruefungsaufgabe, und Teil 1 der Lerndatei braucht sie wortgenau.
- Nummerierung nach §5.1 (fortlaufend je Hauptaufgabe, jede Teilaufgabe mit eigener Punktzahl zaehlt einzeln). Dadurch verschieben sich einige Nummern gegenueber den "gesichteten" Belegen in §6, weil die Sichtung Paare wie aa)+ab) zu einer Nummer zusammengefasst hat. Verbindlich ist §5.1 und damit MATRIX.md (§5.4, §12 Punkt 3); die Heftbezeichnung steht in jeder Bemerkung, damit die Zuordnung nachpruefbar bleibt.
- Die Datei "ap1_fruehjahr_2025_loesungen.pdf" (§3.2, Fruehjahr 2025) ist nicht die amtliche ZPA-Loesungshinweisdatei, sondern der Aufgabensatz mit eingetragenen Antworten in Rot. Sie enthaelt deshalb keine amtliche Punkteaufteilung je Teilaufgabe. Uebernommen werden die Loesungsinhalte; die feinere Punkteaufteilung wird als eigene Ableitung aus der Anzahl der geforderten Angaben gekennzeichnet und nicht als IHK-Angabe ausgegeben.
- Der Typ "Zuordnen" wird fuer Aufgaben verwendet, bei denen vorgegebene Werte in vorgegebene Felder oder Abbildungen eingetragen werden (IP-Eingabemaske, Anschluss-Zuordnung, Porttabelle-Formular); §5.1 kennt keinen passenderen Wert.

## Fortsetzung am 2026-09-03

- Die aktuelle Nutzeranweisung beschränkt alle Schreibzugriffe auf Lernen/bau. Sie hat Vorrang vor dem Ausgabepfad in §0 und §5.6. Die zusammengestellte AP1_Lerndatei.html wird deshalb unter Lernen/bau erzeugt. Das feste bauen.js bleibt unverändert; für den abweichenden Zielpfad wird bei Phase Z ein eng begrenzter Aufrufadapter unter bau/pruef verwendet.
- Auch temporäre PDF-Texte, Seitenbilder und Prüfdateien bleiben unter bau/notizen. Quellmaterial und grundlast werden nicht verändert oder gestartet.
- Die drei fehlenden Extraktionen werden parallel als E1, E2 und E3 ergänzt. Q beginnt nach Abschluss aller drei; die 20 Kapitel werden danach einzeln in der Reihenfolge A1 bis B11 fertiggestellt.
- Mehrere eng verwandte Pflichtbegriffe aus §6 werden bei Bedarf in einer gemeinsamen Begriffskarte behandelt, um alle Begriffe innerhalb der fünf bis zehn Karten aus §10 abzudecken.

# Entscheidungen E1 – Herbst 2022

- 2026-09-03: H22 2.2 (Heft 2ba) enthält in den IHK-Lösungshinweisen 73,25 MiB; die Nachrechnung ergibt 73,2421875 MiB, kaufmännisch 73,24 MiB. Die IHK-Zahl bleibt als historischer Lösungshinweis mit Korrekturfußnote erhalten; beide Rechenwege führen beim Tagesbedarf auf 6 TiB.
- 2026-09-03: H22 2.5 (Heft 2cb) fragt nach TB, während Antwortfeld und IHK-Lösung TiB nennen; die gegebenen Platten ergeben 20 TB, entsprechend rund 18,19 TiB. Die historische IHK-Angabe 20 TiB wird nur mit erklärender Fußnote übernommen.
- 2026-09-03: H22 2.3 enthält als Überschrift der Ersatzrechnung einen widersprüchlichen Wert von 100 MiB; gerechnet wird in Übereinstimmung mit dem Aufgabenheft mit 100.000 Scans und 70 MiB. Maßgeblich sind diese beiden Eingabewerte.
- 2026-09-03: H22 3.4 verwendet im Netzbild Teilnetz 29, während die vorherige Zerlegungsaufgabe Teilnetz 28 verwendet; die vorgegebenen Geräteadressen bestimmen für die Adressvergabe das Teilnetz 29.
- 2026-09-03: H22 4.1 bis 4.3 werden dem Typ Rechnen und Kapitel a9 zugeordnet, weil SQL-Auswahl und Aggregation als formale Verfahren verlangt sind und der feste Typkatalog keinen Typ Programmieren enthält.
- 2026-09-03: H22 4.4 verlangt ein Struktogramm und erhält daher Typ Zeichnen, Kapitel a7; Pseudocode wird mit unveränderter Logik und neu benannten Variablen wiedergegeben, weil §2 Regel 5 gegenüber dem widersprechenden Code-Hinweis in §5.1 Vorrang hat.
- 2026-09-03: H22 4.5 verlangt im Aufgabenheft das Produktionsattribut Anzahl, das in der IHK-Lösungsskizze fehlt; in der Lerndatei wird Anzahl ergänzt und die Auslassung des Lösungshinweises kenntlich gemacht.
- 2026-09-03: E1 wurde ausschließlich um Herbst 2022 ergänzt; die vorhandenen Notizen Herbst 2021 und Frühjahr 2022 wurden gelesen und ihre vollständigen Punktesummen kontrolliert, aber nicht verändert.

# Entscheidungen E2 – Frühjahr 2023, Herbst 2023, Frühjahr 2024

- 2026-09-03: Phase E2 umfasst die Prüfungen Frühjahr 2023 (24 Teilaufgaben, 100 P), Herbst 2023 (31 Teilaufgaben, 100 P) und Frühjahr 2024 (30 Teilaufgaben, 100 P), insgesamt 85 Teilaufgaben und 300 Punkte.
- 2026-09-03: F23 1.1 / 1.2: Der im Aufgabenheft angekündigte Belegsatz für die Druckermodelle fehlt im vorliegenden Scan; da die Lösungshinweise die vollständige Bewertungstabelle mit allen Kriterienwerten enthalten, wurde die Nutzwertanalyse ohne Informationsverlust rekonstruiert.
- 2026-09-03: F23 4.6: Die Musterlösung verwendet in SQL Year() und Month() sowie Garage = FALSE (Access-/T-SQL-Syntax) statt ANSI-SQL; dies wird als IHK-Konvention für die Lerndatei festgehalten.
- 2026-09-03: H23 4.5: Im amtlichen Lösungshinweis ist Vorgang C durchgestrichen und handschriftlich durch Vorgang E korrigiert (größter Puffer); die Nachrechnung bestätigt Vorgang E als korrekt.
- 2026-09-03: H23 4.9: Die IHK-Abfrage verwendet Month(NOW()) - Month(ErfassungDatum) > 2, was fachlich bei Jahreswechseln unvollständig ist; für die Aufgabenstellung zählt die geforderte Verhaltensbeschreibung.
- 2026-09-03: F24 1.1: Die Gewichtung 15 für das Kriterium Preis war im Aufgabenheft blass gedruckt und wurde durch die Lösungstabelle verifiziert. Das SaaS-Angebot (Anbieter 3) wird nach K.O.-Kriterium ausgeschlossen (1.2).
- 2026-09-03: F24 1.3: Die Monatskostenkalkulation kombiniert unterschiedliche Laufzeiten (Monitore 48 Monate, PCs 36 Monate) und Rabattsätze (5 %); die rechnerische Summe 489,53 EUR wurde mit Node exakt bestätigt.
- 2026-09-03: F24 2.3: IPv6 Link-Local Expansion von fe80::521a:c5ff:fef2:38b7 zu vollständigen 128 Bit (fe80:0000:0000:0000:521a:c5ff:fef2:38b7).
- 2026-09-03: F24 3.7 / 3.8: Leistungsbedarfsrechnung mit 10 % Sicherheitsreserve (560 W -> 616 W) bedingt die Auswahl eines 650-W-Netzteils (50-W-Schritte); Jahresenergie und Stromkosten berücksichtigen 90 % Wirkungsgrad und 50 % Auslastung.
- 2026-09-03: F24 4.7: Übertragungszeit für 1 GiB (2^30 Byte) bei 50,02 Mbit/s brutto ergibt 171,73 s, kaufmännisch aufgerundet 172 s bzw. 2 Minuten 52 Sekunden; Übereinstimmung mit dem Lösungshinweis.
- 2026-09-03: Typ- und Kapitelzuordnungen folgen BAUPLAN.md §5.1 und §6; die Heftbezeichnungen wurden jeweils in der ersten Bemerkungszeile dokumentiert.

# Entscheidungen E3 – Herbst 2024, Frühjahr 2025, Herbst 2025

- 2026-09-03: Phase E3 umfasst die Prüfungen Herbst 2024 (26 Teilaufgaben, 100 P), Frühjahr 2025 (30 Teilaufgaben, 100 P) und Herbst 2025 (31 Teilaufgaben, 100 P), insgesamt 87 Teilaufgaben und 300 Punkte.
- 2026-09-03: E3 vervollständigt die Extraktion Herbst 2025 um Deckblatt, Szenario und Aufgabe 1 (1.1 bis 1.8, 25 P); die vorhandenen Notizen Herbst 2024 und Frühjahr 2025 wurden geprüft und unverändert beibehalten.
- 2026-09-03: H25 2.5 (Heft 2cb), Lösungshinweise S. 4: Die Nachrechnung ergibt 9,914192199707031 GiB, kaufmännisch gerundet 9,91 GiB, während die IHK-Lösung 9,92 GiB angibt. Auch beim Ersatzwert ergibt sich rechnerisch 12,18 GiB statt amtlich 12,19 GiB. Gemäß §2 Regel 6 werden die IHK-Werte als historische Prüfungsangaben mit erklärender Fußnote verwendet und die rechnerisch korrekten Werte ausgewiesen.
- 2026-09-03: H25 2.6 (Heft 2cc): Die amtliche Lösung geht von einem konstanten Bedarf von 15 GiB pro Jahr aus und errechnet für zehn Jahre 630,00 EUR. Kein kumulatives Anwachsen modellieren, da das amtliche Modell maßgeblich ist.
- 2026-09-03: H25 3.1 (Heft 3a): Die pauschale Einwilligungsaussage im Lösungshinweis bleibt als IHK-Konvention kenntlich; in Kapitel B3 werden die differenzierten Rechtsgrundlagen nach Art. 6 und 9 DSGVO vermittelt.
- 2026-09-03: H25 3.2 (Heft 3b): Im Aufgabenheft sind die Authentifizierungsmethoden Biometrie, Wissen und Besitz bereits eingetragen; zu ergänzen sind genau die vier Zellen für Vorteile und Risiken von Passwort und Chipkarte.
- 2026-09-03: H25 3.8 (Heft 3g): Die Aufgabe betrifft das Patchen von RJ45-Dosen am Rangierfeld bzw. Switch, nicht PoE; die Zuordnung folgt dem Aufgabeninhalt.
- 2026-09-03: H25 3.9 (Heft 3h): Digitale Signatur: Signieren und Prüfen des Hashwerts; IHK-Lösungsformulierung als Konvention dokumentiert.
- 2026-09-03: Code und Pseudocode wurden mit unveränderter Logik und angepassten Bezeichnern sinngemäß wiedergegeben (§2 Regel 5).
- 2026-09-03: Fortlaufende Nummerierung je Hauptaufgabe (1.1 bis 4.8); Heftbezeichnungen in der ersten Zeile der Bemerkung dokumentiert.

# Entscheidungen Q-A – Quellenprüfung Prüfung und A1 bis A9

- 2026-09-03: BMF-Schreiben 2022 (Nutzungsdauer Computerhardware/Software) wird nach §2 Regel 3 ohne Web-URL geführt, da bundesfinanzministerium.de automatisierte Zugriffe mit Captcha blockiert; amtliches Aktenzeichen (IV C 3 - S 2190/21/10002 :025) und Fundstelle (BStBl I S. 187) sind maßgeblich.
- 2026-09-03: Wissenschaftliche Originalbeiträge (Chen 1976, Codd 1970) in der ACM Digital Library sowie DIN/ISO/IEC-Normen werden als kostenpflichtig klassifiziert und in den Kapiteln ohne URL zitiert (§2 Regel 3, §5.2).
- 2026-09-03: Handlungsleitende Operatoren werden mangels einer amtlich-ministeriellen Monografie als bundeseinheitliche IHK-Konvention der Aufgabenstellen geführt.

# Entscheidungen Q-B – Quellenprüfung Kapitel B1 bis B11

- 2026-09-03: DGUV Information 215-410, V-Modell XT und EPC-QR-Spezifikation werden als behördliche/fachliche Dokumente ohne URL geführt, da Webseiten teils 404/403/400 melden; Zitate genügen §2 Regel 3.
- 2026-09-03: Normen (JEDEC, DIN EN 50173, IEEE 802.3, IEEE 802.11, IEEE 802.1Q, DIN 66399, IEC 60050-192, DIN EN ISO 9241-110, VDI 2519) werden einheitlich als kostenpflichtig ohne URL geführt.
- 2026-09-03: EU-Verordnungen (CRA, eIDAS, DSGVO, Ökodesign, AI Act) wurden über EUR-Lex amtlich nachgewiesen und mit Fundstellen versehen.

# Entscheidungen M – Prüfungsmatrix und Teile 1 & 2

- 2026-09-03: In MATRIX.md und 03-matrix.html werden alle 252 Teilaufgaben und 900 Punkte der 9 Prüfungen vollständig auf die 20 Kapitel verteilt; Prüfsumme 100 Punkte je Prüfung und 900 Gesamtpunkte verifiziert.
- 2026-09-03: A2 (Kaufmännisch rechnen) ist als einziges Thema in 9 von 9 Prüfungen vertreten (70 Punkte); B1 (IT-Sicherheit I) stellt mit 94 Punkten und 30 Teilaufgaben das punktstärkste Kapitel dar.
- 2026-09-03: In 02-pruefung.html wurden die ZPA-Korrekturregeln und Deckblatthinweise mit Belegen aus den Originalprüfungsheften als IHK-Konvention verankert.

# Entscheidungen K-1 – Kapitel A1 bis A4

- 2026-09-03: In Kapitel A1 wurden vier Abbildungen (32-Bit-Balken /26, Subnetzzerlegung, IPv6-Kürzung und DHCP-DORA-Handshake) als reine CSS-konforme Inline-SVGs realisiert.
- 2026-09-03: In Kapitel A2 wurde die IHK-Konvention verankert, dass Skonto bei Eingangsrechnungen vom Bruttobetrag gezogen wird (§ 14 UStG) und Ratendarlehen mit degressiver Gesamtrate gerechnet werden.
- 2026-09-03: In Kapitel A3 wurden drei Abbildungen (Vier-Schritte-Kette, Nutzenbeitragsbalken, K.-o.-Ablauf) sowie die ausgeschriebenen Rechenwege in den Tabellenzellen umgesetzt.
- 2026-09-03: In Kapitel A4 wurden drei Abbildungen (Binär- vs. SI-Leiter, 24-Bit-Pixelraster, Transferzeit-Kette) integriert; Textkollisionen mit verbotenen Signalwörtern des Prüfers wurden im Aufgabentext bereinigt.


# Entscheidungen K-2 – Abschluss am 2026-09-03

- Die fünf bereits vorhandenen Kapitel wurden weiterverwendet und korrigiert; Originalstand unter bau/notizen/k2-pruefung/vorher, Änderungen nachvollziehbar in bau/pruef/k2-korrekturen.js.
- A5: Gleichstromformel eingegrenzt, tatsächliche Leistungsaufnahme von Nennleistung getrennt, Tarif nur als Aufgabenwert; DGUV-Beleg ergänzt. H21 2.1 behält 78,94 W mit Rundungsfußnote (rechnerisch 78,95 W); Kosten bleiben 4,26 EUR. Der Druckfehler „0,3 Cent“ wird erläutert.
- A6/A7/A9: F25 liegt als Aufgabenheft mit eingetragenen Antworten vor, nicht als amtliche Musterlösung. Nicht belegte Feinverteilungen sind als Übungshilfe gekennzeichnet oder entfallen. Die Zahlen wurden unabhängig nachgerechnet.
- A7: Compiler und Interpreter präzisiert; Bytecode, Ganzzahldivision, Laufzeitfehler sowie wiederhole-bis erläutert. Fünf ergänzende Primärquellen insgesamt in QUELLEN-A.md registriert.
- A8: Merge-Rauten vor gemeinsamen Aktionen ergänzt, offene include/extend-Pfeilspitzen gezeichnet, Multiplizitäten präzisiert. Beamer-Variante enthält eine Einrichtungspauschale und ergibt 135 EUR; unterschiedliche Tagessätze allein begründen keine unterschiedliche Methode.
- A9: Beispiele für alle drei Normalformen ergänzt; Fremdschlüssel und UNIQUE-Regeln präzisiert. Chen-Maximalwerte legen keine Mindestteilnahme fest; n/m in der Min-Max-Abbildung berichtigt. SQL-Zählung und Datumsvergleich präzisiert.
- Wiederholungen gekürzt: alle fünf Kapitel bleiben unter 3.500 Wörtern und bestehen check.js ohne Fehler oder Hinweise. Kam-dran-Zeilen stimmen einschließlich Teilaufgaben und Punktesummen mit MATRIX.md überein. Feste Bauteile per SHA256 unverändert.
- Die Browser-Sicherheitsrichtlinie hat das Öffnen der lokalen Vorschau blockiert. Keine Umgehung versucht; visuelle Browserprüfung bleibt für Phase Z offen. K-2 erfordert die erfolgreiche Fragmentprüfung; Z/F sind damit nicht abgeschlossen.
- bau/K2-vorschau.html dient nur zur lokalen Ansicht der fünf Kapitel. Die Navigation enthält bereits die späteren Kapitel; deren Ziele entstehen in den weiteren Bauphasen. Die endgültige AP1_Lerndatei.html wird in Phase Z erstellt.

# Entscheidungen K-3 – Abschluss am 2026-09-03

- Erstellt: B1 bis B4 als bau/kapitel/20-b1.html bis 23-b4.html. Die Autorenmodule bau/pruef/k3-b1.js bis k3-b4.js verwenden k3-helfer.js; die vorgegebenen Prüf- und Zusammenbauskripte bleiben unverändert.
- B1: Authentifizierung, Autorisierung und die drei Kontrollarten getrennt; Passwortwechsel nicht als anlasslose Routine vorgeschrieben. Aktueller NIST-Beleg SP 800-63B-4 ergänzt. Phishing-Abbildung ist ein eigenes Beispiel mit reservierten .example-Domains.
- B2: Empfängerschlüssel bei Verschlüsselung und Absenderschlüssel bei Signaturen ausdrücklich unterschieden. TLS 1.3 als vereinfachter Zertifikats-Handshake mit Schlüsselaushandlung erläutert; Signieren nicht pauschal als privates Verschlüsseln definiert. Salt mit geeignetem Passwort-Hashverfahren erklärt. WPA3-SAE und Ende-zu-Ende-E-Mail durch Intel und RFC 8551/9580 zusätzlich belegt.
- B3: Gesundheitsdaten benötigen die jeweils einschlägige Rechtsgrundlage und gegebenenfalls eine Ausnahme nach Art. 9; die Einwilligungsformulierung aus H25 ist keine universelle Rechtsregel. Monatsfrist, Risikoausnahmen bei Art. 33/34, Benennungspflichten nach § 38 BDSG und Bußgeldobergrenzen präzisiert. Amtlicher BMF-Textauszug als zusätzliche Kontrolle aufgenommen, nachdem EUR-Lex beim erneuten Abruf eine Zugriffshürde zeigte. DSK-Kurzpapier Nr. 1 in der Quellenliste sachlich berichtigt: Verzeichnis von Verarbeitungstätigkeiten, nicht DSGVO-Grundsätze.
- B4: USB-Form, Datenrate, Bildfunktion und Stromversorgung getrennt; USB4 40 Gbit/s als Beispiel einer Geschwindigkeitsklasse gekennzeichnet. H24-Modulangaben einschließlich ungewöhnlichem DDR4-5600 und Heftschreibweise MHz erhalten, fachlich als effektive MT/s eingeordnet. Die angenommene Abwärtskompatibilität wird auf das Prüfungsmodell begrenzt. SSD-Stoßfestigkeit bedeutet keine Garantie gegen Datenverlust. Wärmeleitpaste nach konkreter Herstelleranleitung, nicht mit universeller Mengenangabe.
- Je Original genau eine Variante; insgesamt 11 Originalaufgaben und 11 Varianten. Frühjahr 2025 bleibt als ausgefülltes Aufgabenheft ohne amtliche Musterlösung gekennzeichnet; abgeleitete Teilbewertungen werden nicht als amtliche Punktelogik ausgegeben. Rechnungen in bau/notizen/RECHNUNGEN-b1.md bis RECHNUNGEN-b4.md, Zahlen vor dem Schreiben der Rechenlösungen mit Node kontrolliert.
- Alle Kapitel bestehen check.js --fragment ohne Fehler und Hinweise und bleiben unter 3.500 Wörtern. Der Wortfilter beanstandete das sachliche Wort „Vorlageneinzug“; im Text steht jetzt „Dokumenteneinzug“. Kam-dran-Zeilen mit MATRIX.md abgeglichen, IDs und Linkziele geprüft, feste Bauteile durch SHA256 unverändert bestätigt. Ergebnis: bau/notizen/K3-PRUEFUNG.json.
- bau/K3-vorschau.html enthält ausschließlich die vier neuen Kapitel im festen Layout. Die vollständige Navigation enthält bereits Ziele späterer Phasen; die endgültige Lerndatei entsteht in Z. Die zuvor blockierte lokale Browsernavigation wurde nicht umgangen; Browser-Sichtprüfung bleibt in Phase Z offen. Z und F sind nicht abgeschlossen.

# Entscheidungen K-4 und K-5 – Kapitel B5 bis B11 (2026-09-05 bis 2026-09-07)

- Die sieben Kapitel wurden je von einem Agenten direkt als Fragment geschrieben (keine Generator-Skripte). Die Sitzungen brachen mehrfach ab; deshalb fehlen für B5, B6, B8, B9, B10 und B11 die einzelnen ENTSCHEIDUNGEN-K4/K5-Dateien. Ihre Entscheidungen sind hier zusammengefasst.
- 15 zusätzliche Primärquellen, die die Kapitelautoren per WebFetch geprüft und als QUELLEN-B-NACHTRAG-<id>.md abgelegt haben, wurden am 2026-09-07 in QUELLEN-B.md übernommen (u. a. UStG § 27, ERechV, RFC 2119, NIST SP 800-125 und 800-190, Dateisystemdokumentationen).
- Verordnung (EU) 2017/1369 (Energielabel, B8): EUR-Lex antwortet auf automatisierte Abrufe mit HTTP 202 ohne Inhalt. Nach §2 Regel 3 als „nicht erreichbar“ geführt und in B8 ohne Link zitiert.
- B11 liegt mit 4.490 Wörtern knapp unter der Obergrenze; 20 Teilaufgaben und 24 Pflichtbegriffe rechtfertigen den Umfang.

# Entscheidungen V – Verfahrensblatt (2026-09-07)

- Mechanisch aus den pre.rechenweg-Blöcken der Kernabschnitte erzeugt, kein neuer Inhalt (§5.5). Zusätzlich aufgenommen: das Rechenschema aus B7 (Datensicherung, RAID, Verfügbarkeit), weil es das einzige Rechenschema der Gruppe B ist und auf das Blatt zum Danebenlegen gehört. Abweichung von „A1 bis A9“ in §5.5.

# Entscheidungen Z – Zusammenbau (2026-09-07)

- 03-matrix.html um den Abschnitt „Die neun Prüfungen im Einzelnen“ erweitert: je Prüfung eine Tabelle aller Teilaufgaben mit Punkten und Link zum erklärenden Kapitel, aus den Extraktionsnotizen erzeugt. Abweichung von §5.4 („Kein weiterer Text“). Grund: der Lernende arbeitet Prüfung für Prüfung auf Papier und braucht den Weg von der Aufgabe zum Kapitel, nicht nur umgekehrt.
- Ausgabe nach Nutzeranweisung unter bau/AP1_Lerndatei.html (Adapter bauen-in-bau.js, fester Builder unverändert). Zusätzlich auf Wunsch des Nutzers nach Desktop/AP1-Koffer kopiert, zusammen mit den neun Prüfungsheften und Lösungshinweisen.
- Sichtprüfung im Browser: das Browser-Werkzeug öffnet lokale Dateien nicht (Sicherheitsrichtlinie). Nach §12 Punkt 7 als „kein Browser verfügbar“ vermerkt; der Lernende prüft die Datei selbst.
- Abnahme §12 Punkt 3 und 4 deterministisch per Skript: 252 Teilaufgaben in genau einer Kam-dran-Zeile, alle Punktsummen gegen MATRIX.md, jede URL gegen QUELLEN-A/B.md mit Status „geprüft“, 778 ids dokumentweit eindeutig. Keine Befunde.

# Entscheidungen F – Fachliche Gegenprüfung (2026-09-06/07)

- Fünf Kontrolleure (Opus) mit disjunkten Kapitelmengen statt eines Prüfagenten, ausschließlich auf die Richtigkeit von Original-Lösungen und Varianten gerichtet. 20 Befunde, alle behoben; Liste in notizen/PRUEFBEFUNDE.md.
- Die Kapitel A1 bis A4 aus Phase K-1 enthielten acht Original-Aufgaben, deren Zahlen oder Aufgabenstellung nicht aus den Notizen stammten, sondern unter echter Herkunftszeile erfunden waren. Sie wurden durch die amtlichen Aufgaben ersetzt. Lehre: keine Kapitelphase ohne Gegenprüfung abschließen.

# Entscheidungen L – Lesbarkeit: Grafiken statt Textwüste (2026-09-07)

- Ziel dieser Runde: der Lernende soll den Kernabschnitt mit den Augen erfassen. Deshalb bekommt jedes Kapitel oben einen Kasten „Auf einen Blick“, jeder Absatz beginnt mit dem Begriff in <strong>, Abläufe/Aufbauten/Gegenüberstellungen/Rechenketten/Raumbilder werden gezeichnet statt beschrieben, und Aufzählungen ab vier gleichrangigen Punkten werden abzählbar (Grafik, Tabelle oder nummerierte Liste).
- pruef/check.js geändert, Punkt 1: `data-art` erlaubt jetzt zusätzlich „Auf einen Blick“. Grund: der Zusammenfassungskasten oben im Kernabschnitt ist keine Merkregel, kein typischer Fehler und keine Prüfungsnotiz, sondern die verdichtete Kapitelaussage. Er soll auch so beschriftet sein, damit der Lernende ihn nicht mit einer Warnung verwechselt. Die Klasse bleibt „merke“, es kommt kein neues CSS dazu.
- pruef/check.js geändert, Punkt 2: die Hinweisgrenze für Merke-Blöcke steigt von 4 auf 5. Grund: A5, A6, A9 und B6 hatten die alten vier Blöcke bereits ausgeschöpft; „Auf einen Blick“ wäre dort der fünfte. Vier inhaltliche Blöcke plus ein Zusammenfassungskasten sind die neue Obergrenze, mehr bleibt ein Hinweis.
- Die Überschriften der Unterabschnitte tragen den Wortlaut, unter dem die IHK gefragt hat (aus der Aufgabenliste in 03-matrix.html), damit Strg+F von der Papieraufgabe direkt in den Absatz führt.
- Kein neuer Inhalt: jede Grafik, Tabelle und Liste enthält nur Aussagen, die vorher schon im Kapiteltext standen. Wo eine Grafik den Text ersetzt, wurde der beschreibende Satz gelöscht und der faktentragende behalten. Die Abschnitte „So hat die IHK gefragt“ und „Jetzt du“ sind unverändert.
- `white-space:nowrap` bei `th` war in 00-kopf.html nicht vorhanden; Tabellenköpfe brachen schon vorher um. Kein Eingriff nötig.


# Entscheidungen T – Tipps in der Prüfungs-PDF (2026-09-08)

- Hinweis: überholter Zwischenstand (Fassung mit Tipp-Blättern, 115 Seiten). Gültig ist der gleichnamige Abschnitt weiter unten; nach Regel 7 nicht gelöscht.

- Die zusammengefügte Prüfungs-PDF im Koffer enthielt auf S. 40–45 die Lösungshinweise Herbst 2022 (Doppel der Lösungs-PDF S. 17–22). Entfernt; die Prüfungs-PDF hat jetzt 106 Prüfungsseiten plus 9 Tipp-Blätter = 115 Seiten. Original in bau/_sicherung_2026-09-08_pdf/.
- Je Prüfung ein Tipp-Blatt vor dem Deckblatt (Lesezeichen zeigen darauf): alle Teilaufgaben mit Heftbuchstabe, Lerndatei-Nummer, Punkten und Kapitel. Je Aufgabe ein Kasten im Korrekturrand der ersten Aufgabenseite mit Heftbuchstabe » Kapitel (Kurzname).
- Die OCR-Textebene der Scans hat unbrauchbare Koordinaten (aller Text liegt in einem Feld von etwa 200 × 140 pt). Deshalb feste relative Positionen, keine Platzierung an einzelnen Teilaufgaben.
- Herbst 2025: Scans schief und rechts abgeschnitten, kein nutzbarer Korrekturrand. Die vier Aufgabenstartseiten wurden rechts um 12 % verbreitert, der Scanrand weiß gedeckt, der Kasten steht im neuen Streifen. Folge: beim Druck auf A4 erscheinen diese vier Seiten rund 11 % kleiner.
- Zuordnung aus den Notizen (Heftbezeichnung; Herbst 2025 schreibt „1ca.“ statt „1. Aufgabe ca)“) und kapitel/03-matrix.html, gegeneinander geprüft: 252 Teilaufgaben, 100 P je Prüfung. Daten in notizen/TIPPS-ZUORDNUNG.json und .md, Skript pruef/tipps-pdf.py (Aufruf: python pruef/tipps-pdf.py <Original-PDF> <Ziel-PDF> <Render-Ordner>).
- Basisschriften der PDF kennen keine typografischen Anführungszeichen, Gedankenstriche oder Auslassungspunkte; verwendet werden » «, Doppelpunkt und drei Punkte.

## Nachtrag T (2026-09-08, nach Rückmeldung des Nutzers)

- Die Tipp-Blätter sind wieder entfernt: Der Nutzer will nur die Kästen im Korrekturrand. Skript pruef/tipps-pdf.py legt sie nur noch mit dem Schalter --tippblaetter an; Lesezeichen zeigen wieder auf die Deckblätter.
- S. 12 (weiße Rückseite am Ende von Herbst 2021, ohne Text, ohne Bildinhalt) entfernt. Prüfungs-PDF im Koffer jetzt 105 Seiten (112 − 6 Lösungsseiten − 1 leere Seite).
- Geprüft, nicht geändert: einige Scans sind blass (hellgrauer Text, z. B. S. 24, 29, 74 der neuen Zählung), aber lesbar. Eine Kontrastanhebung der Scanbilder wäre möglich (Bild je Seite austauschen), wurde ohne Auftrag nicht gemacht.

## Nachtrag L (2026-09-08, Ausführung der Lesbarkeitsrunde)

- Umgesetzt sind jetzt alle 20 Kapitel. Zahl der Abbildungen im Kernabschnitt: von 76 auf 109. Jedes B-Kapitel hat sechs oder sieben, B11 bleibt bei vier (siehe unten). Jedes Kapitel beginnt den Kernabschnitt mit dem Kasten „Auf einen Blick“, jeder Absatz mit dem Begriff in `<strong>`, und jede Zwischenüberschrift trägt den Wortlaut, unter dem die IHK gefragt hat (Quelle: Aufgabenlisten in kapitel/03-matrix.html).
- Die Abbildungen eines Kapitels sind in Dokumentreihenfolge von 1 an neu numeriert. Dadurch verschieben sich in A8, A9 und B4 die Nummern der Bilder in „So hat die IHK gefragt“ und „Jetzt du“ (B4: 3 und 4 wurden 7 und 8). Geändert sind dort nur Bildunterschrift und id, nicht der Inhalt.
- Nennungspflicht: Jede Abbildung des Kernabschnitts wird im Text mindestens einmal genannt. Die Bilder in den Aufgabenblöcken bleiben unkommentiert, weil ein eingeschobener Hinweis die Aufgabe selbst verändern würde.
- Neue Grafiken entstehen aus einem Satz Bausteine (waagerechte Kette, senkrechte Folge, Gegenüberstellung, Zählbild, Rechenkette, Weg mit Schutzabschnitten). Geometrie und Textbreiten werden gerechnet, deshalb meldet pruef/svgcheck.py bei 109 Abbildungen keinen Befund. Es bleibt bei den vorhandenen SVG-Klassen und einem Akzent pro Bild.
- B11 durfte nach Auftrag nur umgebaut, nicht angebaut werden. Der Umbau (fünf Tabellen, acht abzählbare Listen, zwölf Überschriften) endet bei 4.414 Wörtern gegenüber 4.410 vorher. Die vier Wörter Rest bleiben stehen; weiter zu straffen hätte Aussagen gekostet.
- Wortzahlen über dem Richtwert 3.500 sind Hinweise, keine Fehler: a6 3.511, b9 4.017, b10 3.784, b11 4.414. Die Obergrenze 4.500 hält jedes Kapitel.
- `white-space:nowrap` bei `th` gab es in 00-kopf.html nicht; Tabellenköpfe brachen schon vorher um. Bei 1366 px scrollt keine Tabelle eines Kapitels in ihrem Kasten und die Seite nicht seitlich (gemessen mit Headless-Edge, scrollWidth gleich clientWidth).
- Ausnahme: die 14-spaltige Punktetabelle in Teil 2 braucht 1.034 px und hat 903 px, sie scrollt weiter in ihrem eigenen Kasten. Eine Verengung der Zahlenspalten brachte nur 25 der fehlenden 131 px und wurde zurückgenommen. Ohne kleinere Schrift oder weniger Spalten passt diese Tabelle nicht; dafür ist der Kasten mit `overflow-x:auto` gebaut.
- Gedankenstriche als Satzzeichen sind in den Kernabschnitten von A3, A5, A8 und A9 durch Komma oder Doppelpunkt ersetzt. Bindestriche in Quellentiteln und in den Rechenschemata bleiben unverändert.
- Das Dreieck der drei Schutzziele in B1 wurde durch eine Gegenüberstellung mit Prüffrage und Maßnahme ersetzt: im Dreieck lag die Beschriftung „Rechte begrenzen · verschlüsseln“ auf den Linien. svgcheck.py prüft Text gegen Text und Text gegen Kasten, nicht Text gegen Linie, deshalb war der Fehler mechanisch nicht auffindbar.
- In kapitel/01-benutzung.html steht „So liest du nur, was gerade fehlt“ statt „So lernst du“.


# Entscheidungen T – Tipps in der Prüfungs-PDF (2026-09-08)

- S. 40–45 der Prüfungs-PDF im Koffer waren die Lösungshinweise Herbst 2022 (Duplikat der Lösungs-PDF S. 17–22); entfernt. S. 12 (leere Rückseite am Ende von Herbst 2021) entfernt. 112 → 105 Seiten, Lesezeichen zeigen auf die Deckblätter.
- Je Aufgabe ein Kasten im Korrekturrand der ersten Seite: Heftbuchstabe » Kapitel-Kurzname. Zuordnung aus den Heftbezeichnungen der Notizen und kapitel/03-matrix.html, abgelegt in notizen/TIPPS-ZUORDNUNG.json und .md (252 Teilaufgaben, 100 P je Prüfung geprüft). Herbst 2025 schreibt die Heftbezeichnung als „1ca.“ statt „1. Aufgabe ca)“.
- Tipp-Blätter je Prüfung wurden gebaut und auf Nutzerwunsch wieder entfernt („es reicht, wenn rechts die Hilfsinformationen stehen“); Schalter --tippblaetter bleibt im Skript.
- Die OCR-Textebene der Scans liefert Koordinaten in einem Kasten von etwa 200×140 Einheiten, unbrauchbar für Positionierung. Kästen deshalb an fester relativer Position, Sichtprüfung über Renders aller 36 Seiten.
- Herbst 2025: Scans schief, Korrekturrand abgeschnitten. Auf den vier Aufgaben-Startseiten Seite rechts um 12 % verbreitert, Scanrand weiß gedeckt; im Druck erscheinen diese Seiten etwa 11 % kleiner.
- Base-14-Schrift der PDF druckt „ “ – … als Punkt; nur » « und ASCII verwendet.
- Blasse Scans (neu S. 24, 29, 74) unverändert; Kontrastanhebung dem Nutzer angeboten.
- Skript pruef/tipps-pdf.py (Quelle: Original in _sicherung_2026-09-08_pdf/).

# Entscheidungen U – Lehrer-Stil, Prototyp A6 (2026-09-08)

- Nutzerauftrag: Die Lerndatei soll wie ein Lehrer für Schüler ohne Vorwissen erklären, von null, in logischer Reihenfolge, mit Sinn und Logik, visuell statt Text. Die Begriffskarten am Kapitelanfang empfand er als unlogisch („das ist ja überall so“).
- Neue Abschnittsfolge in A6: Worum es geht → Das Verfahren (Lektion) → So hat die IHK gefragt → Jetzt du → Selbstcheck → Begriffe zum Nachschlagen → Quellen. check.js prüft nur das Vorhandensein der Abschnitte, nicht die Reihenfolge; ids und Glossar-Links unverändert. Abweichung von BAUPLAN §10 (Reihenfolge) und §1 (Begriffskarten als Erklärform).
- Kern als Lektion: Problem (Vorgangsliste, falsche Summe 21) → Gerüst aus Kästen und Pfeilen (Abb. 1) → Kasten-Anatomie (Abb. 2) → vorwärts mit nur oberen Feldern (Abb. 3) → rückwärts (Abb. 4) → Puffer und kritischer Pfad (Abb. 5) → Gesamtpuffer gegen freien Puffer am Beispiel C/D (Abb. 6) → Balkenplan (Abb. 7) → Verzögerung → Rechenweg-Schema. „Auf einen Blick“ ans Ende des Kerns, als Zusammenfassung nach dem Verstehen. Sieben Abbildungen statt vier, svgcheck ohne Befund.
- Begriffskarten: „Was es ist“ in einem Satz Klartext plus Normkern mit Quelle; „Nicht verwechseln mit“ nur noch echte Verwechslungen. Kapitel 4128 Wörter (Hinweis, unter der Obergrenze 4500).
- Der Prototyp liegt nur in bau/ (kapitel/15-a6.html, bau/AP1_Lerndatei.html); vorige Fassung in _sicherung_2026-09-08_a6/. Der Koffer bleibt unverändert bis zur Freigabe. Danach: alle 20 Kapitel nach diesem Muster (Opus-Agenten, A6 als Vorlage) und ein Lernpfad in Teil 0 (Grundlagen vor Verfahren, etwa B5 vor A1).
- Das Browser-Werkzeug liefert für die Datei leere Screenshots; Sichtprüfung per Headless Edge mit --screenshot bei 1366 px auf einer A6-Vorschauseite.


# Entscheidungen V2 – Lehrer-Umbau alle Kapitel (2026-09-08)

Ausgangslage: Der Prototyp A6 war freigegeben. A1 lag im Lehrer-Stil vor. Die übrigen 18 Kapitel waren
maschinell umsortiert (Begriffe nach hinten, erste Überschrift in „Das Problem: …“ umbenannt, „Auf einen
Blick“ ans Ende, Klasse klein durch t2 ersetzt), inhaltlich aber unverändert. Der Umbau ist jetzt
inhaltlich nachgeholt.

## Was in jedem Kapitel geändert wurde

- Der Kern beginnt mit einem echten Problem aus dem Fall des Abschnitts „Worum es geht“, nicht mit einer
  Definition. Der Fall wird zu Ende erzählt, bevor Fachwörter fallen.
- Wo eine Grundlage fehlte, steht sie jetzt als eigener Baustein vor dem Verfahren, in Alltagsworten.
- Die vorhandenen Originale, Varianten, Selbstchecks und Quellen sind unverändert.

## Kapitel mit neu gebauten Abbildungen

| Kapitel | Neu | Grund |
|---|---|---|
| A2 | A2-1 Treppe mit echten Beträgen, A2-2 sinkende Restschuld, A2-3 Deckungsbeitrag | Die alten Bilder trugen Platzhalter statt Zahlen (§9 der Vorlage verlangt die Zahlen des Kapitelbeispiels) |
| A4 | A4-1 acht Bit als ein Byte, Faktor 8 zwischen Leitung und Datei | häufigste Falle des Kapitels, vorher nur im Fließtext |
| A7 | A7-1 Variablen und Zuweisung, A7-2 Feld mit Index 0 bis 4 | der Leser kann nicht programmieren, die Bausteine fehlten ganz |
| A8 | A8-1 Symbol-Legende aller drei Diagrammarten mit Alltagswort | die Symbole wurden benutzt, aber nie zusammenhängend gezeigt |
| A9 | A9-1 flache Tabelle gegen zwei Tabellen mit Verweis, A9-2 Aufbau einer Tabelle | Tabelle, Zeile, Primär- und Fremdschlüssel waren vorausgesetzt |
| B5 | B5-1 mit neuer Spalte „Was sie tut“, B5-2 Fehlersuche als Treppe | Vorlage §9 verlangt Alltagsworte je Schicht und die Schrittfolge; B5 ist Grundlage für A1 |

In A9, A8, A4 und B5 wurden die vorhandenen Abbildungen dadurch umnummeriert; alle Verweise im Fließtext
wurden nachgezogen. In A7 war zusätzlich ein Verweis im Aufgabenteil betroffen.

## Neue Zahlen

Nur in A2: Tilgungsplan 9.000,00 EUR / 3 Jahre / 5,0 % und das Deckungsbeitragsbeispiel 80,00 / 50,00 /
12.000,00 / 400 Stück. Beide mit python nachgerechnet und in notizen/RECHNUNGEN-a2.md protokolliert.
Für das Darlehen wurden bewusst andere Zahlen als in der Originalaufgabe gewählt, damit die Aufgabe eine
Aufgabe bleibt. Alle anderen Kapitel kamen ohne neue Zahlen aus.

## Reparaturen an Schäden der maschinellen Umbenennung

Die Ersetzung von „klein“ durch „t2“ traf auch den Fließtext. Drei Stellen waren sinnentstellend und
wurden zurückgesetzt: B7 „die Menge bleibt klein“ und „Sie bleibt dadurch klein“, B8 „Der Bildschirm ist
klein“. Eine Suche über alle Kapitel zeigt keine weitere Stelle.

## Abweichungen von der Vorlage, mit Begründung

- **A7, Struktogramm-Legende (Vorlage §9) nicht gebaut.** Im Kapitel liegt keine Quelle für die Bedeutung
  der Symbole; die eiserne Quellenregel (BAUPLAN §2) hat Vorrang. Stattdessen liest ein Absatz das
  vorhandene Bild A7-4 als Struktogramm und verweist auf A8.
- **B5, NAS/SAN von Abbildung zu Tabelle.** Das Bild war faktisch eine Tabelle aus Rechtecken. Als Tabelle
  ist es kürzer und trägt eine dritte Zeile mit den in der Prüfung genannten Vorteilen. Damit bleibt B5
  bei sieben Abbildungen.
- **A8 mit acht Abbildungen** statt der empfohlenen vier bis sieben. Die Legende kommt hinzu, ohne dass
  eine der vorhandenen entbehrlich wäre; sie ist der eigentliche Einstieg für einen Leser ohne Vorwissen.
- **A8-Legende, Startknoten.** Das Gestaltungssystem kennt keine dunkel gefüllte Fläche. Der Kreis bleibt
  hell, die Zeile daneben sagt „ausgefüllter Kreis“.
- **B11 bei 4.494 Wörtern.** Der neue Einstieg wurde zweimal gekürzt und ein doppelter Satz im alten Text
  gestrichen, um unter der Obergrenze 4.500 zu bleiben. Weitere Kürzungen hätten Aussagen gekostet.
- **A7 bei 4.331 Wörtern.** Der Platz kommt aus den Begriffskarten, die auf den neuen Ton gekürzt wurden,
  weil der Kern die fünf Bausteine jetzt selbst erklärt. Zwei Sätze ohne Quelle sind entfallen.

## Teil 0

- Die Beschreibung des Kapitelaufbaus nannte noch die alte Reihenfolge mit den Begriffskarten an zweiter
  Stelle. Sie ist auf die verbindliche Folge gesetzt, ebenso der Arbeitsablauf („Fehlt dir ein Wort,
  schlag es hinten nach und lies weiter“).
- Der Abschnitt „Wenn du bei null anfängst“ ist neu: eine nummerierte Lesereihenfolge B5, A1, B9, A6, A2,
  A3, A4, A5, A7, A8, A9, B1, B2, B3, B4, B6, B7, B8, B10, B11, nur mit Links auf vorhandene ids, ohne
  Zeitangaben. Der frühere Fließtext mit einer anderen Reihenfolge ist ersetzt.

## Abnahme

bauen-in-bau.js: 28 Teile, 1.175 KB, 177 Glossareinträge, 186 Quellen, keine Fehler, neun Wörter-Hinweise
(a6, a7, a8, a9, b5, b7, b9, b10, b11 über dem Richtwert 3.500, alle unter der Obergrenze 4.500).
svgcheck.py: 123 Abbildungen, 0 Befunde. abnahme.js: keine Befunde, alle 18 geprüften Kapitel mit
vollständiger Kam-dran-Zuordnung. Sichtprüfung der Renderstreifen: A1, A2, A4, A7, A8, A9, B2, B5.
Der Koffer enthält weiterhin genau drei Dateien; die vorige Lerndatei liegt in
_sicherung_2026-09-08_vorlehrer/AP1_Lerndatei_koffer_alt.html.

- 2026-09-08, Nachtrag: In A1 Abb. A1-6 war der Router-Kasten mit Akzent gefuellt, der Text darin kaum lesbar. Jetzt weisser Kasten mit Akzentrahmen. Zusammenbau und Koffer danach aktualisiert.


# Entscheidungen W – Begriffe zugeklappt, Wegweiser Aufgabe -> Absatz (2026-09-08)

- Nutzerbefund: Die Begriffskarten waren nur nach hinten geschoben, nicht in Klartext umgeschrieben, und bleiben eine Wand. Beim Loesen von Pruefungsaufgaben fand er im Kapitel nicht die Stelle, die die Aufgabe beantwortet.
- Begriffe-Abschnitt in allen 20 Kapiteln in details/summary gelegt (Knopf Begriffe aufklappen (n Karten)). Ids unveraendert, Glossar-Links funktionieren (Chromium klappt details bei Sprung und Suche automatisch auf). Hinweis-Satz kurz gehalten, weil B11 sonst die 4500-Woerter-Grenze reisst.
- Jede h4-Zwischenueberschrift im Kern hat jetzt eine id <kapitel>-k<n> (Skript, fortlaufend).
- Wegweiser: 20 Sonnet-Agenten haben je Kapitel jede Teilaufgabe aus TIPPS-ZUORDNUNG.json einem Ziel zugeordnet (bevorzugt geloeste Originalaufgabe, sonst Zwischenueberschrift), Dateien notizen/WEGWEISER-<id>.json und .md (mit Luecken). pruef/wegweiser-bauen.py baut daraus je Kapitel eine Tabelle Pruefungsaufgaben zu diesem Kapitel und wo die Antwort steht am Ende von Worum es geht (in einem nav, damit check.js sie nicht als Lesetext zaehlt) und setzt in 03-matrix.html alle 252 Aufgabenzeilen auf das genaue Ziel.
- Gemeldete Inhaltsluecken (Aufgaben, zu denen das Kapitel nichts oder zu wenig sagt), noch offen: A1 IPv6 (H22 3.1-3.5: Vorteile, Praefix/Teilnetz ausschreiben, Anzahl Teilnetze, Adressvergabe, Ping) und F24 2.7; A2 einfache Kosten-/Arbeitstage-Rechnungen (H21 3.2/3.3, H22 1.6, H23 2.5); A4 Ratenrechnung H22 2.1, ASCII/Binaer F24 3.3, Jahreshochrechnung H25 2.5; A5 Lastanteil F24 3.8; A7 F25 3.5; A8 H23 1.1; B1 Autoupdate H21 4.2, Schutzbedarfskategorien H21 4.3, Bordmittel F23 3.5; B2 H23 3.4/3.6 (Wiederherstellungsschluessel, TPM); B3 H23 3.1 (zwei Gesetze), F25 2.1/2.2; B4 DVI, QR/RFID/Barcode, Cache, All-in-One, BIOS-Flashback; B5 F22 3.9; B7 JBOD (H22 2.5/2.6); B8 Homeoffice H23 2.4; B9 externe Projektberatung H22 1.5, Stakeholdergruppen H22 1.4; B10 F22 1.3 Leistungsangebote; B11 Werk-/Dienstvertrag H22 1.7 nur in Begriffen.

- 2026-09-08, Nutzerwunsch: Das Haekchen Sitzt ist komplett entfernt: Label in allen Kapiteln und Vorlagen, CSS-Regeln und data-kap in 00-kopf.html, Speicher-Skript in 99-fuss.html, Pflichtregel und Klasse in check.js, Satz in Teil 0. Abweichung von BAUPLAN Paragraf 10 (Haekchen im Kopf).

# Entscheidungen X – Lektionen selbst geschrieben (2026-09-08, ab 15 Uhr)

- Nutzerbefund: In 14 Kapiteln war der Kern nur ein Spickzettel mit neuem Einstiegsabsatz. Agentenschwaerme sind wegen Kontingent gestoppt; die Kerne werden jetzt nacheinander von Hand als Lektion geschrieben (Problem, Bausteine, Schritte mit Bild, Regel, Falle, Auf einen Blick am Ende), Begriffskarten in Klartext, Luecken aus WEGWEISER-<id>.md geschlossen, WEGWEISER-<id>.json angepasst, nach jedem Kapitel Zusammenbau und Koffer.
- B7 fertig: neue Abb. B7-4 (drei RAID-Grundideen, Pruefsumme als Quersumme), JBOD-Abschnitt (b7-k9) aus den Loesungshinweisen H22 2.5/2.6, Rechenschema ans Ende. 4286 Woerter.
- B1 fertig: neue Abschnitte b1-k14 (Schutzziele als drei Fragen), b1-k15 (Schutzbedarf normal/hoch/sehr hoch mit H21-Tabelle), b1-k16 (Least Privilege); Zutrittstechnik, Autoupdate/Rollentrennung, Bordmittel, Minimalkonfiguration, mobiles Arbeiten (F24 4.1) und Risiko-Situationen (H24 1.2) ergaenzt; vier IHK-Quellen ohne URL neu (q10-q13). 3983 Woerter.
- B9 gezielt ergaenzt (Bedarfsanalyse-Methoden erklaert, formale Angebotsangaben, Stakeholdergruppen mit Einfluss, externe Projektberatung Vor-/Nachteile; Abb. B9-1 Bildunterschrift berichtigt). B2 gezielt ergaenzt: neuer Abschnitt b2-k12 (Datentraegerverschluesselung, TPM, Wiederherstellungsschluessel mit H23-Tabelle), WPA-Abschnitt in Klartext, acht Begriffskarten in Klartext, Quellen q19 (IHK H2023) und q20 (TCG TPM 2.0) ohne URL.
- A3 gezielt umgebaut: Zwischenueberschriften in Klartext, Teilnutzwert am Zahlenbeispiel, zwei Schreibweisen der Gewichte (Prozent/Punkte), Tabelle ausfuellen mit Rueckwaertsrechnung (F24 1.1) und Bewertung 1-3 (H22 3.7), neuer Abschnitt a3-k6 Entscheidung begruenden (F23 1.3/1.4), sieben Karten in Klartext, Quellen q6/q7 (IHK F2023, H2022).
- A5 gezielt umgebaut (2026-09-09): Baustein 1 erklaert Spannung, Stromstaerke und Leistung von null (Wasserleitungs-Bild) und rechnet das USB-Beispiel aus H25 3.5/3.6 durch (24 V x 0,5 A = 12 W; 12 W / 5 V = 2,4 A; USB 2.0 liefert 0,5 A, USB 3 0,9 A, deshalb Stoerungen; neue Quelle usb-2-0-strom in QUELLEN-A). Neuer Baustein 2 Ueberlastnachweis (a5-k9) mit H21 2.4 (3.680 W Grenze, 4.140 W Bedarf) und Balkenbild Abb. A5-2; die alte Pruefungsnotiz 230 V ist Fliesstext. Baustein 3 erklaert die Kilowattstunde von null. Neuer Baustein 5 Lastanteil (a5-k10) mit der F24-3.8-Rechnung (260,00 EUR, Ersatzwert 300,00 EUR). Rechenweg-Schema hinter die Bausteine verschoben; Reserve, Amortisation und USV mit je einem Einstiegssatz; alle 8 Karten in Klartext. Bilder A5-2 bis A5-4 zu A5-3 bis A5-5 durchnummeriert. 4064 Woerter, check/vorschau/abnahme ohne Befund, Koffer aktualisiert. Wegweiser: H21 2.4 -> a5-k9, F24 3.8 -> a5-k10, H25 3.5/3.6 -> a5-k2.
- B4 Kern komplett neu als Lektion (2026-09-09): Problem (drei Auftraege), Baustein 1 Was in einem Rechner steckt (Buero-Bild: CPU Sachbearbeiter, RAM Schreibtisch, Laufwerk Aktenschrank) mit neuer Abb. B4-1 Datenweg Laufwerk-RAM-Cache-CPU und Cache-Erklaerung (F22 2.10); CPU Kerne/Threads (F22 2.9, 16/32); CPU-Einbau drei Schritte und zwei Punkte (F22 2.1/2.2); Waermeleitpaste (F22 2.3); RAM vier Fragen + Dual Channel mit A1/B1-Belegung aus dem Heft (F22 2.4); DDR-3200; HDD/SSD (H24 3.4); SATA/M.2/NVMe (F22 2.5); Anschluesse erkennen mit DVI statt Klinke in Abb. B4-5 (F22 2.6, F24 1.4, F25 1.4), USB-Tabelle vereinfacht, USB-C-Vorteile (F22 2.8); neuer Abschnitt BIOS FlashBack (b4-k14, F22 2.7); Funksymbole; Bildschirm/Drucker kurz; vier Bauformen mit All-in-One statt Tablet in neuer Abb. B4-7 (F23 1.1); neuer Abschnitt Barcode/QR/RFID (b4-k15, H22 2.8). Bilder umnummeriert (Originale/Variante jetzt B4-8/B4-9). Karten: Was es ist in Klartext, IHK-Zeilen gekuerzt. Quellen q13-q20 (IHK F22/H22/F23/F24, DDWG DVI, ISO/IEC 18004, ISO/IEC 18000, ASUS FlashBack; vier neue Schluessel in QUELLEN-B). 4470 Woerter (Grenze 4500), check/vorschau/abnahme ohne Befund, Koffer aktualisiert. Wegweiser-Ziele neu: 2.7 -> b4-k14, 2.10 -> b4-k13, H22 2.8 -> b4-k15.
- B3 Kern als Lektion neu geschrieben (2026-09-09), Bilder und Tabellen unveraendert uebernommen: Problem (Datensicherheit vs. Datenschutz als zwei Fragen, personenbezogene Daten von null, drei Rollen am Haendler/Systemhaus-Fall); neuer Baustein 1 Gesetze (b3-k13): DSGVO als EU-Verordnung seit 25.5.2018, BDSG als deutsche Ergaenzung, Zweck der DSGVO im Wortlaut der Loesung F25 2.2, Antwortliste H23 3.1 (DSGVO, BDSG; IHK liess auch StGB, Art. 10 GG, Landesgesetze gelten); sieben Regeln Art. 5 in Alltagsworten; Rechtsgrundlage als Erlaubnisgruende mit Einwilligung als Nicht-Allzweckantwort; Art. 9 mit H21 4.4 und H25 3.1; Informieren vs. Auskunft; Rechte; Monatsfrist; TOM technisch/organisatorisch erklaert; Datenschutzbeauftragter; Datenpanne 72 h; Bussgeld; KI/Drittland. Neue Merke-Boxen Typischer Fehler und Pruefungsnotiz; Auf einen Blick um Gesetze ergaenzt. Karten Was es ist in Klartext. Quellen q7-q9 (IHK H2023, F2025, H2021; Schluessel vorhanden). 3929 Woerter, check/vorschau/abnahme ohne Befund, Koffer aktualisiert. Wegweiser: H23 3.1, F25 2.1, F25 2.2 -> b3-k13.
- A8 gezielt ergaenzt (2026-09-09): H23 1.1 (Anwendungsfalldiagramm ergaenzen) als vierte geloeste Originalaufgabe a8-original-4 mit neuer Abb. A8-9 (Musterloesung, farbig die einzutragenden Akteure und Anwendungsfaelle, include vom Hauptfall zum Teilschritt; Merkhilfe: das Wort beinhaltet im Aufgabentext signalisiert include) plus Variante a8-variante-4 (Fahrradverleih). check meldet nur den Hinweis 4 Originale. 3881 Woerter, vorschau/abnahme ohne Befund, Koffer aktualisiert. Wegweiser H23 1.1 -> a8-original-4.
- Reststand (2026-09-09, fuer Uebergabe): offen sind B8 (H23 2.4 Homeoffice in den Kern), B10 (F22 1.3 Leistungsangebote), B11 (H22 1.7 Werk-/Dienstvertrag; vorher Karten kuerzen, 4488 Woerter), A7 (F25 3.5 Schreibtischtest ohne Schleife), A4 (H22 2.1 Ratenrechnung, F24 3.3 ASCII vs. Binaer, H25 2.5 Jahreshochrechnung), A2 (H21 3.2/3.3, H22 1.6, H23 2.5 einfache Kostenrechnungen), A1 (IPv6: H22 3.1-3.5, F24 2.7), zuletzt B6 (Kern nur stilistisch, keine Luecke). Vorgehen je Kapitel: Skript im Scratchpad, check, vorschau, bauen, abnahme, Koffer, Wegweiser-JSON, dieser Abschnitt.
- B8, B10, B11 gezielt ergaenzt (2026-09-09): B8 neuer Abschnitt b8-k10 Homeoffice Vor-/Nachteile fuer Beschaeftigte mit Tabelle aus den Loesungshinweisen H23 2.4 (Hinweis: Sicht der Beschaeftigten, nicht der Firma); B10 neuer Abschnitt b10-k13 Leistungsangebote als Nutzen-Saetze (alle acht Begriffe aus F22 1.3, Satzbauplan Wir ... damit Sie ...); B11 neuer Abschnitt b11-k13 Werk- vs. Dienstvertrag (Ergebnis vs. Bemuehen, H22 1.7 Empfehlung Werkvertrag), dafuer in allen zehn Karten So fragt die IHK und Wo es dir begegnet auf den ersten Satz gekuerzt (139 Woerter). Woerter: B8 3506, B10 4209, B11 4479. check/bauen/abnahme ohne Befund, keine Bildaenderungen, Koffer aktualisiert. Wegweiser: H23 2.4 -> b8-k10, F22 1.3 -> b10-k13, H22 1.7 -> b11-k13.
- A7, A4, A2 gezielt ergaenzt (2026-09-09): A7 neuer Abschnitt a7-k12 Schreibtischtest ohne Schleife (F25 3.5, drei Zuweisungen, Rechenweg 2,75 / 46,35 / 37,05, typische Fehler Reihenfolge und Klammer), Karten IHK-/Begegnet-Saetze auf den ersten Satz gekuerzt (37 Woerter), 4476 Woerter. A4 neue Abschnitte a4-k7 Ratenrechnung (H22 2.1, 72.000 Aufnahmen), a4-k8 Jahreshochrechnung und Kompression (H25 2.5, 9,91 bzw. 12,18 GiB, IHK-Aufrundung 9,92/12,19 offengelegt), a4-k9 ASCII- gegen Binaerformat (F24 3.3); Quelle a4-q9 IHK H2022. A2 neue Abschnitte a2-k9 einfache Kostenketten und interner Stundensatz (H21 3.2/3.3, H22 1.6: 5.200 EUR, 2,5 Tage, 81,59 EUR/h) und a2-k10 Mischkalkulation (H23 2.5, fuenf Schritte bis 2,40 EUR/min); Quellen a2-q10 bis q12 (IHK H2021, H2022, H2023). Keine Bildaenderungen. check/bauen/abnahme ohne Befund, Koffer aktualisiert. Wegweiser: F25 3.5 -> a7-k12; H22 2.1 -> a4-k7; H25 2.5 -> a4-k8; F24 3.3 -> a4-k9; H21 3.2/3.3, H22 1.6 -> a2-k9; H23 2.5 -> a2-k10.
- A1 IPv6 ergaenzt (2026-09-09): neuer Baustein a1-k12 IPv6 verstehen (Platzproblem von IPv4, 2^128, Vorteile fuer IoT aus H22 3.1; Aufbau Standortpraefix 48 Bit / Teilnetz-ID 16 Bit / Interface-ID 64 Bit mit neuer Abb. A1-9; H22 3.2 Loesung 2001:0da8:5f2d und 0028; H22 3.3 2^16 = 65.536; F24 2.3 fe80-Adresse ausgeschrieben, 128 Bit, /64, Interface-ID), neuer Abschnitt a1-k13 IPv6 im Netzbild (H22 3.4 Adressvergabe ::18/::19, Gateway = Router ::1; Loopback ::1 und Link-Local fe80:: ; ping-Befehle H22 3.5; H22 3.6). Absatz zu F24 2.7 (IP- und MAC-Adresse aus ipconfig zuordnen) unter a1-k10. Quellen a1-q12 (IHK H2022), q13 (IHK F2024), q14 (RFC 4291, neu in QUELLEN-A). check/vorschau (9 Abbildungen ohne Befund)/bauen/abnahme gruen, Koffer aktualisiert. Wegweiser: H22 3.1-3.3, F24 2.3 -> a1-k12; H22 3.4-3.6 -> a1-k13; F24 2.7 -> a1-k10.
- B6 ergaenzt (2026-09-09): sechs Einzeiler-Abschnitte des Kerns (Betriebssystem als Hausmeister mit fuenf Aufgaben, drei Wege selbst/kaufen/vergeben, vier Argumente gegen Fremdvergabe erklaert, Verteilsoftware am Zwoelf-Rechner-Beispiel, Copyleft vs. permissiv mit Folge fuer eigene Produkte, Frontend/Backend) um je einen Erklaerabsatz von null erweitert; Quellen bestehend (q2, q3, q5, q6, q7). Keine Bildaenderungen. check/bauen/abnahme gruen, Koffer aktualisiert.
- ABSCHLUSS Abschnitt X (2026-09-09): Alle 14 schwachen Kapitel bearbeitet (B7, B1, B9, B2, A3, A5, B4, B3, A8, B8, B10, B11, A7, A4, A2, A1-IPv6, B6). Alle in ENTSCHEIDUNGEN W gemeldeten Inhaltsluecken sind geschlossen, jede Wegweiser-Zeile zeigt auf einen Absatz, der die Aufgabe wirklich beantwortet. Koffer: genau drei Dateien, Lerndatei Stand heute.
- Uebergabe an Codex (2026-09-09): Arbeitsauftrag mit acht Verbesserungsideen aus der Lernsitzung RAID steht in notizen/AUFTRAG-CODEX-2026-09-09.md (Einheiten 1-8, Abschlussroutine, Reststand-Regel). Codex protokolliert unter Abschnitt Y.

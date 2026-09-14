# Prüfbefunde Phase F – fachliche Gegenprüfung (2026-09-06/07)

Fünf unabhängige Kontrolleure (Modell Opus), die keines der Kapitel geschrieben haben, haben in allen 20 Kapiteln
jede Original-Aufgabe gegen den amtlichen Lösungskern der Extraktionsnotizen und jede Übungsvariante durch eigenes
Lösen geprüft. Jede Zahl wurde mit Node oder Python nachgerechnet (Netzpläne komplett, Pseudocode als lauffähiges
Programm ausgeführt, SQL in SQLite gegen Testdaten, Datumsfristen mit Date). Protokolle je Kapitel: Abschnitt
„Kontrolle 2026-09-06“ in notizen/RECHNUNGEN-<kapitel>.md.

Umfang: 54 Original-Aufgaben, 54 Varianten, zusätzlich 6 Netzpläne (55 Knoten), 8 Programme, alle SQL-Abfragen,
alle Kam-dran-Punktsummen, Rechts- und Normangaben in B3, B7, B8, B9, B11. Damit weit über den 40 Stichproben aus §12.

| Kapitel | Stelle | Befund | Korrektur |
|---|---|---|---|
| A1 | a1-original-1 (H24 1.5) | Aufgabendaten frei erfunden (Netz .100.0/26, DNS-Server); amtlich: 192.168.20.0/24, DHCP .20–.254, Router .1 | Aufgabe, Lösung und Punktelogik nach Notiz ersetzt |
| A1 | a1-original-2 (H25 3.7) | Falsche Aufgabe (IPv6-Kürzung); H25 3.7 ist die IPv4-Konfiguration des Kartenterminals | Ersetzt: 172.16.10.254 / 255.255.255.0 / GW 172.16.10.1 |
| A1 | a1-variante-2 | Trainierte nach der Korrektur nicht mehr das Verfahren des Originals | Ersetzt durch 10.10.5.64/27 (Netz, Broadcast, GW, letzte Hostadresse) |
| A2 | a2-original-1 (H24 3.1) | Erfundene Werte (24.000 €, 4 Jahre, 5 %); amtlich 12.000 €, 36 Monate, 6 % | Ersetzt: Zinsen 720/480/240, Summe 13.440 € |
| A2 | a2-original-1 Punkte | Vier Jahreszeilen behauptet; Notiz weist 7 P ohne Einzelaufteilung aus | Punktelogik korrigiert |
| A2 | a2-original-2 (H25 1.3) | Fragestellung und Punktelogik falsch (Überweisungsbetrag statt Skontobetrag) | Auf amtliche Frage korrigiert (1 P Ansatz, 1 P Ergebnis) |
| A3 | a3-original-1 (F25 1.1) | Falsches Verfahren (gewichtete Nutzwertanalyse); amtlich ungewichtete Rangmatrix 4/11/9 | Ersetzt |
| A3 | a3-original-1 Punkte | „je 1,5 Punkte“ als amtlich dargestellt; Notiz: nicht belegt | Als Näherung gekennzeichnet |
| A3 | a3-original-2 (F24 1.2) | Erfundene Duplexdruck-Entscheidung; amtlich vier CAD-Angebote, K.-o. für SaaS-Anbieter 3, Zuschlag Anbieter 4 | Ersetzt |
| A3 | a3-variante-1 | Passte nicht mehr zum korrigierten Original | Ersetzt durch ungewichtete Rangmatrix (NAS 8/9/7) |
| A4 | a4-original-1 (H25 2.4) | Falsche Aufgabe (Scan-Speicherbedarf); amtlich 336 Rechnungen × 124 kB → 40.688 KiB | Ersetzt |
| A4 | a4-original-2 (F24 4.7) | Erfundene Werte (750 GiB, 80 %); amtlich 1 GiB bei 50,02 Mbit/s → 171,73 s ≈ 2 min 52 s | Ersetzt, amtliche Punktesechstelung ergänzt |
| A4 | a4-variante-1 | Passte nicht mehr zum Original | Ersetzt (432 Vorgänge à 86 kB, 36.281 KiB/Tag, 1.062,92 MiB in 30 Tagen) |
| A4 | a4-variante-2 | Zwischenschritt inkonsistent notiert (0,544 × 60 = 32,66) | Auf 0,5444 × 60 = 32,66 berichtigt |
| B2 | b2-original-1 (H25 3.9) | Schutzziel Authentizität fehlte; amtlich Herkunft und Integrität | Satz ergänzt |
| B8 | Die Sache, Nachhaltigkeit | Maßnahmen zu H21 2.3 falsch wiedergegeben (Energiesparoptionen statt Monitore mit Energielabel) | Nach Lösungshinweis korrigiert |
| B8 | Abb. B8-2, Selbstcheck 2 | Alternativtext dem WCAG-Prinzip „Robust“ zugeordnet; gehört zu „Wahrnehmbar“ (1.1.1) | Abbildung und Antwort korrigiert |
| B9 | Vom Bedarf zum Auftrag | „Teilleistungen“ beim Pflichtenheft; H24 4.1 führt sie beim Lastenheft | Gestrichen |
| B9 | Methoden der Bedarfsanalyse (H23 1.4) | „Beobachtung“ nicht im Lösungshinweis, „Medienanalyse“ fehlte | Liste nach Lösungshinweis korrigiert (Kern und Selbstcheck) |
| B10 | Veränderung führen (H25 1.7) | Ursache „Überforderung“ fehlte | Ergänzt |

Ohne Befund: A5, A6, A7, A8, A9, B1, B3, B4, B5, B6, B7, B11.

Gewollt stehen geblieben (IHK-Abweichungen mit Fußnote, §2 Regel 6): H21 2.1 (78,94 W statt 78,95 W), H22 2.5 (TiB statt TB),
H23 4.9 (Monatsdifferenz am Jahreswechsel), H22 4.5 (fehlendes Attribut in der Lösungsskizze), H25 3.1 (pauschale Einwilligung).

Beobachtung ohne Korrekturbedarf: notizen/2024-herbst.md 2.4 nennt im Lösungskern zwei, in der Bemerkung drei Alternativstriche;
Kapitel A8 folgt dem Lösungskern.

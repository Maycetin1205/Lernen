# Quellen-Nachtrag Kapitel B9

Erstellt in Phase K-5 am 2026-09-06. Format nach BAUPLAN.md §5.2.
Grund: Vier Pflichtinhalte aus §6 (Muss-/Soll-/Kann-Kriterium, magisches Dreieck, Teamphase Adjourning, PDCA) haben in `QUELLEN-B.md` keine Quelle. Die Zeilen werden von der Bauleitung in `QUELLEN-B.md` übernommen; dieser Bauer ändert die Liste nicht.

| Schlüssel | Kapitel | Typ | Zitat | URL | Status | Abrufdatum | Fundstellen |
|---|---|---|---|---|---|---|---|
| rfc-2119 | b9 | RFC | Bradner, S.: RFC 2119 – Key words for use in RFCs to Indicate Requirement Levels, IETF 1997 | https://www.rfc-editor.org/rfc/rfc2119 | geprüft | 2026-09-06 | Abschnitte 1, 3 und 5 (MUST als absolute Anforderung, SHOULD als Empfehlung mit begründeten Ausnahmen, MAY als optional); Vorbild der Abstufung Muss-, Soll-, Kann-Kriterium |
| gabler-projektmanagement | b9 | Fachbuch | Hobel, B.; Schütte, S.: Projektmanagement (PM), in: Gabler Wirtschaftslexikon, Springer Fachmedien Wiesbaden | https://wirtschaftslexikon.gabler.de/definition/projektmanagement-pm-46130 | geprüft | 2026-09-06 | Definition Projektmanagement nach DIN 69901; Projektziele „qualitativ, termingerecht und im Kostenrahmen“ (die drei Größen des magischen Dreiecks) |
| tuckman-jensen-1977 | b9 | Fachbuch | Tuckman, B. W.; Jensen, M. A. C.: Stages of Small-Group Development Revisited, Group & Organization Studies, Vol. 2, No. 4, 1977, S. 419–427 | – | kostenpflichtig | 2026-09-06 | Ergänzung des Vier-Phasen-Modells um die fünfte Phase Adjourning (Auflösung) |
| bsi-grundschutz-sicherheitsprozess | b9 | Behörde | BSI: Online-Kurs IT-Grundschutz, Lerneinheit 2.1: Der Sicherheitsprozess, Bundesamt für Sicherheit in der Informationstechnik, Bonn | https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_2_Sicherheitsmanagement/Lektion_2_01/Lektion_2_01_node.html | geprüft | 2026-09-06 | PDCA-Zyklus nach Deming: Plan (Maßnahmen planen), Do (umsetzen), Check (Zielerreichung und Wirksamkeit prüfen), Act (Mängel beheben, verbessern); Einsatz auch im Qualitäts- und Umweltmanagement |

Prüfnotizen (alle am 2026-09-06 mit WebFetch):

- `rfc-2119`: Der Text bestätigt Titel, Autor (S. Bradner) und Jahr 1997. Abschnitt 1 definiert MUST als absolute Anforderung der Spezifikation, Abschnitt 3 SHOULD als Anforderung, von der es in begründeten Einzelfällen Ausnahmen geben kann, Abschnitt 5 MAY als wirklich optional. Das Fragment nutzt das als Herkunft der Abstufung Muss, Soll, Kann.
- `gabler-projektmanagement`: Verlag Springer Fachmedien Wiesbaden, Autoren Hobel und Schütte. Der Artikel zitiert DIN 69901 und nennt als Ziel des Projektmanagements, dass Projektziele „qualitativ, termingerecht und im Kostenrahmen“ erreicht werden. Der Ausdruck „magisches Dreieck“ selbst steht nicht im Artikel; das Fragment belegt damit die drei Zielgrößen und bezeichnet den Namen als gebräuchliche Bezeichnung.
- `tuckman-jensen-1977`: Bibliografische Angaben über die Crossref-Metadaten zu DOI 10.1177/105960117700200404 bestätigt (Titel, beide Autoren, Zeitschrift, Band 2, Heft 4, Seiten 419 bis 427, Dezember 1977). Der Volltext liegt hinter einer Bezahlschranke, deshalb Status „kostenpflichtig“ ohne URL; im Fragment „(nicht online geprüft)“.
- `bsi-grundschutz-sicherheitsprozess`: Die Seite beschreibt die vier Phasen Plan, Do, Check, Act, ordnet das Modell William Edwards Deming zu und nennt den Einsatz in Qualitäts- und Umweltmanagementsystemen. Gewählt statt ISO 9001, weil iso.org für den Abruf gesperrt war (HTTP 403) und die Norm ohnehin nur genannt, nicht zitiert werden sollte.

Nicht nachgetragen, weil bereits vorhanden: `din-69901-5` steht in `QUELLEN-A.md` (Kapitel a6, Status kostenpflichtig) und wird in B9 für die Begriffe Projekt, Meilenstein, Projektphase und Stakeholder mitverwendet; `bgb-werkvertrag` (b11, § 640 Abnahme) und `ihk-korrekturhinweise` (Teil 1) ebenso. Ein zweiter Eintrag wäre jeweils doppelt.

Nicht erreichbar am 2026-09-06: orghandbuch.de (HTTP 400) und iso.org (HTTP 403). Beide wurden deshalb nicht verwendet.

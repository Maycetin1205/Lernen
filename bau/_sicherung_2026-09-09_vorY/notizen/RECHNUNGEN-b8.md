# RECHNUNGEN B8 · Arbeitsplatz: Ergonomie, Barrierefreiheit, Nachhaltigkeit

Kapitel B8 ist ein reines Erklärkapitel. Weder die drei Original-Aufgaben noch die drei Varianten
enthalten eine Sachrechnung: Alle Lösungen bestehen aus Nennung, Erläuterung und Szenariobezug.
Die einzige Rechnung im Umfeld (H21 2.4, Belastbarkeit der Mehrfachsteckdose; Energiekostenrechnung)
liegt in A5 und wird dort protokolliert. Nachgerechnet und geprüft wurden deshalb nur die
Punkteangaben und die Zahlen- und Rechtsangaben des Fragments.

| Nr. | Angabe im Fragment | Prüfgrundlage | Ergebnis |
|---|---|---|---|
| 1 | Kam dran: H21 2.3 = 3 P | notizen/2021-herbst.md, 2.3 | stimmt |
| 2 | Kam dran: H23 2.1 bis 2.4 = 16 P | 4 + 4 + 4 + 4 aus notizen/2023-herbst.md | stimmt |
| 3 | Kam dran: H24 4.5 = 4 P | notizen/2024-herbst.md, 4.5 | stimmt |
| 4 | H24 4.5: 4 P, je Aspekt 2 P | Lösungshinweis, offene Liste, „andere Lösungen möglich" | stimmt |
| 5 | H23 2.2: 4 P, je Aspekt 2 P | Lösungshinweis nennt nur die vier Themenfelder | stimmt |
| 6 | H23 2.3: 4 P, je Möglichkeit 2 P | Lösungshinweis, vier Beispiele plus „weitere sinnvolle Antworten" | stimmt |
| 7 | Beleuchtungsstärke 500 lx nach DIN EN 12464-1 | QUELLEN-B.md, `dguv-215-410` | stimmt |
| 8 | Sehabstand 50 bis 70 cm, Aufstellung parallel zum Fenster | QUELLEN-B.md, `dguv-215-410` | stimmt |
| 9 | Kontrastverhältnis 4,5:1 (Stufe AA) | QUELLEN-B.md, `w3c-wcag-2-2`; W3C-Empfehlung abgerufen | stimmt |
| 10 | BFSG gilt seit 28. Juni 2025 im elektronischen Geschäftsverkehr | QUELLEN-B.md, `bfsg` | stimmt |
| 11 | ArbStättV § 1 Absatz 4 für Telearbeitsplätze (§ 3, § 6, Anhang Nr. 6) | gesetze-im-internet.de, ArbStättV § 1, abgerufen 2026-09-07 | stimmt, Absatz 4 ist richtig |
| 12 | Tischhöhe rund 72 cm, EU-Energielabel Skala A bis G | `dguv-215-410`, `eu-energielabel-2017` | stimmt |

## Kontrolle 2026-09-06

Geprüft: die drei Original-Aufgaben `b8-original-1` bis `b8-original-3` und die drei Varianten
`b8-variante-1` bis `b8-variante-3`.

Geprüfte Angaben je Original: Szenario gegen die Extraktionsnotiz, Vollständigkeit der Lösung
gegen den Lösungskern (Anzahl der Aspekte gleich Punktzahl), Punktzahl in `p.herkunft`,
Absatz „Punkte" gegen die amtliche Verteilung, fachliche Richtigkeit jeder Aussage.

- `b8-original-1` (H24 4.5, 4 P): Szenario, zwei beschriebene Aspekte (Energieverbrauch,
  Materialeinsatz) plus die weiteren Aspekte der offenen Liste (Emissionen, Ressourcenverbrauch
  der Herstellung, Entsorgung der Altmaschine) decken den Lösungskern vollständig ab. Ohne Befund.
- `b8-original-2` (H23 2.2, 4 P): Ergonomie und Anschlussmöglichkeiten erläutert, Softwarenutzung
  und Leistung als weitere Felder benannt; damit sind alle vier Themenfelder des Lösungshinweises
  abgedeckt. Ohne Befund.
- `b8-original-3` (H23 2.3, 4 P): externer Bildschirm und externe Tastatur mit Maus beschrieben,
  Docking-Station und Notebookständer ergänzt; deckt die vier Beispiele des Lösungshinweises ab.
  Ohne Befund.
- `b8-variante-1` bis `b8-variante-3`: unabhängig selbst beantwortet und verglichen. Jede Variante
  fragt dieselbe Sache wie ihr Original (ökologische Aspekte einer Neuinvestition; Tabletbetrieb
  gegen die Anforderungen an einen Bildschirmarbeitsplatz; ergonomische Ergänzungen zum Notebook),
  jede Lösung nennt die geforderte Anzahl an Aspekten samt Begründung. Ohne Befund.

Korrigiert wurden zwei Angaben außerhalb der Aufgabenblöcke, die eine Musterlösung falsch stützen:

1. Abschnitt „Die Sache", Absatz zur Nachhaltigkeit. Alt: „Genau diese drei Maßnahmen führen die
   Lösungshinweise zu Herbst 2021 als Vorschläge zur Senkung der Energiekosten auf". Der Satz
   davor nennt Energiesparoptionen, Steckdosenleisten und Thin Clients; die Lösungshinweise zu
   H21 2.3 nennen aber schaltbare Steckdosen, Monitore mit Energieeffizienzlabel und Thin Clients.
   Neu: „Als Vorschläge zur Senkung der Energiekosten nennen die Lösungshinweise zu Herbst 2021
   schaltbare Steckdosen, Monitore mit Energieeffizienzlabel und Thin Clients". Der Selbstcheck
   nannte die drei bereits richtig; der Widerspruch ist damit aufgelöst.
2. Abb. B8-2 und Selbstcheck 2 ordneten den Alternativtext dem WCAG-Prinzip „Robust" zu.
   Alternativtexte gehören zu Erfolgskriterium 1.1.1 und damit zum Prinzip „Wahrnehmbar";
   unter „Robust" steht Richtlinie 4.1 (Kompatibilität, 4.1.2 Name, Role, Value). Geprüft an der
   W3C-Empfehlung WCAG 2.2, abgerufen 2026-09-07. Neu: Abbildung „Maßnahme: standardkonformer
   Code"; Selbstcheck „Wahrnehmbar: Kontrast von mindestens 4,5:1 und Alternativtexte für Bilder …
   Robust: standardkonformer Code, damit Hilfsmittel den Inhalt auswerten können."

Ergebnis: `node pruef/check.js kapitel/27-b8.html --fragment` meldet nach beiden Änderungen
„Keine Fehler." (keine Hinweise; Wortzahl unter dem Richtwert).

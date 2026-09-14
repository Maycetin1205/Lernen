# Entscheidungen · Phase K-4 · Kapitel B7 (Datensicherung und Verfügbarkeit)

Stand 2026-09-05. Nur echte Entscheidungen, die der Plan offenlässt.

1. **Reihenfolge der Original-Aufgaben nach Punkten, nicht nach Jahr.** Der Auftrag nennt
   „punktreichste und jüngste zuerst". Beides ist hier nicht gleichzeitig möglich: Die punktreichste
   Aufgabe (H21 3.6, 7 P) ist zugleich die älteste. Ich habe nach Punkten absteigend sortiert
   (7 P, 4 P, 3 P), weil die 7-Punkte-Aufgabe das Kapitelthema am vollständigsten abdeckt.

2. **Drei von sieben Teilaufgaben als Original.** Gewählt: H21 3.6 (RAID erklären und entscheiden),
   H22 2.4 (RAID-5-Kapazität rechnen), F24 4.3 (externe Medien). Nicht als eigene Aufgabe, sondern in
   Kern, Variante und Selbstcheck verarbeitet: H21 4.6 und 4.7 (Sicherung auf derselben Platte,
   Verbesserungsvorschlag) als Aufhänger der 3-2-1-Regel, H22 2.5 und 2.6 (JBOD) in Variante 2.
   Grund: höchstens drei Originale erlaubt, und das Wortbudget lässt keine sieben Aufgaben zu.

3. **Eigenes Wochenbeispiel für das Rechenschema.** Keine der sieben Teilaufgaben rechnet
   Speicherbedarf von Voll-, differenzieller und inkrementeller Sicherung. Der Auftrag verlangt das
   Schema trotzdem für Phase V. Ich habe ein eigenes Beispiel gesetzt (500 GB Bestand, 20 GB Änderung
   je Tag, Vollsicherung Sonntag) und es in RECHNUNGEN-b7.md als Lehrbeispiel ohne IHK-Abgleich
   gekennzeichnet. Die Zahlen sind rund, damit man sie im Kopf nachvollziehen kann.

4. **Wiederherstellungsziel „Stand Donnerstagabend".** Die Pflichtabbildung verlangt die
   Wiederherstellungskette „am Donnerstag". Das ist mehrdeutig. Gewählt: Die Sicherungen laufen
   abends, wiederhergestellt wird der Stand von Donnerstagabend. Ergebnis: differenziell zwei,
   inkrementell fünf Sicherungen. Damit erscheint die Vollsicherung in beiden Ketten und die
   Gegenüberstellung ist sauber.

5. **Zehn Begriffskarten, drei Zusammenfassungen.** Fünfzehn Pflichtbegriffe passen nicht in zehn
   Karten. Zusammengelegt: „Wiederherstellung, RPO und RTO", „RAID-Level und Nutzkapazität",
   „Verfügbarkeit, MTBF und USV". Hot Spare blieb eigenständig, weil er sonst die RAID-Karte über
   120 Wörter getrieben hätte.

6. **Neue Quelle für Hot Spare.** QUELLEN-B.md hat für den Pflichtbegriff Hot Spare keine Quelle.
   Ich habe Microsoft Learn „Hot Sparing" (VDS) am 2026-09-05 selbst per WebFetch geprüft und die
   fertige Tabellenzeile nach QUELLEN-B-NACHTRAG-b7.md geschrieben, Schlüssel `ms-hot-sparing`.
   QUELLEN-B.md selbst bleibt unverändert.

7. **USV-Quelle aus QUELLEN-A.md übernommen.** `iec-62040-3` ist dort für A5 geführt (kostenpflichtig,
   ohne URL). Ich verwende sie für den einen USV-Satz in B7, statt einen zweiten Schlüssel zu erfinden.
   Ein Nachtrag wäre eine Dublette.

8. **Aufbewahrungsfristen mit acht Jahren für Buchungsbelege.** Die Fundstellenspalte in QUELLEN-B.md
   nennt nur „10 bzw. 6 Jahre". Ich habe die beiden dort als geprüft geführten URLs am 2026-09-05
   selbst gelesen: § 257 Abs. 4 HGB und § 147 Abs. 3 AO nennen zehn, acht und sechs Jahre. Die acht
   Jahre stehen deshalb im Fragment. Die Änderung wird ohne Gesetzesnamen und ohne Jahreszahl
   erwähnt („gegenüber früheren Fassungen verkürzt"), weil der abgerufene Paragraftext das
   Vierte Bürokratieentlastungsgesetz nicht selbst nennt und ich es nicht belegen kann.

9. **Verfügbarkeitsjahr mit 365 Tagen.** 8.760 h je Jahr, keine Schaltjahre, keine 365,25 Tage.
   Das ist die Rechnung, die zu den Vorgabewerten 8,76 h und 52,56 min führt, und die einfachste.

10. **Drei statt vier Abbildungen.** Zeitstrahl, 3-2-1-Aufbau und RAID-Schema decken die drei
    Mechanismen des Kapitels ab. Eine vierte hätte nur wiederholt, was Tabelle oder Rechenschema
    schon zeigen; §9 verbietet das ausdrücklich.

11. **Abgrenzungen als Link statt als zweite Erklärung.** USV-Aufbau und Überbrückungszeit → A5,
    Schutzziel Verfügbarkeit und Angriffe → B1, Löschpflichten für personenbezogene Daten → B3,
    TB gegen TiB → A4. Der Einheitenwiderspruch aus H22 2.5 steht als Prüfungsnotiz im Kapitel,
    die Einheitenlehre selbst nicht.

12. **JBOD-Zahl 20 TB, nicht 20 TiB.** Der IHK-Lösungshinweis zu H22 2.5 beschriftet das Feld mit
    TiB, obwohl der Aufgabentext TB verlangt. Die Aufgabe erscheint hier nur in Variante 2 mit
    eigenen Zahlen; dort wird konsequent TB gerechnet. Der Widerspruch selbst ist als Prüfungsnotiz
    benannt, ohne die falsche Einheit zu übernehmen.

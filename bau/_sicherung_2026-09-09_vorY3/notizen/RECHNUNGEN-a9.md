# Rechnungen Kapitel A9 · Datenmodell und ER-Diagramm

Stand: 2026-09-03. Phase K-2, Bauer a9. Grundlage: BAUPLAN.md §2 Regel 6.
Jede Zahl, die im Fragment `kapitel/18-a9.html` steht, ist hier mit Eingabe, Ausgabe und Abgleich
gegen den Lösungshinweis aus `notizen/<jahr>-<saison>.md` protokolliert.
Alle Befehle wurden mit Node ausgeführt (`node -e "…"`).

A9 ist ein Zeichen- und Modellierkapitel. Zahlen treten an drei Stellen auf: in den amtlichen
Punkteverteilungen, in den beiden Mengenbeispielen des Kerns und in der Monatsdifferenz aus H23 4.9.

## 1. Punkteverteilungen der Original-Aufgaben

Eingabe:

    console.log('H25-4.4 Punkte:', 2+2+1+2+1);
    console.log('H24-4.2 Punkte:', 1+1+1+1+1+1);
    console.log('F23-4.6 Punkte:', 1+1+1+1);
    console.log('H23-4.6 Punkte:', 1+1+1+1+1);

Ausgabe:

    H25-4.4 Punkte: 8
    H24-4.2 Punkte: 6
    F23-4.6 Punkte: 4
    H23-4.6 Punkte: 5

Abgleich mit den Notizen:

- H25 4.4 (`2025-herbst.md`, Zeile „Lösungskern“): ausdrücklich gedruckte Aufteilung
  zwei ergänzte Entitäten je 1 P = 2 P, zwei Kardinalitäten = 2 P, Primärschlüssel in allen drei
  Entitäten = 1 P, sinnvolle Attributzuordnung = 2 P, Dosierung an der n:m-Beziehung = 1 P.
  Summe 8 P, stimmt mit dem Heftwert 8 P überein.
- H24 4.2 (`2024-herbst.md`): je 1 Punkt für jede Kardinalität, jede Tabelle und jedes Feld an der
  richtigen Stelle. Die Notiz listet genau sechs zu ergänzende Elemente. 6 × 1 P = 6 P, stimmt.
- F23 4.6 (`2023-fruehjahr.md`): der Sache nach je 1 Punkt für SELECT/FROM, Datumsbedingung,
  Summenbedingung, Ausschluss der Garagenfahrzeuge. 4 × 1 P = 4 P, stimmt mit dem Heftwert.
  Die Notiz vermerkt ausdrücklich: keine ausdrückliche Aufteilung in den Lösungshinweisen,
  die Vierteilung ist aus der Sache abgeleitet. Im Fragment ist das als Konvention gekennzeichnet.
- H23 4.6 (`2023-herbst.md`): wörtlich „Je 1 Punkt für die zwei Beziehungen mit den Kardinalitäten,
  jeweils 1 Punkt für die Attribute.“ Zwei Beziehungen + drei fehlende Attribute = 5 P, stimmt.
  Diese Aufgabe wird im Fragment nicht als Original geführt, sondern nur im Kern erwähnt.

## 2. Punktesumme des Kapitels (Kontrolle der Zeile „Kam dran“)

Eingabe:

    const p=[3,4,4,6,3,4,5,2,3,3,6,2,2,2,2,2,8];
    console.log('Anzahl Teilaufgaben:', p.length, 'Summe:', p.reduce((a,b)=>a+b,0));
    console.log('H22:', 3+4+4+6, 'F23:', 3+4, 'H23:', 5+2+3+3, 'H24:', 6, 'F25:', 2+2, 'H25:', 2+2+2+8);
    console.log('Kam-dran-Summe:', 17+7+13+6+4+14);

Ausgabe:

    Anzahl Teilaufgaben: 17 Summe: 61
    H22: 17 F23: 7 H23: 13 H24: 6 F25: 4 H25: 14
    Kam-dran-Summe: 61

Abgleich: `notizen/MATRIX.md` Zeile 17 nennt für A9 die Prüfungswerte 17, 7, 13, 6, 4, 14 und die
Summe 61 bei 6 von 9 Prüfungen. Die Teilaufgabenliste in MATRIX.md §A9 enthält 17 Einträge.
Beides stimmt mit der Rechnung überein. Die Zeile „Kam dran“ im Fragment übernimmt genau diese Werte.

## 3. Mengenbeispiel Redundanz (Kern, Schritt 6)

Eingabe:

    console.log('Adresse 14 Tickets, Aenderungen vorher/nachher:', 14, 1, 'Ersparnis:', 14-1);

Ausgabe:

    Adresse 14 Tickets, Aenderungen vorher/nachher: 14 1 Ersparnis: 13

Herkunft der Zahlen: frei gewähltes Lehrbeispiel des Kapitels, kein Prüfungswert. Steht ein Kunde
mit 14 Tickets in einer einzigen flachen Tabelle, so ist seine Adresse 14-mal gespeichert; nach dem
Auslagern in eine eigene Kundentabelle einmal. Bei einem Umzug sind statt 14 Zeilen nur noch
1 Zeile zu ändern, also 13 Änderungen weniger. Abgleich: F25 4.8 nennt als Problem der Redundanz
die Inkonsistenz und den unnötigen Speicherbedarf; das Beispiel bildet genau diese Kette ab.

## 4. Mengenbeispiel n:m-Auflösung (Kern, Schritt 4)

Eingabe:

    console.log('nm max Zuordnungen 40*12:', 40*12);

Ausgabe:

    nm max Zuordnungen 40*12: 480

Herkunft der Zahlen: frei gewähltes Lehrbeispiel. 40 Mitarbeiter und 12 Projekte ergeben höchstens
40 × 12 = 480 Zuordnungen, die als Zeilen in der Beziehungstabelle stehen können. Kein Prüfungswert,
deshalb kein Abgleich mit einem Lösungshinweis nötig.

## 5. Monatsdifferenz aus H23 4.9 (Block „Typischer Fehler“)

Eingabe:

    const d=(a,b)=>Math.round((new Date(b)-new Date(a))/86400000);
    console.log('Ticket 2025-10-05, heute 2026-01-15, Alter in Tagen:', d('2025-10-05','2026-01-15'));
    console.log('Monatsdifferenz nach Formel: Month(2026-01-15) - Month(2025-10-05) =', 1-10);
    console.log('Bedingung > 2 erfuellt?', (1-10) > 2);
    console.log('Ticket 2026-01-31, heute 2026-04-01, Alter in Tagen:', d('2026-01-31','2026-04-01'));
    console.log('Monatsdifferenz:', 4-1, '> 2 ?', (4-1)>2);

Ausgabe:

    Ticket 2025-10-05, heute 2026-01-15, Alter in Tagen: 102
    Monatsdifferenz nach Formel: Month(2026-01-15) - Month(2025-10-05) = -9
    Bedingung > 2 erfuellt? false
    Ticket 2026-01-31, heute 2026-04-01, Alter in Tagen: 60
    Monatsdifferenz: 4 - 1 = 3 > 2 ? true

Ergebnis: Ein Ticket vom 05.10.2025 ist am 15.01.2026 genau 102 Tage alt, also deutlich älter als
zwei Monate. Die Bedingung `Month(NOW()) - Month(ErfassungDatum) > 2` liefert dafür −9 und ist
nicht erfüllt; das Ticket fehlt im Ergebnis. Umgekehrt liefert ein Ticket vom 31.01.2026 am
01.04.2026 den Wert 3, obwohl es erst 60 Tage alt ist. Abgleich: `2023-herbst.md`, Bemerkung zu 4.9,
vermerkt genau diesen Jahreswechselfehler; die Lösungshinweise sprechen ihn nicht an. Im Fragment
steht deshalb die IHK-Erwartung (reine Beschreibung des Verhaltens) und daneben der Fehler als
Block „Typischer Fehler“ mit den beiden nachgerechneten Datumsbeispielen.

## 6. Punkteverteilungen der drei Varianten

Eingabe:

    console.log('Variante1:', 2+2+1+2+1, 'Variante2:', 6*1, 'Variante3:', 1+1+1+1);

Ausgabe:

    Variante1: 8 Variante2: 6 Variante3: 4

Abgleich: Jede Variante übernimmt Struktur und Punktezahl ihrer Original-Aufgabe.

- Variante 1 (Seminarverwaltung) hat wie H25 4.4 genau zwei zu ergänzende Entitäten, zwei
  Kardinalitäten, drei Primärschlüssel, die Attributzuordnung und ein Attribut an der
  n:m-Beziehung: 2 + 2 + 1 + 2 + 1 = 8 Punkte.
- Variante 2 (Wartungseinsätze) hat wie H24 4.2 genau sechs zu ergänzende Elemente:
  Kardinalität n, Entität Wartungseinsatz, Einsatz-ID als Primärschlüssel, Einsatzbeginn,
  Einsatzende, Techniker_Telefon. 6 × 1 P = 6 Punkte.
- Variante 3 (Wartungsverträge) hat wie F23 4.6 genau vier Bewertungsstellen: SELECT/FROM,
  Datumsbedingung, Entgeltbedingung, Ausschluss über den Wahrheitswert. 4 × 1 P = 4 Punkte.

## 7. Zahlen ohne Rechnung

Folgende Zahlen im Fragment sind reine Textangaben aus den Notizen und enthalten keine Rechnung:
die Auftragsnummer 736298 (H22 4.1), die Grenzwerte 100.000,00 € (F23 4.6) und 5.000,00 €
(Variante 3), die Maße 2 mm, 200 mm und 300 mm (H22 4.3) sowie die Jahres- und Monatsangaben
2022 / Mai und 2024 / September. Sie werden unverändert beziehungsweise als bewusst geänderte
Variantenwerte übernommen.

## Abschlussprüfung K-2, 2026-09-03

Die vorhandenen Fragmente A5–A9 wurden fachlich korrigiert. Ausführung der erneuten
Rechnungen: node bau/pruef/k2-abschluss-check.js; Eingaben und Ergebnisse stehen in
k2-pruefung/NACHRECHNUNG.txt. Die bisherigen Abschnitte dokumentieren den Vorzustand.
Maßgeblich ist das korrigierte Kapitel; umsortierte Originale und Varianten sind über
ihre Prüfungsherkunft zuzuordnen, nicht über die frühere laufende Nummer.

## Kontrolle 2026-09-06

Kontrolleur K-5. Werkzeug: Python 3 mit `sqlite3` (Datei nur im Sitzungs-Scratchpad,
Wegwerfskript `a9sql.py`). Year() und Month() sind in SQLite nicht vorhanden und wurden als
Benutzerfunktionen registriert, damit die Abfragen aus dem Fragment wörtlich laufen.
Geprüft: H25 4.4, H24 4.2, F23 4.6 und die drei Varianten.

### SQL: Original F23 4.6 und Variante 3

Eingabe (Testdaten, Randfälle absichtlich enthalten):

```
KFZ_Versicherung(VID, Versicherung_Summe, Vertragsbeginn, Garage)
1 150000 2022-05-03 0 | 2 150000 2022-05-31 0 | 3 100000 2022-05-10 0
4 250000 2022-05-12 1 | 5 250000 2022-04-30 0 | 6 250000 2022-06-01 0
7 250000 2021-05-15 0 | 8 100000.01 2022-05-20 0

Wartungsvertrag(VNr, Jahresentgelt, Vertragsbeginn, Fernwartung)
101 7500 2024-09-01 0 | 102 6000 2024-09-30 0 | 103 5000 2024-09-15 0
104 9000 2024-09-15 1 | 105 9000 2024-08-31 0 | 106 9000 2024-10-01 0
107 9000 2023-09-15 0
```

Befehl:

```
python -c "import sqlite3; con=sqlite3.connect(':memory:');
con.create_function('Year',1,lambda d:int(d[:4])); con.create_function('Month',1,lambda d:int(d[5:7]));
... ; print([r[0] for r in c.execute(abfrage)])"
```

Ausgabe:

```
F23 4.6              -> [1, 2, 8]
dieselbe mit NOT Garage -> [1, 2, 8]
Variante 3           -> [101, 102]
SELECT Prioritaet, COUNT(TicketID) FROM Ticket GROUP BY Prioritaet -> [(None,1), ('hoch',2), ('mittel',1)]
dieselbe ohne GROUP BY -> [('hoch', 4)]
```

Abgleich: Beide Abfragen liefern genau die im Aufgabentext verlangte Menge. Der Randfall
„Summe genau 100.000" (VID 3) und „Entgelt genau 5.000" (VNr 103) fällt korrekt heraus,
weil `>` und nicht `>=` steht; der Monatsrand 31.05. bzw. 30.09. bleibt drin; das falsche Jahr,
der falsche Monat und die Garage bzw. Fernwartung werden ausgeschlossen. Die im Fragment
genannte Alternative `NOT Garage` liefert dieselbe Menge. Die Abfrage der Lösungshinweise
(`notizen/2023-fruehjahr.md`, 4.6) stimmt Zeichen für Zeichen mit dem Fragment überein.
Year() und Month() sind Access- bzw. T-SQL-Schreibweise; das Fragment kennzeichnet sie in der
Prüfungsnotiz des Kerns als dialektabhängige IHK-Schreibweise und im Lösungstext als
Schreibweise des Lösungshinweises.

### Punkteverteilungen und Modelle

Eingabe/Befehl: `node -e "console.log(2+2+1+2+1, 6*1, 1+1+1+1)"`

Ausgabe: `8 6 4`

Abgleich: H25 4.4 = 8 P (zwei Entitäten 2, zwei Kardinalitäten 2, Primärschlüssel 1,
Attributzuordnung 2, Dosierung an der Beziehung 1) genau wie der gedruckte Lösungskern;
H24 4.2 = 6 P über sechs zu ergänzende Elemente; F23 4.6 = 4 P ohne amtliche Feinverteilung,
im Fragment ausdrücklich als didaktische Einteilung gekennzeichnet. Die Varianten übernehmen
8, 6 und 4 Punkte.

Kardinalitäten in Abb. A9-5: Lieferant 1 – n Medikament (Fremdschlüssel läge auf der
n-Seite Medikament), Medikament n – m Wirkstoff, Dosierung an der Raute der n:m-Beziehung.
In Abb. A9-6: Mitarbeiter 1 – n Aufträge, Mitarbeiter_Vorname am Mitarbeiter, Beginn und
Ende am Auftrag. Beides deckt sich mit den Lösungsdiagrammen der Notizen. Variante 1 setzt
n:m zwischen Seminar und Teilnehmer mit Punktzahl an der Beziehung und 1:n zwischen Referent
und Seminar; die aufgelöste Beziehungstabelle Teilnahme trägt den Schlüssel SemID + TnID.
Keine Abweichung, keine Korrektur am Fragment nötig.

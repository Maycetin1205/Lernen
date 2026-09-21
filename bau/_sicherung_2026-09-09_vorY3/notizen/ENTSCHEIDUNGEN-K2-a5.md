# Entscheidungen Phase K-2, Kapitel A5 · Strom und Energiekosten

Stand: 2026-09-03. Nur echte Entscheidungen, für die der Plan keine eindeutige Vorgabe macht
oder bei denen ich von Vorlage, Entwurf oder Lösungshinweis abgewichen bin.

## Aufgabenauswahl

1. **Drei Originale: H21 2.1, H21 2.2, F24 3.7.** So im Auftrag vorgegeben. Reihenfolge nach
   Punkten: 6&nbsp;P, dann 4&nbsp;P (H21 2.2 vor F24 3.7, weil sie unmittelbar auf 2.1 aufbaut und
   deren Ergebniszahlen weiterverwendet).
2. **H21 2.4, F24 3.8, H25 3.5 und H25 3.6 kommen nicht als eigene Original-Aufgaben vor**, obwohl
   sie in der Kam-dran-Zeile stehen. Der Prüfer lässt höchstens drei zu. Damit trotzdem kein Stoff
   verloren geht, sind sie inhaltlich untergebracht: H21 2.4 (Belastbarkeit 16&nbsp;A) als Begriffskarte,
   Prüfungsnotiz und Selbstcheck-Frage&nbsp;4; H25 3.5 (USB-Strom) als Praxiszeile der ersten Karte und
   Selbstcheck-Frage&nbsp;1; H25 3.6 (Störung durch unzureichende USB-Versorgung) als Schlusssatz derselben
   Antwort; F24 3.8 (Kosten mit Wirkungsgrad und Lastanteil) im Rechenweg-Schema und in Abschnitt&nbsp;3.
3. **Selbstcheck mit vier statt drei Fragen.** Der Plan erlaubt drei bis fünf. Vier waren nötig, um
   die beiden nicht als Original abgebildeten Rechentypen (USB-Strom, Steckdosenbelastbarkeit)
   wenigstens einmal rechnend abzufragen.

## Umgang mit den Lösungshinweisen

4. **Rundung 78,94&nbsp;W statt 78,95&nbsp;W (H21 2.1).** 60&nbsp;/&nbsp;0,76 ergibt 78,9474&nbsp;W; kaufmännisch
   gerundet wären das 78,95&nbsp;W, der Lösungshinweis schneidet auf 78,94&nbsp;W ab. Nach §2 Regel 6 steht
   die IHK-Zahl im Kapitel, die Abweichung ist im Lösungstext als Rundungshinweis benannt und in
   RECHNUNGEN-a5.md protokolliert. Auf das Kostenergebnis wirkt sie sich nicht aus (4,26&nbsp;€ in beiden
   Varianten nachgerechnet).
5. **„0,3 Cent/kWh“ im Lösungshinweis.** Das ist ein Schreibfehler des Hefts; gerechnet wurde dort
   mit 0,30&nbsp;€ je kWh, sonst käme 7,53&nbsp;€ nicht heraus. Die Aufgabe selbst nennt 30&nbsp;Cent. Ich
   verwende 0,30&nbsp;€ und mache die Falle als Prüfungsnotiz sichtbar, statt sie stillschweigend zu
   korrigieren – der Lernende soll den Umgang mit widersprüchlichen Angaben mitnehmen.
6. **Punkteabsatz zu H21 2.2 nennt die Ersatzwerte des Hefts.** Die Lösungshinweise führen eine
   Alternativrechnung (6,83&nbsp;€ / 4,78&nbsp;€ → 49 Monate). Sie steht im Kapitel, weil sie die
   Folgefehlerregel der IHK anschaulich belegt, und ist ebenfalls nachgerechnet.

## Umgang mit dem vorhandenen Entwurf (pruef/erstelle-a5.py)

7. **Übernommen:** die Grundidee der Begriffskarten und die Abbildungen Formeldreieck, Rechenkette
   und Netzteil-Leistungsfluss. Alle Karten wurden neu formuliert, gekürzt und mit den Quellen aus
   QUELLEN-A.md belegt.
8. **Verworfen: beide Original-Aufgaben des Entwurfs.** Der Entwurf gab unter „AP1 Herbst 2025,
   Aufgabe 3.5“ eine Rechnung mit 184&nbsp;W an 230&nbsp;V und unter „AP1 Frühjahr 2024, Aufgabe 3.7“ eine
   Komponentenliste mit 125/220/45/18&nbsp;W und 15&nbsp;% Reserve wieder. Beides steht so in keiner
   Extraktionsnotiz: H25 3.5 rechnet 24&nbsp;V · 0,5&nbsp;A und 12&nbsp;W / 5&nbsp;V, F24 3.7 hat sieben
   Komponentenzeilen mit Stückzahlen und 10&nbsp;% Reserve. Die Zahlen waren also erfunden.
9. **Verworfen: der Merke-Block zu Scheinleistung, cos phi und Voltampere.** Keine der sieben
   Teilaufgaben des Kapitels verlangt Scheinleistung; nach §6 kommt nur hinein, was eine Teilaufgabe
   verlangt.
10. **Verworfen: die konkreten 80-PLUS-Gold-Prozentwerte** (90&nbsp;% bei 20&nbsp;% Last usw.) aus dem
    Entwurf. QUELLEN-A.md weist für `clearesult-80plus` als geprüfte Fundstelle nur die Stufen
    Bronze bis Titan bei 20/50/100&nbsp;% Last aus, nicht die einzelnen Grenzwerte. Deshalb steht im
    Kapitel nur, was belegt ist.
11. **Verworfen: die SVG-Klasse `klein`.** Sie steht zwar in der Klassen-Allowlist von check.js, ist
    aber in §9 nicht als SVG-Klasse aufgeführt und im CSS nur in `rem` definiert; in einem
    skalierten SVG würde sie nicht mit der viewBox mitwachsen. Überall `t2` verwendet.

## Gestaltung und Sprache

12. **Vier Abbildungen statt der zwei Pflichtabbildungen.** Ergänzt wurden der Leistungsfluss durch
    das Netzteil (Abb. A5-3) und die Amortisationsgrafik (Abb. A5-4). Beide zeigen einen Mechanismus,
    der sonst nur als Formel dasteht: die Umkehrung der Leseerichtung beim Wirkungsgrad und den
    Schnittpunkt von Mehrpreis und aufgelaufener Einsparung. Das liegt im Richtwert „drei bis fünf“
    der Gruppe A.
13. **Kein `<strong>` und kein `<em>` im Fließtext**, abweichend vom fertigen Beispielkapitel
    13-a4.html. §8 erlaubt Fettdruck nur in `dt` und Tabellenköpfen; der Prüfer erzwingt das nicht,
    der Plan schon.
14. **`eta` ausgeschrieben statt des Zeichens η**, damit Formel und Fließtext dieselbe Schreibweise
    haben und im SVG keine Sonderzeichenbreite geschätzt werden muss.
15. **Alle SVG-Beschriftungen im gerenderten Dokument nachgemessen** (getBBox gegen die viewBox,
    Chrome headless). Kein Text läuft aus seinem Rahmen. Zwei Stellen wurden danach korrigiert: das
    Wort „Summe“ in Abb. A5-2 lag unter dem Pfeilkopf, und die Beschriftung der Einsparungsgeraden in
    Abb. A5-4 wurde vom Akzentstrich durchschnitten.
16. **Wortzahl 3.138 statt des Richtwerts 2.200 bis 2.800.** Jedes Einzelbudget ist eingehalten
    (Worum 117, Karten 106 bis 119, Verfahren 677, Aufgaben und Varianten unter den Obergrenzen).
    Der Überhang entsteht aus drei Originalen plus drei Varianten plus acht Pflichtbegriffen. Weiter
    zu kürzen hieße, Pflichtinhalt aus §6 zu streichen; die harte Grenze von 4.500 ist weit entfernt.

## Quellen

17. **Zwei Fachbücher ohne Verlinkung.** `hering-physik` und `europa-tabellenbuch-it` stehen in
    QUELLEN-A.md mit Status „nicht online geprüft“, `iec-62040-3` mit „kostenpflichtig“. Alle drei
    erscheinen deshalb ohne `a`-Element und mit `(nicht online geprüft)`.
18. **`ihk-konvention-strom` ohne URL, obwohl Status „geprüft“.** Die Zeile in QUELLEN-A.md führt
    keine URL. Nach §7 Regel 3 gibt es dann kein `a`-Element; der Vermerk lautet
    `(nicht online geprüft)`.
19. **Die Strompreisspanne 0,30&nbsp;€ bis 0,40&nbsp;€ je kWh** ist mit dem Monitoringbericht der
    Bundesnetzagentur belegt, aber bewusst als Spanne und ohne Jahresangabe formuliert, weil
    QUELLEN-A.md nur den Abschnitt „Strompreise“ als Fundstelle nennt und kein Berichtsjahr.

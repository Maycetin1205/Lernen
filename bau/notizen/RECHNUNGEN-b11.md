# K-5 · B11 · Wirtschaft und Recht · Nachrechnung 2026-09-06

Werkzeug: Python 3, Skript `b11.py` im Sitzungs-Scratchpad (Wegwerfdatei, nicht im Projekt).
Datumsrechnung mit `datetime.date` und `timedelta`; Geldbeträge mit `Decimal` und kaufmännischer Rundung
(`ROUND_HALF_UP`) auf zwei Nachkommastellen. Alle Zahlen unten stehen so im Fragment `kapitel/30-b11.html`.
Das Kapitel hat wenige Sachrechnungen; Skonto-, Rabatt- und Leasingvergleich rechnet A2.

## R1 · Abstände auf dem Herbst-2025-Beleg (Abbildung B11-1, Original 1)

Gegeben (Notiz 2025-herbst.md, 1.1 und 1.3): Bestellung 05.09.2025, Lieferung 10.09.2025, Rechnung 11.09.2025,
Skonto bis 30.09.2025, Zahlungsziel 31.10.2025.

Eingabe:
```
best=date(2025,9,5); lief=date(2025,9,10); rech=date(2025,9,11); sk=date(2025,9,30); ziel=date(2025,10,31)
(lief-best).days, (rech-lief).days, (sk-rech).days, (ziel-rech).days, ziel+timedelta(days=1)
```
Ausgabe:
```
Bestellung->Lieferung 5 Tage | Lieferung->Rechnung 1 Tag | Rechnung->Skontofrist 19 Tage
Rechnung->Zahlungsziel 50 Tage | Verzug ab (Tag nach Zahlungsziel): 2025-11-01
```
Abgleich: Der Lösungshinweis zu H25 1.1 verlangt nur die drei Vorgänge mit Datum (05.09., 10.09., 11.09.); die
Abstände sind eigene Ergänzung für die Abbildung. Die Daten selbst stimmen mit der Notiz überein.

## R2 · Zeitstrahl-Beispiel (Abbildung B11-2)

Eigenes Lehrbeispiel, keine IHK-Aufgabe: Rechnung vom 01.10.2025, Zugang am selben Tag, 14 Tage Skontofrist,
30 Tage Zahlungsziel.

Eingabe:
```
r=date(2025,10,1); r+timedelta(days=14), r+timedelta(days=30), r+timedelta(days=31)
```
Ausgabe:
```
+14 Tage Skonto bis 2025-10-15 | +30 Tage Zahlungsziel 2025-10-31 | Verzug ab 2025-11-01
§ 286 Abs. 3 ohne Zahlungsziel: 30 Tage nach Faelligkeit+Zugang -> 2025-10-31, spaetestens Verzug ab 2025-11-01
```
Abgleich: Rechtsgrundlage § 286 Abs. 2 Nr. 1 BGB (kalendermäßig bestimmte Zeit, keine Mahnung nötig) und
§ 286 Abs. 3 BGB (30 Tage nach Fälligkeit und Zugang der Rechnung), beide am 2026-09-06 im Gesetzestext gelesen.
Im Beispiel fallen Zahlungsziel und 30-Tage-Grenze auf denselben Tag, weil das Ziel genau 30 Tage beträgt; das ist
Absicht, damit der Lernende beide Regeln an einer Marke sieht.

## R3 · Rechnungspositionen Herbst 2025, Aufgabe 1.2 (Original 1, Abbildung B11-1)

Eingabe:
```
pos=[(3,"60.00",19),(10,"50.00",19),(2000,"0.15",7)]
Zeilensumme = Menge x Einzelpreis; Netto je Steuersatz; USt = Basis x Satz, kaufmaennisch gerundet
```
Ausgabe:
```
3 x 60,00 = 180,00 (19 %) | 10 x 50,00 = 500,00 (19 %) | 2000 x 0,15 = 300,00 (7 %)
Netto 980,00 | Basis 19 % 680,00 -> USt 129,20 | Basis 7 % 300,00 -> USt 21,00
Brutto 1.130,20
Skonto 2 % vom Brutto: 22,60
```
Abgleich: Der Bruttobetrag 1.130,20 EUR steht so im Aufgabenheft (Notiz H25 1.3); der Skontobetrag 22,60 EUR
deckt sich mit dem Lösungshinweis zu H25 1.3 und mit A2. Die Steuerbeträge 129,20 und 21,00 nennt der
Lösungshinweis nicht; sie ergeben sich aus den Positionen und dem Bruttobetrag und stimmen mit ihm überein
(980,00 + 129,20 + 21,00 = 1.130,20).

## R4 · Variante zu Aufgabe 1.2 (eigenes Beispiel)

Eingabe:
```
pos=[(4,"85.00",19),(20,"12.50",19),(50,"24.00",7)]
```
Ausgabe:
```
4 x 85,00 = 340,00 (19 %) | 20 x 12,50 = 250,00 (19 %) | 50 x 24,00 = 1.200,00 (7 %)
Netto 1.790,00 | Basis 19 % 590,00 -> USt 112,10 | Basis 7 % 1.200,00 -> USt 84,00
Brutto 1.986,10
Fehlerbeispiel: 1.200,00 faelschlich mit 19 % -> 228,00 statt 84,00, Differenz 144,00
```
Abgleich: kein IHK-Lösungshinweis (eigene Variante). Bücher fallen unter den ermäßigten Steuersatz; das ist im
Fragment nur als Beispiel für eine Steuersatzprüfung genannt, ohne Anlage zum UStG zu zitieren.

## R5 · Leasing gegen Kauf, Frühjahr 2023 (Praxiszeile der Begriffskarte)

Eingabe: `6000*60, 6000*60-300000`
Ausgabe: `360000 | 60000`
Abgleich: Lösungshinweis zu F23 2.4 rechnet 6.000 × 60 = 360.000 EUR, Leasing 60.000 EUR teurer. Übereinstimmung.
Die Rechnung selbst gehört zu A2; B11 nennt nur die Zahlen als Beleg, dass Leasingvorteile nicht Kostenvorteile sind.

## R6 · Gewährleistungsfrist als Datum (Selbstcheck, Abbildung B11-3)

Eingabe: Ablieferung 10.09.2025; Verjährung zwei Jahre ab Ablieferung (§ 438 Abs. 1 Nr. 3, Abs. 2 BGB);
Beweislastumkehr ein Jahr seit Gefahrübergang (§ 477 Abs. 1 BGB).
Ausgabe: `Verjaehrung endet 2027-09-10 | Beweislastumkehr Verbraucher bis 2026-09-10`
Abgleich: kein IHK-Lösungshinweis; Fristen aus dem Gesetzestext, am 2026-09-06 gelesen.

## Kontrolle 2026-09-06

Kontrolleur K-5. Werkzeug: Node v25 mit `Date.UTC`, Wegwerfskript `b11chk.js` im
Sitzungs-Scratchpad. Geprüft: H25 1.2, H24 4.3, F24 1.5 und die drei Varianten gegen
`notizen/2025-herbst.md` 1.1 bis 1.3, `notizen/2024-herbst.md` 4.3 und
`notizen/2024-fruehjahr.md` 1.5.

Eingabe und Befehl:

```
node -e "
const d=(y,m,t)=>new Date(Date.UTC(y,m-1,t)), f=x=>x.toISOString().slice(0,10),
      plus=(x,n)=>new Date(x.getTime()+n*864e5), rd=x=>Math.round(x*100)/100;
const r=d(2025,10,1);
console.log(f(r), f(plus(r,14)), f(plus(r,30)), f(plus(r,31)));
const rech=d(2025,9,11), ziel=d(2025,10,31);
console.log('H25', f(d(2025,9,5)), f(d(2025,9,10)), f(rech), f(d(2025,9,30)), f(ziel), f(plus(ziel,1)));
console.log('286 III', f(plus(rech,30)), f(plus(rech,31)));
console.log('Gewaehrleistung', f(d(2027,9,10)), 'Beweislast', f(d(2026,9,10)));
for (const p of [[[3,60,19],[10,50,19],[2000,0.15,7]], [[4,85,19],[20,12.5,19],[50,24,7]]]) {
  let a=0,b=0; for (const [m,e,s] of p) { const z=rd(m*e); if (s===19) a+=z; else b+=z; }
  console.log(a, b, a+b, rd(a*0.19), rd(b*0.07), rd(a+b+rd(a*0.19)+rd(b*0.07))); }
console.log('Skonto', rd(1130.20*0.02), '| 1200 mit 19 %', rd(1200*0.19), 'Differenz', rd(1200*0.19-1200*0.07));
"
```

Ausgabe:

```
2025-10-01 2025-10-15 2025-10-31 2025-11-01
H25 2025-09-05 2025-09-10 2025-09-11 2025-09-30 2025-10-31 2025-11-01
286 III 2025-10-11 2025-10-12
Gewaehrleistung 2027-09-10 Beweislast 2026-09-10
680 300 980 129.2 21 1130.2
590 1200 1790 112.1 84 1986.1
Skonto 22.6 | 1200 mit 19 % 228 Differenz 144
```

Abgleich:

| Stelle im Fragment | Wert im Fragment | Nachrechnung | Abgleich |
|---|---|---|---|
| Original 1, Zeilensummen | 3 × 60 = 180; 10 × 50 = 500; 2.000 × 0,15 = 300 | identisch | stimmt mit dem Beleg der Notiz |
| Abb. B11-1, Steuer und Brutto | Netto 980,00; 19 % auf 680,00 = 129,20; 7 % auf 300,00 = 21,00; Brutto 1.130,20 | identisch | Brutto deckt sich mit dem Heftwert aus H25 1.3 |
| Variante 1, Summen | Netto 1.790,00; 112,10; 84,00; Brutto 1.986,10 | identisch | stimmt |
| Variante 1, Fehlerbeispiel | 228,00 statt 84,00, 144,00 zu viel | identisch | stimmt |
| Abb. B11-2, Fristen | Rechnung 01.10., Skonto 15.10. (Tag 14), Ziel 31.10. (Tag 30), Verzug ab 01.11. | identisch | stimmt |
| Original 3, Vertragsschluss | 7. Oktober 2023 durch Lieferung | – | stimmt mit dem Lösungskern: 1 P Datum, 1 P Begründung |
| Variante 3, Vertragsschluss | 6. März durch Auftragsbestätigung | – | freibleibendes Angebot ist kein bindender Antrag (§ 145 BGB), Bestellung = Antrag, Bestätigung = Annahme |
| Gewährleistung, Abb. B11-3 | 2 Jahre ab Ablieferung, 12 Monate Beweislastumkehr | 2027-09-10 / 2026-09-10 | § 438 Abs. 1 Nr. 3 und Abs. 2 BGB, § 477 Abs. 1 BGB |

Rechtsaussagen gegen die zitierten Paragrafen: § 286 Abs. 2 Nr. 1 BGB trägt den Verzug ohne
Mahnung bei kalendermäßig bestimmtem Zahlungsziel; § 286 Abs. 3 BGB die 30-Tage-Grenze nach
Fälligkeit und Zugang der Rechnung, gegenüber Verbrauchern nur mit Hinweis. Beides steht so
im Fragment. Der eigene 30-Tage-Wert der Abbildung fällt mit der gesetzlichen Obergrenze
zusammen, weil das Zahlungsziel dort genau 30 Tage beträgt; die Abbildung sagt das ausdrücklich.
Vertragsartzuordnung (Kauf § 433, Werk § 631/§ 640, Dienst § 611 BGB), Pflichtangaben
(§ 14 Abs. 4 Nr. 1 bis 8 UStG), Übergangsfristen zur E-Rechnung (§ 27 Abs. 38 UStG:
Papier bis Ende 2026, bis Ende 2027 bei höchstens 800.000 EUR Vorjahresumsatz) und die
Mindestkapitalien (25.000 EUR GmbH, 50.000 EUR AG) treffen die zitierten Fundstellen.

Punkteverteilungen: Original 1 = 6 P (je 2 P je Kontrollvorgang, höchstens drei gewertet),
Original 2 = 6 P (je 2 P je beschriebenem Vorteil), Original 3 = 2 P (1 P Datum, 1 P Begründung).
Alle drei stimmen mit den Lösungskernen der Notizen; die Varianten übernehmen den Schlüssel.

Ergebnis: keine Abweichung, keine Korrektur am Fragment nötig. Der Wortumfang von
`kapitel/30-b11.html` bleibt damit bei 4.490 Wörtern unter der Obergrenze 4.500;
`node pruef/check.js kapitel/30-b11.html --fragment` meldet unverändert „Keine Fehler."

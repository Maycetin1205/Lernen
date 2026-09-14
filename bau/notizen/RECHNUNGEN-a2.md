# A2 · Kaufmännisch rechnen · Nachrechnung

Datei war zuvor nicht vorhanden und wurde bei der Lösungskontrolle angelegt.

## Kontrolle 2026-09-06

Werkzeug: Node v25, Wegwerfskript `rechnung.js` im Sitzungs-Scratchpad (nicht im Projekt).
Geprüft: `kapitel/11-a2.html`, Abschnitte `a2-original-1`, `a2-original-2`, `a2-variante-1`, `a2-variante-2`.
Amtliche Grundlage: `notizen/2024-herbst.md` Abschnitt 3.1 und `notizen/2025-herbst.md` Abschnitt 1.3.

### Eingabe und Befehl

```
let rest=12000, tilg=12000/3, zsum=0, psum=0;
for(let j=1;j<=3;j++){const z=rest*0.06, p=z+tilg; zsum+=z; psum+=p;
  console.log('Jahr',j,[rest,z,tilg,p].join(' | ')); rest-=tilg;}
console.log('Summen', [zsum,psum,rest].join(' | '));

rest=36000; tilg=12000; zsum=0; psum=0;
for(let j=1;j<=3;j++){const z=rest*0.04, p=z+tilg; zsum+=z; psum+=p;
  console.log('Var Jahr',j,[rest,z,p].join(' | ')); rest-=tilg;}
console.log('Var Summen', [zsum,psum,rest].join(' | '));

console.log(1130.20*0.02, Math.round(1130.20*0.02*100)/100);
console.log(3570*0.03, Math.round((3570-3570*0.03)*100)/100);
```

Aufruf: `node rechnung.js`

### Ausgabe

```
Jahr 1 12000 | 720 | 4000 | 4720
Jahr 2 8000 | 480 | 4000 | 4480
Jahr 3 4000 | 240 | 4000 | 4240
Summen 1440 | 13440 | 0
Var Jahr 1 36000 | 1440 | 13440
Var Jahr 2 24000 | 960 | 12960
Var Jahr 3 12000 | 480 | 12480
Var Summen 2880 | 38880 | 0
22.604000000000003 22.6
107.1 3462.9
```

### Abgleich mit den Lösungshinweisen

| Bezug | Amtlicher Lösungskern | Fragment nach der Korrektur |
|---|---|---|
| H24 3.1, 7 P | Zeilen 12.000/720/4.000/4.720, 8.000/480/4.000/4.480, 4.000/240/4.000/4.240; Summen 1.440 und 13.440 | deckungsgleich |
| H25 1.3, 2 P | 1.130,20 * 0,02 = 22,604, kaufmännisch 22,60 EUR | deckungsgleich |
| Variante zu 3.1 | eigene Übungsaufgabe | 1.440 / 960 / 480, Zinssumme 2.880, Gesamtaufwand 38.880 bestätigt |
| Variante zu 1.3 | eigene Übungsaufgabe | 107,10 EUR Skonto, 3.462,90 EUR Zahlbetrag bestätigt |

### Gefundene und behobene Abweichungen

1. `a2-original-1` rechnete mit 24.000,00 EUR, vier Jahren und 5,0 Prozent. Die Notiz zu H24 3.1 nennt
   12.000,00 EUR, 36 Monate und 6,0 Prozent. Der Tilgungsplan lieferte damit durchweg falsche Zahlen
   (3.000,00 EUR statt 1.440,00 EUR Zinsen, 27.000,00 EUR statt 13.440,00 EUR Gesamtzahlung). Aufgabentext
   und Lösung wurden auf die amtlichen Werte gesetzt.
2. Die Punkteverteilung von `a2-original-1` beschrieb vier Jahreszeilen. Die Notiz weist die 7 Punkte
   ohne Einzelaufteilung aus, faktisch je etwa 1 Punkt auf drei Jahreszeilen, drei Summenwerte und den
   Ansatz. Der Satz wurde entsprechend ersetzt.
3. `a2-original-2` verlangte zusätzlich den Zahlbetrag und verteilte die 2 Punkte auf Skontobetrag und
   Überweisungsbetrag. Amtlich gefragt ist nur der Skontobetrag; die 2 Punkte entfallen auf Ansatz und
   gerundeten Endwert. Die Zahlen 1.130,20 EUR, 2 Prozent und 22,60 EUR waren bereits richtig.
4. Beide Varianten waren rechnerisch fehlerfrei und blieben unverändert; sie trainieren dasselbe
   Verfahren wie ihre Originale (Ratendarlehen mit konstanter Tilgung, Skonto vom Bruttobetrag).


## Nachrechnung zum Lehrer-Umbau 2026-09-08

Werkzeug: python -c, Aufruf im Projektverzeichnis. Neue Rechenbeispiele im Kernabschnitt.

### Eingabe

lp=10000.0
rab=lp*0.15; zep=lp-rab
sk=zep*0.02; bep=zep-sk
bez=bep+250
print(rab, zep, round(sk,2), bep, bez); print(lp*0.85, zep*0.98)
rest=9000.0; tilg=9000/3; zs=0; gs=0
for j in (1,2,3):
    z=rest*0.05; zahl=z+tilg; zs+=z; gs+=zahl; print(j, rest, z, tilg, zahl); rest-=tilg
print(zs, gs, rest)
p=80.0; kv=50.0; kf=12000.0
db=p-kv; x=kf/db; print(db, x, x*p, kf+x*kv)

### Ausgabe

1500.0 8500.0 170.0 8330.0 8580.0
8500.0 8330.0
1 9000.0 450.0 3000.0 3450.0
2 6000.0 300.0 3000.0 3300.0
3 3000.0 150.0 3000.0 3150.0
900.0 9900.0 0.0
30.0 400.0 32000.0 32000.0

### Verwendung

| Zahl | Wo im Kapitel |
|---|---|
| 1.500,00 / 8.500,00 / 170,00 / 8.330,00 / 8.580,00 | Schritte 1 bis 3 und Abb. A2-1; identisch mit dem vorhandenen Rechenweg-Schema |
| 10.000,00 * 0,85 und 8.500,00 * 0,98 | Kurzweg im Baustein Prozent und in Abb. A2-1 |
| 9.000,00 EUR, 3 Jahre, 5,0 %: 450/300/150, Tilgung 3.000, Zahlungen 3.450/3.300/3.150, Summen 900 und 9.900 | Tilgungsplan und Abb. A2-2. Eigenes Beispiel, damit die Originalaufgabe (12.000 EUR, 6,0 %) eine Aufgabe bleibt |
| p 80,00, kv 50,00, db 30,00, Kf 12.000,00, x_G 400 Stueck; Kontrolle Erloes 32.000 gleich Kosten 32.000 | Abb. A2-3 und der Absatz zur Gewinnschwelle |

# A3 · Nutzwertanalyse und Entscheidungsmatrix · Nachrechnung

Datei war zuvor nicht vorhanden und wurde bei der Lösungskontrolle angelegt.

## Kontrolle 2026-09-06

Werkzeug: Node v25, Wegwerfskripte `rechnung.js` und `varianten.js` im Sitzungs-Scratchpad (nicht im Projekt).
Geprüft: `kapitel/12-a3.html`, Abschnitte `a3-original-1`, `a3-original-2`, `a3-variante-1`, `a3-variante-2`.
Amtliche Grundlage: `notizen/2025-fruehjahr.md` Abschnitt 1.1 und `notizen/2024-fruehjahr.md` Abschnitt 1.2.

### Eingabe und Befehl

```
const rang = krit => {
  const sum=[0,0,0];
  for(const [n,o] of Object.entries(krit)){
    const idx=[0,1,2].slice().sort((a,b)=> o.hoch ? o.w[a]-o.w[b] : o.w[b]-o.w[a]);
    const p=[0,0,0]; idx.forEach((g,r)=>p[g]=r+1); p.forEach((x,i)=>sum[i]+=x);
    console.log(n, o.w.join(' / '), '->', p.join(' / '));
  }
  console.log('Ergebniszeile', sum.join(' / '), 'Sieger', sum.indexOf(Math.max(...sum))+1);
};
rang({'Druck S/min':{w:[40,62,50],hoch:true}, 'Scan S/min':{w:[20,50,40],hoch:true},
      'Wartung EUR/M':{w:[50,10,15],hoch:false}, 'Preis EUR':{w:[3456,2844,1656],hoch:false}});
rang({'Schreibrate MB/s':{w:[180,320,260],hoch:true}, 'Garantie Jahre':{w:[2,5,3],hoch:true},
      'Leistung W':{w:[38,52,45],hoch:false}, 'Preis EUR':{w:[1100,1650,1850],hoch:false}});
```

Aufruf: `node rechnung.js` und `node varianten.js`

### Ausgabe

```
Druck S/min      40 / 62 / 50        -> 1 / 3 / 2
Scan S/min       20 / 50 / 40        -> 1 / 3 / 2
Wartung EUR/M    50 / 10 / 15        -> 1 / 3 / 2
Preis EUR        3456 / 2844 / 1656  -> 1 / 2 / 3
Ergebniszeile 4 / 11 / 9   Sieger 2

Schreibrate MB/s 180 / 320 / 260     -> 1 / 3 / 2
Garantie Jahre   2 / 5 / 3           -> 1 / 3 / 2
Leistung W       38 / 52 / 45        -> 3 / 1 / 2
Preis EUR        1100 / 1650 / 1850  -> 3 / 2 / 1
Ergebniszeile 8 / 9 / 7   Sieger 2
```

### Abgleich mit den Lösungshinweisen

| Bezug | Amtlicher Lösungskern | Fragment nach der Korrektur |
|---|---|---|
| F25 1.1, 6 P | Rangwerte 1/3/2, 1/3/2, 1/3/2, 1/2/3; Ergebniszeile 4, 11, 9 | deckungsgleich |
| F24 1.2, 2 P | Anbieter 4 erhält den Auftrag; Anbieter 3 scheidet trotz 355 Punkten am K.-o.-Kriterium aus | deckungsgleich |
| Variante zu 1.1 | eigene Übungsaufgabe | Ergebniszeile 8 / 9 / 7, Sieger NAS 2 bestätigt |
| Variante zu 1.2 | eigene Übungsaufgabe | Gewichtsgrenze 1.300 g schließt ProBook mit 1.450 g aus, TravelAir 1.180 g bleibt |

### Gefundene und behobene Abweichungen

1. `a3-original-1` zeigte eine gewichtete Nutzwertanalyse über drei Thin Clients mit Prozentgewichten
   und Skala 1 bis 10 (Ergebnisse 7,65 / 7,45 / 7,35). F25 1.1 ist dagegen eine ungewichtete
   Entscheidungsmatrix über drei Multifunktionsgeräte mit Rangwerten 1 bis 3; die Notiz hält
   ausdrücklich fest, dass keine Gewichtungen vorkommen. Aufgabe und Lösung wurden ersetzt. Die
   Rechenrichtung je Kriterium (bei Geschwindigkeiten ist groß besser, bei Kosten und Preis klein)
   steht jetzt in der Lösung.
2. Die Punkteverteilung von `a3-original-1` war mit "je 1,5 Punkte" als amtliche Aufteilung dargestellt.
   Die Notiz weist die Aufteilung ausdrücklich als nicht amtlich belegt aus. Der Satz sagt das jetzt.
3. `a3-original-2` erfand eine Duplexdruck-Entscheidung zwischen Modell X und Y. F24 1.2 betrifft die
   vier CAD-Angebote mit den Nutzwerten 285, 215, 355 und 310 und den Ausschluss von Anbieter 3 wegen
   der reinen SaaS-Lieferung. Aufgabe und Lösung wurden auf die amtlichen Werte gesetzt; Punktzahl
   und Punktelogik (1 P Wahl, 1 P Ausschlussbegründung) stimmten bereits.
4. `a3-variante-1` war eine gewichtete Analyse zweier Cloud-Anbieter. Sie war rechnerisch fehlerfrei
   (beide 8,10 Punkte), trainierte nach der Korrektur von Punkt 1 aber nicht mehr das Verfahren ihres
   Originals und wurde auf eine ungewichtete Rangmatrix über drei NAS-Systeme umgestellt.
5. `a3-variante-2` war fehlerfrei und blieb unverändert.

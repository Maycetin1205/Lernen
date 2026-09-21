# A1 · IPv4, Subnetting und Netzkonfiguration · Nachrechnung

Datei war zuvor nicht vorhanden und wurde bei der Lösungskontrolle angelegt.

## Kontrolle 2026-09-06

Werkzeug: Node v25, Wegwerfskripte `a1.js` und `rechnung.js` im Sitzungs-Scratchpad (nicht im Projekt).
Geprüft: `kapitel/10-a1.html`, Abschnitte `a1-original-1`, `a1-original-2`, `a1-variante-1`, `a1-variante-2`.
Amtliche Grundlage: `notizen/2024-herbst.md` Abschnitt 1.5 und `notizen/2025-herbst.md` Abschnitt 3.7.

### Eingabe und Befehl

```
const net=(o,p)=>{const b=2**(32-p);const s=Math.floor(o/b)*b;
  return{block:b,netz:s,bc:s+b-1,first:s+1,last:s+b-2,maske:256-b,hosts:b-2};};
console.log('H24 1.5  192.168.20.0/24 :', JSON.stringify(net(0,24)));
console.log('H25 3.7  172.16.10.0/24  :', JSON.stringify(net(0,24)));
console.log('Var 1    172.16.40.128/25:', JSON.stringify(net(128,25)));
console.log('Var 2    10.10.5.64/27   :', JSON.stringify(net(64,27)));
```

Aufruf: `node a1.js`

### Ausgabe

```
H24 1.5  192.168.20.0/24 : {"block":256,"netz":0,"bc":255,"first":1,"last":254,"maske":0,"hosts":254}
H24 1.5  frei zwischen Router .1 und DHCP-Start .20 : 2,3,...,19
H25 3.7  172.16.10.0/24  : {"block":256,"netz":0,"bc":255,"first":1,"last":254,"maske":0,"hosts":254}
Var 1    172.16.40.128/25: {"block":128,"netz":128,"bc":255,"first":129,"last":254,"maske":128,"hosts":126}
Var 2    10.10.5.64/27   : {"block":32,"netz":64,"bc":95,"first":65,"last":94,"maske":224,"hosts":30}
```

### Abgleich mit den Lösungshinweisen

| Bezug | Amtlicher Lösungskern | Fragment nach der Korrektur |
|---|---|---|
| H24 1.5, 4 P | Auswahlknopf "Folgende IP-Adresse verwenden"; IP 192.168.20.10, gültig .2 bis .19; Maske 255.255.255.0; Gateway 192.168.20.1 | deckungsgleich |
| H25 3.7, 3 P | IP 172.16.10.254; Maske 255.255.255.0; Gateway 172.16.10.1 | deckungsgleich |
| Variante zu 1.5 | eigene Übungsaufgabe | Gateway .129, freie IP .141, Maske 255.255.255.128, Broadcast .255 bestätigt |
| Variante zu 3.7 | eigene Übungsaufgabe | Netz .64, Broadcast .95, Gateway .65, Drucker .94, Maske 255.255.255.224, 30 Hosts bestätigt |

### Gefundene und behobene Abweichungen

1. `a1-original-1` nannte das Netz 192.168.100.0/26 mit DNS-Server .2 und vergebenen Hosts .2 bis .11.
   Die Notiz zu H24 1.5 nennt 192.168.20.0/24, DHCP-Bereich .20 bis .254 und Router .1; ein DNS-Feld
   gibt es dort nicht, dafür den Auswahlknopf für die feste Adressvergabe. Aufgabentext, Lösung und
   Punkteverteilung wurden auf die amtlichen Werte gesetzt.
2. `a1-original-2` enthielt eine IPv6-Kürzungsaufgabe (2001:0db8:...:8329). H25 3.7 ist jedoch die
   IPv4-Konfiguration des Kartenterminals mit der letzten nutzbaren Adresse. Aufgabe und Lösung wurden
   ersetzt; Herkunftszeile und Punktzahl (3 P) stimmten bereits.
3. `a1-variante-2` war die Variante zur ersetzten IPv6-Aufgabe und trainierte damit nicht mehr das
   Verfahren ihres Originals. Sie wurde auf "letzte nutzbare Hostadresse in 10.10.5.64/27" umgestellt.
4. `a1-variante-1` war rechnerisch fehlerfrei und blieb unverändert.

### Hinweis

Mit Punkt 2 und 3 enthält A1 keine IPv6-Übungsaufgabe mehr. Die Kürzungs- und Ausschreibregeln nach
RFC 5952 bleiben im Abschnitt "Das Verfahren" samt vollständig gerechnetem Beispiel in Abb. A1-3 erhalten.

## Kontrolle Lehrer-Umbau 2026-09-08

Eingabe: `ipaddress.ip_network('192.168.10.75/26', strict=False)`; ausgegeben wurden Netzadresse, Broadcastadresse, Blockgröße, erster Host, letzter Host und Netzmaske.

Ausgabe: `192.168.10.64 192.168.10.127 64 192.168.10.65 192.168.10.126 255.255.255.192`

Damit sind das durchgehende Beispiel, die 62 nutzbaren Hosts und die Gateway-Beispieladresse `.65` nachgerechnet.

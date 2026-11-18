# Linux ohne Monitor installieren

Für den HP t630, der nur DisplayPort hat. Der Stick installiert Ubuntu Server ohne jede Eingabe und schaltet den PC danach aus.
Ungetestet: Ob der t630 von selbst vom Stick startet, hängt von seinen BIOS-Einstellungen ab.

## Stick bauen (Windows-Laptop)

1. Ubuntu Server 24.04 LTS von ubuntu.com laden (Datei `ubuntu-24.04.x-live-server-amd64.iso`).
2. Rufus starten, ISO und Stick wählen.
   - Partitionsschema: **MBR**, Zielsystem: **BIOS oder UEFI**
   - Bei der Nachfrage: **Im ISO-Abbild-Modus schreiben**
3. Den Ordner `nocloud` mit den Dateien `user-data` und `meta-data` in die oberste Ebene des Sticks kopieren. Die Dateien haben keine Endung, das bleibt so.
4. Auf dem Stick `boot\grub\grub.cfg` mit dem Editor öffnen. Im ersten Eintrag steht:

   ```
   linux	/casper/vmlinuz  ---
   ```

   Ändern in:

   ```
   linux	/casper/vmlinuz autoinstall ds=nocloud\;s=/cdrom/nocloud/ ---
   ```

   Speichern, Stick sicher entfernen.

## Installieren

1. Am t630 nur Netzwerkkabel, Strom und den Stick anschließen. Keine andere Festplatte, kein zweiter Stick.
2. Einschalten und warten. Der Stick wartet 30 Sekunden und startet dann von selbst.
3. Kontrolle: In der Starlink-App taucht nach ein paar Minuten ein neues Gerät auf.
4. Nach 10 bis 25 Minuten schaltet sich der PC aus. Stick abziehen, wieder einschalten.

## Anmelden

Die Adresse des Geräts `heimserver` steht in der Starlink-App.

```bash
ssh chef@adresse
passwd          # sofort ein eigenes Passwort setzen
```

Danach weiter mit `../EINRICHTUNG.md` ab „Erste Befehle per SSH".

## Wenn er sich nach 30 Minuten nicht ausschaltet

- **Kein neues Gerät in der Starlink-App, oder es heißt wie vorher:** Er hat nicht vom Stick gestartet. Ausschalten, einschalten, sofort mehrmals F9 drücken, einmal Pfeil runter, Enter. Sonst mit zweimal Pfeil runter wiederholen.
- **Gerät da, aber kein Ausschalten:** Die Installation hängt an einer Rückfrage. Dann braucht es doch einmal ein Bild.

## Passwort-Hash

`user-data` braucht ein verschlüsseltes Passwort. Unter Linux erzeugt man es mit `openssl passwd -6`.

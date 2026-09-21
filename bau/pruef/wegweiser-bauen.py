# -*- coding: utf-8 -*-
"""Wegweiser einbauen: von jeder Prüfungsaufgabe zum Absatz, der sie beantwortet.

Liest bau/notizen/WEGWEISER-<id>.json (je Kapitel, Format siehe notizen/WEGWEISER-AUFTRAG.md) und
1. setzt in bau/kapitel/03-matrix.html die Links der Aufgabenzeilen auf das genaue Ziel (statt nur aufs Kapitel),
2. hängt in jedem Kapitel an den Abschnitt „Worum es geht“ eine Tabelle „Prüfungsaufgaben zu diesem Kapitel“
   mit Link je Aufgabe an (in einem <nav>, damit sie nicht als Lesetext gezählt wird).
Idempotent: vorhandene Tabellen werden ersetzt. Aufruf: python pruef/wegweiser-bauen.py
"""
import io, os, re, json, glob, sys, html
sys.stdout.reconfigure(encoding="utf-8")
BAU = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = os.path.join(BAU, "kapitel"); N = os.path.join(BAU, "notizen")
NAMEN = {"H21": "Herbst 2021", "F22": "Frühjahr 2022", "H22": "Herbst 2022", "F23": "Frühjahr 2023", "H23": "Herbst 2023",
         "F24": "Frühjahr 2024", "H24": "Herbst 2024", "F25": "Frühjahr 2025", "H25": "Herbst 2025"}
REIHE = list(NAMEN)

def schreibe(pfad, text):
    """Schreibt die Datei mit den Zeilenenden, die sie schon hatte.
    Sonst dreht Windows LF auf CRLF und die Datei gilt als geaendert, obwohl nichts drinsteht."""
    crlf = (chr(13) + chr(10)).encode() in io.open(pfad, "rb").read()
    zeilen = text.split(chr(10))
    ende = (chr(13) + chr(10)) if crlf else chr(10)
    io.open(pfad, "wb").write(ende.join(zeilen).encode("utf-8"))
zuordnung = json.load(io.open(os.path.join(N, "TIPPS-ZUORDNUNG.json"), encoding="utf-8"))
titel = {(z["pruefung"], z["nr"]): z["titel"] for z in zuordnung}

ziele = {}          # (pruefung, nr) -> ziel-id
zellen = {}         # (pruefung, nr) -> fertige Zelle fuer Teil 2 (mit Kapitelkuerzel davor)
fehler = []
for jf in sorted(glob.glob(os.path.join(N, "WEGWEISER-*.json"))):
    kid = re.search(r"WEGWEISER-([ab]\d+)\.json$", jf).group(1)
    dateien = glob.glob(os.path.join(K, f"*-{kid}.html"))
    if len(dateien) != 1:
        fehler.append(f"{kid}: Kapiteldatei nicht eindeutig"); continue
    s = io.open(dateien[0], encoding="utf-8").read()
    ids = set(re.findall(r'\sid="([^"]+)"', s))
    try:
        eintraege = json.load(io.open(jf, encoding="utf-8"))
    except Exception as e:
        fehler.append(f"{kid}: JSON ungültig ({e})"); continue
    soll = {(z["pruefung"], z["nr"]) for z in zuordnung if z["kapitel"].lower() == kid}
    ist = set()
    zeilen = []
    for e in eintraege:
        key = (e.get("pruefung"), e.get("nr"))
        if key not in soll:
            fehler.append(f"{kid}: {key} gehört nicht zu diesem Kapitel"); continue
        if e.get("ziel") not in ids:
            fehler.append(f"{kid}: Ziel {e.get('ziel')} für {key} existiert nicht"); continue
        if e.get("lektion") is not None and e.get("lektion") not in ids:
            fehler.append(f"{kid}: Lektionsziel {e.get('lektion')} für {key} existiert nicht"); continue
        ist.add(key); ziele[key] = e["ziel"]
        # Linktext: Überschrift des Ziels oder „gelöste Originalaufgabe“
        if "-original-" in e["ziel"]:
            text = "Gelöste Originalaufgabe mit Lösung"
        elif "-variante-" in e["ziel"]:
            text = "Übungsvariante mit Lösung"
        elif "-ihk-" in e["ziel"]:
            text = "Diese Aufgabe gelöst, mit Punkten"
        else:
            m = re.search(r'<h4 id="%s">([^<]*)</h4>' % re.escape(e["ziel"]), s)
            if m:
                text = html.unescape(m.group(1))
            else:
                d = re.search(r'<dl class="begriff" id="%s">\s*<dt>([^<]*)' % re.escape(e["ziel"]), s)
                text = ("Begriff: " + html.unescape(d.group(1)).strip()) if d else "Abschnitt im Kapitel"
        if e.get("lektion"):
            lm = re.search(r'<h4 id="%s">([^<]*)</h4>' % re.escape(e["lektion"]), s)
            dm = re.search(r'<dl class="begriff" id="%s">\s*<dt>([^<]*)' % re.escape(e["lektion"]), s)
            if lm:
                lektion_text = html.unescape(lm.group(1))
            elif dm:
                lektion_text = "Begriff: " + html.unescape(dm.group(1)).strip()
            else:
                fehler.append(f"{kid}: Lektionsziel {e['lektion']} für {key} ist keine Kernüberschrift"); continue
            zelle = (f'<a href="#{e["lektion"]}">Erst lernen: {html.escape(lektion_text)}</a><br>'
                     f'<a href="#{e["ziel"]}">Dann prüfen: {html.escape(text)}</a>')
        else:
            zelle = f'<a href="#{e["ziel"]}">{html.escape(text)}</a>'
        # Teil 2 bekommt dieselbe Zelle, nur mit dem Kapitelkuerzel klein davor.
        zellen[key] = f'<span class="kap">{kid.upper()}</span>' + zelle
        zeilen.append((REIHE.index(key[0]), key[1], key, zelle))
    for key in soll - ist:
        fehler.append(f"{kid}: Aufgabe {key} fehlt im Wegweiser")
    zeilen.sort(key=lambda z: (z[0], [int(x) for x in z[1].split(".")]))
    # Tabelle bauen
    tr = "".join(f'\n    <tr><td>{NAMEN[k[0]]}</td><td>{k[1]}</td><td>{html.escape(titel[k])}</td><td>{zelle}</td></tr>'
                 for _, _, k, zelle in zeilen)
    # Zugeklappt, damit beim Lesen von vorn die Lektion direkt nach dem Fall beginnt.
    # Wer eine Aufgabe löst, klappt die Tabelle auf. Der nav bleibt, damit check.js sie nicht als Lesetext zählt.
    tabelle = ('\n  <details class="wegweiser"><summary>Prüfungsaufgaben zu diesem Kapitel aufklappen (%d Aufgaben)</summary>'
               '\n  <nav aria-label="Prüfungsaufgaben dieses Kapitels"><div class="tabelle"><table>'
               '\n    <caption>Wo die Antwort steht</caption>'
               '\n    <tr><th>Prüfung</th><th>Aufgabe</th><th>Worum es ging</th><th>Hier steht es</th></tr>' + tr +
               '\n  </table></div></nav>\n  </details>\n') % len(zeilen)
    m = re.search(r'(<section id="%s-worum">[\s\S]*?)(\n\s*(?:<details class="wegweiser"><summary>[^<]*</summary>\s*)?'
                  r'<nav aria-label="Prüfungsaufgaben dieses Kapitels">[\s\S]*?</nav>\n(?:\s*</details>\n)?)?(</section>)' % kid, s)
    if not m:
        fehler.append(f"{kid}: Abschnitt worum nicht gefunden"); continue
    s = s[:m.start()] + m.group(1).rstrip() + tabelle + m.group(3) + s[m.end():]
    schreibe(dateien[0], s)
    print(f"{kid}: {len(zeilen)} Aufgaben verlinkt")

# Teil 2: die Aufgabenzeilen der neun Pruefungstabellen bekommen
#   - dieselbe Zelle wie der Wegweiser im Kapitel (Kuerzel klein davor),
#   - eine id und data-weg, damit der Rueckweg (Skript in 99-fuss.html) zur Zeile zurueckfindet.
# Idempotent: das Muster passt auf die alte wie auf die neue Zeilenform.
ZEILE = re.compile(r'^(\s*)<tr(?: [^>]*)?><td>([1-4]\.\d+)</td>'
                   r'(<td>[^<]*</td><td>[^<]*</td><td class="z">\d+</td>)<td>.*</td></tr>$')
mp = os.path.join(K, "03-matrix.html"); mx = io.open(mp, encoding="utf-8").read()
umgestellt = 0
for code in REIHE:
    a = mx.find(f'id="pruefung-{code.lower()}"'); b = mx.find("</table>", a)
    raus = []
    for z in mx[a:b].split(chr(10)):
        m = ZEILE.match(z)
        if not m:
            raus.append(z); continue
        einr, nr, mitte = m.group(1), m.group(2), m.group(3)
        rid = "p-%s-%s" % (code.lower(), nr.replace(".", "-"))
        weg = f'{NAMEN[code]}, Aufgabe {nr}'
        if (code, nr) in zellen:
            zelle = zellen[(code, nr)]; umgestellt += 1
        else:
            zelle = re.sub(r'^.*<td class="z">\d+</td><td>(.*)</td></tr>$', '\\1', z)
            fehler.append(f"Teil 2: {code} {nr} hat keinen Wegweiser-Eintrag")
        raus.append(f'{einr}<tr id="{rid}" data-weg="{html.escape(weg, quote=True)}"><td>{nr}</td>{mitte}<td>{zelle}</td></tr>')
    mx = mx[:a] + chr(10).join(raus) + mx[b:]
schreibe(mp, mx)
print(f"Teil 2: {umgestellt} Aufgabenzeilen mit der Wegweiser-Zelle, id und Rueckweg-Beschriftung")
if fehler:
    print("PROBLEME:"); [print("  ", f) for f in fehler]

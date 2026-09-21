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
zuordnung = json.load(io.open(os.path.join(N, "TIPPS-ZUORDNUNG.json"), encoding="utf-8"))
titel = {(z["pruefung"], z["nr"]): z["titel"] for z in zuordnung}

ziele = {}          # (pruefung, nr) -> ziel-id
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
        else:
            m = re.search(r'<h4 id="%s">([^<]*)</h4>' % re.escape(e["ziel"]), s)
            if m:
                text = html.unescape(m.group(1))
            else:
                d = re.search(r'<dl class="begriff" id="%s">\s*<dt>([^<]*)' % re.escape(e["ziel"]), s)
                text = ("Begriff: " + html.unescape(d.group(1)).strip()) if d else "Abschnitt im Kapitel"
        if e.get("lektion"):
            lm = re.search(r'<h4 id="%s">([^<]*)</h4>' % re.escape(e["lektion"]), s)
            if not lm:
                fehler.append(f"{kid}: Lektionsziel {e['lektion']} für {key} ist keine Kernüberschrift"); continue
            lektion_text = html.unescape(lm.group(1))
            zelle = (f'<a href="#{e["lektion"]}">Erst lernen: {html.escape(lektion_text)}</a><br>'
                     f'<a href="#{e["ziel"]}">Dann prüfen: {html.escape(text)}</a>')
        else:
            zelle = f'<a href="#{e["ziel"]}">{html.escape(text)}</a>'
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
    io.open(dateien[0], "w", encoding="utf-8").write(s)
    print(f"{kid}: {len(zeilen)} Aufgaben verlinkt")

# Matrix: Zeilen auf genaue Ziele umstellen
mp = os.path.join(K, "03-matrix.html"); mx = io.open(mp, encoding="utf-8").read()
def ersetze_tabelle(seg, code):
    def zeile(m):
        nr = m.group(1); key = (code, nr)
        if key in ziele:
            return m.group(0).replace(f'href="#{m.group(2)}"', f'href="#{ziele[key]}"', 1)
        return m.group(0)
    return re.sub(r'<tr><td>([1-4]\.\d+)</td>(?:<td>[^<]*</td>){2}<td class="z">\d+</td><td><a href="#([^"]+)">', zeile, seg)
n = 0
for code in REIHE:
    a = mx.find(f'id="pruefung-{code.lower()}"'); b = mx.find("</table>", a)
    seg = mx[a:b]; neu = ersetze_tabelle(seg, code)
    n += sum(1 for _ in re.finditer(r'href="#[ab]\d+-', neu)) - sum(1 for _ in re.finditer(r'href="#[ab]\d+-', seg))
    mx = mx[:a] + neu + mx[b:]
io.open(mp, "w", encoding="utf-8").write(mx)
print(f"Matrix: {sum(1 for _ in re.finditer(r'<tr><td>[1-4].[0-9]+</td>(?:<td>[^<]*</td>){2}<td class=.z.>[0-9]+</td><td><a href=.#[ab][0-9]+-', mx))} Aufgabenzeilen zeigen jetzt auf einen Absatz")
if fehler:
    print("PROBLEME:"); [print("  ", f) for f in fehler]

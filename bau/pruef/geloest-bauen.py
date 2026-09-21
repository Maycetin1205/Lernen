# -*- coding: utf-8 -*-
"""Baut je Kapitel den Abschnitt "Alle Pruefungsaufgaben geloest" aus notizen/20xx-*.md
und stellt den Wegweiser auf "Erst lernen / Dann pruefen" um. Idempotent: ein vorhandener
Abschnitt <kap>-geloest wird ersetzt."""
import re, json, glob, os, html, sys
sys.stdout.reconfigure(encoding="utf-8")
BAU = r"C:\Users\mu.aycetin\Desktop\Lernen\bau"
NAMEN = {"H21": "Herbst 2021", "F22": "Frühjahr 2022", "H22": "Herbst 2022", "F23": "Frühjahr 2023", "H23": "Herbst 2023",
         "F24": "Frühjahr 2024", "H24": "Herbst 2024", "F25": "Frühjahr 2025", "H25": "Herbst 2025"}
REIHE = list(NAMEN)
DATEI = {"H21": "2021-herbst", "F22": "2022-fruehjahr", "H22": "2022-herbst", "F23": "2023-fruehjahr", "H23": "2023-herbst",
         "F24": "2024-fruehjahr", "H24": "2024-herbst", "F25": "2025-fruehjahr", "H25": "2025-herbst"}
SRC = {c: "ihk-ap1-%s%s" % (c[0].lower(), "20" + c[1:]) for c in NAMEN}

def lies(p):
    raw = open(p, "rb").read()
    return raw.decode("utf-8").replace("\r\n", "\n"), (b"\r\n" in raw)

def schreibe(p, s, crlf):
    open(p, "wb").write((s.replace("\n", "\r\n") if crlf else s).encode("utf-8"))

# ---------- Notizen einlesen ----------
aufgaben = {}   # (code, nr) -> dict
for code, dn in DATEI.items():
    s, _ = lies(os.path.join(BAU, "notizen", dn + ".md"))
    bloecke = re.split(r"\n(?=### )", s)
    for b in bloecke:
        m = re.match(r"### ([\d.]+) \| (.*?) \| (\d+) P \| ([^|]*?) \| (\w+)\s*\n", b)
        if not m: continue
        nr, titel, punkte, op, kap = m.groups()
        rest = b[m.end():]
        rest = re.split(r"\n## ", rest)[0]
        # Felder
        felder = {}; akt = None
        for line in rest.split("\n"):
            lm = re.match(r"^(Aufgabe|Material|Lösungskern|Bemerkung)\b[^:\n]*:\s*(.*)$", line)
            if lm and not line.startswith(("- ", "|", "    ")) and lm.group(1) not in felder:
                akt = lm.group(1); felder[akt] = []
                if lm.group(2).strip(): felder[akt].append(lm.group(2))
                continue
            if akt: felder[akt].append(line)
        aufgaben[(code, nr)] = dict(nr=nr, titel=titel.strip(), punkte=int(punkte), op=op.strip(), kap=kap.lower(),
                                    **{k: "\n".join(v).strip() for k, v in felder.items()})

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`([^`]+)`", r"<code class=\"mono\">\1</code>", t)
    t = t.replace("—", " – ")
    return t

def md2html(t):
    """Absaetze, Listen, Codezaeune, Tabellen -> HTML (nur erlaubte Klassen)."""
    if not t: return ""
    out = []; zeilen = t.split("\n"); i = 0
    while i < len(zeilen):
        z = zeilen[i]
        if z.startswith("```"):
            j = i + 1; buf = []
            while j < len(zeilen) and not zeilen[j].startswith("```"): buf.append(zeilen[j]); j += 1
            out.append('<pre class="rechenweg">' + html.escape("\n".join(buf), quote=False) + "</pre>"); i = j + 1; continue
        if z.startswith("|"):
            j = i; buf = []
            while j < len(zeilen) and zeilen[j].startswith("|"): buf.append(zeilen[j]); j += 1
            rows = [r for r in buf if not re.match(r"^\|[\s:|-]+\|$", r)]
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            if cells:
                th = "".join("<th>%s</th>" % inline(c) for c in cells[0])
                tds = "".join("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>" for r in cells[1:])
                out.append('<table class="tabelle"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (th, tds))
            i = j; continue
        if re.match(r"^\s*[-*] ", z):
            j = i; buf = []
            while j < len(zeilen) and re.match(r"^\s*[-*] ", zeilen[j]): buf.append(re.sub(r"^\s*[-*] ", "", zeilen[j])); j += 1
            out.append("<ul>" + "".join("<li>%s</li>" % inline(b) for b in buf) + "</ul>"); i = j; continue
        if re.match(r"^\s*\d+[.)] ", z):
            j = i; buf = []
            while j < len(zeilen) and re.match(r"^\s*\d+[.)] ", zeilen[j]): buf.append(re.sub(r"^\s*\d+[.)] ", "", zeilen[j])); j += 1
            out.append("<ol>" + "".join("<li>%s</li>" % inline(b) for b in buf) + "</ol>"); i = j; continue
        if not z.strip(): i += 1; continue
        j = i; buf = []
        while j < len(zeilen) and zeilen[j].strip() and not re.match(r"^(```|\||\s*[-*] |\s*\d+[.)] )", zeilen[j]): buf.append(zeilen[j]); j += 1
        out.append("<p>%s</p>" % inline(" ".join(buf))); i = j
    return "\n".join(out)

# ---------- Dump-Modus: Aufgaben eines Kapitels kompakt ausgeben ----------
if len(sys.argv) > 2 and sys.argv[1] == "--dump":
    kid = sys.argv[2]
    wp = os.path.join(BAU, "notizen", "WEGWEISER-%s.json" % kid)
    for e in json.load(open(wp, encoding="utf-8")):
        if "-original-" in e["ziel"]: continue
        a = aufgaben[(e["pruefung"], e["nr"])]
        aid = "%s-ihk-%s-%s" % (kid, e["pruefung"].lower(), e["nr"].replace(".", "-"))
        print("=== %s | %s | %s | %d P | Lektion: %s" % (aid, a["titel"], a["op"], a["punkte"], e.get("lektion") or e["ziel"]))
        print("AUFGABE:", a.get("Aufgabe", "").strip())
        if a.get("Material"): print("MATERIAL:", a["Material"].strip())
        print("LOESUNG:", a.get("Lösungskern", "").strip())
        if a.get("Bemerkung"): print("BEMERKUNG:", re.sub(r"Heftbezeichnung:[^\n]*\n?", "", a["Bemerkung"]).strip())
        print()
    sys.exit(0)

# ---------- Erklaerungen (von Hand geschrieben) ----------
erkl = {}
for ep in glob.glob(os.path.join(BAU, "notizen", "ERKLAERUNG-*.json")):
    erkl.update(json.load(open(ep, encoding="utf-8")))

# ---------- Kapitel bearbeiten ----------
gesamt = 0; neu_ziele = 0; ohne_erkl = []
for wp in sorted(glob.glob(os.path.join(BAU, "notizen", "WEGWEISER-*.json"))):
    kid = re.search(r"WEGWEISER-(\w+)\.json", wp).group(1)
    kp = glob.glob(os.path.join(BAU, "kapitel", "*-%s.html" % kid))[0]
    s, crlf = lies(kp)
    ws, wcrlf = lies(wp)
    eintraege = json.loads(ws)
    # Ueberschriften und Begriffe fuer die "Erst lernen"-Zeile
    def ziel_text(z):
        m = re.search(r'<h4 id="%s">([^<]*)</h4>' % re.escape(z), s)
        if m: return html.unescape(m.group(1))
        d = re.search(r'<dl class="begriff" id="%s">\s*<dt>([^<]*)' % re.escape(z), s)
        if d: return "Begriff: " + html.unescape(d.group(1)).strip()
        return None
    # Quellen: vorhandene IHK-Eintraege je Pruefung
    qsec = re.search(r'<section id="%s-quellen">[\s\S]*?</section>' % kid, s).group(0)
    qmap = {m.group(2): m.group(1) for m in re.finditer(r'<li id="(%s-q\d+)" data-src="(ihk-ap1-[fh]20\d\d)"' % kid, qsec)}
    qmax = max(int(x) for x in re.findall(r'<li id="%s-q(\d+)"' % kid, qsec))
    neue_q = []
    artikel = []
    for e in eintraege:
        code, nr = e["pruefung"], e["nr"]
        if "-original-" in e["ziel"]: continue
        a = aufgaben.get((code, nr))
        if not a: print("FEHLT in Notizen:", kid, code, nr); continue
        lektion = e.get("lektion") or e["ziel"]
        lt = ziel_text(lektion)
        if lt is None: print("Lektionsziel unbekannt:", kid, code, nr, lektion); continue
        aid = "%s-ihk-%s-%s" % (kid, code.lower(), nr.replace(".", "-"))
        src = SRC[code]
        if src not in qmap:
            qmax += 1; qid = "%s-q%d" % (kid, qmax); qmap[src] = qid
            neue_q.append('    <li id="%s" data-src="%s"><span class="typ">IHK-Prüfung</span> ZPA Nord-West: Aufgabenheft und Lösungshinweise Abschlussprüfung %s, Teil 1. <span class="abruf">(nicht online geprüft)</span></li>' % (qid, src, NAMEN[code]))
        qid = qmap[src]; qn = qid.split("-q")[1]
        pkt = "1 Punkt" if a["punkte"] == 1 else "%d Punkte" % a["punkte"]
        heft = re.search(r"Heftbezeichnung:\s*([^\n]+)", a.get("Bemerkung", ""))
        bem = re.sub(r"Heftbezeichnung:[^\n]*\n?", "", a.get("Bemerkung", "")).strip()
        teile = ['  <article class="aufgabe" id="%s">' % aid,
                 '    <p class="herkunft">AP1 %s, Aufgabe %s, %s, sinngemäß wiedergegeben<sup class="q"><a href="#%s" title="AP1 %s">%s</a></sup></p>' % (NAMEN[code], nr, pkt, qid, NAMEN[code], qn),
                 '    <div class="text">',
                 '      <p><strong>%s</strong> (Operator: %s%s)</p>' % (inline(a["titel"]), inline(a["op"]), (", im Heft " + inline(heft.group(1).strip().rstrip("."))) if heft else ""),
                 md2html(a.get("Aufgabe", "")).replace("\n", "\n      ")]
        if a.get("Material"): teile.append('      <p><strong>Material im Heft:</strong></p>' + md2html(a["Material"]).replace("\n", "\n      "))
        teile.append('      <p>Der Weg dahin: <a href="#%s">%s</a></p>' % (lektion, html.escape(lt)))
        teile.append('    </div>')
        ek = erkl.get(aid)
        if ek:
            teile.append('    <details><summary>Denkweg und Lösung</summary><div class="inhalt">')
            teile.append('      <p><strong>So kommst du selbst drauf:</strong></p>')
            teile.append('      <ol>' + "".join("<li>%s</li>" % x for x in ek["denkweg"]) + '</ol>')
            teile.append('      <p><strong>Lösung der IHK:</strong></p>')
        else:
            ohne_erkl.append(aid)
            teile.append('    <details><summary>Lösung mit Punktelogik</summary><div class="inhalt">')
        teile.append(md2html(a.get("Lösungskern", "")).replace("\n", "\n      "))
        if bem: teile.append('      <p><strong>Warum so, und worauf die IHK achtet:</strong></p>' + md2html(bem).replace("\n", "\n      "))
        if ek and ek.get("mitnehmen"):
            teile.append('      <p><strong>Das nimmst du mit in deine Prüfung:</strong> %s</p>' % ek["mitnehmen"])
        teile.append('    </div></details>')
        teile.append('  </article>')
        artikel.append((REIHE.index(code), [int(x) for x in nr.split(".")], "\n".join(teile)))
        # Wegweiser umstellen
        if e["ziel"] != aid:
            e["lektion"] = lektion; e["ziel"] = aid; neu_ziele += 1
    artikel.sort(key=lambda x: (x[0], x[1]))
    n = len(artikel); gesamt += n
    block = ('<section id="%s-geloest">\n  <h3>Alle Prüfungsaufgaben zu diesem Kapitel, gelöst</h3>\n'
             '  <p>Hier steht jede Aufgabe aus den neun Prüfungen, die zu diesem Kapitel gehört, mit der Lösung aus den IHK-Lösungshinweisen und dem Link zu der Stelle im Kapitel, die den Weg dahin erklärt. Erst selbst rechnen oder schreiben, dann die Lösung aufklappen.</p>\n'
             '  <details class="geloest"><summary>Gelöste Aufgaben aufklappen (%d Aufgaben)</summary>\n%s\n  </details>\n</section>\n\n') % (kid, n, "\n\n".join(x[2] for x in artikel))
    s = re.sub(r'<section id="%s-geloest">[\s\S]*?</section>\n\n' % kid, "", s)
    marke = '<section id="%s-selbstcheck">' % kid
    assert marke in s, kid
    s = s.replace(marke, block + marke, 1)
    if neue_q:
        s = re.sub(r'(<section id="%s-quellen">[\s\S]*?)(</ol>)' % kid, lambda m: m.group(1) + "\n" + "\n".join(neue_q) + "\n" + m.group(2), s, count=1)
    schreibe(kp, s, crlf)
    schreibe(wp, json.dumps(eintraege, ensure_ascii=False, indent=1) + "\n", wcrlf)
    print("%s: %d gelöste Aufgaben, %d neue Quellen" % (kid, n, len(neue_q)))
print("Gesamt:", gesamt, "Artikel;", neu_ziele, "Wegweiser-Ziele umgestellt;", len(ohne_erkl), "ohne Denkweg")
if ohne_erkl: print("Ohne Denkweg:", " ".join(ohne_erkl))

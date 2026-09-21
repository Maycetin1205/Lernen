# -*- coding: utf-8 -*-
"""Tipps in die Prüfungs-PDF schreiben: je Prüfung ein Tipp-Blatt, je Aufgabe ein Kasten im Korrekturrand.
Aufruf: python tipps-pdf.py <Quell-PDF> <Ziel-PDF> <Render-Ordner>
Schreibt außerdem bau/notizen/TIPPS-ZUORDNUNG.json und .md (die Zuordnung Teilaufgabe -> Kapitel)."""
import fitz, re, json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\mu.aycetin\Desktop\Lernen\bau"
SRC, OUT, RENDER = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(RENDER, exist_ok=True)

KURZ = {"A1":"IPv4/Subnetting","A2":"Kaufm. Rechnen","A3":"Nutzwertanalyse","A4":"Einheiten/Speicher","A5":"Strom/Energie",
        "A6":"Netzplan/Gantt","A7":"Programmlogik","A8":"UML-Diagramme","A9":"ER-Modell/SQL","B1":"IT-Sicherheit I","B2":"Kryptografie",
        "B3":"Datenschutz","B4":"Hardware/Anschl.","B5":"Netzwerk-Grundl.","B6":"Software/Lizenzen","B7":"Datensicherung/RAID","B8":"Arbeitsplatz/Ergon.",
        "B9":"Projekt/Anford.","B10":"Kunde/Kommunik.","B11":"Wirtschaft/Recht"}
LANG = {"A1":"IPv4, Subnetting und Netzkonfiguration","A2":"Kaufmännisch rechnen","A3":"Nutzwertanalyse","A4":"Einheiten, Speicher und Datenrate",
        "A5":"Strom und Energiekosten","A6":"Netzplan und Gantt","A7":"Programmlogik und Schreibtischtest","A8":"UML-Diagramme",
        "A9":"Datenmodell und ER-Diagramm","B1":"IT-Sicherheit I: Schutzziele, Zugang, Angriffe","B2":"IT-Sicherheit II: Kryptografie und sichere Verbindungen",
        "B3":"Datenschutz: DSGVO und BDSG","B4":"Hardware und Anschlüsse","B5":"Netzwerk-Grundlagen","B6":"Software, Lizenzen und Web",
        "B7":"Datensicherung und Verfügbarkeit","B8":"Arbeitsplatz: Ergonomie, Barrierefreiheit, Nachhaltigkeit","B9":"Projekt, Anforderungen und Vorgehen",
        "B10":"Kunde, Kommunikation und Veränderung","B11":"Wirtschaft und Recht"}
PRUEF = [("H21","2021-herbst.md","Herbst 2021"),("F22","2022-fruehjahr.md","Frühjahr 2022"),("H22","2022-herbst.md","Herbst 2022"),
         ("F23","2023-fruehjahr.md","Frühjahr 2023"),("H23","2023-herbst.md","Herbst 2023"),("F24","2024-fruehjahr.md","Frühjahr 2024"),
         ("H24","2024-herbst.md","Herbst 2024"),("F25","2025-fruehjahr.md","Frühjahr 2025"),("H25","2025-herbst.md","Herbst 2025")]

# ---------- 1. Zuordnung aus Notizen + 03-matrix.html ----------
html = open(os.path.join(ROOT, "kapitel", "03-matrix.html"), encoding="utf-8").read()
mx = {}
for code, _, _ in PRUEF:
    seg = html.split(f'id="pruefung-{code.lower()}"', 1)[1].split("</table>", 1)[0]
    for m in re.finditer(r'<tr><td>([1-4]\.\d+)</td><td>(.*?)</td><td>(.*?)</td><td class="z">(\d+)</td><td><a href="#([ab]\d+)">', seg):
        mx[(code, m.group(1))] = (m.group(2), int(m.group(4)), m.group(5).upper())
zuordnung = []
fehler = []
for code, fn, name in PRUEF:
    txt = open(os.path.join(ROOT, "notizen", fn), encoding="utf-8").read()
    for b in re.split(r'\n(?=### [1-4]\.\d+ \|)', txt):
        h = re.match(r'### ([1-4]\.\d+) \| (.*?) \| (\d+) P \| (\w+) \| ([ab]\d+)', b)
        if not h:
            continue
        nr, titel, pkt, op, kap = h.groups()
        lab = re.search(r'Heftbezeichnung:\s*([1-4])\. Aufgabe ([a-z]{1,3})\)', b) or re.search(r'Heftbezeichnung:\s*([1-4])([a-z]{1,3})\.', b)
        if not lab:
            fehler.append(f"{code} {nr}: keine Heftbezeichnung")
            continue
        m = mx.get((code, nr))
        if lab.group(1) != nr.split(".")[0]:
            fehler.append(f"{code} {nr}: Heft nennt Aufgabe {lab.group(1)}")
        if not m:
            fehler.append(f"{code} {nr}: fehlt in 03-matrix.html")
        elif m[2] != kap.upper() or m[1] != int(pkt):
            fehler.append(f"{code} {nr}: Notiz {kap}/{pkt}P vs Matrix {m[2]}/{m[1]}P")
        zuordnung.append(dict(pruefung=code, name=name, nr=nr, aufgabe=int(nr.split(".")[0]), heft=lab.group(2) + ")",
                              titel=titel.strip(), punkte=int(pkt), operator=op, kapitel=kap.upper()))
summen = {}
for z in zuordnung:
    summen[z["pruefung"]] = summen.get(z["pruefung"], 0) + z["punkte"]
print("Zuordnung:", len(zuordnung), "Teilaufgaben; Punkte je Prüfung:", summen)
if fehler or len(zuordnung) != 252 or any(v != 100 for v in summen.values()):
    print("ABBRUCH, Zuordnung unvollständig:", fehler)
    sys.exit(1)
json.dump(zuordnung, open(os.path.join(ROOT, "notizen", "TIPPS-ZUORDNUNG.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(os.path.join(ROOT, "notizen", "TIPPS-ZUORDNUNG.md"), "w", encoding="utf-8") as f:
    f.write("# Tipps: Welche Teilaufgabe steht in welchem Kapitel der Lerndatei\n\n"
            "Quelle: Notizen 2021-herbst.md bis 2025-herbst.md (Heftbezeichnung) und kapitel/03-matrix.html (Kapitel). "
            "252 Teilaufgaben, 900 Punkte.\n")
    for code, _, name in PRUEF:
        f.write(f"\n## AP1 {name}\n\n| Heft | Nr. | Worum es ging | P | Kapitel |\n|---|---|---|---|---|\n")
        for z in zuordnung:
            if z["pruefung"] == code:
                f.write(f"| {z['aufgabe']}. Aufgabe {z['heft']} | {z['nr']} | {z['titel']} | {z['punkte']} | {z['kapitel']} {LANG[z['kapitel']]} |\n")

# ---------- 2. PDF öffnen, Lösungsseiten Herbst 2022 (S. 40-45) entfernen ----------
doc = fitz.open(SRC)
assert len(doc) == 112, f"erwarte 112 Seiten, gefunden {len(doc)}"
assert "sungshinweise" in doc[39].get_text() and "Kopfleiste" in doc[45].get_text(), "S. 40-45 sind nicht die erwarteten Lösungsseiten"
doc.delete_pages(39, 44)
toc = doc.get_toc()
print("Nach Löschen der Lösungsseiten:", len(doc), "Seiten; Lesezeichen:", [t[2] for t in toc])
assert [t[2] for t in toc] == [1, 13, 27, 40, 49, 61, 70, 80, 92], "Lesezeichen zeigen nicht auf die Deckblätter"

# ---------- 2b. Leere Seiten entfernen (S. 12 = weiße Rückseite am Ende von Herbst 2021) ----------
LEER = [12]                                     # Seitenzahlen nach Schritt 2
for pn in sorted(LEER, reverse=True):
    p = doc[pn - 1]
    pix = p.get_pixmap(dpi=30, colorspace=fitz.csGRAY)
    assert p.get_text().strip() == "" and sum(pix.samples) / len(pix.samples) > 253, f"S. {pn} ist nicht leer"
    doc.delete_page(pn - 1)
def versetzt(v): return v - sum(1 for l in LEER if l < v)
toc = doc.get_toc()
soll_toc = [versetzt(v) for v in (1, 13, 27, 40, 49, 61, 70, 80, 92)]
assert [t[2] for t in toc] == soll_toc, f"Lesezeichen {[t[2] for t in toc]} statt {soll_toc}"
print("Nach Löschen der leeren Seiten:", len(doc), "Seiten; Lesezeichen:", soll_toc)
deckblatt = {code: toc[i][2] for i, (code, _, _) in enumerate(PRUEF)}   # 1-basiert

# ---------- 3. Startseiten der Aufgaben finden ----------
ERWARTET = {"H21": [2, 4, 6, 9], "F22": [14, 17, 20, 23], "H22": [28, 30, 32, 34], "F23": [41, 42, 44, 46], "H23": [50, 52, 54, 56],
            "F24": [62, 64, 66, 68], "H24": [71, 73, 76, 78], "F25": [81, 84, 85, 89], "H25": [93, 96, 99, 103]}
ERWARTET = {k: [versetzt(v) for v in vs] for k, vs in ERWARTET.items()}   # um die gelöschten leeren Seiten verschoben
start = {}
grenzen = [deckblatt[c] for c, _, _ in PRUEF] + [len(doc) + 1]
for i, (code, _, _) in enumerate(PRUEF):
    gef = {}
    for pn in range(grenzen[i], grenzen[i + 1]):
        for m in re.finditer(r'([1-4])\.\s*Aufgabe\s*\(\s*(\d+)\s*Punkte', doc[pn - 1].get_text()):
            gef.setdefault(int(m.group(1)), pn)
    start[code] = [gef.get(a) for a in (1, 2, 3, 4)]
    if start[code] != ERWARTET[code]:
        print(f"  {code}: gefunden {start[code]}, erwartet {ERWARTET[code]} -> nehme Erwartungstabelle (Sichtprüfung im Render!)")
        start[code] = ERWARTET[code]
print("Aufgaben-Startseiten (vor Einfügen der Tipp-Blätter):", start)

# ---------- 4. Kästen im Korrekturrand (vor dem Einfügen, damit Seitenzahlen stimmen) ----------
def kasten(page, zeilen):
    W, H = page.rect.width, page.rect.height
    s = W / 595
    if W > 1000:
        # Herbst 2025: Scans ohne brauchbaren Korrekturrand (rechts abgeschnitten, schief).
        # Seite rechts um 12 % verbreitern, den unbrauchbaren Scanrand weiß decken, Kasten in den neuen Streifen.
        alt = page.rect
        page.set_mediabox(fitz.Rect(alt.x0, alt.y0, alt.x1 + 0.12 * W, alt.y1))
        page.draw_rect(fitz.Rect(alt.x1 - 0.075 * W, alt.y0, alt.x1 + 0.12 * W, alt.y1), color=None, fill=(1, 1, 1))
        x0, x1 = alt.x1 - 0.068 * W, alt.x1 + 0.112 * W
    else:
        x0, x1 = W * 0.852, W * 0.988
    y0 = H * 0.072
    fs = 7.2 * s
    def breite(f): return max(fitz.get_text_length(z, fontname="helv", fontsize=f) for z in zeilen)
    while breite(fs) > (x1 - x0) - 5 * s and fs > 4.8 * s:
        fs -= 0.1 * s
    lh = fs * 1.28
    hoehe = lh * (len(zeilen) + 1.2)
    r = fitz.Rect(x0, y0, x1, y0 + hoehe)
    page.draw_rect(r, color=(0.15, 0.15, 0.15), fill=(1, 1, 1), width=0.6 * s)
    y = y0 + lh * 1.05
    page.insert_text(fitz.Point(x0 + 2.5 * s, y), "Lerndatei:", fontname="hebo", fontsize=fs)
    for z in zeilen:
        y += lh
        page.insert_text(fitz.Point(x0 + 2.5 * s, y), z, fontname="helv", fontsize=fs)
    return r

kaesten = []
for code, _, name in PRUEF:
    for a in (1, 2, 3, 4):
        pn = start[code][a - 1]
        page = doc[pn - 1]
        assert page.rotation == 0, f"{code} Aufgabe {a}: Seite {pn} ist gedreht"
        zeilen = [f"{z['heft']} » {z['kapitel']} {KURZ[z['kapitel']]}" for z in zuordnung if z["pruefung"] == code and z["aufgabe"] == a]
        kasten(page, zeilen)
        kaesten.append((code, a, pn))

# ---------- 5. Tipp-Blatt je Prüfung vor das Deckblatt ----------
def tippblatt(doc, vor_seite, code, name):
    page = doc.new_page(pno=vor_seite - 1, width=595, height=842)
    y = 60
    page.insert_text((45, y), f"AP1 {name}: Wo steht das in der Lerndatei?", fontname="hebo", fontsize=15)
    y += 20
    page.insert_text((45, y), "Löse die Prüfung auf Papier. Hängst du bei einer Teilaufgabe, schlag das Kapitel in AP1_Lerndatei.html nach.", fontname="helv", fontsize=8.5)
    y += 11
    page.insert_text((45, y), "Dort steht die Aufgabe auch unter »Kam dran« und als gelöstes Original. Die Nummer (z. B. 1.3) ist der Name der Aufgabe in der Lerndatei.", fontname="helv", fontsize=8.5)
    y += 22
    def kuerzen(text, font, fs, maxbreite):
        basis = text
        while fitz.get_text_length(text, fontname=font, fontsize=fs) > maxbreite and len(basis) > 3:
            basis = basis[:-1].rstrip()
            text = basis + "..."
        return text
    for a in (1, 2, 3, 4):
        rows = [z for z in zuordnung if z["pruefung"] == code and z["aufgabe"] == a]
        page.insert_text((45, y), f"{a}. Aufgabe ({sum(r['punkte'] for r in rows)} Punkte)", fontname="hebo", fontsize=10.5)
        y += 15
        for r in rows:
            page.insert_text((50, y), r["heft"], fontname="hebo", fontsize=8.5)
            page.insert_text((74, y), r["nr"], fontname="helv", fontsize=8.5, color=(0.35, 0.35, 0.35))
            page.insert_text((98, y), kuerzen(r["titel"], "helv", 8.5, 222), fontname="helv", fontsize=8.5)
            page.insert_text((326, y), f"{r['punkte']:>2} P", fontname="helv", fontsize=8.5)
            page.insert_text((352, y), kuerzen(f"{r['kapitel']}  {LANG[r['kapitel']]}", "helv", 8.5, 200), fontname="helv", fontsize=8.5)
            y += 12.5
        y += 9
    page.insert_text((45, 800), "Zuordnung aus AP1_Lerndatei.html, Teil »Was wie oft drankam«, Abschnitt »Die neun Prüfungen im Einzelnen«.", fontname="helv", fontsize=7, color=(0.35, 0.35, 0.35))
    return page

TIPPBLAETTER = "--tippblaetter" in sys.argv   # Nutzerwunsch 2026-09-08: standardmäßig keine Tipp-Blätter, nur die Kästen rechts
neue_toc = []
for i, (code, _, name) in enumerate(PRUEF):
    if TIPPBLAETTER:
        ziel = deckblatt[code] + i       # jedes vorherige Tipp-Blatt verschiebt um 1
        tippblatt(doc, ziel, code, name)
    else:
        ziel = deckblatt[code]
    neue_toc.append([1, f"AP1 {name}", ziel])
doc.set_toc(neue_toc)
doc.save(OUT, garbage=3, deflate=True)
print("Gespeichert:", OUT, len(doc), "Seiten; Lesezeichen ->", [t[2] for t in neue_toc])

# ---------- 6. Renders zur Sichtprüfung ----------
doc = fitz.open(OUT)
def montage(seiten, name, cols=6, dpi=42):
    cw, ch = 300, 420
    m = fitz.open()
    pg = m.new_page(width=cols * cw, height=((len(seiten) + cols - 1) // cols) * ch)
    for k, pn in enumerate(seiten):
        pix = doc[pn - 1].get_pixmap(dpi=dpi)
        r = fitz.Rect((k % cols) * cw + 4, (k // cols) * ch + 4, (k % cols + 1) * cw - 4, (k // cols + 1) * ch - 16)
        pg.insert_image(r, pixmap=pix, keep_proportion=True)
        pg.insert_text(((k % cols) * cw + 6, (k // cols + 1) * ch - 4), f"S.{pn}", fontsize=9)
    pg.get_pixmap(dpi=72).save(os.path.join(RENDER, name))

verschiebung = {code: (i + 1 if TIPPBLAETTER else 0) for i, (code, _, _) in enumerate(PRUEF)}
aufg_seiten = [pn + verschiebung[code] for code, a, pn in kaesten]
montage(aufg_seiten[:18], "aufgaben-1.png")
montage(aufg_seiten[18:], "aufgaben-2.png")
for pn in (aufg_seiten[0], aufg_seiten[32]):
    doc[pn - 1].get_pixmap(dpi=110).save(os.path.join(RENDER, f"gross-S{pn}.png"))
montage(aufg_seiten[32:], "h25.png", cols=4, dpi=60)
if TIPPBLAETTER:
    montage([t[2] for t in neue_toc], "tippblaetter.png", cols=5, dpi=50)
    doc[0].get_pixmap(dpi=100).save(os.path.join(RENDER, "tippblatt-1.png"))
print("Renders in", RENDER, "| Aufgabenseiten im neuen PDF:", aufg_seiten)

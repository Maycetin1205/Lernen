# -*- coding: utf-8 -*-
"""Vorschau und Bildprüfung für EIN Kapitel.

Aufruf:  python pruef/vorschau.py <kapitel-id>        z. B.  python pruef/vorschau.py a6

Macht drei Dinge, ohne andere Dateien zu verändern:
1. Baut aus bau/AP1_Lerndatei.html (Kopf, Navigation, Fuß) und bau/kapitel/NN-<id>.html eine
   Vorschauseite  bau/notizen/vorschau/<id>.html  (nur dieses Kapitel).
2. Rendert sie mit Headless Edge bei 1366 px Breite und schneidet das Bild in Streifen
   bau/notizen/vorschau/<id>-teil1.png, -teil2.png ...  (je 1900 px hoch). Diese PNGs mit dem
   Read-Werkzeug ansehen: Sitzen die Bilder? Läuft Text über Ränder? Ist die Reihenfolge logisch?
3. Misst alle Abbildungen dieses Kapitels auf Textüberlappung (wie pruef/svgcheck.py) und schreibt
   bau/notizen/vorschau/<id>-svgbefunde.txt. Befunde werden auch hier ausgegeben.
"""
import io, os, re, sys, glob, html, subprocess
sys.stdout.reconfigure(encoding="utf-8")
BAU = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if len(sys.argv) < 2 or not re.fullmatch(r"[ab]\d{1,2}", sys.argv[1]):
    print("Aufruf: python pruef/vorschau.py <kapitel-id>   (a1 … a9, b1 … b11)"); sys.exit(2)
kid = sys.argv[1]
treffer = glob.glob(os.path.join(BAU, "kapitel", f"*-{kid}.html"))
if len(treffer) != 1:
    print("Kapiteldatei nicht eindeutig:", treffer); sys.exit(2)
fragment = io.open(treffer[0], encoding="utf-8").read()
aus = os.path.join(BAU, "notizen", "vorschau"); os.makedirs(aus, exist_ok=True)

# 1. Vorschauseite
ganz = io.open(os.path.join(BAU, "AP1_Lerndatei.html"), encoding="utf-8").read()
i_main = ganz.index("<main")
i_first = min(x for x in [ganz.find('<section class="teil"', i_main), ganz.find('<section class="kapitel"', i_main)] if x >= 0)
i_end = ganz.index("</main>")
seite = os.path.join(aus, f"{kid}.html")
io.open(seite, "w", encoding="utf-8").write(ganz[:i_first] + fragment + ganz[i_end:])

# 2. Screenshot in Streifen. Eigenes Profilverzeichnis je Kapitel, damit mehrere Edge-Instanzen
#    gleichzeitig laufen können (sonst blockieren sie sich gegenseitig am Standardprofil).
png = os.path.join(aus, f"{kid}-voll.png")
profil = os.path.join(aus, f"profil-{kid}")
EDGE_OPTS = [EDGE, "--headless=new", "--disable-gpu", "--allow-file-access-from-files", "--no-first-run",
             "--no-default-browser-check", f"--user-data-dir={profil}", "--virtual-time-budget=8000"]
def screenshot(hoehe):
    if os.path.exists(png): os.remove(png)
    subprocess.run(EDGE_OPTS + ["--hide-scrollbars", f"--window-size=1366,{hoehe}", f"--screenshot={png}",
                                "file:///" + seite.replace("\\", "/")], capture_output=True, text=True, timeout=240)
    return os.path.exists(png)
ok = False
for hoehe in (16000, 10000):
    try:
        ok = screenshot(hoehe)
    except subprocess.TimeoutExpired:
        ok = False
    if ok: break
if not ok:
    print("WARNUNG: Screenshot fehlgeschlagen (Edge antwortet nicht). Später erneut versuchen.")
streifen = []
try:
    if not ok: raise ImportError
    from PIL import Image
    im = Image.open(png); W, H = im.size
    g = im.convert("L"); ende = 400
    for y in range(H - 1, 200, -10):                      # Inhaltsende: letzte Zeile mit Tinte in der Textspalte
        if g.crop((380, y, 1340, y + 1)).getextrema()[0] < 235:
            ende = min(H, y + 60); break
    for k, y in enumerate(range(0, ende, 1900)):
        p = os.path.join(aus, f"{kid}-teil{k + 1}.png")
        im.crop((0, y, W, min(y + 1900, ende))).save(p); streifen.append(p)
    for alt in glob.glob(os.path.join(aus, f"{kid}-teil*.png")):
        if alt not in streifen: os.remove(alt)
    os.remove(png)
except ImportError:
    streifen = [png]
print(f"Vorschau: {seite}")
print("Streifen zum Ansehen (Read-Werkzeug):")
for p in streifen: print("  ", p)

# 3. Textüberlappung in den Abbildungen dieses Kapitels
kopf = io.open(os.path.join(BAU, "kapitel", "00-kopf.html"), encoding="utf-8").read()
css = re.search(r"<style>([\s\S]*?)</style>", kopf).group(1)
defs = re.search(r"(<svg[^>]*aria-hidden[^>]*>[\s\S]*?</svg>)", kopf)
defs = defs.group(1) if defs else ""
figs = []
for i, fig in enumerate(re.findall(r"<figure class=\"abb\">[\s\S]*?</figure>", fragment)):
    cap = re.search(r"<figcaption>(Abb\. [^:]+):", fig)
    figs.append((cap.group(1) if cap else f"{kid}#{i + 1}", fig))
script = r"""
<script>
const out = [];
const rects = (a, b) => !(a.x + a.width <= b.x || b.x + b.width <= a.x || a.y + a.height <= b.y || b.y + b.height <= a.y);
document.querySelectorAll('figure.abb').forEach(fig => {
  const name = fig.dataset.name, svg = fig.querySelector('svg');
  const vb = svg.viewBox.baseVal; const texts = [...svg.querySelectorAll('text')];
  const boxes = texts.map(t => { const b = t.getBBox(); return {t, b, s: (t.textContent || '').trim()}; });
  boxes.forEach(({b, s}) => {
    if (b.width === 0) return;
    if (b.x < vb.x - 1 || b.y < vb.y - 1 || b.x + b.width > vb.x + vb.width + 1 || b.y + b.height > vb.y + vb.height + 1)
      out.push(name + ' | RAND | "' + s + '" ragt aus dem Bild (x ' + Math.round(b.x) + '..' + Math.round(b.x + b.width) + ', y ' + Math.round(b.y) + '..' + Math.round(b.y + b.height) + ', Bild ' + vb.width + 'x' + vb.height + ')');
  });
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const A = boxes[i], B = boxes[j]; if (!A.s || !B.s) continue;
    if (rects(A.b, B.b)) {
      const ix = Math.min(A.b.x + A.b.width, B.b.x + B.b.width) - Math.max(A.b.x, B.b.x);
      const iy = Math.min(A.b.y + A.b.height, B.b.y + B.b.height) - Math.max(A.b.y, B.b.y);
      if (ix > 2 && iy > 2) out.push(name + ' | TEXT-TEXT | "' + A.s + '" ueberlappt "' + B.s + '" (' + Math.round(ix) + 'x' + Math.round(iy) + ')');
    }
  }
  const rs = [...svg.querySelectorAll('rect')].map(r => ({x: +r.getAttribute('x') || 0, y: +r.getAttribute('y') || 0, w: +r.getAttribute('width') || 0, h: +r.getAttribute('height') || 0}));
  boxes.forEach(({b, s}) => {
    if (!s) return; const cx = b.x + b.width / 2, cy = b.y + b.height / 2;
    rs.forEach(r => { if (cx > r.x && cx < r.x + r.w && cy > r.y && cy < r.y + r.h && (b.x < r.x - 1 || b.x + b.width > r.x + r.w + 1))
      out.push(name + ' | BOX | "' + s + '" breiter als seine Box (Text ' + Math.round(b.width) + ', Box ' + r.w + ')'); });
  });
});
document.title = 'FERTIG';
document.getElementById('out').textContent = out.join('\n') || 'Keine Befunde.';
</script>"""
pruefseite = ['<!doctype html><html lang="de"><head><meta charset="utf-8"><style>' + css + ' figure.abb{width:640px}</style></head><body>' + defs]
for name, fig in figs:
    pruefseite.append(fig.replace('<figure class="abb">', '<figure class="abb" data-name="' + html.escape(name) + '">', 1))
pruefseite.append('<pre id="out"></pre>' + script + '</body></html>')
ppfad = os.path.join(aus, f"{kid}-svgcheck.html")
io.open(ppfad, "w", encoding="utf-8").write("\n".join(pruefseite))
try:
    dom = subprocess.run(EDGE_OPTS + ["--dump-dom", "file:///" + ppfad.replace("\\", "/")],
                         capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240).stdout
except subprocess.TimeoutExpired:
    dom = ""
m = re.search(r'<pre id="out">([\s\S]*?)</pre>', dom)
bef = html.unescape(m.group(1)).strip() if m else "KEINE AUSGABE (Headless fehlgeschlagen)"
io.open(os.path.join(aus, f"{kid}-svgbefunde.txt"), "w", encoding="utf-8").write(bef)
print(f"Abbildungen geprüft: {len(figs)} | Befunde: {bef if bef == 'Keine Befunde.' else ''}")
if bef != "Keine Befunde.":
    for z in bef.split("\n"): print("  ", z[:160])

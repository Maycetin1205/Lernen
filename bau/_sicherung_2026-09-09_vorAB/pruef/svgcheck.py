# -*- coding: utf-8 -*-
# Mechanische Sichtpruefung aller Abbildungen: baut eine Pruefseite mit allen figure.abb, misst im Headless-Browser
# jede Textbox (getBBox) gegen viewBox und gegen andere Texte, und liefert eine Befundliste. Kein LLM.
import io, re, subprocess, os, json, html
BAU = r"C:\Users\mu.aycetin\Desktop\Lernen\bau"
SCR = os.path.dirname(os.path.abspath(__file__))
kopf = io.open(os.path.join(BAU, "kapitel", "00-kopf.html"), encoding="utf-8").read()
css = re.search(r"<style>([\s\S]*?)</style>", kopf).group(1)
defs = re.search(r"(<svg[^>]*aria-hidden[^>]*>[\s\S]*?</svg>)", kopf)   # Marker-Definitionen
defs = defs.group(1) if defs else ""
figs = []
for f in sorted(os.listdir(os.path.join(BAU, "kapitel"))):
    if not re.match(r"^(1\d|2\d|30)-", f): continue
    s = io.open(os.path.join(BAU, "kapitel", f), encoding="utf-8").read()
    for i, fig in enumerate(re.findall(r"<figure class=\"abb\">[\s\S]*?</figure>", s)):
        cap = re.search(r"<figcaption>(Abb\. [^:]+):", fig)
        figs.append((cap.group(1) if cap else f + "#" + str(i + 1), fig))
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
  // Text ueber Boxen, in denen er nicht steht: Text ragt ueber den Rand eines rect, in dem sein Mittelpunkt liegt
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
seite = ['<!doctype html><html lang="de"><head><meta charset="utf-8"><style>' + css + ' figure.abb{width:640px}</style></head><body>' + defs]
for name, fig in figs:
    seite.append(fig.replace('<figure class="abb">', '<figure class="abb" data-name="' + html.escape(name) + '">', 1))
seite.append('<pre id="out"></pre>' + script + '</body></html>')
pfad = os.path.join(SCR, "svgcheck.html")
io.open(pfad, "w", encoding="utf-8").write("\n".join(seite))
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
dom = subprocess.run([edge, "--headless=new", "--disable-gpu", "--allow-file-access-from-files", "--virtual-time-budget=8000",
                      "--dump-dom", "file:///" + pfad.replace("\\", "/")], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
m = re.search(r'<pre id="out">([\s\S]*?)</pre>', dom)
bef = html.unescape(m.group(1)).strip() if m else "KEINE AUSGABE (Headless fehlgeschlagen)"
zeilen = [z for z in bef.split("\n") if z.strip()]
print("Abbildungen geprueft:", len(figs))
print("Befunde:", 0 if bef == "Keine Befunde." else len(zeilen))
arten = {}
for z in zeilen:
    art = z.split(" | ")[1] if " | " in z else "?"; arten[art] = arten.get(art, 0) + 1
print("nach Art:", arten)
io.open(os.path.join(SCR, "svgbefunde.txt"), "w", encoding="utf-8").write(bef)
for z in zeilen[:40]: print(" ", z[:150])

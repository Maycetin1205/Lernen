#!/usr/bin/env python3
"""Erzeugt das Lego-Modell des Roboters als LDraw-Datei (roboter.ldr) fuer BrickLink Studio.

Raster: x = Breite, z = Tiefe (kleines z ist vorn), h = Hoehe in Platten (1 Stein = 3 Platten).
Aufruf:  python3 build_model.py
"""
import json
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = json.load(open(os.path.join(HERE, 'parts.json')))

YELLOW, BLACK, LGREY, DGREY = 14, 0, 71, 72
COLOR_NAMES = {14: 'Gelb', 0: 'Schwarz', 71: 'Hellgrau', 72: 'Dunkelgrau'}

BRICK1 = {1: '3005', 2: '3004', 3: '3622', 4: '3010', 6: '3009', 8: '3008', 10: '6111'}
TILES = {'2431', '3068b', '6636', '4162', '3069b'}
LINKS_PER_SIDE = 25
EXTERNAL = {'57518': 'Kettenglied breit (5 Noppen)', '57519': 'Kettenrad groß, 10 Zähne', '57520': 'Kettenrad klein, 6 Zähne'}
LOW = {'-z': 0, '-x': 1, '+z': 2, '+x': 3}   # Richtung, in die ein Dachstein abfaellt


def rot_xz(k, x, z):
    k %= 4
    if k == 0:
        return x, z
    if k == 1:
        return z, -x
    if k == 2:
        return -x, -z
    return -z, x


MATS = {0: (1, 0, 0, 0, 1, 0, 0, 0, 1), 1: (0, 0, 1, 0, 1, 0, -1, 0, 0),
        2: (-1, 0, 0, 0, 1, 0, 0, 0, -1), 3: (0, 0, -1, 0, 1, 0, 1, 0, 0)}


class Model:
    def __init__(self):
        self.items = []
        self.step = 'Start'
        self.ox = 0      # Versatz in Noppen fuer alles, was relativ zum Rumpf gesetzt wird
        self.oh = 0      # Versatz in Platten

    def raw(self, part, color, pos, rot=0, ext=False):
        """Teil ausserhalb des Noppenrasters (Achsen, Kettenraeder). pos in LDraw-Einheiten, y nach unten."""
        self.items.append(dict(part=part, color=color, pos=pos, rot=rot % 4, raw=True, ext=ext, step=self.step))

    def add(self, part, color, x, z, h, rot=0):
        """Setzt ein Teil so, dass seine Grundflaeche bei Noppe (x, z) beginnt und seine Unterseite auf Hoehe h liegt."""
        p = PARTS[part]
        x, h = x + self.ox, h + self.oh
        c = [rot_xz(rot, cx, cz) for cx in (p['xmin'], p['xmax']) for cz in (p['zmin'], p['zmax'])]
        rxmin, rxmax = min(q[0] for q in c), max(q[0] for q in c)
        rzmin, rzmax = min(q[1] for q in c), max(q[1] for q in c)
        px, pz = x * 20 - rxmin, z * 20 - rzmin
        py = -h * 8 - p['ymax']
        w, d = round((rxmax - rxmin) / 20), round((rzmax - rzmin) / 20)
        studs = []
        for sx, sz in p['studs']:
            ax, az = rot_xz(rot, sx, sz)
            studs.append((int((ax + px) // 20), int((az + pz) // 20)))
        self.items.append(dict(part=part, color=color, x=x, z=z, h=h, w=w, d=d, hh=round(p['ymax'] / 8), rot=rot % 4,
                               pos=(px, py, pz), studs=studs, step=self.step))

    # --- Hilfen ---------------------------------------------------------
    def along_x(self, part, color, x, z, h):
        self.add(part, color, x, z, h, 0)

    def along_z(self, part, color, x, z, h):
        self.add(part, color, x, z, h, 1)

    def slope(self, part, color, x, z, h, low):
        self.add(part, color, x, z, h, LOW[low])

    def row(self, color, x, z, h, lengths, axis, special=None):
        """Reihe aus 1 Noppe breiten Steinen. special: {index: (teil, farbe)}"""
        pos = 0
        for i, n in enumerate(lengths):
            part, col = BRICK1[n], color
            if special and i in special:
                part, col = special[i]
            if axis == 'x':
                self.along_x(part, col, x + pos, z, h)
            else:
                self.along_z(part, col, x, z + pos, h)
            pos += n


def split(n, avoid, sizes=(8, 6, 4, 3, 2, 1)):
    """Zerlegt die Laenge n in Steinlaengen; Fugen sollen nicht ueber den Fugen der Lage darunter liegen."""
    best = {0: (0, 0, [])}
    for pos in range(1, n + 1):
        cand = None
        for s in sizes:
            if s <= pos and (pos - s) in best:
                pen, cnt, seq = best[pos - s]
                joint = pos - s
                pen2 = pen + (3 if (joint in avoid and joint != 0) else 0) + (1 if s == 1 else 0)
                c = (pen2, cnt + 1, seq + [s])
                if cand is None or c[:2] < cand[:2]:
                    cand = c
        if cand:
            best[pos] = cand
    return best[n][2]


def joints(start, lengths):
    out, p = set(), start
    for n in lengths[:-1]:
        p += n
        out.add(p)
    return out


def build():
    m = Model()

    BX, BZ, B = 5, 2, 6                     # Rumpf: erste Noppe in x und z, Unterkante der Waende in Platten

    # ---------------- Boden ----------------
    m.step = 'Boden'
    for x in (BX, BX + 4, BX + 8):
        m.along_z('3029', DGREY, x, BZ, 4)
    m.along_z('2445', DGREY, BX + 12, BZ, 4)
    for i, z in enumerate(range(BZ, BZ + 12, 2)):
        if i % 2 == 0:
            m.along_x('3034', DGREY, BX, z, 5)
            m.along_x('3795', DGREY, BX + 8, z, 5)
        else:
            m.along_x('3795', DGREY, BX, z, 5)
            m.along_x('3034', DGREY, BX + 6, z, 5)

    # ---------------- Rumpfwaende ----------------
    OPEN = (BX + 3, BX + 10)                # Lautsprecheroeffnung in der Vorderwand
    XL, XR = BX, BX + 13                    # linke und rechte Seitenwand
    prev = defaultdict(set)
    for i in range(10):
        m.step = 'Rumpf Lage %d' % (i + 1)
        h = B + 3 * i
        zfull = i % 2 == 0                                   # Seitenwaende nehmen die Ecken mit
        za, zb = (BZ, BZ + 11) if zfull else (BZ + 1, BZ + 10)
        xa, xb = (BX + 1, BX + 12) if zfull else (BX, BX + 13)
        # Rueckwand
        seq = split(xb - xa + 1, {j - xa for j in prev['back']})
        m.row(YELLOW, xa, BZ + 11, h, seq, 'x')
        prev['back'] = joints(xa, seq)
        # Seitenwaende
        for name, x in (('left', XL), ('right', XR)):
            if i == 0:                                        # Technic-Stein traegt die beiden unteren Kettenachsen
                m.along_z('3895', DGREY, x, za, h)
                prev[name] = set()
            elif i == 3:                                      # Technic-Stein traegt die obere Kettenachse
                m.row(YELLOW, x, za, h, [3, 4, 3], 'z', special={1: ('3701', DGREY)})
                prev[name] = joints(za, [3, 4, 3])
            elif i == 6:                                      # zwei Steine ragen nach aussen und tragen den Arm
                m.row(YELLOW, x, za, h, [3], 'z')
                ax = x - 2 if name == 'left' else x
                m.along_x('3002', YELLOW, ax, BZ + 3, h)
                m.along_x('3002', YELLOW, ax, BZ + 5, h)
                m.row(YELLOW, x, BZ + 7, h, [3, 2], 'z')
                prev[name] = {BZ + 3, BZ + 5, BZ + 7, BZ + 10}
            else:
                seq = split(zb - za + 1, {j - za for j in prev[name]})
                m.row(YELLOW, x, za, h, seq, 'z')
                prev[name] = joints(za, seq)
        # Vorderwand
        n = xb - xa + 1
        if 1 <= i <= 6:
            m.row(YELLOW, xa, BZ, h, split(OPEN[0] - xa, set()), 'x')
            m.row(YELLOW, OPEN[1] + 1, BZ, h, split(xb - OPEN[1], set()), 'x')
            for bx in (BX + 5, BX + 8):                       # Gitterstaebe
                m.add('3062b', DGREY, bx, BZ, h)
            prev['front'] = set()
        elif i == 7:                                          # Sturz ueber der Oeffnung
            seq = [2, 10, 2] if n == 14 else [1, 10, 1]
            m.row(YELLOW, xa, BZ, h, seq, 'x')
            prev['front'] = joints(xa, seq)
        elif i == 8:                                          # Brustfeld
            seq = [4, 6, 4] if n == 14 else [3, 6, 3]
            m.row(YELLOW, xa, BZ, h, seq, 'x', special={1: ('3009', BLACK)})
            prev['front'] = joints(xa, seq)
        else:
            seq = split(n, {j - xa for j in prev['front']})
            m.row(YELLOW, xa, BZ, h, seq, 'x')
            prev['front'] = joints(xa, seq)

    # ---------------- Ketten: Achsen, Kettenraeder, Kettenglieder ----------------
    m.step = 'Ketten'
    y_low, y_top = -(B * 8 + 14), -((B + 9) * 8 + 14)        # Lochmitte der Technic-Steine
    for side, (ax_x, sp_x, bush_x) in (('L', (60, 50, 10)), ('R', (420, 430, 470))):
        for z, y, big in (((BZ + 1) * 20, y_low, True), ((BZ + 11) * 20, y_low, True), ((BZ + 6) * 20, y_top, False)):
            m.raw('3706', BLACK, (ax_x, y, z), 0)
            m.raw('3713', LGREY, (bush_x, y, z), 1)
            m.raw('57519' if big else '57520', BLACK, (sp_x, y, z), 1, ext=True)
    # Kettenglieder: als Stapel neben dem Modell, 25 je Seite
    for k in range(2 * LINKS_PER_SIDE):
        m.raw('57518', DGREY, (-160 - 120 * (k % 5), 0, 60 * (k // 5)), 0, ext=True)

    m.ox, m.oh = 1, 1                       # alles Folgende wurde fuer den Rumpf bei x=4 und h=5 geschrieben
    # ---------------- Dach ----------------
    m.step = 'Dach'
    for x, z in ((4, 2), (4, 8), (12, 2), (12, 8)):
        m.add('3958', YELLOW, x, z, 35)
    m.along_z('3795', YELLOW, 10, 2, 35)
    m.along_x('3023', YELLOW, 10, 13, 35)
    m.along_x('3034', DGREY, 7, 4, 36)
    m.along_x('3460', DGREY, 7, 13, 36)

    # ---------------- Hals ----------------
    m.step = 'Hals'
    m.add('87081', DGREY, 9, 8, 36)
    for h in (39, 42, 45):
        m.add('3941', LGREY, 10, 9, h)

    # ---------------- Servoblock am Halsende ----------------
    m.step = 'Servoblock'
    m.along_x('3032', DGREY, 8, 7, 48)
    m.along_x('3666', DGREY, 8, 11, 48)
    m.row(DGREY, 8, 7, 49, [6], 'x')
    m.row(DGREY, 8, 11, 49, [6], 'x')
    m.row(DGREY, 8, 8, 49, [3], 'z')
    m.row(DGREY, 13, 8, 49, [3], 'z')
    for x in (8, 13):
        m.row(DGREY, x, 7, 52, [2, 2, 1], 'z', special={1: ('3700', LGREY)})
    m.row(DGREY, 9, 7, 52, [4], 'x')
    m.row(DGREY, 9, 11, 52, [4], 'x')
    m.along_x('3666', DGREY, 8, 7, 55)
    m.along_x('3032', DGREY, 8, 8, 55)

    # ---------------- Kopf ----------------
    m.step = 'Kopf Boden'
    m.along_x('3036', LGREY, 3, 5, 56)
    m.along_x('3036', LGREY, 11, 5, 56)
    m.along_z('3795', LGREY, 10, 5, 57)
    for j in range(5):
        m.step = 'Augen Lage %d' % (j + 1)
        h = 57 + 3 * j
        for outer, inner, bx0 in ((3, 9, 3), (18, 12, 12)):       # linke und rechte Augenroehre
            if j % 2 == 0:
                for x in (outer, inner):
                    m.row(LGREY, x, 5, h, [6], 'z')
                m.row(LGREY, bx0 + 1, 10, h, [2, 3] if j % 4 == 0 else [3, 2], 'x')
            else:
                m.row(LGREY, bx0, 10, h, [4, 3] if bx0 == 3 else [3, 4], 'x')
                for x in (outer, inner):
                    m.row(LGREY, x, 5, h, [3, 2], 'z')
    m.step = 'Kopf Deckel'
    m.add('3958', LGREY, 4, 5, 72)
    m.along_z('3666', LGREY, 3, 5, 72)
    m.add('3958', LGREY, 12, 5, 72)
    m.along_z('3666', LGREY, 18, 5, 72)
    m.step = 'Brauen'
    for z in (5, 7, 9):
        m.slope('3298', LGREY, 3, z, 73, '-x')
        m.slope('3298', LGREY, 16, z, 73, '+x')
    for z in (5, 7):
        m.along_x('3001', LGREY, 6, z, 73)
        m.along_x('3001', LGREY, 12, z, 73)
    m.add('3003', LGREY, 6, 9, 73)
    m.add('3003', LGREY, 14, 9, 73)
    m.along_x('2456', DGREY, 8, 9, 73)

    # ---------------- Arme ----------------
    m.step = 'Arme'
    m.ox, m.oh = 0, 0
    for ax in (BX - 2, BX + 14):
        m.along_z('2456', YELLOW, ax, BZ + 1, B + 21)
        m.along_z('3001', DGREY, ax, BZ - 3, B + 21)
        m.along_z('3832', YELLOW, ax, BZ - 3, B + 24)
    return m


def check(m):
    """Prueft: keine Ueberschneidungen, und alles haengt ueber Noppen zusammen."""
    occ, problems = {}, []
    for idx, it in enumerate(m.items):
        if it.get('raw'):
            continue
        for x in range(it['x'], it['x'] + it['w']):
            for z in range(it['z'], it['z'] + it['d']):
                for h in range(it['h'], it['h'] + it['hh']):
                    if (x, z, h) in occ:
                        o = m.items[occ[(x, z, h)]]
                        problems.append('Ueberschneidung %s/%s bei Noppe (%d,%d) Hoehe %d' % (o['part'], it['part'], x, z, h))
                    occ[(x, z, h)] = idx
    parent = list(range(len(m.items)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for idx, it in enumerate(m.items):
        if it.get('raw') or it['part'] in TILES:
            continue
        top = it['h'] + it['hh']
        for sx, sz in it['studs']:
            j = occ.get((sx, sz, top))
            if j is not None and m.items[j]['h'] == top:
                parent[find(idx)] = find(j)
    grid = [i for i, it in enumerate(m.items) if not it.get('raw')]
    groups = Counter(find(i) for i in grid)
    if len(groups) > 1:
        main = groups.most_common(1)[0][0]
        for i in grid:
            it = m.items[i]
            if find(i) != main:
                problems.append('Lose: %s bei (%d,%d) Hoehe %d [%s]' % (it['part'], it['x'], it['z'], it['h'], it['step']))
    return problems


def line(it, prefix=''):
    px, py, pz = it['pos']
    return '1 %d %g %g %g %s %s%s.dat' % (it['color'], px, py, pz, ' '.join(str(v) for v in MATS[it['rot']]), prefix, it['part'])


def write_ldr(m, path):
    out = ['0 Kettenroboter mit Fernglas-Kopf', '0 Name: roboter.ldr', '0 !LDRAW_ORG Unofficial_Model', '']
    step = None
    for it in m.items:
        if it['step'] != step:
            if step is not None:
                out.append('0 STEP')
            step = it['step']
            out.append('0 // ' + step)
        out.append(line(it))
    out.append('0 STEP')
    open(path, 'w').write('\n'.join(out) + '\n')


def part_name(part):
    return EXTERNAL.get(part) or PARTS[part]['name']


def write_parts_list(m, path):
    cnt = Counter((it['part'], it['color']) for it in m.items)
    rows = sorted(cnt.items(), key=lambda kv: (kv[0][1], part_name(kv[0][0])))
    out = ['# Teileliste', '', 'Erzeugt von `build_model.py`. Teilenummern sind LDraw- bzw. BrickLink-Designnummern.', '',
           '| Anzahl | Teil | Nummer | Farbe |', '|---:|---|---|---|']
    for (part, color), n in rows:
        out.append('| %d | %s | %s | %s |' % (n, part_name(part), part, COLOR_NAMES[color]))
    out += ['', 'Summe: %d Teile, %d verschiedene Posten.' % (len(m.items), len(cnt)), '',
            'Kettenglieder: %d je Seite sind gerechnet, nicht gemessen. Bestell 60, dann hast du Reserve.' % LINKS_PER_SIDE]
    open(path, 'w').write('\n'.join(out) + '\n')


if __name__ == '__main__':
    model = build()
    probs = check(model)
    for p in probs[:40]:
        print('PROBLEM', p)
    write_ldr(model, os.path.join(HERE, 'roboter.ldr'))
    write_parts_list(model, os.path.join(HERE, 'TEILELISTE.md'))
    grid = [it for it in model.items if not it.get('raw')]
    xs = [it['x'] for it in grid] + [it['x'] + it['w'] for it in grid]
    zs = [it['z'] for it in grid] + [it['z'] + it['d'] for it in grid]
    hs = [it['h'] + it['hh'] for it in grid]
    print('Teile: %d  Probleme: %d' % (len(model.items), len(probs)))
    print('Breite %d Noppen = %d mm, Tiefe %d Noppen = %d mm, Hoehe %d Platten = %.0f mm' % (
        max(xs) - min(xs), (max(xs) - min(xs)) * 8, max(zs) - min(zs), (max(zs) - min(zs)) * 8, max(hs), max(hs) * 3.2))

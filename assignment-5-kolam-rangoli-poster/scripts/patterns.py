"""
Kolam and rangoli patterns as SVG, all generated in code.

The continuous-line (sikku) kolam uses the "mirror curve" construction:
dots sit at the centres of an n x n grid of cells, and a line travels
diagonally between them, either crossing each cell edge or bouncing off a
"mirror" placed on it. The outer edges are always mirrors. Choosing which
inner edges get mirrors decides the pattern; we search (with a fixed seed,
so the output never changes) for a 4-fold symmetric choice that yields ONE
closed line, which is exactly the rule a kolam artist follows: never lift
the hand, never leave a loose end.
"""

import math
import random

INK = "#fffaf0"          # rice-flour white
FLOOR = "#3a2620"        # wet earth at the doorstep
MARIGOLD = "#f2a516"
VERMILION = "#d83a1f"
MAGENTA = "#c2187a"
TURQUOISE = "#139a9a"
LEAF = "#3f8f3a"
INDIGO = "#2e3a8c"
CREAM = "#fff4dc"


def svg(inner, size=200, bg=None, label=""):
    rect = f'<rect width="{size}" height="{size}" fill="{bg}"/>' if bg else ""
    return (f'<svg viewBox="0 0 {size} {size}" role="img" aria-label="{label}" '
            f'xmlns="http://www.w3.org/2000/svg">{rect}{inner}</svg>')


# ---------------------------------------------------------------------------
# Sikku kolam: mirror curves
# ---------------------------------------------------------------------------
QUADS = ("NE", "NW", "SW", "SE")
# the two cell-edge midpoints each quadrant segment joins
Q_ENDS = {"NE": ("N", "E"), "NW": ("N", "W"), "SW": ("S", "W"), "SE": ("S", "E")}


def _mid(i, j, side):
    """Midpoint of a cell side; cell (i,j) spans x in [i,i+1], y in [j,j+1] (y up)."""
    return {"N": (i + .5, j + 1), "S": (i + .5, j), "E": (i + 1, j + .5), "W": (i, j + .5)}[side]


def mirror_loops(n, vmirror, hmirror):
    """
    Trace the mirror curve on an n x n grid.

    vmirror[(i,j)] is True if the vertical edge between cell (i,j) and (i+1,j)
    holds a mirror; hmirror[(i,j)] likewise for the edge between (i,j) and (i,j+1).
    Returns a list of loops; each loop is a list of points (edge midpoints) in order.
    """
    adj = {}

    def link(a, b, at):
        adj.setdefault(a, []).append((b, at))
        adj.setdefault(b, []).append((a, at))

    for i in range(n):
        for j in range(n):
            # east side
            p = _mid(i, j, "E")
            if i == n - 1 or vmirror[(i, j)]:
                link((i, j, "NE"), (i, j, "SE"), p)
                if i < n - 1:
                    link((i + 1, j, "NW"), (i + 1, j, "SW"), p)
            else:
                link((i, j, "NE"), (i + 1, j, "SW"), p)
                link((i, j, "SE"), (i + 1, j, "NW"), p)
            # north side
            p = _mid(i, j, "N")
            if j == n - 1 or hmirror[(i, j)]:
                link((i, j, "NE"), (i, j, "NW"), p)
                if j < n - 1:
                    link((i, j + 1, "SE"), (i, j + 1, "SW"), p)
            else:
                link((i, j, "NE"), (i, j + 1, "SW"), p)
                link((i, j, "NW"), (i, j + 1, "SE"), p)
            if i == 0:
                link((i, j, "NW"), (i, j, "SW"), _mid(i, j, "W"))
            if j == 0:
                link((i, j, "SE"), (i, j, "SW"), _mid(i, j, "S"))

    seen, loops = set(), []
    for start in adj:
        if start in seen:
            continue
        loop, prev, cur, via = [], None, start, None
        # walk: each segment has exactly two neighbours
        while True:
            seen.add(cur)
            nxt = [(b, at) for b, at in adj[cur] if (b, at) != prev]
            b, at = nxt[0] if prev is not None else adj[cur][0]
            loop.append(at)
            prev, cur = (cur, at), b
            if cur == start:
                break
        loops.append(loop)
    return loops


def _edges(n):
    v = [(i, j) for i in range(n - 1) for j in range(n)]
    h = [(i, j) for i in range(n) for j in range(n - 1)]
    return v, h


def _rot(n, kind, i, j):
    """Rotate an inner edge 90 degrees about the grid centre."""
    # midpoint of the edge in grid coordinates, rotated (x,y) -> (n-y, x)
    x, y = (i + 1, j + .5) if kind == "v" else (i + .5, j + 1)
    rx, ry = n - y, x
    if float(rx).is_integer():           # lies on a vertical line -> vertical edge
        return "v", int(rx) - 1, int(ry - .5)
    return "h", int(rx - .5), int(ry) - 1


def _flip(n, kind, i, j):
    """Reflect an inner edge in the grid's vertical centre line."""
    return ("v", n - i - 2, j) if kind == "v" else ("h", n - i - 1, j)


def symmetric_sikku(n, seed, density=0.5, tries=6000):
    """
    Find a mirror set on an n x n grid that gives a single closed loop.

    Mirrors are switched on in whole symmetry orbits, so the kolam has the
    full symmetry of the square (4 rotations + reflections) when one exists,
    falling back to 4-fold rotation only. Among the single-loop results we
    keep the one with the most mirrors: more mirrors means more of the
    characteristic loops that curl around individual dots.
    """
    v, h = _edges(n)
    every = [("v",) + e for e in v] + [("h",) + e for e in h]

    def orbits(with_flip):
        out, done = [], set()
        for e in every:
            if e in done:
                continue
            orb, frontier = {e}, [e]
            while frontier:
                cur = frontier.pop()
                moves = [_rot(n, *cur)] + ([_flip(n, *cur)] if with_flip else [])
                for m in moves:
                    if m not in orb:
                        orb.add(m)
                        frontier.append(m)
            done |= orb
            out.append(sorted(orb))
        return out

    for with_flip in (True, False):
        orbs = orbits(with_flip)
        rnd = random.Random(seed)
        best = None
        for _ in range(tries):
            on = {e for orb in orbs if rnd.random() < density for e in orb}
            vm = {e: ("v",) + e in on for e in v}
            hm = {e: ("h",) + e in on for e in h}
            loops = mirror_loops(n, vm, hm)
            if len(loops) == 1 and (best is None or len(on) > best[0]):
                best = (len(on), loops[0], vm, hm)
        if best:
            return best[1], best[2], best[3]
    raise RuntimeError(f"no single-loop kolam found for n={n}, seed={seed}")


def smooth_closed(points, scale, ox, oy, size_px):
    """Closed path through edge midpoints, rounding every corner (y flipped for SVG)."""
    P = [(ox + x * scale, oy + size_px - y * scale) for x, y in points]
    mids = [((P[k][0] + P[(k + 1) % len(P)][0]) / 2, (P[k][1] + P[(k + 1) % len(P)][1]) / 2)
            for k in range(len(P))]
    d = f"M {mids[-1][0]:.2f},{mids[-1][1]:.2f} "
    for k in range(len(P)):
        d += f"Q {P[k][0]:.2f},{P[k][1]:.2f} {mids[k][0]:.2f},{mids[k][1]:.2f} "
    return d + "Z"


def sikku_kolam(n=7, seed=2, size=200, pad=16, colour=INK, bg=FLOOR, stroke=2.6):
    loop, _, _ = symmetric_sikku(n, seed)
    cell = (size - 2 * pad) / n
    d = smooth_closed(loop, cell, pad, pad, size - 2 * pad)
    dots = "".join(f'<circle cx="{pad + (i + .5) * cell:.2f}" cy="{pad + (j + .5) * cell:.2f}" '
                   f'r="{max(1.6, cell * .07):.2f}" fill="{colour}"/>'
                   for i in range(n) for j in range(n))
    line = (f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{stroke}" '
            f'stroke-linejoin="round" stroke-linecap="round"/>')
    return svg(dots + line, size, bg, f"A continuous-line sikku kolam drawn around a {n} by {n} grid of dots")


# ---------------------------------------------------------------------------
# Pulli kolam: dots joined by straight lines
# ---------------------------------------------------------------------------

def pulli_kolam(size=200, colour=INK, bg=FLOOR):
    """Dots in a diamond, joined by straight lines into a lattice with petal tips."""
    c, step = size / 2, size / 12
    dots = [(c + x * step, c + y * step) for x in range(-4, 5) for y in range(-4, 5)
            if abs(x) + abs(y) <= 4]
    line = f'fill="none" stroke="{colour}" stroke-width="2" stroke-linejoin="round"'
    out = []
    for r in (2, 4):                                   # two nested diamonds
        pts = [(c, c - r * step), (c + r * step, c), (c, c + r * step), (c - r * step, c)]
        out.append('<path d="M ' + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f' Z" {line}/>')
    for y in range(-3, 4):                             # rows and columns joining the dots
        w = 4 - abs(y)
        out.append(f'<path d="M {c - w * step:.1f},{c + y * step:.1f} L {c + w * step:.1f},{c + y * step:.1f} '
                   f'M {c + y * step:.1f},{c - w * step:.1f} L {c + y * step:.1f},{c + w * step:.1f}" '
                   f'fill="none" stroke="{colour}" stroke-width="1.3" opacity=".75"/>')
    for a in range(4):                                 # petal loops at the four tips
        ang = math.pi / 2 * a
        ux, uy = math.cos(ang), math.sin(ang)
        tx, ty = c + 4 * step * ux, c + 4 * step * uy
        px, py = -uy, ux
        out.append(f'<path d="M {tx:.1f},{ty:.1f} C {tx + ux * 22 + px * 16:.1f},{ty + uy * 22 + py * 16:.1f} '
                   f'{tx + ux * 22 - px * 16:.1f},{ty + uy * 22 - py * 16:.1f} {tx:.1f},{ty:.1f} Z" {line}/>')
    out += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{colour}"/>' for x, y in dots]
    return svg("".join(out), size, bg, "A pulli kolam: rice-flour dots in a diamond joined by straight lines, with petal loops at the tips")


# ---------------------------------------------------------------------------
# Rangoli
# ---------------------------------------------------------------------------

def _petal(cx, cy, r0, r1, w, ang, fill, stroke="#5a2a10", sw=1):
    """A pointed petal from radius r0 to r1 along angle ang (degrees)."""
    a = math.radians(ang)
    ux, uy, px, py = math.cos(a), math.sin(a), -math.sin(a), math.cos(a)
    b = (cx + ux * r0, cy + uy * r0)
    t = (cx + ux * r1, cy + uy * r1)
    m = (r0 + r1) / 2
    c1 = (cx + ux * m + px * w, cy + uy * m + py * w)
    c2 = (cx + ux * m - px * w, cy + uy * m - py * w)
    return (f'<path d="M {b[0]:.1f},{b[1]:.1f} Q {c1[0]:.1f},{c1[1]:.1f} {t[0]:.1f},{t[1]:.1f} '
            f'Q {c2[0]:.1f},{c2[1]:.1f} {b[0]:.1f},{b[1]:.1f} Z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def ring(cx, cy, r, fill, stroke="#5a2a10", sw=1):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def geometric_rangoli(size=200, bg=CREAM):
    c = size / 2
    o = [ring(c, c, 92, INDIGO), ring(c, c, 84, MARIGOLD)]
    for k in range(16):                                  # outer triangles
        a = math.radians(22.5 * k)
        a1, a2 = a - math.radians(11.25), a + math.radians(11.25)
        pts = [(c + 84 * math.cos(a1), c + 84 * math.sin(a1)), (c + 98 * math.cos(a), c + 98 * math.sin(a)),
               (c + 84 * math.cos(a2), c + 84 * math.sin(a2))]
        o.append('<path d="M ' + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) +
                 f' Z" fill="{VERMILION if k % 2 else MAGENTA}" stroke="#5a2a10" stroke-width="1"/>')
    o.append(ring(c, c, 72, TURQUOISE))
    o += [_petal(c, c, 28, 72, 14, 45 * k, MAGENTA) for k in range(8)]
    o += [_petal(c, c, 28, 60, 9, 45 * k + 22.5, MARIGOLD) for k in range(8)]
    o.append(ring(c, c, 30, VERMILION))
    o += [_petal(c, c, 6, 28, 6, 45 * k, CREAM) for k in range(8)]
    o.append(ring(c, c, 7, MARIGOLD))
    o += [f'<circle cx="{c + 78 * math.cos(math.radians(22.5 * k)):.1f}" '
          f'cy="{c + 78 * math.sin(math.radians(22.5 * k)):.1f}" r="2.6" fill="{CREAM}"/>' for k in range(16)]
    return svg("".join(o), size, bg, "A geometric rangoli with 16-fold symmetry in rings of petals and triangles")


def floral_rangoli(size=200, bg=CREAM):
    c = size / 2
    o = []
    o += [_petal(c, c, 40, 94, 18, 30 * k + 15, LEAF) for k in range(12)]       # leaves
    o += [_petal(c, c, 14, 80, 22, 45 * k, "#f4a0b8") for k in range(8)]        # outer petals
    o += [_petal(c, c, 14, 64, 15, 45 * k + 22.5, MAGENTA) for k in range(8)]
    o += [_petal(c, c, 8, 42, 10, 45 * k, "#ffd2df") for k in range(8)]
    o.append(ring(c, c, 15, MARIGOLD))
    o += [f'<circle cx="{c + 9 * math.cos(math.radians(60 * k)):.1f}" '
          f'cy="{c + 9 * math.sin(math.radians(60 * k)):.1f}" r="2.4" fill="{VERMILION}"/>' for k in range(6)]
    return svg("".join(o), size, bg, "A floral rangoli: a lotus of layered pink and magenta petals with green leaves")


def pongal_kolam(size=200, bg=FLOOR):
    """Festival kolam for Pongal: the overflowing pot, sugarcane and the sun."""
    c = size / 2
    o = [f'<circle cx="{c}" cy="{c}" r="90" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round"/>']
    for k in range(12):                                   # sun rays
        a = math.radians(30 * k - 90)
        o.append(f'<path d="M {c + 26 * math.cos(a):.1f},{52 + 26 * math.sin(a):.1f} L {c + 36 * math.cos(a):.1f},{52 + 36 * math.sin(a):.1f}" '
                 f'stroke="{MARIGOLD}" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<circle cx="{c}" cy="52" r="20" fill="{MARIGOLD}" stroke="{INK}" stroke-width="2"/>')
    for side in (-1, 1):                                  # sugarcane
        x = c + side * 52
        o.append(f'<path d="M {x},168 L {x - side * 8},62" stroke="{LEAF}" stroke-width="7" stroke-linecap="round"/>')
        o += [f'<path d="M {x - side * 8 * t:.1f},{168 - 106 * t:.1f} l 6,0" stroke="{INK}" stroke-width="1.5"/>'
              for t in (.2, .4, .6, .8)]
        o.append(f'<path d="M {x - side * 8},62 q {side * -18},-16 {side * -26},-6 M {x - side * 8},62 q {side * 6},-22 {side * 20},-24" '
                 f'stroke="{LEAF}" stroke-width="3" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M {c - 30},112 C {c - 46},150 {c - 30},172 {c},172 C {c + 30},172 {c + 46},150 {c + 30},112 Z" '
             f'fill="{VERMILION}" stroke="{INK}" stroke-width="2.4"/>')                    # pot
    o.append(f'<path d="M {c - 34},112 L {c + 34},112" stroke="{MARIGOLD}" stroke-width="5" stroke-linecap="round"/>')
    o.append(f'<path d="M {c - 30},112 C {c - 34},92 {c - 14},90 {c - 10},100 C {c - 6},86 {c + 10},86 {c + 12},98 '
             f'C {c + 20},88 {c + 36},96 {c + 30},112 Z" fill="{INK}"/>')                   # boiling over
    o.append(f'<path d="M {c - 26},138 q 26,14 52,0" stroke="{MARIGOLD}" stroke-width="2.4" fill="none"/>')
    return svg("".join(o), size, bg, "A Pongal festival kolam: an overflowing pot of pongal between sugarcane under the sun")


def diwali_rangoli(size=200, bg=CREAM):
    c = size / 2
    o = [ring(c, c, 94, VERMILION), ring(c, c, 86, MARIGOLD)]
    o += [_petal(c, c, 60, 94, 10, 30 * k, MAGENTA) for k in range(12)]
    o.append(ring(c, c, 62, INDIGO))
    o += [f'<circle cx="{c + 54 * math.cos(math.radians(30 * k)):.1f}" cy="{c + 54 * math.sin(math.radians(30 * k)):.1f}" '
          f'r="3" fill="{MARIGOLD}"/>' for k in range(12)]
    # the diya
    o.append(f'<path d="M {c - 34},{c + 6} Q {c},{c + 44} {c + 34},{c + 6} Z" fill="#b5651d" stroke="#5a2a10" stroke-width="2"/>')
    o.append(f'<path d="M {c - 34},{c + 6} L {c + 34},{c + 6}" stroke="#5a2a10" stroke-width="2"/>')
    o.append(f'<path d="M {c},{c - 40} C {c + 12},{c - 20} {c + 10},{c - 2} {c},{c + 2} C {c - 10},{c - 2} {c - 12},{c - 20} {c},{c - 40} Z" '
             f'fill="{MARIGOLD}" stroke="{VERMILION}" stroke-width="2"/>')
    o.append(f'<path d="M {c},{c - 22} C {c + 5},{c - 12} {c + 4},{c - 3} {c},{c} C {c - 4},{c - 3} {c - 5},{c - 12} {c},{c - 22} Z" fill="#fff6c8"/>')
    return svg("".join(o), size, bg, "A Diwali rangoli: a lit diya inside a ring of magenta petals")


def kolam_border(length, height=26, colour=INK, step=26):
    """A running two-strand kolam braid around a row of dots (for headers/borders)."""
    n = int(length // step)
    y0 = height / 2
    a = height * .36
    def wave(phase):
        d = f"M 0,{y0}"
        for k in range(n):
            x0, x1 = k * step, (k + 1) * step
            s = 1 if (k + phase) % 2 == 0 else -1
            d += f" C {x0 + step * .5},{y0 - s * a * 1.9} {x1 - step * .5},{y0 - s * a * 1.9} {x1},{y0}"
        return d
    dots = "".join(f'<circle cx="{(k + .5) * step:.1f}" cy="{y0}" r="2" fill="{colour}"/>' for k in range(n))
    return (f'<svg viewBox="0 0 {n * step} {height}" preserveAspectRatio="none" aria-hidden="true" class="braid">'
            f'<path d="{wave(0)}" fill="none" stroke="{colour}" stroke-width="1.8"/>'
            f'<path d="{wave(1)}" fill="none" stroke="{colour}" stroke-width="1.8"/>{dots}</svg>')


if __name__ == "__main__":
    for n, seed in ((5, 1), (7, 2), (9, 4)):
        loop, vm, hm = symmetric_sikku(n, seed)
        print(f"n={n} seed={seed}: single loop through {len(loop)} edge midpoints; "
              f"{sum(vm.values()) + sum(hm.values())} mirrors")

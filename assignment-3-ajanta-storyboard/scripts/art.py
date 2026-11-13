"""
Drawing helpers for the Chhaddanta storyboard.

Every illustration is plain SVG built from these functions, so all eight
panels share one cast of characters and one palette. Nothing here is traced
from a photograph: the shapes are drawn by hand in code, in the flat colours
and dark outlines of the Ajanta murals.

Coordinates: each panel is 480 x 320. Characters are drawn around a local
origin at their feet (ground contact), facing right; pass flip=True to face
left.
"""

# --- Ajanta mineral palette -------------------------------------------------
OUT = "#3b2418"        # outline brown
PLASTER = "#efe4cc"    # lime plaster ground
OCHRE = "#c8902e"      # yellow ochre
OCHRE_D = "#9c6a1e"
RED = "#9b3b26"        # red earth
RED_D = "#6e2416"
LAPIS = "#2c4a7a"      # lapis lazuli
LAPIS_D = "#1c3054"
GREEN = "#5f7a4a"      # terre verte
GREEN_D = "#3f5532"
GREEN_L = "#8aa06a"
IVORY = "#f6eedb"
ELE_W = "#ece3cf"      # the white elephant
ELE_SH = "#cfc2a6"     # its shadow side
ELE_G = "#a49a8a"      # grey cow-elephants
ELE_GSH = "#857b6c"
SKIN_L = "#d9a066"
SKIN_M = "#b5733e"
SKIN_D = "#7d4a2a"
ROBE = "#d9a53a"       # the hunter's borrowed yellow robe
GOLD = "#d8b04a"
PINK = "#e7a9a0"

SW = 2.2               # standard outline width


def g(content, x=0, y=0, s=1.0, flip=False, rot=0, extra=""):
    sx = -s if flip else s
    t = f"translate({x:.1f},{y:.1f})"
    if rot:
        t += f" rotate({rot})"
    t += f" scale({sx},{s})"
    return f'<g transform="{t}" {extra}>{content}</g>'


def path(d, fill, stroke=OUT, sw=SW, extra=""):
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="round" {extra}/>')


def limb(d, colour, w=6.0):
    """A limb drawn as a thick stroke with a dark outline under it."""
    return (f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w + 2.6}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


# --- the elephant -----------------------------------------------------------

def _tusk(bx, by, tx, ty, lift, fill):
    """A curved, tapering tusk from base (bx,by) to tip (tx,ty)."""
    cx, cy = (bx + tx) / 2, min(by, ty) - lift
    return path(f"M {bx},{by - 3.5} Q {cx},{cy - 3} {tx},{ty} "
                f"Q {cx},{cy + 4} {bx},{by + 3.5} Z", fill, sw=1.6)


def elephant(x, y, s=1.0, flip=False, body=ELE_W, shade=ELE_SH, tusks=6,
             trunk="down", kneel=False, arrow=False, crown=False, extra=""):
    """The six-tusked king (tusks=6) or a cow elephant (tusks=0).

    `extra` is SVG drawn last in the elephant's own coordinates (e.g. a saw).
    """
    parts = []
    drop = 26 if kneel else 0

    # far legs (darker), drawn behind the body
    if not kneel:
        for lx in (-50, 26):
            parts.append(path(f"M {lx},-46 L {lx},-6 Q {lx},0 {lx + 6},0 "
                              f"L {lx + 16},0 Q {lx + 22},0 {lx + 22},-6 L {lx + 22},-46 Z",
                              shade))

    # far-side tusks peep out behind the head
    if tusks == 6:
        parts.append(f'<g transform="translate(0,{drop})">' +
                     _tusk(96, -62, 140, -86, 10, "#e3d7bb") +
                     _tusk(96, -58, 150, -70, 6, "#e3d7bb") +
                     _tusk(96, -54, 146, -50, 2, "#e3d7bb") + "</g>")

    # tail
    parts.append(f'<g transform="translate(0,{drop})">' +
                 path("M -78,-74 C -92,-62 -92,-40 -88,-24", "none", sw=2.4) +
                 path("M -91,-28 l -4,10 l 5,-3 l 3,6 l 2,-8 Z", OUT, sw=1) + "</g>")

    # body
    parts.append(f'<g transform="translate(0,{drop})">' + path(
        "M -80,-40 C -88,-96 -30,-120 20,-114 C 54,-110 70,-94 72,-70 "
        "L 72,-40 C 40,-28 -48,-28 -80,-40 Z", body) +
        # belly shadow and skin folds, in the mural's soft ochre line
        path("M -70,-44 C -40,-34 30,-34 66,-44", "none", stroke=shade, sw=5) +
        path("M -56,-86 C -50,-70 -52,-56 -58,-46", "none", stroke=shade, sw=1.6) +
        path("M 44,-96 C 50,-82 50,-62 44,-48", "none", stroke=shade, sw=1.6) + "</g>")

    # near legs
    if kneel:
        parts.append(path("M -70,-14 C -74,-4 -40,-2 -30,-8 L -30,-20 L -70,-20 Z", body))
        parts.append(path("M 30,-14 C 26,-2 76,-2 84,-8 C 88,-14 80,-20 70,-20 L 30,-20 Z", body))
    else:
        for lx in (-72, 40):
            parts.append(path(f"M {lx},-50 L {lx},-6 Q {lx},0 {lx + 6},0 "
                              f"L {lx + 18},0 Q {lx + 24},0 {lx + 24},-6 L {lx + 24},-50 Z",
                              body))
            parts.append("".join(
                f'<path d="M {lx + 4 + 7 * i},0 q 3,-5 6,0" fill="none" stroke="{OUT}" '
                f'stroke-width="1.2"/>' for i in range(3)))

    # head, ear, eye
    head = (path("M 52,-62 C 44,-102 66,-126 90,-120 C 98,-128 112,-122 114,-108 "
                 "C 120,-92 116,-72 108,-62 C 100,-52 70,-50 52,-62 Z", body) +
            path("M 66,-100 C 42,-106 34,-74 44,-58 C 52,-46 66,-54 68,-66 Z", shade) +
            path("M 62,-92 C 50,-92 46,-74 52,-64", "none", stroke=PINK, sw=2) +
            f'<ellipse cx="94" cy="-92" rx="3.2" ry="2.2" fill="{OUT}"/>' +
            path("M 89,-97 Q 94,-100 99,-96", "none", sw=1.2))
    if crown:
        head += (path("M 70,-118 Q 90,-130 110,-116", "none", stroke=GOLD, sw=4) +
                 f'<circle cx="90" cy="-125" r="4" fill="{RED}" stroke="{OUT}" stroke-width="1.2"/>')
    parts.append(f'<g transform="translate(0,{drop})">{head}</g>')

    # trunk
    trunks = {
        "down": "M 104,-70 C 120,-58 118,-30 114,-14 C 112,-6 118,-2 122,-8 L 126,-5 "
                "C 122,6 104,4 104,-12 C 104,-30 102,-48 92,-58 Z",
        "up": "M 102,-74 C 122,-84 134,-114 126,-144 C 124,-152 132,-156 136,-148 "
              "C 144,-112 128,-74 108,-58 Z",
        "reach": "M 104,-72 C 130,-78 150,-96 158,-122 C 160,-130 168,-130 168,-122 "
                 "C 160,-90 136,-68 108,-58 Z",
        "offer": "M 104,-72 C 132,-70 160,-62 178,-52 C 186,-48 190,-58 184,-62 L 188,-66 "
                 "C 196,-56 186,-38 174,-42 C 154,-48 128,-56 104,-56 Z",
        "curl":"M 104,-70 C 124,-62 128,-40 116,-30 C 108,-24 104,-34 112,-38 "
                "C 118,-44 110,-54 96,-56 Z",
    }
    parts.append(f'<g transform="translate(0,{drop})">' + path(trunks[trunk], body) +
                 "".join(path(f"M {a},{b} q 5,2 9,0", "none", stroke=shade, sw=1.2)
                         for a, b in ((108, -50), (110, -40), (110, -30))
                         if trunk == "down") + "</g>")

    # near-side tusks over the trunk root
    if tusks == 6:
        parts.append(f'<g transform="translate(0,{drop})">' +
                     _tusk(100, -64, 146, -92, 10, IVORY) +
                     _tusk(100, -60, 158, -74, 6, IVORY) +
                     _tusk(100, -56, 154, -52, 2, IVORY) + "</g>")

    # the poisoned arrow in his flank
    if arrow:
        parts.append(f'<g transform="translate(0,{drop})">' +
                     path("M -10,-62 L -46,-104", "none", stroke=OUT, sw=2.4) +
                     path("M -46,-104 l -9,-3 l 4,8 Z M -46,-104 l -2,-9 l -6,6 Z", RED, sw=1) +
                     path("M -10,-62 c 2,6 -1,12 -3,18 c -1,4 3,4 3,0", "#a3241a",
                          stroke="#a3241a", sw=1.4) + "</g>")

    if extra:
        parts.append(f'<g transform="translate(0,{drop})">{extra}</g>')

    return g("".join(parts), x, y, s, flip)


# --- people -----------------------------------------------------------------

ARMS = {
    # (near arm, far arm), drawn from the shoulders at about (+-10,-84)
    "down":   ("M 10,-84 C 15,-70 16,-58 14,-48", "M -10,-84 C -15,-70 -16,-58 -14,-48"),
    "anjali": ("M 10,-84 C 16,-74 10,-68 3,-74", "M -10,-84 C -16,-74 -8,-68 1,-74"),
    "offer":  ("M 10,-84 C 20,-76 28,-72 36,-74", "M -10,-84 C -4,-72 16,-70 32,-72"),
    "point":  ("M 10,-84 C 22,-88 32,-94 42,-100", "M -10,-84 C -15,-70 -16,-58 -14,-48"),
    "grief":  ("M 10,-84 C 28,-88 28,-104 12,-106", "M -10,-84 C 0,-74 18,-70 32,-70"),
    "bow":    ("M 10,-84 C 24,-92 34,-100 42,-108", "M -10,-84 C -6,-94 0,-100 6,-104"),
    "saw":    ("M 10,-84 C 22,-80 32,-84 40,-92", "M -10,-84 C -2,-78 14,-80 28,-88"),
    "hold":   ("M 10,-84 C 18,-72 26,-66 34,-64", "M -10,-84 C -6,-70 10,-64 24,-62"),
}


def person(x, y, s=1.0, flip=False, skin=SKIN_M, cloth=RED, cloth2=OCHRE,
           arms="down", kneel=False, crown=False, female=False, robe=False,
           topknot=False, scar=False, extra_hand=""):
    p = []
    near, far = ARMS[arms]
    base = -30 if kneel else -52

    p.append(limb(far, skin, 5.5))

    # lower garment / legs
    if kneel:
        p.append(path("M -14,-30 C -16,-14 -6,-4 26,-4 C 34,-4 34,-14 26,-16 "
                      "L 10,-18 L 14,-30 Z", cloth))
        p.append(path("M -18,-4 C -26,-4 -26,-12 -16,-14", skin, sw=1.6))
    else:
        p.append(path("M -13,-52 L 13,-52 C 16,-34 18,-18 20,-4 L -20,-4 "
                      "C -18,-18 -16,-34 -13,-52 Z", cloth))
        p.append(path("M -2,-50 L -4,-6 M 6,-48 L 9,-6", "none", stroke=cloth2, sw=1.4))
        p.append(f'<ellipse cx="-9" cy="-2" rx="7" ry="3" fill="{skin}" stroke="{OUT}" stroke-width="1.4"/>'
                 f'<ellipse cx="9" cy="-2" rx="7" ry="3" fill="{skin}" stroke="{OUT}" stroke-width="1.4"/>')

    # torso, offset down when kneeling
    dy = base + 52
    torso = path("M -12,-52 C -14,-68 -14,-78 -11,-87 L 11,-87 C 14,-78 14,-68 12,-52 Z",
                 skin)
    torso += path("M -13,-54 L 13,-54 L 13,-50 L -13,-50 Z", cloth2, sw=1.2)  # waist sash
    if female:
        torso += path("M -11,-80 C -6,-72 6,-72 11,-80 L 11,-74 C 6,-68 -6,-68 -11,-74 Z",
                      cloth2, sw=1.2)
    if robe:   # yellow robe over the left shoulder, as monks wear it
        torso += path("M -12,-88 L 4,-88 L 13,-60 L 12,-52 L -12,-52 Z", ROBE)
        torso += path("M -6,-84 L 6,-58 M -2,-86 L 9,-62", "none", stroke=OCHRE_D, sw=1.2)
    neck = path("M -4,-92 L 4,-92 L 4,-86 L -4,-86 Z", skin, sw=1.4)
    jewel = "" if robe else path("M -8,-86 Q 0,-78 8,-86", "none", stroke=GOLD, sw=2.4)

    head = f'<circle cx="0" cy="-100" r="9.5" fill="{skin}" stroke="{OUT}" stroke-width="{SW}"/>'
    # hair: a dark cap with a bun
    head += path("M -9,-102 C -10,-114 8,-114 9,-104 C 4,-108 -4,-108 -9,-102 Z", "#1f150f",
                 sw=1.2)
    if topknot:
        head += f'<ellipse cx="0" cy="-114" rx="5" ry="4.5" fill="#1f150f" stroke="{OUT}" stroke-width="1.2"/>'
    elif not crown:
        head += f'<circle cx="-9" cy="-104" r="5" fill="#1f150f" stroke="{OUT}" stroke-width="1.2"/>'
    head += (f'<path d="M 3,-102 q 3,-1.5 5,0" stroke="{OUT}" stroke-width="1.3" fill="none"/>'
             f'<path d="M 9,-98 l 2,3 l -2,1" stroke="{OUT}" stroke-width="1" fill="none"/>'
             f'<path d="M 4,-94 q 2,1 4,0" stroke="{RED_D}" stroke-width="1.2" fill="none"/>')
    if female:
        head += f'<circle cx="-1" cy="-92" r="2.2" fill="{GOLD}" stroke="{OUT}" stroke-width="0.8"/>'
    if scar:
        head += f'<path d="M 1,-106 L 7,-97" stroke="{RED}" stroke-width="1.6"/>'
    if crown:
        head += path("M -9,-106 L -8,-122 L -3,-114 L 0,-126 L 3,-114 L 8,-122 L 9,-106 Z",
                     GOLD, sw=1.4)
        head += f'<circle cx="0" cy="-112" r="2" fill="{RED}"/>'

    p.append(f'<g transform="translate(0,{dy})">{torso}{neck}{jewel}{head}</g>')
    p.append(f'<g transform="translate(0,{dy})">{limb(near, skin, 5.5)}{extra_hand}</g>')
    return g("".join(p), x, y, s, flip)


def monk(x, y, s=1.0):
    """A Paccekabuddha seated in meditation, with a halo."""
    c = (f'<circle cx="0" cy="-58" r="20" fill="{OCHRE}" opacity="0.35" stroke="{GOLD}" stroke-width="2"/>'
         + path("M -30,0 C -32,-14 -16,-20 0,-20 C 16,-20 32,-14 30,0 Z", "#c66a2c")
         + path("M -14,-20 C -16,-36 -14,-46 -9,-50 L 9,-50 C 14,-46 16,-36 14,-20 Z", "#c66a2c")
         + path("M -12,-22 C -2,-18 2,-18 12,-22 C 8,-14 -8,-14 -12,-22 Z", SKIN_M, sw=1.4)
         + f'<circle cx="0" cy="-60" r="9" fill="{SKIN_M}" stroke="{OUT}" stroke-width="{SW}"/>'
         + f'<path d="M -4,-60 q 2,1.5 4,0 M 1,-60 q 2,1.5 4,0" stroke="{OUT}" stroke-width="1.2" fill="none"/>'
         + path("M -9,-48 L 9,-36", "none", stroke="#9c4e1e", sw=1.4))
    return g(c, x, y, s)


# --- scenery ----------------------------------------------------------------

def rocks(x, y, s=1.0, fill=GREEN, light=GREEN_L, flip=False):
    """Ajanta's stacked, block-like hills."""
    c = (path("M 0,0 L 0,-60 L 18,-74 L 40,-70 L 46,-96 L 70,-104 L 86,-90 L 92,-64 "
              "L 116,-58 L 124,-30 L 140,-22 L 140,0 Z", fill)
         + path("M 0,-60 L 18,-74 L 40,-70 L 34,-58 Z M 46,-96 L 70,-104 L 86,-90 L 66,-86 Z "
                "M 92,-64 L 116,-58 L 108,-48 Z", light, sw=1.2))
    return g(c, x, y, s, flip)


def tree(x, y, s=1.0, flowers=None, foliage=GREEN, dark=GREEN_D):
    """A broad tree: sal when flowers is set, otherwise a banyan."""
    c = [path("M -8,0 C -6,-30 -10,-60 -2,-80 L 6,-80 C 12,-60 8,-30 12,0 Z", "#6b4630"),
         path("M -2,-70 C -20,-80 -30,-92 -36,-100 M 4,-74 C 20,-86 30,-94 40,-104",
              "none", stroke="#6b4630", sw=4)]
    for cx, cy, r in ((-40, -104, 26), (0, -122, 32), (40, -106, 26), (-20, -128, 22),
                      (22, -132, 22), (-56, -90, 16), (56, -92, 16)):
        c.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{foliage}" stroke="{OUT}" stroke-width="1.8"/>')
    for cx, cy in ((-40, -110), (0, -128), (36, -112), (-18, -134), (22, -138), (-4, -112)):
        c.append(f'<path d="M {cx - 6},{cy} q 6,-8 12,0 M {cx - 2},{cy + 8} q 6,-8 12,0" '
                 f'stroke="{dark}" stroke-width="1.6" fill="none"/>')
    if flowers:
        import random
        rnd = random.Random(7)
        for _ in range(26):
            a, b = rnd.uniform(-62, 62), rnd.uniform(-150, -84)
            c.append(f'<circle cx="{a:.0f}" cy="{b:.0f}" r="2.6" fill="{flowers}" stroke="{OUT}" stroke-width="0.6"/>')
    return g("".join(c), x, y, s)


def lotus(x, y, s=1.0):
    c = (f'<ellipse cx="-10" cy="4" rx="12" ry="3.5" fill="{GREEN}" stroke="{OUT}" stroke-width="1.2"/>'
         + path("M 0,0 C -10,-4 -12,-14 -6,-18 C -2,-12 0,-8 0,0 Z", PINK, sw=1.2)
         + path("M 0,0 C 10,-4 12,-14 6,-18 C 2,-12 0,-8 0,0 Z", PINK, sw=1.2)
         + path("M 0,0 C -4,-8 -4,-18 0,-24 C 4,-18 4,-8 0,0 Z", "#f1c8bd", sw=1.2))
    return g(c, x, y, s)


def water(x, y, w, h):
    c = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{LAPIS}" stroke="{OUT}" stroke-width="{SW}"/>'
    for i in range(int(h // 12)):
        for j in range(int(w // 40)):
            c += (f'<path d="M {x + 8 + j * 40 + (i % 2) * 18},{y + 9 + i * 12} q 6,-4 12,0 q 6,4 12,0" '
                  f'stroke="#7f9cc8" stroke-width="1.3" fill="none"/>')
    return c


def pillar(x, y, h, s=1.0):
    c = (path(f"M -9,0 L -9,{-h} L 9,{-h} L 9,0 Z", RED)
         + path(f"M -14,{-h} L 14,{-h} L 10,{-h - 12} L -10,{-h - 12} Z", OCHRE)
         + path(f"M -16,{-h - 12} L 16,{-h - 12} L 16,{-h - 18} L -16,{-h - 18} Z", OCHRE_D)
         + path("M -13,0 L 13,0 L 11,-10 L -11,-10 Z", OCHRE)
         + "".join(f'<path d="M -9,{-h + 20 + 22 * i} L 9,{-h + 20 + 22 * i}" stroke="{GOLD}" stroke-width="2"/>'
                   for i in range(int((h - 30) // 22))))
    return g(c, x, y, s)


def palace(floor_y=260, curtain=RED):
    """A palace interior: pillars, a lintel, festoons and a tiled floor."""
    c = [f'<rect x="0" y="0" width="480" height="{floor_y}" fill="#7a3a24"/>',
         f'<rect x="0" y="{floor_y}" width="480" height="{320 - floor_y}" fill="{OCHRE}"/>']
    for i in range(0, 480, 32):
        c.append(f'<path d="M {i},{floor_y} L {i - 30},320" stroke="{OCHRE_D}" stroke-width="1.4"/>')
    c.append(f'<path d="M 0,{floor_y + 22} L 480,{floor_y + 22} M 0,{floor_y + 46} L 480,{floor_y + 46}" stroke="{OCHRE_D}" stroke-width="1.4"/>')
    c.append(path(f"M 0,{floor_y} L 480,{floor_y}", "none", sw=2))
    c.append(f'<rect x="0" y="0" width="480" height="26" fill="{OCHRE_D}" stroke="{OUT}" stroke-width="{SW}"/>')
    for i in range(0, 480, 24):
        c.append(f'<circle cx="{i + 12}" cy="13" r="5" fill="{GOLD}" stroke="{OUT}" stroke-width="1"/>')
    for i in range(0, 480, 80):  # festoons
        c.append(path(f"M {i},26 Q {i + 40},62 {i + 80},26", "none", stroke=curtain, sw=5))
        c.append(f'<path d="M {i + 40},44 l 0,14" stroke="{GOLD}" stroke-width="2"/>'
                 f'<circle cx="{i + 40}" cy="60" r="3" fill="{GOLD}" stroke="{OUT}" stroke-width="1"/>')
    return "".join(c)


def couch(x, y, w=170):
    return (path(f"M {x},{y} L {x + w},{y} L {x + w},{y + 18} L {x},{y + 18} Z", OCHRE)
            + path(f"M {x + 6},{y + 18} L {x + 10},{y + 40} L {x + 18},{y + 40} L {x + 18},{y + 18} Z "
                   f"M {x + w - 18},{y + 18} L {x + w - 18},{y + 40} L {x + w - 10},{y + 40} L {x + w - 6},{y + 18} Z",
                   OCHRE_D)
            + path(f"M {x},{y} C {x - 4},{y - 18} {x + 8},{y - 26} {x + 26},{y - 20} L {x + 26},{y} Z", LAPIS)
            + "".join(f'<circle cx="{x + 20 + i * 22}" cy="{y + 9}" r="3" fill="{RED}"/>'
                      for i in range(int((w - 30) // 22) + 1)))


# --- bubbles ----------------------------------------------------------------

def bubble(x, y, w, lines, tail, think=False, size=12.5):
    """A speech bubble with its top-left at (x,y) and a tail pointing at `tail`."""
    lh = size * 1.25
    h = lh * len(lines) + 14
    tx, ty = tail
    cx = min(max(tx, x + 18), x + w - 18)
    edge = y + h if ty > y + h / 2 else y
    out = []
    if think:
        out.append(f'<ellipse cx="{x + w / 2}" cy="{y + h / 2}" rx="{w / 2 + 6}" ry="{h / 2 + 6}" '
                   f'fill="#fffaf0" stroke="{OUT}" stroke-width="2"/>')
        for i, r in enumerate((5, 3.5, 2.4)):
            k = (i + 1) / 4
            out.append(f'<circle cx="{cx + (tx - cx) * k:.1f}" cy="{edge + (ty - edge) * k:.1f}" r="{r}" '
                       f'fill="#fffaf0" stroke="{OUT}" stroke-width="1.6"/>')
    else:
        out.append(f'<path d="M {cx - 8},{edge} L {tx},{ty} L {cx + 8},{edge} Z" fill="#fffaf0" '
                   f'stroke="{OUT}" stroke-width="2" stroke-linejoin="round"/>')
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fffaf0" '
                   f'stroke="{OUT}" stroke-width="2"/>')
        out.append(f'<path d="M {cx - 6.5},{edge} L {cx + 6.5},{edge}" stroke="#fffaf0" stroke-width="3"/>')
    for i, line in enumerate(lines):
        out.append(f'<text x="{x + w / 2}" y="{y + 7 + lh * (i + 0.8)}" text-anchor="middle" '
                   f'class="say" font-size="{size}">{line}</text>')
    return "".join(out)


def label(x, y, text, size=10):
    return (f'<text x="{x}" y="{y}" class="lbl" font-size="{size}" text-anchor="middle">{text}</text>')


def frame(inner, title):
    """Wrap a scene in its SVG with plaster texture and a painted border."""
    return (f'<svg viewBox="0 0 480 320" role="img" aria-label="{title}" '
            f'xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="480" height="320" fill="{PLASTER}"/>'
            f'{inner}'
            f'<rect width="480" height="320" filter="url(#plaster)" opacity="0.5" '
            f'style="mix-blend-mode:multiply"/>'
            f'<rect width="480" height="320" fill="url(#vignette)"/>'
            f'<rect x="3" y="3" width="474" height="314" fill="none" stroke="{RED}" stroke-width="6"/>'
            f'<rect x="8" y="8" width="464" height="304" fill="none" stroke="{OCHRE}" stroke-width="2"/>'
            f'</svg>')


DEFS = (f'<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
        f'<defs>'
        f'<filter id="plaster" x="0" y="0" width="100%" height="100%">'
        f'<feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="4"/>'
        f'<feColorMatrix values="0 0 0 0 0.45  0 0 0 0 0.33  0 0 0 0 0.2  0 0 0 0.55 -0.12"/>'
        f'</filter>'
        f'<radialGradient id="vignette" cx="50%" cy="50%" r="70%">'
        f'<stop offset="65%" stop-color="#3b2418" stop-opacity="0"/>'
        f'<stop offset="100%" stop-color="#3b2418" stop-opacity="0.35"/>'
        f'</radialGradient>'
        f'</defs></svg>')

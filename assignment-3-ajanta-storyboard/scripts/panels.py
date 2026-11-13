"""The cover illustration and the eight storyboard scenes, composed from art.py."""

from art import (bubble, couch, elephant, frame, label, lotus, monk, palace, path,
                 person, pillar, rocks, tree, water,
                 ELE_G, ELE_GSH, GOLD, GREEN, GREEN_D, GREEN_L, IVORY, LAPIS,
                 LAPIS_D, OCHRE, OCHRE_D, OUT, PLASTER, RED, RED_D, SKIN_D, SKIN_L,
                 SKIN_M)


def cow(x, y, s, flip=False, **kw):
    return elephant(x, y, s, flip, body=ELE_G, shade=ELE_GSH, tusks=0, **kw)


def forest_ground(y=262, colour="#b59a64"):
    return (f'<rect x="0" y="{y}" width="480" height="{320 - y}" fill="{colour}"/>'
            + path(f"M 0,{y} L 480,{y}", "none", sw=2)
            + "".join(f'<path d="M {x},{y + 14 + (x * 7) % 30} l 4,-8 l 4,8 M {x + 6},{y + 14 + (x * 7) % 30} l 2,-10" '
                      f'stroke="{GREEN_D}" stroke-width="1.4" fill="none"/>'
                      for x in range(18, 470, 46)))


# ---------------------------------------------------------------------------

def cover():
    s = [f'<rect width="480" height="320" fill="#d7c6a0"/>',
         rocks(-10, 240, 1.4, fill="#7d8f62", light="#a5b487"),
         rocks(300, 240, 1.4, fill="#7d8f62", light="#a5b487", flip=True),
         rocks(330, 240, 1.3, fill=GREEN, light=GREEN_L),
         forest_ground(240),
         water(0, 270, 480, 50),
         elephant(196, 264, 1.15, crown=True),
         lotus(40, 300, 1.2), lotus(90, 296, 0.9), lotus(400, 302, 1.2), lotus(450, 294, 0.9)]
    return frame("".join(s), "The white six-tusked elephant king Chhaddanta beside a lotus lake")


def p1():
    s = [f'<rect width="480" height="320" fill="#d9c9a3"/>',
         rocks(-20, 214, 1.2, fill="#8c9b72", light="#b2bf95"),
         rocks(150, 214, 1.0, fill="#7d8f62", light="#a5b487"),
         rocks(300, 214, 1.3, fill="#8c9b72", light="#b2bf95", flip=True),
         rocks(330, 214, 1.2, fill="#7d8f62", light="#a5b487"),
         f'<rect x="0" y="212" width="480" height="108" fill="#b59a64"/>',
         path("M 0,212 L 480,212", "none", sw=2)]
    for i, x in enumerate((40, 84, 128, 360, 404, 448)):   # the distant herd
        s.append(cow(x, 216 + (i % 2) * 5, 0.28, flip=x > 240))
    s += [water(0, 264, 170, 56),
          lotus(26, 300), lotus(70, 290, 0.8), lotus(120, 304), lotus(150, 286, 0.7),
          cow(112, 262, 0.55),
          cow(430, 282, 0.6, flip=True),
          elephant(205, 292, 0.95, crown=True),
          label(240, 36, "THE LAKE OF CHHADDANTA, HIMALAYA", 11)]
    return frame("".join(s), "Chhaddanta, the white six-tusked elephant king, with his two queens and herd by a lotus lake")


def p2():
    falling_flowers = "".join(
        f'<circle cx="{x}" cy="{y}" r="2.8" fill="#f6efe0" stroke="{OUT}" stroke-width="0.6"/>'
        for x, y in ((206, 200), (226, 214), (244, 196), (218, 232), (252, 222), (236, 244)))
    twigs_and_ants = "".join(
        f'<path d="M {x},{y} l 9,-4 m -4,2 l 2,-5" stroke="#5a3a24" stroke-width="1.8" fill="none"/>'
        for x, y in ((96, 200), (122, 214), (84, 224), (134, 238))) + "".join(
        f'<circle cx="{x}" cy="{y}" r="1.8" fill="#b3261a"/>'
        for x, y in ((108, 206), (124, 228), (92, 238), (112, 246), (140, 218), (100, 252)))
    s = [f'<rect width="480" height="320" fill="#d2c39c"/>',
         rocks(-10, 262, 1.0, fill="#8c9b72", light="#b2bf95"),
         forest_ground(262),
         tree(190, 266, 1.0, flowers="#f6efe0"),
         cow(232, 290, 0.56, flip=True),
         cow(70, 292, 0.56),
         elephant(412, 274, 0.9, flip=True, trunk="reach", crown=True),
         falling_flowers, twigs_and_ants,
         label(82, 304, "Chullasubhadda", 10), label(232, 304, "Mahasubhadda", 10),
         bubble(14, 18, 156, ["Flowers for her&#8230;", "dry twigs and ants", "for me!"], (98, 226))]
    return frame("".join(s), "Chhaddanta strikes a flowering sal tree; blossoms fall on Mahasubhadda while twigs and red ants fall on Chullasubhadda")


def p3():
    stars = "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#f6efe0"/>'
                    for x, y in ((260, 30), (300, 60), (340, 24), (420, 44), (450, 80), (240, 84),
                                 (380, 90), (282, 108)))
    fruit_list = ((340, 262, RED), (352, 262, OCHRE), (346, 252, RED), (332, 256, OCHRE))
    fruit = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}" stroke="{OUT}" stroke-width="1.2"/>'
                    for x, y, c in fruit_list)
    s = [f'<rect width="480" height="320" fill="{LAPIS_D}"/>', stars,
         path("M 410,40 A 22,22 0 1,0 432,76 A 17,17 0 1,1 410,40 Z", "#f3e6be", sw=1.2),
         rocks(-30, 270, 1.3, fill="#3f5a3a", light="#5d7a52"),
         path("M 320,270 L 320,150 C 330,110 440,100 470,150 L 480,150 L 480,270 Z", "#4c5f3e"),
         path("M 346,270 L 346,176 C 360,140 430,138 450,176 L 450,270 Z", "#1f2a1c"),
         f'<rect x="0" y="268" width="480" height="52" fill="#6d5a3a"/>',
         path("M 0,268 L 480,268", "none", sw=2),
         monk(398, 266, 1.15),
         fruit,
         cow(160, 268, 0.82, kneel=True, trunk="offer",
             extra=f'<circle cx="186" cy="-58" r="7" fill="#7a9a4a" stroke="{OUT}" stroke-width="1.4"/>'),
         bubble(26, 28, 196, ["May I be born a queen&#8230;", "and may his tusks", "be mine!"],
                (214, 172), think=True),
         label(398, 302, "a Paccekabuddha", 10)]
    return frame("".join(s), "Chullasubhadda kneels before a Paccekabuddha at night, offering wild fruit and praying for revenge")


def p4():
    s = [palace(262),
         pillar(150, 262, 200), pillar(300, 262, 200),
         couch(20, 226, 196)]
    # the queen, lying on the couch in a soiled robe, head on the bolster
    queen = person(0, 0, 0.92, skin=SKIN_L, cloth="#8d7c63", cloth2="#6e604c",
                   female=True, crown=True, arms="grief")
    s.append(f'<g transform="translate(182,222) rotate(-90)">{queen}</g>')
    s += [person(262, 270, 1.0, flip=True, skin=SKIN_M, cloth=LAPIS, cloth2=GOLD,
                 crown=True, arms="hold"),
          person(430, 262, 0.72, flip=True, skin=SKIN_M, cloth=GREEN, cloth2=OCHRE),
          person(462, 262, 0.68, flip=True, skin=SKIN_D, cloth=RED, cloth2=OCHRE),
          person(372, 272, 0.95, flip=True, skin=SKIN_D, cloth=GREEN_D, cloth2=OCHRE,
                 scar=True, arms="point"),
          label(372, 304, "Sonuttara", 10),
          bubble(20, 62, 196, ["I dreamt of a six-tusked", "elephant. Bring me", "his tusks!"],
                 (88, 196)),
          bubble(332, 52, 132, ["I will go,", "my queen."], (366, 150))]
    return frame("".join(s), "In the palace at Benares, the queen feigns illness on her couch and asks for the tusks; the hunter Sonuttara steps forward")


def p5():
    bow = (path("M 30,-146 Q 64,-112 34,-74", "none", stroke="#5a3a24", sw=3)
           + path("M 30,-146 L 8,-104 L 34,-74", "none", stroke="#e9dfc8", sw=1)
           + path("M 8,-104 L 72,-124", "none", stroke=OUT, sw=2)
           + path("M 72,-124 l -8,-4 l 2,7 Z", RED, sw=1))
    leaves = "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="4" fill="{GREEN}" stroke="{OUT}" '
                     f'stroke-width="1" transform="rotate({r} {x} {y})"/>'
                     for x, y, r in ((128, 196, -10), (146, 192, 20), (300, 194, -15),
                                     (316, 198, 10), (286, 200, 25), (162, 198, -20),
                                     (330, 194, 5)))
    s = [f'<rect width="480" height="320" fill="#c9b78c"/>',
         tree(60, 200, 0.95),
         tree(430, 200, 0.8, foliage="#6f8a55"),
         rocks(200, 200, 0.9, fill="#8c9b72", light="#b2bf95"),
         f'<rect x="0" y="200" width="480" height="120" fill="#8a6a42"/>',
         "".join(f'<path d="M 0,{y} L 480,{y}" stroke="#7a5c38" stroke-width="1.2"/>'
                 for y in (230, 262, 294)),
         path("M 150,200 L 158,312 L 286,312 L 296,200 Z", "#3a2a1c"),
         person(222, 306, 1.0, skin=SKIN_D, cloth="#c79434", cloth2=OCHRE_D, robe=True,
                topknot=True, scar=True, arms="bow", extra_hand=bow),
         path("M 0,200 L 150,200 M 296,200 L 480,200", "none", sw=2),
         path("M 120,200 L 196,200 L 196,194 L 120,194 Z M 262,200 L 340,200 L 340,194 L 262,194 Z",
              "#6b4630", sw=1.6),
         leaves,
         elephant(470, 200, 0.82, flip=True),
         path("M 302,160 L 330,152", "none", stroke=OUT, sw=1.2, extra='stroke-dasharray="3 4"')]
    return frame("".join(s), "The hunter, disguised in a yellow robe, hides in a covered pit and shoots a poisoned arrow at the elephant")


def p6():
    s = [f'<rect width="480" height="320" fill="#d2c39c"/>',
         rocks(-20, 262, 1.2, fill="#8c9b72", light="#b2bf95"),
         rocks(360, 262, 1.1, fill="#7d8f62", light="#a5b487", flip=True),
         forest_ground(262),
         elephant(330, 282, 1.0, flip=True, trunk="up", arrow=True, crown=True),
         person(108, 284, 1.0, skin=SKIN_D, cloth="#c79434", cloth2=OCHRE_D, robe=True,
                topknot=True, scar=True, arms="anjali", kneel=True),
         bubble(300, 22, 160, ["Who sent you?", "And why?"], (236, 152)),
         bubble(18, 68, 168, ["The queen of Benares", "wants your tusks."], (112, 176))]
    return frame("".join(s), "The wounded elephant raises his trunk but spares the kneeling hunter because he wears a monk's robe")


def p7():
    saw = (path("M 82,-80 L 128,-48 L 124,-42 L 78,-74 Z", "#9aa0a4", sw=1.4)
           + "".join(f'<path d="M {82 + 4.6 * i},{-74 + 3.2 * i} l 1,4" stroke="{OUT}" stroke-width="1"/>'
                     for i in range(10)))
    s = [f'<rect width="480" height="320" fill="#cfc09a"/>',
         rocks(330, 262, 1.2, fill="#8c9b72", light="#b2bf95"),
         forest_ground(262),
         water(0, 230, 120, 32),
         elephant(320, 280, 1.05, flip=True, trunk="curl", kneel=True, arrow=True, crown=True,
                  extra=saw),
         person(96, 286, 1.0, skin=SKIN_D, cloth="#c79434", cloth2=OCHRE_D, robe=True,
                topknot=True, scar=True, arms="point"),
         bubble(226, 20, 236, ["Take them. The tusks of", "wisdom are far dearer", "to me than these."],
                (238, 150)),
         bubble(16, 104, 100, ["&#8230;!"], (100, 168))]
    return frame("".join(s), "Chhaddanta kneels and saws off his own tusks with his trunk to give them to the hunter")


def p8():
    tusks = ""
    for i in range(6):
        y = 250 - i * 4
        tusks += path(f"M {300 + i * 4},{y} Q {350 + i * 3},{y - 22} {398 + i * 2},{y - 6} "
                      f"Q {350 + i * 3},{y - 12} {300 + i * 4},{y + 6} Z", IVORY, sw=1.4)
    memory = f'<g opacity="0.3">{elephant(104, 192, 0.52, trunk="down")}</g>'
    s = [palace(262),
         pillar(28, 262, 200), pillar(458, 262, 200),
         memory,
         path("M 290,262 L 420,262 L 412,244 L 298,244 Z", RED),
         tusks,
         person(236, 270, 1.15, skin=SKIN_L, cloth=LAPIS, cloth2=GOLD, female=True,
                crown=True, arms="grief", kneel=True),
         person(446, 270, 0.82, flip=True, skin=SKIN_D, cloth="#c79434", cloth2=OCHRE_D,
                robe=True, topknot=True, scar=True, arms="anjali", kneel=True),
         bubble(282, 64, 168, ["My husband&#8230;", "what have I done?"], (254, 150))]
    return frame("".join(s), "Back in the palace, the queen sees the six tusks, remembers her former husband and collapses in grief")


PANELS = [p1, p2, p3, p4, p5, p6, p7, p8]

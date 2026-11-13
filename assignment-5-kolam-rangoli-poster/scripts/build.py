#!/usr/bin/env python3
"""
Build index.html: the Kolam & Rangoli poster.

All patterns come from scripts/patterns.py and are written into the page as
inline SVG, so index.html opens directly in a browser with no build step.
Re-run after changing the text or the patterns.

Usage:  python3 scripts/build.py
"""

import os

import patterns as P

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TILES = [
    (P.pulli_kolam(), "Dots &amp; lines", "Pulli kolam",
     "A grid of dots (<i>pulli</i>) is laid first; straight lines join them into lattices and diamonds."),
    (P.sikku_kolam(5, 1), "Continuous line", "Sikku kolam",
     "One unbroken line loops around every dot and returns to its start, without the hand ever lifting."),
    (P.geometric_rangoli(), "Geometric", "Rangoli",
     "Circles, triangles and petals repeated in 8 or 16 parts, filled with coloured powder."),
    (P.floral_rangoli(), "Floral", "Rangoli",
     "Lotus and flower motifs. The lotus is the seat of Lakshmi and a sign of purity."),
    (P.pongal_kolam(), "Festival: Pongal", "Kolam",
     "The harvest festival's pot boiling over, sugarcane and the Sun, drawn in rice flour."),
    (P.diwali_rangoli(), "Festival: Diwali", "Rangoli",
     "A lamp (<i>diya</i>) at the doorway lights the way for Lakshmi on the night of Diwali."),
]

NAMES = [
    ("Kolam", "Tamil Nadu"), ("Muggulu", "Andhra Pradesh &amp; Telangana"), ("Rangoli", "Maharashtra, Karnataka"),
    ("Alpana", "West Bengal &amp; Assam"), ("Aripan", "Bihar"), ("Mandana", "Rajasthan"),
    ("Chowk purana", "Uttar Pradesh"), ("Pookalam", "Kerala, in flowers"),
]

# small line icons for the "why" list (24 x 24 viewBox)
ICONS = {
    "lotus": '<path d="M12 20c-5 0-9-3-10-7 3 0 6 1 8 3-1-4 0-8 2-11 2 3 3 7 2 11 2-2 5-3 8-3-1 4-5 7-10 7z"/>',
    "door": '<path d="M5 21V9a7 7 0 0 1 14 0v12M2 21h20M9 21v-7h6v7"/>',
    "ant": '<circle cx="6" cy="12" r="2.5"/><circle cx="12" cy="12" r="2"/><circle cx="18" cy="12" r="3"/>'
           '<path d="M10 9l-2-4M14 9l2-4M10 15l-2 4M14 15l2 4M4 10l-2-3M4 14l-2 3M20 10l2-3"/>',
    "diya": '<path d="M3 13h18c-1 4-5 6-9 6s-8-2-9-6zM12 3c2 3 2 6 0 8-2-2-2-5 0-8z"/>',
    "dots": '<circle cx="5" cy="5" r="1.5"/><circle cx="12" cy="5" r="1.5"/><circle cx="19" cy="5" r="1.5"/>'
            '<circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>'
            '<circle cx="5" cy="19" r="1.5"/><circle cx="12" cy="19" r="1.5"/><circle cx="19" cy="19" r="1.5"/>'
            '<path d="M5 5l14 14M19 5L5 19"/>',
}

WHY = [
    ("lotus", "Auspicious beginnings",
     "A kolam at dawn marks a home as clean and blessed, and invites Lakshmi, goddess of prosperity. "
     "Traditionally its absence signals mourning."),
    ("door", "A welcome at the threshold",
     "The doorstep is where the home meets the world. The design greets every guest and is believed "
     "to keep evil away."),
    ("ant", "Food for small lives",
     "Rice flour feeds ants, birds and insects: a daily act of sharing with other living beings."),
    ("diya", "Festivals &amp; celebrations",
     "Pongal and the month of Margazhi, Diwali, Onam, weddings and pujas bring larger, brighter designs."),
    ("dots", "Skill passed down",
     "Learnt from mother to daughter and practised every morning, it trains memory, patience and a "
     "steady hand."),
]


def icon(name):
    return (f'<svg viewBox="0 0 24 24" class="ico" aria-hidden="true" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


def main():
    tiles = "\n".join(
        f'''      <figure class="tile">
        {svg}
        <figcaption><span class="kind">{kind}</span><b>{name}</b><span class="desc">{desc}</span></figcaption>
      </figure>''' for svg, kind, name, desc in TILES)
    names = "".join(f'<li><b>{n}</b><span>{r}</span></li>' for n, r in NAMES)
    why = "\n".join(
        f'''        <li>{icon(i)}<div><b>{t}</b><span>{d}</span></div></li>''' for i, t, d in WHY)
    braid = P.kolam_border(1120, height=24, step=28)

    html = PAGE.format(tiles=tiles, names=names, why=why, braid=braid,
                       maths=P.sikku_kolam(7, 2, size=200, pad=12, stroke=2.2))
    out = os.path.join(HERE, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"wrote {out} ({len(html) // 1024} KB)")


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kolam &amp; Rangoli Poster</title>
<meta name="description" content="A poster on Kolam and Rangoli, the traditional floor art of India: patterns, meaning and why to preserve them.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Yatra+One&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/poster.css">
</head>
<body>
<main class="poster">

  <header class="mast">
    <div class="braid-wrap">{braid}</div>
    <p class="kicker">Traditional Indian Floor Art</p>
    <h1>Kolam <span>&amp;</span> Rangoli</h1>
    <p class="subtitle">The Art of the Threshold</p>
    <p class="slogan">&ldquo;Draw the threshold, welcome the world.&rdquo;</p>
    <p class="byline">Aryan Garg &middot; RA2411003011414 &middot; FML-2 &middot; Sub-assignment 3 (CO4)</p>
    <div class="braid-wrap">{braid}</div>
  </header>

  <section class="intro">
    <div>
      <h2>Drawn at dawn, gone by night</h2>
      <p>Every morning across India the doorstep is swept, sprinkled with water and decorated before sunrise.
         In the South this is the <b>kolam</b>: lines of white rice flour drawn freehand, usually around a grid of
         dots, by the women of the house. In the North and West it is <b>rangoli</b>, from the Sanskrit
         <i>rangavalli</i>, &ldquo;rows of colour&rdquo;: designs filled with coloured powder, rice or flower petals,
         made above all for festivals.</p>
      <p>Both are meant to be temporary. They are walked over, washed away and eaten by ants, then drawn again
         the next day.</p>
    </div>
    <figure class="photo">
      <img src="images/kolam-doorstep.jpg" alt="A colourful Pongal kolam drawn on a street in front of a house gate, with a white rice-flour border">
      <figcaption>A Pongal kolam at a gate in Chennai, with a continuous-line border. Photo: Timothy A. Gonsalves, CC BY-SA 4.0</figcaption>
    </figure>
  </section>

  <section class="names" aria-label="Regional names">
    <h3>One art, many names</h3>
    <ul>{names}</ul>
  </section>

  <section class="patterns">
    <h2>Patterns of the floor</h2>
    <div class="grid">
{tiles}
    </div>
  </section>

  <section class="lower">
    <div class="why">
      <h2>Why we draw them</h2>
      <ul>
{why}
      </ul>
    </div>
    <div class="side">
      <div class="maths">
        <div class="maths-art">{maths}</div>
        <div>
          <h3>Did you know? Kolam is mathematics</h3>
          <p>A sikku kolam follows strict rules: a dot grid, one closed line, no loose ends, perfect symmetry.
             In the 1970s the Chennai computer scientist <b>Gift Siromoney</b> and his colleagues used kolams to define
             &ldquo;kolam array grammars&rdquo;, rules for generating pictures. Every sikku kolam on this poster was
             generated by a program that follows the kolam artist's rules.</p>
        </div>
      </div>
      <div class="pics">
        <figure class="photo">
          <img src="images/rangoli-diwali.jpg" alt="A Diwali rangoli in red, orange and white, lit by small oil lamps">
          <figcaption>Diwali rangoli with diyas, Goa. Photo: Dinesh Korgaokar, CC BY-SA 4.0</figcaption>
        </figure>
        <figure class="photo">
          <img src="images/pookalam-onam.jpg" alt="An Onam pookalam: a large round floor design made of yellow, orange, white and purple flower petals">
          <figcaption>Onam pookalam of flower petals, Kerala. Photo: Shreesha Sharma, CC BY-SA 4.0</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="preserve">
    <div class="preserve-text">
      <h2>Keep the threshold alive</h2>
      <p>Apartment corridors, tiled floors and rushed mornings are making the daily kolam rarer, and plastic stickers are
         replacing hand-drawn designs. Yet a kolam needs only a handful of rice flour and a few quiet minutes.
         Keeping this art alive does not need a museum, only a doorstep.</p>
    </div>
    <ol>
      <li>Learn one kolam from an elder, and teach it to a child.</li>
      <li>Draw with rice flour, flowers and natural colours, not stickers or chemical powders.</li>
      <li>Photograph and record the patterns and names of your region.</li>
      <li>Join a Margazhi or Diwali kolam contest in your neighbourhood.</li>
    </ol>
    <p class="last">A line of rice flour at dawn is a welcome to the world. Let us keep drawing it.</p>
  </section>

  <footer>
    <p><b>Sources:</b> Sahapedia, &ldquo;Significance of Kolam in Tamil Culture&rdquo;; Encyclopaedia Britannica, &ldquo;Rangoli&rdquo;;
       Craft Revival Trust, &ldquo;Rangoli &amp; Kolam: Threshold Arts of India&rdquo; (asiainch.org);
       Chennai Mathematical Institute, Gift Siromoney archive, &ldquo;Kolam&rdquo; (cmi.ac.in/gift).
       All patterns are original vector art by the author; photos via Wikimedia Commons.</p>
  </footer>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    main()

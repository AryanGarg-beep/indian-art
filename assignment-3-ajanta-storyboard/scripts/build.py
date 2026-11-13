#!/usr/bin/env python3
"""
Build index.html for the Chhaddanta Jataka storyboard.

The illustrations are generated from scripts/panels.py (which draws with
scripts/art.py) and written straight into the page as inline SVG, so the
finished index.html needs no build step to view: open it in any browser.
Re-run this only after changing the art or the text below.

Usage:  python3 scripts/build.py
"""

import os

from art import DEFS
from panels import PANELS, cover

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAME = "Aryan Garg"
REG_NO = "RA2411003011414"

PANEL_TEXT = [
    ("The Elephant King",
     "Long ago in the Himalaya, the Bodhisattva was born as Chhaddanta, a white elephant "
     "with six shining tusks. He led a herd of eight thousand elephants by a lotus lake, "
     "with his two queens, Mahasubhadda and Chullasubhadda."),
    ("A Careless Moment",
     "One festive day he struck a flowering sal tree. Blossoms showered on Mahasubhadda, "
     "but dry twigs and red ants fell on Chullasubhadda. It was an accident, but she took "
     "it as an insult and nursed a grudge."),
    ("A Bitter Prayer",
     "Chullasubhadda offered wild fruit to a Paccekabuddha, a solitary sage, and turned the "
     "merit into a wish: to be reborn a queen and win the elephant's tusks. Then she "
     "starved herself to death."),
    ("The Queen of Benares",
     "Reborn as Subhadda, she became chief queen of Benares and remembered her past life. "
     "Feigning illness, she asked the king for the six tusks of the elephant in her dream. "
     "The scarred hunter Sonuttara was chosen to fetch them."),
    ("The Trap",
     "After a long journey, Sonuttara dug a pit where the elephants came to bathe and "
     "covered it over. Dressed in a monk's yellow robe, he waited, then shot the elephant "
     "king with a poisoned arrow."),
    ("The Robe Stays His Anger",
     "Roaring in pain, Chhaddanta rushed at his attacker, then saw the yellow robe. Out of "
     "respect for the robe of holy men he spared the hunter, and asked only who had sent him "
     "and why."),
    ("The Gift",
     "The hunter could not cut through the tusks, so the dying elephant took the saw in his "
     "own trunk and cut them himself. He gave them freely, hoping the gift would bring him "
     "closer to enlightenment."),
    ("The Queen's Grief",
     "When Subhadda saw the six tusks, she remembered the husband she had once loved. "
     "Overcome with grief and remorse, her heart broke and she died that same day."),
]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Chhaddanta Storyboard</title>
<meta name="description" content="An eight-panel storyboard of the Chhaddanta Jataka as painted in the Ajanta Caves.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/story.css">
</head>
<body>
{defs}
<main>

<header class="cover">
  <div>
    <p class="eyebrow">Ajanta Cave Paintings &middot; Storyboard</p>
    <h1>The Elephant Who Gave His Tusks <em>The Chhaddanta Jataka</em></h1>
    <dl class="meta">
      <dt>Name</dt><dd>{name}</dd>
      <dt>Register no.</dt><dd>{reg}</dd>
      <dt>Course</dt><dd>FML-2 &middot; Sub-assignment 1 &middot; CO2</dd>
    </dl>
  </div>
  <div>{cover_art}</div>
</header>

<section id="glance">
  <header>
    <p class="eyebrow">Before the story</p>
    <h2>The story at a glance</h2>
    <p>The Chhaddanta Jataka is No. 514 in the Pali collection of the Buddha's previous lives.
       In it the Bodhisattva, the future Buddha, is born as an elephant, and the story turns on a grudge
       carried from one life into the next.</p>
  </header>
  <div class="glance">
    <div class="card">
      <h3>Main characters</h3>
      <ul class="cast">
        <li><b>Chhaddanta</b>: the Bodhisattva, a white elephant king with six tusks, leader of eight thousand elephants.</li>
        <li><b>Mahasubhadda</b>: his senior queen.</li>
        <li><b>Chullasubhadda</b>: his junior queen. She feels slighted, and is reborn as <b>Subhadda</b>, queen of Benares.</li>
        <li><b>Sonuttara</b>: a hunter sent to bring back the tusks. In the Pali text he is an old enemy of the Bodhisattva.</li>
        <li><b>The king of Benares</b>: Subhadda's husband, who sends out the hunters.</li>
        <li><b>A Paccekabuddha</b>: a solitary enlightened sage, to whom Chullasubhadda offers fruit.</li>
      </ul>
    </div>
    <div class="card">
      <h3>Setting</h3>
      <ul class="settings">
        <li>The lake of Chhaddanta in the Himalaya, where the herd lives by a great banyan tree.</li>
        <li>The royal palace at Benares (Varanasi).</li>
      </ul>
      <h3>Sequence of events</h3>
      <ol class="seq">
        <li>The elephant king and his two queens</li>
        <li>The sal-tree incident and the grudge</li>
        <li>Chullasubhadda's prayer and death</li>
        <li>Rebirth as queen of Benares; the tusks demanded</li>
        <li>The hunter's trap and poisoned arrow</li>
        <li>The robe saves the hunter's life</li>
        <li>Chhaddanta cuts and gives his tusks</li>
        <li>The queen's grief</li>
      </ol>
    </div>
  </div>
</section>

<section id="panels">
  <header>
    <p class="eyebrow">The storyboard</p>
    <h2>Eight panels</h2>
  </header>
  <div class="board">
{panels}
  </div>
</section>

<section id="message">
  <div class="message">
    <p class="eyebrow">Concluding message</p>
    <blockquote>Anger takes everything; compassion gives everything.</blockquote>
    <p>The queen's grudge, carried across a whole lifetime, destroyed the one she had once loved, and
       then destroyed her too. The elephant, betrayed and dying, answered cruelty with forgiveness and
       gave freely. Hatred harmed the one who held it; compassion lasted even as he was being killed.</p>
    <p>That is why Ajanta's painters gave this story a place on the walls where monks lived and prayed:
       it shows <i>dana</i> (generosity) and <i>karuna</i> (compassion) at their most complete.</p>
  </div>
</section>

<section id="significance">
  <header>
    <p class="eyebrow">Historical note</p>
    <h2>Why this story matters at Ajanta</h2>
  </header>
  <div class="note">
    <div>
      <p><b>The Jatakas</b> are the stories of the Buddha's previous births. In them the Bodhisattva,
         sometimes a king and sometimes an animal, perfects virtues such as generosity, patience and
         compassion. At Ajanta they were the main teaching material on the walls: monks and pilgrims
         walked around the halls and &ldquo;read&rdquo; the paintings as stories.</p>
      <p><b>Painted twice, five centuries apart.</b> The Chhaddanta Jataka is painted in both great phases
         of Ajanta. In <b>Cave 10</b>, a chaitya hall of the Satavahana period (c. 2nd&ndash;1st century BCE),
         it is among the oldest surviving paintings in India. In <b>Cave 17</b>, a monastery cave made
         in the late 5th century CE under the Vakataka king Harishena, it appears again in the mature
         classical style. Setting the two side by side shows how Ajanta painting grew over about 500 years.</p>
      <p><b>Continuous narration.</b> The Cave 17 painter did not use frames. Palace and forest scenes flow
         into one another across the wall, and the same characters appear several times. This storyboard
         divides that flow into eight panels, a modern version of the same storytelling idea.</p>
      <p><b>Technique.</b> The murals were painted on a layer of clay mixed with plant fibre, finished with
         a thin coat of lime. The pigments were minerals: red and yellow ochre, green earth (terre verte),
         lamp black, lime white and imported lapis lazuli. The illustrations here use the same colours.</p>
      <p><b>Why a monastery chose it.</b> The elephant spares his killer only because he wears the yellow
         robe. For the monks who lived in these caves, that was a reminder of the respect owed to the robe,
         and of how much it asked of them. The story also teaches that anger turns back on the angry person.</p>
      <p>The caves were rediscovered in 1819 by a British officer, John Smith, and were declared a
         UNESCO World Heritage Site in 1983.</p>
    </div>
    <div class="plates">
      <figure>
        <img src="images/cave17-wall.jpg" alt="The Chhaddanta Jataka wall in Ajanta Cave 17: a palace scene at left and white elephants in a forest at right" loading="lazy">
        <figcaption><b>The original on the cave wall.</b> Cave 17, late 5th century CE: the palace (left) and the herd in the
          forest (right) belong to the same story, in continuous narration. Photo: SpeakingArch, CC BY-SA 4.0, via Wikimedia Commons.</figcaption>
      </figure>
      <figure>
        <img src="images/cave17-chhaddanta.jpg" alt="Detail of the white elephant Chhaddanta with attendants, Ajanta Cave 17" loading="lazy">
        <figcaption>Detail: the white elephant and his herd, Cave 17. Photo: Shishirdasika, CC BY-SA 4.0, via Wikimedia Commons.</figcaption>
      </figure>
      <div>
        <h3>The Ajanta palette used in the panels</h3>
        <div class="palette">
          <div class="swatch"><i style="background:#c8902e"></i>Yellow ochre</div>
          <div class="swatch"><i style="background:#9b3b26"></i>Red ochre</div>
          <div class="swatch"><i style="background:#5f7a4a"></i>Terre verte</div>
          <div class="swatch"><i style="background:#2c4a7a"></i>Lapis lazuli</div>
          <div class="swatch"><i style="background:#efe4cc"></i>Lime white</div>
          <div class="swatch"><i style="background:#2a1d14"></i>Lamp black</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="references">
  <header>
    <p class="eyebrow">Sources</p>
    <h2>References</h2>
  </header>
  <ol class="refs">
    <li>Cowell, E. B. (ed.), <i>The Jataka, or Stories of the Buddha's Former Births</i>, Vol. V, No. 514,
        &ldquo;Chaddanta-Jataka&rdquo;, trans. H. T. Francis. Cambridge University Press, 1905. Online:
        <a href="https://ancient-buddhist-texts.net/English-Texts/Jataka/514.htm">ancient-buddhist-texts.net</a>.</li>
    <li>Schlingloff, Dieter. <i>Ajanta: Handbook of the Paintings 1: Narrative Wall-paintings</i>.
        New Delhi: Indira Gandhi National Centre for the Arts, 2013.</li>
    <li>Spink, Walter M. <i>Ajanta: History and Development</i>. Leiden: Brill, 2005&ndash;2017.</li>
    <li>UNESCO World Heritage Centre, &ldquo;Ajanta Caves&rdquo;.
        <a href="https://whc.unesco.org/en/list/242">whc.unesco.org/en/list/242</a>.</li>
    <li>World History Encyclopedia, &ldquo;The Ajanta Caves&rdquo;.
        <a href="https://www.worldhistory.org/article/849/the-ajanta-caves/">worldhistory.org/article/849</a>.</li>
    <li>Sahapedia, &ldquo;The Ajanta caves: an overview&rdquo;.
        <a href="https://www.sahapedia.org/ajanta-caves-overview">sahapedia.org/ajanta-caves-overview</a>.</li>
    <li>Photographs: &ldquo;The Chaddanta Jatak, 5th century CE, Ajanta cave 17&rdquo; by SpeakingArch, and
        &ldquo;Ajanta chaddanta Jataka&rdquo; by Shishirdasika, both CC BY-SA 4.0, Wikimedia Commons.</li>
  </ol>
</section>

</main>
<footer>{name} &middot; {reg} &middot; FML-2</footer>
</body>
</html>
"""

PANEL = """    <figure class="panel">
      {svg}
      <figcaption>
        <span class="num">Panel {n} of 8</span>
        <h3>{title}</h3>
        <p>{text}</p>
      </figcaption>
    </figure>"""


def main():
    panels = "\n".join(
        PANEL.format(svg=draw(), n=i + 1, title=title, text=text)
        for i, (draw, (title, text)) in enumerate(zip(PANELS, PANEL_TEXT)))
    html = PAGE.format(defs=DEFS, cover_art=cover(), panels=panels, name=NAME, reg=REG_NO)
    out = os.path.join(HERE, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"wrote {out} ({len(html) // 1024} KB)")


if __name__ == "__main__":
    main()

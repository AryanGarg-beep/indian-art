# Kolam & Rangoli: The Art of the Threshold

FML-2, Sub-assignment 3 (CO4): an informative poster on Kolam and Rangoli.
Aryan Garg, RA2411003011414.

## What to submit

- **`poster.pdf`**: one A3 portrait page (297 × 420 mm). It also prints cleanly scaled down to A4
  ("Fit to page").
- **`index.html`**: the same poster as a web page; on a phone it stacks into one column.

## What's on it

- Title, slogan (*"Draw the threshold, welcome the world."*), name and register no.
- Introduction, with a photo of a doorstep kolam, and the regional names (Kolam, Muggulu,
  Rangoli, Alpana, Aripan, Mandana, Chowk purana, Pookalam).
- Six labelled pattern tiles:
  - dots-and-lines (pulli) kolam;
  - continuous-line (sikku) kolam;
  - geometric rangoli;
  - floral rangoli;
  - Pongal festival kolam;
  - Diwali festival rangoli.
- *Why we draw them*: auspiciousness and Lakshmi, welcoming guests at the threshold, feeding small
  creatures, festivals, a skill passed down.
- *Did you know?*: kolam and mathematics (Gift Siromoney's kolam array grammars).
- Photos of a Diwali rangoli and an Onam pookalam.
- Closing message on preservation, with four concrete actions.
- Sources and image credits.

## The patterns are generated, not drawn by hand

`scripts/patterns.py` draws every pattern as SVG. The sikku kolams use the *mirror-curve*
rule:
- A line runs diagonally between grid dots and bounces off "mirrors" placed between them.
- The program searches for a symmetric set of mirrors that gives **one closed line**, the same
  rule a kolam artist follows.
- `python3 scripts/patterns.py` prints a check that each kolam really is a single loop.

## Folder

| Path | What it is |
|---|---|
| `index.html` | The poster (generated, with inline SVG) |
| `css/poster.css` | Layout; the print rules fit it to one A3 page |
| `images/` | Three Wikimedia Commons photos (CC BY-SA 4.0); `manifest.json` holds the credits |
| `scripts/patterns.py` | Kolam and rangoli generators |
| `scripts/build.py` | Writes `index.html`; all poster text lives here |
| `scripts/fetch_images.py` | Re-downloads the photos |

## Rebuilding

```bash
python3 scripts/build.py
google-chrome-stable --headless=new --no-pdf-header-footer \
  --print-to-pdf=poster.pdf "file://$PWD/index.html"
```
Or use the browser's Print → Save as PDF with paper size A3, margins none, background graphics on.

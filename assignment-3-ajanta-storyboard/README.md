# The Elephant Who Gave His Tusks: Chhaddanta Jataka storyboard

FML-2, Sub-assignment 1 (CO2): a storyboard of a story from the Ajanta Cave Paintings.
Aryan Garg, RA2411003011414.

## What to submit

- **`storyboard.pdf`**: the finished storyboard, A4 landscape, 13 pages:
  cover → story at a glance → 8 panels (one per page) → concluding message →
  historical note → references.
- **`index.html`**: the same storyboard as a web page. Double-click to open; no setup needed.

## Folder contents

| Path | What it is |
|---|---|
| `index.html` | The storyboard page. All illustrations are inline SVG inside it |
| `css/story.css` | Layout, colours, and the print rules that produce the PDF |
| `images/` | Two CC BY-SA photos of the real Cave 17 mural (credited in the page) |
| `scripts/art.py` | Drawing helpers: elephants, people, trees, palace, speech bubbles |
| `scripts/panels.py` | The cover and the eight scenes, composed from `art.py` |
| `scripts/build.py` | Writes `index.html`; the panel captions and the name/register no. live here |

## Changing something

1. Edit the text in `scripts/build.py`, or the drawings in `scripts/panels.py`.
2. Rebuild the page: `python3 scripts/build.py`
3. Re-make the PDF, either with your browser's Print → Save as PDF (A4, landscape,
   no headers/footers) or with:
   ```bash
   google-chrome-stable --headless=new --no-pdf-header-footer \
     --print-to-pdf=storyboard.pdf "file://$PWD/index.html"
   ```

The page uses Google Fonts when online and falls back to Georgia/Palatino offline.

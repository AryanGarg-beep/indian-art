# Carving the Cosmos: Arjuna's Penance and the Pancha Rathas

FML-2, Sub-assignment 2 (CO2): a thematic analysis of the rock-cut sculpture of Mahabalipuram.
Aryan Garg, RA2411003011414.

## What to submit

- **`report.pdf`**: the 7-page A4 report (limit: 5–7 pages). Every page has a footer with the
  page number, your name and register no.
- **`index.html`**: the same report as a web page. Double-click to open.

## Contents

1. Introduction: Mahabalipuram and the Pallavas
2. Arjuna's Penance: composition (Fig. 2 zone diagram), iconography, the Arjuna/Bhagiratha
   debate, analysis
3. Pancha Rathas: monolithic carving, the five temple types (Fig. 5 diagram + comparison
   table), analysis
4. Themes across both monuments
5. Conclusion: the Pallava achievement
6. References and image credits

## Folder

| Path | What it is |
|---|---|
| `index.html` | The report. Both diagrams are inline SVG drawn for this report |
| `css/report.css` | Screen styles and the A4 print rules, including the page-number footer |
| `images/` | Eight Wikimedia Commons photos (CC BY / CC BY-SA). `manifest.json` holds the credits |
| `scripts/fetch_images.py` | Re-downloads the photos. Uses the Commons helpers in `../assignment-1-and-2/scripts/` |

## Re-making the PDF

Use the browser's Print → Save as PDF (A4, portrait, headers/footers **off**, background
graphics **on**), or run:

```bash
google-chrome-stable --headless=new --no-pdf-header-footer \
  --print-to-pdf=report.pdf "file://$PWD/index.html"
```

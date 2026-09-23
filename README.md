# Indian Art History — Interactive Timeline & Art Map

A static website built for a college art-history assignment. It contains two
interactive tools:

1. **Interactive Timeline** (`timeline.html`) — fifteen landmark artifacts from
   the prehistoric rock shelters of Bhimbetka to the Santiniketan frescoes,
   arranged across eleven era bands, with an era filter, keyboard navigation and
   a detail view for each piece.
2. **Interactive Art Map** (`map.html`) — fifteen regional art forms pinned to a
   Leaflet map of India, colour-coded by category, with a legend that doubles as
   a filter and a search box.

Everything is plain HTML, CSS and vanilla JavaScript. **There is no build step,
no npm, and no framework.**

---

## How to run it

### Option 1 — just open it

Double-click `index.html`. That's it. Every page works directly from the file
system.

### Option 2 — local web server

If you prefer serving it (or want to test exactly what GitHub Pages will do):

```bash
cd indian-art
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

### What needs an internet connection

| Feature | Works offline? |
|---|---|
| Timeline page, all artifact images and text | **Yes** |
| Map page interface, sidebar, search | Yes |
| The map itself (Leaflet library + OpenStreetMap tiles) | **No** — needs internet |
| Google Fonts headings | No, but the CSS falls back to Georgia/Palatino and the page still looks correct |

### If the map background shows "Access blocked" or grey squares

The pins, detail panels, filters and search are all local and keep working —
only the background map is affected.

OpenStreetMap's tiles come from volunteer-run servers, and their
[usage policy](https://operations.osmfoundation.org/policies/tiles/) asks that
sites avoid bulk or automated requests. If your IP address makes a lot of
requests in a short time — reloading the page over and over while testing, for
example — OSM temporarily serves a grey "Access blocked" tile instead of the
map. **It clears by itself**, usually within a few minutes to an hour. Normal
visitors browsing the site will not trigger it.

If you hit it and do not want to wait, switch tile provider. Open `js/map.js`
and change one word near the top:

```js
var TILES = "osm";     // change to "esri"
```

Esri's World Street Map needs no API key, renders the same OpenStreetMap data,
and is attributed automatically. Everything else stays the same.

The map also shows an explanatory message on the page if tiles fail to load, so
you are never left looking at blank squares with no explanation.

---

## Deploying to GitHub Pages

1. Create a new repository on GitHub (for example `indian-art`).
2. From this folder:

   ```bash
   git init
   git add .
   git commit -m "Indian art history timeline and map"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/indian-art.git
   git push -u origin main
   ```

3. On GitHub go to **Settings → Pages**.
4. Under **Build and deployment**, set **Source** to *Deploy from a branch*, then
   choose branch `main` and folder `/ (root)`. Save.
5. Wait about a minute. The site appears at
   `https://YOUR-USERNAME.github.io/indian-art/`.

Notes:

- All links are relative, so the site works in a subfolder like
  `/indian-art/` without any change.
- No file or folder name starts with an underscore, so GitHub's Jekyll
  processing will not skip anything. A `.nojekyll` file is not needed.
- The `images/` folder is about 17 MB. That is well within GitHub Pages'
  1 GB limit — just remember to commit it, since the site will not work
  without it.

---

## Project structure

```
index.html            landing page linking to both tools
timeline.html         Assignment 1
map.html              Assignment 2
css/style.css         all styling for all three pages
js/timeline.js        timeline rail, era filter, modal, keyboard nav
js/map.js             Leaflet map, category filter, search
data/artifacts.js     the 15 timeline entries  <- edit this to change content
data/locations.js     the 15 map entries       <- edit this to change content
images/               30 downloaded images (~1200px wide)
images/manifest.json  record of what was downloaded, written by the fetch script
scripts/              helper scripts (see below); not needed to run the site
CREDITS.md            every image with author, licence and source URL
README.md             this file
```

---

## Why the data files are `.js` and not `.json`

The assignment brief asked for `data/artifacts.json` and `data/locations.json`.
**This was deliberately changed to `.js`, and here is the reason.**

Loading a local `.json` file requires `fetch()`. When a page is opened by
double-clicking it, the browser treats its origin as *opaque*, and the fetch is
blocked by the same-origin policy:

```
Cross origin requests are only supported for protocol schemes:
http, data, chrome, https.
```

This happens in both Chrome and Firefox. So `.json` + `fetch()` would have
meant the site only worked behind a web server — breaking the "opens by
double-clicking `index.html`" requirement.

The fix is to declare the data as a normal JavaScript variable and load it with
an ordinary `<script>` tag:

```html
<script src="data/artifacts.js"></script>   <!-- defines ARTIFACTS -->
<script src="js/timeline.js"></script>      <!-- uses ARTIFACTS -->
```

```js
const ARTIFACTS = [ { "id": "dancing-girl", ... } ];
```

The content inside is exactly the same structure as JSON would have been, it is
still one file to edit, and now the site works **both** by double-click and on
GitHub Pages with no server at all.

*(If your marker specifically requires a `.json` file, rename the files, change
the two `<script>` tags to `fetch()` calls, and then you must run a local server
to view the site.)*

---

## How to add or edit an entry

### Adding a timeline artifact

Open `data/artifacts.js`, copy an existing block, and change the fields:

```js
{
  id: "my-artifact",              // unique; also the image filename stem
  title: "Name of the artifact",
  era: "gupta",                   // must match an id in the ERAS array above
  dateDisplay: "c. 5th century CE",
  dateSort: 450,                  // signed year, used only for ordering
  region: "Where it is from",
  medium: "Material and technique",
  attribution: "Artist or patron, or Unknown",
  context: "Four to six lines of historical background.",
  whyItMatters: "One line on why it is significant.",
  image: "images/my-artifact.jpg",
  alt: "Description of the picture for screen-reader users.",
  credit: {
    title:   "Title of the file on Wikimedia Commons",
    author:  "Photographer or artist",
    licence: "CC BY-SA 4.0",
    source:  "https://commons.wikimedia.org/wiki/File:..."
  }
}
```

The timeline sorts itself by `dateSort` and groups by `era`, so you do not need
to insert the block in any particular position.

### Adding a map pin

Same idea in `data/locations.js`. `category` must be one of the ids in the
`CATEGORIES` array at the top (`folk`, `court`, `temple`, `modern`), and `lat` /
`lon` are decimal degrees. Adding a new category to that array automatically
adds it to the legend and the filter.

### After changing any `credit` block

Regenerate the credits file so it stays in step:

```bash
python3 scripts/make_credits.py
```

---

## Helper scripts

These were used to build the site and are kept so the process is reproducible.
**You do not need to run them to use the site.**

| Script | What it does |
|---|---|
| `scripts/search_candidates.py` | Searches Wikimedia Commons for candidate images and prints each one's licence, so a human can pick. |
| `scripts/fetch_images.py` | Downloads the chosen images at ~1200px, rejects anything not public domain or Creative Commons, and writes `images/manifest.json`. |
| `scripts/make_credits.py` | Regenerates `CREDITS.md` from the `credit` blocks in the two data files. |

Image filenames were never guessed — every one was found by searching the
Commons API and then verified. Images were downloaded through the Commons
thumbnail renderer at 1200px, so no local image-processing tool was needed.

---

## Accessibility

- Every image has descriptive `alt` text.
- All interactive elements are real `<button>` and `<input>` elements, so they
  are keyboard operable by default.
- A visible focus ring is shown on every focusable element.
- The timeline modal traps `Tab` while open, closes on `Esc`, and returns focus
  to the artifact node that opened it.
- On the map, selecting a pin opens a detail panel rather than a Leaflet popup,
  so long entries are never clipped by the edge of the map. It closes on `Esc`
  and returns focus to the pin. Leaflet fires the same event for a mouse click
  and for `Enter` on a focused pin, so it works either way.
- Filter state is exposed with `aria-pressed`; the active nav link uses
  `aria-current="page"`; result counts are announced with `aria-live`.
- Each page starts with a "Skip to main content" link.
- The design respects `prefers-reduced-motion`.

## Keyboard shortcuts on the timeline

| Key | Action |
|---|---|
| `Tab` | Move between filter buttons and artifact nodes |
| `←` / `→` | Move between artifacts (both on the rail and inside the detail view) |
| `Enter` / `Space` | Open the focused artifact |
| `Esc` | Close the detail view |

Individual artifacts can also be linked to directly, for example
`timeline.html#nataraja`.

---

## Verify before submitting

These are the points where the history is genuinely uncertain, or where a
judgement call was made. **Please check them against your course reading before
you hand this in.** Where a date is disputed the site says so rather than
choosing an answer.

### Dates and attributions that are genuinely disputed

1. **Didarganj Yakshi** — the biggest open question on the timeline. The high
   polish suggests a Mauryan date (3rd century BCE); the jewellery and modelling
   suggest Kushan-period Mathura (1st–2nd century CE). Scholars still disagree.
   The site gives the full range and states the dispute.
2. **Bhimbetka** — the shelters were painted over an enormous span and the
   layers overlap, so the paintings cannot be radiocarbon-dated directly. The
   site gives a range ("c. 10,000 BCE onward") rather than a single date.
3. **Pashupati seal** — the "proto-Shiva" reading is Marshall's interpretation
   from the 1920s and is contested; the Indus script is undeciphered. The site
   presents it as debated, not settled.
4. **Nataraja** — Chola bronzes are dated by style, and the LACMA piece shown is
   given as "c. 11th century". Museum labels vary between the 10th and 12th
   centuries.
5. **Gandhara Buddha** — "c. 2nd–3rd century CE", following the Matsuoka Museum
   label. Gandharan sculpture dating is broad and often approximate.

### Licensing point worth confirming with your department

6. **Nandalal Bose (Santiniketan fresco)** — Bose died in 1966. Indian copyright
   runs for 60 years after the author's death, so his work enters the public
   domain in India in **2027**. The photograph used here is licensed CC BY-SA 4.0
   by the photographer, and Wikimedia Commons hosts it on the basis of India's
   freedom-of-panorama provision (Copyright Act s. 52(1)(u)), which covers works
   permanently situated in public places. This is a reasonable basis, but if your
   department wants only unambiguously public-domain material, replace this entry
   — the timeline would then end with Amrita Sher-Gil (d. 1941, clearly public
   domain).

   Related note: **M. F. Husain** was suggested in the original brief but had to
   be dropped. He died in 2011, so his paintings are in copyright in India until
   2072 and there are no freely licensed images of his work — Wikimedia Commons
   has only photographs *of the artist*, not of his art.

### Editorial judgements

7. **Kalighat is categorised as "Modern / Urban", not folk.** This is a
   deliberate choice: Kalighat is a 19th-century *urban* form that broke from
   village scroll-painting and temple patronage, commented on colonial city life,
   and fed directly into Indian modernism through Jamini Roy. If your course
   treats it as a folk tradition, change `category: "modern"` to
   `category: "folk"` in `data/locations.js` — the legend counts update
   automatically.
8. **Some images illustrate a school rather than one specific named work.** The
   Gandhara Buddha, Kangra folio, Pahari/Basohli pin, Bikaner pin and all the
   folk-art pins are representative examples of their tradition, not "the"
   single famous work. Each is captioned with its actual Commons title.
9. **The Kangra folio is early 19th century**, from the Lambagraon *Gita
   Govinda* series (c. 1820–25), not late 18th century. Kangra painting as a
   style matured earlier, in the later 18th century; the site distinguishes the
   two.
10. **Mathura has no separate entry.** The era band is labelled
    "Gandhara / Mathura" but only a Gandhara Buddha is shown. Adding a Mathura
    red-sandstone Buddha would be the natural sixteenth artifact if your brief
    wants both schools represented side by side.
11. **Santiniketan is not a map pin.** It would be the natural sixteenth pin
    under the "modern" category, pairing with the Nandalal Bose timeline entry.

### Images

12. All 30 images downloaded successfully and **no placeholder images were
    needed**. Every image is public domain or Creative Commons — see
    `CREDITS.md` for the full list with authors, licences and source URLs.
13. Two images are smaller than the 1200px target because Commons holds no
    larger version: `gond.jpg` (734px wide) and `pashupati.jpg` (810px wide).
    Both are perfectly legible at the sizes used on the page.

---

## Credits

Images: Wikimedia Commons — full attribution in [`CREDITS.md`](CREDITS.md).
Map tiles: © OpenStreetMap contributors.
Map library: [Leaflet](https://leafletjs.com/) 1.9.4, loaded from CDN.
Fonts: Cormorant Garamond and Inter, via Google Fonts, with local fallbacks.

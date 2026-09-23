#!/usr/bin/env python3
"""
Stage B of image sourcing: download the chosen Commons images.

Every title below was found by running scripts/search_candidates.py and
picking from real search results -- no filename is ever invented. This
script resolves each title, checks the licence is PD or CC, downloads a
~1200px version (Commons does the resizing for us, so we need no image
tooling locally), and writes images/manifest.json with the credit data
that data/*.js and CREDITS.md are built from.

Usage:  python3 scripts/fetch_images.py
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from search_candidates import api_get, licence_ok, UA        # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(HERE, "images")
MANIFEST = os.path.join(IMAGES, "manifest.json")

# id -> exact Commons File: title, chosen by hand from search results.
PICKS = {
    # --- timeline -------------------------------------------------------
    "bhimbetka":     "File:Rock Shelter 15, Bhimbetka 02.jpg",
    "dancing-girl":  "File:Dancing girl of Mohenjo-daro.jpg",
    "pashupati":     "File:Pashupati seal impression.jpg",
    "lion-capital":  "File:Lion capital of Ashoka, Sarnath.jpg",
    "didarganj":     "File:Didarganj Yakshi full length front.jpg",
    "gandhara":      "File:Standing Buddha, Gandhara, c. 2nd-3rd century AD, gray schist - Matsuoka Museum of Art - Tokyo, Japan - DSC07105.JPG",
    "ajanta":        "File:Ajanta Cave1 Padmapani.jpg",
    "nataraja":      "File:Shiva as the Lord of Dance LACMA edit.jpg",
    "konark":        "File:Chariot wheel, Konârak 01.jpg",
    "mughal":        "File:Bichitr - Jahangir Preferring a Sufi Shaikh to Kings, from the St. Petersburg album - Google Art Project.jpg",
    "kangra":        "File:Companion Persuading Radha as Krishna Flutes, Folio from the 'Lambagraon' Gita Govinda (Song of the Cowherd) LACMA M.71.49.7.jpg",
    "ravi-varma":    "File:Raja Ravi Varma, There Comes Papa (1893).jpg",
    "bharat-mata":   "File:Bharat Mata by Abanindranath Tagore.jpg",
    "sher-gil":      "File:Amrita Sger-Gil Bride's Toilet.jpg",
    "nandalal-bose": "File:Fresco by Nandalal Bose - Dinantika - Ashram Complex - Santiniketan 01.jpg",
    # --- map ------------------------------------------------------------
    "madhubani":     "File:Madhubani painting by Bhuvana Meenakshi.jpg",
    "warli":         "File:Warli painting.jpg",
    "gond":          "File:Gond Painting.JPG",
    "phad":          "File:Pabuji ki phad.jpg",
    "cheriyal":      "File:Cheriyal painting - toddy tappers.jpg",
    "bhil":          "File:Pithora art form.jpg",
    "saura":         "File:Saura painting of Odisha DSCN1052 05.jpg",
    "pahari-kangra": "File:Raja Mednipal of Basohli smoking huqqa.jpg",
    "mughal-delhi":  "File:AbulFazlPresentingAkbarnama.jpg",
    "bikaner":       "File:Ragini Bilawal, 1700 CE, Bikaner Kalam of Rajasthani School of Art, State Museum, Lucknow.jpg",
    "kalamkari":     "File:Kalamkari painting.jpg",
    "pattachitra":   "File:Mathura Vijay - Pattachitra of Odisha.jpg",
    "tanjore":       "File:Thanjavur Painting.jpg",
    "mysore":        "File:Cheluvarayaswamy.jpg",
    "kalighat":      "File:Radha- Krishna, Kalighat Painting.jpg",
}


def strip_html(text):
    """extmetadata Artist/Credit fields arrive as HTML; flatten to plain text."""
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = text.replace("&amp;", "&").replace("&nbsp;", " ").replace("&quot;", '"')
    return re.sub(r"\s+", " ", text).strip(" ,;|") or "Unknown"


def resolve(title):
    """Look up one File: title and return its licence, author and 1200px URL."""
    data = api_get({
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size|mime",
        "iiurlwidth": 1200,          # Commons renders the scaled copy for us
    })
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        return None
    page = next(iter(pages.values()))
    if "missing" in page or "imageinfo" not in page:
        return None
    info = page["imageinfo"][0]
    meta = info.get("extmetadata", {})
    return {
        "commons_title": page["title"],
        "licence": meta.get("LicenseShortName", {}).get("value", "?"),
        "author": strip_html(meta.get("Artist", {}).get("value", "")),
        "source": info["descriptionurl"],
        # thumburl is the resized copy; fall back to the original if absent
        "download": info.get("thumburl") or info["url"],
        "width": info.get("thumbwidth") or info.get("width"),
    }


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = resp.read()
    with open(dest, "wb") as fh:
        fh.write(data)
    return len(data)


def main():
    os.makedirs(IMAGES, exist_ok=True)

    # With no arguments we fetch everything; with arguments we refresh only
    # those ids and merge them into the existing manifest.
    wanted = set(sys.argv[1:])
    manifest, failures = {}, []
    if wanted and os.path.exists(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as fh:
            manifest = json.load(fh)

    for key, title in PICKS.items():
        if wanted and key not in wanted:
            continue
        print(f"-> {key}")
        meta = resolve(title)
        if not meta:
            print("   !! could not resolve; will need a placeholder")
            failures.append((key, "not found"))
            time.sleep(3)
            continue

        if not licence_ok(meta["licence"]):
            print(f"   !! licence rejected: {meta['licence']}")
            failures.append((key, f"licence {meta['licence']}"))
            time.sleep(3)
            continue

        # Keep the original extension so the browser gets a type it knows.
        ext = os.path.splitext(meta["download"].split("?")[0])[1].lower()
        if ext not in (".jpg", ".jpeg", ".png", ".webp"):
            ext = ".jpg"
        filename = f"{key}{ext}"

        try:
            size = download(meta["download"], os.path.join(IMAGES, filename))
        except Exception as exc:                              # noqa: BLE001
            print(f"   !! download failed: {exc}")
            failures.append((key, "download failed"))
            time.sleep(3)
            continue

        meta["file"] = f"images/{filename}"
        meta["bytes"] = size
        manifest[key] = meta
        print(f"   ok  {meta['licence']:<16} {meta['width']}px  {size // 1024}KB  -> {filename}")
        time.sleep(2)                                         # stay under the rate limit

    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False, sort_keys=True)

    print(f"\nresolved {len(manifest)}/{len(PICKS)}")
    if failures:
        print("FAILURES (need placeholders):")
        for key, why in failures:
            print(f"  - {key}: {why}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Download the report's photographs from Wikimedia Commons.

Reuses resolve()/download() from ../assignment-1-and-2/scripts/fetch_images.py,
which check that each file is public-domain or Creative Commons and fetch a
1200px copy. Every title below came from a real Commons search.

Writes images/*.jpg and images/manifest.json (author, licence, source URL).

Usage:  python3 scripts/fetch_images.py
"""

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "..", "assignment-1-and-2", "scripts"))
from fetch_images import download, licence_ok, resolve   # noqa: E402

PICKS = {
    "penance-full":    "File:Descent of the Ganges 01.jpg",
    "penance-ascetic": "File:Bhagiratha Yoga Arjuna Penance Mahabalipuram Sep22 A7C 02492.jpg",
    "penance-cat":     "File:Cat Yoga Arjuna Penance Mahabalipuram Sep22 A7C 02493.jpg",
    "penance-nagas":   "File:Cleft Low Half Descent Ganges Mahabalipuram Sep22 A7C 02497.jpg",
    "rathas-group":    "File:Mahabalipuram-Pancha Rathas-Arjuna's Ratha-Bhima's Ratha-Dharmaraja Ratha-Draupadi's Ratha-Nandi-WUS01873.jpg",
    "ratha-bhima":     "File:Mahabalipuram, Pancha Rathas, India.jpg",
    "ratha-dharmaraja": "File:Dharmaraja Ratha SE Mahabalipuram Sep22 A7C 02542.jpg",
    "ratha-nakula":    "File:Mahabalipuram-Pancha Rathas-Arjuna's Ratha-Nakula Sahadeva Ratha-Elephant sculpture-WUS01898.jpg",
}


def main():
    images = os.path.join(HERE, "images")
    os.makedirs(images, exist_ok=True)
    manifest = {}
    for key, title in PICKS.items():
        for attempt in range(4):
            meta = resolve(title)
            if meta:
                break
            time.sleep(10 * (attempt + 1))
        if not meta or not licence_ok(meta["licence"]):
            sys.exit(f"!! {key}: could not resolve or licence not allowed")
        dest = os.path.join(images, f"{key}.jpg")
        size = download(meta["download"], dest)
        meta.update(file=f"images/{key}.jpg", bytes=size)
        manifest[key] = meta
        print(f"ok  {key:<17} {meta['licence']:<14} {meta['author'][:40]}  {size // 1024}KB")
        time.sleep(3)
    with open(os.path.join(images, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    main()

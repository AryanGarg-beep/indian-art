#!/usr/bin/env python3
"""
Stage A of image sourcing: search Wikimedia Commons for candidate images.

We never guess filenames -- a guessed title returns "missing" from the API.
So for every entry we run a real search, print the candidates with their
licence, and a human picks the best one. The picks are then pinned in
scripts/picks.py and downloaded by scripts/fetch_images.py.

Usage:  python3 scripts/search_candidates.py [only_this_id ...]
"""

import json
import sys
import time
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "IndianArtCollegeProject/1.0 (college art-history assignment; contact: student)"

# Licences we are allowed to use: public domain or any Creative Commons licence.
# Anything else (e.g. GODL-India, fair use) is rejected.
ALLOWED_PREFIXES = ("cc", "public domain", "pd")


def api_get(params, attempts=4):
    """GET the Commons API with retries -- it throttles under tight loops."""
    qs = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{API}?{qs}", headers={"User-Agent": UA})
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8").strip()
            if raw:
                return json.loads(raw)
        except Exception as exc:                      # noqa: BLE001
            print(f"      (retry {attempt + 1}: {exc})", file=sys.stderr)
        time.sleep(2 + attempt * 2)                   # back off before retrying
    return {}


def licence_ok(licence):
    low = licence.lower()
    return any(low.startswith(p) for p in ALLOWED_PREFIXES)


def search(query, limit=6):
    """Return [(title, licence, author), ...] candidates for a search string."""
    data = api_get({
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrnamespace": 6,          # namespace 6 == File:
        "gsrlimit": limit,
        "gsrsearch": query,
        "prop": "imageinfo",
        "iiprop": "extmetadata|size|mime",
    })
    pages = data.get("query", {}).get("pages", {})
    out = []
    for page in pages.values():
        info = page.get("imageinfo", [{}])[0]
        meta = info.get("extmetadata", {})
        out.append((
            page["title"],
            meta.get("LicenseShortName", {}).get("value", "?"),
            meta.get("Artist", {}).get("value", "?")[:60],
            info.get("mime", "?"),
        ))
    return out


# (id, human-readable label, search query)
QUERIES = [
    # --- timeline -------------------------------------------------------
    ("bhimbetka",     "Bhimbetka rock paintings",   "Bhimbetka rock painting shelter"),
    ("dancing-girl",  "Dancing Girl",               "Dancing girl Mohenjo-daro bronze"),
    ("pashupati",     "Pashupati seal",             "Pashupati seal Mohenjo-daro"),
    ("lion-capital",  "Lion Capital of Ashoka",     "Lion Capital of Ashoka Sarnath Museum"),
    ("didarganj",     "Didarganj Yakshi",           "Didarganj Yakshi Patna Museum"),
    ("gandhara",      "Gandhara Buddha",            "Gandhara standing Buddha schist"),
    ("ajanta",        "Ajanta cave murals",         "Ajanta cave 1 painting Padmapani"),
    ("nataraja",      "Nataraja Chola bronze",      "Nataraja Chola bronze museum"),
    ("konark",        "Konark Sun Temple wheel",    "Konark Sun Temple chariot wheel"),
    ("mughal",        "Jahangir / Bichitr",         "Bichitr Jahangir Preferring Sufi Shaikh"),
    ("kangra",        "Kangra painting",            "Kangra painting Gita Govinda"),
    ("ravi-varma",    "Raja Ravi Varma",            "Raja Ravi Varma oil painting lady"),
    ("bharat-mata",   "Bharat Mata",                "Bharat Mata Abanindranath Tagore"),
    ("sher-gil",      "Amrita Sher-Gil",            "Amrita Sher-Gil painting Bride"),
    ("nandalal-bose", "Nandalal Bose fresco",       "Nandalal Bose fresco Santiniketan"),
    # --- map ------------------------------------------------------------
    ("madhubani",     "Madhubani",                  "Madhubani Mithila painting Bihar"),
    ("warli",         "Warli",                      "Warli painting tribal Maharashtra"),
    ("gond",          "Gond",                       "Gond painting Jangarh Madhya Pradesh"),
    ("phad",          "Phad",                       "Phad painting Pabuji scroll Rajasthan"),
    ("cheriyal",      "Cheriyal scroll",            "Cheriyal scroll painting Telangana"),
    ("bhil",          "Bhil / Pithora",             "Pithora painting Bhil Rathwa"),
    ("saura",         "Saura",                      "Saura painting Odisha tribal"),
    ("pahari-kangra", "Pahari / Kangra (map pin)",  "Pahari painting Basohli Kangra hill"),
    ("mughal-delhi",  "Mughal miniature (map pin)", "Mughal miniature painting Akbarnama"),
    ("bikaner",       "Bikaner miniature",          "Bikaner miniature painting Rajasthan"),
    ("kalamkari",     "Kalamkari",                  "Kalamkari Srikalahasti painting cloth"),
    ("pattachitra",   "Pattachitra",                "Pattachitra Odisha painting Raghurajpur"),
    ("tanjore",       "Thanjavur painting",         "Thanjavur painting gold gesso"),
    ("mysore",        "Mysore painting",            "Mysore traditional painting Karnataka"),
    ("kalighat",      "Kalighat painting",          "Kalighat painting Calcutta pat"),
]


def main():
    wanted = set(sys.argv[1:])
    for key, label, query in QUERIES:
        if wanted and key not in wanted:
            continue
        print(f"\n=== {key}  ({label})")
        print(f"    query: {query}")
        results = search(query)
        if not results:
            print("    !! NO RESULTS / throttled")
        for title, lic, author, mime in results:
            flag = "OK " if licence_ok(lic) else "REJ"
            print(f"    [{flag}] {lic:<18} {mime:<12} {title}")
            print(f"           by {author}")
        time.sleep(1.5)                                # be polite to the API


if __name__ == "__main__":
    main()

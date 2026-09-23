/* ===================================================================
   ART MAP  —  Assignment 2
   ===================================================================

   Reads CATEGORIES and LOCATIONS from data/locations.js and builds:

     1. a Leaflet map centred on India with OpenStreetMap tiles
     2. one colour-coded marker per art form
     3. a legend that doubles as a category filter
     4. a search box matching name, state and artists

   Leaflet is loaded from a CDN in map.html, so this page needs an
   internet connection (the map tiles come from the network too).
   =================================================================== */

(function () {
  "use strict";

  var legendEl = document.getElementById("legend");
  var searchEl = document.getElementById("search");
  var noteEl   = document.getElementById("result-note");

  /* ---------------------------------------------------------------
     Guard: if Leaflet did not load, say so instead of failing silently.
     --------------------------------------------------------------- */
  if (typeof L === "undefined") {
    document.getElementById("map").innerHTML =
      '<p style="padding:1.5rem">The map library could not be loaded. ' +
      'This page needs an internet connection for Leaflet and the map tiles.</p>';
    return;
  }

  /* ---------------------------------------------------------------
     State
     --------------------------------------------------------------- */
  // Every category starts switched on.
  var activeCats = {};
  CATEGORIES.forEach(function (c) { activeCats[c.id] = true; });

  var searchTerm = "";
  var markers = {};   // id -> Leaflet marker

  /** Look up a category record by id, with a safe fallback. */
  function catById(id) {
    for (var i = 0; i < CATEGORIES.length; i++) {
      if (CATEGORIES[i].id === id) return CATEGORIES[i];
    }
    return { id: id, label: id, color: "#777" };
  }

  /* ---------------------------------------------------------------
     1. The map
     --------------------------------------------------------------- */
  var map = L.map("map", {
    center: [22.5, 80.0],   // roughly the centre of India
    zoom: 5,
    scrollWheelZoom: true
  });

  /* ---------------------------------------------------------------
     Tile provider.

     OpenStreetMap's tiles are served by volunteers, and their usage
     policy asks that sites do not make bulk or automated requests:
     https://operations.osmfoundation.org/policies/tiles/
     A normal visitor browsing this site is well within that policy.
     But if the servers are ever busy or your address gets rate
     limited, OSM returns a grey "Access blocked" tile instead of the
     map. If that happens, switch TILES to "esri" below -- one word,
     no other change needed.
     --------------------------------------------------------------- */
  var TILES = "osm";        // "osm" (default) or "esri"

  var TILE_PROVIDERS = {
    osm: {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      options: {
        maxZoom: 18,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }
    },
    esri: {
      url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
      options: {
        maxZoom: 18,
        attribution: 'Tiles &copy; Esri &mdash; map data &copy; OpenStreetMap contributors'
      }
    }
  };

  var provider = TILE_PROVIDERS[TILES] || TILE_PROVIDERS.osm;
  var tileLayer = L.tileLayer(provider.url, provider.options).addTo(map);

  /* If tiles fail to load, say so plainly rather than leaving the user
     looking at blank or "Access blocked" squares with no explanation. */
  var tileErrors = 0;
  tileLayer.on("tileerror", function () {
    tileErrors++;
    if (tileErrors === 4 && !document.getElementById("tile-warning")) {
      var warn = document.createElement("p");
      warn.id = "tile-warning";
      warn.className = "result-note";
      warn.setAttribute("role", "status");
      warn.textContent =
        "The background map tiles could not be loaded (no internet " +
        "connection, or the tile server is refusing requests). The pins, " +
        "filters and search all still work. See README.md for how to " +
        "switch tile provider.";
      noteEl.parentNode.insertBefore(warn, noteEl.nextSibling);
    }
  });

  /* ---------------------------------------------------------------
     2. Markers
     --------------------------------------------------------------- */

  /* ---------------------------------------------------------------
     The detail panel.

     Leaflet popups are drawn inside the map container, so a long entry
     gets clipped at the edge of the map. This panel lives outside the
     map in the page, so it can be as tall as it needs and scrolls on
     its own.
     --------------------------------------------------------------- */
  var panel      = document.getElementById("detail-panel");
  var panelClose = document.getElementById("detail-close");
  var lastMarkerEl = null;     // element to restore focus to on close
  var openLocationId = null;   // which art form the panel is showing

  /** Fill the panel with one art form and slide it open. */
  function openPanel(loc, markerEl) {
    var cat = catById(loc.category);

    var img = document.getElementById("detail-image");
    img.src = loc.image;
    img.alt = loc.alt;

    var badge = document.getElementById("detail-cat");
    badge.textContent = cat.label;
    badge.style.background = cat.color;

    // textContent (not innerHTML) means the data can never inject markup.
    document.getElementById("detail-name").textContent      = loc.name;
    document.getElementById("detail-region").textContent    = loc.state;
    document.getElementById("detail-era").textContent       = loc.era;
    document.getElementById("detail-artists").textContent   = loc.artists;
    document.getElementById("detail-works").textContent     = loc.works;
    document.getElementById("detail-technique").textContent = loc.technique;
    document.getElementById("detail-context").textContent   = loc.context;
    document.getElementById("detail-credit").textContent =
      "Image: “" + loc.credit.title + "” by " + loc.credit.author +
      ", " + loc.credit.licence + ", via Wikimedia Commons.";

    lastMarkerEl = markerEl || null;
    openLocationId = loc.id;
    panel.classList.add("is-open");
    panel.scrollTop = 0;
    panelClose.focus();
  }

  function closePanel() {
    panel.classList.remove("is-open");
    openLocationId = null;
    // Send focus back to the pin that opened it, for keyboard users.
    if (lastMarkerEl && document.contains(lastMarkerEl)) lastMarkerEl.focus();
  }

  panelClose.addEventListener("click", closePanel);

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && panel.classList.contains("is-open")) closePanel();
  });

  LOCATIONS.forEach(function (loc) {
    var cat = catById(loc.category);

    // A divIcon is a plain styled <div>, so the colour comes from our CSS
    // palette rather than from a set of image sprites.
    var icon = L.divIcon({
      className: "",                       // suppress Leaflet's default class
      html: '<div class="pin" style="background:' + cat.color + '"></div>',
      iconSize: [20, 20],
      iconAnchor: [10, 10],
      popupAnchor: [0, -10]
    });

    var marker = L.marker([loc.lat, loc.lon], {
      icon: icon,
      title: loc.name,                     // native tooltip + accessible name
      alt: loc.name + ", " + loc.state,
      riseOnHover: true
    });

    // Leaflet fires "click" for a mouse click and for Enter on a focused
    // marker, so this covers pointer and keyboard users alike.
    marker.on("click", function () {
      openPanel(loc, marker.getElement());
    });

    markers[loc.id] = marker;
  });

  /* ---------------------------------------------------------------
     3. Legend / category filter
     --------------------------------------------------------------- */
  function buildLegend() {
    CATEGORIES.forEach(function (cat) {
      var total = LOCATIONS.filter(function (l) {
        return l.category === cat.id;
      }).length;

      var li = document.createElement("li");
      var btn = document.createElement("button");
      btn.type = "button";
      btn.setAttribute("aria-pressed", "true");
      btn.innerHTML =
        '<span class="swatch" style="background:' + cat.color + '"></span>' +
        '<span class="legend-label"></span>' +
        '<span class="count">' + total + '</span>';
      btn.querySelector(".legend-label").textContent = cat.label;

      btn.addEventListener("click", function () {
        activeCats[cat.id] = !activeCats[cat.id];
        btn.setAttribute("aria-pressed", activeCats[cat.id] ? "true" : "false");
        refresh();
      });

      li.appendChild(btn);
      legendEl.appendChild(li);
    });
  }

  /* ---------------------------------------------------------------
     4. Filtering
     --------------------------------------------------------------- */

  /** True when a location passes BOTH the category filter and the search. */
  function matches(loc) {
    if (!activeCats[loc.category]) return false;
    if (searchTerm === "") return true;

    var haystack = (
      loc.name + " " + loc.state + " " + loc.artists + " " +
      loc.works + " " + catById(loc.category).label
    ).toLowerCase();

    return haystack.indexOf(searchTerm) !== -1;
  }

  /** Add or remove markers so the map reflects the current filters. */
  function refresh() {
    var shown = 0;

    LOCATIONS.forEach(function (loc) {
      var marker = markers[loc.id];
      var keep = matches(loc);

      if (keep) {
        if (!map.hasLayer(marker)) marker.addTo(map);
        shown++;
      } else {
        // If a filter hides the pin whose details are open, close the
        // panel too -- otherwise it would describe a pin you can no
        // longer see on the map.
        if (openLocationId === loc.id) closePanel();
        if (map.hasLayer(marker)) map.removeLayer(marker);
      }
    });

    noteEl.textContent = shown === LOCATIONS.length
      ? "Showing all " + LOCATIONS.length + " art forms."
      : "Showing " + shown + " of " + LOCATIONS.length + " art forms.";
  }

  searchEl.addEventListener("input", function () {
    searchTerm = searchEl.value.trim().toLowerCase();
    refresh();
  });

  /* ---------------------------------------------------------------
     5. Start
     --------------------------------------------------------------- */
  buildLegend();
  refresh();
})();

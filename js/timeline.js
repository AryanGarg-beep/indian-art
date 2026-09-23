/* ===================================================================
   TIMELINE  —  Assignment 1
   ===================================================================

   Reads ERAS and ARTIFACTS from data/artifacts.js (loaded by the
   <script> tag above this one in timeline.html) and builds:

     1. an era filter bar
     2. a horizontally scrolling rail of artifact nodes
     3. a modal detail view with prev/next and keyboard navigation

   Written in plain ES5-style JavaScript with no libraries so every
   line can be explained in a viva.
   =================================================================== */

(function () {
  "use strict";

  /* ---------------------------------------------------------------
     Element references
     --------------------------------------------------------------- */
  var track      = document.getElementById("timeline-track");
  var scroller   = document.getElementById("timeline-scroll");
  var filterBar  = document.getElementById("era-filter");
  var resultNote = document.getElementById("result-note");

  var backdrop = document.getElementById("modal-backdrop");
  var modal    = document.getElementById("modal");
  var elClose  = document.getElementById("modal-close");
  var elPrev   = document.getElementById("modal-prev");
  var elNext   = document.getElementById("modal-next");

  /* ---------------------------------------------------------------
     State
     --------------------------------------------------------------- */

  // Artifacts sorted oldest first. slice() copies the array so we never
  // reorder the original data.
  var ordered = ARTIFACTS.slice().sort(function (a, b) {
    return a.dateSort - b.dateSort;
  });

  var activeEra = "all";   // current filter
  var visible = [];        // artifacts currently shown, in display order
  var openIndex = -1;      // index into `visible` of the open artifact
  var lastFocused = null;  // element to restore focus to when the modal closes

  /* ---------------------------------------------------------------
     Helpers
     --------------------------------------------------------------- */

  /** Look up an era record by id. Returns a safe fallback if missing. */
  function eraById(id) {
    for (var i = 0; i < ERAS.length; i++) {
      if (ERAS[i].id === id) return ERAS[i];
    }
    return { id: id, label: id, span: "" };
  }

  /* ---------------------------------------------------------------
     1. Build the era filter bar
     --------------------------------------------------------------- */
  function buildFilter() {
    // "All eras" first, then one button per era that actually has artifacts.
    var options = [{ id: "all", label: "All eras" }];

    ERAS.forEach(function (era) {
      var used = ordered.some(function (a) { return a.era === era.id; });
      if (used) options.push({ id: era.id, label: era.label });
    });

    options.forEach(function (opt) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chip";
      btn.textContent = opt.label;
      btn.setAttribute("aria-pressed", opt.id === activeEra ? "true" : "false");
      btn.addEventListener("click", function () {
        activeEra = opt.id;
        // Update the pressed state on every chip, then redraw the rail.
        var chips = filterBar.querySelectorAll(".chip");
        for (var i = 0; i < chips.length; i++) {
          chips[i].setAttribute("aria-pressed", chips[i] === btn ? "true" : "false");
        }
        render();
      });
      filterBar.appendChild(btn);
    });
  }

  /* ---------------------------------------------------------------
     2. Build the timeline rail
     --------------------------------------------------------------- */
  function render() {
    track.innerHTML = "";

    // Apply the era filter.
    visible = ordered.filter(function (a) {
      return activeEra === "all" || a.era === activeEra;
    });

    var currentEra = null;

    visible.forEach(function (artifact, index) {
      // Insert an era band label whenever the era changes.
      if (artifact.era !== currentEra) {
        currentEra = artifact.era;
        var era = eraById(currentEra);

        var band = document.createElement("div");
        band.className = "era-band";
        band.innerHTML =
          '<span class="era-name"></span><span class="era-span"></span>';
        band.querySelector(".era-name").textContent = era.label;
        band.querySelector(".era-span").textContent = era.span;
        track.appendChild(band);
      }

      // The artifact node is a <button> so it is focusable and
      // keyboard-operable for free.
      var node = document.createElement("button");
      node.type = "button";
      node.className = "node";
      node.dataset.index = String(index);
      node.setAttribute("aria-haspopup", "dialog");

      var img = document.createElement("img");
      img.className = "node-thumb";
      img.src = artifact.image;
      img.alt = "";              // decorative here; the title below carries the name
      img.loading = "lazy";

      var dot = document.createElement("span");
      dot.className = "node-dot";

      var title = document.createElement("span");
      title.className = "node-title";
      title.textContent = artifact.title;

      var date = document.createElement("span");
      date.className = "node-date";
      date.textContent = artifact.dateDisplay;

      node.appendChild(img);
      node.appendChild(dot);
      node.appendChild(title);
      node.appendChild(date);

      node.addEventListener("click", function () { openModal(index); });
      track.appendChild(node);
    });

    resultNote.textContent =
      "Showing " + visible.length + " of " + ordered.length + " artifacts.";

    scroller.scrollLeft = 0;
  }

  /* ---------------------------------------------------------------
     3. The modal detail view
     --------------------------------------------------------------- */

  /** Fill the modal with one artifact and show it. */
  function openModal(index) {
    if (index < 0 || index >= visible.length) return;
    openIndex = index;
    var a = visible[index];

    document.getElementById("modal-image").src = a.image;
    document.getElementById("modal-image").alt = a.alt;
    document.getElementById("modal-era").textContent = eraById(a.era).label;
    document.getElementById("modal-title").textContent = a.title;
    document.getElementById("modal-date").textContent = a.dateDisplay;
    document.getElementById("modal-region").textContent = a.region;
    document.getElementById("modal-medium").textContent = a.medium;
    document.getElementById("modal-attribution").textContent = a.attribution;
    document.getElementById("modal-context").textContent = a.context;
    document.getElementById("modal-why").textContent = a.whyItMatters;
    // Put the artifact id in the address bar so the view can be linked to.
    history.replaceState(null, "", "#" + a.id);

    document.getElementById("modal-credit").textContent =
      "Image: “" + a.credit.title + "” by " + a.credit.author +
      ", " + a.credit.licence + ", via Wikimedia Commons.";

    // Prev/next wrap around, so they are never disabled.
    elPrev.textContent = "‹ " + visible[(index - 1 + visible.length) % visible.length].title;
    elNext.textContent = visible[(index + 1) % visible.length].title + " ›";

    // Remember what had focus, but only when opening fresh -- stepping
    // prev/next must not overwrite it with the modal's own buttons.
    if (backdrop.hidden) lastFocused = document.activeElement;

    backdrop.hidden = false;
    modal.scrollTop = 0;
    elClose.focus();
  }

  function closeModal() {
    backdrop.hidden = true;
    openIndex = -1;
    // Drop the #id from the address bar without adding a history entry.
    if (window.location.hash) {
      history.replaceState(null, "", window.location.pathname + window.location.search);
    }
    // Return focus to the node that opened the modal (accessibility).
    if (lastFocused && document.contains(lastFocused)) lastFocused.focus();
  }

  /** Open whichever artifact the URL hash names, e.g. timeline.html#nataraja */
  function openFromHash() {
    var wanted = window.location.hash.replace(/^#/, "");
    if (!wanted) return;
    for (var i = 0; i < visible.length; i++) {
      if (visible[i].id === wanted) { openModal(i); return; }
    }
  }

  /** Move to the previous/next artifact, wrapping at both ends. */
  function step(delta) {
    if (openIndex < 0 || visible.length === 0) return;

    // If the user clicked Prev/Next, leave focus on that button so they
    // can click through the sequence without the focus jumping away.
    var wasOnNav = document.activeElement === elPrev || document.activeElement === elNext;
    var navButton = document.activeElement;

    openModal((openIndex + delta + visible.length) % visible.length);

    if (wasOnNav) navButton.focus();
  }

  /* ---------------------------------------------------------------
     4. Events
     --------------------------------------------------------------- */
  elClose.addEventListener("click", closeModal);
  elPrev.addEventListener("click", function () { step(-1); });
  elNext.addEventListener("click", function () { step(1); });

  // Clicking the dark area outside the dialog closes it.
  backdrop.addEventListener("click", function (event) {
    if (event.target === backdrop) closeModal();
  });

  document.addEventListener("keydown", function (event) {
    if (!backdrop.hidden) {
      // ---- modal is open ----
      if (event.key === "Escape") { closeModal(); return; }
      if (event.key === "ArrowLeft")  { event.preventDefault(); step(-1); return; }
      if (event.key === "ArrowRight") { event.preventDefault(); step(1);  return; }

      // Focus trap: keep Tab inside the dialog while it is open.
      if (event.key === "Tab") {
        var focusable = modal.querySelectorAll(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        if (focusable.length === 0) return;
        var first = focusable[0];
        var last  = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault(); last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault(); first.focus();
        }
      }
      return;
    }

    // ---- modal is closed: arrow keys walk the rail ----
    // Only when focus is on a node or on the scroll region itself, so we
    // do not hijack arrow keys inside the filter bar.
    var active = document.activeElement;
    var onNode = active && active.classList && active.classList.contains("node");
    var onRail = active === scroller;
    if (!onNode && !onRail) return;

    if (event.key === "ArrowRight" || event.key === "ArrowLeft") {
      event.preventDefault();
      var nodes = track.querySelectorAll(".node");
      if (nodes.length === 0) return;

      var current = onNode ? parseInt(active.dataset.index, 10) : -1;
      var delta = event.key === "ArrowRight" ? 1 : -1;
      var nextIndex = current < 0
        ? (delta === 1 ? 0 : nodes.length - 1)
        : (current + delta + nodes.length) % nodes.length;

      nodes[nextIndex].focus();
      // Keep the focused node comfortably in view.
      nodes[nextIndex].scrollIntoView({ block: "nearest", inline: "center" });
    }

    // Enter/Space on a focused node is handled natively by <button>.
  });

  /* ---------------------------------------------------------------
     5. Start
     --------------------------------------------------------------- */
  buildFilter();
  render();
  openFromHash();          // support links like timeline.html#nataraja
})();

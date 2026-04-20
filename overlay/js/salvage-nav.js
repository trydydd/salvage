/**
 * salvage-nav.js — Salvage Electronics sidebar section navigation
 *
 * Appends a Sections block to the sidebar using the header vol-nav links.
 * Runs after navigation.js (both are deferred; order follows document order).
 *
 * Also re-enables the sidebar toggle on pages where navigation.js would
 * suppress it (no h2 headings, no Kuphaldt chapter links) — the index page
 * being the main case — so the Sections block remains accessible.
 */
(function () {
  'use strict';

  var SIDEBAR_ID   = 'oc-sidebar';
  var TOGGLE_ID    = 'oc-nav-toggle';
  var SCRIM_ID     = 'oc-sidebar-scrim';
  var MOBILE_BREAK = 769;

  function addSectionNav() {
    var sidebar = document.getElementById(SIDEBAR_ID);
    if (!sidebar) return;

    /* Collect only the salvage section links (have data-section); skip Theory */
    var sectionLinks = document.querySelectorAll('.oc-vol-nav a[data-section]');
    if (!sectionLinks.length) return;

    var nav = document.createElement('nav');
    nav.className = 'oc-vollist';
    nav.setAttribute('aria-label', 'Sections');

    var html = '<p class="oc-toc__heading">Sections</p><ol class="oc-toc__list">';
    for (var i = 0; i < sectionLinks.length; i++) {
      var link     = sectionLinks[i];
      var isActive = link.classList.contains('is-active') ? ' is-active' : '';
      html += '<li class="oc-toc__item">';
      html += '<a class="oc-toc__link' + isActive + '" href="' +
              link.getAttribute('href') + '">' +
              link.textContent.trim() + '</a>';
      html += '</li>';
    }
    html += '</ol>';
    nav.innerHTML = html;
    sidebar.appendChild(nav);

    /* If navigation.js hid the toggle (page had no usable TOC content),
       re-enable it and wire up open/close so the Sections block is reachable. */
    var toggle = document.getElementById(TOGGLE_ID);
    if (!toggle || !toggle.hidden) return;

    toggle.hidden = false;

    var scrim = document.getElementById(SCRIM_ID);
    if (!scrim) {
      scrim = document.createElement('div');
      scrim.id        = SCRIM_ID;
      scrim.className = 'oc-sidebar-scrim';
      scrim.setAttribute('aria-hidden', 'true');
      document.body.appendChild(scrim);
    }

    function setOpen(open) {
      document.body.classList.toggle('sidebar-closed', !open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    setOpen(window.matchMedia('(min-width: ' + MOBILE_BREAK + 'px)').matches);

    toggle.addEventListener('click', function () {
      setOpen(document.body.classList.contains('sidebar-closed'));
    });

    scrim.addEventListener('click', function () { setOpen(false); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addSectionNav);
  } else {
    addSectionNav();
  }
})();

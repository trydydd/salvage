# Salvage Electronics — Claude Context

## Project

A portable web guide to salvaging useful electronic components from discarded
consumer devices. The site builds original Markdown content into static HTML for
self-hosted and offline use as part of the Hearth project. Salvage Electronics
is licensed under **CC BY-SA 4.0** and depends on shared Open Circuits design
assets (CSS, fonts, JS) that are pulled at build time under **CC BY 4.0**.

## Key Constraints

- **No CDN dependencies** — all runtime assets must ship in the build output.
- **Shared assets are build-time dependencies** — CSS, fonts, and navigation JS
  come from Open Circuits releases via `build/fetch_shared.py`.
- **Stable URL paths are a contract** — `/salvage/...` paths must remain stable;
  see `docs/HEARTH-INTEGRATION.md`.
- **Theory cross-links are hyperlinks only** — use absolute `/open-circuits/...`
  paths; do not copy Open Circuits theory text into Salvage content.
- **Hazard banners use standard safety colors** — they intentionally do not use
  the Open Circuits accent palette.

## Stack

- **Python 3.10+** build pipeline
- **mistune** for Markdown rendering
- **Jinja2** for templating
- **PyYAML** for frontmatter parsing
- No JS framework — shared navigation uses vanilla JS only

## Build Commands

```bash
make install    # create venv + install deps
make fetch      # pull shared Open Circuits assets
make build      # render Markdown to output/html/
make test       # run pytest
```

## Key Files

- `build/build.py` — Markdown-to-HTML build pipeline
- `build/fetch_shared.py` — fetches pinned shared assets from Open Circuits releases
- `templates/page.html` — base Jinja template for every page
- `templates/partials/header.html` — section navigation and Theory link
- `templates/partials/footer.html` — license, attribution, and Open Circuits credit
- `templates/partials/hazard-banner.html` — donor-guide hazard callout
- `overlay/css/salvage.css` — Salvage-specific styles layered over shared CSS
- `docs/HEARTH-INTEGRATION.md` — path stability and deployment contract
- `docs/STYLE-GUIDE.md` — writing rules and table conventions
- `docs/HAZARD-SYSTEM.md` — hazard rating meanings, usage, and accessibility rules

## Content Conventions

### Frontmatter

Every content page uses YAML frontmatter at the top:

```yaml
---
title: "Page Title"
section: "foundations"
hazard: 3
hazard_summary: "One-line summary of the primary hazard."
---
```

- `title` is required.
- `section` is one of `foundations`, `donor-guides`, `components`, `projects`.
- `hazard` is `1`-`4` or omitted/null.
- `hazard_summary` is the one-line worst-case warning for donor pages.

### Theory cross-references

Use absolute Open Circuits paths such as:

- `/open-circuits/DC/DC_5.html`
- `/open-circuits/Semi/SEMI_6.html`
- `/open-circuits/Exper/EXPER_1.html`

Keep these as short inline hyperlinks only.

### Component tables

Donor guides use the four-column table format:

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Example part | Board location | What the reader can measure | ★★★ |

Prefer measurable details: voltage rating, polarity, package, connector type,
and similar field-usable information.

---

## Design Context

### Users
Everyone — regardless of technical background, device quality, or economic
context. Users might be sitting at a workbench with a cheap Android phone,
reading on a secondhand laptop in low light, or studying on a proper desktop.
The interface must respect all of them equally.

Primary job to be done: read a guide, look up a part, follow a salvage or test
procedure. Deep focus, sustained reading, technical lookup.

### Brand Personality
**Tactile · generous · honest**

Warm and workshop-y — feels like a well-used repair manual or technical zine.
Made by hands, for hands. Inviting and a little rough around the edges. Cares
about the reader without performing that care. The content is the point; the
interface is in service of it.

### Aesthetic Direction
- **Theme:** Light default with automatic dark mode via `prefers-color-scheme`
- **Palette:** Warm cream/paper tones, deep warm charcoal, copper/amber accent from shared design
- **Typography:** Self-hosted fonts bundled through shared assets; no external font loading
- **Texture:** Subtle warmth through spacing, type, and color temperature — not ornament
- **Hazard system:** Hazard banners use standard safety greens/yellows/oranges/reds for clarity

### Design Principles
1. **Serve the text, not the brand.** The interface disappears into the reading experience.
2. **Dignified utility.** Every element earns its place. Warmth comes from type, color temperature, and rhythm.
3. **Works everywhere.** Cheap phones, bright light, no JavaScript, print-friendly output.
4. **Offline-first aesthetics.** Nothing should imply constant connectivity.
5. **Respect, not condescension.** Assume the reader is smart, capable, and resourceful.

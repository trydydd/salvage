# Salvage Electronics — Implementation Plan

> **Audience:** Claude Code, running in the user's repo workspace.
> **Goal:** Bootstrap a new repo `salvage-electronics` that builds a static
> HTML site, sharing design assets with the existing `open-circuits` repo.
> **Scope:** Repo skeleton, build pipeline, path contract, and stub content
> for every section. Not full content — that's for human authors.

---

## 0. Context You Need

**Read these files from the `open-circuits` repo first.** They establish the
patterns, design language, and integration contract that `salvage-electronics`
inherits:

- `CLAUDE.md` — design context, brand personality, users
- `.impeccable.md` — full design document
- `overlay/css/open-circuits.css` — the design tokens and CSS architecture
- `overlay/brand-guide.md` — colors, typography, tone
- `docs/HEARTH-INTEGRATION.md` — the URL path contract model
- `docs/BUILDING.md` — build documentation style to match

**Key facts:**

- Both repos deploy behind nginx on a Hearth box at stable path prefixes.
  Open Circuits is at `/circuits/`. Salvage Electronics will be at
  `/salvage/`. Cross-links use absolute paths (e.g. `/circuits/Semi/SEMI_6.html`).
- Open Circuits is CC BY 4.0 (Kuphaldt's text). Salvage Electronics is
  original work under CC BY-SA 4.0. Compatible in one direction: we can
  depend on CC BY 4.0 assets; our derivatives must stay CC BY-SA.
- Open Circuits uses a Python build pipeline that wraps Kuphaldt's HTML
  with an overlay. Salvage Electronics has no such upstream — it builds
  original Markdown into HTML via Jinja2 templates.
- Shared visual design: salvage-electronics should look like a section
  of the same reference library, not a separate product. Same fonts,
  same colors, same header/footer style. The only net-new UI is the
  hazard banner.

---

## 0.5. Working Setup

**Both repos are checked out side by side on the local machine.** From the
`salvage/` working directory, the open-circuits repo is
available at `../open-circuits/`.

This means:

- **For reference reads** (design context, CSS architecture, doc structure),
  read files directly from `../open-circuits/`. No need to fetch from
  GitHub.
- **For copying files** noted in Section 2, use direct filesystem copies
  (`cp ../open-circuits/.impeccable.md .`) rather than fetching via URL.
- **For understanding patterns** (Makefile style, build script layout,
  documentation conventions), you have the full source tree available —
  use it generously.

**Build-time fetching is separate.** `build/fetch_shared.py` still pulls a
release tarball from GitHub when the build runs. That's intentional: the
build treats open-circuits as a versioned dependency via its releases,
not as a sibling directory. This keeps the build reproducible on CI and
on Hearth deployments where only one repo is checked out.

If `../open-circuits/` is missing for any reason, stop and report — do not
attempt to guess at the patterns. The design consistency between the two
projects matters, and guessing will drift.

---

## 1. Repository Layout

Create this structure at the top of the new repo:

```
salvage-electronics/
├── .gitignore
├── .impeccable.md                   # COPY from open-circuits/
├── ATTRIBUTION.md                   # WRITE — see section 3
├── CLAUDE.md                        # WRITE — see section 3
├── LICENSE.txt                      # WRITE — CC BY-SA 4.0, section 3
├── Makefile                         # WRITE — section 4
├── README.md                        # WRITE — section 3
├── pyproject.toml                   # WRITE — section 4
├── requirements.txt                 # WRITE — section 4
├── requirements-dev.txt             # WRITE — section 4
│
├── build/
│   ├── build.py                     # WRITE — section 5
│   └── fetch_shared.py              # WRITE — section 5
│
├── overlay/
│   ├── css/
│   │   └── salvage.css              # WRITE — section 6
│   └── icons/
│       ├── hazard-1.svg             # WRITE — section 7
│       ├── hazard-2.svg             # WRITE — section 7
│       ├── hazard-3.svg             # WRITE — section 7
│       └── hazard-4.svg             # WRITE — section 7
│
├── templates/
│   ├── page.html                    # WRITE — section 8
│   └── partials/
│       ├── header.html              # WRITE — section 8
│       ├── footer.html              # WRITE — section 8
│       └── hazard-banner.html       # WRITE — section 8
│
├── content/
│   ├── index.md                     # WRITE — section 9
│   ├── foundations/
│   │   ├── 01-why-salvage.md        # WRITE — section 9
│   │   ├── 02-safety.md             # WRITE — section 9
│   │   ├── 03-tools-and-workspace.md # WRITE — section 9
│   │   └── 04-core-techniques.md    # WRITE — section 9
│   ├── donor-guides/
│   │   ├── _template.md             # WRITE — section 9
│   │   ├── 01-battery-devices.md    # WRITE — section 9
│   │   ├── 02-wall-chargers.md      # WRITE — section 9
│   │   ├── 03-routers-modems.md     # WRITE — section 9
│   │   ├── 04-printers.md           # WRITE — section 9
│   │   ├── 05-desktop-computers.md  # WRITE — section 9
│   │   ├── 06-laptops.md            # WRITE — section 9
│   │   ├── 07-atx-power-supplies.md # WRITE — section 9
│   │   ├── 08-audio-equipment.md    # WRITE — section 9
│   │   ├── 09-led-bulbs.md          # WRITE — section 9
│   │   ├── 10-microwave-ovens.md    # WRITE — section 9
│   │   ├── 11-crt-monitors.md       # WRITE — section 9
│   │   └── 12-ups-units.md          # WRITE — section 9
│   ├── components/
│   │   ├── 01-resistors.md          # WRITE — section 9
│   │   ├── 02-capacitors.md         # WRITE — section 9
│   │   ├── 03-diodes.md             # WRITE — section 9
│   │   ├── 04-transistors-bjt.md    # WRITE — section 9
│   │   ├── 05-mosfets.md            # WRITE — section 9
│   │   ├── 06-voltage-regulators.md # WRITE — section 9
│   │   ├── 07-inductors-transformers.md # WRITE — section 9
│   │   ├── 08-relays.md             # WRITE — section 9
│   │   ├── 09-motors.md             # WRITE — section 9
│   │   └── 10-connectors-switches.md # WRITE — section 9
│   └── projects/
│       ├── 01-continuity-tester.md  # WRITE — section 9
│       ├── 02-cap-discharge-tool.md # WRITE — section 9
│       ├── 03-atx-bench-supply.md   # WRITE — section 9
│       ├── 04-component-tester-jig.md # WRITE — section 9
│       ├── 05-usb-charger.md        # WRITE — section 9
│       └── 06-led-lamp.md           # WRITE — section 9
│
├── docs/
│   ├── BUILDING.md                  # WRITE — section 10
│   ├── HAZARD-SYSTEM.md             # WRITE — section 10
│   ├── HEARTH-INTEGRATION.md        # WRITE — section 10
│   └── STYLE-GUIDE.md               # WRITE — section 10
│
├── shared/                          # Populated by fetch_shared.py (gitignored)
│   └── .gitkeep
│
└── output/                          # Build output (gitignored)
    └── .gitkeep
```

---

## 2. Files to Copy Verbatim from `open-circuits`

**Do not re-write these. Copy them, then make the edits noted.**

| Source (in `open-circuits/`) | Destination (in `salvage-electronics/`) | Edits |
|---|---|---|
| `.impeccable.md` | `.impeccable.md` | None — the design philosophy is shared. |

**Do NOT copy:**
- `overlay/css/open-circuits.css` — pulled at build time via `fetch_shared.py`
- `overlay/js/navigation.js` — pulled at build time
- `overlay/fonts/*.woff2` — pulled at build time
- `overlay/templates/header.html` / `footer.html` — salvage has its own
  (different nav structure)
- `overlay/inject_overlay.py` — not applicable; we don't wrap upstream HTML

The `shared/` directory gets populated by `fetch_shared.py` from a pinned
open-circuits release tarball. That's the contract — we consume releases,
not source files.

---

## 3. Top-level Documents

### `README.md`

Project overview. Follow the structure of `open-circuits/README.md`:
heading, one-sentence description, "What's here" overview of the four
sections (Foundations, Donor Guides, Components, Projects), Philosophy
block (tiered techniques, requirements-not-products, safety), Build
section with `make install / fetch / build / serve / clean`, Architecture
table showing the three-repo setup, License section pointing to LICENSE.txt
and ATTRIBUTION.md.

### `LICENSE.txt`

CC BY-SA 4.0 license text. Match the format of `open-circuits/LICENSE.txt`
but with these substitutions:
- License: CC BY-SA 4.0 (not CC BY 4.0)
- Add "ShareAlike" clause explanation
- Copyright: "Copyright (C) 2026 Hearth Project contributors"
- Include a paragraph at the end noting that shared assets (CSS, fonts, JS)
  pulled at build time from open-circuits remain under CC BY 4.0, and that
  CC BY-SA 4.0 is one-way compatible with CC BY 4.0.
- Canonical URL: https://creativecommons.org/licenses/by-sa/4.0/legalcode

### `ATTRIBUTION.md`

Format-match `open-circuits/ATTRIBUTION.md`. Sections needed:

- **Original Work** — identifies this as original content by the Hearth
  project under CC BY-SA 4.0.
- **Dependencies** — Shared UI Assets (CC BY 4.0 from open-circuits) and
  Theory Cross-References (no text copied; hyperlinks only).
- **CC BY-SA 4.0 Compliance** — bullets on Attribution, License notice,
  Indication of changes, ShareAlike.
- **Modification Log** — empty table at first with just "Initial skeleton".

### `CLAUDE.md`

Follow `open-circuits/CLAUDE.md` structure. Sections:

- **Project** — one-paragraph description; note the CC BY-SA 4.0 license
  and the dependency on open-circuits assets.
- **Key Constraints** — no CDN deps, shared assets pulled at build time,
  URL paths stable by contract (point to `docs/HEARTH-INTEGRATION.md`).
- **Stack** — Python 3.10+, mistune for Markdown, Jinja2 for templating,
  no JS framework.
- **Build Commands** — `make install / fetch / build / test`.
- **Key Files** — point to build scripts, templates, overlay CSS, docs.
- **Content Conventions** — frontmatter format (see section 9), theory
  cross-reference format (`/circuits/Semi/SEMI_6.html` absolute paths),
  component table format.
- **Design Context** — duplicate from `.impeccable.md` for quick reference,
  plus a note that hazard banners use standard safety colors regardless
  of the Open Circuits palette.

### `.gitignore`

```
# Python
.venv/
__pycache__/
*.py[cod]
.pytest_cache/

# Build output
output/

# Shared assets pulled at build time
shared/css/
shared/js/
shared/fonts/
shared/SHARED-VERSION.txt

# OS
.DS_Store
Thumbs.db
```

---

## 4. Python Project Setup

### `pyproject.toml`

```toml
[project]
name = "salvage-electronics"
version = "0.1.0"
description = "A practical guide to salvaging electronic components from discarded devices"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest>=7.4"]
```

### `requirements.txt`

```
mistune>=3.0
jinja2>=3.1
pyyaml>=6.0
```

### `requirements-dev.txt`

```
-r requirements.txt
pytest>=7.4
```

### `Makefile`

Model on `open-circuits/Makefile` with these targets:

- `install` — create `.venv/` and install deps from `requirements-dev.txt`
- `fetch` — run `build/fetch_shared.py` to pull assets from open-circuits
- `build` — run `build/build.py` to convert content to HTML
- `all` — `fetch` + `build`
- `serve` — `cd output/html && python3 -m http.server 8080`
- `test` — run pytest
- `clean` — remove `output/`
- `clean-all` — remove output, venv, pytest cache, shared assets
- `help` — print available targets

Match the comment style and `##` docstring pattern used by open-circuits.

---

## 5. Build Scripts

### `build/build.py`

A single-file build script. Responsibilities:

1. **Parse Markdown with YAML frontmatter.** Frontmatter is optional
   `---` delimiters at the top. Use `yaml.safe_load` for the frontmatter
   and `mistune` for the body. Enable mistune plugins: `strikethrough`,
   `table`, `url`, `task_lists`.

2. **Compute depth-relative paths.** A file at `content/foo/bar.md`
   outputs to `output/html/foo/bar.html` and needs asset paths prefixed
   with `../` once. A file at `content/index.md` outputs to
   `output/html/index.html` with no prefix. Write a helper
   `asset_prefix(depth)` that returns the prefix string.

3. **Render each page.** Context for Jinja2 includes:
   - `title`, `section`, `hazard` (1-4 or None), `hazard_summary` —
     from frontmatter
   - `body` — rendered Markdown HTML
   - `css_shared` — relative path to `css/open-circuits.css`
   - `css_salvage` — relative path to `css/salvage.css`
   - `js_nav` — relative path to `js/navigation.js`
   - `icons_path` — relative path prefix to `icons/`
   - Navigation paths: `home`, `foundations`, `donor_guides`, `components`,
     `projects`, `license_path`, `attribution_path` — all depth-relative

4. **Copy assets into output.**
   - `shared/css/` → `output/html/css/` (Open Circuits CSS + fonts refs)
   - `shared/js/` → `output/html/js/` (navigation.js)
   - `shared/fonts/` → `output/html/fonts/` (WOFF2 files)
   - `overlay/css/salvage.css` → `output/html/css/salvage.css`
     (must go into the same css/ dir so font-face paths resolve)
   - `overlay/icons/` → `output/html/icons/`
   - `LICENSE.txt` and `ATTRIBUTION.md` → `output/html/`

5. **Skip files starting with underscore.** `_template.md` and similar
   must not be rendered.

6. **Command-line flags:** `--clean` (remove output first).

7. **On completion:** print count of pages rendered and output path.

**Error handling:** Exit non-zero with a clear message if `CONTENT_DIR`
doesn't exist or if `shared/css/` is missing (suggest running `make fetch`).

### `build/fetch_shared.py`

Pulls shared assets from a pinned open-circuits release. Model on
`open-circuits/build/download_source.py`.

- **Pinned version** as a module-level constant, e.g. `SHARED_VERSION = "v0.1.0"`.
  Bumping this is the mechanism for opting into a new open-circuits design.
- **Release URL template:**
  `https://github.com/trydydd/open-circuits/releases/download/{version}/open-circuits-{version}.tar.gz`
  (verify the exact URL pattern by checking a real release on that repo).
- **Idempotency:** skip if `shared/css/`, `shared/js/`, and `shared/fonts/`
  all exist. `--force` flag to re-fetch.
- **Extract only the asset directories:** the tarball contains
  `open-circuits/{css,js,fonts,...}/`. Extract `css/`, `js/`, `fonts/`,
  stripping the leading `open-circuits/` prefix.
- **Write `shared/SHARED-VERSION.txt`** recording the pinned version
  and fetch date. Format matches `open-circuits/upstream/UPSTREAM-VERSION.txt`.
- **Flags:** `--force`, `--version TAG`.

---

## 6. Salvage-specific CSS

### `overlay/css/salvage.css`

This file cascades on top of `open-circuits.css`. It only contains styles
unique to Salvage Electronics. Do not redefine fonts, base typography,
layout, or color tokens — those come from the shared CSS.

**Contents:**

1. **Header comment** noting the file's role and the no-external-URLs rule.

2. **Hazard color tokens.** Four levels, each with `--haz-N-bg`,
   `--haz-N-border`, `--haz-N-text`. Use standard safety colors
   (not the Open Circuits palette):
   - Level 1: green (low — soft green bg, vivid green border)
   - Level 2: yellow (moderate — soft yellow bg, amber border)
   - Level 3: orange (significant — soft orange bg, vivid orange border)
   - Level 4: red (lethal — soft red bg, fire engine red border)

   Include a `@media (prefers-color-scheme: dark)` override with
   darker backgrounds and the same borders at slightly higher brightness.

3. **`.haz` component.** The hazard banner. Flex layout with an icon on
   the left (48px box, SVG inside at 40px) and text content on the right.
   Left border 6px in the level color. Subtle box-shadow to create a
   "sticker lift" effect:
   ```
   box-shadow:
     0 1px 2px rgba(0, 0, 0, 0.08),
     0 4px 12px rgba(0, 0, 0, 0.06);
   ```
   Level-4 gets a slightly stronger red-tinted shadow.

4. **Override the inherited `img` style inside `.haz__icon`** — the
   shared CSS adds a light background to images in dark mode, which
   would look wrong on a safety icon. Force background, padding,
   border-radius all to none.

5. **`.haz__level`** — bold Chivo text, level name.
   **`.haz__summary`** — Vollkorn body text, the one-line hazard summary.

6. **`.tier` callouts.** For the "no tools / improvised / basic / equipped"
   technique callouts in the Foundations chapter. Four variants:
   `.tier--none`, `.tier--improv`, `.tier--basic`, `.tier--equipped`.
   Each gets a different left-border color (green, yellow, grey, copper).

7. **`.yield-rating`** — monospaced, letter-spacing for the star ratings
   in donor guide tables.

8. **Print overrides.** `.haz` gets `box-shadow: none` and a solid border
   in print.

**Do not include:** `@font-face`, base typography, body layout, header
styles, sidebar styles. All of those come from the shared CSS.

---

## 7. Hazard Icons (SVG)

Four SVG files, each 48×48 viewBox, inline styles (no external CSS).
Icons are bold, high-contrast, readable at 40px on a cheap phone screen.

### `overlay/icons/hazard-1.svg` — Level 1 / Low Risk

Green circle with simple smile. Filled circle fill `#3f8f3f`, darker green
stroke `#1e4f1e` at 2px. White eyes (2.5px circles) at roughly (17,20)
and (31,20). White smile arc from (14,28) curving down through (24,36)
to (34,28), 3px stroke, rounded caps.

### `overlay/icons/hazard-2.svg` — Level 2 / Moderate

Yellow diamond/rhombus (rotated square) with a subtle haze or cloud
mark inside. Fill `#d4a017`, dark amber stroke `#5a4500` at 2px. Inside:
a simple wavy line or cloud glyph in white at roughly mid-height. Keep
it clearly distinct from Level 3 (not a warning triangle).

### `overlay/icons/hazard-3.svg` — Level 3 / Significant

Standard orange warning triangle with centred exclamation mark. Fill
`#d95b0a`, dark stroke `#5a2300` at 2px. White exclamation mark (stroke
or path), about 24px tall, vertically centred with a tiny gap above the
bottom dot. This should match the universally recognized warning symbol.

### `overlay/icons/hazard-4.svg` — Level 4 / Lethal Danger

Red octagon (like a stop sign) with a white skull and crossbones inside.
Octagon fill `#c91a1a`, dark red stroke `#4a0000` at 2px. Skull: two black
or white circles for eye sockets, a simple triangle nose, small rectangle
mouth. Two crossed lines (the crossbones) behind the skull. Keep it
iconic and immediately readable — don't over-detail.

**For each icon:** include `role="img"` and `aria-label` attributes
describing the hazard level. No external references. No embedded fonts
(use paths for any letters).

---

## 8. Templates

### `templates/page.html`

Single Jinja2 template used for every page. HTML5 doctype, `lang="en"`.

`<head>` contents:
- charset UTF-8, viewport meta
- `<title>Salvage Electronics — {{ title }}</title>`
- `<link>` to `{{ css_shared }}` (open-circuits.css)
- `<link>` to `{{ css_salvage }}` (salvage.css) — loaded AFTER shared
- `<script src="{{ js_nav }}" defer>` for the shared sidebar nav

`<body>` structure:
- `<noscript>` block that hides sidebar when JS is off (copy from
  open-circuits' header.html template)
- Inline script adding `sidebar-closed` class to body (copy from
  open-circuits' header.html)
- `{% include "partials/header.html" %}`
- `<aside id="oc-sidebar" class="oc-sidebar">` for the JS-populated TOC
- `<main>` containing:
  - `{% if hazard %}{% include "partials/hazard-banner.html" %}{% endif %}`
  - `<article>{{ body | safe }}</article>`
- `{% include "partials/footer.html" %}`

### `templates/partials/header.html`

Adapt from `open-circuits/overlay/templates/header.html`. Keep the
menu toggle button exactly as-is. Replace:

- Site title: `<a href="{{ home }}">Salvage Electronics</a>` (no logo yet —
  can be added later; keep the `.oc-site-title` class so shared CSS styles it)
- Volume nav → Section nav. Five items:
  ```
  <li><a href="{{ foundations }}">Foundations</a></li>
  <li><a href="{{ donor_guides }}">Donors</a></li>
  <li><a href="{{ components }}">Components</a></li>
  <li><a href="{{ projects }}">Projects</a></li>
  <li><a href="/circuits/index.html">Theory</a></li>
  ```

The "Theory" link is the cross-project connection — it uses an absolute
path because nginx resolves `/circuits/` to the Open Circuits deployment.

### `templates/partials/footer.html`

```html
<footer class="oc-footer">
  <p>Salvage Electronics by the Hearth Project.
  &nbsp;&middot;&nbsp;
  <a href="{{ license_path }}">CC BY-SA 4.0</a>
  &nbsp;&middot;&nbsp;
  <a href="{{ attribution_path }}">Attribution</a>
  &nbsp;&middot;&nbsp;
  Design shared with <a href="/circuits/index.html">Open Circuits</a> (CC BY 4.0)</p>
</footer>
```

### `templates/partials/hazard-banner.html`

The warning banner. Rendered only when `hazard` is set in frontmatter.

```html
<aside class="haz haz--level-{{ hazard }}" role="note" aria-label="Hazard warning">
  <div class="haz__icon">
    <img src="{{ icons_path }}hazard-{{ hazard }}.svg"
         alt="Hazard level {{ hazard }} of 4"
         width="40" height="40">
  </div>
  <div class="haz__content">
    <p class="haz__level">
      {% if hazard == 1 %}Level 1 — Low Risk
      {% elif hazard == 2 %}Level 2 — Moderate
      {% elif hazard == 3 %}Level 3 — Significant
      {% elif hazard == 4 %}Level 4 — Lethal Danger
      {% endif %}
    </p>
    {% if hazard_summary %}
      <p class="haz__summary">{{ hazard_summary }}</p>
    {% endif %}
  </div>
</aside>
```

---

## 9. Content Stubs

Every content file has YAML frontmatter and a body. The body is a
"skeleton stub" — real enough to render and navigate, with clear TODO
markers for the human author to fill in.

**Frontmatter schema** (all keys optional except `title`):

```yaml
---
title: "Page Title"                    # Required
section: "foundations"                 # foundations|donor-guides|components|projects
hazard: 3                              # 1-4 or null; omit for no banner
hazard_summary: "One-line summary of the primary hazard."
---
```

**Stub body pattern:** a short intro paragraph stating what the page will
cover, then `## TODO` section headings matching the outline for that topic,
each with a one-sentence description of what belongs there. No placeholder
lorem-ipsum. The intent: someone reading the stub should understand the
planned scope and be able to start writing any section independently.

Reference `salvage-electronics-outline.md` (attached separately, or
reconstructible from Section 11 of this plan) for the full outline of
each page's intended contents.

### `content/index.md`

Home page. Brief welcome, the four-section navigation, one-line teaser
per section. No hazard banner.

### Foundations (4 pages)

- `01-why-salvage.md` — no hazard. Covers: why reuse, realistic expectations,
  the salvage mindset, how to use the guide.
- `02-safety.md` — **explicitly opt out of the hazard banner** (leave
  `hazard: null` in frontmatter). The whole chapter IS the hazard system.
  Covers: electricity and the body, capacitor discharge, mains awareness,
  CRT safety, batteries, lead solder, sharps.
- `03-tools-and-workspace.md` — no hazard. Tiered minimum kit, soldering
  options (no iron / improvised / basic / equipped), storage.
- `04-core-techniques.md` — no hazard. Desoldering (all tiers), SMD removal,
  cleaning and inspection.

### Donor Guides (12 pages + template)

- `_template.md` — the donor guide template. Starts with `_` so build
  skips it. Contents: frontmatter schema, boilerplate sections (What's
  Inside / Before You Open It / What to Target (table) / How to Get
  Them Out / Watch Out For / Theory Links / Specific Teardowns).
- Each guide uses the template structure. Frontmatter has:
  - `section: donor-guides`
  - `hazard: N` (1-4) — per the table below
  - `hazard_summary: "one line"` — specific to the device

| File | Hazard | Key hazard summary |
|---|---|---|
| `01-battery-devices.md` | 1 | Low voltage, no stored energy concerns. |
| `02-wall-chargers.md` | 2 | Internal caps may hold charge; unplug and wait. |
| `03-routers-modems.md` | 2 | Low-voltage DC internally; powered by external adapter. |
| `04-printers.md` | 2 | Low-voltage logic; laser printer fuser runs at mains voltage (upgrade to 3 for laser). |
| `05-desktop-computers.md` | 2 | Low-voltage DC once unplugged; PSU is a separate device. |
| `06-laptops.md` | 2 | Remove battery first; lithium cells can be hazardous. |
| `07-atx-power-supplies.md` | 3 | Large input caps hold 300V+ for minutes after unplugging. |
| `08-audio-equipment.md` | 3 | Mains-powered; supply caps hold charge. Valve amps are LEVEL 4 — 300-500V HT rail. |
| `09-led-bulbs.md` | 2 | Small driver board with minor stored energy. |
| `10-microwave-ovens.md` | 4 | HV capacitor can hold LETHAL charge for hours or days. |
| `11-crt-monitors.md` | 4 | Anode holds 25,000V+ for weeks after unplugging. |
| `12-ups-units.md` | 4 | Batteries stay live; can deliver very high short-circuit current. |

### Components (10 pages)

All have `section: components` and no hazard banner (desoldering happens
in Foundations, not here).

- `01-resistors.md` — identify, color codes, test with meter, failure modes.
- `02-capacitors.md` — types, markings, test methods, voltage derating.
- `03-diodes.md` — types, diode-mode testing, forward voltage by type.
- `04-transistors-bjt.md` — NPN/PNP, diode-mode test, pin identification.
- `05-mosfets.md` — N/P channel, body diode test, gate behaviour.
- `06-voltage-regulators.md` — 78xx/79xx series, LDO, testing.
- `07-inductors-transformers.md` — identification, continuity, isolation.
- `08-relays.md` — coil/contacts, clicking test, contact condition.
- `09-motors.md` — DC / brushless / stepper / synchronous, testing each.
- `10-connectors-switches.md` — always worth pulling.

### Projects (6 pages)

All have `section: projects` and no hazard banner (project-specific
hazards are called out inline where relevant).

- `01-continuity-tester.md` — LED + battery + resistor.
- `02-cap-discharge-tool.md` — power resistor + probes; safety tool.
- `03-atx-bench-supply.md` — convert salvaged PSU to bench supply.
- `04-component-tester-jig.md` — test jig with perfboard.
- `05-usb-charger.md` — transformer + bridge + 7805 + USB socket.
- `06-led-lamp.md` — LEDs + driver + enclosure.

---

## 10. Documentation

### `docs/HEARTH-INTEGRATION.md`

Model on `open-circuits/docs/HEARTH-INTEGRATION.md`. Sections:

- **Release Artifacts** — HTML tarball and ZIM file (ZIM is Phase 2).
- **Static Mode (nginx)** — how Hearth's Ansible role consumes the
  tarball, location block at `/salvage/`, `hearth.yaml` config.
- **URL Stability Contract** — the stable paths, listed below. This is
  the critical document; cross-linking from open-circuits depends on it.

**Stable paths (contract):**

```
/salvage/index.html                        — root
/salvage/foundations/01-why-salvage.html
/salvage/foundations/02-safety.html
/salvage/foundations/03-tools-and-workspace.html
/salvage/foundations/04-core-techniques.html
/salvage/donor-guides/NN-{slug}.html       — where NN is zero-padded index
/salvage/components/NN-{slug}.html
/salvage/projects/NN-{slug}.html
```

- **Cross-references into Open Circuits** — table of salvage topics to
  open-circuits chapter URLs (reproduce the cross-reference map from the
  outline doc).
- **How open-circuits links back** — sentinel for future: if open-circuits
  ever wants to add "See the salvage guide" links, it does so with absolute
  `/salvage/...` paths.
- **Upgrading** — tag a new version, update `hearth.yaml` in the hearth repo.

### `docs/HAZARD-SYSTEM.md`

The hazard rating specification. Sections:

- **Purpose** — why we rate hazard level on donor pages.
- **The four levels** — table with level number, color, symbol description,
  meaning, example devices. Match the outline.
- **Icon design** — rules for hazard SVGs: 48×48 viewBox, inline only,
  no external refs, readable at 40px. Colors locked to standard safety
  colors, not the brand palette.
- **Placement** — always above the page content, below the header. One
  per page, at the top, before any disassembly instructions.
- **Writing the summary line** — it's the one-sentence worst-case
  warning. Present tense. States the specific hazard, not a generic one.
  "HV capacitor can hold lethal charge for hours" not "be careful."
- **When NOT to use a banner** — Foundations safety chapter (it IS the
  system), Components pages (testing is low-hazard), Projects (inline
  warnings instead). Index page.
- **Accessibility** — alt text and `aria-label` requirements. Colour
  must never be the sole signal (hence the text label).
- **Print rendering** — box-shadow removed, solid border kept.

### `docs/STYLE-GUIDE.md`

Writing standards. Sections:

- **Voice** — active, second person. "Flip the board over," not "the
  board should be flipped."
- **Register** — workshop-y, tactile, honest. Not academic, not
  marketing-y. No exclamation marks. Short paragraphs (phone reading).
- **Safety framing** — hazards stated plainly, never fear-mongering.
  Always pair a hazard with a procedure: "the capacitor can hold a
  lethal charge; here's how to discharge it safely."
- **Tiered techniques** — when presenting a technique, show the range
  from no-tool to equipped. Use the `.tier` callouts. Never assume the
  reader has money.
- **Specs as ranges** — "Electrolytic caps in ATX PSUs range 680µF to
  2200µF" not "use a 1000µF cap."
- **Cross-linking to theory** — absolute path `/circuits/...`. Format:
  short inline link, never a footnote. "These are MOSFETs ([theory])"
  with `[theory]` linking to `/circuits/Semi/SEMI_6.html`.
- **Tables** — use the 4-column donor format: Component / Where / Specs
  / Worth-it. Star rating: ★★★ / ★★☆ / ★☆☆.
- **Component specs** — always give what the reader can actually
  measure. Voltage ratings, polarity, package.
- **Celebrate the salvage** — when a part has a good second life, say
  so. Matches Hearth's resourceful optimism.
- **Mistakes to avoid** — don't gatekeep (assuming expensive tools);
  don't scare without procedure; don't moralize about e-waste; don't
  assume prior knowledge without linking to theory.

### `docs/BUILDING.md`

Model on `open-circuits/docs/BUILDING.md` but much simpler — no overlay
injection, no upstream download. Sections:

- **Prerequisites** — Python 3.10+, make, internet (first fetch only).
- **Quick Start** — `make install && make all && make serve`.
- **Individual steps** — `make fetch` / `make build` / details.
- **Iterating on styles** — edit `overlay/css/salvage.css`, run
  `make build`, reload browser.
- **Adding a new content page** — create `content/section/NN-name.md`
  with frontmatter, run `make build`, it appears.
- **Bumping shared assets** — edit `SHARED_VERSION` in `fetch_shared.py`,
  run `make fetch --force`.
- **Testing** — `make test` (test coverage to be added later).
- **Troubleshooting** — common errors: missing shared assets, malformed
  frontmatter, broken template paths.

---

## 11. Build and Verification

After all files are in place, verify the build works end-to-end:

```sh
make install            # creates .venv, installs deps
make fetch              # downloads shared assets from open-circuits release
make build              # converts content/ to output/html/
make serve              # starts local server
```

Open http://localhost:8080 and verify:

- [ ] Index page loads with header and footer styled correctly
- [ ] Navigation links between sections all work
- [ ] "Theory" link points to `/circuits/index.html` (will 404 in local
      testing — that's expected; works on Hearth deploy)
- [ ] Hazard banners render on donor guide pages with correct colors
      per level
- [ ] Fonts load (Vollkorn body, Chivo headings) — text should NOT be
      in system serif/sans fallback
- [ ] Dark mode works (system preference toggle)
- [ ] No external resource URLs in built HTML (`grep -r "http://" output/html/`
      should return only links to external domains in anchor href, never
      in `<link>` or `<script>` src)
- [ ] LICENSE.txt and ATTRIBUTION.md are reachable from every footer
- [ ] Print stylesheet renders cleanly (Ctrl+P preview)

**If the fetch step fails:** the Open Circuits release tarball URL
pattern may differ from what's assumed in `fetch_shared.py`. Check the
actual releases page and adjust the `RELEASE_URL_TEMPLATE` constant.

---

## 12. What's NOT in Scope for This Initial Build

Do not attempt any of the following in the initial bootstrap. Note them
in a TODO.md at the repo root for future work:

- **Full content writing.** Only stubs. Humans will author real content.
- **Specific device teardowns.** The donor guides are generic. Specific
  make/model teardowns go in `content/donor-guides/teardowns/` in a
  future phase.
- **ZIM packaging.** Phase 2. `build/build_zim.py` can be written later.
- **GitHub Actions workflows.** Add after first successful local build.
- **Site-wide search.** Defer. The shared navigation.js handles per-page
  TOC; site search is Phase 2.
- **Image assets in content.** Schematics, photos — needs its own
  strategy (SVG preferred for schematics; photos compressed heavily for
  offline distribution).

---

## 13. Dependencies and License Clarity Checklist

Before first commit, verify:

- [ ] `LICENSE.txt` is CC BY-SA 4.0, correctly attributed
- [ ] `ATTRIBUTION.md` notes dependency on open-circuits CC BY 4.0 assets
- [ ] Every footer links to `LICENSE.txt` and `ATTRIBUTION.md`
- [ ] Footer explicitly notes "Design shared with Open Circuits (CC BY 4.0)"
- [ ] No text copied from open-circuits into salvage content (only
      hyperlinks via absolute paths)
- [ ] `fetch_shared.py` pins a specific open-circuits version, not `main`
- [ ] `shared/SHARED-VERSION.txt` records which version was fetched

---

## 14. Success Criteria

The bootstrap is done when:

1. `make install && make all && make serve` produces a locally browsable
   site with no errors.
2. Every section has at least one stub page that renders correctly.
3. Hazard banners appear on donor pages with correct colors and icons.
4. The footer credits and license links resolve.
5. A reader on a phone in workshop lighting can read the stub content
   comfortably (test on a real phone, or Chrome DevTools mobile view
   at low zoom).
6. Running `grep -r "https\?://" output/html/ | grep -v "creativecommons.org\|github.com"`
   returns no matches in `<link>` or `<script>` tags — only in content
   anchor hrefs.

Once these criteria pass, commit the skeleton, tag `v0.1.0`, and the
repo is ready for human authors to start filling in content.

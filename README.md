# Salvage Electronics — A Practical Salvage Guide

A practical, offline-friendly guide to salvaging electronic components from discarded devices.

This project builds original Markdown content into a static HTML site while sharing design assets with
[Open Circuits](https://github.com/trydydd/open-circuits), so both resources feel like parts of the same
Hearth reference library.

---

## What's here

| Section | Focus |
|--------|-------|
| Foundations | Safety, salvage mindset, workspace setup, and core techniques |
| Donor Guides | What common discarded devices contain, what to target, and what to watch out for |
| Components | How to identify, test, and reuse the parts you pull |
| Projects | Small builds that turn salvaged parts into useful tools and circuits |

---

## Philosophy

- **Tiered techniques** — Whenever possible, methods should scale from improvised setups to better-equipped benches.
- **Requirements, not products** — The guide should describe what a job needs, not assume a specific branded tool.
- **Safety first** — High-risk donor devices are clearly marked, and theory links point to the relevant Open Circuits chapters.

---

## Build

```bash
# 1. Create the venv and install dependencies
make install

# 2. Fetch shared design assets from Open Circuits
make fetch

# 3. Build the static site
make build

# 4. Serve the output locally
make serve

# 5. Remove generated files
make clean
```

---

## Architecture

| Repository | Role | Notes |
|------------|------|-------|
| `salvage` | Original Salvage Electronics content and build pipeline | Builds Markdown into `/salvage/` HTML output |
| `open-circuits` | Shared design system and theory reference | Provides build-time CSS, fonts, and JS under CC BY 4.0 |
| `hearth` | Deployment and integration | Pins release artifacts and serves them at stable nginx paths |

Salvage Electronics links into Open Circuits using absolute theory URLs such as
`/open-circuits/Semi/SEMI_6.html`. Those are hyperlinks only — Salvage does not copy Open Circuits theory text.

---

## License

Salvage Electronics is original work by the Hearth project and is published under
**Creative Commons Attribution-ShareAlike 4.0 International** (CC BY-SA 4.0).

See `LICENSE.txt` for the license text and `ATTRIBUTION.md` for dependency credits,
modification notices, and attribution details for shared Open Circuits assets.

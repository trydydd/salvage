# Building Salvage Electronics

How to fetch shared assets, build the site, and test the output locally.

---

## Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| `python3` (3.10+) | build scripts and local server | `sudo apt install python3` / standard on macOS |
| `make` | Makefile shortcuts | `sudo apt install make` / standard on macOS |
| Internet access | first shared-asset fetch from Open Circuits releases | only needed for `make fetch` when assets are absent or bumped |

This project does not download upstream content and does not inject an overlay into third-party HTML. It builds local Markdown content and copies shared Open Circuits assets into the output.

---

## Quick Start

```sh
make install && make all && make serve
```

That sequence:
1. creates `.venv` and installs dependencies,
2. fetches the pinned shared CSS, JS, and fonts,
3. builds the site into `output/html/`,
4. serves it locally at <http://localhost:8080>.

---

## Individual Steps

### Fetch shared assets

```sh
make fetch
```

This runs `build/fetch_shared.py`, downloads the pinned Open Circuits release tarball, and populates:

- `shared/css/`
- `shared/js/`
- `shared/fonts/`
- `shared/SHARED-VERSION.txt`

### Build the site

```sh
make build
```

This runs `build/build.py`, renders `content/**/*.md` to `output/html/**/*.html`, copies shared assets, copies `overlay/css/salvage.css`, and includes `LICENSE.txt` plus `ATTRIBUTION.md` in the build output.

### Serve locally

```sh
make serve
```

This serves `output/html/` at <http://localhost:8080> using Python's built-in HTTP server.

---

## Iterating on Styles

Edit `overlay/css/salvage.css`, then rebuild:

```sh
make build
```

Reload the browser after each build. Hazard-banner colors, `.tier` callouts, and print-specific rules all live in this stylesheet.

---

## Adding a New Content Page

1. Create a new Markdown file under the right section, for example `content/components/11-example-part.md`.
2. Add YAML frontmatter.
3. Run `make build`.
4. Open the generated page under `output/html/`.

Minimal frontmatter:

```yaml
---
title: "Example Part"
section: components
---
```

For donor guides, also set `hazard` and `hazard_summary` when the page needs the top-of-page hazard banner.

---

## Bumping Shared Assets

Shared design assets are pinned by `SHARED_VERSION` in `build/fetch_shared.py`.

To opt into a new Open Circuits release:

1. Edit `SHARED_VERSION` in `build/fetch_shared.py`.
2. Re-fetch the assets with force:

```sh
python build/fetch_shared.py --force
```

If the release URL pattern ever changes, update `RELEASE_URL_TEMPLATE` in the same file.

---

## Testing

```sh
make test
```

Today this runs `pytest`. Test coverage will expand later; an empty test collection is currently acceptable.

For manual verification after a build, also check:
- header and footer render correctly,
- `/open-circuits/index.html` is used for the Theory nav link,
- donor-guide hazard banners appear only where intended,
- `LICENSE.txt` and `ATTRIBUTION.md` are reachable from the footer,
- print preview keeps hazard borders and removes banner shadow.

---

## Future ZIM Packaging

ZIM packaging is not part of the current build pipeline. It is planned for Phase 2.

Until that lands:
- the HTML tarball is the real deployment artifact,
- docs reserve `salvage.zim` as the future artifact name,
- no local ZIM build step is required for normal development.

---

## Troubleshooting

### Missing shared assets

If the build says shared assets are missing, run:

```sh
make fetch
```

### Malformed frontmatter

If the build fails while parsing a page, check that:
- frontmatter starts with `---`,
- frontmatter ends with `---`,
- the parsed YAML is a mapping,
- `title` is present.

### Broken template paths

If pages build but styles, icons, or navigation are missing, rebuild and then inspect:
- `templates/page.html`
- `templates/partials/`
- `overlay/css/salvage.css`
- `shared/`

Also confirm the page is being opened through `make serve` or another HTTP server, not directly from the filesystem.

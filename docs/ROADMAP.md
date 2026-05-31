# Roadmap to 1.0.0

The step-by-step path from where the repo is today to a production-ready
`v1.0.0` release. Work top to bottom — milestones are ordered by dependency, and
each one has an explicit **exit criteria** that gates the next.

> **Definition of 1.0.0:** every content page is authored (no `TODO` stubs, no
> open fact-checks), the site passes a technical and accessibility pass, and a
> tagged release publishes the `salvage-vX.Y.Z.tar.gz` artifact that Hearth
> consumes. ZIM packaging and site search are explicitly **Phase 2** and do
> **not** block 1.0.0 (see `HEARTH-INTEGRATION.md`).

---

## Where we are now

| Area | Status |
|------|--------|
| Build pipeline, asset fetch, templates, hazard system | ✅ Done |
| Test suite + CI workflows (`build`, `pages`, `release`) | ✅ Done |
| Docs (building, style, hazard, integration) + authoring skills | ✅ Done |
| Components — 10 pages | ✅ Authored & fact-checked |
| Donor guides — 13 pages | 🟡 3 of 13 done (laptops, ATX PSU, solar fence charger) |
| Foundations — 4 pages | 🔴 All stubs (incl. safety) |
| Projects — 6 pages | 🔴 All stubs |
| Content images / schematics | 🔴 Strategy undefined |

The infrastructure is production-grade; **1.0.0 is gated almost entirely on
content authoring plus a final QA/release pass.**

---

## Milestone 0 — Clear loose ends `in progress`

- [x] Resolve the 4 open `⚠️ FACT-CHECK` markers in `05-mosfets.md` and `08-relays.md`.
- [ ] Confirm `grep -rn "FACT-CHECK" content/` returns nothing and `FACT-CHECKS.md` is empty.
- [ ] `make test` green.
- [ ] Commit + push to the working branch.

**Exit:** no fact-check markers anywhere, tests pass.

---

## Milestone 1 — Foundations (the spine)

The conceptual base that every hazardous donor guide and project links back to.
Author with the `write-foundation` skill, in this order (safety first — it is
referenced site-wide):

- [ ] `content/foundations/02-safety.md` — electricity & the body, capacitor
      discharge, mains awareness, CRT/HV, batteries, solder/fumes, sharps.
- [ ] `content/foundations/01-why-salvage.md`
- [ ] `content/foundations/03-tools-and-workspace.md`
- [ ] `content/foundations/04-core-techniques.md` (finish the sections beyond the
      already-written wall-wart note).
- [ ] Cross-link each to the correct `/open-circuits/...` chapter (see the
      cross-reference map in `HEARTH-INTEGRATION.md`); never link `EXP_1.html`.

**Exit:** no `TODO` in `content/foundations/`; `make build` renders all four;
safety page is the canonical target for hazard-banner "see safety" references.

---

## Milestone 2 — Donor guides

Fill the 10 remaining stubs. Each already has a finished component table; the
prose sections are scaffolded. Use the `write-donor-guide` skill and the three
completed exemplars (`06`, `07`, `13`) as the depth/voice target (~2,000 words).

- [ ] `01-battery-devices` · `02-wall-chargers` · `03-routers-modems` · `04-printers` · `05-desktop-computers`
- [ ] `08-audio-equipment` · `09-led-bulbs` · `10-microwave-ovens` · `11-crt-monitors` · `12-ups-units`
- [ ] Confirm each `hazard` / `hazard_summary` matches the actual worst-case (the
      4-tier guides — microwave, CRT, UPS — get the most scrutiny).
- [ ] Verify every named hazard is paired with a discharge/handling procedure.

**Exit:** no `TODO` in `content/donor-guides/`; hazard banners correct on every page.

---

## Milestone 3 — Projects

Author the 6 build guides with the `write-project` skill. These depend on M1
(safety) and M2 (where parts come from), so they come after.

- [ ] `01-continuity-tester` · `02-cap-discharge-tool` · `03-atx-bench-supply`
- [ ] `04-component-tester-jig` · `05-usb-charger` · `06-led-lamp`
- [ ] The cap-discharge tool and ATX bench supply are safety-adjacent — link them
      tightly to `02-safety.md` and the relevant donor guide.

**Exit:** no `TODO` in `content/projects/`; each project lists salvageable parts,
a build layout, and a test/use procedure.

---

## Milestone 4 — Technical review & content QA

- [ ] Run the `review-technical` skill across every component page and donor guide;
      resolve or fact-check every flagged claim. `FACT-CHECKS.md` ends empty.
- [ ] Spot-check measurable specs (voltages, pinouts, deratings) against the
      skill's calibration table.
- [ ] Verify all `/open-circuits/...` links resolve to live chapters and none point
      at `EXP_1.html` (tests `test_no_stale_exper1_links` / `test_no_exp1_intro_links`).
- [ ] Proofread for STYLE-GUIDE voice (active second person, ranges over vague
      qualifiers, four-column donor tables).

**Exit:** clean technical review, empty fact-check tracker, all cross-links valid.

---

## Milestone 5 — Images & diagrams

Decide and implement the deferred image strategy (TODO.md item).

- [ ] Define conventions: SVG for schematics/pinouts, aggressively compressed
      raster for photos; document in `STYLE-GUIDE.md`.
- [ ] Add build-pipeline handling for an image directory (copy + relative-path
      rewrite alongside existing asset copying in `build/build.py`).
- [ ] Add the schematics/diagrams the projects need to be buildable from the page
      alone (at minimum: continuity tester, cap-discharge tool, ATX bench supply).
- [ ] Confirm images ship in the build output (no CDN refs — offline-first).

**Exit:** projects are buildable from the page; all images are local and sized for offline.

---

## Milestone 6 — Design, accessibility & print pass

- [ ] Run the `i-audit` skill; triage P0/P1 findings.
- [ ] Verify light/dark (`prefers-color-scheme`), responsive layout on a small
      viewport, and full no-JS usability.
- [ ] Verify print output: hazard borders kept, banner shadow removed, readable.
- [ ] Confirm hazard colors use the standard safety palette, not the OC accent
      (per `HAZARD-SYSTEM.md`).

**Exit:** no P0 accessibility issues; print + dark mode + no-JS all verified.

---

## Milestone 7 — Release engineering & 1.0.0 cut

- [ ] Confirm CI (`build.yml`, `pages.yml`, `release.yml`) is green on `main`.
- [ ] Confirm the release workflow produces `salvage-vX.Y.Z.tar.gz` and attaches it
      to the tag, with shared assets bundled (no CDN deps in the artifact).
- [ ] Smoke-test the tarball against the nginx path contract in
      `HEARTH-INTEGRATION.md` (`/salvage/...` paths stable, footer license/attribution reachable).
- [ ] Update the pinned `version:` example in `HEARTH-INTEGRATION.md` to `v1.0.0`.
- [ ] Tag `v1.0.0` and verify the release artifact downloads and serves clean.

**Exit:** `v1.0.0` tagged, artifact published, Hearth can pin it.

---

## Beyond 1.0.0 — Phase 2 (not required to ship)

These are tracked in `TODO.md` and reserved as future-stable contracts; they are
deliberately **out of scope for 1.0.0**:

- [ ] Make/model-specific teardowns under `content/donor-guides/teardowns/`.
- [ ] ZIM packaging (`build/build_zim.py`) → `salvage.zim` for Kiwix deployments.
- [ ] Site-wide search.

---

## Quick reference

| Command | Use |
|---------|-----|
| `make install && make all && make serve` | full local build + preview |
| `make build` | re-render after content edits |
| `make test` | run the pytest suite |
| `grep -rn "TODO\|FACT-CHECK" content/` | find remaining unfinished content |

**Authoring skills:** `write-foundation`, `write-donor-guide`, `write-project`,
`write-component`, `review-technical`. **Design skills:** `i-audit` and the `i-*`
family.

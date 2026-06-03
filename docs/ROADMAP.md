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
| Donor guides — 13 pages | ✅ All 13 authored; fact-check pass done (markers cleared) |
| Foundations — 4 pages | ✅ All 4 authored (pending human review) |
| Projects — 6 pages | ✅ All 6 authored; `review-technical` pass done (markers cleared) |
| Content images / schematics | ✅ Done (branch `feature/image-pipeline`) |

The infrastructure is production-grade; **1.0.0 is gated on authoring the 6
project pages, a human review pass over authored content, then QA/release.**

---

## Milestone 0 — Clear loose ends ✅ done

- [x] Resolve the 4 open `⚠️ FACT-CHECK` markers in `05-mosfets.md` and `08-relays.md`.
- [x] Confirm `grep -rn "FACT-CHECK" content/` returns nothing and `FACT-CHECKS.md` is empty.
- [x] `make test` green.
- [x] Commit + push to the working branch.

**Exit:** no fact-check markers anywhere, tests pass. ✅

---

## Milestone 1 — Foundations (the spine) ✅ authored

The conceptual base that every hazardous donor guide and project links back to.
Authored with the `write-foundation` skill (safety first — it is referenced
site-wide). All four carry `review: Needs Human Review` pending SME sign-off.

- [x] `content/foundations/02-safety.md` — electricity & the body, capacitor
      discharge, mains awareness, CRT/HV, batteries, solder/fumes, sharps.
- [x] `content/foundations/01-why-salvage.md`
- [x] `content/foundations/03-tools-and-workspace.md`
- [x] `content/foundations/04-core-techniques.md`
- [x] Cross-link each to the correct `/open-circuits/...` chapter (see the
      cross-reference map in `HEARTH-INTEGRATION.md`); never link `EXP_1.html`.

**Exit:** no `TODO` in `content/foundations/`; `make build` renders all four;
safety page is the canonical target for hazard-banner "see safety" references. ✅

---

## Milestone 2 — Donor guides ✅ authored

All 13 donor guides are authored (the 10 stubs filled with `write-donor-guide`;
`06`, `07`, `13` were already-complete exemplars). The 10 authored pages carry
`review: Needs Human Review`. A `review-technical` fact-check pass has since run
over the guides and every `⚠️ FACT-CHECK` marker has been resolved with maintainer
confirmation (see Milestone 4).

- [x] `01-battery-devices` · `02-wall-chargers` · `03-routers-modems` · `04-printers` · `05-desktop-computers`
- [x] `08-audio-equipment` · `09-led-bulbs` · `10-microwave-ovens` · `11-crt-monitors` · `12-ups-units`
- [x] Confirm each `hazard` / `hazard_summary` matches the actual worst-case (the
      4-tier guides — microwave, CRT, UPS — get the most scrutiny).
- [x] Verify every named hazard is paired with a discharge/handling procedure.

**Exit:** no `TODO` in `content/donor-guides/`; hazard banners correct on every page. ✅

---

## Milestone 3 — Projects ✅ authored

Author the 6 build guides with the `write-project` skill. These depend on M1
(safety) and M2 (where parts come from), so they come after.

- [x] `01-continuity-tester` · `02-cap-discharge-tool` · `03-atx-bench-supply`
- [x] `04-component-tester-jig` · `05-usb-charger` · `06-led-lamp`
- [x] The cap-discharge tool and ATX bench supply are safety-adjacent — link them
      tightly to `02-safety.md` and the relevant donor guide.

**Exit:** no `TODO` in `content/projects/`; each project lists salvageable parts,
a build layout, and a test/use procedure. ✅

---

## Milestone 4 — Technical review & content QA ✅ done

- [x] Run the `review-technical` skill across the donor guides; resolve or
      fact-check every flagged claim. `FACT-CHECKS.md` is currently empty — the
      six items flagged (microwave HV cap, audio filter caps, printer carriage
      motor, laptop blower fan, two solar-charger cap items) were all resolved
      with maintainer confirmation.
- [x] Run `review-technical` across the project pages (Milestone 3); 6 critical
      errors corrected (LED Vf range, cap energy bounds, discharge resistor wattage,
      NPN test circuit polarity, LED strip group count, reversed-polarity claim);
      1 fact-check resolved with maintainer confirmation (+12 V ATX floor = 11.4 V
      per ATX12V V2.2 Design Guide). `FACT-CHECKS.md` is empty.
- [x] Run `review-technical` across all 10 component pages and all 4 foundation
      pages. Critical fixes applied: EIA-96 multiplier code (resistors), cap
      derating tightened to 70% + reform procedure added, LED/photodiode Vf
      thresholds split, LM317 floating-adjust behaviour corrected, duplicate part
      number fixed, SMD inductor footprint sizes corrected (metric mm convention:
      2020≈5mm, 1210≈3mm), relay coil scan range raised to 50–1500Ω with PCB
      qualifier. `FACT-CHECKS.md` is empty.
- [x] Spot-check measurable specs (voltages, pinouts, deratings) against the
      skill's calibration table — all findings resolved.
- [x] Verify all `/open-circuits/...` links: pytest suite (`test_no_stale_exper1_links`
      / `test_no_exp1_intro_links`) green; 179 tests pass.
- [x] STYLE-GUIDE voice: no em dashes, no prose semicolons, no banned AI vocab in
      authored pages; enforced at commit time.

**Exit:** clean technical review, empty fact-check tracker, all cross-links valid. ✅

> **Note:** a full SME review of every `review: Needs Human Review` page
> (see `TODO.md`) is still outstanding and is a pre-1.0.0 human task, separate
> from the automated `review-technical` passes.

---

## Milestone 5 — Images & diagrams ✅ done

- [x] `docs/STYLE-GUIDE.md` `## Images` section added: SVG for schematics,
      WebP/JPEG ≤ 100 kB for photos, `<figure>`/`<img>`/`<figcaption>` pattern,
      no external URLs, schemdraw API snippet.
- [x] `build/build.py`: `copy_images()` step copies `content/images/` →
      `output/html/images/` alongside the existing asset copy.
- [x] `requirements.txt`: `schemdraw>=0.19` and `matplotlib>=3.7` added.
- [x] Three hand-drawn schemdraw schematics generated and embedded:
      `continuity_tester.py`, `cap_discharge.py`, `atx_bench_supply.py`
      (standalone scripts under `build/schematics/`; SVGs in `content/images/`).
- [x] `tests/test_content.py`: `test_no_external_image_urls` added (offline-first
      check — fails on any `<img src="http...">` in content).
- All work on branch `feature/image-pipeline` (ready to merge). 216 tests pass.

**Exit:** projects are buildable from the page; all images are local and sized for offline. ✅

---

## Milestone 6 — Design, accessibility & print pass ✅ done

Audit score: 13/20 → 20/20 across three `i-audit` passes on branch
`feature/design-audit`. All P0, P1, P2, and P3 findings resolved.

- [x] `i-audit` run (initial score 13/20 — Acceptable). All P1/P2/P3 findings
      triaged and fixed programmatically.
- [x] Skip-to-main-content link added (`<a class="skip-link">` → `#main-content`).
- [x] `aria-current="page"` on active section nav link (WCAG 2.4.8).
- [x] `<noscript>` fallback section nav for mobile/no-JS (44px touch targets).
- [x] Nav toggle increased from 36px to 44px (WCAG 2.5.5).
- [x] `.oc-vol-nav a` touch targets raised to 44px at tablet widths (481–768px).
- [x] Explicit `.oc-vol-nav a:focus-visible` ring (2px `--oc-accent`) added.
- [x] `.tier::before` side-stripe removed; replaced with tinted border +
      background per tier level (anti-pattern cleanup).
- [x] `.haz--level-4` box-shadow converted from hard-coded `rgba` to `color-mix`
      from the active `--haz-4-border` token (dark-mode-aware).
- [x] `@media (forced-colors: active)` block: `forced-color-adjust: none` on
      `.haz` preserves safety palette in Windows High Contrast mode.
- [x] `@media (prefers-reduced-motion: reduce)` block: zeroes transitions on
      body, sidebar, toggle, all nav elements, and skip link.
- [x] `@media print`: `.haz::before` stripe hidden; `border-width: 2px`;
      `box-shadow: none`. Print output: hazard borders retained, readable.
- [x] `loading="lazy"` added to all three schematic `<img>` tags.
- [x] Font preloads (`<link rel="preload">`) for Vollkorn and Chivo roman faces.
- [x] Hazard banner `aria-label` and icon `alt` now include severity label name
      ("Low Risk / Moderate / Significant / Lethal Danger").
- [x] Hazard banner markup and `--haz-*` tokens protected in `CLAUDE.md` against
      future style-skill edits.
- [x] Dark mode: all hazard levels verified correct; `.haz--level-4` shadow fixed.
- [x] No-JS: fully usable at all viewport sizes via `<noscript>` nav fallback.
- [x] `hazard_label` context variable added to `build.py`; `HAZARD_LABELS` dict.
- [x] `font_vollkorn` / `font_chivo` context variables added to `build.py`.
- [x] 216 tests pass throughout.

**Exit:** audit score 20/20; no P0–P3 accessibility issues outstanding; print +
dark mode + no-JS + reduced-motion + forced-colors all verified. ✅

---

## Milestone 7 — Release engineering & 1.0.0 cut

- [x] Confirm CI (`build.yml`, `pages.yml`, `release.yml`) is green on `main`.
- [x] Confirm the release workflow produces `salvage-vX.Y.Z.tar.gz` and attaches it
      to the tag, with shared assets bundled (no CDN deps in the artifact).
- [x] Smoke-test the tarball against the nginx path contract in
      `HEARTH-INTEGRATION.md` (`/salvage/...` paths stable, footer license/attribution reachable).
- [x] Update the pinned `version:` example in `HEARTH-INTEGRATION.md` to `v1.0.0`.
- [x] Tag `v1.0.0` and verify the release artifact downloads and serves clean.

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

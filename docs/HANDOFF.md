# Handoff — Salvage Electronics content authoring

You are picking up an in-progress content-authoring effort on the **Salvage
Electronics** static site (a Markdown-to-HTML guide for salvaging electronic
components). Read this whole file, then continue from "Your task" below.

## Repo & branch

- Repo root: `/home/user/salvage` (git repo for `trydydd/salvage`).
- **Branch `feature/image-pipeline` is complete and unmerged.** If it has not
  yet been merged to `main`, open a PR or merge it first before starting
  Milestone 6 work.
- For Milestone 6, create `feature/design-audit` from the HEAD of
  `feature/image-pipeline` (or `main` if it has already been merged).
- Push with `git push -u origin <branch>`, retrying with backoff on network
  errors. Do NOT open a PR unless asked.
- End commit messages with the session link footer if your harness uses one.
  Do not put any model identifier in commits, code, or content.

## Read these first (project rules)

- `CLAUDE.md` — project constraints (no CDN deps, stable `/salvage/` URLs,
  theory links are hyperlinks only, hazard banner colors).
- `docs/STYLE-GUIDE.md` — voice (active second person, workshop register, no
  exclamation marks, specs as ranges, four-column donor tables, pair every
  hazard with a procedure). Also contains the `## Images` section added in
  Milestone 5 (SVG for schematics, WebP/JPEG ≤ 100 kB for photos).
- `docs/ROADMAP.md` — the milestone plan to 1.0.0. This is the source of truth
  for what's next.
- `docs/HEARTH-INTEGRATION.md` — the Open Circuits cross-reference map (which
  `/open-circuits/...` chapter each topic links to). Never link `EXP_1.html`
  (intro) or `EXPER_1.html` (never existed); tests enforce this.
- `TODO.md` — has a "Needs Human Review" section tracking Claude-authored pages.

## Authoring skills (use them — don't freehand)

There are project skills that encode the structure/voice for each page type.
Invoke the matching one with the target file path as the argument:

- `write-foundation`, `write-donor-guide`, `write-project`, `write-component`
- `review-technical` — fact-checks a page; has a "Resolve mode" for existing
  `⚠️ FACT-CHECK` markers and writes flagged items to `FACT-CHECKS.md`.
- `i-audit` — design/accessibility audit; use for Milestone 6.

The donor-guide stubs already contain a finished component **table** and theory
links — preserve those exactly. You may add rows to the table if genuinely
useful parts are missing, but do not remove or alter existing rows. Replace
only the `## TODO:` sections, and strip the `TODO:` prefix from the heading
text (keep the rest of the heading).

**The authoring skills now automatically add the `author`/`review` frontmatter
fields.** You do not need to add them manually — the skill's Step 7 handles it.
Still add the page to the "Needs Human Review" list in `TODO.md` after writing.

## Conventions established this session (follow them)

1. **One page per turn.** Author a single page, then build + test + commit +
   push before moving on. The environment has intermittent shell-output
   corruption and idle timeouts; small turns keep losses to one page max.
2. **Verify writes with the Read tool, not just shell echo.** A `Write` was
   silently corrupted once in a prior session (10k garbage lines). After
   writing, check line count and the last line; if a file looks wrong, rewrite.
3. **Preserve stub headings exactly.** Don't invent heading text. Diff against
   the committed stub (`git show HEAD:<path>`) if a Read looks garbled.
4. **Style guardrails** (lint each file before commit):
   - No em dashes or semicolons in prose (semicolons OK in table cells).
   - No banned AI vocab (crucial, robust, comprehensive, leverage, seamless,
     navigate, realm, tapestry, pivotal, testament, foster, vibrant, etc.).
   - Specific numbers/ranges over vague intensifiers. Use contractions.
   - Every hazard gets a concrete procedure.
   - Em dashes occasionally survive the first write despite the skill's rules.
     The lint step always catches them — fix before committing.

## Schematic generation (Milestone 5 conventions)

Schematics live in `build/schematics/` and write SVGs to `content/images/`.
Each script is standalone: `python build/schematics/continuity_tester.py`.

Hand-drawn style uses matplotlib's xkcd renderer — NOT a schemdraw flag:

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import schemdraw
schemdraw.use("matplotlib")

plt.xkcd()
with schemdraw.Drawing() as d:
    # add elements
    d.save("output.svg")
plt.close("all")
```

The `canvas='svg'` / `handdrawn=True` API mentioned in older docs does not
exist in schemdraw 0.23. Use the pattern above.

Battery polarity: place `−` at `batt.istart` and `+` at `batt.iend` (these
are the plate anchors, not the wire endpoints). Offset 0.2 upward with `ofst`.
For the `−` label, shift left by 0.75 units: `(batt.istart.x - 0.75, batt.istart.y)`.

Parallel circuits: ensure both branches span the same horizontal width between
junctions, otherwise the closing vertical wire won't align and the probe
terminals won't read as open ends.

## Build / test / verify commands

```sh
make build                     # render content/ -> output/html/ (37 pages)
.venv/bin/pytest -q            # 216 tests; or `make test`
```

`.venv` is present. Shared assets may need re-fetching at the start of a new
container session — run `make fetch` if `make build` complains about missing
shared assets. Quick lint for a file:

```sh
f=content/donor-guides/09-led-bulbs.md
echo "TODO: $(grep -c TODO "$f") | em-dashes: $(grep -c '—' "$f")"
grep -n ';' "$f" | grep -v '^\s*|'   # prose semicolons (table cells are OK)
wc -l "$f"; tail -1 "$f"
```

## Status — what's done vs. remaining

**Done:**
- Milestones 0–5 complete.
- Milestone 0: resolved 4 `FACT-CHECK` markers; `FACT-CHECKS.md` emptied.
- Milestone 1 (Foundations): all 4 pages authored + fact-checked.
- Milestone 2 (Donor guides): all 13 authored; six `review-technical` findings
  resolved with maintainer confirmation.
- Milestone 3 (Projects): all 6 authored; `review-technical` pass cleared 6
  critical errors + 1 fact-check item.
- Milestone 4 (Technical QA): `review-technical` run over all 10 component
  pages and all 4 foundation pages. Fixes: EIA-96 multiplier code, cap
  derating tightened to 70% + reform procedure added, LED/photodiode Vf
  thresholds split, LM317 floating-adjust corrected, duplicate part number
  fixed, SMD inductor footprint sizes corrected (2020≈5mm, 1210≈3mm), relay
  coil scan range raised to 50–1500Ω. `FACT-CHECKS.md` is empty.
- **Milestone 5 (Images & diagrams) complete** on branch `feature/image-pipeline`:
  - `docs/STYLE-GUIDE.md` `## Images` section added.
  - `build/build.py` `copy_images()` step added.
  - `schemdraw>=0.19` and `matplotlib>=3.7` added to `requirements.txt`.
  - Three hand-drawn schematics: continuity tester, cap discharge tool, ATX
    bench supply. Scripts in `build/schematics/`; SVGs in `content/images/`;
    embedded in project pages with `<figure>`/`<img>`/`<figcaption>`.
  - `test_no_external_image_urls` added to `tests/test_content.py`.
  - **216 tests pass.**

**Remaining content:** none — no `## TODO` stubs anywhere in `content/`.

**Outstanding review:** every authored page still carries
`review: Needs Human Review` (see `TODO.md`) — a human SME pass is owed before
1.0.0, separate from the automated fact-check passes.

**Next per ROADMAP:** Milestone 6 = design, accessibility & print pass.

## Your task

Begin Milestone 6: design, accessibility, and print pass.

The ROADMAP lists four concrete deliverables:

1. **Run `i-audit`** — triage all P0 and P1 findings. Fix what can be fixed
   programmatically (CSS, template, overlay). Log anything requiring human
   design decisions as comments in the relevant file or a new `DESIGN-NOTES.md`.

2. **Verify light/dark mode** — `prefers-color-scheme` dark mode should render
   cleanly. Check that hazard banners use the standard safety palette (greens/
   yellows/oranges/reds), not the Open Circuits accent colors.

3. **Verify no-JS usability** — the site must be fully readable with JavaScript
   disabled. Navigation collapse and any salvage-nav.js features should
   degrade gracefully.

4. **Verify print output** — hazard borders should be retained, banner box
   shadows removed, type readable. Check with a browser print preview or
   `@media print` inspection.

Work one deliverable at a time: fix, build, test, commit, push before
moving to the next.

**Lint reminders:** no em dashes or prose semicolons in any new Markdown content;
no banned AI vocab; check with `grep -c '—'` and `grep -n ';'` before committing.

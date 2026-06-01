# Handoff — Salvage Electronics content authoring

You are picking up an in-progress content-authoring effort on the **Salvage
Electronics** static site (a Markdown-to-HTML guide for salvaging electronic
components). Read this whole file, then continue from "Your task" below.

## Repo & branch

- Repo root: `/home/user/salvage` (git repo for `trydydd/salvage`).
- **Work only on branch `feature/image-pipeline`.** Create it locally from
  the current HEAD of `claude/m4-review-technical` if missing;
  never push to `main` without explicit permission.
- Push with `git push -u origin feature/image-pipeline`,
  retrying with backoff on network errors. Do NOT open a PR unless asked.
- End commit messages with the session link footer if your harness uses one.
  Do not put any model identifier in commits, code, or content.

## Read these first (project rules)

- `CLAUDE.md` — project constraints (no CDN deps, stable `/salvage/` URLs,
  theory links are hyperlinks only, hazard banner colors).
- `docs/STYLE-GUIDE.md` — voice (active second person, workshop register, no
  exclamation marks, specs as ranges, four-column donor tables, pair every
  hazard with a procedure).
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

## Build / test / verify commands

```sh
make build                     # render content/ -> output/html/ (37 pages)
.venv/bin/pytest -q            # 179 tests; or `make test`
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
- Milestones 0–4 complete (all pushed through `claude/m4-review-technical`).
- Milestone 0: resolved 4 `FACT-CHECK` markers; `FACT-CHECKS.md` emptied.
- Milestone 1 (Foundations): all 4 pages authored + fact-checked.
- Milestone 2 (Donor guides): all 13 authored; six `review-technical` findings
  resolved with maintainer confirmation.
- Milestone 3 (Projects): all 6 authored; `review-technical` pass cleared 6
  critical errors + 1 fact-check item.
- **Milestone 4 (Technical QA) complete:** `review-technical` run over all 10
  component pages and all 4 foundation pages. Fixes: EIA-96 multiplier code,
  cap derating tightened to 70% + reform procedure added, LED/photodiode Vf
  thresholds split, LM317 floating-adjust corrected, duplicate part number fixed,
  SMD inductor footprint sizes corrected (2020≈5mm, 1210≈3mm), relay coil scan
  range raised to 50–1500Ω. `FACT-CHECKS.md` is empty. 179 tests pass.

**Remaining content:** none — no `## TODO` stubs anywhere in `content/`.

**Outstanding review:** every authored page still carries
`review: Needs Human Review` (see `TODO.md`) — a human SME pass is owed before
1.0.0, separate from the automated fact-check passes.

**Next per ROADMAP:** Milestone 5 = images and diagrams.

## Your task

Begin Milestone 5: define and implement the image/diagram pipeline.

The ROADMAP lists four concrete deliverables:

1. **Define conventions** — SVG for schematics and pinouts; aggressively
   compressed raster (JPEG ≤ 100 kB, WebP preferred) for photos. Document
   the rules in a new `## Images` section in `docs/STYLE-GUIDE.md`.

2. **Build-pipeline support** — `build/build.py` currently copies only shared
   assets. Add a step that copies `content/images/` (or a `content/` subdirectory
   of your choice) into `output/html/` alongside the rendered pages, so
   `<img src="../images/foo.svg">` links work without CDN deps. Confirm the copy
   lands in the right place with `make build` and update `make test` as needed.

3. **Three minimum schematics** — the project pages that need a diagram to be
   buildable from the page alone are:
   - `content/projects/01-continuity-tester.md`
   - `content/projects/02-cap-discharge-tool.md`
   - `content/projects/03-atx-bench-supply.md`

   Use **schemdraw** (pip install `schemdraw`) with its hand-drawn style. The
   hand-drawn rendering fits the site's workshop/zine aesthetic better than
   clean geometric lines, and it's a single flag in the API:
   `with schemdraw.Drawing(canvas='svg') as d: d.push()` ... then call
   `d.draw(handdrawn=True)` before saving. See the style gallery at
   https://schemdraw.readthedocs.io/en/latest/gallery/styles.html#hand-drawn

   Write a separate generation script for each schematic:
   - `build/schematics/continuity_tester.py`
   - `build/schematics/cap_discharge.py`
   - `build/schematics/atx_bench_supply.py`

   Each script should write its output SVG to `content/images/` and be
   runnable standalone (`python build/schematics/continuity_tester.py`).
   Add `schemdraw` to `requirements.txt` (or equivalent). Embed the generated
   SVGs in the project pages using a `<figure>` / `<img>` / `<figcaption>`
   block with a descriptive `alt` attribute.

4. **Offline-first check** — confirm no image references point to external URLs.
   The existing test infrastructure should cover this if you add a test for it;
   add one if it's missing.

Work one deliverable at a time: code/write, build, test, commit, push before
moving to the next. Branch: `feature/image-pipeline` off `claude/m4-review-technical`.

**Lint reminders:** no em dashes or prose semicolons in any new Markdown content;
no banned AI vocab; check with `grep -c '—'` and `grep -n ';'` before committing.

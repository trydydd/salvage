# Handoff — Salvage Electronics content authoring

You are picking up an in-progress content-authoring effort on the **Salvage
Electronics** static site (a Markdown-to-HTML guide for salvaging electronic
components). Read this whole file, then continue from "Your task" below.

## Repo & branch

- Repo root: `/home/user/salvage` (git repo for `trydydd/salvage`).
- **Work only on branch `claude/project-handoff-continuation-C67bD`.** Create it
  locally if missing; never push to `main` without explicit permission.
- Push with `git push -u origin claude/project-handoff-continuation-C67bD`,
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

**Done (all pushed to `claude/project-handoff-continuation-C67bD`):**
- Milestone 0: resolved 4 `FACT-CHECK` markers in `05-mosfets.md` /
  `08-relays.md`; `FACT-CHECKS.md` emptied.
- Added `docs/ROADMAP.md`; added safety→`DC_3.html` link + map row in
  `HEARTH-INTEGRATION.md`.
- **Milestone 1 (Foundations) complete:** `01-why-salvage`, `02-safety`,
  `03-tools-and-workspace`, `04-core-techniques` — all authored + flagged.
- **Milestone 2 (Donor guides) complete:** all 13 authored. The 10 stubs
  (`01-battery-devices`, `02-wall-chargers`, `03-routers-modems`, `04-printers`,
  `05-desktop-computers`, `08-audio-equipment`, `09-led-bulbs`,
  `10-microwave-ovens`, `11-crt-monitors`, `12-ups-units`) were authored +
  flagged; `06-laptops`, `07-atx-power-supplies`, `13-solar-fence-chargers`
  were already-complete exemplars. The three hazard-4 guides (microwave, CRT,
  UPS) each lead with an explicit discharge/isolation procedure.
- Updated all four authoring skills to auto-add `author`/`review` frontmatter.
- **Fact-check pass over the donor guides:** resolved six `review-technical`
  findings with maintainer confirmation — microwave stored-cap voltage (~2.8 kV
  peak), audio filter-cap range, printer carriage-motor voltage (12–24 V),
  laptop blower fan (5 V norm / 12 V gaming), two solar-charger storage-cap items.
- **Safety/liability disclaimer added** to `README.md`, the site home page
  (`content/index.md`), and `content/foundations/02-safety.md`.
- **Milestone 3 (Projects) complete:** all 6 project build guides authored with
  `write-project`, linted (no em dashes, no prose semicolons), built, and tested.
  Pages: `01-continuity-tester`, `02-cap-discharge-tool`, `03-atx-bench-supply`,
  `04-component-tester-jig`, `05-usb-charger`, `06-led-lamp`.
- **`review-technical` pass over all project pages:** 6 critical errors corrected
  (LED Vf diode-mode range, cap energy upper bound, ATX extension resistor wattage,
  NPN transistor test LED polarity, LED strip group count, reversed-polarity claim).
  1 fact-check resolved with maintainer confirmation (+12 V ATX floor = 11.4 V per
  ATX12V V2.2 Design Guide, Section 3.2.1 / Table 2). `FACT-CHECKS.md` is empty.

**Remaining content:** none — no `## TODO` stubs anywhere in `content/`.

**Outstanding review:** every authored page still carries
`review: Needs Human Review` (see `TODO.md`) — a human SME pass is owed over all
foundations, donor guides, and projects before 1.0.0, separate from the
automated fact-check passes.

**Next per ROADMAP:** Milestone 4 = complete the technical/QA review pass.
The `review-technical` skill still needs to run over the component pages
(`content/components/`) and the foundation pages (`content/foundations/`).
After that: Milestone 5 (images), Milestone 6 (accessibility audit), Milestone 7
(release).

## Your task

Continue Milestone 4: run `review-technical` over the remaining pages that
haven't had a pass yet:

1. `content/components/` — 10 pages. Two (`05-mosfets.md`, `08-relays.md`)
   already had specific fact-check items resolved in earlier sessions but have
   not had a full `review-technical` pass. Run the skill on all 10.
2. `content/foundations/` — 4 pages. Safety-critical; run the skill on
   `02-safety.md` first.

For each batch: invoke `review-technical` with the directory path (or file by
file for the foundation pages), apply critical fixes, add fact-check markers for
uncertain items, update `FACT-CHECKS.md`, then commit and push. Resolve any
fact-check markers immediately if you can confirm them from the calibration
reference in the skill itself; flag the rest for maintainer input.

Keep `FACT-CHECKS.md` empty at the end of each session if possible — resolve
or defer, don't accumulate.

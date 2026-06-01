# Handoff — Salvage Electronics content authoring

You are picking up an in-progress content-authoring effort on the **Salvage
Electronics** static site (a Markdown-to-HTML guide for salvaging electronic
components). Read this whole file, then continue from "Your task" below.

## Repo & branch

- Repo root: `/home/user/salvage` (git repo for `trydydd/salvage`).
- **Work only on branch `feature/projects`.** Create it
  locally if missing; never push to `main` without explicit permission.
- At handoff time HEAD is `ee4a72e` ("Add safety/liability disclaimer to
  README, home page, and safety page"), working tree clean, branch pushed and
  in sync with origin.
- Push with `git push -u origin claude/project-evaluation-next-steps-gBojG`,
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

**Done (all pushed):**
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
- **Fact-check pass over the donor guides (this session):** resolved six
  `review-technical` findings with maintainer confirmation — microwave stored-cap
  voltage (~2.8 kV peak, not 2000 V RMS), audio filter-cap range, printer
  carriage-motor voltage (12–24 V + bench-test note), laptop blower fan
  (5 V norm / 12 V gaming), and two solar-charger storage-cap items.
  `FACT-CHECKS.md` is empty.
- **Safety/liability disclaimer added** to `README.md`, the site home page
  (`content/index.md`), and `content/foundations/02-safety.md`.

**Remaining content:** the 6 project stubs in `content/projects/` are still
`## TODO:` scaffolds (~21 lines each). Everything else is authored.

**Outstanding review:** every authored page still carries
`review: Needs Human Review` (see `TODO.md`) — a human SME pass is owed over all
foundations + donor guides before 1.0.0, separate from the fact-check pass.

**Exemplars to match for depth/voice (~2000 words):**
`06-laptops.md`, `07-atx-power-supplies.md`, `13-solar-fence-chargers.md`.

**Next per ROADMAP:** Milestone 3 = author the 6 project stubs in
`content/projects/` with `write-project` (one per turn). Then M4 technical/QA
review, M5 images, M6 accessibility/print audit, M7 release + tag 1.0.0.

## Your task

Start Milestone 3: author the 6 project build guides one per turn, using
`write-project`. Order: `01-continuity-tester`, `02-cap-discharge-tool`,
`03-atx-bench-supply`, `04-component-tester-jig`, `05-usb-charger`, `06-led-lamp`.
For each: read the stub, invoke the skill, lint (em dashes are the most common
survivor), run `make build` + pytest, update `TODO.md`, then commit and push.

The cap-discharge tool and the ATX bench supply are safety-adjacent: link them
tightly to `content/foundations/02-safety.md` and the relevant donor guide, and
pair every stored-energy or mains hazard with a concrete procedure.

Start by reading `docs/STYLE-GUIDE.md` and an exemplar
(`07-atx-power-supplies.md`), then begin with `01-continuity-tester.md`.

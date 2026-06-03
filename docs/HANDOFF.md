# Handoff — Salvage Electronics release engineering

You are picking up an in-progress effort on the **Salvage Electronics** static
site (a Markdown-to-HTML guide for salvaging electronic components). Read this
whole file, then continue from "Your task" below.

## Repo & branch

- Repo root: `/home/user/salvage` (git repo for `trydydd/salvage`).
- **Branch `feature/design-audit` is complete and unmerged.** If it has not yet
  been merged to `main`, open a PR or merge it first before starting Milestone 7
  work.
- For Milestone 7, create `feature/release-engineering` from the HEAD of
  `feature/design-audit` (or `main` if it has already been merged).
- Push with `git push -u origin <branch>`, retrying with backoff on network
  errors. Do NOT open a PR unless asked.
- End commit messages with the session link footer if your harness uses one.
  Do not put any model identifier in commits, code, or content.

## Read these first (project rules)

- `CLAUDE.md` — project constraints (no CDN deps, stable `/salvage/` URLs,
  theory links are hyperlinks only, hazard banner protection).
- `docs/STYLE-GUIDE.md` — writing voice and table conventions.
- `docs/ROADMAP.md` — the milestone plan to 1.0.0. Source of truth for what
  is next.
- `docs/HEARTH-INTEGRATION.md` — path stability contract and nginx deployment
  instructions. The release smoke-test uses this document.

## Build / test / verify commands

```sh
make fetch                     # pull shared Open Circuits assets (needed once per container session)
make build                     # render content/ -> output/html/ (37 pages)
.venv/bin/pytest -q            # 216 tests; or `make test`
```

`.venv` is present. Run `make fetch` first if `make build` complains about
missing shared assets — shared assets are not committed and must be fetched
each fresh container session.

## Status — what's done vs. remaining

**Done:**
- Milestones 0–6 complete.
- Milestone 0: resolved 4 `FACT-CHECK` markers; `FACT-CHECKS.md` emptied.
- Milestone 1 (Foundations): all 4 pages authored + fact-checked.
- Milestone 2 (Donor guides): all 13 authored; `review-technical` pass done
  (markers cleared with maintainer confirmation).
- Milestone 3 (Projects): all 6 authored; `review-technical` pass cleared 6
  critical errors + 1 fact-check item.
- Milestone 4 (Technical QA): `review-technical` over all component and
  foundation pages. `FACT-CHECKS.md` is empty.
- Milestone 5 (Images & diagrams): three hand-drawn schematics, `copy_images()`
  build step, schemdraw dependencies, `test_no_external_image_urls`. 216 tests.
- **Milestone 6 (Design, accessibility & print) complete** on branch
  `feature/design-audit` — audit score 20/20:
  - Skip link + `#main-content` anchor. `aria-current="page"` on active nav.
  - `<noscript>` fallback section nav (mobile no-JS coverage, 44px targets).
  - Nav toggle 44px, `.oc-vol-nav a` 44px at tablet widths (481–768px).
  - Explicit `:focus-visible` ring on all interactive elements.
  - `.tier` anti-pattern cleaned: tinted border + background, no `::before` stripe.
  - `.haz--level-4` shadow uses `color-mix` from token (dark-mode-aware).
  - `@media (forced-colors: active)` with `forced-color-adjust: none` on `.haz`.
  - `@media (prefers-reduced-motion: reduce)` zeroes all transitions.
  - Print: `.haz::before` hidden, `border-width: 2px`, `box-shadow: none`.
  - `loading="lazy"` on all three schematic images.
  - Font preloads (`<link rel="preload">`) for Vollkorn and Chivo.
  - Hazard banner `aria-label` and `alt` include severity label name.
  - `CLAUDE.md` now explicitly protects hazard banner markup and `--haz-*`
    tokens from style-skill edits.
  - `hazard_label`, `font_vollkorn`, `font_chivo` added to build context.
  - 216 tests pass throughout.

**Remaining content:** none — no `## TODO` stubs anywhere in `content/`.

**Outstanding review:** every authored page carries `review: Needs Human Review`
(see `TODO.md`) — a human SME pass is owed before 1.0.0, separate from the
automated fact-check passes. This is a human task, not an agent task.

**Next per ROADMAP:** Milestone 7 = release engineering & 1.0.0 cut.

## Conventions established across sessions (follow them)

1. **Build + test + commit + push each logical unit.** The environment has
   intermittent idle timeouts; small atomic commits keep losses to one change max.
2. **Run `make fetch` at the start of each fresh container session** before
   `make build` — shared assets are not in the repo and are absent in new containers.
3. **No model identifier in commits, code, or content** — ever.
4. **Lint reminders for any content edits:** no em dashes or prose semicolons;
   no banned AI vocab; check with `grep -c '—'` before committing.
5. **`salvage.css` overrides the shared `open-circuits.css`** — never edit shared
   CSS directly. All Salvage-specific overrides go in `overlay/css/salvage.css`.
6. **Hazard banners are off-limits to style passes** — the `.haz` component,
   `--haz-*` tokens, level labels, `aria-label`, and icon `alt` text must not be
   altered by any aesthetic or style command. See `CLAUDE.md` for the full rule.

## Your task

Begin Milestone 7: release engineering and 1.0.0 cut.

The ROADMAP lists five concrete deliverables:

1. **Confirm CI is green on `main`** — check `build.yml`, `pages.yml`, and
   `release.yml` workflows. All must pass on the HEAD of `main` (or the merged
   feature branch). Fix any failures before proceeding.

2. **Confirm the release workflow produces the artifact** — `release.yml` should
   produce `salvage-vX.Y.Z.tar.gz` and attach it to the tag, with shared assets
   bundled (no CDN deps in the tarball). Trigger a dry run or inspect the workflow
   to verify this is wired correctly.

3. **Smoke-test against the Hearth path contract** — check
   `docs/HEARTH-INTEGRATION.md` for the nginx path requirements (`/salvage/...`
   paths must be stable). Verify the build output matches: index at `index.html`,
   sections at `foundations/`, `donor-guides/`, `components/`, `projects/`.
   Verify `LICENSE.txt` and `ATTRIBUTION.md` are present at the output root.

4. **Update the pinned version example in `HEARTH-INTEGRATION.md`** — find the
   `version:` example currently set to a placeholder or old value; update it to
   `v1.0.0`.

5. **Tag `v1.0.0` and verify** — once the above are confirmed, tag `v1.0.0`,
   push the tag, and verify the release artifact is downloadable and serves clean.

Work one deliverable at a time: verify, fix if needed, commit, push before
moving on.

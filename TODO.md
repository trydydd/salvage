# TODO

Future work explicitly deferred from Section 12 of `salvage-electronics-plan.md`:

- [ ] Replace content stubs with full human-authored content across the site.
- [ ] Add specific make/model teardowns under `content/donor-guides/teardowns/`.
- [ ] Implement ZIM packaging support, including a future `build/build_zim.py`.
- [ ] Add GitHub Actions workflows after the local build pipeline is stable.
- [ ] Add site-wide search as a Phase 2 feature.
- [ ] Define and implement a content image strategy for schematics and photos, with SVG preferred for schematics and aggressive compression for offline-friendly photos.

## Needs Human Review

Pages drafted by Claude (`author: Claude`, `review: Needs Human Review` in frontmatter). A human subject-matter expert should verify technical accuracy and safety guidance, then clear the `review` field once approved.

- [ ] `content/foundations/01-why-salvage.md`
- [ ] `content/foundations/02-safety.md` — safety-critical; review first.
- [ ] `content/foundations/03-tools-and-workspace.md`
- [ ] `content/foundations/04-core-techniques.md`
- [ ] `content/donor-guides/01-battery-devices.md`
- [ ] `content/donor-guides/02-wall-chargers.md`
- [ ] `content/donor-guides/03-routers-modems.md`
- [ ] `content/donor-guides/04-printers.md`
- [ ] `content/donor-guides/05-desktop-computers.md`
- [ ] `content/donor-guides/09-led-bulbs.md`
- [ ] `content/donor-guides/08-audio-equipment.md`
- [ ] `content/donor-guides/10-microwave-ovens.md` — safety-critical (lethal HV cap); review first.
- [ ] `content/donor-guides/11-crt-monitors.md` — safety-critical (anode charge, implosion); review first.
- [ ] `content/donor-guides/12-ups-units.md` — safety-critical (live battery short-circuit current, acid); review first.

Also touched this session (corrected, not authored — no frontmatter flag):

- [ ] `content/components/05-mosfets.md` — FACT-CHECK 5/6/7 resolved (body-diode Vf, STP75NF75, IRF9540N).
- [ ] `content/components/08-relays.md` — FACT-CHECK 5 resolved (contact-resistance threshold).

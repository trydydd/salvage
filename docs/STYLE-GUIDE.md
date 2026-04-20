# Style Guide

Writing standards for Salvage Electronics.

---

## Voice

Write in active, second-person prose.

- Say `Flip the board over.`
- Not `The board should be flipped.`

The guide should sound like a capable person talking to another capable person at the bench.

---

## Register

Keep the register workshop-y, tactile, and honest.

- Not academic.
- Not marketing-y.
- No exclamation marks.
- Prefer short paragraphs that still read well on a phone.

Warmth matters, but plain usefulness matters more.

---

## Safety Framing

State hazards plainly and without drama.

Always pair a hazard with a procedure:

- `The capacitor can hold a lethal charge; here's how to discharge it safely.`

Do not fear-monger, but do not soften real danger either.

---

## Tiered Techniques

When a page teaches a technique, show the range from no-tool to equipped.

Use the `.tier` callouts to present that ladder clearly. Never assume the reader has money, branded tools, or a full bench.

---

## Specs as Ranges

Prefer real-world ranges over false precision.

- `Electrolytic caps in ATX PSUs range 680µF to 2200µF.`
- Not `Use a 1000µF capacitor.`

The guide should describe what readers are likely to find in salvage, not pretend every donor device is identical.

---

## Cross-linking to Theory

Theory links always use absolute Open Circuits paths:

- `/open-circuits/DC/DC_5.html`
- `/open-circuits/Semi/SEMI_6.html`
- `/open-circuits/Exper/EXP_1.html`

Format them as short inline links, never footnotes.

Example:

`These are MOSFETs ([theory])` with `[theory]` linking to `/open-circuits/Semi/SEMI_6.html`.

Do not use relative links into Open Circuits.

---

## Tables

Donor guides use the four-column format below:

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Example part | Board location | What the reader can measure in hand | ★★★ |

Use the star scale exactly as:
- `★★★`
- `★★☆`
- `★☆☆`

The table should answer fast: what it is, where it lives, what can be verified, and whether it is worth the effort.

---

## Component Specs

Always give specs the reader can actually measure or observe.

Good examples:
- voltage rating
- polarity
- package
- connector family
- coil resistance
- continuity behavior

Avoid specs a casual salvager cannot verify from markings, a meter, or the part in hand.

---

## Celebrate the Salvage

When a part has a good second life, say so.

The tone should match Hearth's resourceful optimism: practical, generous, and pleased by reuse without turning that into moral pressure.

---

## Mistakes to Avoid

Do not:
- gatekeep by assuming expensive tools
- scare readers without giving a procedure
- moralize about e-waste
- assume prior knowledge when a short theory link would fix it

The guide should feel open-handed and usable on a real bench.

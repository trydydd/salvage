---
name: write-donor-guide
description: Write a complete donor-guide page from a stub. Use when the user wants to fill in a donor guide at content/donor-guides/NN-*.md.
version: 1.0.0
user-invocable: true
argument-hint: "[path/to/donor-guide-stub.md]"
---

Write a complete donor guide page for the salvage electronics site, replacing every `## TODO` section with real, usable content. The output must match the project's voice and conventions exactly.

## Step 1 — Read source files

Read all of these before writing anything:

1. The stub file passed as the argument (absolute or repo-relative path)
2. `docs/STYLE-GUIDE.md`
3. `docs/HAZARD-SYSTEM.md`
4. `content/donor-guides/_template.md`

Extract from the stub:
- `title` — the device type
- `hazard` — integer 1–4
- `hazard_summary` — the one-line worst-case statement
- All existing `## Heading` lines (preserve them exactly)
- Any existing theory links (preserve them exactly)

## Step 2 — Understand the hazard level

The hazard level controls the tone and content of safety sections:

- **Level 1** — Battery-powered consumer devices (remotes, small gadgets). No mains exposure. "Before You Open It" is brief: remove batteries, check for swelling.
- **Level 2** — Mains-powered but low-risk internally (chargers, routers, printers, laptops, LED drivers). "Before You Open It": unplug, wait 30 s for small caps. "Watch Out For": mostly mechanical — sharp edges, ribbon cables, spring clips.
- **Level 3** — Mains with substantial stored charge (ATX PSUs, audio amplifiers). "Before You Open It": unplug, wait several minutes, discharge bulk caps with a discharge tool before touching. "Watch Out For": detailed cap discharge procedure; call out capacitor markings and expected voltages.
- **Level 4** — Can retain lethal voltage after unplugging (microwaves, CRTs, large UPS units). "Before You Open It": strong warning up front, discharge procedures must be specific and step-by-step. "Watch Out For": lead with the worst-case consequence, then the safe-handling procedure. Never soften this section.

## Step 3 — Write each section

Produce content for all seven sections in order. Do not add sections or remove any. Preserve heading text exactly.

---

### What's Inside

Two to four short paragraphs. Describe the major circuit blocks and mechanical assemblies a reader will actually encounter when they open this device. Be specific to the device type — not generic electronics theory. Name real PCB types (switch-mode PSU board, RF front-end, motor driver, etc.). Mention physical features: form factor, screws, clips, heat sinks, board count. End with a sentence about why this device is worth salvaging.

---

### Before You Open It

Opens with an action list tailored to the hazard level (see Step 2). Use a numbered list for any procedure involving more than one step. Then a short paragraph of context if needed.

For all levels: "Unplug from mains and remove any batteries before opening."

Add level-appropriate detail on top. At level 3 or 4, describe exactly which components hold charge and what voltages to expect.

---

### What to Target

A four-column markdown table. Use this exact header:

```
| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
```

Six to ten rows. Each row:
- **Component**: The part name and type. Be specific (e.g. "Electrolytic cap", "NPN transistor", "Schottky diode", not just "capacitor").
- **Where**: Physical location on the board — named board, section, or landmark (e.g. "primary PSU board, near transformer", "logic board, flanking CPU", "output stage heatsink").
- **Specs**: What the reader can read or measure — voltage rating, capacitance, resistance, package type, connector family. Use ranges if values vary (e.g. "470–2200 µF, 6.3–25 V"). No theoretical specs the reader cannot verify.
- **Worth-it**: ★★★ (always pull), ★★☆ (pull if easy), ★☆☆ (only if you need it).

Favour high-worth-it items. Include at least two ★★★ rows.

---

### How to Get Them Out

Practical extraction techniques for the components listed in the table. Tiered by tool access:

- **No soldering iron**: What can be unclipped, unplugged, or snapped free without heat?
- **Soldering iron only**: Through-hole desoldering with solder wick or pump; how to avoid pad damage.
- **With desoldering station / hot air**: SMD part removal; stagger heat to avoid board warp.

Use short paragraphs or a bulleted list per tier. Name the specific components from the table where relevant (e.g. "The output rectifiers are through-hole — wick from below while holding the lead."). Include one or two tips specific to this device type (connector latches, hidden screws, foil shielding that must come off first, etc.).

---

### Watch Out For

A bulleted list. Three to six specific hazards for this device type. Each bullet: state the hazard plainly, then the mitigation in the same sentence or the next. No bullet should be just a warning without a procedure.

Match hazard level (see Step 2). For level 3–4, lead with the stored-energy hazard. Include at least one mechanical hazard (sharp edges, spring-loaded parts, fragile connectors). Include one chemical or thermal hazard if relevant (lead solder, burning insulation smell, swollen electrolyte, hot heatsinks).

---

### Theory Links

Keep any existing theory links from the stub exactly as written. If no links exist, add the appropriate subset from:

- DC measurements and continuity: `/circuits/DC/DC_5.html`
- Semiconductors and regulators: `/circuits/Semi/SEMI_6.html`
- Bench experiments and test fixtures: `/circuits/Exper/EXPER_1.html`

Write each as a short inline sentence, e.g.:

> For measuring DC voltages on salvaged boards, see [DC Measurements](/circuits/DC/DC_5.html).

---

### Specific Teardowns

One short paragraph explaining that device-specific teardowns (named make and model) live in a subdirectory and are linked here as they are added. Do not invent teardown links. Use this placeholder text:

> Specific make-and-model teardowns for [device type] will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

---

## Step 4 — Voice and style rules

Apply these throughout — they are non-negotiable:

- **Second person, active voice.** "Flip the board over" not "The board should be flipped."
- **No exclamation marks.** State urgency through specificity, not punctuation.
- **No moralizing.** Do not add sentences about why salvaging is good or bad. The reader already knows.
- **No gatekeeping.** Never suggest a reader needs more experience or better tools before trying something.
- **Pair every hazard with a procedure.** Never end a warning sentence without a mitigation.
- **Specs as ranges.** "6.3–25 V electrolytic caps" not "a 16 V capacitor."
- **Short paragraphs.** Three to five sentences maximum per paragraph. One idea per paragraph.
- **No marketing language.** No "excellent", "amazing", "great find." Be plain.

## Step 5 — AI writing antipatterns to avoid

These are the patterns Wikipedia's editors use to identify AI-generated text. Every one of them will make the output feel synthetic. Avoid them without exception.

**Banned vocabulary** — do not use these words; replace with plain, specific alternatives:
> delve, crucial, tapestry, landscape, pivotal, underscore, testament, intricate, meticulous, foster, navigate, realm, vibrant, noteworthy, bolstered, garner, enduring, interplay, additionally (as a sentence opener), comprehensive, robust, leverage, seamlessly, cutting-edge

**Banned adverb constructions** — do not use adverbs to describe physical properties or hazards in ways no person would say:
- "cuts fingers reliably" → "the edges are sharp enough to open skin"
- "effectively removes" → just "removes"
- "consistently damages" → say what happens and when
- "notably sharp" / "particularly dangerous" → name the specific hazard

The tell: if the adverb is doing the work of specificity (i.e. you could remove it and lose real information), replace it with actual detail. If it's just intensifying vaguely, cut it.

**Banned phrases:**
- "stands as a testament to" → say what it actually does
- "plays a vital/significant role" → say what role, specifically
- "it is worth noting that" → just say the thing
- "in conclusion" / "in summary" / "overall" → don't summarise; end when the content ends
- "not only X but also Y" → restructure the sentence
- "leaves a lasting impact" / "watershed moment" / "deeply rooted" → too vague; name the actual effect
- Trailing participle clauses: "...highlighting the importance of X", "...showcasing the value of Y" → cut them

**Banned structural patterns:**
- Bullet lists where every item has a bolded lead-in. Reserve bold for genuine key terms, not formatting every point.
- Every paragraph the same length. Vary sentence and paragraph rhythm.
- Em dashes in place of commas, colons, or parentheses. Use the right punctuation for the job.
- A summary or conclusion paragraph at the end that restates what was just said. End on content.
- Rule-of-three negative parallelisms: "No X. No Y. Just Z." — this is an AI tic; avoid it.
- Short imperative fragments used as emphasis beats after a longer sentence: "Start there.", "Do this first.", "Keep that in mind." — no one says these at a bench. Fold the instruction into the sentence it belongs to.
- Compressed spec-sheet constructions that strip the verb: "The fan is two to four screws" → "The fan is held by two to four screws" or "The fan will have two to four screws". Things are not their fasteners. Parts are not their specs. Keep the relationship explicit.

**Banned tone patterns:**
- Generic positive framing instead of specific facts. "A reliable source of useful components" → say which components, what specs, what donor board location.
- Treating ordinary information as uniquely significant. Not every cap is remarkable; say what makes this one worth pulling.
- Hedging preambles before stating something obvious: "It is important to remember that..." → say the thing directly.
- Inflated hazard language. "Extreme caution is advised" → say what the hazard is and what to do about it.

## Step 6 — Rhythm and structure

These rules address the deeper structural patterns that make AI writing feel robotic even after vocabulary and phrase problems are fixed.

**Sentence length must vary deliberately.** Mix short sentences (5–10 words) with longer ones. A short sentence after a dense technical clause creates rhythm and emphasis. Three sentences of similar length in a row is a tell — break the run. Single-sentence paragraphs are fine when the sentence earns it.

**Sections do not need equal depth.** If a point needs one sentence, write one sentence and stop. Do not pad to match adjacent sections. A 40-word Watch Out For bullet next to a 15-word one is realistic. Trying to make them match produces obvious filler.

**Tiered extraction sections should not be three equal-weight blocks.** Weight the tier where most of the actual work happens. If 80% of what's worth pulling comes out without a soldering iron, that tier gets the longest treatment. The hot-air tier might be two sentences if there's genuinely less to say.

**Bulleted lists do not need uniform bullet length.** One short bullet followed by a long one is correct if the content demands it. Forcing all bullets to the same length produces visible padding or compression.

**Use contractions.** "You'll", "don't", "it's", "that's", "there's". Their consistent absence in technical writing is a recognisable tell. A repair guide written by a person uses contractions naturally.

**Include at least one detail that only comes from having done this.** A specific latch mechanism that requires a pin to release. A cap that's always corroded on this donor type. A connector that looks identical to another but isn't. A common mistake that damages the part during removal. These sentences signal firsthand knowledge and cannot be generated from general training data alone.

**Acknowledge real variation between specimens.** Write "most ATX supplies", "some units", "older models", "in higher-wattage supplies" — not "ATX power supplies have X" as if all examples are identical. Real salvage is variable. The guide should reflect that.

**The author has a view.** When something is barely worth pulling, say so directly in the prose — don't just assign ★☆☆ and move on. "The PWM controller is only worth desoldering if you already know the part number and have a use for it" is more useful than silence. When one technique is clearly better, name it.

## Step 7 — Write the file

Produce the complete markdown file: frontmatter unchanged, then all seven sections with full content. Write it back to the same path that was passed as the argument.

Do not add any new headings, sections, or frontmatter fields. Do not remove any existing headings or theory links.

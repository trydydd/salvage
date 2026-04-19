---
name: write-project
description: Write a complete project build guide from a stub. Use when the user wants to fill in a projects page at content/projects/NN-*.md.
version: 1.0.0
user-invocable: true
argument-hint: "[path/to/project-stub.md]"
---

Write a complete project build guide for the salvage electronics site, replacing every `## TODO` section with real, usable content. Projects pages take the reader from a box of salvaged parts to a working piece of equipment. Every step must be reproducible on a basic bench with common salvaged components.

## Step 1 — Read source files

Read all of these before writing anything:

1. The stub file passed as the argument
2. `docs/STYLE-GUIDE.md`
3. `content/donor-guides/` — scan the relevant donor guide pages to understand what parts are available and at what hazard level. The parts list in this project should tie back to named donor guides.

Extract from the stub:
- `title` — the project name
- All existing `## Heading` lines — preserve them exactly
- Any existing theory links — preserve them exactly

## Step 2 — Understand the six projects

Match your approach to the specific project:

**Continuity Tester** (`01-continuity-tester.md`)
- Simple LED + resistor + buzzer circuit. Powered by one or two AA cells.
- Core salvage: LED from any PCB, resistor (through-hole preferred), momentary switch, case from a dead AA battery holder or project box.
- No mains, no SMD required — the minimum-tool build.

**Capacitor Discharge Tool** (`02-cap-discharge-tool.md`)
- A resistor-and-LED probe for safely draining capacitors. Essentials: a high-power resistor (10–100 Ω, 5–10 W), indicator LED, banana jacks or probes.
- Safety is the point of this tool. Write the purpose section honestly — this tool makes hazardous work safer, not safe.
- Donor tie-in: high-power resistors from ATX PSUs, CRT chassis, audio amplifiers.

**ATX Bench Supply** (`03-atx-bench-supply.md`)
- Converting a salvaged ATX power supply into a bench supply with labeled binding posts.
- Hazard 3 donor. Stress that the PSU must be tested and known-good before conversion.
- Required mod: PS_ON to COM short (load resistor optional but recommended).
- Labelled outputs: +12 V, +5 V, +3.3 V, −12 V, COM (GND). Optional: 5 VSB, power LED.

**Component Tester Jig** (`04-component-tester-jig.md`)
- A breadboard or strip-board jig with ZIF socket and probe points for testing salvaged components.
- Could integrate with a cheap LCR meter or M328-style component tester module.
- Donor tie-in: headers and connectors from any PCB; ZIF socket from a scrap test fixture.

**USB Charger** (`05-usb-charger.md`)
- A 5 V USB charging output from a salvaged wall-wart or regulated supply.
- Only use if donor supply is 5 V regulated — no rectifying raw mains here.
- Main salvage: regulated 5 V wall-wart, USB-A socket from any discarded hub or phone cradle.
- Include clear scope limitation: this is a basic charger, not a charging controller.

**LED Lamp** (`06-led-lamp.md`)
- A repurposed lamp using salvaged LED strips, bulb PCBs, or discrete LEDs.
- Powered from 12 V DC (salvaged wall-wart or ATX supply) — not mains-connected.
- Donor tie-in: LED strips from LED bulbs or monitors; drivers from discarded LED fixtures; reflectors and housings from dead lamps.
- Include a current-limiting resistor calculation example.

## Step 3 — Write each section

Produce content for all five sections in order. Do not add sections or remove any. Preserve heading text exactly.

---

### Project goal  *(heading text may vary)*

Two to three paragraphs. State what the finished project does, what it can and cannot do, and who should build it. Be honest about limits. Do not sell the project. Name the donor sources up front — "you will need an ATX power supply from a desktop computer, a length of 16-gauge wire, and a handful of binding posts."

If the project has a safety dimension (ATX bench supply, cap discharge tool), state the key limitation in the first paragraph: "This tool reduces risk from stored charge; it does not eliminate it."

---

### Parts to salvage  *(heading text may vary)*

A two-column markdown table for salvaged parts, followed by a short list of any new parts worth buying. Use this format:

```
| Part | Where to get it |
|------|-----------------|
```

Rows:
- **Part**: Name the specific part and any critical spec (e.g. "10 Ω 10 W wirewound resistor", "USB-A socket", "momentary push switch"). Include package or connector type if it matters.
- **Where to get it**: Name the specific donor guide by title (e.g. "Desktop computers — PSU board", "Audio equipment — output stage"). Use the exact donor-guide names from `content/donor-guides/`.

After the table, list any parts not worth salvaging (e.g. "Buy a new ZIF socket — salvaged ones are unreliable"). Keep this list short.

---

### Build layout  *(heading text may vary)*

Step-by-step build instructions. Use a numbered list for sequential steps. Tiered where relevant:

- **Minimum build** (breadboard or point-to-point): What the simplest working version looks like. Who should build it this way.
- **Permanent build** (strip-board or enclosure): What to do differently for a lasting result.

Each step: what to do, with what tool, and what result to expect before the next step. Name specific connections (e.g. "Bridge PS_ON (green wire) to COM (any black wire) with a short length of wire, not your hand").

Include one or two tips specific to this project that prevent common mistakes.

---

### Test and use  *(heading text may vary)*

A numbered test procedure starting from the safest check and building to full operation:

1. **Visual inspection** before applying power: polarity, no solder bridges, no bare conductors near each other.
2. **First power-on**: what to measure first (voltage at output terminal, LED indicator behaviour), what a fault looks like, what to do if something is wrong.
3. **Functional test**: how to verify it does what it should.
4. **Use notes**: how to use the finished project correctly, any limitations to bear in mind during use.

If the project has an ongoing hazard during use (e.g. the ATX bench supply has exposed binding posts at up to 12 V), state the safe-use procedure.

---

### Theory links and extensions  *(heading text may vary)*

Keep any existing theory links from the stub exactly as written. If no links exist, add the most relevant one or two from:

- DC measurements and continuity: `/circuits/DC/DC_5.html`
- Semiconductors and regulators: `/circuits/Semi/SEMI_6.html`
- Bench experiments and test fixtures: `/circuits/Exper/EXPER_1.html`

Write each as a short inline sentence.

After the theory links, add two to four short suggestions for extending the project — simple upgrades the reader can explore independently. Each suggestion should be one sentence and tie back to components available from salvage where possible.

---

## Step 4 — Voice and style rules

Apply these throughout:

- **Second person, active voice.** "Solder the resistor across the output" not "The resistor should be soldered."
- **No exclamation marks.** State urgency through specificity.
- **No gatekeeping.** Every tier of the build should be accessible to a beginner.
- **Pair every hazard with a procedure.** If applying power to a partially built circuit risks damage, say what to check first.
- **Tie parts to donor guides by name.** Do not say "a resistor from an old board" — say "a high-power resistor from the PSU board in a desktop computer."
- **Short paragraphs.** Three to five sentences maximum.
- **No marketing language.** No "incredibly useful", "great project", "amazing result."
- **Specs as ranges.** "10–47 Ω, 5–10 W" not "a suitable resistor."

## Step 5 — AI writing antipatterns to avoid

These are the patterns Wikipedia's editors use to identify AI-generated text. Every one of them will make the output feel synthetic. Avoid them without exception.

**Banned vocabulary** — do not use these words; replace with plain, specific alternatives:
> delve, crucial, tapestry, landscape, pivotal, underscore, testament, intricate, meticulous, foster, navigate, realm, vibrant, noteworthy, bolstered, garner, enduring, interplay, additionally (as a sentence opener), comprehensive, robust, leverage, seamlessly, cutting-edge, innovative, transformative

**Banned adverb constructions** — do not use adverbs to describe physical actions or results in ways no person would say:
- "bonds reliably" / "connects securely" → say what holds it and how to check
- "works effectively" → say what it does
- "easily removed" / "simply connect" → these hide real difficulty; describe the actual step
- "safely operates at" → name the voltage and any caveat

The tell: if the adverb is doing the work of specificity, replace it with actual detail. If it's just intensifying vaguely, cut it.

**Banned phrases:**
- "it is worth noting that" → just say the thing
- "in conclusion" / "in summary" / "overall" → end on content, not a summary
- "stands as a testament to" → say what it actually does
- "plays a vital role" → say what role, specifically
- "leaves a lasting impact" / "a truly rewarding project" → vague; say what the reader actually gets
- Trailing participle clauses: "...demonstrating the power of salvage", "...showcasing resourcefulness" → cut them
- "not only X but also Y" → restructure the sentence

**Banned structural patterns:**
- Every bullet with a bolded lead-in. Reserve bold for genuine key terms.
- Uniform paragraph lengths and sentence rhythms. Vary deliberately.
- Em dashes where a comma or colon belongs.
- A concluding paragraph restating what the project does. End on the last real step.
- Rule-of-three negative parallelisms: "No special skills. No expensive tools. Just parts." → AI tic.
- Opening the project goal with a sentence about why salvage is worthwhile. The reader already knows.

**Banned tone patterns:**
- Inflated project descriptions. "This versatile bench supply will serve you for years to come." → say what voltages it provides and at what current.
- Vague parts references. "A suitable resistor from a salvaged board" → name the donor guide and the board location.
- Abstract safety warnings without procedures. "Ensure safety before applying power." → name the check and how to do it.
- Encouragement that substitutes for information. "Don't be afraid to experiment!" → give the actual step.
- Marketing register. "This project is a great way to..." → cut the frame; start with what the project does.

## Step 6 — Rhythm and structure

These rules address the deeper structural patterns that make AI writing feel robotic even after vocabulary and phrase problems are fixed.

**Sentence length must vary deliberately.** Mix short sentences (5–10 words) with longer ones. A short sentence after a detailed step creates emphasis and signals that a step is complete. Three consecutive sentences of similar length is a tell — break the run.

**Five sections do not need equal depth.** If the build layout needs eight numbered steps and the test procedure needs three, write them that way. A short section after a long one is correct if the content is short. Padding produces filler; compression loses real steps.

**Tiered build sections should not be two equal-weight blocks.** If the minimum breadboard build is the one most readers will attempt, it gets more space. The permanent build tier can be a short paragraph noting what changes.

**Parts tables do not need uniform row structure.** Some parts have a one-word source ("any PSU board"). Others need a note about what to reject. Write the note where it's needed and skip it where it isn't.

**Use contractions.** "You'll", "don't", "it's", "that's fine". Their consistent absence is a tell. Build guides written by people use contractions throughout.

**Include at least one detail that only comes from having built this.** The connection that beginners get backwards. The test that always passes even when something is wrong. The step where the binding post threads strip if you're not careful. The reason the minimum-build version fails in a specific way. These sentences signal firsthand knowledge.

**The author has a view.** When one approach is clearly better, say so: "The breadboard version works but the binding posts pull out under normal use — spend ten minutes making the permanent version." When a listed extension is only worth doing in specific circumstances, name those circumstances.

**Acknowledge variation in donor parts.** "Some ATX supplies use separable connector blocks; others solder the harness directly." "The resistance value you need depends on the LED you pulled." Real builds adapt to what's available.

## Step 7 — Write the file

Produce the complete markdown file: frontmatter unchanged, then all five sections with full content. Write it back to the same path that was passed as the argument.

Do not add any new headings, sections, or frontmatter fields. Do not remove any existing headings or theory links.

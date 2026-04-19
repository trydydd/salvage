---
name: write-component
description: Write a complete component reference page from a stub. Use when the user wants to fill in a components page at content/components/NN-*.md.
version: 1.0.0
user-invocable: true
argument-hint: "[path/to/component-stub.md]"
---

Write a complete component reference page for the salvage electronics site, replacing every `## TODO` section with real, usable content. The reader is at a workbench with salvaged parts and a basic multimeter. Every sentence should help them identify, test, or reuse what's in their hand.

## Step 1 — Read source files

Read all of these before writing anything:

1. The stub file passed as the argument
2. `docs/STYLE-GUIDE.md`

Extract from the stub:
- `title` — the component type
- All existing `## Heading` lines — preserve them exactly
- Any existing theory links — preserve them exactly

## Step 2 — Write each section

Produce content for all five sections in order. Do not add sections or remove any. Preserve heading text exactly.

---

### Identify the part  *(heading text may vary — use whatever is in the stub)*

How to recognise this component by sight, before any measurement. Cover:

- **Package types**: Name the through-hole and SMD packages the reader will actually encounter on salvaged boards (DIP, TO-92, TO-220, SOT-23, 0805, axial, radial, etc.). Describe what they look like.
- **Markings**: What to read off the body — colour bands, printed codes, date codes, polarity marks. Give real examples of codes they will see (e.g. "104 = 100 nF", "1N4148", "NE555P"). Explain how to decode them.
- **Orientation cues**: Polarity stripe, bevelled edge, dot, notch, pin 1 mark. Where to look.
- **Common confusion**: What else looks similar and how to tell them apart.

Two to four paragraphs. Write for someone who has never seen this component type before, but is not stupid.

---

### Measure and confirm  *(heading text may vary)*

Hands-on test procedures using a basic multimeter. Write a numbered procedure for each test method, from least-tool to most-tool. Cover:

- **Multimeter continuity/diode mode**: What pins to probe, what reading to expect, what a failed part reads.
- **Resistance range check** (where applicable): Which range to set, what values are normal, what values indicate failure.
- **In-circuit vs out-of-circuit**: Note when the reader must desolder the part first, and why.
- **With an ESR meter or component tester** (where relevant and affordable): What extra information it gives.

Use specific numbers: "a good diode reads 0.4–0.7 V forward voltage in diode mode" not "the meter will show a reading." Use ranges, not false precision.

If there are multiple test methods, use a short heading or bold lead-in for each to make them easy to scan.

---

### Failure modes

What goes wrong with this component type when it fails, and how to detect each mode at the bench. Three to five failure modes, each as a short paragraph or tightly written bullet:

- **Name the failure**: Open circuit, short circuit, increased ESR, leakage, thermal runaway, gate oxide damage, etc.
- **What causes it**: Voltage spike, heat, age, reverse polarity, physical damage.
- **How to detect it**: What the multimeter reads, what it looks like (bulging top, burnt smell, cracked body, discoloured board under the part).
- **Whether it is safe to use**: Some failures are recoverable (dirty contacts on a relay); some make the part unsafe to reuse (swollen electrolytic, shorted MOSFET).

Do not soften this section. If a failed electrolytic cap can vent caustic electrolyte, say so.

---

### Reuse notes

Practical guidance on whether and how to use salvaged specimens. Cover:

- **What to prioritise pulling**: Which packages and value ranges are most useful to stock. Which are too integrated or too specialised to bother with.
- **Derating**: What fraction of the rated voltage/current/power to trust in a salvaged part (e.g. "derate electrolytic caps by 20% for voltage when using in a new build — a 25 V cap becomes an 18 V cap in practice").
- **Storage and labelling**: How to sort, label, and store what you pull (tape + marker, pill organiser, labelled bags, etc.). Mention what information must stay with the part (value, voltage, date pulled if electrolytic).
- **When not to reuse**: Any scenario where the risk outweighs the saving — electrolytic caps from failed switching supplies, parts with visible heat stress, etc.

Practical and direct. No moralising about waste or reuse.

---

### Theory links

Keep any existing theory links from the stub exactly as written. If no links exist, add the most relevant one or two from:

- DC measurements and continuity: `/circuits/DC/DC_5.html`
- Semiconductors and regulators: `/circuits/Semi/SEMI_6.html`
- Bench experiments and test fixtures: `/circuits/Exper/EXPER_1.html`

Write each as a short inline sentence, e.g.:

> To understand how this component behaves in a circuit, see [Semiconductors](/circuits/Semi/SEMI_6.html).

Do not add more than two theory links.

---

## Step 3 — Voice and style rules

Apply these throughout:

- **Second person, active voice.** "Probe the anode" not "the anode should be probed."
- **Specs as ranges.** "0.4–0.7 V" not "approximately 0.6 V." Real-world ranges, not datasheet nominal.
- **Only measurable specs.** Never include specs the reader cannot verify with basic tools.
- **No exclamation marks.** State urgency through specificity.
- **No gatekeeping.** Do not suggest experience or expensive tools are required.
- **Short paragraphs.** Three to five sentences max. One idea per paragraph.
- **No marketing language.** No "excellent", "handy", "great choice."
- **Pair hazards with procedures.** If a cap can retain charge, say how to discharge it before the next sentence.

## Step 4 — Write the file

Produce the complete markdown file: frontmatter unchanged, then all five sections with full content. Write it back to the same path that was passed as the argument.

Do not add any new headings, sections, or frontmatter fields. Do not remove any existing headings or theory links.

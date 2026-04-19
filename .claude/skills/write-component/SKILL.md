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

## Step 4 — AI writing antipatterns to avoid

These are the patterns Wikipedia's editors use to identify AI-generated text. Every one of them will make the output feel synthetic. Avoid them without exception.

**Banned vocabulary** — do not use these words; replace with plain, specific alternatives:
> delve, crucial, tapestry, landscape, pivotal, underscore, testament, intricate, meticulous, foster, navigate, realm, vibrant, noteworthy, bolstered, garner, enduring, interplay, additionally (as a sentence opener), comprehensive, robust, leverage, seamlessly, cutting-edge

**Banned adverb constructions** — do not use adverbs to describe physical properties or test results in ways no person would say:
- "measures reliably at 0.6 V" → "reads 0.5–0.7 V"
- "effectively indicates" → just "indicates"
- "consistently fails" → say what failure looks like
- "notably useful" / "particularly common" → name the specific case

The tell: if the adverb is doing the work of specificity, replace it with actual detail. If it's just intensifying vaguely, cut it.

**Banned phrases:**
- "it is worth noting that" → just say the thing
- "in conclusion" / "in summary" / "overall" → don't summarise; end when the content ends
- "plays a vital/significant role" → say what role, specifically
- "stands as a testament to" → say what it actually demonstrates
- "leaves a lasting impact" / "deeply rooted" → too vague; name the specific effect
- Trailing participle clauses: "...highlighting its importance", "...showcasing its versatility" → cut them
- "not only X but also Y" → restructure the sentence

**Banned structural patterns:**
- Bullet lists where every item has a bolded lead-in. Reserve bold for genuine key terms.
- Every paragraph the same length. Vary sentence and paragraph rhythm.
- Em dashes anywhere in prose. Use a comma, colon, or parenthesis instead. No exceptions.
- Semicolons in prose sentences. Split the sentence or use a comma. In table cells, semicolons are fine as spec-list separators.
- A summary paragraph restating what was just said. End on content.
- Rule-of-three negative parallelisms: "No X. No Y. Just Z." — this is an AI tic.
- Short imperative fragments used as emphasis beats: "Start there.", "Do this first.", "Keep that in mind." — fold the instruction into the sentence it belongs to.
- Compressed spec-sheet constructions: "The package is TO-220, three legs" → "TO-220 packages have three leads". Don't strip the verb to pack in specs. Keep the relationship between noun and attribute explicit.
- Burying prerequisites after the instruction that depends on them. State what the reader needs to do or remove first, then give the main step.
- Listing one test or removal method when two legitimate options exist. If the reader can test in-circuit or desoldered, or extract by heat-and-wiggle or with a pump, name both.

**Banned tone patterns:**
- Vague specs instead of real numbers. "A relatively high voltage" → "25–50 V". Always give the actual range.
- Generic framing: "These components are commonly found in many types of circuits." → say which circuits, where on the board.
- Inflated claims about salvage value: "These are extremely valuable finds." → say what they are actually worth and why.
- Hedging preambles: "It is important to note that..." / "Keep in mind that..." → say the thing directly.
- Treating the reader as a beginner who needs reminders to be careful — pair hazards with procedures and move on.

## Step 5 — Rhythm and structure

These rules address the deeper structural patterns that make AI writing feel robotic even after vocabulary and phrase problems are fixed.

**Sentence length must vary deliberately.** Mix short sentences (5–10 words) with longer ones. A short sentence after a dense technical clause creates emphasis. Three sentences of similar length in a row is a tell — break the run. Single-sentence paragraphs are fine when the sentence earns it.

**Five sections do not need equal depth.** If the failure modes section only has two things worth saying, say two things and stop. If the identification section needs four paragraphs, write four. Padding a short section to match a long one produces visible filler; compressing a long one to match a short one loses real information.

**Measurement procedures do not need uniform step counts.** If one test method has two steps and another has five, write them that way. Don't add filler steps to the short one or compress the long one.

**Use contractions.** "You'll", "don't", "it's", "probe it", "that's". Their consistent absence is a tell. A bench guide written by a person uses contractions.

**Include at least one detail that only comes from having done this.** A specific marking code that trips people up. A package that looks like another but measures differently. A failure mode that only shows up at operating temperature, not on the bench. A common desoldering mistake for this specific part type. These sentences cannot be generated from general training data alone.

**Acknowledge real variation.** "Most small-signal transistors", "in switchers you'll often find", "older through-hole parts typically". Not "transistors have a forward voltage of X" as if the bench will always confirm the textbook number.

**Name the legitimate shortcut — and the legitimate long way round.** AI assumes one correct outcome. Real bench writing names the faster path when it's valid, and also names when the slower path serves a different goal: testing in-circuit is fine for a quick check; desoldering first is fine if you want a clean measurement or the practice. Name both where they exist rather than implying one right procedure.

**The author has a view.** When a reuse case is genuinely marginal, say so: "Electrolytic caps from failed switching supplies are rarely worth the risk — the failure mode that killed the supply may have stressed them." When one test method is clearly better than another, name it and say why.

## Step 6 — Write the file

Produce the complete markdown file: frontmatter unchanged, then all five sections with full content. Write it back to the same path that was passed as the argument.

Do not add any new headings, sections, or frontmatter fields. Do not remove any existing headings or theory links.

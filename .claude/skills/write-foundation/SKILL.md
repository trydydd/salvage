---
name: write-foundation
description: Write a complete foundations page from a stub. Use when the user wants to fill in a foundations page at content/foundations/NN-*.md.
version: 1.0.0
user-invocable: true
argument-hint: "[path/to/foundation-stub.md]"
---

Write a complete foundations page for the salvage electronics site, replacing every `## TODO` section with real, usable content. Foundations pages are the entry point for new readers — they establish mindset, safety habits, and practical technique. Write plainly, without condescension. The reader may be a complete beginner or an experienced hobbyist; do not assume either.

## Step 1 — Read source files

Read all of these before writing anything:

1. The stub file passed as the argument
2. `docs/STYLE-GUIDE.md`

Extract from the stub:
- `title` — the page topic
- All existing `## Heading` lines — preserve them exactly
- Any existing theory links — preserve them exactly

## Step 2 — Understand the page role

The four foundations pages serve different purposes. Match your depth and tone to the page title:

**Why Salvage** (`01-why-salvage.md`)
- Sets expectations honestly. Not a manifesto. Not motivational.
- Explain what salvage work actually yields, the learning curve, the limits.
- Describe the kind of reader who gets the most from this guide.
- Show them how to navigate the four sections and when to consult theory links.

**Safety** (`02-safety.md`)
- The most important page on the site. Treat it that way without being dramatic.
- Every section covers one hazard category. Structure: name the hazard → explain the mechanism (briefly) → give the procedure to avoid it.
- No hazard section ends without a concrete procedure.
- Cover the full range: electrical, chemical, mechanical, thermal.

**Tools and Workspace** (`03-tools-and-workspace.md`)
- Tiered from bare minimum to well-equipped. Show three tiers: no-tool, basic (multimeter + screwdrivers), equipped (soldering station, desoldering pump, hot air).
- Name specific cheap options where useful ("a TS80P or similar" not just "a soldering iron").
- Workspace habits: lighting, ESD, organisation, ventilation for solder fumes.

**Core Techniques** (`04-core-techniques.md`)
- Practical procedures. Numbered steps for anything sequential.
- Tiered again: what each technique looks like at each tool level.
- Inspection and triage: how to read a board at a glance, what to target, what to skip.

## Step 3 — Write each section

Produce content for all sections in the stub, in order. The number of sections varies by page (5–7). Do not add sections or remove any. Preserve heading text exactly.

---

### General guidance for all foundations sections

**Opening**: Each section opens with one to two sentences that state plainly what the section is about and why it matters. No throat-clearing. No "In this section we will..."

**Procedures**: Any technique or safety process with more than two steps gets a numbered list. Single-step actions stay in prose. Always specify what tool, what setting, what to watch for.

**Tiered techniques** (for tools and technique pages): Use a consistent pattern — start with no-tool or minimal approach, then add tool tiers. You can use bold lead-ins ("**With a soldering iron only:**") or sub-headings for each tier.

**Safety sections**: Structure is always: name the hazard, explain what makes it dangerous (one or two sentences of mechanism), then the procedure. Never name a hazard and leave the reader without a response.

**Examples**: Use real, specific examples — a 400 µF cap at 450 V, a CRT anode, a lithium pack at 3.7 V — not abstract references. The reader is at a bench with real parts.

**Length per section**: Three to six short paragraphs or an equivalent amount of bulleted/numbered content. Do not pad. Do not repeat content from another section.

---

## Step 4 — Voice and style rules

Apply these throughout:

- **Second person, active voice.** "Discharge the cap before touching it" not "The cap should be discharged."
- **No exclamation marks.** Urgency comes from specificity, not punctuation.
- **No moralising.** Do not add environmental or ethical commentary. The reader is here to learn technique.
- **No gatekeeping.** Never suggest more experience is needed before the reader can proceed. Pair every warning with a procedure.
- **Short paragraphs.** Three to five sentences maximum. One idea per paragraph.
- **Specs as ranges.** "Electrolytic caps in switching supplies often hold 200–400 V" not "a high voltage."
- **Plain language.** No academic register, no marketing language. Workshop-y and honest.
- **Pair every hazard with a procedure.** This is the most important rule for the safety page. Do not end a hazard description without telling the reader what to do.

## Step 5 — AI writing antipatterns to avoid

These are the patterns Wikipedia's editors use to identify AI-generated text. Every one of them will make the output feel synthetic. Avoid them without exception.

**Banned vocabulary** — do not use these words; replace with plain, specific alternatives:
> delve, crucial, tapestry, landscape, pivotal, underscore, testament, intricate, meticulous, foster, navigate, realm, vibrant, noteworthy, bolstered, garner, enduring, interplay, additionally (as a sentence opener), comprehensive, robust, leverage, seamlessly, empower, transformative

**Banned phrases:**
- "it is worth noting that" → just say the thing
- "in conclusion" / "in summary" / "to summarise" → don't summarise; end when the content ends
- "plays a vital role" / "is critically important" → say what role or consequence, specifically
- "stands as a testament to" → say what it actually demonstrates
- "with that in mind" / "that being said" → transition directly
- Trailing participle clauses: "...emphasising the importance of safety", "...highlighting the need for care" → cut them
- "not only X but also Y" → restructure

**Banned structural patterns:**
- Every bullet point with a bolded lead-in phrase. Reserve bold for genuine key terms.
- Every paragraph the same length, every sentence the same structure. Vary rhythm deliberately.
- Em dashes where a comma, colon, or parenthesis would serve correctly.
- Summary paragraph at the end restating the section. End on content.
- Rule-of-three negative parallelisms: "No experience. No expensive tools. Just patience." → AI tic; avoid.
- Opening a section with a sentence that restates the heading: "Tools and workspace are important because..." → cut it and start with the first real point.

**Banned tone patterns:**
- Safety theatre: dramatic, abstract warnings without specific procedures. "Electricity is extremely dangerous." → name the hazard and what to do.
- Moralising about salvage or sustainability. The reader did not ask for it.
- Vague encouragement: "With a bit of practice, anyone can learn this skill." → either give a procedure or don't comment.
- Hedging preambles: "It is important to remember..." / "Always keep in mind..." → state the rule and move on.
- Treating the reader as fragile. Assume they are capable and resourceful.

## Step 6 — Write the file

Produce the complete markdown file: frontmatter unchanged, then all sections with full content. Write it back to the same path that was passed as the argument.

Do not add any new headings, sections, or frontmatter fields. Do not remove any existing headings or theory links.

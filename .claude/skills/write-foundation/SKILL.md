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

**Banned register** — do not use clinical or medical language for physical hazards; use plain workshop language:
- "open skin" / "lacerate" → "cut you" or "cut your hand"
- Use the words a person at a bench would say, not the words a safety manual would use.

**Banned adverb constructions** — do not use adverbs to describe hazards or techniques in ways no person would say:
- "dangerously high voltage" → "300 V" (name the voltage)
- "safely discharged" → say the procedure that makes it safe
- "reliably works" / "consistently effective" → say what works and why
- "particularly important" → if it's important, say what happens if you skip it

The tell: if the adverb is doing the work of specificity, replace it with actual detail. If it's just intensifying vaguely, cut it.

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
- Em dashes anywhere in prose. Use a comma, colon, or parenthesis instead. No exceptions.
- Semicolons in prose sentences. Split the sentence or use a comma. In table cells, semicolons are fine as spec-list separators.
- Summary paragraph at the end restating the section. End on content.
- Rule-of-three negative parallelisms: "No experience. No expensive tools. Just patience." → AI tic; avoid.
- Short imperative fragments used as emphasis beats after a longer sentence: "Start there.", "Remember that.", "Keep this in mind." — fold the instruction into the sentence it belongs to.
- Compressed spec-sheet constructions that strip the verb: "A multimeter is 10 MΩ input impedance" → "Most multimeters have 10 MΩ input impedance". Keep the relationship between noun and attribute explicit.
- Burying prerequisites after the instruction that depends on them. State what the reader needs to do or remove first, then give the main instruction.
- Listing one method when two legitimate options exist. If the reader can do something the quick way or the thorough way, name both.
- Opening a section with a sentence that restates the heading: "Tools and workspace are important because..." → cut it and start with the first real point.

**Banned tone patterns:**
- Safety theatre: dramatic, abstract warnings without specific procedures. "Electricity is extremely dangerous." → name the hazard and what to do.
- Moralising about salvage or sustainability. The reader did not ask for it.
- Vague encouragement: "With a bit of practice, anyone can learn this skill." → either give a procedure or don't comment.
- Hedging preambles: "It is important to remember..." / "Always keep in mind..." → state the rule and move on.
- Treating the reader as fragile. Assume they are capable and resourceful.

## Step 6 — Rhythm and structure

These rules address the deeper structural patterns that make AI writing feel robotic even after vocabulary and phrase problems are fixed.

**Sentence length must vary deliberately.** Mix short sentences (5–10 words) with longer ones. A very short sentence landing after a complex procedural clause creates emphasis and rest. Three sentences of similar length in a row is a tell — break it. Single-sentence paragraphs are fine when the sentence carries weight.

**Sections do not need equal depth.** A safety section covering a common hazard may need four paragraphs. One covering a rarer hazard may need two sentences. Do not pad the short one or compress the long one to make the page feel balanced. Real reference material is uneven because the subject matter is uneven.

**Numbered procedures do not need uniform step counts.** If one technique has three steps and another has seven, write them that way. A filler step added to reach a round number is always visible.

**Use contractions.** "You'll", "don't", "it's", "you're". Their consistent absence in technical prose is a recognisable tell. Workshop writing uses contractions.

**Include at least one detail that only comes from experience.** The specific thing a beginner always gets wrong with this technique. The reason a seemingly obvious shortcut fails. The exception to the rule that a reader will eventually hit. A detail that requires having actually done the work to know. These cannot be generated from surface-level knowledge.

**Name the legitimate shortcut — and the legitimate long way round.** AI prescribes one correct procedure. Real workshop writing acknowledges that readers have different goals: the shortcut is valid when it is, and the harder path is valid when a reader wants to learn or practise. Name both where they apply rather than implying one right way to do something.

**The author has a view.** When one approach is clearly safer or more practical, say which and why — don't present all options as equal. When a technique genuinely requires a specific tool and there is no workaround, say so plainly rather than softening it.

**Vary how sections open.** Not every section should begin with a topic sentence that restates the heading. Some sections can open mid-thought, with context, with a direct instruction, or with the exception before the rule.

## Step 7 — Write the file

Produce the complete markdown file: frontmatter unchanged, then all sections with full content. Write it back to the same path that was passed as the argument.

Do not add any new headings, sections, or frontmatter fields. Do not remove any existing headings or theory links.

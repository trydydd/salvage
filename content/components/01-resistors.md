---
title: "Resistors"
section: components
---

Resistors are the most common part on any donor board, and pulling them costs almost nothing. Most come off cleanly, read reliably, and go straight into general stock. The challenge isn't finding them; it's telling the ordinary ones from the shunts and fusibles, and knowing when a part that looks fine has drifted enough to matter.

## Identify the part

Through-hole resistors come in two forms you'll see constantly. The first is axial carbon film: a small cylinder, 4–9mm long depending on wattage, with colored stripes and a lead coming from each end. The second is metal film, which looks nearly identical but often has a blue or green body and five color bands instead of four. Size is the quickest wattage indicator: a 1/4W part is around 6mm long; 1/2W stretches to 9mm; a 1W or 2W part is noticeably chunkier, often cream or tan.

Color bands give you the value. Four-band parts use three digit bands plus a tolerance band at one end; five-band parts use four digit bands plus tolerance. Read from the end where the bands cluster closest together. The tolerance band is usually gold (5%) or silver (10%) and sits at the far end of the cluster. Black, brown, red, orange, yellow, green, blue, violet, grey, white map to 0–9; any mnemonic that gets you there works.

SMD resistors print the code on the flat top face. Three-digit codes: 104 means 10 followed by four zeros, so 100kΩ. 472 means 4.7kΩ. Four-digit codes work the same way with one more digit before the multiplier. EIA-96 codes show up on 1% 0402 and 0603 parts: two digits plus a letter (01C = 100Ω, 68A = 487Ω). These need a reference table; don't try to decode them from memory.

Two things that look like resistors but aren't: current-sense shunts sit in series with a load, usually near the power transistors, and measure in the 0.005–0.5Ω range. Fusible resistors look like ordinary carbon film but are designed to open cleanly when overloaded; they show up near AC input stages in older Japanese consumer gear. Both are worth pulling if you label them correctly.

## Measure and confirm

**Setting the range**

Set your meter to the resistance range that fits the expected value: 200Ω range for a 100Ω part, 20kΩ or 200kΩ for a 10kΩ part. Before measuring low-value parts, short the probes and note the lead resistance, then subtract it from your reading. A meter with 0.3Ω of lead resistance will make a 0.5Ω shunt look like 0.8Ω.

**In-circuit readings**

Parallel paths through the board pull your reading down. A 10kΩ resistor sitting in parallel with a 1kΩ pull-down will read around 909Ω, not 10k. If your reading is lower than the markings suggest, desolder one leg and measure again before calling the part bad.

**Out-of-circuit confirmation**

A good resistor reads within its tolerance window. A 10kΩ gold-band (5%) part should read 9.5–10.5kΩ. If it reads outside that, it has drifted and you should measure its actual value and write it on the storage bag rather than trusting the color bands in a future build.

An OL (infinite) reading in resistance mode means the part is open. Zero means a short, which is rare in film resistors but does happen in wirewound and cement types after overload.

## Failure modes

**Open circuit**

The most common failure. An overloaded resistor burns through and goes infinite resistance. The body is often cracked, blackened, or the leads have pulled partially loose. In high-current areas you'll see a burn mark on the PCB under the part. There's no recovering an open resistor; it's scrap.

**Resistance drift**

Carbon film resistors, particularly older or heat-stressed ones, can shift 10–30% without visible damage. This is the failure mode you can't see on the bench without measuring. Any resistor pulled from the hot zone around a failed component should be measured before going into stock, regardless of how it looks. Anything beyond twice its marked tolerance window shouldn't be used where the value matters.

**Fusible open**

If you pull a fusible resistor and it reads open, that's expected. The part opened to protect something downstream. The body often looks clean or just slightly discolored at one end. A fused-open part isn't safe to reuse in its original role because the protection it was sized for no longer exists.

**Contamination short**

Salvaged boards from flooded or corroded devices sometimes have conductive deposits bridging the resistor body or the traces alongside it. If you see green or white residue near a resistor and the reading is low, clean the board area with isopropyl alcohol and re-test before deciding whether the resistor itself is bad.

## Reuse notes

Standard carbon film and metal film resistors are safe to pull for general-purpose stock. The values you'll encounter most often are the E12 and E24 series: 1kΩ, 2.2kΩ, 4.7kΩ, 10kΩ, 47kΩ, 100kΩ, and 1MΩ are everywhere. Pull anything with readable markings.

Metal film (blue or green body, five bands) is worth prioritizing from audio boards and instrumentation gear. They run 1% or better tolerance and lower noise than carbon film, and they're genuinely useful in later audio or signal work.

Store resistors by value in compartments or labeled bags. For general stock, the marked value is enough. For anything you measured and found drifted, write the measured value on the bag and mark it "check before use." Keep fusible resistors in a separate bag labeled "fusible" because they're still useful in the right position but can't be substituted for ordinary film resistors.

Don't bother with resistors pulled from directly around a failed or exploded component, parts with charred or illegible markings, or wirewound cement resistors you can't identify. A new resistor costs less than a minute of debugging a value you're not confident in.

## Theory links

For resistance measurement technique and why parallel paths confuse in-circuit readings, see [DC measurements](/open-circuits/DC/DC_5.html). For a simple test circuit that lets you verify a resistor's value by measuring voltage drop rather than resistance directly, see [bench experiments](/open-circuits/Exper/EXP_1.html).

---
title: "Inductors and Transformers"
section: components
---

Coils and transformers span a wide range of sizes and purposes in salvage, from a tiny 1µH shielded SMD inductor in a phone charger to the heavy steel-laminated transformer in a bench power supply. Sorting them by type before testing saves a lot of confusion.

## Identify what kind of coil it is

Fixed inductors come in several forms. Through-hole axial inductors look like large resistors: a cylindrical body with leads from each end, sometimes with color bands, sometimes with a printed value. Radial inductors stand upright off the board on two leads from the same face. Toroidal inductors are the donut-shaped parts wound with wire on a ferrite or powdered-iron ring: you'll find them in power supplies and audio crossovers. SMD inductors are shielded rectangular blocks in sizes from about 4mm square (2020 footprint) down to 2mm (1210 footprint), and they often carry a code on the top face.

Common-mode chokes look like transformers: two windings on a shared ferrite core, usually an E-core or toroid with a flat plastic housing. They appear near AC inputs, USB connectors, and Ethernet ports to suppress conducted interference. Ferrite beads are the SMD parts that look like 0402 or 0805 resistors but read very low DC resistance (under 0.5Ω) and are rated by impedance at 100MHz rather than inductance. Both are worth pulling if you can identify them.

Flyback transformers are the large plastic-bobbin assemblies in offline switching supplies: the kind with multiple pins on the base and a visible ferrite E-core inside the plastic shroud. They're wound for specific voltage ratios in a specific topology; reusing one outside its original circuit is almost never practical, and the circuit that drove it usually touched mains voltage. Pull them for core material if you wind your own coils, otherwise leave them.

Mains transformers are heavy, unmistakable, and have laminated steel cores with copper or aluminum windings. They're labeled by VA rating and secondary voltages, sometimes by primary voltage if the manufacturer was thorough. An old 12V-0-12V 3A toroidal from a Hi-Fi amp is genuinely useful. An oddly-tapped 35VA transformer from a proprietary power supply rarely is.

## Continuity and winding checks

**DC resistance of each winding**

Desolder or disconnect the transformer before testing. Set your meter to the 200Ω range. Touch the probes to the two leads of each winding in turn. A healthy winding reads a low but non-zero resistance. Mains transformer primaries typically read 15–100Ω depending on VA rating and primary voltage. Secondaries read lower: a 12V secondary on a 50VA transformer might read 0.5–3Ω. Buck inductor windings typically read 0.01–0.5Ω. A winding that reads OL (infinite) is open and the part isn't usable for its original purpose.

**Continuity between windings**

After checking each winding separately, probe between windings. You should read OL between the primary and any secondary, and between any two secondaries that don't share a common tap. A reading anywhere between windings that should be isolated means the insulation has broken down. That transformer is not safe to use near mains voltage, and shouldn't be used at all unless you can test it properly for isolation voltage.

**Core isolation**

Touch one probe to any winding lead and the other probe to the transformer core (the steel laminations or the ferrite, somewhere you can get a clean contact). A healthy transformer reads OL here. A reading between any winding and the core means there's a fault to ground, which makes the transformer unsafe for any mains application and questionable for low-voltage use as well.

**Ferrite bead check**

In resistance mode on the 200Ω range, a ferrite bead reads almost nothing: 0.1–0.5Ω is typical. If it reads OL, it's open (uncommon but happens after physical damage). If you're not sure whether a surface-mount part is a ferrite bead or a resistor, the low DC resistance and the impedance-based part number (like BLM18AG601SN1) are the tells.

## Isolation matters

Coils and transformers pulled from mains equipment deserve a different level of attention than low-voltage parts. The wire insulation inside a flyback transformer has been subject to the full voltage stress of the circuit it came from, which can exceed 400V on the primary side of a mains-rectified supply. Even a transformer that passes a DC continuity check may have degraded insulation that would fail under AC stress or over time.

For audio transformers and low-voltage inductors from 5V or 12V circuits, the isolation question is simpler: check that no winding reads to core or to any other winding, and you're done. For anything pulled from the primary side of a mains supply, or from any circuit where you can't confirm the maximum voltage the winding saw, treat isolation as unknown until you can test it with a megohmmeter or simply avoid using the part in any mains-adjacent role.

## Reuse notes

Standard through-hole inductors with readable values are worth pulling, especially if the value is printed (R47 = 0.47µH, 100 = 10µH, 101 = 100µH). Write the value and any part number on the storage bag. For SMD shielded inductors, pull the 10µH–470µH range as these cover most switching converter applications; anything smaller than 1µH in a 0805 footprint isn't worth the effort unless you're doing RF work.

Toroidal inductors from audio equipment are worth keeping if the winding looks intact (no cracked enamel wire, no burnt smell). Measure the DC resistance and write it on the bag. For power work you'll also want to know the inductance, and that requires an LC meter or a dedicated inductance function on a component tester; a plain multimeter can't measure inductance.

Mains transformers with clear voltage labels and a known VA rating are genuinely useful. A 12-0-12V 1A or 2A toroidal is the center of many bench supply builds, and pulling one from a scrapped piece of audio gear saves real money. The weight is roughly proportional to the power rating: a 50VA toroidal weighs around 700g. If the weight is unexpectedly low for a claimed VA rating, measure the primary resistance and compare against what you'd expect for that winding.

Don't bother with flyback transformers from switching supplies unless you're harvesting the ferrite core for winding experiments. Don't reuse any transformer where you found continuity between windings or between any winding and core. Don't reuse inductors with charred wire, melted insulation, or broken leads.

## Theory links

For basic winding checks and how to use a meter to confirm continuity through each winding, see [DC measurements](/open-circuits/DC/DC_5.html). For simple low-voltage coil tests that show inductive behavior without mains involvement, see [bench experiments](/open-circuits/Exper/EXPER_1.html).

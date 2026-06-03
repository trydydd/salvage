---
title: "Inductors and Transformers"
section: components
hazard: 4
hazard_summary: "Mains transformers carry lethal voltage on the primary; CRT flyback transformers generate 15–30 kV and retain charge for days after power-off; interrupting current through a large inductor causes voltage spikes that can destroy components or cause injury."
author: Claude
review: Needs Human Review
---

Coils and transformers span a wide range of sizes and purposes in salvage, from a tiny 1µH shielded SMD inductor in a phone charger to the heavy steel-laminated transformer in a bench power supply. Sorting them by type before testing saves a lot of confusion.

## Identify what kind of coil it is

Fixed inductors come in several forms. Through-hole axial inductors look like large resistors: a cylindrical body with leads from each end, sometimes with color bands, sometimes with a printed value. Radial inductors stand upright off the board on two leads from the same face. Toroidal inductors are the donut-shaped parts wound with wire on a ferrite or powdered-iron ring, and you'll find them in power supplies and audio crossovers. SMD power inductors are shielded square blocks: the common 4040 footprint (4mm × 4mm, roughly 4–5mm tall) carries 1µH–100µH at several amps, while smaller 2016 and 2520 metric footprints appear in phone chargers and laptop boards. They usually carry a value code on the top face.

Axial inductors look identical to resistors on a quick glance, and this trips people up. The color-band system uses the same digit-color mapping as resistors but the result is in microhenries. A printed numeric code also follows the same two-digit-plus-multiplier convention used on capacitors: `100` means 10 × 10⁰ = 10µH, and `101` means 10 × 10¹ = 100µH. An `R` in a code marks the decimal point: `R47` = 0.47µH, `4R7` = 4.7µH. If you pull an axial part that looks like a resistor, put it on the 200Ω range before assuming it's passive: an inductor reads near zero, a resistor reads its rated value.

Common-mode chokes look like transformers: two windings on a shared ferrite core, usually a toroid or flat E-core inside a rectangular plastic housing. They appear near AC inputs, USB connectors, and Ethernet ports to suppress conducted interference. The ones mounted directly on the AC input line (alongside X and Y capacitors on the filter board) have been at mains potential and should be handled with the same caution as any other mains-connected component. Ferrite beads are the SMD parts that look like 0402 or 0805 resistors but read very low DC resistance (0.02–0.3Ω is typical) and are rated by impedance at 100MHz rather than inductance. Both are worth pulling if you can identify them.

Two categories of flyback transformer appear in salvage and they are not the same thing. The first is the offline switching supply flyback: a plastic-bobbin assembly with multiple pins on the base and a visible ferrite E-core inside the plastic shroud, found in any mains-connected switching supply. The circuit around it has touched rectified mains voltage (300–400V DC), so the transformer and all nearby components should be treated as potentially charged until you've discharged the main filter capacitors. The second is the CRT flyback transformer, pulled from older televisions and monitors. These generate 15–30 kV on the high-voltage secondary and the associated high-voltage capacitor (built into the flyback assembly or sitting on the board) retains a lethal charge for days or weeks after power-off, even with the main filter caps fully discharged. CRT flybacks are not salvageable for any practical purpose. Leave them in the carcass and discharge the CRT anode lead before handling anything nearby.

Mains transformers are heavy, unmistakable, and have laminated steel cores with copper or aluminum windings. They're labeled by VA rating and secondary voltages, sometimes by primary voltage if the manufacturer was thorough. An old 12V-0-12V 3A toroidal from a Hi-Fi amp is genuinely useful. An oddly-tapped 35VA transformer from a proprietary power supply rarely is.

## Inductive kickback

Before you desolder, clip, or switch any inductor or transformer winding that's carrying current, understand what happens when you interrupt that current. An inductor resists changes in current. When you break the circuit suddenly, it will generate whatever voltage is needed to keep current flowing. For a small signal inductor this is a transient spike that kills the switching transistor. For a large inductor carrying several amps (a motor winding, a mains filter choke, a power supply output inductor under load), the spike can reach hundreds of volts and cause injury if you're bridging the circuit with your body.

The stored energy is E = ½LI², so doubling the current quadruples the energy. A 1mH inductor carrying 5A stores 12.5mJ. Releasing that in microseconds produces a voltage spike proportional to L × (di/dt). Always discharge or de-energize a circuit before desoldering inductors. If you're probing a live circuit, use a differential probe with appropriate voltage rating, not bare meter leads.

## Continuity and winding checks

**DC resistance of each winding**

Disconnect the transformer fully from the circuit before testing (remove it from the board or at minimum disconnect all leads). Set your meter to the 200Ω range. Touch the probes to the two leads of each winding in turn. A healthy winding reads a low but non-zero resistance. Mains transformer primaries typically read 20–150Ω depending on VA rating and primary voltage. A 240V primary on a 50VA transformer commonly reads 50–100Ω, while a 120V primary on the same VA rating reads roughly a quarter of that. Secondaries read lower: a 12V secondary on a 50VA transformer typically reads 0.5–2Ω. Buck converter output inductors typically read 0.01–0.15Ω. A winding that reads OL (overload/infinite) is open and the part isn't usable for its original purpose.

**Continuity between windings**

After checking each winding separately, probe between windings. You should read OL between the primary and any secondary, and between any two secondaries that don't share a common tap. A non-OL reading between windings that should be isolated means the insulation has broken down. That transformer is not safe to use near mains voltage, and shouldn't be used at all unless you can verify isolation voltage with a megohmmeter.

**Core isolation**

Touch one probe to any winding lead and the other probe to the transformer core (the steel laminations or the ferrite, somewhere you can get a clean contact). A healthy transformer reads OL here. A reading between any winding and the core means there's a fault to ground, which makes the transformer unsafe for any mains application.

**Ferrite bead check**

In resistance mode on the 200Ω range, a ferrite bead reads almost nothing: 0.02–0.3Ω is typical. If it reads OL, it's open (uncommon but happens after physical damage). If you're not sure whether a surface-mount part is a ferrite bead or a resistor, the very low DC resistance and the impedance-based part number (like BLM18AG601SN1) are the tells.

## Isolation matters

Coils and transformers pulled from mains equipment deserve a different level of attention than low-voltage parts. The wire insulation inside a flyback transformer has been subject to the full voltage stress of the circuit it came from, which can exceed 400V DC on the primary side of a mains-rectified supply. Even a transformer that passes a DC continuity check may have degraded insulation that would fail under AC stress or over time.

Before you handle any transformer from mains equipment, discharge the main filter capacitors on the primary side. Set your meter to DC volts and verify the big electrolytic caps read under 10V before you touch anything. A transformer that was in service might have been energized right up until the device was discarded.

For audio transformers and low-voltage inductors from 5V or 12V circuits, the isolation question is simpler: check that no winding reads to core or to any other winding, and you're done. For anything pulled from the primary side of a mains supply, or from any circuit where you can't confirm the maximum voltage the winding saw, treat isolation as unknown until you can test it with a megohmmeter or simply avoid using the part in any mains-adjacent role.

## Failure modes

**Open winding** is the most common failure. The DCR test catches it immediately: a winding that should read a few ohms reads OL instead. Most often caused by a mechanical break at a lead attachment point or by thermal damage that melted the enamel and then the wire. An open primary means the transformer does nothing. An open secondary means that output is dead.

**Shorted turns** are harder to detect with a basic meter and more dangerous to miss. A few turns of the winding are shorted together, reducing effective inductance and causing heating. The DCR often reads slightly lower than expected, but not dramatically so. The real tell is abnormal heat during operation: a transformer running warm with a light load, or an inductor that's noticeably hot to the touch after a few minutes at rated current. If you see discoloration of the wire or the potting around the winding, assume shorted turns.

**Insulation breakdown** between primary and secondary shows up as a non-OL reading on your continuity test between windings. In a mains transformer this means live voltage can reach the secondary and any circuit connected to it. Discard the transformer.

**Core-to-winding fault** reads as a non-OL between any lead and the core. In a steel-laminated transformer this is usually caused by mechanical damage or a chafed lead that's worn through to the laminations. The transformer becomes a shock hazard in any mains application.

**Core saturation damage** usually presents as a partially cracked or chipped ferrite core. If you shake a ferrite-core inductor or transformer and hear a rattle, the core is broken. Cracked ferrite changes the inductance value unpredictably. A broken core in a power inductor will cause the circuit to behave erratically under load even if the DC resistance tests fine.

**Delaminated SMD inductors** show up as a part that tests fine cold but drifts or goes open when it reaches operating temperature. If a board fault disappears on the bench but returns in use, suspect the inductors as well as the capacitors.

## Reuse notes

Standard through-hole inductors with readable values are worth pulling, especially if the value is printed (R47 = 0.47µH, 100 = 10µH, 101 = 100µH). Write the value and any part number on the storage bag. For SMD shielded power inductors, pull the 10µH–470µH range in 4040 or larger footprints, as these cover most switching converter applications. Sub-1µH SMD parts aren't worth the effort unless you're doing RF work.

Toroidal inductors from audio equipment are worth keeping if the winding looks intact (no cracked enamel wire, no burnt smell). Measure the DC resistance and write it on the bag. For power work you'll also want to know the inductance, and that requires an LC meter or a dedicated inductance function on a component tester. A plain multimeter can't measure inductance.

Mains transformers with clear voltage labels and a known VA rating are genuinely useful. A 12-0-12V 1A or 2A toroidal is the center of many bench supply builds, and pulling one from a scrapped piece of audio gear saves real money. The weight is roughly proportional to the power rating: a 50VA toroidal typically weighs 300–750g. If the weight is unexpectedly low for the claimed VA rating, measure the primary resistance. An underweight transformer for its claimed rating sometimes turns out to be mislabeled or rewound.

Flyback transformers from offline switching supplies have no practical reuse outside harvesting the ferrite core for winding experiments. CRT flybacks have no practical reuse at all, so set them aside. Any transformer where you found continuity between windings or between a winding and the core goes in the bin, not the parts drawer. Same for inductors with charred wire, melted insulation, or broken leads.

## Theory links

For basic winding checks and how to use a meter to confirm continuity through each winding, see [DC measurements](/open-circuits/DC/DC_5.html). For simple low-voltage coil tests that show inductive behavior without mains involvement, see [bench experiments](/open-circuits/Exper/EXP_4.html).

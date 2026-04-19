---
title: "MOSFETs"
section: components
---

Power MOSFETs show up in every switching supply, motor driver, and battery management board you'll disassemble. They're worth pulling when you can read the part number, and even when you can't, the body diode test will tell you channel type and orientation before you put the part in a bag.

## Identify channel and role

The most common salvage package is TO-220: a rectangular plastic body with a metal tab at the top and three leads in a row at the bottom. The tab is almost always the drain terminal, and in power circuits the tab is usually bolted to a heatsink or chassis. To desolder a TO-220 properly, remove the mounting screw before you heat the pins; trying to pull the part while the tab is still fastened will lift the pads.

D-PAK (also called TO-252) is the SMD equivalent: a flat rectangular body with a large exposed pad on the bottom that's soldered to the board for heat dissipation, plus three leads on one side. You'll find D-PAK MOSFETs in laptop chargers, phone chargers, and anything that needed to manage power in a compact space. SO-8 packages carry dual MOSFETs on a single eight-pin chip; these appear in motor H-bridges and battery protection boards.

The part number tells you the channel type, though the conventions aren't universal. IRF-prefix parts are almost always N-channel unless the number contains a "9" or ends in "P" (IRF9540 is P-channel, IRF540 is N-channel). FQP30N06L breaks down as N-channel (the N), 30A, 60V. IRFP9240 is P-channel (the 9 position). If the marking is worn, the body diode test below will tell you which channel you have.

Small-signal MOSFETs in TO-92 or SOT-23 packages (2N7000, BSS138, AO3400) look identical to BJT transistors in the same packages. Don't assume a three-lead TO-92 is a BJT just because that's what you expected to find on that board. The diode mode test will clarify quickly: a MOSFET reads OL gate-to-source and gate-to-drain in both directions, where a BJT reads junction voltages through the base.

## Body diode test

Desolder the MOSFET before testing. In-circuit measurements on power MOSFETs are unreliable because the drain is often connected to supply or ground through other components that will affect the reading.

**Finding the body diode**

Set your meter to diode mode. On an N-channel MOSFET, the body diode runs from source to drain with the anode at the source. To find it: probe each combination of the three pins until one pair reads a forward voltage of 0.45–0.65V with the red probe on one pin and the black probe on the other. That forward-biased reading is the body diode. The pin with the red probe is the source; the pin with the black probe is the drain. The remaining pin is the gate.

Swap the probes on the same two pins and check that the meter reads OL. If you get a voltage reading in both directions on any pair of pins, the MOSFET is shorted between those terminals.

**P-channel body diode**

The P-channel body diode runs in the opposite direction: anode at drain, cathode at source. The same test works, but the forward voltage reads with the black probe on source and the red probe on drain.

**Gate check**

Once you've identified the gate pin, touch one probe to the gate and the other to either of the remaining pins. In diode mode, the gate should read OL in both directions. Any numeric reading at the gate means the gate oxide is damaged. A gate-to-source or gate-to-drain short is caused by electrostatic discharge and the part isn't safe to use.

## Gate behavior

The gate is separated from the channel by a thin layer of silicon oxide, which means no DC current flows into or out of it during normal operation. This also means the gate holds whatever charge lands on it, including from your fingers or a charged probe tip. Before testing or handling a MOSFET you've just desoldered, touch the source and drain leads together briefly to discharge the gate through the body diode path.

To do a basic switching test at the bench, connect a resistor (470Ω to 1kΩ) in series with the drain to a supply (3–5V is enough for many logic-level MOSFETs). Connect source to ground. With the gate floating or shorted to source, the MOSFET should be off and no current flows through the resistor. Apply 5–10V gate-to-source: the MOSFET turns on and you can measure voltage across the resistor with the meter. This confirms the gate oxide is intact and the device switches.

Logic-level MOSFETs (often identified by "L" or "LT" in the part number, or a note in the datasheet) turn on fully with 3.3–5V gate-source voltage. Standard power MOSFETs may need 8–12V at the gate to reach full enhancement. Testing at 5V gate voltage will turn them on partially but not fully; the channel resistance will be higher than rated and the device will run warm under load.

## Common damage patterns

**Shorted drain-source**

The most common failure in power MOSFETs. Overvoltage on the drain (from an inductive kick, a mains transient, or a motor back-EMF spike) punches through the gate oxide or the drain-source channel and leaves it conducting in both directions. In diode mode, you'll read a low voltage (often 0.05–0.2V, lower than a normal body diode) in both drain-source directions. The tab is often discolored or the package cracked. Don't reuse it.

**Gate oxide damage from ESD**

The gate oxide is thin enough that a few hundred volts of static discharge will punch through it. The failure shows as a low resistance or dead short gate-to-source or gate-to-drain in diode mode. ESD-damaged MOSFETs sometimes fail partially: the gate still reads as high-impedance, but the threshold voltage has shifted and the device behaves unpredictably under load. Discard any part with a damaged gate.

**Thermal cracking**

Power MOSFETs mounted to heatsinks with too little thermal compound, or run repeatedly at high current, can develop hairline cracks in the plastic body near the tab. The cracks are often visible under good light. A cracked package can still pass all bench tests but will fail early in a high-temperature application. If you see cracking, don't trust the part for power work.

**Package lifted from board**

TO-220 MOSFETs bolted to chassis sometimes get the tab ripped off the body if the board was dropped or the screw was overtorqued. The leads may look fine. Test the tab-to-drain connection in resistance mode: a good part reads zero between tab and drain pin; an open reading means the internal bond is broken and the part is scrap.

## Reuse notes

N-channel TO-220 MOSFETs are the most useful things to pull from switching supplies and motor boards. IRF3205 (55V, 110A), IRF540 (100V, 28A), and STP75NF75 (75V, 75A) are all worth having in stock if you can confirm the part number. Even an unknown N-channel TO-220 with a body diode that tests healthy is useful for low-voltage switching experiments, provided you derate it: treat the current rating as 60% of whatever the package suggests, and stay well below the drain voltage rating.

For P-channel parts, the stock value is lower because N-channel is usually preferred in low-side switching, but IRF9540 (100V, 19A) and similar parts appear often enough that they're worth pulling when labeled.

D-PAK and SO-8 parts are worth pulling only if you're specifically doing SMD work. The time cost of desoldering and the handling precautions for SO-8 packages make them not worth stockpiling unless you have a project in mind.

Store MOSFETs in antistatic bags or foam. A small piece of conductive foam with all three leads shorted into it protects the gate from static. Label the bag with the part number, channel type (N or P), and drain voltage rating. If the part number is gone, label it with the body diode direction and the estimated channel from the test, e.g. "N-channel, TO-220, unknown Vds."

Don't reuse any MOSFET that reads a gate-to-drain or gate-to-source short, any part with visible tab damage or package cracking, or any part pulled from directly beside a shorted or exploded component.

## Theory links

For field-effect device basics and how the gate controls the channel, see [Semiconductors](/open-circuits/Semi/SEMI_6.html). For controlled low-voltage bench checks that let you confirm switching without a full circuit, see [DC measurements](/open-circuits/DC/DC_5.html).

---
title: "ATX Power Supplies"
section: donor-guides
hazard: 3
hazard_summary: "Large input caps hold 300V+ for minutes after unplugging."
---

## What's Inside

An ATX supply packs a full switch-mode power conversion system into a steel box roughly 150 × 86 × 140 mm, depending on wattage class. Open the case (four Phillips screws on the rear panel) and you'll find one main PCB and a brushless fan mounted between the board and the top grille.

The primary side handles mains voltage: an input filter, a bridge rectifier, one or two large filter capacitors, and a pair of switching MOSFETs that drive the main ferrite transformer. Everything on this side operates at line voltage while running and holds charge after unplugging. The isolation boundary — a slot or gap routed into the PCB — marks where primary ends and secondary begins.

The secondary side is the low-voltage output stage: Schottky rectifier diodes on an aluminium heatsink, clusters of filter capacitors on each output rail (12 V, 5 V, 3.3 V, and −12 V), and a feedback circuit that keeps outputs regulated. Output wires leave via a harness with standard ATX connectors for motherboard, CPU, drives, and peripherals.

The fan, output harness, secondary caps, heatsinks, and power devices are all worth pulling. The primary input caps can be good, but they're also the part that injures people who work carelessly — save those for after you've confirmed the board fully discharged.

## Before You Open It

1. Unplug from mains. The 5 V standby rail is live whenever the PSU is connected, even with the unit switched off.
2. Wait at least 10 minutes. The large primary filter caps (200–400 V rated) can hold 300 V or more after mains disconnect; some designs discharge slowly.
3. Before touching the primary side, discharge the input caps deliberately. Probe across each cap's terminals with a multimeter set to DC voltage. If you read above 30 V, connect a 10 kΩ 1 W resistor across the terminals and wait for the reading to drop below 5 V.
4. Identify the isolation boundary on the PCB before picking up any tools. The slot or air gap running across the board separates mains potential from the output side. Stay on the secondary side of that line until the primary caps are confirmed discharged.

If you can't clearly identify the primary-side components or the isolation boundary, harvest only the fan and output harness — both come out without going near the primary side at all.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Case fan | Mounted at top or rear of case | 80 mm or 120 mm; 12 V brushless; 2- or 3-pin connector; spin with a finger to check the bearing | ★★★ |
| Output wire harness | Bundled cables from secondary PCB | 18–20 AWG; ATX 20/24-pin, 4/8-pin CPU, SATA, Molex peripheral plugs; many units use separable connectors at the PCB | ★★★ |
| Secondary filter electrolytics | Secondary PCB, output rail clusters | 680–2200 µF, 6.3–16 V; look for Japanese brands (Nichicon, Rubycon, Panasonic); reject any with bulging tops | ★★★ |
| Schottky rectifier diodes | Secondary heatsink | TO-220 or TO-3P package; 20–100 A, 30–100 V; often dual-package (one body, two diodes) | ★★☆ |
| Aluminium heatsinks | Primary and secondary power stages | L-bracket or plate; retain isolation hardware (mica or silicone pads, nylon screws) with the part | ★★☆ |
| Power MOSFETs | Primary heatsink, near transformer | TO-220; N-channel; 400–600 V, 10–20 A typical; markings like IRF840, K2843, or similar | ★★☆ |
| Primary input electrolytics | Primary PCB, near transformer | 200–400 V, 220–680 µF; reject any with yellowed sleeves, electrolyte crust, or domed tops | ★☆☆ |
| PWM controller IC | Primary PCB, small IC near optocoupler | Common types: TL494, SG3525, KA7500; check markings before desoldering | ★☆☆ |

## How to Get Them Out

Without a soldering iron, the fan, output harness, and case hardware all come out cleanly. The fan is held by two to four screws through the case or a bracket; the connector unplugs from the PCB header. The output harness on many units plugs into the PCB with a separable connector block — lift the latch, pull the block, and the whole harness comes free. On units where harness wires are soldered directly to the board, cut at the PCB end and leave some lead length for later trimming.

With a soldering iron, secondary filter electrolytics are through-hole parts. Heat from the underside while gently rocking the cap; solder wick or a pump works well here. The rectifier diodes on the secondary heatsink are also through-hole — unbolt each from the heatsink first (usually two screws), then desolder. Keep the isolation pad with the diode to identify the package later.

With a desoldering station or hot air: primary MOSFETs are through-hole in most ATX supplies but mounted to a heatsink that limits access. Unbolt each MOSFET from the heatsink before desoldering — trying to pull a bolted device will strip the pads. The PWM controller IC, if SMD, lifts cleanly with hot air at 320–350 °C; hold the board steady with a clip or vise.

## Watch Out For

- The primary input caps hold 300 V or higher for several minutes after unplugging, and longer in larger units. Measure across both terminals with a meter before touching. If the reading is above 30 V, discharge through a 10 kΩ 1 W resistor until it drops below 5 V.
- The isolation boundary on the PCB is a hard line. If you can't see a clear routed slot or gap separating the two halves, treat the whole board as unsafe until you've measured zero volts on the primary caps.
- Sheet-metal edges on the case lid and fan bracket are sharp. Run a finger along cut edges before reaching in; a strip of electrical tape over burrs makes working inside much easier.
- Secondary filter caps with bulging or domed tops have failed. They may vent caustic electrolyte if punctured or heated. Discard rather than salvage.
- Most ATX supplies built before 2006 use leaded solder throughout. Wash hands after handling the PCB, and work with ventilation when desoldering.

## Theory Links

For measuring DC voltages on salvaged boards, see [DC measurements](/circuits/DC/DC_5.html).

For understanding the MOSFETs and rectifiers that dominate PSU salvage value, see [Semiconductors](/circuits/Semi/SEMI_6.html).

## Specific Teardowns

Specific make-and-model teardowns for ATX power supplies will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

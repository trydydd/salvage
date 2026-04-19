---
title: "ATX Power Supplies"
section: donor-guides
hazard: 3
hazard_summary: "Large input caps hold 300V+ for minutes after unplugging."
---

## What's Inside

Four Phillips screws on the rear panel, lid off, and you're looking at one main PCB running most of the case length with a brushless fan sitting above it against the top grille. Higher-wattage units (600 W and above) sometimes have a second daughterboard for extra output rectifiers. Same rules apply to both.

The board splits into two electrical territories. On the primary side: an EMI filter near the IEC socket, a bridge rectifier, one or two large electrolytic caps, and switching MOSFETs bolted to a finned heatsink that drives the main ferrite transformer. This side runs at mains voltage while the supply is on and holds charge after unplugging. A routed slot or air gap crossing the PCB marks where primary ends. Find it before you touch anything.

Past that boundary, the secondary side drops to safe voltages. Schottky rectifier diodes on a second heatsink, banks of filter caps on the 12 V, 5 V, 3.3 V, and -12 V rails, and a PWM feedback loop that keeps everything regulated. Output wiring exits as a bundled harness, or through a socket panel on the back face on modular units.

The fan, harness, and secondary caps alone justify pulling most ATX units. The rest is a bonus.

## Before You Open It

1. Unplug from mains. The 5 V standby rail is live whenever the supply is connected, regardless of the power switch.
2. Wait at least 10 minutes. Primary filter caps are rated 200–400 V and some designs hold charge for longer than you'd expect, especially in supplies that were running hard.
3. Measure across the primary cap terminals with a multimeter on DC voltage before reaching in. Anything above 30 V means wait longer.
4. If you're above 30 V after 15 minutes, clip a 10 kΩ 1 W resistor across the cap terminals and recheck every couple of minutes until you're below 5 V.
5. Locate the isolation boundary before picking up any tools. If you can't find it clearly, work only on the fan and harness. Both come out without going near the primary side.

The discharge step feels slow. It isn't skippable.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Case fan | Above main PCB, against top grille | 80 mm or 120 mm; 12 V brushless; 2- or 3-pin connector; spin the blade to check the bearing | ★★★ |
| Output wire harness | Bundled from secondary PCB; rear socket panel on modular units | 18–20 AWG; 20/24-pin ATX, 4/8-pin CPU, SATA, Molex; often separable at the PCB without desoldering | ★★★ |
| Secondary filter electrolytics | Secondary PCB, clustered near output rails | 680–2200 µF, 6.3–16 V; Japanese brands (Nichicon, Rubycon, Panasonic) are worth the effort. Samxon and Ltec aren't | ★★★ |
| Schottky rectifier diodes | Secondary heatsink | TO-220 or TO-3P; 20–100 A, 30–100 V; often dual-package (one body, two diodes) | ★★☆ |
| Aluminium heatsinks | Primary and secondary power stages | L-bracket or flat plate; keep the isolation hardware (mica pads, nylon shoulder screws) together with it | ★★☆ |
| Power MOSFETs | Primary heatsink, near transformer | TO-220; N-channel; 400–600 V, 10–20 A typical; IRF840, K2843, and similar are common | ★★☆ |
| Primary input electrolytics | Primary PCB, flanking the transformer | 200–400 V, 220–680 µF; only worth pulling from known-good brands with no visible aging | ★☆☆ |
| PWM controller IC | Primary PCB, small DIP or SMD near the optocoupler | TL494, SG3525, KA7500 are the types worth recognising; anything else, check the markings before committing to desoldering | ★☆☆ |

## How to Get Them Out

Start by removing everything you can without a soldering iron.

The fan will generally have screws accessible from outside the case and a connector that needs to be unplugged from the PCB. Some fan connectors, particularly on Seasonic and FSP builds, have a locking tab you need to press before pulling. Using brute force will damage the housing. If you only want the wires, that's fine. Cut them at the connector and move on. On modular PSUs the wiring can simply be unplugged. On non-modular units the wires are soldered to the board. Cut them unless you want the desoldering practice. The heatsinks unbolt from the PCB with two or three screws. When you do this, keep the shoulder screws, nylon spacers, and isolation pads in a bag. They're harder to source than the components they came off.

The secondary filter caps and rectifier diodes are both through-hole. For the caps, heat from the underside and rock the lead while wicking or pumping. For the rectifier diodes, remove the mounting screw from the heatsink before picking up the iron. Trying to desolder a bolted part torques the pads off. Once free, heat and wiggle or use a pump. The isolation pad usually sticks to the heatsink when you unbolt. Tap the diode body sideways and it comes away cleanly.

Hot air is only worth setting up if you're after the PWM controller IC and it's an SMD package. 320–350 °C, hold the board steady, and it lifts in a few seconds. The primary MOSFETs are through-hole in most units, so hot air doesn't add much there.

## Watch Out For

- Primary caps hold 300 V or more for several minutes after unplugging. The bigger the supply, the longer it takes. Measure before touching. The meter reading is the only reliable indicator.
- The isolation boundary is a hard line. If you can't see a clear slot or gap separating the two halves of the board, treat the entire PCB as unsafe until the primary caps read zero.
- The lid and fan bracket have stamped edges that are sharp enough to cut you. Run a finger along them before reaching in. Cover anything that catches with electrical tape while you work.
- Domed or bulging secondary caps have failed and may be under pressure. Don't heat them. Bin them.
- Pre-2006 units use leaded solder throughout. Wash hands, ventilate when desoldering.

## Theory Links

For measuring DC voltages on salvaged boards, see [DC measurements](/open-circuits/DC/DC_5.html).

For understanding the MOSFETs and rectifiers that dominate PSU salvage value, see [Semiconductors](/open-circuits/Semi/SEMI_6.html).

## Specific Teardowns

Specific make-and-model teardowns for ATX power supplies will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

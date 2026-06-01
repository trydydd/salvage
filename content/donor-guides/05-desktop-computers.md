---
title: "Desktop Computers"
section: donor-guides
hazard: 2
hazard_summary: "Low-voltage DC once unplugged; PSU is a separate device."
author: Claude
review: Needs Human Review
---

Desktop towers and small-form-factor PCs open up in minutes and yield fans, heatsinks, cables, connectors, and a handful of board-level parts without any soldering at all. The case itself is the biggest obstacle: two thumbscrews on the rear panel and the side comes off. Everything inside is fastened, clipped, or slotted rather than glued.

## What's Inside

The ATX power supply sits in its own steel subenclosure bolted into one corner of the case. Treat it as a separate donor with its own hazard level. See the [ATX Power Supplies guide](/salvage/donor-guides/07-atx-power-supplies.html) before opening it. Everything else in the case runs on low-voltage DC the moment the PSU is disconnected.

The motherboard is the largest PCB, mounted flat against one side of the case on threaded standoffs. Around the CPU socket you'll find the VRM section: a ring of shielded inductors and polymer or electrolytic capacitors that filter the switched power to the CPU. RAM slots run alongside the socket, and PCIe slots extend toward the bottom edge for expansion cards. SATA connectors, USB headers, and front-panel headers cluster along the board edges.

Cooling hardware takes up the most physical space. The CPU cooler is a heatsink sitting directly on the CPU die, held by push-pins through the motherboard (on most Intel sockets) or a screwed backplate (on AMD and some aftermarket coolers). Many heatsinks have copper heatpipes running through them and are the highest-density copper salvage in the whole machine. Case fans mount to the front, rear, and sometimes top and bottom panels, usually with four screws each.

A small CR2032 coin cell sits in a plastic holder on the motherboard, powering the real-time clock and BIOS settings when the machine is off. It's always worth pulling.

## Before You Open It

1. Unplug from mains.
2. Press the power button once after unplugging. This drains the 5 V standby rail and any residual charge on the decoupling caps through the board's own loads.
3. Set the PSU aside and treat it separately. Don't open it during this teardown unless that's your specific plan for the session.
4. Remove the GPU before you start pulling cables near the PCIe area. A full-length GPU blocks access to half the motherboard and catches on cables when you try to slide it out later.

Once the PSU is disconnected and the power rail is drained, everything inside is safe to handle.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Fans | Case panels, CPU cooler, GPU shroud | Voltage, connector type, bearing noise, airflow direction | ★★★ |
| Heatsinks | CPU, chipset, VRM, GPU | Mounting style, fin density, flatness; heatpipe count on CPU coolers | ★★★ |
| CR2032 CMOS battery | Coin-cell holder on motherboard, usually near PCIe slots | CR2032; check voltage with a meter (should read 2.9–3.3 V) | ★★★ |
| Connectors and harnesses | Front panel, drives, motherboard edges | USB, SATA, headers, wire gauge | ★★☆ |
| RAM sticks | DIMM slots alongside CPU socket | DDR3 or DDR4; capacity marked on label; confirm slot latch releases before pulling | ★★☆ |
| Tact switches and LEDs | Front-panel board | Momentary action, LED color, lens size | ★★☆ |
| Inductors and capacitors | Motherboard power section | Package size, voltage rating, visible damage | ★☆☆ |

## How to Get Them Out

Almost everything worth taking from a desktop PC comes out without a soldering iron, so the no-iron tier is where to spend your time.

Fans unscrew with a Phillips driver, four screws each, and the connector pulls off a header on the motherboard. The 3-pin and 4-pin fan headers look similar but aren't interchangeable for PWM control, though both will spin a fan at full speed on 12 V. If you want the wire management clips that often hold fan cables to the case frame, they usually pop out of their slots with a fingernail.

The CPU heatsink is the most variable part of the teardown. Push-pin coolers (common on older Intel builds) release by rotating each pin a quarter-turn counterclockwise and then pulling straight up, one pin at a time. Alternate diagonally when releasing them: front-left, then rear-right, then front-right, then rear-left. Pulling in order rather than diagonally risks warping the cooler and stressing the PCB. Screw-down coolers just need four bolts from the back of the board. Either way, the heatsink will resist at first because the thermal paste creates a light suction. Twist gently before lifting, rather than yanking straight up, and the die won't come with it.

RAM releases by pressing both slot latches outward simultaneously (or one, on single-latch slots) until the stick pops up at an angle. Pull it out from there. If a stick doesn't pop with normal pressure on the latch, the latch is still engaged on one end.

The front-panel connectors are the fiddliest part of the no-iron teardown. The power LED, reset switch, HDD LED, and power switch connect as individual 1- and 2-pin housings onto a header block on the motherboard. They pull off one by one with needle-nose pliers or fingernails. The labeling on the motherboard header matches the printing on the connectors, but only if you squint. Keep them bundled with the front-panel board rather than scattering them.

SATA data cables pull straight off both the drive and the motherboard. Some SATA connectors have a small locking latch on the drive end that you need to press before pulling. The angled version (L-shaped connector) is easier to reach in tight drive bays and worth keeping separately from the straight ones.

With a soldering iron, the front-panel tact switches and LEDs are through-hole on most small boards. Two leads each, easy to heat and pull. The VRM inductors and capacitors on the motherboard are worth pulling only if you need a specific value and can read the markings. On boards from 2012 or earlier, check the electrolytics for bulging tops before you commit to desoldering them. A bulged cap has already failed and isn't useful.

Hot air is rarely worth setting up for desktop salvage. The occasional SMD component of interest is almost always identifiable as not worth the bother once you see what it is.

## Watch Out For

- The rear I/O shield is a stamped steel plate pressed into the back of the case, with cutouts for ports. Its edges are folded but not smooth and will cut your knuckles when you're reaching around the back of the motherboard to remove standoff screws. Run your hand over it before you commit to working behind it.
- Steel chassis cutouts for PCIe slot covers and drive-bay brackets have sharp stamped edges on the inside face. Handle the chassis with both hands around the panel edges, not around the cutout openings.
- Thermal paste on the CPU heatsink is grey or white and transfers to everything it touches. Wipe the CPU die and the heatsink base with isopropyl alcohol on a cloth before setting either down anywhere useful. Old paste that's dried out crumbles rather than smearing, but it still gets into connector sockets if you're not careful.
- Push-pin cooler retention clips on older Intel boards carry a lot of spring tension. Once you rotate all four pins to the release position, the cooler sometimes pops up on its own with enough force to scatter the pins. Keep a hand on the cooler body after the last pin releases.
- Older boards (roughly pre-2008, or any board with Taiwanese capacitors from that era) sometimes have visibly bulged or leaking electrolytics in the VRM section. The tops will be domed rather than flat. Don't pull those caps expecting to use them.

## Theory Links

- [DC measurements](/open-circuits/DC/DC_5.html) for continuity checks and fan testing.
- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for reading the regulator and MOSFET-heavy power sections around a motherboard CPU socket.

## Specific Teardowns

Specific make-and-model teardowns for desktop computers will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

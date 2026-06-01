---
title: "CRT Monitors"
section: donor-guides
hazard: 4
hazard_summary: "Anode holds 25,000V+ for weeks after unplugging."
author: Claude
review: Needs Human Review
---

This guide covers CRT computer monitors and televisions as donors, with strong emphasis on the high-voltage anode charge and the implosion risk of the tube itself.

A CRT carries two hazards that put it in the same class as a microwave oven. The picture tube and its high-voltage section store a charge of tens of thousands of volts that can stay on the anode for weeks after the set is unplugged, because the tube itself acts as a large capacitor. And the tube is a heavy glass vacuum vessel that can implode if the neck or envelope is cracked, throwing glass with real force. Both hazards have a clear procedure. Discharge the anode to the tube's ground before you touch anything, and handle the tube by its strong front face, never by the thin neck. Do those two things and a CRT becomes a normal, if bulky, donor.

If you take one thing from this page: discharge the anode to the chassis ground first, every time, before any other work inside the case.

## What's Inside

Take the rear cover off, usually a handful of screws around the back shell, and the inside is built around the tube.

The CRT itself dominates the case. It's the large glass funnel with a flat or curved face at the front and a narrow neck at the back. Slipped over a button on the side of the funnel is the high-voltage anode cap, a thick rubber suction cup with a heavy red wire running to the flyback transformer. Under that rubber cup is the metal anode clip that sits at tens of thousands of volts. The outside and inside of the funnel are coated with a conductive layer called aquadag, and together with the glass between them the tube forms its own high-voltage capacitor. That's why it holds charge.

Around the neck of the tube sits the deflection yoke, a pair of copper windings on a ferrite core that steers the beam. Toward the front, looped around the face of the tube, is the degaussing coil, a ring of copper wire with a thermistor in series that demagnetizes the shadow mask at power-on.

The high-voltage section is built around the flyback transformer, the boxy component with the thick red anode wire. The main board holds the power supply with its filter caps, the switching transistors, the rectifiers, and the video and sync circuitry. Many monitors and most small TVs also have a small speaker in the bezel and a set of rear connectors: VGA or signal input, the power inlet, and internal headers.

The low-voltage parts on the main board and the connectors are the friendly salvage. The tube, the flyback, and the anode are the dangerous region and stay off-limits until the anode is discharged.

## Before You Open It

The anode charge defines this donor. Follow this in order and don't skip the discharge, even on a set that's been unplugged for weeks. A CRT can hold its charge for a very long time, and dielectric absorption means it can build a small charge back on its own after a single discharge.

1. Unplug the set and leave it unplugged. Move the cord where you can see it.
2. Remove the rear cover and find the anode cap, the rubber suction cup on the side of the tube with the thick wire to the flyback.
3. Build or grab a discharge tool: an insulated-handle screwdriver with a clip lead attached to its metal shaft, the other end of the clip connected to the tube's ground. The ground is the bare wire or spring that contacts the aquadag coating on the outside of the funnel, or the chassis ground the set uses for it. Don't ground to mains earth through the wall.
4. With one hand behind your back, slide the screwdriver tip under the edge of the rubber anode cap until it touches the metal clip beneath. You may hear a sharp snap as the charge releases.
5. Keep the tip in contact for a few seconds, then withdraw and repeat once or twice. The tube can recover a small charge between discharges.
6. Leave the clip lead connecting the anode to ground while you work, so the tube cannot build charge back up.
7. If you have a high-voltage probe, confirm zero across the anode. Most benches don't, so the deliberate discharge-and-ground step above is the working procedure.

Keeping one hand behind your back means that if you do touch a live point, the current can't cross your chest. The grounded clip lead left in place is your proof the anode stays dead while you work.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Speakers | Front shell or lower cabinet | Impedance, size, connector style | ★★☆ |
| Degaussing coil | Wrapped around the tube face | Heavy insulated coil for experimentation | ★★☆ |
| Control buttons and small PCBs | Front panel or side controls | Tact switches, pots, board connectors | ★★☆ |
| Yoke assembly | Tube neck and funnel area | Coil pack with connector, advanced-use only | ★☆☆ |
| Cabinet hardware | Case and stand | Fasteners, brackets, tilting mechanisms | ★☆☆ |

Nothing in a CRT is a three-star headliner, which is worth knowing before you commit to one. The value is spread across solid two-star parts. The speakers, degaussing coil, and front-panel boards all come off without going near the anode once it's discharged, and the degaussing coil in particular is a good source of enameled copper wire and a series thermistor. The yoke is one star because it's a specialized part most people won't have a use for, and the cabinet hardware is one star unless you happen to need the brackets. The flyback transformer and the tube are deliberately not salvage targets here. The flyback should never be powered up loose, and the tube is heavy leaded glass with little reuse value and a real implosion risk.

## How to Get Them Out

Order matters here as much as on the microwave. Discharge the anode and leave it grounded before any tool comes out. Then take the low-voltage parts and leave the tube intact.

Pull the connectors and the speaker first. The rear connectors unscrew or unclip from the panel, and the speaker lifts out of the bezel after you free its two wires. The front-panel control board unplugs and unscrews the same way.

The main board slides out after you unplug its connectors, including the neck board on the end of the tube and the leads to the yoke and degaussing coil. The board-mounted filter caps may still hold a charge of their own, so measure across the large ones with a meter on DC volts and discharge any above 30 V through a resistor before handling them, the same as on any power supply.

The degaussing coil is just looped around the tube face and taped or clipped in place. Free the clips and lift it off, keeping the series thermistor with it.

The deflection yoke clamps to the neck of the tube behind the gun. It's held by a clamp screw and often a dab of glue or wax. Loosen the clamp, then gently work the yoke back off the neck, which is the most fragile part of the tube. Snapping it lets air in and can cause the tube to implode, so support the tube and ease the yoke straight back rather than twisting hard against the neck. If you only want the copper and don't need the yoke whole, this is the one part where forcing it isn't worth the risk to the neck.

Leave the tube itself intact. There's little salvage value in the glass, and the safe move is to keep the envelope whole and dispose of it through proper e-waste or glass recycling. If you must move it, carry it by the strong front face with both hands, never by the neck.

## Watch Out For

- The anode and high-voltage section can hold a dangerous charge for weeks after power-off. Discharge the anode to the tube's ground with an insulated tool, leave a clip lead grounding it while you work, and keep one hand behind your back during the discharge. This is the hazard most likely to hurt you on a CRT.
- The tube is a glass vacuum vessel and can implode if the neck or envelope cracks, throwing glass. Wear eye protection and gloves, never knock or scratch the glass, and keep the tube intact. The neck is the weakest point, so handle the yoke removal gently.
- The board-mounted filter caps hold their own charge. Measure and discharge them through a resistor before touching, just as on any mains power supply.
- CRT glass is heavy leaded glass and the chassis has sharp stamped edges. Lift the tube with both hands under the face, and run a finger along any metal edge before gripping it.
- Don't power the flyback transformer or any of the high-voltage section loose on the bench. It generates tens of thousands of volts by design.

## Theory Links

- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for understanding the power devices and regulators on the lower-risk support boards only after safe separation.
- [Experiments](/open-circuits/Exper/EXP_2.html) for testing speakers, switches, and other low-voltage salvage once it is fully removed from the CRT chassis.

## Specific Teardowns

Specific make-and-model teardowns for CRT monitors will be linked here as they are added, prioritizing safety procedure and identifying which parts can be harvested without going near the tube. See `content/donor-guides/teardowns/` for in-progress guides.

---
title: "Microwave Ovens"
section: donor-guides
hazard: 4
hazard_summary: "HV capacitor can hold LETHAL charge for hours or days."
author: Claude
review: Needs Human Review
---

This guide covers microwave ovens as donors, with strong emphasis on the lethal high-voltage capacitor and the safe-to-harvest parts that sit away from the high-voltage section.

A microwave oven is two machines in one box. There's an ordinary low-voltage appliance: a turntable motor, a cooling fan, door switches, and a control board, all of which are good, easy salvage. Wrapped around it is a high-voltage section that runs at around 2000 V and stores enough energy in one capacitor to kill you. That capacitor can stay charged for hours or days after you unplug the oven. This is the most dangerous donor in the whole guide, and the danger is concentrated in one part. Learn to identify the high-voltage section, discharge its capacitor before anything else, and keep clear of it, and the rest of the oven is straightforward.

If you take one thing from this page: discharge the high-voltage capacitor first, every time, before you reach for anything else inside the case.

## What's Inside

Take the outer cabinet off, usually a few screws along the back and sides that let the wrap-around steel cover slide back, and the interior divides into two clear regions.

The high-voltage section sits to one side of the cavity. It holds four parts that work together. The high-voltage transformer is a heavy block of iron and copper, far heavier than its size suggests. From it, two thick wires run to the high-voltage capacitor, a sealed metal or plastic can usually marked with its capacitance and a voltage rating around 2100 VAC. Next to the capacitor is the high-voltage diode, a small sealed cylinder that rectifies the transformer output. The whole section feeds the magnetron, the finned aluminum block with a ceramic dome and a pair of strong magnets that generates the microwaves. Everything in this region runs at lethal voltage when powered, and the capacitor holds charge after it's off. Treat all of it as dangerous until the capacitor is proven dead.

The low-voltage region is everything else, and it's the friendly part. Under the floor of the cooking cavity is the turntable motor, a small synchronous AC motor that turns slowly. At the back of the cabinet is the cooling fan that blows air over the magnetron. Behind the front panel are the door interlock switches, the control board with its relays and display, and the keypad. On the cavity wall you'll see a small beige rectangle, the mica waveguide cover, a high-temperature insulator.

The low-voltage parts are the reason most people open a microwave. The high-voltage parts are mostly scrap copper and iron, and the magnetron carries its own warning covered below.

## Before You Open It

The high-voltage capacitor is the hazard that defines this donor. Follow this in order, and don't skip the discharge even if the oven sat unplugged for days. Some capacitors hold charge far longer than you'd expect, and a failed internal bleeder resistor means it may not have drained at all.

1. Unplug the oven from the wall and leave it unplugged. Move the cord where you can see it so nobody plugs it back in.
2. Remove the cabinet cover and locate the high-voltage capacitor. It's the sealed can wired to the transformer, usually marked with a microfarad value and a rating near 2100 VAC.
3. Don't touch the capacitor terminals yet. Assume it's charged.
4. Discharge it deliberately. Clip a resistor of a few hundred ohms to a couple of kilohms, rated 5 W or more, across the two capacitor terminals using well-insulated leads and an insulated handle. Hold it for several seconds. Then, to be certain, short across the two terminals with an insulated-handle screwdriver, and short each terminal to the metal chassis as well, since one side may reference the case.
5. Measure across the terminals with a multimeter on DC volts. It must read near zero. If it doesn't, repeat the discharge and measure again.
6. Only after the meter confirms zero should you reach into the high-voltage section or start removing nearby parts.

The resistor-first step is gentler on the capacitor and on you than a bare short, which throws a large spark at this energy level. The meter reading is the only proof you have. A capacitor that looks identical to a safe one can still be holding 2000 V.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Door interlock switches | Latch assembly by the door | Microswitch type, terminal style, mechanical action | ★★★ |
| Cooling fan | Chassis side or rear | AC or DC type, blade size, mounting pattern | ★★☆ |
| Turntable motor | Under the cavity floor | AC synchronous type, shaft coupler style | ★★☆ |
| Roller ring and mechanical hardware | Turntable assembly and chassis | Reusable motion hardware and odd brackets | ★☆☆ |
| Control-panel buttons and display boards | Front control area | Connector type, membrane stack, display driver board | ★☆☆ |

The door interlock switches are the standout, which surprises people who came for the transformer. A microwave carries two or three mains-rated microswitches with a positive mechanical action, and they're worth more in your parts bin than anything in the high-voltage section. The cooling fan and turntable motor are solid two-star picks: the synchronous turntable motor turns slowly and steadily, which is exactly what you want for a clock, a display turntable, or any slow-rotation project. The roller ring and control board sit at one star, useful only if you happen to need them. The high-voltage transformer and magnetron are deliberately left off this table as salvage targets. They're mostly scrap, the transformer should never be powered up loose, and the magnetron carries the material hazard below.

## How to Get Them Out

Order matters more here than on any other donor. Discharge the high-voltage capacitor and confirm zero with the meter before you pick up any tool. Then work the low-voltage parts first and leave the high-voltage section until last, if you touch it at all.

The door interlock switches sit in a plastic carrier behind the front panel. Note which switch is which before you remove them, because the interlock chain matters if you ever reuse them, then unclip the carrier and free the spade terminals. They usually pull off their tabs without any heat.

Pull the turntable motor from under the cavity floor. It's held by a couple of screws and a simple two-wire connector. Unplug or snip the leads and it's out. The cooling fan at the rear comes off the same way: a few screws and a connector or spade terminals. If you only want the motor or fan and not the wiring, cut the leads at the connector. If you want the connector too, ease it off the board pins.

The control board lifts out after you unplug its ribbon and connectors and remove its mounting screws. Keep the keypad with it if you want the display working later. The mica waveguide cover is just unscrewed or unclipped from the cavity wall. It's a useful high-temperature insulator but fragile, so flex it as little as possible.

If you choose to take the high-voltage parts for scrap, only do it after the capacitor reads zero. The transformer is held by two or four bolts through the chassis floor. It's heavy, so support it before the last bolt comes out. The magnetron is bolted to the waveguide with four nuts. Undo them and lift it away, handling it by the metal body. Don't open it, grind it, or break its ceramic.

## Watch Out For

- The high-voltage capacitor can hold a lethal charge for hours or days after unplugging, and its internal bleeder resistor cannot be trusted. Discharge it through a resistor, short the terminals and each terminal to chassis with an insulated tool, and confirm zero on a meter before any other work. This is the one hazard on the salvage bench that can kill rather than just hurt.
- The magnetron's ceramic insulators contain beryllium oxide in some units. Intact, it's safe to handle. The danger is the dust, which is toxic if inhaled. Never grind, sand, drill, or break the ceramic, and don't smash a magnetron open. If a magnetron's ceramic is already cracked or broken, bag it and dispose of it rather than working on it.
- The high-voltage diode can retain a charge through the capacitor. Treat the whole high-voltage section as live until the capacitor reads zero.
- Microwave chassis are thin stamped steel with sharp edges everywhere, especially where the cabinet cover slides. Run a finger along an edge before gripping, wear gloves, and tape over anything that catches.
- The high-voltage transformer is dense and heavy. Support it before removing the last bolt so it doesn't drop and tear its wiring loose.
- The magnetron magnets are strong. Keep them away from cards, drives, and anything else magnetic-sensitive.

## Theory Links

- [DC measurements](/open-circuits/DC/DC_5.html) only for the low-voltage control parts once they are safely separated from the HV section.
- [Experiments](/open-circuits/Exper/EXP_2.html) for test habits you can use on switches, lamps, and motors after removal from the dangerous chassis.

## Specific Teardowns

Specific make-and-model teardowns for microwave ovens will be linked here as they are added, focused on safe-to-harvest mechanical assemblies and documenting which parts should stay out of scope. See `content/donor-guides/teardowns/` for in-progress guides.

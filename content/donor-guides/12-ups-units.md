---
title: "UPS Units"
section: donor-guides
hazard: 4
hazard_summary: "Batteries stay live; can deliver very high short-circuit current."
author: Claude
review: Needs Human Review
---

This guide covers small UPS units as donors for sealed lead-acid batteries, transformers, capacitors, relays, heavy-gauge wiring, and IEC connectors.

A UPS is a generous donor packed into a heavy little box, and the thing that makes it generous is also what makes it dangerous. At its heart is a sealed lead-acid battery that's always live. You can't unplug it the way you unplug a wall charger. A charged lead-acid battery can dump hundreds of amps into a dead short without warning, enough to weld a wrench across the terminals, throw molten metal, and start a fire. The hazard isn't high voltage here, it's high current from a source that's energized the moment you open the case. Disconnect and insulate the battery before you do anything else, work with insulated tools, and the rest of the UPS is rewarding salvage.

If you take one thing from this page: isolate the battery first, cover its terminals, and never let a tool bridge them.

## What's Inside

Open the case, usually a few screws on the bottom and rear, and the layout is consistent across brands.

The battery takes up a large share of the volume, in its own compartment or strapped to the chassis floor. It's a sealed lead-acid (SLA) block, 12 V in small units or 24 V and up in larger ones, marked with its amp-hour rating and fitted with spade or bolt terminals. It feeds the rest of the unit through heavy wires, often with an inline fuse.

The inverter and charger circuitry lives on the main board. The charger keeps the battery topped up from the mains. The inverter turns battery DC back into AC when the mains fails. Between them sits a transformer, either a toroid or an EI type, that steps the voltage up or down. It's heavy, the same as the one in an audio amplifier, and worth pulling.

Around the inverter you'll find the power MOSFETs bolted to a heat sink, the large filter capacitors on the DC bus, and an output relay that switches the load between mains and inverter. The main board also carries the control electronics, smaller caps, and rectifiers. Connectors and heavy-gauge wiring run throughout, along with the IEC sockets and fuse holders on the rear.

The battery, transformer, and the mains hardware are the headline salvage. The relay, MOSFETs, caps, and wiring are easy bonus parts once the battery is isolated.

## Before You Open It

The battery is the hazard that defines this donor, and unlike a capacitor it doesn't bleed down. It's energized until you physically disconnect it. Follow this in order.

1. Unplug the UPS from the mains and switch it off. The unit may keep running on the battery, and an unplugged UPS is still live inside.
2. Remove anything conductive from your hands and wrists: rings, watches, metal bracelets. These are what cause the worst lead-acid burns when they bridge a terminal.
3. Open the case and find the battery. Note which lead is positive and which is negative before you touch anything.
4. Disconnect the battery first, before any other work. Use an insulated-handle tool, free the negative lead first, then the positive. Work one terminal at a time and don't let the tool touch both terminals or the chassis at once.
5. Insulate the disconnected terminals and lead ends immediately. Cover each with electrical tape or a terminal cap so nothing can bridge them later. Set the battery aside, upright, away from metal.
6. Now treat the board like any mains power supply. The DC bus filter caps can hold a charge. Measure across the large caps with a meter on DC volts and discharge any above 30 V through a resistor of a few hundred ohms before reaching in.

The order is the whole procedure: battery out and insulated first, capacitors discharged second, everything else after. A lead-acid short happens in an instant and gives no warning.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| IEC sockets and mains hardware | Rear panel | C13/C14 fittings, fuse holders, switch gear | ★★★ |
| Sealed lead-acid battery | Battery compartment | 12 V or 24 V, amp-hour rating, terminal type | ★★★ |
| Toroidal or EI transformer | Inverter section | Primary/secondary voltages, VA rating, weight | ★★☆ |
| Relays | Inverter and transfer section | Coil voltage, contact form, current rating | ★★☆ |
| Fans | Rear panel or top cover | Voltage, size, bearing wear, connector | ★★☆ |
| Heavy-gauge wire and ring lugs | Battery and inverter harnesses | Insulation condition, current-handling clues | ★★☆ |

The IEC sockets and mains hardware are an easy three-star win because good panel-mount C13/C14 fittings, fuse holders, and switches are awkward to buy and come straight off the rear panel. The battery is the other three-star part if it still holds a charge: a usable 12 V or 24 V source for projects, though even a tired one has life left for low-demand uses. Check it with a meter and, if you can, a load test before trusting it. The transformer, relays, fans, and heavy wiring are solid two-star parts for power builds. The MOSFETs and DC-bus caps are worth pulling too once the bus reads zero, the same as on any power supply.

## How to Get Them Out

The safe order is fixed: isolate the battery, discharge the caps, then remove parts.

With the battery disconnected and its terminals taped, lift it out of its compartment. It's dense for its size, so use both hands and keep it upright. If the unit had an inline battery fuse, keep it with the battery leads as a reference for the current rating.

Once the DC bus caps read near zero on the meter, take the rest in whatever order is convenient. The rear IEC sockets, fuse holders, and switch unscrew from the panel, then unsolder or unclip from the board. The output relay and connectors come off easily: the relay either unplugs from a socket or desolders from the board with an ordinary iron, and AC sockets and spade terminals pull off their tabs.

The transformer is bolted through the chassis with one central bolt on a toroid or four corner bolts on an EI type. Support it before the last bolt comes out so it doesn't drop and tear its leads. Label the primary and secondary leads before you cut them, and cut them long.

The MOSFETs sit on the inverter heat sink. Remove the screws holding them to the sink before you pick up the iron, then desolder the leads. Lift the heat sink with the MOSFETs attached if you want to keep them paired with their hardware, and keep the insulating pads and shoulder washers together. The large filter caps are through-hole. Heat the leads from the underside and rock each cap free while you wick or pump, the same as on any power supply.

## Watch Out For

- The battery is always live and can deliver a huge short-circuit current. Disconnect and insulate it before any other work, remove rings and watches, use insulated tools, and never let a tool bridge the two terminals or a terminal and the chassis. This current can weld metal and start a fire.
- Damaged or swollen lead-acid batteries can leak sulfuric acid. Don't pry open or puncture a battery. If one is cracked or leaking, wear gloves and eye protection, keep it upright, and dispose of it through proper battery recycling rather than working near it. Wash any acid contact with plenty of water.
- The DC bus filter capacitors hold a charge after the battery is out. Measure across the large ones and discharge any above 30 V through a resistor before touching them.
- The transformer is heavy and dense. Support it before removing the last bolt so it doesn't drop and tear loose its wiring.
- The chassis has sharp stamped edges. Run a finger along an edge before gripping, and tape over anything that catches while you work.
- Never store a salvaged lead-acid battery near anything that can short it. Cap the terminals whenever it's not in a circuit.

## Theory Links

- [DC measurements](/open-circuits/DC/DC_5.html) only for the low-voltage control parts once they are safely separated from the HV section.
- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for identifying the inverter transistors and rectifiers that often dominate the board layout.

## Specific Teardowns

Specific make-and-model teardowns for UPS units will be linked here as they are added, prioritizing battery isolation and identifying which parts can be harvested by non-experts. See `content/donor-guides/teardowns/` for in-progress guides.

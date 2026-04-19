---
title: "Solar Electric Fence Chargers"
section: donor-guides
hazard: 3
hazard_summary: "Output capacitors hold 2–10 kV; discharge before reaching into the circuit."
---

## What's Inside

Four Phillips screws on the back or base (usually with a rubber gasket seal underneath), and you're looking at a battery compartment and a single PCB. The battery is a sealed lead-acid (SLA/AGM) pack, typically 6V or 12V at 4–12Ah depending on the model, sitting in a foam-lined cavity or held by a strap. The solar panel is either built into the top face of the case or attached externally by a short cable through a grommet.

The PCB sits above the battery and splits into two zones separated by the transformer. On the low-voltage side: a blocking diode from the solar input, a basic charge controller (sometimes just a voltage comparator and switching transistor, sometimes a dedicated PWM IC), and the oscillator circuit, usually a 555 timer or a small 8-pin microcontroller. On the high-voltage side: the transformer secondary, a fast-recovery or HV rectifier diode, and the output storage capacitor. That capacitor is a radial or axial electrolytic, typically 1–10µF rated at 400–2000V. It's the part that holds charge after the battery is disconnected.

Cheaper units use a relay driven by the oscillator; you can hear it clicking during operation. Better units use a solid-state switch, an IGBT or power MOSFET, in the primary circuit. The relay is worth noting because it's the most common failure point in these chargers, and a unit where the relay has failed is otherwise often fine.

The solar panel is the main reason to pull one of these. Most units in the 1–10 joule output range carry a 5–20W monocrystalline or polycrystalline panel that's worth considerably more as salvage than any single component on the PCB.

## Before You Open It

1. Disconnect the fence lead and earth lead from the output terminals first. If the unit was running before it came to you, the fence line may still have charge sitting on it.
2. Disconnect the solar panel lead from the input connector or terminal block.
3. Disconnect or remove the battery. SLA batteries with spade terminals lift out once the leads are off. Some cheaper units solder the leads directly to the battery posts; in that case, cut the leads close to the PCB, not close to the battery, so the leads stay with the board.
4. Wait five minutes, then measure across the output storage capacitor terminals with a multimeter on DC voltage before touching anything on the high-voltage side. If you read above 30V, clip a 10kΩ 1W resistor across the capacitor terminals and recheck every couple of minutes until it reads below 5V.

The battery is the only energy source once the solar panel is disconnected. After removing it, the capacitor discharges through the circuit's own internal resistance, but on units without an explicit bleeder resistor this can take longer than you'd expect. Measuring before touching is not optional.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Solar panel | Top face of enclosure or external via cable | 5–20W; 6–24V open-circuit; monocrystalline or polycrystalline; test Voc with a multimeter in daylight | ★★★ |
| Sealed lead-acid battery | Lower compartment, below PCB | 6V or 12V; 4–12Ah; check for firm case and resting voltage above 6V or 12.5V; swollen case means reject | ★★★ |
| HV output capacitor | HV side of PCB, near output terminal block | 1–10µF; 400–2000V; radial or axial electrolytic; voltage rating printed on body | ★★☆ |
| HV rectifier diode | HV side of PCB, between transformer secondary and capacitor | DO-27 or similar axial package; 1–10kV rating; 1–3A; sometimes two diodes stacked in series | ★★☆ |
| Step-up transformer | Centre of PCB, separating the LV and HV zones | Ferrite EI or EE core; open-bobbin or epoxy-encapsulated; high turns ratio | ★★☆ |
| Power MOSFET or IGBT | LV side of PCB, near transformer primary | TO-220 or D-PAK; N-channel; 100–400V, 5–20A typical | ★★☆ |
| Weatherproof enclosure | The outer case | IP65 or better; polycarbonate or ABS; screw-mount tabs on exterior | ★★☆ |
| Oscillator IC | LV side of PCB, small DIP or SMD | NE555, LM555, or 8-pin MCU; only worth pulling if you have a use for one | ★☆☆ |

## How to Get Them Out

Start with the solar panel and battery. If the panel is external, it unplugs from a 2-pin connector lead. If it's integral to the top of the case, four small screws hold it and the cable passes through a grommet you can push out from inside. The lead wire is often thin, 22–24 AWG, so if you plan to use the panel in a project, cut the wire close to the enclosure rather than close to the panel and add a proper connector at the project end.

The battery comes out after disconnecting the leads. SLA spade terminals pull off with a side-to-side wiggle. If the leads are soldered to the battery posts, cut them 20–30mm from the battery rather than from the PCB, so you keep the leads on the board side for identification later.

On the PCB, the HV capacitor and rectifier diode are the main through-hole targets. Confirm the capacitor has discharged by measuring it first, then heat from the underside while rocking and wick or pump from below. The diode is axial; note its orientation before desoldering since the polarity markings on the board may be worn or obscured by flux. The step-up transformer has four mounting pins in most units. Wick all four before trying to lift it, since a partially desoldered transformer will take a trace with it. If it's epoxy-encapsulated it'll come out intact as a unit regardless.

The power MOSFET or IGBT is through-hole in most units, sometimes with a small bolt-on heatsink tab. Remove the heatsink mounting screw before picking up the iron. Heat from below and wiggle, or pump if you have one.

If the unit uses a relay rather than a MOSFET, the relay is worth pulling only if it's a standard 12V SPDT or DPDT footprint you actually need. Worn contacts are the most common failure mode in these chargers, so treat any relay from one as suspect until you've tested it.

## Watch Out For

- The HV output capacitor holds 2–10kV even after the battery is disconnected. Measure across the capacitor terminals before touching anything on the high-voltage side. The boundary is the transformer: everything between the transformer secondary and the output terminals is HV territory.
- SLA batteries can deliver hundreds of amps into a short circuit. Don't rest a tool across the terminals and don't carry the battery loose in a bag with other metal. A swollen or bulging case means the battery has failed internally; don't attempt to recharge or store it.
- These units live outdoors, often in wet and dirty conditions. Battery terminals are frequently corroded and some units will have moisture or mould inside the case. Wear nitrile gloves when handling corroded terminals and work with ventilation if there's any visible mould growth.
- Disconnect the fence and earth leads before disconnecting the battery, not after. A long fence line has distributed capacitance and may carry a small residual charge even when the charger is off.
- Enclosure screws on older units are often rusted. Use a well-fitting screwdriver and penetrating oil if needed. A stripped screw in a plastic mounting boss ruins the enclosure as a reusable part.

## Theory Links

For measuring DC voltages on the solar panel and battery, see [DC measurements](/open-circuits/DC/DC_5.html).

For the MOSFETs, IGBTs, and HV rectifier diodes in the pulse circuit, see [Semiconductors](/open-circuits/Semi/SEMI_6.html).

## Specific Teardowns

Specific make-and-model teardowns for solar electric fence chargers will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

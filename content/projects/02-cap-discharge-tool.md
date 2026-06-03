---
title: "Capacitor Discharge Tool"
section: projects
author: Claude
review: Needs Human Review
---

The cap discharge tool is a resistor-and-LED probe that drains stored charge from capacitors before you touch them. Build it once, keep it where you can see it at the start of a teardown, and reach for it before opening any mains-connected equipment. The LED dims as the cap discharges and goes out when the voltage drops low enough to be close to safe.

This tool makes the process faster and reduces guesswork. It does not make it safe on its own. After the LED goes out, you still need to measure across the cap terminals with a multimeter to confirm the voltage has actually dropped. The meter reading is the confirmation. The LED is the rough progress indicator.

The version described here covers capacitors in the 5–80 V range: audio amplifier filter banks, secondary PSU rails, and similar moderate-voltage sources. You'll need a wirewound power resistor from an ATX power supply or audio amplifier chassis, an indicator LED from any low-voltage PCB, and heavy-gauge insulated wire for the probe leads. For ATX primary caps (200–400 V), the ATX Power Supplies guide describes the 10 kΩ bleeder approach that voltage level requires. For CRT anode discharge and microwave HV caps, each of those guides has a dedicated procedure. Both are out of scope for this tool.

## Purpose and limits

A capacitor stores charge proportional to its capacitance and the voltage across it. Large audio filter caps, typically 4700–22000 µF at 35–80 V, hold 3–70 joules at full charge. That's not lethal in the way a microwave HV cap is, but it's enough to fuse a screwdriver tip, throw your hand, and destroy whatever the cap was connected to. The discharge tool turns that energy into heat in a resistor over several seconds while you watch.

The indicator LED connects in parallel with the power resistor, with a 10 kΩ series resistor in the indicator branch to limit current. At full cap voltage the LED is bright. As the cap drains, the voltage across both branches falls, current through the LED drops, and the indicator dims and goes out.

There's a gap the indicator doesn't close: below about 10–15 V the LED goes dark even though some charge remains. A dark LED means mostly discharged, not confirmed safe. The meter reading is what closes that gap.

## Parts to salvage

| Part | Where to get it |
|------|-----------------|
| Wirewound resistor, 1 kΩ, 10 W | ATX Power Supplies, secondary PCB area; CRT Monitors, main board power stage; Audio Equipment, driver or output stage |
| Through-hole LED, any colour | Battery devices, front panel; Routers and modems, indicator row |
| Through-hole resistor, 10 kΩ, 1 W | Desktop computers, motherboard resistor areas; any 5 V logic board |
| Heavy-gauge insulated wire, 20–22 AWG | Cut from mains-rated appliance cable; heavier insulation is better than thin hookup wire here |
| Short lengths of heat-shrink tubing, two sizes | Any device with internal wiring |

Buy the probe clips new. Alligator clips from salvage have unpredictable spring tension and worn jaw teeth that slip off cap terminals at exactly the wrong moment.

For the heat-shrink: every exposed conductor junction on this tool gets covered before use. A bare solder joint on a discharge probe is not acceptable.

## Build details

The circuit: the 1 kΩ 10 W power resistor connects across both probe leads, positive to negative. The indicator branch (LED anode to cathode, then 10 kΩ in series) also connects positive to negative, in parallel with the power resistor. When the cap is charged, both branches carry current. The power resistor does the discharge work. The LED shows the state.

<figure>
  <img src="../images/cap-discharge.svg" alt="Two parallel branches between Probe+ and Probe−. Top branch: 1 kΩ 10 W power resistor for discharge. Bottom branch: LED in series with a 10 kΩ 1 W resistor for the indicator." loading="lazy">
  <figcaption>Cap discharge tool circuit: 1 kΩ / 10 W power resistor provides the discharge path, with LED and 10 kΩ resistor in series forming the indicator branch in parallel.</figcaption>
</figure>

Before building, measure the wirewound resistor with your meter. Large wirewound resistors often have colour bands obscured by lacquer, and body markings can be missing entirely. If your meter reads 900 Ω–1.1 kΩ, it's the right part. The 10 kΩ indicator resistor needs to be at least 1 W rated. A standard ¼ W part will get hot at 80 V.

1. Cut two lengths of heavy-gauge wire, each at least 600 mm. Mark one with red tape or permanent marker (positive). These are the probe leads.
2. Solder one terminal of the 10 W resistor to the positive lead and the other terminal to the negative lead. This is the discharge path. Cover the resistor body and both solder joints with heat-shrink.
3. Solder the LED anode (longer leg) to the positive probe node, the same point where the power resistor connects. Solder the LED cathode to one end of the 10 kΩ resistor. Solder the other end of the 10 kΩ to the negative probe node, the same point where the power resistor's other terminal connects. The indicator path runs: positive node → LED → 10 kΩ → negative node.
4. Cover both LED legs and both leads of the 10 kΩ resistor with heat-shrink. The only bare metal when you're done should be at the two probe tips.
5. Solder or crimp alligator clips to the probe ends.

The assembly can stay as a compact wired lump or be mounted in a small project box. The box is worth doing if you'll use the tool regularly. The 10 W resistor will get noticeably warm during a full discharge, and having the leads strain-relieved prevents joints pulling loose after repeated use.

One thing beginners get wrong: reversed LED polarity. If the LED doesn't light when you connect to a known-charged cap, check the LED orientation before assuming the cap is already discharged. The discharge still happens either way (the power resistor doesn't care about polarity), but without the correct orientation the indicator branch is reverse-biased and won't light.

## Procedure for use

1. Unplug the equipment. Wait two minutes. Starting with passive bleed time means the tool absorbs less energy and the LED doesn't saturate immediately.
2. Identify the caps to discharge: the tall upright electrolytic cans near the power input section of the board, not the small signal caps scattered around the rest of the PCB.
3. Measure across the cap terminals with your multimeter on DC volts before connecting the tool. This confirms the cap is actually charged and gives you a starting voltage to compare against.
4. Connect the positive (red) probe to the cap's positive terminal and the negative probe to the negative terminal. The LED should light on any cap above about 15 V.
5. Hold both probes steady and watch the LED dim over the next 10–60 seconds. When it goes dark, remove the probes.
6. Measure across the cap terminals again. You should read below 5 V. If you're above 10 V, apply the tool again and wait longer before re-measuring.
7. When the meter confirms below 5 V, the cap is safe to touch.

Store the tool somewhere you see it before a teardown starts. Hanging it near your multimeter means you reach for it automatically rather than improvising.

## Theory links and cautions

For voltage, resistance, and current during discharge, see [DC measurements](/open-circuits/DC/DC_5.html).

For capacitor charge and discharge curves and the maths behind why the LED dims gradually rather than snapping off, the [DC circuit experiments](/open-circuits/Exper/EXP_3.html) cover RC timing and decay in detail.

To extend the tool's range to handle ATX primary caps (200–400 V), replace the 1 kΩ power resistor with a 10 kΩ 25 W wirewound unit and scale the LED indicator resistor to 47 kΩ. At that resistance the discharge takes several minutes rather than seconds, which is normal. Add a small piezo buzzer in parallel with the LED so you get an audible tone while the cap is still charged and can step away while waiting.

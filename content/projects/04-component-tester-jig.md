---
title: "Component Tester Jig"
section: projects
author: Claude
review: Needs Human Review
---

The component tester jig is a small breadboard or stripboard layout wired with a handful of permanent test circuits: a 3 V battery supply, a continuity indicator, an LED test station with known series resistance, and a three-header transistor socket. You'll use it to quickly confirm whether a salvaged LED lights, a switch closes, a diode conducts in the right direction, and an NPN transistor switches a load. Each test takes a few seconds, which matters when you're sorting a bag of mixed parts.

This jig doesn't replace a multimeter. It can't measure resistance, capacitance, or inductance. What it does is handle the go/no-go tests that are tedious with a meter set to a different mode every time: push an LED into the test station and you know in two seconds whether it lights and in which direction. That kind of quick sorting is where the jig earns its place on the bench.

To build it you'll need a small breadboard, a 2×AA battery holder from battery devices, a handful of through-hole resistors and an LED from any low-voltage PCB, and a short length of hookup wire. The whole build takes under an hour on a breadboard.

## What the jig should cover

The most common go/no-go tests when sorting salvaged components: does this LED light and in which direction, does this switch or fuse have continuity, is this diode conducting in the right direction, and will this NPN transistor switch a load when a base signal is applied. The jig is built for exactly those four checks.

Resistor verification belongs on a multimeter in resistance mode rather than on the jig. So does capacitance, which needs a meter with a cap function or the M328-style module described in the extensions. Keeping the jig focused on visual indicator tests makes it fast and unambiguous.

The supply runs at 3 V from two AA cells. This forward-biases most common salvaged LEDs (red, yellow, green) and small-signal diodes. Blue and white LEDs sit close to the 3 V threshold and may glow only dimly. That's a supply voltage constraint, not a fault in the LED.

## Parts to salvage

| Part | Where to get it |
|------|-----------------|
| Through-hole LEDs, two or three colours | Battery devices, front panel; Routers and modems, indicator row |
| Through-hole resistors: 220 Ω (×2), 1 kΩ (×1), 47 kΩ (×1) | Desktop computers, motherboard; Routers and modems, main PCB |
| AA × 2 battery holder with leads | Battery devices, rear shell or battery tray |
| Momentary tact switch | Battery devices, board edge; Routers and modems, reset switch |
| 2.54 mm male header pin strips | Routers and modems, rear I/O header; Laptops, daughterboard edge connectors |

Buy a new half-size (170-point) breadboard rather than using a salvaged one. Worn contact clips give intermittent connections, and a bad contact in a test jig means you can't trust your results. A new breadboard costs almost nothing.

## Build layout

Arrange the jig in four sections from left to right. A fixed layout means you remember where each section is without reading the labels every time.

1. Power section (columns 1–4): connect the battery holder positive lead to the top red power rail and the negative lead to the blue power rail. These two rails run the full length of the breadboard and power everything.
2. Continuity indicator (columns 5–8): wire a 220 Ω resistor from the red rail to an LED anode. Connect the LED cathode to the blue rail. Two bare header pins below this form the test points. When anything conductive bridges the two test-point pins, the series LED lights.
3. LED test station (columns 10–15): place a 220 Ω resistor from the red rail to one header pin (the positive test pin). Run a second header pin from the blue rail (the negative test pin). To test a salvaged LED, push its anode into the positive pin and cathode into the negative pin. If it lights, it's working. If it doesn't, flip it to locate the anode. If it doesn't light in either orientation, the LED is open or requires more than 3 V.
4. Transistor test station (columns 17–25): place three labeled header pins: B, C, and E. For NPN testing, wire the B pin through a 47 kΩ resistor to the red rail, the C pin through a 1 kΩ resistor to the anode of an indicator LED whose cathode goes to the red rail, and the E pin directly to the blue rail. When a working NPN transistor is inserted with its leads matched to B, C, and E, base bias allows current through the collector and the LED lights.
5. Label each section with a strip of tape and marker: "Cont", "LED", "NPN". Add + and − at each end of the power rails on the breadboard edge.

That's the breadboard version and it's enough for sorting. The contacts loosen after a year or two of use, and an intermittent connection in the transistor station produces confusing results where a working transistor seems to fail. When that starts happening, the stripboard build is worth the hour.

For the stripboard version: transfer the same layout, solder the resistors and indicator LEDs in place, and use male header pins as test points so you can push component leads in. Add a small slide switch in series with the battery to avoid draining the cells when the jig is stored. A salvaged tact switch also works, but you'll have to hold it down during each test.

One thing beginners get wrong in the transistor station: the 47 kΩ base resistor may be too large to saturate some transistors fully, so the indicator LED glows dimly rather than fully bright. If you see a dim indicator on a transistor you know is working, drop the base resistor to 10 kΩ. Start with 47 kΩ because it handles unknown gain values without stressing the base junction. It just means some transistors appear dim rather than fully on.

## Using the jig

LED test: push the LED leads into the test station, anode into the + post and cathode into the − post. It lights: working. It doesn't light: try the reverse orientation to find the anode. If it still doesn't light in either direction, it's open. Blue and white LEDs may be dim at 3 V, which is normal.

Switch and fuse test: touch both component leads against the two continuity test-point pins. A closed switch or intact fuse lights the indicator. An open switch should not light it. If the indicator lights with both leads touching the same contact, there's a solder bridge somewhere in the jig build.

Diode polarity: insert the diode leads into the continuity test points, one way, then the other. The direction that lights the indicator is the forward direction (anode positive). This is faster than switching your meter into diode mode for a bag of unmarked diodes.

NPN transistor test: identify the pinout from the transistor's part number and a datasheet, then insert each lead into the matching B, C, or E header pin. The indicator should light. If it doesn't, check the pinout. TO-92 NPN transistors vary in whether the flat side reads EBC, CBE, or another order, and getting that wrong is the most common reason a working transistor appears to fail. Try all three rotations before concluding the transistor is dead.

PNP transistors need the supply polarity reversed. For occasional PNP testing, touching a flying lead from a small 3 V cell reversed across the battery holder is the quick way. If you regularly handle PNP devices from audio output stages, a second reversed battery holder next to the jig is worth adding.

## Theory links and future add-ons

For LED and battery circuits that explain why each test station works, the bench [experiments](/open-circuits/Exper/EXP_2.html) cover the series-circuit basics in exactly the right order.

For voltage drop, resistance, and what the meter is measuring when you check a component, see [DC measurements](/open-circuits/DC/DC_5.html).

The most useful extension is a M328-style component tester module (buy new for around the price of a coffee): it identifies resistors, capacitors, inductors, diodes, transistors, and MOSFETs automatically and mounts beside the breadboard. Add a 9 V battery snap from any donor device to power the module separately from the jig's 3 V section. Try wiring a 5 V rail from a salvaged wall-wart alongside the 3 V section to bring full brightness to blue and white LEDs when you're sorting LED bulb salvage. Wire a second transistor station with the polarity reversed for PNP devices if you work through a lot of audio amplifier output transistors from audio equipment.

---
title: "Relays"
section: components
---

Relays come off boards with their specs printed on the case and their contacts usually in better shape than you'd expect. A multimeter and the right supply voltage is enough to test them thoroughly without any other equipment.

## Read the case markings

Most PCB relays print the coil voltage, contact form, and contact current rating directly on the plastic case. The coil voltage is the most important thing to read first: common values in consumer equipment are 5V, 12V, and 24V DC. Occasionally you'll find 3V or 48V coils. Some older relays use AC coils (marked with "AC" or a tilde); these need AC to operate and won't pull in properly from a DC bench supply.

Contact form describes what the relay switches. SPDT (single-pole double-throw) gives you one common, one normally-open, and one normally-closed terminal, and it's the type you'll see most. DPDT gives you two independent sets of SPDT contacts. Some case markings use form codes: 1C or 1CO means SPDT, 2C or 2CO means DPDT, 1A means SPST normally open only. The contact current rating is usually in amps: 5A, 10A, 15A, 30A for power relays; 0.5A or 1A for signal relays.

Part numbers like SRD-05VDC-SL-C encode some of this: SRD = series, 05 = 5V coil, VDC = DC, SL = low-sensitivity, C = changeover (SPDT). Omron and Panasonic relays tend to have part numbers that include the coil voltage, like G5V-2-H1-12VDC (12V coil, DPDT). If the case marking is too worn to read, the coil resistance test below will help you estimate the coil voltage.

## Find coil and contacts

Desolder the relay for clean testing, or test in-circuit on a powered-down board if you just want to check coil continuity quickly. The relay's footprint on the board usually shows which pins are coil and which are contacts, but you can find them with continuity without needing the datasheet.

**Identifying coil and contact pins**

Set your meter to resistance (ohms) mode. Probe between each pair of pins until you find two that read a consistent resistance of 50–1000Ω. Those are the coil pins. For 5V relays, coil resistance runs 50–150Ω. For 12V, expect 200–400Ω. For 24V, 600–1200Ω. Higher voltage means higher resistance for a similar coil power draw.

**Normally open and normally closed contacts**

With the coil de-energized, use continuity mode to find the common terminal. The common will read continuity to one contact (normally closed, NC) and OL to another (normally open, NO). A 5V SPDT relay typically has the common in the middle, NC on one side, NO on the other, but the coil pins can be anywhere on the package. Board silkscreen often labels "COM", "NC", "NO" which helps.

If you can't get continuity in either direction from any pair of contact pins, check that the coil isn't accidentally energized by something on the board.

## Click test and contact condition

Before energizing, put a flyback diode across the coil pins (anode to the negative coil pin, cathode to the positive coil pin). The inductive kickback when the coil turns off can exceed 300V in worst-case scenarios, which will damage nearby components on the bench without protection. A 1N4148 is fine for signal relays. A 1N4001 or higher for anything with a coil above 100mA.

Apply the rated coil voltage from a bench supply or battery. The relay should click audibly and the armature should pull in within about 10ms — datasheets typically spec a maximum of 7ms, so anything slower suggests a degraded coil or mechanical damage. Immediately after the click, re-check the contact pins: the normally-open pair should now read continuity, and the normally-closed pair should read OL. Remove the supply; you should hear a second click as the spring returns the armature, and the contacts should return to their resting state.

A clean pull-in click is distinct and immediate. A sluggish pull-in or a buzzing sound when energized suggests the armature is stiff or the contact spring is worn. Both are signs of a relay that has worked hard and may not be reliable for long switching cycles.

**Contact resistance check**

In continuity, the closed contacts should read under 0.1Ω. A reading above 0.5Ω on what should be a closed contact suggests oxidation or pitting. You can clean mild oxidation from silver contacts by switching the relay rapidly 20–30 times (cycle the coil on and off quickly) with a small resistive load on the contacts. If the reading drops to under 0.2Ω after that, the contacts are usable. If it stays high, the surface damage is too deep to recover with this method.

> ⚠️ **FACT-CHECK 5** — Verify whether 0.2 Ω is an appropriate "usable" threshold for cleaned contacts; relay datasheets typically specify 100 mΩ (0.1 Ω) max, making 0.2 Ω potentially too permissive for higher-current loads.

## Failure modes

**Open coil**

The coil winding burns through when the relay runs at elevated temperature or is fed the wrong voltage. In resistance mode, an open coil reads OL where you'd expect 50–1500Ω. The plastic case sometimes shows discoloration near the coil, and you may smell the burned enamel. An open-coil relay can't be repaired.

**Welded contacts**

High-current inductive loads (motor starts, solenoid surges) can arc the contacts together. The arc melts and fuses the contact surfaces. In continuity, the supposedly normally-open contacts read closed even with the coil de-energized, and don't open when you energize the coil either. The contacts make a ticking sound when you try to separate them by hand through the case. The relay isn't safe to reuse in any load-switching application because it won't reliably break the circuit.

**Burned and pitted contacts**

Silver contacts pit gradually when they arc repeatedly during switching, especially with inductive loads and no snubber. You won't always see this without opening the case, but you can measure it: contact resistance above 0.5Ω when closed, or intermittent continuity when the relay is tapped lightly with a finger while energized. These relays are not reliable for sustained use but may still work for low-current signal switching.

**Stiff or stuck armature**

The return spring can weaken with age or the armature pivot can corrode in damp environments. The coil energizes (correct resistance on the coil pins, voltage confirmed) but the contacts don't switch, or switch slowly, or only switch when you tap the case. The relay will fail unpredictably under load. It's not reusable.

## Reuse notes

SPDT relays with a readable coil voltage and contact rating are the most useful thing to pull. A 5V 10A SPDT relay is directly usable in Arduino-scale projects for switching mains lighting or 12V loads. A 12V 30A relay is useful for automotive applications. Pull whatever you find and label the bag with coil voltage, contact form, and contact current rating. If the part number is legible, include that too.

Derate the contact current rating to 75% for salvaged relays used with resistive loads, and to 50% for inductive loads. Contacts that have switched motor or solenoid loads have more surface wear than contacts that switched resistive heating elements. You can't tell the history from the outside, so the derating covers the uncertainty.

> ⚠️ **FACT-CHECK 6** — Verify whether 75% derating is conservative enough for salvaged relay contacts with unknown switching history; some sources recommend 50% for all salvaged contacts regardless of load type.

Store relays upright if possible, leads down, so the armature rests in its natural position. A relay stored on its side for years with the spring compressed slightly will have a softer return force when you pull it out. Label the storage bag; a relay with no coil voltage information is almost useless on a future build when you're in a hurry.

Don't reuse a relay that failed to click clearly on the bench test, has welded contacts, or where the coil read OL. Relays with burned plastic cases or a strong acrid smell are also out.

## Theory links

For simple relay test rigs using a resistor as a load and a battery as the coil supply, see [bench experiments](/open-circuits/Exper/EXPER_1.html). For coil resistance measurement and continuity checks across the contact terminals, see [DC measurements](/open-circuits/DC/DC_5.html).

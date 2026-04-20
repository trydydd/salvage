---
title: "BJT Transistors"
section: components
---

Bipolar junction transistors turn up on almost every board in salvage, from the single NPN switch driving a relay to the matched pairs in a linear audio output stage. Most pull cleanly, and a basic multimeter is enough to confirm they're alive and sort NPN from PNP.

## Recognize the package

The TO-92 package is the one you'll see most: a small D-shaped plastic block, flat face on one side, curved on the other, with three leads coming from the bottom in a row. Small-signal transistors like the 2N3904, BC547, S8050, and their PNP counterparts (2N3906, BC557, S8550) all live in this package. The flat face usually carries the part number in tiny text, sometimes faded, sometimes marked with abbreviations.

Medium-power transistors use the TO-220 package: a taller body with a metal tab at the top for heatsinking, three leads in a row. You'll find TIP31, TIP41, TIP120, and similar parts driving motors, larger relay coils, and audio output stages. The TO-126 package is similar but smaller, and appears in older audio equipment. Metal-can transistors in the TO-18 package (small, round, like a tiny silver hat with three leads) are usually RF or low-noise audio types and are rarer in modern salvage.

SMD transistors in SOT-23 packages look like three-legged beetles. They're very common on any board made in the last twenty years, and the marking is usually a two or three character code, not a full part number. A code like "1A" on a SOT-23 is MMBT3904 (NPN); "2A" is MMBT3906 (PNP). These codes vary by manufacturer, so searching "[code] SOT-23 transistor" usually gets you the answer faster than trying to memorize them.

The common confusion in TO-92 is that the pin order is not standardized across families. A 2N3904 read from the flat face (left to right) goes Emitter, Base, Collector. A BC547 in the same orientation goes Collector, Base, Emitter. The part number on the body is the only reliable guide; don't assume the pinout matches a part you've used before.

## NPN versus PNP

NPN transistors conduct from collector to emitter when the base is pulled above the emitter voltage. PNP transistors conduct from emitter to collector when the base is pulled below the emitter voltage. In salvage, the distinction matters immediately for storage: mixing them means test work later.

The naming is a clue for older Japanese parts. The 2SC and 2SD series are NPN. The 2SA and 2SB series are PNP. European parts follow no universal rule, but BC5xx devices split by the final two digits: BC547/548/549 are NPN, BC557/558/559 are PNP. S8050 is NPN, S8550 is PNP.

In diode mode, you can confirm polarity by finding which probe on the base gives you forward junction readings to both other pins. For an NPN, the red probe on the base reads 0.55–0.75V to the emitter and 0.55–0.75V to the collector. Swap the probes and both read OL. For a PNP, the black probe on the base reads 0.55–0.75V to emitter and collector; swap to red and both read OL.

## Diode-mode testing

Desolder the transistor before testing if you want a clean result. Parallel paths through the board can give you false junction readings. For a quick alive-or-dead check on an otherwise healthy board, in-circuit probing will catch shorted transistors, though it won't confirm a subtly leaky one.

**Finding the base**

Pick one lead at random and touch the red probe to it, then touch the black probe to each of the other two leads in turn. If both give you a reading in the range 0.55–0.75V, you've found the base of an NPN transistor. If neither gives you a reading (both read OL), try the black probe on that pin: if both other pins now read 0.55–0.75V, you have the base of a PNP. If you don't get consistent readings on any pin, move to the next lead and try again.

**Confirming the junctions**

Once you have the base confirmed, the emitter-collector pair should read OL in both directions in diode mode. If you get a reading in either direction between emitter and collector, the transistor is damaged.

**Emitter vs. collector**

With a TO-92 part in hand, check the datasheet for the pinout. If you don't have access, the base-emitter junction typically reads a slightly lower forward voltage than the base-collector junction (0.60–0.65V vs 0.65–0.70V for many small-signal parts), but this difference is small enough to be unreliable with a budget meter. When in doubt, look up the part number.

**Component tester**

A cheap transistor tester (around £10–20) displays NPN or PNP, labels each pin, and gives you the HFE (gain). This is the fastest way to sort a bag of unknown parts and is well worth the outlay if you're doing this regularly.

## Failure modes

**Shorted collector-emitter**

The most common failure in power transistors. Overvoltage or overcurrent fuses the silicon and leaves C-E looking like a short. In diode mode, you'll get a near-zero reading between collector and emitter in both directions. The body is often intact; you can't see the damage. Any TO-220 pulled from near a burned section of board should be tested for C-E continuity before being trusted.

**Open junction**

Overcurrent can burn the bond wire inside the transistor before shorting the junction. An open-junction transistor reads OL on all three leads in every direction. This sometimes happens to small-signal transistors in ESD-sensitive positions on boards that were handled without care.

**Leaky junction**

A degraded transistor passes some current even when it should be off. In diode mode you might see a low reading (0.2–0.4V) where you expect OL, or a normal forward voltage that drops under the meter's test current. Without an HFE tester, this failure can hide. If a transistor in a linear circuit is creating offset or distortion that you can't account for elsewhere, test the transistors out of circuit.

**Thermal stress in TO-92**

TO-92 transistors don't heatsink well, and in circuits where they ran near their limits you'll sometimes find the plastic body slightly browned or the leads discolored close to the package. These parts may still pass a junction test but have uncertain long-term reliability. They're fine for experiments; don't use them in anything you need to trust.

## Pin identification

When the part number is readable, find the datasheet: search the number plus "datasheet" and look for the pin diagram. For TO-92 parts, the standard diagram shows the flat face with three pins labeled from left to right. For TO-220, the tab is usually at the top and the collector is often connected to the tab, which makes the tab helpful for identification.

If the part number is gone and you can't find a match for the abbreviated SOT-23 code, use the base identification technique above to find the base, then check whether it's NPN or PNP. You can store it labeled "NPN small signal, base = middle pin" and test for the actual pinout when you need it.

The one test that catches most failures without knowing the pinout at all: in resistance mode, check all three pin combinations in both directions (six checks total). A healthy transistor shows no near-zero readings except the two expected junction directions through the base. Any low-resistance path that shouldn't exist points to a damaged device.

## Theory links

For transistor action and how the base current controls collector current, see [Semiconductors](/open-circuits/Semi/SEMI_6.html). For simple transistor test fixtures you can build at the bench to confirm HFE and switching behavior, see [bench experiments](/open-circuits/Exper/EXPER_1.html).

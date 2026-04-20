---
title: "Connectors and Switches"
section: components
---

Connectors and switches are the parts that most people skip in salvage, and that's a mistake. A matched pair of JST-PH connectors, a barrel jack, a handful of tact switches, or a good rocker switch can be the part that makes a project buildable rather than a parts-ordering delay.

## Why these are always worth pulling

Unlike active components, connectors and switches don't degrade in ways that are invisible. You can test them completely with a continuity check and a visual inspection. A 2.54mm pin header is a 2.54mm pin header regardless of where it came from, and the only thing that limits its usefulness is physical condition.

Matched connector pairs are more valuable than singles. When a device has a wiring loom with a JST-XH or Molex connector on each end, pulling the pair plus the wiring gives you something immediately reusable: a ready-made cable with known terminations. A bare connector body without its mating half is still useful but requires more effort to deploy.

## Identify the family

**Headers and housings**

2.54mm (0.1") pitch pin headers are the foundation of most hobby electronics wiring. They look like rows of square gold or silver pins on a black plastic strip. Male headers solder to boards; female housings accept the pins. You'll find both in every size from 2-pin to 40-pin. The pitch (pin-to-pin distance) matters: 2.0mm pitch connectors from phone and camera boards look almost identical but won't mate with 2.54mm parts.

JST connectors are the small latching housings with molded plastic bodies. The JST-PH series uses 2.0mm pitch and is common in small lithium battery packs and compact PCB assemblies. JST-XH uses 2.5mm pitch and appears in RC equipment, 3D printer beds and extruders, and small consumer electronics. JST-SM uses the same 2.5mm pitch with a slightly different latch. The color and shape of the housing is not a reliable guide to family; measure or compare against a known part.

**Barrel jacks and DC power connectors**

Barrel jacks mount on boards and panels for DC power input. The most common sizes are 5.5mm outer diameter with either 2.1mm or 2.5mm inner pin. The difference matters: a 2.1mm plug in a 2.5mm jack makes intermittent contact; a 2.5mm plug won't seat in a 2.1mm jack. The center pin is nearly always positive, but confirm the polarity mark on the board or device before assuming. Smaller 3.5mm barrel jacks appear on some laptops and portable devices.

**Switches**

Tact switches are the 6mm×6mm or 12mm×12mm square pushbuttons with four legs. They're momentary, normally open, and the legs come in pairs: each pair is internally connected, so the two legs on one side connect to the button on one side, and the two legs on the other side connect to the other side of the button. Rocker switches are the large rectangular toggles used for mains or 12V power. They're usually SPST or DPDT, rated for 10–16A. Slide switches are smaller, with a physical sliding actuator, rated for 0.5–5A typically. DIP switches are multi-position rocker arrays on a narrow DIP-style body, used for configuration jumpers.

## Test and inspect

**Continuity check on switches**

Set the meter to continuity mode. For a tact switch, probe one leg from each side (diagonally opposite legs work fine). Press the button: you should get continuity only when pressed, and OL when released. If continuity is present unpressed, the switch is stuck or failed closed. If pressing the button gives no continuity, the contacts are oxidized or the mechanism is broken.

For a rocker switch, probe across the switched terminals in both positions. The switch should read continuity (under 0.5Ω) in the ON position and OL in the OFF position. Rocker switches with a lamp sometimes have separate terminals for the lamp; probe each set independently.

**Continuity check on connectors**

Probe each pin against its expected mate. For a wire harness, probe the pin on the board connector against the matching pin on the wire-end connector. Any pin that reads OL on a circuit that should be continuous has a broken crimp, a bent pin, or a cracked housing. Wiggle the connector gently while probing: intermittent connections that come and go during movement indicate a failing crimp or a damaged contact spring.

For bare connector bodies without wiring, check that all pins are seated fully (no pushed-back pins), that no pins are bent or missing, and that the latch mechanism snaps and releases cleanly.

**Grip test for latching connectors**

Mate the connector pair and pull with a steady force. The latch should hold without the housing separating. A connector that pulls apart without releasing the latch has a broken or fatigued latch clip. It'll work for a bench connection but won't stay put in a moving device. Label it "no latch" rather than discarding it outright, since a glue-assisted static mount may still be fine.

## Failure modes

**Oxidized contacts**

Silver and tin contacts oxidize over time, especially in humid environments. The contact surface goes dull gray-brown rather than bright. Continuity tests may still pass because the probe pressure breaks through the oxide, but the connection resistance under real current can be much higher. Burnishing the contact surface with a pencil eraser removes light oxidation. Deep oxidation that pits the contact surface won't clean up reliably, and the connector should be discarded for any current-carrying use.

**Bent or pushed-back pins**

Connector pins get bent from improper mating or physical damage. A bent male pin can be straightened carefully with fine-nose pliers or a dental pick, but the metal is work-hardened and may snap at the bend if you straighten it more than once. Pushed-back pins (where the pin has slid back into the housing) are often recoverable: a pointed tool inserted alongside the pin can re-engage the retention barb. Test continuity after straightening any pin.

**Cracked or split housing**

Plastic connector housings crack from overtorqued screws, dropped parts, or excessive force during mating. A cracked housing can still work electrically, but the pins may not be held at the correct spacing, and the crack will propagate under vibration. For static applications, a cracked housing with intact contacts is usually fine. For anything that moves, it's not.

**Worn tact switch contacts**

Tact switches rated for 50,000–100,000 cycles wear out through use. The failure mode is usually increased contact resistance rather than a hard open: the switch reads continuity when pressed firmly but not when pressed lightly, or the click feel changes from crisp to mushy. On a bench test you'll catch a dead switch but may not catch a borderline one. Tact switches from heavily used controls (volume buttons, power buttons on devices that were on for years) are worth checking more carefully than ones from configuration panels.

## Harvesting strategy

When a connector has a wiring harness attached, cutting the wires close to the board preserves more value than desoldering. You lose the board real estate, but you keep the crimp connections and wire lengths, which take time to re-create. Leave 100–150mm of wire if the loom allows it. If the connector is board-mounted with no loom, desolder it with the board face-up on a heat mat or with a hot-air station so you can see the pins; drag soldering these pins out one at a time risks pulling the housing out of square.

Panel-mounted connectors (barrel jacks, rocker switches, toggle switches) are often attached to the case with a hex nut. Unscrew the nut before cutting any wires, and the connector and its panel cutout comes out as a single piece. That's more useful than a bare connector, because you can mount it in a new panel using the same thread.

JST housings have a latch that engages a tab on the mating connector. When mating connectors are stuck, use a fine plastic tool or a toothpick to depress the latch before pulling; pulling without releasing the latch cracks the housing or bends the retention tab. The housings are thin and the latch is a single small feature; force always breaks something.

Store connectors by family and pitch in small bags or compartments. Label with the connector type (JST-PH 2-pin, XH 4-pin, 2.54mm header 8-pin) because the families are harder to distinguish by eye when you're in a hurry. Rocker and toggle switches should be labeled with their switching configuration (SPST, DPDT) and current rating if it's printed on the case.

## Theory links

For continuity work and understanding how contact resistance affects circuit behavior, see [DC measurements](/open-circuits/DC/DC_5.html). For quick switch and connector test setups that confirm behavior under real load, see [bench experiments](/open-circuits/Exper/EXP_1.html).

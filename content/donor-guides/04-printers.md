---
title: "Printers"
section: donor-guides
hazard: 2
hazard_summary: "Low-voltage logic; laser printer fuser runs at mains voltage (upgrade to 3 for laser)."
author: Claude
review: Needs Human Review
---

Printers are unusually good mechanical donors. The carriage rails from an inkjet, three or four stepper motors, and a spread of optointerrupters represent more raw motion-project hardware than most other donor classes combined. The electronics are modest. The disassembly is mostly screws.

## What's Inside

Two broad families worth treating differently. Inkjet printers run entirely on low-voltage DC from an internal or external switch-mode supply. The main board handles USB or network and drives the motors. The carriage assembly rides one or two precision steel rods, pulled by a timing belt from a DC motor, and carries the printhead or the cartridge holder. A separate stepper motor drives the rubber rollers that pull paper through. Optointerrupters at four or five points around the mechanism track carriage home position, paper presence, and feed roller position.

Laser printers have all of that plus a fuser assembly and a high-voltage board. The fuser presses two rollers together and heats them with a halogen lamp or a ceramic element at mains voltage, reaching 150–220 °C during use. The high-voltage board generates the bias rails for the corona wires and developer roller, which are several hundred volts but very low current and discharge quickly once the machine is off. The rest of the laser internals (DC supply, formatter board, motor driver, polygon mirror scanner) fill out the back half of the case.

The hazard rating here covers inkjets. Treat a laser printer as hazard 3 for the fuser specifically: unplug it, let it cool, and don't touch the fuser rollers until they're cold.

The carriage rod is consistently the highest-value single part in most inkjet teardowns. A straight, hardened steel shaft at 6–8 mm diameter is useful in far more projects than anything on the logic board.

## Before You Open It

1. Unplug from mains. Inkjets often have an external brick. Lasers always have an internal mains supply.
2. Remove ink cartridges or the toner cartridge before opening the top panel. Loose toner and wet ink both make a mess if they get into the mechanism.
3. If it's a laser printer, wait at least 10 minutes after unplugging before handling the fuser. The rollers stay very hot after power-off.
4. On a laser, leave the high-voltage board alone unless you know you want something on it. The bias outputs aren't lethal, but they'll give you a sharp jolt if you put a finger across them before they've bled down.

For an inkjet, once cartridges are out and the power is disconnected, there's nothing inside that poses more than a mechanical hazard.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Stepper motors | Paper feed and carriage assemblies | Coil count, connector style, shaft length | ★★★ |
| Optointerrupters | Paper path and lid sensors | Slot width, package style, emitter-detector pairing | ★★★ |
| DC carriage motor | Inkjet carriage drive, attached to belt pulley | 24 V DC; encoder strip alongside; 2-pin motor lead plus 2-pin encoder; confirm free rotation | ★★★ |
| Carriage steel rod | Inkjet carriage, spanning full print width | 6–8 mm diameter; 200–300 mm length; hardened steel; check for rust or scoring along bearing surface | ★★★ |
| Belts, gears, and rails | Carriage and feed mechanisms | Pitch, length, bearing surfaces, straightness | ★★☆ |
| Power connectors | PSU and board harnesses | Locking style, pin count, wire gauge | ★★☆ |
| Small fans | Laser printer power or fuser area | Voltage marking, size, bearing noise | ★☆☆ |

## How to Get Them Out

Most of the yield here comes out with a screwdriver. Printers are designed for field service, so mechanical assemblies separate at screws and snap clips rather than adhesive or heat stakes. Pull the paper tray out first, because it often hides a screw or a clip that keeps the bottom shell from releasing. On Canon and Epson inkjets there are usually one or two screws under stickers on the underside of the case, so run your thumb over every sticker before you start levering seams.

Once the shells come off, the carriage assembly is accessible without further disassembly. The steel rod is held at each end by a bracket retained by a single screw or a spring clip. Slide the carriage to the center of the rod before you release the end clips, so it doesn't drop when the rod comes free. The rod slides straight out once both ends are loose. On dual-rod units, the second shaft is usually thinner and unpolished: it guides without bearing load, so it's less useful but still fine for lighter jobs.

The timing belt hooks onto a bracket on the carriage. If you want the belt intact, unhook it from the carriage before pulling the rod. If you don't need the belt, cut it.

The paper-feed stepper unbolts from the main frame with two or three screws and has a JST ZH or similar connector going to the main board. Unplug the connector and unbolt the motor. Keep as much lead length as possible. A motor with 100 mm of lead and an intact connector is much easier to reuse than one with 20 mm of stub.

Optointerrupters are through-hole on most units, soldered to the main board or to a small carrier board near each sensor position. Heat from beneath, wick or pump, and rock the body gently until each leg comes free. Don't lever against the body while any pin is still soldered, or the housing cracks. If the optointerrupter spans a slot with the emitter and detector on opposite sides, keep them as a matched pair rather than pulling one and leaving the other.

The laser scanner assembly (polygon mirror, BLDC motor, and laser diode module) is four screws and one ribbon cable. The BLDC motor is occasionally worth extracting if you have a specific use for it, but the polygon mirror itself won't survive being spun outside the original housing. Only pull the scanner assembly if you need the motor.

Hot air adds almost nothing here. There's very little surface-mount work worth doing on a printer board.

## Watch Out For

- Laser fuser assemblies get very hot in use and stay that way for 10–15 minutes after unplugging. Let it cool before touching it. If you're pulling the fuser for its rollers or lamp, keep the thermistors and their wiring with it so the assembly stays identifiable.
- Toner dust is extremely fine and disperses easily. Don't blow it with compressed air and don't vacuum it with a standard household vacuum. Wipe up spills with a damp cloth rather than a dry one, which just moves the dust around.
- The inkjet waste ink pad sits in the bottom of the case, saturated with old ink. It can drip. Keep the bottom shell face-up when you lift it away, and set it somewhere it won't stain anything before dealing with the pad.
- The ribbon cables connecting the printhead carriage to the main board have ZIF connectors with small hinged latches. Flip the latch up before pulling the cable. Forcing the cable without opening the latch tears both the cable and the connector housing, and a damaged ZIF socket on the main board isn't repairable.
- Paper-path springs are under tension throughout the mechanism and will fly when an assembly is disassembled past its normal travel. Work slowly once the frame is exposed and check where each spring is anchored before you remove the part it's pressing against.

## Theory Links

- [DC measurements](/open-circuits/DC/DC_5.html) for testing motors, switches, and sensor harnesses after removal.
- [Experiments](/open-circuits/Exper/EXP_2.html) for simple bench setups that help sort motors and optical sensors into known-good bins.

## Specific Teardowns

Specific make-and-model teardowns for printers will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

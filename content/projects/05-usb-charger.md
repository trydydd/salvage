---
title: "USB Charger"
section: projects
author: Claude
review: Needs Human Review
---

This project takes a salvaged regulated 5 V wall-wart and wires a USB-A socket to its output, giving you a basic 5 V USB charging port. It's a wiring exercise. The donor supply stays sealed and unmodified. The mains circuitry inside is not touched.

There's a hard prerequisite: the supply must be regulated and must measure 5.0 V DC on its output. An unregulated "5 V" supply has an output that varies with load and can swing well above 5 V on no load, which will damage whatever you plug in. Confirm the output before building anything. Every step below assumes you've already done that check.

You'll need a regulated 5 V DC wall-wart from any dead phone charger or small appliance adapter, a USB-A socket from a dead router or hub, and a short length of hookup wire. Nothing else.

## Project scope

The finished charger provides 5 V at the USB socket's VBUS pin at up to the supply's rated current. A 5 V 1 A wall-wart makes a 1 A charger. Don't connect anything that tries to draw more than the supply's label rating, because the output will sag, the supply will run hot, or it will shut down.

What it won't charge: modern iPhones and iPads (require specific D+/D- voltages for Apple charging protocol), any USB-C device that needs Power Delivery negotiation, anything that needs more than the supply can deliver. What it will charge: most Android phones from 2011 onward that recognize a Dedicated Charging Port, MP3 players, small accessories, and anything else that's happy with basic 5 V.

The D+ and D- pins in the USB socket (pins 2 and 3) carry no power. Bridging them together signals to USB Battery Charging-compliant devices that the port is a Dedicated Charging Port, which allows those devices to draw their full rated charge current. Without that bridge, many devices will show "not charging" or will trickle-charge at 100 mA. The bridge is two pins close together and takes thirty seconds to add.

## Parts to salvage

| Part | Where to get it |
|------|-----------------|
| Regulated 5 V DC wall-wart, 500 mA to 2 A rated output | Wall chargers, any phone or device adapter labeled "5 V DC"; confirm with meter |
| USB-A socket, panel-mount with short leads or through-hole | Routers and modems, rear panel USB port; any dead USB hub; Laptops, USB daughterboard |
| Short hookup wire, 22–24 AWG, two colours if possible | Any low-voltage PCB |

This is a short parts list because the project is simple. Buy nothing.

One note on the USB socket: a panel-mount socket with a short cable tail (the kind bolted to the rear of a router) is much easier to work with than a through-hole socket desoldered from a hub PCB. If you're pulling a through-hole socket, you can skip desoldering and just cut the PCB traces close to the socket body, leaving enough copper to solder to directly. That works just as well.

## Circuit outline

Look at the USB-A socket from the front. Left to right, the four pins are: pin 1 (VBUS, +5 V), pin 2 (D−), pin 3 (D+), pin 4 (GND). The power pins are the two outer ones.

Before cutting anything, confirm the supply's output polarity. Barrel-jack wall-warts are almost always center-positive, but not universally. Measure with a multimeter: red probe to the center pin of the barrel connector, black to the outer ring. A positive reading means center-positive. Reversing polarity at the USB socket puts −5 V on VBUS and will immediately damage any device you plug in.

1. Plug the supply into mains and confirm the output: measure the cable leads or the barrel connector with your multimeter on DC volts. You need 4.75–5.25 V. If you see outside that range, or a fluctuating reading, find a different supply.
2. Unplug from mains.
3. Cut the supply cable about 100 mm from the end, or remove the barrel connector if you'd rather wire directly. Strip 10 mm from each conductor.
4. Solder the positive supply lead to USB pin 1 (VBUS) and the negative lead to USB pin 4 (GND).
5. Bridge pin 2 to pin 3 with a short piece of wire or a small solder bridge. These are the two narrow center pins. If you're working with a through-hole socket on a PCB, bridge the pin 2 and pin 3 pads on the underside.
6. Cover all connections with heat-shrink.

That's the whole build. For a more permanent version, mount the USB socket through a hole in a small plastic project box, bring the supply cable through a rear hole with a strain-relief knot inside, and solder inside the box. The knot in the cable is the only strain relief you need. Without it, tugging on the cable will eventually crack a solder joint at the socket.

A common mistake: checking the supply voltage before and forgetting to unplug before soldering. The supply doesn't need to be plugged in during the wiring steps. Do all soldering cold, then plug in to test.

## Test and troubleshoot

Before plugging into mains, inspect all connections. Confirm no bare wire is touching an adjacent pin on the USB socket.

1. Plug in. Measure across USB pins 1 and 4 with your multimeter on DC volts (red probe to pin 1). You should read 4.75–5.25 V.
2. If you read 0 V: either the supply isn't starting, or there's an open connection between the supply lead and pin 1 or pin 4. Unplug and check continuity from the supply positive wire to pin 1, and negative to pin 4.
3. If you read negative voltage (between −4.75 and −5.25 V): polarity is reversed. Unplug, swap the supply leads at the USB socket.
4. Connect a USB cable and a device that you know charges from a basic charger. It should show charging on screen within a few seconds.
5. After five minutes, feel the supply body. Warm is normal for any linear-regulator supply. Switch-mode supplies run cooler. Uncomfortably hot means the device is drawing more current than the supply is rated for. Either use a higher-rated supply or accept that this supply can only charge lighter loads.

Voltage should stay above 4.75 V under load. If it sags below that, the supply's output stage is weak or the device is drawing too much for its rating.

## Theory links and safety notes

For measuring the output voltage and confirming polarity before connecting anything, see [DC measurements](/open-circuits/DC/DC_5.html).

For how the regulator inside the donor supply keeps its output stable under load, see [semiconductors](/open-circuits/Semi/SEMI_6.html).

Add a 47–100 µF electrolytic capacitor (10 V or higher rating) from VBUS to GND at the socket to reduce output ripple from the donor supply. A good candidate is a filter cap pulled from the secondary side of a dead wall charger. If you want to charge Apple devices at full speed, look up the resistor-divider values for Apple's charging protocol (2.0 V on D+ and D−) and add two resistor pairs between VBUS, GND, and the D pins. If you have access to a supply with a higher voltage output (9–12 V), pair it with a 7805 linear regulator from any donor PSU board to generate a regulated 5 V at up to 1 A, which is the transformer-to-regulator chain the stub originally described.

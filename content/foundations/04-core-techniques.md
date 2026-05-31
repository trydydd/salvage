---
title: "Core Techniques"
section: foundations
---
This page collects the hands-on techniques used throughout the guide, from getting parts off a board without wrecking them to deciding which components are worth keeping.

## Desoldering through-hole parts

Through-hole desoldering is the core skill for component salvage, and it comes down to getting a joint fully molten and removing the solder before it sets again. The two common methods are braid and a pump, and most people end up using both.

With desoldering braid, lay the braid over the joint, press it down with the iron tip, and wait for the solder to wick up into the copper. Once it does, lift braid and iron together. Braid suits flat pads, surface-mount joints, and cleanup, and it's gentle enough that it rarely damages anything. Add a little fresh flux to the braid if it isn't drinking the solder.

With a solder pump, heat the joint until the solder flows, pull the iron away, and in the same second put the pump's nozzle over the molten blob and fire it. Speed matters, since the solder sets in well under a second. A pump clears the bulk fast, which is what you want on a part with several pins, and braid finishes the holes.

A few things make the difference between clean pulls and torn pads:

1. Add fresh solder to an old joint before removing it. Mixing new leaded solder into an old joint lowers its melting point and helps it flow, even when you're about to take it all out again.
2. Give big pins and ground planes more heat, or a hotter tip, not more time. A copper plane pulls heat away as fast as the iron puts it in, and sitting on a stubborn joint at too low a temperature cooks the board.
3. Work one lead at a time on multi-pin parts, freeing each before moving on. On a two- or three-pin part you can heat and rock the part out lead by lead.
4. Stop and reflux when a joint goes dull and grainy. That look means the flux has burned off and you're heating dead solder.

Know when to give up on a joint. If a pad is lifting, the part is cheap, or you've reheated the same hole four times, cut the leads flush and pull them out individually instead. A salvaged part is rarely worth a destroyed donor board, and sometimes the donor board is worth more than the part.

Low-melt alloy is the cheat code for the hard jobs. Adding a low-temperature desoldering alloy (the Chip Quik type) to a joint drops its melting point far enough that a whole multi-pin part stays molten at once and lifts free. It's the easy way through a part that braid and a pump can't beat, at the cost of a bit of alloy and a thorough clean afterward.

## SMD removal

Surface-mount parts don't have leads through the board, so you melt all their joints at once and lift them off. Hot air is the usual way, with a couple of alternatives for when you don't have it.

With hot air, set the station around 320-350 °C with a medium airflow, add flux to the joints, and play the nozzle evenly over the part until the solder goes shiny and liquid. Pick the part straight up with tweezers rather than dragging it, or you'll smear solder across neighbouring pads. Keep the nozzle moving so you heat the joints and not a hole in the board, and shield tall plastic parts nearby with foil or kapton tape if they're at risk.

Without hot air, small two-terminal parts (resistors, ceramic caps, small diodes) come off with a single iron by heating one end, then the other, walking the part loose in a second or two. A blob of solder bridging both ends lets you heat both at once. For anything with more pins than that, low-melt alloy flooded across all the leads keeps them molten together long enough to slide the part off.

The real risk with SMD is lifting pads and tearing fine-pitch leads. Too much heat for too long, or any sideways force while the solder is only half-melted, peels the copper off the board. That mostly costs you the donor footprint, which you don't care about, but it can also wreck the part's own leads. Aim for a full melt and a clean vertical lift every time.

Be honest about what's worth recovering. Passives in 0805 and bigger pull easily but are nearly free new, so it's practice more than profit. ICs are worth it only if you can identify them and have a use, since a mystery SMD chip you can't test or look up is just a tidy piece of e-scrap. The SMD parts that genuinely pay off are the marked, identifiable ones: regulators, MOSFETs, connectors, crystals, and the occasional sensor.

## Cleaning salvaged parts

A freshly pulled part carries old solder, burnt flux, and whatever dust and grime the donor collected over its life. Clean it before you inspect it, measure it, or bag it, so you're not judging a part through a layer of crud or carrying contamination into your next project.

Start with the leads. A blob of old solder left on a through-hole lead stops the part sitting flat in a new board or a breadboard. Reheat it and wick it off with braid, or drag the molten blob off against a damp sponge or brass wool. The lead should come away tinned and straight, not lumpy.

Then the body and the flux. Isopropyl alcohol (90% or higher is ideal) on an old toothbrush or a cotton swab lifts sticky brown flux and most grime. Scrub, wipe, and let the part dry fully before you power it or store it. Compressed air or a soft brush clears dust out of connectors, fan housings, and switch bodies where alcohol can't reach.

Clean parts are readable parts. Once the flux and grime are gone, the markings, the cracks, and any corrosion show clearly, which is exactly what the inspection step depends on. Don't bag a part still coated in flux. The residue attracts dust and can creep across pins over time.

## Inspection and triage

With a part cleaned, decide which pile it goes in: tested-good, scrap, or uncertain-and-labeled. Most of that call you can make by eye before a meter ever touches it.

Look for heat damage first. Brown scorching, a melted or discoloured body, the smell of burnt plastic, or charring on the board where the part sat, all mean stress. The part is suspect, and so is whatever was driving it. Set heat-damaged parts aside as scrap unless they're valuable enough to be worth testing carefully.

Then the physical faults:

1. Bulged or vented electrolytic caps, domed tops or crusty residue at the base, have failed. Bin them, and treat their neighbours as stressed.
2. Cracked or chipped bodies, common on ceramic caps and on parts near board flex points or mounting screws, usually mean scrap.
3. Bent or half-broken leads can often be straightened, but a lead that's been flexed repeatedly will snap at the body. Check where it enters the package before you count on it.
4. Green or white corrosion, from leaked electrolyte or moisture, creeps along leads and traces. Clean it off and check whether the metal underneath survived.

What you can't settle by eye goes in the uncertain pile, labeled as such, for a meter check later. A part that looks fine isn't proven good, and a part with worn markings isn't proven anything. The components pages cover the specific tests for each family. The job here is to keep the obviously-dead parts out of your stock and to flag the maybes so you test them before you trust them, not after a build fails.

## Documenting what you pulled

The information about a part is worth as much as the part. A tested 12 V relay with a known coil resistance is inventory you'll actually use. The same relay loose in a tin, markings unread, is something you'll test again from scratch or skip. A light documentation habit keeps the knowledge attached to the part.

Keep it as simple as it can be while still working. For most people that's writing the essentials straight onto the storage bag in marker: what it is, the spec you'll search on, where it came from if that matters, and whether you've tested it. "Nichicon 1000µF 16V, ATX secondary, tested ESR ok" on the bag beats any filing system you won't keep up.

Capture the details at the moment they're visible, not later. The part number is readable in place and gone once the top's scuffed. A connector's wiring is obvious while it's still plugged in. A couple of phone photos during teardown, the board before you strip it and a connector before you unplug it, cost nothing and answer the questions you'll have weeks on.

If you do more volume, a single running notes file or spreadsheet, one line per useful pull, is plenty: date, donor, part, spec, tested. The aim isn't a database. It's that when a build calls for a part, you can find it and trust it instead of starting the identification over every time.

## Wall wart identification and testing

A wall wart is a good first thing to read, because everything you need is on the label or in your hand. The aim is to know its output, its connector, and whether to trust it, in about five minutes and without opening it.

Start with the label. The output line gives you a figure like "12V 1A" or "5V 2A," and tells you whether it's DC or AC out: a solid line over a dashed line (or "DC") for DC, a wavy line (or "AC") for AC. An AC-output wart feeds a rectifier inside the original device, so don't expect clean DC from it. The label may say whether it's regulated. Treat anything that doesn't say so as unregulated until the meter proves otherwise. Watch one trap here: a rating given in VA is not the same as watts. The VA number can read bigger than the real usable power, so size a load by the voltage and current figures, not by a headline VA rating.

Identify the connector before you count on it. Barrel jacks are sized by outer and inner diameter, commonly 5.5 mm OD with either a 2.1 mm or a 2.5 mm pin, and the two aren't interchangeable. USB outputs (A, micro, or C) are their own standard and usually mean a regulated 5 V. Anything moulded and odd-looking is probably proprietary, worth keeping only if you have the matching socket or you're willing to cut the plug off for the cable. Note the polarity symbol next to the connector, the little diagram showing whether the centre pin is positive or negative. Centre-positive is common but far from universal, and getting it wrong kills things.

Weight and feel tell you the technology, which tells you how the meter will behave. Heft an old adapter against a modern one of the same rating. The heavy one, often warm even at idle, has a mains-frequency transformer and is usually unregulated. The light one is a switching supply and is usually regulated. This matters because an unloaded unregulated wart reads well above its rated voltage, a "9V" unit showing 12-14 V open-circuit, and only settles to spec under load. A regulated switcher reads close to its label with nothing connected.

Then verify, rather than trusting the label:

1. Plug it in and set a multimeter to DC volts, or AC volts if the label said AC.
2. Probe the output connector, red to the positive terminal per the polarity symbol, black to the other. A reading near the rated voltage, or above it for an unloaded unregulated type, means it's alive.
3. Watch the polarity. If the meter reads negative, your probes or your assumptions about the connector are reversed. Sort that out now, on the meter, not later on a powered circuit.
4. If you'll rely on it, load it. A power resistor or a 12 V bulb across the output, meter still connected, shows whether the voltage holds or sags. An unregulated wart drops toward its rating under load, while a healthy regulated one barely moves.

A wall wart that holds its voltage under load, with known polarity and a connector you can use, is one of the most reusable things you'll salvage: free regulated power for benches, projects, and repairs. One that reads wildly off, collapses under load, or buzzes and gets hot is scrap. For the theory behind what you're measuring, see [DC measurements](/open-circuits/DC/DC_5.html).

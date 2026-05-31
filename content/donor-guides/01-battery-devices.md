---
title: "Battery Devices"
section: donor-guides
hazard: 1
hazard_summary: "Low voltage, no stored energy concerns."
author: Claude
review: Needs Human Review
---

Small battery-powered gadgets are the easiest donors to start on: toys, remotes, battery lights, handheld tools, and similar low-voltage devices with simple boards and modest parts yields. There's no stored energy to worry about and nothing inside runs above a few volts, so you can open one with a screwdriver and learn the basics without any of the hazards that come with mains gear.

## What's Inside

Open the battery hatch, pull the cells, and a couple of screws or snap clips get you the rest of the way into most of these. Inside you'll usually find a small single-sided PCB, a battery holder or sprung contacts wired to it, a switch, and whatever the device actually does: an LED or two, a small bulb, a buzzer, or a tiny motor.

The board itself is rarely the prize. It's often a blob-top IC (a black epoxy dot hiding an unmarked chip) with a handful of discrete parts around it, none of it worth desoldering. The value is in the bits hanging off the board: the holder, the switch, the connectors, and the output device. Wiring is thin but usually flexible and pre-tinned, handy for low-current jobs.

These devices are beginner-friendly precisely because there's so little that can go wrong. Nothing holds charge, nothing's hot, and the parts come off with a basic iron or no iron at all.

## Before You Open It

Take the batteries out first, every time. That's the whole safety procedure for this class of donor, and it also stops a half-dead cell from feeding the board while you poke at it.

Look at the battery compartment before you go further. White or crusty residue around the contacts is leaked alkaline electrolyte, which is mildly caustic and corrodes everything it touches. Wipe it out with a little vinegar on a swab, which neutralises the alkaline crust, and wash your hands after. If you find a swollen lithium pouch in something you assumed was disposable, treat it as covered on the safety page: don't puncture it, and recycle it rather than binning it.

Find the seams and clips before you pry. Many of these cases are held by hidden snap tabs as much as screws, and the thin plastic cracks if you lever from the wrong side. Run a fingernail or a plastic spudger around the seam to find where it gives before you force it.

## What to Target

The table below is the quick scan for parts worth noticing when one of these lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Battery holders | Rear shell or battery tray | AA/AAA/coin-cell formats, spring condition, wire tabs | ★★★ |
| Switches | Board edge or top shell | Slide, tact, or rocker style with clear contact action | ★★★ |
| LEDs | Front panel or light pipe | Color, package size, polarity, diffuser style | ★★☆ |
| Small DC motors | Gearbox or vibration assembly | Approximate voltage from cell count, shaft style | ★★☆ |
| Speakers or buzzers | Front shell cavity | Impedance markings, diameter, lead length | ★☆☆ |

## How to Get Them Out

Most of the value here comes off with cutters, not an iron. Cut wires at the board and keep the connector or the component on the other end, rather than unsoldering both. For a battery holder, snip the two wires where they meet the PCB and you've got the holder with leads ready to reuse.

Spring battery contacts are staked or spot-welded into the plastic. Free them by easing the retaining tab back and sliding the contact out of its slot rather than pulling on it, which deforms the spring. If they're soldered to the board through tabs instead, heat the tab and lift it clear in one go.

For the small parts, a basic iron is plenty. LEDs and tact switches are cheap, so they're more practice than profit, but they come out easily: heat one lead while rocking the part, then the other. Don't linger on an LED. The plastic lens and the chip inside don't love heat, and a few seconds too long dulls or kills them. Small DC motors and speakers usually have two solder pads or short flying leads, so cut the leads long and keep them on the part.

## Watch Out For

- Leaked alkaline residue is corrosive and creeps into the contacts and the nearest board traces. Clean it off before you judge whether the holder and switch are worth keeping.
- Battery tabs and spot-welded straps have sharp stamped edges. They'll nick a finger if you run a hand through the compartment without looking.
- Springs and small mechanisms sit under light tension and ping loose when you remove the part holding them. Catch them, or they vanish into the carpet.
- Some disposable-looking gadgets hide a small rechargeable cell, a LiPo pouch or a soldered-in coin cell. Check before you assume there's nothing inside to remove with care.

## Theory Links

- [DC measurements](/open-circuits/DC/DC_5.html) for checking battery polarity, voltage, and switch continuity.
- [Experiments](/open-circuits/Exper/EXP_2.html) for simple LED and battery test setups you can reuse while sorting parts.

## Specific Teardowns

Specific make-and-model teardowns for battery devices will be linked here as they're added. See `content/donor-guides/teardowns/` for in-progress guides.

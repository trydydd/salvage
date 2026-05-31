---
title: "Wall Chargers"
section: donor-guides
hazard: 2
hazard_summary: "Internal caps may hold charge; unplug and wait."
author: Claude
review: Needs Human Review
---

Phone chargers and plug-in adapters pile up faster than any other donor on the bench. Most are worth a few minutes for the cable, the socket, and one or two small parts, as long as the case opens without a fight. The first question is always whether you can get inside without wrecking everything you came for, because a lot of modern chargers are sealed shut by design.

## What's Inside

There are two families here, and you can tell them apart by weight before you open anything. The old transformer bricks are heavy and run warm. Inside you'll find a laminated-iron transformer taking up most of the volume, a bridge rectifier or four discrete diodes, a fat filter cap, and on the regulated ones a linear regulator bolted to a small tab of metal. Low parts density, low frequency, usually held together with screws or simple snaps.

The light ones are switch-mode supplies, and they're where most chargers made in the last fifteen years land. The board is packed edge to edge. On the primary side, at mains voltage, you've got an input fuse or a fusible resistor, a small bridge or four diodes, a bulk electrolytic cap rated around 400 V, a switching controller and MOSFET (often combined into one chip on cheap units), and a small high-frequency ferrite transformer. That transformer splits the board into a primary half and a secondary half, with an optocoupler bridging the isolation gap to carry feedback across.

Past the transformer, the secondary side drops to safe voltage: a Schottky rectifier, one or two low-voltage filter caps, and the output. Form factor ranges from the old captive-cable wall wart to the USB-A cube to the denser USB-C GaN brick, which packs bigger caps and more clever silicon into less space.

The cable, the output socket, and any ferrite beads are the usual prize. The caps and the transformer are occasional bonuses if the unit opens cleanly.

## Before You Open It

1. Unplug from mains and remove any batteries before opening. A charger has no battery, but make it the same habit across every donor so you never skip it on something that does.
2. Wait at least 30 seconds. The bulk primary cap in a small charger is only a few microfarads and bleeds down fast, but it's rated 400 V and can still give you a sharp jolt.
3. Before you reach for the primary side, set a meter to DC volts and measure across the bulk cap. Anything above 30 V means clip a 1 kΩ to 2 kΩ resistor across its legs for a few seconds, then recheck until it reads near zero.
4. Decide whether the case is even worth opening. Look hard at the seam first.

A lot of modern chargers are ultrasonically welded, which means there's no screw anywhere, just a glued plastic seam that has to be cracked. If the unit is potted in epoxy, the parts inside are entombed and you're better off keeping it whole for study than fighting the resin for a 10 cent cap.

## What to Target

Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Output cable or USB socket | Low-voltage end of the case | Connector type, wire gauge, strain relief quality | ★★★ |
| Ferrite bead or choke | Cable exit or input filter | Clip-on or wound style, intact core | ★★☆ |
| Electrolytic capacitors | Secondary side of the board | Low-voltage ratings, capacitance, ESR-sensitive service use | ★★☆ |
| Small transformer | Center of the board | Package size, isolation barriers, pin integrity | ★☆☆ |
| Bridge rectifier or diodes | Primary side near mains input | Package style and markings for later identification | ★☆☆ |

## How to Get Them Out

Most of the worthwhile yield comes off without heat. If you only want the cable, cut it free where it leaves the case and keep as much length as you can. Captive cables almost always fail right at the molded strain-relief boot where they flex most, so cut back past the boot to reach copper that hasn't been work-hardened. A USB socket on a separate daughterboard sometimes unclips or unplugs, but on most cheap units it's soldered straight to the main board, so it comes out with the iron.

Getting the case open is half the job on welded units. Run a sharp knife along the seam to score it, then work a thin blade in and lever along the line, or set the seam in a vise and tap it apart. Go slow. The plastic cracks where you don't want it to if you rush, and a slipped blade is the most likely way to cut your hand on one of these.

With an iron, the secondary caps and the output socket are through-hole on roomy boards. Heat from underneath, add a little fresh solder to wet the joint, then wick or pump. The ferrite transformer has four to eight thick pins with a lot of thermal mass, so feed fresh solder onto each pin and use a pump rather than wick, which won't pull enough heat through.

On dense USB-C boards almost everything is surface-mount, and hot air is the only sane way to lift the Schottky rectifier and the controller. Stagger the heat across the board so you don't warp it, and accept that the transformer will fight you the whole way because of its bulk. There's genuinely not much else to say about the hot-air tier here, since the parts that justify it are few.

## Watch Out For

- The bulk primary cap is rated around 400 V and can hold a sting after unplugging. Measure across it on DC volts before touching the primary side, and bleed it through a 1 kΩ to 2 kΩ resistor if it reads above 30 V.
- If you bench-test a board out of its case to confirm the output works, the entire primary half is live and exposed with no plastic around it. Probe only the isolated secondary, and never put fingers or a meter lead anywhere past the transformer while it's plugged in.
- Cheap and counterfeit chargers cut the isolation gap between primary and secondary down to nothing. Don't trust the low-voltage side as safe on a sketchy unit while it's powered, and if the gap between the two halves looks hair-thin, treat the whole board as live.
- Cracking a welded case throws sharp plastic shards and leaves jagged edges along the seam. Pry slowly and keep your guiding hand behind the blade.
- Old transformer bricks are heavy enough to tear their own pads loose if you desolder them dangling. Support the transformer or lay the board flat so its weight isn't hanging off the joints you're heating.

## Theory Links

- [DC measurements](/open-circuits/DC/DC_5.html) for testing the output side once the unit is safely isolated and discharged.
- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for identifying rectifiers, switches, and other three-terminal power devices on the board.

## Specific Teardowns

Specific make-and-model teardowns for wall chargers will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

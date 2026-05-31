---
title: "Routers and Modems"
section: donor-guides
hazard: 2
hazard_summary: "Low-voltage DC internally; powered by external adapter."
author: Claude
review: Needs Human Review
---

Routers, cable modems, DSL boxes, and access points are among the safest mains-adjacent donors you'll handle, because all the voltage conversion happens in the external power brick. The board inside runs entirely on low-voltage DC. That means you can open one on a table with no discharge steps and no particular electrical anxiety, and still walk away with a handful of useful parts.

## What's Inside

The main board is usually a single PCB running most of the enclosure's length. At one end you'll find the power input section: a barrel jack, a small bridge or a diode, and one or more synchronous buck regulators with shielded inductors stepping the 5 V or 12 V input down to the 3.3 V, 1.8 V, and core voltages the SoC needs. Consumer routers from the last decade almost always use a Qualcomm Atheros, MediaTek, or Broadcom SoC that integrates the CPU, switch, and WiFi radio into one package.

The RF section sits under one or more metal shield cans, which are soldered or press-fitted to the board and cover the radio circuitry. Dual-band units have two cans. Along the rear edge you'll find the RJ45 magjacks (integrated transformers and all), a USB port on units that support storage or modems, and sometimes a WAN port that's physically identical to the LAN ports. Front-panel LEDs and at least one tact switch (reset) run on flexible wire or directly from the main board edge.

On DSL gateway units and older VOIP-capable modems, check for a small backup battery tucked into a corner or mounted on a daughterboard. These are usually a small cylindrical lithium cell or a flat Li-ion pouch, and they stay charged while the unit was in use.

The magjacks and barrel jack are the reliable yield here. Everything else depends on what the board has room to carry.

## Before You Open It

1. Unplug the external power adapter from the wall and from the barrel jack.
2. If the unit has a backup battery, disconnect or remove it before handling the board.
3. Before pulling the board, photograph any antenna wiring and front-panel light pipe routing. These are fiddly to reassemble if you're keeping the enclosure for anything, and the antenna pigtail routing isn't always obvious once the board is out.

Wait a few seconds after disconnecting power. The small filter caps on the power rails bleed down almost instantly at these voltages, so there's no meaningful stored energy concern once the adapter is out.

## What to Target

Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Barrel jack | Power-input edge | Common 5 V or 12 V input styles, center-pin size | ★★★ |
| RJ45 jacks | Rear I/O row | Integrated magnetics, shield tabs, port count | ★★★ |
| U.FL antenna pigtails | Board-edge or SoC area, short coax to RP-SMA or IPEX | 50 Ω coax; length 50–150 mm; connector condition matters | ★★☆ |
| Electrolytic capacitors | Near input filtering and regulators | Voltage rating, capacitance, radial package | ★★☆ |
| Shielded inductors | Buck regulator area | Package size, inductance code, current-handling clues | ★★☆ |
| USB Type-A socket | Rear panel or board edge | Standard 2.0 or 3.0; through-hole or SMD mount | ★★☆ |
| Tact switches and LEDs | Front-panel area | Momentary action, lens color, package size | ★☆☆ |

## How to Get Them Out

Getting inside is the first obstacle. Screws on these enclosures are almost always under the rubber feet, so peel them back carefully, because the adhesive fails if you stretch them. Some units from TP-Link and Netgear also have a hidden screw at the back behind a sticker, so run your thumb around the seam before you lever anything. Once the screws are out, most cases split with a thumbnail along the side seam.

The antenna pigtails unplug at the U.FL (IPEX) connector on the board: use a fingernail or a spudger tip to lift straight up, not at an angle. The center pin tears out of the socket if you pull sideways, and a damaged U.FL isn't worth using. Keep the pigtails attached to their RP-SMA or screw-mount bulkhead connectors, since that's usually the useful end.

With a soldering iron, the barrel jack and RJ45 magjacks are both through-hole. The barrel jack is two or three pins and comes out easily. The magjacks are the time-consuming pull: each one has eight signal pins plus two or more wide shield tabs, and those tabs wick a lot of heat. Add fresh solder to wet each joint, work pin by pin, and use a pump rather than wick on the shield tabs. Trying to lift a magjack before all the shield tabs are free will tear the pads, so take your time and check continuity on the underside before you lever anything up.

The shielded inductors are SMD, and hot air is the right tool for them if you want them intact. The shield cans lift cleanly with hot air at around 300–320 °C once you've gone around all four sides. There's rarely a strong reason to remove a can unless you're after a specific chip underneath.

The tact switches and LEDs are through-hole on older units and 0805 or smaller on anything made in the last five years. Pull the through-hole ones the usual way. The SMD versions are too small to justify the effort unless you specifically need them.

## Watch Out For

- Screws under rubber feet are the rule on most consumer routers. Peel the feet back slowly from one edge rather than peeling them off entirely, and they'll re-stick.
- The pressed-metal shield can edges are sharp enough to cut your fingers if you slide a hand across them. Lift the board by its edges or by the connector row, not from the top.
- U.FL connectors need to be pulled straight up. An angled pull tears the center pin and ruins the socket on the board side, which is the half you usually want to keep.
- Some DSL gateway units have a thin telephone-line protection board (MOV and gas discharge tube) bridged between the DSL input and the main board by a flex cable. The flex connector is fragile, and the MOV itself can fracture if the board is dropped or flexed. Handle the DSL input side carefully.
- Pre-2010 units may have conformal coating over the board, which makes desoldering messy. It smells when heated and gums up wick. Scrape it off the pads with a knife tip before applying the iron.

## Theory Links

- [DC measurements](/open-circuits/DC/DC_5.html) for tracing input filtering and regulator outputs.
- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for identifying regulators, transistors, and protection devices around the power section.

## Specific Teardowns

Specific make-and-model teardowns for routers and modems will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

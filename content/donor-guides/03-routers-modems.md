---
title: "Routers and Modems"
section: donor-guides
hazard: 2
hazard_summary: "Low-voltage DC internally; powered by external adapter."
---

This guide will cover routers, cable modems, DSL boxes, and access points, which are usually safe low-voltage donors with a strong yield of connectors, regulators, passive parts, and enclosure hardware.

## TODO: What's Inside
Describe the main logic board, shield cans, barrel jack input, status LEDs, and the mix of connectors and small power circuitry that make networking gear a solid donor class.

## TODO: Before You Open It
Tell readers to disconnect the external power brick, remove any internal backup battery if present, and photograph antenna wiring or front-panel light pipes before pulling the board.

## TODO: What to Target
Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Barrel jack | Power-input edge | Common 5 V or 12 V input styles, center-pin size | ★★★ |
| RJ45 jacks | Rear I/O row | Integrated magnetics, shield tabs, port count | ★★★ |
| Electrolytic capacitors | Near input filtering and regulators | Voltage rating, capacitance, radial package | ★★☆ |
| Shielded inductors | Buck regulator area | Package size, inductance code, current-handling clues | ★★☆ |
| Tact switches and LEDs | Front-panel area | Momentary action, lens color, package size | ★☆☆ |

## TODO: How to Get Them Out
Explain how to free board-edge connectors without ripping pads, when hot air helps with shield cans, and when it is faster to keep subassemblies like antenna leads intact.

## TODO: Watch Out For
Mention fragile plastic clips, RF shield edges, hidden screws under rubber feet, and the occasional telephone-line protection parts that can tear off if the board is flexed.

## TODO: Theory Links
- [DC measurements](/open-circuits/DC/DC_5.html) for tracing input filtering and regulator outputs.
- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for identifying regulators, transistors, and protection devices around the power section.

## TODO: Specific Teardowns
Reserve this space for future router and modem teardowns that show which brands are easy to open and which are mostly glue and shield cans.

---
title: "Wall Chargers"
section: donor-guides
hazard: 2
hazard_summary: "Internal caps may hold charge; unplug and wait."
---

This guide will cover common phone chargers and plug-in adapters, which can yield connectors, ferrites, cable assemblies, and a few useful power parts if the enclosure can be opened without destroying everything.

## TODO: What's Inside
Describe the split between potted throwaway chargers and better serviceable units, then map the usual mains side, transformer or switcher section, and low-voltage output side.

## TODO: Before You Open It
Tell readers to unplug the charger, wait, inspect the case seam, and decide early whether the unit is glued too aggressively to justify opening at all.

## TODO: What to Target
Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Output cable or USB socket | Low-voltage end of the case | Connector type, wire gauge, strain relief quality | ★★★ |
| Ferrite bead or choke | Cable exit or input filter | Clip-on or wound style, intact core | ★★☆ |
| Electrolytic capacitors | Secondary side of the board | Low-voltage ratings, capacitance, ESR-sensitive service use | ★★☆ |
| Small transformer | Center of the board | Package size, isolation barriers, pin integrity | ★☆☆ |
| Bridge rectifier or diodes | Primary side near mains input | Package style and markings for later identification | ★☆☆ |

## TODO: How to Get Them Out
Explain when to cut the cable free first, how to keep the low-voltage side isolated from the primary side during teardown, and which parts are not worth fighting through potting compound to save.

## TODO: Watch Out For
Highlight glued cases, brittle plastic, stored charge on primary capacitors, and the rule that potted or damaged chargers are often better for study than for harvesting live parts.

## TODO: Theory Links
- [DC measurements](/open-circuits/DC/DC_5.html) for testing the output side once the unit is safely isolated and discharged.
- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for identifying rectifiers, switches, and other three-terminal power devices on the board.

## TODO: Specific Teardowns
Leave space for future teardowns of older transformer bricks, USB-A chargers, and USB-C adapters, noting how repairability and salvage yield differ.

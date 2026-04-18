---
title: "ATX Power Supplies"
section: donor-guides
hazard: 3
hazard_summary: "Large input caps hold 300V+ for minutes after unplugging."
---

This guide will cover ATX power supplies as high-yield but higher-risk donors, useful for fans, heatsinks, connectors, wire, power semiconductors, and large electrolytics if you know where the dangerous side begins.

## TODO: What's Inside
Describe the split between primary and secondary sides, the large input capacitors, heat-sinked power devices, transformer area, and output wiring that make ATX supplies both useful and serious.

## TODO: Before You Open It
Tell readers to unplug the supply, wait, verify the large capacitors are safe before going further, and stop if they cannot confidently identify the primary side and isolation boundary.

## TODO: What to Target
Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Fan | Top cover or rear panel | 12 V brushless type, bearing condition, connector | ★★★ |
| Output wire and connectors | Harness bundle | Wire gauge, ATX peripheral plugs, crimp quality | ★★★ |
| Heatsinks | Primary and secondary power stages | Mass, mounting holes, insulation hardware | ★★☆ |
| Power MOSFETs and rectifiers | Bolted to heatsinks | Package, markings, isolation pads | ★★☆ |
| Large electrolytics | Primary input and secondary filters | Capacitance, voltage rating, visible aging | ★☆☆ |

## TODO: How to Get Them Out
Explain the rule that low-risk harvesting focuses on the fan, case hardware, and output harness first, while board-level salvage waits until the dangerous capacitors are confirmed discharged.

## TODO: Watch Out For
State plainly that the primary capacitors can stay at hundreds of volts after unplugging, that isolation slots matter, and that the safest choice for many readers is to reuse a whole PSU rather than strip the board.

## TODO: Theory Links
- [DC measurements](/circuits/DC/DC_5.html) for verifying low-voltage outputs and checking discharge status with the right procedure.
- [Semiconductors](/circuits/Semi/SEMI_6.html) for understanding the MOSFETs and rectifiers that dominate PSU salvage value.

## TODO: Specific Teardowns
Reserve this section for future ATX teardown examples that compare older heavy units, modern efficient supplies, and the difference between good donor candidates and unsafe junk.

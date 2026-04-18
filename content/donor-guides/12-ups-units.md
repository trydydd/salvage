---
title: "UPS Units"
section: donor-guides
hazard: 4
hazard_summary: "Batteries stay live; can deliver very high short-circuit current."
---

This guide will cover small UPS units as donors for fans, relays, heavy-gauge wiring, IEC connectors, and sometimes reusable enclosures, while making clear that the battery system keeps the hazard alive even when the unit is unplugged.

## TODO: What's Inside
Describe the battery compartment, inverter board, charger section, relay cluster, fan, and mains I/O so readers understand why UPS units combine both ordinary salvage value and unusually persistent electrical risk.

## TODO: Before You Open It
Tell readers to disconnect the UPS from mains, remove or isolate the battery before touching the rest of the internals, and treat every heavy wire and bus bar as live until proven otherwise.

## TODO: What to Target
Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| IEC sockets and mains hardware | Rear panel | C13/C14 fittings, fuse holders, switch gear | ★★★ |
| Relays | Inverter and transfer section | Coil voltage, contact form, current rating | ★★☆ |
| Fans | Rear panel or top cover | Voltage, size, bearing wear, connector | ★★☆ |
| Heavy-gauge wire and ring lugs | Battery and inverter harnesses | Insulation condition, current-handling clues | ★★☆ |
| Lead-acid battery hardware | Battery tray and terminals | Terminal type, hold-down brackets, connector blocks | ★☆☆ |

## TODO: How to Get Them Out
Explain that the battery comes out first, that wiring should be insulated as soon as it is freed, and that relays or connectors on the board are only worth desoldering after the battery path is unquestionably safe.

## TODO: Watch Out For
Call out the battery short-circuit hazard, heavy components that shift when the case opens, charged capacitors in the inverter stage, and acid or corrosion from aged sealed lead-acid packs.

## TODO: Theory Links
- [DC measurements](/circuits/DC/DC_5.html) for testing fans, relays, and battery-side continuity only after the live battery path is removed.
- [Semiconductors](/circuits/Semi/SEMI_6.html) for identifying the inverter transistors and rectifiers that often dominate the board layout.

## TODO: Specific Teardowns
Leave room for future UPS teardowns that compare standby and line-interactive designs, with strong notes about battery isolation and which salvage tasks are reasonable for non-experts.

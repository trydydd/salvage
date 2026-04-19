---
title: "Desktop Computers"
section: donor-guides
hazard: 2
hazard_summary: "Low-voltage DC once unplugged; PSU is a separate device."
---

This guide will cover desktop towers and small-form-factor PCs, which are often generous donors for fans, heatsinks, cables, connectors, switches, and low-voltage board hardware.

## TODO: What's Inside
Describe the case, motherboard, drive assemblies, cooling system, front-panel wiring, and the important boundary that the ATX power supply should be treated as its own donor class.

## TODO: Before You Open It
Tell readers to unplug the machine, press the power button to drain the low-voltage rails, remove the side panels, and decide whether the PSU will stay sealed for a separate guide.

## TODO: What to Target
Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Fans | Case, CPU cooler, GPU shroud | Voltage, connector type, bearing noise, airflow direction | ★★★ |
| Heatsinks | CPU, chipset, VRM, GPU | Mounting style, fin density, flatness | ★★★ |
| Connectors and harnesses | Front panel, drives, motherboard edges | USB, SATA, headers, wire gauge | ★★☆ |
| Tact switches and LEDs | Front-panel board | Momentary action, LED color, lens size | ★★☆ |
| Inductors and capacitors | Motherboard power section | Package size, voltage rating, visible damage | ★☆☆ |

## TODO: How to Get Them Out
Explain the order that preserves value: pull whole modules first, strip cables intact, and only desolder motherboard parts if the connector or component is genuinely useful.

## TODO: Watch Out For
Mention sharp chassis edges, hidden screws in drive cages, stale thermal paste, and the temptation to open the PSU as if it were just another low-voltage board.

## TODO: Theory Links
- [DC measurements](/open-circuits/DC/DC_5.html) for continuity checks and fan testing.
- [Semiconductors](/open-circuits/Semi/SEMI_6.html) for reading the regulator and MOSFET-heavy power sections around a motherboard CPU socket.

## TODO: Specific Teardowns
Reserve this section for future examples that compare office desktops, gaming towers, and mini PCs by salvage yield and ease of disassembly.

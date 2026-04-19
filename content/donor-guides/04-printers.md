---
title: "Printers"
section: donor-guides
hazard: 2
hazard_summary: "Low-voltage logic; laser printer fuser runs at mains voltage (upgrade to 3 for laser)."
---

This guide will cover inkjet and laser printers as large-format donors with good mechanical yields: motors, sensors, rollers, rails, gears, and a scattering of power and logic parts.

## TODO: What's Inside
Map the printer into motion assemblies, paper-path sensors, logic board, power supply, and model-specific extras such as scanner heads or the mains-driven fuser in laser units.

## TODO: Before You Open It
Tell readers to identify whether the machine is inkjet or laser before opening it, remove cartridges or toner, and set aside any model that hides mains wiring in the first layer of disassembly.

## TODO: What to Target
Use this quick-reference table to show the first parts worth noticing when this donor lands on the bench.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Stepper motors | Paper feed and carriage assemblies | Coil count, connector style, shaft length | ★★★ |
| Optointerrupters | Paper path and lid sensors | Slot width, package style, emitter-detector pairing | ★★★ |
| Belts, gears, and rails | Carriage and feed mechanisms | Pitch, length, bearing surfaces, straightness | ★★☆ |
| Power connectors | PSU and board harnesses | Locking style, pin count, wire gauge | ★★☆ |
| Small fans | Laser printer power or fuser area | Voltage marking, size, bearing noise | ★☆☆ |

## TODO: How to Get Them Out
Explain how to strip mechanical modules in layers, keep matched sensor pairs together, and avoid damaging shafts or belts by forcing assemblies past molded stops.

## TODO: Watch Out For
Call out ink mess, toner dust, spring-loaded mechanisms, scanner glass, and the fact that laser printers bring mains wiring and hot fuser assemblies that deserve a higher-hazard approach.

## TODO: Theory Links
- [DC measurements](/open-circuits/DC/DC_5.html) for testing motors, switches, and sensor harnesses after removal.
- [Experiments](/open-circuits/Exper/EXPER_1.html) for simple bench setups that help sort motors and optical sensors into known-good bins.

## TODO: Specific Teardowns
Leave room for future inkjet and laser teardown notes, especially which families give the best motor and rail yields for small motion projects.

---
title: "Donor Guide Template"
section: donor-guides
---

This template shows the structure every donor guide should follow, with enough placeholder guidance that a human author can drop in device-specific advice without rebuilding the page from scratch.

## TODO: Frontmatter schema
Use `section: donor-guides`, set `hazard` to `1` through `4` for the device class, and write a `hazard_summary` sentence that names the worst-case danger in plain language.

## TODO: What's Inside
Describe the donor device at a glance, name the subassemblies readers are likely to find, and explain whether it is usually a quick harvest or a long teardown.

## TODO: Before You Open It
Tell the reader what to disconnect, discharge, remove, photograph, or identify before the first screw comes out, including any chemistry or mains checks that change the process.

## TODO: What to Target
Include a four-column table using the standard format below so the guide quickly answers what is worth pulling first.

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Example part | Main board edge | Mark the voltage, polarity, package, or connector family a reader can verify in hand | ★★★ |
| Example maybe | Power section | Note the rating range or package clues that make it useful later | ★★☆ |

## TODO: How to Get Them Out
Explain the teardown order, what tools help at different tiers, and which parts should be removed whole versus clipped, desoldered, or harvested with their wiring attached.

## TODO: Watch Out For
State the donor-specific hazards, the common ways people break salvageable parts during removal, and the point where the guide should tell an untrained reader to stop.

## TODO: Theory Links
Add short inline links to Open Circuits chapters using absolute paths such as [DC measurements](/circuits/DC/DC_5.html), [semiconductors](/circuits/Semi/SEMI_6.html), or [experiments](/circuits/Exper/EXPER_1.html).

## TODO: Specific Teardowns
Leave room for future model-specific links and note what a teardown entry should add beyond the generic guide: exact fasteners, board revisions, and the best-yield parts for that model.

---
title: "Tools and Workspace"
section: foundations
author: Claude
review: Needs Human Review
---
This page maps a workspace from the kitchen-table minimum up to a better-equipped bench, with the emphasis on what each tier of gear actually lets you salvage rather than on a shopping list.

## Minimum kit

You can start with less than you'd think. The non-negotiable items are a screwdriver set, a multimeter, and a pair of side cutters. With those three you can open most consumer gear, sort the parts, and tell whether what you pulled is alive.

For screwdrivers, a cheap precision set with interchangeable bits covers almost everything: small Phillips and flathead, plus the Torx and the occasional tri-wing or pentalobe that manufacturers use to keep you out. A magnetic tip saves a lot of dropped-screw hunting in a deep case.

A multimeter is the one tool worth not buying at the bottom of the range. A $15-30 meter with continuity, DC volts, resistance, and diode mode does everything in this guide. Continuity for tracing and checking switches, DC volts for confirming a supply or a discharged cap, diode mode for semiconductors. You don't need a $200 meter. You do need one that reads reliably.

Round it out as you go with what the work asks for: tweezers for SMD and fine wires, a spudger or an old guitar pick for prying plastic clips without scarring them, needle-nose pliers, and a craft knife. None of that is urgent on day one. Buy the next tool when a teardown actually makes you wish you had it.

## Soldering options by tier

How much soldering gear you need depends entirely on what you want to pull, and plenty of good salvage needs no iron at all.

**No iron.** Connectors, fans, motors, switches, heatsinks, wire, mechanical parts, and anything socketed comes off with a screwdriver and cutters. Cut a wire harness at the connector rather than unsoldering it and you keep the connector and lose nothing useful. A surprising amount of a teardown is reachable this way, and it's where to start.

**A basic iron.** A $20-40 temperature-controlled iron opens up through-hole desoldering: caps, diodes, regulators, relays, headers. Pair it with a solder sucker or a roll of desoldering braid. This is where most component salvage actually happens. The frustration point is large ground planes and big multi-pin parts, where a single iron can't put heat in fast enough.

**A desoldering tool.** A heated desoldering gun, or a hot-air station, makes the painful jobs reasonable. Hot air (a cheap 858D-style station is fine) lifts surface-mount parts and multi-lead packages you'd destroy with an iron. A heated suction gun clears through-hole boards fast. Neither is necessary for getting started, and both earn their place only once you're pulling SMD parts or doing enough volume that the time saved matters.

Buying in that order, no iron, then a controlled iron and braid, then hot air, matches each step to a real jump in what you can recover. Skipping straight to a hot-air station won't help if what you're pulling is fans and connectors.

## Holding and handling work

A board that slides around while you're heating a joint is how pads get torn and fingers get burned. You don't need a fixture to stop that. A blob of poster putty, a heavy mug, or a couple of jar lids will wedge most boards steady enough to work on.

The cheap version of a third hand is exactly that: a "helping hands" clamp with two alligator clips, often under $10, holding a board on edge so you can reach both sides. A small bench vise with soft jaws does the same job more solidly if you've got one. For fine work, anything that frees up the hand you'd otherwise use to hold the board is worth having.

Screws are the thing that turns a teardown into a mess. They're all slightly different lengths and they roll. Keep them sorted as they come out: a muffin tin, an egg carton, a magnetic parts mat, or strips of masking tape you press the screws onto in the order you removed them. Label which assembly each group came from. Reassembling later, or even just keeping the case shut on a half-stripped donor, depends on it.

Photograph anything before you take it apart if there's a chance you'll want to reverse the process or remember how a connector was routed. A phone photo costs nothing and has saved many a reassembly.

## Storage and labeling

Salvaged parts are only worth pulling if you can find them again. An unsorted box of components is just slower landfill. The fix is to sort by type first, then by the spec that matters for that type.

Small zip bags or a parts organiser with dividers work for most things. Group by family, electrolytics together, connectors together, semiconductors together, and within a family sort by the number you'll search on later: capacitance and voltage for caps, value for resistors, part number for ICs and transistors. Write the spec on the bag, not on a slip of paper inside that you'd have to open every bag to read.

Note your confidence along with the spec. There's a real difference between "IRF540, tested good" and "TO-220, markings worn, probably N-channel." Both are worth keeping. Mixing them up is how you waste an afternoon when a build doesn't work. A quick tag, tested or untested, keeps the doubtful parts from masquerading as known-good ones.

Keep the parts you reach for often within arm's reach and the long-shot stuff boxed and labeled on a shelf. The goal is that future-you, mid-build, can put a hand on the right connector in under a minute. If you can't, the salvage didn't really save you anything.

## Workspace habits

Good light is the cheapest upgrade to your bench. A bright, adjustable lamp you can pull right over the board turns squinting at a faded part number into reading it. Daylight-temperature LED is easy on the eyes for long sessions, and a magnifier or a phone camera's zoom handles the smallest markings.

Deal with solder smoke at the source. A small fan set to pull the flux plume sideways and away from your face is enough for occasional work, as covered on the safety page. Work near a window you can crack open. You don't need a fume hood to pull a few parts, but you shouldn't breathe a session's worth of rosin smoke head-on either.

Put the power on a single switched strip you can kill with one motion. When you're testing salvaged supplies or freshly built projects, cutting everything at once rather than groping for a plug is worth the few dollars a switched strip costs. Plug the iron into it too, so "bench off" also means "iron off."

Clean up between devices, not between sessions. Loose cut leads and stray screws migrate into the next teardown and into your fingers. A quick brush of the bench into a bin, and getting the last donor's parts into their bags before the next one comes apart, keeps the pile from compounding. The session you start on a clear bench is the one you'll actually finish.

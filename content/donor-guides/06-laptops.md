---
title: "Laptops"
section: donor-guides
hazard: 2
hazard_summary: "Remove battery first; lithium cells can be hazardous."
---

## What's Inside

Laptops have more distinct subassemblies packed into a smaller footprint than most consumer electronics. The main PCB (mainboard or logic board) runs across the middle of the lower shell and carries the CPU, GPU if there is one, memory (almost always soldered on machines made after 2015), and storage connectors. A flat lithium battery pack, either removable or glued under the bottom cover, occupies a large portion of the remaining space.

The cooling assembly is worth noting separately. A copper heatpipe routes from the CPU or GPU die to a fin stack, with a thin centrifugal (blower) fan pushing air through and out a side grille. On older machines the pipe terminates at a small flat heatsink. On modern slim designs it can span the full width of the board. The fan is a specific shape you won't find in standard fan assortments: squirrel-cage, 5V or 12V, often less than 5mm thick.

Daughterboards handle I/O. USB ports, audio jack, SD card reader, and the DC jack or USB-C charging port typically live on small boards along the side or front edges, each connected to the mainboard via a flat-flex cable or short wiring harness. The display assembly hinges at the rear and contains the LCD panel, LED backlight strip, webcam module, and two thin WiFi antenna coax leads running through the hinge channels.

The speakers and blower fans are the most consistently useful salvage from laptops. That fan form factor doesn't appear in standard component assortments, and the enclosed speaker units are shaped and tuned for compact builds in ways that bare speaker drivers aren't.

## Before You Open It

1. Disconnect the charger. The DC jack or USB-C charge board sees input voltage whenever the machine is plugged in, regardless of whether it's on.
2. On machines with a removable battery, slide it out before opening anything else. On slim machines with an internal battery, remove the back cover first, find the battery connector on the mainboard (a small flat plug near the battery's edge), and unplug it before touching anything else on the board.
3. Check for hidden screws before prying. Rubber feet almost always hide at least one, sometimes two. Labels, keyboard trim strips, and small plastic plugs are common spots too.
4. Photograph the screw locations before you start. Laptops often use three to five different screw lengths in the same base shell. A screw that's 0.5mm too long will crack the mounting boss or pull the thread out on reassembly.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Laptop speakers | Lower shell corners or front edge | 4–8 Ω; small sealed enclosure with attached cable; connector style varies by brand | ★★★ |
| Blower (centrifugal) fan | Cooling assembly, above or beside fin stack | 5V or 12V; 2-pin, 3-pin, or 4-pin connector; blade diameter 50–80mm; measure thickness before pulling | ★★★ |
| WiFi/BT card | M.2 slot on mainboard; mini-PCIe on older machines | M.2 2230 or 2242 footprint; two coax antenna leads attached; 802.11ac or ax visible on label | ★★☆ |
| DC jack or USB-C charge board | Side or front daughterboard | Board-mount or chassis-mount connector; short flex harness or wire loom to mainboard | ★★☆ |
| Heat pipe and fin stack | Cooling assembly above mainboard | One to four copper pipes; fin stack roughly 40–70mm wide; keep with the fan if storage allows | ★★☆ |
| Flat-flex (FFC) cables | Keyboard, touchpad, display connections | 0.5mm or 1.0mm pitch; cable width 10–40mm; ZIF locking connector at each end | ★★☆ |
| Webcam and mic module | Display bezel, top centre | Small PCB on short USB cable; USB 2.0; usually 720p or 1080p marked on board or cable | ★☆☆ |
| Display backlight LED strip | Bottom or side edge of LCD panel | Thin flex PCB with LED array; 3V; only worth pulling if you need the strip length. Older CCFL tubes aren't worth it. | ★☆☆ |

## How to Get Them Out

Most of what's worth pulling from a laptop comes out without a soldering iron. The order matters more than it does in most donors: back cover, battery disconnect, fans and heatsink, daughterboards, then speakers. Go for the heatsink before disconnecting the battery and you'll find screws buried under cables that don't have enough slack to move.

The blower fans are held by two or three screws and a small connector. On most machines the connector pulls straight off a header on the mainboard. Some Dell and HP builds route the fan cable under the fin stack: unscrew the fins before trying to move the cable, or you'll tear it. Keep the fan with its heatsink assembly if storage allows. They test and reuse better together.

Before pulling the WiFi card, disconnect the two antenna coax leads by lifting them straight up from the snap connectors (MHF4 size on most modern machines). Pulling at an angle breaks the connector body off the card. The leads don't need to come with the card; leave them in the chassis unless you specifically need them. One screw holds the card; remove it, then pull the card toward the open end of the slot.

Speakers come out with one or two small screws, followed by a glue tab on most modern machines. Keep the enclosure intact. A laptop speaker without its enclosure loses most of its low-frequency response. The enclosure is part of what makes it useful.

Flat-flex cables from the keyboard and touchpad detach by opening the ZIF latch first. The latch is a thin brown or beige tab that rotates 90° on a hinge on the connector body. Open it fully before touching the cable. If it isn't fully open and you pull anyway, the connector tears off the board. Once the latch is open, the cable slides straight out with no force.

DC jack and USB-C charge boards come out with one or two screws and a connector pull or flex detach, depending on the machine. There's usually no need to desolder anything.

## Watch Out For

- A swollen battery may already be lifting the bottom cover. Don't pry the cover against the pack, don't puncture it, and don't put pressure on the bulge. Slide the cover off at an angle that clears the swelling, set the pack aside in a non-flammable container, and let it discharge fully before disposal.
- Flat-flex connectors break when you pull the cable before opening the latch. If it doesn't slide out freely, the latch isn't open. Force tears the connector off the board and there's no recovering it.
- Screw lengths vary across the base shell, sometimes by less than 1mm. Keep them sorted by position, not by eye. A screw that looks identical to its neighbour but is half a millimetre longer will crack the mounting boss.
- The display panel is glass and breaks from flex, not just from drops. Prying the bezel sends force through the frame into the panel. Start at a bottom corner with a thin spudger or flat pick, work around slowly, and keep the assembly flat on the table while you work.
- Older machines (pre-2010 roughly) often used CCFL backlights running at 600–900V AC from a small inverter board near the hinge. If you see a small PCB with a transformer near the display hinge, or thin glass tubes inside the display stack, disconnect the inverter before handling the display assembly.
- Pre-2006 boards use leaded solder throughout. Wash hands after handling them, and ventilate if you're desoldering anything.

## Theory Links

For testing fans, switches, and speaker modules after removal, see [DC measurements](/circuits/DC/DC_5.html).

For simple continuity and low-voltage test fixtures that help sort tiny laptop parts, see [Experiments](/circuits/Exper/EXPER_1.html).

## Specific Teardowns

Specific make-and-model teardowns for laptops will be linked here as they are added. See `content/donor-guides/teardowns/` for in-progress guides.

---
title: "Audio Equipment"
section: donor-guides
hazard: 3
hazard_summary: "Mains-powered amplifiers can store energy in large filter capacitors."
author: Claude
review: Needs Human Review
---

This guide covers home audio gear such as powered speakers, stereo receivers, and amplifiers as donors for audio connectors, potentiometers, large filter capacitors, transformers, and heat sinks.

Old audio gear is one of the richer donors you'll find, partly because it was built to last and partly because the parts inside are big, well marked, and easy to handle. A 1980s receiver holds a real mains transformer, fat filter caps, a pair of finned heat sinks, and a front panel full of knobs and switches that still feel good after thirty years. Newer powered speakers and class-D amps are leaner but still give up useful connectors and a small switching supply. The catch is the same one that makes the gear worth opening: it runs on mains and stores energy. Linear amplifiers in particular keep a charge in their main filter caps after you pull the plug, so the discharge step here is not optional.

## What's Inside

Open the lid of a classic integrated amplifier or receiver and the chassis splits into recognizable zones. Near the mains inlet sits the power supply: a heavy transformer, a bridge rectifier, and two or more large electrolytic filter caps that smooth the rectified DC into the rails the amplifier runs on. The transformer is either a toroid, a doughnut wound on a round core, or an older EI type built from stacked steel laminations. Both are worth pulling.

The amplifier section runs down one or both sides of the chassis. Each channel ends in an output stage bolted to a finned aluminum heat sink, usually along the rear or the sides where air can move. The output transistors live on those heat sinks, mounted in complementary pairs so one device handles the positive half of the waveform and its partner handles the negative half. Around them sit driver transistors, emitter resistors, and bias components.

The front panel is its own parts bin. Volume, balance, bass, and treble are carried on potentiometers, often ganged so one shaft turns two tracks for stereo. Source selection runs through rotary or push switches with a satisfying detent. Behind the panel you'll sometimes find a small display, indicator LEDs, and a headphone jack.

The rear panel carries the connectors: RCA input and output jacks, speaker binding posts or spring clips, and on receivers an antenna section. These connectors are some of the most reusable parts in the whole unit because good audio jacks and binding posts are expensive to buy new.

Powered speakers and modern class-D units compress all of this. The transformer may be replaced by a compact switching supply, the heat sinks shrink, and the output stage becomes a small module. You still get connectors, a volume pot, and the supply, just less of everything.

## Before You Open It

1. Unplug from mains and leave it unplugged. Don't work on audio gear that's still connected, even switched off.
2. Wait at least 10 minutes before reaching in. The main filter caps in a linear amplifier are large, often 4700 microfarads to 22000 microfarads, and rated 35 V to 80 V or more. They bleed down slowly, and some hold a meaningful charge for many minutes.
3. Measure before you touch. Set a multimeter to DC volts and read across the terminals of each large filter cap. The terminals are usually the two solder lugs or the screw posts on top of the can. Anything above 30 V means wait longer.
4. If a cap is still above 30 V after 15 minutes, discharge it deliberately. Clip a 100 ohm to 1 kilohm resistor rated at least 5 W across the cap terminals using insulated leads, leave it for 30 seconds, then recheck with the meter. Repeat until you read below 5 V. Don't short the terminals with a bare screwdriver. That damages the cap and throws a spark.
5. Confirm zero before you commit. The meter reading across the caps is the only proof the supply is safe. When every large cap reads near zero, you can work.

The discharge habit is the same one from the foundations safety page. Treat every large can as charged until your meter says otherwise.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| Large filter capacitors | Power supply section | Capacitance, voltage rating, physical size | ★★★ |
| Toroidal or EI transformer | Power supply section | Primary/secondary voltages, VA rating, weight | ★★★ |
| Audio output connectors | Rear panel | Binding posts, RCA jacks, headphone jacks | ★★☆ |
| Potentiometers and switches | Front panel | Resistance taper, ganging, detents | ★★☆ |
| Power amplifier heat sinks | Output stage | Size, fin layout, mounting holes | ★★☆ |
| Output transistors | On the heat sinks | Complementary pairs, package, part numbers | ★★☆ |

The filter caps and the transformer are the headline parts. A clean, undomed filter cap from a name brand is worth keeping, and a transformer that reads sensible secondary voltages is a future power supply on its own. The connectors and controls earn their stars because they're hard to source new and easy to remove with the panel off. The heat sinks are good raw stock for any power build. The output transistors are worth pulling as matched pairs, but check the part numbers against what you can actually identify before spending desoldering time on them.

## How to Get Them Out

Work in an order that gets the bulky, awkward parts out first while the chassis still holds everything steady.

Start with the front and rear panels once the caps read zero. Potentiometers and switches usually mount with a threaded bushing and a panel nut, plus solder lugs or a ribbon to the main board. Remove the knob, undo the panel nut, then free the electrical connection. Keep ganged pots whole, and keep the matching knob with its pot so you remember the taper and feel later. Rear connectors come off the same way: nut or screws on the panel, then desolder or unclip from the board.

The transformer is heavy and bolted through the chassis floor, usually with one central bolt on a toroid or four corner bolts on an EI type. Support the transformer with one hand before you remove the last bolt so it doesn't drop and tear its leads. Then deal with the wiring. Primary leads go to the mains switch and inlet, secondary leads to the rectifier. Label which secondary pair is which before you cut, because an unlabeled multi-tap transformer is a guessing game later. Cut the leads long so you have wire to work with.

The filter caps mount in a few ways. Snap-in and screw-terminal cans sit upright on the board or on a bracket. Axial cans lie on their side in clips. For board-mounted caps, heat the leads from the underside and rock the cap free while you wick or pump the solder. Big cap leads are thick and hold a lot of heat, so give the joint time and use a clean, hot tip. Don't yank a cap that hasn't fully released. You'll lift the pad.

The heat sinks unbolt from the chassis and the board. Before you pick up an iron, remove the screws holding the output transistors to the sink so the board isn't fighting the metal. Desolder the transistor leads, then lift the heat sink with its transistors still attached if you want to keep the pairing intact. Keep the insulating hardware together: the mica or silicone pads and the nylon shoulder washers are small, easy to lose, and harder to replace than the transistors. Bag the matched complementary pairs with a note of their part numbers.

## Watch Out For

- The main filter caps hold a real charge after unplugging. Measure across each one with a meter before reaching in, and discharge any cap above 30 V through a resistor as described above. This is the hazard most likely to hurt you on this bench.
- Mains wiring runs from the inlet to the switch, the fuse, and the transformer primary. Identify it and keep clear of it until the unit is unplugged and the caps are confirmed dead. Don't cut wiring you haven't traced.
- The transformer is heavy and dense. Support it before the last bolt comes out, and lift with your hand under it rather than by its leads, which can tear loose and leave bare mains-side conductors.
- Chassis edges and stamped brackets are sharp. Run a finger along an edge before you grip it, and tape over anything that catches while you work inside the case.
- Old gear may use leaded solder and dusty interiors. Ventilate while desoldering, wash your hands afterward, and blow the dust out before you start so it doesn't end up in your face.

## Theory Links

For checking voltages and confirming discharged capacitors, see [DC measurements](/open-circuits/DC/DC_5.html).

For transformer and inductor basics behind the power supply, see [AC circuit experiments](/open-circuits/Exper/EXP_4.html).

For identifying the output transistors, see [Semiconductors](/open-circuits/Semi/SEMI_6.html).

## Specific Teardowns

Specific make-and-model teardowns for audio gear will be linked here as they're added. See `content/donor-guides/teardowns/` for in-progress guides.

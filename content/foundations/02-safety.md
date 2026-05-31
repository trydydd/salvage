---
title: "Safety"
section: foundations
hazard: null
---
Most of what you'll salvage runs at voltages that can't hurt you. A handful of devices can, and a few can kill you minutes or hours after they're unplugged. This page sorts those apart so you know when a job is routine and when it needs a procedure before you pick up a tool.

## Electricity and the body

What hurts you is current through your body, not voltage on its own. Voltage matters because it pushes current through whatever resistance your skin offers. Dry skin runs something like 50–100 kΩ across two hands, and at that resistance a 9 V battery or a 12 V rail can't push enough current to register. Wet, sweaty, or broken skin drops to a few kΩ, and the same contact pushes far more. Open Circuits covers the shock-current side of this in its [Electrical Safety](/open-circuits/DC/DC_3.html) chapter.

The numbers worth carrying in your head are small. Around 1 mA is the threshold you can feel. By 10–20 mA your muscles clamp and you can't let go of the conductor you're holding. Somewhere past 50 mA across the chest, the heart can drop into fibrillation. Mains at 120–230 V through damp skin clears that range easily, which is why mains and stored high voltage sit in a different category from everything else here.

The path counts as much as the current. Hand to hand runs straight across your chest, and so does hand to foot. The habit that protects you is to keep one hand off the work whenever you're probing something that might be live above 50 V, so there's no loop through your chest.

The mistake beginners make is bracing themselves: planting the spare hand flat on the chassis or the board edge while reaching in with the probe. That's the exact hand-to-hand path you're trying to avoid. Keep the spare hand in a pocket or behind your back and let the bench hold the work, not you.

Most salvage never gets near this. Anything battery-powered, or fed from an external wall adapter, runs at voltages that won't drive a dangerous current through dry skin once it's unplugged. Save the one-hand discipline and the measure-first habit for devices that plug straight into the wall, and for the stored charge covered next.

## Capacitor discharge

A capacitor holds its charge after you cut the power. A large electrolytic on a PSU primary, 220–680 µF at 200–400 V, can sit at most of its working voltage for minutes after the plug comes out, and the bleeder resistor meant to drain it sometimes fails open. There's enough stored energy there to burn you, knock you back off the bench, or weld a screwdriver tip.

1. Unplug and wait. Ten minutes is a sensible floor for PSU primary caps, and longer for a supply that was running hard.
2. Set a multimeter to DC volts and measure straight across the cap's two terminals. The reading is the only thing you can trust, since time alone is no guarantee. See [DC measurements](/open-circuits/DC/DC_5.html) for the basics.
3. If it reads above about 30 V, drain it through a resistor instead of waiting. A 10 kΩ 1–2 W resistor across the terminals pulls a big cap down in under a minute. Clip it on, leave it a moment, recheck.
4. Confirm the meter reads under 5 V before you reach in or pick up an iron.

Don't discharge a big cap by shorting it with a screwdriver. The spark pits and welds the tip, can crack the cap internally, and sprays bits of metal. A resistor turns the same energy into a couple of seconds of mild warmth instead. The capacitor discharge tool project builds a reusable version of this, a resistor and a pair of leads in a handle, so you're not clipping loose parts on every job.

Caps marked in kilovolts, the kind inside CRTs and microwave ovens, are a different scale of danger. Treat anything rated in kV as lethal and follow the device-specific procedure in its donor guide rather than the bench routine above.

## Mains awareness

The first question for any unfamiliar device is whether it has a mains section at all. If it runs from batteries or plugs into an external wall adapter, the inside is low voltage and safe to open once it's unplugged. If it plugs straight into the wall on its own cord, part of the board runs at mains voltage and holds charge after the plug comes out.

You can read the mains side off the board once you know the shape of it. It starts where the cord enters, usually through a fuse and a couple of film capacitors (the X and Y caps in the input filter), into a bridge rectifier and one or two large electrolytics. From there an optocoupler and a routed slot or air gap across the PCB mark the isolation boundary. Everything past that line runs at the low voltages the device actually uses.

Find that boundary before you touch anything on a mains device. If you can see it clearly, discharge the primary caps as above and you can work the whole board. If you can't find it, keep to the parts obviously on the safe side, the fan, the output wiring, the mechanical hardware, or leave the device closed. Deciding a particular board isn't worth the risk and pulling only the easy externals is a perfectly good outcome.

## CRT safety

A CRT is the one donor within easy reach that can kill you with stored charge weeks after it last ran. The anode sits at 25–30 kV in use, and the glass and the conductive coating around it form a capacitor that holds a large fraction of that for a long time afterward. The thick rubber cup on the side of the tube, the anode cap, covers that connection.

If you haven't been trained to discharge a CRT, and you don't have an insulated HV probe and a grounding lead, leave the tube alone. This is the one place in the guide where the right move for most readers is to not open the device. You can still take the speakers, the cabinet hardware, the degaussing coil, and the circuit boards that sit away from the tube neck, none of which go near the anode.

Done properly, discharging a CRT means clipping a jumper from chassis ground to an insulated screwdriver or HV probe, sliding the tip under the lip of the anode cap until it touches the anode button, and waiting for the discharge. Done wrong, it arcs across your hand. If that description doesn't already sound familiar, take it as the signal to stop and leave the tube to someone equipped for it.

The tube is under vacuum on top of all that. A sharp knock to the neck can implode it and throw glass across the room. Keep tools clear of the neck, and don't try to vent or cut into a tube.

## Batteries

A lithium cell stores a lot of energy in a thin package, and it fails hard when that package is breached. Puncturing, crushing, or sharply bending a lithium pouch or an 18650 can vent and catch fire within seconds, and a pack that's already swollen has failed internally and is heading that way. Handle them with that in mind:

1. Take the battery out before you start a teardown, not partway through, so you're never levering a board around next to a live cell.
2. Tape over the terminals once it's out, so a dropped tool can't short it.
3. Treat a swollen or warm pack as finished. Don't charge it, don't puncture it to "deflate" it, and take it to a battery recycler rather than the household bin.

Sealed lead-acid batteries, the kind in a UPS or an emergency light, look inert and carry a different danger. A small 7 Ah SLA holds enough short-circuit current to dump well over 100 A into a dropped wrench, heating it red-hot and welding it across the terminals. Take off rings and a watch before you handle one, cover one terminal while you disconnect the other, and lift with the weight in mind. The acid and the mass are the lesser problems next to that short-circuit current.

When you reconnect any salvaged cell to test it, check polarity twice before the leads touch. A reversed charger or a backward meter lead is a fast way to vent a cell or pop a component.

## Lead solder and fumes

The smoke that rises when you solder is burning flux, not vaporised lead. Lead boils far above any soldering iron's temperature, so it doesn't go airborne at the bench. The rosin in that smoke is a real respiratory irritant though, and a long session breathing it straight on will leave you coughing.

Keep the smoke out of your face. A small desk fan set to draw the plume sideways, or an open window with a bit of cross-draught, handles occasional work fine. A proper fume extractor is a nice upgrade if you solder a lot, not a requirement for pulling a few parts.

Lead itself gets into you hand to mouth, not through your skin or your lungs. So the rules are dull and they work: wash your hands before you eat or touch your face, keep food and drink off the bench, and don't let kids handle the spool or the dross tray. Leaded and lead-free solder both want the same handwashing habit. Lead-free just drops the lead worry and trades it for a higher melting point.

## Sharps and mechanical hazards

Most of the cuts you'll pick up salvaging come from stamped sheet metal. PSU lids, drive cages, and case panels have shear edges sharp enough to open your hand if you drag it across one reaching for a screw. Run a finger along an edge before you commit to a grip, and cover anything that catches with a strip of electrical tape while you work.

Printers, optical drives, and retractable mechanisms are full of springs under load, and they let go the moment you pull the screw or clip holding them. Expect it. Take retaining screws out with the assembly held down, and ease tension off deliberately rather than letting it snap. Safety glasses earn their place around anything spring-loaded or under vacuum.

Snapped plastic leaves edges as sharp as the metal does. Cut and pry away from your body and your other hand, so a slip ends in air rather than skin. Lamps, scanner beds, and CRT tubes bring glass into the mix, and a CRT under vacuum can throw it. Wear the glasses, keep tools away from the neck, and cover the metal edges as above.

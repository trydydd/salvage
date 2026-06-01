---
title: "LED Bulbs"
section: donor-guides
hazard: 2
hazard_summary: "Small driver board with minor stored energy."
author: Claude
review: Needs Human Review
---

This guide covers mains LED bulbs and lamps as compact donors for LED boards, diffusers, small heat sinks, and a few low-cost driver components if the housing can be opened without shattering the shell.

A dead LED bulb is rarely dead all the way through. Most of them fail because one LED in a series string goes open and takes the whole string dark, or because a cheap driver cap dries out. The aluminum body, the diffuser, and often most of the LEDs are fine. That makes these good practice donors. They're everywhere, they cost nothing, and the worst that happens if you crack one is you've lost a burned-out bulb. Treat your first few as teardown practice rather than a parts haul and you'll do better on the ones that matter.

## What's Inside

Pull the diffuser off a standard A19-style bulb and the layout is almost always the same. A frosted plastic or glass dome sits over a flat round circuit board, the LED board, dotted with small white LED packages. That board screws or clips to an aluminum slug or shell that doubles as the heat sink and the body of the lamp. Below the slug, tucked into the base, is a small driver board that converts mains AC down to the constant current the LED string wants.

The LED board is the part worth the most attention. The LEDs sit in a series string, sometimes two strings in parallel, mounted on a metal-core PCB (MCPCB) that spreads heat into the slug behind it. Count the packages and you can usually work out the string voltage later. Cheaper bulbs use a single string of many small LEDs run at low current. Better ones use fewer, larger emitters.

The driver is the smallest and least rewarding part. In a budget bulb it's a capacitive-dropper design: a film cap, a bridge rectifier, a couple of resistors, and a small electrolytic, with no transformer and no isolation from the mains. In a better bulb it's a small switching driver with a tiny inductor or transformer and a driver IC. The switching type is safer to reuse and holds more interesting parts, but both are cramped and the components are small.

The aluminum shell and the diffuser are the easy wins. The shell is real machined or cast aluminum, useful as a heat sink for a future build. The diffuser is a ready-made light-spreading dome that fits a round board nicely. Think of LED bulbs as a source of enclosures and LED panels first, components second.

## Before You Open It

1. Unplug the bulb and let it sit. Five minutes is plenty for the small driver caps in a bulb. There's no large reservoir here like in a PSU, but the dropper cap can still bite, so don't rush it.
2. Decide your approach before you pry. Look at the seam where the diffuser meets the body. If it's a clean snap-fit you can often twist it off by hand. If it's glued, you'll need heat or a blade, and you have to choose whether you care about keeping the diffuser whole.
3. Check whether the dome is glass or plastic. Tap it gently against a fingernail. Glass rings, plastic thuds. Glass domes shatter into sharp fragments and want gloves and eye protection. Plastic domes are more forgiving but can crack along glue lines.
4. Decide if the base matters to you. If you want to reuse the E27 or B22 shell, work gently from the diffuser end and leave the base crimp alone. If you only want the boards, you can be rougher and break the base apart from below.

The whole job is low hazard. The thing that hurts people here is glass and blades, not voltage.

## What to Target

| Component | Where | Specs | Worth-it |
|-----------|-------|-------|----------|
| LED board | Under the diffuser | Series LED count, board diameter, thermal pad layout | ★★★ |
| Diffuser globe | Outer shell | Material, size, light spread for enclosure reuse | ★★☆ |
| Aluminum heatsink shell | Body of the lamp | Thread style, mass, mounting options | ★★☆ |
| Bridge rectifier and small caps | Driver board | Package, voltage rating, compact mains-driver parts | ★☆☆ |
| E27 or B22 base hardware | Lamp base | Thread or bayonet shell for fixture experiments | ★☆☆ |

The LED board earns its three stars because it's both the easiest part to free and the most reusable. A round panel of working LEDs already mounted on a metal substrate is a finished light source. The diffuser and shell are solid two-star picks: useful, easy, but not worth fighting glue for. The driver parts sit at one star because they're tiny, often cheap, and a capacitive dropper has very little worth pulling. The base hardware is a curiosity for fixture experiments more than a real component.

## How to Get Them Out

Start with the diffuser, because everything else is under it.

On a snap-fit bulb, grip the dome and the body in separate hands and twist while pulling. It either pops or it doesn't. If it doesn't budge, it's glued.

For glued diffusers you have two routes. The gentle one is heat: warm the seam with a hair dryer or a heat gun on low, kept moving, until the glue softens enough to work a thin plastic spudger into the joint. Run the spudger around the rim and the dome lifts. The faster but riskier route is a thin blade run around the seam, which works but tends to crack plastic domes and will crack glass ones. If you don't care about keeping the dome whole, a glass diffuser can simply be broken away. Wrap it in a rag, tap it, and pick the LED board out of the pieces.

With the dome off, the LED board is exposed. It's usually held by two or three small screws into the slug, or pressed against the slug under a retaining ring, or in cheaper bulbs just stuck down with thermal adhesive. Screws come straight out. A retaining ring lifts off. Thermal adhesive is the annoying case: warm the back of the slug with the heat gun and ease a spudger under one edge of the board, lifting evenly so you don't snap it. MCPCBs are stiff but they crack if you pry from a single corner.

Once the board is free, the driver hangs below on its wires. The board-to-driver connection is usually two short wires soldered at both ends or a small two-pin plug. Snip the wires or unplug, and the LED board is a clean, separate part. Keep the LED board, its diffuser, and its slug together as a matched set if you're thinking about a lamp project later. They're sized for each other and rarely interchange cleanly between bulbs.

The driver pulls out of the base by its mains-side wires, which run up to the screw shell and the center contact. Snip those and the driver is free. The aluminum shell is then empty and ready to reuse. If you want the E27 or B22 base shell intact, it's usually crimped or glued to the body, and getting it off whole takes patience with heat and gentle prying.

For the driver components themselves, the through-hole parts come off with an ordinary iron from the underside. The film dropper cap and the bridge rectifier are the only parts most people bother with, and only on switching drivers is the small inductor or transformer worth the effort.

## Watch Out For

- Glass diffusers shatter into sharp shards. Wear eye protection and a glove on the hand holding the dome, and break glass inside a rag so the pieces stay contained. Sweep up small fragments rather than wiping with a bare hand.
- Plastic domes and bases turn brittle after years of heat near the base. They snap without warning along glue lines. Work slowly and keep your prying force spread out so a crack doesn't run into your fingers.
- The aluminum slug and any stamped shell edges can be sharp where the casting was trimmed. Run a finger along an edge before you grip it hard, and cover anything that catches with tape while you work.
- The driver board carries a small but real stored charge after the lamp is off the fixture, mostly in the dropper cap. Five minutes of sitting handles it. If you want to be sure, briefly bridge the dropper cap's two leads with an insulated screwdriver tip before handling, and check across them with a meter on DC volts.
- Capacitive-dropper drivers are not isolated from mains. The whole driver board, and sometimes the LED board too, can sit at mains potential when powered. Never power a bare bulb board on the bench without isolation, and treat any non-switching driver as live when plugged in. For testing LED strings, use a current-limited bench supply, not mains.

## Theory Links

For checking LED strings and polarity with a current-limited setup, see [DC measurements](/open-circuits/DC/DC_5.html).

For simple LED test rigs and current-limited bench habits, see [Experiments](/open-circuits/Exper/EXP_2.html).

## Specific Teardowns

Specific bulb teardowns will be linked here as they're added, comparing easy-to-open repairable lamps with fully glued disposable ones. See `content/donor-guides/teardowns/` for in-progress guides.

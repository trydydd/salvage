---
title: "Diodes"
section: components
---

Diodes are everywhere on donor boards, and most come off cleanly with a quick diode-mode check telling you exactly what you've got. The tricky part is separating the families by sight before you probe them, because the packages overlap in ways that will trip you up if you haven't seen them before.

## Identify the type

The standard rectifier diode is an axial cylinder, about 5mm long, with a colored stripe at one end marking the cathode (negative end). The 1N400x series (1N4001 through 1N4007) is the type you'll see most: same gray glass or black plastic body, stripe at the cathode, rated 1A at various voltages from 50V to 1000V. Signal diodes like the 1N4148 use the same DO-35 package but smaller, about 3mm, usually with an orange-tinted glass body. The marking is printed on the body in tiny text and often faded; the stripe is still reliable.

Schottky diodes look like any other DO-41 or DO-35 part on the outside. Common ones in salvage include the 1N5817, 1N5819, and BAT46. The only way to be sure you have a Schottky is by the part number or the forward voltage measurement. Schottky forward voltage (0.15–0.45V depending on current and temperature) is noticeably lower than silicon (0.55–0.8V), so diode mode on the meter will tell you quickly.

Zener diodes use the same packages as signal diodes and are easy to confuse. The marking is the clue: a zener might be labeled BZX55C5V6 (a 5.6V zener) or 1N4733A (5.1V). The number after the type code is the zener voltage. In diode mode, a zener reads the same forward voltage as a regular silicon diode; you can't test the zener voltage with a standard meter without a separate circuit.

Bridge rectifiers are the square or rectangular four-pin blocks, through-hole or SMD, with AC, +, and – terminals usually marked on the case. SMD diodes come in SOD-123 (about the size of a 0805 resistor with a band at the cathode end), SOD-323 (smaller), and the SOT-23 three-pin package (which is a diode plus a second function, or a dual diode). LEDs are the clear or colored dome parts you know already. In salvage they sometimes appear on boards with the dome removed for space reasons, leaving just a flat-top LED that looks almost like a tantalum cap until you probe it.

## Use diode mode

Set your meter to diode mode (the diode symbol, usually shared with the continuity buzzer position). In this mode, the meter applies a small voltage through the probes and displays the forward voltage drop in volts.

**Forward check**

Touch the red probe to the anode and the black probe to the cathode (the end with the stripe). Keep the meter in diode mode — do not switch to a voltage range. A good silicon rectifier or signal diode reads 0.55–0.80V. A Schottky reads 0.15–0.45V. A germanium diode (mostly older through-hole stock) reads 0.20–0.35V.

**Reverse check**

Swap the probes: red to cathode, black to anode. A good diode reads OL (over-limit), meaning no significant current flows. Any numeric reading in reverse means the diode is leaking, which makes it suspect. A reading close to zero in reverse means it's shorted.

**In-circuit vs. desoldered**

For a quick check on an otherwise healthy board, probing in-circuit is sometimes good enough. Parallel paths through the circuit can lower the forward voltage reading or give you a false OL in reverse. If the reading looks wrong, desolder one leg (the cathode is easier to lift on most through-hole parts because it's near the board edge in rectifier circuits) and check again.

**LED forward voltage by color**

LEDs in diode mode light faintly if the meter voltage is enough. Red and infrared LEDs read 1.7–2.2V. Yellow and orange read 1.8–2.2V. Green LEDs vary: standard green reads 1.9–2.5V, but high-brightness green reads 2.9–3.6V. Blue and white read 3.0–3.6V. A reading below 1.5V on what looks like an LED usually means the part is shorted or it's actually a photodiode.

> ⚠️ **FACT-CHECK 6** — The 1.5V threshold for calling an LED shorted or a photodiode may be slightly too high; verify photodiode Vf (e.g. BPW34, TEPT5700) and whether any common consumer LED type legitimately reads below 1.5V without being defective.

## Forward voltage by type

The forward voltage range is your best quick-sort tool when you're working through a batch of unmarked parts. Write the reading down and match it to the family:

- 0.15–0.45 V: Schottky silicon
- 0.20–0.35 V: germanium (old stock, glass body, often marked OA91 or AA119)
- 0.55–0.80 V: standard silicon rectifier or signal diode
- 1.7–2.2 V: red or infrared LED
- 1.8–2.2 V: yellow or amber LED
- 1.9–2.5 V: standard green LED (typ 2.2 V, max 2.5 V)
- 2.9–3.6 V: blue, white, or high-brightness green LED (HB-green typ 3.2 V, max 3.6 V)

Zeners read a normal silicon forward voltage in diode mode. You can't identify the zener voltage without a test circuit that applies reverse voltage up to the breakdown point.

## Common failure modes

**Shorted**

The most common failure in power rectifiers and bridge diodes. Overvoltage (usually a surge from the AC line or an inductive load) or sustained overcurrent burns through the junction and leaves the part conducting in both directions. In diode mode, a shorted diode reads a low voltage (0.1V or less) in both directions, or reads zero. The body is sometimes cracked or scorched, but often looks fine. A shorted rectifier in a bridge supply will blow the input fuse and may damage the transformer or filter caps.

**Open circuit**

Less common than shorting but happens when a diode is overloaded and the bond wire inside burns through rather than the junction shorting. In diode mode, an open diode reads OL in both directions. You'll find this occasionally in high-current positions where the fuse or protection was slow to respond. Open diodes are not reusable.

**Leaky in reverse**

A reading in reverse diode mode that isn't quite zero and isn't OL indicates the junction is partially broken down. The part may still pass the forward test. Leaky diodes are unreliable in anything voltage-sensitive, like a clamp or reference circuit, and should be discarded. They're not obviously dangerous, just inaccurate.

**Heat stress without obvious failure**

Rectifier diodes in linear power supplies often run warm continuously. A diode that has lived near its rated current for years may measure fine on the bench but fail prematurely under load. If you're pulling from a supply where the diode ran warm (yellowed or browned board underneath it), expect shortened remaining life and derate accordingly.

## Reuse notes

Standard rectifier diodes (1N4001–1N4007, 1N5400–1N5408) are worth pulling in quantity. They're used in almost every DC power circuit: rectifying AC, blocking reverse voltage, and clamping inductive spikes. Sort them by part number if you can read the markings; if not, a diode-mode reading will at least confirm it's silicon and give you the forward voltage range. Store them in labeled compartments by current rating (1A vs 3A vs higher) if you're pulling mixed types.

1N4148 signal diodes are worth a dedicated small parts bag. They appear in audio, logic, and protection circuits, and a general stock of 50–100 costs less than one new component module. Keep them separate from rectifiers because the packages look identical.

Schottky diodes are worth pulling and labeling by part number if you can read it, or "Schottky" plus the measured forward voltage range if you can't. They're useful in low-dropout circuits and as flyback clamps across relay coils.

Don't bother desoldering SMD diodes smaller than SOD-323 unless you specifically need one for a project. The time cost outweighs the stock value. SOD-123 parts are manageable.

Don't reuse diodes with any visible cracking, burning, or a zero-ohm reading in both directions. Don't reuse bridge rectifiers from a supply where the fuse blew: the event that blew the fuse may have shorted the bridge.

## Theory links

For how diode junctions work and why the forward voltage matters in circuit design, see [Semiconductors](/open-circuits/Semi/SEMI_6.html). For meter habits that make diode-mode readings consistent and meaningful, see [DC measurements](/open-circuits/DC/DC_5.html).

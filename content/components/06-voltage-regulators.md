---
title: "Voltage Regulators"
section: components
---

Voltage regulators are among the easiest active components to identify and test in salvage. The common linear families print the output voltage directly in the part number, and a bench supply plus a meter is enough to confirm whether a pulled part still regulates properly.

## Common families

The 78xx series covers positive linear regulators in TO-220 packages: 7805 outputs 5V, 7808 outputs 8V, 7809 outputs 9V, 7812 outputs 12V, 7815 outputs 15V. The input must be at least 2–3V above the rated output to regulate correctly. Rated current is 1A in the standard TO-220 package. The 79xx series is the negative-voltage counterpart: 7905 outputs -5V, 7912 outputs -12V. These use the same package but the pinout is mirrored, which trips people up when they're testing or wiring a part they haven't identified yet.

The LM317 and LM337 are adjustable versions of the same idea. The LM317 sets its output using two resistors between the output and adjust pins: output ranges from 1.25V to around 37V, current up to 1.5A in TO-220. The LM337 does the same for negative voltages. You'll recognize these by the part number on the body. Without knowing the surrounding resistor values, you can't predict the output voltage from the part number alone, which matters when you're testing a desoldered LM317 without the resistors attached.

LDO (low dropout) regulators are the small three-pin parts you'll find on every modern logic board: AMS1117-3.3, AMS1117-5.0, LP2950, MCP1700, and many house-numbered equivalents. They appear in SOT-89 or SOT-223 packages (wider body, larger tab than SOT-23, three visible leads plus a fourth pad) or occasionally TO-92. The AMS1117 is the most common: it's on virtually every cheap Arduino clone, USB hub, and development board made in the last fifteen years. The suffix codes the output: AMS1117-3.3 gives 3.3V, AMS1117-ADJ is adjustable.

Switching regulator ICs are a different animal. The MC34063 in an 8-pin DIP runs buck, boost, or inverting converter topologies from a single chip, and you'll spot it on boards with an adjacent inductor, a diode, and a filter cap. The LM2576 and LM2596 are fixed or adjustable buck regulators in 5-pin TO-220 or TO-263 packages. These are harder to test without supporting circuitry, and the neighboring components matter as much as the chip.

## Read the markings

The 78xx and 79xx part numbers decode directly: the last two digits are the output voltage in volts. A part marked UA7805 or LM7805 or KA7805 or MC7805 all output 5V regulated. The prefix (UA, LM, KA, MC, NJM, etc.) identifies the manufacturer but doesn't change the function. A suffix letter indicates package type: 7805T is TO-220, 7805CT is the same package from some manufacturers.

The 78Lxx and 79Lxx parts look like TO-92 transistors and output 100mA. A 78L05 in a TO-92 package looks identical to a 2N3904. You can't tell them apart by eye. If you're pulling what looks like a transistor from the +5V or +3.3V rail of a device, check the silk screen for an "L" in the part number or a voltage reference in the nearby schematic notation.

AMS1117 and similar LDO regulators print the output voltage as a suffix after a dash: AMS1117-3.3, AMS1117-1.8, NCP1117-5.0. The tab on a SOT-89 package connects to the output terminal (not the input, not ground), which surprises people who assume it's ground like a MOSFET tab. This matters if you're trying to heatsink one on a board: the tab is at output potential.

If the part number is completely worn off a TO-220 regulator, the output voltage test below is more useful than trying to guess from appearance.

## Testing approach

**Quick output voltage test**

Desolder the regulator or test it in circuit on a powered-down board with an external supply applied at the input. For a 7805, apply 8–12V to the input pin (pin 1 in the standard TO-220 orientation), connect ground to pin 2, and measure pin 3 against ground. A healthy 7805 reads 4.92–5.08V. A 7812 should read 11.8–12.2V. The tab on a 78xx TO-220 is connected to the ground pin, so if you're using the tab as a ground reference it'll read correctly.

The 79xx series uses the same physical package but the pinout is different: in the standard orientation (tab facing away, leads pointing down), pin 1 is ground, pin 2 is input (negative voltage), and pin 3 is output. Connect the negative terminal of your supply to pin 2 and measure pin 3 versus ground.

**Load test**

A regulator that reads the right voltage at no load can still fail under current. Add a load resistor between output and ground to draw 100–200mA: for a 5V regulator, a 27Ω to 47Ω resistor works. The output should stay within 1% of rated voltage while the load is connected. If the output droops more than 5% under that load, the regulator is degraded.

Linear regulators dissipate (Vin minus Vout) times load current as heat. A 7805 running from 12V input at 500mA dissipates 3.5W. It will go into thermal shutdown without a heatsink, and the output will cut out and recover repeatedly. If you see the output cycling on and off during a load test, that's thermal shutdown, not a failed part.

**LDO in-circuit quick check**

If the board is accessible and you can apply power, measuring the output pin of an AMS1117-3.3 against ground with the rest of the circuit connected is a fast check. A reading of 3.25–3.35V under light load is good. A reading of 0V or the full input voltage both suggest failure.

## Failure modes

**Output stuck at input voltage (pass element shorted)**

The internal pass transistor shorts, removing all regulation and passing full input voltage directly to the output. Measuring output gives you 8–12V where you expect 5V. Any downstream logic or sensitive components on that rail will be destroyed if the supply ran in this state. A 7805 with a shorted pass element reads near-zero resistance from input to output in both directions in the resistance mode.

**Output stuck at zero (open pass element or open thermal fuse)**

The pass element opens or an internal thermal fuse blows. Output reads 0V regardless of input. On the bench, input voltage is present (confirmed by meter) but output is dead. The part is not reusable.

**Output low under load (high dropout or degraded pass element)**

The regulator holds its rated voltage at no load but drops under current. This is most obvious in LDOs that are asked to run with a small input-output differential. An AMS1117-3.3 needs about 1.3V of headroom: input must be at least 4.6V for it to regulate properly. If the input is 4.5V, output will be lower than 3.3V under any load. This is a design constraint, not always a failure, but a regulator from a board that ran this way may have heat-stressed the pass element.

**Thermal damage from inadequate heatsinking**

TO-220 regulators without heatsinks in high-dissipation positions often show a yellowed or brown board area under the package, and sometimes the plastic body is darkened near the tab. These parts may still test correctly on the bench, but their long-term reliability under continuous load is uncertain. Use them for experiments, not anything left unattended.

## Reuse notes

The 78xx and 79xx series are worth pulling in any readable condition. 7805, 7812, and 7805 equivalents appear in thousands of designs and are always useful. Pull them with the decoupling capacitors if you can, since the caps stay with the circuit role anyway.

LM317 parts are worth keeping because they're adjustable and handle up to 1.5A. Label the bag with the part number and the fact that output voltage requires external resistors; a bare LM317 without resistors will output its minimum adjustment voltage (1.25V) if the adjust pin is left floating, which can confuse testing.

AMS1117 and similar SOT-89 LDOs are worth pulling if they're from a working board. They're fragile to ESD and to reversed input voltage, and there's no way to know the stress history of a part from a failed device. From working boards, pull and label them with the output voltage from the suffix.

Don't pull switching regulator ICs without their support components. A bare MC34063 chip without the inductor, diode, timing capacitor, and feedback resistors tells you almost nothing about the original design and is difficult to reuse without rebuilding the circuit from scratch.

Derate linear regulators to 70% of rated current in a new build: a 1A-rated 7805 becomes a 700mA part. This accounts for thermal variation, age, and the fact that linear regulators get hotter as the input-output differential grows.

## Theory links

For voltage checks and understanding what the output pin should read under different loads, see [DC measurements](/open-circuits/DC/DC_5.html). For how the active devices inside a linear regulator work, see [Semiconductors](/open-circuits/Semi/SEMI_6.html).

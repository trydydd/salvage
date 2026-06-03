---
title: "Motors"
section: components
author: Claude
review: Needs Human Review
---

Motors in salvage span a wider range than most components: from a 6mm pager vibration motor running on 1.5–3V to a synchronous turntable motor that only works on AC mains. Identifying the type before you apply power is the part that matters.

## Sort the motor type

Brushed DC motors have two terminals and run on any DC voltage in a range suited to their size. Toy motors, tool motors, and small appliance motors are almost always brushed. Spin the shaft by hand: it should rotate freely with a slight magnetic cogging or detent feel as the commutator segments pass under the brushes. You can hear the brushes if you rotate the shaft slowly in a quiet space. Two wires, no defined polarity (reversing the wires reverses the direction).

Brushless DC motors have three wires, corresponding to the three phases of the stator coils. PC fans, hard drive motors, and drone motors are all brushless. The shaft spins more freely than a brushed motor because there's no brush friction. Three-wire fans (12V for standard PC fans, 5V for some smaller ones) run from their power and ground connections directly; the third wire is a tachometer output, not a phase wire. Four-wire fans add a PWM control line for speed control. Applying 12V to the power pins of a 12V brushless fan is the fastest bench test.

Stepper motors have four, five, or six wires and feel distinctly different when you spin the shaft by hand: you'll feel a series of detent positions as the rotor snaps between stable points. Bipolar steppers have four wires forming two independent coil windings. Unipolar steppers have five or six wires with a center tap on each winding. You'll pull these from 3D printers, flatbed scanners, and inkjet print carriages. They require a stepper driver to run; you can't simply apply DC to the wires.

Synchronous and induction AC motors have two wires and run on AC, not DC. Small synchronous types turn up in microwave turntable mechanisms and older clock mechanisms. Shaded-pole induction motors are common in small appliance fans and HVAC damper actuators: they have a squirrel-cage rotor and a stator with a shading coil (a copper ring around part of each pole) that creates the rotating magnetic field. Neither type will rotate on DC. If the device ran on mains voltage, the motor is rated for mains voltage: treat it with mains caution and test only with an isolated supply or leave it alone.

Universal motors also turn up frequently in salvage and look similar to brushed DC motors because they are brush-type machines. You'll find them in power tools (drills, circular saws, angle grinders), vacuum cleaners, and hair dryers. They run on mains AC or on DC, which is why they're called universal. The windings are live at mains potential when the tool is plugged in. Treat any motor from a mains-powered tool as a mains-voltage device even after removal.

## Test each family safely

**Brushed DC motors**

Measure the winding resistance between the two terminals. Toy and pager motors typically read 1–5Ω. Medium-duty motors (130-size, 260-size) typically read 3–15Ω. High-current can motors like the 775 and 550 sizes run on 12–24V and draw 10A or more at stall, so their armature resistance is often below 2Ω. Many read 0.5–1.5Ω on a meter, which is at the lower limit of a cheap DMM's accuracy. An OL reading means the winding is open or the brush contact is broken. Zero resistance means a shorted winding.

With the meter on continuity or a high resistance range, probe between each terminal and the motor can (the metal housing). You should get OL. Any low-resistance reading means the winding is shorted to the case, which is a ground fault. Don't use that motor.

For a basic spin test, connect a bench supply set to the motor's rated voltage through a 10–47Ω current-limiting resistor. The motor should spin. Without knowing the rated voltage, start at 1.5V and work up. Small toy motors run on 1.5–6V. Larger appliance motors typically run on 6–24V. When you switch the supply off, the spinning rotor generates a voltage spike back through the leads (back-EMF). If you're connecting the motor to a transistor or driver IC rather than a bench supply, fit a flyback diode across the motor terminals to protect the driver from that spike.

**Stepper motors**

Set your meter to the resistance range. On a bipolar stepper, probe each pair of adjacent wires. You're looking for pairs that read 1–20Ω: those are the two ends of one winding. If you have four wires, you should find two pairs with equal resistance. Wires from different windings should read OL to each other. For a unipolar stepper with five wires, one wire is the common (center-tap). The common reads half the end-to-end resistance of each coil when probed against any phase wire. If the coil end-to-end resistance is 10Ω, the common reads 5Ω to each phase wire. You can confirm the motor is alive by connecting two wires from one phase to a 3–12V supply briefly while holding the shaft: you'll feel or see it try to step. Also probe between any winding wire and the motor body to confirm there's no short to case: it should read OL.

**Brushless fans**

Apply rated voltage to the power and ground pins. Most 3-wire PC fans run on 12V. Some smaller fans run on 5V. You don't need to connect the tachometer or PWM pins to get the motor spinning at full speed. If the fan doesn't spin, check the voltage with the meter on the power pin while connected. A fan that draws current (supply current increases above the baseline) but doesn't spin usually has a stuck or seized bearing. A fan that draws no current has an open winding or the driver IC is failed.

**Synchronous motors from mains-rated equipment**

Don't test these on the bench without an isolated transformer or a variac. If you're not set up for that, note the voltage rating from the case or equipment label, store the motor with the rating written on a tag, and test it when you have the right setup.

## Mechanical condition

Spin the shaft by hand with no electrical connection. It should rotate with little friction and no grinding. Some gearmotors have a lot of gear reduction, so they'll feel stiff; that's the gearbox, not failed bearings. The tell is whether the stiffness is uniform or whether it catches, crunches, or has a dead spot.

Check shaft play by gripping the shaft and trying to move it sideways while it's in its normal orientation. In a motor with good sleeve bearings, there's a tiny amount of play. In one with worn bearings, you'll feel the shaft shift noticeably. More than 0.3mm of lateral play on a motor you plan to run under load means the bearing is on the way out.

In brushed motors, the brushes are accessible through small apertures on the motor can. If you can see them, check that they make contact with the commutator and aren't worn to a stub. A brushed motor that sparks heavily at low speed or runs roughly has commutator surface damage, burned-on carbon, or glazed commutator segments. Cleaning the commutator with a cotton swab and isopropyl alcohol sometimes recovers light glazing; heavy pitting or grooving won't clean up.

## Failure modes

**Open winding (brushed)**

An open winding in a brushed motor usually means either the armature winding burned through from overcurrent or the brush contact broke from spring fatigue. In resistance mode, the terminals read OL instead of the expected 1–20Ω. A brush that has worn down to the spring contact will do the same thing and may recover if you reseat the brush. Open armature windings don't recover.

**Seized bearings**

Bearings seize from age, contamination, or running dry. The shaft won't rotate freely, and the motor draws high current when powered because the rotor is fighting the friction. Small motors with sleeve bearings can sometimes be recovered by applying a drop of light machine oil to the bearing aperture at each end of the can and working the shaft back and forth. Ball-bearing motors that are seized are usually past the useful life of the bearings themselves; the balls have deformed or corroded.

**Shorted windings**

A shorted winding in a brushed motor reads lower resistance than expected: a motor that should read 5Ω reads 1.5Ω. Shorted winding turns waste energy as heat and cause the motor to run hot and lose torque. It'll still spin, but it'll draw more current than normal and get warm quickly. Don't use shorted motors in applications where they run continuously.

**Demagnetised permanent magnets**

Small brushed DC motors and BLDC motors rely on permanent magnets in the stator or rotor. Prolonged overheating or a severe overcurrent event can partially demagnetise these magnets. The winding resistance will measure fine and the bearings will feel fine, but the motor produces less torque than it should and runs faster under no load than normal for its voltage. There's no bench test that reliably catches this with a basic DMM. If a motor that should have real torque (say, a 12V drill motor) spins freely but feels weak and doesn't pull hard against your finger, suspect demagnetisation. It isn't recoverable.

**Dead brushless driver**

Many brushless fans and motors have the driver IC integrated into the motor housing. If the fan draws power but doesn't spin, and the bearing rotates freely, the driver is likely failed. The motor windings themselves are often fine, but without the driver they're not useful as a drop-in replacement.

## Reuse notes

Brushed DC motors are the most straightforward to reuse because they run on any suitable DC voltage. Small toy and pager motors are useful for light mechanical projects. 775-size and 550-size can motors from battery-powered tools and toy cars give you real torque. Label each motor with the rated voltage from the original device if you know it, and with the measured winding resistance.

Universal motors from mains-powered tools (drills, vacuum cleaners, angle grinders) physically resemble large brushed DC motors but are a different design. They'll run on DC, but their voltage ratings and winding impedances are calculated for mains frequency AC. Running one on low-voltage DC is possible for experimentation, but the speeds and currents won't match mains operation, and the brushes and commutator wear faster on DC. Treat any motor from a mains-powered appliance as a mains-voltage device even when you're bench-testing it at low voltage.

Brushless PC fans are worth pulling in any working condition. They're useful for cooling projects, and a 12V fan with a tachometer output gives you speed feedback for free. Store them by voltage (5V, 12V) and by connector type if you have a mix.

Stepper motors are worth keeping if you know the winding resistance. Write the winding resistance per phase on a label tied to the wire bundle: a motor labeled "bipolar, 12Ω per phase" is immediately usable in a new project. Steppers without labels are still usable but require the identification procedure above before wiring them to a driver.

Gearmotors should stay with their gearbox. The output shaft torque and speed are set by the gear ratio, and a motor body without its gearbox is just a motor body. Keep the whole assembly and note the output shaft RPM at rated voltage if you can measure it.

Don't keep motors with seized or heavily worn bearings unless you plan to replace the bearings. Don't keep synchronous motors from mains equipment unless you have a clear use in mind and the voltage rating is confirmed.

## Theory links

For safe low-voltage motor checks and understanding current-limited testing, see [DC measurements](/open-circuits/DC/DC_5.html). For basic motor-driving experiments that show you how to get a brushed or stepper motor moving with simple circuits, see [bench experiments](/open-circuits/Exper/EXP_3.html).

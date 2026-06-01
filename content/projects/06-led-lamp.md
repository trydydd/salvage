---
title: "LED Lamp"
section: projects
author: Claude
review: Needs Human Review
---

This project builds a working desk or bench lamp from salvaged LEDs, a heat sink, and a 12 V DC supply. The whole lamp runs from low-voltage DC: a 12 V wall-wart from a dead router or printer, or the +12 V rail of the ATX bench supply from project 3. Nothing in this build connects to mains.

The output depends on what you salvage. A 300 mm section of 12 V LED strip from a dead undercabinet fixture, mounted on the aluminum shell of a dead LED bulb, gives you a useful desk light. Twelve discrete white LEDs on stripboard with calculated series resistors give softer light at lower current. Neither matches a purpose-built lamp, but both are bright enough to work by.

One note on what won't work directly here: the round LED boards from inside dead LED bulbs are designed for series strings at 28–100 V, not 12 V. Don't try to power them from 12 V without modification. The aluminum shell and diffuser from those bulbs are worth keeping for the housing, but the LED board itself needs a different supply voltage or a shortened series string.

## Project goal

The simplest version of this lamp is three parts: a length of 12 V LED strip, something flat and metallic to stick it to for heat spreading, and a supply wire. A 12 V strip has built-in current-limiting resistors for every group of three LEDs, so there's no calculation required. You connect + and − and the strip lights up.

The discrete-LED version requires a resistor calculation for each LED or string. That calculation is covered in the layout section with a worked example. It's the right choice when you have a bag of individual LEDs from PCB salvage and no strip.

Current capacity and brightness are set by the supply. A 12 V 1 A wall-wart can power about 450 mm of typical 5050-type strip (three groups of 3 LEDs each drawing 60 mA, about six groups per 300 mm = 360 mA). Don't exceed the supply's rated current by adding more strip than the label allows.

## Parts to salvage

| Part | Where to get it |
|------|-----------------|
| LED strip, 12 V rated, any length | Dead LED light fixtures (undercabinet lighting, strip lights); not laptop backlight strips, which run at 3 V |
| Aluminum slug or shell for heat sink | LED Bulbs, body of the lamp; or any flat aluminum bracket from Desktop computers |
| Diffuser or reflector | LED Bulbs, diffuser globe; flashlights and spotlights, reflector cup |
| 12 V DC regulated wall-wart | Wall chargers, any brick marked "12 V DC"; Routers and modems, the external brick |
| Hookup wire, 20–22 AWG, two colours | Any low-voltage PCB wiring |
| SPST switch | Battery devices, board edge; any dead appliance front panel |
| White through-hole LEDs, 20–30 mA rated (if using discrete route) | Battery devices, front panel; Desktop computers, front-panel board |
| Through-hole resistors, 470 Ω–820 Ω (value from calculation) | Desktop computers, motherboard; Routers and modems, main PCB |

Buy new thermal adhesive tape if the LED strip's own backing has given up, which it does on cheap strips after a few heat cycles. A 10 mm wide strip of the double-sided thermal type keeps the LEDs firmly bonded to the heat sink.

## Mechanical and electrical layout

**Strip route (fastest):**

A 12 V strip has the resistors built in. Every group of three LEDs shares one series resistor. The strip can be cut at the marked intervals between groups (every 50 mm on most 5050 strips, every 25 mm on denser types). Cut in the middle of the copper pad between groups, which leaves a solderable pad at each cut end.

1. Choose a length. At about 60 mA per group, a 300 mm strip draws around 360 mA at 12 V. Three hundred millimetres gives a readable pool of light about 200 mm wide.
2. Press the strip to your heat sink, adhesive backing down. The aluminum slug from an LED bulb is ideal: it's flat on one face, already sized for a lamp footprint, and has some mass to absorb heat. Without a metal backing, the strip surface reaches 60–70°C under prolonged use and the LEDs lose output over months.
3. Solder a short hookup wire to the + and − copper pads at the supply end of the strip. The + and − markings are printed between pads on most strips.
4. Run the positive wire through your switch and then to the supply positive. Connect the negative wire to supply negative.

That's the minimum build. For a desk lamp, mount the aluminum slug to the arm of a dead lamp using the slug's existing threading or a bracket, aimed at the desk. A dab of epoxy on an arm that has no threading is enough for the weight.

**Discrete LED route:**

This uses individual through-hole LEDs wired in parallel branches, each branch containing one LED and its own series resistor. Calculate the resistor value for each LED type.

The formula: R = (V\_supply − V\_f) / I\_target

For white LEDs with a forward voltage of 3.2 V at 15 mA:

R = (12 − 3.2) / 0.015 = 587 Ω → use 560 Ω (standard value) or 620 Ω

Measure the actual forward voltage of your LEDs with a multimeter on diode mode. The reading in volts is V\_f. If your LEDs measure 3.0 V, R = (12 − 3.0) / 0.015 = 600 Ω → use 560 Ω or 620 Ω. If they measure 3.4 V, R = (12 − 3.4) / 0.015 = 573 Ω → same result.

For a twelve-LED array at 15 mA each, total current draw is 180 mA. That fits comfortably within a 12 V 500 mA supply.

1. Lay out the LEDs on a piece of stripboard, spacing them as needed for your beam pattern. Typically, space LEDs 20–30 mm apart for even coverage.
2. Solder each LED in series with its calculated resistor. Each LED's anode (longer leg) connects to the +12 V row through the resistor. Each LED's cathode (shorter leg) connects to the GND row.
3. Check each branch with a continuity tester before connecting to the supply.

The discrete route produces a gentler light than a dense strip and lets you aim individual LEDs if you're mounting them in a reflector cup.

**Heat check after ten minutes:**

Feel the heat sink after running the lamp for ten minutes. Comfortably warm (around 40–50°C) is fine. Too hot to hold means the strip current is too high for the aluminum you've provided, or the adhesive is insulating rather than conducting. Use a larger piece of aluminum or reduce the strip to fewer groups.

## Testing and use

1. Before connecting the supply, check polarity at the LED connections: + to strip positive (or LED anodes), − to strip negative (or LED cathodes). On the discrete build, a reversed 12 V supply puts the full voltage in reverse across each LED. Most LEDs have a reverse breakdown voltage around 5 V, so the check matters. On the strip build, three LEDs in series raise the combined breakdown threshold close to 12 V, so the risk is lower, but check before connecting either way.
2. Connect the supply and switch on. All sections of the strip should light uniformly. A dark segment in a 12 V strip means that three-LED group is open (usually a failed LED or a cold solder joint at the pad). A dark individual LED in the discrete build means that branch is open.
3. If nothing lights: measure the supply output at the switch (12 V expected), then measure across the LED connections with the switch on. Zero voltage there means the switch or a wire is open. Correct polarity but no light means check the LED orientation.
4. After ten minutes, run the heat check as described above.

In normal use, the switch in the DC circuit gives you on/off without unplugging. The supply can stay plugged in. Twelve volts DC at the switch is safe to operate by hand.

## Theory links and variations

For LED forward voltage, series resistors, and the circuit behind each branch, the [experiments](/open-circuits/Exper/EXP_2.html) chapter covers this circuit in worked form.

For checking LED polarity and measuring forward voltage with your meter, see [DC measurements](/open-circuits/DC/DC_5.html).

Add a PWM dimmer module in series with the positive supply lead to get adjustable brightness. Small DC PWM modules appear in dead LED fixtures and LED controllers salvaged from desktop computer fans. Try warm-white strips from dead LED light fixtures alongside cool-white strips for a tunable color temperature by adjusting which rails are switched on. Mount the lamp head on the gooseneck arm of a dead desk lamp whose own LED has failed. These often have a 12 V adapter still attached that can power the replacement strip. Wire two strips in parallel from the same supply if you've confirmed the supply's current rating covers the load.

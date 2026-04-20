# Technical Review: Relays

## Critical Errors

1. Wrong meter mode for coil identification
    Found:   "Set your meter to the 200mA current range."
    Fix:     "Set your meter to resistance mode (the 2kΩ range works well)."
    Reason:  Coil resistance is measured in ohms; putting the meter in current mode would damage the meter and give no useful reading.

2. 5 V relay coil resistance range is wrong
    Found:   "For 5V relays, coil resistance runs 10–30Ω."
    Fix:     "For 5V relays, coil resistance runs 50–150Ω."
    Reason:  10–30Ω is far below the calibrated 5 V coil resistance window of 50–150Ω; a reader using this range would incorrectly reject good relays or accept shorted coils.

## Fact-Check Items

3. Inductive kick voltage magnitude
    Claim:   "The inductive kick when the coil turns off can reach 50–100V in a 12V relay coil"
    Concern: Inductive flyback spikes from relay coils can exceed 100 V depending on coil inductance and circuit impedance; 50–100 V may understate the worst case for unprotected coils.
    Source:  Relay coil inductance specs in SRD-05VDC or G5V-2 datasheets; /open-circuits/DC/DC_5.html for inductive transient background.

4. Relay pull-in time range
    Claim:   "the armature should pull in within about 10–20ms"
    Concern: Most small PCB relays spec pull-in times of 3–10ms; 10–20ms is at or above the typical upper limit and may flag good relays as slow.
    Source:  Omron G5V-2 datasheet (operate time), Songle SRD datasheet — check the "operate time" row.

5. Post-cleaning contact resistance threshold
    Claim:   "If the reading drops to under 0.2Ω after that, the contacts are usable."
    Concern: The document states clean contacts read under 0.1Ω; accepting 0.2Ω after cleaning as "usable" doubles that threshold without explanation. May be too permissive for any load above a few amps.
    Source:  IEC 61810-1 contact resistance limits; relay datasheets typically list max contact resistance of 100mΩ (0.1Ω).

6. Resistive-load derating percentage for salvaged relays
    Claim:   "Derate the contact current rating to 75% for salvaged relays used with resistive loads"
    Concern: 75% derating for resistive loads on an unknown-history relay may still be too generous; some sources recommend 50% for any salvaged contact with unknown switching history.
    Source:  IEC 61810-1 §8 (endurance ratings); Omron relay application notes on contact derating for unknown service history.

## Clean

- Read the case markings: No issues found. Contact form codes, part number decoding, and AC coil note are all accurate.
- Normally open and normally closed contacts: No issues found.
- Click test and contact condition (general): No issues found. Flyback diode polarity and 1N4148/1N4001 guidance are correct.
- Contact resistance check (clean threshold): No issues found for the 0.1Ω / 0.5Ω thresholds themselves.
- Failure modes — Open coil, Welded contacts, Burned and pitted contacts, Stiff or stuck armature: No issues found beyond the implied dependency on the corrected 5 V coil range.
- Reuse notes (general): No issues found. Label and storage guidance is sensible.
- Theory links: No issues found. Paths are valid absolute /open-circuits/... links.

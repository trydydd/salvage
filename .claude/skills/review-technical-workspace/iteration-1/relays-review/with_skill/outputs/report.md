# Technical Review: Relays

## Critical Errors

1. Wrong meter mode for coil identification
    Found:   "Set your meter to the 200mA current range."
    Fix:     "Set your meter to resistance mode (200Ω or 2kΩ range)."
    Reason:  Coil resistance is measured in Ω mode; the current range routes the signal through the meter's low-resistance shunt, which will read near zero and may damage the meter if the coil is connected to any residual voltage.

2. 5V coil resistance range is too low
    Found:   "For 5V relays, coil resistance runs 10–30Ω."
    Fix:     "For 5V relays, coil resistance runs 50–150Ω."
    Reason:  A 5V relay coil at 10–30Ω would draw 167–500mA, far above the 20–80mA typical for PCB relay coils; the correct range for 5V coils is 50–150Ω, consistent with standard coil power budgets.

## Fact-Check Items

3. Inductive kickback voltage range
    Claim:   "The inductive kick when the coil turns off can reach 50–100V in a 12V relay coil"
    Concern: For a 12V PCB relay coil with moderate inductance switched without snubbing, the back-EMF spike can realistically exceed 100V — figures of 100–300V are commonly cited in application notes. 50–100V may understate the hazard and lead readers to choose inadequate protection.
    Source:  Check relay manufacturer application notes (e.g. Omron G5V, Panasonic TQ series); measure peak spike directly with an oscilloscope on a representative coil to establish a more defensible upper bound.

4. 1N4001 recommendation for coils above 100mA
    Claim:   "A 1N4001 or higher for anything with a coil above 100mA."
    Concern: The 1N4001 has a peak inverse voltage (PIV) rating of only 50V. If the inductive kickback spike can exceed 50V (see item 3), the 1N4001 may avalanche or fail, making the 1N4002 (100V) or 1N4007 (1000V) safer general recommendations. "1N4001 or higher" implies the reader should step up to 1N4002/4003/etc., but a reader unfamiliar with the series may not understand the "or higher" caveat.
    Source:  1N400x series datasheet (Vishay or ON Semi); cross-check against the spike voltage established in item 3 to confirm minimum required PIV.

## Clean

- Read the case markings: No issues found. Coil voltages, AC coil note, contact form codes, part number decode, and brand examples are all accurate.
- Click test and contact condition (pull-in timing, contact check procedure, cycling method): No issues found.
- Failure modes (open coil, welded contacts, burned contacts, stiff armature): Root causes and diagnostic procedures are accurate.
- Reuse notes (derating percentages, storage advice, reuse criteria): No issues found.
- Theory links: Correct absolute path format; link targets are appropriate to the referenced content.

---

**Apply fixes:** enter `all`, a comma-separated list of IDs (e.g. `1,3`), `interactive` to step through one at a time, or `skip`.

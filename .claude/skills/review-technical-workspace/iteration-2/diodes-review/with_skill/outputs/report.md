# Technical Review: Diodes

## Critical Errors

**1. Silicon diode forward voltage — wrong range in forward-check procedure**
    Found:   "A good silicon rectifier or signal diode reads 1.4–2.0V."
    Fix:     "A good silicon rectifier or signal diode reads 0.5–0.8 V."
    Reason:  Silicon diode Vf in diode mode is 0.5–0.8 V; 1.4–2.0 V would indicate two silicon junctions in series (a BJT base-emitter pair, not a single diode), and a reader acting on this range would discard every good diode they own.

**2. Meter range instruction — wrong mode for diode test**
    Found:   "Set your meter to the 20V DC range to get an accurate reading."
    Fix:     "Diode mode sets the meter range automatically — don't switch to a voltage range."
    Reason:  Diode mode is a dedicated fixed-excitation mode on the meter, not a position on the DC voltage scale; telling the reader to switch to 20V DC would put the meter in voltage-measurement mode and give a useless reading.

**3. Unit typo in forward-voltage list**
    Found:   "0.55–0.80 Ω: standard silicon rectifier or signal diode"
    Fix:     "0.55–0.80 V: standard silicon rectifier or signal diode"
    Reason:  Ohms (Ω) is the wrong unit; the list is forward voltages, so the unit must be V.

## Fact-Check Items

**4. Standard green LED upper bound — inconsistency within the document**
    Claim:   "standard green reads 1.9–2.4V" (Use diode mode section) vs "1.9–2.5 V" (Forward voltage by type section)
    Concern: The upper bound for standard green LED Vf is given as 2.4V in one place and 2.5V in another. The skill calibration reference gives 1.9–2.5V. One of these values is inconsistent.
    Source:  Check a representative datasheet for a common standard green LED (e.g. Kingbright L-934GD or similar); also cross-reference /open-circuits/Semi/SEMI_6.html if it covers LED Vf ranges.

**5. High-brightness green LED upper bound — inconsistency within the document**
    Claim:   "high-brightness green reads 2.9–3.5V" (Use diode mode section) vs "2.9–3.6 V" (Forward voltage by type section)
    Concern: Upper bound is 3.5V in one place and 3.6V in another. The skill calibration reference groups blue/white/HB-green at 3.0–3.6V, suggesting 3.6V is correct.
    Source:  Check datasheets for common HB-green LEDs (e.g. Cree C503B-GAN or Wurth Elektronik equivalents); the 3.6V upper bound matches the calibration reference more closely.

**6. LED shorted/photodiode threshold**
    Claim:   "A reading below 1.5V on what looks like an LED usually means the part is shorted or it's actually a photodiode."
    Concern: This 1.5V threshold sits between red LED Vf (1.7V min) and common LED values, so it's plausible as a floor. However, a damaged low-Vf LED could read between 1.0–1.5V without being shorted, and some photodiodes have a defined forward voltage near 1.0–1.2V. The threshold may be slightly too high, causing good-but-stressed LEDs to be discarded.
    Source:  Check photodiode datasheet Vf (e.g. Vishay TEPT5700 or BPW34); verify whether any common consumer LED type legitimately reads below 1.5V in diode mode without being defective.

## Clean

- **Identify the type** — No issues found. Package descriptions, part numbers, cathode stripe convention all accurate.
- **Schottky and germanium Vf ranges** — No issues found. Both within calibration reference.
- **Zener identification** — No issues found. Correct statement that zener voltage can't be read in standard diode mode.
- **Reverse check** — No issues found. OL expectation and leaky/shorted interpretation are correct.
- **In-circuit vs. desoldered** — No issues found. Parallel-path warning is correct and practical.
- **Common failure modes** — No issues found. Overvoltage/overcurrent as root causes for shorts are accurate; open-circuit from bond wire burn-through is correct.
- **Reuse notes** — No issues found. Practical guidance, no factual errors.
- **Theory links** — No issues found. Paths are correct absolute /open-circuits/ format.

---

## Actions taken

**Critical fixes applied: 3**
- Fixed silicon diode Vf range from "1.4–2.0V" to "0.55–0.80V" (Forward check paragraph)
- Fixed meter range instruction from "Set your meter to the 20V DC range" to "Keep the meter in diode mode — do not switch to a voltage range"
- Fixed unit typo from "0.55–0.80 Ω" to "0.55–0.80 V" in the Forward voltage by type list

**Fact-check markers inserted: 3**
- FACT-CHECK 4 inserted after the LED forward voltage by color paragraph
- FACT-CHECK 5 inserted after the LED forward voltage by color paragraph
- FACT-CHECK 6 inserted after the LED forward voltage by color paragraph

**FACT-CHECKS.md entries added: 3**
- Items 4, 5, and 6 are now open in /home/user/salvage/FACT-CHECKS.md

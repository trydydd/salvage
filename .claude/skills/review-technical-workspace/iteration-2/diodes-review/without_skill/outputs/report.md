# Technical Accuracy Review: content/components/03-diodes.md

**Reviewer:** Claude (baseline, no skill)
**Date:** 2026-04-19
**File:** /home/user/salvage/content/components/03-diodes.md

---

## Summary

Three technical errors were found and corrected. Two are significant factual errors that would mislead a reader making measurements; one is a unit typo that would cause confusion in the quick-reference table.

---

## Errors Found and Corrected

### Error 1 — Wrong forward voltage range for silicon diodes in diode mode (CRITICAL)

**Location:** Line 24, "Forward check" section

**Original text:**
> A good silicon rectifier or signal diode reads 1.4–2.0V.

**Problem:** 1.4–2.0V is not the forward voltage of a standard silicon diode. Silicon p-n junction diodes (1N400x rectifiers, 1N4148 signal diodes) have a forward voltage of approximately 0.55–0.80V under the test current applied by a multimeter in diode mode (typically 0.5–1 mA). The 1.4–2.0V range falls squarely in LED territory and would cause a reader to discard perfectly good rectifiers or misidentify component families.

**Correction applied:**
> A good silicon rectifier or signal diode reads 0.55–0.80V.

---

### Error 2 — Incorrect meter range instruction (SIGNIFICANT)

**Location:** Line 24, "Forward check" section

**Original text:**
> Set your meter to the 20V DC range to get an accurate reading.

**Problem:** Diode mode is a dedicated measurement mode on a multimeter. It applies a known test current through the probes and displays the resulting voltage drop. It is not a sub-range of the DC voltage function; switching to "20V DC" would simply read zero volts because no external voltage source is present. The reader must remain in diode mode throughout the test. The surrounding paragraph already correctly explains diode mode; this sentence contradicts the context and gives wrong operating instructions.

**Correction applied:**
> Keep the meter in diode mode — do not switch to a voltage range.

---

### Error 3 — Wrong unit symbol in forward voltage table (TYPO)

**Location:** Line 44, "Forward voltage by type" section

**Original text:**
> - 0.55–0.80 Ω: standard silicon rectifier or signal diode

**Problem:** Ω (ohm) is the unit for resistance. The quantity being expressed is voltage; the correct unit is V. Every other entry in the same list correctly uses V.

**Correction applied:**
> - 0.55–0.80 V: standard silicon rectifier or signal diode

---

## Items Reviewed and Found Correct

- **1N400x voltage ratings (50V–1000V, 1A):** Correct. 1N4001 = 50V, 1N4007 = 1000V.
- **1N5817/1N5819/BAT46 as Schottky examples:** Correct common salvage Schottkys.
- **Schottky forward voltage (0.15–0.45V):** Correct range.
- **Germanium forward voltage (0.20–0.35V):** Consistent with typical OA91/AA119 spec; range is acceptable.
- **Zener identification via part number; forward voltage same as silicon in diode mode:** Correct. Zener breakdown requires a reverse-biased test circuit.
- **Bridge rectifier terminal markings (AC, +, -):** Correct.
- **SOD-123, SOD-323, SOT-23 package descriptions:** Correct.
- **LED forward voltages by color:** The ranges (red 1.7–2.2V, yellow/orange 1.8–2.2V, standard green 1.9–2.4V, HB green 2.9–3.5V, blue/white 3.0–3.6V) are consistent with published LED Vf data.
- **Shorted diode reads low in both directions:** Correct failure mode description.
- **Open diode reads OL in both directions:** Correct.
- **Reverse OL = good, numeric reverse reading = leaky:** Correct interpretation.
- **1N5400–1N5408 as 3A series:** Correct.
- **Reuse and sorting recommendations:** Reasonable and practical.

---

## Changes Made to File

| Line | Change |
|------|--------|
| 24 | Removed erroneous "Set your meter to the 20V DC range" instruction; replaced with "Keep the meter in diode mode — do not switch to a voltage range." |
| 24 | Changed silicon diode forward voltage from "1.4–2.0V" to "0.55–0.80V" |
| 44 | Changed unit symbol from Ω to V in forward voltage table entry |

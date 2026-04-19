# Technical Accuracy Review: Diodes Component Page

**File reviewed:** `/home/user/salvage/content/components/03-diodes.md`

---

## Errors Found

### Error 1 — Wrong meter mode instruction (Line 24, "Forward check" section)

**Quoted text:** "Set your meter to the 20V DC range to get an accurate reading."

**Problem:** This instruction is incorrect and contradicts the setup described just four lines earlier, which correctly tells the reader to set the meter to diode mode (the diode symbol). Diode mode is a dedicated meter function — the meter applies its own test voltage internally and displays the forward voltage drop directly. There is no separate DC voltage range to select. Following this instruction would switch the meter *out* of diode mode and into a voltage measurement range, which would not test the diode at all.

**Correct guidance:** When using diode mode, no additional range selection is required. The reader should remain in diode mode as set in the preceding paragraph.

---

### Error 2 — Wrong forward voltage range for silicon diodes (Line 24, "Forward check" section)

**Quoted text:** "A good silicon rectifier or signal diode reads 1.4–2.0V."

**Problem:** This voltage range is wrong by roughly a factor of two. Standard silicon rectifier diodes (1N400x series) and signal diodes (1N4148) have a forward voltage of approximately 0.55–0.75V under typical test conditions — commonly cited as about 0.6–0.7V. A reading of 1.4–2.0V describes LEDs, not silicon rectifiers. A reader following this guide would conclude that every normal silicon diode they test is defective, and might discard good parts or accept bad ones.

This error is compounded by the fact that the "Forward voltage by type" table on line 44 correctly lists silicon rectifiers at 0.55–0.80V, creating a direct internal contradiction in the document.

**Correct range:** 0.55–0.75V (commonly 0.6–0.7V) for standard silicon rectifiers and signal diodes.

---

### Error 3 — Wrong unit symbol (Line 44, "Forward voltage by type" section)

**Quoted text:** "0.55–0.80 Ω: standard silicon rectifier or signal diode"

**Problem:** The unit is listed as ohms (Ω) instead of volts (V). Forward voltage is measured in volts; ohms is a unit of resistance and is not what diode mode displays. This appears to be a copy/paste or formatting error, but it is a factual unit error nonetheless.

**Correct unit:** V (volts). The line should read "0.55–0.80 V: standard silicon rectifier or signal diode".

---

## Items Verified as Correct

The following technical claims were checked and are accurate:

- 1N4001–1N4007 voltage ratings (50V to 1000V) and current rating (1A) are correct.
- Schottky forward voltage range (0.15–0.45V) is reasonable for common salvage Schottkys.
- Germanium diode forward voltage (0.20–0.35V) is correct.
- LED forward voltage ranges by color are accurate (red/IR 1.7–2.2V, yellow/orange 1.8–2.2V, green 1.9–2.4V / high-brightness 2.9–3.5V, blue/white 3.0–3.6V).
- Zener behavior in diode mode (reads normal silicon forward voltage; cannot identify zener voltage without reverse-biasing test circuit) is correct.
- OL (over-limit) in reverse indicating a good diode is correct.
- Shorted diode reading low voltage in both directions is correct.
- Open diode reading OL in both directions is correct.
- Package descriptions (DO-35, DO-41, SOD-123, SOD-323, SOT-23) are accurate.
- The cathode stripe convention is correct.
- Parallel circuit paths can affect in-circuit diode readings — correct.
- Bridge rectifier terminal labeling (AC, +, –) is correct.

---

## Summary

Three errors found: one contradictory and incorrect meter instruction (line 24), one seriously wrong forward voltage value for silicon diodes (line 24), and one wrong unit symbol (line 44). The silicon forward voltage error is the most consequential because it directly contradicts established component specifications and would cause readers to misidentify good silicon diodes as defective.

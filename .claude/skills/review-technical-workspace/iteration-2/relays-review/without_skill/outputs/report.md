# Technical Review: content/components/08-relays.md

## Review Date
2026-04-19

## Summary
Two technical errors were found and corrected. The rest of the document is accurate.

---

## Errors Found and Corrected

### Error 1 — Wrong meter mode for coil identification (Line 22)

**Original:**
> Set your meter to the 200mA current range.

**Problem:** The 200mA current range is used for measuring current flow, not resistance. Probing relay pins with the meter set to current mode would give nonsensical readings and could damage the meter. The procedure described — probing pairs of pins to find a consistent resistance — requires the meter to be in resistance/ohms mode.

**Correction applied:**
> Set your meter to resistance (ohms) mode.

---

### Error 2 — Wrong coil resistance range for 5V relays (Line 22)

**Original:**
> For 5V relays, coil resistance runs 10–30Ω.

**Problem:** A 5V relay coil with 10–30Ω resistance would draw 167–500mA and dissipate 0.8–2.5W — far beyond what any small PCB relay coil is designed for. Actual 5V PCB relay coils (e.g., Songle SRD-05VDC-SL-C, Omron G5LE, HLS8, TE V23079) measure approximately 70–200Ω, corresponding to coil currents of 25–70mA and coil power of 125–350mW. The stated 10–30Ω range is physically implausible for any relay intended for PCB mounting.

The same section correctly states that the coil resistance range to probe for is 50–1000Ω, which is internally inconsistent with the 10–30Ω figure. The failure-modes section (line 46) also states "you'd expect 70–1200Ω," which is more accurate.

**Correction applied:**
> For 5V relays, coil resistance runs 70–200Ω.

---

## Items Verified as Correct

- SPDT/DPDT contact form descriptions and form codes (1C, 2C, 1A) are accurate.
- Part number decoding example (SRD-05VDC-SL-C) is correct.
- Flyback diode orientation (anode to negative coil pin, cathode to positive) is correct.
- Back-EMF estimate of 50–100V for a 12V relay coil without protection is plausible.
- Contact resistance thresholds (<0.1Ω good, >0.5Ω suspect) are accurate.
- Pull-in time of ~10–20ms is accurate for typical PCB relays.
- Description of welded contacts behavior is accurate.
- Derating guidance (75% resistive, 50% inductive) is conservative and sound.
- 12V coil resistance range (200–400Ω) is correct.
- 24V coil resistance range (600–1200Ω) is correct.
- Storage and labeling advice is correct.

---

## Corrections Applied

Both corrections were applied directly to the file. No other changes were made.

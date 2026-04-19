# Technical Review: 08-relays.md

Reviewer: Claude (without skill)
Date: 2026-04-19

---

## Summary

The page is broadly accurate and practical. Most guidance is sound. There are
two clear technical errors and one piece of guidance that is unsafe or
misleading. Several minor inaccuracies are also noted.

---

## Errors Found

### 1. WRONG METER MODE — Coil identification (Critical / Misleading)

**Location:** "Identifying coil and contact pins" section

**What the page says:**
> Set your meter to the 200mA current range. Probe between each pair of pins
> until you find two that read a consistent resistance of 50–1000Ω.

**Error:** You cannot read resistance on a current (mA) range. The 200mA range
is for measuring current (amperes), not resistance. The instruction should say
to set the meter to **resistance mode (Ω)**, not the 200mA current range. Using
the current range on a relay coil pin with no external driving voltage will
yield no useful reading and could damage the meter if there is any residual
voltage on the circuit.

**Correction:** "Set your meter to resistance mode (Ω)."

---

### 2. WRONG COIL RESISTANCE RANGE for 5V relays (Significant)

**Location:** "Identifying coil and contact pins" section

**What the page says:**
> For 5V relays, coil resistance runs 10–30Ω.

**Error:** This range is too low and inconsistent with real-world 5V PCB relays.
At 10Ω, P = V²/R = 5²/10 = 2.5W — far too hot for a small PCB relay. At 30Ω,
that is ~830mW — still very high. Typical 5V PCB relay coil resistances run in
the range of approximately 70–150Ω. The SRD-05VDC-SL-C, cited by name in the
same page, has a coil resistance of ~89Ω, drawing ~56mA at 5V.

The overall range given (50–1000Ω) in the same sentence is a more defensible
broad heuristic, but the per-voltage breakdown is wrong for 5V.

**Correction:** For 5V relays, expect approximately 50–200Ω. For 12V, 200–500Ω.
For 24V, 600–1500Ω.

---

### 3. FLYBACK DIODE ORIENTATION — Safety gap (Minor/Safety)

**Location:** "Click test and contact condition" section

**What the page says:**
> put a flyback diode across the coil pins (anode to the negative coil pin,
> cathode to the positive coil pin)

**Issue:** The orientation described is correct for a known polarity coil — the
diode is reverse-biased during normal operation and conducts the back-EMF spike
at turnoff. However, the guidance assumes the reader already knows which coil
pin is positive when probing an unmarked relay for the first time. Installing a
polarized diode (1N4148, 1N400x) backwards would short the supply through the
diode. The text should note that coil polarity must be confirmed before
installing a polarized diode, or suggest using a bidirectional TVS/snubber if
polarity is unknown.

---

### 4. INDUCTIVE KICK VOLTAGE ESTIMATE — Minor understatement

**Location:** "Click test and contact condition" section

**What the page says:**
> The inductive kick when the coil turns off can reach 50–100V in a 12V relay
> coil

**Issue:** Spikes above 100V are common, especially when driving the coil
through a transistor with a fast turn-off. The range "50–100V" understates the
upper bound. "50–200V or higher" would be more accurate and better conveys the
risk. Not a critical error, but the page uses this to justify using a flyback
diode, so understatement matters.

---

### 5. OPEN COIL RESISTANCE RANGE — Internal inconsistency

**Location:** "Failure modes / Open coil" section

**What the page says:**
> In resistance mode, an open coil reads OL where you'd expect 70–1200Ω.

**Note:** This range (70–1200Ω) is more realistic than the 5V coil range of
10–30Ω given in the identification section. The inconsistency between the two
values in the same document is additional evidence that the voltage-to-resistance
table in item 2 is wrong, not this sentence.

---

### 6. CONTACT RESISTANCE THRESHOLD — Minor / Defensible

**Location:** "Contact resistance check" section

**What the page says:**
> the closed contacts should read under 0.1Ω ... If the reading drops to under
> 0.2Ω after that, the contacts are usable.

**Note:** 0.1Ω as a pass threshold is slightly strict but reasonable. Accepting
0.2Ω after cycling is arguably permissive for high-current or mains-switching
applications where contact heating under rated load becomes a concern. Not a
clear error, but worth a caveat like "acceptable for low-current signal use only."

---

## Items That Are Correct

- Form code descriptions (1C, 1CO, 2C, SPDT, DPDT, 1A) are accurate.
- Part number decoding examples (SRD-05VDC-SL-C, G5V-2-H1-12VDC) are correct.
- Common coil voltages for consumer equipment (5V, 12V, 24V) are correct.
- Contact current ratings listed (5A, 10A, 15A, 30A for power; 0.5A–1A signal) are realistic.
- Normally-open and normally-closed behavior descriptions are accurate.
- Welded contact failure mode description is technically accurate.
- Derating guidance (75% resistive, 50% inductive) is reasonable salvage practice.
- Storage guidance is practical and accurate.
- 1N4148 for signal relays / 1N4001+ for higher coil current guidance is correct.
- 10–20ms pull-in time is reasonable for typical PCB relays.
- Contact cycling to clean mild oxidation is a legitimate technique.

---

## Priority Summary

| # | Location | Severity | Issue |
|---|----------|----------|-------|
| 1 | Coil ID section | Critical | Wrong meter mode: "200mA current range" should be resistance (Ω) mode |
| 2 | Coil ID section | Significant | 5V coil resistance 10–30Ω is too low; typical range is ~70–150Ω |
| 3 | Click test section | Minor/Safety | Flyback diode polarity guidance unsafe if coil polarity is unknown |
| 4 | Click test section | Minor | Inductive kick range 50–100V understates possible upper bound |
| 5 | Failure modes | Note | OL expected range (70–1200Ω) inconsistent with but more correct than the 5V figure in item 2 |
| 6 | Contact resistance | Minor | 0.2Ω post-cycling acceptance may be permissive for high-current use |

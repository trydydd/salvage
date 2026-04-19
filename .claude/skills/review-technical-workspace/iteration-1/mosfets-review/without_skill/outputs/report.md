# Technical Review: 05-mosfets.md

Reviewed by: Claude (without skill file)
Date: 2026-04-19

---

## Summary

The page is generally well-written and practically useful. However, two critical
body diode direction errors were found that would cause a reader following the
test procedure to get wrong results, plus two minor issues.

---

## Errors Found

### 1. CRITICAL — N-channel body diode polarity stated backwards (line 24)

**The text says:**
> On an N-channel MOSFET, the body diode runs from drain to source with the
> anode at the drain.

**What is correct:**
The body diode of an N-channel MOSFET has its **anode at the source** and its
**cathode at the drain**. The body diode is formed between the P-body region
(source side, anode) and the N-drain (cathode). Current through the body diode
flows from source toward drain (source = anode, drain = cathode).

The probe assignment that follows ("red probe on drain, black probe on source
reads the forward voltage") is therefore also wrong: with a correctly oriented
body diode, the forward drop reads with **red on source, black on drain**.

A reader who follows these instructions will probe drain (+) and source (-),
which reverse-biases the body diode and reads OL. They will conclude the device
is bad or that they've identified the wrong pin pair.

**Correction:**
- N-channel body diode: anode at source, cathode at drain.
- Forward-biased reading in diode mode: red probe on source, black on drain.
- The pin with the red probe is the **source**; the pin with the black probe is
  the **drain**.

---

### 2. CRITICAL — P-channel body diode described incorrectly (line 30)

**The text says:**
> The P-channel body diode runs in the opposite direction: anode at drain,
> cathode at source.

**What is correct:**
Both N-channel and P-channel MOSFETs have their body diode in the same
orientation relative to device terminals: **anode at source, cathode at drain**.
The difference between the channel types is the direction of normal drain
current flow and where the source is connected in the circuit, not the polarity
of the body diode.

Stating "anode at drain" for a P-channel device is incorrect. It would imply
the diode conducts when the drain is positive relative to the source, which is
the wrong direction for a P-channel body diode.

**Correction:**
- P-channel body diode: anode at source, cathode at drain (same as N-channel).
- In diode mode: red probe on source, black on drain reads the forward drop for
  both channel types. The circuit context differs (P-channel source is normally
  at positive supply), but the diode's terminal polarity is the same.

---

### 3. MINOR — Gate discharge path incorrectly described (line 38)

**The text says:**
> touch the source and drain leads together briefly to discharge the gate
> through the body diode path.

**Issue:**
The body diode connects source to drain and does not involve the gate terminal.
Shorting source to drain does not discharge the gate capacitance. The gate
oxide capacitor (C_gs and C_gd) is discharged by shorting the **gate to
source** (or gate to drain), not source to drain.

Shorting source-to-drain before handling is sensible practice (it prevents
current flow through the body diode if the drain node floats high), but it does
not itself bleed gate charge.

**Correction:**
To discharge the gate, briefly short the **gate and source** leads. This drains
the gate oxide capacitance. Shorting source-to-drain is also harmless and good
handling practice but does not discharge the gate.

---

### 4. INFO — IRF3205 current rating is the 25 °C case figure (line 64)

**The text says:**
> IRF3205 (55V, 110A)

The 110 A figure is technically the datasheet continuous rating at 25 °C case
temperature. At a more realistic 100 °C case temperature the continuous rating
is approximately 78 A. This is not wrong, but a reader may be misled into
treating 110 A as an achievable continuous current under typical conditions.

No correction strictly required, but worth a parenthetical note.

---

## Items Verified as Correct

- TO-220 tab = drain; remove mounting screw before desoldering — correct.
- D-PAK exposed pad = drain for thermal path — correct.
- IRF part number conventions (9 = P-channel, trailing P = P-channel) — correct.
- MOSFET in diode mode reads OL gate-to-source vs. BJT junction forward voltage — correct.
- Shorted drain-source reads 0.05–0.2 V in both directions as failure indicator — correct.
- ESD gate oxide damage description — correct.
- Logic-level threshold 3.3–5 V vs. standard 8–12 V — correct.
- Bench test circuit (resistor in series, 3–5 V supply for logic-level) — correct and safe.
- Derating salvaged parts to 60% current — conservative and appropriate.
- IRF540 100V/28A, IRF9540 100V/19A, STP75NF75 75V/75A — all correct.
- Storage in antistatic foam with all leads shorted — correct.

---

## Priority Summary

| # | Severity | Line | Issue |
|---|----------|------|-------|
| 1 | CRITICAL | 24 | N-channel body diode: anode stated at drain, should be at source; probe assignments consequently inverted |
| 2 | CRITICAL | 30 | P-channel body diode: "anode at drain" is wrong; anode is at source for both channel types |
| 3 | MINOR | 38 | Gate discharge path: shorting source-to-drain does not discharge the gate; gate-to-source short is needed |
| 4 | INFO | 64 | IRF3205 110 A is the 25 °C case spec; could note this is a best-case figure |

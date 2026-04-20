# Technical Review: 05-mosfets.md

**Reviewer:** Claude (baseline, no skill)
**Date:** 2026-04-19
**File:** /home/user/salvage/content/components/05-mosfets.md

---

## Summary

Two confirmed technical errors found and corrected. The rest of the content — package descriptions, part number conventions, spec values, gate behavior, damage patterns, and storage advice — is accurate.

---

## Errors Found and Corrected

### Error 1 — N-channel body diode polarity reversed (Major)

**Location:** "Body diode test" section, "Finding the body diode" paragraph

**Original text:**
> On an N-channel MOSFET, the body diode runs from drain to source with the anode at the drain. [...] The pin with the red probe is the drain; the pin with the black probe is the source.

**Problem:** The body diode in a discrete N-channel MOSFET is formed by the P-type body (bulk) connected to the source terminal and the N+ drain diffusion. This makes a P-N junction with the anode at the source and the cathode at the drain. The body diode therefore conducts in the source-to-drain direction. With a DMM in diode mode, forward bias is obtained by placing the red (positive) probe on the source and the black (negative) probe on the drain — not the reverse. The original text had both the anatomical description and the probe-to-pin assignment backwards.

**Correction applied:**
- Changed "anode at the drain" to "anode at the source"
- Changed "runs from drain to source" to "runs from source to drain"
- Changed "The pin with the red probe is the drain; the pin with the black probe is the source" to "The pin with the red probe is the source; the pin with the black probe is the drain"

---

### Error 2 — Incorrect gate discharge method (Major)

**Location:** "Gate behavior" section, first paragraph

**Original text:**
> Before testing or handling a MOSFET you've just desoldered, touch the source and drain leads together briefly to discharge the gate through the body diode path.

**Problem:** The gate is separated from all other terminals by silicon dioxide and has no conductive path to source, drain, or body in a healthy device. Shorting the source to the drain via the body diode does not discharge the gate — it only forward-biases the body diode, which has no electrical connection to the gate terminal. The only way to drain the gate capacitance is to provide a conductive path from the gate itself to another terminal, normally source. This is a safety-relevant error: a reader following the original instruction might handle an ESD-sensitive gate thinking it is discharged when it is not.

**Correction applied:**
- Changed "touch the source and drain leads together briefly to discharge the gate through the body diode path" to "touch the gate and source leads together briefly to discharge any charge stored on the gate"

---

## Items Verified as Correct

- TO-220 pinout convention: tab = drain; remove mounting screw before desoldering — correct.
- D-PAK and SO-8 package descriptions — accurate.
- Part number conventions: IRF9540 P-channel (9 in number), IRF540 N-channel, FQP30N06L breakdown — correct.
- Small-signal MOSFET identification vs. BJT: OL on gate pairs vs. junction voltages — correct.
- Body diode forward voltage range (0.45–0.65V) — typical for silicon; correct.
- P-channel body diode polarity: anode at drain, cathode at source; red probe on drain — correct.
- Gate oxide check: OL in both directions on a healthy gate — correct.
- Logic-level vs. standard gate drive voltages: 3.3–5V vs. 8–12V — correct characterization.
- Shorted drain-source symptom: low voltage in both directions (0.05–0.2V) — correct.
- ESD gate oxide damage description — correct.
- IRF3205 specs (55V, 110A) — correct.
- IRF540 specs (100V, 28A) — correct for the original IRF540.
- STP75NF75 specs (75V, 75A) — correct.
- IRF9540 specs (100V, 19A) — correct.
- Derating advice (60% current for unknown salvage parts) — conservative and appropriate.
- Tab-to-drain resistance check: zero ohms expected — correct.
- Storage advice (antistatic foam, shorting all leads into foam) — correct practice.

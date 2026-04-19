# Technical Review: MOSFETs

## Critical Errors

1. N-channel body diode polarity — anode stated at drain
    Found:   "On an N-channel MOSFET, the body diode runs from drain to source with the anode at the drain."
    Fix:     "On an N-channel MOSFET, the body diode runs from source to drain with the anode at the source."
    Reason:  In an N-channel MOSFET the parasitic body diode has its anode at the source and its cathode at the drain — current flows source-to-drain through the diode, not drain-to-source.

2. N-channel probe assignment follows the wrong polarity
    Found:   "The pin with the red probe is the drain; the pin with the black probe is the source."
    Fix:     "The pin with the red probe is the source; the pin with the black probe is the drain."
    Reason:  Because the body diode anode is at the source, forward biasing requires red (positive) on the source and black on the drain, so the probe-to-pin mapping is exactly backwards in the original text.

3. Gate discharge method — shorting drain to source does not discharge the gate
    Found:   "touch the source and drain leads together briefly to discharge the gate through the body diode path."
    Fix:     "touch the gate lead to the source lead briefly to discharge the gate capacitance before handling or testing."
    Reason:  The body diode is between drain and source, not connected to the gate; shorting drain-to-source provides no discharge path for the gate capacitance, so the gate remains charged and vulnerable to ESD damage. The correct method is to short gate to source.

## Fact-Check Items

4. Body diode Vf lower bound may be slightly narrow
    Claim:   "one pair reads a forward voltage of 0.45–0.65V"
    Concern: The calibration reference for MOSFET body diode Vf runs 0.4–0.65 V; some power MOSFETs (especially low-Rdson devices) measure body diode Vf as low as 0.4 V, which would be missed by a 0.45 V floor.
    Source:  Check a cross-section of salvage-common parts: IRF3205, IRF540, IRFZ44N datasheets — look at "body diode forward voltage" at low forward current (1 mA test condition is typical for diode-mode meters).

5. Drain-source short root cause conflates two failure modes
    Claim:   "Overvoltage on the drain … punches through the gate oxide or the drain-source channel"
    Concern: Gate oxide punch-through is primarily an ESD/overvoltage-at-the-gate failure mode; drain overvoltage typically destroys the device through avalanche/second-breakdown in the drift region, not through the gate oxide. Attributing a drain-source short to gate oxide damage in the same breath as a drain-transient event may confuse the root cause for readers trying to diagnose boards.
    Source:  Application notes on MOSFET failure analysis — STMicroelectronics AN10273 or Vishay "Power MOSFET Basics" cover the distinction between avalanche failure and gate oxide failure clearly.

## Clean

- Identify channel and role: package descriptions, part number conventions, and small-signal vs. power MOSFET identification all look accurate. No issues found.
- P-channel body diode: polarity (anode at drain, cathode at source) and probe assignment (red on drain, black on source) are correct for P-channel. No issues found.
- Gate check: OL gate-to-drain and gate-to-source in both directions is accurate. Attributing a gate short to ESD is correct. No issues found.
- Gate behavior (DC isolation, logic-level vs. standard Vgs thresholds): 3.3–5 V for logic-level, 8–12 V for standard power MOSFETs — both ranges are reasonable and commonly cited. No issues found.
- Reuse notes: IRF3205 (55 V, 110 A), IRF540 (100 V, 28 A), STP75NF75 (75 V, 75 A), IRF9540 (100 V, 19 A) all match published datasheets. 60% current derating for unknown parts is appropriate. No issues found.
- Thermal cracking and Package lifted sections: qualitative failure descriptions are accurate. No issues found.
- Theory links: /open-circuits/Semi/SEMI_6.html and /open-circuits/DC/DC_5.html are correct path formats. No issues found.

---

**Apply fixes:** enter `all`, a comma-separated list of IDs (e.g. `1,3`), `interactive` to step through one at a time, or `skip`.

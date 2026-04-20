# Technical Review: MOSFETs

## Critical Errors

1. N-channel body diode polarity — anode stated at drain
    Found:   "On an N-channel MOSFET, the body diode runs from drain to source with the anode at the drain."
    Fix:     "On an N-channel MOSFET, the body diode runs from source to drain with the anode at the source."
    Reason:  In an N-channel MOSFET the body (P-type) is shorted to the source, so the body diode anode is at the source and the cathode is at the drain — the opposite of what the text states.

2. N-channel probe assignment — red/black leads swapped
    Found:   "That forward-biased reading is the body diode. The pin with the red probe is the drain; the pin with the black probe is the source."
    Fix:     "That forward-biased reading is the body diode. The pin with the red probe is the source; the pin with the black probe is the drain."
    Reason:  The red probe (positive) must sit on the anode to forward-bias the diode. Because the N-channel body diode anode is at the source, the red probe identifies the source, not the drain.

3. Gate discharge method — wrong leads shorted
    Found:   "touch the source and drain leads together briefly to discharge the gate through the body diode path."
    Fix:     "touch the gate and source leads together briefly to discharge any charge sitting on the gate."
    Reason:  Shorting drain to source leaves the gate floating and does nothing to discharge it; gate charge is removed by shorting gate to source (Vgs = 0).

4. Shorted drain-source failure — incorrect mechanism cited
    Found:   "Overvoltage on the drain (from an inductive kick, a mains transient, or a motor back-EMF spike) punches through the gate oxide or the drain-source channel"
    Fix:     "Overvoltage on the drain (from an inductive kick, a mains transient, or a motor back-EMF spike) exceeds the drain-source breakdown voltage and avalanches or punches through the drain-body junction"
    Reason:  Gate oxide punch-through is caused by gate overvoltage or ESD, not drain overvoltage. Drain overvoltage failures destroy the drain-body junction through avalanche breakdown, not the gate oxide.

## Fact-Check Items

5. N-channel body diode Vf lower bound
    Claim:   "one pair reads a forward voltage of 0.45–0.65V"
    Concern: The skill calibration reference floor for MOSFET body diode Vf is 0.4 V. Stating 0.45 V as the lower bound may cause a technician to discard a healthy part whose body diode measures 0.40–0.44 V, which is within normal range for many power MOSFETs.
    Source:  Check several common salvage MOSFETs (IRF3205, IRF540, IRFZ44N) in diode mode on a calibrated meter; confirm whether any healthy parts read below 0.45 V. Cross-reference body diode forward voltage in those datasheets.

6. STP75NF75 ratings
    Claim:   "STP75NF75 (75V, 75A)"
    Concern: Plausible part number but the current rating should be confirmed against the STMicroelectronics datasheet — some revisions or lookalike parts differ.
    Source:  STMicroelectronics STP75NF75 datasheet; confirm Vds and Id(continuous) at 25 °C.

7. IRF9540 continuous current rating
    Claim:   "IRF9540 (100V, 19A)"
    Concern: The IRF9540N (the commonly stocked variant) is rated 100 V, 23 A; the original IRF9540 is 19 A. Using 19 A risks undervaluing parts that are actually the N-suffix version, and the N-suffix is far more common in recent salvage stock.
    Source:  Vishay / IR IRF9540 and IRF9540N datasheets; compare Id(continuous) at 25 °C.

## Clean

- **Identify channel and role** — Package descriptions, part number conventions, and TO-92/SOT-23 identification guidance are accurate. No issues found.
- **P-channel body diode direction** — Anode at drain, cathode at source is correct for P-channel; probe assignment (black on source, red on drain) correctly follows from that polarity. No issues found.
- **Gate check** — OL reading in both directions and short-circuit interpretation are correct. No issues found.
- **Gate behavior (switching test)** — Resistor value, supply range, and gate voltage ranges for logic-level vs. standard MOSFETs are all reasonable. No issues found.
- **Thermal cracking** — Description is accurate. No issues found.
- **Package lifted from board** — Tab-to-drain resistance test and interpretation are correct. No issues found.
- **Reuse notes (general)** — 60% current derating for unknowns is conservative and safe. IRF3205 and IRF540 ratings are correct. No issues found.
- **Storage and labeling** — Antistatic foam guidance and labeling convention are correct. No issues found.
- **Theory links** — Cross-reference paths are correctly formatted absolute paths. No issues found.

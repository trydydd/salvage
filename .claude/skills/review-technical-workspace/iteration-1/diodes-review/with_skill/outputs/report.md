# Technical Review: Diodes

## Critical Errors

**1** Meter range instruction contradicts diode mode

    Found:   "Set your meter to the 20V DC range to get an accurate reading."
    Fix:     "Most meters give a stable reading in diode mode without any range adjustment — just confirm the selector is on the diode symbol, not a voltage range."
    Reason:  Diode mode is a fixed function selected by symbol; there is no voltage range to set within it, and following this instruction literally (switching to 20 V DC) would put the meter in voltage measurement mode, where it would read ~0 V across any diode and appear failed.

**2** Silicon diode forward voltage range is wrong by 2×

    Found:   "A good silicon rectifier or signal diode reads 1.4–2.0V."
    Fix:     "A good silicon rectifier or signal diode reads 0.5–0.8 V."
    Reason:  Silicon diodes measure 0.5–0.8 V in diode mode; 1.4–2.0 V is the LED range, and a reader would wrongly reject every good rectifier diode they test.

**3** Wrong unit in forward-voltage quick-sort table

    Found:   "0.55–0.80 Ω: standard silicon rectifier or signal diode"
    Fix:     "0.55–0.80 V: standard silicon rectifier or signal diode"
    Reason:  The unit is listed as Ω (ohms) instead of V (volts), which is inconsistent with every other entry in the same table and would confuse a reader trying to use it as a reference.

## Fact-Check Items

**4** Silicon diode lower-bound Vf stated as 0.55 V in two places

    Claim:   "silicon (0.55–0.8V)" (Identify the type) and "0.55–0.80 V" (Forward voltage by type table)
    Concern: The calibration reference puts the silicon diode Vf window at 0.5–0.8 V. Low-current readings on signal diodes and some rectifiers can reach 0.5–0.55 V; using 0.55 V as the lower bound may cause good parts to be discarded.
    Source:  1N4148 datasheet (On Semiconductor / Vishay) — check Vf at 1 mA test current; /open-circuits/Semi/SEMI_6.html for junction physics.

**5** Standard green LED upper bound stated as 2.4 V in "Use diode mode"

    Claim:   "standard green reads 1.9–2.4V"
    Concern: The calibration reference gives 1.9–2.5 V for standard green. 2.4 V may clip the top of the real range.
    Source:  Any commodity 5 mm green LED datasheet (e.g., Kingbright WP7113GD) — check Vf at 10 mA; compare to the 2.5 V listed in the Forward voltage by type table in the same document.

**6** High-brightness / blue lower bound stated as 2.9 V

    Claim:   "high-brightness green reads 2.9–3.5V" (Use diode mode) and "2.9–3.6 V: blue, white, or high-brightness green LED" (Forward voltage by type)
    Concern: The calibration reference sets the blue/white/HB-green window at 3.0–3.6 V. A lower bound of 2.9 V could cause standard green LEDs to be misidentified as HB-green, or vice versa.
    Source:  Cree C503B-GAS or Kingbright APHD2012CGCK HB-green LED datasheet — check Vf at low meter test current; /open-circuits/Semi/SEMI_6.html.

## Clean

- **Identify the type** — Part identification, package descriptions, and Schottky Vf range are accurate. No issues beyond finding 4.
- **Use diode mode — Reverse check** — OL guidance and leakage interpretation are correct. No issues.
- **Use diode mode — In-circuit vs. desoldered** — Parallel path warning is accurate and appropriately flagged. No issues.
- **Common failure modes** — Shorted, open circuit, leaky, and heat-stress descriptions are all technically accurate. Root causes correctly attributed. No issues.
- **Reuse notes** — Selection guidance and discard criteria are sound. No issues.
- **Theory links** — Link paths match the required `/open-circuits/...` format. No issues.

---

**Apply fixes:** enter `all`, a comma-separated list of IDs (e.g. `1,3`), `interactive` to step through one at a time, or `skip`.

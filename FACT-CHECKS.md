# Fact-Check Tracker

Items flagged for human verification by the `review-technical` skill. Delete each entry once verified and the source page updated.

---

- [ ] **Relays** · Click test and contact condition · FACT-CHECK 3: Verify whether inductive kick in a 12 V relay coil can exceed 100 V; 50–100 V may understate the worst case for unprotected coils.  
  Claim: "The inductive kick when the coil turns off can reach 50–100V in a 12V relay coil"  
  Source: Relay coil inductance specs in SRD-05VDC or G5V-2 datasheets; /open-circuits/DC/DC_5.html for inductive transient background.  
  File: content/components/08-relays.md

- [ ] **Relays** · Click test and contact condition · FACT-CHECK 4: Verify typical pull-in time for small PCB relays; most datasheets spec 3–10 ms, making 10–20 ms potentially too slow as a pass threshold.  
  Claim: "the armature should pull in within about 10–20ms"  
  Source: Omron G5V-2 datasheet (operate time), Songle SRD datasheet — check the "operate time" row.  
  File: content/components/08-relays.md

- [ ] **Relays** · Contact resistance check · FACT-CHECK 5: Verify whether 0.2 Ω is an appropriate "usable" threshold for cleaned contacts; relay datasheets typically specify 100 mΩ (0.1 Ω) max, making 0.2 Ω potentially too permissive for higher-current loads.  
  Claim: "If the reading drops to under 0.2Ω after that, the contacts are usable."  
  Source: IEC 61810-1 contact resistance limits; relay datasheets typically list max contact resistance of 100 mΩ (0.1 Ω).  
  File: content/components/08-relays.md

- [ ] **Relays** · Reuse notes · FACT-CHECK 6: Verify whether 75% derating is conservative enough for salvaged relay contacts with unknown switching history; some sources recommend 50% for all salvaged contacts regardless of load type.  
  Claim: "Derate the contact current rating to 75% for salvaged relays used with resistive loads"  
  Source: IEC 61810-1 §8 (endurance ratings); Omron relay application notes on contact derating for unknown service history.  
  File: content/components/08-relays.md

- [ ] **review-technical skill** · Calibration reference · LED Vf typical values: red/orange/yellow typ 2.0V and max 2.2V are estimates — not verified against datasheets.  
  Claim: "typ 2.0 V, max 2.2 V" for red / orange / yellow LED Vf  
  Source: Check datasheets for common red LEDs (e.g. Kingbright APT2012SRCPRV, Cree C503B-RAN) and yellow/orange LEDs (e.g. Kingbright APT2012SYCK); confirm both typ and max at IF=20mA. Note whether orange and yellow differ enough from red to warrant separate rows.  
  File: .claude/skills/review-technical/SKILL.md

# Fact-Check Tracker

Items flagged for human verification by the `review-technical` skill. Delete each entry once verified and the source page updated.

---



- [ ] **Relays** · Contact resistance check · FACT-CHECK 5: Verify whether 0.2 Ω is an appropriate "usable" threshold for cleaned contacts; relay datasheets typically specify 100 mΩ (0.1 Ω) max, making 0.2 Ω potentially too permissive for higher-current loads.  
  Claim: "If the reading drops to under 0.2Ω after that, the contacts are usable."  
  Source: IEC 61810-1 contact resistance limits; relay datasheets typically list max contact resistance of 100 mΩ (0.1 Ω).  
  File: content/components/08-relays.md

- [ ] **Relays** · Reuse notes · FACT-CHECK 6: Verify whether 75% derating is conservative enough for salvaged relay contacts with unknown switching history; some sources recommend 50% for all salvaged contacts regardless of load type.  
  Claim: "Derate the contact current rating to 75% for salvaged relays used with resistive loads"  
  Source: IEC 61810-1 §8 (endurance ratings); Omron relay application notes on contact derating for unknown service history.  
  File: content/components/08-relays.md


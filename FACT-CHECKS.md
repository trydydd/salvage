# Fact-Check Tracker

Items flagged for human verification by the `review-technical` skill. Delete each entry once verified and the source page updated.

---

- [ ] **Microwave Ovens** · Before You Open It · FACT-CHECK 1: stored capacitor voltage vs. cited ~2000 V operating voltage  
  Claim: "a high-voltage section that runs at around 2000 V" / "can still be holding 2000 V"  
  Source: MOT circuit reference / HV cap datasheet (0.9–1.1 µF, 2100 VAC types); voltage-doubler analysis. The secondary is ~2000 V RMS, but the cap charges to ~2.8 kV peak and the doubler drives the magnetron to ~-4 kV — confirm the figure or reword so 2000 V isn't read as the ceiling.  
  File: content/donor-guides/10-microwave-ovens.md

- [ ] **Audio Equipment** · Before You Open It · FACT-CHECK 1: filter-cap capacitance upper bound  
  Claim: "often 4700 microfarads to 22000 microfarads, and rated 35 V to 80 V or more"  
  Source: Service manuals / cap markings on mid-power receivers (NAD, Marantz, Pioneer). Voltage range and lower bound are right; 22000 µF is at the top end, with most salvage amps at 6800–15000 µF per rail. Confirm the upper bound isn't overstated.  
  File: content/donor-guides/08-audio-equipment.md

- [ ] **Printers** · What to Target · FACT-CHECK 1: carriage DC motor stated as flat 24 V  
  Claim: "24 V DC; encoder strip alongside; 2-pin motor lead plus 2-pin encoder"  
  Source: Service-manual rail voltages for a few Epson/Canon/HP inkjets; measure the carriage-motor supply on the main board. Carriage motors run off the printhead drive rail, commonly ~21–42 V; 24 V is presented as universal.  
  File: content/donor-guides/04-printers.md

- [ ] **Laptops** · What to Target · FACT-CHECK 1: blower fan voltage "5V or 12V"  
  Claim: "5V or 12V; 2-pin, 3-pin, or 4-pin connector" (also in intro)  
  Source: Fan-label voltages on salvaged laptop blowers; EC fan-rail measurement. Laptop blowers are predominantly 5 V (some 3.3 V); 12 V is a desktop figure, uncommon in laptops.  
  File: content/donor-guides/06-laptops.md

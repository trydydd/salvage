---
title: "Capacitors"
section: components
---

Capacitors cover a wider range of shapes, sizes, and failure modes than almost any other component family. Sorting them takes a few minutes of practice; after that you'll be able to glance at a board and know which ones are worth pulling before you pick up the iron.

## Types you will meet

Electrolytic capacitors are the aluminum cylinders standing upright off the board, with two leads from the bottom. They're polarized: a stripe printed along the side marks the negative lead, and the negative lead is also usually shorter. Values run from around 0.1µF up to 10,000µF or more, and you'll find them anywhere that needs bulk energy storage or supply filtering: the main filter caps in a switching supply are often 470µF–3300µF at 16–450V, depending on what the supply puts out.

Ceramic capacitors are the small brown or tan disc shapes (through-hole) or the tiny rectangular blocks on modern boards (SMD). They have no polarity and handle values from a few pF up to around 10µF. You'll find them everywhere: bypassing supply rails, coupling signals, or in the feedback networks of switching converters. SMD ceramics in 0402 or 0603 packages are tiny and hard to handle without tweezers, but 0805 and 1206 are manageable.

Film capacitors are the rectangular blocks, often yellow, orange, or green, with leads coming from either end or both from the same face. They're non-polar. Values typically run from 1nF to around 1µF, and they appear in audio circuits, motor suppression, and anywhere that a capacitor needs to handle AC without degrading. Polyester (Mylar) and polypropylene are the two you'll see most; you can't tell them apart by eye, but both are worth pulling.

Tantalum capacitors are the small teardrop-shaped or rectangular parts, usually brown, yellow, or a faded orange. The positive lead is marked with a stripe or a "+" symbol. SMD tantalums look like a squat rectangular block and often have a painted stripe on the positive end. They run small values (0.1µF–100µF) at higher reliability than electrolytics, and they show up in portable electronics on logic supply rails. They fail short, which matters for reuse decisions. Supercapacitors look like large electrolytics but carry values in farads, not microfarads, and are worth pulling whenever you find them.

## Read the markings

Electrolytic markings are usually printed in full: the value in µF, the voltage rating (16V, 35V, 100V, etc.), a temperature grade (85°C or 105°C), and the brand. If the printing is worn, the stripe for the negative lead is often still legible and you can at least establish polarity. The capacitance and voltage will be stamped into the top cap on some older parts; check there if the side is blank.

Ceramic disc capacitors often use the same three-digit code as resistors, but the unit is picofarads. 104 means 10 × 10^4 pF = 100nF (= 0.1µF). 101 means 100pF. 221 means 220pF. A code of just 47 or 100 with no multiplier digit means that value in pF directly. SMD ceramics frequently have no marking at all below 0805 size; with those you're working from board position and schematic, not the part itself.

Film capacitors print the value in nF or µF, or use the same three-digit pF code. A part marked 0.1µF and one marked 100nF and one marked 104 are all the same value. Voltage ratings appear as a number followed by V or KV; a 630V rating is common in mains-rated parts and means the part sat on the AC side of something, which is worth noting for reuse.

## Test methods

**Multimeter resistance mode (quick check)**

Desolder the capacitor first. In-circuit checks for capacitors are largely useless because parallel components swamp the reading. Set your meter to a high resistance range (2MΩ or the highest available). Touch the probes to the capacitor leads, observing polarity on electrolytics (red probe to positive). The reading should start low, then climb toward OL as the capacitor charges from the meter's internal battery. Reverse the probes and watch it discharge and charge again. A capacitor that reads a dead short (zero, staying at zero) is failed short. One that reads OL immediately with no charge sweep is open or dry. The charge-and-climb behavior is the confirmation you're looking for.

**Multimeter capacitance mode**

If your meter has a capacitance range, discharge the capacitor first by shorting the leads together for a few seconds, then connect it to the meter. For electrolytics, observe polarity. The reading should be within 20% of the marked value for a healthy part. Readings more than 50% low on an electrolytic usually indicate significant degradation; anything below 20% of the marked value is worth discarding. Ceramics and film caps read more accurately and should be within 10–20% of marked.

**ESR meter**

A basic ESR meter (around £15–30 for a kit or entry-level unit) tells you the equivalent series resistance of an electrolytic, which the multimeter can't. Healthy electrolytics read 0.05–0.5Ω depending on value and voltage rating; large 105°C low-ESR parts from switching supplies should be under 0.1Ω. A reading above 2–5Ω on a standard electrolytic is a degraded part. ESR meters can check in-circuit on a powered-down board, which saves desoldering time during diagnosis, though nearby components can still affect the reading.

## Failure modes

**Bulging top (electrolytic)**

The vent on the top of an aluminum electrolytic is meant to open before the can ruptures. When the vent bulges upward or the top appears domed instead of flat, the cap has built up internal pressure from heat or overvoltage. The electrolyte inside is caustic and can cause chemical burns on contact with skin. Don't use a bulged cap; discard it. If you suspect a vented cap has already leaked, the dried residue around the base is often brown or dark gray, and the board traces nearby may show corrosion.

**High ESR without visible damage**

This is the failure mode that kills switching power supplies silently. The cap looks fine, measures the right capacitance, but its internal series resistance has risen from normal (0.1–0.5Ω) to 5–20Ω. The supply regulates poorly under load, output ripple climbs, and the supply runs warm. An ESR meter catches this; a standard multimeter doesn't. Electrolytics from supplies that ran hot for years are suspect even if they look intact.

**Shorted tantalum**

Tantalum capacitors fail short, often catastrophically. Reverse polarity or overvoltage is the usual cause, but tantalums can also fail short if the rated voltage is exceeded even briefly. A shorted tantalum in a 5V logic rail will draw continuous current, heat up, and sometimes ignite the electrolyte inside. Before reusing any tantalum, check it in resistance mode with the probes in both orientations: a good part charges like an electrolytic; a shorted part reads zero in both directions.

**Cracked ceramic (SMD)**

Board flex cracks SMD ceramic capacitors, particularly on boards that have been dropped or that mount near screw holes used to torque the board down. A cracked ceramic often measures as a partial short. You can't see the crack visually in many cases; if a ceramic is measuring much lower resistance than expected and the board shows no obvious contamination, check the ceramic first. These aren't worth reusing; a cracked ceramic can change value with temperature or vibration in ways that are hard to predict.

**Dried-out electrolytic**

An old or heat-stressed electrolytic can lose electrolyte slowly through the seal. The capacitance reading drops, ESR rises, and the part feels lighter than a comparable new cap. You'll find this most often in equipment that ran warm for years: old CRT monitors, high-load linear supplies, anything with poor ventilation. The cap may look completely normal. Date-code the electrolytics you pull from old equipment: a part with a date code showing manufacture before 2005 deserves extra scrutiny.

## Voltage derating

Derate electrolytic capacitors to 80% of their marked voltage in any new build. A 25V cap becomes an 18V cap in practice. This accounts for age, for production variation, and for the short voltage spikes that appear in real circuits. Tantalums need more conservative derating: treat a marked 35V tantalum as a 20V part. Film and ceramic capacitors derate less aggressively, but staying 20% below the marked voltage is still the sensible choice for anything running near AC mains.

Capacitors from the hot side of a switching supply have typically seen voltage stress every time the supply was loaded. The caps running on the primary side of a mains switching supply (often rated 400V or 450V) are under stress every time the supply runs. Even if they measure fine at the bench, the stress history is unknown. For low-risk general-purpose builds, pull them anyway and mark the bag with the rated voltage; for anything where the cap failure has consequences, use new parts at that voltage.

## Reuse notes

Ceramic and film capacitors from healthy boards are almost always worth pulling. They don't degrade with age the way electrolytics do, and a ceramic marked 104 is the same part regardless of when it was made. Prioritize larger physical sizes (1206 and above for SMD, standard disc sizes for through-hole) because they're easier to work with. The tiny 0402 SMD parts are not worth the effort unless you specifically need that package.

Electrolytics are the judgment call. From audio equipment and linear supplies that ran cool and were not from a failure, they're often still fine. From switching supplies, especially failed ones, treat them as suspect regardless of how they look. Always record the value, voltage rating, and temperature grade on the storage bag. For 85°C parts pulled from a design that ran them hard, note that too.

Tantalums are worth pulling for their value, but label them with polarity clearly: a strip of tape on the positive end with "+" in marker avoids any ambiguity later. Keep them in a separate compartment from electrolytics.

Don't reuse any capacitor with a bulged top, visible corrosion at the base, or a cracked body. Don't reuse electrolytics from the board that failed the supply you're pulling from: the failure mode may have stressed every cap on that board.

## Theory links

For charge and discharge behavior and how to observe it with a meter, see [DC measurements](/open-circuits/DC/DC_5.html). For test setups that let you see how a capacitor behaves under real load conditions, see [bench experiments](/open-circuits/Exper/EXP_3.html).

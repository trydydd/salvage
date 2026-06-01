#!/usr/bin/env python3
"""Generate SVG schematic for the continuity tester project page.

Run standalone:  python build/schematics/continuity_tester.py
Output:          content/images/continuity-tester.svg
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

OUTPUT = (
    Path(__file__).resolve().parent.parent.parent / "content" / "images" / "continuity-tester.svg"
)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with schemdraw.Drawing(canvas="svg") as d:
        d.config(fontsize=11)

        # Top rail: battery → switch → resistor → LED → Probe A
        batt = d.add(elm.Battery().right().label("3 V (2×AA)", loc="left", ofst=0.2))
        d.add(elm.Switch().right().label("SW (opt.)", loc="top"))
        d.add(elm.Resistor().right().label("100–220 Ω", loc="top"))
        led = d.add(elm.LED().right().label("LED", loc="top"))
        d.add(elm.Dot())
        d.add(elm.Label().at(led.end).label("Probe A", loc="right"))

        # Close the loop: down, left, up
        d.add(elm.Line().down())
        d.add(elm.Line().left().tox(batt.start))
        probe_b = d.add(elm.Dot())
        d.add(elm.Label().at(probe_b.end).label("Probe B", loc="left"))
        d.add(elm.Line().up().toy(batt.start))

    d.save(str(OUTPUT))
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()

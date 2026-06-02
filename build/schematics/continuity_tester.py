#!/usr/bin/env python3
"""Generate hand-drawn SVG schematic for the continuity tester project page.

Run standalone:  python build/schematics/continuity_tester.py
Output:          content/images/continuity-tester.svg
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

OUTPUT = (
    Path(__file__).resolve().parent.parent.parent / "content" / "images" / "continuity-tester.svg"
)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    plt.xkcd()
    plt.rcParams["figure.facecolor"] = "none"
    plt.rcParams["axes.facecolor"] = "none"
    schemdraw.use("matplotlib")

    with schemdraw.Drawing() as d:
        d.config(fontsize=12)

        # Top rail: battery → switch → resistor → LED → Probe A
        # Battery going right: start = left = negative, end = right = positive
        batt = d.add(elm.Battery().right().label("3 V (2×AA)", loc="top"))
        # istart and iend are at the battery plates themselves (leads excluded)
        d.add(elm.Label().at((batt.istart.x - 0.75, batt.istart.y)).label("−", ofst=0.2))
        d.add(elm.Label().at(batt.iend).label("+", ofst=0.2))
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

        d.save(str(OUTPUT), transparent=True)

    plt.close("all")
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()

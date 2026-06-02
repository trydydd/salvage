#!/usr/bin/env python3
"""Generate hand-drawn SVG schematic for the capacitor discharge tool project page.

Run standalone:  python build/schematics/cap_discharge.py
Output:          content/images/cap-discharge.svg

Circuit: two parallel branches between Probe+ and Probe−
  - Power path: 1 kΩ / 10 W wirewound resistor
  - Indicator: LED in series with 10 kΩ / 1 W resistor
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

OUTPUT = (
    Path(__file__).resolve().parent.parent.parent / "content" / "images" / "cap-discharge.svg"
)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    plt.xkcd()
    schemdraw.use("matplotlib")

    with schemdraw.Drawing() as d:
        d.config(fontsize=12)

        # Left input lead labelled Probe+
        left = d.add(elm.Line().right(1.5).label("Probe +", loc="left"))
        left_jxn = d.add(elm.Dot())
        left_pos = left_jxn.end

        # Top branch: 1.5-unit bridge + power resistor + 1.5-unit bridge = 6 units total,
        # matching the bottom branch (LED 3 + 10 kΩ 3 = 6) so the closing line meets the
        # right junction cleanly and Probe − reads as an open terminal.
        d.add(elm.Line().right(1.5))
        d.add(elm.Resistor().right().label("1 kΩ / 10 W", loc="top"))
        d.add(elm.Line().right(1.5))
        right_jxn = d.add(elm.Dot())
        right_pos = right_jxn.end

        # Right output lead labelled Probe−
        d.add(elm.Line().right(1.5).label("Probe −", loc="right"))

        # Bottom branch from left junction: LED then indicator resistor
        d.add(elm.Line().at(left_pos).down())
        d.add(elm.LED().right().label("LED", loc="bottom"))
        d.add(elm.Resistor().right().label("10 kΩ / 1 W", loc="bottom"))
        d.add(elm.Line().up().toy(right_pos))

        d.save(str(OUTPUT))

    plt.close("all")
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()

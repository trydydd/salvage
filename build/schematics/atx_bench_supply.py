#!/usr/bin/env python3
"""Generate hand-drawn SVG schematic for the ATX bench supply project page.

Run standalone:  python build/schematics/atx_bench_supply.py
Output:          content/images/atx-bench-supply.svg

Shows: ATX PSU block with output rails, PS_ON toggle switch, dummy load
resistor on +5 V, and PWR_OK indicator LED.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

OUTPUT = (
    Path(__file__).resolve().parent.parent.parent
    / "content"
    / "images"
    / "atx-bench-supply.svg"
)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    plt.xkcd()
    schemdraw.use("matplotlib")

    with schemdraw.Drawing() as d:
        d.config(fontsize=10)

        # ATX PSU block
        psu = d.add(
            elm.Ic(
                pins=[
                    elm.IcPin(name="PS_ON", side="left", pin="1"),
                    elm.IcPin(name="+12 V", side="right", pin="2"),
                    elm.IcPin(name="+5 V", side="right", pin="3"),
                    elm.IcPin(name="+3.3 V", side="right", pin="4"),
                    elm.IcPin(name="−12 V", side="right", pin="5"),
                    elm.IcPin(name="GND", side="right", pin="6"),
                    elm.IcPin(name="PWR_OK", side="right", pin="7"),
                ],
                pinspacing=1.5,
                edgepadH=0.5,
            ).label("ATX PSU", loc="center")
        )

        # PS_ON toggle switch from PS_ON pin to ground
        d.add(elm.Switch().at(psu.PS_ON).left().label("toggle SW", loc="top"))
        d.add(elm.Ground())

        # +12 V binding post
        d.add(elm.Line().at(psu["+12 V"]).right(2).label("+12 V post", loc="right"))

        # +5 V rail with dummy load to GND
        five_v_start = psu["+5 V"]
        d.add(elm.Line().at(five_v_start).right(1))
        five_v_node = d.add(elm.Dot())
        d.add(elm.Line().right(1).label("+5 V post", loc="right"))
        d.add(elm.Resistor().at(five_v_node.end).down().label("10–47 Ω\n10 W", loc="right"))
        d.add(elm.Ground())

        # +3.3 V binding post
        d.add(elm.Line().at(psu["+3.3 V"]).right(2).label("+3.3 V post", loc="right"))

        # −12 V binding post
        d.add(elm.Line().at(psu["−12 V"]).right(2).label("−12 V post", loc="right"))

        # GND binding post
        d.add(elm.Line().at(psu["GND"]).right(1))
        gnd_node = d.add(elm.Dot())
        d.add(elm.Line().right(1).label("GND posts", loc="right"))
        d.add(elm.Ground().at(gnd_node.end))

        # PWR_OK indicator LED with 470 Ω series resistor
        d.add(elm.Resistor().at(psu["PWR_OK"]).right().label("470 Ω", loc="top"))
        d.add(elm.LED().right().label("PWR LED (opt.)", loc="top"))
        d.add(elm.Line().down())
        d.add(elm.Ground())

        d.save(str(OUTPUT))

    plt.close("all")
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()

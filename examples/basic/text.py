"""
text.py — demonstrate rendering text on copper and silkscreen.

Usage:
    cd examples/basic
    python text.py
Outputs:
    Gerber (GTO, GTL, GBL) and drill files in ./text/
"""

import math

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board --- #
    brd = Board((40, 30))

    # --- Add text using the drawing context --- #
    brd.DC((10, 10)).text("Top Text", side="top")
    brd.DC((20, 10)).text("Bottom Text", side="bottom")

    # --- Directly add text to various locations and layers --- #
    brd.add_text(
        (10, 15), "Test Text 1", scale=1.0, layer="GTO"
    )  # Top silkscreen, will also default to silkscreen
    brd.add_text(
        (10, 20), "Copper Text 1", scale=1.0, layer="GTL"
    )  # Top copper, default side is top
    brd.add_text(
        (10, 25), "Copper Text 2", scale=2.0, layer="GTL", keepout_box=True
    )  # Top copper with keepout box
    brd.add_text(
        (20, 15), "Copper Text 3", side="bottom", scale=2.0, layer="GBL"
    )  # Bottom copper
    brd.add_text(
        (20, 20),
        "Copper Text 4",
        side="bottom",
        scale=2.0,
        layer="GBL",
        keepout_box=True,
    )  # Bottom copper with keepout box
    brd.add_text(
        (20, 25),
        "Copper Text 5",
        side="bottom",
        scale=2.0,
        layer="GBL",
        keepout_box=True,
        soldermask_box=True,
    )  # Bottom copper with keepout and soldermask box

    # --- Add outline & pour GND on top/bottom --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "GND")

    # --- Save outputs to a folder named after this script ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

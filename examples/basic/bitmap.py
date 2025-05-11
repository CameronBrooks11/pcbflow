"""
bitmap.py — demonstrate placing and rendering bitmap logos.

Usage:
    cd examples/basic
    python bitmap.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./bitmap/
"""

import math

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board --- #
    brd = Board((40, 30))

    # --- Add a bitmap logo various to various locations and layers --- #
    # Note: if no side is specified, it defaults to top side, and
    # if no layer is specified, it defaults to silkscreen layer
    brd.add_bitmap((10, 10), "fxlogo.png", scale=0.5)  # GTO
    brd.add_bitmap((30, 10), "fxlogo.png", side="bottom", scale=0.33)  # GBO
    brd.add_bitmap((10, 20), "fxlogo.png", scale=0.5, layer="GTL")
    brd.add_bitmap((25, 20), "fxlogo.png", scale=0.5, layer="GTL", keepout_box=True)
    brd.add_bitmap((30, 20), "fxlogo.png", side="bottom", layer="GBL", scale=0.33)

    # --- Add outline & pour GND on top/bottom --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "GND")

    # --- Save outputs in folder with the same name as this script --- #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

"""
holes.py — demonstrate adding mechanical holes.

Usage:
    cd examples/basic
    python holes.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./holes/
"""

import math

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board --- #
    brd = Board((40, 30))

    # --- Specify four holes at the corners of the board --- #
    holes = [
        (5, 5),
        (5, 25),
        (35, 5),
        (35, 25),
    ]
    for hole in holes:
        brd.add_hole(hole, 2.0)  # add non‑plated drill at the positions  #

    # --- Add outline & pour GND on top/bottom --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "GND")

    # --- Save outputs to a folder named after this script ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

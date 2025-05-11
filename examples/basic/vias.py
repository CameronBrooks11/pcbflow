"""
vias.py — demonstrate placing through‑vias.

Usage:
    cd examples/basic
    python vias.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./vias/
"""

import math

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board --- #
    brd = Board((40, 30))

    # --- Use drawing context to add vias to the top and bottom layers --- #
    # Note: by default DRC rules set via holes to 0.5mm with 8mil annular ring
    brd.DC((10, 10)).via()
    brd.DC((20, 10)).via()
    brd.DC((10, 20)).via()
    brd.DC((20, 20)).via()

    # --- Add outline & pour GND on top/bottom --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "GND")

    # --- Save outputs to a folder named after this script ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

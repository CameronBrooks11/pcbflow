"""
blank.py — create a blank board outline and pour ground.

Usage:
    cd examples/basic
    python blank.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./blank/
"""

import os
import math
import shapely.geometry as sg

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board ---  #
    brd = Board((40, 30))

    # --- Add outline and pour GND on top/bottom ---  #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "GND")

    # --- Save outputs to a folder named after this script ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

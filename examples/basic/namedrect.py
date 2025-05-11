"""
namedrect.py — demonstrate copper fills with named regions.

Usage:
    cd examples/basic
    python namedrect.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./namedrect/
"""

import math
import shapely.geometry as sg

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board ---  #
    brd = Board((40, 30))

    # --- Add outline ---  #
    brd.add_outline()

    # --- Add named copper regions (rectangles) ---  #
    brd.add_named_rect((5, 25), (15, 20), "GTL", "ABC")  # top ABC zone
    brd.add_named_rect((5, 15), (25, 3), "GTL", "VCC")  # top VCC zone
    brd.add_named_rect((15, 25), (35, 20), "GBL", "GND")  # bottom GND zone
    brd.add_named_rect((8, 15), (35, 3), "GBL", "VCC")  # bottom VCC zone

    # --- Pour with unused named region for that layer ---  #
    brd.fill_layer("GTL", "GND")  # top fill GND
    brd.fill_layer("GBL", "ABC")  # bottom fill ABC

    # --- Save outputs ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

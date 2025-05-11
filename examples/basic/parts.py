"""
parts.py — demonstrate placement of various component footprints.

Usage:
    cd examples/basic
    python parts.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./parts/
"""

import math
import shapely.geometry as sg

from pcbflow import *


if __name__ == "__main__":

    # --- Create a 50×30 mm board ---  #
    brd = Board((50, 30))

    # --- Place SOT, TSSOP, QFN, HDMI on top side ---  #
    brd.add_part((5, 20), SOT23, side="top")
    brd.add_part((15, 20), SOT223, side="top")
    brd.add_part((25, 20), TSSOP14, side="top")
    brd.add_part((35, 10), QFN64, side="top")
    brd.add_part((40, 22), HDMI, side="top")

    # --- Place some more on bottom side too ---  #
    brd.add_part((5, 10), SOT23, side="bottom")
    brd.add_part((15, 10), SOT223, side="bottom")
    brd.add_part((25, 10), SOIC8, side="bottom")

    # --- Add outline & pour GND on top/bottom --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "VCC")

    # --- Save outputs to a folder named after this script ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

    # --- Print parts and layer net strings ---  #
    print(brd.parts_str())
    print(brd.layer_net_str())

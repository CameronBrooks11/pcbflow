"""
headers.py — demonstrate placing various header and DIP footprints.

Usage:
    cd examples/basic
    python headers.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./headers/
"""

import math

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board --- #
    brd = Board((40, 30))

    # --- Place single‑row headers with different silkscreen styles ---  #
    SIL(brd.DC((10, 5)).right(90), "2")
    SIL(brd.DC((10, 10)).right(90), "4")
    SIL_2mm(brd.DC((20, 5)).right(90), "2")
    SIL_2mm(brd.DC((20, 10)).right(90), "4")

    # --- Place DIP packages top & bottom ---  #
    DIP8(brd.DC((15, 20)))
    DIP16(brd.DC((30, 15)), side="bottom")

    # --- Add outline & pour GND on top/bottom --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "GND")

    # --- Save outputs to a folder named after this script ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))

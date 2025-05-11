"""
eagle_import.py — demonstrate importing footprints from an Eagle library.

Usage:
    cd examples/eagle_import
    python eagle_import.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./eagle_import/
"""

import math
import os
import shapely.geometry as sg

from pcbflow import *

eagle_spkfun_lib = "../_example_libs/eagle/sparkfun.lbr"  # Eagle library file

if __name__ == "__main__":

    # --- Initialize a 50×50 mm board --- #
    brd = Board((50, 50))

    # --- Place Eagle parts from sparkfun.lbr ---  #
    EaglePart(brd.DC((10, 40)), libraryfile=eagle_spkfun_lib, partname="TSSOP-24")
    EaglePart(brd.DC((35, 34)), libraryfile=eagle_spkfun_lib, partname="ARDUINO_MINI")

    # --- Create a USB‑B connector and route its D‑ pad using turtle graphics ---  #
    uc = EaglePart(brd.DC((40, 9)), libraryfile=eagle_spkfun_lib, partname="TQFP64")
    usb_con = EaglePart(
        brd.DC((10, 10)), libraryfile=eagle_spkfun_lib, partname="USB-B-SMT", side="top"
    )
    usb_con.pad("D-").turtle("r 90 f 5 l 90 f 10").wire(width=0.25)

    # --- Add outline & pour nets --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "VCC")

    # --- Save and report board data --- #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))
    print(brd.parts_str())
    print(brd.layer_net_str())

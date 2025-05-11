"""
kicad_import.py — demonstrate importing footprints from KiCad modules.

Usage:
    cd examples/kicad_import
    python kicad_import.py
Outputs:
    Preview, Gerber (GTL, GBL) and drill files in ./kicad_import/
"""

import math
import os
import shapely.geometry as sg

from pcbflow import *

kicad_lib1 = "../_example_libs/kicad/kc1.kicad_mod"
kicad_lib2 = "../_example_libs/kicad/kc2.kicad_mod"
kicad_lib3 = "../_example_libs/kicad/kc3.kicad_mod"
kicad_lib4 = "../_example_libs/kicad/kc4.kicad_mod"
kicad_lib5 = "../_example_libs/kicad/kc5.kicad_mod"
kicad_lib6 = "../_example_libs/kicad/kc6.kicad_mod"

if __name__ == "__main__":
    # --- Initialize a 50×30 mm board ---  #
    brd = Board((50, 30))

    # --- Place KiCadFootprint modules top & bottom ---  #
    brd.add_part((5, 8), KiCadPart, libraryfile=kicad_lib1, side="top")
    KiCadPart(brd.DC((22, 20)), libraryfile=kicad_lib2, side="top")
    KiCadPart(brd.DC((8, 22)), libraryfile=kicad_lib3, side="top")
    KiCadPart(brd.DC((35, 20)), libraryfile=kicad_lib4, side="top")
    KiCadPart(brd.DC((25, 20)), libraryfile=kicad_lib5, side="bottom")
    KiCadPart(brd.DC((35, 8)), libraryfile=kicad_lib6, side="bottom")

    # --- Outline & pour nets ---  #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "VCC")

    # --- Save and report board data ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))
    print(brd.parts_str())
    print(brd.layer_net_str())

"""
passive.py — demonstrate placing passive components and fan‑out.

Usage:
    cd examples/basic
    python passive.py
Outputs:
    Preview, Gerber (GTL, GBL, GP2) and drill files in ./passive/
"""

import math
import shapely.geometry as sg

from pcbflow import *


if __name__ == "__main__":
    # --- Create a 40×30 mm board --- #
    brd = Board((40, 30))

    # --- Add an inner copper layer --- #
    brd.add_inner_copper_layer()  # Numbered GP2, GP3, ...

    # --- Set DRC rules to 24 mil for all layers --- #
    brd.drc.via_track_width = MILS(24)

    # --- Place C0603 caps on top and bottom with fan‑out nets, rotated 90 deg ---  #
    C0603(brd.DC((20, 20)).right(90), "0.1 uF", side="top").fanout(None, "VCC")
    C0603(brd.DC((22, 20)).right(90), "0.1 uF", side="bottom").fanout("GND", None)
    C0603(brd.DC((24, 20)).right(90), "0.1 uF", side="top").fanout(None, "GND")
    C0603(brd.DC((26, 20)).right(90), "0.1 uF", side="bottom").fanout("VCC", None)

    # --- Place C0402 caps on top and bottom with some fan‑out nets, rotated 90 deg ---  #
    C1206(brd.DC((5, 10)).right(90), "0.1 uF", side="top").fanout("VDD", None)
    C1206(brd.DC((8, 10)).right(90), "0.1 uF", side="bottom")
    C1206(brd.DC((11, 10)).right(90), "0.1 uF", side="top").fanout(None, "VDD")
    C1206(brd.DC((14, 10)).right(90), "0.1 uF", side="bottom")

    # --- Place R0603 resistors on top and bottom ---  #
    R0603(brd.DC((20, 10)), "4.7k", side="top")
    R0603(brd.DC((22, 13)), "4.7k", side="bottom")
    R0603(brd.DC((25, 10)), "4.7k", side="top")
    R0603(brd.DC((27, 13)), "4.7k", side="bottom")

    # --- Place R0402 resistors on top and bottom, rotated 90 deg ---  #
    R0402(brd.DC((5, 20)).right(90), "4.7k", side="top")
    R0402(brd.DC((8, 20)).right(90), "4.7k", side="bottom")
    R0402(brd.DC((11, 20)).right(90), "4.7k", side="top")
    R0402(brd.DC((14, 20)).right(90), "4.7k", side="bottom")

    # --- Place R0805 resistors on top and bottom ---  #
    R0805(brd.DC((30, 20)), "2k", side="top")
    R0805(brd.DC((32, 23)), "2k", side="bottom")
    R0805(brd.DC((35, 20)), "2k", side="top")
    R0805(brd.DC((37, 23)), "2k", side="bottom")

    # --- Add outline & pour GND on top/bottom and inner layer --- #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GP2", "VDD")
    brd.fill_layer("GBL", "VCC")

    # --- Save outputs to a folder named after this script ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))
    # Note: currently, the inner layer is not saved in the output folder.

    # --- Print parts and layer net strings ---  #
    print(brd.layer_stack_str())
    print(brd.parts_str())
    print(brd.layer_net_str())

"""
sample.py — comprehensive demo combining parts, copper pours, and routing.

Usage:
    cd examples/sample
    python sample.py
Outputs:
    Preview, Gerber (GTL, GBL, GP2, GP3) and drill files in ./sample/
"""

import math
import optparse
import shapely.geometry as sg

from pcbflow import *


eagle_spkfun_lib = "../_example_libs/eagle/sparkfun.lbr"  # Eagle library file

if __name__ == "__main__":
    # --- Initialize a 55×30 mm board with two inner copper layers ---
    brd = Board((55, 30))
    brd.add_inner_copper_layer(2)

    # --- Define an inner GND zone on GP2---  #
    brd.add_named_rect((27, 25), (40, 10), "GP2", "GND")

    # --- Place HDMI and QFN footprints ---  #
    brd.add_part((5, 15), HDMI, side="top", rot=90, family="J")
    brd.add_part((32, 15), QFN64, side="top")

    # --- Place resistors & caps with pad assignment & fanout ---  #
    rx = brd.add_part((15, 18), R0603, side="top")
    ry = brd.add_part((15, 12), R0603, side="top", val="4.7k")
    brd.add_part((15, 25), R0603, side="top", val="200", rot=90).assign_pads(
        "VCC", None
    ).fanout()
    C0603(brd.DC((35, 23)), "0.1 uF", side="top").assign_pads("GND", "VCC").fanout(
        ["VCC", "GND"]
    )
    C0603(brd.DC((41, 22)), "0.1 uF", side="bottom").assign_pads("GND", None).fanout(
        ["VCC", "GND"]
    )
    C0603(brd.DC((35, 7)).right(90), "0.1 uF", side="top").assign_pads(
        "VCC", "GND"
    ).fanout("VDD GND")
    C0603(brd.DC((42, 8)).right(90), "0.1 uF", side="bottom").assign_pads(
        "VCC", None
    ).fanout("VCC")

    # --- Row of C0402 capacitors ---  #
    for x in range(5):
        brd.add_part((5 + x * 3, 4), C0402, side="top")

    # --- Place discrete SOT and SOIC parts on bottom ---  #
    brd.add_part((25, 25), SOT23, side="bottom")
    brd.add_part((20, 8), SOT223, side="bottom")
    brd.add_part((35, 5), SOIC8, side="bottom")

    # --- Add USB‑B connector & route D+ / D‑ ---  #
    usb_con = EaglePart(
        brd.DC((50, 15)).right(180),
        libraryfile=eagle_spkfun_lib,
        partname="USB-B-SMT",
        side="top",
    )
    for p in ["D+", "D-"]:
        usb_con.pad(p).turtle("R90 f2 r 45 f1 L45 f 2 .GBL f 2").wire()

    # --- Route from resistor pads to U1 pads ---  #
    rx.pads[1].turtle("o f5 l45 f1.02 r45 f3 > U1-1").wire()
    ry.pads[1].turtle("o f5 l45 f2 l45 .GP3 f2 .GTL r45 f4 > U1-2").wire()

    # --- Outline & pour all nets ---  #
    brd.add_outline()
    brd.fill_layer("GTL", "GND")
    brd.fill_layer("GBL", "VCC")
    brd.fill_layer("GP2", "VCC")
    brd.fill_layer("GP3", "GND")

    # --- Save and report board data ---  #
    brd.save("%s" % (os.path.basename(__file__)[:-3]))
    print(brd.parts_str())
    print(brd.layer_net_str())

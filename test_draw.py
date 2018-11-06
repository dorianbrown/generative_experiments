#!/usr/bin/env python

from src.draw import Canvas
from fn import Fn

cnv_settings = {
    "fname": f"temp/test",
    "dpi": 300,
    "width": 15,
    "height": 10,
    "bg_rgb": [(0.05, 0.05, 0.05), (0.7, 0.7, 0.7)]
}

with Canvas(**cnv_settings) as cnv:
    cnv.draw_edge([[0, 0], [1, 1]], 0.00001, [1, 1, 1])
    cnv.draw_edge([[1, 0], [0, 1]], 0.00001, [1, 1, 1])

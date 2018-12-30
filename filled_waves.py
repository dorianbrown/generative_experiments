#!/usr/bin/env python

import numpy as np
from math import pi
import random

from src.draw import Canvas
from fn import Fn
from matplotlib import cm

palette = {
    "green": (25, 75, 90, 1),
    "grey": (186, 199, 213, 1),
    "purple": (59, 65, 137, 1),
    "pink": (177, 80, 182, 1),
    "beige": (234, 210, 172, 1)
}

cnv_conf = {
    "fname": f"temp/{Fn().name()}",
    "dpi": 150,
    "width": 20,
    "height": 10,
    "bg_rgb": [(0.05, 0.05, 0.05), (0.15, 0.15, 0.15)]
}

draw_conf = {
    "n_lines": 10
}

with Canvas(**cnv_conf) as cnv:
    start = [0, 0.3]
    curve_w = 0.4
    dips_x = [curve_w * i for i in range(int(1/curve_w) + 2)]
    dips_y = [0.3 + random.normalvariate(0, 0.1) for _ in range(len(dips_x))]
    dips = list(zip(dips_x, dips_y))

    def gen_ctrl_points(a, b):
        points = [random.uniform(a, b), random.uniform(a, b)]
        return min(points), max(points)

    for idx in range(len(dips) - 1):
        print(dips[idx:idx+2])

    cnv.ctx.set_source_rgba(0.9, 0.9, 0.9, 1)
    cnv.ctx.set_line_width(0.01)
    cnv.ctx.move_to(0, 0.7)
    cnv.ctx.rel_curve_to(0.2, 0.25, 0.3, -0.25, 0.5, 0)
    cnv.ctx.rel_curve_to(0.2, 0.25, 0.3, -0.25, 0.5, 0)
    cnv.ctx.rel_line_to(0, -0.3)
    cnv.ctx.rel_curve_to(-0.2, 0.25, -0.1, -0.25, -0.5, 0)
    cnv.ctx.rel_curve_to(-0.2, 0.25, -0.1, -0.25, -0.5, 0)
    cnv.ctx.save()
    cnv.ctx.fill()
    cnv.ctx.restore()

#!/usr/bin/env python

import numpy as np
from math import pi

from src.draw import Canvas, normalize
from fn import Fn
from matplotlib import cm


def gen_along_sq(angle, lines, start, end, side):
    x_mid = np.random.uniform(start - 0.5 * np.tan(angle), end + 0.5 * np.tan(angle), lines)

    _x0 = np.zeros(lines)
    _x1 = np.ones(lines)
    if side is "left":
        _y0 = x_mid + np.tan(angle) * 0.5
        _y1 = x_mid - np.tan(angle) * 0.5
    elif side is "right":
        _y0 = x_mid - np.tan(angle) * 0.5
        _y1 = x_mid + np.tan(angle) * 0.5

    # y0 < 0
    _x0 = _x0 - (_y0 / np.tan(angle)) * (_y0 < 0)
    _y0 = _y0 - _y0 * (_y0 < 0)

    # y0 > 1
    _x0 = _x0 + ((_y0 - 1) / np.tan(angle)) * (_y0 > 1)
    _y0 = _y0 + (1 - _y0) * (_y0 > 1)

    # y1 < 0
    _x1 = _x1 + (_y1 / np.tan(angle)) * (_y1 < 0)
    _y1 = _y1 - _y1 * (_y1 < 0)

    # y1 > 1
    _x1 = _x1 - ((_y1 - 1) / np.tan(angle)) * (_y1 > 1)
    _y1 = _y1 + (1 -_y1) * (_y1 > 1)

    return _x0, _y0, _x1, _y1


# Document configuration
cnv_conf = {
    "fname": f"temp/{Fn().name()}",
    "dpi": 300,
    "width": 10,
    "height": 15,
    "bg_rgb": [(0.05, 0.05, 0.05), (0.15, 0.15, 0.15)]
}

n_lines = 1000
color_noise_var = 0.1
cm = cm.jet
alpha = 0.3
lw = 0.000001

# Draw to canvas
with Canvas(**cnv_conf) as cnv:

    x0, y0, x1, y1 = gen_along_sq(angle=0.1 * pi, lines=n_lines, start=0.15, end=0.8, side="left")

    for x0, y0, x1, y1 in zip(x0, y0, x1, y1):
        edge = [[x0, y0], [x1, y1]]
        cnv.draw_edge(edge, lw, (0.8, 0.8, 0.8, alpha))

    x0, y0, x1, y1 = gen_along_sq(angle=0.1 * pi, lines=n_lines, start=0.2, end=0.7, side="right")

    for x0, y0, x1, y1 in zip(x0, y0, x1, y1):
        edge = [[x0, y0], [x1, y1]]
        cnv.draw_edge(edge, lw, (0.8, 0.8, 0.8, alpha))

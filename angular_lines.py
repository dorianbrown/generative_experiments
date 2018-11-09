#!/usr/bin/env python

import cairo as cr
import numpy as np
from random import choice
from math import pi

from src.objects import DrawGraph
from src.draw import Canvas
from fn import Fn
from matplotlib import cm

# Constants


# Create graph


# Document configuration
cnv_conf = {
    "fname": f"temp/{Fn().name()}",
    "dpi": 300,
    "width": 10,
    "height": 20,
    "bg_rgb": [(0.05, 0.05, 0.05), (0.15, 0.15, 0.15)]
}

n_lines = 1000
cm = cm.viridis

# Draw to canvas
with Canvas(**cnv_conf) as cnv:

    angle = 0.5*pi*np.random.uniform()
    angle = 0.25*pi
    y0 = np.random.uniform(0.1*1, 1, n_lines)
    x0 = y0*np.tan(angle)
    col_mid = choice(y0)
    col_vec = (y0 - min(y0))/max(y0 - min(y0))
    colors = cm(col_vec, alpha=0.15)

    for x, y, col in zip(x0, y0, colors):
        edge = [[0, y], [x, 0]]
        cnv.draw_edge(edge, 0.00001, col)

#!/usr/bin/env python

import cairo as cr
import numpy as np
from random import choice
from math import pi

from src.objects import DrawGraph
from src.draw import Canvas, normalize
from fn import Fn
from matplotlib import cm


# Document configuration
cnv_conf = {
    "fname": f"temp/{Fn().name()}",
    "dpi": 300,
    "width": 10,
    "height": 20,
    "bg_rgb": [(0.05, 0.05, 0.05), (0.15, 0.15, 0.15)]
}

n_lines = 2000
noise = 0.5
color_noise_var = 0.1
cm = cm.jet
alpha = 0.1
lw = 0.0000025

# Draw to canvas
with Canvas(**cnv_conf) as cnv:

    # Angle1
    angle = 0.3 * pi
    y0 = np.random.uniform(0.1, 0.8, n_lines)
    x0 = y0*np.tan(angle)

    col_mid = choice(y0)
    col_vec = normalize(np.exp(-np.power(y0 - col_mid + np.random.normal(0, color_noise_var, len(y0)), 2)),
                        nmin=0, nmax=1)
    colors = cm(col_vec, alpha=alpha)

    for x, y, col in zip(x0, y0, colors):
        edge = [[0, y], [x, 0]]
        cnv.draw_edge(edge, lw, col)

    # Angle2
    angle = 0.45 * pi
    y0 = np.random.uniform(0.15, 0.7, n_lines)
    x0 = y0*np.tan(angle)

    col_mid = choice(y0)
    col_vec = normalize(np.exp(-np.power(y0 - col_mid + np.random.normal(0, color_noise_var, len(y0)), 2)),
                        nmin=0, nmax=1)
    colors = cm(col_vec, alpha=alpha)

    for x, y, col in zip(x0, y0, colors):
        edge = [[0, y], [x, 0]]
        cnv.draw_edge(edge, lw, col)

    # Angle3
    angle = 0.2 * pi
    y0 = np.random.uniform(0.6, 1.3, n_lines)
    x0 = y0*np.tan(angle)

    col_mid = choice(y0)
    col_vec = normalize(np.exp(-np.power(y0 - col_mid + np.random.normal(0, color_noise_var, len(y0)), 2)),
                        nmin=0, nmax=1)
    colors = cm(col_vec, alpha=alpha)

    for x, y, col in zip(x0, y0, colors):
        edge = [[0, y], [x, 0]]
        cnv.draw_edge(edge, lw, col)

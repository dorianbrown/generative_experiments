#!/usr/bin/env python

import cairo as cr
import numpy as np
from matplotlib import cm

from objects import DrawGraph
from rnd import rnd_crc_pnt
from draw import Canvas
from fn import Fn

init_vert = [0.5, 0.5]
edge_length = 0.0025

graph = DrawGraph()
graph.add_vertex(init_vert)

tries = 0
while len(graph.verts) < 17_500:
    if len(graph.verts) % 100 == 0 and tries == 0:
        print(f"vertices: {len(graph.verts)}")
    tries += 1
    new_vert = graph.verts[-1] + (1.25 + 0.1*tries)*edge_length*rnd_crc_pnt()
    # Don't draw edge if we wrap-around to other side
    if (new_vert != new_vert % 1).any():
        graph.add_vertex(new_vert % 1)
        continue
    # If we have a candidate point far away enough, add it with edge
    if graph.closest_vert_dist(new_vert) > 1.25*edge_length:
        if len(graph.verts) % 100 == 0:
            print(tries)
        tries = 0
        graph.add_vertex(new_vert)
        graph.add_edge(len(graph.verts) - 1, len(graph.verts) - 2)


# Document configuration
cnv_settings = {
    "fname": f"temp/{Fn().name()}",
    "dpi": 300,
    "width": 10,
    "height": 10,
    "bg_rgb": (0.05, 0.05, 0.05)
}

with Canvas(**cnv_settings) as cnv:
    cnv.ctx.set_line_cap(cr.LINE_CAP_ROUND)

    for edge in graph.edges:
        edge_coord = [graph.verts[i] for i in edge]
        if np.linalg.norm(edge_coord[0] - edge_coord[1]) < 2*edge_length:
            cnv.draw_edge(edge_coord, 0.01, [0.95, 0.95, 0.95])

#!/usr/bin/env python

import cairo as cr
import numpy as np

from objects import DrawGraph
from rnd import rnd_crc_pnt

# Fractional x,y coordinates [0,1]x[0,1]


init_vert = [0.01, 0.01]
edge_length = 0.01

graph = DrawGraph()
graph.add_vertex(init_vert)

tries = 0
while graph.verts.shape[0] < 10_000:
    if graph.verts.shape[0] % 100 == 0 and tries == 0:
        print(f"vertices: {len(graph.verts)} - tries: {tries}")
    tries += 1
    new_vert = graph.verts[-1] + tries/50*edge_length*rnd_crc_pnt()
    if (new_vert != new_vert % 1).any():
        graph.add_vertex(new_vert % 1)
        continue
    closest_dist, closest_vert = graph.closest_vert(new_vert)
    if closest_dist > edge_length:
        tries = 0
        graph.add_vertex(new_vert)
        graph.add_edge(len(graph.verts) - 1, len(graph.verts) - 2)


# Document configuration
fname = "example2.svg"
dpi = 300
width = 10 * dpi
height = 10 * dpi


def draw_edge(ctx, edge, line_width, rgb):
    edge = [[width, height]*v for v in edge]
    ctx.move_to(*edge[0])
    ctx.line_to(*edge[1])
    ctx.save()
    ctx.set_line_width(line_width)
    ctx.stroke_preserve()
    ctx.set_source_rgb(*rgb)
    ctx.fill()
    ctx.restore()


surf = cr.SVGSurface(fname, width, height)
ctx = cr.Context(surf)

# Set a background color
ctx.save()
ctx.set_source_rgb(1, 1, 1)
ctx.paint()
ctx.restore()
ctx.set_line_cap(cr.LINE_CAP_ROUND)

for edge in graph.edges:
    edge_coord = [graph.verts[i] for i in edge]
    if np.linalg.norm(edge_coord[0] - edge_coord[1]) < 0.02:
        draw_edge(ctx, edge_coord, 7, [0.3, 0.3, 0.3])

# Finishing export
surf.write_to_png("example3.png")
surf.finish()

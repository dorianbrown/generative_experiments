import cairocffi as cr
import logging
from math import sqrt
from time import time

import numpy as np
from webcolors import hex_to_rgb

log = logging.getLogger('my_logger')


class Canvas:

    def __init__(self, width, height, bg, fg, fname="tmp"):
        self.width = width
        self.height = height
        self.bg = bg
        self.fg = fg
        self.fname = fname
        self.t0 = time()

    def __enter__(self):
        log.debug(f"Creating canvas object with [{self.width}, {self.height}] dims")
        self.surface = cr.ImageSurface(cr.FORMAT_ARGB32, self.width, self.height)
        # Set background color
        self.ctx = cr.Context(self.surface)
        self.ctx.set_antialias(cr.ANTIALIAS_FAST)
        self.ctx.save()
        self.set_color(self.bg)
        self.ctx.paint()
        self.ctx.restore()
        # Transform coordinates so that origin is at bottom-right
        # Two operations, translate to bottom and flip y coordinate
        self.ctx.set_matrix(cr.Matrix(yy=-1, y0=self.height))

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close canvas and export it
        self.surface.write_to_png(f"{self.fname}.png")
        self.surface.finish()
        print(f"Total running time: {round(time() - self.t0)} seconds")
        print(f"Drawing saved to: {self.fname}.png")

    def draw_pixel(self, xy, rgba):
        # We need to shift the line by (1,1) in order to get a square
        to_xy = tuple(x + 1 for x in xy)
        self.draw_line(xy, to_xy, rgba)

    def draw_line(self, from_xy, to_xy, rgba=None, width=1):
        log.debug(f"Initializing line {from_xy} => {to_xy}")
        if rgba is None:
            rgba = self.fg
        self.ctx.move_to(*from_xy)
        self.ctx.line_to(*to_xy)
        self.set_color(rgba)
        self.ctx.set_line_width(width)
        self.ctx.stroke()
        log.debug(f"Drawing line")

    def set_color(self, color):
        # Sets line color to rgb, rgba or hex
        log.debug(f"Setting color to {color}")
        if len(color) == 3:
            self.ctx.set_source_rgb(*color)
        elif len(color) == 4:
            self.ctx.set_source_rgba(*color)
        elif len(color) == 7:
            rgb = list(hex_to_rgb(color))
            log.debug(f"Hex {color} converted to {rgb}")
            self.ctx.set_source_rgb(*rgb)

    def get_oob(self, pos):
        return np.all(np.logical_or(pos <= [0, 0], pos >= [self.width, self.height]), axis=1)

    def sandpaint(self, from_xy, to_xy, rgb=(0, 0, 0), alpha=0.001, n=100):
        # # Scale frequency to line length
        dist = sqrt(sum((px - qx) ** 2.0 for px, qx in zip(from_xy, to_xy)))
        n = round(n*dist)

        # Create n random points on line
        a = np.random.rand(n).reshape(-1, 1)
        from_xy = np.tile(from_xy, n).reshape(-1, 2)
        to_xy = np.tile(to_xy, n).reshape(-1, 2)
        sand_points = from_xy*a + to_xy*(1-a)

        for pnt in sand_points:
            self.draw_pixel(pnt, (*rgb, alpha))

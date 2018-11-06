import cairo as cr


class Canvas:

    def __init__(self, width, height, dpi, fname, bg_rgb):
        """
        Create a canvas object.
        :param width: Width in inch (of inner canvas)
        :param height: Height in inch (of inner canvas)
        :param dpi: Dots-per-inch of final png
        :param fname:
        :param bg_rgb:
        :param zoom: Fractional border size between outer and inner canvas
        """
        self.inner_width = width * dpi
        self.inner_height = height * dpi
        self.dpi = dpi
        self.fname = fname
        self.zoom_factor = 1.1
        if width > height:
            self.outer_width = self.inner_width * self.zoom_factor
            self.outer_height = self.inner_width * self.zoom_factor
        else:
            self.outer_width = self.inner_height * self.zoom_factor
            self.outer_height = self.inner_height * self.zoom_factor
        if len(bg_rgb) is 1:
            self.bg_rgb = bg_rgb[0]
            self.fg_rgb = bg_rgb[0]
        elif len(bg_rgb) is 2:
            self.bg_rgb = bg_rgb[0]
            self.fg_rgb = bg_rgb[1]

    def __enter__(self):
        self.surface = cr.SVGSurface(f"{self.fname}.svg",
                                     self.outer_width,
                                     self.outer_height)
        self.ctx = cr.Context(self.surface)

        self.ctx.save()
        self.ctx.set_source_rgb(*self.bg_rgb)
        self.ctx.paint()
        self.ctx.restore()

        # Paint inner background
        self.ctx.save()
        self.ctx.set_source_rgb(*self.fg_rgb)
        y_top = 0.5*(self.outer_height - self.inner_height)
        x_top = 0.5*(self.outer_width - self.inner_width)
        self.ctx.rectangle(x_top, y_top, self.inner_width, self.inner_height)
        self.ctx.fill()
        self.ctx.restore()

        xtrans = 0.5 * (self.outer_width - self.inner_width)
        ytrans = 0.5 * (self.outer_height - self.inner_height)
        xmult = self.inner_width
        ymult = self.inner_height

        trans_matrix = cr.Matrix(x0=xtrans, xx=xmult, y0=ytrans, yy=ymult, xy=0, yx=0)
        self.ctx.set_matrix(trans_matrix)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close canvas and export it
        self.surface.write_to_png(f"{self.fname}.png")
        self.surface.finish()

    def draw_edge(self, edge, line_width, rgb):
        self.ctx.set_source_rgba(*rgb)
        self.ctx.set_line_width(line_width * self.dpi)
        self.ctx.move_to(*edge[0])
        self.ctx.line_to(*edge[1])
        self.ctx.save()
        self.ctx.stroke_preserve()
        self.ctx.fill()
        self.ctx.restore()

import cairo as cr


class Canvas:

    def __init__(self, width, height, dpi, fname, bg_rgb):
        self.width = width*dpi
        self.height = height*dpi
        self.fname = fname
        self.bg_rgb = bg_rgb

    def __enter__(self):
        self.surface = cr.SVGSurface(f"{self.fname}.svg",
                                     self.width,
                                     self.height)
        self.ctx = cr.Context(self.surface)
        self.ctx.save()
        self.ctx.set_source_rgb(*self.bg_rgb)
        self.ctx.paint()
        self.ctx.restore()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close canvas and export it
        self.surface.write_to_png(f"{self.fname}.png")
        self.surface.finish()

    def draw_edge(self, edge, line_width, rgb):
        w, h = self.width, self.height
        edge = [[w, h]*v for v in edge]
        self.ctx.set_source_rgb(*rgb)
        self.ctx.move_to(*edge[0])
        self.ctx.line_to(*edge[1])
        self.ctx.save()
        self.ctx.set_line_width(line_width)
        self.ctx.stroke_preserve()
        self.ctx.fill()
        self.ctx.restore()
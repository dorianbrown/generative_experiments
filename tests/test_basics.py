import sys
import os
import logging

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.draw import Canvas
from src import rnd
from matplotlib.colors import CSS4_COLORS as colors

# logging.getLogger("my_logger").setLevel(logging.DEBUG)

# Shared variables

small_conf = {
    "width": 12,
    "height": 12,
    "bg": (255, 255, 255),
    "fg": (0, 0, 0)
}

big_conf = {
    "width": 500,
    "height": 500,
    "bg": (255, 255, 255),
    "fg": (0, 0, 0)
}

# Tests


def test_initialization():
    with Canvas(**small_conf) as c:
        a = 1


def test_lines_and_pixels():
    with Canvas(**small_conf) as c:
        # FIXME: Hex colors not working. Aqua+Orange: yes, tomato: no
        c.draw_pixel([1, 1], colors['aqua'])
        c.draw_line([1, 11], [11, 1])
        c.draw_pixel([10, 10], colors['darkorange'])

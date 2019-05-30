#!/usr/bin/env python
import numpy as np
from fn import Fn

from src.draw import Canvas
from src.rnd import rnd_crc


small_conf = {
    "width": 4000,
    "height": 4000,
    "bg": (0, 0, 0),
    "fg": (255, 255, 255, 1),
    "fname": Fn().name(),
}


food = np.array([3000, 3000])


with Canvas(**small_conf) as c:
    xy = np.array([0.5*c.width, 0.5*c.height])
    width = 10
    growth_vector = np.array([1, 1])/np.sqrt(2)
    speed = 25
    noise = 5
    food_strength = 1
    # at each time step, decrease width and length
    for i in range(1000):
        food_dir = (food - xy)/np.linalg.norm(food - xy)
        growth_dir = growth_vector * (1 - (speed - 1)/(i+1)) + rnd_crc(n=1)[0]*noise + food_dir*food_strength
        new_xy = xy + growth_dir
        c.draw_line(xy, new_xy, width= 2 + (width - 2)/(i + 1))
        growth_vector = growth_dir/np.linalg.norm(growth_dir)
        xy = new_xy

#!/usr/bin/env python
import numpy as np
from fn import Fn

from src.draw import Canvas
from src.rnd import rnd_crc


small_conf = {
    "width": 4000,
    "height": 4000,
    "bg": (0, 0, 0),
    "fg": (255, 255, 255, 0.25),
    "fname": Fn().name(),
}


def acc_vec(_pos, _mass):
    d2 = _pos @ (-2 * _pos.T)
    diag = -0.5 * np.einsum('ii->i', d2)
    d2 = d2 + diag + diag[:, None]
    np.einsum('ii->i', d2)[...] = 1
    return np.nansum((_pos[:, None, :] - _pos) * (_mass[:, None] * d2 ** -1.5)[..., None], axis=0)


with Canvas(**small_conf) as c:

    # Initial particle conditions
    n = 3000
    pos = np.random.uniform(0, 4000, (n, 2))
    mass = np.ones(n)*500
    # Add radial initial velocity
    vel = rnd_crc(n=n)
    dt = 0.5

    while pos.size > 1:
        acc = acc_vec(pos, mass)
        vel += acc*dt
        pos_new = pos + vel*dt

        for old, new, v in zip(pos, pos_new, np.linalg.norm(vel, axis=1)):
            alpha = min(1, 0.75 / v)
            c.draw_line(old, new, rgba=(255, 255, 255, alpha), width=4)

        # Remove points we don't want to draw
        oob_idx = c.get_oob(pos_new)
        remove_idx = oob_idx

        pos = pos_new[~remove_idx]
        mass = mass[~remove_idx]
        vel = vel[~remove_idx]
        if n > pos.size > 0:
            print(f"# Points left: {pos.size}")
            n = pos.size

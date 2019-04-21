#!/usr/bin/env python
import numpy as np

from src.draw import Canvas
from matplotlib import cm

small_conf = {
    "width": 4000,
    "height": 4000,
    "bg": (0, 0, 0),
    "fg": (255, 255, 255, 0.25)
}


def acc_vec(pos, mass):
    d2 = pos @ (-2 * pos.T)
    diag = -0.5 * np.einsum('ii->i', d2)
    d2 = d2 + diag + diag[:, None]
    np.einsum('ii->i', d2)[...] = 1
    return np.nansum((pos[:, None, :] - pos) * (mass[:, None] * d2 ** -1.5)[..., None], axis=0)


with Canvas(**small_conf) as c:

    # Initial particle conditions
    n = 2000
    # pos = np.random.multivariate_normal([500, 500], [[1000, 250], [250, 1000]], n)
    pos = np.random.uniform(0, 4000, (n, 2))
    mass = np.ones(n)*500
    # Add radial initial velocity
    vel = np.zeros((n, 2), dtype=np.float)
    dt = 0.5

    while pos.size > 1:
        acc = acc_vec(pos, mass)
        vel += acc*dt
        pos_new = pos + vel*dt

        for old, new, v in zip(pos, pos_new, np.linalg.norm(vel, axis=1)):
            alpha = min(1, 1 / v)
            color = (*cm.viridis(v/10)[:3], alpha)
            c.draw_line(old, new, rgba=color, width=4)

        # Remove points we don't want to draw
        oob_idx = c.get_oob(pos_new)
        # too_fast_idx = np.linalg.norm(vel, axis=1) > 8
        remove_idx = oob_idx # | too_fast_idx

        pos = pos_new[~remove_idx]
        mass = mass[~remove_idx]
        vel = vel[~remove_idx]
        if n > pos.size > 0:
            print(f"# Points: {pos.size}")
            print(f"Vel range: [{vel.min()}, {vel.max()}]")
            n = pos.size

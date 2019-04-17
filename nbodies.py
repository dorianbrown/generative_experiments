#!/usr/bin/env pypy3
import numpy as np

from src.draw import Canvas

small_conf = {
    "width": 2000,
    "height": 2000,
    "bg": (0, 0, 0),
    "fg": (255, 255, 255, 0.1)
}


def acc_vec(pos, mass):
    d2 = pos @ (-2 * pos.T)
    diag = -0.5 * np.einsum('ii->i', d2)
    d2 = d2 + diag + diag[:, None]
    np.einsum('ii->i', d2)[...] = 1
    return np.nansum((pos[:, None, :] - pos) * (mass[:, None] * d2 ** -1.5)[..., None], axis=0)


with Canvas(**small_conf) as c:

    # Initial particle conditions
    n = 5000
    # pos = np.random.multivariate_normal([500, 500], [[1000, 250], [250, 1000]], n)
    pos = np.random.uniform(0, 2000, (n, 2))
    mass = np.ones(n)*500
    # Add radial initial velocity
    vel = np.zeros((n, 2), dtype=np.float)
    dt = 0.25

    while pos.size > 1:
        acc = acc_vec(pos, mass)
        vel += acc*dt
        pos_new = pos + vel*dt

        for old, new in zip(pos, pos_new):
            c.draw_line(old, new)

        # Remove points no longer on canvas
        remove_idx = c.get_oob(pos_new)

        pos = pos_new[~remove_idx]
        mass = mass[~remove_idx]
        vel = vel[~remove_idx]
        if n > pos.size > 0:
            print(f"# Points: {pos.size}")
            print(f"Vel range: [{vel.min()}, {vel.max()}]")
            n = pos.size

import numpy as np


def rnd_crc_pnt(n=1):
    theta = np.random.uniform(0, 2*np.pi, n)
    return np.vstack((np.cos(theta), np.sin(theta))).T
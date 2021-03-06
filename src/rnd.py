import numpy as np


def rnd_crc(radius=1, n=1):
    # Uniformly choose angles in [0,2pi) for each point
    theta = np.random.uniform(0, 2 * np.pi, n)
    # Convert angles to (x,y) coordinates, add center, and convert to list
    return np.vstack((np.cos(theta), np.sin(theta))).T * radius

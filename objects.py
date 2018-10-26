import numpy as np


class DrawGraph:

    def __init__(self):
        self.verts = np.ndarray(shape=(0, 2), dtype=np.float_)
        self.edges = set()

    def __repr__(self):
        output = f"{self.__class__} has:\n " \
                 f"- {self.verts.shape[0]} vertices\n " \
                 f"- {int(self.edges.sum()/2)} edges"
        return output

    def add_vertex(self, pos):
        pos = np.array(pos)
        self.verts = np.vstack((self.verts, pos))

    def add_edge(self, ind_1, ind_2):
        if ind_1 == ind_2:
            raise ValueError
        self.edges.add((ind_1, ind_2))

    def closest_vert(self, pos, excluding=[]):
        dist = np.linalg.norm(self.verts - pos, axis=1)
        dist[excluding] += dist.max() + 1
        return dist.min(), dist.argmin()
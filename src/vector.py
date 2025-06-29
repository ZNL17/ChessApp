import numpy as np


class Vector:
    def __init__(self, values):
        self.v = np.array(values)

    def __add__(self, other):
        return Vector(self.v, other.v)

    def dot(self, other):
        return np.dot(self.v, other.v)

    def cross(self, other):
        return Vector(np.cross(self.v, other.v))

    def __repr__(self):
        return f"Vector({self.v})"

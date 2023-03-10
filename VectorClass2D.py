#2D Vector Class
import numpy as np
import matplotlib.pyplot as plt


class Vector2D:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        #self.z = z

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __subtract__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __dotprod__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    #def __vctprod__(self, other):
    #Use for when we cover 3D Vectors

    def length(self):
        return np.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        return Vector2D(self.x / self.length(), self.y / self.length())
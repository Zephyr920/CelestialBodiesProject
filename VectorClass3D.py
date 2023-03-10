#3D Vector Class
import numpy as np
import matplotlib.pyplot as plt


class Vector3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __dotprod__(self, other):
        return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __vectprod__(self, other):
        return Vector3D((self.y * other.z - self.z * other.y), - (self.x * other.z - self.z * other.x), (self.x * other.y - self.y * other.x))

    def length(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        return Vector3D(self.x / self.length(), self.y / self.length(), self.z / self.length())
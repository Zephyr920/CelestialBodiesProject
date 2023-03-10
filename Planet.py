#Planet Class
import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self, r, d, angle=0):
        self.radius = r
        self.distance = d
        self.angle = angle
        self.planets = None

    def show_sun(self):
        sun = plt.Circle((0, 0), self.radius, color='yellow', fill=True, label='Sun')
        plt.gca().add_artist(sun)

    def spawn_moons(self, total):
        self.planets = [None]*total
        for i in range(total):
            r = self.radius * 0.5
            d = np.random.randint(100, 200)
            self.planets[i] = Planet(r, d)

    def show_planet(self):
        celestial_body = plt.Circle((self.distance, self.distance*np.tan(self.angle)), self.radius, color='white', fill=True, label='Planet')
        plt.gca().add_artist(celestial_body)
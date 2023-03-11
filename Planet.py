#Planet Class
import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self, r, xpos, ypos, angle=0):
        self.radius = r
        #self.distance = d
        self.xpos = xpos
        self.ypos = ypos
        self.angle = angle
        self.planets = None

    def show_sun(self):
        sun = plt.Circle((self.xpos, self.ypos), self.radius, color='yellow', fill=True, label='Sun')
        plt.gca().add_artist(sun)

    def spawn_moons(self, total):
        self.planets = [None]*total
        for i in range(total):
            r = self.radius * 0.5
            xpos, ypos = np.random.randint(100, 200)
            self.planets[i] = Planet(r, np.sqrt(xpos**2 + ypos**2))

    def show_planet(self):
        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='white', fill=True, label='Planet')
        plt.gca().add_artist(celestial_body)
#Planet Class
import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self, xpos, ypos, xvel, yvel, m, r):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.mass = m
        self.radius = r
        #self.angle = angle
        #self.distance = d
        self.planets = []

    def show_properties(self):
        return self.xpos, self.ypos, self.xvel, self.yvel, self.mass, self.radius

    def show_sun(self):
        sun = plt.Circle((self.xpos, self.ypos), self.radius, color='yellow', fill=True, label='Sun')
        plt.gca().add_artist(sun)

    def spawn_moons(self, total):
        self.planets = []
        for i in range(total):
            r = self.radius * 0.5
            #d = np.random.uniform(100, 200)
            #xpos = np.random.randint(100, 200)
            #ypos = np.random.randint(100, 200)
            xpos = 0
            ypos = np.random.randint(100, 300)
            self.planets.append(Planet(xpos, ypos, 0, 0, 0, r))
        return self.planets

    def show_planet(self):
        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='white', fill=True, label='Planet')
        plt.gca().add_artist(celestial_body)

        if self.planets is not None:
            for planet in self.planets:
                planet.show_planet()
        #plt.plot(self.x_array, self.y_array, color = 'white', linestyle = '--')
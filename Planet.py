#Planet Class
import numpy as np
import matplotlib.pyplot as plt
import math


class Planet:
    AU = 149597871000
    G = 6.6743e-11
    DT = 3600
    SCALE = 250 / AU
    def __init__(self, xpos, ypos, xvel, yvel, mass, r):
        #self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.mass = mass
        self.radius = r
        self.planets = []
        #self.colour = colour

    def show_properties(self):
        return self.xpos, self.ypos, self.xvel, self.yvel, self.mass, self.radius

    def update_planet_position(self, other_planets):

        for other in other_planets:
            if other is not self:
                xdist = self.xpos - other.xpos
                ydist = self.ypos - other.ypos
                dist = np.sqrt(xdist**2 + ydist**2)
                angle = np.arctan2(ydist, xdist)

                ft = self.G * self.mass * other.mass / dist**2
                fx = ft * np.cos(angle)
                fy = ft * np.sin(angle)

                ax = fx / self.mass
                ay = fy / self.mass

                self.xvel += ax * self.DT
                self.yvel += ay * self.DT
                self.xpos += self.xvel * self.DT
                self.ypos += self.yvel * self.DT

        return self.xpos, self.ypos, self.xvel, self.yvel

    def show_sun(self):
        sun = plt.Circle((self.xpos*self.SCALE, self.ypos*self.SCALE), self.radius*self.SCALE, color='yellow', fill=True, label='Sun')
        plt.gca().add_artist(sun)

    def spawn_moons(self, total, other):
        self.planets = []
        for i in range(total):
            r = self.radius * 0.5
            #d = np.random.uniform(100, 200)
            xpos = np.random.randint(-100, 100)
            ypos = np.random.randint(-100, 100)
            #xpos = 0
            #ypos = np.random.randint(-100, 100)
            self.planets.append(Planet('moon', other.xpos+xpos, other.ypos+ypos, 0, 0, 0, r, None)) #Need to add that it's xpos and ypos from the planet
        return self.planets

    def show_moon(self):
        moon = plt.Circle((self.xpos*self.SCALE, self.ypos*self.SCALE), self.radius*self.SCALE, color='blue', fill=True)
        plt.gca().add_artist(moon)

    def show_planet(self):
        plt.xlim(-1000, 1000)
        plt.ylim(-1000, 1000)
        celestial_body = plt.Circle((self.xpos*self.SCALE, self.ypos*self.SCALE), 40, color='yellow', fill=True, label='body')
        plt.gca().add_artist(celestial_body)
        #plt.plot(self.x_array, self.y_array, color = 'white', linestyle = '--')
        if self.planets is not None:
            for planet in self.planets:
                planet.show_moon()
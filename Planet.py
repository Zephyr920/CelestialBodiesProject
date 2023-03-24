#Planet Class
import numpy as np
import matplotlib.pyplot as plt
import math

AU = 149597871000
G = 6.6743e-11
DT = 60
TIMESTEP = 3600 * 24 * 365

class Planet:
    def __init__(self, xpos, ypos, xvel, yvel, mass, r):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.mass = mass
        self.radius = r
        self.planets = []
        self.orbit = []

    def show_properties(self):
        return self.xpos, self.ypos, self.xvel, self.yvel, self.mass, self.radius, self.angle

    def update_planet_position(self, other):
        DT = 3600

        print("Initial xpos", self.xpos)
        xdist = self.xpos - other.xpos
        ydist = self.ypos - other.ypos
        dist = np.sqrt(xdist**2 + ydist**2)
        angle = np.arctan2(ydist, xdist) #radians
        print(dist)
        print("angle ", angle)

        ft = G * self.mass * other.mass / dist**2
        fx = ft * np.cos(np.radians(angle))
        fy = ft * np.sin(np.radians(angle))
        print("ft ", ft)
        print("fx ", fx)
        print("fy ", fy)
        print("Reverse: ", np.sqrt(fx**2 + fy**2))

        ax = fx / self.mass
        ay = fy / self.mass
        print("ax ", ax)
        print("ay ", ay)

        vxf = (ax * DT - self.xvel) * (-1)
        vyf = (ay * DT - self.yvel) * (-1)
        print("Velocity ", np.sqrt(vxf**2+vyf**2))

        self.xpos += vxf * DT
        self.ypos += vyf * DT
        print("final xpos ", self.xpos)

#About to get this bit to work
#    def simulate(self):
#        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='white', fill=True, label='Planet')
#        plt.gca().add_artist(celestial_body)
#        plt.pause(0.0001)
#        plt.show()
#        plt.clf()


    def show_sun(self):
        sun = plt.Circle((self.xpos, self.ypos), self.radius, color='yellow', fill=True, label='Sun')
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
            self.planets.append(Planet(other.xpos+xpos, other.ypos+ypos, 0, 0, 0, r)) #Need to add that it's xpos and ypos from the planet
        return self.planets


    def show_moon(self):
        moon = plt.Circle((self.xpos, self.ypos), self.radius, color='blue', fill=True)
        plt.gca().add_artist(moon)

    def show_planet(self):
        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='white', fill=True, label='Planet')
        plt.gca().add_artist(celestial_body)
        #plt.plot(self.x_array, self.y_array, color = 'white', linestyle = '--')
        if self.planets is not None:
            for planet in self.planets:
                planet.show_moon()
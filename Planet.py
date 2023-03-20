#Planet Class
import numpy as np
import matplotlib.pyplot as plt
import math

AU = 149597871000
G = 6.6743e-11
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

#    def update_planet_position(self, fx_total, fy_total, dt):
#        ax = fx_total / self.mass
#        ay = fy_total / self.mass
#        self.xvel += ax * dt
#        self.yvel += ay * dt
#        self.xpos += self.xvel * dt
#        self.ypos += self.yvel * dt

    def gravitational_attraction(self, other):
        xdist = other.xpos - self.xpos
        ydist = other.ypos - self.ypos
        distance = np.sqrt(xdist ** 2 + ydist ** 2)
        if xdist == 0:
            angle = 0
        else:
            angle = np.arctan(np.radians(ydist / xdist))

        ft = G * self.mass * other.mass / distance**2
        fx = np.cos(angle) * ft
        fy = np.sin(angle) * ft
        return fx, fy

    def update_position(self, planets):
        fx_total = 0
        fy_total = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.gravitational_attraction(planet)
            fx_total += fx
            fy_total += fy
        self.xvel += fx_total / self.mass * TIMESTEP
        self.yvel += fy_total / self.mass * TIMESTEP
        self.xpos += self.xvel * TIMESTEP
        self.ypos += self.yvel * TIMESTEP
        self.orbit.append((self.xpos, self.ypos))

    def update_planet_position(self, fx, fy, dt):
        if self.mass == 0:
            pass
        else:
            ax = fx / self.mass
            ay = fy / self.mass
            self.xvel += ax * dt
            self.yvel += ay * dt
            self.xpos += self.xvel * dt
            self.ypos += self.yvel * dt

    def update_planets(self, dt):
        for planet in self.planets:
            fx = 0
            fy = 0
            for other in self.planets:
                print(planet)
                if planet == other:
                    continue
                else:
                    r = np.sqrt(((planet.xpos - other.xpos) ** 2 + (planet.ypos - other.ypos) ** 2))
                    angle = math.atan2(planet.ypos - other.ypos, planet.xpos - other.xpos)
                    ft = G * planet.mass * other.mass / (r ** 2)
                    fx += ft * np.cos(angle)
                    fy += ft * np.sin(angle)
            planet.update_planet_position(fx, fy, dt)

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
        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='red', fill=True, label='Planet')
        plt.gca().add_artist(celestial_body)
        #plt.plot(self.x_array, self.y_array, color = 'white', linestyle = '--')
        if self.planets is not None:
            for planet in self.planets:
               planet.show_moon()
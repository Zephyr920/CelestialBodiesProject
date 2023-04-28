#Planet Class
import numpy as np
import matplotlib.pyplot as plt
import pygame


class Planet:
    AU = 149597871000
    G = 6.6743e-11
    DT = 3600
    SCALE = 250 / AU
    def __init__(self, xpos, ypos, zpos, xvel, yvel, zvel, mass, r, colour, vis_r):
        #self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.xvel = xvel
        self.yvel = yvel
        self.zvel = zvel
        self.mass = mass
        self.radius = r
        self.planets = []
        self.orbit = []
        self.orbitx = []
        self.orbity = []
        self.colour = colour
        self.vis_r = vis_r #Radius when we plot so it looks nice :D

    def show_properties(self):
        return self.xpos, self.ypos, self.xvel, self.yvel, self.mass, self.radius

    def force_calculation(self, other):
        xdist = other.xpos - self.xpos
        ydist = other.ypos - self.ypos
        dist = np.sqrt(xdist**2 + ydist**2)
        angle = np.arctan2(ydist, xdist)

        ft = self.G * self.mass * other.mass / dist**2
        fx = ft * np.cos(angle)
        fy = ft * np.sin(angle)
        return fx, fy

    def update_planet_position(self, planets):
        fxt = fyt = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.force_calculation(planet)
            fxt += fx
            fyt += fy

            ax = fxt / self.mass
            ay = fyt / self.mass

        self.xvel += ax * self.DT
        self.yvel += ay * self.DT
        self.xpos += self.xvel * self.DT
        self.ypos += self.yvel * self.DT

        self.orbit.append((self.xpos, self.ypos))
        self.orbitx.append(self.xpos)
        self.orbity.append(self.ypos)

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
        plt.xlim(800, 800)
        plt.ylim(800, 800)
        celestial_body = plt.Circle((self.xpos*self.SCALE, self.ypos*self.SCALE), self.vis_r, color=self.colour, fill=True, label='body')
        plt.gca().add_artist(celestial_body)
    def pygame_plot(self, win):
        x = self.xpos * self.SCALE + 800 / 2
        y = self.ypos * self.SCALE + 800 / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + 800 / 2
                y = y * self.SCALE + 800 / 2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.colour, False, updated_points, 2)

        pygame.draw.circle(win, self.colour, (x, y), self.vis_r)

    def pygame_forces(self, other):
        xdist = other.xpos - self.xpos
        ydist = other.ypos - self.ypos
        dist = np.sqrt(xdist**2 + ydist**2)

        ft = self.G * self.mass * other.mass / dist**2
        angle = np.arctan2(ydist, xdist)
        fx = np.cos(angle) * ft
        fy = np.sin(angle) * ft
        return fx, fy

    def pygame_update_position(self, planets):
        fxt = fyt = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.pygame_forces(planet)
            fxt += fx
            fyt += fy

        self.xvel += fxt / self.mass * self.DT
        self.yvel += fyt / self.mass * self.DT

        self.xpos += self.xvel * self.DT
        self.ypos += self.yvel * self.DT
        self.orbit.append((self.xpos, self.ypos))


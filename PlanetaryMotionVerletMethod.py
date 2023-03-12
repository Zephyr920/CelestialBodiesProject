import numpy as np

G = 6.6743e-11

class PlanetaryMotion:
    def __init__(self, planets):
        self.planets = planets

    def calculate_forces(self):
        for i in range(len(self.planets)):
            for j in range(i+1, len(self.planets)):
                pi = self.planets[i]
                pj = self.planets[j]

                dx = pj.xpos - pi.xpos
                dy = pj.ypos - pi.ypos
                dist = np.sqrt(dx**2 + dy**2)

                f = G * pi.mass * pj.mass / dist**2
                fx = f * dx / dist
                fy = f * dy / dist

                pi.xforce += fx
                pi.yforce += fy
                pj.xforce -= fx
                pj.yforce -= fy

    def update(self, dt):
        for planet in self.planets:
            ax = planet.xforce / planet.mass
            ay = planet.yforce / planet.mass

            planet.xpos += planet.xvel * dt + 0.5 * ax * dt**2
            planet.ypos += planet.yvel * dt + 0.5 * ay * dt**2

            planet.xvel += 0.5 * planet.xforce / planet.mass * dt
            planet.yvel += 0.5 * planet.yforce / planet.mass * dt

        self.calculate_forces()

        for planet in self.planets:
            ax = planet.xforce / planet.mass
            ay = planet.yforce / planet.mass

            planet.xvel += 0.5 * ax * dt
            planet.yvel += 0.5 * ay * dt
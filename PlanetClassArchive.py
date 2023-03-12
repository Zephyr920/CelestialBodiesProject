#Planet Class
import numpy as np
import matplotlib.pyplot as plt

#Constants
G = 6.6743e-11
DT = 3600
T_END = 365 * 24 * 3600

class Planet:

    #Initialize the class
    def __init__(self, xpos, ypos, xvel, yvel, m, r):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.mass = m
        self.radius = r
        #self.angle = angle
        #self.distance = d
        self.planets = None

        #Calculate initial acceleration of the planets
        self.ax = 0
        self.ay = 0
        self.update_acceleration()

        #Initialize arrays to store the position and velocity of the planet at each time step
        self.x_array = [self.xpos]
        self.y_array = [self.ypos]
        self.vx_array = [self.xvel]
        self.vy_array = [self.yvel]
        self.t_array = [0]
        self.dt = 3600

    #Show the properties the planet possesses
    def show_properties(self):
        return self.xpos, self.ypos, self.xvel, self.yvel, self.mass, self.radius

    def update_acceleration(self):
        ax = -G * self.mass * self.xpos / self.radius ** 3
        ay = -G * self.mass * self.ypos / self.radius ** 3

        self.ax = ax
        self.ay = ay

    def update_position(self):
        # Update the position of the planet using the Verlet algorithm
        self.xpos += self.xvel * dt + 0.5 * self.ax * dt ** 2
        self.ypos += self.yvel * dt + 0.5 * self.ay * dt ** 2

        # Update the acceleration of the planet
        self.update_acceleration()

        # Update the velocity of the planet
        self.xvel += 0.5 * (self.ax + self.ax) * dt
        self.yvel += 0.5 * (self.ay + self.ay) * dt

        # Append the new position and velocity to the arrays
        self.x_array.append(self.xpos)
        self.y_array.append(self.ypos)
        self.vx_array.append(self.xvel)
        self.vy_array.append(self.yvel)
        self.t_array.append(self.t_array[-1] + dt)

    #def show_sun(self):
    #    sun = plt.Circle((self.xpos, self.ypos), self.radius, color='yellow', fill=True, label='Sun')
    #    plt.gca().add_artist(sun)

    #def spawn_moons(self, total):
    #    self.planets = [None]*total
    #    for i in range(total):
    #        r = self.radius * 0.5
    #        xpos, ypos = np.random.randint(100, 200)
    #        self.planets[i] = Planet(r, np.sqrt(xpos**2 + ypos**2))

    def show_planet(self):
        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='white', fill=True, label='Planet')
        plt.gca().add_artist(celestial_body)
        #plt.plot(self.x_array, self.y_array, color = 'white', linestyle = '--')
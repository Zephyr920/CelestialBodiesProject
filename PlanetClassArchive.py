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
#    def show_properties(self):
#        return self.xpos, self.ypos, self.xvel, self.yvel, self.mass, self.radius

#    def update_acceleration(self):
#        ax = -G * self.mass * self.xpos / self.radius ** 3
#        ay = -G * self.mass * self.ypos / self.radius ** 3

#        self.ax = ax
#        self.ay = ay

#    def update_position(self):
        # Update the position of the planet using the Verlet algorithm
#        self.xpos += self.xvel * dt + 0.5 * self.ax * dt ** 2
#        self.ypos += self.yvel * dt + 0.5 * self.ay * dt ** 2

        # Update the acceleration of the planet
#        self.update_acceleration()

        # Update the velocity of the planet
#        self.xvel += 0.5 * (self.ax + self.ax) * dt
#        self.yvel += 0.5 * (self.ay + self.ay) * dt

        # Append the new position and velocity to the arrays
#        self.x_array.append(self.xpos)
#        self.y_array.append(self.ypos)
#        self.vx_array.append(self.xvel)
#        self.vy_array.append(self.yvel)
#        self.t_array.append(self.t_array[-1] + dt)

    #def show_sun(self):
    #    sun = plt.Circle((self.xpos, self.ypos), self.radius, color='yellow', fill=True, label='Sun')
    #    plt.gca().add_artist(sun)

    #def spawn_moons(self, total):
    #    self.planets = [None]*total
    #    for i in range(total):
    #        r = self.radius * 0.5
    #        xpos, ypos = np.random.randint(100, 200)
    #        self.planets[i] = Planet(r, np.sqrt(xpos**2 + ypos**2))

#    def show_planet(self):
#        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='white', fill=True, label='Planet')
#        plt.gca().add_artist(celestial_body)
#        plt.plot(self.x_array, self.y_array, color = 'white', linestyle = '--')



#ATTEMPT AT GETTING THE ORBITS TO WORK
#    def orbit(self):
#        orbital_speed = np.sqrt(self.xvel**2 + self.yvel**2)
#        self.angle += orbital_speed
#        if self.planets != None:
#            for i in range(len(self.planets)):
#                self.planets[i].orbit()
#            for planet in self.planets:
#                planet.orbit()

#    def show_celestial_body(self):
#        plt.fill_between([self.xpos, self.ypos], self.radius, self.radius, color='white')
#        plt.gca().add_patch(plt.Circle((self.distance*np.cos(self.angle), self.distance*np.sin(self.angle)), self.radius, color='white'))
#        if self.planets is not None:
#            for planet in self.planets:
#                planet.show_celestial_body()

#    def simulate(self):
#        plt.plot([planet.xpos for planet in self.planets], [planet.ypos for planet in self.planets], 'o')
#        plt.xlim(-1000, 1000)
#        plt.ylim(-1000, 1000)
#        plt.title('Simulation Visualization')
#        plt.xlabel('Displacement / m')
#        plt.ylabel('Displacement / m')
#        plt.gca().set_aspect('equal', adjustable='box')
#        plt.pause(0.00001)
#        plt.clf()

def attraction(self, other):
    xdist = other.xpos - self.xpos
    ydist = other.ypos - self.ypos
    distance = np.sqrt(xdist**2 + ydist**2)

    ft = G * self.mass * other.mass / distance**2
    fx = np.cos(self.angle) * ft
    fy = np.sin(self.angle) * ft
    return fx, fy

def update_position(self, planets):
    fx_total = 0
    fy_total = 0
    for planet in self.planets:
        if self == planet:
            continue

        fx, fy = self.attraction(planet)
        fx_total += fx
        fy_total += fy

    self.xvel += fx_total / self.mass * self.DT
    self.yvel += fy_total / self.mass * self.DT

    self.xpos += self.xvel * self.DT
    self.ypos += self.yvel * self.DT
    self.orbit.append((self.xpos, self.ypos))

#    def update_planet_position(self, fx_total, fy_total, dt):
#        ax = fx_total / self.mass
#        ay = fy_total / self.mass
#        self.xvel += ax * dt
#        self.yvel += ay * dt
#        self.xpos += self.xvel * dt
#        self.ypos += self.yvel * dt

#    def update_planet_position(self, fx, fy, dt):
#        if self.mass == 0:
#            pass
#        else:
#            ax = fx / self.mass
#            ay = fy / self.mass
#            self.xvel += ax * dt
#            self.yvel += ay * dt
#            self.xpos += self.xvel * dt
#            self.ypos += self.yvel * dt

#    def update_planets(self, dt):
#        for planet in self.planets:
#            fx = 0
#            fy = 0
#            for other in self.planets:
#                if planet == other:
#                    continue
#                else:
#                    r = np.sqrt(((planet.xpos - other.xpos) ** 2 + (planet.ypos - other.ypos) ** 2))
#                    angle = math.atan2(planet.ypos - other.ypos, planet.xpos - other.xpos)
#                    ft = G * planet.mass * other.mass / (r ** 2)
#                    fx += ft * np.cos(angle)
#                    fy += ft * np.sin(angle)
#            planet.update_planet_position(fx, fy, dt)

#    def update_position(self, planets):
#        fx_total = 0
#        fy_total = 0
#        for planet in planets:
#            if self == planet:
#                continue
#            fx, fy = self.gravitational_attraction(planet)
#            fx_total += fx
#            fy_total += fy
#        self.xvel += fx_total / self.mass * TIMESTEP
#        self.yvel += fy_total / self.mass * TIMESTEP
#        self.xpos += self.xvel * TIMESTEP
#        self.ypos += self.yvel * TIMESTEP
#        self.orbit.append((self.xpos, self.ypos))

#    def gravitational_attraction(self, other):
#        xdist = other.xpos - self.xpos
#        ydist = other.ypos - self.ypos
#        distance = np.sqrt(xdist ** 2 + ydist ** 2)
#        if xdist == 0:
#            angle = 0
#        else:
#            angle = np.arctan(np.radians(ydist / xdist))
#
#        ft = G * self.mass * other.mass / distance**2
#        fx = np.cos(angle) * ft
#        fy = np.sin(angle) * ft
#        return fx, fy

    #    def update_planet_position(self, fx_total, fy_total, dt):
    #        ax = fx_total / self.mass
    #        ay = fy_total / self.mass
    #        self.xvel += ax * dt
    #        self.yvel += ay * dt
    #        self.xpos += self.xvel * dt
    #        self.ypos += self.yvel * dt

#About to get this bit to work
#    def simulate(self):
#        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='white', fill=True, label='Planet')
#        plt.gca().add_artist(celestial_body)
#        plt.pause(0.0001)
#        plt.show()
#        plt.clf()
#Imma bout to need this real soon homie

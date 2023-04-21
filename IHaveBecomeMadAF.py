#Angry File
import numpy as np
import matplotlib.pyplot as plt

PAUSE = 0.00001

class Planet:
    G = 1
    DT = 36
    def __init__(self, xpos, ypos, xvel, yvel, mass, r):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.mass = mass
        self.radius = r

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



    def show_planet(self):
        plt.xlim(-1000, 1000)
        plt.ylim(-1000, 1000)
        celestial_body = plt.Circle((self.xpos, self.ypos), self.radius, color='black', fill=True, label='body')
        plt.gca().add_artist(celestial_body)

#Stopping Caps
#xpos, ypos, xvel, yvel, m, r
planet_1 = Planet(0, 0, 0, 0, 2000, 35)
planet_2 = Planet(200, 150, 0.1, 0.2, 25, 15)
planet_3 = Planet(-500, -450, 0.2, 0.5, 50, 20)

planet_array = [planet_1, planet_2, planet_3]

for i in range(len(planet_array)):
    print("Initial xpos: ", planet_array[0].xpos)
    planet_array[i].show_planet()
    planet_array[i].update_planet_position(planet_array)
    print("Final xpos: ", planet_array[0].xpos)
    plt.pause(PAUSE)
    plt.cla()

for n in range(10):
    z = 0
    for j in range(len(planet_array)):
        print("Initial xpos: ", planet_array[0].xpos)
        planet_array[j].show_planet()
        planet_array[j].update_planet_position(planet_array)
        print("Final xpos: ", planet_array[0].xpos) #So the data is carried onwards.
        plt.pause(PAUSE)
        plt.clf()
    z += 1

plt.show()
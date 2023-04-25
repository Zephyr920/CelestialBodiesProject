#Main File
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Planet as p
import PlanetsData as psd

TIMESTEP = 3600
PAUSE = 0.001
planet_array = []

data_list, xpos, ypos, xvel, yvel, mass, radius = psd.load_data('PlanetData.csv')

#Creates 10 objects for each 'planet' from Sun to Pluto. To be used for that actual calculations
for i, row in enumerate(data_list):
    var_name = f'planet_{i}'
    locals()[var_name] = p.Planet(float(xpos[i]), float(ypos[i]), float(xvel[i]), float(yvel[i]), float(mass[i]), float(radius[i])) #Yes I know! Do I care? Nope!
    planet_array.append(locals()[var_name])

print(planet_array)

fig, ax = plt.subplots()
ax.set_xlim(-0.1e10, 0.1e10)
ax.set_ylim(-0.1e10, 0.1e10)
ax.set_aspect('equal')
def update_plot(frame):
    for i in range(len(planet_array)):
        planet_array[i].update_planet_position(planet_array)
        ax.clear()
        ax.plot(planet_0.xpos, planet_0.ypos, 'ro')
        ax.set_xlim(-0.1e10, 0.1e10)
        ax.set_ylim(-0.1e10, 0.1e10)
        ax.set_aspect('equal')

ani = FuncAnimation(fig, update_plot, frames=365, interval=10)
plt.show()


#fig, ax = plt.subplots()
#ax.plot(planet_0.xpos, planet_0.ypos, 'ro')
#ax.set_xlim(0, 1e10)
#ax.set_ylim(0, 1e10)
#ax.set_aspect('equal')


#for i in range(365*24):
#    for j in range(len(planet_array)):
#        planet_array[j].update_planet_position(planet_array, TIMESTEP)
#        ax.clear()
#        ax.plot(planet_0.xpos, planet_0.ypos, 'ro')
#        ax.set_xlim(0, 0.1e10)
#        ax.set_ylim(0, 0.1e10)
#        ax.set_aspect('equal')
#        plt.pause(0.00001)
#    print("Day {}: x = {:.3f}, y = {:.3f}, vx = {:.3f}, vy = {:.3f}".format(i+1, planet_0.xpos, planet_0.ypos, planet_0.xvel, planet_0.yvel))



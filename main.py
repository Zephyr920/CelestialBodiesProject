#Main File
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Planet as p
import PlanetsData as psd

AU = 149597871000
TIMESTEP = 3600
PAUSE = 0.001
SCALE = 250 / AU

sun = p.Planet(1.81899E+08, 9.83630E+08, -1.58778E+07, -1.12474E+01, 7.54876E+00, 2.68723E-01, 1.98854E+30, 6.95500E+08, 'yellow', 30)
mercury = p.Planet(-5.67576E+10, -2.73592E+10, 2.89173E+09, 1.16497E+04, -4.14793E+04, -4.45952E+03, 3.30200E+23, 2.44000E+06, 'white', 6)
venus = p.Planet(4.28480E+10, 1.00073E+11, -1.11872E+09, -3.22930E+04, 1.36960E+04, 2.05091E+03, 4.86850E+24, 6.05180E+06, 'white', 8)
earth = p.Planet(-1.43778E+11, -4.00067E+10, -1.38875E+07, 7.65151E+03, -2.87514E+04, 2.08354E+00, 5.97219E+24, 6.37101E+06, 'blue', 12)
mars = p.Planet(-1.14746E+11, -1.96294E+11, -1.32908E+09, 2.18369E+04, -1.01132E+04, -7.47957E+02, 6.41850E+23, 3.38990E+06, 'red', 13)
jupiter = p.Planet(-5.66899E+11, -5.77495E+11, 1.50755E+10, 9.16793E+03, -8.53244E+03, -1.69767E+02, 1.89813E+27, 6.99110E+07, 'white', 18)
saturn = p.Planet(8.20513E+10, -1.50241E+12, 2.28565E+10, 9.11312E+03, 4.96372E+02, -3.71643E+02, 5.68319E+26, 5.82320E+07, 'white', 15)
uranus = p.Planet(2.62506E+12, 1.40273E+12, -2.87982E+10, -3.25937E+03, 5.68878E+03, 6.32569E+01, 8.68103E+25, 2.53620E+07, 'white', 13)
neptune = p.Planet(4.30300E+12, -1.24223E+12, -7.35857E+10, 1.47132E+03, 5.25363E+03, -1.42701E+02, 1.02410E+26, 2.46240E+07, 'white', 9)
pluto = p.Planet(1.65554E+12, -4.73503E+12, 2.77962E+10, 5.24541E+03, 6.38510E+02, -1.60709E+03, 1.30700E+22, 1.19500E+06, 'white', 4)

planet_array = [sun, mercury, venus]

#fig, ax = plt.subplots()
#ax.set_xlim(-0.1e10, 0.1e10)
#ax.set_ylim(-0.1e10, 0.1e10)
#ax.set_aspect('equal')
#def update_plot(frame):
#    for i in range(len(planet_array)):
#        planet_array[i].update_planet_position(planet_array)
#        ax.clear()
#        ax.plot(planet_0.xpos, planet_0.ypos, 'ro')
#        ax.set_xlim(-0.1e10, 0.1e10)
#        ax.set_ylim(-0.1e10, 0.1e10)
#        ax.set_aspect('equal')

#ani = FuncAnimation(fig, update_plot, frames=365, interval=10)
#plt.show()

while True:
    for planet in planet_array:
        plt.plot(planet.xpos*SCALE, planet.ypos*SCALE, '.')
        plt.plot(planet.xpos*SCALE, planet.ypos*SCALE)
        plt.xlim(-1000, 1000)
        plt.ylim(-1000, 1000)
        plt.gca().set_aspect('equal', adjustable='box')
        #planet.show_planet()
        planet.update_planet_position(planet_array)
    plt.pause(0.0000001)
    plt.clf()






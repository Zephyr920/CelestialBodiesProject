#Main File
import numpy as np
import matplotlib.pyplot as plt
import Planet as p
import PlanetsData as psd
import PlanetaryMotionVerletMethod as pm

data_list, xpos, ypos, xvel, yvel, mass, radius = psd.load_data('PlanetData.csv')

#Creates 10 objects for each 'planet' from Sun to Pluto
for i, row in enumerate(data_list):
    var_name = f'planet_{i}'
    locals()[var_name] = p.Planet(float(xpos[i]), float(ypos[i]), float(xvel[i]), float(yvel[i]), float(mass[i]), float(radius[i])) #Yes I know! Do I care? Nope!

#visualize_planets_ypos = []
#planet_0.show_sun()
#planet_1.show_planet()

visualize_planets_names = ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
visualize_planets_xpos = [0, 50, 75, 100, 150, 250, 305, 360, 420, 480]
visualize_planets_ypos = [0, 50, 0, -100, 0, -250, 0, -360, 0, -480]
visualize_planets_xvel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
visualize_planets_yvel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
visualize_planets_mass = [1000, 20, 40, 50, 55, 85, 65, 75, 80, 10]
visualize_planets_radius = [25, 5, 5, 7, 7, 20, 5, 5, 15, 2]



for i in range(len(visualize_planets_names)):
    visualize_planets_names[i] = p.Planet(visualize_planets_xpos[i], visualize_planets_ypos[i], visualize_planets_xvel[i], visualize_planets_yvel[i], visualize_planets_mass[i], visualize_planets_radius[i])

planet = p.Planet(150, 0, 5, 10, 100, 5)
planet2 = p.Planet(0, 0, 0, 0, 500, 10)
planetary_system = pm.PlanetaryMotion([planet, planet2])


plt.figure(figsize=(6, 6))
plt.axis([-500, 500, -500, 500])
plt.gca().set_facecolor((0, 0, 0))
plt.title('Simulation in Space')
plt.xlabel('Displacement')
plt.ylabel('Displacement')
plt.gca().set_aspect('equal', adjustable='box')

planet.show_planet()
planet2.show_planet()

plt.legend()

dt = 100
num_steps = 1000
for i in range(num_steps):
    planetary_system.update(dt)

#for j in range(len(visualize_planets_names)):
#    visualize_planets_names[j].show_planet()

plt.show()



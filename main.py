#Main File
import numpy as np
import matplotlib.pyplot as plt
import Planet as p
import PlanetsData as psd

data_list, xpos, ypos, radius = psd.load_data('PlanetData.csv')


for i, row in enumerate(data_list):
    var_name = f'planet_{i}'
    locals()[var_name] = p.Planet(float(radius[i]), float(xpos[i]), float(ypos[i]), 0) #Yes I know! Do I care? Nope!



sun = p.Planet(50, 0, 0, 0)
planet = p.Planet(15, 0, 200, np.pi)
plt.figure(figsize=(6, 6))
plt.axis([-500, 500, -500, 500])
plt.gca().set_facecolor((0, 0, 0))
sun.show_sun()
planet.show_planet()
#planet_0.show_sun()
#planet_1.show_planet()
plt.title('Simulation in Space')
plt.xlabel('Displacement')
plt.ylabel('Displacement')
plt.gca().set_aspect('equal', adjustable='box')

#plt.legend()
plt.show()



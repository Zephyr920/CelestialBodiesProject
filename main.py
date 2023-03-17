#Main File
#Testing Commits
import numpy as np
import matplotlib.pyplot as plt
import Planet as p
import PlanetsData as psd
#import PlanetaryMotionVerletMethod as pm

data_list, xpos, ypos, xvel, yvel, mass, radius = psd.load_data('PlanetData.csv')

#Creates 10 objects for each 'planet' from Sun to Pluto. To be used for that actual calculations
for i, row in enumerate(data_list):
    var_name = f'planet_{i}'
    locals()[var_name] = p.Planet(float(xpos[i]), float(ypos[i]), float(xvel[i]), float(yvel[i]), float(mass[i]), float(radius[i])) #Yes I know! Do I care? Nope!

#visualize_planets_ypos = []
#planet_0.show_sun()
#planet_1.show_planet()

#Initial Planet Visualization Arrays to prop the simulation all I took out was sun, 0, 0, 0, 0, 1000, 25, 0
#visualize_planets_names = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
#visualize_planets_xpos = [50, 75, 100, 150, 250, 305, 360, 420, 480]
#visualize_planets_ypos = [50, 0, -100, 0, -250, 0, -360, 0, -480]
#visualize_planets_xvel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#visualize_planets_yvel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#visualize_planets_mass = [20, 40, 50, 55, 85, 65, 75, 80, 10] #1000
#visualize_planets_radius = [5, 5, 7, 7, 20, 5, 5, 15, 2] #25
#visualize_planets_moons = [0, 0, 1, 2, 9, 8, 6, 5, 3]


#Bad Practice but archived for potential future use?
#for i in range(len(visualize_planets_names)):
#    visualize_planets_names[i] = p.Planet(visualize_planets_xpos[i], visualize_planets_ypos[i], visualize_planets_xvel[i], visualize_planets_yvel[i], visualize_planets_mass[i], visualize_planets_radius[i])

#Creating the planet objects and their number of moons
#object = p.Planet(xpos, ypos, xvel, yvel, mass, radius)
visual_sun = p.Planet(0, 0, 0, 0, 500, 10)
visual_mercury = p.Planet(150, 0, 5, 10, 100, 5)
visual_venus = p.Planet(250, 0, 10, 15, 110, 6)
visual_earth = p.Planet(300, 125, 20, 25, 140, 8)
visual_mars = p.Planet(-350, -150, 20, 20, 145, 8.5)
visual_moon_array = [0, 0, 1, 1]

#Complete Planet Visualization Array
visual_planets_array = [visual_mercury, visual_venus, visual_earth, visual_mars]

plt.figure(figsize=(6, 6))
plt.axis([-1000, 1000, -1000, 1000])
plt.gca().set_facecolor((0, 0, 0))
plt.title('Simulation in Space')
plt.xlabel('Displacement')
plt.ylabel('Displacement')
plt.gca().set_aspect('equal', adjustable='box')

for n in range(len(visual_planets_array)):
    visual_planets_array[n].spawn_moons(visual_moon_array[n], visual_planets_array[n])
    visual_planets_array[n].show_planet()


#Using Dynamic Variable Naming, Bad Practice
#visual_sun.show_sun()
#for j in range(len(visualize_planets_names)):
#    visualize_planets_names[j].spawn_moons(visualize_planets_moons[j], visualize_planets_names[j])
#    visualize_planets_names[j].show_planet()

plt.legend()
plt.show()



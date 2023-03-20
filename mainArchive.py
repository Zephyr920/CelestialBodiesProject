import numpy as np
import matplotlib.pyplot as plt
import Planet as p
import PlanetsData as psd

#Initial Planet Visualization Arrays to prop the simulation all I took out was sun, 0, 0, 0, 0, 1000, 25, 0
#visualize_planets_names = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
#visualize_planets_xpos = [50, 75, 100, 150, 250, 305, 360, 420, 480]
#visualize_planets_ypos = [50, 0, -100, 0, -250, 0, -360, 0, -480]
#visualize_planets_xvel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#visualize_planets_yvel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#visualize_planets_mass = [20, 40, 50, 55, 85, 65, 75, 80, 10] #1000
#visualize_planets_radius = [5, 5, 7, 7, 20, 5, 5, 15, 2] #25
#visualize_planets_moons = [0, 0, 1, 2, 9, 8, 6, 5, 3]


#TO BE USED WITH ORBIT IN PLANET_CLASS_ARCHIVE
#for n in range(1000):
# visual_sun.show_sun()
#    plt.cla()
#    visual_earth.show_celestial_body()
#    visual_earth.orbit()
#    plt.pause(1)
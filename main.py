#Main File
#Testing Commits
import numpy as np
import matplotlib.pyplot as plt
import Planet as p
import PlanetsData as psd

dt = 3600 # time step in seconds
t = 0 # current time in seconds
t_end = 3600 * 24 * 365# end time in seconds


data_list, body, xpos, ypos, xvel, yvel, mass, radius, colour = psd.load_data('PlanetData.csv')

#Creates 10 objects for each 'planet' from Sun to Pluto. To be used for that actual calculations
for i, row in enumerate(data_list):
    var_name = f'planet_{i}'
    locals()[var_name] = p.Planet(str(body), float(xpos[i]), float(ypos[i]), float(xvel[i]), float(yvel[i]), float(mass[i]), float(radius[i]), str(colour)) #Yes I know! Do I care? Nope!



#visualize_planets_ypos = []
#planet_0.show_sun()
#planet_1.show_planet()

#Bad Practice but archived for potential future use?
#for i in range(len(visualize_planets_names)):
#    visualize_planets_names[i] = p.Planet(visualize_planets_xpos[i], visualize_planets_ypos[i], visualize_planets_xvel[i], visualize_planets_yvel[i], visualize_planets_mass[i], visualize_planets_radius[i])

#Creating the planet objects and their number of moons
#object = p.Planet(name, xpos, ypos, xvel, yvel, mass, radius, colour)
visual_sun = p.Planet('Sun', 0, 0, 0, 0, 500, 15, 'yellow')
visual_mercury = p.Planet('Mercury', 150, 0, 5, 10, 100, 5, 'white')
visual_venus = p.Planet('Venus', 250, 0, 10, 15, 110, 6, 'white')
visual_earth = p.Planet('Earth', 300, 125, 20, 25, 140, 8, 'green')
visual_mars = p.Planet('Mars', -350, -150, 20, 20, 145, 8.5, 'red')
visual_jupiter = p.Planet('Jupiter', 0, -300, 15, 5, 200, 12, 'blue')
visual_saturn = p.Planet('Saturn', -300, 0, 10, 10, 185, 10, 'white')
visual_uranus = p.Planet('Uranus', -50, 340, 0, 25, 150, 9, 'white')
visual_neptune = p.Planet('Neptune', -500, -500, 0, 5, 123, 6, 'white')
visual_pluto = p.Planet('Pluto', -800, 950, 2, 5, 45, 2, 'red')
visual_moon_array = [0, 0, 1, 1, 9, 7, 6, 5, 1]

#Complete Planet Visualization Array
visual_planets_array = [visual_mercury, visual_venus, visual_earth, visual_mars, visual_jupiter, visual_saturn, visual_uranus, visual_neptune, visual_pluto]



plt.figure(figsize=(6, 6))
plt.xlim(-1000, 1000)
plt.ylim(-1000, 1000)
plt.gca().set_facecolor((0, 0, 0))
plt.title('Simulation in Space')
plt.xlabel('Displacement')
plt.ylabel('Displacement')
plt.gca().set_aspect('equal', adjustable='box')

#visual_sun.show_sun()
#visual_earth.show_planet()
print(planet_3.xpos)
planet_3.update_planet_position(planet_0)
print(planet_3.xpos) #Debugging purposes stop the bulli pls okay thank you

visual_sun.show_sun()
for n in range(len(visual_planets_array)):
    visual_planets_array[n].spawn_moons(visual_moon_array[n], visual_planets_array[n])
    visual_planets_array[n].show_planet()

#Using Dynamic Variable Naming, Bad Practice
#visual_sun.show_sun()
#for j in range(len(visualize_planets_names)):
#    visualize_planets_names[j].spawn_moons(visualize_planets_moons[j], visualize_planets_names[j])
#    visualize_planets_names[j].show_planet()

#while t < t_end:
#    t += dt
#    plt.clf()
#    for planet in visual_planets_array:
#        planet.update_planets(dt)
#        planet.show_planet()
#    visual_sun.show_sun()
#    plt.xlim([-1200, 1200])
#    plt.ylim([-1200, 1200])
#    plt.gca().set_aspect('equal')
#    plt.legend(loc='upper right')
    #plt.pause(0.01)


plt.legend()
plt.show()

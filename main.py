#Main File
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Planet as p
import PlanetsData as psd

NUM_TIMESTEPS = 36000
PAUSE = 0.001
planet_array = []

data_list, xpos, ypos, xvel, yvel, mass, radius = psd.load_data('PlanetData.csv')

#Creates 10 objects for each 'planet' from Sun to Pluto. To be used for that actual calculations
for i, row in enumerate(data_list):
    var_name = f'planet_{i}'
    locals()[var_name] = p.Planet(float(xpos[i]), float(ypos[i]), float(xvel[i]), float(yvel[i]), float(mass[i]), float(radius[i])) #Yes I know! Do I care? Nope!
    planet_array.append(locals()[var_name])

print(planet_array)

#Creating the planet objects and their number of moons
#object = p.Planet(name, xpos, ypos, xvel, yvel, mass, radius, colour)
#visual_sun = p.Planet('Sun', 0, 0, 0, 0, 500, 15, 'yellow')
#visual_mercury = p.Planet('Mercury', 150, 0, 5, 10, 100, 5, 'white')
#visual_venus = p.Planet('Venus', 250, 0, 10, 15, 110, 6, 'white')
#visual_earth = p.Planet('Earth', 300, 125, 20, 25, 140, 8, 'green')
#visual_mars = p.Planet('Mars', -350, -150, 20, 20, 145, 8.5, 'red')
#visual_jupiter = p.Planet('Jupiter', 0, -300, 15, 5, 200, 12, 'blue')
#visual_saturn = p.Planet('Saturn', -300, 0, 10, 10, 185, 10, 'white')
#visual_uranus = p.Planet('Uranus', -50, 340, 0, 25, 150, 9, 'white')
#visual_neptune = p.Planet('Neptune', -500, -500, 0, 5, 123, 6, 'white')
#visual_pluto = p.Planet('Pluto', -800, 950, 2, 5, 45, 2, 'red')
#visual_moon_array = [0, 0, 1, 1, 9, 7, 6, 5, 1]

#Complete Planet Visualization Array
#visual_planets_array = [visual_mercury, visual_venus, visual_earth, visual_mars, visual_jupiter, visual_saturn, visual_uranus, visual_neptune, visual_pluto]

#planet_0.show_planet()
#print(planet_0.xpos*(250/149597871000), planet_0.ypos*(250/149597871000), planet_0.radius*(250/149597871000))
#planet_1.show_planet()
#print(planet_1.xpos*(250/149597871000), planet_1.ypos*(250/149597871000), planet_1.radius*(250/149597871000))

#plt.figure(figsize=(6, 6))
#plt.xlim(-12, 12)
#plt.ylim(-12, 12)
#plt.gca().set_facecolor((0, 0, 0))
#plt.title('Simulation in Space')
#plt.xlabel('Displacement')
#plt.ylabel('Displacement')
#plt.gca().set_aspect('equal', adjustable='box')


for i in range(len(planet_array)):
    print("Initial xpos: ", planet_array[0].xpos)
    planet_array[i].show_planet()
    planet_array[i].update_planet_position(planet_array)
    print("Final xpos: ", planet_array[0].xpos)
for j in range(len(planet_array)):
    print("Initial xpos: ", planet_array[0].xpos)
    planet_array[j].show_planet()
    planet_array[j].update_planet_position(planet_array)
    print("Final xpos: ", planet_array[0].xpos) #So the data is carried onwards.

plt.show()


#for i in range(len(planet_array)):
#    fig, ax = plt.subplots(figsize=(8,8))
#    ax.set_xlabel('X Position (AU)')
#    ax.set_ylabel('Y Position (AU)')
#    ax.set_title('Solar System')

    # set up plot window
#    plt.xlim(-1000, 1000)
#    plt.ylim(-1000, 1000)
#    planet_array[i].show_planet()
#    planet_array[i].update_planet_position(planet_array)
#    plt.show()
#    print("You are here")
#    plt.clf()
#    plt.pause(PAUSE)


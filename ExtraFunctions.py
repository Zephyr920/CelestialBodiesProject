# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv
    
# Open the file in 'r' mode, not 'rb'
csv_file = open('horizons_results_earth.csv','r')
earth_xtraj = []
earth_ytraj = []
earth_ztraj = []
earth_xvel = []
earth_yvel = []
earth_zvel = []


# Split columns while reading
for x, y, z, vx,vy,vz in csv.reader(csv_file, delimiter=','):
    # Append each variable to a separate list
    if(x[:3]) == "ï»¿":
        earth_xtraj.append(float(x[3:])*1e3)
    else:
        earth_xtraj.append(float(x)*1e3)
    earth_ytraj.append(float(y)*1e3)
    earth_ztraj.append(float(z)*1e3)
    earth_xvel.append(float(vx)*1e3)
    earth_yvel.append(float(vy)*1e3)
    earth_zvel.append(float(vz)*1e3)

def com(planet_array):
    mass_pos_sum = np.array([0.0,0.0,0.0])
    mass = 0
    for planet in planet_array:
        pos = np.array([planet.xpos,planet.ypos,planet.zpos])
        m_pos = planet.mass * pos
        mass += planet.mass
        mass_pos_sum += m_pos
    mass_pos_sum = mass_pos_sum / mass
    return mass_pos_sum
        

def error_from_exact(planet_array,dt):
    earth = planet_array[3]
    plt.plot(np.linspace(0,8768,len(earth.orbitx)),earth.orbitx)
    plt.plot(earth_xtraj)
    plt.show()

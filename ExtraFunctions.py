# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:57:58 2023

@author: Agustin
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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
    massPos_sum = np.array([0.0,0.0,0.0])
    mass = 0
    for planet in planet_array:
        pos = np.array([planet.xpos,planet.ypos,planet.zpos])
        m_pos = planet.mass * pos
        mass += planet.mass
        massPos_sum += m_pos
    massPos_sum = massPos_sum / mass
    return massPos_sum
        

def error_from_exact(planet_array,dt):
    earth = planet_array[3]
    plt.plot(np.linspace(0,8768,len(earth.orbitx)),earth.orbitx)
    plt.plot(earth_xtraj)
    plt.show()

def truncation_errors(dt,tmax,planet_array): 
    for i in range(1,4):
        t = 0
        trunc_error = 1
        while t <= tmax:
            if i == 1:
                for planet in planet_array:
                    initialPosVel = [planet.xpos,planet.ypos,planet.zpos,planet.xvel,planet.yvel,planet.zvel]
                    planet.update_planet_position_euler(planet_array,dt)
                    planet.update_planet_position_euler(planet_array,dt)
                    dt_two_steps = [planet.xpos,planet.ypos,planet.zpos]
                    del planet.orbitx[-1]
                    del planet.orbitx[-1]
                    del planet.orbity[-1]
                    del planet.orbity[-1]
                    del planet.orbitz[-1]
                    del planet.orbitz[-1]
                    planet.xpos,planet.ypos,planet.zpos = initialPosVel[0],initialPosVel[1],initialPosVel[2]
                    planet.xvel,planet.yvel,planet.zvel = initialPosVel[3],initialPosVel[4],initialPosVel[5]
                    planet.update_planet_position_euler(planet_array,2*dt)
                    if(len(planet.orbitx) != 0):
                        del planet.orbitx[-1]
                        del planet.orbity[-1]
                        del planet.orbitz[-1]
                    two_dt_one_steps = [planet.xpos,planet.ypos,planet.zpos]
                    planet.xpos,planet.ypos,planet.zpos = initialPosVel[0],initialPosVel[1],initialPosVel[2]
                    planet.xvel,planet.yvel,planet.zvel = initialPosVel[3],initialPosVel[4],initialPosVel[5]
                    planet.update_planet_position_euler(planet_array,dt)
                    trunc_error = trunc_error * (np.abs(1 - (np.sum(np.divide(two_dt_one_steps,dt_two_steps))/3))+1)
                    planet.truncation_error_euler.append(trunc_error)
            if i == 2:
                for planet in planet_array:
                    initialPosVel = [planet.xpos,planet.ypos,planet.zpos,planet.xvel,planet.yvel,planet.zvel]
                    planet.update_planet_position_rk4(planet_array,dt)
                    planet.update_planet_position_rk4(planet_array,dt)
                    dt_two_steps = [planet.xpos,planet.ypos,planet.zpos]
                    del planet.orbitx[-1]
                    del planet.orbitx[-1]
                    del planet.orbity[-1]
                    del planet.orbity[-1]
                    del planet.orbitz[-1]
                    del planet.orbitz[-1]
                    planet.xpos,planet.ypos,planet.zpos = initialPosVel[0],initialPosVel[1],initialPosVel[2]
                    planet.xvel,planet.yvel,planet.zvel = initialPosVel[3],initialPosVel[4],initialPosVel[5]
                    planet.update_planet_position_rk4(planet_array,2*dt)
                    del planet.orbitx[-1]
                    del planet.orbity[-1]
                    del planet.orbitz[-1]
                    two_dt_one_steps = [planet.xpos,planet.ypos,planet.zpos]
                    planet.xpos,planet.ypos,planet.zpos = initialPosVel[0],initialPosVel[1],initialPosVel[2]
                    planet.xvel,planet.yvel,planet.zvel = initialPosVel[3],initialPosVel[4],initialPosVel[5]
                    planet.update_planet_position_euler(planet_array,dt)
                    trunc_error = trunc_error * (np.abs(1 - (np.sum(np.divide(two_dt_one_steps,dt_two_steps))/3))+1)
                    planet.truncation_error_rk4.append(trunc_error)
            if i == 3:
                for planet in planet_array:
                    initialPosVel = [planet.xpos,planet.ypos,planet.zpos,planet.xvel,planet.yvel,planet.zvel]
                    planet.update_planet_position_verlet(planet_array,dt)
                    planet.update_planet_position_verlet(planet_array,dt)
                    dt_two_steps = [planet.xpos,planet.ypos,planet.zpos]
                    del planet.orbitx[-1]
                    del planet.orbitx[-1]
                    del planet.orbity[-1]
                    del planet.orbity[-1]
                    del planet.orbitz[-1]
                    del planet.orbitz[-1]
                    planet.xpos,planet.ypos,planet.zpos = initialPosVel[0],initialPosVel[1],initialPosVel[2]
                    planet.xvel,planet.yvel,planet.zvel = initialPosVel[3],initialPosVel[4],initialPosVel[5]
                    planet.update_planet_position_verlet(planet_array,2*dt)
                    if(len(planet.orbitx) != 0):
                        del planet.orbitx[-1]
                        del planet.orbity[-1]
                        del planet.orbitz[-1]
                    two_dt_one_steps = [planet.xpos,planet.ypos,planet.zpos]
                    planet.xpos,planet.ypos,planet.zpos = initialPosVel[0],initialPosVel[1],initialPosVel[2]
                    planet.xvel,planet.yvel,planet.zvel = initialPosVel[3],initialPosVel[4],initialPosVel[5]
                    planet.update_planet_position_euler(planet_array,dt)
                    trunc_error = trunc_error * (np.abs(1 - (np.sum(np.divide(two_dt_one_steps,dt_two_steps))/3))+1)
                    planet.truncation_error_verlet.append(trunc_error)
            t = t + dt
        for planet in planet_array:
            
            planet.orbitx = []
            planet.orbity = []
            planet.orbitz = []
            planet.xpos = planet.initial_xpos
            planet.ypos = planet.initial_ypos
            planet.zpos = planet.initial_zpos
            planet.xvel = planet.initial_xvel
            planet.yvel = planet.initial_yvel
            planet.zvel = planet.initial_zvel
            eulerLength = len(planet.truncation_error_euler)
    truncation_error_euler = np.zeros(eulerLength)
    truncation_error_rk4 = np.zeros(eulerLength)
    truncation_error_verlet = np.zeros(eulerLength)
    for planet in planet_array:
        truncation_error_euler += np.array(planet.truncation_error_euler)
        truncation_error_rk4 += np.array(planet.truncation_error_rk4)
        truncation_error_verlet += np.array(planet.truncation_error_verlet)
    truncation_error_euler = truncation_error_euler/len(planet_array)
    truncation_error_rk4 = truncation_error_rk4/len(planet_array)
    truncation_error_verlet = truncation_error_verlet/len(planet_array)
    
    plt.yscale('log')
    
    plt.plot(np.arange(len(truncation_error_euler)),truncation_error_euler,label="Euler")
    plt.plot(np.arange(len(truncation_error_rk4)),truncation_error_rk4,label="RK4")
    plt.plot(np.arange(len(truncation_error_verlet)),truncation_error_verlet,label="Verlet")
    plt.title("Error chart")
    plt.xlabel("Step no.")
    plt.ylabel("Compounded local errors")
    plt.legend(loc="upper right")
    plt.show()
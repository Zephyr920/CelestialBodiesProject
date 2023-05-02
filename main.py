# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:18:07 2023

@author: Agustin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import ExtraFunctions as ef
import Planet as p
import csv

daysUntil_07052033 = 3658

AU = 149597871000
TIMESTEP = 3600
PAUSE = 0.001
SCALE = 250 / AU
dt = 12*60*60

total_ke = []
total_gpe = []
comArrx = []
comArry = []
comArrz = []
comArr_r = []



planet_array = [] # initialises planet list
namelist = ["Sun","Venus","Mercury""Earth","Moon","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","JWST"] # namelist for planets
with open('planet_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    index = 0 # index for the name list
    for row in reader:    
        mass, xpos, ypos, zpos, xvel, yvel, zvel = map(float, row)
        planet_array.append(p.Planet(xpos * 1e3, ypos * 1e3, zpos * 1e3, xvel * 1e3, yvel * 1e3, zvel * 1e3,mass)) #numbers from JPL Horizons are in km , 1e3 turns it into metres
        
        index = index + 1 

    
def menu():
    selection = 1
    choice = input("Sim (S) or Orbit plot (O) \n")
    dt = int(input("dt in seconds (integer)"))
    
    if choice == "S":
        
        selection = int(input("Euler (1) or RK4 (2) or Verlet (3)"))    
        #sim
        while True:
            total_ke_temp = 0
            total_gpe_temp = 0
            for planet in planet_array:
                #planet.show_planet()
                if selection == 1:
                    planet.update_planet_position_euler(planet_array,dt)
                
                # rk4 part
                if selection == 2:
                    planet.update_planet_position_rk4(planet_array,dt)
                    
                if selection == 3:
                    planet.update_planet_position_verlet(planet_array,dt)
                
                plt.scatter(planet.xpos, planet.ypos)
                plt.plot(planet.orbitx,planet.orbity)
            
            plt.show()
            
         
    
    elif choice == "O":
        #orbit plot
        
        fig = plt.figure()
        ax = plt.axes(projection='3d') # sets the plot for 3d 
        
        t = 0
        tmax = int(input("Input sim time in days (integer)"))
        tmax = tmax * 24 * 60 * 60
        selection = int(input("Euler (1) or RK4 (2) or Verlet (3)"))   
        if choice == "E":
            rk4 = False
        elif choice == "R":
            rk4 = True
        
        while t <= tmax:
            total_ke_temp = 0
            total_gpe_temp = 0
            for planet in planet_array:
                 
                if selection == 1:
                    planet.update_planet_position_euler(planet_array,dt)
                
                # rk4 part
                if selection == 2:
                    planet.update_planet_position_rk4(planet_array,dt)
                    
                if selection == 3:
                    planet.update_planet_position_verlet(planet_array,dt)
                
                total_ke_temp += planet.ke[-1]
                total_gpe_temp += planet.gpe[-1]
                #centre of mass calculations
                centre_of_mass = ef.com(planet_array)
                comArrx.append(centre_of_mass[0])
                comArry.append(centre_of_mass[1])
                comArrz.append(centre_of_mass[2])
                comArr_r.append(np.sqrt(centre_of_mass[0]**2 + centre_of_mass[1]**2 + centre_of_mass[2]**2))
            #energy calculations
            total_ke.append(total_ke_temp)
            total_gpe.append(total_gpe_temp)
            t = t + dt
        for planet in planet_array:
            ax.plot3D(comArrx, comArry,comArrz)
            ax.scatter(comArrx[-1], comArry[-1],comArrz[-1])
            ax.plot3D(planet.orbitx, planet.orbity,planet.orbitz)
            ax.scatter(planet.orbitx[-1], planet.orbity[-1],planet.orbitz[-1])
        plt.show()
        plt.plot(total_gpe)
        plt.plot(total_ke)
        plt.plot(np.array(total_gpe)+np.array(total_ke))
        plt.show()
        if selection == 1:
            method = "Euler"
        if selection == 2:
            method = "RK4"
        if selection == 3:
            method = "Verlet"
        plt.plot(np.arange(len(comArr_r)),comArr_r,label="centre of mass pos")
        plt.title("Centre of mass plot for " + method + " method")
        plt.show()
        ef.error_from_exact(planet_array,dt)
        
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
        menu()
menu()    





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
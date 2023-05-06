# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:57:58 2023

@author: Agustin
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
 
import matplotlib

matplotlib.rcParams.update({'font.size': 14})

# Open the file in 'r' mode, not 'rb'
csv_file = open('horizons_results_earth.csv','r')
earth_xtraj = []
earth_ytraj = []
earth_ztraj = []
earth_xvel = []
earth_yvel = []
earth_zvel = []

mercury_xtraj = []
mercury_ytraj = []
mercury_ztraj = []
mercury_xvel = []
mercury_yvel = []
mercury_zvel = []


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
# Split columns while reading
csv_file = open('horizons_results_mercury.csv','r')
for x, y, z, vx,vy,vz in csv.reader(csv_file, delimiter=','):
    # Append each variable to a separate list
    if(x[:3]) == "ï»¿":
        earth_xtraj.append(float(x[3:])*1e3)
    else:
        mercury_xtraj.append(float(x)*1e3)
        mercury_ytraj.append(float(y)*1e3)
        mercury_ztraj.append(float(z)*1e3)
        mercury_xvel.append(float(vx)*1e3)
        mercury_yvel.append(float(vy)*1e3)
        mercury_zvel.append(float(vz)*1e3)

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
        
def difference_orbitradius(earth_or_mercury,planet_array,method,dt):
    if earth_or_mercury == "Earth":
        planet = planet_array[1]
        planet_radius = np.sqrt(np.array(planet.orbitx)**2 + np.array(planet.orbity)**2 + np.array(planet.orbitz)**2)
        expected_radius = np.sqrt(np.array(earth_xtraj[:8767])**2 + np.array(earth_ytraj[:8767])**2 + np.array(earth_ztraj[:8767])**2)
    else:
        planet = planet_array[4]
        planet_radius = np.sqrt(np.array(planet.orbitx)**2 + np.array(planet.orbity)**2 + np.array(planet.orbitz)**2)
        expected_radius = np.sqrt(np.array(mercury_xtraj[:8767])**2 + np.array(mercury_ytraj[:8767])**2 + np.array(mercury_ztraj[:8767])**2)
    
    adjusted_list = []
    if dt == 36000:
        skip = 1
    elif dt == 72000:
        skip = 2
    elif dt == 144000:
        skip = 4
    elif dt == 288000:
        skip = 8
    for i in range(0,len(expected_radius),skip):
        adjusted_list.append(expected_radius[i])
        
    diff = np.array(adjusted_list) - planet_radius[:len(adjusted_list)]
    
    if dt == 288000:
        if planet.name == "Mercury":
            plt.plot(np.linspace(0,len(diff)-1,len(diff))*(dt/60/60)/24 , diff)
            plt.ylim(-2e10,2e10)
            plt.title("ΔR for " + planet.name + " between NASA and " + method + " data,dt=" + str(dt) + "s," + method + "\n",fontsize = 10)
            plt.xlabel("Days")
            plt.ylabel("ΔR (metres)")
            plt.savefig('orbitradius-'+ planet.name +'-dt=' + str(dt) + '-' + method +'.png', dpi=300, bbox_inches = "tight")
            plt.show()
    else:
        plt.plot(np.linspace(0,len(diff)-1,len(diff))*(dt/60/60)/24 , diff)
        plt.title("ΔR for " + planet.name + " between NASA and " + method + " data,dt=" + str(dt) + "s," + method + "\n",fontsize = 10)
        plt.xlabel("Days")
        plt.ylabel("ΔR (metres)")
        plt.savefig('orbitradius-'+ planet.name +'-dt=' + str(dt) + '-' + method +'.png', dpi=300, bbox_inches = "tight")
        plt.show()
    
    

def error_from_exact_xpos(planet_array,method,dt):
    earth = planet_array[1]
    adjusted_list = []
    if dt == 36000:
        skip = 1
    elif dt == 72000:
        skip = 2
    elif dt == 144000:
        skip = 4
    elif dt == 288000:
        skip = 8
    for i in range(0,len(earth_xtraj),skip):
        adjusted_list.append(earth_xtraj[i])
        
    diff = np.array(adjusted_list) - np.array(earth.orbitx[:len(adjusted_list)])

    
    plt.figure(figsize=(16,4.8))    
    plt.plot(np.linspace(0,len(earth.orbitx)-1,len(earth.orbitx))*(dt/60/60)/24,  earth.orbitx,label="Sim earth X coord")
    plt.plot(np.linspace(0,len(adjusted_list)-1,len(adjusted_list))*(dt/60/60)/24,  adjusted_list,label="Nasa Earth X coord")
    plt.title("NASA & " + method + " X coord of Earth,dt=" + str(dt) + "s,t=3658 Days \n",fontsize = 14)
    plt.xlabel("Days")
    plt.ylabel("X (metres)")
    plt.legend(loc='upper right', fontsize='small')
    plt.savefig('xcoord-earth-dt=' + str(dt) + '-' + method +'.png', dpi=300, bbox_inches = "tight")
    plt.show()
    plt.plot(np.linspace(0,len(diff)-1,len(diff))*(dt/60/60)/24,diff)
    plt.title("ΔX for Earth between NASA and " + method + " data,dt=" + str(dt) + "s," + method + "\n",fontsize = 10)
    plt.xlabel("Days")
    plt.ylabel("ΔX (metres)")
    plt.legend(loc='upper right',fontsize = 6)
    plt.savefig('xcoord-error-earth-dt=' + str(dt) + '-' + method +'.png', dpi=300, bbox_inches = "tight")
    plt.show()

def earth_halley_distance(planet_array,dt,method):
    Halley = planet_array[-1]
    Earth = planet_array[1]
    earth_halley_dist = np.array(np.sqrt((np.array(Earth.orbitx) - np.array(Halley.orbitx))**2 + (np.array(Earth.orbity) - np.array(Halley.orbity))**2 + (np.array(Earth.orbitz) - np.array(Halley.orbitz))**2) )
    
    index_of_min = np.array(earth_halley_dist).argmin()
    
    plt.scatter(index_of_min*(dt/60/60)/24,earth_halley_dist[index_of_min],label="Halley pass at " + str(int(dt*index_of_min/60/60/24)))
    plt.plot(np.linspace(0,len(earth_halley_dist)-1,len(earth_halley_dist))*(dt/60/60)/24,earth_halley_dist,label="Distance")
    plt.title("Earth-Halley distance: " + method + ",dt="+str(dt)+"s\n",fontsize = 14)
    plt.xlabel("Days")
    plt.ylabel("Distance (metres)")
    plt.legend(loc='upper right', fontsize='small')
    plt.savefig('Earth-Halley distance-'+method+',dt='+str(dt)+'s.png', dpi=300, bbox_inches = "tight")
    plt.show()
    

def error_from_exact_xpos_mercury(planet_array,method,dt):
    mercury = planet_array[4]
    adjusted_list = []
    if dt == 36000:
        skip = 1
    elif dt == 72000:
        skip = 2
    elif dt == 144000:
        skip = 4
    elif dt == 288000:
        skip = 8
    for i in range(0,len(mercury_xtraj),skip):
        adjusted_list.append(mercury_xtraj[i])
    diff = np.array(adjusted_list) - np.array(mercury.orbitx[:len(adjusted_list)])
    
    plt.figure(figsize=(16,4.8)) 
    plt.plot(np.linspace(0,len(mercury.orbitx)-1,len(mercury.orbitx))*(dt/60/60)/24,mercury.orbitx,label="Sim mercury x coord")
    plt.plot(np.linspace(0,len(adjusted_list)-1,len(adjusted_list))*(dt/60/60)/24,adjusted_list,label="Exact mercury x coord")
    plt.title("NASA & " + method + " X coord of Mercury,dt=" + str(dt) + "s,t=3658 Days \n",fontsize = 14)
    plt.xlabel("Days")
    plt.ylabel("X coord (metres)")
    plt.legend(loc='upper right',fontsize = 6)
    
    plt.savefig('xcoord-mercury-dt=' + str(dt) + '-' + method +'.png', dpi=300, bbox_inches = "tight")
    plt.show()
    plt.plot(np.linspace(0,len(diff)-1,len(diff))*(dt/60/60)/24,diff)
    plt.title("ΔX for Mercury between NASA and " + method + " data,dt=" + str(dt) + "s," + method + "\n",fontsize = 10)
    plt.xlabel("Days")
    plt.ylabel("ΔX (metres)")
    plt.legend(loc='upper right',fontsize = 6)
    plt.savefig('xcoord-error-mercury-dt=' + str(dt) + '-' + method +'.png', dpi=300, bbox_inches = "tight")
    plt.show()
    

    

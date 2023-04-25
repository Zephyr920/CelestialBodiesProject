# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:35:06 2023

@author: Agustin
"""
import numpy as np
import matplotlib.pyplot as plt

G = 6.6743e-11
dt = 12*60*60


class planetObj:
    def __init__(self,mass,xpos,ypos,zpos,xvel,yvel,zvel):
        self.xtraj = []
        self.ytraj = []
        self.ztraj = []
        self.mass = mass
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.xvel = xvel
        self.yvel = yvel
        self.zvel = zvel
        self.xforce = 0
        self.yforce = 0   
        self.zforce = 0          
            
planets = []

planets.append(planetObj(1.98854E+30 ,1.81899E+08	,9.83630E+08	,-1.58778E+07	,0	, 0	,	0  ))
planets.append(planetObj(5.97219E+24	 ,-1.43778E+11		,-4.00067E+10		,-1.38875E+07		,7.65151E+03		,-2.87514E+04		,2.08354E+00		  ))
planets.append(planetObj(6.41850E+23		 ,-1.14746E+11		,-1.96294E+11		,-1.32908E+09		,2.18369E+04		,-1.01132E+04		,-7.47957E+02		  ))


def return_acceleration(planet,xpos,ypos,zpos): 
    xforce = 0
    yforce = 0
    zforce = 0
    for i in range(len(planets)):
        
        if planet != planets[i]:
            
            otherPlanet = planets[i]
            thisPlanet = planet

            dx = xpos - otherPlanet.xpos
            dy = ypos - otherPlanet.ypos
            dz = zpos - otherPlanet.zpos
            dist = np.sqrt(dx**2 + dy**2 + dz**2)

            f = G * otherPlanet.mass * thisPlanet.mass / dist**2
            fx = f * dx / dist
            fy = f * dy / dist
            fz = f * dz / dist
        
            xforce += -fx
            yforce += -fy
            zforce += -fz

    return np.array([xforce/thisPlanet.mass,yforce/thisPlanet.mass,zforce/thisPlanet.mass])


    
def update_RK4():

    for i in range(len(planets)):
                        
        thisPlanet = planets[i]
        
        vel = np.array([thisPlanet.xvel , thisPlanet.yvel, thisPlanet.zvel])
        initialPos = np.array([thisPlanet.xpos,thisPlanet.ypos, thisPlanet.zpos])
        
        dv1 = dt * np.array([thisPlanet.xforce / thisPlanet.mass , thisPlanet.yforce / thisPlanet.mass, thisPlanet.zforce / thisPlanet.mass])
        dr1 = dt * vel
        
        dr2 = dt * (vel + np.array([thisPlanet.xforce / thisPlanet.mass , thisPlanet.yforce / thisPlanet.mass, thisPlanet.zforce / thisPlanet.mass]) * dt/2)
        r = initialPos + (dr1/2)
        dv2 = dt * return_acceleration(thisPlanet , r[0] , r[1], r[2])
        
        dr3 = dt * (vel + dv2/2)
        r = initialPos + (dr2/2)
        dv3 = dt * return_acceleration(thisPlanet , r[0] , r[1], r[2])
        
        dr4 = dt * (vel + dv3)
        r = initialPos + (dr3)
        dv4 = dt * return_acceleration(thisPlanet , r[0] , r[1], r[2])
        
        finalv = vel + (1/6) * (dv1 + 2*dv2 + 2*dv3 + dv4)
        finalpos = initialPos + (1/6) * (dr1 + 2*dr2 + 2*dr3 + dr4)
        
        thisPlanet.xvel = finalv[0]
        thisPlanet.yvel = finalv[1]
        thisPlanet.zvel = finalv[2]
        
        thisPlanet.xpos = finalpos[0]
        thisPlanet.ypos = finalpos[1]
        thisPlanet.zpos = finalpos[2]
        
        thisPlanet.xtraj.append(finalpos[0])
        thisPlanet.ytraj.append(finalpos[1])
        thisPlanet.ztraj.append(finalpos[2])
    
tmax = 365*10*24*60*60
t = 0
while t < tmax:
    update_RK4()
    t = t + dt


fig = plt.figure()
ax = plt.axes(projection='3d')

for planet in planets:
    ax.plot3D(planet.xtraj,planet.ytraj,planet.ztraj)
    

    









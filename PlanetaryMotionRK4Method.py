# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:35:06 2023

@author: Agustin
"""
import numpy as np

G = 6.6743e-11

class PlanetaryMotion:
    def __init__(self, planets):
        self.planets = planets
    
    def calculate_forces(self):
        for i in range(len(self.planets)):
            for j in range(len(self.planets)):
                if i != j :
                    pi = self.planets[i]
                    pj = self.planets[j]
    
                    dx = pj.xpos - pi.xpos
                    dy = pj.ypos - pi.ypos
                    dist = np.sqrt(dx**2 + dy**2)
    
                    f = G * pi.mass * pj.mass / dist**2
                    fx = f * dx / dist
                    fy = f * dy / dist
    
                    pi.xforce += fx
                    pi.yforce += fy
                    pj.xforce -= fx
                    pj.yforce -= fy
                
    def return_acceleration(self,planet,xpos,ypos): "Function that returns forces on a single planet at a position , for RK4 steps"
        xforce = 0
        yforce = 0
        for i in range(len(self.planets)):
            
            if planet.self != self.planets[i]:
                
                otherPlanet = self.planets[i]
                thisPlanet = planet.self

                dx = xpos - otherPlanet.xpos
                dy = ypos - otherPlanet.ypos
                dist = np.sqrt(dx**2 + dy**2)

                f = G * otherPlanet.mass * thisPlanet.mass / dist**2
                fx = f * dx / dist
                fy = f * dy / dist
            
                xforce += fx
                yforce += fy

        return [xforce/thisPlanet.mass,yforce/thisPlanet.mass]
            
    def update_RK4(self):
        "Loop through all planets , do RK4 for each planet at a time"
        for i in range(len(self.planets)):
                            
            thisPlanet = self.planets
            
            vel = [thisPlanet.xvel , thisPlanet.yvel] ""
            initialPos = [thisPlanet.xpos,thisPlanet.ypos]
            
            dv1 = dt * [thisPlanet.xforce / thisPlanet.mass , thisPlanet.yforce / thisPlanet.mass]
            dr1 = dt * vel
            
            dr2 = dt * (vel + [thisPlanet.xforce / thisPlanet.mass , thisPlanet.yforce / thisPlanet.mass] * dt/2)
            r = initialPos + (dr1/2)
            dv2 = dt * return_acceleration(thisPlanet , r[0] , r[1])
            
            dr3 = dt * (vel + dv2/2)
            r = initialPos + (dr2/2)
            dv3 = dt * return_acceleration(thisPlanet , r[0] , r[1])
            
            dr4 = dt * (vel + dv3)
            r = initialPos + (dr3)
            dv4 = dt * return_acceleration(thisPlanet , r[0] , r[1])
            
            finalv = vel + (1/6) * (dv1 + 2*dv2 + 2*dv3 + dv4)
            finalpos = initialPos + (1/6) * (dr1 + 2*dr2 + 2*dr3 + dr4)
            
            thisPlanet.xvel = finalv[0]
            thisPlanet.yvel = finalv[1]
            
            thisPlanet.xpos = finalpos[0]
            thisplanet.ypos = finalpos[1]
            












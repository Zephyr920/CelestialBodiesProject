# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:35:06 2023

@author: Agustin
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

G = 6.6743e-11 # defines G gravity constant and below timestep is set
dt = 24*60*60

class planetObj:
    def __init__(self,mass,xpos,ypos,zpos,xvel,yvel,zvel,name):
        self.name = name # initialise function for the planet object class
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
        self.ke = []
        self.gpe = []
        

planets = [] # initialises planet list
namelist = ["Sun","Earth","Moon","Venus","Mercury","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","JWST"] # namelist for planets
with open('planet_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    index = 0 # index for the name list
    for row in reader:    
        mass, xpos, ypos, zpos, xvel, yvel, zvel = map(float, row)
        planets.append(planetObj(mass, xpos * 1e3, ypos * 1e3, zpos * 1e3, xvel * 1e3, yvel * 1e3, zvel * 1e3,namelist[index])) #numbers from JPL Horizons are in km , 1e3 turns it into metres
        index = index + 1 

def return_acceleration(planet,xpos,ypos,zpos): 
    xforce = 0
    yforce = 0
    zforce = 0
    potential = 0
    for i in range(len(planets)): #loop for the planets list , could use for planet in planets too
        
        if planet != planets[i]:
            
            otherPlanet = planets[i] # gets acceleration on the selected planet from all the other planets hence it loops through all others with a planet != planets[i] check
            thisPlanet = planet

            dx = xpos - otherPlanet.xpos # calculates the difference in x,y,z coords from the other planet to then carry out newtons law of gravitation calculations
            dy = ypos - otherPlanet.ypos
            dz = zpos - otherPlanet.zpos
            dist = np.sqrt(dx**2 + dy**2 + dz**2) # calculates distance from the dx,dy,dz variables

            f = G * otherPlanet.mass * thisPlanet.mass / dist**2 # newtons law of gravitation
            fx = f * dx / dist
            fy = f * dy / dist
            fz = f * dz / dist # gets the vector quantities for the force
        
            xforce += -fx # sums the negative of the force components linearly onto the xforce,yforce,zforce variables
            yforce += -fy
            zforce += -fz
            
            potential += -G * otherPlanet.mass * thisPlanet.mass / dist # calculates the GPE for use in energy conservation plots later
    thisPlanet.gpe.append(potential)
    return np.array([xforce/thisPlanet.mass,yforce/thisPlanet.mass,zforce/thisPlanet.mass]) # returns a as a vector


totalke = []
totalgpe = [] # the two Ke and GPE arrays are initialised
    
def update_RK4(dt): 
    totalke_temp = 0
    totalgpe_temp = 0 # temporary Ke, GPE variables for use in a loop
    for i in range(len(planets)): # loops through all the planets , uses the return acceleration function which contains the second loop.
                        
        thisPlanet = planets[i] 
        
        vel = np.array([thisPlanet.xvel , thisPlanet.yvel, thisPlanet.zvel])
        initialPos = np.array([thisPlanet.xpos,thisPlanet.ypos, thisPlanet.zpos]) # initial velocity and position vectors for use in the steps
        
        # first step in RK4 uses the initial values
        dv1 = dt * np.array([thisPlanet.xforce / thisPlanet.mass , thisPlanet.yforce / thisPlanet.mass, thisPlanet.zforce / thisPlanet.mass])
        dr1 = dt * vel
        
        # second step in RK4 , takes a dt/2 step forward
        dr2 = dt * (vel + np.array([thisPlanet.xforce / thisPlanet.mass , thisPlanet.yforce / thisPlanet.mass, thisPlanet.zforce / thisPlanet.mass]) * dt/2)
        r = initialPos + (dr1/2)
        dv2 = dt * return_acceleration(thisPlanet , r[0] , r[1], r[2]) #uses the new r to get the next velocity
        
        # third step in RK4 , takes another dt/2 step like step 2 but instead feeds back step 2's velocity and position for this iteration
        dr3 = dt * (vel + dv2/2)
        r = initialPos + (dr2/2) #note r here is not the r from step 2 adding on dr2/2 but instead the initial position as demanded by RK4 method
        dv3 = dt * return_acceleration(thisPlanet , r[0] , r[1], r[2])
        
        # fourth step , takes a full step in dt and uses the third steps values
        dr4 = dt * (vel + dv3)
        r = initialPos + (dr3)
        dv4 = dt * return_acceleration(thisPlanet , r[0] , r[1], r[2])
        
        finalv = vel + (1/6) * (dv1 + 2*dv2 + 2*dv3 + dv4) # changes the velocity and position by the coefficients needed for RK4
        finalpos = initialPos + (1/6) * (dr1 + 2*dr2 + 2*dr3 + dr4)
        
        thisPlanet.xvel = finalv[0]
        thisPlanet.yvel = finalv[1]
        thisPlanet.zvel = finalv[2] # assigns the new velocity to the planet
        
        thisPlanet.ke.append(0.5 * thisPlanet.mass * (thisPlanet.xvel**2 + thisPlanet.yvel**2 + thisPlanet.zvel**2))
        totalke_temp = totalke_temp + 0.5 * thisPlanet.mass * (thisPlanet.xvel**2 + thisPlanet.yvel**2 + thisPlanet.zvel**2) #calculates the Ke and adds it to the object and also calculates the total systems Ke
        
        thisPlanet.xpos = finalpos[0]
        thisPlanet.ypos = finalpos[1]
        thisPlanet.zpos = finalpos[2] # assigns new coords to the planet
        
        thisPlanet.xtraj.append(finalpos[0])
        thisPlanet.ytraj.append(finalpos[1])
        thisPlanet.ztraj.append(finalpos[2]) #appends the new coords to the trajectory path used for plotting
        totalgpe_temp += thisPlanet.gpe[-1] # sums the GPE to the total system gpe. GPE is summed twice so is divided by 2 later
    

    totalke.append(totalke_temp)
    totalgpe.append(totalgpe_temp) # appends the temporary iteration values for Ke and GPE to the running totals total Ke + total GPE ( ie total E) should be constant in the solar system

def update_Verlet(dt):
    totalke_temp = 0
    totalgpe_temp = 0 # temporary Ke, GPE variables for use in a loop
    for i in range(len(planets)):
        # verlet method will already start with a pre calculated first step using the velocity verlet method and this is the standard verlet method that will be iterated.               
        thisPlanet = planets[i]
        
        vel = np.array([thisPlanet.xvel , thisPlanet.yvel, thisPlanet.zvel])
          
        pos_n = np.array([thisPlanet.xpos,thisPlanet.ypos, thisPlanet.zpos])
        pos_nminus = np.array([thisPlanet.xtraj[-2],thisPlanet.ytraj[-2], thisPlanet.ztraj[-2]]) # uses the current and last position for use in the verlet formula
        
        a = return_acceleration(thisPlanet,thisPlanet.xpos,thisPlanet.ypos,thisPlanet.zpos)
        
        pos_nplus = 2*pos_n - pos_nminus + a * dt**2
        vel = (pos_nplus - pos_n)/dt
              
        thisPlanet.xvel = vel[0]
        thisPlanet.yvel = vel[1]
        thisPlanet.zvel = vel[2] # assigns the new velocity to the planet
        
        thisPlanet.ke.append(0.5 * thisPlanet.mass * (thisPlanet.xvel**2 + thisPlanet.yvel**2 + thisPlanet.zvel**2))
        totalke_temp = totalke_temp + 0.5 * thisPlanet.mass * (thisPlanet.xvel**2 + thisPlanet.yvel**2 + thisPlanet.zvel**2) #calculates the Ke and adds it to the object and also calculates the total systems Ke
        
        thisPlanet.xpos = pos_nplus[0]
        thisPlanet.ypos = pos_nplus[1]
        thisPlanet.zpos = pos_nplus[2] # assigns new coords to the planet
        
        thisPlanet.xtraj.append(pos_nplus[0])
        thisPlanet.ytraj.append(pos_nplus[1])
        thisPlanet.ztraj.append(pos_nplus[2]) #appends the new coords to the trajectory path used for plotting
        totalgpe_temp += thisPlanet.gpe[-1] # sums the GPE to the total system gpe. GPE is summed twice so is divided by 2 later
    

    totalke.append(totalke_temp)
    totalgpe.append(totalgpe_temp)

t = 0

fig = plt.figure()
ax = plt.axes(projection='3d') # sets the plot for 3d

for planet in planets:
    ax.plot3D(planet.xtraj,planet.ytraj,planet.ztraj)
plt.savefig('filename.png', dpi=600)

def run_simulation(tmax):
    t = 0
    selected_method = integration_method.get()
    if selected_method == "RK4":
        while t <= tmax:
            update_RK4(dt)
            t = t + dt
    elif selected_method == "Verlet":
        #step1
        totalgpe_temp = 0
        totalke_temp = 0
        for planet in planets:        
            vel = np.array([planet.xvel , planet.yvel, planet.zvel])
            initialPos = np.array([planet.xpos,planet.ypos, planet.zpos])        
            a = return_acceleration(planet,planet.xpos,planet.ypos,planet.zpos)         
            initialPos += vel * dt + 0.5 * a * dt**2
            vel += 0.5*a*dt                                           
            planet.xvel = vel[0]
            planet.yvel = vel[1]
            planet.zvel = vel[2]           
            planet.ke.append(0.5 * planet.mass * (planet.xvel**2 + planet.yvel**2 + planet.zvel**2))
            totalke_temp = totalke_temp + 0.5 * planet.mass * (planet.xvel**2 + planet.yvel**2 + planet.zvel**2) 
            planet.xpos = initialPos[0]
            planet.ypos = initialPos[1]
            planet.zpos = initialPos[2]     
            planet.xtraj.append(initialPos[0])
            planet.ytraj.append(initialPos[1])
            planet.ztraj.append(initialPos[2])
            print(len(planet.xtraj))
            totalgpe_temp += planet.gpe[-1]  # this is the code for the first step using velocity verlet method that is then carrried over to the while loop   
        t = t + dt
        while t <= tmax:
            update_Verlet(dt)
            t = t + dt
            
# GUI code in tkinter

    
selected_planet_name = '(0, 0, 0)'
focus = None
def refocus(selected_planet_name):
    global focus
    if selected_planet_name == '(0, 0, 0)':
        focus = None
    else:
        for planet in planets:
            if planet.name == selected_planet_name:
                focus = planet
                break   

def create_plot(ax, zoom, selected_planet=None):
    ax.clear()
    global focus
    if focus is not None:
        ax.set_xlim(focus.xpos - zoom, focus.xpos + zoom)
        ax.set_ylim(focus.ypos - zoom, focus.ypos + zoom)
        ax.set_zlim(focus.zpos - zoom, focus.zpos + zoom)
    else:
        ax.set_xlim(-zoom, zoom)
        ax.set_ylim(-zoom, zoom)
        ax.set_zlim(-zoom, zoom)

    for planet in planets:
        ax.plot3D(planet.xtraj, planet.ytraj, planet.ztraj,label=planet.name)
        if selected_planet == planet.name:
            ax.scatter(planet.xpos, planet.ypos, planet.zpos, c='red', s=100)
        else:
            ax.scatter(planet.xpos, planet.ypos, planet.zpos)

    ax.legend()

    canvas.draw()

    plt.plot(np.arange(0,len(totalke)), totalke)
    plt.plot(np.arange(0,len(totalgpe)), np.array(totalgpe)*0.5)
    totale = np.array(totalgpe)*0.5 + np.array(totalke)
    plt.plot(np.arange(0,len(totalgpe)), totale)
    plt.show()
    
def update_zoom(event):
    zoom_exponent = float(event)
    create_plot(ax, 10**zoom_exponent)
    
def update_focus(selected_planet):
    # Get the position of the selected planet
    planet = next((p for p in planets if p.name == selected_planet), None)
    if planet is None:
        return
    
    # Set camera position
    ax.set_position([0, 0, 0.2, 0.8])
    ax.set_xlim3d([planet.xpos - 5e11, planet.xpos + 5e11])
    ax.set_ylim3d([planet.ypos - 5e11, planet.ypos + 5e11])
    ax.set_zlim3d([planet.zpos - 5e11, planet.zpos + 5e11])

    # Set camera angles
    ax.view_init(elev=30, azim=45)

def rotate_plot_horizontal(event):
    angle = float(event) * 360 / 100
    ax.view_init(elev=ax.elev, azim=angle)
    canvas.draw()

def rotate_plot_vertical(event):
    angle = float(event) * 180 / 100 - 90
    ax.view_init(elev=angle, azim=ax.azim)
    canvas.draw()

# tkinter GUI

def on_submit():
    tmax = int(tmax_var.get()) * 24 * 60 * 60
    selected_planet = planet_var.get()
    for planet in planets:
        planet.xtraj = []
        planet.ytraj = []
        planet.ztraj = []
        for planet in planets:
            planet.xtraj.append(planet.xpos)
            planet.ytraj.append(planet.ypos)
            planet.ztraj.append(planet.zpos)
    run_simulation(tmax)
    create_plot(ax, float(zoom_var.get()), selected_planet)
    

root = tk.Tk()
root.title("Solar System Simulation")

planet_var = tk.StringVar()
integration_method = tk.StringVar()

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

tmax_var = tk.StringVar()
zoom_var = tk.StringVar()

integration_label = ttk.Label(frame, text="Integration Method:")
integration_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
integration_combobox = ttk.Combobox(frame, textvariable=integration_method)
integration_combobox['values'] = ('RK4', 'Verlet')
integration_combobox.current(0)  # set initial selection to 'RK4'
integration_combobox.grid(row=3, column=1, padx=5, pady=5)

tmax_label = ttk.Label(frame, text="Max Time (days):")
tmax_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tmax_entry = ttk.Entry(frame, textvariable=tmax_var)
tmax_entry.grid(row=0, column=1, padx=5, pady=5)

zoom_label = ttk.Label(frame, text="Zoom (log10):")
zoom_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, pady=10)

refocus_button = ttk.Button(frame, text="Refocus", command=lambda: refocus(planet_var.get()))
refocus_button.grid(row=2, column=1, pady=10)

focus_object_label = ttk.Label(frame, text="Focus Object:")
focus_object_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
focus_object_combobox = ttk.Combobox(frame, textvariable=planet_var, values=[planet.name for planet in planets] + ['(0, 0, 0)'], state='readonly')
focus_object_combobox.current(len(planets))  # set initial selection to '(0, 0, 0)'
focus_object_combobox.grid(row=4, column=1, padx=5, pady=5)

fig = plt.figure(dpi=100)
ax = plt.axes(projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

horizontal_rotation_scale = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=rotate_plot_horizontal)
horizontal_rotation_scale.grid(row=2, column=0, sticky=(tk.W, tk.E))

vertical_rotation_scale = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=rotate_plot_vertical)
vertical_rotation_scale.grid(row=3, column=0, sticky=(tk.W, tk.E))

zoom_scale = ttk.Scale(frame, from_=9, to=13, orient=tk.HORIZONTAL, command=update_zoom)
zoom_scale.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

root.mainloop()

    









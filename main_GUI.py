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
import ExtraFunctions as ef
import Planet as p
from tkinter import ttk

daysUntil_07052033 = 3658
dt = 12*60*60

total_ke = []
total_gpe = []
comArrx = []
comArry = []
comArrz = []
comArr_r = []

planet_array = [] # initialises planet list
namelist = ["Sun","Earth","Moon","Venus","Mercury","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","JWST"] # namelist for planets
with open('planet_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    index = 0 # index for the name list
    for row in reader:    
        mass, xpos, ypos, zpos, xvel, yvel, zvel = map(float, row)
        planet_array.append(p.Planet(xpos * 1e3, ypos * 1e3, zpos * 1e3, xvel * 1e3, yvel * 1e3, zvel * 1e3,mass,namelist[index])) #numbers from JPL Horizons are in km , 1e3 turns it into metres
        index = index + 1 
t = 0
comArrx = []
comArry = []
comArrz = []

fig = plt.figure()
ax = plt.axes(projection='3d') # sets the plot for 3d

for planet in planet_array:
    ax.plot3D(planet.orbitx,planet.orbity,planet.orbitz)
plt.savefig('filename.png', dpi=600)

def run_simulation(tmax):
    t = 0
    dt = int(dt_var.get())
    selected_method = integration_method.get()
    if selected_method == "RK4":
        while t <= tmax:
            total_ke_temp = 0
            total_gpe_temp = 0
            for planet in planet_array:
                planet.update_planet_position_rk4(planet_array,dt)
                total_ke_temp += planet.ke[-1]
                total_gpe_temp += planet.gpe[-1]
            #centre of mass calculations
            centre_of_mass = ef.com(planet_array)
            comArrx.append(centre_of_mass[0])
            comArry.append(centre_of_mass[1])
            comArrz.append(centre_of_mass[2])
            comArr_r.append(np.sqrt(centre_of_mass[0]**2 + centre_of_mass[1]**2 + centre_of_mass[2]**2))
            total_ke.append(total_ke_temp)
            total_gpe.append(total_gpe_temp)
            t = t + dt
    elif selected_method == "Verlet":                 
        while t <= tmax:
            total_ke_temp = 0
            total_gpe_temp = 0
            for planet in planet_array:
                planet.update_planet_position_verlet(planet_array,dt)
                total_ke_temp += planet.ke[-1]
                total_gpe_temp += planet.gpe[-1]
            centre_of_mass = ef.com(planet_array)
            comArrx.append(centre_of_mass[0])
            comArry.append(centre_of_mass[1])
            comArrz.append(centre_of_mass[2])
            comArr_r.append(np.sqrt(centre_of_mass[0]**2 + centre_of_mass[1]**2 + centre_of_mass[2]**2))
            total_ke.append(total_ke_temp)
            total_gpe.append(total_gpe_temp)
            t = t + dt
    elif selected_method == "Euler":
        while t <= tmax:
            total_ke_temp = 0
            total_gpe_temp = 0
            for planet in planet_array:
                planet.update_planet_position_euler(planet_array,dt)
                total_ke_temp += planet.ke[-1]
                total_gpe_temp += planet.gpe[-1]
            centre_of_mass = ef.com(planet_array)
            comArrx.append(centre_of_mass[0])
            comArry.append(centre_of_mass[1])
            comArrz.append(centre_of_mass[2])
            comArr_r.append(np.sqrt(centre_of_mass[0]**2 + centre_of_mass[1]**2 + centre_of_mass[2]**2))
            total_ke.append(total_ke_temp)
            total_gpe.append(total_gpe_temp)
            t = t + dt
                   
selected_planet_name = '(0, 0, 0)'
focus = None
def refocus(selected_planet_name):
    global focus
    if selected_planet_name == '(0, 0, 0)':
        focus = None
    else:
        for planet in planet_array:
            if planet.name == selected_planet_name:
                focus = planet
                break   

def create_plot(ax, zoom, replot,selected_planet=None):
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

    for planet in planet_array:
        if (planet.name != "Moon") & (planet.name != "JWST"): 
            ax.plot3D(planet.orbitx, planet.orbity, planet.orbitz,label=planet.name)
            if selected_planet == planet.name:
                ax.scatter(planet.xpos, planet.ypos, planet.zpos, c='red', s=100)
            else:
                ax.scatter(planet.xpos, planet.ypos, planet.zpos)
    ax.plot3D(comArrx, comArry, comArrz,label="Centre of mass")
    ax.scatter(comArrx[-1], comArry[-1], comArrz[-1],label="Centre of mass")
    ax.legend()
    canvas.draw()
    
    if replot == True:
        
        plt.plot(np.arange(0,len(total_ke)), total_ke)
        plt.plot(np.arange(0,len(total_gpe)), total_gpe)
        totale = np.array(total_gpe) + np.array(total_ke)
        plt.plot(np.arange(0,len(total_gpe)), totale)
        plt.show()
        
        plt.plot(np.arange(len(comArr_r)),comArr_r,label="centre of mass pos")
        plt.title("Centre of mass plot for " + integration_method.get() + " method")
        plt.show()
    
        ef.error_from_exact(planet_array,dt)

def update_zoom(event):
    zoom_exponent = float(event)
    create_plot(ax, 10**zoom_exponent,False)
    
def update_focus(selected_planet):

    planet = next((p for p in planet_array if p.name == selected_planet), None)
    if planet is None:
        return
    
    # Set camera position
    ax.set_position([0, 0, 0.2, 0.8])
    ax.set_xlim3d([planet.xpos - 5e11, planet.xpos + 5e11])
    ax.set_ylim3d([planet.ypos - 5e11, planet.ypos + 5e11])
    ax.set_zlim3d([planet.zpos - 5e11, planet.zpos + 5e11])

    ax.view_init(elev=30, azim=45)

def rotate_plot_horizontal(event):
    angle = float(event) * 360 / 100
    ax.view_init(elev=ax.elev, azim=angle)
    canvas.draw()

def rotate_plot_vertical(event):
    angle = float(event) * 180 / 100 - 90
    ax.view_init(elev=angle, azim=ax.azim)
    canvas.draw()

def on_submit():
    tmax = int(tmax_var.get()) * 24 * 60 * 60
    selected_planet = planet_var.get()
    for planet in planet_array:
        planet.orbitx = []
        planet.orbity = []
        planet.orbitz = []
        for planet in planet_array:
            planet.orbitx.append(planet.xpos)
            planet.orbity.append(planet.ypos)
            planet.orbitz.append(planet.zpos)
    run_simulation(tmax)
    create_plot(ax, float(zoom_var.get()),True, selected_planet)
    
root = tk.Tk()
root.title("Solar System Simulation")
planet_var = tk.StringVar()
integration_method = tk.StringVar()
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
tmax_var = tk.StringVar()
dt_var = tk.StringVar()
zoom_var = tk.StringVar()
integration_label = ttk.Label(frame, text="Integration Method:")
integration_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
integration_combobox = ttk.Combobox(frame, textvariable=integration_method)
integration_combobox['values'] = ('RK4', 'Verlet','Euler')
integration_combobox.current(0)  # set initial selection to 'RK4'
integration_combobox.grid(row=3, column=1, padx=5, pady=5)
tmax_label = ttk.Label(frame, text="Max Time (days):")
tmax_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tmax_entry = ttk.Entry(frame, textvariable=tmax_var)
tmax_entry.grid(row=0, column=1, padx=5, pady=5)
dt_label = ttk.Label(frame, text="dt (seconds):")
dt_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
dt_entry = ttk.Entry(frame, textvariable=dt_var)
dt_entry.grid(row=0, column=3, padx=5, pady=5)
zoom_label = ttk.Label(frame, text="Zoom (log10):")
zoom_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, pady=10)
refocus_button = ttk.Button(frame, text="Refocus", command=lambda: refocus(planet_var.get()))
refocus_button.grid(row=2, column=1, pady=10)
focus_object_label = ttk.Label(frame, text="Focus Object:")
focus_object_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
focus_object_combobox = ttk.Combobox(frame, textvariable=planet_var, values=[planet.name for planet in planet_array] + ['(0, 0, 0)'], state='readonly')
focus_object_combobox.current(len(planet_array))  # set initial selection to '(0, 0, 0)'
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

    









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
import time as time

t = 0
total_ke = []
total_gpe = []
comArrx = []
comArry = []
comArrz = []
comArr_r = []

planet_array = [] # initialises planet list
namelist = ["Sun","Earth","Moon","Venus","Mercury","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","JWST","Halley"] # namelist for planets
with open('planet_data.csv',encoding='utf-8-sig',newline='') as csvfile:
    reader = csv.reader(csvfile)
    index = 0 # index for the name list
    for row in reader:    
        mass, xpos, ypos, zpos, xvel, yvel, zvel = map(float, row)
        planet_array.append(p.Planet(xpos * 1e3, ypos * 1e3, zpos * 1e3, xvel * 1e3, yvel * 1e3, zvel * 1e3,mass,namelist[index])) #numbers from JPL Horizons are in km , 1e3 turns it into metres
        index = index + 1 


fig = plt.Figure(figsize=(10, 10), dpi=100)

ax = fig.add_subplot(111, projection='3d') # sets the plot for 3d

for planet in planet_array:
    ax.plot3D(planet.orbitx,planet.orbity,planet.orbitz)
plt.savefig('filename.png', dpi=600)

def time_plots():
    time_arr = [9000,13500,18000,28000,36000,54000,72000,108000,144000,216000,288000]
    method_list = ["Euler","Verlet","RK4"]
    euler_time = []
    verlet_time = []
    RK4_time = []
    for method in method_list:
        for dt in time_arr:
            start = time.time()
            tmax = int(tmax_var.get())* 24 * 60 * 60
            run_simulation(tmax,method,dt)
            end = time.time()
            elapsed = end - start
            if method == "Euler":
                euler_time.append(elapsed)
            elif method == "Verlet":
                verlet_time.append(elapsed)
            elif method == "RK4":
                RK4_time.append(elapsed)
        for planet in planet_array:
            planet.orbitx = []
            planet.orbity = []
            planet.orbitz = []
            planet.vel_arr = []
            planet.planets = []
            planet.ke = []
            planet.gpe = []
            planet.potential = []
            planet.xvel = planet.initial_xvel
            planet.yvel = planet.initial_yvel
            planet.zvel = planet.initial_zvel
            planet.xpos = planet.initial_xpos
            planet.ypos = planet.initial_ypos
            planet.zpos = planet.initial_zpos
    plt.show()
    plt.plot(time_arr,euler_time,label="Euler")
    plt.plot(time_arr,verlet_time,label="Verlet")
    plt.plot(time_arr,RK4_time,label="RK4")
    
    
    log_time = np.log(np.array(time_arr))
    log_euler_time = np.log(np.array(euler_time))
    log_verlet_time = np.log(np.array(verlet_time))
    log_RK4_time = np.log(np.array(RK4_time))
    
    euler_fit = np.polyfit(log_time,log_euler_time,1)
    verlet_fit = np.polyfit(log_time,log_verlet_time,1)
    RK4_fit = np.polyfit(log_time,log_RK4_time,1)
    
    
    
    euler_A = np.exp(euler_fit[1])
    verlet_A = np.exp(verlet_fit[1])
    RK4_A = np.exp(RK4_fit[1])
    
    euler_alpha = euler_fit[0]
    verlet_alpha = verlet_fit[0]
    RK4_alpha = RK4_fit[0]
    
    euler_fit = log_time * euler_fit[0] + euler_fit[1]
    verlet_fit = log_time * verlet_fit[0] + verlet_fit[1]
    RK4_fit = log_time * RK4_fit[0] + RK4_fit[1]
    
    plt.title("Computation time chart for Euler,Verlet and RK4 for dt values with sim time of 365 days\n",fontsize=10)    
    plt.legend(loc='upper right',fontsize=7)
    plt.xlabel("dt (s)")
    plt.ylabel("Computation time (s)")
    plt.savefig('CompTimes.png', dpi=400, bbox_inches = "tight")
    plt.show()
    plt.plot(log_time,log_euler_time,label="Euler")
    plt.plot(log_time,log_verlet_time,label="Verlet")
    plt.plot(log_time,log_RK4_time,label="RK4")
    plt.plot(log_time, euler_fit, linestyle='dashed',label="Euler power law fit t= " + str(round(euler_A,3)) + "dt^(" + str(round(euler_alpha,4)) + ")")
    plt.plot(log_time, verlet_fit, linestyle='dashed',label="Verlet power law fit t= " + str(round(verlet_A,3)) + "dt^(" + str(round(verlet_alpha,4)) + ")")
    plt.plot(log_time, RK4_fit, linestyle='dashed',label="RK4 power law fit t= " + str(round(RK4_A,2)) + "dt^(" + str(round(RK4_alpha,2)) + ")")
    plt.title("log(computation time) chart for Euler,Verlet and RK4 for log(dt) values with sim time of 365 days\n",fontsize=10)
    plt.legend(loc='upper right',fontsize=6)
    plt.xlabel("log(dt)")
    plt.ylabel("log(computation time)")
    plt.savefig('CompTimesLog.png', dpi=400, bbox_inches = "tight")
    plt.show()

def run_simulation(tmax,selected_method,dt):
    t = 0
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
    #ax.plot3D(comArrx, comArry, comArrz,label="Centre of mass")
    #ax.scatter(comArrx[-1], comArry[-1], comArrz[-1],label="Centre of mass")
    ax.set_xlabel('\nx(m)')     
    ax.yaxis.set_label_text('\ny(m) ')
    ax.zaxis.set_label_text(' z(m) ')
    ax.set_title("Orbit plot of solar system: dt="+str(dt_var.get())+",t="+str(tmax_var.get())+" Days"+ " : "+str(integration_method.get()) + "\n\n",fontsize=10)
    legend = ax.legend(bbox_to_anchor=(1.05, 1.05), loc='upper left',fontsize=7)
    frame = legend.get_frame() 
    frame.set_linewidth(0.4)
    frame.set_alpha(1)
    frame.set_boxstyle('round,pad=0.1')
    plt.subplots_adjust(right=0.65)
    canvas.draw()
    
        
        
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

def save_plot():
    dt = str(dt_var.get())
    t = str(tmax_var.get())
    method = str(integration_method.get())
    fig.savefig(str(method) + '-DT='+str(dt)+'-T='+str(t)+'-.png', dpi=300, bbox_inches='tight')

def on_submit():
    global comArrx
    global comArry
    global comArrz
    global total_ke
    global total_gpe
    global comArr_r
    
    tmax = int(tmax_var.get()) * 24 * 60 * 60
    selected_planet = planet_var.get()
    for planet in planet_array:
        planet.orbitx = []
        planet.orbity = []
        planet.orbitz = []
        planet.vel_arr = []
        planet.planets = []
        planet.ke = []
        planet.gpe = []
        planet.potential = []
        planet.xvel = planet.initial_xvel
        planet.yvel = planet.initial_yvel
        planet.zvel = planet.initial_zvel
        planet.xpos = planet.initial_xpos
        planet.ypos = planet.initial_ypos
        planet.zpos = planet.initial_zpos
        
    t = 0
    total_ke = []
    total_gpe = []
    comArrx = []
    comArry = []
    comArrz = []
    comArr_r = []
    
    start = time.time()
    run_simulation(tmax,integration_method.get(),int(dt_var.get()))
    end = time.time()
    print("time taken was: " + str(end - start))
    create_plot(ax, 1e11,True, selected_planet)
    plt.plot(np.arange(0,len(total_ke)), total_ke)
    plt.plot(np.arange(0,len(total_gpe)), total_gpe)
    totale = np.array(total_gpe) + np.array(total_ke)
    plt.plot(np.arange(0,len(total_gpe)), totale)
    plt.show()
    plt.plot(np.linspace(0,len(comArr_r)-1,len(comArr_r))*(int(dt_var.get())/60/60)/24,comArr_r,label="CoM pos")
    plt.title("Centre of mass ΔR for " + integration_method.get() + " method,dt="+dt_var.get()+"s,t=" + tmax_var.get() + "Days \n")
    plt.xlabel("Days")
    plt.ylabel("ΔR of CoM (metres)")
    plt.savefig('CoM-'+ integration_method.get()+"-dt="+dt_var.get()+'-t='+tmax_var.get()+'.png', dpi=300, bbox_inches = "tight")
    plt.show() 
    print("Centre of Mass")
    print(comArr_r[-1])
    
    plt.plot(np.linspace(0,len(total_gpe)-1,len(total_gpe))*(int(dt_var.get())/60/60)/24,total_gpe,label="GPE")
    plt.plot(np.linspace(0,len(total_ke)-1,len(total_ke))*(int(dt_var.get())/60/60)/24,total_ke,label="Kinetic energy")
    totale = np.array(total_gpe)+np.array(total_ke)
    plt.plot(np.linspace(0,len(totale)-1,len(totale))*(int(dt_var.get())/60/60)/24,totale,label="Total energy")
    totale = np.array(total_gpe)+np.array(total_ke)
    plt.title("System energy plot: dt=" + dt_var.get() + "s" + ", t=" + tmax_var.get() + " Days : "  + integration_method.get() + "\n",fontsize=11)    
    plt.legend(loc='upper right',fontsize=6)
    plt.xlabel("Days")
    plt.ylabel("E (Joules)")
    plt.savefig('Energy-Plot-'+ integration_method.get()+"-dt="+dt_var.get()+'.png', dpi=300, bbox_inches = "tight")
    print("Start energy joules: " + str(totale[0]))
    print("End energy joules: " + str(totale[-1]))
    print("Energy percentage at end, of initial energy: " + str(totale[-1]/totale[0] * 100) + "%")
    plt.show()
    
    
    
    ef.earth_halley_distance(planet_array,int(dt_var.get()) ,integration_method.get())
    ef.error_from_exact_xpos_mercury(planet_array,integration_method.get(),int(dt_var.get()))
    ef.difference_orbitradius("Earth",planet_array,integration_method.get(),int(dt_var.get()))
    ef.difference_orbitradius("Mercury",planet_array,integration_method.get(),int(dt_var.get()))
    ef.error_from_exact_xpos(planet_array,integration_method.get(),int(dt_var.get()))
    

    
    

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
save_button = ttk.Button(frame, text="Save Plot", command=save_plot)
save_button.grid(row=5, column=0, pady=10)  # Adjust grid position as needed
time_plot_btn = ttk.Button(frame, text="Compute Time Plots", command=time_plots)
time_plot_btn.grid(row=7, column=0, pady=10)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
horizontal_rotation_scale = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=rotate_plot_horizontal)
horizontal_rotation_scale.grid(row=2, column=0, sticky=(tk.W, tk.E))
vertical_rotation_scale = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=rotate_plot_vertical)
vertical_rotation_scale.grid(row=3, column=0, sticky=(tk.W, tk.E))
zoom_scale = ttk.Scale(frame, from_=9, to=13, orient=tk.HORIZONTAL, command=update_zoom)
zoom_scale.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
root.mainloop()





    









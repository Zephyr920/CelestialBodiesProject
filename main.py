# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ExtraFunctions import *
import Planet as p
import csv
import PlanetsData as pd
from tkinter import *

AU = 149597871000
G = 6.6743e-11
DT = 3600
T = 0
TMAX = 3600*24*365
SCALE = 250 / AU

sun = p.Planet(-1.322562303708917E+09,-1.510322441919945E+08,3.203975493688115E+07,4.101352294486514E-00,-1.469546932963308E+01,2.779623040363461E-02,1988500E+24, 'sun')
mercury = p.Planet(-3.996400393329824E+10,-5.676579748964631E+10,-1.050174158779547E+09,3.039237766846970E+04,-2.517724333295673E+04,-4.843621076486203E+03,3.302E+23, 'mercury')
venus = p.Planet(-1.039948460827050E+11,3.134941744261564E+10,6.388979460838756E+09,-1.043770550903666E+04,-3.365457605758372E+04,1.406919359514074E+02,48.685E+23, 'venus')
earth = p.Planet(-1.063836865199870E+11,-1.084880633909394E+11,3.848228559143096E+07,2.089344659638734E+04,-2.086072337216753E+04,2.016345553396803E-00,5.97219E+24, 'earth')
mars = p.Planet(-2.067490090832551E+11,1.399805895929806E+11,8.007957703505665E+09,-1.273892078545696E+04,-1.796477416591897E+04,-6.358970889053150E+01,6.4171E+23, 'mars')
jupiter = p.Planet(6.769674391689956E+11,2.981157314122288E+11,-1.638244206585099E+10,-5.412050411082397E+03,1.257342409628819E+04,6.896022861749174E+01,189818722E+19, 'jupiter')
saturn = p.Planet(1.267445562886671E+12,-7.346687166842732E+11,-3.768881184755635E+10,4.304729612123042E+03,8.337587949098694E+03,-3.159550545804253E+02,5.6834E+26, 'saturn')
uranus = p.Planet(1.943179286590177E+12,2.204519034249868E+12,-1.698663303099823E+10,-5.158906192272998E+03,4.185843189406060E+03,8.235502809204975E+01,86.813E+24, 'uranus')
neptune = p.Planet(4.455847699628186E+12,-3.809534580212967E+11,-9.484469667376244E+10,4.270848810104238E+02,5.447827204612601E+03,-1.219996566597767E+02,102.409E+24, 'neptune')
pluto = p.Planet(2.472333883925951E+12,-4.568859366154775E+12,-2.262489141364276E+11,4.935600957328479E+03,1.413381695781684E+03,-1.582272481281092E+03,1.307E+22, 'pluto')

planet_array = [sun, mercury, venus, earth]

update_functions = {'euler': lambda: planet.update_planet_position_euler(planet_array, DT), 'rk4': lambda: planet.update_planet_position_rk4(planet_array, DT), 'verlet': lambda: planet.update_planet_position_verlet(planet_array, DT)}

def simulation():
    global matplotlib_or_pygame, matplotlib_pyplot, pygame

    greetings.pack_forget()
    orbit_or_sim_question.pack_forget()
    simulation_button.pack_forget()

    matplotlib_or_pygame = Label(root, text="Would you like to see the simulation through matplotlib or Pygame?")

    matplotlib_pyplot = Button(root, text="Matplotlib.pyplot", padx=41, pady=50, command=matplotlib_plt)
    pygame = Button(root, text="PyGame", padx=65, pady=50)

    matplotlib_or_pygame.pack()
    matplotlib_pyplot.pack()
    pygame.pack()

def matplotlib_plt():
    global sim_numerical_method, sim_euler, sim_rk4, sim_verlet

    matplotlib_or_pygame.pack_forget()
    matplotlib_pyplot.pack_forget()
    pygame.pack_forget()

    #e = Entry(root, width=38)
    #e.pack()
    #e.insert(DT, "Enter the timestep (s), by default it's 3600s.")

    sim_numerical_method = Label(root, text="Choose which numerical method you would like to use.")

    sim_euler = Button(root, text="euler", padx=30, pady=33, command= lambda: simulate('euler'))
    sim_rk4 = Button(root, text="rk4", padx=35, pady=33, command=lambda: simulate('rk4'))
    sim_verlet = Button(root, text="verlet", padx=28, pady=33, command=lambda: simulate('verlet'))

    sim_numerical_method.pack()
    sim_euler.pack()
    sim_rk4.pack()
    sim_verlet.pack()


def simulate(method):
    sim_numerical_method.pack_forget()
    sim_euler.pack_forget()
    sim_rk4.pack_forget()
    sim_verlet.pack_forget()

    root.destroy()

    plt.title(method.capitalize() + ' Simulation')
    plt.xlim(-1000, 1000)
    plt.ylim(-1000, 1000)

    if method == 'euler':
        while True:
            for planet in planet_array:
                plt.plot(planet.xpos * SCALE, planet.ypos * SCALE, '.')
                plt.plot(planet.orbitx, planet.orbity, label=planet.name)
                planet.update_planet_position_euler(planet_array, DT)
            plt.legend()
            plt.pause(0.00001)
            plt.clf()
    elif method == 'rk4':
        while True:
            for planet in planet_array:
                plt.plot(planet.xpos * SCALE, planet.ypos * SCALE, '.', label=planet.name)
                planet.update_planet_position_rk4(planet_array, DT)
            plt.legend()
            plt.pause(0.00001)
            plt.clf()
    else:
        while True:
            for planet in planet_array:
                plt.plot(planet.xpos * SCALE, planet.ypos * SCALE, '.', label=planet.name)
                planet.update_planet_position_verlet(planet_array, DT)
            plt.legend()
            plt.pause(0.00001)
            plt.clf()

def pygame_sim():
    matplotlib_or_pygame.pack_forget()
    matplotlib_pyplot.pack_forget()
    pygame.pack_forget()

def plt_sim(method):
    while True:
        plt.title(method.capitalize() + ' Simulation')
        plt.xlim(-1000, 1000)
        plt.ylim(-1000, 1000)
        for planet in planet_array:
            plt.plot(planet.xpos * SCALE, planet.ypos * SCALE, '.', label=planet.name)
            planet.update_planet_position_euler(planet_array, DT)
        plt.legend()
        plt.pause(0.00001)
        plt.clf()




#Initial Settings
root = Tk()
root.title('Solar System Visual Representation')
root.geometry("400x400")

#Labels
greetings = Label(root, text ="Greetings Dear User!\n", font = 20)
orbit_or_sim_question = Label(root, text = "Pray tell me, \nWould you like to see the simulation of your dreams \nOr the trajectories of your textbooks?")

#Buttons
simulation_button = Button(root, text = "Simulation", padx=50, pady=50, command=simulation)
#orbit_button = Button(root, text = "Orbit", padx=65, pady=50, command=ef.orbit)

#User Input


greetings.pack()
orbit_or_sim_question.pack()
simulation_button.pack()
#orbit_button.pack()


root.mainloop()
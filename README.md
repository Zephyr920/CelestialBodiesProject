# Celestial Bodies Project
Physics 305 Project Repository

# Introduction



Welcome to our Celestial Bodies Project, a computational physics project built in Python aimed at simulating the movement of 
planets and other objects in our solar system , using a suitable numerical integration techniques.The simulator is designed to set up the solar system, simulate the movement 
of planets, and aims to investigate the varying numerical integration techniques and how they affect the dynamics and physical accuracy of our model.
The goal of the project is to analyze the results and draw conclusions about the dynamics of space objects, and the error and accuracy of
our simulation.


# Aims

-Set up the solar system and simulate the movement of planets  
-Analyze the results and draw conclusions about the dynamics of space objects and the physical quantities that can be investigated.

# Code

The program uses Python and modules such as numpy and matplotlib. Data on the celestial objects is stored in a .csv file
and passed through to the main program which reads them in and instantiates the corresponding objects of class planet with the 
desired attributes. The planet class also contains many functions for the simulation.

# Usage

- Download as a zip, load main.py or main_GUI in (main.py for Live simulation and main_GUI.py for orbit plots)

-For main_GUI enter a max time in days, a time step in seconds and choose an integration method (Euler, Verlet and RK4) and submit. It may take a while to finish but after the auxiliary plots appear in the console it has finished. Then the zoom and rotation scales can be used to move around and the refocus utility to change the plots focus.

# References

http://www.wiu.edu/cas/mathematics_and_philosophy/graduate/equations-planetary-motion.pdf - Used for guidance on numerical integration solutions for planetary motion

https://gereshes.com/2018/07/09/verlet-integration-the-n-body-problem/ - Compares error of Verlet vs other methods like euler method

# Acknowledgments

The Celestial Bodies Project was created by Alex Stancioiu and Agustin Montemurro.

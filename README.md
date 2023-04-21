# Celestial Bodies Project
Physics 305 Project Repository

# Introduction



Welcome to our Celestial Bodies Project, a computational physics project built in Python aimed at simulating the movement of 
planets and other objects in our solar system , using a suitable numerical integration technique , which we chose as the Verlet method. The simulator is designed to set up the solar system, simulate the movement 
of planets, and aims to simulate the path of space probes from launch to gravity-assist maneuvers.
The goal of the project is to analyze the results and draw conclusions about the dynamics of space objects, and the error and accuracy of
our simulation.

![image](https://user-images.githubusercontent.com/82035685/233155003-1b39c9bc-3afe-478c-aaa3-56baccf7d59a.png)

# Aims

-Set up the solar system and simulate the movement of planets  
-Launch asteroids towards Earth and test Jupiter's Effect on asteroid impacts on Earth  
-Simulate path of space probes from launch to gravity-assist manoeuvers  
-Simulate the path of the James Webb Space Telescope  
-Analyze the results and draw conclusions about the dynamics of space objects.

# Code

The program uses Python and modules such as numpy and matplotlib. Data on the celestial objects is stored in a .csv file
and passed through to the main program which reads them in and instantiates the corresponding objects of class planet with the 
desired attributes. The planet class also contains many functions for the simulation. The planet class is where the functions for
the Verlet integration method are present. The main code uses the planet class
to simulate the system and plot the graphics for a visual representation of the simulation.

# Installation

- Updated when finished

# Usage

- Updated when finished

# References

http://www.wiu.edu/cas/mathematics_and_philosophy/graduate/equations-planetary-motion.pdf - Used for guidance on numerical integration solutions for planetary motion

https://gereshes.com/2018/07/09/verlet-integration-the-n-body-problem/ - Compares error of Verlet vs other methods like euler method

# Acknowledgments

The Celestial Bodies Project was created by a team consisting of Alex Stancioiu, Hubert Radecki, Michael Ravenscroft, Oliver Rubia Alcarria and Agustin Montemurro.

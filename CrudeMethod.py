import numpy as np
import matplotlib.pyplot as plt

# Define the initial conditions for the sun, earth, and moon
sun_mass = 2e30
earth_mass = 6e24
moon_mass = 7.3e22
sun_pos = np.array([0, 0])
earth_pos = np.array([1.48e11, 0])
earth_vel = np.array([0, 3e4])
moon_pos = np.array([1.48e11 + 3.84e8, 0])
moon_vel = np.array([0, 1e3])

# Define the gravitational constant
G = 6.67e-11

# Define the time step and simulation duration
dt = 36000
t_end = 365 * 24 * 3600

# Initialize the positions and velocities
pos = np.array([sun_pos, earth_pos, moon_pos])
vel = np.array([np.zeros(2), earth_vel, moon_vel])
mass = np.array([sun_mass, earth_mass, moon_mass])

# Run the simulation
t = 0
while t < t_end:

    # Calculate the gravitational forces on each object
    F = np.zeros_like(pos)
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            r = pos[j] - pos[i]
            F[i] += G * mass[i] * mass[j] / np.linalg.norm(r)**3 * r
            F[j] -= F[i]

    # Update the positions and velocities using the Verlet method
    pos += vel * dt + 0.5 * F / mass[:, np.newaxis] * dt**2
    F_new = np.zeros_like(pos)
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            r = pos[j] - pos[i]
            F_new[i] += G * mass[i] * mass[j] / np.linalg.norm(r)**3 * r
            F_new[j] -= F_new[i]
    vel += 0.5 * (F + F_new) / mass[:, np.newaxis] * dt
    F = F_new

    # Increment the time step
    t += dt

    # Plot the positions of the objects
    plt.plot(pos[:, 0], pos[:, 1], '.')
    plt.xlim(-2e11, 2e11)
    plt.ylim(-2e11, 2e11)
    plt.title('Sun, Earth and Moon')
    plt.xlabel('Displacement / m')
    plt.ylabel('Displacement / m')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.0001)
    plt.clf()

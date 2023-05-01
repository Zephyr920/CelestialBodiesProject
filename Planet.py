#Planet Class
import numpy as np
import matplotlib.pyplot as plt
import pygame

G = 6.6743e-11 #¬¬

class Planet:
    AU = 149597871000
    G = 6.6743e-11
    DT = 3600*24*365*3600
    SCALE = 250 / AU
    def __init__(self, xpos, ypos, zpos, xvel, yvel, zvel, mass, r, colour, vis_r):
        #self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.xvel = xvel
        self.yvel = yvel
        self.zvel = zvel
        self.mass = mass
        self.radius = r
        self.planets = []
        self.orbit = []
        self.orbitx = []
        self.orbity = []
        self.orbitz = []
        self.colour = colour
        self.vis_r = vis_r #Radius when we plot so it looks nice :D
        self.ke = []
        self.gpe = []
        self.potential = []

    def show_properties(self):
        return self.xpos, self.ypos, self.xvel, self.yvel, self.mass, self.radius

    def force_calculation(self, other):
        #Quest to find the distance between the two planets and the angle to the x-axis of the distance.
        xdist = other.xpos - self.xpos
        ydist = other.ypos - self.ypos
        zdist = other.zpos - self.zpos
        dist = np.sqrt(xdist**2 + ydist**2 + zdist**2)
        #angle = np.arctan2(ydist, xdist)

        # Newton's Law of Gravitation finds Total force now we split it to Force on x/y - axis
        ft = self.G * self.mass * other.mass / dist**2
        fx = ft * xdist / dist
        fy = ft * ydist / dist
        fz = ft * zdist / dist

        return fx, fy, fz, dist

    def return_acceleration(self, planet, xpos, ypos, zpos, planets):
        xforce = 0
        yforce = 0
        zforce = 0
        potential = 0
        for i in range(len(planets)):  # loop for the planets list , could use for planet in planets too
            if planet != planets[i]:
                otherPlanet = planets[
                    i]  # gets acceleration on the selected planet from all the other planets hence it loops through all others with a planet != planets[i] check

                dx = self.xpos - otherPlanet.xpos  # calculates the difference in x,y,z coords from the other planet to then carry out newtons law of gravitation calculations
                dy = self.ypos - otherPlanet.ypos
                dz = self.zpos - otherPlanet.zpos
                dist = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)  # calculates distance from the dx,dy,dz variables

                f = G * otherPlanet.mass * self.mass / dist ** 2  # newtons law of gravitation
                fx = f * dx / dist
                fy = f * dy / dist
                fz = f * dz / dist  # gets the vector quantities for the force

                xforce += -fx  # sums the negative of the force components linearly onto the xforce,yforce,zforce variables
                yforce += -fy
                zforce += -fz

                ax = xforce / self.mass
                ay = yforce / self.mass
                az = zforce / self.mass

                potential += -G * otherPlanet.mass * self.mass / dist  # calculates the GPE for use in energy conservation plots later
        self.gpe.append(potential)
        return np.array([ax, ay, az])

    def update_planet_position_euler(self, planets, dt):
        fxt = fyt = fzt = 0
        potential = 0

        #Making sure the planet we're calculating the gravitational forces for is not with itself.
        for planet in planets:
            if self == planet:
                continue

            #Finding the forces and acceleration of the planet.
            fx, fy, fz, dist = self.force_calculation(planet)
            fxt += fx
            fyt += fy
            fzt += fz

            #Finding the velocity from F = ma
            ax = fxt / self.mass
            ay = fyt / self.mass
            az = fzt / self.mass

            potential += -self.G * self.mass * planet.mass / dist

        self.gpe.append(potential)

        #Updating velocities and position of planet.
        self.xvel += ax * dt
        self.yvel += ay * dt
        self.zvel += az * dt
        self.xpos += self.xvel * dt
        self.ypos += self.yvel * dt
        self.zpos += self.zvel * dt

        #Appending the planet's orbit to arrays
        self.orbit.append((self.xpos, self.ypos, self.zpos))
        self.orbitx.append(self.xpos)
        self.orbity.append(self.ypos)
        self.orbitz.append(self.zpos)

        self.ke.append(0.5 * self.mass * (self.xvel**2 + self.yvel**2 + self.zvel**2))

    def update_RK4(self, dt, planets):
        dt = float(dt)
        totalke_temp = 0
        totalgpe_temp = 0  # temporary Ke, GPE variables for use in a loop

        vel = np.array([self.xvel, self.yvel, self.zvel])
        initialPos = np.array(
            [self.xpos, self.ypos, self.zpos])  # initial velocity and position vectors for use in the steps

        # first step in RK4 uses the initial values
        dv1 = dt * self.return_acceleration(self, initialPos[0], initialPos[1], initialPos[2], planets)
        dr1 = dt * vel

        # second step in RK4 , takes a dt/2 step forward
        dr2 = dt * (vel + self.return_acceleration(self, initialPos[0], initialPos[1], initialPos[2], planets) * dt / 2)
        r = initialPos + (dr1 / 2)
        dv2 = dt * self.return_acceleration(self, r[0], r[1], r[2], planets)  # uses the new r to get the next velocity

        # third step in RK4 , takes another dt/2 step like step 2 but instead feeds back step 2's velocity and position for this iteration
        dr3 = dt * (vel + dv2 / 2)
        r = initialPos + (
                    dr2 / 2)  # note r here is not the r from step 2 adding on dr2/2 but instead the initial position as demanded by RK4 method
        dv3 = dt * self.return_acceleration(self, r[0], r[1], r[2], planets)

        # fourth step , takes a full step in dt and uses the third steps values
        dr4 = dt * (vel + dv3)
        r = initialPos + (dr3)
        dv4 = dt * self.return_acceleration(self, r[0], r[1], r[2], planets)

        finalv = vel + (1 / 6) * (
                    dv1 + 2 * dv2 + 2 * dv3 + dv4)  # changes the velocity and position by the coefficients needed for RK4
        finalpos = initialPos + (1 / 6) * (dr1 + 2 * dr2 + 2 * dr3 + dr4)

        self.xvel = finalv[0]
        self.yvel = finalv[1]
        self.zvel = finalv[2]  # assigns the new velocity to the planet

        self.ke.append(0.5 * self.mass * (self.xvel ** 2 + self.yvel ** 2 + self.zvel ** 2))
        totalke_temp = totalke_temp + 0.5 * self.mass * (
                    self.xvel ** 2 + self.yvel ** 2 + self.zvel ** 2)  # calculates the Ke and adds it to the object and also calculates the total systems Ke

        self.xpos = finalpos[0]
        self.ypos = finalpos[1]
        self.zpos = finalpos[2]  # assigns new coords to the planet

        self.orbit.append((self.xpos, self.ypos, self.zpos))
        self.orbitx.append(self.xpos)
        self.orbity.append(self.ypos)
        self.orbitz.append(self.zpos)
        totalgpe_temp += self.gpe[
            -1]  # sums the GPE to the total system gpe. GPE is summed twice so is divided by 2 later

        # remember to do the total ke and gpe in the other parts of the code

    def pygame_plot(self, win):
        #Optimization plotting
        #Adjusts the xpos and ypos to fit the screen
        x = self.xpos * self.SCALE + 800 / 2
        y = self.ypos * self.SCALE + 800 / 2

        #Drawing orbit path after it has moved at least once
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + 800 / 2
                y = y * self.SCALE + 800 / 2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.colour, False, updated_points, 2)

        #This is what our planet looks like!
        pygame.draw.circle(win, self.colour, (x, y), self.vis_r)

    def pygame_forces(self, other):
        #Identical to force_calculation
        xdist = other.xpos - self.xpos
        ydist = other.ypos - self.ypos
        dist = np.sqrt(xdist**2 + ydist**2)

        ft = self.G * self.mass * other.mass / dist**2
        angle = np.arctan2(ydist, xdist)
        fx = np.cos(angle) * ft
        fy = np.sin(angle) * ft
        return fx, fy

    def pygame_update_position(self, planets):
        #Euler Method identical to update_planet_position_euler
        #Only looked at 2D
        fxt = fyt = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.pygame_forces(planet)
            fxt += fx
            fyt += fy

        self.xvel += fxt / self.mass * self.DT
        self.yvel += fyt / self.mass * self.DT

        self.xpos += self.xvel * self.DT
        self.ypos += self.yvel * self.DT
        self.orbit.append((self.xpos, self.ypos))

    def update_planet_position_verlet(self, planets, dt):
        #Setting the initial acceleration as 0
        ax = ay = az = 0
        potential = 0
        new_potential = 0

        #Making sure the 2 planets we're working with aren't the same
        for planet in planets:
            if self == planet:
                continue

            #Calculating the forces of the planets
            fx, fy, fz, dist = self.force_calculation(planet)
            ax += fx / self.mass
            ay += fy / self.mass
            az += fz / self.mass

            potential += -self.G * self.mass * planet.mass / dist

        #Updating position
        self.xpos += self.xvel * dt + 0.5 * ax * dt ** 2
        self.ypos += self.yvel * dt + 0.5 * ay * dt ** 2
        self.zpos += self.zvel * dt + 0.5 * az * dt ** 2

        ax_new = ay_new = az_new = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy, fz, dist = self.force_calculation(planet)
            ax_new += fx / self.mass
            ay_new += fy / self.mass
            az_new += fz / self.mass

            new_potential += -self.G * self.mass * planet.mass / dist

        self.gpe.append(0.5*(potential+new_potential))

        #Updating new velocities using the average of the start acceleration and next acceleration
        self.xvel += 0.5 * (ax + ax_new) * dt
        self.yvel += 0.5 * (ay + ay_new) * dt
        self.zvel += 0.5 * (az + az_new) * dt

        self.orbit.append((self.xpos, self.ypos))
        self.orbitx.append(self.xpos)
        self.orbity.append(self.ypos)
        self.orbitz.append(self.zpos)

        self.ke.append(0.5 * self.mass * (self.xvel ** 2 + self.yvel ** 2 + self.zvel ** 2))

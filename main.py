#Main File
import numpy as np
import matplotlib.pyplot as plt
import Planet as p

import matplotlib.pyplot as plt
sun = p.Planet(10, 0, 0)
planet = p.Planet(5, 25, 45)
plt.figure(figsize=(6, 6))
plt.axis([-500, 500, -500, 500])
plt.gca().set_facecolor((0, 0, 0))
sun.show_sun()
planet.show_planet()
plt.title('Simulation in Space')
plt.xlabel('Displacement')
plt.ylabel('Displacement')
plt.gca().set_aspect('equal', adjustable='box')

plt.legend()
plt.show()



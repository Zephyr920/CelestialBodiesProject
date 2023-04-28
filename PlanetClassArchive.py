#def update_planet_position_verlet(self, planets):
#    fxt0 = fyt0 = 0
#    fxt1 = fyt1 = 0
#    for planet in planets:
#        if self == planet:
#            continue
#
#        fx0, fy0 = self.force_calculation(planet)
#        fxt0 += fx0
#        fyt0 += fy0
#
#    a0x = fxt0 / self.mass
#    a0y = fyt0 / self.mass
#
#    self.xpos += self.xvel + a0x * (self.DT * self.DT * 0.5)
#    self.ypos += self.yvel + a0y * (self.DT * self.DT * 0.5)
#
#    for planet in planets:
#        if self == planet:
#            continue
#
#        fx1, fy1 = self.force_calculation(planet)
#        fxt1 += fx1
#        fyt1 += fy1
#
#    a1x = fxt1 / self.mass
#    a1y = fyt1 / self.mass
#
#    self.xvel += (a0x + a1x) * (self.DT * 0.5)
#    self.yvel += (a0y + a1y) * (self.DT * 0.5)

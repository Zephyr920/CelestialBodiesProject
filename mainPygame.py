import numpy as np
import pygame
import Planet as p
import PlanetsData as psd

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Attempt")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOUR1 = (100, 100, 0)
COLOUR2 = (0, 100, 100)
COLOUR3 = (100, 0, 100)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
COLOUR4 = (0, 255, 255)
COLOUR5 = (100, 100, 100)

def main():
    run = True
    max_fr = pygame.time.Clock()

    sun = p.Planet(1.81899E+08, 9.83630E+08, -1.58778E+07, -1.12474E+01, 7.54876E+00, 2.68723E-01, 1.98854E+30, 'sun', YELLOW, 20)
    mercury = p.Planet(-5.67576E+10, -2.73592E+10, 2.89173E+09, 1.16497E+04, -4.14793E+04, -4.45952E+03, 3.30200E+23, 'mercury', COLOUR1, 6)
    venus = p.Planet(4.28480E+10, 1.00073E+11, -1.11872E+09, -3.22930E+04, 1.36960E+04, 2.05091E+03, 4.86850E+24, 'venus', COLOUR2, 8)
    earth = p.Planet(-1.43778E+11, -4.00067E+10, -1.38875E+07, 7.65151E+03, -2.87514E+04, 2.08354E+00, 5.97219E+24, 'earth', BLUE, 12)
    mars = p.Planet(-1.14746E+11, -1.96294E+11, -1.32908E+09, 2.18369E+04, -1.01132E+04, -7.47957E+02, 6.41850E+23, 'mars', RED, 13)
    jupiter = p.Planet(-5.66899E+11, -5.77495E+11, 1.50755E+10, 9.16793E+03, -8.53244E+03, -1.69767E+02, 1.89813E+27, 'jupiter', COLOUR3, 16)
    saturn = p.Planet(8.20513E+10, -1.50241E+12, 2.28565E+10, 9.11312E+03, 4.96372E+02, -3.71643E+02, 5.68319E+26, 'saturn', PURPLE, 15)
    uranus = p.Planet(2.62506E+12, 1.40273E+12, -2.87982E+10, -3.25937E+03, 5.68878E+03, 6.32569E+01, 8.68103E+25, 'uranus', COLOUR4, 13)
    neptune = p.Planet(4.30300E+12, -1.24223E+12, -7.35857E+10, 1.47132E+03, 5.25363E+03, -1.42701E+02, 1.02410E+26, 'neptune', GREEN, 9)
    pluto = p.Planet(1.65554E+12, -4.73503E+12, 2.77962E+10, 5.24541E+03, 6.38510E+02, -1.60709E+03, 1.30700E+22, 'pluto', COLOUR5, 4)

    planet_array = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

    while run:
        max_fr.tick(900)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planet_array:
            planet.pygame_update_position_verlet(planet_array, 3600)
            planet.pygame_plot(WIN)

        pygame.display.update()

    pygame.quit()

main()

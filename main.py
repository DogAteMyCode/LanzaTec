import pygame
import ctypes
import utility
from Planet import Planet
from Ship import Ship
import numpy as np

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

center = pygame.Vector2(w, h) / 2

planets: list[Planet] = []

ships: list[Ship] = []

planets += [Planet(0, 0, 0, 1000, 20, "orange", center),
            Planet(200, 0, 1, 200, 10, "blue", center),
            Planet(200 * 1.5229, 0, 1 / 1.8807, 200, 5, "red", center)
            ]
time_scale = 2 * np.pi/3.154e+7
length_scale = 200/149_610_000
pygame.init()

screen = pygame.display.set_mode((w, 0.95 * h))
clock = pygame.time.Clock()
running = True
pygame.event.set_keyboard_grab(True)
launch = False

v = (39600/60**2)*length_scale / (1*time_scale)
# v = 1000

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    dt = clock.tick(120) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                s = utility.marcian_half_year(planets[1], planets[2], v)
                ships.append(Ship(planets[1].position, s, 'blue'))


    s = utility.marcian_half_year(planets[1], planets[2], v)
    ships.append(Ship(planets[1].position, s))
    screen.fill("black")
    # RENDER YOUR GAME HERE
    for planet in planets:
        pygame.draw.circle(screen, planet.color, planet.position, planet.planetRadius)
        pygame.draw.arc(screen, planet.color, planet.rect, 0, 2 * np.pi)
        planet.advance(dt)

    for ship in ships:
        if (ship.position - center).magnitude() >= planets[2].radius:
            ships.remove(ship)
            del ship

    for ship in ships:
        pygame.draw.polygon(screen, ship.color, ship.vertices)
        ship.advance(dt)
    # flip() the display to put your work on screen
    pygame.display.flip()
pygame.quit()

if __name__ == "__main__":
    pass

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

pygame.init()

screen = pygame.display.set_mode((w, 0.95 * h))
clock = pygame.time.Clock()
running = True
pygame.event.set_keyboard_grab(True)
launch = False

v = 1

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

    # speed1 = utility.speed1(planets[1], planets[2])
    # speed2 = utility.speed2(planets[1], planets[2])
    # # print(speed)
    # for s in [speed1, speed2]:
    #     if not isinstance(s, int):
    #         ships.append(Ship(planets[1].position, s, pygame.Color(65, 65, 65)))

    # fill the screen with a color to wipe away anything from last frame
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

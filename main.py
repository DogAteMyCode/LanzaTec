import pygame
import ctypes
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
speed = 0
launch = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    dt = clock.tick(120) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed += 1
            if event.key == pygame.K_LEFT:
                speed -= 1
            if event.key == pygame.K_SPACE:
                launch = True

    if launch:
        angle = planets[1].angle + np.pi / 2
        ships.append(
            Ship(planets[1].position, angle, speed, pygame.Color(65, 65, 65))
        )
        print(ships[-1].speed)

        launch = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for planet in planets:
        pygame.draw.circle(screen, planet.color, planet.position, planet.planetRadius)
        pygame.draw.arc(screen, planet.color, planet.rect, 0, 2 * np.pi)
        planet.advance(dt)

    for ship in ships:
        pygame.draw.polygon(screen, ship.color, ship.vertices)
        ship.advance(dt)
        if not pygame.Rect((0, 0), (w, h)).contains(ship.position, (1, 1)):
            ships.remove(ship)
    # flip() the display to put your work on screen
    pygame.display.flip()
pygame.quit()

if __name__ == "__main__":
    pass

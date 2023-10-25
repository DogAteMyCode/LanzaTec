from pygame import Vector2, Color, Rect
import numpy as np


class Planet:
    radius: float
    planetRadius: float
    angle: float
    angularV: float
    mass: float
    color: Color
    offset: Vector2
    rect: Rect

    def __init__(self, radius: float, angle: float, angular_v: float, mass: float, planet_radius: float, color: Color,
                 offset: Vector2):
        self.radius = radius
        self.angle = angle
        self.angularV = angular_v
        self.mass = mass
        self.color = color
        self.planetRadius = planet_radius
        self.offset = offset
        self.rect = Rect(offset - Vector2(radius, radius), 2*Vector2(radius, radius))

    @property
    def position(self):
        return self.radius * Vector2(np.cos(self.angle), np.sin(self.angle)) + self.offset

    def advance(self, dt):
        self.angle += self.angularV * dt

    def __str__(self):
        return f"{self.planetRadius}, {self.position}"

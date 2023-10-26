from pygame import Vector2, Color, Rect
import numpy as np


class Planet:
    radius: float
    planetRadius: float
    _angle: float
    angularV: float
    mass: float
    color: Color
    offset: Vector2
    rect: Rect
    _time: float = 0

    def __init__(self, radius: float, angle: float, angular_v: float, mass: float, planet_radius: float, color: Color,
                 offset: Vector2):
        self.radius = radius
        self._angle = angle
        self.angularV = angular_v
        self.mass = mass
        self.color = color
        self.planetRadius = planet_radius
        self.offset = offset
        self.rect = Rect(offset - Vector2(radius, radius), 2 * Vector2(radius, radius))

    @property
    def angle(self):
        return (self._angle + self._time * self.angularV) % (2*np.pi)

    @property
    def position(self):
        return self.radius * Vector2(np.cos(self.angle), np.sin(self.angle)) + self.offset

    def advance(self, dt):
        self._time += dt

    def __str__(self):
        return f"{self.planetRadius}, {self.position}"

    def time_to_angle(self, angle):
        if angle - self.angle > 0:
            return (angle - self.angle)/self.angularV
        else:
            return (2*np.pi + angle - self.angle)/self.angularV


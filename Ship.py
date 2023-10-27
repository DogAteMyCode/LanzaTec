import pygame.transform
from pygame import Vector2, Color, Rect
import numpy as np


class Ship:
    _position: Vector2
    speed: Vector2
    _vertices: list[Vector2]
    _time: float = 0

    def __init__(self, position: Vector2, speed: Vector2):
        self._vertices = []
        self._position = position
        self.speed = speed
        angle = Vector2(1, 0).angle_to(self.speed)
        print(f"Angulo (grados) {angle}")
        angle = np.deg2rad(angle)
        for point in [Vector2(0, 0), Vector2(-2, -13), Vector2(2, -13)]:
            self._vertices.append(point.rotate_rad(angle - np.pi / 2))

    @property
    def color(self):
        return Color(int(max([np.floor(255*(2*np.pi - self._time)/(2*np.pi)), 0])), 0, int(min([np.floor(255*self._time/(2*np.pi)), 200])), 255)

    @property
    def vertices(self):
        return [vertex + self.position for vertex in self._vertices]

    @property
    def position(self):
        return self._position + self.speed * self._time

    def advance(self, dt):
        self._time += dt

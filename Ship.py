from pygame import Vector2, Color, Rect
import numpy as np


class Ship:
    _position: Vector2
    speed: Vector2
    color: Color
    _vertices: list[Vector2]
    _time: float = 0

    def __init__(self, position: Vector2, speed: Vector2, color: Color):
        self._vertices = []
        self._position = position
        self.speed = speed
        self.color = color
        angle = np.deg2rad(Vector2(1, 0).angle_to(self.speed))
        for point in [Vector2(0, 0), Vector2(-2, -13), Vector2(2, -13)]:
            self._vertices.append(point.rotate_rad(angle - np.pi / 2))

    @property
    def vertices(self):
        return [vertex + self.position for vertex in self._vertices]

    @property
    def position(self):
        return self._position + self.speed * self._time

    def advance(self, dt):
        self._time += dt

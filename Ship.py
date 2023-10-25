from pygame import Vector2, Color, Rect
import numpy as np


class Ship:
    position: Vector2
    speed: Vector2
    color: Color
    _vertices: list[Vector2]

    def __init__(self, position: Vector2, angle: float, speed: float, color: Color):
        self._vertices = []
        self.position = position
        self.speed = (Vector2(1, 0) * speed).rotate_rad(angle)
        self.color = color
        angle = np.deg2rad(Vector2(1, 0).angle_to(self.speed))
        for point in [Vector2(0, 10), Vector2(-2, -3), Vector2(2, -3)]:
            self._vertices.append(point.rotate_rad(angle - np.pi / 2))

    @property
    def vertices(self):
        return [vertex + self.position for vertex in self._vertices]

    def advance(self, dt):
        self.position += self.speed * dt

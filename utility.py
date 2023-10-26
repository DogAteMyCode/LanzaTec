from copy import copy

import numpy as np
from pygame import Vector2

from Planet import Planet


# def speed1(earth: Planet, mars: Planet):
#     d = np.sqrt(mars.radius ** 2 - earth.radius ** 2)
#     t = (np.arccos(
#         (earth.radius * np.cos(earth.angle) - np.sin(earth.angle) * d) / mars.radius) - mars.angle) / mars.angularV
#     if t <= 0:
#         return 0
#     v = d / t * Vector2(-np.sin(earth.angle), np.cos(earth.angle))
#     return v
#
#
# def speed2(earth: Planet, mars: Planet):
#     d = np.sqrt(mars.radius ** 2 - earth.radius ** 2)
#     t = (np.arccos(
#         (earth.radius * np.cos(earth.angle) + np.sin(earth.angle) * d) / mars.radius) - mars.angle) / mars.angularV
#     if t <= 0:
#         return 0
#     v = d / t * Vector2(-np.sin(earth.angle), np.cos(earth.angle))
#     return v
#
# def marcian_year(earth: Planet, mars: Planet):
#     vec = mars.position - earth.position
#     t = 2*np.pi / mars.angularV
#     return vec/t

# def marcian_half_year(earth: Planet, mars: Planet, v_max: float):
#     c_mars = copy(mars)
#     c_mars._angle += np.pi/10
#     vec = c_mars.position - earth.position
#     t = np.pi / c_mars.angularV
#     return vec/t
def marcian_half_year(earth: Planet, mars: Planet, v_max: float):
    c_mars = copy(mars)
    v = Vector2(0, np.inf)
    while v.magnitude() > v_max:
        c_mars._angle += 1
        vec = c_mars.position - earth.position
        t = c_mars._angle / c_mars.angularV
        v = vec / t
    print(v.magnitude())
    return v

def perpendicular(earth: Planet, mars: Planet, v_max: float):

    return v

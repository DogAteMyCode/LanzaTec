from copy import copy
import numpy as np
from pygame import Vector2
from Planet import Planet

def marcian_half_year(earth: Planet, mars: Planet, v_max: float):
    c_mars = copy(mars)
    v = Vector2(0, np.inf)
    while v.magnitude() > v_max:
        c_mars._angle += 1
        vec = c_mars.position - earth.position
        t = c_mars._angle / c_mars.angularV
        v = vec / t
    return v

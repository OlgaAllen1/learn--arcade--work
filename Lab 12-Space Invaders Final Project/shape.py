from arcade import Sprite
from constants import SHIP_SCALE


class Shape(Sprite):
    def __init__(self, filename, shape):
        super().__init__(filename, scale=SHIP_SCALE)
        self.choose_shape = shape

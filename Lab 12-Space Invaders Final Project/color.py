from arcade import Sprite
from constants import COLOR_SCALE


class Color(Sprite):
    def __init__(self, filename, color):
        super().__init__(filename, scale=COLOR_SCALE)
        self.choose_color = color

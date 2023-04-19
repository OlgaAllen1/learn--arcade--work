from arcade import Sprite, Text, load_texture, draw_texture_rectangle
from arcade.color import GRAY
from time import time


class PowerUp(Sprite):
    def __init__(self, filename, cost, cx, cy):
        super().__init__(filename, 1.5)
        self.cost = cost
        self.set_position(cx, cy)
        self.opened = False
        self.locked_texture = load_texture("assets/UI/lock.png")
        self.cost_text = Text(str(self.cost), self.center_x - 15, self.bottom - 10, font_size=16,
                              font_name="kenvector future")
        self.color = GRAY
        self.timer = None
        self.active = False

    def draw(self, **kwargs):
        super().draw()
        self.cost_text.draw()
        if not self.opened:
            draw_texture_rectangle(self.center_x, self.center_y, self.locked_texture.width / 4,
                                   self.locked_texture.height / 4, self.locked_texture)

    def activate(self):
        self.active = True
        self.timer = time()

    def time_end(self):
        if self.active and time() - self.timer >= self.activate_time:
            return True


class LaserCountPowerUp(PowerUp):
    def __init__(self, filename, cost, cx, cy, laser_power):
        super().__init__(filename, cost, cx, cy)
        self.laser_power = laser_power
        self.activate_time = 15


class LaserTypePowerUp(PowerUp):
    def __init__(self, filename, cost, cx, cy, laser_type):
        super().__init__(filename, cost, cx, cy)
        self.laser_type = laser_type
        self.activate_time = 30


class ShipPowerUp(PowerUp):
    def __init__(self, filename, cost, cx, cy):
        super().__init__(filename, cost, cx, cy)
        self.activate_time = 30

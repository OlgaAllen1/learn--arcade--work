from animate import AnimatedSprite
from laser import RicochetLaser, PenetrateLaser, CommonLaser, HomingLaser
from arcade import load_texture
import constants as C


class Player(AnimatedSprite):
    def __init__(self, hp, window, shape="Ship1", color="blue"):
        super().__init__(f"assets/Player/player{shape}_{color}.png", scale=0.8)
        self.center_y = 150
        self.shoot_mode = 1
        self.shape = shape
        self.shape_color = color
        self.hp = hp
        self.laser_type = "common"
        self.window = window

    def change_hp(self, damage):
        self.window.lose_live_sound.play()
        self.hp = self.hp - damage
        self.window.lives.pop()

    def change_shape(self):
        self.texture = load_texture(f"assets/Player/player{self.shape}_{self.shape_color}.png")

    def shooting(self):
        if self.shoot_mode == 1:
            self.common_shooting()
        elif self.shoot_mode == 2:
            self.double_shooting()
        else:
            self.triple_shooting()

    def create_laser(self, scale, x):
        params = {
            "color": self.shape_color,
            "enemies": self.window.enemies,
            "boundary_top": self.window.height,
        }
        if self.laser_type == "common":
            laser = CommonLaser(**params, damage=C.COMMON_LASER_DAMAGE, speed=C.COMMON_LASER_SPEED)
        elif self.laser_type == "ricochet":
            laser = RicochetLaser(**params, damage=C.RICOCHET_LASER_DAMAGE, speed=C.RICOCHET_LASER_SPEED)
        elif self.laser_type == "penetrate":
            laser = PenetrateLaser(**params,
                                   damage=C.PENETRATE_LASER_DAMAGE,
                                   speed=C.PENETRATE_LASER_SPEED,
                                   max_scale=scale
                                   )
        else:
            laser = HomingLaser(**params, damage=C.HOMING_LASER_SPEED, speed=C.HOMING_LASER_DAMAGE)
        laser.set_position(x, self.top)
        self.window.player_lasers.append(laser)
        laser.scale = scale

    def common_shooting(self):
        self.create_laser(1, self.center_x)

    def double_shooting(self):
        self.create_laser(0.8, self.center_x - 30)
        self.create_laser(0.8, self.center_x + 30)

    def triple_shooting(self):
        self.common_shooting()
        self.double_shooting()

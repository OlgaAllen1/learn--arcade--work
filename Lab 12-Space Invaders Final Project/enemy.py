from arcade import Sprite
from random import randint, choice
from time import time
from laser import CommonLaser, RicochetLaser, HomingLaser
import constants as C
from explosion import Explosion


class Enemy(Sprite):
    def __init__(self, hp, window, shape=1):
        colors = ["blue", "green", "red"]
        # random enemy color can't be color of the user
        colors.remove(window.main_player_ship.shape_color)
        self.shape_color = choice(colors)
        super().__init__(f"assets/Enemies/enemy_{self.shape_color}{shape}.png", 1)
        self.window = window
        self.center_x = randint(int(self.width / 2), self.window.width - self.width // 2 - 200)  # set random position x
        self.change_y = C.ENEMY_SPEED
        self.hp = hp

    def change_hp(self, damage):
        self.hp = self.hp - damage

    def update(self):
        self.center_y = self.center_y - self.change_y
        if self.top <= 0:
            self.window.set_game_over()
            self.kill()

    def create_explosion(self):
        explosion = Explosion(self.center_x, self.center_y)
        self.window.explosions.append(explosion)
        self.kill()


class ShootingEnemy(Enemy):
    def __init__(self, hp, window, laser_type, shooting_speed):
        # select shape of enemy according to its laser type
        if laser_type == "common":
            shape = 2
        elif laser_type == "ricochet":
            shape = 3
        else:
            shape = 4

        super().__init__(hp, window, shape, )
        self.shooting_time = time()
        self.laser_type = laser_type
        self.shooting_speed = shooting_speed

    def update(self):
        super().update()
        if self.top <= self.window.height:
            if time() - self.shooting_time >= self.shooting_speed:  # after shooting speed(second) shoot
                self.shoot()

    def shoot(self):
        """
            Method that creates laser for enemy
        """
        self.window.enemy_laser_sound.play(volume=0.1)
        params = (self.shape_color, self.window.player_ships, 1, self.window.height)
        if self.laser_type == "common":
            laser = CommonLaser(*params, -C.COMMON_LASER_SPEED)
        elif self.laser_type == "homing":
            laser = HomingLaser(*params, C.HOMING_LASER_SPEED)
        else:
            laser = RicochetLaser(*params, -C.RICOCHET_LASER_SPEED)
        laser.set_position(self.center_x, self.bottom)
        self.window.enemies_lasers.append(laser)
        self.shooting_time = time()

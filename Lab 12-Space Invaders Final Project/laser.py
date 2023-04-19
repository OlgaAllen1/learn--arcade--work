from arcade import Sprite, check_for_collision_with_list
import constants as C
from time import time
import math


class Laser(Sprite):
    """
        Base Laser Class
    """

    def __init__(self, color, laser_type, speed, damage, boundary_top, enemies):
        super().__init__(f"assets/Lasers/laser_{color}_{laser_type}.png", scale=1)
        self.damage = damage
        self.change_y = speed
        self.enemies = enemies
        self.boundary_top = boundary_top

    def update(self):
        self.center_y = self.center_y + self.change_y  # just go up

    def check_collision_with_enemies(self):
        # Check if collides with enemies
        hits = check_for_collision_with_list(self, self.enemies)
        if len(hits) > 0:
            for enemy in hits:
                enemy.change_hp(self.damage)
            return True

    def check_boundary(self):
        if self.change_y < 0:
            return self.top <= 0
        else:
            return self.bottom >= self.boundary_top


class CommonLaser(Laser):
    """
        Common Laser Class
    """

    def __init__(self, color, enemies, damage, boundary_top, speed):
        super().__init__(color, "common", speed, damage, boundary_top, enemies)

    def update(self):
        super().update()
        if self.check_boundary() or self.check_collision_with_enemies():  # if out the screen kill the sprite
            self.kill()


class RicochetLaser(Laser):
    """
        Ricochet Laser Class
    """

    def __init__(self, color, enemies, damage, boundary_top, speed):
        super().__init__(color, "ricochet", speed, damage, boundary_top, enemies)
        self.ricochet_times = 0

    def update(self):
        super().update()
        self.angle += C.RICOCHET_ROTATION_SPEED
        if self.bottom <= 0 or self.top >= self.boundary_top or self.check_collision_with_enemies():
            # if collides with screen borders
            self.ricochet()

        if self.ricochet_times >= 5:  # if ricochet count >= 5 kill the sprite
            self.kill()

    def ricochet(self):
        self.change_y = -self.change_y  # ricochet
        self.ricochet_times += 1  # increase ricochet count by 1


class PenetrateLaser(Laser):
    """
        Penetrate Laser Class
    """

    def __init__(self, color, enemies, damage, max_scale, boundary_top, speed):
        super().__init__(color, "penetrate", speed, damage, boundary_top, enemies)
        self.change_scale = C.PENETRATE_PULSE_SPEED
        self.max_scale = max_scale

    def update(self):
        super().update()
        self.pulse()
        self.check_collision_with_enemies()
        if self.check_boundary():  # if out the screen kill the sprite
            self.kill()

    def pulse(self):
        self.scale += self.change_scale
        if self.scale >= self.max_scale + 0.3 or self.scale <= self.max_scale - 0.3:
            self.change_scale = -self.change_scale


class HomingLaser(Laser):
    def __init__(self, color, enemies, damage, boundary_top, speed):
        super().__init__(color, "homing", speed, damage, boundary_top, enemies)
        self.speed = speed
        self.live_time = time()

    def update(self):
        super().update()
        if self.check_collision_with_enemies() or self.check_boundary():
            self.kill()
        self.center_x = self.center_x + self.change_x
        if len(self.enemies) > 0:
            # Calculate the angle between the laser and the player

            player_x, player_y = self.enemies[0].position
            laser_x, laser_y = self.position
            angle = math.atan2(player_y - laser_y, player_x - laser_x)

            # Turn the laser towards the player
            self.angle = math.degrees(angle) - 90
            if self.angle < 0:
                self.angle += 360

            # Move the laser forward
            self.change_x = math.cos(angle) * self.speed
            self.change_y = math.sin(angle) * self.speed

        if time() - self.live_time >= 5:
            self.kill()

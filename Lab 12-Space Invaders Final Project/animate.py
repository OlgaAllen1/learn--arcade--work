import arcade


class AnimatedSprite(arcade.Sprite):
    i = 0
    time = 0

    def update_animation(self, delta_time=1/60):
        self.time += delta_time
        if self.time >= 0.1:
            self.time = 0
            if self.i == len(self.textures) - 1:
                self.i = 0
            else:
                self.i += 1
            self.set_texture(self.i)

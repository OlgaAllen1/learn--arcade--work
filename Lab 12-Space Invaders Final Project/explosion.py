from arcade import load_texture, Sprite


class Explosion(Sprite):
    def __init__(self, x, y):
        super().__init__("assets/Effects/explosion00.png", scale=0.2)
        self.set_position(x, y)
        self.i = 0
        self.time = 0
        for i in range(1, 9):
            self.append_texture(load_texture(f"assets/Effects/explosion0{i}.png"))

    def update_animation(self, delta_time=1/60):
        self.time += delta_time
        if self.time >= 0.1:
            self.time = 0
            if self.i == len(self.textures) - 1:
                self.kill()
            else:
                self.i += 1
            self.set_texture(self.i)

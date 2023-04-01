import arcade 


class Trap(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, scale=0.75)
    
    def update(self):
        self.angle += self.change_angle
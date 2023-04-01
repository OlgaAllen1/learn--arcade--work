import arcade 
from animate import AnimatedSprite
from constants import PLAYER_SPEED


class Player(AnimatedSprite):
    def __init__(self, start_x, start_y):
        super().__init__("assets\images\player\player-stand.png", scale=0.6)
        self.walk_right_frames = []
        self.walk_left_frames = []
        self.run_right_frames = []
        self.run_left_frames = []
        self.start_x = start_x
        self.start_y = start_y

        for i in range(8):
            self.walk_right_frames.append(arcade.load_texture(f"assets\images\player\walk\walk{i}.png"))
            self.walk_left_frames.append(arcade.load_texture(f"assets\images\player\walk\walk{i}.png", 
                                                             flipped_horizontally=True))
        
        self.is_moving = False
        self.is_jumping = False
        self.direction = 1 # 1 - right, 2 - left

    def reset(self): 
        self.stand()
        self.set_position(self.start_x, self.start_y)

    def change_costumes(self): 
        if self.direction == 1:
            self.textures = self.walk_right_frames
        else: 
            self.textures = self.walk_left_frames

    def change_jump_costume(self):
        if self.is_jumping:
            if self.direction == 1: 
                self.texture = arcade.load_texture("assets\images\player\player-jump.png")
            else: 
                self.texture = arcade.load_texture("assets\images\player\player-jump.png", flipped_horizontally=True)

    def change_stand_constume(self):
        if not self.is_moving:
            if self.direction == 1:
                self.texture = arcade.load_texture("assets\images\player\player-stand.png")
            else: 
                self.texture = arcade.load_texture("assets\images\player\player-stand.png", flipped_horizontally=True)

    def go_left(self):
        self.direction = 2
        self.is_moving = True
        self.change_costumes()
        self.change_x = -PLAYER_SPEED

    def go_right(self):
        self.direction = 1
        self.is_moving = True
        self.change_costumes()
        self.change_x = PLAYER_SPEED
    
    def stand(self):
        self.is_moving = False
        self.change_x = 0

    def update(self):
        if self.is_jumping:
            self.change_jump_costume()
        elif not self.is_moving:
            self.change_stand_constume()

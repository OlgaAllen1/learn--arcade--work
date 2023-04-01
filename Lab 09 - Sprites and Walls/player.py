import arcade 
from animate import AnimatedSprite
from constants import PLAYER_SPEED


class Player(AnimatedSprite):
    def __init__(self, start_x, start_y):
        super().__init__("assets/images/player/player-stand.png", scale=0.6)
        self.walk_right_frames = []
        self.walk_left_frames = []
        self.start_x = start_x
        self.start_y = start_y

        for i in range(8):
            """Loading all textures from walk folder in images from 0-7"""
            self.walk_right_frames.append(arcade.load_texture(f"assets/images/player/walk/walk{i}.png"))
            """Initially all images are right-sided, we flip them when go left"""
            self.walk_left_frames.append(arcade.load_texture(f"assets/images/player/walk/walk{i}.png", 
                                                             flipped_horizontally=True))
        """Shows if player is moving or standing still"""
        self.is_moving = False
        self.is_jumping = False
        self.direction = 1  # 1 - right, 2 - left (direction where our player is headed)

    def reset(self):
        """Reset user to the starting position, not moving"""
        self.stand()
        self.set_position(self.start_x, self.start_y)

    def change_costumes(self): 
        if self.direction == 1:
            """The images of the player depends on where the player is facing"""
            self.textures = self.walk_right_frames
        else: 
            self.textures = self.walk_left_frames

    def change_jump_costume(self):
        if self.is_jumping:
            if self.direction == 1:
                # images of the jumping costume depends on where the player is facing
                self.texture = arcade.load_texture("assets/images/player/player-jump.png")
            else: 
                self.texture = arcade.load_texture("assets/images/player/player-jump.png", flipped_horizontally=True)

    def change_stand_costume(self):
        if not self.is_moving:
            if self.direction == 1:
                self.texture = arcade.load_texture("assets/images/player/player-stand.png")
            else: 
                self.texture = arcade.load_texture("assets/images/player/player-stand.png", flipped_horizontally=True)

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
        """If the player is jumping, we change image to jumping, if the player is standing - stand image"""
        if self.is_jumping:
            self.change_jump_costume()
        elif not self.is_moving:
            self.change_stand_costume()

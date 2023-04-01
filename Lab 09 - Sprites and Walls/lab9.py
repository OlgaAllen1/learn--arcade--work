import arcade  
from constants import *
import random
from player import Player
from trap import Trap
from maps import *
from button import Button
from utils import difference


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        """ SOUND """
        self.bg_sound = arcade.load_sound("assets/audio/Cave.wav")
        self.gem_sound = arcade.load_sound("assets/audio/Collect.wav")
        self.door_sound = arcade.load_sound("assets/audio/Door Closing.wav")
        self.lose_live_sound = arcade.load_sound("assets/audio/Crunch.wav")
        self.lose_sound = arcade.load_sound("assets/audio/Oops.wav")
        self.win_sound = arcade.load_sound("assets/audio/Triumph.wav")
        self.music_player = arcade.play_sound(self.bg_sound, 0.3, looping=True)
        """ Sprite Lists """
        self.tiles = None
        self.traps = None
        self.lives = None
        self.gems = None
        self.player = Player(difference(1, TILE_WIDTH) , difference(1, TILE_HEIGHT))
        self.rooms = [ROOM_1, ROOM_2, ROOM_3, ROOM_4]
        self.current_room = 0
        self.win = False
        self.lose = False
        self.room = self.rooms[self.current_room]
        self.key = None
        self.door = None
        self.set_mouse_visible(False)
        self.mouse_cursor = arcade.Sprite("assets/images/ui/cursor_hand.png")
        arcade.load_font("assets/font/kenvector_future.ttf")
        self.win_text = arcade.Text("YOU WIN!", SCREEN_WIDTH/6, SCREEN_HEIGHT/2, arcade.color.GHOST_WHITE,
                                    75, font_name="kenvector future")
        self.lose_text = arcade.Text("YOU LOSE!", SCREEN_WIDTH/6, SCREEN_HEIGHT/2, arcade.color.RED, 70,
                                     font_name="kenvector future")
        self.gems_count = 0
        self.gems_text = arcade.Text(f"GEMS: {self.gems_count}", difference(1, TILE_WIDTH), difference(ROW_COUNT-3, TILE_HEIGHT),  arcade.color.WHITE, 15,
                                     font_name="kenvector future")
        
        self.restart_button = Button("RESTART", "assets/images/ui/yellow_button00.png", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-80)
        self.setup()
        self.setup_lives()

    def on_draw(self): 
        self.clear((24, 119, 87))
        self.tiles.draw()
        self.traps.draw()
        if self.key is not None:
            self.key.draw()
        if self.door is not None:
            self.door.draw()
        self.player.draw()
        self.lives.draw()
        self.gems_text.draw()
        self.gems.draw()
        if self.win: 
            self.win_text.draw()
        if self.lose: 
            self.lose_text.draw()
        if self.win or self.lose: 
            self.restart_button.draw()
            self.mouse_cursor.draw()
     
    def update(self, delta_time):
        if self.win or self.lose:
            return 
        if len(self.lives) == 0: 
            self.lose = True
            self.player.stand()
            arcade.stop_sound(self.music_player)
            self.music_player = arcade.play_sound(self.lose_sound)
        if self.player.is_moving: 
            self.player.update_animation(delta_time)

        self.player.update()
        self.physics_engine.update()
        self.traps.update()
        
        if self.physics_engine.can_jump():
            self.player.is_jumping = False
        
        hits = arcade.check_for_collision_with_list(self.player, self.traps)
        if len(hits) > 0:
            for trap in hits: 
                self.lives.pop()        
                self.player.reset()
                arcade.play_sound(self.lose_live_sound)

        hits = arcade.check_for_collision_with_list(self.player, self.gems)
        if len(hits) > 0:
            for gem in hits: 
                self.gems_count += 1
                self.gems_text.text = f"GEMS: {self.gems_count}"
                gem.kill()
                arcade.play_sound(self.gem_sound)

        if self.key is not None : 
            if arcade.check_for_collision(self.player, self.key):
                self.key = None 
                self.door.texture = arcade.load_texture("assets/images/doors/door-open.png")
                arcade.play_sound(self.door_sound)
        elif self.door is not None: 
            if arcade.check_for_collision(self.player, self.door):
                self.current_room += 1
                if self.current_room < len(self.rooms):
                    self.room = self.rooms[self.current_room] 
                    self.door = None
                    self.setup()
                else: 
                    self.win = True
                    arcade.stop_sound(self.music_player)
                    self.music_player = arcade.play_sound(self.win_sound)

    def setup_lives(self):
        """The method that adds three hearts in the left top corner to show how many lives left"""
        self.lives = arcade.SpriteList()
        for i in range(3):
            heart = arcade.Sprite("assets/images/player/heart.png")
            heart.center_x = difference(i+1, TILE_WIDTH)
            heart.center_y = difference(ROW_COUNT-2, TILE_HEIGHT)
            self.lives.append(heart)

    def setup_borders(self):
        """ The method that sets up walls on every level"""
        for y in range(ROW_COUNT): 
            for x in range(COLUMN_COUNT):
                if y == 0 or y == ROW_COUNT - 1 or x == 0 or x == COLUMN_COUNT - 1: 
                    tile = arcade.Sprite("assets/images/tiles/tile1.png", scale=0.75)
                    tile.center_x = difference(x, TILE_WIDTH)
                    tile.center_y = difference(y, TILE_HEIGHT)
                    self.tiles.append(tile)

    def setup(self):
        """ The method that setups every level """
        self.tiles = arcade.SpriteList()
        self.traps = arcade.SpriteList()
        self.gems = arcade.SpriteList()
        self.setup_borders()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=PLAYER_GRAVITY, walls=self.tiles)
        self.player.reset()
        # ROOM BLOCKS
        random_color = random.randint(1, 4)
        for y in range(0, ROW_COUNT - 2): 
            for x in range(0, COLUMN_COUNT - 2):
                if self.room[y][x] == "w":
                    tile = arcade.Sprite("assets/images/tiles/tile2.png", scale=0.75)
                    tile.center_x =  difference(x+1, TILE_WIDTH)
                    tile.center_y = difference(y+1, TILE_HEIGHT)
                    self.tiles.append(tile)
                elif self.room[y][x] == "g":
                    gem = arcade.Sprite(f"assets/images/gems/gem{random_color}.png", scale=0.75)
                    gem.center_x =  difference(x+1, TILE_WIDTH)
                    gem.center_y = difference(y+1, TILE_HEIGHT)
                    self.gems.append(gem)
                elif self.room[y][x] == "t":
                    random_trap = random.randint(1, 2)
                    trap = Trap(f"assets/images/traps/trap{random_trap}.png")
                    if random_trap == 2: 
                        trap.change_angle = TRAP_SPIN_SPEED
                    trap.center_x = difference(x+1, TILE_WIDTH)
                    trap.center_y = difference(y+1, TILE_HEIGHT)
                    self.traps.append(trap)
                elif self.room[y][x] == "k":
                    self.key = arcade.Sprite(f"assets/images/keys/key{random_color}.png", scale=0.75)
                    self.key.center_x = difference(x+1, TILE_WIDTH) 
                    self.key.center_y = difference(y+1, TILE_HEIGHT)
                elif self.room[y][x] == "d":
                    self.door = arcade.Sprite(f"assets/images/doors/door{random_color}.png", scale=0.75)
                    self.door.center_x = difference(x+1, TILE_WIDTH)
                    self.door.center_y = difference(y+1, TILE_HEIGHT)
    
    def restart(self):
        self.current_room = 0
        self.win = False
        self.lose = False
        self.player.stand()
        self.gems_count = 0
        arcade.stop_sound(self.music_player)
        self.music_player = arcade.play_sound(self.bg_sound, 0.3, looping=True)     
        self.gems_text.text = f"GEMS: {self.gems_count}"
        self.room = self.rooms[self.current_room]
        self.setup()
        self.setup_lives()

    def on_key_press(self, key, modifiers):
        if self.win or self.lose:
            return 
        if key == arcade.key.RIGHT: 
            self.player.go_right()
        if key == arcade.key.LEFT: 
            self.player.go_left()
        
        if key == arcade.key.SPACE and self.physics_engine.can_jump():
            self.physics_engine.jump(PLAYER_JUMP_HEIGHT)
            self.player.is_jumping = True

    def on_key_release(self, key, modifiers):
        if self.win or self.lose:
            return 
        if key == arcade.key.RIGHT or key == arcade.key.LEFT : 
            self.player.stand()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.win or self.lose:
            self.mouse_cursor.center_x = x
            self.mouse_cursor.center_y = y
            if self.restart_button.left < x < self.restart_button.right  and self.restart_button.bottom < y < self.restart_button.top:
                self.restart_button.texture = arcade.load_texture("assets/images/ui/yellow_button01.png")
            else: 
                self.restart_button.texture = arcade.load_texture("assets/images/ui/yellow_button00.png")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.win or self.lose and button == arcade.MOUSE_BUTTON_LEFT:
            if self.restart_button.left < x < self.restart_button.right  and self.restart_button.bottom < y < self.restart_button.top:
                self.restart()

            
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()

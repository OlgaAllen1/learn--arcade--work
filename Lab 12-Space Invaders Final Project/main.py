import arcade
import random
from time import time
from constants import *
from color import Color
from shape import Shape
from button import Button
from player import Player
from enemy import ShootingEnemy, Enemy
from utils import *
from powerup import LaserCountPowerUp, LaserTypePowerUp, ShipPowerUp
from explosion import Explosion


class Game(arcade.Window):
    """Main class for the game"""
    
    def __init__(self, title):
        super().__init__(title=title, fullscreen=True)
        self.set_mouse_visible(False)

        # Loading Background textures 
        self.bg = arcade.load_texture("assets/Backgrounds/black.png")
        self.planet = arcade.load_texture("assets/Backgrounds/planet.png")

        self.menu = True
        self.pause = False

        # Loading Custom Font
        arcade.load_font("assets/Font/kenvector_future.ttf")
        self.cursor = arcade.Sprite("assets/UI/cursor.png")

        # Texts
        self.choose_text = arcade.Text(
            "Choose you spaceship!",
            self.width / 5,
            self.height - 100,
            font_size=50,
            font_name="kenvector future"
        )

        self.color_text = arcade.Text(
            "Color",
            self.width / 5,
            self.height / 2,
            font_size=28,
            font_name="kenvector future"
        )

        self.shape_text = arcade.Text(
            "Shape",
            self.width / 5,
            self.height / 2 - 200,
            font_size=28,
            font_name="kenvector future"
        )

        self.start_timer_text = arcade.Text(
            "3",
            self.width / 2,
            self.height / 2,
            font_size=75,
            font_name="kenvector future"
        )

        self.score_text = arcade.Text(
            "SCORE: 0",
            self.width - 170,
            self.height - 150,
            font_size=18,
            font_name="kenvector future"
        )

        self.level_text = arcade.Text(
            "LEVEL: 1",
            50,
            self.height - 50,
            font_size=18,
            font_name="kenvector future"
        )
        self.end_game_text = arcade.Text(
            "",
            self.width / 4,
            self.height / 2 + 100,
            font_size=75,
            font_name="kenvector future"
        )

        self.record_text = arcade.Text(
            "RECORD: 0",
            50,
            self.height - 100,
            font_size=18,
            font_name="kenvector future"
        )
        # Start Timer
        self.start_timer = time()
        self.start_countdown = 3
        self.start = False

        # Game Over
        self.game_over = False
        # Win
        self.win = False
        # Player score
        self.score = 0
        # Player record
        self.record = 0
        # Level count
        self.level = 1

        # SpriteLists 
        self.player_ships = arcade.SpriteList()
        self.main_player_ship = Player(3, self)
        self.player_ships.append(self.main_player_ship)

        self.colors = arcade.SpriteList()
        self.shapes = arcade.SpriteList()
        self.lives = None
        self.player_lasers = arcade.SpriteList()
        self.enemies = None
        self.enemies_lasers = arcade.SpriteList()
        self.explosions = arcade.SpriteList()
        Explosion(-100,
                  -100)  # first explosion, to make animation work faster, to prevent cooldown after first enemy kill
        self.power_ups = arcade.SpriteList()
        self.setup_colors()
        self.setup_shapes()

        # Buttons
        self.choose_button = Button("CHOOSE", "assets/UI/button_blue.png", self.width / 2, 100)
        self.pause_button = Button("MENU", "assets/UI/button_blue.png", self.width - 50, 100)
        self.resume_button = Button("RESUME", "assets/UI/button_blue.png", self.width / 2, self.height / 2 + 50)
        self.quit_button = Button("QUIT", "assets/UI/button_blue.png", self.width / 2, self.height / 2 - 50)
        self.restart_button = Button("RESTART", "assets/UI/button_blue.png", self.width / 2, self.height / 2)

        # Sounds
        self.explosion_sound = arcade.Sound("assets/Sounds/lowFrequency_explosion_000.ogg")
        self.power_up_sound = arcade.Sound("assets/Sounds/power-up.ogg")
        self.laser_sound = arcade.Sound("assets/Sounds/laserLarge_003.ogg")
        self.select_sound = arcade.Sound("assets/Sounds/click.ogg")
        self.lose_live_sound = arcade.Sound("assets/Sounds/sfx_lose_live.ogg")
        self.enemy_laser_sound = arcade.Sound("assets/Sounds/laserSmall_004.ogg")
        self.game_sound = arcade.Sound("assets/Sounds/Movie 2.wav")
        self.menu_sound = arcade.Sound("assets/Sounds/Drip Drop.wav")
        self.player = self.menu_sound.play(volume=0.1, loop=True)

    def setup_colors(self):
        """
            Method that creates colors on the screen, and places them
        """
        blue = Color("assets/UI/dotBlue.png", "blue")
        blue.scale = COLOR_CHOSEN_SCALE
        green = Color("assets/UI/dotGreen.png", "green")
        red = Color("assets/UI/dotRed.png", "red")
        blue.set_position(self.width / 2, self.height / 2 + 20)
        green.set_position(self.width / 2 + 100, self.height / 2 + 20)
        red.set_position(self.width / 2 + 200, self.height / 2 + 20)
        self.colors.append(blue)
        self.colors.append(green)
        self.colors.append(red)

    def setup_powerups(self):
        """
            Method that creates powerups in the menu
        """
        power_up = LaserCountPowerUp(
            f"assets/Power-ups/double_laser_{self.main_player_ship.shape_color}.png",
            10, self.width - 75, self.height / 2 + 225, 2
        )
        power_up_2 = LaserCountPowerUp(
            f"assets/Power-ups/triple_laser_{self.main_player_ship.shape_color}.png",
            20, self.width - 75, self.height / 2 + 150, 3
        )
        power_up_3 = LaserTypePowerUp(
            f"assets/Power-ups/{self.main_player_ship.shape_color}_ricochet.png",
            25, self.width - 75, self.height / 2 + 75, "ricochet"
        )
        power_up_4 = LaserTypePowerUp(
            f"assets/Power-ups/{self.main_player_ship.shape_color}_penetrate.png",
            30, self.width - 75, self.height / 2, "penetrate"
        )
        power_up_5 = LaserTypePowerUp(
            f"assets/Power-ups/{self.main_player_ship.shape_color}_homing.png",
            30, self.width - 75, self.height / 2 - 75, "homing"
        )
        power_up_6 = ShipPowerUp(
            f"assets/Power-ups/{self.main_player_ship.shape}_{self.main_player_ship.shape_color}_add.png",
            30, self.width - 75, self.height / 2 - 150
        )
        self.power_ups.append(power_up)
        self.power_ups.append(power_up_2)
        self.power_ups.append(power_up_3)
        self.power_ups.append(power_up_4)
        self.power_ups.append(power_up_5)
        self.power_ups.append(power_up_6)

    def setup_lives(self):
        """
            Method that creates lives of player, according to shape and color
        """
        self.lives = arcade.SpriteList()
        for i in range(3):
            live = arcade.Sprite(
                f"assets/Lives/player{self.main_player_ship.shape}_{self.main_player_ship.shape_color}.png", 1)
            live.set_position(self.width - 150 + 60 * i, self.height - 100)
            self.lives.append(live)

    def setup_shapes(self):
        """
            Method that creates shapes on the screen, and places them
        """
        for i in range(1, 5):
            shape = Shape(f"assets/Player/playerShip{i}_blue.png", f"Ship{i}")
            shape.set_position(self.width / 3 + 180 * i, self.height / 2 - 200 + 20)
            self.shapes.append(shape)
        self.shapes[0].scale = SHIP_CHOSEN_SCALE

    def setup_common_enemies(self, hp, enemy_count, enemy_speed=ENEMY_SPEED):
        """
            Method that creates common enemies 
        """
        for i in range(enemy_count):
            enemy = Enemy(hp, self)
            enemy.change_y = enemy_speed
            enemy.center_y = self.height + 100 * i
            self.enemies.append(enemy)

    def setup_shooting_enemies(self, hp, enemy_count, laser_type="common", shooting_speed=ENEMY_SHOOTING_TIMER):
        """
            Method that creates shooting enemies 
        """
        for i in range(enemy_count):
            if isinstance(laser_type, tuple):
                laser = random.choice(laser_type)
            else:
                laser = laser_type
            enemy = ShootingEnemy(hp, self, laser, shooting_speed)
            enemy.center_y = self.height + 100 * i
            self.enemies.append(enemy)

    def setup_levels(self):
        """
            Method that creates levels
        """
        if self.level == 1:
            self.enemies = arcade.SpriteList()
            self.setup_common_enemies(1, 25)
        elif self.level == 2:
            self.setup_common_enemies(2, 25, ENEMY_SPEED + 0.2)
        elif self.level == 3:
            self.setup_shooting_enemies(3, 25, "common")
        elif self.level == 4:
            self.setup_shooting_enemies(4, 30, "ricochet")
        elif self.level == 5:
            self.setup_shooting_enemies(5, 40, "homing", ENEMY_SHOOTING_TIMER - 0.5)
        elif self.level == 6:
            self.setup_shooting_enemies(6, 40, ("homing", "ricochet", "common"), ENEMY_SHOOTING_TIMER - 1)
        elif self.level == 7:
            self.setup_common_enemies(8, 30, ENEMY_SPEED + 0.2)
            self.setup_shooting_enemies(8, 10, ("homing", "ricochet", "common"), ENEMY_SHOOTING_TIMER - 1.5)
        else:
            self.win = True
            self.end_game_text.text = "YOU WIN!"
            self.end_game_text.x = self.width / 3

    def setup_countdown_timer(self):
        self.start = False
        self.start_countdown = 3
        self.start_timer_text.text = self.start_countdown
        self.start_timer = time()

    def on_draw(self):
        self.clear()
        # Drawing background of the game
        arcade.draw_texture_rectangle(
            self.width / 2,
            self.height / 2,
            self.width,
            self.height,
            self.bg
        )
        # Drawing the planet
        arcade.draw_texture_rectangle(
            self.width / 2,
            -self.height / 3,
            self.planet.width,
            self.planet.height,
            self.planet
        )

        if self.menu:  # in menu mode
            self.choose_text.draw()
            self.color_text.draw()
            self.colors.draw()
            self.shape_text.draw()
            self.shapes.draw()
            self.choose_button.draw()
        else:
            self.player_ships.draw()
            self.enemies.draw()
            self.enemies_lasers.draw()
            self.explosions.draw()
            self.player_lasers.draw()
            self.lives.draw()
            # Player shop
            arcade.draw_rectangle_filled(
                self.width - 75,
                self.height / 2 + 25,
                100,
                500,
                arcade.color.DARK_BLUE_GRAY
            )

            # Power ups
            for power_up in self.power_ups:
                power_up.draw()

            # Player score 
            self.score_text.draw()
            # Level 
            self.level_text.draw()
            # Record
            self.record_text.draw()

        # Drawing pause button
        self.pause_button.draw()

        if self.game_over or self.win :
            self.end_game_text.draw()
        
        if self.pause:
            arcade.draw_rectangle_filled(
                self.width / 2,
                self.height / 2,
                300,
                250,
                arcade.color.WHITE
            )
            self.resume_button.draw()
            if self.menu:
                self.quit_button.center_y = self.height / 2
                self.quit_button.text.y = self.quit_button.center_y - 5
            else:
                self.quit_button.center_y = self.height / 2 - 50
                self.quit_button.text.y = self.quit_button.center_y - 5
            self.quit_button.draw()
        
        if (self.game_over or self.win or self.pause) and not self.menu:
            self.restart_button.draw()

        if not self.pause and not self.menu and not self.start and not self.win and not self.game_over:
            self.start_timer_text.draw()
        # Drawing cursor
        self.cursor.draw()
        arcade.finish_render()

    def update(self, delta_time):
        if self.menu or self.pause or self.game_over or self.win:
            return

        if not self.start:
            if time() - self.start_timer > 1:
                self.start_countdown = self.start_countdown - 1
                self.start_timer = time()
                self.start_timer_text.text = self.start_countdown
            if self.start_countdown == 0:
                self.start = True
            return
        self.player_lasers.update()
        self.enemies.update()
        self.enemies_lasers.update()
        self.explosions.update_animation()

        if len(self.enemies) == 0:
            self.level = self.level + 1
            self.setup_levels()
            self.level_text.text = f"LEVEL: {self.level}"

        # if any of enemies are destroyed create an explosion after them
        for enemy in self.enemies:
            if enemy.hp <= 0:
                enemy.create_explosion()
                self.explosion_sound.play()
                # Increase score by 1 and change score text on the screen
                self.score = self.score + 1
                self.update_score_text()
                if self.score > self.record:
                    self.record = self.score
                    self.record_text.text = f"RECORD: {self.record}"

            # Check if player collides with enemies 
            hits = arcade.check_for_collision_with_list(enemy, self.player_ships)
            if len(hits) > 0:
                enemy.create_explosion()
                for player in hits:
                    player.change_hp(1)

        # Open power up is player has enough money
        for power in self.power_ups:
            if self.score >= power.cost:
                power.opened = True
                power.color = arcade.color.WHITE
            else:
                power.opened = False
                power.color = arcade.color.GRAY
            if power.time_end():
                power.active = False
                if isinstance(power, LaserCountPowerUp):
                    self.change_players_shoot(1)
                elif isinstance(power, LaserTypePowerUp):
                    self.change_players_laser("common")
                else:
                    while len(self.player_ships) != 1:
                        self.player_ships.pop()

        # Check if player lasers collide with enemy lasers 
        for laser in self.enemies_lasers:
            hits = arcade.check_for_collision_with_list(laser, self.player_lasers)
            if len(hits) > 0:
                laser.kill()
                for player_laser in hits:
                    player_laser.kill()

        if self.main_player_ship.hp == 0:
            self.set_game_over()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor.set_position(x, y)
        if self.win or self.game_over or self.pause or self.menu or not self.start:
            return
            # To make cursor move with user mouse

        # Move user's ship to the cursor position x
        if x < self.width - 200:
            self.main_player_ship.center_x = x

        # If user have more than 1 ship
        if len(self.player_ships) > 1:
            for i in range(1, len(self.player_ships)):
                if i % 2 == 0:  # for even i values, make center_x negative
                    center_x = self.main_player_ship.center_x - 100 * (i // 2)
                else:  # for odd i values, make center_x positive
                    center_x = self.main_player_ship.center_x + 100 * (i // 2 + 1)
                self.player_ships[i].center_x = center_x

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Handle click on Pause Button
            if check_item_clicked(x, y, self.pause_button):
                self.pause = True
                self.select_sound.play(volume=0.1)

            # Handle click on Restart Button
            elif check_item_clicked(x, y, self.restart_button) and (self.game_over or self.win or self.pause) and not self.menu:
                self.restart()
                self.select_sound.play(volume=0.1)
                self.pause = False

            if self.pause:
                # Handle click on Resume Button
                if check_item_clicked(x, y, self.resume_button):
                    self.pause = False
                    self.setup_countdown_timer()
                    self.select_sound.play(volume=0.1)

                # Handle click on Quit Button
                elif check_item_clicked(x, y, self.quit_button):
                    self.close()

            elif self.menu:
                # Choosing color
                for color in self.colors:
                    if check_item_clicked(x, y, color):
                        self.select_sound.play(volume=0.1)

                        # Reset all colors scales
                        for c in self.colors:
                            c.scale = COLOR_SCALE

                        # Save chosen color
                        self.main_player_ship.shape_color = color.choose_color

                        # Make chosen color bigger
                        color.scale = COLOR_CHOSEN_SCALE

                        # Change buttons texture depending on chosen color 
                        button_texture = arcade.load_texture(f"assets/UI/button_{color.choose_color}.png")
                        self.choose_button.texture = button_texture
                        self.pause_button.texture = button_texture
                        self.resume_button.texture = button_texture
                        self.quit_button.texture = button_texture
                        self.restart_button.texture = button_texture

                        # Change Shapes textures depending on chosen color 
                        for shape in self.shapes:
                            shape.texture = arcade.load_texture(
                                f"assets/Player/player{shape.choose_shape}_{color.choose_color}.png")

                # Choosing Shape of SpaceShip
                for shape in self.shapes:
                    if check_item_clicked(x, y, shape):
                        self.select_sound.play(volume=0.1)

                        # Reset all shapes scales
                        for s in self.shapes:
                            s.scale = SHIP_SCALE

                        # Save chosen shape
                        self.main_player_ship.shape = shape.choose_shape

                        # Make chosen shape bigger
                        shape.scale = SHIP_CHOSEN_SCALE

                # Handle clicking to "Choose button"
                if check_item_clicked(x, y, self.choose_button):
                    self.select_sound.play(volume=0.1)
                    self.menu = False  # Turn off menu mode
                    self.setup_countdown_timer()
                    self.setup_levels()
                    self.start_timer = time()
                    # Creating player according to user choice
                    self.main_player_ship.change_shape()
                    self.main_player_ship.center_x = self.width / 2
                    self.setup_powerups()
                    arcade.stop_sound(self.player)
                    self.player = self.game_sound.play(volume=0.1, loop=True)
                    self.setup_lives()
            elif not self.game_over and not self.win:
                if self.start and x < self.width - 200:
                    self.laser_sound.play(volume=0.1)
                    for player in self.player_ships:
                        player.shooting()

                # If user choose a power up
                for power_up in self.power_ups:
                    if check_item_clicked(x, y, power_up) and power_up.opened:
                        self.power_up_sound.play()
                        self.score = self.score - power_up.cost
                        self.update_score_text()
                        power_up.activate()
                        if isinstance(power_up, LaserCountPowerUp):
                            self.change_players_shoot(power_up.laser_power)
                        elif isinstance(power_up, LaserTypePowerUp):
                            self.change_players_laser(power_up.laser_type)
                        else:
                            self.create_ship()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.pause = not self.pause
            if not self.pause:
                self.setup_countdown_timer()

    def restart(self):
        arcade.stop_sound(self.player)
        self.player = self.menu_sound.play(volume=0.1, loop=True)
        self.game_over = False
        self.win = False
        self.menu = True
        destroy_all_sprites(self.lives)
        self.setup_lives()
        self.main_player_ship.hp = 3
        destroy_all_sprites(self.enemies)
        destroy_all_sprites(self.explosions)
        self.player_lasers.clear()
        self.enemies_lasers.clear()
        self.level = 1
        self.level_text.text = f"LEVEL: {self.level}"
        self.score = 0
        self.update_score_text()
        self.setup_levels()

    def update_score_text(self):
        self.score_text.text = f"SCORE: {self.score}"

    def change_players_shoot(self, mode):
        for player in self.player_ships:
            player.shoot_mode = mode

    def change_players_laser(self, ltype):
        for player in self.player_ships:
            player.laser_type = ltype

    def create_ship(self):
        player = Player(1, self, self.main_player_ship.shape, self.main_player_ship.shape_color)
        player.center_x = self.main_player_ship.center_x
        player.laser_type = self.main_player_ship.laser_type
        player.shoot_mode = self.main_player_ship.shoot_mode
        self.player_ships.append(player)

    def set_game_over(self):
        self.game_over = True
        self.end_game_text.x = self.width / 4
        self.end_game_text.text = "GAME OVER"


window = Game(SCREEN_TITLE)
arcade.run()

import arcade
import random
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "GOOD-BAD"
BUNNY_SPEED = 7
EGG_SPEED = 2
EGGS_COUNT = 50
TIMER = 30


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bunny = Bunny()
        self.easter_eggs = arcade.SpriteList()
        self.rotten_eggs = arcade.SpriteList()
        self.score = 0
        self.time = time.time()
        self.timer = TIMER
        self.bg = arcade.load_texture("images/bg.jpg")
        self.background_sound = arcade.load_sound("music/Eggs.wav")
        self.win_sound = arcade.load_sound("music/Win.wav")
        self.lost_sound = arcade.load_sound("music/Lose.wav")
        self.player = None
        self.status_player = None
        self.setup()
        self.status = ""

    def setup(self):

        self.player = arcade.play_sound(self.background_sound, volume=0.5, looping=True)
        for i in range(EGGS_COUNT):
            easter_egg = EasterEgg()
            self.easter_eggs.append(easter_egg)
        for i in range(15):
            rotten_egg = RottenEgg()
            self.rotten_eggs.append(rotten_egg)

    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.easter_eggs.draw()
        self.rotten_eggs.draw()
        self.bunny.draw()
        arcade.draw_text("COLLECT 50 EASTER EGGS UNTIL TIME IS UP!", SCREEN_WIDTH / 6, SCREEN_HEIGHT - 30,
                         arcade.color.DARK_GREEN, 14)
        arcade.draw_text(f"SCORE: {self.score}", 30, 30, arcade.color.DARK_GREEN, 16)
        arcade.draw_text(f"TIME LEFT: {self.timer}", SCREEN_WIDTH - 170, 30, arcade.color.DARK_GREEN, 16)
        if self.status != "":
            arcade.draw_text(self.status, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2, arcade.color.DARK_GREEN, 40)

    def update(self, delta_time):
        if self.timer > 0:
            self.bunny.update()
            self.easter_eggs.update()
            self.rotten_eggs.update()
            easter_eggs_hit_list = arcade.check_for_collision_with_list(self.bunny, self.easter_eggs)
            if len(easter_eggs_hit_list) > 0:
                for easter_egg in easter_eggs_hit_list:
                    self.score += 1
                    easter_egg.reset()

            rotten_eggs_hit_list = arcade.check_for_collision_with_list(self.bunny, self.rotten_eggs)
            if len(rotten_eggs_hit_list) > 0:
                for rotten_egg in rotten_eggs_hit_list:
                    self.score -= 1
                    rotten_egg.reset()

            if time.time() - self.time >= 1:
                self.time = time.time()
                self.timer -= 1
        elif self.score >= EGGS_COUNT:
            self.status = "WINNER"
            arcade.stop_sound(self.player)
            if self.status_player is None:
                self.status_player = arcade.play_sound(self.win_sound)
        else:
            self.status = "LOSER"
            arcade.stop_sound(self.player)
            if self.status_player is None:
                self.status_player = arcade.play_sound(self.lost_sound)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.bunny.change_x = -BUNNY_SPEED
        if symbol == arcade.key.RIGHT:
            self.bunny.change_x = BUNNY_SPEED
        if symbol == arcade.key.UP:
            self.bunny.change_y = BUNNY_SPEED
        if symbol == arcade.key.DOWN:
            self.bunny.change_y = -BUNNY_SPEED

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.bunny.change_x = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.bunny.change_y = 0


class Bunny(arcade.Sprite):
    def __init__(self):
        super().__init__("images/bunny.png", 0.1)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x = self.center_x + self.change_x
        self.center_y = self.center_y + self.change_y
        if self.left < 0:
            self.left = 0

        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT

        if self.bottom < 0:
            self.bottom = 0


class EasterEgg(arcade.Sprite):
    def __init__(self):
        super().__init__(f"images/easter-egg ({random.randint(1, 7)}).png", 0.05)
        self.change_x = EGG_SPEED
        self.change_y = EGG_SPEED
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)

    def update(self):
        self.center_x = self.center_x + self.change_x
        self.center_y = self.center_y + self.change_y
        if self.left > SCREEN_WIDTH or self.bottom > SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.center_x = random.randint(-SCREEN_WIDTH, 0)
        self.center_y = random.randint(-SCREEN_HEIGHT, 0)


class RottenEgg(arcade.Sprite):
    def __init__(self):
        super().__init__("images/rotten-egg.png", 0.05)
        self.change_x = -EGG_SPEED
        self.change_y = -EGG_SPEED
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)

    def update(self):
        self.center_x = self.center_x + self.change_x
        self.center_y = self.center_y + self.change_y
        if self.right < 0 or self.top < 0:
            self.reset()

    def reset(self):
        self.center_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
        self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()


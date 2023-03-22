""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNOWMAN_SPEED = 3


class SnowMan:
    """
    Building Snowman
    The center for the snowman is the center of the top circle.
    Attributes:
        change-the speed of the snowman
    """

    def __init__(self):
        self.center_x = 100
        self.change_x = 0
        self.center_y = 350
        self.change_y = 0
        self.sound = arcade.load_sound("Sound.wav")

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 20, arcade.csscolor.GHOST_WHITE)
        arcade.draw_circle_filled(self.center_x, self.center_y-42, 30, arcade.csscolor.GHOST_WHITE)
        arcade.draw_circle_filled(self.center_x, self.center_y-100, 40, arcade.csscolor.GHOST_WHITE)
        arcade.draw_circle_filled(self.center_x - 8, self.center_y+5, 4, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(self.center_x + 8, self.center_y+5, 4, arcade.csscolor.BLACK)
        arcade.draw_triangle_filled(self.center_x, self.center_y, self.center_x + 30, self.center_y-5, self.center_x,
                                    self.center_y-10, arcade.csscolor.ORANGE)

    def update(self):
        """
        The logic for hitting the end of the screen on the right and on the left, up and down
        """
        self.center_x = self.center_x + self.change_x
        if self.center_x > SCREEN_WIDTH - 40 or self.center_x < 40:
            self.change_x = -self.change_x
            arcade.play_sound(self.sound)

        self.center_y = self.center_y + self.change_y
        if self.center_y > SCREEN_HEIGHT/2 + 130 or self.center_y < 140:
            self.change_y = -self.change_y
            arcade.play_sound(self.sound)  # playing "Boing" sound


class ChristmasTree:
    """
    Building Christmas Tree
    The center for the Christmas Tree is the center of the top triangle.
    """

    def __init__(self):
        self.center_x = 400
        self.center_y = 470

    def draw(self):
        # trunc of the tree
        arcade.draw_rectangle_filled(self.center_x, self.center_y-150, 20, 60, arcade.csscolor.SIENNA)

        # main triangle
        arcade.draw_triangle_filled(self.center_x, self.center_y, self.center_x-50, self.center_y-150, self.center_x+50,
                                    self.center_y-150, arcade.csscolor.DARK_GREEN)
        # top triangle "star"
        arcade.draw_triangle_filled(self.center_x, self.center_y+10, self.center_x-10, self.center_y, self.center_x+10,
                                    self.center_y, arcade.csscolor.RED)

        # Christmas Decoration for the tree
        # arcade.draw_circle_filled(390, 440, 5, arcade.csscolor.ORANGE)
        # arcade.draw_circle_filled(400, 420, 5, arcade.csscolor.PINK)
        # arcade.draw_circle_filled(420, 400, 5, arcade.csscolor.PURPLE)
        # arcade.draw_circle_filled(410, 385, 5, arcade.csscolor.BLUE)
        # arcade.draw_circle_filled(395, 365, 5, arcade.csscolor.ORANGE)
        # arcade.draw_circle_filled(378, 345, 5, arcade.csscolor.RED)
        # arcade.draw_circle_filled(358, 345, 5, arcade.csscolor.LIME)


class MyGame(arcade.Window):
    """
     Our Custom Window Class
     Attributes:
         clicker-logical variable that corresponds to clicking mouse with left button
    """

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.snowman = SnowMan()
        self.christmas_tree = ChristmasTree()
        self.clicker = False

    def on_draw(self):
        arcade.start_render()
        # Set the background color
        arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

        # Draw snow
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/2, 0, (227, 227, 227))

        # House
        arcade.draw_triangle_filled(140, 450, 300, 560, 460, 450, arcade.csscolor.BLACK)
        arcade.draw_polygon_filled([
            [150, 300],
            [150, 450],
            [300, 550],
            [450, 450],
            [450, 300]
        ], arcade.csscolor.SADDLE_BROWN)
        arcade.draw_rectangle_filled(220, 370, 80, 140, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(220, 370, 75, 135, arcade.csscolor.BROWN)
        arcade.draw_rectangle_filled(355, 380, 140, 110, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(355, 380, 135, 105, arcade.csscolor.DARK_GRAY)
        arcade.draw_rectangle_filled(355, 380, 125, 95, arcade.csscolor.BLACK)

        self.christmas_tree.draw()

        self.snowman.draw()

        # Draw a sun
        arcade.draw_circle_filled(100, 550, 40, arcade.color.YELLOW)

        # Rays to the left, right, up, and down
        arcade.draw_line(100, 550, 100, 600, arcade.color.YELLOW, 3)
        arcade.draw_line(100, 550, 0, 550, arcade.color.YELLOW, 3)
        arcade.draw_line(100, 550, 0, 450, arcade.color.YELLOW, 3)
        arcade.draw_line(100, 550, 0, 650, arcade.color.YELLOW, 3)

        # Diagonal rays
        arcade.draw_line(100, 550, 200, 450, arcade.color.YELLOW, 3)
        arcade.draw_line(100, 550, 100, 450, arcade.color.YELLOW, 3)
        arcade.draw_line(100, 550, 150, 600, arcade.color.YELLOW, 3)
        arcade.draw_line(100, 550, 200, 550, arcade.color.YELLOW, 3)

    def update(self, delta_time):
        self.snowman.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.snowman.change_x = -SNOWMAN_SPEED
        if symbol == arcade.key.RIGHT:
            self.snowman.change_x = SNOWMAN_SPEED
        if symbol == arcade.key.UP:
            self.snowman.change_y = SNOWMAN_SPEED
        if symbol == arcade.key.DOWN:
            self.snowman.change_y = -SNOWMAN_SPEED

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.snowman.change_x = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.snowman.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        if 180 < y < SCREEN_HEIGHT * 3/4 + 30 and 50 < x < SCREEN_WIDTH-50 and self.clicker:
            self.christmas_tree.center_x = x
            self.christmas_tree.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.clicker = not self.clicker


def main():
    window = MyGame()
    arcade.run()


main()

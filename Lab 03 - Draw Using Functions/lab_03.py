

# Import the "arcade" library
import arcade


def draw_house(x, y):
    # roof
    arcade.draw_triangle_filled(
        x-150-10, y,
        x, y+100+10,
        x+150+10, y, arcade.csscolor.BLACK)

    # house background
    arcade.draw_polygon_filled([
        [x-150, y-150],
        [x-150, y],
        [x, y+100],
        [x+150, y],
        [x+150, y-150]
    ], arcade.csscolor.SADDLE_BROWN)

    # door
    arcade.draw_rectangle_filled(x-80, y-80, 80, 140, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x-80, y-80, 75, 135, arcade.csscolor.BROWN)

    # window
    arcade.draw_rectangle_filled(x+55, y-70, 140, 110, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x+55, y-70, 135, 105, arcade.csscolor.DARK_GRAY)
    arcade.draw_rectangle_filled(x+55, y-70, 125, 95, arcade.csscolor.BLACK)


def draw_snowman(x,y,r):
    arcade.draw_circle_filled(x, y, r, arcade.csscolor.GHOST_WHITE)
    arcade.draw_circle_filled(x, y-2.3*r, r*1.5, arcade.csscolor.GHOST_WHITE)
    arcade.draw_circle_filled(x, y-5.4*r, 2*r, arcade.csscolor.GHOST_WHITE)
    arcade.draw_circle_filled(x-r*0.33, y+r*0.25, r/5, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x+r*0.33, y+r*0.25, r/5, arcade.csscolor.BLACK)
    arcade.draw_triangle_filled(x, y, x+1.5*r, y-0.25*r, x, y-0.5*r, arcade.csscolor.ORANGE)

def draw_christmas_tree(x,y,r):
    # Triangle is made of these three points:
    # (400, 470), (350, 320), (450, 320)
    arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(400, 470, 350, 320, 450, 320, arcade.csscolor.DARK_GREEN)
    arcade.draw_triangle_filled(400, 480, 390, 470, 410, 470, arcade.csscolor.RED)
    arcade.draw_circle_filled(390, 440, r, arcade.csscolor.ORANGE)
    arcade.draw_circle_filled(400, 420, r, arcade.csscolor.PINK)
    arcade.draw_circle_filled(420, 400, r, arcade.csscolor.PURPLE)
    arcade.draw_circle_filled(410, 385, r, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(395, 365, r, arcade.csscolor.ORANGE)
    arcade.draw_circle_filled(378, 345, r, arcade.csscolor.RED)
    arcade.draw_circle_filled(358, 345, r, arcade.csscolor.LIME)
# Open up a window.
arcade.open_window(600, 600, "My second picture")

# Set the background color
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

# Get ready to draw
arcade.start_render()

# sky
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, (227, 227, 227))

# House
draw_house(400, 450)
# (300, 450)

# Snowman
draw_snowman(100, 420, 30)


# Christmas tree, with a trunk and triangle for top
draw_christmas_tree()


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

# Draw text with a font size of 24 pts.
arcade.draw_text("Merry Christmas and Happy New Year!",
                 15, 150,
                 arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
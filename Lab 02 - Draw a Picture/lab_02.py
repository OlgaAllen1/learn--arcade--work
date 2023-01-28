

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "My first picture")

# Set the background color
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, (227, 227, 227))

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

# Snowman
arcade.draw_circle_filled(100, 350, 20, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(100, 308, 30, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(100, 250, 40, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(92, 355, 4, arcade.csscolor.BLACK)
arcade.draw_circle_filled(108, 355, 4, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(100, 350, 130, 345, 100, 340, arcade.csscolor.ORANGE)

# Christmas tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (400, 470), (350, 320), (450, 320)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 470, 350, 320, 450, 320, arcade.csscolor.DARK_GREEN)
arcade.draw_triangle_filled(400, 480, 390, 470, 410, 470, arcade.csscolor.RED)
arcade.draw_circle_filled(390, 440, 5, arcade.csscolor.ORANGE)
arcade.draw_circle_filled(400, 420, 5, arcade.csscolor.PINK)
arcade.draw_circle_filled(420, 400, 5, arcade.csscolor.PURPLE)
arcade.draw_circle_filled(410, 385, 5, arcade.csscolor.BLUE)
arcade.draw_circle_filled(395, 365, 5, arcade.csscolor.ORANGE)
arcade.draw_circle_filled(378, 345, 5, arcade.csscolor.RED)
arcade.draw_circle_filled(358, 345, 5, arcade.csscolor.LIME)

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

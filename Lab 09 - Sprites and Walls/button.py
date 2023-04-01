import arcade


class Button(arcade.Sprite):  # Class for Button
    def __init__(self, text, image, center_x, center_y):
        super().__init__(image)
        self.center_x = center_x
        self.center_y = center_y
        self.restart_text = arcade.Text(text, center_x - 60, center_y - 5, arcade.color.GHOST_WHITE, 15,
                                        font_name="kenvector future")

    def draw(self):
        super().draw()
        self.restart_text.draw()

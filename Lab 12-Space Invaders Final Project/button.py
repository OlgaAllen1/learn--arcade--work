import arcade


class Button(arcade.Sprite):
    def __init__(self, text, image, center_x, center_y, color=arcade.color.BLACK):
        super().__init__(image)
        self.center_x = center_x
        self.center_y = center_y
        self.text = arcade.Text(text, center_x - 60 + len(text), center_y - 5, color, 15,
                                        font_name="kenvector future")

    def draw(self):
        super().draw()
        self.text.draw()

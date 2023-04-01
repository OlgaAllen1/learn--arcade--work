import arcade


class AnimatedSprite(arcade.Sprite):
    """ Loop for Animation.
    Frame by Frame Animation."""
    i = 0  # i-number of the current texture
    time = 0

    def update_animation(self, delta_time):
        self.time += delta_time
        if self.time >= 0.1:  # To Slow down animation.
            self.time = 0
            if self.i == len(self.textures)-1:  # If we get to the end of the list of textures, return back to the 1st.
                self.i = 0
            else:
                self.i += 1
            self.set_texture(self.i)
            
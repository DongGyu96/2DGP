from pico2d import *

class Block:
    image = None
    effect_image = None
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        if self.type == 0:
            self.left = x - 85
            self.right = x + 85
            self.top = y + 30
            self.bottom = y - 30
            if self.image == None:
                self.image = load_image('block.png')
                self.effect_image = load_image('block_effect.png')
        elif self.type == 1:
            self.left = x - 160
            self.right = x + 160
            self.top = y + 30
            self.bottom = y - 30
            if self.image == None:
                self.image = load_image('block_type1.png')
                self.effect_image = load_image('block_type1_effect.png')

    def Draw(self):
        self.effect_image.draw(self.x, self.y + 10)
        self.effect_image.draw(self.x, self.y + 20)
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= 1.5
        self.bottom -= 1.5
        self.top -= 1.5
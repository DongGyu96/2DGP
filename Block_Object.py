from pico2d import *

class Block:
    image = None
    effect_image = None
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        if self.type == -1: # 블록의 끝
            self.left = -1
            self.right = -1
            self.top = -1
            self.bottom = -1
            if self.image == None:
                self.image = load_image('block_end.png')
                self.effect_image = load_image('block_end.png')
        elif self.type == 0: # 가로로 긴 작은 직사각형
            self.left = x - 85
            self.right = x + 85
            self.top = y + 30
            self.bottom = y - 30
            if self.image == None:
                self.image = load_image('block.png')
                self.effect_image = load_image('block_effect.png')
        elif self.type == 1: # 가로로 긴 직사각형
            self.left = x - 160
            self.right = x + 160
            self.top = y + 30
            self.bottom = y - 30
            if self.image == None:
                self.image = load_image('block_type1.png')
                self.effect_image = load_image('block_type1_effect.png')
        elif self.type == 2: # 세로로 긴 작은 사각형
            self.left = x - 30
            self.right = x + 30
            self.top = y + 85
            self.bottom = y - 85
            if self.image == None:
                self.image = load_image('block_type2.png')
                self.effect_image = load_image('block_type2_effect.png')
        elif self.type == 3: # 정사각형
            self.left = x - 70
            self.right = x + 70
            self.top = y + 70
            self.bottom = y - 70
            if self.image == None:
                self.image = load_image('block_type3.png')
                self.effect_image = load_image('block_type3_effect.png')
        elif self.type == 4: # 대형 직사각형
            self.left = x - 120
            self.right = x + 120
            self.top = y + 310
            self.bottom = y - 310
            if self.image == None:
                self.image = load_image('block_type4.png')
                self.effect_image = load_image('block_type4_effect.png')

    def Draw(self):
        self.effect_image.draw(self.x, self.y + 10)
        self.effect_image.draw(self.x, self.y + 20)
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= 4
        self.bottom -= 4
        self.top -= 4
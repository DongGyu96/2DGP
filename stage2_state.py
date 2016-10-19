import game_framework
import main_state
import math
from pico2d import *

class Ball:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.trace_x = [x] * 10
        self.trace_y = [y] * 10
        for n in range(0, 10):
            self.trace_y[n] = y - (n * 5)

    def update(self):
        for n in range(1, 10):
            self.trace_x[10 - n] = self.trace_x[9 - n]
            self.trace_y[10 - n] = self.trace_y[9 - n]
        self.trace_x[0] = self.x
        self.trace_y[0] = self.y
        self.count = 0



class Block:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        if self.type == 0:
            self.left = x - 85
            self.right = x + 85
            self.top = y + 30
            self.bottom = y - 30
        elif self.type == 1:
            self.left = x - 160
            self.right = x + 160
            self.top = y + 30
            self.bottom = y - 30

name = "Stage1State"
image = None
text_image = None
circle = None
blueball = None
redball = None
blueball_effect = None
redball_effect = None
pausebutton_image = None
block_image = None
move = False
reverse = True
RedBall = None
BlueBall = None
blocks = None
running = None
pausemenu_image = None
block_type1_image = None
block_type1_effect_image = None

def enter():
    global image
    global text_image
    global pausebutton_image
    global circle
    global blueball, blueball_effect
    global redball, redball_effect
    global running
    global block_image
    global block_effect_image
    global RedBall, BlueBall, blocks
    global pausemenu_image
    global block_type1_image, block_type1_effect_image
    pausemenu_image = load_image('pause_image.png')
    block_effect_image = load_image('block_effect.png')
    block_image = load_image('block.png')
    circle = load_image('circle.png')
    blueball = load_image('blueball.png')
    redball = load_image('redball.png')
    blueball_effect = load_image('blueball_effect.png')
    redball_effect = load_image('redball_effect.png')
    text_image = load_image('stage2.png')
    pausebutton_image = load_image('pausebutton.png')
    image = load_image('background.png')
    block_type1_image = load_image('block_type1.png')
    block_type1_effect_image = load_image('block_type1_effect.png')
    RedBall = Ball(390, 150, 0)
    BlueBall = Ball(110, 150, 180)
    blocks = [Block(120, 700, 1), Block(120, 980, 1), Block(120, 1260, 1), Block(120, 1540, 1), Block(350, 1820, 1), Block(120, 2100, 1)]
    running = True
    pass


def exit():
    global blocks
    global RedBall, BlueBall
    del(RedBall)
    del(BlueBall)
    for block in blocks:
        del(block)
    pass


def update():
    if running == True:
       for block in blocks:
           block.y -= 2
           block.bottom -= 2
           block.top -= 2

       if move == True:
           if reverse == True:
               BlueBall.angle -= 1.2
               RedBall.angle -= 1.2
           elif reverse == False:
               BlueBall.angle += 1.2
               RedBall.angle += 1.2

       BlueBall.x = 250 + (math.cos(BlueBall.angle * math.pi / 180.0) * 140)
       BlueBall.y = 150 + (math.sin(BlueBall.angle * math.pi / 180.0) * 140)
       RedBall.x = 250 + (math.cos(RedBall.angle * math.pi / 180.0) * 140)
       RedBall.y = 150 + (math.sin(RedBall.angle * math.pi / 180.0) * 140)

       BlueBall.update()
       RedBall.update()

       for block in blocks:
           if block.left < BlueBall.x < block.right and block.bottom < BlueBall.y < block.top:
               enter()
           elif block.left < RedBall.x < block.right and block.bottom < RedBall.y < block.top:
               enter()

    if blocks[len(blocks) - 1].y < -100:
        enter()
    pass


def draw():
    clear_canvas()
    image.draw(250,400)

    for n in range(0 , 10):
        blueball_effect.draw(BlueBall.trace_x[n], BlueBall.trace_y[n])
        redball_effect.draw(RedBall.trace_x[n], RedBall.trace_y[n])


    for block in blocks:
        if block.type == 0:
            block_effect_image.draw(block.x, block.y + 10)
            block_effect_image.draw(block.x, block.y + 20)
            block_image.draw(block.x, block.y)
        elif block.type == 1:
            block_type1_effect_image.draw(block.x, block.y + 10)
            block_type1_effect_image.draw(block.x, block.y + 20)
            block_type1_image.draw(block.x, block.y)

    text_image.draw(50,780)
    pausebutton_image.draw(470,770)
    circle.draw(250,150)
    blueball.draw(BlueBall.x, BlueBall.y)
    redball.draw(RedBall.x, RedBall.y)

    if running == False:
        pausemenu_image.draw(250,400)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    global running
    global move,reverse
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 450 < event.x < 490 and 750 < 800 - event.y < 790:
                if running == False:
                    resume()
                else:
                    pause()
            if 180 < event.x < 320 and 375 < 800 - event.y < 425:
                if running == False:
                    game_framework.change_state(main_state)
            if 210 < event.x < 290 and 320 < 800 - event.y < 360:
                if running == False:
                    resume()

        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_BACKSPACE:
                game_framework.pop_state()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
                move = True
                reverse = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
                move = True
                reverse = True
            elif event.type == SDL_KEYUP:
                move = False

    pass


def pause():
    global running
    running = False
    pass


def resume():
    global running
    running = True
    pass
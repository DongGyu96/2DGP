import game_framework
import main_state
import random
from pico2d import *
from Ball_Object import Ball
from Block_Object import Block

name = "Infinity_State"
image = None
text_image = None
circle = None
blueball = None
redball = None
blueball_effect = None
redball_effect = None
pausebutton_image = None
move = False
reverse = True
RedBall = None
BlueBall = None
blocks = None
sub_blocks = None
all_blocks = None
running = None
pausemenu_image = None
failmenu_image = None
blocks_type = None
sub_blocks_type = None
font = None
score = None
fail = None
Boost = None

def enter():
    global image
    global text_image
    global pausebutton_image, failmenu_image
    global circle
    global blueball, blueball_effect
    global redball, redball_effect
    global running, fail
    global RedBall, BlueBall, blocks, sub_blocks, all_blocks
    global pausemenu_image
    global blocks_type , sub_blocks_type
    global font
    global score
    global Boost
    pausemenu_image = load_image('pause_image.png')
    circle = load_image('circle.png')
    blueball = load_image('blueball.png')
    redball = load_image('redball.png')
    blueball_effect = load_image('blueball_effect.png')
    redball_effect = load_image('redball_effect.png')
    text_image = load_image('Infinity.png')
    pausebutton_image = load_image('pausebutton.png')
    image = load_image('background.png')
    failmenu_image = load_image('Fail_image.png')
    font = load_font('KOVERWATCH.TTF', 30)
    blocks_type = random.randint(0, 9)
    sub_blocks_type = random.randint(0, 3)
    RedBall = Ball(390, 150, 0)
    BlueBall = Ball(110, 150, 180)
    set_blocks()
    set_sub_blocks(0)
    score = 0
    running = True
    fail = False
    Boost = False
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
    global blocks_type, sub_blocks_type
    global score
    global all_blocks, running, fail
    if running == True:
       all_blocks = blocks + sub_blocks
       for block in all_blocks:
           block.update()
           if block.y < 0 and block.type != -1:
               score += 1
               block.type = -1
           if Boost == True:
               block.update()
               block.update()

       if move == True:
           if reverse == True:
               BlueBall.move(True)
               RedBall.move(True)
           elif reverse == False:
               BlueBall.move(False)
               RedBall.move(False)

       BlueBall.x = 250 + (math.cos(BlueBall.angle * math.pi / 180.0) * 140)
       BlueBall.y = 150 + (math.sin(BlueBall.angle * math.pi / 180.0) * 140)
       RedBall.x = 250 + (math.cos(RedBall.angle * math.pi / 180.0) * 140)
       RedBall.y = 150 + (math.sin(RedBall.angle * math.pi / 180.0) * 140)

       BlueBall.update()
       RedBall.update()


       for block in all_blocks:
           if Boost == False:
               if block.left < BlueBall.x < block.right and block.bottom < BlueBall.y < block.top:
                   running = False
                   fail = True
               elif block.left < RedBall.x < block.right and block.bottom < RedBall.y < block.top:
                   running = False
                   fail = True

    if blocks[len(blocks) - 1].y < 0:
        blocks_type = random.randint(0, 9)
        set_blocks()

    if sub_blocks[len(sub_blocks) - 1].y < 0:
        sub_blocks_type = random.randint(0, 3)
        set_sub_blocks(-1000)
    pass


def draw():
    clear_canvas()
    image.draw(250,400)

    for n in range(0 , 10):
        blueball_effect.draw(BlueBall.trace_x[n], BlueBall.trace_y[n])
        redball_effect.draw(RedBall.trace_x[n], RedBall.trace_y[n])

    all_blocks = blocks + sub_blocks
    for block in all_blocks:
        block.Draw()

    text_image.draw(50,780)
    pausebutton_image.draw(470,770)
    circle.draw(250,150)
    blueball.draw(BlueBall.x, BlueBall.y)
    redball.draw(RedBall.x, RedBall.y)

    font.draw(230, 775, '%4d' % (score), (128, 128, 255))

    if running == False:
        if fail == True:
            failmenu_image.draw(250, 400)
            font.draw(320, 470, '%4d' % (score), (255, 128, 0))
        else:
            pausemenu_image.draw(250, 400)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    global running
    global move,reverse
    global Boost
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
                    if fail == False:
                        resume()
                    else:
                        enter()

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
            elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
                if Boost == True:
                    Boost = False
                else:
                    Boost = True
            elif event.type == SDL_KEYUP and event.key == SDLK_a:
                if reverse == False:
                    move = False
            elif event.type == SDL_KEYUP and event.key == SDLK_d:
                if reverse == True:
                    move = False

    pass

def set_blocks():
    global blocks
    if blocks_type == 0:
        blocks = [Block(125, 1000, 1), Block(425, 1160, 2), Block(75, 1080, 2), Block(375, 1250, 1), Block(250, 1750, 4), Block(475, 2170, 2), Block(25, 2170, 2), Block(350, 2250, 1), Block(0, 2300, -1)]
    elif blocks_type == 1:
        blocks = [Block(150, 1000, 0), Block(400, 1200, 0), Block(260, 1450, 0), Block(100, 1700, 1), Block(200, 2000, 2), Block(400, 2300, 1), Block(0, 2300, -1), Block(0, 2300, -1), Block(0, 2300, -1)]
    elif blocks_type == 2:
        blocks = [Block(100, 1000, 1), Block(100, 1250, 1), Block(100, 1500, 1), Block(100, 1750, 1), Block(400, 2000, 1), Block(100, 2250, 0), Block(0, 2300, -1), Block(0, 2300, -1), Block(0, 2300, -1)]
    elif blocks_type == 3:
        blocks = [Block(150, 1000, 3), Block(330, 1250, 3), Block(30, 1400, 3), Block(270, 1600, 3), Block(460, 1850, 3), Block(100, 2000, 3), Block(375, 2200, 3), Block(0, 2300, -1), Block(0, 2300, -1)]
    elif blocks_type == 4:
        blocks = [Block(50, 1300, 4), Block(450, 1300, 4), Block(250, 1500, 2), Block(100, 1900, 1), Block(400, 2150, 1), Block(100, 2300, 0), Block(0, 2300, -1), Block(0, 2300, -1), Block(0, 2300, -1)]
    elif blocks_type == 5:
        blocks = [Block(100, 1100, 0), Block(180, 1200, 0), Block(450, 1300, 0), Block(380, 1550, 3), Block(70, 1320, 3), Block(150, 1750, 0), Block(400, 2000, 1), Block(100, 2250, 1), Block(0, 2300, -1)]
    elif blocks_type == 6:
        blocks = [Block(100, 1000, 0), Block(300, 1250, 2), Block(100, 1500, 1), Block(400, 1750, 1), Block(200, 2000, 3), Block(400, 2200, 3), Block(80, 2200, 2), Block(450, 1500, 3), Block(0, 2300, -1)]
    elif blocks_type == 7:
        blocks = [Block(250, 1300, 4), Block(80, 1800, 3), Block(130, 1850, 3), Block(180, 1900, 3), Block(400, 2100, 3), Block(350, 2150, 3), Block(300, 2200, 3), Block(20, 2100, 0), Block(0, 2300, -1)]
    elif blocks_type == 8:
        blocks = [Block(90, 1100, 2), Block(240, 1100, 2), Block(400, 1100, 2), Block(240, 1200, 2), Block(360, 1600, 1), Block(100, 1800, 0), Block(400, 2000, 0), Block(130, 2200, 1), Block(0, 2300, -1)]
    elif blocks_type == 9:
        blocks = [Block(125, 1000, 1), Block(250, 1250, 0), Block(125, 1500, 1), Block(425, 1700, 3), Block(75, 1850, 0), Block(375, 1950, 3), Block(400, 2100, 1), Block(125, 2270, 0), Block(0, 2300, -1)]

def set_sub_blocks(start_y):
    global sub_blocks
    if sub_blocks_type == 0:
        sub_blocks = [Block(250, start_y + 2650, 2), Block(250, start_y + 2800, 2), Block(250, start_y + 2950, 2), Block(0, start_y + 3300, -1), Block(0, start_y + 3300, -1)]
    elif sub_blocks_type == 1:
        sub_blocks = [Block(400, start_y + 2550, 0), Block(120, start_y + 2800, 0), Block(80, start_y + 2700, 0), Block(260, start_y + 3020, 0), Block(0, start_y + 3300, -1)]
    elif sub_blocks_type == 2:
        sub_blocks = [Block(260, start_y + 2550, 0), Block(260, start_y + 2800, 0), Block(350, start_y + 2870, 0), Block(50, start_y + 3050, 0), Block(0, start_y + 3300, -1)]
    elif sub_blocks_type == 3:
        sub_blocks = [Block(200, start_y + 2500, 0), Block(100, start_y + 2600, 0), Block(400, start_y + 2800, 1), Block(100, start_y + 3050, 1), Block(0, start_y + 3300, -1)]


def pause():
    global running
    running = False
    pass


def resume():
    global running
    running = True
    pass
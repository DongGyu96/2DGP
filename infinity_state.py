import game_framework
import main_state
import random
from pico2d import *
from Ball_Object import Ball
from Block_Object import Block
from BGM_Object import BGM

name = "Infinity_State"
image = None
text_image = None
circle = None
blueball = None
redball = None
blueball_effect = None
redball_effect = None
blueball_dead_image = None
redball_dead_image = None
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
redball_dead = None
blueball_dead = None
count = None
dead_animation_frame = None
bgm = None
speed = 1
time = 0

def enter():
    global image
    global text_image
    global pausebutton_image, failmenu_image
    global circle
    global blueball, blueball_effect, blueball_dead_image
    global redball, redball_effect, redball_dead_image
    global running, fail
    global RedBall, BlueBall, blocks, sub_blocks, all_blocks
    global pausemenu_image
    global blocks_type , sub_blocks_type
    global font
    global score
    global Boost
    global blueball_dead, redball_dead, dead_animation_frame, count, bgm
    global time, speed
    pausemenu_image = load_image('Resource/pause_image.png')
    circle = load_image('Resource/circle.png')
    blueball = load_image('Resource/blueball.png')
    redball = load_image('Resource/redball.png')
    blueball_effect = load_image('Resource/blueball_effect.png')
    redball_effect = load_image('Resource/redball_effect.png')
    text_image = load_image('Resource/Infinity.png')
    pausebutton_image = load_image('Resource/pausebutton.png')
    image = load_image('Resource/stage_background.png')
    failmenu_image = load_image('Resource/Fail_image.png')
    blueball_dead_image = load_image('Resource/blueball_dead_animation.png')
    redball_dead_image = load_image('Resource/redball_dead_animation.png')
    font = load_font('Font/KOVERWATCH.TTF', 30)
    blocks_type = random.randint(0, 9)
    sub_blocks_type = random.randint(0, 3)
    RedBall = Ball(390, 150, 0)
    BlueBall = Ball(110, 150, 180)
    set_blocks()
    set_sub_blocks(0)
    score = 0
    count = 0
    dead_animation_frame = 0
    running = True
    fail = False
    Boost = False
    redball_dead = False
    blueball_dead = False
    bgm = BGM(9)
    time = 0
    speed = 1


def exit():
    global blocks
    global RedBall, BlueBall, bgm
    del(RedBall)
    del(BlueBall)
    del(bgm)
    for block in blocks:
        del(block)
    pass


def update(frame_time):
    global blocks_type, sub_blocks_type, blueball_dead, redball_dead, dead_animation_frame
    global score
    global all_blocks, running, fail, count
    global speed
    global time
    if running:
       all_blocks = blocks + sub_blocks
       for block in all_blocks:
           block.update(frame_time * speed)
           if block.y < 0 and block.type != -1:
               score += 1
               block.type = -1

       if move:
           if reverse:
               BlueBall.move(True, frame_time * speed)
               RedBall.move(True, frame_time * speed)
           elif not reverse:
               BlueBall.move(False, frame_time * speed)
               RedBall.move(False, frame_time * speed)

       BlueBall.update(frame_time * speed)
       RedBall.update(frame_time * speed)


       for block in all_blocks:
           if block.left < BlueBall.x < block.right and block.bottom < BlueBall.y < block.top:
               running = False
               blueball_dead = True
           elif block.left < RedBall.x < block.right and block.bottom < RedBall.y < block.top:
               running = False
               redball_dead = True
       time += frame_time
       if time > 25:
           speed += 0.1
           time -= 25

    if blocks[len(blocks) - 1].y < 0:
        blocks_type = random.randint(0, 9)
        set_blocks()

    if sub_blocks[len(sub_blocks) - 1].y < 0:
        sub_blocks_type = random.randint(0, 3)
        set_sub_blocks(-1000)

    if not running:
        count += 1
        if count == 6:
            if blueball_dead or redball_dead:
                dead_animation_frame += 1
                count = 0
                if dead_animation_frame == 10:
                    fail = True

def draw(frame__time):
    clear_canvas()
    image.draw(250,400)

    for n in range(0 , 10):
        if not blueball_dead:
            blueball_effect.draw(BlueBall.trace_x[n], BlueBall.trace_y[n])
        if not redball_dead:
            redball_effect.draw(RedBall.trace_x[n], RedBall.trace_y[n])

    all_blocks = blocks + sub_blocks
    for block in all_blocks:
        block.Draw()

    text_image.draw(50,780)
    pausebutton_image.draw(470,770)
    circle.draw(250,150)
    if not blueball_dead:
        blueball.draw(BlueBall.x, BlueBall.y)
    if not redball_dead:
        redball.draw(RedBall.x, RedBall.y)

    font.draw(230, 775, '%4d' % (score), (128, 128, 255))

    if not running:
        if fail:
            failmenu_image.draw(250, 400)
            font.draw(320, 470, '%4d' % (score), (255, 128, 0))
        elif blueball_dead:
            blueball_dead_image.clip_draw(dead_animation_frame * 106, 0, 106, 106, BlueBall.x, BlueBall.y)
        elif redball_dead:
            redball_dead_image.clip_draw(dead_animation_frame * 106, 0, 106, 106, RedBall.x, RedBall.y)
        else:
            pausemenu_image.draw(250, 400)
    update_canvas()
    pass


def handle_events(frame_time):
    events = get_events()
    global running
    global move,reverse
    global Boost
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if 450 < event.x < 490 and 750 < 800 - event.y < 790:
                if not running:
                    resume()
                else:
                    pause()
            if 180 < event.x < 320 and 375 < 800 - event.y < 425:
                if not running:
                    game_framework.change_state(main_state)
            if 210 < event.x < 290 and 320 < 800 - event.y < 360:
                if not running:
                    if not fail:
                        resume()
                    else:
                        enter()

        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_BACKSPACE:
                game_framework.change_state(main_state)
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
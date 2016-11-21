import game_framework
import main_state
import math
import stage8_state
from pico2d import *
from Ball_Object import Ball
from Block_Object import Block

name = "Stage7_State"
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
running = None
pausemenu_image = None

def enter():
    global image
    global text_image
    global pausebutton_image
    global circle
    global blueball, blueball_effect
    global redball, redball_effect
    global running
    global RedBall, BlueBall, blocks
    global pausemenu_image
    pausemenu_image = load_image('pause_image.png')
    circle = load_image('circle.png')
    blueball = load_image('blueball.png')
    redball = load_image('redball.png')
    blueball_effect = load_image('blueball_effect.png')
    redball_effect = load_image('redball_effect.png')
    text_image = load_image('stage7.png')
    pausebutton_image = load_image('pausebutton.png')
    image = load_image('stage_background.png')
    RedBall = Ball(390, 150, 0)
    BlueBall = Ball(110, 150, 180)
    blocks = [Block(100, 1100, 0), Block(300, 1350, 2), Block(100, 1600, 1), Block(400, 1850, 1), Block(200, 2100, 3), Block(400, 2300, 3), Block(50, 2600, 1), Block(100, 2850, 1), Block(100, 3100, 1), Block(350, 3400, 3), Block(100, 3600, 1), Block(250, 3900, 3)]
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

       for block in blocks:
           if block.left < BlueBall.x < block.right and block.bottom < BlueBall.y < block.top:
               enter()
           elif block.left < RedBall.x < block.right and block.bottom < RedBall.y < block.top:
               enter()

    if blocks[len(blocks) - 1].y < -300:
        game_framework.push_state(stage8_state)
    pass


def draw():
    clear_canvas()
    image.draw(250,400)

    for n in range(0 , 10):
        blueball_effect.draw(BlueBall.trace_x[n], BlueBall.trace_y[n])
        redball_effect.draw(RedBall.trace_x[n], RedBall.trace_y[n])


    for block in blocks:
        block.Draw()

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
            elif event.type == SDL_KEYDOWN and event.key == SDLK_m:
                game_framework.push_state(stage8_state)
            elif event.type == SDL_KEYUP and event.key == SDLK_a:
                if reverse == False:
                    move = False
            elif event.type == SDL_KEYUP and event.key == SDLK_d:
                if reverse == True:
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
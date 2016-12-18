import game_framework
import main_state
from pico2d import *


name = "StartState"
image = None
background_image = None
logo_time = 0.0


def enter():
    global image
    global background_image
    image = load_image('Resource/kpu_credit.png')
    background_image = load_image('Resource/white_background.png')
    pass


def exit():
    global image
    del(image)
    pass


def update(frame_time):
    global logo_time
    if(logo_time > 1.2):
        logo_time = 0
        game_framework.change_state(main_state)
    delay(0.01)
    logo_time += 0.01
    pass


def draw(frame_time):
    global image
    clear_canvas()
    background_image.draw(250,400)
    image.draw(250,400)
    update_canvas()
    pass




def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass





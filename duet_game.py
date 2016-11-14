import game_framework
import start_state
from pico2d import *

open_canvas(500,800, sync = True)
game_framework.run(start_state)
close_canvas()
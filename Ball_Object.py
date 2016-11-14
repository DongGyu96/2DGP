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

    def move(self, reverse):
        if reverse == True:
            self.angle -= 3.6
        elif reverse == False:
            self.angle += 3.6
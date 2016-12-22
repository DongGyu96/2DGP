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

    def update(self, frame_time):
        self.x = 250 + (math.cos(self.angle * math.pi / 180.0) * 140)
        self.y = 150 + (math.sin(self.angle * math.pi / 180.0) * 140)
        for n in range(1, 10):
            self.trace_x[10 - n] = self.trace_x[9 - n]
            self.trace_y[10 - n] = self.trace_y[9 - n]
            self.trace_y[10-n] -= frame_time * 200
        self.trace_x[0] = self.x
        self.trace_y[0] = self.y
        self.count = 0

    def move(self, reverse, frame_time):
        if reverse:
            self.angle -= frame_time * 180
        elif not reverse:
            self.angle += frame_time * 180
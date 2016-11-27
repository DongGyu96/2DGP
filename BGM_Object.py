from pico2d import *

class BGM:
    TITLE, STAGE1, STAGE2, STAGE3, STAGE4, STAGE5, STAGE6, STAGE7, STAGE8, INFINITY = 0,1,2,3,4,5,6,7,8,9
    def __init__(self, stage):
        if stage == BGM.TITLE:
            self.bgm = load_music('Virtual Riot - Energy Drink.mp3')
        elif stage == BGM.INFINITY:
            self.bgm = load_music('TheFatRat+-+Windfall.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
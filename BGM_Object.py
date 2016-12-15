from pico2d import *
import random

class BGM:
    TITLE, STAGE1, STAGE2, STAGE3, STAGE4, STAGE5, STAGE6, STAGE7, STAGE8, INFINITY = 0,1,2,3,4,5,6,7,8,9
    def __init__(self, stage):
        if stage == BGM.TITLE:
            self.bgm = load_music('Sound/Virtual Riot - Energy Drink.mp3')
        elif stage == BGM.INFINITY:
            sound = random.randint(0, 3)
            if sound == 0:
                self.bgm = load_music('Sound/TheFatRat+-+Windfall.mp3')
            elif sound == 1:
                self.bgm = load_music('Sound/DJVI+-+Back+On+Track.mp3')
            elif sound == 2:
                self.bgm = load_music('Sound/OMFG - Hello.mp3')
            elif sound == 3:
                self.bgm = load_music('Sound/Bossfight+-+Milky+Ways.mp3')
        else:
            self.bgm = load_music('Sound/500476_Stereo-Madness.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
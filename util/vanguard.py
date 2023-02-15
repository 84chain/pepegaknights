from util.imports import *
from util.operator import Operator


class Vanguard(Operator):
    def __init__(self, name, potential, dp, init_sp, total_sp, skill_duration, redeploy, dp_refund_mod=0.5):
        super().__init__(name, potential, dp, init_sp, total_sp, skill_duration, redeploy, dp_refund_mod)
        self.delay = 0
        self.instant = False
        self.skill_dp = 0

    def set_skill(self, dp, instant, delay):
        self.skill_dp = dp
        self.instant = instant
        self.delay = delay

    def update(self, frame):
        if math.floor((frame - self.skill_start_frame) / 60) == self.skill_duration:
            self.using_skill = False
            self.skill_start_frame = -1
            self.sp = 0
        else:
            if (frame - self.deployed_frame) % 60 == 0 and frame != self.deployed_frame:
                self.sp += 1
        if self.using_skill:
            if self.instant:
                if frame == self.skill_start_frame + self.delay:
                    return self.skill_dp
            else:
                return math.floor(
                    self.skill_dp * math.floor((frame - self.skill_start_frame) / 60) / self.skill_duration)
        else:
            return None


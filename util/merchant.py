from util.imports import *
from util.operator import Operator

class Merchant(Operator):
    def __init__(self, name, potential, dp, init_sp, total_sp, skill_duration, redeploy, dp_refund_mod=0.5):
        super().__init__(name, potential, dp, init_sp, total_sp, skill_duration, redeploy, dp_refund_mod)
        self.module = False

    def set_module(self, module):
        self.module = module

    def update(self, frame):
        if math.floor((frame - self.skill_start_frame) / 60) == self.skill_duration:
            self.using_skill = False
            self.skill_start_frame = -1
            self.sp = 0
        else:
            if (frame - self.deployed_frame) % 60 == 0 and frame != self.deployed_frame:
                self.sp += 1
        return math.floor(math.floor((frame - self.deployed_frame) / 60) / 3 * -2 if self.module else -3)
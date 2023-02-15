from util.imports import *


class Operator:
    def __init__(self, name, potential, dp, init_sp, total_sp, skill_duration, redeploy, dp_refund_mod=0.5):
        self.name = name
        self.potential = potential
        self.dp = dp
        self.init_sp = init_sp
        self.sp = init_sp
        self.total_sp = total_sp
        self.skill_duration = skill_duration
        self.using_skill = False
        self.skill_start_frame = -1
        self.redeploy = redeploy
        self.dp_refund_mod = dp_refund_mod
        self.sp_regen_mod = 1

        self.deployed_frame = -1  # frame number >= 0, -1 for not deployed
        self.retreated_frame = -1  # frame number >= 0, -1 for deployed

    def set_sp_regen_mod(self, sp_regen_mod):
        self.sp_regen_mod = sp_regen_mod

    def set_init_sp_mod(self, init_sp_mod):
        self.init_sp += init_sp_mod
        self.sp = self.init_sp

    def deploy(self, frame):
        if self.retreated_frame > 0:
            return 0
        self.deployed_frame = frame
        self.retreated_frame = -1
        self.sp = self.init_sp
        return -self.dp

    def retreat(self, frame):
        if self.deployed_frame > 0:
            return 0
        self.retreated_frame = frame
        self.deployed_frame = -1
        refund = self.dp * self.dp_refund_mod
        self.dp = math.floor(self.dp * 1.5)
        return refund

    def activate_skill(self, frame):
        if self.deployed_frame < 0:
            return False
        if self.using_skill:
            return False
        if self.sp >= self.total_sp:
            self.using_skill = True
            self.skill_start_frame = frame
            self.sp = 0
            return True

    def update(self, frame):
        if math.floor((frame - self.skill_start_frame) / 60) == self.skill_duration:
            self.using_skill = False
            self.skill_start_frame = -1
            self.sp = 0
        else:
            if (frame - self.deployed_frame) % 60 == 0 and frame != self.deployed_frame:
                self.sp += 1
        return None

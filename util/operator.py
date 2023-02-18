from imports import *


class Operator:
    def __init__(self, name, op_class, dp, potential, redeploy, module=False):
        self.name = name
        self.op_class = op_class
        self.potential = potential
        self.dp = dp - 1 if 1 < self.potential < 6 else 2 if self.name not in welfare_operators else 3

        self.redeploy = redeploy
        self.deployed = False
        self.deployed_frame = 0
        self.redeploy_time = 0

        self.init_sp = 0
        self.total_sp = 0
        self.current_sp = 0
        self.sp_gain = 1

        self.skill_type = None
        self.skill_active = False

        self.skill_duration = 0
        self.skill_duration_left = 0
        self.skill_dp_generation = 0

        self.module = module

    def set_modifiers(self, factors):
        self.sp_gain = factors["sp"]
        self.dp *= factors["dp_cost"][self.op_class]
        self.redeploy *= factors["redeploy"][self.op_class]

    def set_skill(self, init_sp, total_sp, skill_duration, skill_type, skill_dp_generation=0):
        self.skill_type = skill_type
        self.init_sp = init_sp
        self.total_sp = total_sp
        self.skill_duration = skill_duration
        self.skill_dp_generation = skill_dp_generation

    def deploy(self, frame):
        self.deployed = True
        self.deployed_frame = frame
        self.current_sp = self.init_sp
        self.redeploy_time = 0

    def retreat(self):
        self.deployed = False
        self.redeploy_time = self.redeploy
        self.current_sp = 0

    def activate_skill(self):
        if self.skill_type != "auto":
            return
        if self.skill_active:
            raise NoSPException
        else:
            self.skill_active = True
            self.current_sp = 0
            self.skill_duration_left = self.skill_duration

    def update(self, frame):
        if self.deployed:
            if self.skill_active:
                if self.skill_duration_left > 0:
                    self.skill_duration_left -= 1
                else:
                    self.skill_duration_left = 0
                    self.skill_active = False
            else:
                self.current_sp = min(self.total_sp, self.current_sp + self.sp_gain)
        else:
            if self.redeploy_time > 0:
                self.redeploy_time -= 1
        return 0  # dp gain, to be overridden by vg and merchant

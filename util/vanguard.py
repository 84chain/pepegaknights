from imports import *

from operator import Operator


class Vanguard(Operator):
    def update(self, frame):
        if self.deployed:
            if self.skill_active:
                if self.skill_duration_left > 0:
                    if math.floor(self.skill_duration_left / self.skill_duration * 60) - math.floor(
                            (self.skill_duration_left - 1) / self.skill_duration * 60):
                        return 1
                    self.skill_duration_left -= 1
                else:
                    self.skill_duration_left = 0
                    self.skill_active = False
            else:
                self.current_sp = min(self.total_sp, self.current_sp + 1)
        else:
            if self.redeploy_time > 0:
                self.redeploy_time -= 1
        return 0

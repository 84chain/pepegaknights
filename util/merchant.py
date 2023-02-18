from operator import Operator


class Merchant(Operator):
    def update(self, frame):
        if self.deployed:
            if self.skill_active:
                if self.skill_duration_left > 0:
                    self.skill_duration_left -= 1
                else:
                    self.skill_duration_left = 0
                    self.skill_active = False
            else:
                self.current_sp = min(self.total_sp, self.current_sp + 1)
        else:
            if self.redeploy_time > 0:
                self.redeploy_time -= 1
        if (frame - self.deployed_frame) * 60 // 3 == 0:
            return -2 if self.module else -3

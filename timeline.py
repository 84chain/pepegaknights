from util.imports import *
from util.vanguard import Vanguard


class TimelineError(Exception):
    def __init__(self, message):
        print(message)

class Timeline:
    def __init__(self, starting_dp, operators, dp_regen_mod, sp_regen_mod):
        self.starting_dp = starting_dp
        self.dp = starting_dp  # only dp from natural sources such as regen, deploy, retreat
        self.operators = operators
        self.dp_regen_mod = dp_regen_mod
        self.sp_regen_mod = sp_regen_mod

        self.timeline = []

        [i.set_sp_regen_mod(self.sp_regen_mod) for i in self.operators]

        try:
            bagpipe = [i for i in self.operators if i.name == "Bagpipe"][0]
            [i.set_init_sp_mod(8 if bagpipe.potential >= 5 else 6) for i in self.operators if type(i) == Vanguard]
        except:
            pass
        try:
            eyja = [i for i in self.operators if i.name == "Eyjafjalla"][0]
            eyja.set_init_sp_mod(round(random.randint(5, 12) if eyja.potential >= 3 else random.randint(9, 15)))
        except:
            pass

    def init_timeline(self, timeline):
        # timeline is list of ops by name then deploy/retreat/skill in dict format
        # e.g. {"name": "Bagpipe", "action": "deploy", "frame": 0}

        self.timeline = timeline

    def perform_action(self, action, frame):
        for i in self.operators:
            if i.name == action["name"] and action["frame"] == frame:
                if action["action"] == "deploy":
                    if self.dp >= i.dp:
                        self.dp += i.deploy(frame)
                    else:
                        raise TimelineError("Cannot deploy")
                elif action["action"] == "retreat":
                    self.dp += i.retreat(frame)
                elif action["action"] == "skill":
                    if not i.activate_skill(frame):
                        raise TimelineError("Not enough sp")

    def run(self):
        if not self.timeline:
            print("Empty timeline")
            return
        last_frame = sorted(self.timeline, key=lambda x: x["frame"])[-1]["frame"]
        for frame in range(last_frame + 1):
            if frame % round(60 / self.dp_regen_mod) == 0:
                self.dp += 1
            try:
                for action in self.timeline:
                    self.perform_action(action, frame)
            except TimelineError:
                print("Timeline does not work with your team")
            for operator in self.operators:
                operator.update(frame)
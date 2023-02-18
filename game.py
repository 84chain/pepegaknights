from util.imports import *


class Game:
    def __init__(self, operators, starting_dp, factors=default_map_factors):
        self.operators = operators
        self.starting_dp = starting_dp
        self.current_dp = starting_dp
        self.factors = factors
        self.timeline = None
        self.last_frame = 0
        self.frame = 0

    def init_timeline(self, timeline):
        self.timeline = timeline

    def perform_action(self, action):
        operator = [i for i in self.operators if i.name == action["name"]][0]
        if action["action"] == "deploy":
            operator.deploy(action["frame"])
        elif action["action"] == "retreat":
            operator.retreat()
        elif action["action"] == "skill":
            operator.activate_skill()

    def update(self):
        while self.frame <= self.last_frame:
            if self.timeline.has_action(self.frame):
                for action in self.timeline.get_action(self.frame):
                    try:
                        self.perform_action(action)
                    except NoSPException:
                        pass
                    except NoDPException:
                        pass
                    except NoOperatorException:
                        pass
            self.current_dp += self.factors["dp"]
            for i in self.operators:
                self.current_dp += i.update(self.frame)
            self.frame += 1

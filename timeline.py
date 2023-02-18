class Timeline:
    # timeline is [{"frame": int, "name": str, "action": enum("deploy", "retreat", "skill")}]
    def __init__(self, timeline):
        self.timeline = timeline

    def has_action(self, frame):
        return bool(len([i for i in self.timeline if i["frame"] == frame]))

    def get_action(self, frame):
        return [i for i in self.timeline if i["frame"] == frame]

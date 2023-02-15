from util.imports import *
from util.operator import Operator
from util.vanguard import Vanguard
from util.merchant import Merchant
from util.common_operators import *
from timeline import Timeline, TimelineError

team = [bagpipe]
starting_dp = 10
dp_regen_mod = 1
sp_regen_mod = 1

timeline = [
    {
        "name": "Bagpipe",
        "action": "deploy",
        "frame": 3 * 60
    },
    {
        "name": "Bagpipe",
        "action": "skill",
        "frame": 7 * 60 + 1
    }
]

# if __name__ == "main":
tl = Timeline(
    starting_dp=starting_dp,
    operators=team,
    dp_regen_mod=dp_regen_mod,
    sp_regen_mod=sp_regen_mod
)
tl.init_timeline(timeline)
tl.run()
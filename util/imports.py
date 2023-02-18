import math

welfare_operators = []

default_map_factors = {
    "dp": 1,
    "sp": 1,
    "redeploy": {
        "Vanguard": 1,
        "Guard": 1,
        "Defender": 1,
        "Sniper": 1,
        "Caster": 1,
        "Medic": 1,
        "Supporter": 1,
        "Specialist": 1
    },
    "dp_cost": {
        "Vanguard": 1,
        "Guard": 1,
        "Defender": 1,
        "Sniper": 1,
        "Caster": 1,
        "Medic": 1,
        "Supporter": 1,
        "Specialist": 1
    }
}


class NoSPException(Exception):
    pass


class NoDPException(Exception):
    pass


class NoOperatorException(Exception):
    pass

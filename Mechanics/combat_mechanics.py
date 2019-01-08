from Map_Gen.ParseMap import WorldMap
from Mechanics import core_mechanics, ui_mechanics
from random import randint

CONST_CHANCE = 37


def combat_init(player):
    pass


# Checking for encounters
def check_for_encounter(player):
    if randint(0, 100) <= 37:
        # Choose random enemy
        combat_init(player)



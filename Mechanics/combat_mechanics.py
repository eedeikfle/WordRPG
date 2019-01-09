from script import Character
from random import randint
from Mechanics.ui_mechanics import clear, pause
CONST_CHANCE = 37


def combat_init(player, mob, pos):
    # TODO: put this in script\screen.py
    clear()
    print(pos)
    print("\nA wild {} has appeared!!\n".format(mob))
    print(
        "(1) Fight\n"
        "(2) Run Away"
    )
    choice = input()
    if choice == "1":
        pass
    else:
        # Try and run away
        pause()


# Checking for encounters
def check_for_encounter(player, pos):
    if randint(0, 100) <= 37:
        # Choose random enemy
        combat_init(player, Character.random_mob(pos), pos)


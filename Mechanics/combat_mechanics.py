from script import Character
from random import randint
from Mechanics.ui_mechanics import clear, pause
CONST_CHANCE = 37


def combat_init(player, mob, pos):
    # TODO: put this in script\screen.py
    clear()
    print(pos)
    print("\nA wild {} has appeared!!\n".format(mob.name))
    print(
        "(1) Fight\n"
        "(2) Run Away"

    )
    choice = input()
    if choice == "1":
        fight(player, mob)
    else:
        # Try and run away
        pause()


# Checking for encounters
def check_for_encounter(player, pos):
    if randint(0, 100) <= 37:
        # Choose random enemy
        combat_init(player, Character.random_mob(pos), pos)


def fight(player, mob):
    # TODO: add into script\screen.py
    print("{}:".format(mob.name))
    print(
        "CLASS: {} ".format(mob.mob_class),
        "HP: {}".format(mob.health),
        "STAMINA: {}".format(mob.stamina),
        "ATTACK: {}".format(mob.attack),
        "DEFENCE: {}".format(mob.defense)
    )

    print("\n{}:".format(player.name))
    print(
        "CLASS: {} ".format(player._class),
        "HP: {}".format(player.health),
        "STAMINA: {}".format(player.stamina),
        "ATTACK: {}".format(player.attack),
        "DEFENCE: {}".format(player.defense)
    )

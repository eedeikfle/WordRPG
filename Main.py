# Starting Data November 6, 2018
# Made By Cowboy8625
# Waste Land
__author__ = 'Cowboy8625', 'Cyy', 'BJTMastermind', 'HexTree', 'Byteme8bit', 'Giioke', 'ThePinkChicken', 'Djsurry'

# Import Modules
import sys
import time

from Mechanics.core_mechanics import *
from Mechanics.ui_mechanics import *
from script import Screen, Story
import ChangeLog


# Main() is the first function
# Gets input from player to either Start Load Help or Exit
def main():

    choice = None             # Initializes variable

    while choice != '1':            # Continues loop while choice is not to start the game - will change later
        Screen.main_menu_screen()
        choice = input('\n\nSELECT A NUMBER:> ')

        if choice == '1':           # Starts Game
            main_game_loop(char_creation(), opening=True)

        elif choice == '2':  # LOADED AND SAVE
            print('NOT AN OPTION YET')
            time.sleep(2)

        elif choice == '3':  # Help
            print('NOT AN OPTION YET')
            time.sleep(2)

        elif choice == '4':
            ChangeLog.change_log_print()
            pause()

        elif choice == '5':
            sys.exit()

        else:
            print("Not an Option.")
            pause()


# main_game_loop() is where all the logic for the player to move about the map
# or any other event while not in a fight
def main_game_loop(player, opening=True):
    if opening:
        Story.intro_story(player)
        input("Press Enter to continue: ")
        opening = False

    while True:
        clear()
        directions = {
            "1": "North",
            "2": "South",
            "3": "East",
            "4": "West"
        }
        choice = input(
            "Which way do you want to travel?\n"
            f"Coords: {player.pos_x}:{player.pos_y}\n\n"
            "(1): North\n"
            "(2): South\n"
            "(3): East\n"
            "(4): West\n"
            "(5): Inspect Area\n"
            "(6): Inventory\n"
            "(7): Look For Resources\n"
            "Input a Number:>  ")
        if choice in ['1', '2', '3', '4']:
            player.move(directions[choice])
        elif choice == "5":
            player.inspect_area()
        elif choice == "6":
            inventory_mode(player)
        elif choice == "7":
            pass
        elif choice == 'Quit':  # QUIT, I'll take this out after testing
            sys.exit()
        else:
            print(f'Invalid choice {choice}')
            pause()

if __name__ == "__main__":
    main()

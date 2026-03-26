"""GAME_COMMANDS = {
    "start game": start_game,
    "pcl": print_commands_list, 
    "end game": end_game, 
    "pbc": print_building_costs,
    "pod": print_own_deck, 
    "inf": display_info, 
    "cr": print_credits,
    "roll": roll_die,
    "ru": print_game_rules
    }"""

PRE_COMMANDS = {
    "ru": "print_game_rules", 
    "cr": "print_credits", 
    "inf": "display_info",
    "ppc": "print_pre_commands"
    }

GAME_COMMANDS = {}

def set_up_game():

    initial_list = {}

    while True:
        try:
            player_number = int(input().strip()) 
            if player_number in [3, 4]:
                break

        except ValueError:
            print("enter an integer between 1 and 4 please.")

    initial_list["player_number"] = player_number

    return initial_list

        


def main_game_loop():

    



    pass

def main():
    game = False
    while not game:
        action = input().strip().lower()
        if not action in PRE_COMMANDS and action in GAME_COMMANDS:
            print("That command's game specific! meuehhrhehre try againnnn")
        elif action == 'start game':
            game = True
        else:
            try:
                PRE_COMMANDS[action]
            except KeyError:
                print("That command doesn't seem to be available. Do you want to check commands with 'ppc'?")

    variables_to_unpack = set_up_game()
    




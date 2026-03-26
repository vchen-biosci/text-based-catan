from os import system
import random

def assign_player_named_dicts(initial_dict : dict):

    player_number = initial_dict["player_number"]

    for i in player_number:
        "first insert different dictionaries into the dictionary"
        initial_dict[str(i + 1)] = {}

    for i in player_number:
        "then I'll iterate through the players and put their names into their respective dictionaries, putting name in the key called name"
        player_name = input("What do you want to be called?").strip()
        initial_dict[str(i + 1)]["name"] = player_name 

    return initial_dict

def assign_player_colours(initial_dict : dict):

    player_number = initial_dict["player_number"]

    for i in player_number:
        """write this code after studying ANSII codes and how they work. I think I can pass stuff in as a string later, and i hope python processes it like this."""
        initial_dict[str(i + 1)]["colour"] = "whatever ansii code they want lowk though i should ask them if theyre sure or not about codes that fall within a certain range. I also need to check if they're valid."

def get_player_number():
    while True:
        try:
            player_number = int(input().strip()) 
            if player_number in [3, 4]:
                break
            else: 
                print("You can only play with 3 or 4 people, sorry!")

        except ValueError:
            print("enter an integer between 1 and 4 please.")

    return player_number

def assign_resource_cards(initial_dict : dict):
    
    
    for i in initial_dict["player_number"]:
        initial_dict[str(i + 1)]["resource_cards"] = {}

def edit_game_bank(instructions : dict, game_bank : dict, initial_dict : dict, game_info : dict):
    
    
    "give them resource card dictionaries."

    if game_info["game_state"] == "setup":
        print("Setting up your resource cards...")
        for resource in game_info["resources"]:
            game_bank[resource] = 19
        print("Setting up your development cards...")
        """then set up development cards lol"""

    return game_bank

    #we add different categories. ok, we can do this by making a big list of stuff to add first.

def print_commands_list(game_info):

    print("Here are the commands available to you during the game:\n")
    for key in GAME_COMMANDS:
        print(key)

    print("And here are the commands available to you before the game starts:\n")
    for key in PRE_COMMANDS:
        print(key)

def print_building_costs(game_info):

    #dude im setting this up later. i cant be bothered.
    print("""HEre are your building costs my friend:""")

def display_info(game_info):
    print("Here's yo info but im lazy rn")

def print_credits(game_info):
    print("Once again my love, im lazy")

def print_own_deck(game_info, initial_dict):
    
    print("Here are your resource cards:")
    for key in initial_dict[game_info["turn"]]["resource_cards"]:
        print(key, initial_dict[game_info["turn"]]["resource_cards"][key])
    print("And here are your development cards.")
    for key in initial_dict[game_info["turn"]]["dev_cards"]:
        print(key, initial_dict[game_info["turn"]]["dev_cards"][key])
    print(f"And here are your victory points: {initial_dict[game_info["turn"]]["victory_points"]}")

def roll_die():
    "i swear this is actually written yukw ill transfer it rn"

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    roll = dice_1 + dice_2
    print(f"The die have spoken!! |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}! You have rolled a {roll} :3")

    return roll

def print_game_rules(game_info : dict):
    print(game_info["rules"])


def set_up_game(game_info : dict):

    initial_dict = {}
    game_bank = {}

    initial_dict["player_number"] = get_player_number()
    initial_dict = assign_player_named_dicts(initial_dict)
    initial_dict = assign_player_colours(initial_dict)
    initial_dict = assign_resource_cards(initial_dict)
    
    game_bank = edit_game_bank(game_bank, initial_dict, game_info)
    game_bank = edit_game_bank(game_bank, initial_dict, game_info)
    ##im not sure if i want to use a class for all the game information or a list. i think ill use a list. thatll make it easier
    ## i forgot what i need the list for?????????????????????????????????????????????????????
    ##okay yeah i need a dictionary of all game information
    ##do i?????
    ##ok yeah that seems like a nice idea, right?
    ##so in main, I'll make the game run and then pass in that dictionary so that we can always tell whats happening
    ##eg after setup we change the variable to game_state = normal or something like that
    ## and then setup game can parse the curent game state as normal so that we just make normal changes
    ##ok so using dictionaries is a PRETTYYYY nice idea... what should i include in it?
    ##it can be like.... oh man idk

    return initial_dict, game_bank


def main_game_loop():





    pass

GAME_COMMANDS = {
    "pcl": print_commands_list, 
    "pbc": print_building_costs,
    "pod": print_own_deck, 
    "inf": display_info, 
    "cr": print_credits,
    "roll": roll_die,
    "ru": print_game_rules
    }

PRE_COMMANDS = {
    "ru": print_game_rules, 
    "cr": print_credits, 
    "inf": display_info,
    "pcl": print_commands_list
    }

def main():

    game_info = {}
    game_info["resources"] = ["ores", "grain", "wood", "brick", "sheep"]
    game_info["dev_cards"] = ["knight", "progress", "vps"]

    game_info["game_state"] = "off"
    while game_info["game_state"] == "off":
        action = input().strip().lower()
        if not action in PRE_COMMANDS and action in GAME_COMMANDS:
            print("That command's game specific! meuehhrhehre try againnnn")
        elif action == 'start game':
            game_info["game_state"] == "setup"
        else:
            try:
                PRE_COMMANDS[action](game_info)
            except KeyError:
                print("That command doesn't seem to be available. Do you want to check commands with 'ppc'?")

    initial_dict, game_bank = set_up_game(game_info)


if __name__== "__main__":
    main()

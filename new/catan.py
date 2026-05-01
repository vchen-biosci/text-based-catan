import random, time, os

#game["player_number"]
#quick_key

def get_player_number() -> int:
        player_number = 0
        while not player_number in [3, 4]:
                try:
                        player_number = int(input("How many people are playing?\n> ").strip()) 
                        if not player_number in [3, 4]:
                                print("You can only play with 3 or 4 people.")
                except ValueError:
                        print("Enter an integer (3 or 4) please.")
                        
        return player_number

def create_player_key(player_number : int) -> list:
        quick_key = []
        for player in range(player_number):
                quick_key.append(player + 1)
                
        return quick_key

def get_player_name(player, player_names) -> str:
        valid_name = False
        while not valid_name:
                player_name = input(f"Player {player}, enter the name you'd like to be known by.\n> ").strip()
                if player_name in player_names:
                        print("... That name's already owned. Choose something else.")
                elif player_name.isdigit():
                        print("Sorry, you're not allowed a name consisting of only numbers, as this will cause problems later.")
                else:
                        valid_name = True
                        
        return player_name

def create_player_dicts(quick_key : list) -> dict:
        player_dictionaries = {}
        for player in quick_key:
                player_dictionaries[player] = {}
                
        return player_dictionaries

def get_player_password() -> str:
        valid_password = False
        while not valid_password:
                password = input("Please enter a password; it'll be used to check for your consent later. Keep it short but memorable, and make sure it's not a password you use for important sites.\n> ")
                if len(password) > 7:
                        print("That password is way too long. Keep it to 7 or below characters.")
                else:
                        valid_password = True
        
        return password

def setup_player_dicts(quick_key : list):
        player_names = []
        player_dictionaries = create_player_dicts(quick_key)
        for player in quick_key:
                name = get_player_name(player, player_names)
                player_names.append(name)
                player_dictionaries[player]['name'] = name
                player_dictionaries[player]['password'] = get_player_password()
                clear_screen()
        
        return player_dictionaries
        
        
def setup_player_dicts(game : dict, CONSTS : dict):

        player_number = get_player_number()
        clear_screen()
        quick_key = create_player_key(player_number)
        player_names = []
        

                valid_password = False
                while not valid_password:
                        password = input("Please enter a password; it'll be used to check for your consent later. Keep it short but memorable, and make sure it's not a password you use for important sites.\n> ")
                        if len(password) > 7:
                                print("That password is way too long. Keep it to 7 or below characters.")
                        else:
                                valid_password = True
                game[player]['password'] = password
                
                clear_screen()
        
        game["player_names"] = player_names

        return game


def setup_game(game : dict, CONSTS : dict):

        print("Notice: While setting up the game, you temporarily can't use other commands.")

        game = setup_player_dicts(game, CONSTS)

        print("Okay; your names are: ")
        for player in range(game['player_number']):
                if player == game['quick_key'][-2]:
                        print(game['player_names'][player], end=".\n")
                elif player == game['quick_key'][-3]:
                        print(game['player_names'][player], end=", and ")
                else:
                        print(game['player_names'][player], end=", ")
                        
        game = assign_player_colours(game, CONSTS)

        print("Initialising player cards...")
        for player in quick_key:

                game[player]["resources"] = {}
                for resource in CONSTS["resources"]:
                        game[player]["resources"][resource] = 0
                        
                game[player]["dev_cards"] = {}
                quick_dev_dict = dict(zip(CONSTS['dev_cards'], CONSTS["dev_card_numbers"]))
                for dev_card in quick_dev_dict:
                        game[player]["dev_cards"][dev_card] = quick_dev_dict[dev_card]

                game[player]['roads'] = []
                game[player]['settlements'] = []
                game[player]['cities'] = []
                game[player]['construct_bank'] = {"settlements": 5, "cities": 4, "roads": 15}
                game[player]['achievements'] = {"longest road" : 0, "largest army" : 0}
                game[player]['knights_recruited'] = 0
                game[player]['VPs'] = 0

        print("Setting up the resource bank...")
        game["resource_bank"] = {}
        for resource in CONSTS["resources"]:
                game["resource_bank"][resource] = 19
        game["dev_cards"] = {}
        for dev_card in quick_dev_dict:
                game["dev_cards"][dev_card] = quick_dev_dict[dev_card]

        print("Generating your grid...")
        game = generate_grid(game, CONSTS)
        clear_screen()

        return game

def start_game(game : dict, CONSTS : dict):
        print("Starting your game...")
        time.sleep(1)
        clear_screen()
        game = setup_game(game, CONSTS)
        game = game_stage_1(game, CONSTS)
        print("Great. Your initial setup is complete, so you now have access to the full range of commands. Happy playing.")
        game = main_game(game, CONSTS)
        print("The game's over. You're getting sent back to the main starting programme now.")

def clear_screen():
        print("\033c", end="")

def rules(CONSTS):
        print(CONSTS["rules"])

def main():
        CONSTS = {

                "rules": """This is the link to the official Catan Almanac:
https://www.catan.com/sites/default/files/2024-01/Almanac%20CATAN-3D.pdf
If the link doesn't work, please paste it into your browser.""",

                "resources": ["ores", "grain", "wood", "brick", "sheep"],

                "dev_cards": ["knight", "year of plenty", "road building", "monopoly", "VPs"],  

                "dev_card_numbers": [14, 2, 2, 2, 5],

                "ports": ["wood", "grain", "cow", "ore", "brick"],
                "welcome_message": """WELCOME TO MY TEXT-BASED CATAN.
Before we start, make sure \x1b[38;2;142;194;21mthis text\x1b[0m is green!
CREDITS: Vivienne, CATAN game studio. To start the game, type 'start', or type 'rng' to gamble!
ENTER YOUR COMMAND TO BEGIN""",

                "pre_commands" : {
                        "rng": infinite_rng
},

                "commands" : { 
                        "deck": print_own_deck, 
                        "roll": roll_die,
},

                "credits": """The credits for this code are as follows:""",

                "commands info" : """These are the commands available to you and what they mean""",

                "colors" : ["red", "green", "blue"],

                "biomes" : [],

                "number_tokens" : [],

                "road_types" : ["__", "/", "\\"],

                "road_strings" : ["ABCDEF$GHIJKMNOPRSTUVWYZabdefghiklmnpqrstuvwxyz+", 
                        "ADCG$LRXMSHNEIJPQWVbcihnoutyx+rwmsflagOUTZYedjkq",
                        "BEFJDHIOGMLRSYNTXdekjpqvwzsxntiobhWcKQPVUaZfgmlr"],

                "kaomojis" : {
                        "ores": "‧₊˚🗻`",
                        "brick": "↟↟↟↟↟↟",
                        "grain": "˚ʚ🌱₊˚",
                        "wood": " ݁˖𓂃.𖠰.",
                        "sheep": ":3 ^^~", 
                        "desert": " ⛰︎ ོ ༄-"
},
                "settlement_locations" : [],

                "ports" : ["wood", "grain", "sheep", "ore", "brick"],

                "starting_constructs" : {'settlements' : 5, 'cities' : 4, 'paths' : 15},

                "building costs" : """---BUILDING COSTS---
 Road: Wood (1), Brick (1)
 Settlement: Wood (1), Brick (1), Grain (1), Sheep (1)
 City: Ores (3), Grain (2)
 Development cards: Ores (1), Grain (1), Sheep (1)""",
 
                "guide": """To play Catan, you should look at the 'rules' to check how it's generally played . 
In terms of this game's grid, some things are done differently. 
The grid is made with ASCII art. Instead of stating the biome names on each hex, the resources obtained from each are stated in their place.
Each hex is labeled with 'S1', 'S2', and so on and so forth. You do NOT place your settlements on the hexes. You place them on their verteces.
For instance, on the S1 hex, you can place your settlements on A, B, E, I, H, and D.
As for placing down roads, you name the two settlements that, by placing a road, you will connect. EG, you could place a road on KQ; between K and Q.
You must have a settlement linked to the road that you're trying to build in order to place it, or it will be invalid.
                """,
                
                "S1": ["A", "B", "E", "I", "H", "D"],
                "S2": ["C", "D", "H", "N", "M", "G"],
                "S3": ["E", "F", "J", "P", "O", "I"],
                "S4": ["$", "G", "M", "S", "R", "L"],
                "S5": ["H", "I", "O", "U", "T", "N"],
                "S6": ["J", "K", "Q", "W", "V", "P"],
                "S7": ["M", "N", "T", "Z", "Y", "S"],
                "S8": ["O", "P", "V", "b", "a", "U"],
                "S9": ["R", "S", "Y", "e", "d", "X"],
                "S10": ["T", "U", "a", "g", "f", "Z"],
                "S11": ["V", "W", "c", "i", "h", "b"],
                "S12": ["Y", "Z", "f", "l", "k", "e"],
                "S13": ["a", "b", "h", "n", "m", "g"],
                "S14": ["d", "e", "k", "q", "p", "j"],
                "S15": ["f", "g", "m", "s", "r", "l"],
                "S16": ["h", "i", "o", "u", "t", "n"],
                "S17": ["k", "l", "r", "w", "v", "q"],
                "S18": ["m", "n", "t", "y", "x", "s"],
                "S19": ["r", "s", "x", "+", "z", "w"]

        }

        for i in range(10):
                if (i + 2) != 7:
                        for x in range(2):
                                CONSTS["number_tokens"].append(i + 2)
        CONSTS["number_tokens"].append(1)
        CONSTS["number_tokens"].append(12)

        CONSTS["settlement_locations"] = "abcdefghijklmnopqrstuvwxyz".upper()
        CONSTS["settlement_locations"] += CONSTS["settlement_locations"].lower() + "+" + "$"

        for i in range(3):
                CONSTS["biomes"].append("ores")
                CONSTS["biomes"].append("brick")

        for i in range(4):
                CONSTS["biomes"].append("grain")
                CONSTS["biomes"].append("wood")
                CONSTS["biomes"].append("sheep")

        game = {
                "input type" : CONSTS["pre_commands"],
                "on" : True
        }

        print(CONSTS["welcome_message"])

        while True:
                action = input("> ").strip().lower()

                if action == "ru":
                        print(CONSTS["rules"])
                elif action == "cr":
                        print(CONSTS["credits"])
                elif action == "pcl":
                        print(CONSTS["commands info"])
                elif action == "pbc":
                        print(CONSTS["building costs"])
                elif action == 'start':
                        start_game(game, CONSTS)
                elif action == 'end':
                        break
                elif action == 'guide':
                        print(CONSTS['guide'])
                        
                else:
                        try:
                                CONSTS["pre_commands"][action](game, CONSTS)
                        except KeyError:
                                print("That command doesn't seem to exist. Do you want to check commands with 'pcl'?")

if __name__ == "__main__":
        main()

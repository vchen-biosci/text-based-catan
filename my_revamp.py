from os import system
import random, os

def setup_player_names(initial_dict : dict):

        player_number = initial_dict["player_number"]

        for i in range(player_number):
                "first insert different dictionaries into the dictionary"
                initial_dict[str(i + 1)] = {}

        for i in range(player_number):
                "then I'll iterate through the players and put their names into their respective dictionaries, putting name in the key called name"
                player_name = input(f"What do you want to be called?, player {i + 1}?\n> ").strip()
                initial_dict[str(i + 1)]["name"] = player_name 

        return initial_dict

def ansi_stitching(color : list, text):
        
        colored_ver = ""
        colored_ver += "\x1b[38;2;"

        reps = 0
        for value in color:
                colored_ver += str(value)
                reps += 1

                if reps != 3:
                        colored_ver += ";"
        
        colored_ver += "m"
        colored_ver += text
        colored_ver += "\x1b[0m"

        return colored_ver

def assign_player_colours(initial_dict : dict):

        player_number = initial_dict["player_number"]

        table = """"""

        for i in range(player_number):
                colors = ["red", "green", "blue"]

                for player in range(player_number):
                        player_colour = []
                        big_loop = True
                        while big_loop:
                                for color in colors:

                                        

                                        action = input(f"Player {player + 1}, what value would you like to use for {color}? " + 
                                                        "Type 'table' to see available colour tables.\n> ").strip().lower()
                                        
                                        if action == "table":
                                                print(table)

                                        else:
                                                loop = True
                                                while loop:

                                                        try:
                                                                if int(action) <= 255:
                                                                        player_colour.append(int(action))
                                                                        loop = False

                                                                        
                                                                else:
                                                                        print("Sorry; RGB values only go up to 255.")
                                                                        action = input(f"Player {player + 1}, what value would you like to use for {color}? " + 
                                                        "Type 'table' to see available colour tables.\n> ").strip().lower()

                                                        except ValueError:

                                                                if action == "table":
                                                                        print(table)
                                                                else:
                                                                        print("Please input a valid integer, in arabic numerals, within the range of 0 to 255.")
                                                                
                                                                action = input(f"Player {player + 1}, what value would you like to use for {color}? " + 
                                                        "Type 'table' to see available colour tables.\n> ").strip().lower()

                                confirm_loop = True
                                while confirm_loop:

                                        confirm = input(ansi_stitching(player_colour, """This is what your colour looks like - are you sure you want it? Type 'Y' for yes and 'N' for no. 
Please make sure all other players are able to read this!\n> """)).strip()
                                        
                                        
                                        if confirm == "N":
                                                colors = []
                                                confirm_loop = False
                                        
                                        elif confirm == "Y":
                                                confirm_loop = False
                                                big_loop = False
                                                
                                        else:
                                                print("Please type either 'Y' or 'N'. This is case sensitive.")

                                                        
                                
                
        return initial_dict

def get_player_number():
        while True:
                try:
                        player_number = int(input("How many people are playing? :)\n> ").strip()) 
                        if player_number in [3, 4]:
                                break
                        else: 
                                print("You can only play with 3 or 4 people, sorry!")

                except ValueError:
                        print("Enter an integer 3 or 4 please.")

        return player_number

def assign_resource_cards(initial_dict):
        
        for i in range(initial_dict["player_number"]):
                initial_dict[str(i + 1)]["resource_cards"] = {}

        return initial_dict

def edit_game_bank(game_bank : dict, initial_dict : dict, game_info : dict):
        
        
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
                print(key, end=" ")

        print("\n")

        print("And here are the commands available to you before the game starts:\n")
        for key in PRE_COMMANDS:
                print(key, end=", ")

        print("\n")

def print_building_costs(game_info):

        #dude im setting this up later. i cant be bothered.
        print("""HEre are your building costs my friend:""")

def display_info(game_info):
        print("Here's yo info but im lazy rn")

def print_credits(game_info):
        print("Once again my love, im lazy")

def print_own_deck(game_info : dict, initial_dict : dict):
        
        print("Here are your resource cards:")
        for key in initial_dict[game_info["turn"]]["resource_cards"]:
                print(key, initial_dict[game_info["turn"]]["resource_cards"][key])
        print("And here are your development cards.")
        for key in initial_dict[game_info["turn"]]["dev_cards"]:
                print(key, initial_dict[game_info["turn"]]["dev_cards"][key])
        print(f"And here are your victory points: {initial_dict[game_info['turn']]['victory_points']}")

def roll_die(game_info : dict):
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
        initial_dict = setup_player_names(initial_dict)
        initial_dict = assign_player_colours(initial_dict)
        initial_dict = assign_resource_cards(initial_dict)
        
        game_bank = edit_game_bank(game_bank, initial_dict, game_info)

        return initial_dict, game_bank

def welcome_player():
        print("WELCOME TO MY TEXT-BASED CATAN!")
        print("Hi! Before we start, make sure \x1b[38;2;142;194;21mthis text\x1b[0m is green!")
        print("""CREDITS: Vivienne, CATAN game studio""")
        print("ENTER YOUR COMMAND TO BEGIN :)")

def setup_terrain(game_info):
        print("Rendering your grid...")
        tiles = {}
        for i in range(19):
                tiles[("S"+str(i+1))] = {}

        biomes = []
        for i in range(3):
                biomes.append("ores")
                biomes.append("brick")
        for i in range(4):
                biomes.append("grain")
                biomes.append("wood")
                biomes.append("sheep")


        number_tokens = []
        for i in range(10):
                if (i + 2) != 7:
                        for x in range(2):
                                number_tokens.append(i + 2)
        number_tokens.append(1)
        number_tokens.append(12)

        desert_placement = random.randint(1, 19)
        tiles[("S"+str(desert_placement))]["biome"] = "desert"
        tiles[("S"+str(desert_placement))]["number"] = 7

        for i in range(18):

                try:
                        x = tiles[("S"+str(i+1))]["biome"] != "desert"
                                
                except KeyError:
                        random.shuffle(biomes)
                        chosen_biome = biomes.pop()
                        tiles[("S"+str(i+1))]["biome"] = chosen_biome

                        random.shuffle(number_tokens)
                        chosen_number = number_tokens.pop()
                        tiles[("S"+str(i+1))]["number"] = chosen_number
        
        return tiles

def setup_locs(game_info):

        possible_locs = "abcdefghijklmnopqrstuvwxyz".upper()
        possible_locs = possible_locs + possible_locs.lower()
        possible_locs = possible_locs + "+"
        settlement_locs = {}

        for letter in possible_locs:
                settlement_locs[letter] = {"display": letter}
                settlement_locs[letter]["port"] = ""


        for loc in "ABFJouxy":
                settlement_locs[loc]["port"] = {"3:1 port"}
        i = 0
        ports = ["wood", "grain", "cow", "ore", "brick"]
        reps = 0
        for loc in "RQCGWcvwjp":
                reps += 1
                thing_to_put = f"2:1 {ports[i]} port"
                settlement_locs[loc]["port"] = thing_to_put
                if reps%2 == 0:
                        i += 1
        
        return settlement_locs

def main_game_loop():





        pass

def infinite_rng(game_info : dict):
        
        possible_stat_commands = ["cache", "mode", "mean", "num", "?", "reset", "indie"]
        print("Ohohoho, it seems you wish to play infinite rng, hm?")
        print("Type 'r' to roll, type 'esc' to escape! Oh, and 'stats' if you're into that sort of thing.")
        roll_cache = []
        cache_dice_1 = []
        cache_dice_2 = []

        rng_loop = True
        while rng_loop:

                action = input("> ").strip().lower()

                if not action in ["stats", "esc"]:
                        if action == "r":
                                dice_1 = random.randint(1, 6)
                                dice_2 = random.randint(1, 6)
                                roll = dice_1 + dice_2
                                roll_cache.append(roll)
                                cache_dice_1.append(dice_1)
                                cache_dice_2.append(dice_2)
                                print(f"The die have spoken!! |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}! You have rolled a {roll}!!")
                        else:
                                print("Uh oh. You're a silly bunny, aren't you? Either type 'r' or 'esc'! Oh, and 'stats' if you wanna see some cool stats. ykwim.")

                elif action == "stats":

                        loop = True
                        print("What stat do you want to see? (Hint: type '?' if you want to see the commands available for stats, or 'leave stats' to escape!)")

                        if len(roll_cache) == 0:
                                print("Warning: your cache is empty right now, so there aren't any stats for you to see. But you can proceed if you want.")

                        while loop:
                                action = input("> ").strip().lower()
                                if action in possible_stat_commands:
                                        if action == "cache":
                                                print(roll_cache)

                                        elif action == "mode":

                                                if len(roll_cache) != 0:

                                                        most_rolled = 0
                                                        contenders_list = []

                                                        for number in roll_cache:
                                                                if roll_cache.count(number) > roll_cache.count(most_rolled):
                                                                        most_rolled = number
                                                                        contenders_list = []

                                                                elif roll_cache.count(number) == roll_cache.count(most_rolled):
                                                                        if number == most_rolled:
                                                                                "idk"
                                                                        else:
                                                                                contenders_list.append(number)

                                                        if contenders_list == []:
                                                                print(f"Your mode was {most_rolled}, and you rolled it a whopping {roll_cache.count(number)} times!!")
                                                        else:
                                                                print(f"Well, you don't really have ONE singular mode. You have an entire {len(contenders_list)} contenders for the throne! They are: {str(set(contenders_list))} and {most_rolled}, rolled {roll_cache.count(most_rolled)} times each!")

                                                else:
                                                        print("Your cache is empty! Roll some more to get started!")

                                        elif action == "mean":

                                                if len(roll_cache) != 0:
                                                        print(f"The mean of all your rolls is {sum(roll_cache) / len(roll_cache)}")
                                                else:
                                                        print("Your roll cache is empty. Get grinding!")
                                        
                                        elif action == "num":

                                                print(f"You've rolled {len(roll_cache)} times this gambling session.")

                                        elif action == "reset":

                                                print("Ok, tough decision!")
                                                print("Erasing your cache... IRREVERSIBLE BTW")
                                                roll_cache = []
                                                cache_dice_1 = []
                                                cache_dice_2 = []
                                        
                                        elif action == "?":

                                                print("""You currently find yourself in a totally developed and advanced gambling history analysis, capable of:
> showcasing your ENTIRE roll history (in this session)! ('cache')
> showing your most rolled number ('mode')
> showing your mean roll ('mean')
> showing you the number of rolls you've done in this session ('num')
> answering your greatest ?s ('?', you're here right now)
> allowing you to escape your dark past of terrible rolls ('reset')
> letting you break free, omg ('leave stats')
> showing your single die stats ('indie')
> letting you end rng??? ('esc')\n""")
                                                
                                        elif action == "indie":

                                                stats = {}
                                                i = 1
                                                for cache in [cache_dice_1, cache_dice_2]:
                                                        mode = 0
                                                        highest_roll = 0
                                                        contenders_cachelist = []
                                                        for number in cache:
                                                                if cache.count(number) > cache.count(mode):
                                                                        mode = number
                                                                        contenders_cachelist = []
                                                                elif cache.count(number) == cache.count(mode):
                                                                        contenders_cachelist.append(number)

                                                                if number >= highest_roll:
                                                                        highest_roll = number
                                                        
                                                        mean = sum(cache) / len(cache)
                                                        contenders_cachelist.append(mode)


                                                        
                                                        print(f"For dice number {i}, your highest roll was {highest_roll}, your mean was {mean}, and your mode was something like {set(contenders_cachelist)}, rolled a whopping {cache.count(contenders_cachelist[0])} times {('each' * (0 if len(contenders_cachelist) == 0 else 1))} !")
                                                        i += 1
                                                        ##might end up making some sort of function and passing in parameters to run each thing. I'd use an 'if' to sort through bad commands eg calc_stats(action) if action == whole elif action == dice_1 elif action == dice_2 else printstupid idkkk i do want to do this
                                                        


                                elif action == "leave stats":
                                        print("Okay! Bye!")
                                        loop = False
                                
                                elif action == "esc":
                                        rng_loop = False

                                else:
                                        print("Stick to the commands!! Type '?' if you're lost. The input loop's not even case sensitive. BEHAVE!")


                else:
                        print("YOU'RE BEING TELEPORTED OUT OF THE MATRIX. RETURNING TO THE MAINFRAME...")
                        print("(Erasing all your gambling records...)")
                        rng_loop = False

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
        "pcl": print_commands_list,
        "rng": infinite_rng
        }

def main():

        welcome_player()

        game_info = {}
        game_info["rules"] = """Um idk."""
        game_info["resources"] = ["ores", "grain", "wood", "brick", "sheep"]
        game_info["dev_cards"] = ["knight", "progress", "vps"]

        game_info["game_state"] = "off"
        while game_info["game_state"] == "off":
                action = input("> ").strip().lower()
                if not action in PRE_COMMANDS and action in GAME_COMMANDS:
                        print("That command's game specific! meuehhrhehre try againnnn")
                elif action == 'start game':
                        print("\nStarting your game...\n")
                        game_info["game_state"] = "setup"
                else:
                        try:
                                PRE_COMMANDS[action](game_info)
                        except KeyError:
                                print("That command doesn't seem to be available. Do you want to check commands with 'pcl'?")

        initial_dict, game_bank = set_up_game(game_info)
        print("Shuffling your terrains...")
        tiles = setup_terrain(game_info)
        print("Adding your settlement spots...")
        settlement_locs = setup_locs(game_info)
        print("Making your actual grid...")


if __name__== "__main__":
        main()

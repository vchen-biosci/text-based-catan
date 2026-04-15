import random, os, time

def infinite_rng(game, CONSTS):
        
        
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

def setup_player_dicts(game, CONSTS):

        game = game

        while True:
                try:
                        player_number = int(input("How many people are playing? :)\n> ").strip()) 
                        if player_number in [3, 4]:
                                break
                        else: 
                                print("You can only play with 3 or 4 people, sorry!")

                except ValueError:
                        print("Enter an integer 3 or 4 please.")
                        
        game["player_number"] = player_number
        quick_key = []
        for player in range(player_number):
                quick_key.append(player + 1)
        game["quick_key"] = quick_key

        player_names = []
        for i in range(player_number):
                game[i + 1] = {}
                valid_name = False
                while not valid_name:

                        player_name = input(f"What do you want to be called?, player {i + 1}?\n> ").strip()
                        if player_name not in player_names:
                                
                                break

                        else:
                                print("Stop stealing another player's name!! Weirdo!!")

                player_names.append(player_name)
                game[i + 1]["name"] = player_name 
        
        game["player_names"] = player_names


        return game

def print_own_deck(game, CONSTS):
        print("this is ur deck")

def roll_die(game, CONSTS):


        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll = dice_1 + dice_2
        print(f"The die have spoken!! |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}! You have rolled a {roll} :3")

        return roll

def setup_game(game, CONSTS):
        print("Notice: While setting up the game, you temporarily can't use other commands.")
        time.sleep(0.5)

        game = setup_player_dicts(game, CONSTS)

        print("Okay; your names are: ")
        for player in range(game['player_number']):
                print(game['player_names'][player], end="")
                if player != 3:
                        print(", ", end="")
                else:
                        print(".\n")
        time.sleep(0.5)

        game = assign_player_colours(game, CONSTS)

        print("Initialising player cards...")
        for player in game["quick_key"]:
                for resource in CONSTS["resources"]:
                        game[player][resource] = 0
                for dev_card in CONSTS["dev_cards"]:
                        game[player]["dev_cards"] = 0
        time.sleep(0.3)

        print("Setting up the resource bank...")
        for resource in CONSTS["resources"]:
                game[resource] = 19
        for dev_card in CONSTS["dev_cards"]:
                pass
        time.sleep(0.3)

        




        return game

def ansi_stitching(color : list, text : str):
        
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

def choose_colours(CONSTS):

        player_color = []

        satisfied = False
        while not satisfied:
                for color in CONSTS["colors"]:                  
                        
                        valid_input = False
                        while not valid_input:
                                action = input(f"What value would you like to use for {color}?\n> ").strip().lower()

                                try:
                                        if int(action) <= 255:
                                                player_color.append(int(action))
                                                valid_input = True

                                                
                                        else:
                                                print("Sorry; RGB values only go up to 255.")
                                        

                                except ValueError:

                                        print("Please input a valid integer, in arabic numerals, within the range of 0 to 255.")     
                                        
                confirmed = False
                while not confirmed:

                        confirm = input(ansi_stitching(player_color, """This is what your colour looks like - are you sure you want it? Type 'Y' for yes and 'N' for no. 
Please make sure all other players are able to read this!\n""") + "> ").strip()
                        
                        if confirm == "N":
                                player_color = []
                                confirmed = True
                        
                        elif confirm == "Y":
                                satisfied = True
                                confirmed = True
                                
                        else:
                                print("Please type either 'Y' or 'N'. This is case sensitive.")

        return player_color

def assign_player_colours(game, CONSTS):


        preset_colors = [[0, 201, 184], [252, 210, 0], [252, 84, 0], [210, 0, 252]]

        manual = ""
        while manual not in ["y", "m"]:

                manual = input("Would you like to use our pre-selected, super aesthetic colours or customise your own? Please be responsible!!" +
                        " Type 'Y' for yes and 'M' to manually select.\n> ").lower().strip()
                
        if manual == "m":

                for player in range(game["player_number"]):
                        print(f"OKAY! PLAYER {player + 1}, YOU'RE UP!!!")
                        game[player + 1]["color"] = choose_colours(CONSTS)

        else:
                
                for player in range(game["player_number"]):
                        game[player+1]["color"] = preset_colors[player]

        for player in range(game["player_number"]):
                print(ansi_stitching(game[player + 1]["color"], f"Player {player + 1}, this is your colour."))
                time.sleep(0.3)

        return game

def main():
        CONSTS = {

                "rules": "The rules of catan are as follows: meow",

                "resources": ["ores", "grain", "wood", "brick", "sheep"],

                "dev_cards": ["knight", "progress", "vps"],  

                "ports": ["wood", "grain", "cow", "ore", "brick"],
                "welcome_message": """WELCOME TO MY TEXT-BASED CATAN!
Before we start, make sure \x1b[38;2;142;194;21mthis text\x1b[0m is green!
CREDITS: Vivienne, CATAN game studio
ENTER YOUR COMMAND TO BEGIN :)""",

                "pre_commands" : {
                        "rng": infinite_rng
},

                "commands" : { 
                        "pod": print_own_deck, 
                        "roll": roll_die,
},
        

                "credits": """The credits for this code are as follows:""",


                "commands info" : """These are the commands available to you and what they mean""",

                "building costs" : "building costs are:",

                "colors" : ["red", "green", "blue"]

        }

        game = {
                "input type" : CONSTS["pre_commands"],
                "on" : True
        }

        print(CONSTS["welcome_message"])

        while True:
        
                action = input("> ").strip().lower()

                if not action in game["input type"] and action in [CONSTS["commands"], CONSTS["pre_commands"]]:
                        print("That command's not available right now! Please enter something allowed in the commands.")

                elif action == "ru":
                        print(CONSTS["rules"])

                elif action == "cr":
                        print(CONSTS["credits"])

                elif action == "pcl":
                        print(CONSTS["commands info"])

                elif action == "info":
                        print(CONSTS["info"])

                elif action == "pbc":
                        print(CONSTS["building costs"])

                elif action == 'start game':
                        game["input type"] = CONSTS["commands"]
                        print("Starting your game...")
                        game = setup_game(game, CONSTS)
                        
                else:
                        try:
                                CONSTS["pre_commands"][action](game, CONSTS)
                        except KeyError:
                                print("That command doesn't seem to exist. Do you want to check commands with 'pcl'?")







if __name__== "__main__":
        break program lowk
        main()
import random, time, os

class Grid:
        """A class to contain information that needs to be accessed when either printing or referring to the grid."""
        
        def __init__(self, robber, tiles, settlement_locs, roads, kaomojis, biomes):
                self.robber = robber
                self.tiles = tiles
                self.settlement_locs = settlement_locs
                self.roads = roads
                self.kaomojis = kaomojis
                self.biomes = biomes


class PlayerInfo:
        """A class to easily pass in all variables about player information"""
        
        def __init__(self, game_bank, quick_key, player_dicts):
                self.game_bank = game_bank
                self.quick_key = quick_key
                self.player_dicts = player_dicts
                self.player_turn = 1
                self.game_mode = "initial"
             
                                    
def quick_reorder(road : str):
        """Reorders a 2-letter string based on ascii values (alphabetical order I suppose). 
        This allows me to standardise the way in which roads are called from the dictionary."""

        if road[0] > road[1]:
                road = road[1] + road[0]

        return road


def clear_screen():
        """Clears the screen :D"""
        print("\033c", end="")


def ansi_stitching(color : list, text : str) -> str:
        """Edits the string's value with an ANSI code that imbues it with pretty colours :3"""
        
        colored_ver = "\x1b[38;2;"

        reps = 0
        for value in color:
                colored_ver += str(value)

                reps += 1
                if reps < 3:
                        colored_ver += ";"
        
        colored_ver += "m" + text + "\x1b[0m"

        return colored_ver


def get_player_number() -> int:
        """Gets the number of players, doesn't quit until it's valid"""
        
        player_number = 0
        while not player_number in [3, 4]:
                try:
                        player_number = int(input("How many people are playing? ⋆˚✿🍒𐙚⋆˚\n˚₊ · »-♡→ ").strip()) 
                        if not player_number in [3, 4]:
                                print("You can only play with 3 or 4 people.")
                                
                except ValueError:
                        print("Enter an integer (3 or 4) please.")
                        
        return player_number


def create_player_key(player_number : int) -> list:
        """Simply creates a key which can be used to iterate through players!"""
        
        quick_key = []
        for player in range(player_number):
                quick_key.append(player + 1)
                
        return quick_key


def get_player_name(player : int, player_names : list) -> str:
        """Gets the name of the current player and checks the length and if it is composed of numbers."""
        
        valid_name = False
        while not valid_name:
                
                player_name = input(f"Player {player}, enter your name!\n˚₊ · »-♡→ ").strip()
                if player_name in player_names:
                        print("... That name's already owned. Choose something else.")
                        
                elif player_name.isdigit():
                        print("Sorry, you're not allowed a name consisting of only numbers, as this will cause problems later.")
                        
                elif len(player_name) > 8:
                        print("Please set a shorter name. Sorry if your name is really that long, but it's hard to display.")
                        
                else:
                        valid_name = True
                        
        return player_name


def create_player_dicts(quick_key : list) -> dict:
        """Creates a dictionary for each player"""
        
        player_dicts = {}
        for player in quick_key:
                player_dicts[player] = {}
                
        return player_dicts


def get_player_password() -> str:
        """Gets a password and checks if it's valid."""
        
        valid_password = False
        while not valid_password:
                password = input("Please enter a password; it'll be used to check for your consent later. Keep it short but memorable," + 
                                 "and make sure it's not a password you use for important sites.\n˚₊ · »-♡→ ")
                
                if len(password) > 7:
                        print("That password is way too long. Keep it to 7 or below characters.")
                else:
                        valid_password = True
        
        return password


def setup_player_dicts(quick_key : list) -> dict:
        """Adds a bountiful multitude of keys to each player's dictionary"""
        
        resources = ["ores", "grain", "wood", "brick", "sheep"]
        player_names = []
        player_dicts = create_player_dicts(quick_key)
        for player in quick_key:
                
                name = get_player_name(player, player_names)
                player_names.append(name)
                player_dicts[player]['name'] = name
                player_dicts[player]['password'] = get_player_password()
                
                player_dicts[player]["resources"] = {}
                for resource in resources:
                        player_dicts[player]["resources"][resource] = 0
                player_dicts[player]["dev_cards"] = {}
                
                quick_dict = dict(zip(["knight", "year of plenty", "build road", "monopoly", "VP cards"], [14, 2, 2, 2, 5]))
                for dev_card in quick_dict:
                        player_dicts[player]["dev_cards"][dev_card] = quick_dict[dev_card]
                        
                player_dicts = add_keys(player_dicts, quick_key)
                clear_screen()
                
        print_names(player_names, quick_key)
        return player_dicts


def print_names(player_names, quick_key):
        """Iterates through each player, printing their names"""
        
        print("Okay; your names are: ")
        for player in quick_key:
                if player == quick_key[-1]:
                        print(player_names[player - 1], end=".\n")
                elif player == quick_key[-2]:
                        print(player_names[player - 1], end=", and ")
                else:
                        print(player_names[player - 1], end=", ")


def calculate_VP(player_info : PlayerInfo) -> dict:
        
        victory_points = {}
        for player in player_info.quick_key:
                victory_points[player] = 0
                victory_points[player] += player_info.player_dicts[player]['VP cards']
                for key in player_info.player_dicts[player]['achievements']:
                        victory_points[player] += player_info.player_dicts[player]['achievements'][key]
                victory_points[player] += len(player_info.player_dicts[player]['settlements'])
                victory_points[player] += len(player_info.player_dicts[player]['cities']) * 2
                
        return victory_points
        
        
def check_if_game(victory_points : dict, player_info : PlayerInfo) -> bool:
        """Checks if game should continue or not"""
        
        for player in player_info.quick_key:
                if victory_points[player] >= 10:
                        game = False
                else:
                        game = True
                        
        return game
  
        
def add_keys(player_dicts, quick_key) -> dict:
        """Adds keys to each existing player dictionary"""
        
        for player in quick_key:
                
                player_dicts[player]['roads'] = []
                player_dicts[player]['settlements'] = []
                player_dicts[player]['cities'] = []
                player_dicts[player]['construct_bank'] = {"settlements": 5, "cities": 4, "roads": 15}
                
                player_dicts[player]['achievements'] = {"longest road" : 0, "largest army" : 0}
                player_dicts[player]['knights_recruited'] = 0
                player_dicts[player]['VP cards'] = 0
                
        return player_dicts
               
               
def initialise_player_dicts() -> tuple[list, dict]:
        """Calls all the functions initially neded for the initialising of player dictionaries"""
        
        player_number = get_player_number()
        quick_key = create_player_key(player_number)
        player_dicts = setup_player_dicts(quick_key)
        player_colors = assign_player_colors(quick_key)
        for player, color in zip(player_dicts, player_colors):
                player_dicts[player]["color"] = color
        
        return quick_key, player_dicts


def print_rules():
        """Prints the rules"""
        
        print("""This is the link to the official Catan Almanac:
https://www.catan.com/sites/default/files/2024-01/Almanac%20CATAN-3D.pdf
If the link doesn't work, please paste it into your browser.""")


def choose_color() -> list:
        """Get a player's colors by iterating through red, blue, and green."""
        
        player_color = []
        satisfied = False
        while not satisfied:
                get_color(player_color)   
                                        
                confirmed = False
                while not confirmed:
                        confirmed, satisfied = confirm_color(player_color, satisfied, confirmed)
                        

        clear_screen()
        return player_color


def get_color(player_color : list) -> list:
        color_codes = {"red" : [255, 0, 0], "green" : [0, 255, 0], "blue" : [0, 0, 255]}
        for color in color_codes:               
                        valid_input = False
                        while not valid_input:
                                action = input(ansi_stitching(color_codes[color], f"‧₊˚♪ 𝄞₊˚⊹ What value would you like to use for {color}? ‧₊˚♪ 𝄞₊˚⊹\n˚₊ · »-♡→ ")).strip().lower()
                                try:
                                        if int(action) <= 255:
                                                player_color.append(int(action))
                                                valid_input = True
                                        else:
                                                print("Sorry; RGB values only go up to 255.")
                                        
                                except ValueError:
                                        print("Please input a valid integer, in arabic numerals, within the range of 0 to 255.")
                                        
        return player_color
            
            
def confirm_color(player_color, satisfied, confirmed) -> tuple[bool, bool]:
        confirm = input(ansi_stitching(player_color, """This is what your color looks like - are you sure you want it? 
Type 'Y' for yes and 'N' for no. 
Please make sure all other players can see this color.\n""") + "> ").strip()
        if confirm == "N":
                player_color = []
                confirmed = True
        elif confirm == "Y":
                satisfied = True
                confirmed = True
        else:
                print("Please type either 'Y' or 'N'. This is case sensitive.")
                
        return confirmed, satisfied
                               
                                                            
def assign_player_colors(quick_key : list) -> list:
        """Iterates through each player and makes sure they have a colour assigned"""
        
        preset_colors = [[1, 201, 184], [252, 210, 1], [252, 84, 1], [210, 1, 252]]
        player_colors = []
        for player in quick_key:
                action = ""
                while not action in ["y", "n"]:
                        action = input("Would you like to customise your own color? (If not, you'll get a premade one!)" + 
                                       " Type 'Y' for yes and 'N' for no.\n˚₊ · »-♡→ ").strip().lower()
                        if action == "y":
                                player_colors.append(choose_color())
                        elif action == "n":
                                print(ansi_stitching(preset_colors[player - 1], "This is your assigned color!"))
                                player_colors.append(preset_colors[player - 1])
                                time.sleep(0.3)
                        else:
                                print("Sorry, please either type 'y' or 'n'.")
                clear_screen()
                                
        print_player_colors(quick_key, player_colors)
        
        return player_colors           

                                
def print_player_colors(quick_key, player_colors):
        """Prints the colour for each player"""
        
        for player in quick_key:
                print(ansi_stitching(player_colors[player - 1], f"Player {player}, this is your color."))
                time.sleep(0.3)


def initialise_resource_cards() -> tuple[dict, dict]:
        """Initialises the dictionary for each resource to be passed into the game bank"""
        
        resources = {}
        for resource in ["ores", "grain", "wood", "brick", "sheep"]:
                resources[resource] = 19
        dev_bank = {}
        dev_cards = ["knight", "year of plenty", "build road", "monopoly", "VP cards"]
        dev_values = [14, 2, 2, 2, 5]
        for dev_card, value in zip(dev_cards, dev_values):
                dev_bank[dev_card] = value
                
        print(dev_bank)
        
        return resources, dev_bank


def draw_dev_card(card_list : list, game_bank) -> tuple[str, dict]:
        """Draws a card and makes it so that the game bank loses the relevant card."""
        
        drawn_card = card_list.pop(0)
        game_bank['dev_cards'][drawn_card] -= 1
        
        return drawn_card, game_bank
                
                
def list_dev_cards(game_bank : dict) -> list:
        """Compiles a list of all the development cards available to draw"""
        
        card_list = []
        for card in game_bank['dev_cards']:
                if game_bank['dev_cards'][card] > 0:
                        card_list.append(card)
        
        if card_list == []:
                print("Looks like the game bank is out of dev cards. Sorry!")
        
        return card_list
        
                
def make_bank() -> dict:
        """Calls the functions needed to set up the game bank"""
        
        game_bank = {}
        resources, dev_bank = initialise_resource_cards()
        game_bank['resources'] = resources
        game_bank['dev_cards'] = dev_bank
        game_bank['building_costs'] = {'roads' : {'brick' : 1, 'wood' : 1},
                                       'settlements' : {'brick' : 1, 'wood' : 1, 'grain' : 1, 'sheep' : 1},
                                       'cities' : {'grain' : 2, 'ores' : 3},
                                       'dev card': {'sheep' : 1, 'grain' : 1, 'ores' : 1}}
        
        return game_bank


def create_tiles() -> dict:
        """Sets up tiles"""
        
        print("Setting up your tiles...")
        tiles = {}
        for i in range(19):
                tiles[("S"+str(i+1))] = {}
                
        return tiles


def place_desert(tiles : dict) -> tuple[dict, str]:
        """Places the exception desert"""
        
        print("Spawning your desert...")
        desert_placement = random.randint(1, 19)
        tiles[("S"+str(desert_placement))]["biome"] = "desert"
        tiles[("S"+str(desert_placement))]["number"] = "NA"
        robber = "S"+str(desert_placement)
        
        return tiles, robber

        
def generate_grid(biomes : list, number_tokens : list, associated_settlements : dict) -> tuple[dict, str, dict, dict]:
        """Generates the grid"""
        
        settlement_locations = "abcdefghijklmnopqrstuvwxyz".upper()
        settlement_locations += settlement_locations.lower() + "+" + "$"
        
        tiles = create_tiles()
        tiles, robber = place_desert(tiles)
        tiles = assign_tile_variables(tiles, biomes, number_tokens, associated_settlements)
        
        settlement_locs = assign_ports(settlement_locations)
        roads = create_roads()
        
        return tiles, robber, settlement_locs, roads

        
def create_roads() -> dict:
        """Creates a dictionary for roads and adds roads into it"""
        
        print("Paving your roads...")
        counter = 0
        quick_dict = dict(zip(["__", "/", "\\"], ["ABCDEF$GHIJKMNOPRSTUVWYZabdefghiklmnpqrstuvwxyz+", 
                        "ADCG$LRXMSHNEIJPQWVbcihnoutyx+rwmsflagOUTZYedjkq",
                        "BEFJDHIOGMLRSYNTXdekjpqvwzsxntiobhWcKQPVUaZfgmlr"]))
        roads = {}
        for road_type in ["__", "/", "\\"]:
                for i in range(len(quick_dict[road_type])//2):
                        
                        road = quick_dict[road_type][counter]
                        counter += 1
                        road += quick_dict[road_type][counter]
                        counter += 1

                        road = quick_reorder(road)
                        roads[road] = {'display' : road_type, 'owner' : 0}
                counter = 0
                
        return roads

        
def assign_tile_variables(tiles : dict, biomes : list, number_tokens : list, associated_settlements):
        """Assigns variables to each tile"""
         
        for i in range(19):
                try:
                        tiles[("S"+str(i+1))]["biome"]
                except KeyError:
                        random.shuffle(biomes)
                        chosen_biome = biomes.pop()
                        tiles[("S"+str(i+1))]["biome"] = chosen_biome

                        random.shuffle(number_tokens)
                        chosen_number = number_tokens.pop()
                        tiles[("S"+str(i+1))]["number"] = chosen_number
                
                tiles["S"+str(i+1)]["attached_settlements"] = associated_settlements["S"+str(i+1)]
        
        return tiles


def assign_ports(settlement_locations : str) -> dict:
        """Assigns ports to relevant tiles"""
        
        ports = ["wood", "grain", "sheep", "ore", "brick"]
        settlement_locs = {}
        for letter in settlement_locations:
                settlement_locs[letter] = {"display": letter}
                settlement_locs[letter]["port"] = ""
                settlement_locs[letter]["owner"] = 0
        for loc in "ABFJouxy":
                settlement_locs[loc]["port"] = "3:1 port"
        i = 0
        reps = 0
        for loc in "RQCGWcvwjp":
                reps += 1
                port_to_place = f"2:1 {ports[i]} port"
                settlement_locs[loc]["port"] = port_to_place
                if reps % 2 == 0:
                        i += 1
        
        return settlement_locs

                        
def make_biomes() -> list:
        """Creates a list of biomes"""
        
        biomes = []
        for i in range(3):
                biomes.append("ores")
                biomes.append("brick")

        for i in range(4):
                biomes.append("grain")
                biomes.append("wood")
                biomes.append("sheep")
        
        return biomes


def make_token_list() -> list:
        """Creates a list of the number tokens that will be assigned onto each hex of the grid."""
        
        number_tokens = []
        for i in range(10):
                if (i + 2) != 7:
                        for x in range(2):
                                number_tokens.append(i + 2)
        number_tokens.append(1)
        number_tokens.append(12)
        
        return number_tokens


def print_board(player_info : PlayerInfo, grid : Grid, game_bank : dict):
        """Prints out basic information (visual display for what players need to see during their turns)"""
        
        print("________ WELCOME TO THE WORLD OF CATAN. WHERE WILL YOU SETTLE TODAY? ________\n")
        print(f"˗ˋˏ$ˎˊ˗ GAME BANK ˗ˋˏ$ˎˊ˗")
        for resource in game_bank["resources"]:
                print(f'{resource} : {game_bank["resources"][resource]}', end="  ||  ")
        print("\n")
        for dev_card in game_bank['dev_cards']:
                print(f'{dev_card} : {game_bank["dev_cards"][dev_card]}', end="  ||  ")
        print("\n")
        for player in player_info.quick_key:
                print(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player} ({player_info.player_dicts[player]['name']})"), end="  ||  ")
        print("\n")
        
        print_grid(grid)
        
        print(f"The robber is currently pillaging the citizens of {grid.robber} and stealing all their {grid.tiles[grid.robber]['biome']}...")

        
def initial_loop(player_info : PlayerInfo, grid : Grid, game_bank : dict) -> tuple[PlayerInfo, Grid, dict]:
        """Carries out the initial loop for the players to place down their settlements and roads FOR FREE."""

        print_board(player_info, grid, game_bank)
        print(f"We'll go from player 1 to player {len(player_info.quick_key)}; you can place two settlements and two roads for free. Please choose wisely.")
        
        for i in range(2):
                for player in player_info.quick_key:
                        player_info.player_turn = player
                        
                        player_info, grid = place_settlement(player_info, grid, game_bank)
                        player_info, grid = place_road(player_info, grid, game_bank)
                        

        player_info.player_turn = 1
                        
        return player_info, grid, game_bank


def place_settlement(player_info : PlayerInfo, grid, game_bank):
        """Places down a settlement. Does not deduct any resources from the player, do this separately"""
        
        player = player_info.player_turn
        valid = False
        while not valid:
                text = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, where would you like to place your settlement?") + "\n˚₊ · »-♡→ ").strip()
                valid = check(text, grid, player_info, "settlement")
        player_info.player_dicts[player]['settlements'].append(text)
        print(grid.settlement_locs[text]['display'])
        grid.settlement_locs[text]['display'] = ansi_stitching(player_info.player_dicts[player]['color'], grid.settlement_locs[text]['display'])
        grid.settlement_locs[text]['owner'] = player
        clear_screen()
        print_board(player_info, grid, game_bank)
        
        return player_info, grid


def place_road(player_info : PlayerInfo, grid : Grid, game_bank : dict) -> tuple[PlayerInfo, Grid]:
        """Places down a road and changes player information accordingly, as well as the grid. Does not take resources from the player in the process."""
        
        player = player_info.player_turn
        
        valid = False
        while not valid:
                text = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, where are you placing your road?") + "\n˚₊ · »-♡→ ").strip()
                valid = check(text, grid, player_info, "road")
        player_info.player_dicts[player]['roads'].append(text)
        grid.roads[quick_reorder(text)]['display'] = ansi_stitching(player_info.player_dicts[player]['color'], grid.roads[quick_reorder(text)]['display'])
        clear_screen()
        print_board(player_info, grid, game_bank)
        
        return player_info, grid
        
        
def print_grid(grid : Grid):
        """Prints out the grid."""

        grid_part_1 = (
#line 1
(" " * 65) + "3: 1 port" + "\n" +
#line 2
(" " * 65) + "/      \\" + "\n" +
#line 3
(" " * 64) + "/        \\" + "\n" +
#line 4
(" " * 20) + "sea" + (" " * 38) + grid.settlement_locs["A"]["display"] + " " + (grid.roads["AB"]["display"] + " ") * 4 + grid.settlement_locs["B"]["display"] + (" " * 38) + "sea" + "\n" +
#line 5
(" " * 61) + grid.roads["AD"]["display"] + "              " + grid.roads["BE"]['display'] + "\n" +
#line 6 & 7
(" " * 60) + grid.roads["AD"]['display'] + "                " + grid.roads["BE"]['display'] + "\n\n" +
#line 8
(" " * 35) + ("2:1 grain port") + (" " * 9) + grid.roads["AD"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S1"]["biome"]] + (" "* 7) + grid.roads["BE"]['display'] + (" " * 16) + "3:1 port" + "\n" +
#line 9
(" " * 36) + "|    " + "\\" + "   " + (grid.roads["CD"]['display'] + " ") * 4 + grid.roads["AD"]['display'] + (" " * 10) + str(grid.tiles["S1"]["number"]) 
+ (" " * 11 if len(str(grid.tiles["S1"]["number"])) == 1 else " " * 10) + grid.roads["BE"]['display'] + " " + (grid.roads["EF"]['display'] + " ") * 4 + "   /  |\n" +
#line 10
(" " * 36) + "|" + (" " * 3) + grid.settlement_locs["C"]["display"] + " " + grid.roads["CG"]['display'] + (" " * 11) + grid.settlement_locs["D"]["display"] + "  " + grid.roads["DH"]['display']
+ (" " * ((22 - len(str(grid.tiles["S1"]["biome"])))//2)) + grid.tiles["S1"]["biome"] +
(" " * (((22-len(str(grid.tiles["S1"]["biome"])))//2)+ (1 if len(str(grid.tiles["S1"]["biome"]))%2 != 0 else 0)))
+ grid.roads["EI"]['display'] + " " + grid.settlement_locs["E"]["display"] + (" " * 8) + grid.settlement_locs["F"]["display"] + "  " + grid.roads["FJ"]['display'] + "     |\n" +
#line 11
(" " * 36) + "|" + "    " + grid.roads["CG"]['display'] +  (" " * 16) + grid.roads["DH"]['display'] + (" " * 9) + "S1" + (" " * 9) + grid.roads["EI"]['display'] + (" " * 15) + 
grid.roads["FJ"]['display'] + "    |" + "\n" +
#line 12
(" " * 36) + "|" + (" " * 63) + "|" + "\n" +
#line 13
(" " * 36) + "|" + "  " + grid.roads["CG"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S2"]["biome"]] + (" " * 7) + grid.roads["DH"]['display'] 
+ (" " * 16) + grid.roads["EI"]['display'] + " "  + (" " * 6) + (grid.kaomojis[grid.tiles["S3"]["biome"]]) 
+ (" " * 6) + grid.roads["FJ"]['display'] +"  |\n" +
#line 14
(" " * 21) + grid.settlement_locs["$"]["display"] + " " + (grid.roads[quick_reorder("G$")]['display'] + " ") * 4 + grid.settlement_locs["G"]["display"] + "  " + grid.roads["CG"]['display'] + (" " * 10) + str(grid.tiles["S2"]["number"]) + 
(" " * 9 if len(str(grid.tiles["S2"]["number"])) == 1 else " " * 8) + grid.settlement_locs["H"]["display"] + " " + grid.roads["DH"]['display'] + " " + (grid.roads["HI"]['display'] + " ") * 4 + " " + grid.roads["EI"]['display'] + " " + grid.settlement_locs["I"]["display"] +
(" " * 8) + str(grid.tiles["S3"]["number"]) + (" " * 8 if len(str(grid.tiles["S3"]["number"])) == 1 else " " * 7) + grid.settlement_locs["J"]["display"] + " " + grid.roads["FJ"]['display'] + " | " + (grid.roads["JK"]['display'] + " ") * 4 
+ grid.settlement_locs["K"]["display"] + "\n" +
#line 15
(" " * 21) + grid.roads[quick_reorder("L$")]['display'] + (" " * 16) + grid.roads["GM"]['display'] + (" " * ((22 - len(str(grid.tiles["S2"]["biome"])))//2)) + grid.tiles["S2"]["biome"] + (" " * 9 if grid.tiles["S2"]["biome"] != "desert" else " " * 8)
+ grid.roads["HN"]['display'] + (" " * 14) + grid.roads["IO"]['display'] + (" " * ((21 - len(str(grid.tiles["S3"]["biome"])))//2)) + grid.tiles["S3"]["biome"] + (" " * ( (21 - len(grid.tiles["S3"]["biome"])) //2   ) ) + 
(" " * (1 if len(grid.tiles["S3"]["biome"]) % 2 != 1 else 0)) + grid.roads["JP"]['display'] + (" " * 14) + grid.roads["KQ"]['display'] + "\n" +
#line 16 & 17 
(" " * 20) + grid.roads[quick_reorder("L$")]['display'] + (" " * 18) + grid.roads["GM"]['display'] + (" " * 9) + "S2" + (" " * 9) + grid.roads["HN"]['display'] + (" " * 16) + grid.roads["IO"]['display'] + (" " * 8) + "S3" + (" " * 9) + grid.roads["JP"]['display'] + 
(" " * 16) + grid.roads["KQ"]['display'] + "\n\n" +
#line 18
(" " * 18) + grid.roads[quick_reorder("L$")]['display'] + (" " * 8) + grid.kaomojis[grid.tiles["S4"]["biome"]] + (" " * 8) + grid.roads["GM"]['display'] + (" " * 16) + grid.roads["HN"]['display'] + (" " * 7) + 
grid.kaomojis[grid.tiles["S5"]["biome"]] + (" " * 7) + grid.roads["IO"]['display']
+ (" " * 15) + grid.roads["JP"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S6"]["biome"]] + (" " * 7) + grid.roads["KQ"]['display'] + "\n" + 
#line 19
(" " * 15) + grid.settlement_locs["L"]["display"] + " " + grid.roads[quick_reorder("L$")]['display'] + (" " * 11) + str(grid.tiles["S4"]["number"]) + (" " * (10 if len(str(grid.tiles["S4"]["number"])) == 1 else 9)) + grid.settlement_locs["M"]["display"] +
" " + grid.roads["GM"]['display'] + "  " + (grid.roads["MN"]['display'] + " ") * 4 + grid.roads["HN"]['display'] + grid.settlement_locs["N"]["display"] + (" " * 9) + str(grid.tiles["S5"]["number"]) + (" " * 9 if len(str(grid.tiles["S5"]["number"])) == 1 else " " * 8) + grid.settlement_locs["O"]["display"] +
" " + grid.roads["IO"]['display'] + " " + (grid.roads["OP"]['display'] + " ") * 4 + grid.roads["JP"]['display'] + " " + grid.settlement_locs["P"]["display"] + (" " * 8) + str(grid.tiles["S6"]["number"]) + (" " * 11 if len(str(grid.tiles["S6"]["number"])) == 1 else " " * 10) + grid.roads["KQ"]['display']
+ " " + grid.settlement_locs["Q"]["display"] + "\n"
)

        grid_part_2 = (
#line 20
(" " * 17) + grid.roads["LR"]['display'] + (" " * ((24 - len(str(grid.tiles["S4"]["biome"])))//2)) + grid.tiles["S4"]["biome"] + (" " * 10 if grid.tiles["S4"]["biome"] != "desert" else " " * 9) + grid.roads["MS"]['display'] + (" " * 14) + grid.roads["NT"]['display'] +
(" " * ((22 - len(str(grid.tiles["S5"]["biome"])))//2)) + grid.tiles["S5"]["biome"] + (" " * 9 if grid.tiles["S5"]["biome"] != "desert" else " " * 8) + grid.roads["OU"]['display'] + (" " * 13) + grid.roads["PV"]['display'] +
(" " * ((22 - len(str(grid.tiles["S6"]["biome"])))//2)) + grid.tiles["S6"]["biome"] + (" " * 9 if grid.tiles["S6"]["biome"] != "desert" else " " * 8) + grid.roads["QW"]['display'] + "\n" +
#line 21 & 22
(" " * 18) + grid.roads["LR"]['display'] + (" " * 10) + "S4" + (" " * 10) + grid.roads["MS"]['display'] + (" " * 16) + grid.roads["NT"]['display'] + (" " * 9) + "S5" + (" " * 9) + grid.roads["OU"]['display'] + (" " * 15) + grid.roads["PV"]['display'] 
+ (" " * 9) + "S6" + (" " * 9) + grid.roads["QW"]['display'] + "\n\n" +
#line 23
(" " * 20) + grid.roads["LR"]['display'] + (" " * 18) + grid.roads["MS"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S7"]["biome"]] + (" " * 7) + grid.roads["NT"]['display'] + (" " * 16) + grid.roads["OU"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S8"]["biome"]]  + (" " * 6) + grid.roads["PV"]['display'] +
(" " * 16) + grid.roads["QW"]['display'] + "\n" +
#line 24
(" " * 3) + "2:1 wood port - " + grid.settlement_locs["R"]["display"] + " " + grid.roads["LR"]['display'] + "  " + (grid.roads["RS"]['display'] + " ") * 4 + grid.settlement_locs["S"]["display"] + " " + grid.roads["MS"]['display'] + (" " * 10) + str(grid.tiles["S7"]["number"]) + 
(" " * 8 if len(str(grid.tiles["S7"]["number"])) == 1 else " " * 7) + grid.settlement_locs["T"]["display"] + "  " + grid.roads["NT"]['display'] + "  " + (grid.roads["TU"]['display'] + " ") * 4 + grid.roads["OU"]['display'] + " " + grid.settlement_locs["U"]["display"] +
(" " * 8) + str(grid.tiles["S8"]["number"]) + (" " * 8 if len(str(grid.tiles["S8"]["number"])) == 1 else " " * 7) + grid.settlement_locs["V"]["display"] + " " + grid.roads["PV"]['display'] + " " + (grid.roads["VW"]['display'] + " ") * 4 + " " + grid.roads["QW"]['display'] + 
grid.settlement_locs["W"]["display"] +  " _ _ _  2:1 sheep port" + "\n" +
#line 25
(" " * 8) + "\\" + (" " * 12) + grid.roads["RX"]['display'] + (" " * 16) + grid.roads["SY"]['display'] + (" " * ((22 - len(str(grid.tiles["S7"]["biome"])))//2)) + grid.tiles["S7"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S7"]["biome"])))//2) + (1 if len(str(grid.tiles["S7"]["biome"]))%2 != 0 else 0))) + grid.roads["TZ"]['display'] + (" " * 14) + grid.roads["Ua"]['display'] +
(" " * ((21 - len(str(grid.tiles["S8"]["biome"])))//2)) + grid.tiles["S8"]["biome"] + 
(" " * (((21-len(str(grid.tiles["S8"]["biome"])))//2) + (1 if len(str(grid.tiles["S8"]["biome"]))%2 != 1 else 0))) + grid.roads["Vb"]['display'] + (" " * 14) + grid.roads["Wc"]['display'] + "         /\n" +
#line 26
(" " * 9) + "\\" + (" " * 10) + grid.roads["RX"]['display'] + (" " * 18) + grid.roads["SY"]['display'] + (" " * 9) + "S7" + (" " * 9) + grid.roads["TZ"]['display'] + (" " * 16) + grid.roads["Ua"]['display'] + (" " * 8) + "S8" + (" " * 9) + 
grid.roads["Vb"]['display'] + (" " * 16) + grid.roads["Wc"]['display'] + "       /" + "\n" +
#line 27
(" " * 10) + "\\" + (" " * 110) + "/" + "\n" +
#line 28
(" " * 11) + "\\" + (" " * 6) + grid.roads["RX"]['display'] + (" " * 8) + grid.kaomojis[grid.tiles["S9"]["biome"]] + (" " * 8) + grid.roads["SY"]['display'] + (" " * 16) + 
grid.roads["TZ"]['display'] + (" " * 6) + grid.kaomojis[grid.tiles["S10"]["biome"]] + (" " * 8) + grid.roads["Ua"]['display']
+ (" " * 15) + grid.roads["Vb"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S11"]["biome"]] + (" " * 7) + grid.roads["Wc"]['display'] + "   /" + "\n" +
#line 29
(" " * 12) + "\\  " + grid.settlement_locs["X"]["display"] + " " + grid.roads["RX"]['display'] + (" " * 12) + str(grid.tiles["S9"]["number"]) + 
(" " * 9 if len(str(grid.tiles["S9"]["number"])) == 1 else " " * 8) 
+ grid.settlement_locs["Y"]["display"] + " " + grid.roads["SY"]['display'] + " " + (grid.roads["YZ"]['display'] + " ") * 4 + grid.settlement_locs["Z"]["display"] + 
grid.roads["TZ"]['display'] + (" " * 10) + str(grid.tiles["S10"]["number"]) + (" " * 9 if len(str(grid.tiles["S10"]["number"])) == 1 else " " * 8) + 
grid.settlement_locs["a"]["display"] + " " + grid.roads["Ua"]['display'] + (" " + grid.roads["ab"]['display']) * 4 + grid.settlement_locs["b"]["display"] + grid.roads["Vb"]['display'] +
(" " * 10) + str(grid.tiles["S11"]["number"]) + (" " * 11 if len(str(grid.tiles["S11"]["number"])) == 1 else " " * 10) + grid.roads["Wc"]['display'] + " " + grid.settlement_locs["c"]["display"] + "\n" +
#line 30
(" " * 17) + grid.roads["Xd"]['display'] + (" " * ((24 - len(str(grid.tiles["S9"]["biome"])))//2)) + grid.tiles["S9"]["biome"] + (" " * (((24-len(str(grid.tiles["S9"]["biome"])))//2) + (1 if len(str(grid.tiles["S9"]["biome"]))%2 != 0 else 0))) 
+ grid.roads["Ye"]['display'] + (" " * 14) + grid.roads["Zf"]['display'] + (" " * ((22 - len(str(grid.tiles["S10"]["biome"])))//2)) + grid.tiles["S10"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S10"]["biome"])))//2) + (1 if len(str(grid.tiles["S10"]["biome"]))%2 != 0 else 0))) + grid.roads["ag"]['display'] + (" " * 13) + grid.roads["bh"]['display'] +
(" " * ((22 - len(str(grid.tiles["S11"]["biome"])))//2)) + grid.tiles["S11"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S11"]["biome"])))//2) + (1 if len(str(grid.tiles["S11"]["biome"]))%2 != 0 else 0))) + grid.roads["ci"]['display'] + "\n"
        
        )

        grid_part_3 = (
#line 31 & 32
(" " * 18) + grid.roads["Xd"]['display'] + (" " * 10) + "S9" + (" " * 10) + grid.roads["Ye"]['display'] + (" " * 16) + grid.roads["Zf"]['display'] + (" " * 8) + "S10" + (" " * 9) + grid.roads["ag"]['display'] + (" " * 15) + grid.roads["bh"]['display'] + (" " * 8) + "S11" + (" " * 9) + grid.roads["ci"]['display'] + "\n\n" +
#line 33
(" " * 20) + grid.roads["Xd"]['display'] + (" " * 18) + grid.roads["Ye"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S12"]["biome"]] + (" " * 7) + grid.roads["Zf"]['display'] + (" " * 16) + grid.roads["ag"]['display'] + (" " * 6) + grid.kaomojis[grid.tiles["S13"]["biome"]] + (" " * 7) + 
grid.roads["bh"]['display'] + (" " * 16) + grid.roads["ci"]['display']
+ "\n" +
#line 34
(" " * 19) + grid.settlement_locs["d"]["display"] + " " + grid.roads["Xd"]['display'] + "  " + (grid.roads["de"]['display'] + " ") * 4 + grid.settlement_locs["e"]["display"] + " " + grid.roads["Ye"]['display'] + (" " * 10) + 
str(grid.tiles["S12"]["number"]) + (" " * 9 if len(str(grid.tiles["S12"]["number"])) == 1 else " " * 8) + grid.settlement_locs["f"]["display"] + " " + grid.roads["Zf"]['display'] + " " + (grid.roads["fg"]['display'] + " ") * 4 + grid.settlement_locs["g"]["display"] + grid.roads["ag"]['display'] +
(" " * 10) + str(grid.tiles["S13"]["number"]) + (" " * 8 if len(str(grid.tiles["S13"]["number"])) == 1 else " " * 7) + grid.settlement_locs["h"]["display"] + " " + grid.roads["bh"]['display'] + " " + (grid.roads["hi"]['display'] + " ") * 4 + " " + grid.roads["ci"]['display'] + " " 
+ grid.settlement_locs["i"]["display"] + "\n" +
#line 35
(" " * 21) + grid.roads["dj"]['display'] + (" " * 16) + grid.roads["ek"]['display'] + (" " * ((23 - len(str(grid.tiles["S12"]["biome"])))//2)) + grid.tiles["S12"]["biome"] + 
(" " * (((21-len(str(grid.tiles["S12"]["biome"])))//2) + (1 if len(str(grid.tiles["S12"]["biome"]))%2 != 1 else 0))) + grid.roads["fl"]['display'] + (" " * 14) + grid.roads["gm"]['display']
+ (" " * ((21 - len(str(grid.tiles["S13"]["biome"])))//2)) + grid.tiles["S13"]["biome"] + 
(" " * (((21-len(str(grid.tiles["S13"]["biome"])))//2) + (1 if len(str(grid.tiles["S13"]["biome"]))%2 != 1 else 0))) + grid.roads["hn"]['display'] + (" " * 14) + grid.roads["io"]['display'] + "\n" +
#line 36 & 37
(" " * 20) + grid.roads["dj"]['display'] + (" " * 18) + grid.roads['ek']['display'] + (" " * 8) + "S12" + (" " * 9) + grid.roads['fl']['display'] + (" " * 16) + grid.roads['gm']['display'] + (" " * 8) + "S13" + (" " * 8) + grid.roads['hn']['display'] + (" " * 16) + grid.roads['io']['display'] + "\n\n" +
#line 38 
(" " * 18) + grid.roads['dj']['display'] + (" " * 8) + grid.kaomojis[grid.tiles["S14"]["biome"]] + (" " * 8) + grid.roads['ek']['display'] + (" " * 16) + grid.roads['fl']['display'] + 
(" " * 7) + grid.kaomojis[grid.tiles["S15"]["biome"]] + (" " * 7) + grid.roads['gm']['display'] + (" " * 15) + grid.roads['hn']['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S16"]["biome"]] + (" " * 7)
+ grid.roads['io']['display'] + "\n" +
#line 39
(" " * 15) + grid.settlement_locs["j"]["display"] + " " + grid.roads['dj']['display'] + (" " * 11) + str(grid.tiles["S14"]["number"]) + (" " * 10 if len(str(grid.tiles["S14"]["number"])) == 1 else " " * 9) + grid.settlement_locs["k"]["display"]
+ " " + grid.roads['ek']['display'] + " " + (grid.roads["kl"]['display'] + " ") * 4 + grid.settlement_locs["l"]["display"] + grid.roads['fl']['display'] + (" " * 10) + str(grid.tiles["S15"]["number"]) + (" " * 9 if len(str(grid.tiles["S15"]["number"])) == 1 else " " * 8)
+ grid.settlement_locs["m"]["display"] + " " + grid.roads['gm']['display'] + " " + (grid.roads["mn"]['display'] + " ") * 4 + grid.roads['hn']['display'] + grid.settlement_locs["n"]["display"] + (" " * 9) + str(grid.tiles["S16"]["number"]) + 
(" " * 11 if len(str(grid.tiles["S16"]["number"])) == 1 else " " * 10) + grid.roads['io']['display'] + " " + grid.settlement_locs["o"]["display"] + "\n" +
#line 40
(" " * 17) + grid.roads['jp']['display'] + (" " * ((24 - len(str(grid.tiles["S14"]["biome"])))//2)) + grid.tiles["S14"]["biome"] +
(" " * (((24-len(str(grid.tiles["S14"]["biome"])))//2) + (1 if len(str(grid.tiles["S14"]["biome"]))%2 != 0 else 0))) + grid.roads['kq']['display'] + (" " * 14) + grid.roads['lr']['display'] +
(" " * ((22 - len(str(grid.tiles["S15"]["biome"])))//2)) + grid.tiles["S15"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S15"]["biome"])))//2) + (1 if len(str(grid.tiles["S15"]["biome"]))%2 != 0 else 0))) + grid.roads['ms']['display'] + (" " * 13) + grid.roads['nt']['display'] +
(" " * ((22 - len(str(grid.tiles["S16"]["biome"])))//2)) + grid.tiles["S16"]["biome"] + 
(" " * (((22 - len(str(grid.tiles["S16"]["biome"])))//2) + (1 if len(str(grid.tiles["S16"]["biome"]))%2 != 0 else 0))) + grid.roads['ou']['display'] + "\n" +
#line 41 
(" " * 14) + "/" + (" " * 3) + grid.roads['jp']['display'] + (" " * 9) + "S14"  + (" " * 10) + grid.roads['kq']['display'] + (" " * 16) + grid.roads['lr']['display'] + (" " * 8) + "S15" + (" " * 9) + grid.roads['ms']['display'] 
+ (" " * 15) + grid.roads['nt']['display'] + (" " * 8) + "S16" + (" " * 9) + grid.roads['ou']['display'] + 
(" " * 3) + "\\" + "\n" +
#line 42
(" " * 13) + "/" + (" " * 107) + "\\" + "\n" 
                )

        grid_part_4 = (
#line 43
(" " * 12) + "/" + (" " * 7) + grid.roads['jp']['display'] + (" " * 18) + grid.roads['kq']['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S17"]["biome"]] + 
(" " * 7) + grid.roads['lr']['display'] + (" " * 16) + grid.roads['ms']['display'] + (" " * 6) + grid.kaomojis[grid.tiles["S18"]["biome"]] + (" " * 7)
+ grid.roads['nt']['display'] + (" " * 16) + grid.roads['ou']['display'] + (" " * 7) + "\\" + "\n" +
#line 44
" 2:1 brick port _  " + grid.settlement_locs["p"]["display"] + " " + grid.roads['jp']['display'] + " " + (grid.roads["pq"]['display'] + " ") * 4 + " " 
+ grid.settlement_locs["q"]["display"] + " " + grid.roads['kq']['display'] + (" " * 11) + str(grid.tiles["S17"]["number"]) +
(" " * 8 if len(str(grid.tiles["S17"]["number"])) == 1 else " " * 7) + grid.settlement_locs["r"]["display"] + " " + grid.roads['lr']['display'] + " " + 
(grid.roads["rs"]['display'] + " ") * 4 + grid.settlement_locs["s"]["display"] + grid.roads['ms']['display'] + (" " * 10) + 
str(grid.tiles["S18"]["number"]) + (" " * 8 if len(str(grid.tiles["S18"]["number"])) == 1 else " " * 7) + grid.settlement_locs["t"]["display"] + " " + grid.roads['nt']['display'] + 
" " + (grid.roads["tu"]['display'] + " ") * 4 + " " + grid.roads['ou']['display'] +
grid.settlement_locs["u"]["display"] + "  _ _ 3:1 port" + "\n" +
#line 45
(" " * 38) + grid.roads['qv']['display'] + (" " * ((22 - len(str(grid.tiles["S17"]["biome"])))//2)) + grid.tiles["S17"]["biome"] + 
(" " * (((22 - len(str(grid.tiles["S17"]["biome"])))//2) + (1 if len(str(grid.tiles["S17"]["biome"]))%2 != 0 else 0))) + grid.roads['rw']['display'] + (" " * 14) + grid.roads['sx']['display'] +
(" " * ((21 - len(str(grid.tiles["S18"]["biome"])))//2)) + grid.tiles["S18"]["biome"] + (" " * (((21 - len(str(grid.tiles["S18"]["biome"])))//2) 
+ (1 if len(str(grid.tiles["S18"]["biome"]))%2 != 1 else 0))) + grid.roads['ty']['display'] + "\n" +
#line 46 & 47
(" " * 39) + grid.roads['qv']['display'] + (" " * 8)  + "S17" + (" " * 9) + grid.roads['rw']['display'] + (" " * 16) + grid.roads['sx']['display'] + 
(" " * 8) + "S18" + (" " * 8) + grid.roads['ty']['display'] + "\n\n" +
#line 48
(" " * 41) + grid.roads['qv']['display'] + (" " * 16) + grid.roads['rw']['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S19"]["biome"]] + (" " * 7) + 
grid.roads['sx']['display'] + (" " * 15) + grid.roads['ty']['display'] + "\n" +
#line 49
(" " * 42) + grid.roads['qv']['display'] + grid.settlement_locs["v"]["display"] + " " + (grid.roads["vw"]['display'] + " ") * 4 + grid.settlement_locs["w"]["display"] + 
(" " * 10) + str(grid.tiles["S19"]["number"]) + (" " * 9 if len(str(grid.tiles["S19"]["number"])) == 1 else " " * 8) + grid.settlement_locs["x"]["display"] + " " + 
grid.roads['sx']['display'] + " " + (grid.roads["xy"]['display'] + " ") * 4 + grid.roads['ty']['display'] + " " 
+ grid.settlement_locs["y"]["display"] + "\n" +
#line 50
(" " * 58) + grid.roads['wz']['display'] +(" " * ((21 - len(str(grid.tiles["S19"]["biome"])))//2)) + grid.tiles["S19"]["biome"] + 
(" " * (((21 - len(str(grid.tiles["S19"]["biome"])))//2) + (1 if len(str(grid.tiles["S19"]["biome"]))%2 != 1 else 0))) + grid.roads[quick_reorder("x+")]['display'] + "\n" +
#line 51
(" " * 44) + "\\" + (" " * 11) + "/  " + grid.roads['wz']['display'] + (" " * 8) + "S19" + (" " * 8) + grid.roads[quick_reorder("x+")]['display'] + "  \\          /" + "\n" +
#line 52
(" " * 45) + "\\         /" + (" " * 27) + "\\" + "        " + "/" + "\n" +
#line 53
(" " * 46) + "\\       /      " + grid.roads['wz']['display'] + "               " + grid.roads[quick_reorder("x+")]['display'] + "      " + "\\" + "      " + "/" + "\n" +
#line 54
(" " * 45) + "2:1 ore port     " + grid.roads['wz']['display'] + grid.settlement_locs["z"]["display"] + " " + (grid.roads["+z"]['display'] + " ") * 4 + grid.settlement_locs["+"]["display"] 
+ "      3:1 port"

        )

        quick_grid_access = [grid_part_1, grid_part_2, grid_part_3, grid_part_4]

        for grid in quick_grid_access:
                print(grid, end="")
        print("\n")


def check(text : str, grid : Grid, player_info : PlayerInfo, mode : str) -> bool:
        """Checks if the settlement/road is eligible to be claimed"""

        valid = True 

        if mode == 'settlement':
                settlement = text
                try:
                        if grid.settlement_locs[settlement]['owner'] != 0:
                                print("This settlement is already taken. Pro tip: if it has a colour, it's not up for grabs.")
                                valid = False
                                
                        else:
                                related_roads = []
                                for road in grid.roads:
                                        if settlement in road:
                                                related_roads.append(road)
                                
                                related_settlements = []
                                for road in related_roads:
                                        for place in road:
                                                if place != settlement:
                                                        related_settlements.append(place)

                                for place in related_settlements:
                                        if grid.settlement_locs[place]['owner'] != 0:
                                                print(f"It looks like you're trying to place a settlement adjacent to another settlement, 'location {place}'. You must place it at least two roads away.")
                                                valid = False
                                                break
        
                except KeyError:
                        if settlement in grid.settlement_locs:
                                valid = True
                        else:
                                print("That settlement doesn't exist.")
                                valid = False

                if player_info.game_mode != "initial":
                        case = []
                        for road in grid.roads:
                                if settlement in road:
                                        if grid.roads[road]['owner'] != 0:
                                                owner = grid.roads[road]['owner']
                                                if owner == player_info.player_turn:
                                                        case.append(road)

                        if len(case) != 0:
                                print("Congratulations on obtaining a new settlement.")
                        else:
                                print("You can only build next to a road that you own. Sorry.")
                                valid = False


        elif mode == 'road':

                try:
                        text = quick_reorder(text)
                except IndexError:
                        pass

                if text not in grid.roads:
                        valid = False
                        print("That road doesn't exist.")

                else:      
                        owner = grid.roads[text]['owner']
                        if owner != player_info.player_turn and grid.roads[text]['owner'] != 0:
                                print("That road already belongs to someone else.")
                                valid = False         
                        case = []
                        for settlement in text:
                                if grid.settlement_locs[settlement]['owner'] != 0:
                                        owner = grid.settlement_locs[settlement]['owner']
                                        if player_info.player_turn == owner:
                                                case.append(settlement)

                                for road in grid.roads:
                                        if settlement in road:
                                                owner = grid.settlement_locs[settlement]['owner']
                                                if player_info.player_turn == owner:
                                                        case.append(road)
                                                        
                                for road in player_info.player_dicts[player_info.player_turn]["roads"]:
                                        for char in road:
                                                if char in text:
                                                        case.append(road)
                        
                        if valid != False and len(case) != 0:
                                print("Congratulations on paving a new road.")
                        else:
                                print("You don't own any settlements/roads next to that road, so you can't build it. Sorry.")
                                valid = False

        return valid


def rolled_a_seven(grid : Grid, player_info : PlayerInfo, game_bank : dict):
        """Makes the player place the robber somewhere else and players over 7 cards to discard half their hand size."""
        
        grid.robber = place_robber(grid)
        halve_decks(player_info, game_bank)
        
        return grid.robber
        
        
def halve_decks(player_info : PlayerInfo, game_bank : dict):
        """Makes greedy players discard half their hand"""
        
        for player in player_info.quick_key:
                hand_size = calculate_hand_size(player_info.player_dicts, player)
                if hand_size >= 8:
                        print(f"Player {player} has too many cards. You must discard half your deck.")
                        
                        valid = False
                        while not valid:
                                print(f"Please turn your screen away. Player {player}, it is mandatory that you complete this stage.\nDo not attempt to skip the entering of your password.")
                                valid = check_password(player, player_info)
                                
                        needed_size = hand_size // 2
                        while hand_size > needed_size:
                                player_info, game_bank = discard_resource(player_info, game_bank, player)
                                
                                hand_size = calculate_hand_size(player_info.player_dicts, player)
                                if hand_size > needed_size:
                                        print(f"You are still {hand_size - needed_size} cards above the number you are allowed.")                
                        
        return player_info, game_bank


def calculate_hand_size(player_dicts : dict, player : int) -> int:
        """Calculates the hand size of the given player"""
        
        hand_size = 0
        for resource in player_dicts[player]['resources']:
                hand_size += player_dicts[player]['resources'][resource]
                
        return hand_size
                

def discard_resource(player_info : PlayerInfo, game_bank : dict, player : int):
        """Discards resources"""
        
        resource = input("Which resource would you like to discard?\n˚₊ · »-♡→ ").strip().lower()
        if resource in player_info.player_dicts[player]['resources']:
                if player_info.player_dicts[player]['resources'][resource] == 0:
                        print("You have 0 of that card.")
                else:
                        number = get_discard_number(player_info, resource, player)
                        if number == 'cancel':
                                pass
                        else:
                                player_info.player_dicts[player]['resources'][resource] -= number
                                game_bank['resources'][resource] += number
                                
        return player_info, game_bank
                                        
                                                
def get_discard_number(player_info, resource, player):
        valid = False
        while not valid:
                number = input(f"How many of your {resource} would you like to discard? Hint: type 'cancel' to cancel.").strip().lower()
                if number.isdigit():
                        number = int(number)
                        if player_info.player_dicts[player]['resources'][resource] < number:
                                print(f"You only have {player_info.player_dicts[player]['resources'][resource]} {resource}.\nWould you like to type 'check' to view your hand?")
                        else:
                                valid = True
                elif number == 'cancel':
                        valid = True
                else:
                        print("Oops, enter arabic numerals please.")
                        
        
        return number       


def place_robber(grid : Grid):
        error_message = "That tile doesn't exist. Please input as either the arabic numerals following the S or with the S."
        valid = False
        while not valid:
                placement = input("Where would you like to place the robber?\n˚₊ · »-♡→ ")
                
                if placement in grid.tiles.keys():
                        tile = placement
                        proceed = True
                elif placement.isdigit():
                        if int(placement) <= 19:
                                tile = "S" + str(placement)
                                proceed = True
                        else:
                                print(error_message)
                                proceed = False
                else:
                        print(error_message)
                        proceed = False
                               
                if proceed:
                        if grid.robber == tile:
                                print("You can't choose not to move it!")
                                
                        else:
                                grid.robber = tile
                                valid = True
                                
        return grid.robber


def roll_die(player_info : PlayerInfo, grid : Grid, game_bank):
        
        player_dicts = player_info.player_dicts
        
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll = dice_1 + dice_2
        print(f"As everyone watches with bated breath, you roll the die. You pray for a good result. They land as follows: |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}. You've rolled a {roll}.")
        
        if roll == 7:
                print(f"The robber has awakened and will now migrate to a hex of P{player_info.player_turn}'s choosing.")
                grid.robber = rolled_a_seven(grid, player_info, game_bank)
                clear_screen()
                print_board(player_info, grid, game_bank)
                
        for player in player_info.quick_key:
                for settlement, tile in zip(player_dicts[player]["settlements"], grid.tiles):
                        if settlement in grid.tiles[tile]["attached_settlements"]:
                                game_bank, player_info = check_robber(roll, grid, tile, game_bank, player_info, settlement)
                                
        
        return game_bank, player_info


def check_robber(roll : int, grid : Grid, tile : str, game_bank : dict, player_info : PlayerInfo, settlement : str):
        """Checks if robber is occupying the relevant tile; if not, hands out resources."""
        
        if roll == grid.tiles[tile]["number"]:
                if grid.robber != tile:
                        game_bank, player_info = give_resources(grid.tiles[tile]['biome'], game_bank, player_info, settlement)
                else:
                        print(f"The robber has prevented anyone from obtaining resources on {tile}")
                        
        return game_bank, player_info
                        
                                                
def give_resources(resource : str, game_bank : dict, player_info : PlayerInfo, settlement) -> tuple[dict, PlayerInfo]:
        """Assigns relevant resources to relevant players based on their rolls"""
        
        if game_bank['resources'][resource] != 0:
                if settlement != "":
                        print(f"P{player_info.player_turn} has obtained {resource} from their settlement {settlement}.")
                        
                game_bank['resources'][resource] -= 1
                player_info.player_dicts[player_info.player_turn]['resources'][resource] += 1
        else:
                print(f"The bank has run out of {resource}! P{player_info.player_turn} is unable to obtain {resource} from their settlement {settlement}")

        return game_bank, player_info
        

def check_password(player, player_info) -> bool:
        print("Enter your password:")
        valid = False
        while not valid:
                password = input("> ")
                
                if password == player_info.player_dicts[player]["password"]:
                        print("Password is correct. You may allow everyone to see the screen now.")
                        valid = True
                        
                elif password in ['X', 'x']:
                        print("Password was not authenticated.")
                        valid = False
                        break
                        
                else:
                        print("Please try again. You may type 'X' if you cannot remember.")
        
        return valid


def force_password(player_info):
        """Absolutely insists upon receiving the correct password"""
        player = player_info.player_turn
        
        valid = False
        while not valid:
                valid = check_password(player, player_info)
                
def main_game(player_info, grid, game_bank):
        """The main input loop after initial resource setup"""
        
        game = True
        player_info.game_mode = "main"

        while player_info.game_mode == "main" and game:

                for player in player_info.quick_key:
                        if not game:
                                print("Game has ended!")
                                break
                        player_info.player_turn = player
                        turn = True
                        roll_allowed = True
                        while turn:
                                action = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, what's your move?") + "\n˚₊ · »-♡→ ").strip().lower()

                                if action == "end turn":
                                        turn = allow_turn_end(roll_allowed, player_info)

                                elif action == "build":
                                        build(player_info, game_bank)
                                
                                elif action == "trade":
                                        choice = call_trade(player_info, grid, game_bank)
                                        
                                        
                                elif action == "roll":
                                        game_bank, player_info = allow_roll(roll_allowed, player_info, grid, game_bank)
                                        
                                        
                                else:
                                        print("That action doesn't exist.")
                                        
                                                
                        game = check_if_game(calculate_VP(player_info), player_info)
                        clear_screen()
                        print_board(player_info, grid, game_bank)  
                        
        print("Game has ended :)")


def allow_turn_end(roll_allowed : bool, player_info : PlayerInfo) -> bool:
        if not roll_allowed:
                if check_password(player_info.player_turn, player_info):
                        print("Your turn has ended.")
                        turn = False
        else:
                print("You must roll before you can end your turn."
                      )
                
        return turn
        
        
def build(player_info : PlayerInfo, game_bank : dict):

        
        while True:
                action = input("What would you like to build?").strip().lower()
                if action in game_bank['constructs'].keys():
                        if action == 'draw':
                                dev_card_list = list_dev_cards(game_bank)
                                drawn_card, game_bank = draw_dev_card(dev_card_list, game_bank)
                        """check if player has enough of the required materials and prompt if not"""
                elif action == 'check':
                        """print constructs THEY can build. with a numbered list hopefully"""
                elif action == 'mats':
                        """print full building costs list"""
                elif action in ['X', 'cancel']:
                        print("Leaving the construction site...")
                        break
                        
        return player_info, game_bank

def execute_dev_card(dev_card, grid : Grid, player_info : PlayerInfo, game_bank : dict):
        if dev_card == 'knight':
                grid.robber = place_robber(grid)
        elif dev_card == 'build road':
                for i in range(2):
                        print(f"Placing road no.{i + 1} out of your 2 free roads...")
                        player_info, grid = place_road(player_info, grid, game_bank)
        elif dev_card == "year of plenty":
                year_of_plenty()
        elif dev_card == "monopoly":
                monopoly(player_info)
                
def monopoly(player_info):
        pass
                
def year_of_plenty():
        print("You have drawn the year of plenty card and may now choose to take a card from the game bank.")

def something(materials):
        pass

def allow_roll(roll_allowed, player_info, grid, game_bank):
        """Roll die if roll is allowed"""
        
        if roll_allowed:
                game_bank, player_info = roll_die(player_info, grid, game_bank)
                roll_allowed = False
        else:
                print("You've already rolled this turn. You can only roll once per turn.") 
                
        return game_bank, player_info
        

def trade_port(player_info : PlayerInfo, grid : Grid, game_bank : dict) -> tuple[dict, PlayerInfo]:
        """Collects the data needed for port trades and calls the port trade subroutine"""
        
        player_ports = []
        for settlement in player_info.player_dicts[player_info.player_turn]["settlements"]:
                if grid.settlement_locs[settlement]["port"] != "":
                        player_ports.append(grid.settlement_locs[settlement]["port"])
                        
        if player_ports == []:
                print("It seems like you don't have any ports accessible for trade right now. Kindly build a settlement next to the sea.")
                ports = False
        else:
                ports = True
        
        
        if ports:
                ports, port = other_thing(player_ports)      
        
        if ports:
                game_bank, player_info = port_exchange(game_bank, player_info, port)
                
        return game_bank, player_info


def trade_player(player_info : PlayerInfo):
        
        valid = False
        while not valid:
                action = input("Which player would you like to trade with? (Hint: 'x' or 'cancel' to end loop)\n˚₊ · »-♡→ ").strip().lower()
                if action in ["cancel", "x"]:
                        wants_to_trade = False
                        valid = True
                try:
                        action = int(action)
                        if not action in player_info.quick_key:
                                print("That's not an existing player. If you want to exit, please type 'x' or 'cancel'.")
                        elif action == player_info.player_turn:
                                print("You're trying to trade with... yourself?")
                        else:
                                wants_to_trade = True
                                valid = True
                except ValueError:
                        for i in range(len(player_info.quick_key)):
                                if action == player_info.player_dicts[i + 1]["name"]:
                                        if action != player_info.player_turn:
                                                wants_to_trade = True
                                                valid = True
        
        if wants_to_trade == "True":
                """trade_with_player(player_info, action)"""
                
        return player_info


def other_thing(player_ports : list):
        
        loop = True
        while loop:
        
                action = input("Which port would you like to select? (Hint: type 'check' to see what ports are available.)\n˚₊ · »-♡→ ").strip().lower()
                if action in player_ports:
                        port = action
                        loop = False
                        
                elif action == 'check':
                        i = 1
                        print(f"Your port{'s are: ' if len(player_ports) != 1 else ' is: '}")
                        for port in player_ports:
                                print(str(i) + ". " + port, end=", " if port != player_ports[-1] else "\n")
                                i += 1
                                
                else:
                        try:
                                if int(action) <= len(player_ports):
                                        port = player_ports[int(action) - 1]
                                        ports = True
                                        loop = False
                                else:
                                        print("You don't even have that many ports in the first place!")
                        except ValueError:
                                print("That's not an option. Sorry.")
                                
        return ports, port
                                
def port_exchange(game_bank, player_info, port):
        ports = ["wood", "grain", "sheep", "ore", "brick"]
        resource = find_starting_resource(ports, port)
        
        if resource != 'anything':
                if not player_info.player_dicts[player_info.player_turn]['resources'][resource] >= 2:
                        print("You actually don't have enough to trade that resource. You need at least 2.")
                        return game_bank, player_info
                
        print(f"You can trade {'3 of' if resource == 'anything' else '2'} {resource} for a resource of your choosing.?")
        
        offer = {}
        if resource == 'anything':
                print("Choose which resource you'd like to give/put down 3 of to carry out the trade.")
                offer['resource'] = pick_resource(player_info, ports, 'offer')
                if offer['resource'] == 'none':
                        print('Trade canceled')
                        return game_bank, player_info
                else:
                        offer['number'] = 3
        else:
                offer['resource'] = resource
                offer['number'] = 2
                
        
        if player_info.player_dicts[player_info.player_turn]['resources'][offer['resource']] < offer['number']:
                print(f"Looks like you don't have enough {offer['resource']} to make the trade.")
                return game_bank, player_info
        
                
        compensation = {}
        
        print("Please pick which resource you'd like to obtain from the trade.")
        compensation['resource'] = pick_resource(player_info, ports, 'recieve')
        if compensation['resource'] == 'none':
                print("Trade canceled")
                return game_bank, player_info
        else:
                compensation['number'] = pick_number(compensation['resource'])
                if compensation['number'] == 0:
                        return game_bank, player_info
                if game_bank['resources'][compensation['resource']] < compensation['number']:
                        print("The game bank can't afford it. Come back again next time.")
                        return game_bank, player_info
        
        player_info, game_bank = trade(player_info, game_bank, offer, compensation)
        print("Trade successful!")
                
        return game_bank, player_info
   
            
def pick_number(resource):
        """Forces player to pick a number"""
        
        valid = False
        while not valid:
                number = input(f"How many {resource} would you like to recieve?\n˚₊ · »-♡→ ")
                
                if number.isdigit():
                        number = int(number)
                        if number > 0:
                                print(f"Okay, you're trading for {number} {resource}.")
                        if number == 0:
                                print("Looks like you're canceling the trade.")      
                        
                        valid = True
                                
                elif input == 'cancel':
                        print("To cancel, just type in 0.")
                        
                else:
                        print("Please enter arabic numerals. If you want to cancel the trade, just input a 0." + 
                              "Negative numbers are not allowed, by the way.")
        
        return number
       
            
def find_starting_resource(ports, port):
        """Based on the port the player has selected, finds the relevant resource that is being traded"""
        
        if port[0] == "3":
                resource = "anything"
                
        else:
                for attribute in ports:
                        for character in attribute:
                                if character.isalpha():
                                        first_letter = character
                                        break
                        if first_letter == port[0]:
                                resource = attribute 
                                
        return resource                   
          
          
def player_trade(player_info : PlayerInfo):
        pass
 
        
def trade(player_info : PlayerInfo, game_bank : dict, offer : dict, compensation : dict) -> tuple[PlayerInfo, dict]:
        
        player = player_info.player_turn
        player_info.player_dicts[player]['resources'][offer['resource']] -= offer['number']
        game_bank['resources'][offer['resource']] += offer ['number']
        
        player_info.player_dicts[player]['resources'][compensation['resource']] += compensation['number']
        game_bank['resources'][compensation['resource']] -= compensation['number']
        
        return player_info, game_bank
 
          
def pick_resource(player_info, resources : list, mode : str) -> str:
        
        resources_with_numbers = {}
        i = 1
        for resource in resources:
                resources_with_numbers[str(i)] = resource
                i += 1
        loop = True
        while loop:
                action = input("Which resource would you like to select? (Hint: type 'check' to view the available resources)\n˚₊ · »-♡→ ").strip().lower()
                
                if action in resources:
                        resource = action
                        loop = False
                elif action in resources_with_numbers:
                        resource = resources_with_numbers[action]
                        loop = False
                elif action == "check":
                        print("The possible resources available to you are:")
                        for key in resources_with_numbers:
                                print(key, f". {resources_with_numbers[key]}")
                elif action == 'cancel':
                        resource = "none"
                        loop = False
                else:
                        print("Invalid. (Hint: type 'cancel' to cancel!)")
        
        return resource
        

def call_trade(player_info : PlayerInfo, grid : Grid, game_bank : dict):
        
        valid = False
        while not valid:
                choice = input("Would you like to trade at 1. a port, or 2. with a player?\n˚₊ · »-♡→ ").strip().lower()
                if choice in ["1", "port"]:
                        game_bank, player_info = trade_port(player_info, grid, game_bank)
                        valid = True

                elif choice in ["2", "player"]:
                        player_info = trade_player(player_info)
                        valid = True
                        
                elif choice in ["cancel", "x"]:
                        valid = True
                
                else:
                        print("Please type in a valid response! If you don't want to anymore, type 'X' or 'cancel'!")
                        
        return player_info, game_bank


def main():    
                        
        associated_settlements = {
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
        
        kaomojis = {
                        "ores": "‧₊˚🗻`",
                        "brick": "↟↟↟↟↟↟",
                        "grain": "˚ʚ🌱₊˚",
                        "wood": " ݁˖𓂃.𖠰.",
                        "sheep": ":3 ^^~", 
                        "desert": " ⛰︎ ོ ༄-"
        }
        
        number_tokens = make_token_list()
        biomes = make_biomes() 

        
        print("Starting your game...")
        time.sleep(1)
        clear_screen()
        quick_key, player_dicts = initialise_player_dicts()
        game_bank = make_bank()
        tiles, robber, settlement_locs, roads = generate_grid(biomes, number_tokens, associated_settlements)
        
        grid = Grid(robber, tiles, settlement_locs, roads, kaomojis, biomes)
        player_info = PlayerInfo(game_bank, quick_key, player_dicts)
        
        clear_screen()
        player_info, grid, game_bank = initial_loop(player_info, grid, game_bank)
        main_game(player_info, grid, game_bank)
        


if __name__ == "__main__":
        loop = True
        while loop:
                action = input().strip().lower()
                if action == "":
                        print("Welcome to Catan!")
                        main()
                elif action == 'break':
                        break

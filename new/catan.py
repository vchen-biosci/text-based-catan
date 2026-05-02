import random, time, os

class Grid:
        def __init__(self, robber, tiles, settlement_locs, roads, kaomojis):
                self.robber = robber
                self.tiles = tiles
                self.settlement_locs = settlement_locs
                self.roads = roads
                self.kaomojis = kaomojis

class PlayerInfo:
        def __init__(self, game_bank, quick_key, player_dicts):
                self.game_bank = game_bank
                self.quick_key = quick_key
                self.player_dicts = player_dicts
                        
def quick_reorder(road : str):

        if road[0] > road[1]:
                road = road[1] + road[0]

        return road

def clear_screen():
        print("\033c", end="")

def ansi_stitching(color : list, text : str) -> str:
        
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

def get_player_name(player : int, player_names : list) -> str:
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
        player_dicts = {}
        for player in quick_key:
                player_dicts[player] = {}
                
        return player_dicts

def get_player_password() -> str:
        valid_password = False
        while not valid_password:
                password = input("Please enter a password; it'll be used to check for your consent later. Keep it short but memorable, and make sure it's not a password you use for important sites.\n> ")
                if len(password) > 7:
                        print("That password is way too long. Keep it to 7 or below characters.")
                else:
                        valid_password = True
        
        return password

def setup_player_dicts(quick_key : list) -> dict:
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
                quick_dict = dict(zip(["knight", "year of plenty", "road building", "monopoly", "VPs"], [14, 2, 2, 2, 5]))
                for dev_card in quick_dict:
                        player_dicts[player]["dev_cards"][dev_card] = quick_dict[dev_card]
                        
                player_dicts = add_keys(player_dicts, quick_key)
                clear_screen()
                
        print_names(player_names, quick_key)
        return player_dicts

def print_names(player_names, quick_key):
        print("Okay; your names are: ")
        for player in quick_key:
                if player == quick_key[-1]:
                        print(player_names[player - 1], end=".\n")
                elif player == quick_key[-2]:
                        print(player_names[player - 1], end=", and ")
                else:
                        print(player_names[player - 1], end=", ")

def add_keys(player_dicts, quick_key) -> dict:
        for player in quick_key:
                player_dicts[player]['roads'] = []
                player_dicts[player]['settlements'] = []
                player_dicts[player]['cities'] = []
                player_dicts[player]['construct_bank'] = {"settlements": 5, "cities": 4, "roads": 15}
                player_dicts[player]['achievements'] = {"longest road" : 0, "largest army" : 0}
                player_dicts[player]['knights_recruited'] = 0
                player_dicts[player]['VPs'] = 0
        return player_dicts
               
def initialise_player_dicts() -> tuple[list, int, dict]:
        player_number = get_player_number()
        quick_key = create_player_key(player_number)
        player_dicts = setup_player_dicts(quick_key)
        player_colors = assign_player_colors(quick_key)
        for player, color in zip(player_dicts, player_colors):
                player_dicts[player]["color"] = color
        
        return quick_key, player_number, player_dicts

def print_rules():
        print("""This is the link to the official Catan Almanac:
https://www.catan.com/sites/default/files/2024-01/Almanac%20CATAN-3D.pdf
If the link doesn't work, please paste it into your browser.""")

def choose_color() -> list:
        player_color = []
        satisfied = False
        while not satisfied:
                for color in ["red", "blue", "green"]:                  
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

        clear_screen()
        return player_color

def assign_player_colors(quick_key : list) -> list:
        preset_colors = [[1, 201, 184], [252, 210, 1], [252, 84, 1], [210, 1, 252]]
        player_colors = []
        for player in quick_key:
                action = ""
                while not action in ["y", "n"]:
                        action = input("Would you like to customise your own color? (If not, you'll get a premade one!)" + 
                                       " Type 'Y' for yes and 'N' for no.").strip().lower()
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
        for player in quick_key:
                print(ansi_stitching(player_colors[player - 1], f"Player {player}, this is your color."))
                time.sleep(0.3)

def initialise_resource_cards() -> tuple[dict, dict]:
        
        resources = {}
        for resource in ["ores", "grain", "wood", "brick", "sheep"]:
                resources[resource] = 19
        dev_bank = {}
        dev_cards = ["knight", "year of plenty", "road building", "monopoly", "VPs"]
        dev_values = [14, 2, 2, 2, 5]
        for dev_card, value in zip(dev_cards, dev_values):
                dev_bank[dev_card] = value
        
        return resources, dev_bank
                
def make_bank() -> dict:
        game_bank = {}
        resources, dev_bank = initialise_resource_cards()
        game_bank['resources'] = resources
        game_bank['dev_cards'] = dev_bank
        
        return game_bank

def create_tiles() -> dict:
        print("Setting up your tiles...")
        tiles = {}
        for i in range(19):
                tiles[("S"+str(i+1))] = {}
                
        return tiles

def place_desert(tiles : dict) -> tuple[dict, str]:
        print("Spawning your desert...")
        desert_placement = random.randint(1, 19)
        tiles[("S"+str(desert_placement))]["biome"] = "desert"
        tiles[("S"+str(desert_placement))]["number"] = "NA"
        robber = "S"+str(desert_placement)
        
        return tiles, robber
        
def generate_grid(biomes : list, number_tokens : list, associated_settlements : dict) -> tuple[dict, str, dict, dict]:
        settlement_locations = "abcdefghijklmnopqrstuvwxyz".upper()
        settlement_locations += settlement_locations.lower() + "+" + "$"
        
        tiles = create_tiles()
        tiles, robber = place_desert(tiles)
        tiles = assign_tile_variables(tiles, biomes, number_tokens, associated_settlements)
        
        settlement_locs = assign_ports(settlement_locations)
        roads = create_roads()
        
        return tiles, robber, settlement_locs, roads
        
def create_roads() -> dict:
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
        number_tokens = []
        for i in range(10):
                if (i + 2) != 7:
                        for x in range(2):
                                number_tokens.append(i + 2)
        number_tokens.append(1)
        number_tokens.append(12)
        
        return number_tokens

def print_board(player_info : PlayerInfo, grid : Grid, game_bank : dict):
        print("________ WELCOME TO THE WORLD OF CATAN. WHERE WILL YOU SETTLE TODAY? ________\n")
        print(f"GAME BANK:")
        for resource in game_bank["resources"]:
                print(f'{resource} : {game_bank["resources"][resource]}', end="  ||  ")
        print("\n")
        for dev_card in game_bank['dev_cards']:
                print(f'{dev_card} : {game_bank["dev_cards"][dev_card]}', end="  ||  ")
        print("\n")
        for player in player_info.quick_key:
                print(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player} ({player_info.player_dicts[player]['name']})"), end="  ||  ")
        print("\n")
        print_grid(grid.settlement_locs, grid.roads, grid.tiles, grid.kaomojis)
        print(f"The robber is currently pillaging the citizens of {grid.robber} and stealing all their {grid.tiles[grid.robber]['biome']}...")
        
def initial_loop(player_info : PlayerInfo, grid : Grid, game_bank : dict) -> tuple[PlayerInfo, Grid, dict]:
        
        game_mode = "initial"
        player_turn = 1 

        print_board(player_info, grid, game_bank)
        print(f"We'll go from player 1 to player {len(player_info.quick_key)}; you can place two settlements and two roads for free. Please choose wisely.")
        for i in range(2):
                for player in player_info.quick_key:
                        player_turn = player
                        valid = False
                        while not valid:
                                text = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, where would you like to place your settlement?") + "\n> ").strip()
                                valid = check(text, grid.settlement_locs, grid.roads, 'settlement', player_turn, 'initial', player_info.player_dicts)
                        player_info.player_dicts[player]['settlements'].append(text)
                        print(grid.settlement_locs[text]['display'])
                        grid.settlement_locs[text]['display'] = ansi_stitching(player_info.player_dicts[player]['color'], grid.settlement_locs[text]['display'])
                        grid.settlement_locs[text]['owner'] = player
                        clear_screen()
                        print_board(player_info, grid, game_bank)

                        valid = False
                        while not valid:
                                text = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, where are you placing your road?") + "\n> ").strip()
                                valid = check(text, grid.settlement_locs, grid.roads, 'road', player_turn, "initial", player_info.player_dicts)
                        player_info.player_dicts[player]['roads'].append(text)
                        grid.roads[quick_reorder(text)]['display'] = ansi_stitching(player_info.player_dicts[player]['color'], grid.roads[quick_reorder(text)]['display'])
                        clear_screen()
                        print_board(player_info, grid, game_bank)

        player_turn = 1
                        
        return player_info, grid, game_bank

def print_grid(settlement_locs : dict, roads : dict, tiles : dict, kaomojis : dict):

        grid_part_1 = (
#line 1
(" " * 65) + "3: 1 port" + "\n" +
#line 2
(" " * 65) + "/      \\" + "\n" +
#line 3
(" " * 64) + "/        \\" + "\n" +
#line 4
(" " * 20) + "sea" + (" " * 38) + settlement_locs["A"]["display"] + " " + (roads["AB"]["display"] + " ") * 4 + settlement_locs["B"]["display"] + (" " * 38) + "sea" + "\n" +
#line 5
(" " * 61) + roads["AD"]["display"] + "              " + roads["BE"]['display'] + "\n" +
#line 6 & 7
(" " * 60) + roads["AD"]['display'] + "                " + roads["BE"]['display'] + "\n\n" +
#line 8
(" " * 35) + ("2:1 grain port") + (" " * 9) + roads["AD"]['display'] + (" " * 7) + kaomojis[tiles["S1"]["biome"]] + (" "* 7) + roads["BE"]['display'] + (" " * 16) + "3:1 port" + "\n" +
#line 9
(" " * 36) + "|    " + "\\" + "   " + (roads["CD"]['display'] + " ") * 4 + roads["AD"]['display'] + (" " * 10) + str(tiles["S1"]["number"]) 
+ (" " * 11 if len(str(tiles["S1"]["number"])) == 1 else " " * 10) + roads["BE"]['display'] + " " + (roads["EF"]['display'] + " ") * 4 + "   /  |\n" +
#line 10
(" " * 36) + "|" + (" " * 3) + settlement_locs["C"]["display"] + " " + roads["CG"]['display'] + (" " * 11) + settlement_locs["D"]["display"] + "  " + roads["DH"]['display']
+ (" " * ((22 - len(str(tiles["S1"]["biome"])))//2)) + tiles["S1"]["biome"] +
(" " * (((22-len(str(tiles["S1"]["biome"])))//2)+ (1 if len(str(tiles["S1"]["biome"]))%2 != 0 else 0)))
+ roads["EI"]['display'] + " " + settlement_locs["E"]["display"] + (" " * 8) + settlement_locs["F"]["display"] + "  " + roads["FJ"]['display'] + "     |\n" +
#line 11
(" " * 36) + "|" + "    " + roads["CG"]['display'] +  (" " * 16) + roads["DH"]['display'] + (" " * 9) + "S1" + (" " * 9) + roads["EI"]['display'] + (" " * 15) + 
roads["FJ"]['display'] + "    |" + "\n" +
#line 12
(" " * 36) + "|" + (" " * 63) + "|" + "\n" +
#line 13
(" " * 36) + "|" + "  " + roads["CG"]['display'] + (" " * 7) + kaomojis[tiles["S2"]["biome"]] + (" " * 7) + roads["DH"]['display'] 
+ (" " * 16) + roads["EI"]['display'] + " "  + (" " * 6) + (kaomojis[tiles["S3"]["biome"]]) 
+ (" " * 6) + roads["FJ"]['display'] +"  |\n" +
#line 14
(" " * 21) + settlement_locs["$"]["display"] + " " + (roads[quick_reorder("G$")]['display'] + " ") * 4 + settlement_locs["G"]["display"] + "  " + roads["CG"]['display'] + (" " * 10) + str(tiles["S2"]["number"]) + 
(" " * 9 if len(str(tiles["S2"]["number"])) == 1 else " " * 8) + settlement_locs["H"]["display"] + " " + roads["DH"]['display'] + " " + (roads["HI"]['display'] + " ") * 4 + " " + roads["EI"]['display'] + " " + settlement_locs["I"]["display"] +
(" " * 8) + str(tiles["S3"]["number"]) + (" " * 8 if len(str(tiles["S3"]["number"])) == 1 else " " * 7) + settlement_locs["J"]["display"] + " " + roads["FJ"]['display'] + " | " + (roads["JK"]['display'] + " ") * 4 
+ settlement_locs["K"]["display"] + "\n" +
#line 15
(" " * 21) + roads[quick_reorder("L$")]['display'] + (" " * 16) + roads["GM"]['display'] + (" " * ((22 - len(str(tiles["S2"]["biome"])))//2)) + tiles["S2"]["biome"] + (" " * 9 if tiles["S2"]["biome"] != "desert" else " " * 8)
+ roads["HN"]['display'] + (" " * 14) + roads["IO"]['display'] + (" " * ((21 - len(str(tiles["S3"]["biome"])))//2)) + tiles["S3"]["biome"] + (" " * ( (21 - len(tiles["S3"]["biome"])) //2   ) ) + 
(" " * (1 if len(tiles["S3"]["biome"]) % 2 != 1 else 0)) + roads["JP"]['display'] + (" " * 14) + roads["KQ"]['display'] + "\n" +
#line 16 & 17 
(" " * 20) + roads[quick_reorder("L$")]['display'] + (" " * 18) + roads["GM"]['display'] + (" " * 9) + "S2" + (" " * 9) + roads["HN"]['display'] + (" " * 16) + roads["IO"]['display'] + (" " * 8) + "S3" + (" " * 9) + roads["JP"]['display'] + 
(" " * 16) + roads["KQ"]['display'] + "\n\n" +
#line 18
(" " * 18) + roads[quick_reorder("L$")]['display'] + (" " * 8) + kaomojis[tiles["S4"]["biome"]] + (" " * 8) + roads["GM"]['display'] + (" " * 16) + roads["HN"]['display'] + (" " * 7) + 
kaomojis[tiles["S5"]["biome"]] + (" " * 7) + roads["IO"]['display']
+ (" " * 15) + roads["JP"]['display'] + (" " * 7) + kaomojis[tiles["S6"]["biome"]] + (" " * 7) + roads["KQ"]['display'] + "\n" + 
#line 19
(" " * 15) + settlement_locs["L"]["display"] + " " + roads[quick_reorder("L$")]['display'] + (" " * 11) + str(tiles["S4"]["number"]) + (" " * (10 if len(str(tiles["S4"]["number"])) == 1 else 9)) + settlement_locs["M"]["display"] +
" " + roads["GM"]['display'] + "  " + (roads["MN"]['display'] + " ") * 4 + roads["HN"]['display'] + settlement_locs["N"]["display"] + (" " * 9) + str(tiles["S5"]["number"]) + (" " * 9 if len(str(tiles["S5"]["number"])) == 1 else " " * 8) + settlement_locs["O"]["display"] +
" " + roads["IO"]['display'] + " " + (roads["OP"]['display'] + " ") * 4 + roads["JP"]['display'] + " " + settlement_locs["P"]["display"] + (" " * 8) + str(tiles["S6"]["number"]) + (" " * 11 if len(str(tiles["S6"]["number"])) == 1 else " " * 10) + roads["KQ"]['display']
+ " " + settlement_locs["Q"]["display"] + "\n"
)

        grid_part_2 = (
#line 20
(" " * 17) + roads["LR"]['display'] + (" " * ((24 - len(str(tiles["S4"]["biome"])))//2)) + tiles["S4"]["biome"] + (" " * 10 if tiles["S4"]["biome"] != "desert" else " " * 9) + roads["MS"]['display'] + (" " * 14) + roads["NT"]['display'] +
(" " * ((22 - len(str(tiles["S5"]["biome"])))//2)) + tiles["S5"]["biome"] + (" " * 9 if tiles["S5"]["biome"] != "desert" else " " * 8) + roads["OU"]['display'] + (" " * 13) + roads["PV"]['display'] +
(" " * ((22 - len(str(tiles["S6"]["biome"])))//2)) + tiles["S6"]["biome"] + (" " * 9 if tiles["S6"]["biome"] != "desert" else " " * 8) + roads["QW"]['display'] + "\n" +
#line 21 & 22
(" " * 18) + roads["LR"]['display'] + (" " * 10) + "S4" + (" " * 10) + roads["MS"]['display'] + (" " * 16) + roads["NT"]['display'] + (" " * 9) + "S5" + (" " * 9) + roads["OU"]['display'] + (" " * 15) + roads["PV"]['display'] 
+ (" " * 9) + "S6" + (" " * 9) + roads["QW"]['display'] + "\n\n" +
#line 23
(" " * 20) + roads["LR"]['display'] + (" " * 18) + roads["MS"]['display'] + (" " * 7) + kaomojis[tiles["S7"]["biome"]] + (" " * 7) + roads["NT"]['display'] + (" " * 16) + roads["OU"]['display'] + (" " * 7) + kaomojis[tiles["S8"]["biome"]]  + (" " * 6) + roads["PV"]['display'] +
(" " * 16) + roads["QW"]['display'] + "\n" +
#line 24
(" " * 3) + "2:1 wood port - " + settlement_locs["R"]["display"] + " " + roads["LR"]['display'] + "  " + (roads["RS"]['display'] + " ") * 4 + settlement_locs["S"]["display"] + " " + roads["MS"]['display'] + (" " * 10) + str(tiles["S7"]["number"]) + 
(" " * 8 if len(str(tiles["S7"]["number"])) == 1 else " " * 7) + settlement_locs["T"]["display"] + "  " + roads["NT"]['display'] + "  " + (roads["TU"]['display'] + " ") * 4 + roads["OU"]['display'] + " " + settlement_locs["U"]["display"] +
(" " * 8) + str(tiles["S8"]["number"]) + (" " * 8 if len(str(tiles["S8"]["number"])) == 1 else " " * 7) + settlement_locs["V"]["display"] + " " + roads["PV"]['display'] + " " + (roads["VW"]['display'] + " ") * 4 + " " + roads["QW"]['display'] + 
settlement_locs["W"]["display"] +  " _ _ _  2:1 sheep port" + "\n" +
#line 25
(" " * 8) + "\\" + (" " * 12) + roads["RX"]['display'] + (" " * 16) + roads["SY"]['display'] + (" " * ((22 - len(str(tiles["S7"]["biome"])))//2)) + tiles["S7"]["biome"] + 
(" " * (((22-len(str(tiles["S7"]["biome"])))//2) + (1 if len(str(tiles["S7"]["biome"]))%2 != 0 else 0))) + roads["TZ"]['display'] + (" " * 14) + roads["Ua"]['display'] +
(" " * ((21 - len(str(tiles["S8"]["biome"])))//2)) + tiles["S8"]["biome"] + 
(" " * (((21-len(str(tiles["S8"]["biome"])))//2) + (1 if len(str(tiles["S8"]["biome"]))%2 != 1 else 0))) + roads["Vb"]['display'] + (" " * 14) + roads["Wc"]['display'] + "         /\n" +
#line 26
(" " * 9) + "\\" + (" " * 10) + roads["RX"]['display'] + (" " * 18) + roads["SY"]['display'] + (" " * 9) + "S7" + (" " * 9) + roads["TZ"]['display'] + (" " * 16) + roads["Ua"]['display'] + (" " * 8) + "S8" + (" " * 9) + 
roads["Vb"]['display'] + (" " * 16) + roads["Wc"]['display'] + "       /" + "\n" +
#line 27
(" " * 10) + "\\" + (" " * 110) + "/" + "\n" +
#line 28
(" " * 11) + "\\" + (" " * 6) + roads["RX"]['display'] + (" " * 8) + kaomojis[tiles["S9"]["biome"]] + (" " * 8) + roads["SY"]['display'] + (" " * 16) + 
roads["TZ"]['display'] + (" " * 6) + kaomojis[tiles["S10"]["biome"]] + (" " * 8) + roads["Ua"]['display']
+ (" " * 15) + roads["Vb"]['display'] + (" " * 7) + kaomojis[tiles["S11"]["biome"]] + (" " * 7) + roads["Wc"]['display'] + "   /" + "\n" +
#line 29
(" " * 12) + "\\  " + settlement_locs["X"]["display"] + " " + roads["RX"]['display'] + (" " * 12) + str(tiles["S9"]["number"]) + 
(" " * 9 if len(str(tiles["S9"]["number"])) == 1 else " " * 8) 
+ settlement_locs["Y"]["display"] + " " + roads["SY"]['display'] + " " + (roads["YZ"]['display'] + " ") * 4 + settlement_locs["Z"]["display"] + 
roads["TZ"]['display'] + (" " * 10) + str(tiles["S10"]["number"]) + (" " * 9 if len(str(tiles["S10"]["number"])) == 1 else " " * 8) + 
settlement_locs["a"]["display"] + " " + roads["Ua"]['display'] + (" " + roads["ab"]['display']) * 4 + settlement_locs["b"]["display"] + roads["Vb"]['display'] +
(" " * 10) + str(tiles["S11"]["number"]) + (" " * 11 if len(str(tiles["S11"]["number"])) == 1 else " " * 10) + roads["Wc"]['display'] + " " + settlement_locs["c"]["display"] + "\n" +
#line 30
(" " * 17) + roads["Xd"]['display'] + (" " * ((24 - len(str(tiles["S9"]["biome"])))//2)) + tiles["S9"]["biome"] + (" " * (((24-len(str(tiles["S9"]["biome"])))//2) + (1 if len(str(tiles["S9"]["biome"]))%2 != 0 else 0))) 
+ roads["Ye"]['display'] + (" " * 14) + roads["Zf"]['display'] + (" " * ((22 - len(str(tiles["S10"]["biome"])))//2)) + tiles["S10"]["biome"] + 
(" " * (((22-len(str(tiles["S10"]["biome"])))//2) + (1 if len(str(tiles["S10"]["biome"]))%2 != 0 else 0))) + roads["ag"]['display'] + (" " * 13) + roads["bh"]['display'] +
(" " * ((22 - len(str(tiles["S11"]["biome"])))//2)) + tiles["S11"]["biome"] + 
(" " * (((22-len(str(tiles["S11"]["biome"])))//2) + (1 if len(str(tiles["S11"]["biome"]))%2 != 0 else 0))) + roads["ci"]['display'] + "\n"
        
        )

        grid_part_3 = (
#line 31 & 32
(" " * 18) + roads["Xd"]['display'] + (" " * 10) + "S9" + (" " * 10) + roads["Ye"]['display'] + (" " * 16) + roads["Zf"]['display'] + (" " * 8) + "S10" + (" " * 9) + roads["ag"]['display'] + (" " * 15) + roads["bh"]['display'] + (" " * 8) + "S11" + (" " * 9) + roads["ci"]['display'] + "\n\n" +
#line 33
(" " * 20) + roads["Xd"]['display'] + (" " * 18) + roads["Ye"]['display'] + (" " * 7) + kaomojis[tiles["S12"]["biome"]] + (" " * 7) + roads["Zf"]['display'] + (" " * 16) + roads["ag"]['display'] + (" " * 6) + kaomojis[tiles["S13"]["biome"]] + (" " * 7) + 
roads["bh"]['display'] + (" " * 16) + roads["ci"]['display']
+ "\n" +
#line 34
(" " * 19) + settlement_locs["d"]["display"] + " " + roads["Xd"]['display'] + "  " + (roads["de"]['display'] + " ") * 4 + settlement_locs["e"]["display"] + " " + roads["Ye"]['display'] + (" " * 10) + 
str(tiles["S12"]["number"]) + (" " * 9 if len(str(tiles["S12"]["number"])) == 1 else " " * 8) + settlement_locs["f"]["display"] + " " + roads["Zf"]['display'] + " " + (roads["fg"]['display'] + " ") * 4 + settlement_locs["g"]["display"] + roads["ag"]['display'] +
(" " * 10) + str(tiles["S13"]["number"]) + (" " * 8 if len(str(tiles["S13"]["number"])) == 1 else " " * 7) + settlement_locs["h"]["display"] + " " + roads["bh"]['display'] + " " + (roads["hi"]['display'] + " ") * 4 + " " + roads["ci"]['display'] + " " 
+ settlement_locs["i"]["display"] + "\n" +
#line 35
(" " * 21) + roads["dj"]['display'] + (" " * 16) + roads["ek"]['display'] + (" " * ((23 - len(str(tiles["S12"]["biome"])))//2)) + tiles["S12"]["biome"] + 
(" " * (((21-len(str(tiles["S12"]["biome"])))//2) + (1 if len(str(tiles["S12"]["biome"]))%2 != 1 else 0))) + roads["fl"]['display'] + (" " * 14) + roads["gm"]['display']
+ (" " * ((21 - len(str(tiles["S13"]["biome"])))//2)) + tiles["S13"]["biome"] + 
(" " * (((21-len(str(tiles["S13"]["biome"])))//2) + (1 if len(str(tiles["S13"]["biome"]))%2 != 1 else 0))) + roads["hn"]['display'] + (" " * 14) + roads["io"]['display'] + "\n" +
#line 36 & 37
(" " * 20) + roads["dj"]['display'] + (" " * 18) + roads['ek']['display'] + (" " * 8) + "S12" + (" " * 9) + roads['fl']['display'] + (" " * 16) + roads['gm']['display'] + (" " * 8) + "S13" + (" " * 8) + roads['hn']['display'] + (" " * 16) + roads['io']['display'] + "\n\n" +
#line 38 
(" " * 18) + roads['dj']['display'] + (" " * 8) + kaomojis[tiles["S14"]["biome"]] + (" " * 8) + roads['ek']['display'] + (" " * 16) + roads['fl']['display'] + 
(" " * 7) + kaomojis[tiles["S15"]["biome"]] + (" " * 7) + roads['gm']['display'] + (" " * 15) + roads['hn']['display'] + (" " * 7) + kaomojis[tiles["S16"]["biome"]] + (" " * 7)
+ roads['io']['display'] + "\n" +
#line 39
(" " * 15) + settlement_locs["j"]["display"] + " " + roads['dj']['display'] + (" " * 11) + str(tiles["S14"]["number"]) + (" " * 10 if len(str(tiles["S14"]["number"])) == 1 else " " * 9) + settlement_locs["k"]["display"]
+ " " + roads['ek']['display'] + " " + (roads["kl"]['display'] + " ") * 4 + settlement_locs["l"]["display"] + roads['fl']['display'] + (" " * 10) + str(tiles["S15"]["number"]) + (" " * 9 if len(str(tiles["S15"]["number"])) == 1 else " " * 8)
+ settlement_locs["m"]["display"] + " " + roads['gm']['display'] + " " + (roads["mn"]['display'] + " ") * 4 + roads['hn']['display'] + settlement_locs["n"]["display"] + (" " * 9) + str(tiles["S16"]["number"]) + 
(" " * 11 if len(str(tiles["S16"]["number"])) == 1 else " " * 10) + roads['io']['display'] + " " + settlement_locs["o"]["display"] + "\n" +
#line 40
(" " * 17) + roads['jp']['display'] + (" " * ((24 - len(str(tiles["S14"]["biome"])))//2)) + tiles["S14"]["biome"] +
(" " * (((24-len(str(tiles["S14"]["biome"])))//2) + (1 if len(str(tiles["S14"]["biome"]))%2 != 0 else 0))) + roads['kq']['display'] + (" " * 14) + roads['lr']['display'] +
(" " * ((22 - len(str(tiles["S15"]["biome"])))//2)) + tiles["S15"]["biome"] + 
(" " * (((22-len(str(tiles["S15"]["biome"])))//2) + (1 if len(str(tiles["S15"]["biome"]))%2 != 0 else 0))) + roads['ms']['display'] + (" " * 13) + roads['nt']['display'] +
(" " * ((22 - len(str(tiles["S16"]["biome"])))//2)) + tiles["S16"]["biome"] + 
(" " * (((22 - len(str(tiles["S16"]["biome"])))//2) + (1 if len(str(tiles["S16"]["biome"]))%2 != 0 else 0))) + roads['ou']['display'] + "\n" +
#line 41 
(" " * 14) + "/" + (" " * 3) + roads['jp']['display'] + (" " * 9) + "S14"  + (" " * 10) + roads['kq']['display'] + (" " * 16) + roads['lr']['display'] + (" " * 8) + "S15" + (" " * 9) + roads['ms']['display'] 
+ (" " * 15) + roads['nt']['display'] + (" " * 8) + "S16" + (" " * 9) + roads['ou']['display'] + 
(" " * 3) + "\\" + "\n" +
#line 42
(" " * 13) + "/" + (" " * 107) + "\\" + "\n" 
                )

        grid_part_4 = (
#line 43
(" " * 12) + "/" + (" " * 7) + roads['jp']['display'] + (" " * 18) + roads['kq']['display'] + (" " * 7) + kaomojis[tiles["S17"]["biome"]] + 
(" " * 7) + roads['lr']['display'] + (" " * 16) + roads['ms']['display'] + (" " * 6) + kaomojis[tiles["S18"]["biome"]] + (" " * 7)
+ roads['nt']['display'] + (" " * 16) + roads['ou']['display'] + (" " * 7) + "\\" + "\n" +
#line 44
" 2:1 brick port _  " + settlement_locs["p"]["display"] + " " + roads['jp']['display'] + " " + (roads["pq"]['display'] + " ") * 4 + " " 
+ settlement_locs["q"]["display"] + " " + roads['kq']['display'] + (" " * 11) + str(tiles["S17"]["number"]) +
(" " * 8 if len(str(tiles["S17"]["number"])) == 1 else " " * 7) + settlement_locs["r"]["display"] + " " + roads['lr']['display'] + " " + 
(roads["rs"]['display'] + " ") * 4 + settlement_locs["s"]["display"] + roads['ms']['display'] + (" " * 10) + 
str(tiles["S18"]["number"]) + (" " * 8 if len(str(tiles["S18"]["number"])) == 1 else " " * 7) + settlement_locs["t"]["display"] + " " + roads['nt']['display'] + 
" " + (roads["tu"]['display'] + " ") * 4 + " " + roads['ou']['display'] +
settlement_locs["u"]["display"] + "  _ _ 3:1 port" + "\n" +
#line 45
(" " * 38) + roads['qv']['display'] + (" " * ((22 - len(str(tiles["S17"]["biome"])))//2)) + tiles["S17"]["biome"] + 
(" " * (((22 - len(str(tiles["S17"]["biome"])))//2) + (1 if len(str(tiles["S17"]["biome"]))%2 != 0 else 0))) + roads['rw']['display'] + (" " * 14) + roads['sx']['display'] +
(" " * ((21 - len(str(tiles["S18"]["biome"])))//2)) + tiles["S18"]["biome"] + (" " * (((21 - len(str(tiles["S18"]["biome"])))//2) 
+ (1 if len(str(tiles["S18"]["biome"]))%2 != 1 else 0))) + roads['ty']['display'] + "\n" +
#line 46 & 47
(" " * 39) + roads['qv']['display'] + (" " * 8)  + "S17" + (" " * 9) + roads['rw']['display'] + (" " * 16) + roads['sx']['display'] + 
(" " * 8) + "S18" + (" " * 8) + roads['ty']['display'] + "\n\n" +
#line 48
(" " * 41) + roads['qv']['display'] + (" " * 16) + roads['rw']['display'] + (" " * 7) + kaomojis[tiles["S19"]["biome"]] + (" " * 7) + 
roads['sx']['display'] + (" " * 15) + roads['ty']['display'] + "\n" +
#line 49
(" " * 42) + roads['qv']['display'] + settlement_locs["v"]["display"] + " " + (roads["vw"]['display'] + " ") * 4 + settlement_locs["w"]["display"] + 
(" " * 10) + str(tiles["S19"]["number"]) + (" " * 9 if len(str(tiles["S19"]["number"])) == 1 else " " * 8) + settlement_locs["x"]["display"] + " " + 
roads['sx']['display'] + " " + (roads["xy"]['display'] + " ") * 4 + roads['ty']['display'] + " " 
+ settlement_locs["y"]["display"] + "\n" +
#line 50
(" " * 58) + roads['wz']['display'] +(" " * ((21 - len(str(tiles["S19"]["biome"])))//2)) + tiles["S19"]["biome"] + 
(" " * (((21 - len(str(tiles["S19"]["biome"])))//2) + (1 if len(str(tiles["S19"]["biome"]))%2 != 1 else 0))) + roads[quick_reorder("x+")]['display'] + "\n" +
#line 51
(" " * 44) + "\\" + (" " * 11) + "/  " + roads['wz']['display'] + (" " * 8) + "S19" + (" " * 8) + roads[quick_reorder("x+")]['display'] + "  \\          /" + "\n" +
#line 52
(" " * 45) + "\\         /" + (" " * 27) + "\\" + "        " + "/" + "\n" +
#line 53
(" " * 46) + "\\       /      " + roads['wz']['display'] + "               " + roads[quick_reorder("x+")]['display'] + "      " + "\\" + "      " + "/" + "\n" +
#line 54
(" " * 45) + "2:1 ore port     " + roads['wz']['display'] + settlement_locs["z"]["display"] + " " + (roads["+z"]['display'] + " ") * 4 + settlement_locs["+"]["display"] 
+ "      3:1 port"

        )

        quick_grid_access = [grid_part_1, grid_part_2, grid_part_3, grid_part_4]

        for grid in quick_grid_access:
                print(grid, end="")
        print("\n")

def check(text, settlement_locs : dict, roads, mode, player_turn, game_mode, player_dicts):

        valid = True 

        if mode == 'settlement':
                settlement = text
                try:
                        if settlement_locs[settlement]['owner'] != 0:
                                print("This settlement is already taken. Pro tip: if it has a colour, it's not up for grabs.")
                                valid = False
                                
                        else:
                                related_roads = []
                                for road in roads:
                                        if settlement in road:
                                                related_roads.append(road)
                                
                                related_settlements = []
                                for road in related_roads:
                                        for place in road:
                                                if place != settlement:
                                                        related_settlements.append(place)

                                for place in related_settlements:
                                        if settlement_locs[place]['owner'] != 0:
                                                print(f"It looks like you're trying to place a settlement adjacent to another settlement, 'location {place}'. You must place it at least two roads away.")
                                                valid = False
                                                break
        
                except KeyError:
                        if settlement in settlement_locs:
                                valid = True
                        else:
                                print("That settlement doesn't exist.")
                                valid = False

                if game_mode != "initial":
                        case = []
                        for road in roads:
                                if settlement in road:
                                        if roads[road]['owner'] != 0:
                                                owner = roads[road]['owner']
                                                if owner == player_turn:
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

                if text not in roads:
                        valid = False
                        print("That road doesn't exist.")

                else:      
                        owner = roads[text]['owner']
                        if owner != player_turn and roads[text]['owner'] != 0:
                                print("That road already belongs to someone else.")
                                valid = False         
                        case = []
                        for settlement in text:
                                if settlement_locs[settlement]['owner'] != 0:
                                        owner = settlement_locs[settlement]['owner']
                                        if player_turn == owner:
                                                case.append(settlement)

                                for road in roads:
                                        if settlement in road:
                                                owner = settlement_locs[settlement]['owner']
                                                if player_turn == owner:
                                                        case.append(road)
                                                        
                                for road in player_dicts[player_turn]["roads"]:
                                        for char in road:
                                                if char in text:
                                                        case.append(road)
                        
                        if valid != False and len(case) != 0:
                                print("Congratulations on paving a new road.")
                        else:
                                print("You don't own any settlements/roads next to that road, so you can't build it. Sorry.")
                                valid = False

        return valid

def roll_die(quick_key : list, player_dicts : dict, tiles : dict): #"player_dicts, game_bank"
        
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll = dice_1 + dice_2
        print(f"As everyone watches with bated breath, you roll the die. You pray for a good result. They land as follows: |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}. You've rolled a {roll}.")
        for player in quick_key:
                for settlement in player_dicts[player]["settlements"]:
                        for tile in tiles:
                                if settlement in tiles[tile]["attached_settlements"]:
                                        if roll == tiles[tile]["number"]:
                                                print(f"P{player} has obtained {tiles[tile]['biome']} from settlement {settlement}.")
        
        pass

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
        quick_key, player_number, player_dicts = initialise_player_dicts()
        game_bank = make_bank()
        tiles, robber, settlement_locs, roads = generate_grid(biomes, number_tokens, associated_settlements)
        
        grid = Grid(robber, tiles, settlement_locs, roads, kaomojis)
        player_info = PlayerInfo(game_bank, quick_key, player_dicts)
        
        print_board(player_info, grid, game_bank)
        player_info, grid, game_bank = initial_loop(player_info, grid, game_bank)
        
        """game = True
        while game:
                pass"""

if __name__ == "__main__":
        main()

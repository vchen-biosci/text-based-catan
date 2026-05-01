import random, time, os

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
               
def initialise_player_dicts():
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
        
def generate_grid(biomes : list, number_tokens : list, associated_settlements : dict):
        settlement_locations = "abcdefghijklmnopqrstuvwxyz".upper()
        settlement_locations += settlement_locations.lower() + "+" + "$"
        
        tiles = create_tiles()
        tiles, robber = place_desert(tiles)
        tiles = assign_tile_variables(tiles, biomes, number_tokens, associated_settlements)
        settlement_locs = assign_ports(settlement_locations)
        
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
        number_tokens = make_token_list()
        biomes = make_biomes() 
        
        print("Starting your game...")
        time.sleep(1)
        clear_screen()
        quick_key, player_number, player_dicts = initialise_player_dicts()
        game_bank = make_bank()#get the cleverly named vriable? hahahahahahhaa WERE making bank tiday YES US
        generate_grid(biomes, number_tokens, associated_settlements)

if __name__ == "__main__":
        main()

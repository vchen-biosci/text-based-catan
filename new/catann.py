import random, time

class GameInfo:
    """An object containing future variables that the program may reference"""
    def __init__(self):
        self.resources = ["ores", "grain", "wood", "brick", "sheep"]#this is a constant but it's ugly so I don't want to write it as full caps
   
    
class GameResources:
    def __init__(self):
        pass
   
    
class PlayerInfo:
    """An object containing player information. Pass in when modifying player libraries or info"""
    def __init__(self, game_bank, quick_key, player_dicts):
        self.game_bank = game_bank
        self.quick_key = quick_key
        self.player_dicts = player_dicts
        self.player_turn = 1


class Grid:
    """An object to contain all the important information needed to render the grid or access its variables"""
    def __init__(self, robber, tiles, settlement_locs, roads, biomes):
        self.robber = robber
        self.tiles = tiles
        self.settlement_locs = settlement_locs
        self.roads = roads
        self.kaomojis = {
        "ores": "‧₊˚🗻`",
        "brick": "↟↟↟↟↟↟",
        "grain": "˚ʚ🌱₊˚",
        "wood": " ݁˖𓂃.𖠰.",
        "sheep": ":3 ^^~", 
        "desert": " ⛰︎ ོ ༄-"
}
        self.biomes = biomes


def clear_screen():
    """Clears the screen with ansi code"""
    print("\033c", end="")
    
    
def create_player_info() -> tuple[list, dict]:
    """Obtains player information needed to initialise variables"""
    
    quick_key = create_player_key(get_player_number())
    player_dicts = {}
    player_names = []
    for player in quick_key:
        player_dicts[player] = {}
        name = get_player_name(player, player_names)
        player_dicts[player]['name'] = name
        player_names.append(name)
    
    return quick_key, player_dicts
    
    
def create_player_key(player_number : int) -> list:
    """Creates a key which can be used to iterate through players or find player number"""
    
    #iterates through each player and appends their ID to the quick key
    quick_key = []
    for player in range(player_number):
        quick_key.append(player + 1)
        
    return quick_key

def create_tiles() -> dict:
    """Creates one of each tile in a dictionary of tiles"""
        
    tiles = {}
    for i in range(19):#there are 19 total tiles.
        tiles[("S"+str(i+1))] = {}
                
    return tiles

def place_desert(tiles : dict) -> tuple[dict, str]:
    """The desert and robber are placed on the same random tile"""
        
    print("Spawning your desert...")
    desert = random.randint(1, 19)#the parameters for possible tiles (there are 19)
    tiles[("S"+str(desert))]["biome"] = "desert"
    tiles[("S"+str(desert))]["number"] = "NA"
    robber = "S"+str(desert)

    return tiles, robber


def quick_reorder(road : str):
        """Reorders a 2-letter string based on ascii values (alphabetical order I suppose). 
        This allows me to standardise the way in which roads are called from the dictionary."""

        if road[0] > road[1]:
                road = road[1] + road[0]

        return road


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


def generate_grid(biomes : list, number_tokens : list, associated_settlements : dict) -> tuple[dict, str, dict, dict]:
        """Generates the grid"""
        
        settlement_locations = "abcdefghijklmnopqrstuvwxyz".upper()
        settlement_locations += settlement_locations.lower() + "+" + "$"
        #duplicates it in lowercase as the settlements are denoted alphabetically
        
        tiles = create_tiles()
        tiles, robber = place_desert(tiles)
        number_tokens = make_token_list()
        tiles = assign_tile_variables(tiles, biomes, number_tokens, associated_settlements)
        
        settlement_locs = assign_ports(settlement_locations)
        roads = create_roads()
        
        return tiles, robber, settlement_locs, roads


def assign_ports(settlement_locations : str) -> dict:
    """Assigns ports to relevant tiles"""
        
    ports = ["wood", "grain", "sheep", "ore", "brick"]
    settlement_locs = {}
    for loc in settlement_locations:
        settlement_locs[loc] = {"display": loc}#the display is the string that will be directly accessed for colouring later
        settlement_locs[loc]["port"] = ""
        settlement_locs[loc]["owner"] = 0
        
    for loc in "ABFJouxy":#these settlements can access the ports
        settlement_locs[loc]["port"] = "3:1 port"
        
    i = 0
    reps = 0
    for loc in "RQCGWcvwjp":
        reps += 1
        port_to_place = f"2:1 {ports[i]} port"
        settlement_locs[loc]["port"] = port_to_place
        if reps % 2 == 0:
            i += 1#it just makes sure that we iterate through the possible ports every 2 repetitions

    return settlement_locs

def assign_tile_variables(tiles : dict, biomes : list, number_tokens : list, associated_settlements):
    """Assigns variables to each tile"""
         
    for i in range(19):
        try:
            tiles[("S"+str(i+1))]["biome"]#the desert currently has no biome tag so simply calling it will return error
        except KeyError:
            #shuffle the biomes; pop is fast
            random.shuffle(biomes)
            chosen_biome = biomes.pop()
            #adds the chosen variables to the biome.
            tiles[("S"+str(i+1))]["biome"] = chosen_biome
            #shuffles the tokens too
            random.shuffle(number_tokens)
            chosen_number = number_tokens.pop()
            tiles[("S"+str(i+1))]["number"] = chosen_number
        
        tiles["S"+str(i+1)]["attached_settlements"] = associated_settlements["S"+str(i+1)]

    return tiles


def create_game_bank():
    """Calls the functions needed to set up the game bank"""
    
    game_bank = {}
    #adds the dictionaries for asset values into the game bank
    resources, dev_bank = initialise_resource_cards()
    game_bank['resources'] = resources
    game_bank['dev_cards'] = dev_bank
    
    #initialises construct number
    game_bank['constructs'] = {'road' : 60,
                     'settlement' : 20,
                     'city' : 16
    }
    
    #creates a bank of building costs that the game can directly access
    game_bank['building_costs'] = {'road' : {'brick' : 1, 'wood' : 1},
                         'settlement' : {'brick' : 1, 'wood' : 1, 'grain' : 1, 'sheep' : 1},
                         'city' : {'grain' : 2, 'ores' : 3},
                         'dev card': {'sheep' : 1, 'grain' : 1, 'ores' : 1}}
    
    return game_bank


def get_player_number() -> int:
    """Gets the number of players, repeats until valid"""
    
    player_number = 0
    while not player_number in [3, 4]:
        try:
            player_number = int(input("How many people are playing? ⋆˚✿🍒𐙚⋆˚\n˚₊ · »-♡→ ").strip()) 
            if not player_number in [3, 4]:
                print("You can only play with 3 or 4 people.")
                
        except ValueError:
            print("Enter an integer (3 or 4) please.")
            
    return player_number
 
 
def make_token_list() -> list:
    """These are the possible tokens that can be assigned onto hexes."""
        
    number_tokens = []
    for i in range(2,12): #the range is between 2 and 11 inclusive as 1 and 12 only appear once.
        for x in range(2): #need to repeat this twice as these tokens appear twice.
            number_tokens.append(i)
        
    number_tokens.append(1)
    number_tokens.append(12)
        
    return number_tokens

 
def initialise_resource_cards() -> tuple[dict, dict]:
    """Initialises the dictionary for each resource to be passed into the game bank"""
    
    #Initialises 19 of each resource
    resources = {}
    for resource in ["ores", "grain", "wood", "brick", "sheep"]:
        resources[resource] = 19
        
    #creates the development card bank and initialises the number for each
    dev_bank = {}
    dev_cards = ["knight", "year of plenty", "build road", "monopoly", "VP cards"]
    dev_values = [14, 2, 2, 2, 5]
    for dev_card, value in zip(dev_cards, dev_values):
        dev_bank[dev_card] = value
    
    return resources, dev_bank
 
 
def get_player_name(player : int, player_names : list) -> str:
    """Gets the name of the current player and checks the length and if it is composed of numbers."""
    
    valid_name = False
    while not valid_name:
        player_name = input(f"Player {player}, enter your name!\n˚₊ · »-♡→ ").strip()
        if player_name in player_names:
            #checks if name has already been created by accessing past names
            print("... That name's already owned. Choose something else.")
        elif player_name.isdigit():
            print("Sorry, you're not allowed a name consisting of only numbers, as this will cause problems later.")
        elif len(player_name) > 8:
            print("Please set a shorter name. Sorry if your name is really that long, but it's hard to display.")
        else:
            valid_name = True
            
    return player_name    


def get_initial_inputs():
    print("""WELCOME TO MY TEXT-BASED CATAN.
Before we start, make sure \x1b[38;2;142;194;21mthis text\x1b[0m is green!
CREDITS: Vivienne, CATAN game studio. To start the game, type 'start', or type 'rng' to gamble!
ENTER YOUR COMMAND TO BEGIN""")#the welcome message
    
    while True:
        action = input("What would you like to do? :)\n˚₊ · »-♡→ ")     
        if action == 'start':
            print("Starting your game now!")
            #aesthetics for a loading/clearing screen
            time.sleep(1)
            clear_screen()
            break
        elif action == 'rng':
            print("Sorry, that's been removed from the program now.")#currently under work. i might add it back but there were some fishy calculations
        elif action == 'cls':
            clear_screen()
        else:
            print("That's not currently a valid command.")
      
      
def create_classes():
    #sets up the classes with their variables
    quick_key, player_dicts = create_player_info()
    game_bank = create_game_bank()
    generate_grid()
    
def main():
    """the main code for the game"""
    
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
    make_token_list()
    
    
    
    get_initial_inputs()
    
    

    
if __name__ == "__main__":
    main()
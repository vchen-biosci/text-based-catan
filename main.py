##hi! all the patches up till now have been trying to get a feel for the game!
##I might either rewrite the whole project or rework it majorly
##my reflection comments are below!!
##I'll be wrapping all the gameplay into a main loop
##I can wrap classes into classes
##I was meant to avoid dictionaries but it'll be SO MUCH EASIER TO USE DICTIONARIES FOR MY COMMANDS!
##plan out turn structure commands (eg cannot roll dice twice in one turn)
## I'll make the cache a game log instead and use file writing for other things
##thx for tuning in, I'll be back heheheheheh

from os import system
import random
##cute ansii codes r 75, 219, and 159


class Resource_Cards:
    def __init__(self):
        self.ores = 0
        self.grain = 0
        self.wood = 0
        self.brick = 0
        self.sheep = 0

    def as_list(self):
        return [self.ores, self.grain, self.wood, self.brick, self.sheep]


class Development_Cards:
    def __init__(self):
        self.knight_cards = 0
        self.progress_cards = 0
        self.victory_point_cards = 0


class Player_Deck:
    def __init__(self):
        self.resource_cards = Resource_Cards()
        self.development_cards = Development_Cards()


class Player_Info:
    def __init__(self):
        self.name = "empty"
        self.order = 0
        self.color = ""
        self.deck = Player_Deck()

def display_info():
    pass


def welcome_players():   

    print("CATAN SIMULATOR - made by VIVIVIVIVIVIVIIII!!!")
    print("Welcome to my version of Settlers of Catan! :)" + "\n")

def print_commands_list():

    print("\n")
    print("""The available commands are as follows:
> pcl: print commands list
> End game: end game
> pbc: print building costs
> pod: print your own deck
> Start game: start game
> inf: open information commands
> cr: display credits
> ru: display rules
> roll: roll die
          
Happy playing ^^ """)
     
def erase_terminal(reprint : bool):

    system("cls")
    if reprint:
        cache_manager("display")
    
    pass


def end_game():
    
    pass


def print_building_costs():

    pass


def print_own_deck(turn : classmethod):

    pass

def start_game():
    game = True
    cache = ""
    return game, cache

def clear_terminal():

    ###bro this might be one of the MOST important programs
    ###wait whats even the point of them clearing the terminal if its gonna repritn automatically...
    ###do i need two files
    ###bc im lowk invested on ts
    pass


def cache_manager(mode, cache):
    if mode == "display":
        print(cache)

    

"""def recieve_input():

    user_action = ""
    while user_action not in COMMANDS_LIST:
        user_action = input("What command?\n")
        if user_action not in COMMANDS_LIST.list:
            print("Hey... if you need to look at the commands list, just type 'ccs' to see the available inputs for each action!")
        else: 
            print("Okay! Processing...")

    return user_action"""


def process_actions(action):
    pass


def print_credits():
    print("""Code created by Vivienne C, Kellett School Hong Kong
          Official game belongs to CATAN""")


def print_game_rules():
    
    print("""My lovely people, the official catan link is available at this link! 
          https://www.catan.com/sites/default/files/2024-01/Almanac%20CATAN-3D.pdf
          I mean... I sure hope it works? But if the link doesn't work you can just search it up :D""")

    
def create_cache():

    filename = input("We'll quickly open a file to store your game data."
                    + "What would you like to name your file?")
    with open(filename, 'w') as catan_file:
        catan_file.write("SETTLERS OF CATAN :)")
    
    return catan_file


def write_into_cache(catan_file, logged_sentence : str):

    catan_file.write(logged_sentence)


"""def assign_player_colours(player_number):
    player_colours = {}
    colour_list = ['yellow', 'red', 'blue', 'green']
    for i in range(get_number_of_players()):
        name = input(f"player {i+1}, what is your colour?")
        players_list[i]

def create_player_assets():

    player_info = get_player_info()
    player_colours = assign_player_colours()
    for info, colours in zip(player_info, player_colours):


    return players_list"""


def edit_resource_bank(mode, action):


    if mode == "set_up":
        resource_bank = Resource_Cards()
        print("Setting up your resource cards... adding 19 cards to each category!!")
        for resource in resource_bank.as_list():
            resource += 19

        return resource_bank

    if mode == "edit":

        if action == "blahblahblah":
            pass
    
    #im not sure if i should add classes to this lol


def edit_development_bank():
    pass

        
def get_number_of_players():

    loop = True
    while loop:
        try:
            number_of_players = int(input())
            while not isinstance(number_of_players, int) or (number_of_players != 3 and number_of_players != 4):
                print("Hi, please enter it as a whole integer of either 3 and 4!")
                number_of_players = int(input())
                loop = False
            
        except TypeError:
            print("Hi, are you sure that your variable is written in arabic numerals? ^^")

    return number_of_players


def get_player_info():

    number_of_players = get_number_of_players()
    player_names = get_player_names(number_of_players)
    player_infolist = []

    return player_infolist


def get_player_names(number_of_players : int):
    
    name_list = []

    for i in range(number_of_players):

        loop = True
        while loop:
            name = input(f"Player {i+1}, what's your name?")
            repeat = input("Are you sure?")
            if repeat.lower() == "y":
                loop = False
            if repeat.lower() == "n":
                pass
            else:
                print("Type either 'Y' or 'N', silly kid!")
        
        name_list.append(name)

    return name_list

    # note for later: need to figure out the correct way to nest the loop. For now I'll just move on


def roll_die(game):

    """dice_results = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    odds = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    roll = random.choices(dice_results, weights=odds, k=1)[0]
    print(f"The dice have spoken! You have rolled a {roll}!")
    
    return(roll)"""
    if game:
        roll_state = True
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll = dice_1 + dice_2
        print(f"The dice have spoken!! |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}! You have rolled a {roll}")

        return roll
    elif not game:
        print("The game hasn't started yet buddy boy OOF aura loss")
    else:
        print("oops, you've already rolled this turn mueehehe")

COMMANDS_LIST = {"start game": start_game,
                  "pcl": print_commands_list, 
                  "end game": end_game, 
                  "pbc": print_building_costs,
                  "pod": print_own_deck, 
                  "inf": display_info, 
                  "cr": print_credits,
                  "roll": roll_die,
                  "ru": print_game_rules}


"""if action == COMMANDS_LIST.startgame[1]:
    game = True
    resource_bank = Resource_Cards()
    edit_resource_bank("set_up", "x")
    resource_bank = edit_resource_bank("view", "x")
    players_list = create_player_assets()
    for player in players_list:
        print(player.colour)

if action == COMMANDS_LIST.pcl[1]:
    COMMANDS_LIST.pcl[0]()

if action == COMMANDS_LIST.end_game[1]:
    if game:
        loop = True
        while loop:
            confirm = input("Are you very sure? (Hint: type 'Y' or 'N')")
            if confirm.lower() not in ("y", "n"):
                print("Please enter either 'y' or 'n'!")
            else:
                loop = False
        
        if confirm.lower() == "y":
            end_game()

    else:
        print("Sorry - it seems that you don't have a game running, and so cannot run this command :(")

if action == COMMANDS_LIST.roll[1]:
    COMMANDS_LIST.roll[0]()"""

def main():
    welcome_players()
    print_commands_list()
    game = False

    while not game:
        player_action = input()
        try:
            COMMANDS_LIST[player_action](game)
        except KeyError:
            print("That's not a valid command! If you need to look at the commands list, type 'cmd' :) Happy playing!")




if __name__ == "__main__": 
    main()
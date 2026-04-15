from os import system
import random, time

##at the start of the game, welcome the player
##then ask if they want to see credits/start a game. use a while loop to make sure that the game has not yet started.
##for taking inputs, define a dictionary. Then, check what the player wants to do and pass the input directly into the directory and call the key value
##use 'except' to catch them out
##perhaps the classes won't work?
##path for classes: start by defining the class. Everytime game data is needed, call the class? 
# I need two types of classes. 
##ok thats a desirable so nvm
##first step today: create an input loop
##get the player's input, find it in the directory, validate/invalidate it, then run it if it's valid,

class GameDirectory:
    def __init__(self):

        def roll_die(self):
             dice_1 = random.randint(1, 6)
             dice_2 = random.randint(1, 6)
             roll = dice_1 + dice_2
             print(f"The dice have spoken!! |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}! You have rolled a {roll}")

             return roll
        

        def thing(self):
            pass
        self.roll_die = {'name': 'roll', 'call': self.roll_die}
        self.player_directory = {'roll': self.roll_die}
        self.global_directory = {}
        self.commands = """The available commands are as follows:
> pcl: print commands list
> end: end game
> pbc: print building costs
> pod: print your own deck
> start: start game
> log: look at game log
> inf: open information commands
> cr: display credits
> ru: display rules
> roll: roll die
          
Happy playing ^^ """

        def print_commands(self):
            print(self.commands)

        

def take_playerinput():
    pass

class GameTemplate:
    def __init__(self):
        self.started = False

GAMEDIRECTORY = GameDirectory()
GAME = GameTemplate()

def welcome_player():
    print("CATAN SIMULATOR - made by VIVIVIVIVIVIVIIII!!!")
    print("Welcome to my version of Settlers of Catan! :)" + "\n")

while not GAME.started == False:
    #recieve input and run corresponding functions
    pass

while GAME.started == True:
    player_move = input(f"What's your move, player {GAME.started}?").strip().lower()
    x = GAMEDIRECTORY.player_directory[player_move]
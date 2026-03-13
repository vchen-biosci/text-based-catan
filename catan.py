from os import system
import random

init(autoreset=True)

class Game:
        
    def __init__(self):
        self.player_decks = "player_decks"
        self.log = []
        self.running = False
        self.credits = """Code created by Vivienne C, Kellett School Hong Kong
Official game belongs to CATAN\n"""
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
        self.rules = """My lovely people, the official catan link is available at this link! 
https://www.catan.com/sites/default/files/2024-01/Almanac%20CATAN-3D.pdf
I mean... I sure hope it works? But if the link doesn't work you can just search it up :D"""
        self.info = self.commands + self.credits + self.rules
        self.player_directory = {}
        self.full_directory = {}
        self.grid = f"""n"""

    def print_commands(self):
            print("\n")
            print(self.commands)

    def print_info(self):
        print("Displaying all basic info:")
        print(self.info)

    def print_log(self):
        print(self.log)

    def print_rules(self):
        print(self.rules)
    
    def start_game(self):
        print("Game has now started!")
        return False
    
    def create_player_directory(self):
        self.player_directory = {"cmds": self.print_commands, "info": self.print_info, "log": self.print_log, "rules": self.print_rules, "start": self.start_game}

    def create_full_directory(self):
        self.full_directory = {}
        self.full_directory.update(self.player_directory)

    #def __init__(self):
        #self.directory = {"cmds": print_commands, "info": print_info, "log": print_log, "rules": print_rules, "start": start_game}
        
GAME = Game()

def roll_die():

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    roll = dice_1 + dice_2
    print(f"The dice have spoken!! |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}! You have rolled a {roll}")

    return roll

def welcome_players():

    print("CATAN SIMULATOR - made by VIVIVIVIVIVIVIIII!!!")
    print("Welcome to my version of Settlers of Catan! :)" + "\n")

def main():
    
    ##start by welcoming the players
    ##btw imma put everything that needs to access data into a class called Game
    welcome_players()
    ##then, ask the player if they want to display more information or start the game
    GAME.create_player_directory()
    while GAME.running == False:
        input_loop = True
        while input_loop:
            action = input("\nWhat would you like to do? :) (hint: 'start' to start a new game or 'info' to view more information)\n> ").strip().lower()
            if action in GAME.player_directory:
                GAME.player_directory[action]()
            else:
                print("That's not an available command! Type 'cmds' to see the available commands!")

        
    while GAME.running == True:
        GAME.full_directory[action]()
        pass

if __name__ == "__main__": 
    main()
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

def add_keys(player_dicts, quick_key):
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

def initialise_resource_cards():
        
        resources = {}
        for resource in ["ores", "grain", "wood", "brick", "sheep"]:
                resources[resource] = 19
        dev_bank = {}
        dev_cards = ["knight", "year of plenty", "road building", "monopoly", "VPs"]
        dev_values = [14, 2, 2, 2, 5]
        for dev_card, value in zip(dev_cards, dev_values):
                dev_bank[dev_card] = value
        
        return resources, dev_bank
                
def make_bank_heh():
        game_bank = {}
        resources, dev_bank = initialise_resource_cards()
        game_bank['resources'] = resources
        game_bank['dev_cards'] = dev_bank
        
def main():
        
        print("Starting your player_dicts...")
        time.sleep(1)
        clear_screen()
        quick_key, player_number, player_dicts = initialise_player_dicts()
        game_bank = make_bank_heh()

if __name__ == "__main__":
        main()

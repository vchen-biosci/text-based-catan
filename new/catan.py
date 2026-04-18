import random, time, os

def infinite_rng(game : dict, CONSTS : dict):
        
        
        possible_stat_commands = ["cache", "mode", "mean", "num", "?", "reset", "indie"]
        print("INFINITE RNG")
        print("Type 'r' to roll, type 'esc' to escape. Use 'stats' if you're into that sort of thing. Enter '?' to access the full list of commands.")
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
                                print(f"Time seems to stop, just momentarily, as the die tumble to the ground. You stare at the result, in awe. |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}. You have rolled {roll}.")
                        else:
                                print("Your current input isn't valid. If you're confused on what inputs are allowed, type '?'")

                elif action == "stats":

                        loop = True
                        print("What stat do you want to see? (Hint: type '?' if you want to see the commands available for stats, or 'leave stats' to escape.)")

                        if len(roll_cache) == 0:
                                print("Warning: your cache is empty right now, so there aren't any stats for you to see.")

                        while loop:
                                action = input("> ").strip().lower()
                                if action in possible_stat_commands:
                                        if action == "cache":
                                                print(roll_cache)

                                        elif action == "mode":

                                                if len(roll_cache) != 0:

                                                        quick_set = set(roll_cache)
                                                        quick_list = []
                                                        for number in quick_set:
                                                                quick_list.append(number)

                                                        contenders_list = []
                                                        mode = quick_list[0]

                                                        for number in quick_list:
                                                                if roll_cache.count(number) > roll_cache.count(mode):
                                                                        mode = number
                                                                elif roll_cache.count(number) == roll_cache.count(mode):
                                                                        contenders_list.append(number)

                                                        if mode in contenders_list:
                                                                contenders_list.remove(mode)


                                                        if contenders_list == []:
                                                                print(f"Your mode was {mode}, and you rolled it a whopping {roll_cache.count(number)} times.")
                                                        else:
                                                                print(f"Well, you don't really have ONE singular mode. In fact, you have {len(contenders_list) + 1}. They are: {str(set(contenders_list))[1:-1]} and {mode}, rolled {roll_cache.count(mode)} time{'s' if roll_cache.count(mode) != 1 else ''} each.")

                                                else:
                                                        print("Your cache is empty; roll some more to get started.")

                                        elif action == "mean":

                                                if len(roll_cache) != 0:
                                                        print(f"The mean of all your rolls is {sum(roll_cache) / len(roll_cache)}")
                                                else:
                                                        print("Your roll cache is empty. Get grinding.")
                                        
                                        elif action == "num":

                                                print(f"You've rolled {len(roll_cache)} times this gambling session.")

                                        elif action == "reset":

                                                print("Ok, tough decision.")
                                                print("Erasing your cache... IRREVERSIBLE BTW")
                                                roll_cache = []
                                                cache_dice_1 = []
                                                cache_dice_2 = []
                                        
                                        elif action == "?":

                                                print("""You currently find yourself in a gambling history analysis, capable of:
> showcasing your roll history (in this session) ('cache')
> showing your most rolled number ('mode')
> showing your mean roll ('mean')
> showing you the number of rolls you've done in this session ('num')
> answering your greatest ?s ('?', you're here right now)
> erasing your cache ('reset')
> allowing you to leave stats... ('leave stats')
> showcasing your single die stats ('indie')
> letting you end rng ('esc').\n""")
                                                
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


                                                        
                                                        print(f"For dice number {i}, your highest roll was {highest_roll}, your mean was {mean}, and your modes were {set(contenders_cachelist)}, rolled a whopping {cache.count(contenders_cachelist[0])} times {('each' * (0 if len(contenders_cachelist) == 0 else 1))}.")
                                                        i += 1
                                                        ##might end up making some sort of function and passing in parameters to run each thing. I'd use an 'if' to sort through bad commands eg calc_stats(action) if action == whole elif action == dice_1 elif action == dice_2 else printstupid idkkk i do want to do this
                                                        


                                elif action == "leave stats":
                                        print("Back to gambling?")
                                        loop = False
                                
                                elif action == "esc":
                                        rng_loop = False

                                else:
                                        print("Stick to the commands. Type '?' if you're lost.")


                else:
                        print("RETURNING TO THE MAINFRAME...")
                        print("(Erasing all your gambling records...)")
                        rng_loop = False

def setup_player_dicts(game : dict, CONSTS : dict):

        player_number = 0
        while not player_number in [3, 4]:
                try:
                        player_number = int(input("How many people are playing?\n> ").strip()) 
                        if not player_number in [3, 4]:
                                print("You can only play with 3 or 4 people.")

                except ValueError:
                        print("Enter an integer 3 or 4 please.")
        clear_screen()
                        
        game["player_number"] = player_number
        game["quick_key"] = []
        for player in range(player_number):
                game["quick_key"].append(player + 1)

        player_names = []
        for player in game["quick_key"]:
                game[player] = {}

                valid_name = False
                while not valid_name:
                        player_name = input(f"Player {player}, enter the name you'd like to be known by.\n> ").strip()
                        if player_name in player_names:
                                print("... That name's already owned. Choose something else.")
                        else:
                                valid_name = True
                game[player]["name"] = player_name 
                player_names.append(player_name)

                valid_password = False
                while not valid_password:
                        password = input("Please enter a password; it'll be used to check for your consent later. Keep it short but memorable, and make sure it's not a password you use for important sites.\n> ")
                        if len(password) > 7:
                                print("That password is way too long. Keep it to 7 or below characters.")
                        else:
                                valid_password = True
                game[player]['password'] = password
                
                clear_screen()
        
        game["player_names"] = player_names

        return game

def print_own_deck(game : dict, CONSTS : dict):
        print("this is ur deck")

def roll_die(game : dict, CONSTS : dict):

        if game["roll_allowed"] == True:
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                roll = dice_1 + dice_2
                print(f"As everyone watches with baited breath, you roll the die. You pray for a good result. They land as follows: |{dice_1}| |{dice_2}| ... {dice_1} + {dice_2} = {roll}. You've rolled a {roll}.")
                game["roll_allowed"] = False
                
        else:
                print("You've already rolled this turn.")

        return roll

def quick_reorder(road : str):

        if road[0] > road[1]:
                road = road[1] + road[0]

        return road

def print_grid(game : dict, CONSTS : dict):

        grid_part_1 = (
#line 1
(" " * 65) + "3: 1 port" + "\n" +
#line 2
(" " * 65) + "/      \\" + "\n" +
#line 3
(" " * 64) + "/        \\" + "\n" +
#line 4
(" " * 20) + "sea" + (" " * 38) + game['settlement_locs']["A"]["display"] + " " + (game['roads']["AB"] + " ") * 4 + game['settlement_locs']["B"]["display"] + (" " * 38) + "sea" + "\n" +
#line 5
(" " * 61) + game['roads']["AD"] + "              " + game['roads']["BE"] + "\n" +
#line 6 & 7
(" " * 60) + game['roads']["AD"] + "                " + game['roads']["BE"] + "\n\n" +
#line 8
(" " * 35) + ("2:1 grain port") + (" " * 9) + game['roads']["AD"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S1"]["biome"]] + (" "* 7) + game['roads']["BE"] + (" " * 16) + "3:1 port" + "\n" +
#line 9
(" " * 36) + "|    " + "\\" + "   " + (game['roads']["CD"] + " ") * 4 + game['roads']["AD"] + (" " * 10) + str(game['tiles']["S1"]["number"]) + (" " * 11 if len(str(game['tiles']["S1"]["number"])) == 1 else " " * 10) + game['roads']["BE"] + " " + (game['roads']["EF"] + " ") * 4 + "   /  |\n" +
#line 10
(" " * 36) + "|" + (" " * 3) + game['settlement_locs']["C"]["display"] + " " + game['roads']["CG"] + (" " * 11) + game['settlement_locs']["D"]["display"] + "  " + game['roads']["DH"] 
+ (" " * ((22 - len(str(game['tiles']["S1"]["biome"])))//2)) + game['tiles']["S1"]["biome"] + 
(" " * (((22-len(str(game['tiles']["S1"]["biome"])))//2)+ (1 if len(str(game['tiles']["S1"]["biome"]))%2 != 0 else 0)))
+ game['roads']["EI"] + " " + game['settlement_locs']["E"]["display"] + (" " * 8) + game['settlement_locs']["F"]["display"] + "  " + game['roads']["FJ"] + "     |\n" +
#line 11
(" " * 36) + "|" + "    " + game['roads']["CG"] +  (" " * 16) + game['roads']["DH"] + (" " * 9) + "S1" + (" " * 9) + game['roads']["EI"] + (" " * 15) + game['roads']["FJ"] + "    |" + "\n" +
#line 12
(" " * 36) + "|" + (" " * 63) + "|" + "\n" +
#line 13
(" " * 36) + "|" + "  " + game['roads']["CG"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S2"]["biome"]] + (" " * 7) + game['roads']["DH"] 
+ (" " * 16) + game['roads']["EI"] + " "  + (" " * 6) + (CONSTS['kaomojis'][game['tiles']["S3"]["biome"]]) 
+ (" " * 6) + game['roads']["FJ"] +"  |\n" +
#line 14
(" " * 21) + game['settlement_locs']["$"]["display"] + " " + (game['roads'][quick_reorder("G$")] + " ") * 4 + game['settlement_locs']["G"]["display"] + "  " + game['roads']["CG"] + (" " * 10) + str(game['tiles']["S2"]["number"]) + 
(" " * 9 if len(str(game['tiles']["S2"]["number"])) == 1 else " " * 8) + game['settlement_locs']["H"]["display"] + " " + game['roads']["DH"] + " " + (game['roads']["HI"] + " ") * 4 + " " + game['roads']["EI"] + " " + game['settlement_locs']["I"]["display"] +
(" " * 8) + str(game['tiles']["S3"]["number"]) + (" " * 8 if len(str(game['tiles']["S3"]["number"])) == 1 else " " * 7) + game['settlement_locs']["J"]["display"] + " " + game['roads']["FJ"] + " | " + (game['roads']["JK"] + " ") * 4 
+ game['settlement_locs']["K"]["display"] + "\n" +
#line 15
(" " * 21) + game['roads'][quick_reorder("L$")] + (" " * 16) + game['roads']["GM"] + (" " * ((22 - len(str(game['tiles']["S2"]["biome"])))//2)) + game['tiles']["S2"]["biome"] + (" " * 9 if game['tiles']["S2"]["biome"] != "desert" else " " * 8)
+ game['roads']["HN"] + (" " * 14) + game['roads']["IO"] + (" " * ((21 - len(str(game['tiles']["S3"]["biome"])))//2)) + game['tiles']["S3"]["biome"] + (" " * ( (21 - len(game['tiles']["S3"]["biome"])) //2   ) ) + 
(" " * (1 if len(game['tiles']["S3"]["biome"]) % 2 != 1 else 0)) + game['roads']["JP"] + (" " * 14) + game['roads']["KQ"] + "\n" +
#line 16 & 17 
(" " * 20) + game['roads'][quick_reorder("L$")] + (" " * 18) + game['roads']["GM"] + (" " * 9) + "S2" + (" " * 9) + game['roads']["HN"] + (" " * 16) + game['roads']["IO"] + (" " * 8) + "S3" + (" " * 9) + game['roads']["JP"] + (" " * 16) + game['roads']["KQ"] + "\n\n" +
#line 18
(" " * 18) + game['roads'][quick_reorder("L$")] + (" " * 8) + CONSTS['kaomojis'][game['tiles']["S4"]["biome"]] + (" " * 8) + game['roads']["GM"] + (" " * 16) + game['roads']["HN"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S5"]["biome"]] + (" " * 7) + game['roads']["IO"]
+ (" " * 15) + game['roads']["JP"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S6"]["biome"]] + (" " * 7) + game['roads']["KQ"] + "\n" + 
#line 19
(" " * 15) + game['settlement_locs']["L"]["display"] + " " + game['roads'][quick_reorder("L$")] + (" " * 11) + str(game['tiles']["S4"]["number"]) + (" " * (10 if len(str(game['tiles']["S4"]["number"])) == 1 else 9)) + game['settlement_locs']["M"]["display"] +
" " + game['roads']["GM"] + "  " + (game['roads']["MN"] + " ") * 4 + game['roads']["HN"] + game['settlement_locs']["N"]["display"] + (" " * 9) + str(game['tiles']["S5"]["number"]) + (" " * 9 if len(str(game['tiles']["S5"]["number"])) == 1 else " " * 8) + game['settlement_locs']["O"]["display"] +
" " + game['roads']["IO"] + " " + (game['roads']["OP"] + " ") * 4 + game['roads']["JP"] + " " + game['settlement_locs']["P"]["display"] + (" " * 8) + str(game['tiles']["S6"]["number"]) + (" " * 11 if len(str(game['tiles']["S6"]["number"])) == 1 else " " * 10) + game['roads']["KQ"]
+ " " + game['settlement_locs']["Q"]["display"] + "\n"
        
        
)

        grid_part_2 = (
#line 20
(" " * 17) + game['roads']["LR"] + (" " * ((24 - len(str(game['tiles']["S4"]["biome"])))//2)) + game['tiles']["S4"]["biome"] + (" " * 10 if game['tiles']["S4"]["biome"] != "desert" else " " * 9) + game['roads']["MS"] + (" " * 14) + game['roads']["NT"] +
(" " * ((22 - len(str(game['tiles']["S5"]["biome"])))//2)) + game['tiles']["S5"]["biome"] + (" " * 9 if game['tiles']["S5"]["biome"] != "desert" else " " * 8) + game['roads']["OU"] + (" " * 13) + game['roads']["PV"] +
(" " * ((22 - len(str(game['tiles']["S6"]["biome"])))//2)) + game['tiles']["S6"]["biome"] + (" " * 9 if game['tiles']["S6"]["biome"] != "desert" else " " * 8) + game['roads']["QW"] + "\n" +
#line 21 & 22
(" " * 18) + game['roads']["LR"] + (" " * 10) + "S4" + (" " * 10) + game['roads']["MS"] + (" " * 16) + game['roads']["NT"] + (" " * 9) + "S5" + (" " * 9) + game['roads']["OU"] + (" " * 15) + game['roads']["PV"] + (" " * 9) + "S6" + (" " * 9) + game['roads']["QW"] + "\n\n" +
#line 23
(" " * 20) + game['roads']["LR"] + (" " * 18) + game['roads']["MS"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S7"]["biome"]] + (" " * 7) + game['roads']["NT"] + (" " * 16) + game['roads']["OU"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S8"]["biome"]]  + (" " * 6) + game['roads']["PV"] +
(" " * 16) + game['roads']["QW"] + "\n" +
#line 24
(" " * 3) + "2:1 wood port - " + game['settlement_locs']["R"]["display"] + " " + game['roads']["LR"] + "  " + (game['roads']["RS"] + " ") * 4 + game['settlement_locs']["S"]["display"] + " " + game['roads']["MS"] + (" " * 10) + str(game['tiles']["S7"]["number"]) + 
(" " * 8 if len(str(game['tiles']["S7"]["number"])) == 1 else " " * 7) + game['settlement_locs']["T"]["display"] + "  " + game['roads']["NT"] + "  " + (game['roads']["TU"] + " ") * 4 + game['roads']["OU"] + " " + game['settlement_locs']["U"]["display"] +
(" " * 8) + str(game['tiles']["S8"]["number"]) + (" " * 8 if len(str(game['tiles']["S8"]["number"])) == 1 else " " * 7) + game['settlement_locs']["V"]["display"] + " " + game['roads']["PV"] + " " + (game['roads']["VW"] + " ") * 4 + " " + game['roads']["QW"] + 
game['settlement_locs']["W"]["display"] +  " _ _ _  2:1 sheep port" + "\n" +
#line 25
(" " * 8) + "\\" + (" " * 12) + game['roads']["RX"] + (" " * 16) + game['roads']["SY"] + (" " * ((22 - len(str(game['tiles']["S7"]["biome"])))//2)) + game['tiles']["S7"]["biome"] + 
(" " * (((22-len(str(game['tiles']["S7"]["biome"])))//2) + (1 if len(str(game['tiles']["S7"]["biome"]))%2 != 0 else 0))) + game['roads']["TZ"] + (" " * 14) + game['roads']["Ua"] +
(" " * ((21 - len(str(game['tiles']["S8"]["biome"])))//2)) + game['tiles']["S8"]["biome"] + 
(" " * (((21-len(str(game['tiles']["S8"]["biome"])))//2) + (1 if len(str(game['tiles']["S8"]["biome"]))%2 != 1 else 0))) + game['roads']["Vb"] + (" " * 14) + game['roads']["Wc"] + "         /\n" +
#line 26
(" " * 9) + "\\" + (" " * 10) + game['roads']["RX"] + (" " * 18) + game['roads']["SY"] + (" " * 9) + "S7" + (" " * 9) + game['roads']["TZ"] + (" " * 16) + game['roads']["Ua"] + (" " * 8) + "S8" + (" " * 9) + game['roads']["Vb"] + (" " * 16) + game['roads']["Wc"] + "       /" + "\n" +
#line 27
(" " * 10) + "\\" + (" " * 110) + "/" + "\n" +
#line 28
(" " * 11) + "\\" + (" " * 6) + game['roads']["RX"] + (" " * 8) + CONSTS['kaomojis'][game['tiles']["S9"]["biome"]] + (" " * 8) + game['roads']["SY"] + (" " * 16) + game['roads']["TZ"] + (" " * 6) + CONSTS['kaomojis'][game['tiles']["S10"]["biome"]] + (" " * 8) + game['roads']["Ua"]
+ (" " * 15) + game['roads']["Vb"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S11"]["biome"]] + (" " * 7) + game['roads']["Wc"] + "   /" + "\n" +
#line 29
(" " * 12) + "\\  " + game['settlement_locs']["X"]["display"] + " " + game['roads']["RX"] + (" " * 12) + str(game['tiles']["S9"]["number"]) + (" " * 9 if len(str(game['tiles']["S9"]["number"])) == 1 else " " * 8) 
+ game['settlement_locs']["Y"]["display"] + " " + game['roads']["SY"] + " " + (game['roads']["YZ"] + " ") * 4 + game['settlement_locs']["Z"]["display"] + game['roads']["TZ"] + (" " * 10) + str(game['tiles']["S10"]["number"]) + 
(" " * 9 if len(str(game['tiles']["S10"]["number"])) == 1 else " " * 8) + game['settlement_locs']["a"]["display"] + " " + game['roads']["Ua"] + (" " + game['roads']["ab"]) * 4 + game['settlement_locs']["b"]["display"] + game['roads']["Vb"] +
(" " * 10) + str(game['tiles']["S11"]["number"]) + (" " * 11 if len(str(game['tiles']["S11"]["number"])) == 1 else " " * 10) + game['roads']["Wc"] + " " + game['settlement_locs']["c"]["display"] + "\n" +
#line 30
(" " * 17) + game['roads']["Xd"] + (" " * ((24 - len(str(game['tiles']["S9"]["biome"])))//2)) + game['tiles']["S9"]["biome"] + (" " * (((24-len(str(game['tiles']["S9"]["biome"])))//2) + (1 if len(str(game['tiles']["S9"]["biome"]))%2 != 0 else 0))) 
+ game['roads']["Ye"] + (" " * 14) + game['roads']["Zf"] + (" " * ((22 - len(str(game['tiles']["S10"]["biome"])))//2)) + game['tiles']["S10"]["biome"] + 
(" " * (((22-len(str(game['tiles']["S10"]["biome"])))//2) + (1 if len(str(game['tiles']["S10"]["biome"]))%2 != 0 else 0))) + game['roads']["ag"] + (" " * 13) + game['roads']["bh"] +
(" " * ((22 - len(str(game['tiles']["S11"]["biome"])))//2)) + game['tiles']["S11"]["biome"] + 
(" " * (((22-len(str(game['tiles']["S11"]["biome"])))//2) + (1 if len(str(game['tiles']["S11"]["biome"]))%2 != 0 else 0))) + game['roads']["ci"] + "\n"
        
        )

        grid_part_3 = (
#line 31 & 32
(" " * 18) + game['roads']["Xd"] + (" " * 10) + "S9" + (" " * 10) + game['roads']["Ye"] + (" " * 16) + game['roads']["Zf"] + (" " * 8) + "S10" + (" " * 9) + game['roads']["ag"] + (" " * 15) + game['roads']["bh"] + (" " * 8) + "S11" + (" " * 9) + game['roads']["ci"] + "\n\n" +
#line 33
(" " * 20) + game['roads']["Xd"] + (" " * 18) + game['roads']["Ye"] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S12"]["biome"]] + (" " * 7) + game['roads']["Zf"] + (" " * 16) + game['roads']["ag"] + (" " * 6) + CONSTS['kaomojis'][game['tiles']["S13"]["biome"]] + (" " * 7) + game['roads']["bh"] + (" " * 16) + game['roads']["ci"] 
+ "\n" +
#line 34
(" " * 19) + game['settlement_locs']["d"]["display"] + " " + game['roads']["Xd"] + "  " + (game['roads']["de"] + " ") * 4 + game['settlement_locs']["e"]["display"] + " " + game['roads']["Ye"] + (" " * 10) + 
str(game['tiles']["S12"]["number"]) + (" " * 9 if len(str(game['tiles']["S12"]["number"])) == 1 else " " * 8) + game['settlement_locs']["f"]["display"] + " " + game['roads']["Zf"] + " " + (game['roads']["fg"] + " ") * 4 + game['settlement_locs']["g"]["display"] + game['roads']["ag"] +
(" " * 10) + str(game['tiles']["S13"]["number"]) + (" " * 8 if len(str(game['tiles']["S13"]["number"])) == 1 else " " * 7) + game['settlement_locs']["h"]["display"] + " " + game['roads']["bh"] + " " + (game['roads']["hi"] + " ") * 4 + " " + game['roads']["ci"] + " " 
+ game['settlement_locs']["i"]["display"] + "\n" +
#line 35
(" " * 21) + game['roads']["dj"] + (" " * 16) + game['roads']["ek"] + (" " * ((23 - len(str(game['tiles']["S12"]["biome"])))//2)) + game['tiles']["S12"]["biome"] + 
(" " * (((21-len(str(game['tiles']["S12"]["biome"])))//2) + (1 if len(str(game['tiles']["S12"]["biome"]))%2 != 1 else 0))) + game['roads']["fl"] + (" " * 14) + game['roads']["gm"]
+ (" " * ((21 - len(str(game['tiles']["S13"]["biome"])))//2)) + game['tiles']["S13"]["biome"] + 
(" " * (((21-len(str(game['tiles']["S13"]["biome"])))//2) + (1 if len(str(game['tiles']["S13"]["biome"]))%2 != 1 else 0))) + game['roads']["hn"] + (" " * 14) + game['roads']["io"] + "\n" +
#line 36 & 37
(" " * 20) + game['roads']["dj"] + (" " * 18) + game['roads']['ek'] + (" " * 8) + "S12" + (" " * 9) + game['roads']['fl'] + (" " * 16) + game['roads']['gm'] + (" " * 8) + "S13" + (" " * 8) + game['roads']['hn'] + (" " * 16) + game['roads']['io'] + "\n\n" +
#line 38 
(" " * 18) + game['roads']['dj'] + (" " * 8) + CONSTS['kaomojis'][game['tiles']["S14"]["biome"]] + (" " * 8) + game['roads']['ek'] + (" " * 16) + game['roads']['fl'] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S15"]["biome"]] + (" " * 7) + game['roads']['gm'] + (" " * 15) + game['roads']['hn'] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S16"]["biome"]] + (" " * 7)
+ game['roads']['io'] + "\n" +
#line 39
(" " * 15) + game['settlement_locs']["j"]["display"] + " " + game['roads']['dj'] + (" " * 11) + str(game['tiles']["S14"]["number"]) + (" " * 10 if len(str(game['tiles']["S14"]["number"])) == 1 else " " * 9) + game['settlement_locs']["k"]["display"]
+ " " + game['roads']['ek'] + " " + (game['roads']["kl"] + " ") * 4 + game['settlement_locs']["l"]["display"] + game['roads']['fl'] + (" " * 10) + str(game['tiles']["S15"]["number"]) + (" " * 9 if len(str(game['tiles']["S15"]["number"])) == 1 else " " * 8)
+ game['settlement_locs']["m"]["display"] + " " + game['roads']['gm'] + " " + (game['roads']["mn"] + " ") * 4 + game['roads']['hn'] + game['settlement_locs']["n"]["display"] + (" " * 9) + str(game['tiles']["S16"]["number"]) + 
(" " * 11 if len(str(game['tiles']["S16"]["number"])) == 1 else " " * 10) + game['roads']['io'] + " " + game['settlement_locs']["o"]["display"] + "\n" +
#line 40
(" " * 17) + game['roads']['jp'] + (" " * ((24 - len(str(game['tiles']["S14"]["biome"])))//2)) + game['tiles']["S14"]["biome"] +
(" " * (((24-len(str(game['tiles']["S14"]["biome"])))//2) + (1 if len(str(game['tiles']["S14"]["biome"]))%2 != 0 else 0))) + game['roads']['kq'] + (" " * 14) + game['roads']['lr'] +
(" " * ((22 - len(str(game['tiles']["S15"]["biome"])))//2)) + game['tiles']["S15"]["biome"] + 
(" " * (((22-len(str(game['tiles']["S15"]["biome"])))//2) + (1 if len(str(game['tiles']["S15"]["biome"]))%2 != 0 else 0))) + game['roads']['ms'] + (" " * 13) + game['roads']['nt'] +
(" " * ((22 - len(str(game['tiles']["S16"]["biome"])))//2)) + game['tiles']["S16"]["biome"] + 
(" " * (((22 - len(str(game['tiles']["S16"]["biome"])))//2) + (1 if len(str(game['tiles']["S16"]["biome"]))%2 != 0 else 0))) + game['roads']['ou'] + "\n" +
#line 41 
(" " * 14) + "/" + (" " * 3) + game['roads']['jp'] + (" " * 9) + "S14"  + (" " * 10) + game['roads']['kq'] + (" " * 16) + game['roads']['lr'] + (" " * 8) + "S15" + (" " * 9) + game['roads']['ms'] + (" " * 15) + game['roads']['nt'] + (" " * 8) + "S16" + (" " * 9) + game['roads']['ou'] + 
(" " * 3) + "\\" + "\n" +
#line 42
(" " * 13) + "/" + (" " * 107) + "\\" + "\n" 
                )

        grid_part_4 = (
#line 43
(" " * 12) + "/" + (" " * 7) + game['roads']['jp'] + (" " * 18) + game['roads']['kq'] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S17"]["biome"]] + (" " * 7) + game['roads']['lr'] + (" " * 16) + game['roads']['ms'] + (" " * 6) + CONSTS['kaomojis'][game['tiles']["S18"]["biome"]] + (" " * 7)
+ game['roads']['nt'] + (" " * 16) + game['roads']['ou'] + (" " * 7) + "\\" + "\n" +
#line 44
" 2:1 brick port _  " + game['settlement_locs']["p"]["display"] + " " + game['roads']['jp'] + " " + (game['roads']["pq"] + " ") * 4 + " " + game['settlement_locs']["q"]["display"] + " " + game['roads']['kq'] + (" " * 11) + str(game['tiles']["S17"]["number"]) +
(" " * 8 if len(str(game['tiles']["S17"]["number"])) == 1 else " " * 7) + game['settlement_locs']["r"]["display"] + " " + game['roads']['lr'] + " " + (game['roads']["rs"] + " ") * 4 + game['settlement_locs']["s"]["display"] + game['roads']['ms'] + (" " * 10) + 
str(game['tiles']["S18"]["number"]) + (" " * 8 if len(str(game['tiles']["S18"]["number"])) == 1 else " " * 7) + game['settlement_locs']["t"]["display"] + " " + game['roads']['nt'] + " " + (game['roads']["tu"] + " ") * 4 + " " + game['roads']['ou'] +
game['settlement_locs']["u"]["display"] + "  _ _ 3:1 port" + "\n" +
#line 45
(" " * 38) + game['roads']['qv'] + (" " * ((22 - len(str(game['tiles']["S17"]["biome"])))//2)) + game['tiles']["S17"]["biome"] + 
(" " * (((22 - len(str(game['tiles']["S17"]["biome"])))//2) + (1 if len(str(game['tiles']["S17"]["biome"]))%2 != 0 else 0))) + game['roads']['rw'] + (" " * 14) + game['roads']['sx'] +
(" " * ((21 - len(str(game['tiles']["S18"]["biome"])))//2)) + game['tiles']["S18"]["biome"] + 
(" " * (((21 - len(str(game['tiles']["S18"]["biome"])))//2) + (1 if len(str(game['tiles']["S18"]["biome"]))%2 != 1 else 0))) + game['roads']['ty'] + "\n" +
#line 46 & 47
(" " * 39) + game['roads']['qv'] + (" " * 8)  + "S17" + (" " * 9) + game['roads']['rw'] + (" " * 16) + game['roads']['sx'] + (" " * 8) + "S18" + (" " * 8) + game['roads']['ty'] + "\n\n" +
#line 48
(" " * 41) + game['roads']['qv'] + (" " * 16) + game['roads']['rw'] + (" " * 7) + CONSTS['kaomojis'][game['tiles']["S19"]["biome"]] + (" " * 7) + game['roads']['sx'] + (" " * 15) + game['roads']['ty'] + "\n" +
#line 49
(" " * 42) + game['roads']['qv'] + game['settlement_locs']["v"]["display"] + " " + (game['roads']["vw"] + " ") * 4 + game['settlement_locs']["w"]["display"] + (" " * 10) + str(game['tiles']["S19"]["number"]) +
(" " * 9 if len(str(game['tiles']["S19"]["number"])) == 1 else " " * 8) + game['settlement_locs']["x"]["display"] + " " + game['roads']['sx'] + " " + (game['roads']["xy"] + " ") * 4 + game['roads']['ty'] + " " 
+ game['settlement_locs']["y"]["display"] + "\n" +
#line 50
(" " * 58) + game['roads']['wz'] +(" " * ((21 - len(str(game['tiles']["S19"]["biome"])))//2)) + game['tiles']["S19"]["biome"] + 
(" " * (((21 - len(str(game['tiles']["S19"]["biome"])))//2) + (1 if len(str(game['tiles']["S19"]["biome"]))%2 != 1 else 0))) + game['roads'][quick_reorder("x+")] + "\n" +
#line 51
(" " * 44) + "\\" + (" " * 11) + "/  " + game['roads']['wz'] + (" " * 8) + "S19" + (" " * 8) + game['roads'][quick_reorder("x+")] + "  \\          /" + "\n" +
#line 52
(" " * 45) + "\\         /" + (" " * 27) + "\\" + "        " + "/" + "\n" +
#line 53
(" " * 46) + "\\       /      " + game['roads']['wz'] + "               " + game['roads'][quick_reorder("x+")] + "      " + "\\" + "      " + "/" + "\n" +
#line 54
(" " * 45) + "2:1 ore port     " + game['roads']['wz'] + game['settlement_locs']["z"]["display"] + " " + (game['roads']["+z"] + " ") * 4 + game['settlement_locs']["+"]["display"] + "      3:1 port"

        )

        quick_grid_access = [grid_part_1, grid_part_2, grid_part_3, grid_part_4]

        for grid in quick_grid_access:
                print(grid, end="")
        print("\n")

def generate_grid(game : dict, CONSTS : dict):

        print("Setting up your tiles...")
        tiles = {}
        for i in range(19):
                tiles[("S"+str(i+1))] = {}

        print("Spawning your desert...")
        desert_placement = random.randint(1, 19)
        tiles[("S"+str(desert_placement))]["biome"] = "desert"
        tiles[("S"+str(desert_placement))]["number"] = "NA"
        game['robber'] = "S"+str(desert_placement)

        print("Generating random numbers...")
        for i in range(19):
                try:
                        tiles[("S"+str(i+1))]["biome"]
                except KeyError:
                        random.shuffle(CONSTS["biomes"])
                        chosen_biome = CONSTS["biomes"].pop()
                        tiles[("S"+str(i+1))]["biome"] = chosen_biome

                        random.shuffle(CONSTS["number_tokens"])
                        chosen_number = CONSTS["number_tokens"].pop()
                        tiles[("S"+str(i+1))]["number"] = chosen_number

        print("Sailing to your ports...")
        settlement_locs = {}
        for letter in CONSTS["settlement_locations"]:
                settlement_locs[letter] = {"display": letter}
                settlement_locs[letter]["port"] = ""
        for loc in "ABFJouxy":
                settlement_locs[loc]["port"] = {"3:1 port"}
        i = 0
        reps = 0
        for loc in "RQCGWcvwjp":
                reps += 1
                port_to_place = f"2:1 {CONSTS['ports'][i]} port"
                settlement_locs[loc]["port"] = port_to_place
                if reps % 2 == 0:
                        i += 1

        print("Paving your roads...")
        counter = 0
        quick_dict = dict(zip(CONSTS["road_types"], CONSTS["road_strings"]))
        roads = {}
        for road_type in CONSTS["road_types"]:
                for i in range(len(quick_dict[road_type])//2):
                        
                        road = quick_dict[road_type][counter]
                        counter += 1
                        road += quick_dict[road_type][counter]
                        counter += 1

                        road = quick_reorder(road)
                        roads[road] = road_type
                counter = 0

        game['roads'] = roads
        game["tiles"] = tiles
        game['settlement_locs'] = settlement_locs

        return game

def print_board(game : dict, CONSTS : dict):
        print("________ WELCOME TO THE WORLD OF CATAN. WHERE WILL YOU SETTLE TODAY? ________\n")
        
        print(f"GAME BANK:")
        for resource in game['resource_bank']:
                print(f'{resource} : {game["resource_bank"][resource]}', end="  ||  ")
        print("\n")
        for dev_card in game['dev_cards']:
                print(f'{dev_card} : {game["dev_cards"][dev_card]}', end="  ||  ")
        print("\n")
        for player in game['quick_key']:
                print(ansi_stitching(game[player]['color'], f"Player {player} ({game[player]['name']})"), end="  ||  ")
        print("\n")
        print_grid(game, CONSTS)
        print(f"The robber is currently pillaging the citizens of {game['robber']} and stealing all their {game['tiles'][game['robber']]['biome']}...")

def setup_game(game : dict, CONSTS : dict):

        print("Notice: While setting up the game, you temporarily can't use other commands.")

        game = setup_player_dicts(game, CONSTS)

        print("Okay; your names are: ")
        for player in range(game['player_number']):
                if player == game['quick_key'][-2]:
                        print(game['player_names'][player], end=".\n")
                elif player == game['quick_key'][-3]:
                        print(game['player_names'][player], end=", and ")
                else:
                        print(game['player_names'][player], end=", ")
                        
        game = assign_player_colours(game, CONSTS)

        print("Initialising player cards...")
        for player in game["quick_key"]:

                game[player]["resources"] = {}
                for resource in CONSTS["resources"]:
                        game[player]["resources"][resource] = 0
                        
                game[player]["dev_cards"] = {}
                quick_dev_dict = dict(zip(CONSTS['dev_cards'], CONSTS["dev_card_numbers"]))
                for dev_card in quick_dev_dict:
                        game[player]["dev_cards"][dev_card] = quick_dev_dict[dev_card]

                game[player]['roads'] = []
                game[player]['settlements'] = []
                game[player]['cities'] = []

                game[player]['construct_bank'] = {"settlements": 5, "cities": 4, "roads": 15}
                game[player]['achievements'] = {"longest road" : 0, "largest army" : 0}
                game[player]['knights_recruited'] = 0
                game[player]['VPs'] = 0

        print("Setting up the resource bank...")
        game["resource_bank"] = {}
        for resource in CONSTS["resources"]:
                game["resource_bank"][resource] = 19
        game["dev_cards"] = {}
        for dev_card in quick_dev_dict:
                game["dev_cards"][dev_card] = quick_dev_dict[dev_card]

        print("Generating your grid...")
        game = generate_grid(game, CONSTS)
        clear_screen()

        return game

def clear_screen():
        print("\033c", end="")

def ansi_stitching(color : list, text : str):
        
        colored_ver = "\x1b[38;2;"

        reps = 0
        for value in color:
                colored_ver += str(value)

                reps += 1
                if reps < 3:
                        colored_ver += ";"
        
        colored_ver += "m" + text + "\x1b[0m"

        return colored_ver

def check(text : str, CONSTS : dict, game : dict, mode : str):

        valid = True 

        if mode == 'settlement':
                settlement = text
                try:
                        if game['settlement_locs'][settlement]['display'] != settlement:
                                print("This settlement is already taken. Pro tip: if it has a colour, it's not up for grabs.")
                                valid = False
                                
                        else:
                                related_roads = []
                                for road in game['roads']:
                                        if settlement in road:
                                                related_roads.append(road)
                                
                                related_settlements = []
                                for road in related_roads:
                                        for place in road:
                                                if place != settlement:
                                                        related_settlements.append(place)

                                for place in related_settlements:
                                        if place != game['settlement_locs'][place]['display']:
                                                print(f"It looks like you're trying to place a settlement adjacent to another settlement, 'location {place}'. You must place it at least two roads away.")
                                                valid = False
                                                break
        
                except KeyError:
                        if settlement in game['settlement_locs']:
                                valid = True
                        else:
                                print("That settlement doesn't exist.")
                                valid = False

                if game["mode"] != "initial":
                        case = []
                        for road in game['roads']:
                                if settlement in road:
                                        if game['roads'][road] != road:
                                                owner = analyse_ownership(game, CONSTS, settlement)
                                                if owner == game["player_turn"]:
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

                if text not in game['roads']:
                        valid = False
                        print("That road doesn't exist.")

                else:
                        #look through each road, check if the road has been modified...
                        
                        owner = analyse_ownership(game, CONSTS, game["roads"][text])
                        if owner != game['player_turn'] and len(game["roads"][text]) > 5:
                                print("That road already belongs to someone else.")
                                valid = False      
                                        
                        case = []
                        for settlement in text:
                                if game["settlement_locs"][settlement]['display'] != settlement:
                                        owner = analyse_ownership(game, CONSTS, game['settlement_locs'][settlement]['display'])
                                        if game['player_turn'] == owner:
                                                case.append(settlement)

                                for road in game['roads']:
                                        if settlement in road:
                                                owner = analyse_ownership(game, CONSTS, game['roads'][road])
                                                if game['player_turn'] == owner:
                                                        case.append(road)
                        
                        if valid != False and len(case) != 0:
                                print("Congratulations on paving a new road.")
                        else:
                                print("You don't own any settlements/roads next to that road, so you can't build it. Sorry.")
                                valid = False

        return valid

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

def assign_player_colours(game : dict, CONSTS : dict):

        preset_colors = [[1, 201, 184], [252, 210, 1], [252, 84, 1], [210, 1, 252]]

        manual = ""
        while manual not in ["y", "m"]:

                manual = input("Would you like to use our pre-selected colours or customise your own?" +
                        " Type 'Y' for yes and 'M' to manually select.\n> ").lower().strip()
                
        if manual == "m":

                for player in range(game["player_number"]):
                        print(f"Player {player + 1}, your turn to choose.")
                        game[player + 1]["color"] = choose_colours(CONSTS)

        else:
                
                for player in range(game["player_number"]):
                        game[player+1]["color"] = preset_colors[player]

        for player in range(game["player_number"]):
                print(ansi_stitching(game[player + 1]["color"], f"Player {player + 1}, this is your colour."))
                time.sleep(0.3)


        return game

def game_stage_1(game : dict, CONSTS : dict):
        game['player_turn'] = 1 #ok i know this looks redundant but print board requires that variable ok?

        print_board(game, CONSTS)
        print(f"We'll go from player 1 to player {len(game['quick_key'])}; you can place two settlements and two roads for free. Please choose wisely.")
        game['mode'] = "initial"
        
        for i in range(2):
                for player in game['quick_key']:
                        game['player_turn'] = player
                        valid = False
                        while not valid:
                                text = input(ansi_stitching(game[player]['color'], f"Player {player}, where would you like to place your settlement?") + "\n> ").strip()
                                valid = check(text, CONSTS, game, 'settlement')
                        game[player]['settlements'].append(text)
                        print(game['settlement_locs'][text]['display'])
                        game['settlement_locs'][text]['display'] = ansi_stitching(game[player]['color'], game['settlement_locs'][text]['display'])
                        clear_screen()
                        print_board(game, CONSTS)

                        valid = False
                        while not valid:
                                text = input(ansi_stitching(game[player]['color'], f"Player {player}, where are you placing your road?") + "\n> ").strip()
                                valid = check(text, CONSTS, game, 'road')
                        game[player]['roads'].append(text)
                        game['roads'][quick_reorder(text)] = ansi_stitching(game[player]['color'], game['roads'][quick_reorder(text)])
                        clear_screen()
                        print_board(game, CONSTS)

        game['player_turn'] = 1
                        
        return game

def password_confirm(game : dict, CONSTS : dict):
        confirm = input("What's your password?")
        if confirm == game[game['suspect']]['password']:
                return True
        else:
                print("That's not your password.")
                return False

def trade_cards(game : dict, CONSTS : dict):
        valid = False
        while not valid:
                other_party = input(f"Who would you like to trade with?").strip().lower()

                try:
                        other_party = int(other_party)
                        if other_party in game["quick_key"]:
                                valid = True
                
                except TypeError:
                        pass

                for player in game["quick_key"]:
                        if game[player]['name'] == other_party:
                                other_party = player
                                valid = True

        valid = False
        while not valid:
                confirm = input(f"Player {other_party}, {game[other_party]['name']}, do you agree to this trade? Hint: you can either check your own deck or type 'Y' or 'N' to confirm.")
                pass

def evaluate_game_state(game : dict, CONSTS : dict):
        for player in game["quick_key"]:

                state = "on"

                if game[player]['VPs'] == 10:
                        state = "ended"
                
                if len(game[player]['roads']) >= 5:
                        for achiever in game["quick_key"]:
                                if game[achiever]['achievements']["longest_road"] == 1:
                                        if len(game[achiever]['roads']) < len(game[player]['roads']):
                                                game[achiever]['achievements']['longest_road'] = 0
                                                game[player]['achievements']['longest_road'] = 1
                
        return state, game

def build(game : dict, CONSTS : dict):
        pass

def main_game(game, CONSTS):
        game["mode"] = "main"

        while game["mode"] == "main":

                for player in game["quick_key"]:
                        while game["player_turn"] == player:

                                game["mode"], game = evaluate_game_state(game, CONSTS)
                                action = input(ansi_stitching(game[player]['color'], f"Player {player}, what's your move?") + "\n> ").strip().lower()

                                if action == "end turn":
                                        game['suspect'] = player
                                        if password_confirm(game, CONSTS):
                                                break

                                elif action == "end turn":
                                        game['suspect'] = player
                                        if password_confirm(game, CONSTS):
                                                trade_cards(game, CONSTS)

                                elif action == "build":
                                        build(game, CONSTS)

                                else:
                                        try:
                                                CONSTS["commands"][action](game, CONSTS)
                                        except KeyError:
                                                print("Oops, that command doesn't exist.")

                        

        return game

def start_game(game : dict, CONSTS : dict):
        game["input type"] = CONSTS["commands"]
        print("Starting your game...")
        time.sleep(1)
        clear_screen()
        game = setup_game(game, CONSTS)
        game = game_stage_1(game, CONSTS)
        print("Great. Your initial setup is complete, so you now have access to the full range of commands. Happy playing.")
        game = main_game(game, CONSTS)
        print("The game's over. You're getting sent back to the main starting programme now.")

def analyse_ownership(game : dict, CONSTS : dict, element):

        element = element[7:]
        counter = 0
        for i in element:
                if i in [";", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        counter += 1

        colors = element[:counter - 1].split(";")
        color = []
        for value in colors:
                if len(value) == 0:
                        value = "0"
                color.append(int(value))

        for player in game["quick_key"]:
                if game[player]['color'] == color:
                        return player

def main():
        CONSTS = {

                "rules": """This is the link to the official Catan Almanac:
https://www.catan.com/sites/default/files/2024-01/Almanac%20CATAN-3D.pdf
If the link doesn't work, please paste it into your browser.""",

                "resources": ["ores", "grain", "wood", "brick", "sheep"],

                "dev_cards": ["knight", "year of plenty", "road building", "monopoly", "VICTORY POINT"],  

                "dev_card_numbers": [14, 2, 2, 2, 5],

                "ports": ["wood", "grain", "cow", "ore", "brick"],
                "welcome_message": """WELCOME TO MY TEXT-BASED CATAN.
Before we start, make sure \x1b[38;2;142;194;21mthis text\x1b[0m is green!
CREDITS: Vivienne, CATAN game studio
ENTER YOUR COMMAND TO BEGIN""",

                "pre_commands" : {
                        "rng": infinite_rng
},

                "commands" : { 
                        "deck": print_own_deck, 
                        "roll": roll_die,
},

                "credits": """The credits for this code are as follows:""",

                "commands info" : """These are the commands available to you and what they mean""",

                "colors" : ["red", "green", "blue"],

                "biomes" : [],

                "number_tokens" : [],

                "road_types" : ["__", "/", "\\"],

                "road_strings" : ["ABCDEF$GHIJKMNOPRSTUVWYZabdefghiklmnpqrstuvwxyz+", 
                        "ADCG$LRXMSHNEIJPQWVbcihnoutyx+rwmsflagOUTZYedjkq",
                        "BEFJDHIOGMLRSYNTXdekjpqvwzsxntiobhWcKQPVUaZfgmlr"],

                "kaomojis" : {
                        "ores": "‧₊˚🗻`",
                        "brick": "↟↟↟↟↟↟",
                        "grain": "˚ʚ🌱₊˚",
                        "wood": " ݁˖𓂃.𖠰.",
                        "sheep": ":3 ^^~", 
                        "desert": " ⛰︎ ོ ༄-"
},
                "settlement_locations" : [],

                "ports" : ["wood", "grain", "sheep", "ore", "brick"],

                "starting_constructs" : {'settlements' : 5, 'cities' : 4, 'paths' : 15},

                "building costs" : """---BUILDING COSTS---
 Road: Wood (1), Brick (1)
 Settlement: Wood (1), Brick (1), Grain (1), Sheep (1)
 City: Ores (3), Grain (2)
 Development cards: Ores (1), Grain (1), Sheep (1)"""

        }

        
        for i in range(10):
                if (i + 2) != 7:
                        for x in range(2):
                                CONSTS["number_tokens"].append(i + 2)
        CONSTS["number_tokens"].append(1)
        CONSTS["number_tokens"].append(12)

        CONSTS["settlement_locations"] = "abcdefghijklmnopqrstuvwxyz".upper()
        CONSTS["settlement_locations"] += CONSTS["settlement_locations"].lower() + "+" + "$"

        for i in range(3):
                
                CONSTS["biomes"].append("ores")
                CONSTS["biomes"].append("brick")

        for i in range(4):
                
                CONSTS["biomes"].append("grain")
                CONSTS["biomes"].append("wood")
                CONSTS["biomes"].append("sheep")

        

        game = {
                "input type" : CONSTS["pre_commands"],
                "on" : True
        }


        print(CONSTS["welcome_message"])

        while True:
        
                action = input("> ").strip().lower()

                if not action in game["input type"] and action in [CONSTS["commands"], CONSTS["pre_commands"]]:
                        print("That command's not available right now. Please enter something allowed in the commands.")

                elif action == "fahh":
                        analyse_ownership({}, {}, "\x1b[38;2;142;194;21mthis text\x1b[0m")

                elif action == "ru":
                        print(CONSTS["rules"])

                elif action == "cr":
                        print(CONSTS["credits"])

                elif action == "pcl":
                        print(CONSTS["commands info"])

                elif action == "pbc":
                        print(CONSTS["building costs"])

                elif action == 'start':
                        start_game(game, CONSTS)

                elif action == 'end':
                        break
                        
                else:
                        try:
                                CONSTS["pre_commands"][action](game, CONSTS)
                        except KeyError:
                                print("That command doesn't seem to exist. Do you want to check commands with 'pcl'?")

if __name__ == "__main__":
        main()
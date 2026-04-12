import random

grid_1 = """                                                                3:1 port                                                                                                                                                                           
                                                                 /      \\
                                                                /        \\                                                                                
                    sea                                      A __ __ __ __ B                  sea                                             
                                                             /              \\                                                                   
                                                            /                \\                                                                 
                                                                                                                                                               
                                   2:1 grain port         /       ݁ ˖𓂃.𖠰       \\               3:1 port                                        
                                    |    \\   __ __ __ __ /          12          \\ __ __ __ __    /                                        
                                    |   C /           D  \\         Wood         / E        F  \\     |                                           
                                    |    /                \\         S1         /               \\    |                                          
                                    |                                                               |                                           
                                    |  /    ˚ʚ 🌱 ₊˚✧       \\                /      𐔌՞. .՞𐦯     \\   |                                                             
                      $__ __ __ __ G  /           3        H \\  __ __ __ __ / I        6        J \\ | __ __ __ __ K                                  
                     /                \\       Grain :)       /              \\       Sheep!        /              \\                                  
                    /                  \\         S2         /                \\        S3         /                \\                                  
                                                                                                                                                    
                  /     ˚ʚ 🌱 ₊˚✧       \\                 /        ⛰︎ ོ ༄        \\               /      ᨒ↟ 𖠰         \\                                  
               L /          5           M \\  __ __ __ __ /N         N\\A       O \\ __ __ __ __ / P        6           \\ Q                                  
                 \\        Grain :)        /              \\       Desert ^^     /              \\        Brick         /                                  
                  \\         S4           /                \\         S5        /                \\         S6         /                                  
                                                                                                                                                                 
                    \\                  /        ᨒ↟ 𖠰       \\                /     ‧₊˚🗻`˖*⋆      \\               /                                  
   2:1 wood port - R \\ __ __ __ __ S  /          5         T \\ __ __ __ __ / U        2          V\\ __ __ __ __ /W _ _ _  2:1 sheep port                 
        \\            /                \\         Brick         /             \\        Ores         /             \\         /                             
         \\          /                  \\         S7          /               \\         S8        /               \\       /                               
          \\                                                                                                             /                      
           \\      /       ݁ ˖𓂃.𖠰         \\                  /   ‧₊˚🗻`˖*⋆       \\               /      ᨒ↟ 𖠰         \\   /                                  
               Q /           4           Y\\  __ __ __ __Z /          6         a\\ __ __ __ __ /b        2           \\ c                                  
                 \\          Wood          /               \\         Ores        /              \\       Brick          /                                  
                  \\          S9          /                 \\        S10        /                \\       S11         /                                  
                                                                                                                                               
                    \\                  /      ˚ʚ 🌱 ₊˚✧      \\                /     ˖𓂃.𖠰           \\              /                                  
                    d\\ __ __ __ __  e /          9          f \\  __ __ __ __g/         10          h\\ __ __ __ __ /i                                  
                     /                \\         Grain :)      /              \\        Wood          /             \\                                  
                    /                  \\         S12         /                \\        S13         /               \\                                  
                                                                                                                                                                                 
                  /          𐔌՞. .՞𐦯      \\               /        𐔌՞. .՞𐦯     \\                 /       𐔌՞. .՞𐦯     \\                                  
                j/           8           k\\  __ __ __ __ l/          10        m \\ __ __ __ __n /          3          \\o                                  
                  \\        Sheep!         /               \\         Sheep!       /              \\       Sheep!        / \\                                  
              /    \\        S14          /                 \\         S15        /                \\       S16         /   \\                                                     
             /                                                                                                           \\                                                                
            /       \\                  /      ݁ ˖𓂃.𖠰         \\                 /      ‧₊˚🗻`˖*⋆     \\               /       \\                                   
 2:1 brick port _  p \\ __ __ __ __  q /           1         r \\  __ __ __ __s/          11        t \\ __ __ __ __ /u  _ _ 3:1 port                                  
                                      \\          Wood         /               \\        Ores         /                                                                   
                                       \\         S17         /                 \\        S18        /                                                               
                                                                                                                                                                        
                                         \\                 /     ˚ʚ 🌱 ₊˚✧       \\               /                                                                                     
                                          \\ v __ __ __ __ w           11         x\\ __ __ __ __ / y                                                        
                                                          \\        Grain :)       /                                                                       
                                            \\           /  \\         S19         /  \\          /                                                             
                                             \\         /                             \\        /                                                           
                                              \\       /      \\                 /      \\      /                                                                                   
                                             2:1 ore port     \\z __ __ __ __  /+      3:1 port 
"""

#123456
#‧₊˚🗻`
print(grid_1)

for line in grid_1.splitlines():
    line = line.rstrip()
    print(line)

tiles = {}

for i in range(19):
    tiles[("S"+str(i+1))] = {}

print(tiles)

biomes = []
for i in range(3):
    biomes.append("ores")
    biomes.append("brick")
for i in range(4):
    biomes.append("grain")
    biomes.append("wood")
    biomes.append("sheep")


number_tokens = []
for i in range(10):
    if (i + 2) != 7:
        for x in range(2):
            number_tokens.append(i + 2)
number_tokens.append(1)
number_tokens.append(12)

print(number_tokens)

print("biomes", biomes)

desert_placement = random.randint(1, 19)
tiles[("S"+str(desert_placement))]["biome"] = "desert"
tiles[("S"+str(desert_placement))]["number"] = 7

for i in range(18):

    try:
        x = tiles[("S"+str(i+1))]["biome"] != "desert"
            
    except KeyError:
        random.shuffle(biomes)
        chosen_biome = biomes.pop()
        tiles[("S"+str(i+1))]["biome"] = chosen_biome

        random.shuffle(number_tokens)
        chosen_number = number_tokens.pop()
        tiles[("S"+str(i+1))]["number"] = chosen_number

kaomojis = {
    "ores": "‧₊˚🗻`",
    "brick": "↟↟↟↟↟↟",
    "grain": "˚ʚ🌱₊˚",
    "wood": " ݁˖𓂃.𖠰.",
    "sheep": ":3 ^^~", 
    "desert": " ⛰︎ ོ ༄-"
}

tiles["S1"]["roads"] = []
counter = 0
roads_string = "ABBEEIIHHDDA"
for i in range((len(roads_string))//2):

    road = ""
    road += roads_string[counter]
    counter += 1
    road += roads_string[counter]
    counter += 1
    
    if road[0] > road[1]:
        road = road[1] + road[0]
    tiles["S1"]["roads"].append(road)
    
print(f'\n\n\n\n\n{tiles["S1"]["roads"]}\n\n\n\n')
    

print(tiles)

possible_locs = "abcdefghijklmnopqrstuvwxyz".upper()
possible_locs = possible_locs + possible_locs.lower()
possible_locs = possible_locs + "+"
settlement_locs = {}

for letter in possible_locs:
    settlement_locs[letter] = {"display": letter}
    settlement_locs[letter]["port"] = ""


for loc in "ABFJouxy":
    settlement_locs[loc]["port"] = {"3:1 port"}
i = 0
ports = ["wood", "grain", "sheep", "ore", "brick"]
reps = 0
for loc in "RQCGWcvwjp":
    reps += 1
    thing_to_put = f"2:1 {ports[i]} port"
    settlement_locs[loc]["port"] = thing_to_put
    if reps%2 == 0:
        i += 1

routes = "ABBEEIIHHDDA"

print(settlement_locs)


print("\n\n\n\n\n")
grid_part_1 = (
    #line 1
    (" " * 65) + "3: 1 port" + "\n" +
    #line 2
    (" " * 65) + "/      \\" + "\n" +
    #line 3
    (" " * 64) + "/        \\" + "\n" +
    #line 4
    (" " * 20) + "sea" + (" " * 38) + settlement_locs["A"]["display"] + " __ __ __ __ " + settlement_locs["B"]["display"] + (" " * 38) + "sea" + "\n" +
    #line 5
    (" " * 61) + ("/              \\") + "\n" +
    #line 6 & 7
    (" " * 60) + ("/                \\") + "\n\n" +
    #line 8
    (" " * 35) + ("2:1 grain port") + (" " * 9) + "/" + (" " * 7) + kaomojis[tiles["S1"]["biome"]] + (" "* 7) + "\\" + (" " * 16) + "3:1 port" + "\n" +
    #line 9
    (" " * 36) + "|    \\   __ __ __ __ /" + (" " * 10) + str(tiles["S1"]["number"]) + (" " * 11 if len(str(tiles["S1"]["number"])) == 1 else " " * 10) + "\\ __ __ __ __    /  |\n" +
    #line 10
    (" " * 36) + "|" + (" " * 3) + settlement_locs["C"]["display"] + (" /") + (" " * 11) + settlement_locs["D"]["display"] + "  \\" 
    + (" " * ((22 - len(str(tiles["S1"]["biome"])))//2)) + tiles["S1"]["biome"] + 
    (" " * (((22-len(str(tiles["S1"]["biome"])))//2)+ (1 if len(str(tiles["S1"]["biome"]))%2 != 0 else 0)))
    + "/ " + settlement_locs["E"]["display"] + (" " * 8) + settlement_locs["F"]["display"] + "  \\     |\n" +
    #line 11
    (" " * 36) + "|" + "    /" +  (" " * 16) + "\\" + (" " * 9) + "S1" + (" " * 9) + "/" + (" " * 15) + "\\    |" + "\n" +
    #line 12
    (" " * 36) + "|" + (" " * 63) + "|" + "\n" +
    #line 13
    (" " * 36) + "|" + "  /" + (" " * 7) + kaomojis[tiles["S2"]["biome"]] + (" " * 7) + "\\" 
    + (" " * 16) + "/ "  + (" " * 6) + (kaomojis[tiles["S3"]["biome"]]) 
    + (" " * 6) + "\\  |\n" +
    #line 14
    (" " * 23) + ("__ " * 4) + settlement_locs["G"]["display"] + "  /" + (" " * 10) + str(tiles["S2"]["number"]) + 
    (" " * 9 if len(str(tiles["S2"]["number"])) == 1 else " " * 8) + settlement_locs["H"]["display"] + " \\ " + (" __" * 4) + " / " + settlement_locs["I"]["display"] +
    (" " * 8) + str(tiles["S3"]["number"]) + (" " * 8 if len(str(tiles["S3"]["number"])) == 1 else " " * 7) + settlement_locs["J"]["display"] + " " + "\\" + " | " + ("__ " * 4) 
    + settlement_locs["K"]["display"] + "\n" +
    #line 15
    (" " * 21) + "/" + (" " * 16) + "\\" + (" " * ((22 - len(str(tiles["S2"]["biome"])))//2)) + tiles["S2"]["biome"] + (" " * 9 if tiles["S2"]["biome"] != "desert" else " " * 8)
    + "/" + (" " * 14) + "\\" + (" " * ((21 - len(str(tiles["S3"]["biome"])))//2)) + tiles["S3"]["biome"] + (" " * ( (21 - len(tiles["S3"]["biome"])) //2   ) ) + 
    (" " * (1 if len(tiles["S3"]["biome"]) % 2 != 1 else 0)) + "/" + (" " * 14) + "\\" + "\n" +
    #line 16 & 17 
    (" " * 20) + "/" + (" " * 18) + "\\" + (" " * 9) + "S2" + (" " * 9) + "/" + (" " * 16) + "\\" + (" " * 8) + "S3" + (" " * 9) + "/" + (" " * 16) + "\\" + "\n\n" +
    #line 18
    (" " * 18) + "/" + (" " * 8) + kaomojis[tiles["S4"]["biome"]] + (" " * 8) + "\\" + (" " * 16) + "/" + (" " * 7) + kaomojis[tiles["S5"]["biome"]] + (" " * 7) + "\\"
    + (" " * 15) + "/" + (" " * 7) + kaomojis[tiles["S6"]["biome"]] + (" " * 7) + "\\" + "\n" + 
    #line 19
    (" " * 15) + settlement_locs["L"]["display"] + " " + "/" + (" " * 11) + str(tiles["S4"]["number"]) + (" " * (10 if len(str(tiles["S4"]["number"])) == 1 else 9)) + settlement_locs["M"]["display"] +
    " " + "\\" + "  " + ("__ " * 4) + "/" + settlement_locs["N"]["display"] + (" " * 9) + str(tiles["S5"]["number"]) + (" " * 9 if len(str(tiles["S5"]["number"])) == 1 else " " * 8) + settlement_locs["O"]["display"] +
    " " + "\\" + " " + ("__ " * 4) + "/" + " " + settlement_locs["P"]["display"] + (" " * 8) + str(tiles["S6"]["number"]) + (" " * 11 if len(str(tiles["S6"]["number"])) == 1 else " " * 10) + "\\"
    + " " + settlement_locs["Q"]["display"] + "\n" +
    #line 20
    (" " * 17) + "\\" + (" " * ((24 - len(str(tiles["S4"]["biome"])))//2)) + tiles["S4"]["biome"] + (" " * 10 if tiles["S4"]["biome"] != "desert" else " " * 9) + "/" + (" " * 14) + "\\" +
    (" " * ((22 - len(str(tiles["S5"]["biome"])))//2)) + tiles["S5"]["biome"] + (" " * 9 if tiles["S5"]["biome"] != "desert" else " " * 8) + "/" + (" " * 13) + "\\" +
    (" " * ((22 - len(str(tiles["S6"]["biome"])))//2)) + tiles["S6"]["biome"] + (" " * 9 if tiles["S6"]["biome"] != "desert" else " " * 8) + "/" + "\n" +
    #line 21 & 22
    (" " * 18) + "\\" + (" " * 10) + "S4" + (" " * 10) + "/" + (" " * 16) + "\\" + (" " * 9) + "S5" + (" " * 9) + "/" + (" " * 15) + "\\" + (" " * 9) + "S6" + (" " * 9) + "/" + "\n\n" +
    #line 23
    (" " * 20) + "\\" + (" " * 18) + "/" + (" " * 7) + kaomojis[tiles["S7"]["biome"]] + (" " * 7) + "\\" + (" " * 16) + "/" + (" " * 7) + kaomojis[tiles["S8"]["biome"]]  + (" " * 6) + "\\" +
    (" " * 16) + "/"
    
)

grid_part_2 = (
    #line 24
    (" " * 3) + "2:1 wood port - " + settlement_locs["R"]["display"] + " " + "\\" + "  " + ("__ " * 4) + settlement_locs["S"]["display"] + " " + "/" + (" " * 10) + str(tiles["S7"]["number"]) + 
    (" " * 8 if len(str(tiles["S7"]["number"])) == 1 else " " * 7) + settlement_locs["T"]["display"] + "  " + "\\" + "  " + ("__ " * 4) + "/" + " " + settlement_locs["U"]["display"] +
    (" " * 8) + str(tiles["S8"]["number"]) + (" " * 8 if len(str(tiles["S8"]["number"])) == 1 else " " * 7) + settlement_locs["V"]["display"] + " " + "\\" + " " + ("__ " * 4) + " " + "/" + 
    settlement_locs["W"]["display"] +  " _ _ _  2:1 sheep port" + "\n" +
    #line 25
    (" " * 8) + "\\" + (" " * 12) + "/" + (" " * 16) + "\\" + (" " * ((22 - len(str(tiles["S7"]["biome"])))//2)) + tiles["S7"]["biome"] + 
    (" " * (((22-len(str(tiles["S7"]["biome"])))//2) + (1 if len(str(tiles["S7"]["biome"]))%2 != 0 else 0))) + "/" + (" " * 14) + "\\" +
    (" " * ((21 - len(str(tiles["S8"]["biome"])))//2)) + tiles["S8"]["biome"] + 
    (" " * (((21-len(str(tiles["S8"]["biome"])))//2) + (1 if len(str(tiles["S8"]["biome"]))%2 != 1 else 0))) + "/" + (" " * 14) + "\\" + "         /\n" +
    #line 26
    (" " * 9) + "\\" + (" " * 10) + "/" + (" " * 18) + "\\" + (" " * 9) + "S7" + (" " * 9) + "/" + (" " * 16) + "\\" + (" " * 8) + "S8" + (" " * 9) + "/" + (" " * 16) + "\\" + "       /" + "\n" +
    #line 27
    (" " * 10) + "\\" + (" " * 110) + "/" + "\n" +
    #line 28
    (" " * 11) + "\\" + (" " * 6) + "/" + (" " * 8) + kaomojis[tiles["S9"]["biome"]] + (" " * 8) + "\\" + (" " * 16) + "/" + (" " * 6) + kaomojis[tiles["S10"]["biome"]] + (" " * 8) + "\\"
    + (" " * 15) + "/" + (" " * 7) + kaomojis[tiles["S11"]["biome"]] + (" " * 7) + "\\" + "   /" + "\n" +
    #line 29
    (" " * 12) + "\\  " + settlement_locs["Q"]["display"] + " " + "/" + (" " * 12) + str(tiles["S9"]["number"]) + (" " * 9 if len(str(tiles["S9"]["number"])) == 1 else " " * 8) 
    + settlement_locs["Y"]["display"] + " " + "\\" + " " + ("__ " * 4) + settlement_locs["Z"]["display"] + "/" + (" " * 10) + str(tiles["S10"]["number"]) + 
    (" " * 9 if len(str(tiles["S10"]["number"])) == 1 else " " * 8) + settlement_locs["a"]["display"] + " " + "\\" + (" __" * 4) + settlement_locs["b"]["display"] + "/" +
    (" " * 10) + str(tiles["S11"]["number"]) + (" " * 11 if len(str(tiles["S11"]["number"])) == 1 else " " * 10) + "\\" + " " + settlement_locs["c"]["display"] + "\n" +
    #line 30
    (" " * 17) + "\\" + (" " * ((24 - len(str(tiles["S9"]["biome"])))//2)) + tiles["S9"]["biome"] + (" " * (((24-len(str(tiles["S9"]["biome"])))//2) + (1 if len(str(tiles["S9"]["biome"]))%2 != 0 else 0))) 
    + "/" + (" " * 14) + "\\" + (" " * ((22 - len(str(tiles["S10"]["biome"])))//2)) + tiles["S10"]["biome"] + 
    (" " * (((22-len(str(tiles["S10"]["biome"])))//2) + (1 if len(str(tiles["S10"]["biome"]))%2 != 0 else 0))) + "/" + (" " * 13) + "\\" +
    (" " * ((22 - len(str(tiles["S11"]["biome"])))//2)) + tiles["S11"]["biome"] + 
    (" " * (((22-len(str(tiles["S11"]["biome"])))//2) + (1 if len(str(tiles["S11"]["biome"]))%2 != 0 else 0))) + "/" + "\n" +
    #line 31 & 32
    (" " * 18) + "\\" + (" " * 10) + "S9" + (" " * 10) + "/" + (" " * 16) + "\\" + (" " * 8) + "S10" + (" " * 9) + "/" + (" " * 15) + "\\" + (" " * 8) + "S11" + (" " * 9) + "/" + "\n\n" +
    #line 33
    (" " * 20) + "\\" + (" " * 18) + "/" + (" " * 7) + kaomojis[tiles["S12"]["biome"]] + (" " * 7) + "\\" + (" " * 16) + "/" + (" " * 6) + kaomojis[tiles["S13"]["biome"]] + (" " * 7) + "\\" + (" " * 16) + "/" 
    + "\n" +
    #line 34
    (" " * 19) + settlement_locs["d"]["display"] + " " + "\\" + "  " + ("__ " * 4) + settlement_locs["e"]["display"] + " " + "/" + (" " * 10) + 
    str(tiles["S12"]["number"]) + (" " * 9 if len(str(tiles["S12"]["number"])) == 1 else " " * 8) + settlement_locs["f"]["display"] + " " + "\\" + " " + ("__ " * 4) + settlement_locs["g"]["display"] + "/" +
    (" " * 10) + str(tiles["S13"]["number"]) + (" " * 8 if len(str(tiles["S13"]["number"])) == 1 else " " * 7) + settlement_locs["h"]["display"] + " " + "\\" + " " + ("__ " * 4) + " " + "/" + " " 
    + settlement_locs["i"]["display"] + "\n" +
    #line 35
    (" " * 21) + "/" + (" " * 16) + "\\" + (" " * ((23 - len(str(tiles["S12"]["biome"])))//2)) + tiles["S12"]["biome"] + 
    (" " * (((21-len(str(tiles["S12"]["biome"])))//2) + (1 if len(str(tiles["S12"]["biome"]))%2 != 1 else 0))) + "/" + (" " * 14) + "\\"
    + (" " * ((21 - len(str(tiles["S13"]["biome"])))//2)) + tiles["S13"]["biome"] + 
    (" " * (((21-len(str(tiles["S13"]["biome"])))//2) + (1 if len(str(tiles["S13"]["biome"]))%2 != 1 else 0))) + "/" + (" " * 14) + "\\" + "\n" +
    #line 36 & 37
    (" " * 20) + "/" + (" " * 18) + "\\" + (" " * 8) + "S12" + (" " * 9) + "/" + (" " * 16) + "\\" + (" " * 8) + "S13" + (" " * 8) + "/" + (" " * 16) + "\\" + "\n\n" )

grid_part_3 = (
    #line 38 
    (" " * 18) + "/" + (" " * 8) + kaomojis[tiles["S14"]["biome"]] + (" " * 8) + "\\" + (" " * 16) + "/" + (" " * 7) + kaomojis[tiles["S15"]["biome"]] + (" " * 7) + "\\" + (" " * 15) + "/" + (" " * 7) + kaomojis[tiles["S16"]["biome"]] + (" " * 7)
    + "\\" + "\n" +
    #line 39
    (" " * 15) + settlement_locs["j"]["display"] + " " + "/" + (" " * 11) + str(tiles["S14"]["number"]) + (" " * 10 if len(str(tiles["S14"]["number"])) == 1 else " " * 9) + settlement_locs["k"]["display"]
    + " " + "\\" + " " + ("__ " * 4) + settlement_locs["l"]["display"] + "/" + (" " * 10) + str(tiles["S15"]["number"]) + (" " * 9 if len(str(tiles["S15"]["number"])) == 1 else " " * 8)
    + settlement_locs["m"]["display"] + " " + "\\" + " " + ("__ " * 4) + "/" + settlement_locs["n"]["display"] + (" " * 9) + str(tiles["S16"]["number"]) + 
    (" " * 11 if len(str(tiles["S16"]["number"])) == 1 else " " * 10) + "\\" + settlement_locs["o"]["display"] + "\n" +
    #line 40
    (" " * 17) + "\\" + (" " * ((24 - len(str(tiles["S14"]["biome"])))//2)) + tiles["S14"]["biome"] +
    (" " * (((24-len(str(tiles["S14"]["biome"])))//2) + (1 if len(str(tiles["S14"]["biome"]))%2 != 0 else 0))) + "/" + (" " * 14) + "\\" +
    (" " * ((22 - len(str(tiles["S15"]["biome"])))//2)) + tiles["S15"]["biome"] + 
    (" " * (((22-len(str(tiles["S15"]["biome"])))//2) + (1 if len(str(tiles["S15"]["biome"]))%2 != 0 else 0))) + "/" + (" " * 13) + "\\" +
    (" " * ((22 - len(str(tiles["S16"]["biome"])))//2)) + tiles["S16"]["biome"] + 
    (" " * (((22 - len(str(tiles["S16"]["biome"])))//2) + (1 if len(str(tiles["S16"]["biome"]))%2 != 0 else 0))) + "/" + "\n" +
    #line 41 
    (" " * 14) + "/" + (" " * 3) + "\\" + (" " * 9) + "S14"  + (" " * 10) + "/" + (" " * 16) + "\\" + (" " * 8) + "S15" + (" " * 9) + "/" + (" " * 15) + "\\" + (" " * 8) + "S16" + (" " * 9) + "/" + 
    (" " * 3) + "\\" + "\n" +
    #line 42
    (" " * 13) + "/" + (" " * 107) + "\\" + "\n" +
    #line 43
    (" " * 12) + "/" + (" " * 7) + "\\" + (" " * 18) + "/" + (" " * 7) + kaomojis[tiles["S17"]["biome"]] + (" " * 7) + "\\" + (" " * 16) + "/" + (" " * 6) + kaomojis[tiles["S18"]["biome"]] + (" " * 7)
    + "\\" + (" " * 16) + "/" + (" " * 7) + "\\" + "\n" +
    #line 44
    " 2:1 brick port _  " + settlement_locs["p"]["display"] + " " + "\\" + " " + ("__ " * 4) + " " + settlement_locs["q"]["display"] + " " + "/" + (" " * 11) + str(tiles["S17"]["number"]) +
    (" " * 8 if len(str(tiles["S17"]["number"])) == 1 else " " * 7) + settlement_locs["r"]["display"] + " " + "\\" + " " + ("__ " * 4) + settlement_locs["s"]["display"] +"/" + (" " * 10) + 
    str(tiles["S18"]["number"]) + (" " * 8 if len(str(tiles["S18"]["number"])) == 1 else " " * 7) + settlement_locs["t"]["display"] + " " + "\\" + " " + ("__ " * 4) + " " + "/" +
    settlement_locs["u"]["display"] + "  _ _ 3:1 port" + "\n" +
    #line 45
    (" " * 38)
)



print(grid_part_1)
print(grid_part_2)
print(grid_part_3)

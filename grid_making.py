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
                       __ __ __ __ G  /           3        H \\  __ __ __ __ / I        6        J \\ | __ __ __ __ K                                  
                     /                \\       Grain :)       /              \\       Sheep!        /              \\                                  
                    /                  \\         S2         /                \\        S3         /                \\                                  
                                                                                                                                                    
                  /     ˚ʚ 🌱 ₊˚✧       \\                 /        ⛰︎ ོ ༄        \\               /      ᨒ↟ 𖠰         \\                                  
               L /          5           M \\  __ __ __ __ /N         N\\A       O \\ __ __ __ __ / P        6           \\ Q                                  
                 \\        Grain :)        /              \\       Desert ^^     /              \\        Brick         /                                  
                  \\         S4           /                \\         S5        /                \\         S6         /                                  
                                                                                                                                                                 
                    \\                  /        ᨒ↟ 𖠰       \\                /     ‧₊˚🗻`˖*⋆      \\               /                                  
   2:1 wood port - R \\ __ __ __ __ S  /          5         T \\ __ __ __ __ / U        2          V\\ __ __ __ __ /W _ _ _  2:1 cow port                 
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

print(grid_1)

for line in grid_1.splitlines():
    line = line.rstrip()
    print(line)

tiles = {}

for i in range(19):
    tiles[("S"+str(i+1))] = {}

for tile in tiles:
    print("x")

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
    "ores": "‧₊˚🗻`˖*⋆",
    "brick": "ᨒ↟ 𖠰",
    "grain": "˚ʚ 🌱 ₊˚✧",
    "wood": " ݁ ˖𓂃.𖠰",
    "sheep": "𐔌՞. .՞𐦯", 
    "desert": "⛰︎ ོ ༄"
}

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
ports = ["wood", "grain", "cow", "ore", "brick"]
reps = 0
for loc in "RQCGWcvwjp":
    reps += 1
    thing_to_put = f"2:1 {ports[i]} port"
    settlement_locs[loc]["port"] = thing_to_put
    if reps%2 == 0:
        i += 1



print(settlement_locs)

encoded_grid = (
    (" " * 65) + "3: 1 port" + "\n" +
    #line 2
    (" " * 65) + "/      \\" + "\n" +
    #line 3
    (" " * 64) + "/        \\" + "\n" +
    #line 4
    (" " * 20) + "sea" + (" " * 38) + settlement_locs["A"]["display"] + " __ __ __ __ " + settlement_locs["B"]["display"] + (" " * 38) + "sea" + "\n" +
    #line 5 
    (" " * 61) + ("/              \\") + "\n" +
    #line 6
    (" " * 60) + ("/                \\") + "\n" +
    #line 7
    "\n" +
    #line 8
    (" " * 35) + ("2:1 grain port") + (" " * 9) + "/" + (" " * ((20 - (len(kaomojis[tiles["S1"]["biome"]])))//2)) + (kaomojis[tiles["S1"]["biome"]]) + (" " * ((20 - (len(kaomojis[tiles["S1"]["biome"]])))//2)) + (" " * ((20 - (len(kaomojis[tiles["S1"]["biome"]])))% 2)) + "\\" + (" " * 15) + "3:1 port" + "\n" +
    #line 9
    (" " * 36) + "|    \\   __ __ __ __ /" + (" " * ((22 - len(str(tiles["S1"]["number"])))//2)) + str(tiles["S1"]["number"]) + (" " * ((22 - len(str(tiles["S1"]["number"])))//2)) + "\\ __ __ __ __    /   |" + "\n" +
    #line 10
    (" " * 36) + "|" + (" " * 3) + settlement_locs["C"]["display"] + (" /") + (" " * 11) + settlement_locs["D"]["display"] + "  \\" + (" " * ((22 - len(str(tiles["S1"]["biome"])))//2)) + tiles["S1"]["biome"] + (" " * 9) + "/ " + settlement_locs["E"]["display"] + (" " * 8) + settlement_locs["F"]["display"] + "  \\     |"
)





print(encoded_grid)


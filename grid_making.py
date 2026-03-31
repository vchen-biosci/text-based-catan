import random

grid_1 = """\n                                                                 3:1 port                                                                                                                                                                           
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
\n"""

print(grid_1)

for line in grid_1.splitlines():
    line = line.rstrip()
    print(line)

    "𐔌՞. .՞𐦯"

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


encoded_grid = (
    "\n" + 
    #line 1
    (" " * 65) + "3: 1 port"
    #line 2
    #wait im confused how should i do this?? with a class, dictionary, array, list?

)



print(encoded_grid)


#i used \\ to escape my escape and just print \ (i found this on a useful reddit thread yay), so ik it looks weird but it wont
text = """
                                                               3:1 port                                                                                                                                                                           
                                                                 /      \\                                                                                 
                                                                /        \\                                                                                
                    sea                                      A __ __ __ __ B                  sea                               
                                                             /              \\                                                                   
                                                            /                \\                                                                
                                                                                                                                                               
                                   2:1 grain port         /       ݁ ˖𓂃.𖠰       \\               3:1 port                                       
                                    |    \\   __ __ __ __ /          12          \\ __ __ __ __    /                                       
                                    |   C /           D  \\         Wood         / E        F  \\    |                                          
                                    |    /                \\         S1         /               \\   |                                         
                                    |                                                                |                                          
                                    |  /    ˚ʚ 🌱 ₊˚✧       \\                /    ૮꒰ ˶• ༝ •˶꒱ა    \\  |                                                             
                       __ __ __ __ G  /           3        H \\  __ __ __ __ / I       6        J \\ | __ __ __ __ K                                  
                     /                \\       Grain :)       /              \\        Sheep!        /              \\                                  
                    /                  \\         S2         /                \\        S3          /                \\                                  
                                                                                                                                                    
                  /     ˚ʚ 🌱 ₊˚✧       \\                 /       ⛰︎ ོ ༄       \\                 /      ᨒ↟ 𖠰        \\                                  
               L /          5           M \\  __ __ __ __ /N         N\\A       O \\ __ __ __ __ / P        6           \\ Q                                  
                 \\        Grain :)        /               \\       Desert ^^     /             \\        Brick         /                                  
                  \\         S4           /                 \\         S5        /               \\         S6         /                                  
                                                                                                                                                                 
                    \\                  /        ᨒ↟ 𖠰        \\               /     ‧₊˚🗻`˖*⋆      \\               /                                  
   2:1 wood port - R \\ __ __ __ __ S  /          5          T \\ __ __ __ __ / U        2           V\\ __ __ __ __ /W _ _ _  2:1 cow port                 
        \\            /                \\         Brick         /             \\        Ores          /             \\         /                             
         \\          /                  \\         S7          /               \\         S8         /               \\       /                               
         \\                                                                                                 /                      
            \\     /       ݁ ˖𓂃.𖠰         \\                 /    ‧₊˚🗻`˖*⋆     \\                 /      ᨒ↟ 𖠰        \\    /                                  
               Q /           4           Y\\  __ __ __ __Z /          6         a\\ __ __ __ __  /b        2            \\ c                                  
                 \\          Wood          /               \\         Ores        /              \\       Brick          /                                  
                  \\          S9          /                 \\        S10        /                \\       S11         /                                  
                                                                                                                                               
                    \\                  /      ˚ʚ 🌱 ₊˚✧      \\                /     ˖𓂃.𖠰          \\               /                                  
                    d\\ __ __ __ __  e /          9          f \\  __ __ __ __g/         10          h\\ __ __ __ __ /i                                  
                     /                \\         Grain :)      /              \\        Wood          /             \\                                  
                    /                  \\         S12         /                \\        S13         /               \\                                  
                                                                                                                                                                                 
                  /     ૮꒰ ˶• ༝ •˶꒱ა      \\                 /    ૮꒰ ˶• ༝ •˶꒱ა     \\                 /   ૮꒰ ˶• ༝ •˶꒱ა     \\                                  
                j/           8           k\\  __ __ __ __ l/          10        m \\ __ __ __ __n /          3          \\o                                  
                  \\        Sheep!         /               \\         Sheep!       /              \\       Sheep!       / \\                                  
              /    \\        S14          /                 \\         S15        /                \\       S16        /   \\                                                     
             /                                                                                                           \\                                                                
            /       \\                  /      ݁ ˖𓂃.𖠰         \\                /      ‧₊˚🗻`˖*⋆      \\              /       \\                                   
 2:1 brick port _  p \\ __ __ __ __  q /           1         r \\  __ __ __ __s/          11        t \\ __ __ __ __/u  _ _ 3:1 port                                  
                                      \\          Wood         /               \\        Ores         /                                                                   
                                       \\         S17         /                 \\        S18        /                                                               
                                                                                                                                                                        
                                         \\                 /     ˚ʚ 🌱 ₊˚✧      \\                /                                                                                     
                                          \\ v __ __ __ __ w           11         x\\ __ __ __ __ / y                                                        
                                                          \\        Grain :)       /                                                                       
                                            \\           /  \\         S19         /  \\          /                                                             
                                             \\         /                             \\        /                                                           
                                              \\       /      \\                 /      \\      /                                                                                   
                                             2:1 ore port     \\z __ __ __ __  /+      3:1 port                                                                                                     








"""

print(text)

class Grid:
    def __init__(self):
        self.full_grid = full_grid

##this is how im going to add stuff to the thing
##im not sure yet if im going to enf up being a meow meower
##what i meant to say is that im not sure if im going to end up classing each line of self somehow (its a lot of lines of code but i can automate it with python then copy and past it into python) or use a list. even then, should i add them one by one? or i can directly define it. I techincally dont need to individually define the lines I guess, but idkkkk
full_grid = []
for i in range(53):
    full_grid.append([f"line {i+1}"])

#this is how im gonna call singular lines
for i in full_grid:
    print(i[0])

full_grid[0].append(" "*63)

print(len("                                                               "))
print(full_grid[0][1] + "meow")
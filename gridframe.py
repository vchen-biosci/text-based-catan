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
               X /           4           Y\\  __ __ __ __Z /          6         a\\ __ __ __ __ /b        2           \\ c                                  
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

existing_roads = "ABBEEFFJJKKQQWWcciioouuttyyxx++zzwwvvqqppjjddXXRRLL$$GGCCDDADHHIIEGMMNNHIOOPPJRSSMNTTUUOPVVWSYYZZTUaabbVdeeYZffggabhhiekkllfgmmnnhpqqklrrssmnttuvwwrsxxyz+"
roads = []

counter = 0

for i in range(len(existing_roads)//2):

        road = ""
        road += existing_roads[counter]
        counter += 1
        road += existing_roads[counter]
        counter += 1
        
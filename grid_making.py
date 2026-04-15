import random


def ansi_stitching(color : list, text):
        
        colored_ver = ""
        colored_ver += "\x1b[38;2;"

        reps = 0
        for value in color:
                colored_ver += str(value)
                reps += 1

                if reps != 3:
                        colored_ver += ";"
        
        colored_ver += "m"
        colored_ver += text
        colored_ver += "\x1b[0m"

        return colored_ver

def quick_reorder(road : str):

        if road[0] > road[1]:
                road = road[1] + road[0]

        return road

ports = ["wood", "grain", "sheep", "ore", "brick"]

def create_biomes():
        biomes = []
        for i in range(3):
                
                biomes.append("ores")
                biomes.append("brick")

        for i in range(4):
                
                biomes.append("grain")
                biomes.append("wood")
                biomes.append("sheep")

        return(biomes)

biomes = create_biomes()

number_tokens = []
for i in range(10):
        if (i + 2) != 7:
                for x in range(2):
                        number_tokens.append(i + 2)
number_tokens.append(1)
number_tokens.append(12)

kaomojis = {
    "ores": "‧₊˚🗻`",
    "brick": "↟↟↟↟↟↟",
    "grain": "˚ʚ🌱₊˚",
    "wood": " ݁˖𓂃.𖠰.",
    "sheep": ":3 ^^~", 
    "desert": " ⛰︎ ོ ༄-"
}

tiles = {}
for i in range(19):
        tiles[("S"+str(i+1))] = {}

desert_placement = random.randint(1, 19)
tiles[("S"+str(desert_placement))]["biome"] = "desert"
tiles[("S"+str(desert_placement))]["number"] = 7

for i in range(19):

        try:
                x = tiles[("S"+str(i+1))]["biome"] != "desert"
            
        except KeyError:
                random.shuffle(biomes)
                chosen_biome = biomes.pop()
                tiles[("S"+str(i+1))]["biome"] = chosen_biome

                random.shuffle(number_tokens)
                chosen_number = number_tokens.pop()
                tiles[("S"+str(i+1))]["number"] = chosen_number


possible_locs = "abcdefghijklmnopqrstuvwxyz".upper()
possible_locs = possible_locs + possible_locs.lower()
possible_locs = possible_locs + "+" + "$"
settlement_locs = {}

for letter in possible_locs:
        
        settlement_locs[letter] = {"display": letter}
        settlement_locs[letter]["port"] = ""


for loc in "ABFJouxy":
        settlement_locs[loc]["port"] = {"3:1 port"}

i = 0
reps = 0
for loc in "RQCGWcvwjp":
        
        reps += 1
        port_to_place = f"2:1 {ports[i]} port"
        settlement_locs[loc]["port"] = port_to_place

        if reps % 2 == 0:
                i += 1


road_types = ["__", "/", "\\"]
road_strings = ["ABCDEF$GHIJKMNOPRSTUVWYZabdefghiklmnpqrstuvwxyz+", 
                "ADCG$LRXMSHNEIJPQWVbcihnoutyx+rwmsflagOUTZYedjkq",
                "BEFJDHIOGMLRSYNTXdekjpqvwzsxntiobhWcKQPVUaZfgmlr"]

counter = 0
quick_dict = dict(zip(road_types, road_strings))
roads = {}
for road_type in road_types:
        for i in range(len(quick_dict[road_type])//2):

                road = ""
                road += quick_dict[road_type][counter]
                counter += 1
                road += quick_dict[road_type][counter]
                counter += 1

                road = quick_reorder(road)
                
                roads[road] = ansi_stitching([0, 201, 184], road_type)
        counter = 0

        print(roads)


grid_part_1 = (
    
        #line 1
        (" " * 65) + "3: 1 port" + "\n" +
        #line 2
        (" " * 65) + "/      \\" + "\n" +
        #line 3
        (" " * 64) + "/        \\" + "\n" +
        #line 4
        (" " * 20) + "sea" + (" " * 38) + settlement_locs["A"]["display"] + " " + (roads["AB"] + " ") * 4 + settlement_locs["B"]["display"] + (" " * 38) + "sea" + "\n" +
        #line 5
        (" " * 61) + roads["AD"] + "              " + roads["BE"] + "\n" +
        #line 6 & 7
        (" " * 60) + roads["AD"] + "                " + roads["BE"] + "\n\n" +
        #line 8
        (" " * 35) + ("2:1 grain port") + (" " * 9) + roads["AD"] + (" " * 7) + kaomojis[tiles["S1"]["biome"]] + (" "* 7) + roads["BE"] + (" " * 16) + "3:1 port" + "\n" +
        #line 9
        (" " * 36) + "|    " + "\\" + "   " + (roads["CD"] + " ") * 4 + roads["AD"] + (" " * 10) + str(tiles["S1"]["number"]) + (" " * 11 if len(str(tiles["S1"]["number"])) == 1 else " " * 10) + roads["BE"] + " " + (roads["EF"] + " ") * 4 + "   /  |\n" +
        #line 10
        (" " * 36) + "|" + (" " * 3) + settlement_locs["C"]["display"] + " " + roads["CG"] + (" " * 11) + settlement_locs["D"]["display"] + "  " + roads["DH"] 
        + (" " * ((22 - len(str(tiles["S1"]["biome"])))//2)) + tiles["S1"]["biome"] + 
        (" " * (((22-len(str(tiles["S1"]["biome"])))//2)+ (1 if len(str(tiles["S1"]["biome"]))%2 != 0 else 0)))
        + roads["EI"] + " " + settlement_locs["E"]["display"] + (" " * 8) + settlement_locs["F"]["display"] + "  " + roads["FJ"] + "     |\n" +
        #line 11
        (" " * 36) + "|" + "    " + roads["CG"] +  (" " * 16) + roads["DH"] + (" " * 9) + "S1" + (" " * 9) + roads["EI"] + (" " * 15) + roads["FJ"] + "    |" + "\n" +
        #line 12
        (" " * 36) + "|" + (" " * 63) + "|" + "\n" +
        #line 13
        (" " * 36) + "|" + "  " + roads["CG"] + (" " * 7) + kaomojis[tiles["S2"]["biome"]] + (" " * 7) + roads["DH"] 
        + (" " * 16) + roads["EI"] + " "  + (" " * 6) + (kaomojis[tiles["S3"]["biome"]]) 
        + (" " * 6) + roads["FJ"] +"  |\n" +
        #line 14
        (" " * 21) + settlement_locs["$"]["display"] + " " + (roads[quick_reorder("G$")] + " ") * 4 + settlement_locs["G"]["display"] + "  " + roads["CG"] + (" " * 10) + str(tiles["S2"]["number"]) + 
        (" " * 9 if len(str(tiles["S2"]["number"])) == 1 else " " * 8) + settlement_locs["H"]["display"] + " " + roads["DH"] + " " + (roads["HI"] + " ") * 4 + " " + roads["EI"] + " " + settlement_locs["I"]["display"] +
        (" " * 8) + str(tiles["S3"]["number"]) + (" " * 8 if len(str(tiles["S3"]["number"])) == 1 else " " * 7) + settlement_locs["J"]["display"] + " " + roads["FJ"] + " | " + (roads["JK"] + " ") * 4 
        + settlement_locs["K"]["display"] + "\n" +
        #line 15
        (" " * 21) + roads[quick_reorder("L$")] + (" " * 16) + roads["GM"] + (" " * ((22 - len(str(tiles["S2"]["biome"])))//2)) + tiles["S2"]["biome"] + (" " * 9 if tiles["S2"]["biome"] != "desert" else " " * 8)
        + roads["HN"] + (" " * 14) + roads["IO"] + (" " * ((21 - len(str(tiles["S3"]["biome"])))//2)) + tiles["S3"]["biome"] + (" " * ( (21 - len(tiles["S3"]["biome"])) //2   ) ) + 
        (" " * (1 if len(tiles["S3"]["biome"]) % 2 != 1 else 0)) + roads["JP"] + (" " * 14) + roads["KQ"] + "\n" +
        #line 16 & 17 
        (" " * 20) + roads[quick_reorder("L$")] + (" " * 18) + roads["GM"] + (" " * 9) + "S2" + (" " * 9) + roads["HN"] + (" " * 16) + roads["IO"] + (" " * 8) + "S3" + (" " * 9) + roads["JP"] + (" " * 16) + roads["KQ"] + "\n\n" +
        #line 18
        (" " * 18) + roads[quick_reorder("L$")] + (" " * 8) + kaomojis[tiles["S4"]["biome"]] + (" " * 8) + roads["GM"] + (" " * 16) + roads["HN"] + (" " * 7) + kaomojis[tiles["S5"]["biome"]] + (" " * 7) + roads["IO"]
        + (" " * 15) + roads["JP"] + (" " * 7) + kaomojis[tiles["S6"]["biome"]] + (" " * 7) + roads["KQ"] + "\n" + 
        #line 19
        (" " * 15) + settlement_locs["L"]["display"] + " " + roads[quick_reorder("L$")] + (" " * 11) + str(tiles["S4"]["number"]) + (" " * (10 if len(str(tiles["S4"]["number"])) == 1 else 9)) + settlement_locs["M"]["display"] +
        " " + roads["GM"] + "  " + (roads["MN"] + " ") * 4 + roads["HN"] + settlement_locs["N"]["display"] + (" " * 9) + str(tiles["S5"]["number"]) + (" " * 9 if len(str(tiles["S5"]["number"])) == 1 else " " * 8) + settlement_locs["O"]["display"] +
        " " + roads["IO"] + " " + (roads["OP"] + " ") * 4 + roads["JP"] + " " + settlement_locs["P"]["display"] + (" " * 8) + str(tiles["S6"]["number"]) + (" " * 11 if len(str(tiles["S6"]["number"])) == 1 else " " * 10) + roads["KQ"]
        + " " + settlement_locs["Q"]["display"] + "\n"
        
        
)

grid_mid = (
        #line 20
        (" " * 17) + roads["LR"] + (" " * ((24 - len(str(tiles["S4"]["biome"])))//2)) + tiles["S4"]["biome"] + (" " * 10 if tiles["S4"]["biome"] != "desert" else " " * 9) + roads["MS"] + (" " * 14) + roads["NT"] +
        (" " * ((22 - len(str(tiles["S5"]["biome"])))//2)) + tiles["S5"]["biome"] + (" " * 9 if tiles["S5"]["biome"] != "desert" else " " * 8) + roads["OU"] + (" " * 13) + roads["PV"] +
        (" " * ((22 - len(str(tiles["S6"]["biome"])))//2)) + tiles["S6"]["biome"] + (" " * 9 if tiles["S6"]["biome"] != "desert" else " " * 8) + roads["QW"] + "\n" +
        #line 21 & 22
        (" " * 18) + roads["LR"] + (" " * 10) + "S4" + (" " * 10) + roads["MS"] + (" " * 16) + roads["NT"] + (" " * 9) + "S5" + (" " * 9) + roads["OU"] + (" " * 15) + roads["PV"] + (" " * 9) + "S6" + (" " * 9) + roads["QW"] + "\n\n" +
        #line 23
        (" " * 20) + roads["LR"] + (" " * 18) + roads["MS"] + (" " * 7) + kaomojis[tiles["S7"]["biome"]] + (" " * 7) + roads["NT"] + (" " * 16) + roads["OU"] + (" " * 7) + kaomojis[tiles["S8"]["biome"]]  + (" " * 6) + roads["PV"] +
        (" " * 16) + roads["QW"] + "\n" +
        #line 24
        (" " * 3) + "2:1 wood port - " + settlement_locs["R"]["display"] + " " + roads["LR"] + "  " + (roads["RS"] + " ") * 4 + settlement_locs["S"]["display"] + " " + roads["MS"] + (" " * 10) + str(tiles["S7"]["number"]) + 
        (" " * 8 if len(str(tiles["S7"]["number"])) == 1 else " " * 7) + settlement_locs["T"]["display"] + "  " + roads["NT"] + "  " + (roads["TU"] + " ") * 4 + roads["OU"] + " " + settlement_locs["U"]["display"] +
        (" " * 8) + str(tiles["S8"]["number"]) + (" " * 8 if len(str(tiles["S8"]["number"])) == 1 else " " * 7) + settlement_locs["V"]["display"] + " " + roads["PV"] + " " + (roads["VW"] + " ") * 4 + " " + roads["QW"] + 
        settlement_locs["W"]["display"] +  " _ _ _  2:1 sheep port" + "\n" +
        #line 25
        (" " * 8) + "\\" + (" " * 12) + roads["RX"] + (" " * 16) + roads["SY"] + (" " * ((22 - len(str(tiles["S7"]["biome"])))//2)) + tiles["S7"]["biome"] + 
        (" " * (((22-len(str(tiles["S7"]["biome"])))//2) + (1 if len(str(tiles["S7"]["biome"]))%2 != 0 else 0))) + roads["TZ"] + (" " * 14) + roads["Ua"] +
        (" " * ((21 - len(str(tiles["S8"]["biome"])))//2)) + tiles["S8"]["biome"] + 
        (" " * (((21-len(str(tiles["S8"]["biome"])))//2) + (1 if len(str(tiles["S8"]["biome"]))%2 != 1 else 0))) + roads["Vb"] + (" " * 14) + roads["Wc"] + "         /\n" +
        #line 26
        (" " * 9) + "\\" + (" " * 10) + roads["RX"] + (" " * 18) + roads["SY"] + (" " * 9) + "S7" + (" " * 9) + roads["TZ"] + (" " * 16) + roads["Ua"] + (" " * 8) + "S8" + (" " * 9) + roads["Vb"] + (" " * 16) + roads["Wc"] + "       /" + "\n" +
        #line 27
        (" " * 10) + "\\" + (" " * 110) + "/" + "\n" +
        #line 28
        (" " * 11) + "\\" + (" " * 6) + roads["RX"] + (" " * 8) + kaomojis[tiles["S9"]["biome"]] + (" " * 8) + roads["SY"] + (" " * 16) + roads["TZ"] + (" " * 6) + kaomojis[tiles["S10"]["biome"]] + (" " * 8) + roads["Ua"]
        + (" " * 15) + roads["Vb"] + (" " * 7) + kaomojis[tiles["S11"]["biome"]] + (" " * 7) + roads["Wc"] + "   /" + "\n" +
        #line 29
        (" " * 12) + "\\  " + settlement_locs["X"]["display"] + " " + roads["RX"] + (" " * 12) + str(tiles["S9"]["number"]) + (" " * 9 if len(str(tiles["S9"]["number"])) == 1 else " " * 8) 
        + settlement_locs["Y"]["display"] + " " + roads["SY"] + " " + (roads["YZ"] + " ") * 4 + settlement_locs["Z"]["display"] + roads["TZ"] + (" " * 10) + str(tiles["S10"]["number"]) + 
        (" " * 9 if len(str(tiles["S10"]["number"])) == 1 else " " * 8) + settlement_locs["a"]["display"] + " " + roads["Ua"] + (" " + roads["ab"]) * 4 + settlement_locs["b"]["display"] + roads["Vb"] +
        (" " * 10) + str(tiles["S11"]["number"]) + (" " * 11 if len(str(tiles["S11"]["number"])) == 1 else " " * 10) + roads["Wc"] + " " + settlement_locs["c"]["display"] + "\n" +
        #line 30
        (" " * 17) + roads["Xd"] + (" " * ((24 - len(str(tiles["S9"]["biome"])))//2)) + tiles["S9"]["biome"] + (" " * (((24-len(str(tiles["S9"]["biome"])))//2) + (1 if len(str(tiles["S9"]["biome"]))%2 != 0 else 0))) 
        + roads["Ye"] + (" " * 14) + roads["Zf"] + (" " * ((22 - len(str(tiles["S10"]["biome"])))//2)) + tiles["S10"]["biome"] + 
        (" " * (((22-len(str(tiles["S10"]["biome"])))//2) + (1 if len(str(tiles["S10"]["biome"]))%2 != 0 else 0))) + roads["ag"] + (" " * 13) + roads["bh"] +
        (" " * ((22 - len(str(tiles["S11"]["biome"])))//2)) + tiles["S11"]["biome"] + 
        (" " * (((22-len(str(tiles["S11"]["biome"])))//2) + (1 if len(str(tiles["S11"]["biome"]))%2 != 0 else 0))) + roads["ci"] + "\n"
    
)

grid_part_2 = (
        #line 31 & 32
        (" " * 18) + "\\" + (" " * 10) + "S9" + (" " * 10) + "/" + (" " * 16) + "\\" + (" " * 8) + "S10" + (" " * 9) + "/" + (" " * 15) + "\\" + (" " * 8) + "S11" + (" " * 9) + "/" + "\n\n" +
        #line 33
        (" " * 20) + "\\" + (" " * 18) + "/" + (" " * 7) + kaomojis[tiles["S12"]["biome"]] + (" " * 7) + "\\" + (" " * 16) + "/" + (" " * 6) + kaomojis[tiles["S13"]["biome"]] + (" " * 7) + "\\" + (" " * 16) + "/" 
        + "\n" +
        #line 34
        (" " * 19) + settlement_locs["d"]["display"] + " " + "\\" + "  " + (roads["de"] + " ") * 4 + settlement_locs["e"]["display"] + " " + "/" + (" " * 10) + 
        str(tiles["S12"]["number"]) + (" " * 9 if len(str(tiles["S12"]["number"])) == 1 else " " * 8) + settlement_locs["f"]["display"] + " " + "\\" + " " + (roads["fg"] + " ") * 4 + settlement_locs["g"]["display"] + "/" +
        (" " * 10) + str(tiles["S13"]["number"]) + (" " * 8 if len(str(tiles["S13"]["number"])) == 1 else " " * 7) + settlement_locs["h"]["display"] + " " + "\\" + " " + (roads["hi"] + " ") * 4 + " " + "/" + " " 
        + settlement_locs["i"]["display"] + "\n" +
        #line 35
        (" " * 21) + "/" + (" " * 16) + "\\" + (" " * ((23 - len(str(tiles["S12"]["biome"])))//2)) + tiles["S12"]["biome"] + 
        (" " * (((21-len(str(tiles["S12"]["biome"])))//2) + (1 if len(str(tiles["S12"]["biome"]))%2 != 1 else 0))) + "/" + (" " * 14) + "\\"
        + (" " * ((21 - len(str(tiles["S13"]["biome"])))//2)) + tiles["S13"]["biome"] + 
        (" " * (((21-len(str(tiles["S13"]["biome"])))//2) + (1 if len(str(tiles["S13"]["biome"]))%2 != 1 else 0))) + "/" + (" " * 14) + "\\" + "\n" +
        #line 36 & 37
        (" " * 20) + "/" + (" " * 18) + "\\" + (" " * 8) + "S12" + (" " * 9) + "/" + (" " * 16) + "\\" + (" " * 8) + "S13" + (" " * 8) + "/" + (" " * 16) + "\\" + "\n\n" +
        #line 38 
        (" " * 18) + "/" + (" " * 8) + kaomojis[tiles["S14"]["biome"]] + (" " * 8) + "\\" + (" " * 16) + "/" + (" " * 7) + kaomojis[tiles["S15"]["biome"]] + (" " * 7) + "\\" + (" " * 15) + "/" + (" " * 7) + kaomojis[tiles["S16"]["biome"]] + (" " * 7)
        + "\\" + "\n" +
        #line 39
        (" " * 15) + settlement_locs["j"]["display"] + " " + "/" + (" " * 11) + str(tiles["S14"]["number"]) + (" " * 10 if len(str(tiles["S14"]["number"])) == 1 else " " * 9) + settlement_locs["k"]["display"]
        + " " + "\\" + " " + (roads["kl"] + " ") * 4 + settlement_locs["l"]["display"] + "/" + (" " * 10) + str(tiles["S15"]["number"]) + (" " * 9 if len(str(tiles["S15"]["number"])) == 1 else " " * 8)
        + settlement_locs["m"]["display"] + " " + "\\" + " " + (roads["mn"] + " ") * 4 + "/" + settlement_locs["n"]["display"] + (" " * 9) + str(tiles["S16"]["number"]) + 
        (" " * 11 if len(str(tiles["S16"]["number"])) == 1 else " " * 10) + "\\" + " " + settlement_locs["o"]["display"] + "\n" +
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
        (" " * 13) + "/" + (" " * 107) + "\\" + "\n" 
        )

grid_part_3 = (
        #line 43
        (" " * 12) + "/" + (" " * 7) + "\\" + (" " * 18) + "/" + (" " * 7) + kaomojis[tiles["S17"]["biome"]] + (" " * 7) + "\\" + (" " * 16) + "/" + (" " * 6) + kaomojis[tiles["S18"]["biome"]] + (" " * 7)
        + "\\" + (" " * 16) + "/" + (" " * 7) + "\\" + "\n" +
        #line 44
        " 2:1 brick port _  " + settlement_locs["p"]["display"] + " " + "\\" + " " + (roads["pq"] + " ") * 4 + " " + settlement_locs["q"]["display"] + " " + "/" + (" " * 11) + str(tiles["S17"]["number"]) +
        (" " * 8 if len(str(tiles["S17"]["number"])) == 1 else " " * 7) + settlement_locs["r"]["display"] + " " + "\\" + " " + (roads["rs"] + " ") * 4 + settlement_locs["s"]["display"] +"/" + (" " * 10) + 
        str(tiles["S18"]["number"]) + (" " * 8 if len(str(tiles["S18"]["number"])) == 1 else " " * 7) + settlement_locs["t"]["display"] + " " + "\\" + " " + (roads["tu"] + " ") * 4 + " " + "/" +
        settlement_locs["u"]["display"] + "  _ _ 3:1 port" + "\n" +
        #line 45
        (" " * 38) + "\\" + (" " * ((22 - len(str(tiles["S17"]["biome"])))//2)) + tiles["S17"]["biome"] + 
        (" " * (((22 - len(str(tiles["S17"]["biome"])))//2) + (1 if len(str(tiles["S17"]["biome"]))%2 != 0 else 0))) + "/" + (" " * 14) + "\\" +
        (" " * ((21 - len(str(tiles["S18"]["biome"])))//2)) + tiles["S18"]["biome"] + 
        (" " * (((21 - len(str(tiles["S18"]["biome"])))//2) + (1 if len(str(tiles["S18"]["biome"]))%2 != 1 else 0))) + "/" + "\n" +
        #line 46 & 47
        (" " * 39) + "\\" + (" " * 8)  + "S17" + (" " * 9) + "/" + (" " * 16) + "\\" + (" " * 8) + "S18" + (" " * 8) + "/" + "\n\n" +
        #line 48
        (" " * 41) + "\\" + (" " * 16) + "/" + (" " * 7) + kaomojis[tiles["S19"]["biome"]] + (" " * 7) + "\\" + (" " * 15) + "/" + "\n" +
        #line 49
        (" " * 42) + "\\" + settlement_locs["v"]["display"] + " " + (roads["vw"] + " ") * 4 + settlement_locs["w"]["display"] + (" " * 10) + str(tiles["S19"]["number"]) +
        (" " * 9 if len(str(tiles["S19"]["number"])) == 1 else " " * 8) + settlement_locs["x"]["display"] + " " + "\\" + " " + (roads["xy"] + " ") * 4 + "/" + " " 
        + settlement_locs["y"]["display"] + "\n" +
        #line 50
        (" " * 58) + "\\" +(" " * ((21 - len(str(tiles["S19"]["biome"])))//2)) + tiles["S19"]["biome"] + 
        (" " * (((21 - len(str(tiles["S19"]["biome"])))//2) + (1 if len(str(tiles["S19"]["biome"]))%2 != 1 else 0))) + "/" + "\n" +
        #line 51
        (" " * 44) + "\\" + (" " * 11) + "/  " + "\\" + (" " * 8) + "S19" + (" " * 8) + "/" + "  \\          /" + "\n" +
        #line 52
        (" " * 45) + "\\         /" + (" " * 27) + "\\" + "        " + "/" + "\n" +
        #line 53
        (" " * 46) + "\\       /      " + "\\" + "               " + "/" + "      " + "\\" + "      " + "/" + "\n" +
        #line 54
        (" " * 45) + "2:1 ore port     " + "\\" + settlement_locs["z"]["display"] + " " + (roads["+z"] + " ") * 4 + settlement_locs["+"]["display"] + "      3:1 port"

)

grid = [grid_part_1, grid_mid, grid_part_2, grid_part_3]
for part in grid:
        print(part, end="")
print("\n")

player_1_colors = [0, 201, 184]
player_2_colors = [252, 210, 0]
player_3_colors = [252, 84, 0]
player_4_colors = [210, 0, 252]
print(ansi_stitching(player_1_colors, "this is player 1's color"))
print(ansi_stitching(player_2_colors, "this is player 2's color"))
print(ansi_stitching(player_3_colors, "this is player 3's color"))
print(ansi_stitching(player_4_colors, "this is player 4's color"))



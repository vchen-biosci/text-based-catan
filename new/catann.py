import random, time, sys

##CLASSES


class GameInfo:
    """An object containing future variables that the program may reference"""
    def __init__(self):
        self.resources = ["ores", "grain", "wood", "brick", "sheep"]#this is a constant but it's ugly so I don't want to write it as full caps
        self.associated_settlements = {
    "S1": ["A", "B", "E", "I", "H", "D"],
    "S2": ["C", "D", "H", "N", "M", "G"],
    "S3": ["E", "F", "J", "P", "O", "I"],
    "S4": ["$", "G", "M", "S", "R", "L"],
    "S5": ["H", "I", "O", "U", "T", "N"],
    "S6": ["J", "K", "Q", "W", "V", "P"],
    "S7": ["M", "N", "T", "Z", "Y", "S"],
    "S8": ["O", "P", "V", "b", "a", "U"],
    "S9": ["R", "S", "Y", "e", "d", "X"],
    "S10": ["T", "U", "a", "g", "f", "Z"],
    "S11": ["V", "W", "c", "i", "h", "b"],
    "S12": ["Y", "Z", "f", "l", "k", "e"],
    "S13": ["a", "b", "h", "n", "m", "g"],
    "S14": ["d", "e", "k", "q", "p", "j"],
    "S15": ["f", "g", "m", "s", "r", "l"],
    "S16": ["h", "i", "o", "u", "t", "n"],
    "S17": ["k", "l", "r", "w", "v", "q"],
    "S18": ["m", "n", "t", "y", "x", "s"],
    "S19": ["r", "s", "x", "+", "z", "w"]
    }
        self.cards = {'knight': 14, 'year of plenty': 2, 'build road': 2, 'monopoly': 2, 'VP cards': 5}
   
    
class PlayerInfo:
    """An object containing player information. Pass in when modifying player libraries or info"""
    def __init__(self, game_bank, quick_key, player_dicts):
        self.game_bank = game_bank
        self.quick_key = quick_key
        self.player_dicts = player_dicts
        self.player_turn = 1
        self.game_stage = 1


class Grid:
    """An object to contain all the important information needed to render the grid or access its variables"""
    def __init__(self, robber, tiles, settlement_locs, roads, biomes):
        self.robber = robber
        self.tiles = tiles
        self.settlement_locs = settlement_locs
        self.roads = roads
        self.kaomojis = {
        "ores": "‧₊˚🗻`",
        "brick": "↟↟↟↟↟↟",
        "grain": "˚ʚ🌱₊˚",
        "wood": " ݁˖𓂃.𖠰.",
        "sheep": ":3 ^^~", 
        "desert": " ⛰︎ ོ ༄-"
}
        self.biomes = biomes


##DISPLAY-RELATED


def clear_screen():
    """Clears the screen with ansi code"""
    print("\033c", end="")
    
    
def print_grid(grid : Grid):##this is a very long function so keep it closed
        """Prints out the grid. KEEP THIS SUBROUTINE FOLDED OR IT WILL BE A GIANT BLOCK OF TEXT"""

        grid_part_1 = (
#line 1
(" " * 65) + "3: 1 port" + "\n" +
#line 2
(" " * 65) + "/      \\" + "\n" +
#line 3
(" " * 64) + "/        \\" + "\n" +
#line 4
(" " * 20) + "sea" + (" " * 38) + grid.settlement_locs["A"]["display"] + " " + (grid.roads["AB"]["display"] + " ") * 4 + grid.settlement_locs["B"]["display"] + (" " * 38) + "sea" + "\n" +
#line 5
(" " * 61) + grid.roads["AD"]["display"] + "              " + grid.roads["BE"]['display'] + "\n" +
#line 6 & 7
(" " * 60) + grid.roads["AD"]['display'] + "                " + grid.roads["BE"]['display'] + "\n\n" +
#line 8
(" " * 35) + ("2:1 grain port") + (" " * 9) + grid.roads["AD"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S1"]["biome"]] + (" "* 7) + grid.roads["BE"]['display'] + (" " * 16) + "3:1 port" + "\n" +
#line 9
(" " * 36) + "|    " + "\\" + "   " + (grid.roads["CD"]['display'] + " ") * 4 + grid.roads["AD"]['display'] + (" " * 10) + str(grid.tiles["S1"]["number"]) 
+ (" " * 11 if len(str(grid.tiles["S1"]["number"])) == 1 else " " * 10) + grid.roads["BE"]['display'] + " " + (grid.roads["EF"]['display'] + " ") * 4 + "   /  |\n" +
#line 10
(" " * 36) + "|" + (" " * 3) + grid.settlement_locs["C"]["display"] + " " + grid.roads["CG"]['display'] + (" " * 11) + grid.settlement_locs["D"]["display"] + "  " + grid.roads["DH"]['display']
+ (" " * ((22 - len(str(grid.tiles["S1"]["biome"])))//2)) + grid.tiles["S1"]["biome"] +
(" " * (((22-len(str(grid.tiles["S1"]["biome"])))//2)+ (1 if len(str(grid.tiles["S1"]["biome"]))%2 != 0 else 0)))
+ grid.roads["EI"]['display'] + " " + grid.settlement_locs["E"]["display"] + (" " * 8) + grid.settlement_locs["F"]["display"] + "  " + grid.roads["FJ"]['display'] + "     |\n" +
#line 11
(" " * 36) + "|" + "    " + grid.roads["CG"]['display'] +  (" " * 16) + grid.roads["DH"]['display'] + (" " * 9) + "S1" + (" " * 9) + grid.roads["EI"]['display'] + (" " * 15) + 
grid.roads["FJ"]['display'] + "    |" + "\n" +
#line 12
(" " * 36) + "|" + (" " * 63) + "|" + "\n" +
#line 13
(" " * 36) + "|" + "  " + grid.roads["CG"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S2"]["biome"]] + (" " * 7) + grid.roads["DH"]['display'] 
+ (" " * 16) + grid.roads["EI"]['display'] + " "  + (" " * 6) + (grid.kaomojis[grid.tiles["S3"]["biome"]]) 
+ (" " * 6) + grid.roads["FJ"]['display'] +"  |\n" +
#line 14
(" " * 21) + grid.settlement_locs["$"]["display"] + " " + (grid.roads[quick_reorder("G$")]['display'] + " ") * 4 + grid.settlement_locs["G"]["display"] + "  " + grid.roads["CG"]['display'] + (" " * 10) + str(grid.tiles["S2"]["number"]) + 
(" " * 9 if len(str(grid.tiles["S2"]["number"])) == 1 else " " * 8) + grid.settlement_locs["H"]["display"] + " " + grid.roads["DH"]['display'] + " " + (grid.roads["HI"]['display'] + " ") * 4 + " " + grid.roads["EI"]['display'] + " " + grid.settlement_locs["I"]["display"] +
(" " * 8) + str(grid.tiles["S3"]["number"]) + (" " * 8 if len(str(grid.tiles["S3"]["number"])) == 1 else " " * 7) + grid.settlement_locs["J"]["display"] + " " + grid.roads["FJ"]['display'] + " | " + (grid.roads["JK"]['display'] + " ") * 4 
+ grid.settlement_locs["K"]["display"] + "\n" +
#line 15
(" " * 21) + grid.roads[quick_reorder("L$")]['display'] + (" " * 16) + grid.roads["GM"]['display'] + (" " * ((22 - len(str(grid.tiles["S2"]["biome"])))//2)) + grid.tiles["S2"]["biome"] + (" " * 9 if grid.tiles["S2"]["biome"] != "desert" else " " * 8)
+ grid.roads["HN"]['display'] + (" " * 14) + grid.roads["IO"]['display'] + (" " * ((21 - len(str(grid.tiles["S3"]["biome"])))//2)) + grid.tiles["S3"]["biome"] + (" " * ( (21 - len(grid.tiles["S3"]["biome"])) //2   ) ) + 
(" " * (1 if len(grid.tiles["S3"]["biome"]) % 2 != 1 else 0)) + grid.roads["JP"]['display'] + (" " * 14) + grid.roads["KQ"]['display'] + "\n" +
#line 16 & 17 
(" " * 20) + grid.roads[quick_reorder("L$")]['display'] + (" " * 18) + grid.roads["GM"]['display'] + (" " * 9) + "S2" + (" " * 9) + grid.roads["HN"]['display'] + (" " * 16) + grid.roads["IO"]['display'] + (" " * 8) + "S3" + (" " * 9) + grid.roads["JP"]['display'] + 
(" " * 16) + grid.roads["KQ"]['display'] + "\n\n" +
#line 18
(" " * 18) + grid.roads[quick_reorder("L$")]['display'] + (" " * 8) + grid.kaomojis[grid.tiles["S4"]["biome"]] + (" " * 8) + grid.roads["GM"]['display'] + (" " * 16) + grid.roads["HN"]['display'] + (" " * 7) + 
grid.kaomojis[grid.tiles["S5"]["biome"]] + (" " * 7) + grid.roads["IO"]['display']
+ (" " * 15) + grid.roads["JP"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S6"]["biome"]] + (" " * 7) + grid.roads["KQ"]['display'] + "\n" + 
#line 19
(" " * 15) + grid.settlement_locs["L"]["display"] + " " + grid.roads[quick_reorder("L$")]['display'] + (" " * 11) + str(grid.tiles["S4"]["number"]) + (" " * (10 if len(str(grid.tiles["S4"]["number"])) == 1 else 9)) + grid.settlement_locs["M"]["display"] +
" " + grid.roads["GM"]['display'] + "  " + (grid.roads["MN"]['display'] + " ") * 4 + grid.roads["HN"]['display'] + grid.settlement_locs["N"]["display"] + (" " * 9) + str(grid.tiles["S5"]["number"]) + (" " * 9 if len(str(grid.tiles["S5"]["number"])) == 1 else " " * 8) + grid.settlement_locs["O"]["display"] +
" " + grid.roads["IO"]['display'] + " " + (grid.roads["OP"]['display'] + " ") * 4 + grid.roads["JP"]['display'] + " " + grid.settlement_locs["P"]["display"] + (" " * 8) + str(grid.tiles["S6"]["number"]) + (" " * 11 if len(str(grid.tiles["S6"]["number"])) == 1 else " " * 10) + grid.roads["KQ"]['display']
+ " " + grid.settlement_locs["Q"]["display"] + "\n"
)

        grid_part_2 = (
#line 20
(" " * 17) + grid.roads["LR"]['display'] + (" " * ((24 - len(str(grid.tiles["S4"]["biome"])))//2)) + grid.tiles["S4"]["biome"] + (" " * 10 if grid.tiles["S4"]["biome"] != "desert" else " " * 9) + grid.roads["MS"]['display'] + (" " * 14) + grid.roads["NT"]['display'] +
(" " * ((22 - len(str(grid.tiles["S5"]["biome"])))//2)) + grid.tiles["S5"]["biome"] + (" " * 9 if grid.tiles["S5"]["biome"] != "desert" else " " * 8) + grid.roads["OU"]['display'] + (" " * 13) + grid.roads["PV"]['display'] +
(" " * ((22 - len(str(grid.tiles["S6"]["biome"])))//2)) + grid.tiles["S6"]["biome"] + (" " * 9 if grid.tiles["S6"]["biome"] != "desert" else " " * 8) + grid.roads["QW"]['display'] + "\n" +
#line 21 & 22
(" " * 18) + grid.roads["LR"]['display'] + (" " * 10) + "S4" + (" " * 10) + grid.roads["MS"]['display'] + (" " * 16) + grid.roads["NT"]['display'] + (" " * 9) + "S5" + (" " * 9) + grid.roads["OU"]['display'] + (" " * 15) + grid.roads["PV"]['display'] 
+ (" " * 9) + "S6" + (" " * 9) + grid.roads["QW"]['display'] + "\n\n" +
#line 23
(" " * 20) + grid.roads["LR"]['display'] + (" " * 18) + grid.roads["MS"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S7"]["biome"]] + (" " * 7) + grid.roads["NT"]['display'] + (" " * 16) + grid.roads["OU"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S8"]["biome"]]  + (" " * 6) + grid.roads["PV"]['display'] +
(" " * 16) + grid.roads["QW"]['display'] + "\n" +
#line 24
(" " * 3) + "2:1 wood port - " + grid.settlement_locs["R"]["display"] + " " + grid.roads["LR"]['display'] + "  " + (grid.roads["RS"]['display'] + " ") * 4 + grid.settlement_locs["S"]["display"] + " " + grid.roads["MS"]['display'] + (" " * 10) + str(grid.tiles["S7"]["number"]) + 
(" " * 8 if len(str(grid.tiles["S7"]["number"])) == 1 else " " * 7) + grid.settlement_locs["T"]["display"] + "  " + grid.roads["NT"]['display'] + "  " + (grid.roads["TU"]['display'] + " ") * 4 + grid.roads["OU"]['display'] + " " + grid.settlement_locs["U"]["display"] +
(" " * 8) + str(grid.tiles["S8"]["number"]) + (" " * 8 if len(str(grid.tiles["S8"]["number"])) == 1 else " " * 7) + grid.settlement_locs["V"]["display"] + " " + grid.roads["PV"]['display'] + " " + (grid.roads["VW"]['display'] + " ") * 4 + " " + grid.roads["QW"]['display'] + 
grid.settlement_locs["W"]["display"] +  " _ _ _  2:1 sheep port" + "\n" +
#line 25
(" " * 8) + "\\" + (" " * 12) + grid.roads["RX"]['display'] + (" " * 16) + grid.roads["SY"]['display'] + (" " * ((22 - len(str(grid.tiles["S7"]["biome"])))//2)) + grid.tiles["S7"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S7"]["biome"])))//2) + (1 if len(str(grid.tiles["S7"]["biome"]))%2 != 0 else 0))) + grid.roads["TZ"]['display'] + (" " * 14) + grid.roads["Ua"]['display'] +
(" " * ((21 - len(str(grid.tiles["S8"]["biome"])))//2)) + grid.tiles["S8"]["biome"] + 
(" " * (((21-len(str(grid.tiles["S8"]["biome"])))//2) + (1 if len(str(grid.tiles["S8"]["biome"]))%2 != 1 else 0))) + grid.roads["Vb"]['display'] + (" " * 14) + grid.roads["Wc"]['display'] + "         /\n" +
#line 26
(" " * 9) + "\\" + (" " * 10) + grid.roads["RX"]['display'] + (" " * 18) + grid.roads["SY"]['display'] + (" " * 9) + "S7" + (" " * 9) + grid.roads["TZ"]['display'] + (" " * 16) + grid.roads["Ua"]['display'] + (" " * 8) + "S8" + (" " * 9) + 
grid.roads["Vb"]['display'] + (" " * 16) + grid.roads["Wc"]['display'] + "       /" + "\n" +
#line 27
(" " * 10) + "\\" + (" " * 110) + "/" + "\n" +
#line 28
(" " * 11) + "\\" + (" " * 6) + grid.roads["RX"]['display'] + (" " * 8) + grid.kaomojis[grid.tiles["S9"]["biome"]] + (" " * 8) + grid.roads["SY"]['display'] + (" " * 16) + 
grid.roads["TZ"]['display'] + (" " * 6) + grid.kaomojis[grid.tiles["S10"]["biome"]] + (" " * 8) + grid.roads["Ua"]['display']
+ (" " * 15) + grid.roads["Vb"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S11"]["biome"]] + (" " * 7) + grid.roads["Wc"]['display'] + "   /" + "\n" +
#line 29
(" " * 12) + "\\  " + grid.settlement_locs["X"]["display"] + " " + grid.roads["RX"]['display'] + (" " * 12) + str(grid.tiles["S9"]["number"]) + 
(" " * 9 if len(str(grid.tiles["S9"]["number"])) == 1 else " " * 8) 
+ grid.settlement_locs["Y"]["display"] + " " + grid.roads["SY"]['display'] + " " + (grid.roads["YZ"]['display'] + " ") * 4 + grid.settlement_locs["Z"]["display"] + 
grid.roads["TZ"]['display'] + (" " * 10) + str(grid.tiles["S10"]["number"]) + (" " * 9 if len(str(grid.tiles["S10"]["number"])) == 1 else " " * 8) + 
grid.settlement_locs["a"]["display"] + " " + grid.roads["Ua"]['display'] + (" " + grid.roads["ab"]['display']) * 4 + grid.settlement_locs["b"]["display"] + grid.roads["Vb"]['display'] +
(" " * 10) + str(grid.tiles["S11"]["number"]) + (" " * 11 if len(str(grid.tiles["S11"]["number"])) == 1 else " " * 10) + grid.roads["Wc"]['display'] + " " + grid.settlement_locs["c"]["display"] + "\n" +
#line 30
(" " * 17) + grid.roads["Xd"]['display'] + (" " * ((24 - len(str(grid.tiles["S9"]["biome"])))//2)) + grid.tiles["S9"]["biome"] + (" " * (((24-len(str(grid.tiles["S9"]["biome"])))//2) + (1 if len(str(grid.tiles["S9"]["biome"]))%2 != 0 else 0))) 
+ grid.roads["Ye"]['display'] + (" " * 14) + grid.roads["Zf"]['display'] + (" " * ((22 - len(str(grid.tiles["S10"]["biome"])))//2)) + grid.tiles["S10"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S10"]["biome"])))//2) + (1 if len(str(grid.tiles["S10"]["biome"]))%2 != 0 else 0))) + grid.roads["ag"]['display'] + (" " * 13) + grid.roads["bh"]['display'] +
(" " * ((22 - len(str(grid.tiles["S11"]["biome"])))//2)) + grid.tiles["S11"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S11"]["biome"])))//2) + (1 if len(str(grid.tiles["S11"]["biome"]))%2 != 0 else 0))) + grid.roads["ci"]['display'] + "\n"
        
        )

        grid_part_3 = (
#line 31 & 32
(" " * 18) + grid.roads["Xd"]['display'] + (" " * 10) + "S9" + (" " * 10) + grid.roads["Ye"]['display'] + (" " * 16) + grid.roads["Zf"]['display'] + (" " * 8) + "S10" + (" " * 9) + grid.roads["ag"]['display'] + (" " * 15) + grid.roads["bh"]['display'] + (" " * 8) + "S11" + (" " * 9) + grid.roads["ci"]['display'] + "\n\n" +
#line 33
(" " * 20) + grid.roads["Xd"]['display'] + (" " * 18) + grid.roads["Ye"]['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S12"]["biome"]] + (" " * 7) + grid.roads["Zf"]['display'] + (" " * 16) + grid.roads["ag"]['display'] + (" " * 6) + grid.kaomojis[grid.tiles["S13"]["biome"]] + (" " * 7) + 
grid.roads["bh"]['display'] + (" " * 16) + grid.roads["ci"]['display']
+ "\n" +
#line 34
(" " * 19) + grid.settlement_locs["d"]["display"] + " " + grid.roads["Xd"]['display'] + "  " + (grid.roads["de"]['display'] + " ") * 4 + grid.settlement_locs["e"]["display"] + " " + grid.roads["Ye"]['display'] + (" " * 10) + 
str(grid.tiles["S12"]["number"]) + (" " * 9 if len(str(grid.tiles["S12"]["number"])) == 1 else " " * 8) + grid.settlement_locs["f"]["display"] + " " + grid.roads["Zf"]['display'] + " " + (grid.roads["fg"]['display'] + " ") * 4 + grid.settlement_locs["g"]["display"] + grid.roads["ag"]['display'] +
(" " * 10) + str(grid.tiles["S13"]["number"]) + (" " * 8 if len(str(grid.tiles["S13"]["number"])) == 1 else " " * 7) + grid.settlement_locs["h"]["display"] + " " + grid.roads["bh"]['display'] + " " + (grid.roads["hi"]['display'] + " ") * 4 + " " + grid.roads["ci"]['display'] + " " 
+ grid.settlement_locs["i"]["display"] + "\n" +
#line 35
(" " * 21) + grid.roads["dj"]['display'] + (" " * 16) + grid.roads["ek"]['display'] + (" " * ((23 - len(str(grid.tiles["S12"]["biome"])))//2)) + grid.tiles["S12"]["biome"] + 
(" " * (((21-len(str(grid.tiles["S12"]["biome"])))//2) + (1 if len(str(grid.tiles["S12"]["biome"]))%2 != 1 else 0))) + grid.roads["fl"]['display'] + (" " * 14) + grid.roads["gm"]['display']
+ (" " * ((21 - len(str(grid.tiles["S13"]["biome"])))//2)) + grid.tiles["S13"]["biome"] + 
(" " * (((21-len(str(grid.tiles["S13"]["biome"])))//2) + (1 if len(str(grid.tiles["S13"]["biome"]))%2 != 1 else 0))) + grid.roads["hn"]['display'] + (" " * 14) + grid.roads["io"]['display'] + "\n" +
#line 36 & 37
(" " * 20) + grid.roads["dj"]['display'] + (" " * 18) + grid.roads['ek']['display'] + (" " * 8) + "S12" + (" " * 9) + grid.roads['fl']['display'] + (" " * 16) + grid.roads['gm']['display'] + (" " * 8) + "S13" + (" " * 8) + grid.roads['hn']['display'] + (" " * 16) + grid.roads['io']['display'] + "\n\n" +
#line 38 
(" " * 18) + grid.roads['dj']['display'] + (" " * 8) + grid.kaomojis[grid.tiles["S14"]["biome"]] + (" " * 8) + grid.roads['ek']['display'] + (" " * 16) + grid.roads['fl']['display'] + 
(" " * 7) + grid.kaomojis[grid.tiles["S15"]["biome"]] + (" " * 7) + grid.roads['gm']['display'] + (" " * 15) + grid.roads['hn']['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S16"]["biome"]] + (" " * 7)
+ grid.roads['io']['display'] + "\n" +
#line 39
(" " * 15) + grid.settlement_locs["j"]["display"] + " " + grid.roads['dj']['display'] + (" " * 11) + str(grid.tiles["S14"]["number"]) + (" " * 10 if len(str(grid.tiles["S14"]["number"])) == 1 else " " * 9) + grid.settlement_locs["k"]["display"]
+ " " + grid.roads['ek']['display'] + " " + (grid.roads["kl"]['display'] + " ") * 4 + grid.settlement_locs["l"]["display"] + grid.roads['fl']['display'] + (" " * 10) + str(grid.tiles["S15"]["number"]) + (" " * 9 if len(str(grid.tiles["S15"]["number"])) == 1 else " " * 8)
+ grid.settlement_locs["m"]["display"] + " " + grid.roads['gm']['display'] + " " + (grid.roads["mn"]['display'] + " ") * 4 + grid.roads['hn']['display'] + grid.settlement_locs["n"]["display"] + (" " * 9) + str(grid.tiles["S16"]["number"]) + 
(" " * 11 if len(str(grid.tiles["S16"]["number"])) == 1 else " " * 10) + grid.roads['io']['display'] + " " + grid.settlement_locs["o"]["display"] + "\n" +
#line 40
(" " * 17) + grid.roads['jp']['display'] + (" " * ((24 - len(str(grid.tiles["S14"]["biome"])))//2)) + grid.tiles["S14"]["biome"] +
(" " * (((24-len(str(grid.tiles["S14"]["biome"])))//2) + (1 if len(str(grid.tiles["S14"]["biome"]))%2 != 0 else 0))) + grid.roads['kq']['display'] + (" " * 14) + grid.roads['lr']['display'] +
(" " * ((22 - len(str(grid.tiles["S15"]["biome"])))//2)) + grid.tiles["S15"]["biome"] + 
(" " * (((22-len(str(grid.tiles["S15"]["biome"])))//2) + (1 if len(str(grid.tiles["S15"]["biome"]))%2 != 0 else 0))) + grid.roads['ms']['display'] + (" " * 13) + grid.roads['nt']['display'] +
(" " * ((22 - len(str(grid.tiles["S16"]["biome"])))//2)) + grid.tiles["S16"]["biome"] + 
(" " * (((22 - len(str(grid.tiles["S16"]["biome"])))//2) + (1 if len(str(grid.tiles["S16"]["biome"]))%2 != 0 else 0))) + grid.roads['ou']['display'] + "\n" +
#line 41 
(" " * 14) + "/" + (" " * 3) + grid.roads['jp']['display'] + (" " * 9) + "S14"  + (" " * 10) + grid.roads['kq']['display'] + (" " * 16) + grid.roads['lr']['display'] + (" " * 8) + "S15" + (" " * 9) + grid.roads['ms']['display'] 
+ (" " * 15) + grid.roads['nt']['display'] + (" " * 8) + "S16" + (" " * 9) + grid.roads['ou']['display'] + 
(" " * 3) + "\\" + "\n" +
#line 42
(" " * 13) + "/" + (" " * 107) + "\\" + "\n" 
                )

        grid_part_4 = (
#line 43
(" " * 12) + "/" + (" " * 7) + grid.roads['jp']['display'] + (" " * 18) + grid.roads['kq']['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S17"]["biome"]] + 
(" " * 7) + grid.roads['lr']['display'] + (" " * 16) + grid.roads['ms']['display'] + (" " * 6) + grid.kaomojis[grid.tiles["S18"]["biome"]] + (" " * 7)
+ grid.roads['nt']['display'] + (" " * 16) + grid.roads['ou']['display'] + (" " * 7) + "\\" + "\n" +
#line 44
" 2:1 brick port _  " + grid.settlement_locs["p"]["display"] + " " + grid.roads['jp']['display'] + " " + (grid.roads["pq"]['display'] + " ") * 4 + " " 
+ grid.settlement_locs["q"]["display"] + " " + grid.roads['kq']['display'] + (" " * 11) + str(grid.tiles["S17"]["number"]) +
(" " * 8 if len(str(grid.tiles["S17"]["number"])) == 1 else " " * 7) + grid.settlement_locs["r"]["display"] + " " + grid.roads['lr']['display'] + " " + 
(grid.roads["rs"]['display'] + " ") * 4 + grid.settlement_locs["s"]["display"] + grid.roads['ms']['display'] + (" " * 10) + 
str(grid.tiles["S18"]["number"]) + (" " * 8 if len(str(grid.tiles["S18"]["number"])) == 1 else " " * 7) + grid.settlement_locs["t"]["display"] + " " + grid.roads['nt']['display'] + 
" " + (grid.roads["tu"]['display'] + " ") * 4 + " " + grid.roads['ou']['display'] +
grid.settlement_locs["u"]["display"] + "  _ _ 3:1 port" + "\n" +
#line 45
(" " * 38) + grid.roads['qv']['display'] + (" " * ((22 - len(str(grid.tiles["S17"]["biome"])))//2)) + grid.tiles["S17"]["biome"] + 
(" " * (((22 - len(str(grid.tiles["S17"]["biome"])))//2) + (1 if len(str(grid.tiles["S17"]["biome"]))%2 != 0 else 0))) + grid.roads['rw']['display'] + (" " * 14) + grid.roads['sx']['display'] +
(" " * ((21 - len(str(grid.tiles["S18"]["biome"])))//2)) + grid.tiles["S18"]["biome"] + (" " * (((21 - len(str(grid.tiles["S18"]["biome"])))//2) 
+ (1 if len(str(grid.tiles["S18"]["biome"]))%2 != 1 else 0))) + grid.roads['ty']['display'] + "\n" +
#line 46 & 47
(" " * 39) + grid.roads['qv']['display'] + (" " * 8)  + "S17" + (" " * 9) + grid.roads['rw']['display'] + (" " * 16) + grid.roads['sx']['display'] + 
(" " * 8) + "S18" + (" " * 8) + grid.roads['ty']['display'] + "\n\n" +
#line 48
(" " * 41) + grid.roads['qv']['display'] + (" " * 16) + grid.roads['rw']['display'] + (" " * 7) + grid.kaomojis[grid.tiles["S19"]["biome"]] + (" " * 7) + 
grid.roads['sx']['display'] + (" " * 15) + grid.roads['ty']['display'] + "\n" +
#line 49
(" " * 42) + grid.roads['qv']['display'] + grid.settlement_locs["v"]["display"] + " " + (grid.roads["vw"]['display'] + " ") * 4 + grid.settlement_locs["w"]["display"] + 
(" " * 10) + str(grid.tiles["S19"]["number"]) + (" " * 9 if len(str(grid.tiles["S19"]["number"])) == 1 else " " * 8) + grid.settlement_locs["x"]["display"] + " " + 
grid.roads['sx']['display'] + " " + (grid.roads["xy"]['display'] + " ") * 4 + grid.roads['ty']['display'] + " " 
+ grid.settlement_locs["y"]["display"] + "\n" +
#line 50
(" " * 58) + grid.roads['wz']['display'] +(" " * ((21 - len(str(grid.tiles["S19"]["biome"])))//2)) + grid.tiles["S19"]["biome"] + 
(" " * (((21 - len(str(grid.tiles["S19"]["biome"])))//2) + (1 if len(str(grid.tiles["S19"]["biome"]))%2 != 1 else 0))) + grid.roads[quick_reorder("x+")]['display'] + "\n" +
#line 51
(" " * 44) + "\\" + (" " * 11) + "/  " + grid.roads['wz']['display'] + (" " * 8) + "S19" + (" " * 8) + grid.roads[quick_reorder("x+")]['display'] + "  \\          /" + "\n" +
#line 52
(" " * 45) + "\\         /" + (" " * 27) + "\\" + "        " + "/" + "\n" +
#line 53
(" " * 46) + "\\       /      " + grid.roads['wz']['display'] + "               " + grid.roads[quick_reorder("x+")]['display'] + "      " + "\\" + "      " + "/" + "\n" +
#line 54
(" " * 45) + "2:1 ore port     " + grid.roads['wz']['display'] + grid.settlement_locs["z"]["display"] + " " + (grid.roads["+z"]['display'] + " ") * 4 + grid.settlement_locs["+"]["display"] 
+ "      3:1 port"

        )

        quick_grid_access = [grid_part_1, grid_part_2, grid_part_3, grid_part_4]

        for grid in quick_grid_access:
                print(grid, end="")
        print("\n")
  
        
def print_board(player_info : PlayerInfo, grid : Grid):
    """Prints out basic information (visual display for what players need to see during their turns)"""

    print("________ WELCOME TO THE WORLD OF CATAN. WHERE WILL YOU SETTLE TODAY? ________\n")
    print(f"˗ˋˏ$ˎˊ˗ GAME BANK ˗ˋˏ$ˎˊ˗")
    game_bank = player_info.game_bank
    for resource in game_bank["resources"]:
        print(f'{resource} : {game_bank["resources"][resource]}', end="  ||  ")
    print("\n")
    for dev_card in game_bank['cards']:
        print(f'{dev_card} : {game_bank["cards"][dev_card]}', end="  ||  ")
    print("\n")
    for player in player_info.quick_key:
        print(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player} ({player_info.player_dicts[player]['name']})"), end="  ||  ")
    print("\n")

    print_grid(grid)

    print(f"The robber is currently pillaging the citizens of {grid.robber} and stealing all their {grid.tiles[grid.robber]['biome']}...")


##COLOURS


def ansi_stitching(color : list, text : str) -> str:
	"""Edits the string's value with an ANSI code that imbues it with pretty colours :3"""
	
	colored_ver = "\x1b[38;2;"
	reps = 0
	for value in color:
		colored_ver += str(value)
		reps += 1
		if reps < 3:
			colored_ver += ";"
	
	colored_ver += "m" + text + "\x1b[0m"

	return colored_ver
    
    
def add_colours(player_info) -> tuple[list, dict]:
        """Calls all the functions initially needed for the initialising of player dictionaries"""
        quick_key, player_dicts = player_info.quick_key, player_info.player_dicts
        
        player_colors = assign_player_colors(quick_key)
        for player, color in zip(player_dicts, player_colors):
                player_dicts[player]["color"] = color
        
        return player_dicts
    
    
def assign_player_colors(quick_key : list) -> list:
    """Iterates through each player and makes sure they have a colour assigned"""
    
    preset_colors = [[1, 201, 184], [252, 210, 1], [252, 84, 1], [210, 1, 252]]#this variable only needs to be temporary
    player_colors = []
    new_color = False
    for player in quick_key:#iterates through players
        action = ""
        while not action in ["y", "n"]:#indefinite iteration
            print(' We strongly recommend making your own, since the default may be similar to the color someone else has chosen.' if new_color else '')
            action = input("Would you like to customise your own color? (If not, you'll get a premade one!)" + 
" Type 'Y' for yes and 'N' for no.\n˚₊ · »-♡→ ").strip().lower()#a prompt, as the default may be too similar and undifferentiable from a pre-chosen colour
            if action == "y":
                player_colors.append(choose_color())
                new_color = True
            elif action == "n":
                print(ansi_stitching(preset_colors[player - 1], "This is your assigned color!"))
                player_colors.append(preset_colors[player - 1])
                time.sleep(0.3)
            else:
                print("Sorry, please either type 'y' or 'n'.")
        clear_screen()
                            
    print_player_colors(quick_key, player_colors)
    return player_colors   
    
    
def choose_color() -> list:
    """Get a player's colors by iterating through red, blue, and green."""
    
    player_color = []
    satisfied = False
    while not satisfied:
        get_color(player_color)   
                                
        confirmed = False
        while not confirmed:
            confirmed, satisfied = confirm_color(player_color, satisfied, confirmed)

    clear_screen()
    return player_color
    
    
def confirm_color(player_color, satisfied, confirmed) -> tuple[bool, bool]:
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
                
        return confirmed, satisfied
    
    
def print_player_colors(quick_key, player_colors):
        """Prints the colour for each player"""
        
        for player in quick_key:
                print(ansi_stitching(player_colors[player - 1], f"Player {player}, this is your color."))
                time.sleep(0.3)
                
                
def get_color(player_color : list) -> list:
    color_codes = {"red" : [255, 0, 0], "green" : [0, 255, 0], "blue" : [0, 0, 255]}
    for color in color_codes:#iterate through colours               
        valid_input = False
        while not valid_input:#makes sure that it doesn't end without getting the right colour
            action = input(ansi_stitching(color_codes[color], f"‧₊˚♪ 𝄞₊˚⊹ What value would you like to use for {color}? ‧₊˚♪ 𝄞₊˚⊹\n˚₊ · »-♡→ ")).strip().lower()
            try:
                if int(action) <= 255:
                    player_color.append(int(action))
                    valid_input = True
                else:
                    print("Sorry; RGB values only go up to 255.")
                    
            except ValueError:
                print("Please input a valid integer, in arabic numerals, within the range of 0 to 255.")
                                    
    return player_color
    

##PLAYER INFORMATION/DICTIONARIES
  
  
def create_player_info() -> tuple[list, dict]:
    """Obtains player information needed to initialise variables"""
    
    quick_key = create_player_key(get_player_number())
    player_dicts = {}#the player dictionaries are also stored in dictionaries
    player_names = []
    for player in quick_key:
        player_dicts[player] = {}
        name = get_player_name(player, player_names)
        player_dicts[player]['name'] = name
        player_names.append(name)
    
    return quick_key, player_dicts
    
    
def create_player_key(player_number : int) -> list:
    """Creates a key which can be used to iterate through players or find player number"""
    
    #iterates through each player and appends their ID to the quick key
    quick_key = []
    for player in range(player_number):
        quick_key.append(player + 1)
        
    return quick_key


def get_player_number() -> int:
    """Gets the number of players, repeats until valid"""
    
    player_number = 0
    while not player_number in [3, 4]:#only 3 and 4 players are accepted so I simply created a list to make the conditional shorter.
        try:
            player_number = int(input("How many people are playing? ⋆˚✿🍒𐙚⋆˚\n˚₊ · »-♡→ ").strip()) 
            if not player_number in [3, 4]:
                print("You can only play with 3 or 4 people.")
                
        except ValueError:#as not entering an integer would lead the 'int' to return a value error (the types do not align)
            print("Enter an integer (3 or 4) please.")
            
    return player_number


def get_player_name(player : int, player_names : list) -> str:
    """Gets the name of the current player and checks the length and if it is composed of numbers."""
    
    valid_name = False
    while not valid_name:
        player_name = input(f"Player {player}, enter your name!\n˚₊ · »-♡→ ").strip()
        if player_name in player_names:
            #checks if name has already been created by accessing past names
            print("... That name's already owned. Choose something else.")
        elif player_name.isdigit():
            print("Sorry, you're not allowed a name consisting of only numbers, as this will cause problems later.")
        elif len(player_name) > 8:
            print("Please set a shorter name. Sorry if your name is really that long, but it's hard to display.")
        else:
            valid_name = True
            
    return player_name   


def add_keys(player_info : PlayerInfo, game_info : GameInfo) -> dict:
    """Adds keys to each existing player dictionary"""
    player_dicts = player_info.player_dicts
    
    for player in player_info.quick_key:
            
        player_dicts[player]['roads'] = []
        player_dicts[player]['settlements'] = []
        player_dicts[player]['cities'] = []
        player_dicts[player]['construct_bank'] = {"settlements": 3, "cities": 4, "roads": 13}#technically they have more but they use it up initially - so it's easier to do this
        
        player_dicts[player]['achievements'] = {"longest road" : 0, "largest army" : 0}
        player_dicts[player]['knights_recruited'] = 0
        player_dicts[player]['VP cards'] = 0
        
        player_dicts[player]['resources'] = {}
        for resource in game_info.resources:
            player_dicts[player]['resources'][resource] = 0
            
        player_dicts[player]['cards'] = {}
        for dev_card in game_info.cards:
            player_dicts[player]['cards'][dev_card] = 0
            
    return player_dicts
    

##GRID GENERATION


def create_tiles() -> dict:
    """Creates one of each tile in a dictionary of tiles"""
        
    tiles = {}
    for i in range(19):#there are 19 total tiles.
        tiles[("S"+str(i+1))] = {}
                
    return tiles


def place_desert(tiles : dict) -> tuple[dict, str]:
    """The desert and robber are placed on the same random tile"""
        
    print("Spawning your desert...")
    desert = random.randint(1, 19)#the parameters for possible tiles (there are 19)
    tiles[("S"+str(desert))]["biome"] = "desert"
    tiles[("S"+str(desert))]["number"] = "NA"
    robber = "S"+str(desert)

    return tiles, robber


def make_token_list() -> list:
    """These are the possible tokens that can be assigned onto hexes."""
        
    number_tokens = []
    for i in range(2,12): #the range is between 2 and 11 inclusive as 1 and 12 only appear once.
        for x in range(2): #need to repeat this twice as these tokens appear twice.
            number_tokens.append(i)
        
    number_tokens.append(1)
    number_tokens.append(12)
        
    return number_tokens


def create_roads() -> dict:
	"""Creates a dictionary for roads and adds roads into it"""
	
	print("Paving your roads...")
	counter = 0
	quick_dict = dict(zip(["__", "/", "\\"], ["ABCDEF$GHIJKMNOPRSTUVWYZabdefghiklmnpqrstuvwxyz+", 
					"ADCG$LRXMSHNEIJPQWVbcihnoutyx+rwmsflagOUTZYedjkq",
					"BEFJDHIOGMLRSYNTXdekjpqvwzsxntiobhWcKQPVUaZfgmlr"]))
	roads = {}
	for road_type in ["__", "/", "\\"]:
		for i in range(len(quick_dict[road_type])//2):
			road = ""
			for x in range(2): 
				road += quick_dict[road_type][counter]
				counter += 1

			road = quick_reorder(road)
			roads[road] = {'display' : road_type, 'owner' : 0}
		counter = 0#resets the counter
			
	return roads


def make_grid(biomes : list, number_tokens : list, associated_settlements : dict) -> tuple[dict, str, dict, dict]:
        """Creates variables used in the grid"""
        
        settlement_locations = "abcdefghijklmnopqrstuvwxyz".upper()
        settlement_locations += settlement_locations.lower() + "+" + "$"
        #duplicates it in lowercase as the settlements are denoted alphabetically
        
        tiles = create_tiles()
        tiles, robber = place_desert(tiles)
        number_tokens = make_token_list()
        
        tiles = assign_tile_variables(tiles, biomes, number_tokens, associated_settlements)
        settlement_locs = assign_ports(settlement_locations)
        roads = create_roads()
        
        return tiles, robber, settlement_locs, roads


def assign_ports(settlement_locations : str) -> dict:
    """Assigns ports to relevant tiles"""
        
    ports = ["wood", "grain", "sheep", "ore", "brick"]
    settlement_locs = {}
    for loc in settlement_locations:
        settlement_locs[loc] = {"display": loc}#the display is the string that will be directly accessed for colouring later
        settlement_locs[loc]["port"] = ""
        settlement_locs[loc]["owner"] = 0
        
    for loc in "ABFJouxy":#these settlements can access the ports
        settlement_locs[loc]["port"] = "3:1 port"
        
    i = 0
    reps = 0
    for loc in "RQCGWcvwjp":
        reps += 1
        port_to_place = f"2:1 {ports[i]} port"
        settlement_locs[loc]["port"] = port_to_place
        if reps % 2 == 0:
            i += 1#it just makes sure that we iterate through the possible ports every 2 repetitions

    return settlement_locs


def assign_tile_variables(tiles : dict, biomes : list, number_tokens : list, associated_settlements):
    """Assigns variables to each tile"""
         
    for i in range(19):
        try:
            tiles[("S"+str(i+1))]["biome"]#the desert currently has no biome tag so simply calling it will return error
        except KeyError:
            #shuffle the biomes; pop is fast
            random.shuffle(biomes)
            chosen_biome = biomes.pop()
            #adds the chosen variables to the biome.
            tiles[("S"+str(i+1))]["biome"] = chosen_biome
            #shuffles the tokens too
            random.shuffle(number_tokens)
            chosen_number = number_tokens.pop()
            tiles[("S"+str(i+1))]["number"] = chosen_number
        
        tiles["S"+str(i+1)]["attached_settlements"] = associated_settlements["S"+str(i+1)]

    return tiles


def make_biomes() -> list:
        """Creates a list of biomes"""
        
        biomes = []
        for i in range(3):
                biomes.append("ores")
                biomes.append("brick")

        for i in range(4):
                biomes.append("grain")
                biomes.append("wood")
                biomes.append("sheep")
        
        return biomes
    
    
##GAME ASSETS


def create_game_bank(game_info : GameInfo):
    """Calls the functions needed to set up the game bank"""
    
    game_bank = {}
    #adds the dictionaries for asset values into the game bank
    resources, dev_bank = initialise_resource_cards(game_info)
    game_bank['resources'] = resources
    game_bank['cards'] = dev_bank
    
    #initialises construct number
    game_bank['constructs'] = {'road' : 60,
                     'settlement' : 20,
                     'city' : 16
    }
    
    #creates a bank of building costs that the game can directly access
    game_bank['building_costs'] = {'road' : {'brick' : 1, 'wood' : 1},
                         'settlement' : {'brick' : 1, 'wood' : 1, 'grain' : 1, 'sheep' : 1},
                         'city' : {'grain' : 2, 'ores' : 3},
                         'dev card': {'sheep' : 1, 'grain' : 1, 'ores' : 1}}
    
    return game_bank

 
def initialise_resource_cards(game_info : GameInfo) -> tuple[dict, dict]:
    """Initialises the dictionary for each resource to be passed into the game bank"""
    
    #Initialises 19 of each resource
    resources = {}
    for resource in game_info.resources:
        resources[resource] = 19
        
    #creates the development card bank
    cards = game_info.cards
    
    return resources, cards

 
##CONSTRUCTS/ASSETS


def build(player_info : PlayerInfo):
    """Asks the player what they would like to build, then builds it"""
    
    while True:
        action = input("What would you like to build?\n˚₊ · »-♡→ ").strip().lower()
        
        if action in ['x', 'cancel']:
            break
        elif action == 'road':
            place_road(player_info, grid)
                    
    return player_info

    
def place_road(player_info : PlayerInfo, grid : Grid) -> tuple[PlayerInfo, Grid]:
    """Places down a road and changes player information accordingly, as well as the grid. Does not take resources from the player in the process."""
    
    player = player_info.player_turn
    
    valid = False
    while not valid:
        text = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, where are you placing your road?") + "\n˚₊ · »-♡→ ").strip()
        valid = check(text, grid, player_info, "road")
        if text == 'cls':#allows player to clear their screen
            clear_screen()
            print_board(player_info, grid)
            
    player_info.player_dicts[player]['roads'].append(text)
    grid.roads[quick_reorder(text)]['display'] = ansi_stitching(player_info.player_dicts[player]['color'], grid.roads[quick_reorder(text)]['display'])
    clear_screen()
    print_board(player_info, grid)
    
    player_info.game_bank['constructs']['roads'][quick_reorder(text)] -= 1
    return player_info, grid


def place_settlement(player_info : PlayerInfo, grid, game_bank):
    """Places down a settlement. Does not deduct any resources from the player, do this separately"""

    player = player_info.player_turn
    valid = False
    while not valid:
        text = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, where would you like to place your settlement?") + "\n˚₊ · »-♡→ ").strip()
        valid = check(text, grid, player_info, "settlement")
        if text == 'cls':
            clear_screen()
            print_board(player_info, grid)
    player_info.player_dicts[player]['settlements'].append(text)
    print(grid.settlement_locs[text]['display'])
    grid.settlement_locs[text]['display'] = ansi_stitching(player_info.player_dicts[player]['color'], grid.settlement_locs[text]['display'])
    grid.settlement_locs[text]['owner'] = player
    clear_screen()
    print_board(player_info, grid)

    return player_info, grid
    
	
##PROCESSING


def quick_reorder(road : str):
    """Reorders a 2-letter string based on ascii values (alphabetical order I suppose). 
        This allows me to standardise the way in which roads are called from the dictionary."""

    if road[0] > road[1]:
        road = road[1] + road[0]

    return road


def check(text : str, grid : Grid, player_info : PlayerInfo, mode : str) -> bool:
	"""Checks if the settlement/road is eligible to be claimed"""

	valid = True 
	if mode == 'settlement':
		settlement = text
		try:
			if grid.settlement_locs[settlement]['owner'] != 0:
				print("This settlement is already taken. Pro tip: if it has a colour, it's not up for grabs.")
				valid = False
			else:
				related_roads = []
				for road in grid.roads:
					if settlement in road:
						related_roads.append(road)
				related_settlements = []
				for road in related_roads:
					for place in road:
						if place != settlement:
							related_settlements.append(place)
				for place in related_settlements:
					if grid.settlement_locs[place]['owner'] != 0:
						print(f"It looks like you're trying to place a settlement adjacent to another settlement, 'location {place}'. You must place it at least two roads away.")
						valid = False
						break
		except KeyError:
			if settlement in grid.settlement_locs:
				valid = True
			else:
				print("That settlement doesn't exist.")
				valid = False

		if player_info.game_stage != 1:
				case = False
				for road in grid.roads:
						if settlement in road:
								if grid.roads[road]['owner'] != 0:
										owner = grid.roads[road]['owner']
										if owner == player_info.player_turn:
												case = True

				if case:
						print("Congratulations on obtaining a new settlement.")
				else:
						print("You can only build next to a road that you own. Sorry.")
						valid = False


	elif mode == 'road':

			try:
					text = quick_reorder(text)
			except IndexError:
					pass

			if text not in grid.roads:
					valid = False
					print("That road doesn't exist.")

			else:      
					owner = grid.roads[text]['owner']
					if owner != player_info.player_turn and grid.roads[text]['owner'] != 0:
							print("That road already belongs to someone else.")
							valid = False         
					case = False
					for settlement in text:
							if grid.settlement_locs[settlement]['owner'] != 0:
									owner = grid.settlement_locs[settlement]['owner']
									if player_info.player_turn == owner:
											case = True

							for road in grid.roads:
									if settlement in road:
											owner = grid.settlement_locs[settlement]['owner']
											if player_info.player_turn == owner:
													case = True
													
							for road in player_info.player_dicts[player_info.player_turn]["roads"]:
									for char in road:
											if char in text:
													case = True
					
					if valid != False and case:
							print("Congratulations on paving a new road.")
					else:
							print("You don't own any settlements/roads next to that road, so you can't build it. Sorry.")
							valid = False

	return valid


def check_road(text : str, grid : Grid, player_info : PlayerInfo) -> bool:
    try:
        quick_reorder(text)
    except IndexError:
        print("Roads are two letters long. Please enter the settlements that you are stringing together!")
        return False
    
    if text not in grid.roads:
        print("That road doesn't exist.")
        return False
    
    owner = grid.roads[text]['owner']
    if owner != player_info.player_turn and owner != 0:#checks if a player that's not the current one owns it
        print(f"That road already belongs to player {owner}. Better luck next time.")
        return False
    
    for settlement in text:
        owner = grid.settlement_locs[settlement]['owner']
        if owner != 0
    
    return False#FLAGFLAGFLAG


def create_classes() -> tuple[Grid, PlayerInfo, GameInfo]:
    """Sets up class variables for later use"""
    game_info = GameInfo()
    number_tokens = make_token_list()
    biomes = make_biomes()
    quick_key, player_dicts = create_player_info()
    game_bank = create_game_bank(game_info)
    tiles, robber, settlement_locs, roads = make_grid(biomes, number_tokens, game_info.associated_settlements)
    
    
    grid = Grid(robber, tiles, settlement_locs, roads, biomes)
    player_info = PlayerInfo(game_bank, quick_key, player_dicts)
    clear_screen()
    
    return grid, player_info, game_info


def allow_turn_end(roll_allowed : bool, player_info : PlayerInfo) -> bool:
        """Checks if the turn can end and returns the turn"""
        
        if not roll_allowed:
                if check_password(player_info.player_turn, player_info):
                        print("Your turn has ended.")
                        turn = False
        else:
                print("You must roll before you can end your turn."
                      )
                turn = True
                
        return turn
  
    
##PROGRAM STAGES


def get_initial_inputs():
    print("""WELCOME TO MY TEXT-BASED CATAN.
Before we start, make sure \x1b[38;2;142;194;21mthis text\x1b[0m is green!
CREDITS: Vivienne, CATAN game studio. To start the game, type 'start', or type 'rng' to gamble!
To see the available commands, type 'cmds'.
ENTER YOUR COMMAND TO BEGIN""")#the welcome message
    
    while True:
        action = input("What would you like to do? :)\n˚₊ · »-♡→ ").lower()  
        if action == 'start':
            print("Starting your game now!")
            #aesthetics for a loading/clearing screen
            time.sleep(1)
            clear_screen()
            break
        elif action == 'rng':
            print("Sorry, that's been removed from the program now.")#currently under work. i might add it back but there were some fishy calculations
        elif action == 'cls':
            clear_screen()
        elif action == 'cmds':
            print("""The available commands are:
> 'cls' clears your screen
> 'start' starts your game
> 'rng' begins rng
'cmds' allows you to view current commands.""")
        else:
            print("That's not currently a valid command.")
      

def initial_loop(player_info : PlayerInfo, grid : Grid) -> tuple[PlayerInfo, Grid]:
    """Carries out the initial loop for the players to place down their settlements and roads FOR FREE."""
    
    game_bank = player_info.game_bank

    print_board(player_info, grid)
    print(f"We'll go from player 1 to player {len(player_info.quick_key)}; you can place two settlements and two roads for free. Please choose wisely.")

    for i in range(2):
        for player in player_info.quick_key:
            player_info.player_turn = player
            
            player_info, grid = place_settlement(player_info, grid, game_bank)
            player_info, grid = place_road(player_info, grid, game_bank)
                    

    player_info.player_turn = 1
    player_info.game_bank = game_bank
                    
    return player_info, grid


def main_game(player_info, grid):
    """The main input loop after initial resource setup"""
    
    game = True##begins the game
    player_info.game_stage = 2#enters main game. stage 2 is just the stage ykwim
    game_bank = player_info.game_bank

    while player_info.game_stage == 2 and game:

        for player in player_info.quick_key:
            if not game:
                print("Game has ended!")
                break
            
            player_info.player_turn = player
            turn = True
            roll_allowed = True
            while turn:
                action = input(ansi_stitching(player_info.player_dicts[player]['color'], f"Player {player}, what's your move?") + "\n˚₊ · »-♡→ ").strip().lower()

                if action == "end turn":
                    turn = allow_turn_end(roll_allowed, player_info)

                elif action == "build":
                    build(player_info)
                
                elif action == "trade":
                    choice = call_trade(player_info, grid, game_bank)
                        
                elif action == "roll":
                    game_bank, player_info = allow_roll(roll_allowed, player_info, grid, game_bank)
                        
                elif action == "cls":
                    clear_screen()
                    print_board(player_info, grid, game_bank)
                        
                else:
                    print("That action doesn't exist.")
                            
                                    
            game = check_if_game(calculate_VP(player_info), player_info)
            clear_screen()
            print_board(player_info, grid, game_bank)
                    
    print("Game has ended :)")
    
    
def main():
    """Main code for the game, initially called"""
    #sys.exit()########remove this line if playing
    get_initial_inputs()#the initial input loop ends as soon as the game starts
    grid, player_info, game_info = create_classes()#assigns variables to the classes and makes them direct objects to call
    player_info.player_dicts = add_colours(player_info)#gives each player colours
    player_info.player_dicts = add_keys(player_info, game_info)#adds further keys to player dictionaries
    player_info, grid = initial_loop(player_info, grid)#go through the initial loop for the game
    print(player_info.player_dicts)#FLAGFLAGFLAG
    
    
##DO NOT TOUCH
    
if __name__ == "__main__":
    main()
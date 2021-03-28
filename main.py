from Classes import HandMatch, Player
from random import random


n_players = 6

player_list = [Player("", random()*100//1) for _ in range(n_players//2)]
Hand_match = HandMatch(n_players)

for player in player_list:
    Hand_match << player

[table.deck >> table.players[p] for p in table.players if table.players[p]]
[table.deck >> table.players[p] for p in table.players if table.players[p]]




# d1 = Dealer()
#
#
# deck >> None
# deck >> player
# deck >> table
# player.show_hand()
# table
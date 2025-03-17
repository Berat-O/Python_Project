# Mini-Project-1: Pig 
"""
Players take turns to roll a single die as many times as they wish, adding all roll results to a running total, 
but losing their gained score for the turn if they roll a 1.
The first player to score the maximum points wins.
"""

import random
import time

def roll():
    min_val = 0
    max_val = 19
    roll = random.randint(min_val, max_val)
    return roll

print("\n_______WELCOME_TO_PIG______\n")

while True:
    min_players = int(input("Minimum Players : "))
    max_players = int(input("Maximum Players : "))
    players = input(f"Enter total number of players({max_players} max): ")
    if players.isdigit():
        players = int(players)
        if min_players <= players <= max_players:
            break
        elif players < min_players:
            print(f"Minimum {min_players} players allowed")
        else:
            print(f"Only {min_players} - {max_players} allowed")
    else:
        print("Invalid Number. Please do not enter alphanumerics or symbols.")
print(players)

max_score = 100
player_scores = [0 for _ in range(players)]
print(player_scores)

for player_idx in range(players):
    print(f"\nPlayer No. {player_idx + 1} turn has now started")
    curr_score = 0
    while True:
        player_roll = input("Would you like to roll(y/n)? ")
        if player_roll.lower() == 'y':
            value = roll()
        else:
            break
        if value == 1:
            print("You rolled 1. Turn done!")
            break
        elif player_roll.lower() == 'n':
            print("Player choses to stop. Turn done!")
            break
        else:
            curr_score += value 
            print(f"You rollled {value}")
        print(f"Current Score : {curr_score}")
    player_scores[player_idx] += curr_score
    print(f"Player Total Score: {player_scores[player_idx]}")
print(player_scores)

max_score = max(player_scores)
winner = player_scores.index(max_score)
print(f"Winner : {winner + 1}, Score : {max_score}")
import random

def roll():
    return random.randint(1, 6)  # standard die

print("\n_______WELCOME TO PIG______\n")

# Setup players
while True:
    min_players = int(input("Minimum Players : "))
    max_players = int(input("Maximum Players : "))
    players = input(f"Enter total number of players ({max_players} max): ")
    if players.isdigit():
        players = int(players)
        if min_players <= players <= max_players:
            break
        elif players < min_players:
            print(f"Minimum {min_players} players allowed")
        else:
            print(f"Only {min_players} - {max_players} allowed")
    else:
        print("Invalid number. Please do not enter letters or symbols.")

# Game setup
winning_score = 100
player_scores = [0 for _ in range(players)]
print(f"\nGame started with {players} players. First to {winning_score} wins!\n")

# Main game loop
winner = None
while not winner:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn")
        curr_score = 0
        while True:
            player_roll = input("Roll the die? (y/n): ").lower()
            if player_roll == 'y':
                value = roll()
                print(f"You rolled {value}")
                if value == 1:
                    print("Oops! You rolled a 1. Turn over, no points this round.")
                    curr_score = 0
                    break
                else:
                    curr_score += value
                    print(f"Current turn score: {curr_score}")
            elif player_roll == 'n':
                print("Player chooses to hold. Turn over.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        player_scores[player_idx] += curr_score
        print(f"Total score for Player {player_idx + 1}: {player_scores[player_idx]}")

        if player_scores[player_idx] >= winning_score:
            winner = player_idx
            break

# Announce winner
print("\nGame Over!")
print(f"Winner: Player {winner + 1} with {player_scores[winner]} points 🎉")

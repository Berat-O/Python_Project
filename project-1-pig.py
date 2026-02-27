import random

def roll():
    """Return a random integer between 1 and 6 (simulating a die)."""
    return random.randint(1, 6)  # standard die

print("\n_______WELCOME TO PIG______\n")

# Setup players
while True:
    min_players = int(input("Minimum Players : "))
    max_players = int(input("Maximum Players : "))
    total_players_input = input(f"Enter total number of players ({max_players} max): ")
    if total_players_input.isdigit():
        total_players = int(total_players_input)
        if min_players <= total_players <= max_players:
            break
        elif total_players < min_players:
            print(f"Minimum {min_players} players allowed")
        else:
            print(f"Only {min_players} - {max_players} allowed")
    else:
        print("Invalid number. Please do not enter letters or symbols.")

# Game setup
winning_score = 100
player_scores = [0 for _ in range(total_players)]
print(f"\nGame started with {total_players} players. First to {winning_score} wins!\n")

# Main game loop
winner = None
while winner is None:
    for player_index in range(total_players):
        print(f"\nPlayer {player_index + 1}'s turn")
        current_score = 0
        while True:
            player_choice = input("Roll the die? (y/n): ").lower()
            if player_choice == 'y':
                dice_value = roll()
                print(f"You rolled {dice_value}")
                if dice_value == 1:
                    print("Oops! You rolled a 1. Turn over, no points this round.")
                    current_score = 0
                    break
                else:
                    current_score += dice_value
                    print(f"Current turn score: {current_score}")
            elif player_choice == 'n':
                print("Player chooses to hold. Turn over.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        player_scores[player_index] += current_score
        print(f"Total score for Player {player_index + 1}: {player_scores[player_index]}")

        if player_scores[player_index] >= winning_score:
            winner = player_index
            break

# Announce winner
print("\nGame Over!")
print(f"Winner: Player {winner + 1} with {player_scores[winner]} points 🎉")

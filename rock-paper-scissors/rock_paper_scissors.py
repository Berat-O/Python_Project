"""
Rock, Paper, Scissors Game
A simple command-line game where you play against the computer.
"""

import random


def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_user_choice():
    """Get and validate the user's choice."""
    while True:
        user_input = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()
        
        if user_input == 'quit':
            return None
        
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")


def determine_winner(user_choice, computer_choice):
    """Determine the winner of the round."""
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"


def display_result(user_choice, computer_choice, winner):
    """Display the result of the round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round! 🎉")
    else:
        print("Computer wins this round!")


def play_game():
    """Main game loop."""
    print("=" * 50)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 50)
    print("\nGame Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    
    # Score tracking
    user_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice is None:
            break
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        else:
            ties += 1
        
        # Display current score
        print(f"\nScore - You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    
    # Display final results
    print("\n" + "=" * 50)
    print("Thanks for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    
    if user_score > computer_score:
        print("Congratulations! You won overall! 🏆")
    elif computer_score > user_score:
        print("Computer won overall. Better luck next time!")
    else:
        print("It's an overall tie!")
    print("=" * 50)


if __name__ == "__main__":
    play_game()
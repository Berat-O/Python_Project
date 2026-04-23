import random

def play_game():
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it correctly.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Set the number of allowed attempts
    attempts = 7

    # Game loop
    while attempts > 0:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess: "))

            # Ensure that guess is between 1-100
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue

            # Check if the guess is correct
            if guess == secret_number:
                print("🎉 Congratulations! You guessed the number!")
                return
            elif guess < secret_number:
                print("Too low. Try a higher number.")
            else:
                print("Too high. Try a lower number.")

            # Decrease remaining attempts
            attempts -= 1
            print(f"Attempts left: {attempts}\n")

        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.\n")

    # If no attempts are left
    if attempts == 0:
        print(f"❌ Game over! The number was {secret_number}. Better luck next time.")

def ask_to_play_again():
    # Play again option
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    return play_again == "y"

def main():
    # Introduction
    print("Welcome to the Guessing Game!")

    while True:
        play_game()
        if not ask_to_play_again():
            print("Thanks for playing!")
            break



main()
import random

# Introduction
print("Welcome to the Guessing Game!")
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

        # Check if the guess is correct
        if guess == secret_number:
            print("🎉 Congratulations! You guessed the number!")
            break
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

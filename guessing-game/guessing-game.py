import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 attempts to guess it correctly.\n")

secret_number = random.randint(1, 100)
attempts = 7

while attempts > 0:
    user_input = input("Enter your guess (1-100): ")

    # Check if input is a number
    if not user_input.isdigit():
        print("❌ Please enter a valid number.\n")
        continue

    guess = int(user_input)

    # Check range
    if guess < 1 or guess > 100:
        print("❌ Number must be between 1 and 100.\n")
        continue

    # Game logic
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    attempts -= 1
    print(f"Attempts left: {attempts}\n")

if attempts == 0:
    print(f"❌ Game over! The number was {secret_number}.")
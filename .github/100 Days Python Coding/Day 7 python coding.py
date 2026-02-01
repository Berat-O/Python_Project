# Project: Hangman
import random
from hangman_art import stages, logo
from hangman_word import word_list
# from replit import clear 

# Logo
print(logo)

# Randomly choose a word from the list
random_word = random.choice(word_list)
# print(random_word)

# Number of lives available
lives = 6
end_of_game = False

# Create a list to display guessed letters if correct
display = []
for letter in random_word:
    display += "_"
print(display)
while not end_of_game:
    
# Ask user to guess a letter from the word
    guess = input("Guess a letter from the secret word: ").lower().strip()

    # User guessed a letter that is already guessed
    if guess in display:
        print(f"You've already guessed {guess}")
    
# Check if the guessed letter is in the word
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
        if "_" not in display:
            end_of_game = True
            print("You win!")
    print(display)
    # clear()
    
  # Guess a wrong letter  
    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 6:
            print(stages[6])
        elif lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        elif lives == 0:
            print(stages[0])
        if lives == 0:
            end_of_game = True
            print("You lose!")
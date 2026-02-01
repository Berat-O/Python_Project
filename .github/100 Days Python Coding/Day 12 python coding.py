# Namespaces: Local vs Global Scopes
lives = 6
def live_left():
  lives = 1
  return lives
print(live_left())
print(lives)

# Project: Guess the Number
import random

def difficulty_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10  
  elif level == "hard":
    return 5

def check_guess(guess, random_number, attempt):
  if guess < 1 or guess > 100:
    print("Invalid number. Please enter a number between 1 and 100.")
  elif guess < random_number:
    print("Too low.")
    return attempt - 1
  elif guess > random_number:
    print("Too high.")
    return attempt - 1
  else:
    print(f"You got it! The answer was {random_number}.")
 
def play_game():
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100. ")
  rand_num = random.randint(1, 100)

  attempt = difficulty_level()

  guess = 0
  while guess != rand_num:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempt = check_guess(guess, rand_num, attempt)
    if attempt == 0:
        print("You've run out of guesses, you lose!")
        return
    elif guess != rand_num:
      print("Guess again.")
     
play_game()





      

  
  
  







  
 
 
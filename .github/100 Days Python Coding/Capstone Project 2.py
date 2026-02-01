## Capstone Project: Higher Lower Game
import random
from data import data
from replit import clear

# Import asciiart in art
from art import logo, vs

# Create a function that compares the follower_count of variable_a and variable_b and returns the one with the higher score.
def highest_follower(a_follower, b_follower):
  highest_follower = 0
  if a_follower['follower_count'] > b_follower['follower_count']:
    highest_follower = a_follower['follower_count']
    return highest_follower
  else:
    highest_follower = b_follower['follower_count']
    return highest_follower
    
 # Create a function that checks answer and returns the follower_count of the player's guess.   
def check_answer(guess, a_follower, b_follower):
  if guess == "a":
    return a_follower['follower_count']
  elif guess == "b":
    return b_follower['follower_count']
  else:
    print("Invalid input. Please try again.")

# Create a function that ask player if they want to play again.
def play_again():
  play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
  if play_again == "y":
    clear()
    play_game()
  else:
    print("Goodbye!")

def play_game():
  
  # Randomly select dictionary from the list of data and assign it to variable_a and another to variable_b. Radomly generated dictionaries should return other items except follower_count.
  variable_a = random.choice(data)
  variable_b = random.choice(data)
  
  # Create a function that checks if variable_a and variable_b are the same. If they are, randomly select another dictionary from the list of data and assign it to variable_b.
  def start_game(variable_a, variable_b):
    print(logo)
    while variable_a == variable_b:
      variable_b = random.choice(data)
  
    print(f"Compare A: {variable_a['name']}, a {variable_a['description']},from {variable_a['country']}")
    
    print(vs)
    
    print(f"Against B: {variable_b['name']}, a {variable_b['description']},from {variable_b['country']}")

  start_game(variable_a, variable_b)
  # Function that compares and returns the highest follower count
  max_follower = highest_follower(a_follower=variable_a, b_follower=variable_b)
  # print(f"Highest follower count: {max_follower}")
  
  # Create a function that will receive the player's answer.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  guess_count = check_answer(guess=guess, a_follower=variable_a, b_follower=variable_b)
  # print(f"The guess_count: {guess_count}")

  # compare_answer(guess_count, max_follower)
  score = 0
  if guess_count == max_follower:
    score += 1
    # print(f"You're right! Current score: {score}")
  else:
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")
    play_again()
  
# Create a loop that runs while the player's guess is correct, and create a new variable for the next round.
  while guess_count == max_follower:
    clear()
    print(f"You're right! Current score: {score}")
    if variable_a['follower_count'] != max_follower:
      variable_a = variable_a
    else:
      variable_a = variable_b
    variable_b = random.choice(data)
    
    start_game(variable_a, variable_b)
    max_follower = highest_follower(a_follower=variable_a, b_follower=variable_b)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    guess_count = check_answer(guess=guess, a_follower=variable_a, b_follower=variable_b)
    # compare_answer(guess_count, max_follower)
    if guess_count == max_follower:
      score += 1
      # print(f"You're right! Current score: {score}")
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")
      play_again()
  
play_game()





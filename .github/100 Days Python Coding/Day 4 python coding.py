# Random Module
import random
random_integer = random.randint(1, 20)
print(random_integer)
# Random_float
random_float = random.random()
print(random_float)

# Exercise
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
coin_side = random.randint(0, 1)
if coin_side == 0:
  print("Heads")
else:
  print("Tails")

# Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",  "Alaska", "Hawaii"]
print(states_of_america[0])
print(states_of_america[-1])
states_of_america.insert(0, "Puerto Rico")
states_of_america.insert(len(states_of_america), "News State")
print(states_of_america)

# Exercise: Who is paying the bill?
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names including yours separated by a comma. ")
names = names_string.split(", ")
name_length = len(names)
random_choice = random.randint(0, name_length - 1)
chosen_name = names[random_choice]
print(f"{chosen_name} is going to buy the meal today!")

# Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Exercise: Treasure Map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# Project: Rock Paper Scissors
rock = '''
 _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
      '''
paper = '''
 _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
      '''
scissors = '''
 _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
      '''
import random
fig = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if fig == 0:
  print(rock)
elif fig == 1:
  print(paper)
else:
  print(scissors)
computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print(f"Computer chose:\n{rock}")
elif computer_choice == 1:
  print(f"Computer chose:\n{paper}")
else:
  print(f"Computer chose:\n{scissors}")
if fig == 0 and computer_choice == 0:
  print("It's a draw")
elif fig == 0 and computer_choice == 1:
  print("You lose")
elif fig == 0 and computer_choice == 2:
  print("You win")
elif fig == 1 and computer_choice == 0:
  print("You win")
elif fig == 1 and computer_choice == 1:
  print("It's a draw")
elif fig == 1 and computer_choice == 2:
  print("You lose")
elif fig == 2 and computer_choice == 0:
  print("You lose")
elif fig == 2 and computer_choice == 1:
  print("You win")
elif fig == 2 and computer_choice == 2:
  print("It's a draw")
else:
  print("You typed an invalid number, try again")
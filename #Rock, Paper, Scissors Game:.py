##Rock, Paper, Scissors Game:

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
fig = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if fig == 0:
  print(rock)
elif fig == 1:
  print(paper)
else:
  print(scissors)
#Computer's choice
print("Computer's choice:")
computer_choice = random.randint(0,2)
if computer_choice ==0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
  #Game logic
if fig == computer_choice:
  print("It's tie, give it another try")
  fig = int(input("Pick another number:"))
  if fig == 0:
    print(rock)
  elif fig == 1:
    print(paper)
  else:
    print(scissors)
  #Player wins
elif fig == 0 and computer_choice == 2:
  print("You win! Do you want to play again?")
elif fig == 1 and computer_choice == 2:
  print("You win! Do you want to play again?")
elif fig == 2 and computer_choice == 1:
  print("You win! Do you want to play again?")
  #Computer wins
if computer_choice == 0 and fig == 2:
  print("You lose!, do you want to play again?")
elif computer_choice == 1 and fig == 0:
  print("You lose!, do you want to play again?")
elif computer_choice == 2 and fig == 1:
   print("You lose!, do you want to play again?")
  
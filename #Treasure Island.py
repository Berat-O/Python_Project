#Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
lower_choice1 = choice1.lower()
if lower_choice1 == "left":
  print("You have come to a lake. There is an island in the middle of the lake.")
  choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
  lower_choice2 = choice2.lower()
  if lower_choice2 == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
    choice3 = input("Which colour do you choose?\n")
    colour = choice3.lower()
    if colour == "red":
      print("You just got burned by the flame from a dinosaur mouth. Game Over.")
    elif colour == "yellow":
      print("You found the treasue and won the game. Congratulations! You are now rich. Get ready for the next adventure.")
    else:
      print("You got eaten by a blue dragon. Game Over.")
  else:
    print("You got attacked by an angry sea beast. Game Over.")
else:
  print("You fell into a hole and died. Game Over.")
  
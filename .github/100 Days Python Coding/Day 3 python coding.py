#Control overflow; if else and conditional statements
number = int(input("Which number do you want to check? "))
if number %2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#Nested if and elif statements
# Ticket issuance
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

# BMI Calculator Advanced
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2, 1)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
  print(f"Your BMI is {bmi}, you are obese.") 
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

# Exercise: Leap Year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"The year {year} is a leap year.")
    else:
      print(f"The year {year} is not a leap year.")
  else:
    print(f"The year {year} is a leap year.")
else:
  print(f"The year {year} is not a leap year.")

# Multiple if statements in succession
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    bill = 5
    print("child ticket is $5.")
  elif age <= 18:
    bill = 7
    print("Youth ticket is $7.")
  elif age >= 45 and age <= 55:
    print("We have got a special offer for you. Your ticket is free.")
  else:
    bill = 12
    print("Adult ticket is $12.")
  photo_shoot = input("Do you want a photo taken? Y or N. ")
  if photo_shoot == "Y":
    bill += 3
  print(f"Your final bill is ${bill}.")
else:
  print("Sorry, you have to grow taller before you can ride.")

# Exercise: Pizza Order
print("Welcome to Sumptuous Pizza Deliveries!")
size = input("What pizza size would you like to get? S, M, or L. ")
pepperoni = input("Do you want pepperoni? Y or N. ")
bill = 0
if size == "S":
   bill += 15
   print("Small pizza is $15.")
elif size == "M":
  bill += 20
  print("Medium pizza is $20.")
else:
  bill += 25
  print("Large pizza is $25.")
if pepperoni == "Y":
   if size == "S":
   bill += 2
   else:
   bill += 3
extra_cheese = input("Do you want extra cheese? Y or N. ")
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is: ${bill}.")

# Exercise: Love Calculator
print("Welcome to the Love Calculator!")
print("Input your first and last names only to get your love score.")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1 + name2
lower_case_names = combined_names.lower()
t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
true = t + r + u + e
love = l + o + v + e
true_love = str(true) + str(love)
true_love_int = int(true_love)
print("Your love score is calculating...")
if true_love_int < 10 or true_love_int > 90:
  print(f"Your score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int >=40 and true_love_int <= 50:
  print(f"Your score is {true_love_int}, you are alright together.")
else:
  print(f"Your score is {true_love_int}, we hope you get along together.")

# Project: Treasure Island
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
print("Your mission is to find the lost treasure that is hidden at the end of a desserted island")
print("You just landed on the island by an helicopter and you are at the crossroad now. Where do you want to go?")
first_choice = input('Type "left" or "right" to choose your path.\n')
first_choice_lower = first_choice.lower()
first_move = first_choice_lower.strip()
if first_move == "left":
  print("You have chosen the left path. You have successfully crossed the dark forest and now, you are at the lake side. What do you want to do?")
  second_choice = input('Type "wait" to wait for a boat or type "swim" to swim across the lake. The choice is yours, make your decision quickly.\n')
  second_choice_lower = second_choice.lower()
  second_move = second_choice_lower.strip()
  if second_move == "wait":
    print("You have chosen the right choice. You have successfully boarded a boat and now, you have reached the island. You are now in front of the castle where the treasure is hidden. Wanna get the treasure?")
    third_choice = input('You wanna proceed further? Type "Blue", "Red" or "Yellow" to choose the door you want to open. Be very careful, the wrong choice will cost you your dear life.\n')
    third_choice_lower = third_choice.lower()
    third_move = third_choice_lower.strip()
    if third_move == "yellow":
      print("Congratulations! You have found the treasure hidden for decades. Now, you can return home as a hero and conqueror. Your people will be proud of you. You have won the game.")
    elif third_move == "red":
      print("You just opened a door full of packs of hungry wolves, how would you survive? You have been eaten alive by the wolves. Game Over.")
    else:
      print("You just opened a door full of fire. You have been smoked to ashes by the fire. Game Over.")
  else: 
    print("What a bad decision you just made! You have been eaten by a crocodile. Game Over.")  
else:
  print("You have chosen the right path. Unfortunately, you have been biten by a poisonous snake and died. Game Over.")
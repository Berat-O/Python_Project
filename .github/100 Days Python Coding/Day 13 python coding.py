# Debugging
# Describe the problem
def my_function():
  for i in range(1, 21):
   if i == 20:
     print("You got it")
my_function()

# Reproduce the bug
from random import randint
dice_ings = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 5)
print(dice_ings[dice_num])

# Play computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the error
age = int(input("How old are you? "))
if age > 18:
   print(f"You can drive at age {age}.")

# Print is your friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Use a debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)
mutate([1,2,3,5,8,13])

# Exercise 1
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# Exercise 2
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")

else:
#   print("Not leap year.")

# Exercise 3
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)


# # For Loop
fruits = ["apples", "pears", "oranges", "bananas"]
for fruit in fruits:
  print(fruit)
  print(fruit + "pie")
# Exercise 1: Average Height
student_heights = input("Input a list of student heights ").replace(',', ' ').split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
  total_height += height
num_of_students = 0
for student in student_heights:
  num_of_students += 1
average_height = round(total_height / num_of_students)
print(f"The average height is {average_height}")

# Exercise 2: The Highest Score
student_scores = input("Input a list of student scores ").replace(', ', ' ').split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
  else:
    highest_score = highest_score
print(f"The highest score in the class is: {highest_score}")

# Exercise 3: Adding Even Numbers
total = 0
for num in range(2, 101, 2):
  total += num
print(total)
# or
total1 = 0
for num in range(1, 101):
  if num % 2 == 0:
    total1 += num
print(total1)

# Exercise 4: FizzBuzz Game
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)

# Project: PyPassword Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
            'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))
password = ""
for char in range(1, no_letters + 1):
  password += random.choice(letters)
for char in range(1, no_symbols + 1):
  password += random.choice(symbols)
for char in range(1, no_numbers + 1):
  password += random.choice(numbers)
#Randomize password
randomized_password = ""
for num in range(1, len(password) + 1):
  randomized_password += random.choice(password)
print(f"Your password is: {randomized_password}")
#or
password_list = []
for char in range(1, no_letters + 1):
  password_list.append(random.choice(letters))
for char in range(1, no_symbols + 1):
  password_list.append(random.choice(symbols))
for char in range(1, no_numbers + 1):
  password_list.append(random.choice(numbers))
random.shuffle(password_list)
# Randomized password
password = ""
for char in password_list:
  password += char
print(f"Your password is: {password}")
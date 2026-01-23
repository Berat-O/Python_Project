#For Loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for a in fruits:
  print(a)
  print("I love " + a)

  #Average Height Calcuation
student_heights = input("Input a list of student heights\n").split( )
for n in range(0,len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
  total_height += height
number_of_students = 0
for student in range(0, len(student_heights)):
  number_of_students = student + 1
average_height = round(total_height / number_of_students)
print(f"The average height is {average_height}")

#High score exercise
student_scores = input("Input a list of student scores: \n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

#For loop with range
for num in range(1, 21, 5):
  print(num)

#Sum of numbers btw 1 and 100
total = 0
for num in range(1, 101):
  total += num
print(total)

#Sum of even numbers btw 1 and 100
total = 0
for num in range(0, 101, 2):
  total += num
print(total)
#OR
total_x = 0
for num in range(1, 101):
  if num % 2 == 0:
    total_x += num
print(total_x)

#Mini Project
#FizzBuzz Game
#write a program that automatically prints the solution to the FizzBuzz game, for the numbers 1 through 100.
for numbers in range(1, 101):
  if numbers % 3 == 0 and numbers % 5 == 0:
    print("FizzBuzz")
  elif numbers % 3 == 0:
    print("Fizz")
  elif numbers % 5 == 0:
    print("Buzz")
  else:
    print(numbers)


##Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like\n"))
#Level 1
password = ""
for char in range(1, num_letters + 1):
  rand_letter = random.choice(letters)
  password += rand_letter
for char in range(1, num_symbols + 1):
  rand_symbol = random.choice(symbols)
  password += rand_symbol
for char in range(1, num_numbers + 1):
  rand_number = random.choice(numbers)
  password += rand_number
print(password)
#Or
#Level 2
password_list = []
for char in range(1, num_letters +1):
  rand_letter = random.choice(letters)
  password_list.append(rand_letter)
for char in range(1, num_symbols + 1):
  rand_symbol = random.choice(symbols)
  password_list.append(rand_symbol)
for char in range(1, num_numbers + 1):
  rand_number = random.choice(numbers)
  password_list.append(rand_number)
random.shuffle(password_list)
password = ""
for char in password_list:
  password += char
print(f"Your password is {password}")
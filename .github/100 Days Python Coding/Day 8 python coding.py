# Functions with input
def greet():
  print("Hello")
  print("How are you doing?")
  print("I am a great machine learning engineer")
greet()

# Functions with parameters
def greet_my_friend(name):
  print(f"Hello {name}")
  print(f"How are you doing {name}?")
  print(f"{name} is a good friend of mine")
greet_my_friend("Tomiwa")

# Functions with positional arguments
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"Tell me about you")
  print(f"How can you relate similar situations in your {location}?")
greet_with("Blessing", "Abeokuta")

# Functions with keyword arguments
def greet_colleagues(name, location, status):
  print(f"Hello, my name is {name}")
  print(f"I currently reside in {location}")
  print(f"I am {status} at the moment hopefully my status may change soon.")
greet_colleagues(status="single", location="Lagos", name="Tomiwa")

# Exercise 1: Paint Area Calculator
height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage_area = 5
def paint_calc(h, w, c_a):
  area = height * width
  no_of_cans = round(area / coverage_area)
  print(f"You will need {no_of_cans} cans of paint.")
paint_calc(h=height, w=width, c_a= coverage_area)

# Exercise 2: Prime Number Checker
num = int(input("Input a number to check if it is a prime number or not: "))
def prime_checker(number):
  is_prime = True
  for i in range(2, number - 1):
    if number % i == 0:
      is_prime = False
  if is_prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
prime_checker(number=num)


# Project: Caesar Cipher(encryption code)

logo = """"""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
 a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
 "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
            ""             88
                           88
  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
 a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
 8b         88 88       d8 88       88 8PP""""""" 88
 "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
               a8"         88       88            
               88          88       88            
""""""
        
# from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(word, shift_no, cipher_direction):
  plain_word = ""
  if cipher_direction == "decode":
    shift_no *= -1
  for char in word:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_no
      if new_position > 25:
        new_position -= 26
      new_letter = alphabet[new_position]
      plain_word += new_letter
    else:
      plain_word += char
  print(f"Here is the {cipher_direction}d result: {plain_word}")

end_game = False
while not end_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 25
  caesar(word=text, shift_no=shift, cipher_direction=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() 
  if restart == "yes":
    end_game = False
  elif restart == "no":
    end_game = True
    print("Goodbye")
# Functions with output
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  first_name = f_name.title()
  last_name = l_name.title()
  return f"{first_name} {last_name}"

output = format_name(input("What is your first name?: "), input("What is your last name?:"))
print(output)

# Exercise: Days in Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """"Takes a year and a month and returns the number of days in that month""""
  if month > 12 or month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month - 1]

days = days_in_month(year=int(input("Enter a year: ")), month=int(input("Enter a month:")))
print(days)

# Docstring
""""Takes a year and a month and returns the number of days in that month""""
# Docstring is a string that comes right after the function declaration and is used to explain the function.

## Project: Calculator
#from art import logo_calculator
logo_calculator = """
                       _____________________
                       |  _________________  |
                       | | JO           0. | |
                       | |_________________| |
                       |  ___ ___ ___   ___  |
                       | | 7 | 8 | 9 | | + | |
                       | |___|___|___| |___| |
                       | | 4 | 5 | 6 | | - | |
                       | |___|___|___| |___| |
                       | | 1 | 2 | 3 | | x | |
                       | |___|___|___| |___| |
                       | | . | 0 | = | | / | |
                       | |___|___|___| |___| |
                       |_____________________|


                      88                     
                      88                        ,d     
                      88                        88     
,adPPYba, ,adPPYYba,  88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM  
a8"     "" ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88     
8b         ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88     
"8a,   ,aa 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,    
`"Ybbd8"' `"8bbdP"Y8 88  `"Ybbd8"'  `"YbbdP'Y8 88 `"8bbdP"Y8   "Y888 


,adPPYba,  8b,dPPYba,  
a8"     "8a 88P'   "Y8  
8b       d8 88          
"8a,   ,a8" 88          
`"YbbdP"'  88  
"""
print(logo_calculator)
# Add

def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo_calculator)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  still_calculating = True
    
  while still_calculating:
    operation_symbol = input("Pick an operation:")
    num2 = float(input("What's the next number?: "))
    cal_function = operations[operation_symbol]
    cal_function(num1, num2)
    answer = cal_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    another_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
    if another_calc == "y":
      num1 = answer
    else:
      still_calculating = False
      calculator()

calculator()

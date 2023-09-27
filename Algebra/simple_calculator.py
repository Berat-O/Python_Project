import math
import sympy
from sympy import symbols
from sympy.solvers import solve
from fractions import Fraction
import sys

def main():
   
   while True:

    main_menu()
    choice = input("Enter your choice (1-12): ")

    if choice == '1':
        add()
        check()
    elif choice == '2':
        subtract()
        check()
    elif choice == '3':
        multiply()
        check()
    elif choice == '4':
        divide()
        check()
    elif choice == '5':
        prime_number()
        check()
    elif choice == '6':
        prime_factor()
        check()
    elif choice == '7':
        square_root()
        check()
    elif choice == '8':
        solve()
        check()
    elif choice == '9':
        convert_decimals_to()
        check()
    elif choice == '10':
        convert_fractions_to()
        check()
    elif choice == '11':
        convert_percents_to()
        check()
    elif choice == '12':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-12).")
   


  


def add():
  a = int(input('Enter an integer: '))
  b = int(input('Enter an integer: '))
  print(f"a+b = {a+b}")

def subtract():
  a = int(input('Enter an integer: '))
  b = int(input('Enter an integer: '))
  print(f"a-b = {a-b}")

def multiply():
  a = int(input('Enter an integer: '))
  b = int(input('Enter an integer: '))
  print(f"a*b = {a*b}")

def divide():
  a = int(input('Enter an integer: '))
  b = int(input('Enter an integer: '))
  print(f"a/b = {a/b}")


def prime_number():
  number = int(input("Enter a positive integer: "))
  prime_or_comp = "prime"

  for test_number in range(2,number):
      # Change the if statement to test one factor here:
      if number % test_number == 0:
          prime_or_comp = "composite"

  print(prime_or_comp)


def prime_factor():
  number = int(input('Enter an integer: '))
  for test_factor in range(1, number+1):
    if number % test_factor ==0:
        print(test_factor)

def square_root():
  

  n = int(input('Without the radical, enter a square root to factor: '))

  # Use these variables
  upper_limit = math.floor(math.sqrt(n)) + 1
  max_factor = 1
  other_factor = 1
  square_root = 1

  # Notice what the loop is doing here
  for maybe_factor in range(1, upper_limit):
      if n % (maybe_factor**2) == 0:
          max_factor = maybe_factor**2

  # Divide out the greatest square factor
  other_factor = n/max_factor

  # Output - keep this:
  square_root = int(math.sqrt(max_factor))
  other_factor = int(other_factor)
  output = square_root*sympy.sqrt(other_factor)



  print(output)


def solve():
  

  x = symbols('x')

  eq = input('Enter an equation to solve for x: 0 = ')
  print(len(solve(eq,x)))
  print("x = ", solve(eq,x)[0])

def convert_decimals_to():
  

  digits = input("Enter a decimal number to convert: ")
  exponent = int(len(digits))-1
  n = float(digits)

  # Change the values of these three variables
  numerator = int(n*10**exponent)
  denominator = 10**exponent
  percent = n*100

  # Output - keep this
  print("The decimal is ", n)
  print("The fraction is ", numerator, "/", denominator)
  print("The percent is ", percent, " %")

def convert_fractions_to():
  a,b = input("Enter a fraction :").split("/")
  print("The decimal is ", int(a)/int(b))
  print("The percent is ", (int(a)/int(b))*100, " %")

def convert_percents_to():
  
  percent = input("Enter a percent :").strip("%")
  decimal=float(percent)/100
  fraction_value = Fraction(decimal).limit_denominator()



  print("The decimal is ", decimal)
  print("The fraction is ",fraction_value )

# Write your code here
def main_menu():
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Check if a Number is Prime")
    print("6. Find Prime Factors")
    print("7. Square Root Factorization")
    print("8. Solve Equation for x")
    print("9. Convert decimals to fractions and percents")
    print("10. Convert fractions to decimals and percents")
    print("11. Convert percents to decimals and fractions")
    print("12. Exit")

def check():
   
    check = input("Do you want to continue calculations ? (Y/N)").upper()
    if check == "N"  :
      sys.exit("Goodbye")
    else:
      return
   






if __name__=='__main__':
    main()

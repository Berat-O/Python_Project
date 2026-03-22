# Importing required libraries
import math                          # for mathematical functions like sqrt, isqrt
from sympy import symbols, solve, sqrt   # for solving algebra equations
from fractions import Fraction      # for fraction conversions
import sys                           # for exiting the program


def main():
    # Infinite loop to keep program running until user exits
    while True:
        main_menu()   # display menu options

        choice = input("Enter your choice (1-12): ")

        # Based on user choice, call respective function
        if choice == '1':
            perform_operation(add)
        elif choice == '2':
            perform_operation(subtract)
        elif choice == '3':
            perform_operation(multiply)
        elif choice == '4':
            perform_operation(divide)
        elif choice == '5':
            perform_operation(prime_number)
        elif choice == '6':
            perform_operation(prime_factor)
        elif choice == '7':
            perform_operation(square_root)
        elif choice == '8':
            perform_operation(solve)
        elif choice == '9':
            perform_operation(convert_decimals_to)
        elif choice == '10':
            perform_operation(convert_fractions_to)
        elif choice == '11':
            perform_operation(convert_percents_to)
        elif choice == '12':
            print("Goodbye!")
            break   # exit loop
        else:
            print("Invalid choice. Please choose a valid option (1-12).")


# ================= BASIC OPERATIONS =================

def add():
    try:
        a = int(input('Enter an integer: '))
        b = int(input('Enter an integer: '))
        print(f"a+b = {a+b}")
    except ValueError:
        print("Invalid input. Please enter integers only.")


def subtract():
    try:
        a = int(input('Enter an integer: '))
        b = int(input('Enter an integer: '))
        print(f"a-b = {a-b}")
    except ValueError:
        print("Invalid input. Please enter integers only.")


def multiply():
    try:
        a = int(input('Enter an integer: '))
        b = int(input('Enter an integer: '))
        print(f"a*b = {a*b}")
    except ValueError:
        print("Invalid input. Please enter integers only.")


def divide():
    try:
        a = int(input('Enter an integer: '))
        b = int(input('Enter an integer: '))

        if b == 0:   # prevent division by zero
            print("Cannot divide by zero!")
        else:
            print(f"a/b = {a/b}")
    except ValueError:
        print("Invalid input. Please enter integers only.")


# ================= NUMBER THEORY =================

def prime_number():
    try:
        number = int(input("Enter a positive integer: "))

        if number <= 0:
            print("Invalid input. Please enter a positive integer.")
            return

        # Check if number is prime
        is_prime = all(number % i != 0 for i in range(2, number))

        print("prime" if is_prime else "composite")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")


def prime_factor():
    try:
        number = int(input('Enter an integer: '))

        if number <= 0:
            print("Invalid input. Please enter a positive integer.")
            return

        # Find all factors of number
        factors = [i for i in range(1, number + 1) if number % i == 0]

        print(factors)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")


# ================= ROOT & EQUATIONS =================

def square_root():
    try:
        n = int(input('Without the radical, enter a square root to factor: '))

        if n <= 0:
            print("Invalid input. Please enter a positive integer.")
            return

        # Find largest perfect square factor
        max_factor = max(i**2 for i in range(1, math.isqrt(n) + 1) if n % (i**2) == 0)

        other_factor = n // max_factor   # remaining part

        square_root = int(math.sqrt(max_factor))  # √(perfect square)

        # Final simplified form using sympy sqrt
        output = square_root * sqrt(other_factor)

        print(output)

    except ValueError:
        print("Invalid input. Please enter a positive integer.")


def solve():
    try:
        x = symbols('x')   # define variable

        eq = input('Enter an equation to solve for x: 0 = ')

        solutions = solve(eq, x)   # solve equation

        print(f"x = {solutions[0]}" if solutions else "No solutions found.")

    except (ValueError, TypeError, IndexError):
        print("Invalid equation or no solutions found.")


# ================= CONVERSIONS =================

def convert_decimals_to():
    try:
        decimal = float(input("Enter a decimal number to convert: "))

        fraction = Fraction(decimal).limit_denominator()
        percent = decimal * 100

        print(f"The decimal is {decimal}")
        print(f"The fraction is {fraction}")
        print(f"The percent is {percent}%")

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")


def convert_fractions_to():
    try:
        fraction = input("Enter a fraction (numerator/denominator): ")

        numerator, denominator = map(int, fraction.split("/"))

        decimal = numerator / denominator
        percent = decimal * 100

        print(f"The decimal is {decimal}")
        print(f"The percent is {percent}%")

    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please enter a valid fraction.")


def convert_percents_to():
    try:
        percent = float(input("Enter a percent: ").strip("%"))

        decimal = percent / 100
        fraction = Fraction(decimal).limit_denominator()

        print(f"The decimal is {decimal}")
        print(f"The fraction is {fraction}")

    except ValueError:
        print("Invalid input. Please enter a valid percent.")


# ================= CONTROL FUNCTIONS =================

def perform_operation(operation_func):
    # Calls the function passed (like add, subtract, etc.)
    operation_func()

    # Ask user if they want to continue
    if not continue_calculations():
        sys.exit("Goodbye")   # exit program completely


def continue_calculations():
    check = input("Do you want to continue calculations? (Y/N): ").upper()

    return check != "N"   # return False only if user enters N


def main_menu():
    # Display all menu options
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


# Entry point of program
if __name__ == '__main__':
    main()
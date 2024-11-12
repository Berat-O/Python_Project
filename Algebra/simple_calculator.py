import math
from sympy import symbols, solve, sqrt
from fractions import Fraction
import sys

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-12): ").strip()
        
        options = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide,
            '5': prime_number,
            '6': prime_factors,
            '7': square_root_factorization,
            '8': solve_equation,
            '9': convert_decimals_to,
            '10': convert_fractions_to,
            '11': convert_percents_to,
            '12': exit_program
        }

        operation = options.get(choice)
        if operation:
            perform_operation(operation)
        else:
            print("Invalid choice. Please choose a valid option (1-12).")

def add():
    """Add two integers."""
    a, b = get_two_integers()
    print(f"{a} + {b} = {a + b}")

def subtract():
    """Subtract two integers."""
    a, b = get_two_integers()
    print(f"{a} - {b} = {a - b}")

def multiply():
    """Multiply two integers."""
    a, b = get_two_integers()
    print(f"{a} * {b} = {a * b}")

def divide():
    """Divide two integers."""
    a, b = get_two_integers()
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print(f"{a} / {b} = {a / b}")

def prime_number():
    """Check if a number is prime."""
    number = get_positive_integer()
    if number < 2:
        print("Numbers less than 2 are not prime.")
        return
    is_prime = all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1))
    print("Prime" if is_prime else "Composite")

def prime_factors():
    """Find all prime factors of a number."""
    number = get_positive_integer()
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    print(f"Prime factors: {factors}")

def square_root_factorization():
    """Factor a number under the square root."""
    n = get_positive_integer()
    max_square = max(i**2 for i in range(1, int(math.isqrt(n)) + 1) if n % (i**2) == 0)
    other_factor = n // max_square
    result = int(math.sqrt(max_square)) * sqrt(other_factor)
    print(f"√{n} = {result}")

def solve_equation():
    """Solve an equation for x."""
    x = symbols('x')
    eq = input('Enter an equation to solve for x (in the form "0 = equation"): ').strip()
    try:
        solutions = solve(eq, x)
        print(f"x = {solutions[0]}" if solutions else "No solutions found.")
    except (ValueError, TypeError):
        print("Invalid equation or no solutions found.")

def convert_decimals_to():
    """Convert decimal to fraction and percent."""
    decimal = get_float("Enter a decimal number to convert: ")
    fraction = Fraction(decimal).limit_denominator()
    percent = decimal * 100
    print(f"The fraction is {fraction}")
    print(f"The percent is {percent}%")

def convert_fractions_to():
    """Convert fraction to decimal and percent."""
    try:
        fraction = input("Enter a fraction (numerator/denominator): ").strip()
        numerator, denominator = map(int, fraction.split("/"))
        decimal = numerator / denominator
        percent = decimal * 100
        print(f"The decimal is {decimal}")
        print(f"The percent is {percent}%")
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please enter a valid fraction.")

def convert_percents_to():
    """Convert percent to decimal and fraction."""
    percent = get_float("Enter a percent (without % sign): ")
    decimal = percent / 100
    fraction = Fraction(decimal).limit_denominator()
    print(f"The decimal is {decimal}")
    print(f"The fraction is {fraction}")

def get_two_integers():
    """Get two integers from the user with error handling."""
    try:
        a = int(input('Enter first integer: '))
        b = int(input('Enter second integer: '))
        return a, b
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return get_two_integers()

def get_positive_integer():
    """Get a positive integer from the user with error handling."""
    try:
        n = int(input('Enter a positive integer: '))
        if n <= 0:
            raise ValueError
        return n
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return get_positive_integer()

def get_float(prompt):
    """Get a float value from the user with error handling."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_float(prompt)

def perform_operation(operation_func):
    """Perform a selected operation."""
    operation_func()
    if not continue_calculations():
        sys.exit("Goodbye")

def continue_calculations():
    """Prompt the user to continue calculations."""
    check = input("Do you want to continue calculations? (Y/N): ").strip().upper()
    return check == "Y"

def main_menu():
    """Display the main menu."""
    print("\nMenu:")
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

def exit_program():
    """Exit the program."""
    sys.exit()

if __name__ == '__main__':
    main()

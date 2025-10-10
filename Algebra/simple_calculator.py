import math
from sympy import symbols, solve as sympy_solve, sqrt
from fractions import Fraction
import sys

# Helper Functions

def get_int(prompt):
    """Safely get an integer input."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def get_float(prompt):
    """Safely get a float input."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

# Math Operations

def add():
    a, b = get_int("Enter first integer: "), get_int("Enter second integer: ")
    if a is not None and b is not None:
        print(f"Result: {a + b}")

def subtract():
    a, b = get_int("Enter first integer: "), get_int("Enter second integer: ")
    if a is not None and b is not None:
        print(f"Result: {a - b}")

def multiply():
    a, b = get_int("Enter first integer: "), get_int("Enter second integer: ")
    if a is not None and b is not None:
        print(f"Result: {a * b}")

def divide():
    a, b = get_int("Enter dividend: "), get_int("Enter divisor: ")
    if a is not None and b is not None:
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {a / b}")

def check_prime():
    num = get_int("Enter a positive integer: ")
    if num is None or num <= 0:
        print("Please enter a positive integer.")
        return
    is_prime = all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
    print("Prime" if is_prime else "Composite")

def prime_factors():
    num = get_int("Enter a positive integer: ")
    if num is None or num <= 0:
        print("Please enter a positive integer.")
        return
    factors = [i for i in range(1, num + 1) if num % i == 0]
    print(f"Prime factors of {num}: {factors}")

def square_root_factorization():
    n = get_int("Enter a number under the radical: ")
    if n is None or n <= 0:
        print("Please enter a positive integer.")
        return
    max_square = max(i**2 for i in range(1, math.isqrt(n) + 1) if n % (i**2) == 0)
    root_part = int(math.sqrt(max_square))
    other_part = n // max_square
    print(f"Simplified root: {root_part}√{other_part}")

def solve_equation():
    try:
        x = symbols('x')
        eq = input("Enter an equation (e.g. x**2 - 4): ")
        solutions = sympy_solve(eq, x)
        print("Solutions:", solutions if solutions else "No solutions found.")
    except Exception:
        print("Invalid equation.")

# Conversion Functions

def convert_decimal():
    decimal = get_float("Enter a decimal number: ")
    if decimal is None:
        return
    print(f"Fraction: {Fraction(decimal).limit_denominator()}")
    print(f"Percent: {decimal * 100}%")

def convert_fraction():
    try:
        num, denom = map(int, input("Enter a fraction (num/den): ").split("/"))
        decimal = num / denom
        print(f"Decimal: {decimal}")
        print(f"Percent: {decimal * 100}%")
    except Exception:
        print("Invalid fraction format or zero denominator.")

def convert_percent():
    percent = get_float("Enter percent value: ")
    if percent is None:
        return
    decimal = percent / 100
    print(f"Decimal: {decimal}")
    print(f"Fraction: {Fraction(decimal).limit_denominator()}")

# Menu and Program Flow

def main_menu():
    menu = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "5": ("Check Prime", check_prime),
        "6": ("Prime Factors", prime_factors),
        "7": ("Simplify Square Root", square_root_factorization),
        "8": ("Solve Equation", solve_equation),
        "9": ("Decimal to Fraction/Percent", convert_decimal),
        "10": ("Fraction to Decimal/Percent", convert_fraction),
        "11": ("Percent to Decimal/Fraction", convert_percent),
        "12": ("Exit", None)
    }

    print("\n=== Calculator Menu ===")
    for key, (label, _) in menu.items():
        print(f"{key}. {label}")

    choice = input("\nEnter your choice (1–12): ").strip()
    if choice in menu:
        if choice == "12":
            sys.exit("Goodbye!")
        else:
            menu[choice][1]()
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        main_menu()
        cont = input("\nContinue? (Y/N): ").strip().upper()
        if cont == "N":
            sys.exit("Goodbye!")

if __name__ == "__main__":
    main()

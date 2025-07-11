import math
from sympy import symbols, solve, sqrt
from fractions import Fraction
import sys

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            perform_operation(add)
        elif choice == '2':
            perform_operation(subtract)
        elif choice == '3':
            perform_operation(multiply)
        elif choice == '4':
            perform_operation(divide)
        elif choice == '5':
            perform_operation(check_prime)
        elif choice == '6':
            perform_operation(prime_factors)
        elif choice == '7':
            perform_operation(factor_square_root)
        elif choice == '8':
            perform_operation(solve_equation)
        elif choice == '9':
            perform_operation(decimal_to_other)
        elif choice == '10':
            perform_operation(fraction_to_other)
        elif choice == '11':
            perform_operation(percent_to_other)
        elif choice == '12':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-12).")

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_positive_integer(prompt):
    while True:
        num = get_integer_input(prompt)
        if num > 0:
            return num
        print("Please enter a positive integer.")

def add():
    a = get_integer_input("Enter first integer: ")
    b = get_integer_input("Enter second integer: ")
    print(f"{a} + {b} = {a + b}")

def subtract():
    a = get_integer_input("Enter first integer: ")
    b = get_integer_input("Enter second integer: ")
    print(f"{a} - {b} = {a - b}")

def multiply():
    a = get_integer_input("Enter first integer: ")
    b = get_integer_input("Enter second integer: ")
    print(f"{a} * {b} = {a * b}")

def divide():
    a = get_integer_input("Enter dividend: ")
    b = get_integer_input("Enter divisor: ")
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {a / b}")

def check_prime():
    number = get_positive_integer("Enter a positive integer: ")
    if number == 1:
        print("1 is neither prime nor composite.")
        return
    is_prime = all(number % i != 0 for i in range(2, int(math.isqrt(number)) + 1))
    print(f"{number} is prime." if is_prime else f"{number} is composite.")

def prime_factors():
    number = get_positive_integer("Enter a positive integer: ")
    factors = []
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    print(f"Prime factors: {factors}")

def factor_square_root():
    n = get_positive_integer("Enter number to factor its square root: ")
    max_square = max(i**2 for i in range(1, int(math.isqrt(n)) + 1) if n % (i**2) == 0)
    other = n // max_square
    root = int(math.sqrt(max_square))
    print(f"√{n} = {root}√{other}")

def solve_equation():
    x = symbols('x')
    eq = input("Enter equation to solve for x (0 = ...): ")
    try:
        solutions = solve(eq, x)
        if solutions:
            print(f"Solutions: x = {', '.join(map(str, solutions))}")
        else:
            print("No solutions found.")
    except:
        print("Invalid equation format.")

def decimal_to_other():
    while True:
        try:
            decimal = float(input("Enter a decimal number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid decimal.")
    fraction = Fraction(decimal).limit_denominator()
    percent = decimal * 100
    print(f"Decimal: {decimal}")
    print(f"Fraction: {fraction}")
    print(f"Percent: {percent}%")

def fraction_to_other():
    while True:
        try:
            fraction = input("Enter a fraction (numerator/denominator): ").strip()
            numerator, denominator = map(int, fraction.split('/'))
            if denominator == 0:
                print("Denominator cannot be zero.")
                continue
            break
        except (ValueError, TypeError):
            print("Invalid format. Use numerator/denominator.")
    decimal = numerator / denominator
    percent = decimal * 100
    print(f"Decimal: {decimal}")
    print(f"Percent: {percent}%")

def percent_to_other():
    while True:
        try:
            percent = float(input("Enter a percent: ").strip('%'))
            break
        except ValueError:
            print("Invalid input. Please enter a valid percent.")
    decimal = percent / 100
    fraction = Fraction(decimal).limit_denominator()
    print(f"Decimal: {decimal}")
    print(f"Fraction: {fraction}")

def perform_operation(operation):
    operation()
    if not continue_calculations():
        sys.exit("Goodbye")

def continue_calculations():
    response = input("Continue calculations? (Y/N): ").strip().upper()
    return response != "N"

def main_menu():
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Check Prime Number")
    print("6. Find Prime Factors")
    print("7. Factor Square Root")
    print("8. Solve Equation for x")
    print("9. Convert Decimal to Fraction/Percent")
    print("10. Convert Fraction to Decimal/Percent")
    print("11. Convert Percent to Decimal/Fraction")
    print("12. Exit")

if __name__ == '__main__':
    main()

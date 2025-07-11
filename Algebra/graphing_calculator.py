import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, linsolve, simplify

def get_valid_input(prompt, validation_func=None):
    while True:
        user_input = input(prompt).strip()
        if validation_func is None or validation_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_valid_expression(expr, symbols):
    try:
        sympy_expr = simplify(expr)
        allowed_symbols = {str(s) for s in symbols}
        return all(str(s) in allowed_symbols for s in sympy_expr.free_symbols)
    except:
        return False

def display_graph_and_table():
    x = symbols('x')
    equation = get_valid_input("Enter the equation in terms of 'x': y = ", 
                              lambda e: is_valid_expression(e, [x]))
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.array([simplify(equation).subs(x, val) for val in x_vals], dtype=float)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of y = {equation}')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.axis('off')
    rows = [[x_val, simplify(equation).subs(x, x_val)] for x_val in range(-5, 6)]
    plt.table(cellText=rows, colLabels=['x', 'y'], cellLoc='center', loc='center')
    plt.title("Values Table")
    
    plt.tight_layout()
    plt.show()

def solve_system_of_equations():
    x, y = symbols('x y')
    print("Use Python syntax with x and y as variables (e.g., 2*x + 3*y - 6)")
    first = get_valid_input("Enter the first equation: 0 = ", 
                           lambda e: is_valid_expression(e, [x, y]))
    second = get_valid_input("Enter the second equation: 0 = ", 
                            lambda e: is_valid_expression(e, [x, y]))
    
    try:
        solution = linsolve([first, second], (x, y))
        if not solution:
            print("No solution exists.")
        else:
            x_sol, y_sol = solution.args[0]
            print(f"Solution: x = {x_sol}, y = {y_sol}")
    except Exception as e:
        print(f"Error solving system: {e}")

def graph_and_find_intersection():
    m1, b1 = map(float, get_valid_input(
        "Enter m and b for first equation (y=mx+b), separated by comma: ",
        lambda s: len(s.split(',')) == 2 and all(is_number(p) for p in s.split(','))
    ).split(','))
    
    m2, b2 = map(float, get_valid_input(
        "Enter m and b for second equation (y=mx+b), separated by comma: ",
        lambda s: len(s.split(',')) == 2 and all(is_number(p) for p in s.split(','))
    ).split(','))
    
    x, y = symbols('x y')
    try:
        solution = linsolve([m1*x + b1 - y, m2*x + b2 - y], (x, y))
        x_sol, y_sol = map(float, solution.args[0])
    except:
        print("Lines are parallel or coincident.")
        return
    
    xmin, xmax = int(x_sol)-10, int(x_sol)+10
    ymin, ymax = int(y_sol)-10, int(y_sol)+10
    x_vals = np.linspace(xmin, xmax, 200)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, m1*x_vals + b1, label=f'y = {m1}x + {b1}')
    plt.plot(x_vals, m2*x_vals + b2, label=f'y = {m2}x + {b2}')
    plt.plot(x_sol, y_sol, 'ro', label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')
    
    plt.axhline(y=0, color='k', alpha=0.5)
    plt.axvline(x=0, color='k', alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersection of Two Lines')
    plt.grid(True)
    plt.legend()
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()

def plot_quadratic_roots_and_vertex():
    a = float(get_valid_input("Enter coefficient 'a': ", is_number))
    b = float(get_valid_input("Enter coefficient 'b': ", is_number))
    c = float(get_valid_input("Enter coefficient 'c': ", is_number))
    
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a * x_vals**2 + b * x_vals + c
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'y = {a}x² + {b}x + {c}')
    
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        plt.scatter([root1, root2], [0, 0], color='red', s=50, label=f'Roots: {root1:.2f}, {root2:.2f}')
    elif discriminant == 0:
        root = -b / (2*a)
        plt.scatter([root], [0], color='red', s=50, label=f'Root: {root:.2f}')
    
    vertex_x = -b / (2*a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.scatter([vertex_x], [vertex_y], color='blue', s=50, label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')
    
    plt.axhline(y=0, color='k', alpha=0.5)
    plt.axvline(x=0, color='k', alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Equation')
    plt.grid(True)
    plt.legend()
    plt.axis([-10, 10, -10, 10])
    plt.show()

def main():
    while True:
        print("\nMenu:")
        print("1. Display graph and table of values")
        print("2. Solve system of two equations")
        print("3. Graph two equations and intersection")
        print("4. Plot quadratic roots and vertex")
        print("5. Exit")
        
        choice = get_valid_input("Enter your choice: ", lambda c: c in {'1', '2', '3', '4', '5'})
        
        if choice == '1':
            display_graph_and_table()
        elif choice == '2':
            solve_system_of_equations()
        elif choice == '3':
            graph_and_find_intersection()
        elif choice == '4':
            plot_quadratic_roots_and_vertex()
        else:
            break

if __name__ == '__main__':
    main()

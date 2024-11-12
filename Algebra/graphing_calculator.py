import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, linsolve, sqrt

def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        options = {
            '1': display_graph_and_table,
            '2': solve_system_of_equations,
            '3': graph_and_find_intersection,
            '4': plot_quadratic_roots_and_vertex,
            '5': exit_program
        }

        operation = options.get(choice)
        if operation:
            operation()
        else:
            print("Invalid choice. Please try again.")

def display_main_menu():
    """Display the main menu options."""
    print("\nMenu:")
    print("1. Display the graph and table of values for an equation")
    print("2. Solve a system of two equations without graphing")
    print("3. Graph two equations and plot the point of intersection")
    print("4. Plot the roots and vertex of a quadratic equation")
    print("5. Exit")

def display_graph_and_table():
    """Display graph and table of values for a user-input equation."""
    equation = input("Enter the equation in terms of 'x' (e.g., 'x**2 + 2*x - 3'): y = ")
    x_values = np.linspace(-10, 10, 400)
    try:
        y_values = eval(equation)
        plot_graph(x_values, y_values, equation)
        display_table(x_values, y_values)
    except (NameError, SyntaxError):
        print("Invalid equation. Please enter a valid equation in terms of 'x'.")

def plot_graph(x_values, y_values, equation):
    """Plot a graph for the provided x and y values."""
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of y = {equation}')
    plt.grid(True)
    plt.show()

def display_table(x_values, y_values):
    """Display a table of values for the equation."""
    print("\n x       y")
    print("-----------------")
    for x, y in zip(x_values[::40], y_values[::40]):
        print(f"{x:.2f}   {y:.2f}")

def solve_system_of_equations():
    """Solve a system of two equations without graphing."""
    x, y = symbols('x y')
    eq1 = input("Enter the first equation in terms of x and y (e.g., 'x + y - 3'): ")
    eq2 = input("Enter the second equation in terms of x and y (e.g., '2*x - y - 1'): ")
    try:
        solution = linsolve([eq1, eq2], (x, y))
        if solution:
            x_solution, y_solution = solution.args[0]
            print(f"x = {x_solution}, y = {y_solution}")
        else:
            print("No solutions found.")
    except Exception:
        print("Invalid input. Make sure the equations are in terms of x and y.")

def graph_and_find_intersection():
    """Graph two linear equations and plot their intersection point."""
    m1, b1 = get_slope_intercept("first")
    m2, b2 = get_slope_intercept("second")

    # Solve for the intersection
    x, y = symbols('x y')
    solution = linsolve([m1 * x + b1 - y, m2 * x + b2 - y], (x, y))
    if solution:
        x_intersect, y_intersect = map(float, solution.args[0])
        print(f"Intersection at: ({x_intersect:.2f}, {y_intersect:.2f})")
        plot_lines_with_intersection(m1, b1, m2, b2, x_intersect, y_intersect)
    else:
        print("The lines are parallel and do not intersect.")

def get_slope_intercept(label):
    """Prompt the user to enter the slope and intercept."""
    while True:
        try:
            m, b = map(float, input(f"Enter the slope and intercept for the {label} line, separated by a comma (e.g., '2, 3'): ").split(","))
            return m, b
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")

def plot_lines_with_intersection(m1, b1, m2, b2, x_intersect, y_intersect):
    """Plot two lines and their intersection point."""
    x_vals = np.linspace(x_intersect - 10, x_intersect + 10, 200)
    y1_vals = m1 * x_vals + b1
    y2_vals = m2 * x_vals + b2
    
    plt.plot(x_vals, y1_vals, label=f"y = {m1}x + {b1}")
    plt.plot(x_vals, y2_vals, label=f"y = {m2}x + {b2}")
    plt.plot(x_intersect, y_intersect, 'ro', label=f"Intersection ({x_intersect:.2f}, {y_intersect:.2f})")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersection of Two Lines')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_quadratic_roots_and_vertex():
    """Plot the roots and vertex of a quadratic equation."""
    a, b, c = get_quadratic_coefficients()
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a * x_vals**2 + b * x_vals + c

    # Plot the quadratic equation
    plt.plot(x_vals, y_vals, label=f"y = {a}x^2 + {b}x + {c}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Equation')
    plt.grid(True)

    # Calculate roots
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        plt.scatter([root1, root2], [0, 0], color='green', label=f"Roots: x1={root1:.2f}, x2={root2:.2f}")

    # Calculate the vertex
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.scatter(vertex_x, vertex_y, color='blue', label=f"Vertex ({vertex_x:.2f}, {vertex_y:.2f})")

    plt.legend()
    plt.show()

def get_quadratic_coefficients():
    """Prompt the user to enter coefficients for a quadratic equation."""
    while True:
        try:
            a = float(input("Enter coefficient 'a': "))
            b = float(input("Enter coefficient 'b': "))
            c = float(input("Enter coefficient 'c': "))
            return a, b, c
        except ValueError:
            print("Invalid input. Please enter numeric coefficients.")

def exit_program():
    """Exit the program."""
    exit()

if __name__ == '__main__':
    main()

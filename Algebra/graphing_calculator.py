import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def main():
    while True:
        print("\nMenu:")
        print("1. Display the graph and table of values for an equation")
        print("2. Solve a system of two equations without graphing")
        print("3. Graph two equations and plot the point of intersection")
        print("4. Plot the roots and vertex of a quadratic equation")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_graph_and_table()
        elif choice == '2':
            solve_system_of_equations()
        elif choice == '3':
            graph_and_find_intersection()
        elif choice == '4':
            plot_quadratic_roots_and_vertex()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def display_graph_and_table():
    equation = input("Enter the equation in terms of 'x': y = ")
    x = np.linspace(-10, 10, 400)  # Adjust the range as needed
    y = eval(equation)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of {equation}')
    plt.grid(True)
    plt.show()
    display_table(equation)

def display_table(equation):
    ax = plt.subplot()
    ax.set_axis_off()
    title = f"y = {equation}"
    cols = ('x', 'y')
    rows = [[0, 0]]
    for x in range(1, 10):
        rows.append([x, eval(equation)])

    ax.set_title(title)
    plt.table(cellText=rows, colLabels=cols, cellLoc='center', loc='upper left')
    plt.show()

def solve_system_of_equations():
    x, y = symbols('x y')
    print("Remember to use Python syntax with x and y as variables")
    print("Notice how each equation is already set equal to zero")
    first = input("Enter the first equation: 0 = ")
    second = input("Enter the second equation: 0 = ")
    solution = linsolve([first, second], (x, y))
    x_solution = solution.args[0][0]
    y_solution = solution.args[0][1]

    print("x = ", x_solution)
    print("y = ", y_solution)

def graph_and_find_intersection():
    print("First equation: y = mx + b")
    mb_1 = input("Enter m and b, separated by a comma: ")
    mb_in1 = mb_1.split(",")
    m1 = float(mb_in1[0])
    b1 = float(mb_in1[1])

    print("Second equation: y = mx + b")
    mb_2 = input("Enter m and b, separated by a comma: ")
    mb_in2 = mb_2.split(",")
    m2 = float(mb_in2[0])
    b2 = float(mb_in2[1])

    # Solve the system of equations
    x, y = symbols('x y')
    first = m1 * x + b1 - y
    second = m2 * x + b2 - y
    solution = linsolve([first, second], (x, y))
    x_solution = round(float(solution.args[0][0]), 3)
    y_solution = round(float(solution.args[0][1]), 3)

    # Make sure the window includes the solution
    xmin = int(x_solution) - 20
    xmax = int(x_solution) + 20
    ymin = int(y_solution) - 20
    ymax = int(y_solution) + 20
    points = 2 * (xmax - xmin)

    # Define the x values once for the graph
    graph_x = np.linspace(xmin, xmax, points)

    # Define the y values for the graph
    y1 = m1 * graph_x + b1
    y2 = m2 * graph_x + b2

    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])  # window size
    plt.plot([xmin, xmax], [0, 0], 'b')  # blue x-axis
    plt.plot([0, 0], [ymin, ymax], 'b')  # blue y-axis

    # line 1
    plt.plot(graph_x, y1)

    # line 2
    plt.plot(graph_x, y2)

    # point
    plt.plot([x_solution], [y_solution], 'ro')

    plt.show()
    print(" ")
    print("Solution: (", x_solution, ",", y_solution, ")")

def plot_quadratic_roots_and_vertex():
    print("y = ax² + bx + c")
    a = float(input("Enter the coefficient 'a' of the quadratic equation: "))
    b = float(input("Enter the coefficient 'b' of the quadratic equation: "))
    c = float(input("Enter the coefficient 'c' of the quadratic equation: "))
    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10
    points = 2 * (xmax - xmin)
    x = np.linspace(xmin, xmax, points)
    y = a * x**2 + b * x + c
    plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Equation')
    plt.grid(True)

    # Calculate the roots using the quadratic formula
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        plt.scatter([root1, root2], [0, 0], color='green', label=f'Roots: x1={root1}, x2={root2}')
    elif discriminant == 0:
        root = -b / (2 * a)
        plt.scatter(root, 0, color='green', label=f'Root: x={root}')

    # Calculate the vertex
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.scatter(vertex_x, vertex_y, color='blue', label=f'Vertex ({vertex_x}, {vertex_y})')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()

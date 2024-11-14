import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def get_user_equation():
    """Prompts the user to input an equation for y in terms of x."""
    while True:
        eq = input("Enter the equation for y in terms of x: ")
        try:
            x = sp.symbols('x')
            y_expr = sp.sympify(eq)
            y_func = sp.lambdify(x, y_expr, 'numpy')
            return y_func, eq
        except (sp.SympifyError, TypeError):
            print("Invalid equation. Please enter a valid mathematical expression.")

def plot_graph(y_func, equation_str):
    """Plots the graph of the equation y = y_func(x)."""
    # Set the graph limits and generate x values
    xmin, xmax = -100, 100
    ymin, ymax = -100, 100
    x = np.linspace(xmin, xmax, 500)

    # Calculate y values safely, handling any runtime issues
    try:
        y = y_func(x)
    except Exception as e:
        print(f"Error evaluating the equation over the range: {e}")
        return

    # Initialize plot
    fig, ax = plt.subplots()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.plot([xmin, xmax], [0, 0], "b")  # x-axis
    ax.plot([0, 0], [ymin, ymax], "b")  # y-axis

    # Plot settings
    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    ax.set_title(f"Graph of y = {equation_str}")
    ax.grid(True)
    ax.set_xticks(np.arange(xmin, xmax + 1, 20))
    ax.set_yticks(np.arange(ymin, ymax + 1, 20))

    # Plot the equation
    ax.plot(x, y, label=f"y = {equation_str}", color='red')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    y_function, equation_text = get_user_equation()
    plot_graph(y_function, equation_text)

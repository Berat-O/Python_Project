import matplotlib.pyplot as plt

def get_point_input(point_label):
    """Get the (x, y) coordinates of a point from user input."""
    while True:
        try:
            x = int(input(f"Please type the x value for {point_label}: "))
            y = int(input(f"Please type the y value for {point_label}: "))
            return x, y
        except ValueError:
            print("Invalid input. Please enter integer values.")

def calculate_line_equation(x1, y1, x2, y2):
    """Calculate the slope (m) and intercept (b) of the line passing through points (x1, y1) and (x2, y2)."""
    if x1 == x2:
        raise ValueError("The points have the same x-coordinate; the line is vertical, and slope is undefined.")
    
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def plot_line_and_points(x1, y1, x2, y2, m, b):
    """Plot the line y = mx + b along with the points (x1, y1) and (x2, y2) on a graph."""
    # Define the x range based on the input points, with some padding
    x_min = min(x1, x2) - 5
    x_max = max(x1, x2) + 5
    y_min = min(y1, y2, m * x_min + b, m * x_max + b) - 5
    y_max = max(y1, y2, m * x_min + b, m * x_max + b) + 5

    # Define the y values of the line at the x_min and x_max boundaries
    y_start = m * x_min + b
    y_end = m * x_max + b

    # Set up the plot
    plt.figure(figsize=(8, 6))
    plt.plot([x_min, x_max], [y_start, y_end], 'r', label=f'y = {m:.2f}x + {b:.2f}')
    plt.scatter([x1, x2], [y1, y2], color='green', marker='o', label=f'Points ({x1}, {y1}), ({x2}, {y2})')
    
    # Add axis lines and labels
    plt.axhline(0, color='blue', linewidth=0.5)  # x-axis
    plt.axvline(0, color='blue', linewidth=0.5)  # y-axis
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # Title, legend, and grid
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of the Linear Equation')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Let's find the equation of the line passing through two points and plot it.")
    try:
        x1, y1 = get_point_input("point 1")
        x2, y2 = get_point_input("point 2")
        m, b = calculate_line_equation(x1, y1, x2, y2)
        plot_line_and_points(x1, y1, x2, y2, m, b)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

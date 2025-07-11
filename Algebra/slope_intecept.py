import matplotlib.pyplot as plt

def get_coordinate(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_line_parameters(x1, y1, x2, y2):
    if x1 == x2:
        return None, x1  # Vertical line x = x1
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def plot_line_and_points(x1, y1, x2, y2, m, b):
    xmin, xmax = -10, 10
    ymin, ymax = -10, 10

    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], 'b')
    plt.plot([0, 0], [ymin, ymax], 'b')

    if m is None:
        equation = f'x = {b}'
        plt.axvline(x=b, color='r', label=equation)
    else:
        equation = f'y = {m}x + {b}'
        y3 = m * xmin + b
        y4 = m * xmax + b
        plt.plot([xmin, xmax], [y3, y4], 'r', label=equation)

    plt.scatter([x1, x2], [y1, y2], color='green', marker='o', 
                label=f'Points ({x1}, {y1}), ({x2}, {y2})')
    plt.legend()
    plt.show()

x1 = get_coordinate("Please enter x1 value: ")
y1 = get_coordinate("Please enter y1 value: ")
x2 = get_coordinate("Please enter x2 value: ")
y2 = get_coordinate("Please enter y2 value: ")

m, b = calculate_line_parameters(x1, y1, x2, y2)
plot_line_and_points(x1, y1, x2, y2, m, b)

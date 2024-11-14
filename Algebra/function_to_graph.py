import matplotlib.pyplot as plt
import numpy as np


xmin = -100
xmax = 100
ymin = -100
ymax = 100
points = xmax - xmin
x = np.linspace(xmin, xmax, points)


while True:
    eq = input("Enter the equation for y in terms of x: ")

    # Use eval() to evaluate the user's input as a mathematical expression
    try:
        y = eval(eq)  # Evaluate the expression with x as a variable
        break
    except:
        print("Invalid input equation.")


fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], "b")
plt.plot([0, 0], [ymin, ymax], "b")

ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("Equation Graph")
ax.grid(True)

ax.set_xticks(np.arange(xmin, xmax, 20))
ax.set_yticks(np.arange(ymin, ymax, 20))


plt.plot(x, y, label=f"y= {eq}")

plt.legend()
plt.show()

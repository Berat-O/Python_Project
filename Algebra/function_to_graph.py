import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, symbols
from sympy.utilities.lambdify import lambdify
from sympy.core.sympify import SympifyError


xmin = -100
xmax = 100
ymin = -100
ymax = 100
points = xmax - xmin
x = np.linspace(xmin, xmax, points)


while True:
    eq = input("Enter the equation for y in terms of x: ")

    try:
        # Parse the expression safely using sympy and convert to a numpy-callable function
        x_sym = symbols('x')
        expr = sympify(eq)
        func = lambdify(x_sym, expr, modules=['numpy'])
        y = func(x)
        break
    except (SympifyError, TypeError, NameError, ValueError) as e:
        print(f"Invalid input equation: {e}")


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

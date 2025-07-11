import matplotlib.pyplot as plt
import numpy as np

def get_valid_expression(prompt: str) -> str:
    while True:
        expr = input(prompt).strip()
        if is_safe_expression(expr):
            return expr
        print("Invalid or unsafe expression. Please try again.")

def is_safe_expression(expr: str) -> bool:
    allowed_names = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                     'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
                     'pi': np.pi, 'e': np.e}
    code = compile(expr, '<string>', 'eval')
    for name in code.co_names:
        if name not in allowed_names:
            return False
    return True

def main():
    xmin, xmax = -100, 100
    ymin, ymax = -100, 100
    points = 1000
    
    x = np.linspace(xmin, xmax, points)
    
    eq = get_valid_expression("Enter the equation for y in terms of x: ")
    
    allowed_names = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                     'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
                     'pi': np.pi, 'e': np.e, 'x': x}
    try:
        y = eval(eq, {"__builtins__": None}, allowed_names)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return
    
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.axis([xmin, xmax, ymin, ymax])
    
    plt.axhline(y=0, color='blue', linestyle='-', alpha=0.5)
    plt.axvline(x=0, color='blue', linestyle='-', alpha=0.5)
    
    ax.set_xlabel("x values", fontsize=12)
    ax.set_ylabel("y values", fontsize=12)
    ax.set_title("Equation Graph", fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    ax.set_xticks(np.arange(xmin, xmax+1, 20))
    ax.set_yticks(np.arange(ymin, ymax+1, 20))
    
    plt.plot(x, y, label=f"y = {eq}", linewidth=2)
    
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

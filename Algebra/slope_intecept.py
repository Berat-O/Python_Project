import matplotlib.pyplot as plt

x1 = int(input("Please type x1 value :"))
y1 = int(input("Please type y1 value :"))
x2 = int(input("Please type x2 value :"))
y2 = int(input("Please type y2 value :"))

# Develop the equation y = mx + b
if x1==x2:
    print("This is a vertical line")
    print(f"The equation is x = {x1}")
else:
    m = (y2 - y1) / (x2 - x1)

    b = y1 - m*x1
    if b>=0:
        equation = f'y = {m}x + {b}'
    else:
        equation=f'y = {m}x - {-1*b}'

# For the graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10


# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
if x1==x2:
    plt.plot([x1, x1], [ymin, ymax], '-r', label=equation)
else:    
    # Plot the linear function as a red line
    y3 = m*xmin + b 
    y4 = m*xmax + b 
    plt.plot([xmin,xmax],[y3,y4],'r',label=equation)
plt.scatter([x1, x2], [y1, y2], color='green', marker='o', label=f'Points ({x1}, {y1}), ({x2}, {y2})')


plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
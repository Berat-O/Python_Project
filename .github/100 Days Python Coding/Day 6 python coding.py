# Defining & calling function
def my_function():
  print("Hello, welcome to my world")
  print("See you soon")
my_function()
# Exercise 1: Reeborg's World
def turn_right():
  turn_left()
  turn_left()
  turn_left()
#draw square
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
#Exercise 2
def turn_right:
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
def jump_hurdle():
    move()
    jump()
    turn_left()
#Hurdle race
for step in range(6):
    jump_hurdle()

#While loop
def turn_right:
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#exercise: jumping over hurdles with variable heights
def turn_right:
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move

#exercise: project
def turn_right:
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move
    else:
        turn_left()

  #All code was run on Reeborg's World website
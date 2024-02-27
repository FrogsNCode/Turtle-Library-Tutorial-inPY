import turtle

##################################
# Initial Setup and Basic Movement
##################################

# Initial setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Python Turtle Guide")
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.speed(1)  # Set turtle speed

# Basic movement
t.forward(100)  # Move forward by 100 pixels
t.left(90)      # Turn left by 90 degrees
t.forward(100)

#########################
# Drawing Simple Shapes
#########################

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw a circle
t.circle(50)

# Draw a triangle
for _ in range(3):
    t.forward(100)
    t.left(120)

#################################################
# Using Loops and Functions for Complex Drawings
#################################################

# Draw a hexagon
def draw_hexagon():
    for _ in range(6):
        t.forward(100)
        t.left(60)

draw_hexagon()


# Draw a spiral
def draw_spiral():
    length = 5
    for _ in range(60):
        t.forward(length)
        t.right(90)
        length += 5

draw_spiral()

import turtle

# Initial setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Python Turtle Guide")
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.speed(20)  # Set turtle speed

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

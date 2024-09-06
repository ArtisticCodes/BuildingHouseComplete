import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a House")
screen.bgcolor("lightblue")

# Create a turtle named "builder"
builder = turtle.Turtle()
builder.speed(2)

# Function to draw a square
def draw_square(size,is_window=False):
    if is_window:
        builder.begin_fill()
        builder.color("red")
        for _ in range(4):
            builder.forward(size)
            builder.right(90)
        builder.end_fill()
    else:
        builder.begin_fill()
        builder.color("darkgreen")
        for _ in range(4):
            builder.forward(size)
            builder.right(90)
        builder.end_fill()

# Function to draw a triangle (for the roof)
def draw_triangle(size):
    builder.begin_fill()
    builder.color("yellow")
    for _ in range(3):
        builder.forward(size)
        builder.left(120)
    builder.end_fill()

# Function to draw a door
def draw_door():
    builder.begin_fill()
    builder.color("brown")
    builder.forward(50)
    builder.right(90)
    builder.forward(80)
    builder.right(90)
    builder.forward(50)
    builder.end_fill()

# Function to draw a window
def draw_window():
    
    draw_square(30,True)
   

# Draw the house
builder.penup()
builder.goto(-100, -100)  # Position for the house base
builder.pendown()
builder.color("black")

draw_square(200)  # Draw the base of the house

draw_triangle(200)  # Draw the roof

builder.penup()
builder.goto(-25, -220)  # Position for the door
builder.pendown()
draw_door()  # Draw the door

builder.penup()
builder.goto(-40, -150)  # Position for the window
builder.pendown()
draw_window()  # Draw a window

builder.penup()
builder.goto(60, -150)  # Position for the other window
builder.pendown()
draw_window()  # Draw another window

# Hide the turtle and finish
builder.hideturtle()
screen.mainloop()

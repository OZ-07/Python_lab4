import turtle
import random

""""put your functions here"""
def draw_circle(t,radius):
    """draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t,sides, length):
    """draws a regular polygon with a given number of sides and side length."""
    angle = 360/sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def jump(x, y):
    """Move forward radius units without leaving a trail.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
def draw_pumpkin(t, x, y, radius):
    "draws a pumpkin (orange circle) at given  (x,y) location with a green stem."
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    jump(x, y+1.9*radius)

    #drawing stem

    t.fillcolor("green")
    t.begin_fill()
    t.left(90) #point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius //5)
    t.end_fill()

def draw_eye(t,x,y,size):
    """draws on triangle eye at the given x, y position."""
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t,3,size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """draws a jagged mouth using a series of connected lines"""
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    # create a simple zigzag mouth
    for _ in range(5):
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_star(t, x, y, size):
    """draws a star at the given x,y position."""
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144) #144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t,num_stars):
    """draws a starry sky with given number of stars"""
    for _ in range(num_stars):
        x = random.randint(-300,300)
        y = random.randint(50,300)
        size = random.randint(10,30)
        draw_star(t,x,y,size)

#create turtle object
t = turtle.Turtle()

# hide the turtle and set speed
t.speed(10) #(1 is slow, 10 is fast, 0 is instant)
t.hideturtle()

#Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
#set the width and height of the screen
screen.setup(width=800, height=600)
#clear the screen
t.clear()
"""put draw calls on functions here"""
draw_pumpkin(t,-150,-200,100)
draw_eye(t,-190,-110,30)# left eye
draw_eye(t,-110,-110,30)#right eye
draw_mouth(t,-190,-150,80) # mouth

draw_pumpkin(t,0,-200,80)
draw_eye(t, -20, -120, 25)
draw_eye(t, 20, -120, 25)
draw_mouth(t, -30, -160, 60)

draw_pumpkin(t, 150, -200, 100)
draw_eye(t,110,-110,30)
draw_eye(t, 190, -110, 30)
draw_mouth(t,110,-150,80)

draw_sky(t,20)

turtle.exitonclick()
# put the pumpkins down the page
#push eyes down the page
# make them below the stars x,y cords
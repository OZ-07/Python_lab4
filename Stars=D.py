import turtle
import random

""""put your functions here"""

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
        y = random.randint(0,300)
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
#draw_star(t,-100,150,30)
#draw_star(t,50,180,20)
draw_sky(t,20)

turtle.exitonclick()

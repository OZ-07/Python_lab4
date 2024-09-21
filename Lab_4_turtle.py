# part 1
import turtle


""""put your functions here"""
# draw square
def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t,radius):
    """draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t,sides, length):
    """draws a regular polygon with a given number of sides and side length."""
    angle = 360/sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

#create turtle object
t = turtle.Turtle()

# hide the turtle and set speed
t.speed(10) #(1 is slow, 10 is fast, 0 is instant)
t.hideturtle()

#Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")
#set the width and height of the screen
screen.setup(width=600, height=600)
#clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTION  HERE"""
# example
#draw_square(t,100)
#draw_circle(t,25)
#draw_polygon(t,5,25) # hexagon

#close the turtle graphics window when clicked
turtle.exitonclick()

#turtle shape and color
#t.color('blue')
#t.shape('turtle')





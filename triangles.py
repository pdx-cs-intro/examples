# Draw a picture using "turtle graphics"
# Bart Massey 2021
from turtle import *

# Draw a fancy figure using the turtle. End with the turtle
# at the same facing and position it started with.
def spiro():
    
    # Draw a triangle using the turtle. End with the turtle
    # at the same facing and position it started with.
    def triangle():
        # Move the turtle forward 100 "units".
        forward(100)
        # Turn the turtle left 120 degrees.
        left(120)
        forward(100)
        left(120)
        forward(100)
        left(120)

    # Draw 36 triangles.
    for _ in range(36):
        # Draw a triangle.
        triangle()
        # Turn the turtle left 10 degrees.
        left(10)

# Make the turtle drag a green pen.
color("green")
# Draw a fancy shape.
spiro()
# Have the turtle pick up the pen.
penup()
# Move the turtle forward 10 units.
forward(10)
# Have the turtle drag the pen again.
pendown()
# Make the turtle drag a red pen.
color("red")
# Draw a fancy shape.
spiro()

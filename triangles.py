# Draw a picture using "turtle graphics"
# Bart Massey 2021
from turtle import *

def spiro():

    def triangle():
        """
        Draw a triangle with the turtle.
        End with original position and facing.
        """
        forward(100)
        left(120)
        forward(100)
        left(120)
        forward(100)
        left(120)

    for _ in range(36):
        triangle()
        left(10)

color("green")
spiro()
forward(10)
color("red")
spiro()

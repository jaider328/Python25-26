import turtle
from myfunctions import *

screen = turtle.Screen()
screen.bgcolor("black")
turtle.colormode(1.0)

bob = turtle.Turtle()
bob.speed(0)
bob.hideturtle()

draw_spiral_flowers(bob, 30)

turtle.done()


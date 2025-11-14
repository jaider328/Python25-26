import turtle
import random

def draw_triangle(turt, size, color1, color2, rotate_angle):  # Drawing a triangle
    """
    Draws a triangle, filling it with color.
    Uses rotate_angle to offset
    """
    turt.fillcolor(color1)
    turt.begin_fill()
    for _ in range(3):
        turt.forward(size)
        turt.left(120)  # Each angle is 60 (180/3), the change of 120 makes this shape a triangle
    turt.end_fill()
    turt.right(rotate_angle) #rotates the turtle for an additional offset

def draw_diamond(turt, size, color1, color2, offset):
  """
    Draws a diamond made of 4 triangles
  """
  draw_triangle(turt, size, color1, color2, 60)
  turt.forward(size)
  draw_triangle(turt, size, color2, color1, 60)
  turt.forward(size)
  draw_triangle(turt, size, color1, color2, 60)
  turt.forward(size)
  draw_triangle(turt, size, color2, color1, 60)
  turt.penup()
  turt.goto(turt.xcor() - offset, turt.ycor() - offset)
  turt.pendown()

def set_up_screen(screen_color):
  """
    Sets up the screen.  Returns the turtle and the screen.
  """
  screen = turtle.Screen()
  screen.bgcolor(screen_color)
  t = turtle.Turtle()
  t.speed(0)  # Fastest speed
  t.hideturtle() # hides the turtle object
  return t, screen

import turtle
from myfunctions import *
import random

# --- Setup ---
screen_height = screen.window_height()
square_size = 30
rows = screen_height // square_size  # integer division to get whole squares
cols = screen_width // square_size
offset = 0 # variable for the offest in the x,y

# --- Colors ---
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

# --- Draw the Pattern ---
for row in range(rows):
    for col in range(cols):
        x = col * square_size - screen_width // 2 + square_size//2  # Centering
        y = row * square_size - screen_height // 2 + square_size//2
        t.penup()
        t.goto(x, y)
        t.pendown()
        color1 = random.choice(colors)
        color2 = random.choice(colors)
        mf.draw_diamond(t, square_size, color1, color2, offset)
        offset += 2 # add a small offset
screen.mainloop()  # Keep the window open        

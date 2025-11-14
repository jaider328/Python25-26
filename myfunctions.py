import turtle
import random

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def draw_petal(t, radius):
    t.fillcolor(random_color())
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, 60)
        t.left(120)
    t.end_fill()

def draw_flower(t, petals, radius):
    for _ in range(petals):
        draw_petal(t, radius)
        t.right(360 / petals)

def draw_spiral_flowers(t, n):
    for i in range(n):
        draw_flower(t, 6, 40)
        t.right(20)
        t.forward(i * 3)


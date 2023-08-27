from turtle import *
from math import *
from random import *
def get(n, i):
    return factorial(n) // (factorial(i) * factorial(n - i))
def bezier(control_points, t):
    n = len(control_points) - 1
    x, y = 0, 0
    for i in range(n + 1):
        coefficient = get(n, i) * ((1 - t) ** (n - i)) * (t ** i)
        x += coefficient * control_points[i][0]
        y += coefficient * control_points[i][1]
    return x, y

def draw_bezier(control_points):
    num_points=100
    colormode(255)
    penup()
    for point in control_points:
        goto(point)
    pendown()
    step = 1 / num_points
    for i in range(num_points + 1):
        t = i * step
        x, y = bezier(control_points, t)
        pencolor((randint(0,255),randint(0,255),randint(0,255)))
        goto(x, y)
pensize(2)
speed(0)
for i in range(8):
    control_points = [(randint(0,300),0)]
    for i in range(2):
        control_points.append((randint(200,300),randint(0,300)))
    control_points.append((randint(200,300),0))
    print(control_points)
    draw_bezier(control_points)
    
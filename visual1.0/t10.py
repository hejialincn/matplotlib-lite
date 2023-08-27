import turtle
from random import *

def bubble(x, y, size):
    turtle.penup()
    turtle.goto(x, y - size)
    turtle.pendown()
    turtle.circle(size)

def main():
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.hideturtle() 
    data = []
    for i in range(10):
        data.append((randint(0,300),randint(0,300),randint(0,20)))   
        
    for x, y, size in data:
        color = (random(), random(), random())
        turtle.fillcolor(color)
        turtle.begin_fill()
        bubble(x, y, size)
        turtle.end_fill()

turtle.goto(400,0)
turtle.penup()
turtle.goto(0,400)
turtle.pendown()
turtle.goto(0,0)
main()
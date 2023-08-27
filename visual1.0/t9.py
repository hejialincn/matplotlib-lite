import turtle
import random

# 随机生成一些散点数据
def generate_random_points(num_points):
    points = []
    for _ in range(num_points):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        points.append((x, y))
    return points

# 绘制散点图
def draw_scatter_plot(points):
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    for point in points:
        x, y = point
        t.goto(x, y)
        t.dot(5)

    t.hideturtle()
    screen.mainloop()
turtle.speed(0)
num_points = 1000
points = generate_random_points(num_points)
draw_scatter_plot(points)
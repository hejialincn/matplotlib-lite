from turtle import *
from random import *

colors = ["green","blue","red","brown","orange","purple","pink","cyan","black","magenta","gold"]

def drawpart(radius, percentage, color,name):
    pencolor("tomato") 
    fillcolor(color)
    begin_fill()
    forward(radius)
    left(90)
    circle(radius, percentage * 360/2)
    at=pos()
    print(at)
    penup()
    if at[1]<0 :
        goto(at[0],at[1]+50)
    if at[1]>0:
        goto(at[0],at[1]-50)
    pendown()
    print(name+str(pos()))
    write(str(round(percentage * 360))+"。",align="right",font=("宋体",10,"normal"))
    penup()
    goto(at[0],at[1])
    pendown()
    write(name,align="right",font=("宋体",15,"normal"))
    circle(radius, percentage * 360/2)
    left(90)
    forward(radius//2)
    forward(radius//2)
    end_fill()
    left(180)
def pie(radius, data, colors,name):
    total = sum(data)
    angle = 0
    for i in range(len(data)):
        percentage = data[i] / total
        drawpart(radius, percentage, colors[i],name[i])
        angle += percentage * 360
        setheading(angle)
    hideturtle()
    done()

data=[]
name2=[]
name= input("请输入饼图名称:")
for i in range(3):
    name1= input("请输入饼图{}的名称：".format(i+1))
    percent= eval(input("请输入饼图{}的百分比：".format(i+1)))
    data.append(percent)
    name2.append(name1)
penup()
goto(0,170)
pendown()
write(name,align="center",font=("宋体",20,"normal"))
speed(0)
penup()
goto(0, 0)
pendown()
color=[]
for i in range(3):
    c=choice(colors)
    color.append(c)
print(color)
pie(150, data,color,name2)

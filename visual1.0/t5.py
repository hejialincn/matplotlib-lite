from turtle import *
from random import *

def axis(data,name,cos,title,color):
    pencolor(color)
    long=len(data)*20
    height=max(data)+20
    penup()
    goto((long*cos)//2+-(long*cos//2),height*cos)
    goto(-(long*cos//2),0)
    pendown()
    forward(long*cos)
    penup()
    goto(-(long*cos//2),0)
    pendown()
    rt(-90)
    forward(height*cos)
    penup()
    goto(-(long*cos//2),0)
    pendown()
    rt(90)
    new=zip(data,name)
    counter=0
    pendown()
    for i in new:
        goto(-(long*cos//2)+counter*cos,i[0]*cos)
        dot(5)
        write(str(i[0]))
        counter=counter+20
colormode(255)
speed(0)   
pensize(2)
data=[]
name=[]
k=0
cos=2.5
title="1234"
for i in range(100):
    for i in range(5):
        data.append(randint(1,100))
    for i in range(5):
        name.append(str(randint(1,100)))
    if k==0:
        long=len(data)*20
        height=max(data)+20
        penup()
        goto((long*cos)//2+-(long*cos//2),height*cos)
        write(title,align="right",font=("宋体",15,"normal"))
        goto(-(long*cos//2),0)
        pendown()
        k=1
    axis(data,name,cos,title,(randint(0,255),randint(0,255),randint(0,255)))
    data=[]
    name=[]

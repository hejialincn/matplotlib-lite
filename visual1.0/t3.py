from turtle import *
from random import *

def axis(data,name,cos,title):
    long=len(data)*20
    height=max(data)+20
    penup()
    goto((long*cos)//2+-(long*cos//2),height*cos)
    write(title,align="right",font=("宋体",15,"normal"))
    new=zip(data,name)
    counter=0
    penup()
    one=list(new)[0]
    goto(-(long*cos//2),one[0]*cos)
    new=zip(data,name)
    for i in new:
        pendown()
        goto(-(long*cos//2)+counter*cos,i[0]*cos)
        dot(5)
        write(str(i[0]))
        counter=counter+20
    
pensize(2)
data=[]
for i in range(10):
    data.append(randint(-100,100))
name=["1","2","3","4","5","6","7","8","9","10"]
axis(data,name,1,"1234")


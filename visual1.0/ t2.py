from turtle import *

def axis(data,name,cos,title):
    long=len(data)*20
    height=max(data)+20
    penup()
    goto((long*cos)//2+-(long*cos//2),height*cos)
    write(title,align="right",font=("宋体",15,"normal"))
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
    for i in new:
        penup()
        goto(-(long*cos//2)+counter*cos,-20)
        pendown()
        write(i[1])
        counter=counter+20
    new=zip(data,name)
    counter=0
    penup()
    goto(0,0)
    pendown()
    for i in new:
        goto(-(long*cos//2)+counter*cos,i[0]*cos)
        dot(5)
        write(str(i[0]))
        counter=counter+20
    
pensize(2)
data=[1,10,3,4,5,6,100,200,6,300,15,200]
name=["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
axis(data,name,1,"1234")

from turtle import *
from math import *
penup()
goto(-100,-100)
pendown()
goto(400,300)
speed(1)
start=(-100,-100)
end=(400,300)
pencolor("orange")
y=abs(end[1]-start[1])
x=abs(end[0]-start[0])
get=x/y
print(get)
if end[1]<0 :
    goto(end[0]-get*300,end[1]+300)
if end[1]>0 :
    goto(end[0]-get*300,end[1]-300)
else:
    print("111")
done()
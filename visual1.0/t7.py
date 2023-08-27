from turtle import *

data=[(-10,1),(10,100),(1,2),(2,3)]
new=[]
ls=[]
def one(data):
    dt={}
    for i  in range(len(data)-1):
        if i+2<=len(data)-1:
            new.append(data[i][0])
            new.append(data[i+1][0])
            new.append(data[i+2][0])
            if new[0] is not max(new):
                dt[(i+1,i+2)]="True"
                dt[(i+2,i+3)]="True"
            else:
                dt[(i+1,i+2)]="false"
                dt[(i+2,i+3)]="false"
    return(dt)
def get(i,l):
    speed(1)
    list1=[]
    start=i
    penup()
    goto(start)
    pendown()
    goto(l)
    end=l
    tuple1=end
    pencolor("orange")
    print(start,end)
    print(int((abs(int(start[0])+1)/abs(int(start[1])+1))))
    print(int((abs(int(end[0])+1)/abs(int(end[1])+1))))
    y=abs(end[1]-start[1])
    x=abs(end[0]-start[0])
    get=x/y
    print(get)
    if end[1]<0 :
        goto(end[0]-get*10,end[1]+10)
    if end[1]>0 :
        goto(end[0]+get*10,end[1]+10)   
list1=get((10,100),(-10,1))    

import math
import turtle
import time


#Stairway2 is a better version
def stairway1(x, y):
    t1 = turtle.Turtle()
    turtle.delay(0.5)
    sides = 11
    coord_list = []
    coord_list.append(t1.pos())
    for i in range(sides - 1):
        t1.forward(15)
        coord_list.append(t1.pos())
        t1.left(360 / sides)
    time.sleep(1)
    print(coord_list)
    i = 0
    n = 100

    while (i < n):
        l = 0.1 + (i / 10)
        for j in range(sides):
            # t1.right(t1.towards(coord_list[j]))
            del_x = -t1.pos()[0] + coord_list[j][0]
            del_y = -t1.pos()[1] + coord_list[j][1]
            den = math.sqrt(del_x ** 2 + del_y ** 2)
            del_x = del_x / den
            del_y = del_y / den
            t1.goto(coord_list[j])
            t1.goto(coord_list[j][0] + del_x * l, coord_list[j][1] + del_y * l)
            coord_list[j] = t1.pos()
        # time.sleep(1)
        i += 1


def stairway2(x, y):
    #Settable parameters
    no_of_sides=7
    side_length=300
    start_x=-200
    start_y=-250
    #If you want animation, set animate to True and set animation_speed(0=Fastest)
    animate=False
    animation_speed=0
    #If the image is not very clean with automatic_decay=True, make automatic decay=False and set decay value
    #Good decay values>0.98
    automatic_decay=False
    decay=0.995

    myWin = turtle.Screen()
    t1 = turtle.Turtle("circle")
    t1.shapesize(0.1, 0.1, 0)
    if(not animate):
        myWin.tracer(False)
    else:
        turtle.delay(animation_speed)
    # turtle.delay(0)
    sides = no_of_sides
    #decay=0.7
    coord_list = []
    st_x = start_x
    st_y = start_y
    s_len=side_length
    t1.penup()
    t1.goto(st_x, st_y)
    t1.pendown()
    d_in = 10
    for i in range(sides):
        t1.forward(d_in)
        coord_list.append(tuple(t1.pos()))
        t1.forward(s_len-d_in)
        t1.left(360/sides)

    coord_list.append(coord_list[0])

    while(True):
        new_side_length=math.sqrt((coord_list[0][0]-coord_list[1][0])**2+(coord_list[0][1]-coord_list[1][1])**2)

        if(automatic_decay):
            new_d_length=d_in*(new_side_length/s_len)
        else:
            new_d_length=d_in*decay
            d_in=new_d_length

        if (new_side_length < 0.1 or new_d_length<0.01):
            break
        t1.goto(coord_list[0])
        for i in range(sides):
            del_x=coord_list[i+1][0]-coord_list[i][0]
            del_y=coord_list[i+1][1]-coord_list[i][1]
            t1.goto(t1.pos()[0]+(del_x*new_d_length)/new_side_length,t1.pos()[1]+(del_y*new_d_length)/new_side_length)
            coord_list[i]=t1.pos()
            t1.goto(coord_list[i+1])

        coord_list[-1]=coord_list[0]

    if (not animate):
        myWin.update()



turtle.onscreenclick(stairway2)
turtle.mainloop()






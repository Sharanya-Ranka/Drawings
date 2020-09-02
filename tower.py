import math
import turtle
import time


def make_tower(x,y):
    #Settable parameters
    background_color="yellow"
    pen_color="blue"
    breadth_size=400
    lb_ratio=1  #Length-breadth ratio
    step_size=10
    animation_speed=0 #Lower value=faster 0 is near-instantaneous


    turtle.bgcolor(background_color)
    turtle.color(pen_color,pen_color)
    turtle.shape("circle")
    turtle.shapesize(0.2,0.2,0)
    start=breadth_size
    mult=lb_ratio
    step=step_size
    turtle.delay(animation_speed)
    turtle.penup()
    turtle.setpos(0,start)
    turtle.pendown()
    turtle.setpos(0,-1*start)
    turtle.penup()
    turtle.setpos(-1*mult*start,0)
    turtle.pendown()
    turtle.setpos(mult*start,0)
    i=1

    while (i*step<=start):
        turtle.pendown()
        turtle.setpos(mult*(start+step*(1-i)),0)
        turtle.setpos(0,-1*i*step)
        turtle.setpos(-1*mult*(start+step*(1-i)),0)
        turtle.setpos(0,i*step)
        turtle.setpos(mult*(start+step*(1-i)),0)
        turtle.penup()
        i+=1
    turtle.goto(0,0)
    turtle.exitonclick()


#make_tower(0,0)
sc=turtle.Screen()
#sc.setup(800,800)
turtle.onscreenclick(make_tower)
turtle.mainloop()
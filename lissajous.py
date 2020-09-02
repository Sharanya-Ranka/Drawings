import math
import time
import turtle

def Lissajous(x, y):
    #Settable parameters
    pen_color="black"
    length=200
    breadth=100
    #Ratio is the frequency ratio of the sin to the cosine component(eg. 2,4,17,249,2.33 etc)
    ratio=3.62
    #Phases of the sine and cosine values respectively
    s_phase=0
    c_phase=0

    speed=0.0005
    # Updates screen after these many iterations. May lead to speed changes high value-Higher speed, low value- Lower speed
    update_after_iterations=1000
    max_updates=100

    #print("In lissajous")
    sc = turtle.Screen()
    t = turtle.Turtle("circle")
    t.color(pen_color,pen_color)
    t.shapesize(0.1, 0.1, 0)
    sc.tracer(False)
    x_scale = length
    y_scale = breadth
    time = 0
    time_inc = speed
    show_time = 1
    time_ratio = update_after_iterations
    #ratio = 3.43
    x = x_scale * math.sin(ratio * time + s_phase)
    y = y_scale * math.cos(time+c_phase)
    t.penup()
    t.goto(x, y)
    t.pendown()
    # t.goto(100,100)
    i = 0
    while (max_updates):
        # print("In while")
        time += time_inc
        x = x_scale * math.sin(ratio * time + s_phase)
        y = y_scale * math.cos(time+c_phase)
        t.goto(x, y)
        i += 1
        # sc.update()
        if i % time_ratio == 0:
            # print("Updating")
            max_updates-=1
            sc.update()


turtle.onscreenclick(Lissajous)
turtle.mainloop()
import math
import time
import turtle
import random

class complex():
    def __init__(self,real=0.0,imag=0.0):
        self.real=real
        self.imag=imag

    def __add__(self,other):
        return complex(self.real+other.real,self.imag+other.imag)

    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        c=complex(0,0)
        c.real=(self.real*other.real)-(self.imag*other.imag)
        c.imag=(self.real*other.imag)+(self.imag*other.real)

        return c

    def mod(c):
        return math.sqrt(c.real**2+c.imag**2)

    def mod2(c):
        return (c.real**2+c.imag**2)

    def convert_from_polar(magnitude,angle):
        c=complex()
        c.real=magnitude*math.cos(angle)
        c.imag=magnitude*math.sin(angle)
        return(c)

    def __truediv__(self, other):
        #Uses c*c_bar=mod(c)^2

        mod_o_sq=complex.mod(other)**2
        other_inv=complex(other.real/mod_o_sq,-other.imag/mod_o_sq)

        return(self*other_inv)







def stability_mandelbrot(c,acc=100):
    num=complex()
    i = 0
    esc = acc
    while (i < esc):
        i += 1
        num=(num*num)+c
        if (complex.mod2(num)>4):
            break

    if (i == esc):
        return (1)
    else:
        return (0)

def stability_julia(c,julia_constant,acc=100):
    i = 0
    esc = acc
    while (i < esc):
        i += 1
        c=(c*c)+julia_constant
        if (complex.mod2(c)>4):
            break

    if (i == esc):
        return (1)
    else:
        return (0)


def mandelbrot(x, y):
    #Settable parameters
    jump=2 #No. of pixels to jump. Will increase speed, but decrease "density"
    scale=0.0025 #Scale of the image(small no. ->larger diagram)
    accuracy=100 #Increase accuracy at the cost of computation time(no max value)

    myWin = turtle.Screen()
    # myWin.clear()
    # t2=turtle.Turtle()
    t1 = turtle.Pen()
    t1.clear()
    t1.shapesize(0.1, 0.1, 0)
    myWin.tracer(False)
    t1.penup()
    jx = jump
    jy = jump
    # c=[0.7885*math.cos(random.random()*2*math.pi),0.7885*math.sin(random.random()*2*math.pi)]
    x_range = range(-700, 700, jx)
    y_range = range(-700, 700, jy)
    for i in x_range:
        for j in y_range:
            if stability_mandelbrot(complex(i*scale,j*scale)) == 1:
                t1.goto(i, j)
                t1.dot(2)
        if (i % 100 == 0):
            print("done", i)

    myWin.update()


def quadratic_julia(x, y):
    # Settable parameters
    jump = 2  # No. of pixels to jump. Will increase speed, but decrease "density"
    scale = 0.0025  # Scale of the image(small no. ->larger diagram)
    #If you want to enter a specific constant, set random_value to False, and set c_real and c_imag(inary)
    random_value=True
    c_real=0
    c_imag=0

    accuracy = 100  # Increase accuracy at the cost of computation time(no max value)

    pi=3.14159265
    if(random_value):
        julia_constant = complex.convert_from_polar(0.7885,random.random()*2*pi)
    else:
        julia_constant=complex(c_real,c_imag)
    myWin = turtle.Screen()
    # myWin.clear()
    # t2=turtle.Turtle()
    t1 = turtle.Pen()
    t1.clear()
    t1.shapesize(0.1, 0.1, 0)
    myWin.tracer(False)
    t1.penup()
    jx = jump
    jy = jump

    x_range = range(-700, 700, jx)
    y_range = range(-700, 700, jy)
    for i in x_range:
        for j in y_range:
            if stability_julia(complex(i * scale, j * scale),julia_constant) == 1:
                t1.goto(i, j)
                t1.dot(2)
        if (i % 100 == 0):
            print("done", i)

    myWin.update()


turtle.onscreenclick(quadratic_julia)
turtle.mainloop()

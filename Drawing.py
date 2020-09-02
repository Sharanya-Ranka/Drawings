import turtle
import math
import time
import random


#turtle.onscreenclick(hello())


def make_tower(x,y):
	turtle.bgcolor("yellow")
	turtle.color('blue','blue')
	turtle.shape("circle")
	turtle.shapesize(0.2,0.2,0)
	start_time=time.time()
	start=400
	mult=1
	step=25
	turtle.delay(0.1)
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
	turtle.exitonclick()


def Lissajous(x,y):
        print("In lissajous")
        sc=turtle.Screen()
        t=turtle.Turtle("circle")
        t.shapesize(0.1,0.1,0)
        sc.tracer(False)
        x_scale=200
        y_scale=100
        time=0
        time_inc=0.05
        show_time=5
        time_ratio=show_time//time_inc
        ratio=0.248
        x=x_scale*math.sin(ratio*time)
        y=y_scale*math.cos(time)
        t.penup()
        t.goto(x,y)
        t.pendown()
        #t.goto(100,100)
        i=0
        while(True):
                #print("In while")
                time+=time_inc
                x=x_scale*math.sin(ratio*time)
                y=y_scale*math.cos(time)
                t.goto(x,y)
                i+=1
                #sc.update()
                if i%time_ratio==0:
                        
                        #print("Updating")
                        sc.update()





def spirographv1(x,y):
        #R/r should be a fraction like 10/3 for good patterns.If you want pointy ends, w2 should be R/r (10/3 in this case)
        #If you want end loops, w2 should be greater than previously mentioned value. If you do not want loops, w2 should be less than that value
        #To increase the speed of the drawing, increase w1 and w2 in same ratio
        turtle.delay(5)
        t1=turtle.Turtle("circle")
        t2=turtle.Turtle("circle")
        t1.shapesize(0.2,0.2,0)
        t2.shapesize(0.2,0.2,0)
        R=[316.67,198.26153,107.15370]
        r=[53.33,64.73846,26.3762]
        w1=[1,1,1]
        w2=[6.8714/2,3.0628*2/2,(4.0625*3+3)/2]
        cl=["green","blue","black"]
        tl=[50.26544*2,50.26544*2,31.45]
        t=[]
        for i in range(3):
                t.append(turtle.Turtle("circle"))
                t[i].shapesize(0.2,0.2,0)
                t[i].color(cl[i])
                t[i].penup()
                t[i].setpos(R[i],r[i]) if i>0 else t[i].setpos(R[i]+r[i],0)
                t[i].pendown()
        start=time.time()
        el=0
        while(el<max(tl)):
                el=time.time()-start
                for i in range(3):
                        if(i>0) and el<tl[i]:
                                t[i].setpos(R[i]*math.cos(w1[i]*el)+r[i]*math.sin(w2[i]*el),R[i]*math.sin(w1[i]*el)+r[i]*math.cos(w2[i]*el))
                        elif i<=0 and el<tl[i]:
                                t[i].setpos(R[i]*math.cos(w1[i]*el)+r[i]*math.cos(w2[i]*el),R[i]*math.sin(w1[i]*el)+r[i]*math.sin(w2[i]*el))
        
                                

def spirographv2(x,y):
        turtle.delay(5)
        hypo=turtle.Turtle("circle")
        epi=turtle.Turtle("circle")
        hypo.shapesize(0.2,0.2,0)
        epi.shapesize(0.2,0.2,0)
        R=100
        r=10
        w=10
        a=10
        start=time.time()
        el=0
        epi.penup()
        hypo.penup()
        
        epi.setpos(R-r+a*r,0)
        hypo.setpos(R+r-a*r,0)
        
        epi.pendown()
        hypo.pendown()
        while(True):
                el=time.time()-start
                el=w*el
                #hypo.setpos((R-r)*math.cos((r/R*el))+a*r*math.cos((1-(r/R))*el),(R-r)*math.sin((r/R*el))-a*r*math.sin((1-(r/R))*el))
                epi.setpos((R+r)*math.cos((r/R*el))-a*r*math.cos((1+(r/R))*el),(R+r)*math.sin((r/R*el))-a*r*math.sin((1+(r/R))*el))


def stairway1(x,y):
        
        t1=turtle.Turtle()
        turtle.delay(0.5)
        sides=11
        coord_list=[]
        coord_list.append(t1.pos())
        for i in range(sides-1):
                t1.forward(15)
                coord_list.append(t1.pos())
                t1.left(360/sides)
        time.sleep(1)
        print(coord_list)
        i=0
        n=100
        
        while(i<n):
                l=0.1+(i/10)
                for j in range(sides):
                        #t1.right(t1.towards(coord_list[j]))
                        del_x=-t1.pos()[0]+coord_list[j][0]
                        del_y=-t1.pos()[1]+coord_list[j][1]
                        den=math.sqrt(del_x**2+del_y**2)
                        del_x=del_x/den
                        del_y=del_y/den
                        t1.goto(coord_list[j])
                        t1.goto(coord_list[j][0]+del_x*l,coord_list[j][1]+del_y*l)
                        coord_list[j]=t1.pos()
                #time.sleep(1)
                i+=1


def stairway2(x,y):
        myWin=turtle.Screen()
        t1=turtle.Turtle("circle")
        t1.shapesize(0.1,0.1,0)
        myWin.tracer(False)
        #turtle.delay(0)
        sides=4
        coord_list=[]
        st_x=-200
        st_y=-250
        t1.penup()
        t1.goto(st_x,st_y)
        t1.pendown()
        start=t1.pos()
        #coord_list.append(t1.pos())
        d_in=20
        for i in range(sides):
                t1.forward(d_in)
                if i==0:
                        start=(t1.pos())
                coord_list.append(t1.pos())##(t1.pos()[0]+st_x,t1.pos()[0]+st_y)
                t1.forward(250-d_in)
                t1.left(360/sides)
        coord_list.append(start)
        i=0
        while(True):
                d=d_in-i/50
                if d==0:
                        break
                t1.setpos(coord_list[0][0],coord_list[0][1])
                #time.sleep(1)
                for j in range(sides):
                        del_x=coord_list[j+1][0]-coord_list[j][0]
                        del_y=coord_list[j+1][1]-coord_list[j][1]
                        den=math.sqrt(del_x**2+del_y**2)
                        del_x=del_x/den
                        del_y=del_y/den
                        dis=t1.distance(coord_list[j+1])
                        
                        t1.setpos(coord_list[j][0]+del_x*d,coord_list[j][1]+del_y*d)
                        coord_list[j]=t1.pos()
                        if j==0:
                                start=t1.pos()
                        t1.setpos(coord_list[j][0]+del_x*(dis-d),coord_list[j][1]+del_y*(dis-d))
                        #time.sleep(1)
                        if j==sides-1:
                                coord_list[j+1]=start 
                
                i+=1
                
        #time.sleep(1)
        print(coord_list)
        i=0
        n=100
        

def stability(c,s):
##        if c[0]>1 or c[1]<1:
##                return(1)
##        else:
##                return(0)
        sx=s[0]
        sy=s[1]
        cx=c[0]*sx
        cy=c[1]*sy
        
        num=[0,0]
        t=[0,0]
        i=0
        esc=200
        while(i<esc):
                i+=1
                nx=num[0]
                ny=num[1]
                num[0]=(nx*nx-ny*ny)+cx
                num[1]=(2*nx*ny)+cy
                if((num[0]**2+num[1]**2)>4):
                       break
        if(i==esc):
                return(1)
        else:
                return(0)
                
def mandelbrot(x,y):
        myWin=turtle.Screen()
        #myWin.clear()
        #t2=turtle.Turtle()
        t1=turtle.Pen()
        t1.clear()
        t1.shapesize(0.1,0.1,0)
        myWin.tracer(False)
        t1.penup()
        jx=2  #jump
        jy=2
        scale=0.0025
        #c=[0.7885*math.cos(random.random()*2*math.pi),0.7885*math.sin(random.random()*2*math.pi)]
        x_range=range(-700,700,jx)
        y_range=range(-700,700,jy)
        for i in x_range:
                for j in y_range:
                        if stability([i,j],[scale,scale])==1:
##                                if(j>0):
##                                        print(i,j)
                                t1.goto(i,j)
                                t1.dot(2)
                if(i%100==0):
                        print("done",i)

        myWin.update()
##        t2.goto(0,0)
##        t2.goto(0,200)
##        t2.goto(100,100)

def rotatingsquare(x,y):
        myWin=turtle.Screen()
        #myWin.clear()
        #t2=turtle.Turtle()
        t1=turtle.Pen()
        t1.clear()
        t1.shapesize(0.1,0.1,0)
        myWin.tracer(False)
        t1.penup()
        t1.goto(x,y)
        side=100
        i=0
        while(True):
                t1.clear()
                t1.penup()
                t1.goto(x,y)
                t1.forward(side/1.4142)
                t1.left(135)
                t1.pendown()
                for _ in range(4):
                        t1.forward(side)
                        t1.left(90)
##                        time.sleep(0.5)
##                        myWin.update()
                t1.right(135)
                time.sleep(0.005)
                myWin.update()
                t1.left(1)
                i+=1

rotator_win=turtle.Screen()
rotator_turtle=turtle.Turtle()
rotator_turtle.shapesize(0.1,0.1,0)
turtle.delay(0)
rotator_win.tracer(False)
def draw_rotatingcube(points):
        global rotator_win,rotator_turtle
        t=rotator_turtle
        t.clear()
        t.penup()
        t.goto(points[3])
        t.pendown()
        t.goto(points[0])
        t.goto(points[1])
        t.goto(points[2])
        t.goto(points[3])
        t.goto(points[7])
        t.goto(points[6])
        t.goto(points[2])
        t.goto(points[1])
        t.goto(points[5])
        t.goto(points[4])
        t.goto(points[0])
        t.goto(points[3])
        t.goto(points[7])
        t.goto(points[4])
        t.goto(points[5])
        t.goto(points[6])
        rotator_win.update()
        
        time.sleep(0)
        
        
                        
                        
        
def rotatingcube(x,y):
        side=100
        s=side
        speed=0.001
        r2=1.414
        points=[[s/r2,-s/2,0],[0,-s/2,-s/r2],[-s/r2,-s/2,0],[0,-s/2,s/r2],
                [s/r2,s/2,0],[0,s/2,-s/r2],[-s/r2,s/2,0],[0,s/2,s/r2]]
        projected_points=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        pictureplanez=200
        print("input observer x y z")
        obs_coord=[200,200,1000] ##list(map(int,input().split()))
        t=0
        while(True):
                t+=speed
                x=s/r2*math.cos(t)              ##Anticlockwise movement
                z=-s/r2*math.sin(t)             ##x z correspond to first point
                for i in [0,4]:
                        points[i][0]=x
                        points[i][2]=z
                        points[i+1][0]=z
                        points[i+1][2]=-x
                        points[i+2][0]=-x
                        points[i+2][2]=-z
                        points[i+3][0]=-z
                        points[i+3][2]=x
                ## To find projected points
                for i,point in enumerate(points):
                        ratio=((pictureplanez-obs_coord[2])/(point[2]-obs_coord[2]))
                        current_point=projected_points[i]
                        current_point[0]=ratio*(point[0]-obs_coord[0])+obs_coord[0]
                        current_point[1]=ratio*(point[1]-obs_coord[1])+obs_coord[1]

                ##To draw projection
                draw_rotatingcube(projected_points)
                        
                
                
        
        
        
	
        
turtle.onscreenclick(make_tower)	


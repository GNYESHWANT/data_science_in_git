from turtle import *
import colorsys as cs
bgcolor("black")
tracer(2)
h=10
pensize(4)
for i in range(200):
    c=cs.hsv_to_rgb(h,1,1)
    h+=0.007
    goto(0,0)
    pencolor(c)
    left(150)
    forward(270-i)
    left(250)
    right(160)
    circle(17,50)
    forward(190)
    right(90)
    forward(i)
    left(100)
done()
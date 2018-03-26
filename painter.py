# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:08:17 2017

@author: warrenl0134
"""
import turtle, random
wn = turtle.Screen()
t = turtle.Turtle()
colors = ['red', 'blue', 'green', 'gold', 'white', 'purple', 'coral', 'crimson', 'black']
size = 10
def triangle(painter, size):
    painter.speed(0)
    if size > 20000:
        return 0
    #painter.fillcolor(random.choice(colors))
    #painter.begin_fill()
    for i in range(3):
        painter.pensize(1)
        painter.fd(size)
        painter.lt(120)
        painter.left(120)
    #painter.end_fill()
    triangle(t,size + 10)
    
triangle(t, size)
wn.exitonclick()
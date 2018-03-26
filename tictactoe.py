# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:32:06 2017

@author: warrenl0134
"""

import turtle


wn = turtle.Screen()
painter = turtle.Turtle()
painter.pensize(4)
painter.speed(5)

painter.color('black')
locations = ['center', 'midright', 'midleft', 'lowleft', 'lowmid', 'lowright', 'topleft', 'topmid', 'topright']
X_used_locations = []
O_used_locations = []
#center = painter.goto(-50,-40)   
#midleft = painter.goto(-150,-40)
#midright = painter.goto(50,-40)
#topleft = painter.goto(-150,60)
#topmid = painter.goto(-50,60)
#topright = painter.goto(50,60)
#lowleft = painter.goto(-150,-140)
#lowmid = painter.goto(-50,-140)
#lowright = painter.goto(50,-140)

def board():
    painter.pu()
    painter.goto(-100, -150)
    painter.pd()
    painter.lt(90)
    painter.fd(300)
    painter.pu()
    painter.goto(0, 150)
    painter.pd()
    painter.rt(180)
    painter.fd(300)
    painter.pu()
    painter.goto(-200, -50)
    painter.pd()
    painter.lt(90)
    painter.fd(300)
    painter.pu()
    painter.goto(-200, 50)
    painter.pd()
    painter.fd(300)
    painter.pu()
    
def drawO(place):
    if place not in locations or place in O_used_locations or place in X_used_locations:
        return False
    O_used_locations.append(place)
    painter.rt(135)
    painter.pu()
    moveTo(place)
    painter.pd()
    painter.circle(40)
    painter.pu()
    painter.lt(135)
    return True

def drawX(place):
    if place not in locations or place in O_used_locations or place in X_used_locations:
        return False
    X_used_locations.append(place)
    painter.rt(45)
    painter.pu()
    moveTo(place)
    painter.pd()
    painter.setheading(0)
    painter.rt(45)
    painter.fd(100)
    painter.lt(135)
    painter.pu()
    painter.fd(70.7)
    painter.lt(135)
    painter.pd()
    painter.fd(100)
    painter.pu()
    painter.lt(135)
    return True

def moveTo(location):
    if location == 'center':
        painter.goto(-85,35)
    if location == 'midleft':
        painter.goto(-195,35)
    if location == 'midright':
        painter.goto(20,35)
    if location == 'topleft':
        painter.goto(-195,150)
    if location == 'topmid':
        painter.goto(-85,150)
    if location == 'topright':
        painter.goto(20,150)
    if location == 'lowleft':
        painter.goto(-195,-70)
    if location == 'lowmid':
        painter.goto(-85,-70)
    if location == 'lowright':
        painter.goto(20,-70)

def wincombo(lst):
    if 'topleft' in lst and 'topmid' in lst and 'topright' in lst:
        return True
    if 'topleft' in lst and 'center' in lst and 'lowright' in lst:
        return True
    if 'topleft' in lst and 'midleft' in lst and 'lowleft' in lst:
        return True
    if 'topmid' in lst and 'center' in lst and 'lowmid' in lst:
        return True
    if 'topright' in lst and 'center' in lst and 'lowleft' in lst:
        return True
    if 'topright' in lst and 'midright' in lst and 'lowright' in lst:
        return True
    if 'midleft' in lst and 'center' in lst and 'midright' in lst:
        return True
    if 'lowleft' in lst and 'lowmid' in lst and 'lowright' in lst:
        return True
    return False
    
board()
iteration = 0
while True:
    place = input("enter a location for the piece: ")
    if iteration % 2 == 0:
        if drawX(place) == True:
            iteration += 1
    else:
        if drawO(place) == True:
            iteration += 1
    if wincombo(X_used_locations):
        print("X won!")
        break
    if wincombo(O_used_locations):
        print("O won!")
        break
    
    
    

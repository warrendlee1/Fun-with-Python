# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:15:45 2018

@author: warrenl0134
"""

#derivative calc

#prompts user for values in the equation
print("all equations are in ax^2 + bx + c form")
power1 = int(input("enter a power factor: "))
a = int(input("enter the a value: "))
b = int(input("enter the b value: "))
c = int(input("enter the c value: "))
print("%sx^2 + %sx  + %s" % (a,b,c))

da = a*2
db = b
dc = 0
print("%sx + %s  + %s" % (da,db,dc))



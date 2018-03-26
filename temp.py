# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def temperature():
    C = int(input("enter a temmperature in Celsius: "))
    F = ((9/5) * C + 32)
    return F
#print(str(temperature()) + " degrees Fahrenheit")
#the comma can print different pieces such as float and str
print(temperature(), " degrees Fahrenheit")
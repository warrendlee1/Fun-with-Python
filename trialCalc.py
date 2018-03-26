# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:43:43 2017

@author: warrenl0134
"""
while True:
    print("POSSIBLE AMERICAN FUNCTIONS: +, -, %, /, and *")#shows user what valid inputs are
    value1 = float(input("enter a number: "))#requests user to input values for calc
    while True:
        calc = str(input("enter an operation: "))#requests for operation input
        if calc not in ["+", "-", "%", "/", "*"]:
            print("invalid function.")
        else:
            break
    value2 = float(input("enter a number: "))#requests user to input values for calc
    if calc == "+":
        result = value1 + value2
    elif calc == "-":
        result = value1 - value2
    elif calc == "%":
        result = value1 % value2
    elif calc == "/":
        result = value1 / value2
    elif calc == "*":
        result = value1 * value2
    print("%g %s %g = %g" % (value1, calc, value2, result))#%g removes any trailing numbers
    quit = str(input("Do you want to quit? "))
    if quit in ["yes","Yes", "Y", "y"]:
       break
    else:
       continue
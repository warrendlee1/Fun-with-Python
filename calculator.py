# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:34:49 2017

@author: warrenl0134
"""
print("POSSIBLE POlISH FUNCTIONS: +, -, %, /, and *")#shows user what valid inputs are
value1 = float(input("enter a number: "))#requests user to input values for calc
value2 = float(input("enter a number: "))#requests user to input values for calc
while True:
    calc = str(input("enter an operation: "))#requests for operation input
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
    else:
        print("invalid function.")
        continue #iterates through the loop again if an invalid function is inputed
    print("%g %s %g = %g" % (value1, calc, value2, result))#%g removes any trailing numbers
    break #breaks out of the loop if a valid input is given
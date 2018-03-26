# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:07:57 2017

@author: warrenl0134
"""
#Return true if the given non-negative number is a multiple of 3 or a multiple of 5. Use the % "mod" operator 

#or35(3) → true
#or35(10) → true
#or35(8) → false

def number(a):
    if a%3 == 0 or a%5 == 0:
        return True
    else:
        return False
print(number(4))
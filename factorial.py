# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:29:04 2017

@author: warrenl0134
"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))
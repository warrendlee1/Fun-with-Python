# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:45:33 2017

@author: warrenl0134
"""

def num8(number):
    if number == 0:
        return 0
    if number % 10 == 8:
        return 1 + num8(number //10)
    return num8(number//10)
print(num8(880))
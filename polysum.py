# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:39:36 2017

@author: warrenl0134
"""
import math
def polysum(n,s):
    perimeter_sqr = (n * s) ** 2
    area = 0.25*n*(s**2)/(math.tan(math.pi/n))
    return (round(perimeter_sqr + area, 4))
print(polysum(52,39))
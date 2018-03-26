# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:13:15 2017

@author: warrenl0134
"""
def max1020(a,b):
    if (a or b) >= 10 and (a or b) <= 20:
        if a > b:
            return a
        else:
            return b
    else:
        return 0
print(max1020(10,20))

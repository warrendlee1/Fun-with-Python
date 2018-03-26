# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:55:44 2017

@author: warrenl0134
"""
def number(a,b,neg):
    return (neg and a < 0 and b < 0) or (not neg and (a < 0 and b > 0) or (a > 0 and b < 0))
print(number(-8,-10,True))
    
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:11:01 2017

@author: warrenl0134
"""
array =[-3,-5,-9,-12,9,50,0]
def max(array):
    mx = array[0]
    for i in array:
        if i > mx:
            mx = i
    print(mx)
max(array)
        
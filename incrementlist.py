# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:53:16 2018

@author: warrenl0134
"""
def count(array):
    counter = 0 
    while counter > 0:
        counter = 0
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i+1] = array[i]
                array[i] = temp
                counter +=1
array = [5,4,3,2,1]
count(array)
print(array)
    
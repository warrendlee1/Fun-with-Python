# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:19:54 2017

@author: warrenl0134
"""

def odd_Tuple(tup):
    for i in range(len(tup)):
        if i % 2 == 0:
            print(tup[i])
tup = ['I', 'am', 'a', 'Test', 'Tuple']
odd_Tuple(tup)


# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:34:24 2017

@author: warrenl0134
"""

def recursive_power(base, power):
    if power == 0:
        return 1
    return base * recursive_power(base, power - 1)

print (recursive_power(50, 2))
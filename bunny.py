# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:38:37 2017

@author: warrenl0134
"""

def bunny(ears):
    if ears == 0:
        return 0
    else:
        return 2 + bunny(ears - 1)
print(bunny(6))
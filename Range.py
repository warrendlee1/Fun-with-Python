# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:59:33 2017

@author: warrenl0134
"""
def nearHundred(n):
    result = False
    if 90<=n<=110 or 190<=n<=210:
        result = True
    return result
print(nearHundred(201))
    
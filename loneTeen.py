# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:29:24 2017

@author: warrenl0134
"""
def teen(a,b):
    if ((a>=13 and a<=19) and (b<13 or b>19)) or ((b>=13 and b<=19) and (a<13 or a>19)):
        return True
    else:
        return False
print(teen(13,19))
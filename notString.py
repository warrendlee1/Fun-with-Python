# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:50:37 2017

@author: warrenl0134
"""
def notString(string):
    #check to see if 'not' is in the beginning of the string
    #if 'not' is at the beginning of the string, print string
    #else print 'not' + string
    if string[:3] == "not ":
        print(string)
    else:
        print("not " + string)
notString("liked")
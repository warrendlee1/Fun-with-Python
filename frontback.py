# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:33:39 2017

@author: warrenl0134
"""
def front_back(string):
    if len(string) > 1:
        return(string[-1] + string[1:-1] + string[0])#its -1 because we do not count the value that it is on
    return(string)
print(front_back("a"))
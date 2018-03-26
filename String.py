# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:09:19 2017

@author: warrenl0134
"""
def missing_char(string, n):
    return(string[:n] + string[n+1:])
print(missing_char("kitten",4))
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:36:42 2018

@author: warrenl0134
"""
import string
def adjf(shift):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    combined = {}
    for i in lower:
        combined[i] = (shift)
    for i in upper:
        combined[i] = (shift)
    for i in combined:
        ascii_char = ord(i)
       # combined[i] = chr(97 + ((ascii_char - 97 + shift) % 26))
    #for i in combined:
        #ascii_char = ord(i) 
        #combined[i] = chr(65 + ((ascii_char - 65 + shift) % 26))
    return combined
print(adjf(0))

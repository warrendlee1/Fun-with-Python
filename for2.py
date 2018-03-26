# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:53:49 2017

@author: warrenl0134
"""

sentence = input("enter a sentence: ")
y = 0
for i in sentence:
    if i == "h":
        y += 1
print(y)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 01:47:57 2017

@author: warrenl0134
"""
num_bob = 0
letters = input("enter random letters: ")
for i in range(len(letters)):
    if letters[i:i+3] == 'bob':
        num_bob += 1
print(num_bob)

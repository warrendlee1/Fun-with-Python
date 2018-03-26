# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:44:56 2017

@author: warrenl0134
"""
def is_string(string):
    try:
        str(string)
        return True
    except:
        return False
num_vowels = 0
letters = input("enter random letters: ")
while is_string(letters) == False:  
    letters = input("enter random letters: ")
for i in letters:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        num_vowels += 1
print(num_vowels)

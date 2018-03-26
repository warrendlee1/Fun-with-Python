# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:50:08 2017

@author: warrenl0134
"""
high = 99
low = 0
guess = (high+low)//2
print(guess)
hint = input("is the guess too high (h), too low (l), or correct (c)? ")
while hint != "c":
    if hint == "h":
        high = guess - 1
        guess = (high+low)//2
        print(guess)
        hint = input("is the guess too high (h), too low (l), or correct (c)? ")
    elif hint == "l":
        low = guess + 1
        guess = (high+low)//2
        print(guess)
        hint = input("is the guess too high (h), too low (l), or correct (c)? ")
    else:
        print(guess)
        hint = input("is the guess too high (h), too low (l), or correct (c)? ")
print(str(guess) + " is your number! :)")
        
   
    

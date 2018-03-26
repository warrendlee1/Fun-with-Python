# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:34:42 2017

@author: warrenl0134
"""
# defines a function that ensures that a str input can be a int
def get_num (string):
    try:
        int(string)
        return True
    except:
        return False
# fulfills all the requirements under a false condition
# when the conditions are true, it will exit the loop 
condition = False
while condition == False:
    height = input("enter a height value: ")
    condition = get_num(height) and int(height) > 0 and int(height) < 23
# creates the spacing between all #'s
print("Height = " + str(height))
for i in range(int(height) + 1):
    print(" " * (int(height) - i) + "#" * i + "  " + "#" * i)
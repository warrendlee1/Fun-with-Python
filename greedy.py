# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:26:09 2017

@author: warrenl0134
"""
#we defined a function get_float() that returns true if input can be converted to a type float and returns false if the function isn't able to return a float(string)
def get_float(string):
    try:
        float(string)
        return True
    except:
        return False

#defined a boolean variable called condition, setting it to False 
condition = False
while condition == False: #created a while loop that runs when condition is False
    amount = input("How much change is owed in cents? ") #defined a new var amount that takes a string input
    condition = get_float(amount) and float(amount) > 0 #to exit while loop, both amount needs to be able to be turned into a float, and the float val of amount must be positive
                                                        #when condition is true, it no longer needs to run the while loop. 
#the next line determines max number of quarters needed in the amount. 
q = float(amount) // 25 # the // rounds the quotient of float(amount) and val of quarter (25) down to the nearest whole int and sets it to a var q 
print(str(q) + " quarters") #prints the previous value q
q_leftover = float(amount) % 25 # we take the left over or remainder of float(amount) when it is divided by 25
d = q_leftover // 10 # we repeat the same code with the value of dimes given the initial value of the left over value of quarter
print(str(d) + " dimes") #repeat this step for each coin type until pennies. 
d_leftover = q_leftover % 10
n = d_leftover // 5
print(str(n) + " nickels")
n_leftover = d_leftover % 5
p = n_leftover // 1
print(str(p) + " pennies")


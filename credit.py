# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:40:50 2017

@author: warrenl0134
"""

#Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products' digits together.
#Add the sum to the sum of the digits that weren’t multiplied by 2.
#If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
def is_int(string):
    try:
        int(string)
        return True
    except:
        return False

credit_score = input("enter your credit number: ")
while is_int(credit_score) == False:    
    credit_score = input("enter your credit number: ")
    
array_credit = list(credit_score)
running_sum = 0

for i in range(len(array_credit)):
    if i % 2 == 1: #if odd
        product = int(array_credit[i]) * 2
        for z in str(product): #just in case double digits are appearing
            running_sum = running_sum + int(z)
    else: #if even
        running_sum = running_sum + int(array_credit[i]) #running_sum gets added a even val
if running_sum % 10 == 0:
    print("legit card!")
else:
    print("invalid card!")
            
            
    
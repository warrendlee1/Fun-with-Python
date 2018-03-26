9# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:28:28 2017

@author: warrenl0134
"""
def is_int(string):
    try:
        int(string)
        return True
    except:
        return False

book_check = input("enter your ISBN number: ")
while is_int(book_check) == False and len(book_check) != 10:    
    book_check = input("enter ISBN: ")

array_ISBN = list(book_check)
ISBN_final = 0
for i in range(len(array_ISBN)):
    product = (i+1) * int(array_ISBN[i])
    ISBN_final += product
if ISBN_final % 11 == 0:
    print("valid ISBN")
else:
    print("invalid ISBN")
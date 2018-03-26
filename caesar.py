# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:23:31 2017

@author: warrenl0134
"""
def caesar(message, key):
    '''
    input: message is a string, key is an int
    output: a string where each char has been shifted by the key amount
    special characters will not be changed
    '''
    c_msg = ""
    if key >= 0:#key has to be non-negative
        for i in message:
            ascii_char = ord(i)
            if ascii_char >= 65 and ascii_char <= 90: #if uppercase
                c_char = 65 + ((ascii_char - 65 + key) % 26)
            elif ascii_char >= 97 and ascii_char <= 122: #if lowercase
                c_char = 97 + ((ascii_char - 97 + key) % 26)
            else:# if the char is a special char
                c_char = ascii_char
            c_msg += chr(c_char)
    else: #invalid if key is a negative number
        print("invalid key")
    return c_msg
print(caesar("Or fher gb qevax lbhe Binygvar!", 13))
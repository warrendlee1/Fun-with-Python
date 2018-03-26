# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:41:43 2018

@author: warrenl0134
"""

'''
Applies the Caesar Cipher to self.message_text with the input shift.
Creates a new string that is self.message_text shifted down the
alphabet by some number of characters determined by the input shift        
        
shift (integer): the shift with which to encrypt the message.
0 <= shift < 26

Returns: the message text (string) in which every character is shifted
down the alphabet by the input shift
'''
message = ""
dct = self.build_shift_dict(shift)
text = self.message_text
for i in text:
    message += dct[letter]
return message
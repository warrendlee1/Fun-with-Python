# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:39:05 2017

@author: warrenl0134
"""

#1
words = (["a", "b", "a", "c", "b"]) 
def word0(words):
    dict1 = {}
    for i in words:
        dict1[i] = 0
    return dict1
print(word0(words))

#2
strings = (["code", "code", "code", "bug", "a", "abc"])
def wordLen(strings):
    dict1 = {}
    for i in strings:
        dict1[i] = len(i)
    return dict1
print(wordLen(strings))

#3
x = (["man", "moon", "good", "night"]) 
def pairs(x):
    return {i[0]:i[-1] for i in x}
print(pairs(x))

#4
b = (["a", "b", "a", "c", "b"])
def wordCount(b):
    return {i:len(b.i()) for i in b}
print(wordCount(b))

#5
c = (["aa", "bb", "cc", "aAA", "cCC", "d"])
#def firstChar(c):
    
#6
w = (["a", "b", "a", "c", "a", "d", "a"])
def wordAppend(w):
    result = {}
    for i in w:
        if i == 'a':
            result[i] = "a"
    return result
print(wordAppend(w))
        
        
            
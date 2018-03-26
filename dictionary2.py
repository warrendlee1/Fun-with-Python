# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:13:57 2017

@author: warrenl0134
"""
#1
d = ({"a": "aaa", "b": "bbb", "c": "ccc"})
def dictionaryShare(d):
    if "a" in d:
        d['b'] = d['a']
    del(d['c'])
    return d
print(dictionaryShare(d))

#2
b = ({"a": "candy", "b": "dirt"})
def dictionaryBully(b):
    if "a" in b:
        b["b"] = b["a"]
        b["a"] = ""
    return b
print(dictionaryBully(b))

#3
ab = ({"a": "Hi", "b": "There"})
def dictionaryAB(ab):
    if "a" in ab and "b" in ab:
        ab["ab"] = ab["a"]+ab["b"]
    return ab
print(dictionaryAB(ab))

#4
food = ({"ice cream": "cherry", "spinach": "dirt", "yogurt":"salt"})
def topping(food):
    if len(food["ice cream"]) != 0:
        food["yogurt"] = food["ice cream"]
    if len(food["spinach"]) != 0:
        food["spinach"] = "nuts"
    return food
print(topping(food))

#5
t = ({"potato":"ketchup", "salad": "oil", "spinach": "","fries": ""})
def topping3(t):
    if len(t["potato"]) != 0:
        t["fries"] = t["potato"]
    if len(t["salad"]) != 0:
        t["spinach"] = t["salad"]
    return t
print(topping3(t))

#6
x = ({"a": "aaa", "b": "aaa", "c": "cake"})
def ab(x):
    if "a" in x and "b" in x and x["a"] == x["b"]:
        del(x["a"])
        del(x["b"])
    return x
print(ab(x))
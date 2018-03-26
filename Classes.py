# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:27:28 2018

@author: warrenl0134
"""

class intSet(object):
    def __init__(self):
        #makes list called self.vals to hold set on ints 
        self.vals = []
    def insert(self, e):
        #check to see if e is in in self.vals, if not then it appends e to self.vals
        if e not in self.vals:
            self.vals.append(e)
    def member(self,e):
        #return true if e in self.vals, False otherwise
        return e in self.vals
    def remove(self, e):
        #removes e from self.vals, raises a Vlue Error if e no in self.vals
        try:
            self.vals.remove(e)
        except:
            raise ValueError 
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return "blah blah"

s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
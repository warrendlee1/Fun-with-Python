# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:03:55 2018

@author: warrenl0134
"""

class Polygon(object):
    def __init__(self, numSides):
        self.numSides = numSides
        self.sides = []
    def inputSides(self):
        for i in range(self.numSides):
            x = float(input("enter a float: "))
            self.sides.append(x)
    def dispSides(self):
        for i in range(self.numSides):
            print(float(self.sides[i]))
    def __str__(self):
        for i in range(self.numSides):
            return "Side "+str(i)+" is"+str(self.dispSides)
polygon = Polygon(5)
polygon.inputSides()
polygon.dispSides()
print(polygon.__str__())

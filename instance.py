# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:40:13 2018

@author: warrenl0134
"""

class PartyAnimal:
    x = 0
    
    def _init_(self, x = 0):
        print("I am constructed")
    
    def party(self):
        self.x = self.x + 1
        print('so far ', self.x)
        
me = PartyAnimal
me.party()
me.party()
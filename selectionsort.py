"""
Created on Thu Feb  8 11:31:13 2018

@author: warrenl0134
"""
import random
array = []
n = 10
for i in range(n):
    array.append(random.randint(1,100))
    
for i in range(len(array)):
    minimum = i
    for j in range(i+1, len(array)):
        if array[j] < array[minimum]:
            minimum = j
    if minimum != i:
        array[minimum], array[i] = array[i], array[minimum]
print(array)      
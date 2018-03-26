"""
Created on Wed Feb  7 11:53:16 2018

@author: warrenl0134
"""
array = [4, 18, 101, 78, 1, 54, 22, 300, 9, 41]
for i in range(len(array)):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
print(array)
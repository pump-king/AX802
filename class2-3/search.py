# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:33:53 2020

@author: marco
"""

data = [1,2,3,4,5,6]

def linearSearch(data,value):
    a = 0
    while data[a] != value:
        a += 1
    return True


def binarySearch(data,value):
    lower = 0
    upper = len(data)-1
    while lower <= upper:
        mid = (upper + lower)//2
        midValue = data[mid]
        if midValue < value:
            lower = mid+1
        elif midValue > value:
            upper = mid-1
        else:
            return True
    
print(linearSearch(data,3))
print(binarySearch(data,4))
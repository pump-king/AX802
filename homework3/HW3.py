# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:49:21 2020

@author: marco
"""

data = [1,2,3,4,5,6]

def lS(data,v):
    a = 0
    while data[a] != v:
        a += 1
    return data[a]

def bS(data,v):
    low = 0
    up = len(data)-1
    while low <= up:
        mid = (up + low)//2
        midV = data[mid]
        if midV < v:
            low = mid+1
        elif midV > v:
            up = mid-1
        else:
            return mid

print(lS(data,3))
print(bS(data,5))
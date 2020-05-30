# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:20:40 2020

@author: marco
"""

data = [2,0,5,8,9,3]
def bubbleSort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j+1]<data[j]:
                data[j],data[j+1] = data[j+1],data[j]
                
bubbleSort(data)
print(data)
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:14:26 2020

@author: marco
"""

data = [2,0,5,8,9,3]
def b(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j+1]<data[j]:
                data[j],data[j+1] = data[j+1],data[j]
                
b(data)
print(data)
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:04:55 2020

@author: marco
"""

import myList
a = 5

my = myList.linkingList()
my.trace()
for i in range(a):
    my.append(i)
my.delete(3)
my.trace()
print("---")
print(my.quene())
print("---")
my.trace()
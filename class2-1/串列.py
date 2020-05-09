# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:04:55 2020

@author: marco
"""

import myList
my = myList.linkingList()
my.trace()
for i in range(10):
    my.append(i)
my.delete(5)
my.trace()

# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:40:51 2020

@author: marco
"""

import random
from functools import cmp_to_key

data = [1,5,2,15,3,36]

def myCmp(data1, data2):
    r = random.randrange(-1,2)
    return r

data.sort(key=cmp_to_key(myCmp))
print(data)
    
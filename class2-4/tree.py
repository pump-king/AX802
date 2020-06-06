# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:42:10 2020

@author: marco
"""

class node:
    def __init__(self,value):
        self.value = value
        self.child = []

root = node(100)

n = node(5)
root.child.append(n)
n = node(80)
root.child.append(n)

print(root.value)
print(root.child[0].value)
print(root.child[1].value)
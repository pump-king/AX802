# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:04:55 2020

@author: marco
"""

class node:
    def __init__(self,value):
        self.value = value
        self.next = None
"""
myNode = node(1)
myNode.next = node(2)
myNode.next.next = node(3)
myNode.next.next.next = node(4)
myNode.next.next.next.next = node(5)
"""
class linkingList:
    def __init__(self):
        self.head = node(0)
    def trace(self):
        run = self.head.next
        while run != None:
            print(run.value)
            run = run.next
    def append(self,value):
        run = self.head
        while run.next != None:
            run = run.next
        run.next = node(value)
        
        
my = linkingList()
my.trace()
for i in range(10):
    my.append(i)
my.trace()
    
"""
run = myNode
while run.next != None:
    print(run.value)
    run = run.next

print("-----")
run.next = node(6)

run = myNode
while run != None:
    print(run.value)
    run = run.next
"""
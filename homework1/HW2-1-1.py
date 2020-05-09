# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:00:37 2020

@author: marco
"""

class n:
    def __init__(self,v):
        self.v = v
        self.next = None

class l:
    def __init__(self):
        self.head = n(0)
    def t(self):
        r = self.head.next
        while r:
            print(r.v)
            r = r.next
    def a(self,v):
        r = self.head
        while r.next:
            r = r.next
        r.next = n(v)
        
m = l()
m.t()
for i in range(5):
    m.a(i)
m.t()
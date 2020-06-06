# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:56:09 2020

@author: marco
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if s == t:
            return True
        else:
            return False

s = "rat"
t = "car"

ans = Solution().isAnagram(s,t)
print(ans)
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:02:44 2020

@author: marco
"""

List = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
                
print(Solution().twoSum(List,target))
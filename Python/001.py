# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 20:57:17 2017

@author: Xt
"""
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsdict = {k:v for v,k in enumerate(nums)}
        for i in range(len(nums)-1):
            a = target-nums[i]
            if a in numsdict.keys():
                if numsdict[a]!=i:
                    return [i,numsdict[a]]
        return
                    









        
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:25:47 2017

@author: Xt
"""

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer. 
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        for i in range(n-2):
            c = a + b
            a = b
            b = c
        return c    
            
            
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:03:38 2017

@author: Xt
"""

'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 0
        b = x        
        while True:
            y = int((a+b)/2)
            if y**2 > x:
                b = y  
            elif (y+1)**2 <= x:
                a = y+1
            else:
                return y
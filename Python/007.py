# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:58:21 2017

@author: Xt
"""
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows. 
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minint = -2**31
        maxint = 2**31-1
        int2str = str(x)
        newstr = ''
        length = len(int2str)
        if int2str[0]=='-':
            newstr += '-'
            for i in range(0,length-1):
                newstr += int2str[length-i-1]
        else:
            for i in range(length):
                newstr += int2str[length-i-1]
         
        newint = int(newstr) 
        if minint <= newint <= maxint:
            return newint
        return 0

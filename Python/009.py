# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:29:24 2017

@author: Xt
"""
'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #return ((x>=0) and (str(x)[::-1]==str(x)))
        if x<0:
            return False
        a=0
        b=x
        for i in range(len(str(x))):
            a = a*10 + int((b%10))
            b = int(b - b%10)/10
        return a==x
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:49:18 2017

@author: Xt
"""
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        if h == 0 or h < n:
            return -1
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
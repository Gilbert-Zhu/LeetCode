# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:44:15 2017

@author: Xt
"""

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5. 
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        if len(s)==0:
            return 0
        length = len(s)
        for i in range(length):
            if s[length-i-1]==' ':
                return i
        return length
        
        
        
        
        
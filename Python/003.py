# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:01:58 2017

@author: Xt
"""

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        m = [1]
        n = [s[0]]
        for i in range(1,len(s)):
            if s[i] in n[i-1]:
                n.append(s[i])
                m.append(1)
            else:
                n.append(n[i-1]+s[i])
                m.append(m[i-1]+1)            
        return max(m)
    